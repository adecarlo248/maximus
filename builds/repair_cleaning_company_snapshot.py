#!/usr/bin/env python3
import json, subprocess, time
from datetime import datetime
from pathlib import Path

BASE='https://services.leadconnectorhq.com'
LOC='qxs3X4jCYse1W18z5H3k'
TOKEN='pit-3ecbb243-76a6-4d43-9d5e-825eb8ac4c0d'
LOG=Path('/home/maximus/.openclaw/workspace/builds/cleaning-company-snapshot-repair-log.md')

def curl(method,path,body=None,version='2021-07-28'):
    cmd=['curl','-sS','-w','\n%{http_code}','-X',method,BASE+path,'-H',f'Authorization: Bearer {TOKEN}','-H',f'Version: {version}','-H','Content-Type: application/json']
    if body is not None: cmd += ['-d', json.dumps(body)]
    out=subprocess.check_output(cmd,text=True); raw,code=out.rsplit('\n',1)
    try: data=json.loads(raw) if raw.strip() else {}
    except Exception: data={'raw':raw}
    return int(code),data

def get(path):
    cmd=['curl','-sS','-w','\n%{http_code}',BASE+path,'-H',f'Authorization: Bearer {TOKEN}','-H','Version: 2021-07-28']
    out=subprocess.check_output(cmd,text=True); raw,code=out.rsplit('\n',1)
    return int(code),json.loads(raw) if raw.strip() else {}

def existing():
    _,f=get(f'/locations/{LOC}/customFields')
    _,p=get(f'/opportunities/pipelines?locationId={LOC}')
    _,t=get(f'/locations/{LOC}/tags')
    return ({x.get('name') for x in f.get('customFields',[])}, {x.get('name') for x in p.get('pipelines',[])}, {x.get('name') for x in t.get('tags',[])})

FIELDS=[
 ('Lead Source','SINGLE_OPTIONS',["Google","Facebook","Instagram","Website","Referral","Walk-In","Phone Call","Repeat Customer","Property Manager","Realtor","Airbnb Host","Commercial Referral"]),
 ('Cleaning Type','SINGLE_OPTIONS',["Residential Standard","Residential Deep Clean","Move-In / Move-Out","Airbnb / Short-Term Rental Turnover","Commercial / Office","Post-Construction","Recurring Maintenance","One-Time Clean","Window / Add-On","Other"]),
 ('Service Frequency','SINGLE_OPTIONS',["One-Time","Weekly","Bi-Weekly","Monthly","As Needed","Turnover Schedule","Commercial Contract"]),
 ('Property Type','SINGLE_OPTIONS',["House","Apartment / Condo","Townhouse","Office","Retail","Salon / Spa","Daycare","Restaurant","Airbnb / STR","Post-Construction Site","Other Commercial"]),
 ('Pets On Site','RADIO',["Yes","No"]),
 ('Deposit Paid','RADIO',["Yes","No","Not Required"]),
 ('Review Requested','RADIO',["Yes","No"]),
 ('Review Received','RADIO',["Yes","No"]),
 ('Referral Requested','RADIO',["Yes","No"]),
 ('Recurring Client','RADIO',["Yes","No"]),
 ('Next Service Date','DATE',None),
 ('Airbnb Checkout Time','TEXT',None),
]
PIPELINES={
 'Cleaning - New Leads':["New Inquiry","Auto Reply Sent","Needs More Info","Quote Requested","Quote Sent","Follow-Up Active","Booked","Cold Lead","Lost / Not Now"],
 'Cleaning - Bookings':["Booked","Confirmed","Cleaner Assigned","In Progress","Completed","Invoice Sent","Paid","Review Requested"],
 'Cleaning - Recurring Clients':["Recurring Quote Requested","Recurring Proposal Sent","Active Weekly","Active Bi-Weekly","Active Monthly","At Risk","Paused","Cancelled"],
 'Cleaning - Airbnb Turnovers':["New Turnover Request","Timing Confirmed","Turnover Scheduled","Cleaner Assigned","Completed","Issue Reported","Recurring Turnover Offered","Recurring Turnover Active"],
 'Cleaning - Commercial Leads':["New Commercial Inquiry","Walkthrough Booked","Walkthrough Completed","Proposal Sent","Follow-Up Active","Contract Won","Active Account","Lost / Not Now"],
}
TAGS=['cleaning-booked','customer-active','cold-lead','recurring-client','needs-quote','quote-sent','invoice-sent','paid','service-complete']

results={'builtAt':datetime.now().isoformat(),'fields':[],'pipelines':[],'tags':[],'errors':[]}
fields,pipes,tags=existing()

for name,typ,options in FIELDS:
    if name in fields:
        results['fields'].append({'name':name,'status':'skipped-existing'}); continue
    body={'name':name,'dataType':typ}
    if options: body['options']=options
    code,res=curl('POST',f'/locations/{LOC}/customFields',body)
    rec={'name':name,'statusCode':code}
    if code in (200,201): rec['id']=(res.get('customField') or res).get('id')
    else: rec['error']=res; results['errors'].append({'field':name,'status':code,'response':res})
    results['fields'].append(rec); time.sleep(0.8)

fields,pipes,tags=existing()
for pname,stages in PIPELINES.items():
    if pname in pipes:
        results['pipelines'].append({'name':pname,'status':'skipped-existing'}); continue
    body={'name':pname,'locationId':LOC,'stages':[{'name':s,'position':i} for i,s in enumerate(stages)]}
    code,res=curl('POST','/opportunities/pipelines',body)
    rec={'name':pname,'statusCode':code}
    if code in (200,201): rec['id']=(res.get('pipeline') or res).get('id')
    else: rec['error']=res; results['errors'].append({'pipeline':pname,'status':code,'response':res})
    results['pipelines'].append(rec); time.sleep(1.0)

fields,pipes,tags=existing()
for tag in TAGS:
    if tag in tags:
        results['tags'].append({'name':tag,'status':'skipped-existing'}); continue
    code,res=curl('POST',f'/locations/{LOC}/tags',{'name':tag})
    rec={'name':tag,'statusCode':code}
    if code in (200,201): rec['id']=(res.get('tag') or res).get('id')
    else: rec['error']=res; results['errors'].append({'tag':tag,'status':code,'response':res})
    results['tags'].append(rec); time.sleep(1.0)

LOG.write_text('# Cleaning Company Snapshot Repair Log\n\n```json\n'+json.dumps(results,indent=2)+'\n```\n')
print(json.dumps({
 'fieldsCreated':len([x for x in results['fields'] if x.get('statusCode') in (200,201)]),
 'pipelinesCreated':len([x for x in results['pipelines'] if x.get('statusCode') in (200,201)]),
 'tagsCreated':len([x for x in results['tags'] if x.get('statusCode') in (200,201)]),
 'errors':len(results['errors']),
 'log':str(LOG)
},indent=2))

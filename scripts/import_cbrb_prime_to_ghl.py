#!/usr/bin/env python3
import csv, json, subprocess, time, sys
from pathlib import Path

CSV_PATH=Path('leads/cbrb/1app_cbrb_prime_targets_import.csv')
LOG_PATH=Path('leads/cbrb/1app_cbrb_prime_import_log.jsonl')
ERR_PATH=Path('leads/cbrb/1app_cbrb_prime_import_errors.csv')
SERVER='gohighlevel-1app'
OP='upsert-contact'

# Resume support: skip phones already logged success.
done=set()
if LOG_PATH.exists():
    for line in LOG_PATH.read_text(encoding='utf-8', errors='ignore').splitlines():
        try:
            rec=json.loads(line)
            if rec.get('ok') and rec.get('phone'):
                done.add(rec['phone'])
        except Exception:
            pass

rows=list(csv.DictReader(CSV_PATH.open(encoding='utf-8')))
errors=[]
count=0
skipped=0
for i,r in enumerate(rows,1):
    phone=(r.get('Phone') or '').strip()
    biz=(r.get('Business Name') or '').strip()
    if not phone or not biz:
        continue
    if phone in done:
        skipped+=1
        continue
    tags=['CBRB','1app target','prime target']
    cat=(r.get('Category') or '').strip()
    if cat: tags.append(cat)
    body={
        'name': biz,
        'companyName': biz,
        'phone': phone,
        'tags': tags,
        'source': 'CBRB directory - 1app prime target import 2026-07-10',
        'locationId': 'SfJSWQP1qvxdFNAzdsxz',
        'country': 'CA',
        'createNewIfDuplicateAllowed': False,
    }
    website=(r.get('Website') or '').strip()
    if website: body['website']=website
    args={'operationId': OP, 'idempotencyKey': '1app-cbrb-prime-'+''.join(ch for ch in phone if ch.isdigit()), 'params': {'body': body}}
    cmd=['mcporter','call',f'{SERVER}.execute_operation','--args',json.dumps(args),'--output','json']
    started=time.time()
    try:
        p=subprocess.run(cmd, text=True, capture_output=True, timeout=45)
        ok=p.returncode==0
        data=None
        try:
            data=json.loads(p.stdout) if p.stdout.strip() else None
            if isinstance(data,dict) and data.get('success') is not True:
                ok=False
        except Exception:
            pass
        rec={'i':i,'business':biz,'phone':phone,'ok':ok,'returncode':p.returncode,'seconds':round(time.time()-started,2),'response':data,'stderr':p.stderr[-1000:]}
        with LOG_PATH.open('a',encoding='utf-8') as f: f.write(json.dumps(rec,ensure_ascii=False)+'\n')
        if ok:
            count+=1
        else:
            errors.append({**r,'error':(p.stderr or p.stdout)[-1000:]})
        if (count+len(errors))%25==0:
            print(f'processed={count+len(errors)} success={count} errors={len(errors)} skipped={skipped}', flush=True)
        time.sleep(0.12)
    except Exception as e:
        errors.append({**r,'error':repr(e)})
        with LOG_PATH.open('a',encoding='utf-8') as f: f.write(json.dumps({'i':i,'business':biz,'phone':phone,'ok':False,'exception':repr(e)},ensure_ascii=False)+'\n')

if errors:
    fields=list(rows[0].keys())+['error']
    with ERR_PATH.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(errors)
print(json.dumps({'total_rows':len(rows),'success_new_this_run':count,'skipped_already_done':skipped,'errors':len(errors),'log':str(LOG_PATH),'errors_csv':str(ERR_PATH) if errors else None},indent=2))

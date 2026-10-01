#!/usr/bin/env python3
import csv, html, json, re, time, urllib.parse
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

BASE='https://www.thecbrb.ca'
OUTDIR=Path('leads/cbrb')
OUTDIR.mkdir(parents=True, exist_ok=True)
UA='Mozilla/5.0 (compatible; MaximusLeadResearch/1.0; +https://use1app.com)'
PHONE_RE=re.compile(r'(?:\+?1[\s\-.]?)?(?:\(?\d{3}\)?[\s\-.]?\d{3}[\s\-.]?\d{4})')

SERVICE_INCLUDE = re.compile(r'''(?ix)
(service|services|contractor|contractors|builder|builders|realtor|accountant|clinic|repair|rental|agency|agencies|consultant|consultants|delivery|electrician|excavation|planner|logistics|funeral|instructor|gym|hvac|inspector|employment|landscaper|lawyer|legal|locksmith|broker|moving|junk|painting|plumbing|photographer|videographer|physio|printing|investigator|property management|roofing|security|software|storage|telecommunications|towing|travel|tutoring|web design|marketing|windows|doors|auto body|detailing|cleaning|pest|architectural|coaching|mortgage|insurance|home improvement|interior designer|immigration|fingerprinting|freight)
''')
SERVICE_EXCLUDE = re.compile(r'''(?ix)
(restaurants?|schools?|stores?|bakeries|butcher|breweries|wineries|candy|candle|cannabis|clothing|gift|grocery|liquor|pawn|pharmacies|shopping malls|toy|vape|movie theaters|museums|libraries|tourist|charities|non-profit|religious|retirement homes|student housing|campgrounds|cemeteries|galleries|escape rooms|indoor playgrounds|sports clubs|golf courses|gun shops|flea markets|tattoo|jewelry|mattress|appliance stores|book stores|fireplace stores|garden centers)
''')

def fetch(url):
    req=Request(url, headers={'User-Agent': UA})
    with urlopen(req, timeout=30) as r:
        return r.read().decode('utf-8', errors='replace')

def strip_tags(s):
    s=re.sub(r'<script\b.*?</script>', ' ', s, flags=re.I|re.S)
    s=re.sub(r'<style\b.*?</style>', ' ', s, flags=re.I|re.S)
    s=re.sub(r'<[^>]+>', ' ', s, flags=re.S)
    s=html.unescape(s).replace('\xa0',' ')
    return ' '.join(s.split())

def clean_phone(p):
    p=p.strip().replace('\xa0',' ')
    digits=re.sub(r'\D','',p)
    if len(digits)==11 and digits.startswith('1'):
        digits=digits[1:]
    if len(digits)==10:
        return f'+1{digits}'
    return p

def parse_directory_categories(text):
    links=[]; seen=set()
    for m in re.finditer(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', text, flags=re.I|re.S):
        href=html.unescape(m.group(1)); label=strip_tags(m.group(2))
        if href.startswith('/directory/') and href != '/directory' and href not in seen and label:
            seen.add(href); links.append({'category': label, 'path': href, 'url': urllib.parse.urljoin(BASE, href)})
    return links

def target_category(label):
    return bool(SERVICE_INCLUDE.search(label)) and not bool(SERVICE_EXCLUDE.search(label))

def parse_category(cat, text):
    path=urllib.parse.urlparse(cat['url']).path.rstrip('/')
    patt=rf'<a\b[^>]*href=["\']({re.escape(path)}/[^"\']+)["\'][^>]*>(.*?)</a>'
    matches=list(re.finditer(patt, text, flags=re.I|re.S))
    rows=[]
    for i,m in enumerate(matches):
        name=strip_tags(m.group(2))
        if not name or name.lower() in {'directory','home','selection','benefits','apply','about us'}:
            continue
        detail_url=urllib.parse.urljoin(BASE, html.unescape(m.group(1)))
        seg=text[m.end(): matches[i+1].start() if i+1 < len(matches) else min(len(text), m.end()+3000)]
        clean=strip_tags(seg)
        # Segment normally: "- Industry City, Province - Phone"
        phone_match=PHONE_RE.search(clean)
        phone=''
        before_phone=clean
        if phone_match:
            phone=clean_phone(phone_match.group(0))
            before_phone=clean[:phone_match.start()].strip(' -')
        industry=''
        location=''
        if before_phone.startswith('-'):
            before_phone=before_phone[1:].strip()
        # Split on last likely location delimiter. Use province names as anchors.
        provinces='Alberta|British Columbia|Manitoba|New Brunswick|Newfoundland and Labrador|Nova Scotia|Ontario|Prince Edward Island|Quebec|Québec|Saskatchewan|Northwest Territories|Nunavut|Yukon'
        pm=list(re.finditer(rf'([A-Za-z .\'’\-&/]+,\s*(?:{provinces}))', before_phone))
        if pm:
            last=pm[-1]
            location=last.group(1).strip(' -')
            industry=before_phone[:last.start()].strip(' -')
        else:
            # Fallback: first phrase after dash is industry, rest unknown
            industry=before_phone.strip(' -')
        # Capture first external website link in this listing segment, excluding Google search.
        website=''
        for am in re.finditer(r'<a\b[^>]*href=["\']([^"\']+)["\']', seg, flags=re.I|re.S):
            href=html.unescape(am.group(1))
            if href.startswith('http') and 'google.' not in href and 'thecbrb.ca' not in href:
                website=href; break
        if phone or detail_url:
            rows.append({
                'business_name': name,
                'phone': phone,
                'category': cat['category'],
                'industry_description': industry,
                'location': location,
                'website': website,
                'source_url': detail_url,
                'source_category_url': cat['url'],
                'target_for_1app': 'yes' if target_category(cat['category']) else 'no',
                'notes': 'CBRB directory public listing'
            })
    return rows

def dedupe(rows):
    out=[]; seen=set()
    for r in rows:
        key=(re.sub(r'\W+','',r['business_name'].lower()), r['phone'])
        if key in seen: continue
        seen.add(key); out.append(r)
    return out

def main():
    index=fetch(BASE+'/directory')
    cats=parse_directory_categories(index)
    allrows=[]; errors=[]
    for idx,cat in enumerate(cats,1):
        try:
            text=fetch(cat['url'])
            rows=parse_category(cat,text)
            allrows.extend(rows)
            print(f'{idx:3}/{len(cats)} {cat["category"]}: {len(rows)}')
            time.sleep(0.25)
        except Exception as e:
            errors.append({'category': cat, 'error': repr(e)})
            print(f'ERR {cat["category"]}: {e}')
            time.sleep(1)
    allrows=dedupe(allrows)
    targets=[r for r in allrows if r['target_for_1app']=='yes' and r['phone']]
    fields=['business_name','phone','category','industry_description','location','website','source_url','source_category_url','target_for_1app','notes']
    for filename,rows in [('cbrb_all_businesses.csv',allrows),('cbrb_1app_service_targets.csv',targets)]:
        with (OUTDIR/filename).open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
    (OUTDIR/'categories.json').write_text(json.dumps(cats,indent=2),encoding='utf-8')
    (OUTDIR/'errors.json').write_text(json.dumps(errors,indent=2),encoding='utf-8')
    print('\nDONE')
    print('categories',len(cats),'all_rows',len(allrows),'targets',len(targets),'errors',len(errors))
    print('files:', OUTDIR/'cbrb_all_businesses.csv', OUTDIR/'cbrb_1app_service_targets.csv')
if __name__=='__main__': main()

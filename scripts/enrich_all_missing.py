"""
Enrich all expired/no-sponsor agents that are missing phone numbers.
Loads all fsra_expired_*.csv files, checks against latest enriched master,
enriches only the missing ones, then merges into a new master CSV.

Usage: python3 enrich_all_missing.py
"""

import csv, glob, os, re, time
from datetime import datetime
from collections import defaultdict
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

def load_all_expired():
    agents = []
    csv_files = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "fsra_expired_*.csv")))
    for f in csv_files:
        city_slug = os.path.basename(f).replace("fsra_expired_","").split("_2026")[0]
        city = city_slug.replace("_"," ").title()
        with open(f, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("Name","").strip():
                    row["Source City"] = city
                    agents.append(row)
    print(f"[+] Loaded {len(agents)} expired agents from {len(csv_files)} cities")
    return agents

def load_enriched():
    files = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "enriched_contacts_*.csv")))
    if not files:
        return {}
    enriched = {}
    with open(files[-1], newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = (row.get("Name","").strip(), row.get("Source City","").strip())
            enriched[key] = row
    print(f"[+] Loaded {len(enriched)} already-enriched agents from {os.path.basename(files[-1])}")
    return enriched

def clean_name(raw):
    nick_match = re.search(r'\(([^)]+)\)', raw)
    nick = nick_match.group(1).title() if nick_match else None
    name = re.sub(r'\([^)]+\)', '', raw).strip()
    if ',' in name:
        last, first = name.split(',', 1)
        first_name = f"{first.strip().title()} {last.strip().title()}"
        nick_name  = f"{nick} {last.strip().title()}" if nick else None
        return first_name, nick_name
    return name.title(), None

def extract_phones(text):
    phones = re.findall(r'(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    seen, out = set(), []
    for p in phones:
        d = re.sub(r'\D','',p)
        if len(d) in (10,11) and d not in seen:
            seen.add(d)
            out.append(f"({d[-10:-7]}) {d[-7:-4]}-{d[-4:]}")
    return out[:2]

def extract_emails(text):
    emails = re.findall(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}', text)
    junk = ['google','schema','example','w3.org','sentry','pixel','track']
    return list(dict.fromkeys(
        e for e in emails if not any(j in e.lower() for j in junk)
    ))[:2]

def extract_linkedin(text):
    m = re.search(r'linkedin\.com/in/([a-zA-Z0-9\-_%]+)', text)
    return f"https://www.linkedin.com/in/{m.group(1)}" if m else ""

def search_canada411(page, name, city):
    try:
        url = f"https://411.ca/search/person?name={name.replace(' ','+')}&where={city.replace(' ','+')}+ON"
        page.goto(url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(1.5)
        text = page.inner_text("body")
        phones = extract_phones(text)
        if not phones:
            url2 = f"https://www.canada411.ca/search/si/1/{name.replace(' ','+')}/{city.replace(' ','+')}+ON/"
            page.goto(url2, wait_until="domcontentloaded", timeout=15000)
            time.sleep(1.5)
            text = page.inner_text("body")
            phones = extract_phones(text)
        addr_match = re.search(r'\d+\s+\w+.*?(?:ON|Ontario).*?(?:\n|$)', text)
        addr = addr_match.group(0).strip()[:80] if addr_match else ""
        return phones, addr
    except Exception:
        return [], ""

def search_bing(page, name, city):
    try:
        query = f'"{name}" {city} Ontario phone insurance'
        url = f"https://www.bing.com/search?q={query.replace(' ','+')}"
        page.goto(url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(1)
        text = page.inner_text("body")
        phones = extract_phones(text)
        linkedin = extract_linkedin(text)
        return phones, linkedin
    except Exception:
        return [], ""

def enrich_agent(page, agent):
    raw_name = agent.get("Name","")
    city = (agent.get("City","") or agent.get("Source City","")).split(",")[0].strip()
    primary, alt = clean_name(raw_name)
    names = [primary] + ([alt] if alt else [])

    phones, emails, linkedin, address = [], [], "", ""

    for name in names:
        p, addr = search_canada411(page, name, city)
        phones += p
        if addr: address = addr
        if not phones:
            bp, bl = search_bing(page, name, city)
            phones += bp
            if bl: linkedin = bl
        if phones or linkedin:
            break

    phones = list(dict.fromkeys(phones))[:2]
    found = "YES" if phones or linkedin else "NO"
    return {
        "Search Name":      primary,
        "Phone 1":          phones[0] if phones else "",
        "Phone 2":          phones[1] if len(phones) > 1 else "",
        "Email 1":          emails[0] if emails else "",
        "Email 2":          "",
        "LinkedIn":         linkedin,
        "Facebook":         "",
        "Address":          address,
        "Found":            found,
    }

FIELDS = ["Name","Search Name","City","Source City","Status","Expiry Date",
          "Termination Date","Licence Class","Licence #",
          "Phone 1","Phone 2","Email 1","Email 2","LinkedIn","Facebook","Address","Found"]

def main():
    all_expired = load_all_expired()
    enriched    = load_enriched()

    # Find missing
    missing = []
    for a in all_expired:
        key = (a.get("Name","").strip(), a.get("Source City","").strip())
        existing = enriched.get(key)
        if not existing or not existing.get("Phone 1","").strip():
            missing.append(a)

    print(f"[+] {len(missing)} agents need enrichment\n")

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    checkpoint_file = os.path.join(SCRIPTS_DIR, f"enriched_new_batch_{ts}.csv")
    found_count = 0
    new_results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox","--disable-dev-shm-usage"])
        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            viewport={"width":1280,"height":900}
        )
        page = ctx.new_page()

        for i, agent in enumerate(missing):
            name = agent.get("Name","")
            city = agent.get("Source City","")
            print(f"  [{i+1}/{len(missing)}] {name[:40]:<40} ({city})", end=" ", flush=True)

            e = enrich_agent(page, agent)
            parts = []
            if e["Phone 1"]:  parts.append(f"📞 {e['Phone 1']}")
            if e["LinkedIn"]: parts.append("💼 LinkedIn")
            print(" | ".join(parts) if parts else "(not found)", flush=True)

            if e["Found"] == "YES":
                found_count += 1

            new_results.append({
                "Name":             name,
                "Search Name":      e["Search Name"],
                "City":             agent.get("City",""),
                "Source City":      city,
                "Status":           agent.get("Status",""),
                "Expiry Date":      agent.get("Expiry Date",""),
                "Termination Date": agent.get("Termination Date",""),
                "Licence Class":    agent.get("Licence Class",""),
                "Licence #":        agent.get("Licence #",""),
                "Phone 1":          e["Phone 1"],
                "Phone 2":          e["Phone 2"],
                "Email 1":          e["Email 1"],
                "Email 2":          e["Email 2"],
                "LinkedIn":         e["LinkedIn"],
                "Facebook":         e["Facebook"],
                "Address":          e["Address"],
                "Found":            e["Found"],
            })

            # Checkpoint every 100 agents
            if (i + 1) % 100 == 0:
                with open(checkpoint_file, "w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=FIELDS)
                    w.writeheader()
                    w.writerows(new_results)
                print(f"\n  [CHECKPOINT] {i+1}/{len(missing)} done, {found_count} found so far\n")

        browser.close()

    # Final save of new batch
    with open(checkpoint_file, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(new_results)

    # Merge with existing enriched
    existing_rows = list(enriched.values())
    all_rows = existing_rows + new_results

    master_out = os.path.join(SCRIPTS_DIR, f"enriched_contacts_{ts}.csv")
    with open(master_out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(all_rows)

    total_with_phones = sum(1 for r in all_rows if r.get("Phone 1","").strip())

    print(f"\n{'='*65}")
    print(f"ENRICHMENT COMPLETE")
    print(f"New agents enriched:  {len(new_results)}")
    print(f"New phones found:     {found_count} ({round(found_count/len(new_results)*100)}% hit rate)")
    print(f"Master list total:    {len(all_rows)} agents")
    print(f"Total with phones:    {total_with_phones}")
    print(f"Master CSV:           {master_out}")
    print(f"{'='*65}")

if __name__ == "__main__":
    main()

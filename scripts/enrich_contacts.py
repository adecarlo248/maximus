"""
FSRA Agent Contact Enricher v2
Uses Canada411, YellowPages Canada, and LinkedIn search.
Much more reliable than Google for Canadian contacts.

Usage:
    python3 enrich_contacts.py
"""

import csv
import time
import os
import re
import glob
from datetime import datetime
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPTS_DIR, f"enriched_contacts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

def load_all_agents():
    agents = []
    csv_files = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "fsra_expired_*.csv")))
    for f in csv_files:
        city_slug = os.path.basename(f).replace("fsra_expired_","").split("_2026")[0]
        city = city_slug.replace("_"," ").title()
        with open(f, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                row["Source City"] = city
                agents.append(row)
    print(f"[+] Loaded {len(agents)} agents from {len(csv_files)} cities")
    return agents

def clean_name(raw):
    """'LAST, FIRST (NICK)' -> ('First Last', 'Nick Last')"""
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

def search_canada411(page, first_last, city):
    """Search 411.ca for phone number."""
    try:
        city_clean = city.split(",")[0].strip()
        # Try 411.ca as primary (different rate limits than Canada411)
        name_parts = first_last.strip().split()
        first = name_parts[0] if name_parts else ""
        last  = name_parts[-1] if len(name_parts) > 1 else ""
        url = f"https://411.ca/search/person?name={first_last.replace(' ','+')}&where={city_clean.replace(' ','+')}+ON"
        page.goto(url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(1.5)
        text = page.inner_text("body")
        phones = extract_phones(text)
        addr_match = re.search(r'\d+\s+\w+.*?(?:ON|Ontario).*?(?:\n|$)', text)
        addr = addr_match.group(0).strip()[:80] if addr_match else ""
        if not phones:
            # Fallback to Canada411
            url2 = f"https://www.canada411.ca/search/si/1/{first_last.replace(' ','+')}/{city_clean.replace(' ','+')}+ON/"
            page.goto(url2, wait_until="domcontentloaded", timeout=15000)
            time.sleep(1.5)
            text2 = page.inner_text("body")
            phones = extract_phones(text2)
            if not addr:
                addr_match2 = re.search(r'\d+\s+\w+.*?(?:ON|Ontario).*?(?:\n|$)', text2)
                addr = addr_match2.group(0).strip()[:80] if addr_match2 else ""
        return phones, addr
    except Exception:
        return [], ""

def search_yellowpages(page, first_last, city):
    """Search YellowPages Canada."""
    try:
        city_clean = city.split(",")[0].strip().replace(" ", "+")
        name_clean = first_last.replace(" ", "+")
        url = f"https://www.yellowpages.ca/search/si/1/{name_clean}/{city_clean}+ON"
        page.goto(url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(1)
        text = page.inner_text("body")
        phones = extract_phones(text)
        emails = extract_emails(text)
        return phones, emails
    except Exception:
        return [], []

def search_linkedin(page, first_last, city):
    """Search LinkedIn via Google (avoids login wall)."""
    try:
        query = f'site:linkedin.com/in "{first_last}" Ontario insurance'
        url = f"https://www.bing.com/search?q={query.replace(' ','+')}"
        page.goto(url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(1)
        text = page.inner_text("body")
        return extract_linkedin(text)
    except Exception:
        return ""

def search_facebook(page, first_last, city):
    """Search Facebook via Bing."""
    try:
        city_clean = city.split(",")[0].strip()
        query = f'site:facebook.com "{first_last}" "{city_clean}" insurance'
        url = f"https://www.bing.com/search?q={query.replace(' ','+')}"
        page.goto(url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(1)
        text = page.inner_text("body")
        fb = re.search(r'facebook\.com/[a-zA-Z0-9.]+', text)
        return f"https://www.{fb.group(0)}" if fb else ""
    except Exception:
        return ""

def enrich(page, agent):
    raw_name = agent.get("Name") or ""
    city     = agent.get("City") or agent.get("Source City") or ""
    city_clean = city.split(",")[0].strip() if city else ""

    primary, alt = clean_name(raw_name)
    names_to_try = [primary] + ([alt] if alt else [])

    phones, emails, linkedin, facebook, address = [], [], "", "", ""

    for name in names_to_try:
        # Canada411
        p, addr = search_canada411(page, name, city_clean)
        phones  += p
        if addr: address = addr

        # YellowPages
        yp_phones, yp_emails = search_yellowpages(page, name, city_clean)
        phones += yp_phones
        emails += yp_emails

        # LinkedIn (via Bing)
        if not linkedin:
            linkedin = search_linkedin(page, name, city_clean)

        # Facebook (via Bing)
        if not facebook:
            facebook = search_facebook(page, name, city_clean)

        # Stop if we found something good
        if phones or emails or linkedin:
            break

    # Deduplicate
    phones = list(dict.fromkeys(phones))[:2]
    emails = list(dict.fromkeys(emails))[:2]

    found = "YES" if (phones or emails or linkedin or facebook) else "NO"
    return {
        "Search Name": primary,
        "Phone 1":     phones[0] if phones else "",
        "Phone 2":     phones[1] if len(phones)>1 else "",
        "Email 1":     emails[0] if emails else "",
        "Email 2":     emails[1] if len(emails)>1 else "",
        "LinkedIn":    linkedin,
        "Facebook":    facebook,
        "Address":     address,
        "Found":       found,
    }

def run():
    agents = load_all_agents()
    if not agents:
        print("[!] No CSVs found in scripts folder.")
        return

    results = []
    found_count = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox","--disable-dev-shm-usage"])
        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            viewport={"width":1280,"height":900}
        )
        page = ctx.new_page()

        print(f"\n[+] Enriching {len(agents)} agents via Canada411 + YellowPages + LinkedIn\n")

        for i, agent in enumerate(agents):
            name   = agent.get("Name") or ""
            city   = agent.get("Source City") or ""
            status = agent.get("Status") or ""

            if not name.strip():
                continue

            print(f"  [{i+1}/{len(agents)}] {name[:38]:<38} ({city})", end=" ", flush=True)

            e = enrich(page, agent)

            parts = []
            if e["Phone 1"]:   parts.append(f"📞 {e['Phone 1']}")
            if e["Email 1"]:   parts.append(f"✉ {e['Email 1']}")
            if e["LinkedIn"]:  parts.append("💼 LinkedIn")
            if e["Facebook"]:  parts.append("👤 Facebook")
            print(" | ".join(parts) if parts else "(not found)", flush=True)

            if e["Found"] == "YES":
                found_count += 1

            results.append({
                "Name":             name,
                "Search Name":      e["Search Name"],
                "City":             agent.get("City",""),
                "Source City":      city,
                "Status":           status,
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

        browser.close()

    fields = ["Name","Search Name","City","Source City","Status","Expiry Date",
              "Termination Date","Licence Class","Licence #",
              "Phone 1","Phone 2","Email 1","Email 2","LinkedIn","Facebook","Address","Found"]

    with open(OUTPUT_FILE,"w",newline="",encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields).writeheader()
        csv.DictWriter(f, fieldnames=fields).writerows(results)

    print(f"\n{'='*60}")
    print(f"DONE: {found_count}/{len(results)} agents with contact info found")
    print(f"      {OUTPUT_FILE}")
    print(f"{'='*60}")

if __name__ == "__main__":
    run()

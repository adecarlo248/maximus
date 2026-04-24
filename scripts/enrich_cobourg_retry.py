"""
Retry enrichment for Cobourg agents that came back with no phone.
Uses slower, more thorough searches.
"""

import csv, time, re, os, glob
from datetime import datetime
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

def extract_phones(text):
    phones = re.findall(r'(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    seen, out = set(), []
    for p in phones:
        d = re.sub(r'\D','',p)
        if len(d) in (10,11) and d not in seen:
            seen.add(d)
            out.append(f"({d[-10:-7]}) {d[-7:-4]}-{d[-4:]}")
    return out[:2]

def search(page, url):
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(2)
        return page.inner_text("body")
    except Exception:
        return ""

def find_phones(page, name, city):
    """Try multiple sources for a single person."""
    results = []

    # Try 1: 411.ca
    text = search(page, f"https://411.ca/search/person?name={name.replace(' ','+')}&where={city.replace(' ','+')}+ON")
    results += extract_phones(text)

    if not results:
        time.sleep(2)
        # Try 2: Canada411
        text = search(page, f"https://www.canada411.ca/search/si/1/{name.replace(' ','+')}/{city.replace(' ','+')}+ON/")
        results += extract_phones(text)

    if not results:
        time.sleep(2)
        # Try 3: Bing search with phone
        text = search(page, f"https://www.bing.com/search?q={name.replace(' ','+')}+{city.replace(' ','+')}+Ontario+phone")
        results += extract_phones(text)

    if not results:
        time.sleep(2)
        # Try 4: Just name + Ontario on Bing
        text = search(page, f"https://www.bing.com/search?q=%22{name.replace(' ','+')}%22+Ontario+insurance")
        results += extract_phones(text)

    return list(dict.fromkeys(results))[:2]

def run():
    # Load current enriched file
    enriched_file = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "enriched_contacts_*.csv")))[-1]
    print(f"[+] Loading: {enriched_file}")

    rows = []
    with open(enriched_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Find Cobourg agents with no phone
    cobourg_missing = [r for r in rows
                       if "cobourg" in r.get("Source City","").lower()
                       and not r.get("Phone 1","").strip()]

    print(f"[+] {len(cobourg_missing)} Cobourg agents with no phone found\n")

    if not cobourg_missing:
        print("[*] All Cobourg agents already have phones!")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox","--disable-dev-shm-usage"])
        page = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            viewport={"width":1280,"height":900}
        ).new_page()

        for agent in cobourg_missing:
            name = agent.get("Search Name") or agent.get("Name","")
            city = "Cobourg"
            print(f"  Retrying: {name[:45]:<45}", end=" ", flush=True)

            phones = find_phones(page, name, city)
            if phones:
                print(f"📞 {phones[0]}", flush=True)
                # Update in rows
                for r in rows:
                    if r.get("Name") == agent.get("Name") and "cobourg" in r.get("Source City","").lower():
                        r["Phone 1"] = phones[0]
                        r["Phone 2"] = phones[1] if len(phones) > 1 else ""
                        r["Found"]   = "YES"
            else:
                print("(still not found)", flush=True)

            time.sleep(3)

        browser.close()

    # Save updated CSV
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = os.path.join(SCRIPTS_DIR, f"enriched_contacts_{ts}.csv")
    fields = list(rows[0].keys())
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"\n[+] Saved updated CSV: {out}")

    # Rebuild PDFs
    import subprocess
    subprocess.run(["python3", os.path.join(SCRIPTS_DIR, "generate_cobourg_pdf.py")])
    subprocess.run(["python3", os.path.join(SCRIPTS_DIR, "generate_enriched_pdf.py")])

if __name__ == "__main__":
    run()

"""
Retry phone lookup for all agents with no phone number found.
Tries multiple sources with longer delays.
"""
import csv, time, re, os, glob, subprocess
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
    results = []
    for url in [
        f"https://411.ca/search/person?name={name.replace(' ','+')}&where={city.replace(' ','+')}+ON",
        f"https://www.canada411.ca/search/si/1/{name.replace(' ','+')}/{city.replace(' ','+')}+ON/",
        f"https://www.bing.com/search?q=%22{name.replace(' ','+')}%22+{city.replace(' ','+')}+Ontario+phone+number",
        f"https://www.bing.com/search?q=%22{name.replace(' ','+')}%22+Ontario+insurance+agent",
    ]:
        text = search(page, url)
        results += extract_phones(text)
        if results:
            break
        time.sleep(2)
    return list(dict.fromkeys(results))[:2]

def run():
    enriched_file = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "enriched_contacts_*.csv")))[-1]
    print(f"[+] Loading: {enriched_file}")

    rows = []
    with open(enriched_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    missing = [r for r in rows if not r.get("Phone 1","").strip()]
    print(f"[+] {len(missing)} agents with no phone — retrying...\n")

    if not missing:
        print("[*] All agents have phones!")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox","--disable-dev-shm-usage"])
        page = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            viewport={"width":1280,"height":900}
        ).new_page()

        found_count = 0
        for agent in missing:
            name = agent.get("Search Name") or agent.get("Name","")
            city = (agent.get("City","") or agent.get("Source City","")).split(",")[0].strip()
            print(f"  {name[:45]:<45} ({city})", end=" ", flush=True)

            phones = find_phones(page, name, city)
            if phones:
                print(f"📞 {phones[0]}", flush=True)
                found_count += 1
                for r in rows:
                    if r.get("Name") == agent.get("Name") and r.get("Source City") == agent.get("Source City"):
                        r["Phone 1"] = phones[0]
                        r["Phone 2"] = phones[1] if len(phones) > 1 else ""
                        r["Found"]   = "YES"
            else:
                print("(not found)", flush=True)
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

    total_found = sum(1 for r in rows if r.get("Phone 1","").strip())
    print(f"\n[+] Retry found {found_count} more numbers")
    print(f"[+] Total with phones: {total_found}/{len(rows)}")
    print(f"[+] Saved: {out}")

    # Rebuild all PDFs
    print("\n[+] Rebuilding PDFs...")
    for script in ["generate_cobourg_pdf.py", "generate_enriched_pdf.py"]:
        path = os.path.join(SCRIPTS_DIR, script)
        if os.path.exists(path):
            subprocess.run(["python3", path])

    # Build Port Hope PDF
    subprocess.run(["python3", os.path.join(SCRIPTS_DIR, "generate_port_hope_pdf.py")])

if __name__ == "__main__":
    run()

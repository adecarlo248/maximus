"""
FSRA Ontario - Expired Insurance Agent Scraper
Pass 1: collect all agent hrefs via pagination
Pass 2: visit each detail URL directly

Usage: python3 fsra_scraper.py --city Peterborough
"""

import argparse
import csv
import re
import time
import os
from datetime import datetime
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

BASE_URL  = "https://alias2a.fsco.gov.on.ca/"
CITY_ID   = "MainPlaceHolder_Content4_aliascity"
SEARCH_ID = "MainPlaceHolder_Content4_srButton"

EXPIRED_STATUSES = ["expired", "not authorized", "no sponsor",
                    "terminated", "lapsed", "suspended", "cancelled"]

def is_expired(status):
    return any(kw in status.lower() for kw in EXPIRED_STATUSES)

def parse_detail(body):
    detail = {"Status": "", "Licence Class": "", "Expiry Date": "", "Termination Date": ""}
    for field, pattern in [
        ("Licence Class",    r"Licence Class:\s*([^\n]+)"),
        ("Status",           r"Status:\s*([^\n]+)"),
        ("Expiry Date",      r"Expiry Date\s+([A-Za-z][^\n]+)"),
        ("Termination Date", r"Termination Date:\s*([^\n]+)"),
    ]:
        m = re.search(pattern, body, re.IGNORECASE)
        if m:
            detail[field] = m.group(1).strip()
    return detail

def wait_for_agents(page, timeout=15000):
    try:
        page.wait_for_function(
            "() => !!document.querySelector('a[href*=\"ShowAgent.aspx\"]')",
            timeout=timeout
        )
        time.sleep(0.3)
        return True
    except PlaywrightTimeout:
        return False

def get_agents_python(page):
    """Use Playwright locators (pure Python) — no JS string passed to evaluate."""
    agents = []
    links = page.locator('a[href*="ShowAgent.aspx"]')
    count = links.count()
    for i in range(count):
        try:
            link = links.nth(i)
            href = link.get_attribute("href") or ""
            licence_num = link.inner_text(timeout=500).strip()
            # Get parent row cells
            row = page.locator('a[href*="ShowAgent.aspx"]').nth(i).locator("xpath=ancestor::tr[1]")
            cells = row.locator("td")
            cell_count = cells.count()
            name = ""
            city = ""
            if cell_count >= 3:
                name = cells.nth(1).inner_text(timeout=500).strip()
                city = cells.nth(2).inner_text(timeout=500).strip()
            elif cell_count >= 1:
                raw = cells.nth(0).inner_text(timeout=500)
                parts = [p.strip() for line in raw.splitlines()
                         for p in line.split("\t") if p.strip()]
                name = parts[1] if len(parts) > 1 else ""
                city = parts[2] if len(parts) > 2 else ""
            agents.append({
                "licence_num": licence_num,
                "name": name,
                "city": city,
                "href": "https://alias2a.fsco.gov.on.ca/" + href if href.startswith("Show") else href
            })
        except Exception:
            continue
    return agents

def get_first_href(page):
    try:
        return page.locator('a[href*="ShowAgent.aspx"]').first.get_attribute("href", timeout=1000) or ""
    except Exception:
        return ""

def click_page_and_wait(page, num):
    before = get_first_href(page)
    clicked = False
    links = page.locator("a")
    count = links.count()
    for i in range(count):
        try:
            link = links.nth(i)
            if link.inner_text(timeout=300).strip() == str(num):
                link.click()
                clicked = True
                break
        except Exception:
            continue
    if not clicked:
        return False
    for _ in range(50):
        time.sleep(0.2)
        after = get_first_href(page)
        if after and after != before:
            time.sleep(0.3)
            return True
    return False

def run(city):
    all_agents = []
    expired    = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            viewport={"width": 1280, "height": 900}
        )
        page = ctx.new_page()

        # Search
        print("[+] Loading FSRA and searching...")
        page.goto(BASE_URL, wait_until="networkidle", timeout=30000)
        page.fill("#" + CITY_ID, city)
        page.click("#" + SEARCH_ID)

        if not wait_for_agents(page):
            print("[!] No results.")
            browser.close()
            return []

        # Pass 1 - collect all hrefs
        print("[+] Pass 1: collecting all agent links\n")
        page_num = 1
        while True:
            agents = get_agents_python(page)
            all_agents.extend(agents)
            print(f"    Page {page_num}: {len(agents)} agents (total: {len(all_agents)})")
            if not click_page_and_wait(page, page_num + 1):
                print("    No more pages.\n")
                break
            page_num += 1

        print(f"[+] {len(all_agents)} agents collected total.\n")

        # Pass 2 - visit each detail directly
        print("[+] Pass 2: fetching licence details...\n")
        for i, agent in enumerate(all_agents):
            licence_num = agent["licence_num"]
            name        = agent["name"]
            city_val    = agent["city"]
            href        = agent["href"]

            print(f"  [{i+1}/{len(all_agents)}] {name[:44]:<44} ({licence_num})", end=" ", flush=True)

            try:
                page.goto(href, wait_until="domcontentloaded", timeout=15000)
                try:
                    page.wait_for_function(
                        "() => document.body.innerText.indexOf('Licence Class:') >= 0",
                        timeout=8000
                    )
                except PlaywrightTimeout:
                    print("(timeout)", flush=True)
                    continue

                body   = page.inner_text("body")
                detail = parse_detail(body)
                status = detail["Status"]
                expiry = detail["Expiry Date"]
                tag    = " <EXPIRED>" if is_expired(status) else ""
                print(f"| {status[:40]:<40} | {expiry}{tag}", flush=True)

                if is_expired(status):
                    expired.append({
                        "Licence #":        licence_num,
                        "Name":             name,
                        "City":             city_val,
                        "Licence Class":    detail["Licence Class"],
                        "Status":           status,
                        "Expiry Date":      expiry,
                        "Termination Date": detail["Termination Date"],
                    })

            except Exception as e:
                print(f"(error: {e})", flush=True)

        browser.close()

    return expired


def save(records, output_path):
    if not records:
        print("\n[!] No expired agents found.")
        return
    fields = ["Licence #", "Name", "City", "Licence Class",
              "Status", "Expiry Date", "Termination Date"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(records)
    print(f"\n{'='*60}")
    print(f"DONE: {len(records)} EXPIRED AGENTS SAVED")
    print(f"      {output_path}")
    print(f"{'='*60}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", default="Peterborough")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    city     = args.city
    ts       = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = args.output or f"fsra_expired_{city.lower().replace(' ','_')}_{ts}.csv"
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), out_file)

    print("=" * 60)
    print(f"  FSRA Expired Agent Scraper")
    print(f"  City:   {city}")
    print(f"  Output: {out_file}")
    print("=" * 60)

    records = run(city)
    save(records, out_path)

    if records:
        print(f"\nExpired agents ({len(records)} total):")
        print(f"  {'Name':<44} {'Status':<38} {'Expiry'}")
        print(f"  {'-'*44} {'-'*38} {'-'*15}")
        for r in records:
            print(f"  {r['Name']:<44} {r['Status']:<38} {r['Expiry Date']}")


if __name__ == "__main__":
    main()

"""
Ontario Province-Wide FSRA Scraper
Runs through all major Ontario cities/towns and collects expired agents.
Skips cities already scraped (checks for existing fsra_expired_<city>_*.csv).
Saves one CSV per city, prints running totals.

Usage: python3 scrape_ontario_all.py
"""

import os
import glob
import subprocess
import sys
from datetime import datetime

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

# ~150 Ontario cities/towns worth scraping (pop ~5k+)
ONTARIO_CITIES = [
    # Already done — will be auto-skipped
    "Peterborough", "Belleville", "Lindsay", "Trenton", "Brighton",
    "Cobourg", "Bowmanville", "Port Hope", "Oshawa", "Courtice",
    "Whitby", "Newcastle",

    # Greater Toronto Area
    "Toronto", "Mississauga", "Brampton", "Markham", "Vaughan",
    "Richmond Hill", "Oakville", "Burlington", "Ajax", "Pickering",
    "Milton", "Newmarket", "Aurora", "King City", "Stouffville",
    "Georgetown", "Maple", "Thornhill", "Woodbridge",

    # Hamilton / Niagara
    "Hamilton", "St. Catharines", "Niagara Falls", "Welland",
    "Grimsby", "Thorold", "Fort Erie", "Port Colborne", "Pelham",
    "Lincoln", "Smithville",

    # Halton / Wellington
    "Guelph", "Cambridge", "Kitchener", "Waterloo", "Stratford",
    "Fergus", "Elora", "Orangeville", "Shelburne",

    # Ottawa / East Ontario
    "Ottawa", "Kingston", "Cornwall", "Brockville", "Pembroke",
    "Carleton Place", "Smiths Falls", "Perth", "Kanata",
    "Orleans", "Nepean", "Gloucester", "Rockland", "Hawkesbury",
    "Prescott", "Gananoque", "Napanee",

    # Central Ontario / Cottage Country
    "Barrie", "Orillia", "Midland", "Collingwood", "Owen Sound",
    "Penetanguishene", "Wasaga Beach", "Innisfil", "Bradford",
    "Alliston", "Huntsville", "Gravenhurst", "Bracebridge",
    "Parry Sound", "Haliburton",

    # Simcoe County / York
    "Bradford West Gwillimbury", "East Gwillimbury", "Georgina",
    "Keswick", "Sutton",

    # Durham Region (beyond what we have)
    "Clarington", "Scugog", "Uxbridge", "Beaverton",

    # Kawartha / Northumberland (beyond what we have)
    "Campbellford", "Norwood", "Madoc", "Bancroft", "Havelock",

    # Southwestern Ontario
    "London", "Windsor", "Chatham", "Sarnia", "St. Thomas",
    "Woodstock", "Brantford", "Simcoe", "Tillsonburg", "Leamington",
    "Amherstburg", "LaSalle", "Tecumseh", "Essex", "Strathroy",
    "Ingersoll", "Aylmer", "Delhi", "Dunnville", "Caledonia",

    # Huron / Bruce
    "Goderich", "Clinton", "Exeter", "Wingham", "Kincardine",
    "Walkerton", "Hanover", "Durham", "Listowel", "Seaforth",

    # Northern Ontario
    "Sudbury", "Thunder Bay", "Sault Ste. Marie", "North Bay",
    "Timmins", "Kenora", "Elliot Lake", "Kapuskasing",
    "New Liskeard", "Temiskaming Shores", "Espanola", "Blind River",
]

def already_scraped(city):
    slug = city.lower().replace(" ", "_").replace(".", "").replace("'", "")
    pattern = os.path.join(SCRIPTS_DIR, f"fsra_expired_{slug}_*.csv")
    return len(glob.glob(pattern)) > 0

def count_records(city):
    slug = city.lower().replace(" ", "_").replace(".", "").replace("'", "")
    pattern = os.path.join(SCRIPTS_DIR, f"fsra_expired_{slug}_*.csv")
    files = glob.glob(pattern)
    if not files:
        return 0
    import csv
    count = 0
    with open(files[-1], newline="", encoding="utf-8") as f:
        count = sum(1 for _ in csv.DictReader(f))
    return count

def main():
    print("=" * 65)
    print("  Ontario Province-Wide FSRA Scraper")
    print(f"  Cities to process: {len(ONTARIO_CITIES)}")
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 65)

    total_expired = 0
    skipped = 0
    errors = []

    already_done = [c for c in ONTARIO_CITIES if already_scraped(c)]
    for city in already_done:
        count = count_records(city)
        total_expired += count
        skipped += 1

    print(f"\n[+] Skipping {skipped} already-scraped cities ({total_expired} expired agents already in hand)\n")

    to_scrape = [c for c in ONTARIO_CITIES if not already_scraped(c)]
    print(f"[+] Scraping {len(to_scrape)} new cities...\n")

    for i, city in enumerate(to_scrape):
        print(f"\n{'='*65}")
        print(f"  [{i+1}/{len(to_scrape)}] {city}")
        print(f"{'='*65}")

        result = subprocess.run(
            [sys.executable, os.path.join(SCRIPTS_DIR, "fsra_scraper.py"), "--city", city],
            capture_output=False,
            timeout=300
        )

        if result.returncode != 0:
            print(f"  [!] ERROR scraping {city}")
            errors.append(city)
            continue

        count = count_records(city)
        total_expired += count
        print(f"\n  >> {city}: {count} expired | Running total: {total_expired}")

    print(f"\n{'='*65}")
    print(f"  PROVINCE-WIDE SCRAPE COMPLETE")
    print(f"  Total expired agents: {total_expired}")
    print(f"  Cities scraped: {len(to_scrape)}")
    print(f"  Cities skipped (already done): {skipped}")
    if errors:
        print(f"  Errors: {', '.join(errors)}")
    print(f"  Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*65}")
    print(f"\nNext step: run enrich_contacts.py to get phone numbers for all new agents.")

if __name__ == "__main__":
    main()

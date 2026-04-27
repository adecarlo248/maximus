"""
Build No Sponsor filtered list from all fsra_expired_*.csv files.
Outputs:
  - no_sponsor_ontario.csv — all No Sponsor agents across Ontario
  - no_sponsor_ontario.pdf — clean call sheet PDF
"""

import csv, glob, os, re
from datetime import datetime
from collections import defaultdict
from weasyprint import HTML

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

def load_no_sponsor():
    from datetime import datetime
    # Load from enriched master CSV (has phone numbers)
    enriched_files = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "enriched_contacts_*.csv")))
    if not enriched_files:
        print("[!] No enriched CSV found — falling back to raw FSRA files")
        return [], defaultdict(int)
    latest = enriched_files[-1]
    print(f"[+] Loading from: {os.path.basename(latest)}")
    today = datetime.today()
    agents = []
    city_counts = defaultdict(int)
    skipped = 0
    with open(latest, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if "no sponsor" not in row.get("Status","").lower():
                continue
            if not row.get("Name","").strip():
                continue
            # Filter: only keep agents with active (non-expired) licence
            expiry_str = row.get("Expiry Date","").strip()
            try:
                expiry = datetime.strptime(expiry_str, "%B %d, %Y")
                if expiry < today:
                    skipped += 1
                    continue
            except:
                pass  # unknown date — keep it
            agents.append(row)
            city = row.get("Source City","").strip() or row.get("City","").strip()
            city_counts[city] += 1
    print(f"[+] Found {len(agents)} ACTIVE No Sponsor agents ({skipped} expired licences excluded)")
    return agents, city_counts

def save_csv(agents):
    out = os.path.join(SCRIPTS_DIR, "no_sponsor_ontario.csv")
    fields = ["Name", "City", "Source City", "Licence Class", "Status", "Expiry Date", "Termination Date", "Licence #"]
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(agents)
    print(f"[+] CSV saved: {out}")
    return out

def build_pdf(agents, city_counts):
    by_city = defaultdict(list)
    for a in agents:
        by_city[a["Source City"]].append(a)

    city_rows = ""
    for city in sorted(by_city.keys()):
        city_agents = by_city[city]
        rows = ""
        for a in city_agents:
            phone = a.get('Phone 1','')
            phone2 = a.get('Phone 2','')
            phones = phone
            if phone2 and phone2 != phone:
                phones += f" / {phone2}"
            rows += f"""<tr>
                <td>{a.get('Name','')}</td>
                <td>{phones or '<em style="color:#bbb">—</em>'}</td>
                <td>{a.get('Expiry Date','')}</td>
                <td>{a.get('Licence Class','')}</td>
            </tr>"""
        city_rows += f"""
        <div class="city-section">
          <h2>{city} <span class="city-count">{len(city_agents)} agents</span></h2>
          <table>
            <thead><tr><th>Name</th><th>Phone</th><th>Expiry</th><th>Licence Class</th></tr></thead>
            <tbody>{rows}</tbody>
          </table>
        </div>"""

    total = len(agents)
    num_cities = len(by_city)

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>Ontario No Sponsor Agents — Hot Lead List</title>
<style>
  @page {{ size: A4; margin: 1.5cm; }}
  body {{ font-family: Arial, sans-serif; font-size: 8.5pt; color: #222; line-height: 1.4; }}
  .header {{ background: #c8a000; color: white; padding: 16px 20px; margin-bottom: 16px; border-radius: 4px; }}
  .header h1 {{ margin: 0 0 4px 0; font-size: 16pt; }}
  .header p {{ margin: 0; font-size: 8.5pt; opacity: 0.9; }}
  .summary {{ display: table; width: 100%; border-collapse: collapse; margin-bottom: 16px; }}
  .summary-box {{ display: table-cell; background: #fffbe6; border: 1px solid #e6c800; padding: 10px 14px; text-align: center; }}
  .summary-box .num {{ font-size: 20pt; font-weight: bold; color: #8a6f00; display: block; }}
  .summary-box .lbl {{ font-size: 7.5pt; color: #666; }}
  .pitch-box {{ background: #fff3cc; border-left: 4px solid #c8a000; padding: 8px 12px; margin-bottom: 16px; font-size: 8pt; color: #5a4600; }}
  .pitch-box strong {{ color: #8a6f00; }}
  h2 {{ font-size: 11pt; color: #8a6f00; border-bottom: 2px solid #c8a000; padding-bottom: 3px; margin: 20px 0 8px 0; page-break-after: avoid; }}
  .city-count {{ font-size: 8pt; font-weight: normal; color: #999; margin-left: 8px; }}
  .city-section {{ page-break-inside: avoid; }}
  table {{ width: 100%; border-collapse: collapse; margin-bottom: 4px; }}
  th {{ background: #c8a000; color: white; padding: 5px 7px; text-align: left; font-size: 7.5pt; }}
  td {{ padding: 5px 7px; border-bottom: 1px solid #f0e8c0; vertical-align: top; }}
  tr:nth-child(even) td {{ background: #fffdf0; }}
  .footer {{ margin-top: 20px; font-size: 7.5pt; color: #999; text-align: center; border-top: 1px solid #ddd; padding-top: 8px; }}
</style></head><body>
<div class="header">
  <h1>🔥 Ontario No Sponsor Agents — Hot Lead List</h1>
  <p>Licensed. No Company. Ready to recruit. &nbsp;|&nbsp; Source: FSRA Ontario &nbsp;|&nbsp; {datetime.now().strftime('%B %d, %Y')}</p>
</div>
<div class="summary">
  <div class="summary-box"><span class="num">{total}</span><span class="lbl">No Sponsor Agents</span></div>
  <div class="summary-box"><span class="num">{num_cities}</span><span class="lbl">Cities Covered</span></div>
  <div class="summary-box"><span class="num">$0</span><span class="lbl">Cold Calling Required</span></div>
</div>
<div class="pitch-box">
  <strong>YOUR PITCH:</strong> "Hey [Name], I came across your licence on the FSRA registry — noticed you're currently without a sponsor.
  I'm with Primerica and we help licensed agents get active and earning fast. Would you be open to a quick 15-minute call this week?"
</div>
{city_rows}
<div class="footer">
  Built by Maximus &nbsp;|&nbsp; Tony DeCarlo — Primerica &nbsp;|&nbsp; FSRA Ontario Public Registry &nbsp;|&nbsp; {datetime.now().strftime('%B %d, %Y')}
</div>
</body></html>"""

    out = os.path.join(SCRIPTS_DIR, "no_sponsor_ontario.pdf")
    HTML(string=html).write_pdf(out)
    print(f"[+] PDF saved: {out}")
    return out

if __name__ == "__main__":
    agents, city_counts = load_no_sponsor()
    save_csv(agents)
    build_pdf(agents, city_counts)
    print(f"\nTop 10 cities by No Sponsor count:")
    for city, count in sorted(city_counts.items(), key=lambda x: -x[1])[:10]:
        print(f"  {city:<30} {count}")

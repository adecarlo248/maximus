"""
Generate individual city PDF from enriched master CSV.
Usage: python3 generate_city_pdf.py --city Courtice
"""
import argparse, csv, glob, os
from weasyprint import HTML
from collections import defaultdict

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

def status_tag(status):
    if "Expired" in status:
        return '<span class="tag tag-hot">EXPIRED</span>'
    return '<span class="tag tag-warm">NO SPONSOR</span>'

def generate(city_name):
    csv_file = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "enriched_contacts_*.csv")))[-1]
    agents = []
    with open(csv_file, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            src = row.get("Source City","").strip().lower()
            if src == city_name.lower() and row.get("Name","").strip():
                agents.append(row)

    if not agents:
        print(f"[!] No agents found for city: {city_name}")
        return

    rows_html = ""
    for a in agents:
        phone1   = a.get("Phone 1","")
        phone2   = a.get("Phone 2","")
        email1   = a.get("Email 1","")
        linkedin = a.get("LinkedIn","")
        status   = a.get("Status","")
        expiry   = a.get("Expiry Date","")
        tag      = status_tag(status)
        phones   = phone1
        if phone2 and phone2 != phone1:
            phones += f"<br><small>{phone2}</small>"
        contact = phones or "<em style='color:#999'>—</em>"
        if email1:
            contact += f"<br><small>✉ {email1}</small>"
        if linkedin:
            contact += f"<br><small>💼 LinkedIn</small>"
        rows_html += f"""<tr>
            <td>{a.get('Name','')}</td>
            <td>{tag}</td>
            <td>{expiry}</td>
            <td>{contact}</td>
        </tr>"""

    expired_count = sum(1 for a in agents if "Expired" in a.get("Status",""))
    sponsor_count = len(agents) - expired_count
    found_count   = sum(1 for a in agents if a.get("Phone 1","").strip())

    html_content = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>{city_name} — Insurance Agent Leads</title>
<style>
  @page {{ size: A4; margin: 1.5cm; }}
  body {{ font-family: Arial, sans-serif; font-size: 8.5pt; color: #222; line-height: 1.4; }}
  .header {{ background: #1a3a6b; color: white; padding: 16px 20px; margin-bottom: 16px; border-radius: 4px; }}
  .header h1 {{ margin: 0 0 4px 0; font-size: 16pt; }}
  .header p {{ margin: 0; font-size: 8.5pt; opacity: 0.85; }}
  .summary {{ display: table; width: 100%; border-collapse: collapse; margin-bottom: 16px; }}
  .summary-box {{ display: table-cell; background: #f0f4ff; border: 1px solid #c8d4f0; padding: 10px 14px; text-align: center; }}
  .summary-box .num {{ font-size: 20pt; font-weight: bold; color: #1a3a6b; display: block; }}
  .summary-box .lbl {{ font-size: 7.5pt; color: #555; }}
  .pitch-box {{ background: #fffbe6; border-left: 4px solid #f0a500; padding: 8px 12px; margin-bottom: 16px; font-size: 8pt; }}
  .pitch-box strong {{ color: #b37a00; }}
  table {{ width: 100%; border-collapse: collapse; margin-bottom: 4px; }}
  th {{ background: #1a3a6b; color: white; padding: 5px 7px; text-align: left; font-size: 7.5pt; }}
  td {{ padding: 5px 7px; border-bottom: 1px solid #e8e8e8; vertical-align: top; }}
  tr:nth-child(even) td {{ background: #f7f9ff; }}
  .tag {{ display: inline-block; font-size: 7pt; padding: 1px 6px; border-radius: 8px; font-weight: bold; white-space: nowrap; }}
  .tag-hot {{ background: #ffe0e0; color: #c00; }}
  .tag-warm {{ background: #fff3cc; color: #996600; }}
  .footer {{ margin-top: 20px; font-size: 7.5pt; color: #999; text-align: center; border-top: 1px solid #ddd; padding-top: 8px; }}
</style></head><body>
<div class="header">
  <h1>{city_name} — Insurance Agent Lead List</h1>
  <p>Expired &amp; Lapsed Agents &nbsp;|&nbsp; Source: FSRA Ontario &nbsp;|&nbsp; April 2026</p>
</div>
<div class="summary">
  <div class="summary-box"><span class="num">{len(agents)}</span><span class="lbl">Total Agents</span></div>
  <div class="summary-box"><span class="num">{expired_count}</span><span class="lbl">Fully Expired</span></div>
  <div class="summary-box"><span class="num">{sponsor_count}</span><span class="lbl">No Sponsor</span></div>
  <div class="summary-box"><span class="num">{found_count}</span><span class="lbl">With Phone Numbers</span></div>
</div>
<div class="pitch-box">
  <strong>EXPIRED:</strong> "Your licence expired but your experience didn't. Primerica gets you back active fast."
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>NO SPONSOR:</strong> "You're already licensed — you just need a sponsor. Let's talk."
</div>
<table>
  <thead><tr><th>Name</th><th>Status</th><th>Expiry</th><th>Contact Info</th></tr></thead>
  <tbody>{rows_html}</tbody>
</table>
<div class="footer">
  Built by Maximus &nbsp;|&nbsp; Tony DeCarlo — Primerica &nbsp;|&nbsp; FSRA Ontario Public Registry &nbsp;|&nbsp; April 2026
</div>
</body></html>"""

    slug = city_name.lower().replace(" ","_")
    out  = os.path.join(SCRIPTS_DIR, f"{slug}_expired_agents.pdf")
    HTML(string=html_content).write_pdf(out)
    print(f"PDF saved: {out}")
    print(f"{len(agents)} agents | {found_count} with phones")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", required=True)
    args = parser.parse_args()
    generate(args.city)

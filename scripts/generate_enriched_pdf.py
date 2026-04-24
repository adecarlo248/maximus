from weasyprint import HTML
import csv, os

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the enriched CSV
import glob
csv_file = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "enriched_contacts_*.csv")))[-1]
agents = []
with open(csv_file, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row.get("Name","").strip():
            agents.append(row)

# Group by city
from collections import defaultdict
by_city = defaultdict(list)
for a in agents:
    by_city[a.get("Source City","Unknown")].append(a)

def status_tag(status):
    if "Expired" in status:
        return '<span class="tag tag-hot">EXPIRED</span>'
    return '<span class="tag tag-warm">NO SPONSOR</span>'

def build_city_section(city, agents):
    rows = ""
    for a in agents:
        name    = a.get("Name","")
        phone1  = a.get("Phone 1","")
        phone2  = a.get("Phone 2","")
        email1  = a.get("Email 1","")
        linkedin = a.get("LinkedIn","")
        status  = a.get("Status","")
        expiry  = a.get("Expiry Date","")
        tag     = status_tag(status)

        phones = phone1
        if phone2 and phone2 != phone1:
            phones += f"<br><small>{phone2}</small>"

        contact = phones or "<em style='color:#999'>—</em>"
        if email1:
            contact += f"<br><small>✉ {email1}</small>"
        if linkedin:
            contact += f"<br><small>💼 LinkedIn</small>"

        rows += f"""<tr>
            <td>{name}</td>
            <td>{tag}</td>
            <td>{expiry}</td>
            <td>{contact}</td>
        </tr>"""

    expired_count = sum(1 for a in agents if "Expired" in a.get("Status",""))
    sponsor_count = len(agents) - expired_count

    return f"""
<div class="city-section">
  <h2>{city} <span class="city-count">{len(agents)} agents &nbsp;·&nbsp; {expired_count} expired &nbsp;·&nbsp; {sponsor_count} no sponsor</span></h2>
  <table>
    <thead>
      <tr><th>Name</th><th>Status</th><th>Expiry</th><th>Contact Info</th></tr>
    </thead>
    <tbody>{rows}</tbody>
  </table>
</div>"""

city_sections = ""
for city in sorted(by_city.keys()):
    city_sections += build_city_section(city, by_city[city])

total = len(agents)
found = sum(1 for a in agents if a.get("Phone 1","").strip())
expired_total = sum(1 for a in agents if "Expired" in a.get("Status",""))
sponsor_total = total - expired_total

html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Ontario Insurance Agent Lead List — April 2026</title>
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
  h2 {{ font-size: 11pt; color: #1a3a6b; border-bottom: 2px solid #1a3a6b; padding-bottom: 3px; margin: 20px 0 8px 0; page-break-after: avoid; }}
  .city-count {{ font-size: 8pt; font-weight: normal; color: #666; margin-left: 8px; }}
  .city-section {{ page-break-inside: avoid; }}
  table {{ width: 100%; border-collapse: collapse; margin-bottom: 4px; }}
  thead {{ page-break-after: avoid; }}
  tr {{ page-break-inside: avoid; }}
  th {{ background: #1a3a6b; color: white; padding: 5px 7px; text-align: left; font-size: 7.5pt; }}
  td {{ padding: 5px 7px; border-bottom: 1px solid #e8e8e8; vertical-align: top; }}
  tr:nth-child(even) td {{ background: #f7f9ff; }}
  .tag {{ display: inline-block; font-size: 7pt; padding: 1px 6px; border-radius: 8px; font-weight: bold; white-space: nowrap; }}
  .tag-hot {{ background: #ffe0e0; color: #c00; }}
  .tag-warm {{ background: #fff3cc; color: #996600; }}
  .footer {{ margin-top: 20px; font-size: 7.5pt; color: #999; text-align: center; border-top: 1px solid #ddd; padding-top: 8px; }}
</style>
</head>
<body>
<div class="header">
  <h1>Ontario Insurance Agent Lead List</h1>
  <p>Expired &amp; Lapsed Agents — Peterborough Region &nbsp;|&nbsp; Source: FSRA Ontario &nbsp;|&nbsp; April 24, 2026</p>
</div>

<div class="summary">
  <div class="summary-box"><span class="num">{total}</span><span class="lbl">Total Agents</span></div>
  <div class="summary-box"><span class="num">{expired_total}</span><span class="lbl">Fully Expired</span></div>
  <div class="summary-box"><span class="num">{sponsor_total}</span><span class="lbl">No Sponsor</span></div>
  <div class="summary-box"><span class="num">{found}</span><span class="lbl">Phone Numbers Found</span></div>
  <div class="summary-box"><span class="num">5</span><span class="lbl">Cities Covered</span></div>
</div>

<div class="pitch-box">
  <strong>EXPIRED:</strong> "Your licence expired but your experience didn't. Primerica gets you back active fast."
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>NO SPONSOR:</strong> "You're already licensed — you just need a sponsor. Let's talk."
</div>

{city_sections}

<div class="footer">
  Built by Maximus &nbsp;|&nbsp; Tony DeCarlo — Primerica &nbsp;|&nbsp; FSRA Ontario Public Registry &nbsp;|&nbsp; April 24, 2026
</div>
</body>
</html>"""

out = os.path.join(SCRIPTS_DIR, "ontario_agent_leads_with_contacts.pdf")
HTML(string=html_content).write_pdf(out)
print(f"PDF saved: {out}")
print(f"Total: {total} agents | {found} with phone numbers")

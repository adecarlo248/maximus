from weasyprint import HTML
import csv, os, glob

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

# Load enriched data for Cobourg agents
enriched_file = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "enriched_contacts_*.csv")))[-1]
cobourg_agents = []
with open(enriched_file, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if "cobourg" in row.get("Source City","").lower():
            cobourg_agents.append(row)

def status_tag(status):
    if "Expired" in status:
        return '<span class="tag tag-hot">EXPIRED</span>'
    return '<span class="tag tag-warm">NO SPONSOR</span>'

rows = ""
for a in cobourg_agents:
    name    = a.get("Name","")
    phone1  = a.get("Phone 1","")
    phone2  = a.get("Phone 2","")
    status  = a.get("Status","")
    expiry  = a.get("Expiry Date","")
    tag     = status_tag(status)
    phones  = phone1
    if phone2 and phone2 != phone1:
        phones += f"<br><small>{phone2}</small>"
    contact = phones or "<em style='color:#999'>Not found</em>"
    rows += f"<tr><td>{name}</td><td>{tag}</td><td>{expiry}</td><td>{contact}</td></tr>"

expired_count = sum(1 for a in cobourg_agents if "Expired" in a.get("Status",""))
sponsor_count = len(cobourg_agents) - expired_count
found_count   = sum(1 for a in cobourg_agents if a.get("Phone 1","").strip())

html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Cobourg Expired Insurance Agents — April 2026</title>
<style>
  @page {{ size: A4; margin: 2cm; }}
  body {{ font-family: Arial, sans-serif; font-size: 10pt; color: #222; line-height: 1.5; }}
  .header {{ background: #1a3a6b; color: white; padding: 20px 24px; margin-bottom: 20px; border-radius: 4px; }}
  .header h1 {{ margin: 0 0 4px 0; font-size: 18pt; }}
  .header p {{ margin: 0; font-size: 9pt; opacity: 0.85; }}
  .summary-box {{ background: #f0f4ff; border-left: 4px solid #1a3a6b; padding: 12px 16px; margin-bottom: 20px; font-size: 9.5pt; }}
  .summary-box strong {{ color: #1a3a6b; }}
  h2 {{ font-size: 12pt; color: #1a3a6b; border-bottom: 2px solid #1a3a6b; padding-bottom: 4px; margin-top: 24px; }}
  .tag {{ display: inline-block; font-size: 8pt; padding: 1px 7px; border-radius: 8px; font-weight: bold; }}
  .tag-hot {{ background: #ffe0e0; color: #c00; }}
  .tag-warm {{ background: #fff3cc; color: #996600; }}
  .pitch {{ background: #f9f9f9; border: 1px solid #ddd; border-radius: 4px; padding: 10px 14px; font-size: 9pt; font-style: italic; margin-bottom: 14px; color: #444; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 9pt; }}
  th {{ background: #1a3a6b; color: white; padding: 7px 8px; text-align: left; font-size: 8.5pt; }}
  td {{ padding: 6px 8px; border-bottom: 1px solid #e0e0e0; vertical-align: top; }}
  tr:nth-child(even) td {{ background: #f7f9ff; }}
  .footer {{ margin-top: 30px; font-size: 8pt; color: #999; text-align: center; border-top: 1px solid #ddd; padding-top: 10px; }}
</style>
</head>
<body>
<div class="header">
  <h1>Cobourg — Expired &amp; Lapsed Insurance Agents</h1>
  <p>Source: FSRA Ontario Public Registry &nbsp;|&nbsp; Pulled: April 24, 2026 &nbsp;|&nbsp; Total: {len(cobourg_agents)} agents</p>
</div>
<div class="summary-box">
  <strong>{expired_count} Fully Expired</strong> — licence lapsed &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>{sponsor_count} No Sponsor</strong> — licensed but needs a new home &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>{found_count} Phone Numbers Found</strong>
</div>
<div class="pitch">
  <strong>EXPIRED:</strong> "Your licence expired but your experience didn't. Primerica gets you back active fast."
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>NO SPONSOR:</strong> "You're already licensed — you just need a sponsor. Let's talk."
</div>
<table>
  <thead><tr><th>Name</th><th>Status</th><th>Expiry Date</th><th>Phone</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
<div class="footer">
  Built by Maximus &nbsp;|&nbsp; Tony DeCarlo — Primerica &nbsp;|&nbsp; FSRA Ontario Public Registry &nbsp;|&nbsp; April 24, 2026
</div>
</body>
</html>"""

out = os.path.join(SCRIPTS_DIR, "cobourg_expired_agents.pdf")
HTML(string=html_content).write_pdf(out)
print(f"PDF saved: {out}")
print(f"{len(cobourg_agents)} agents | {found_count} with phones")

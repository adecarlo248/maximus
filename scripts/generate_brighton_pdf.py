from weasyprint import HTML
import os

expired = [
    ("BROWN, THOMAS", "07097722", "May 2, 2024"),
    ("KNECHT, GAIL A", "93003232", "August 28, 2024"),
    ("MORAN, PAUL R.", "94026219", "August 31, 2025"),
    ("O'DONNELL, JOHN RYAN PATRICK (RYAN)", "16151301", "March 11, 2026"),
    ("TAYLOR, ETHAN ROBERT", "22210106", "November 9, 2024"),
]

no_sponsor = [
    ("HASE, KENDAL ALISA", "23219226", "October 2, 2025", "Oct 31, 2024"),
    ("HUTCHINGS, SCOTT A", "04082408", "July 22, 2027", "Mar 25, 2026"),
    ("ROSS-ROBINSON, JOYA LYNN", "23212733", "February 7, 2025", "Oct 22, 2024"),
    ("WONG-ESSENDI, LAPWAN", "19173000", "March 14, 2025", "—"),
]

expired_rows = "".join(f"<tr><td>{i+1}</td><td>{n}</td><td>{l}</td><td>{e}</td></tr>"
                       for i,(n,l,e) in enumerate(expired))
sponsor_rows = "".join(f"<tr><td>{i+1}</td><td>{n}</td><td>{l}</td><td>{e}</td><td>{t}</td></tr>"
                       for i,(n,l,e,t) in enumerate(no_sponsor))

html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Brighton Expired Insurance Agents — April 2026</title>
<style>
  @page {{ size: A4; margin: 2cm; }}
  body {{ font-family: Arial, sans-serif; font-size: 10pt; color: #222; line-height: 1.5; }}
  .header {{ background: #1a3a6b; color: white; padding: 20px 24px; margin-bottom: 20px; border-radius: 4px; }}
  .header h1 {{ margin: 0 0 4px 0; font-size: 18pt; }}
  .header p {{ margin: 0; font-size: 9pt; opacity: 0.85; }}
  .summary-box {{ background: #f0f4ff; border-left: 4px solid #1a3a6b; padding: 12px 16px; margin-bottom: 20px; font-size: 9.5pt; }}
  .summary-box strong {{ color: #1a3a6b; }}
  h2 {{ font-size: 12pt; color: #1a3a6b; border-bottom: 2px solid #1a3a6b; padding-bottom: 4px; margin-top: 24px; page-break-after: avoid; }}
  .tag {{ display: inline-block; font-size: 8pt; padding: 2px 8px; border-radius: 10px; font-weight: bold; margin-left: 8px; vertical-align: middle; }}
  .tag-hot {{ background: #ffe0e0; color: #c00; }}
  .tag-warm {{ background: #fff3cc; color: #996600; }}
  .pitch {{ background: #f9f9f9; border: 1px solid #ddd; border-radius: 4px; padding: 10px 14px; font-size: 9pt; font-style: italic; margin-bottom: 14px; color: #444; }}
  table {{ width: 100%; border-collapse: collapse; margin-bottom: 8px; font-size: 8.5pt; }}
  th {{ background: #1a3a6b; color: white; padding: 7px 8px; text-align: left; font-size: 8pt; }}
  td {{ padding: 6px 8px; border-bottom: 1px solid #e0e0e0; }}
  tr:nth-child(even) td {{ background: #f7f9ff; }}
  .footer {{ margin-top: 30px; font-size: 8pt; color: #999; text-align: center; border-top: 1px solid #ddd; padding-top: 10px; }}
</style>
</head>
<body>
<div class="header">
  <h1>Brighton — Expired &amp; Lapsed Insurance Agents</h1>
  <p>Source: FSRA Ontario Public Registry &nbsp;|&nbsp; Pulled: April 24, 2026 &nbsp;|&nbsp; Total: 9 agents</p>
</div>
<div class="summary-box">
  <strong>5 Fully Expired</strong> — licence lapsed, not authorized to sell &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>4 No Sponsor</strong> — licensed but terminated, looking for a new home &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>City:</strong> Brighton, ON
</div>
<h2>Priority Targets — Fully Expired <span class="tag tag-hot">HOT</span></h2>
<div class="pitch">"Your licence expired but your experience didn't. Primerica can get you back active fast — and you already know how this business works."</div>
<table>
  <thead><tr><th>#</th><th>Name</th><th>Licence #</th><th>Expiry Date</th></tr></thead>
  <tbody>{expired_rows}</tbody>
</table>
<h2>Secondary Targets — No Sponsor <span class="tag tag-warm">WARM</span></h2>
<div class="pitch">"You're already licensed — you just need a sponsor. Your licence is still active. Let's get you earning again."</div>
<table>
  <thead><tr><th>#</th><th>Name</th><th>Licence #</th><th>Licence Expiry</th><th>Terminated</th></tr></thead>
  <tbody>{sponsor_rows}</tbody>
</table>
<div class="footer">
  Built by Maximus &nbsp;|&nbsp; Tony DeCarlo — Primerica &nbsp;|&nbsp; Data: FSRA Ontario Public Registry &nbsp;|&nbsp; April 24, 2026
</div>
</body>
</html>"""

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brighton_expired_agents.pdf")
HTML(string=html_content).write_pdf(out_path)
print(f"PDF saved: {out_path}")

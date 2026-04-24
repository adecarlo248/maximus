from weasyprint import HTML
import os

expired = [
    ("ANTUNES, DANNY", "23213510", "March 5, 2025"),
    ("AUBREY, RANDY T", "94021341", "December 13, 2024"),
    ("BALAKRISHNAN, ARUNJITH", "21199537", "December 9, 2025"),
    ("BEATTIE, RYAN JAMES", "19175767", "September 8, 2024"),
    ("BRYANT, CATRINA ANN", "22211227", "December 15, 2024"),
    ("BURROWES, ROXANNE E", "04085171", "May 29, 2024"),
    ("CAUME, JEREMY RYAN", "23216690", "June 12, 2025"),
    ("DESJARDINS, GERALD", "02070252", "March 10, 2026"),
    ("O'BRIEN, LAURA LEE ANN", "09108042", "April 21, 2025"),
    ("SONNYLAL, BRIAN", "23215624", "May 10, 2025"),
    ("THOMPSON, DEREK", "17157933", "May 14, 2024"),
]

no_sponsor = [
    ("BERNARD, DANIEL WILLIAM", "23213673", "March 8, 2025", "Jun 4, 2024"),
    ("CANDOW, PATRICIA MARGARET CATHERINE", "22209161", "October 12, 2026", "May 29, 2025"),
    ("CORLEY, LISA PATRICA", "25234368", "March 19, 2027", "Jun 14, 2025"),
    ("DEDUK, SANDRA", "16154907", "October 12, 2024", "May 25, 2024"),
    ("JOY, JIA", "21199408", "December 6, 2025", "—"),
    ("MITCHELL, RYAN MELVIN", "25237842", "July 23, 2027", "Sep 24, 2025"),
    ("PATEL, RUCHIT GHANSHYAMBHAI", "21197865", "October 31, 2025", "May 14, 2024"),
    ("SONNYLAL, EMMANUEL BRIAN", "23219555", "October 19, 2025", "Oct 28, 2024"),
    ("STEWART, PETER DONALD", "94011717", "February 20, 2026", "—"),
]

expired_rows = "".join(f"<tr><td>{i+1}</td><td>{n}</td><td>{l}</td><td>{e}</td></tr>"
                       for i,(n,l,e) in enumerate(expired))
sponsor_rows = "".join(f"<tr><td>{i+1}</td><td>{n}</td><td>{l}</td><td>{e}</td><td>{t}</td></tr>"
                       for i,(n,l,e,t) in enumerate(no_sponsor))

html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Trenton Expired Insurance Agents — April 2026</title>
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
  <h1>Trenton — Expired &amp; Lapsed Insurance Agents</h1>
  <p>Source: FSRA Ontario Public Registry &nbsp;|&nbsp; Pulled: April 24, 2026 &nbsp;|&nbsp; Total: 20 agents</p>
</div>
<div class="summary-box">
  <strong>11 Fully Expired</strong> — licence lapsed, not authorized to sell &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>9 No Sponsor</strong> — licensed but terminated, looking for a new home &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>City:</strong> Trenton, ON
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

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trenton_expired_agents.pdf")
HTML(string=html_content).write_pdf(out_path)
print(f"PDF saved: {out_path}")

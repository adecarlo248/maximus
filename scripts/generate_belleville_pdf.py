from weasyprint import HTML
import os

expired = [
    ("ARMSTRONG, CAROLINE MARY GRACE", "24222250", "January 25, 2026"),
    ("BROWN, MEBO SIBI", "21191819", "April 14, 2025"),
    ("CENIZA, AILEEN TAGALOG", "13132325", "December 14, 2025"),
    ("CHRISTIAN, ANGEL SNEHALBHAI", "22202925", "March 28, 2026"),
    ("CODNER CLARKE, SHERNETTE ALECIA", "23220774", "November 22, 2025"),
    ("DEVARA, KALYAN", "21193370", "May 29, 2025"),
    ("DORAN, JOSEPH BERNARD", "15148597", "February 13, 2026"),
    ("EDNIE, DAVID", "06093746", "November 8, 2024"),
    ("HAWTHORN, REBECCA A", "16150773", "October 16, 2025"),
    ("HOLLAND, JESSICA LYNN", "23211656", "January 3, 2025"),
    ("HUBBLE, GEORGE ROY", "03076790", "April 11, 2025"),
    ("JENSEN, WILLIAM H", "97044886", "April 6, 2025"),
    ("KADIYA, DEEP NILESHKUMAR", "22207402", "August 22, 2024"),
    ("KAUR, KOMALPREET", "22205573", "June 21, 2024"),
    ("KAUR, NAVNEET", "23218815", "September 10, 2025"),
    ("KAUR, SHARANDEEP", "23218912", "September 12, 2025"),
    ("KUTTIKKADAN, ALWIN SHOLLY", "23218705", "September 5, 2025"),
    ("LEWIS, GLENNA", "08101300", "November 2, 2024"),
    ("MAGUIRE, CHRISTOPHER GERARD", "94029232", "March 30, 2025"),
    ("MCEATHRON, TONI LYNNE", "07100310", "January 28, 2026"),
    ("MORGAN, JESSICA PAYGE", "20186991", "December 13, 2024"),
    ("NEELY, JACOB KENT", "23220566", "November 17, 2025"),
    ("NOHRIA, CHAKSHU", "23215588", "May 9, 2025"),
    ("NORONHA, MELISSA JILL", "20185757", "November 5, 2024"),
    ("PATEL, DWIT ASHWINBHAI", "24222465", "January 31, 2026"),
    ("PATEL, MAHENDRABHAI", "20186935", "December 12, 2024"),
    ("RAKHRA, AKSHDEEP SINGH", "23218431", "August 23, 2025"),
    ("SACHDEVA, SUHANI", "22203153", "April 3, 2026"),
    ("SEWELL, ERIC T", "00059946", "February 6, 2026"),
    ("STAPLEY, CODY TYLER", "23216012", "May 25, 2025"),
    ("STURCH, PHILIP", "94024695", "March 7, 2025"),
]

no_sponsor = [
    ("ALINGBAS, DELIA DULINEN", "24226616", "July 9, 2026", "Jan 20, 2025"),
    ("BARSOTTI, DANIELLA ANGELIQUE", "12127320", "August 23, 2024", "—"),
    ("BENOIT, ALISON ELIZABETH", "23219206", "September 28, 2025", "Mar 28, 2025"),
    ("BROOKS, JEFFREY JAMES", "14138950", "January 13, 2026", "Feb 1, 2025"),
    ("CALLAGHAN, THOMAS JOHN", "22205377", "June 15, 2024", "May 12, 2024"),
    ("COLTON, ERIN", "24226807", "July 15, 2026", "Sep 29, 2024"),
    ("CONDON, SARAH", "19176477", "September 3, 2025", "Oct 11, 2024"),
    ("LAPALM, KENNETH E", "93007451", "March 11, 2025", "—"),
    ("MABEE, CRYSTAL MARJORIE", "23218207", "August 10, 2025", "Jul 30, 2025"),
    ("MCCUTCHEON, RYAN CLIFFORD", "24223153", "March 4, 2026", "Jan 13, 2025"),
    ("PAUL, NEENU", "25232475", "January 29, 2027", "Apr 11, 2025"),
    ("PATEL, SHREEPAL", "25233890", "March 6, 2027", "Mar 25, 2026"),
    ("REENA, REENA", "23218273", "August 13, 2025", "Jun 30, 2025"),
    ("SPENCE, KENDRA FRANCES", "24228913", "October 6, 2026", "Jan 23, 2026"),
    ("TAYLOR, REBECCA LYNN", "24228527", "September 23, 2026", "Nov 29, 2024"),
]

expired_rows = "".join(f"<tr><td>{i+1}</td><td>{n}</td><td>{l}</td><td>{e}</td></tr>"
                       for i,(n,l,e) in enumerate(expired))
sponsor_rows = "".join(f"<tr><td>{i+1}</td><td>{n}</td><td>{l}</td><td>{e}</td><td>{t}</td></tr>"
                       for i,(n,l,e,t) in enumerate(no_sponsor))

html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Belleville Expired Insurance Agents — April 2026</title>
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
  <h1>Belleville — Expired &amp; Lapsed Insurance Agents</h1>
  <p>Source: FSRA Ontario Public Registry &nbsp;|&nbsp; Pulled: April 24, 2026 &nbsp;|&nbsp; Total: 46 agents</p>
</div>
<div class="summary-box">
  <strong>31 Fully Expired</strong> — licence lapsed, not authorized to sell &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>15 No Sponsor</strong> — licensed but terminated, looking for a new home &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>City:</strong> Belleville, ON
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

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "belleville_expired_agents.pdf")
HTML(string=html_content).write_pdf(out_path)
print(f"PDF saved: {out_path}")

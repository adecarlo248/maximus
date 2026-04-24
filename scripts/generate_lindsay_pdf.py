from weasyprint import HTML
import os

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Lindsay Expired Insurance Agents — April 2026</title>
<style>
  @page { size: A4; margin: 2cm; }
  body { font-family: Arial, sans-serif; font-size: 10pt; color: #222; line-height: 1.5; }
  .header { background: #1a3a6b; color: white; padding: 20px 24px; margin-bottom: 20px; border-radius: 4px; }
  .header h1 { margin: 0 0 4px 0; font-size: 18pt; }
  .header p { margin: 0; font-size: 9pt; opacity: 0.85; }
  .summary-box { background: #f0f4ff; border-left: 4px solid #1a3a6b; padding: 12px 16px; margin-bottom: 20px; font-size: 9.5pt; }
  .summary-box strong { color: #1a3a6b; }
  h2 { font-size: 12pt; color: #1a3a6b; border-bottom: 2px solid #1a3a6b; padding-bottom: 4px; margin-top: 24px; page-break-after: avoid; }
  .tag { display: inline-block; font-size: 8pt; padding: 2px 8px; border-radius: 10px; font-weight: bold; margin-left: 8px; vertical-align: middle; }
  .tag-hot { background: #ffe0e0; color: #c00; }
  .tag-warm { background: #fff3cc; color: #996600; }
  .pitch { background: #f9f9f9; border: 1px solid #ddd; border-radius: 4px; padding: 10px 14px; font-size: 9pt; font-style: italic; margin-bottom: 14px; color: #444; }
  table { width: 100%; border-collapse: collapse; margin-bottom: 8px; font-size: 8.5pt; }
  th { background: #1a3a6b; color: white; padding: 7px 8px; text-align: left; font-size: 8pt; }
  td { padding: 6px 8px; border-bottom: 1px solid #e0e0e0; }
  tr:nth-child(even) td { background: #f7f9ff; }
  .footer { margin-top: 30px; font-size: 8pt; color: #999; text-align: center; border-top: 1px solid #ddd; padding-top: 10px; }
</style>
</head>
<body>

<div class="header">
  <h1>Lindsay — Expired &amp; Lapsed Insurance Agents</h1>
  <p>Source: FSRA Ontario Public Registry &nbsp;|&nbsp; Pulled: April 24, 2026 &nbsp;|&nbsp; Total: 12 agents</p>
</div>

<div class="summary-box">
  <strong>7 Fully Expired</strong> — licence lapsed, not authorized to sell &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>5 No Sponsor</strong> — licensed but terminated, looking for a new home &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>City:</strong> Lindsay, ON
</div>

<h2>Priority Targets — Fully Expired <span class="tag tag-hot">HOT</span></h2>
<div class="pitch">
  "Your licence expired but your experience didn't. Primerica can get you back active fast — and you already know how this business works."
</div>
<table>
  <thead>
    <tr><th>#</th><th>Name</th><th>Licence #</th><th>Expiry Date</th><th>Licence Class</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>HARDING, JASMINE AMBER</td><td>21191701</td><td>May 14, 2025</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>2</td><td>HINES, STRICKLAND H</td><td>22209983</td><td>November 6, 2024</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>3</td><td>LOIGNON, MARCEL JOSEPH</td><td>17156962</td><td>March 4, 2026</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>4</td><td>MCKYE, MICHAEL WILLIAM (MIKE)</td><td>15146446</td><td>September 17, 2025</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>5</td><td>MOONEY, CAROL</td><td>94014250</td><td>September 13, 2024</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>6</td><td>MOONEY, DAVID</td><td>94018310</td><td>February 24, 2025</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>7</td><td>MUCHA, JANE MARIE</td><td>08105823</td><td>November 27, 2024</td><td>Life &amp; A&amp;S</td></tr>
  </tbody>
</table>

<h2>Secondary Targets — No Sponsor <span class="tag tag-warm">WARM</span></h2>
<div class="pitch">
  "You're already licensed — you just need a sponsor. Your licence is still active. Let's get you earning again."
</div>
<table>
  <thead>
    <tr><th>#</th><th>Name</th><th>Licence #</th><th>Licence Expiry</th><th>Terminated</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>ARCHIBALD, ANDREW CAMERON</td><td>22209180</td><td>October 13, 2026</td><td>Jan 27, 2025</td></tr>
    <tr><td>2</td><td>BUDWAY, JESSICA ANN</td><td>19177634</td><td>October 15, 2025</td><td>Mar 7, 2025</td></tr>
    <tr><td>3</td><td>HARDING, BIBI WAHEEDA</td><td>24224301</td><td>April 10, 2026</td><td>Oct 9, 2024</td></tr>
    <tr><td>4</td><td>JEWELL, BROOKE ALEEN MARGARET</td><td>24225012</td><td>May 7, 2026</td><td>Oct 7, 2024</td></tr>
    <tr><td>5</td><td>MASSEY, SUNIL MANUJ (NEIL)</td><td>22210476</td><td>November 21, 2026</td><td>Jun 16, 2025</td></tr>
  </tbody>
</table>

<div class="footer">
  Built by Maximus &nbsp;|&nbsp; Tony DeCarlo — Primerica &nbsp;|&nbsp; Data: FSRA Ontario Public Registry &nbsp;|&nbsp; April 24, 2026
</div>

</body>
</html>
"""

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lindsay_expired_agents.pdf")
HTML(string=html_content).write_pdf(out_path)
print(f"PDF saved: {out_path}")

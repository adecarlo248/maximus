from weasyprint import HTML, CSS
import os

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Peterborough Expired Insurance Agents — April 2026</title>
<style>
  @page {
    size: A4;
    margin: 2cm;
  }
  body {
    font-family: Arial, sans-serif;
    font-size: 10pt;
    color: #222;
    line-height: 1.5;
  }
  .header {
    background: #1a3a6b;
    color: white;
    padding: 20px 24px;
    margin-bottom: 20px;
    border-radius: 4px;
  }
  .header h1 {
    margin: 0 0 4px 0;
    font-size: 18pt;
    letter-spacing: 0.5px;
  }
  .header p {
    margin: 0;
    font-size: 9pt;
    opacity: 0.85;
  }
  .summary-box {
    background: #f0f4ff;
    border-left: 4px solid #1a3a6b;
    padding: 12px 16px;
    margin-bottom: 20px;
    font-size: 9.5pt;
  }
  .summary-box strong { color: #1a3a6b; }
  h2 {
    font-size: 12pt;
    color: #1a3a6b;
    border-bottom: 2px solid #1a3a6b;
    padding-bottom: 4px;
    margin-top: 24px;
    page-break-after: avoid;
  }
  .tag {
    display: inline-block;
    font-size: 8pt;
    padding: 2px 8px;
    border-radius: 10px;
    font-weight: bold;
    margin-left: 8px;
    vertical-align: middle;
  }
  .tag-hot { background: #ffe0e0; color: #c00; }
  .tag-warm { background: #fff3cc; color: #996600; }
  .pitch {
    background: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px 14px;
    font-size: 9pt;
    font-style: italic;
    margin-bottom: 14px;
    color: #444;
    page-break-inside: avoid;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 8px;
    font-size: 8.5pt;
    page-break-inside: auto;
  }
  thead { page-break-after: avoid; }
  tr { page-break-inside: avoid; }
  th {
    background: #1a3a6b;
    color: white;
    padding: 7px 8px;
    text-align: left;
    font-size: 8pt;
  }
  td {
    padding: 6px 8px;
    border-bottom: 1px solid #e0e0e0;
  }
  tr:nth-child(even) td { background: #f7f9ff; }
  tr:hover td { background: #eef2ff; }
  .footer {
    margin-top: 30px;
    font-size: 8pt;
    color: #999;
    text-align: center;
    border-top: 1px solid #ddd;
    padding-top: 10px;
  }
</style>
</head>
<body>

<div class="header">
  <h1>Peterborough — Expired &amp; Lapsed Insurance Agents</h1>
  <p>Source: FSRA Ontario Public Registry &nbsp;|&nbsp; Pulled: April 24, 2026 &nbsp;|&nbsp; Total: 43 agents</p>
</div>

<div class="summary-box">
  <strong>18 Fully Expired</strong> — licence lapsed, not authorized to sell &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>25 No Sponsor</strong> — licensed but terminated, looking for a new home &nbsp;&nbsp;|&nbsp;&nbsp;
  <strong>City:</strong> Peterborough, ON
</div>

<h2>Priority Targets — Fully Expired <span class="tag tag-hot">HOT</span></h2>
<div class="pitch">
  Pitch: "Your licence expired but your experience didn't. Primerica can get you back active fast — and you already know how this business works."
</div>
<table>
  <thead>
    <tr><th>#</th><th>Name</th><th>Licence #</th><th>Expiry Date</th><th>Licence Class</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>BATEMAN, BRADLEY H</td><td>96037642</td><td>June 18, 2024</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>2</td><td>BURNES, KATHERINE ROSE (KATIE)</td><td>16152885</td><td>April 27, 2025</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>3</td><td>CAMPBELL, HEATHER LYNN</td><td>10116388</td><td>September 29, 2024</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>4</td><td>COONEY, LORRAINE</td><td>09109801</td><td>August 11, 2025</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>5</td><td>DARIA, ARIANE MAE</td><td>22201912</td><td>February 24, 2026</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>6</td><td>DEVI, POOJA</td><td>22204159</td><td>May 10, 2024</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>7</td><td>DOWNIE, EMILY CAROLINE</td><td>14136050</td><td>March 4, 2026</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>8</td><td>DWAMENA, ISAAC NYANOR</td><td>23216339</td><td>June 4, 2025</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>9</td><td>GILLARD, HANK C</td><td>96037072</td><td>May 6, 2024</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>10</td><td>GOODMAN, KIRK RONALD GORDON</td><td>09109341</td><td>July 13, 2025</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>11</td><td>HARRINGTON, BEVERLY ANN</td><td>96035951</td><td>October 8, 2024</td><td>General</td></tr>
    <tr><td>12</td><td>JANK, TARREN MICHAEL</td><td>22203453</td><td>April 11, 2026</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>13</td><td>JARQUIN, CARLOS JOSUE</td><td>16152863</td><td>October 1, 2024</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>14</td><td>KONAKALLA, SRI VIDYA</td><td>21197660</td><td>October 26, 2025</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>15</td><td>MANN, HARPREET SINGH</td><td>23219081</td><td>September 21, 2025</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>16</td><td>MCMASTER, DENISE LOUISE</td><td>12126264</td><td>November 17, 2024</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>17</td><td>MITCHELL, KRISTINE ALICE</td><td>09108414</td><td>October 22, 2025</td><td>Life &amp; A&amp;S</td></tr>
    <tr><td>18</td><td>NAUS, BENJAMIN FREDERICK</td><td>23215207</td><td>April 30, 2025</td><td>Life &amp; A&amp;S</td></tr>
  </tbody>
</table>

<h2>Secondary Targets — No Sponsor <span class="tag tag-warm">WARM</span></h2>
<div class="pitch">
  Pitch: "You're already licensed — you just need a sponsor. Your licence is still active. Let's get you earning again."
</div>
<table>
  <thead>
    <tr><th>#</th><th>Name</th><th>Licence #</th><th>Licence Expiry</th><th>Terminated</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>ABU AMOUNA, BILLAL</td><td>25234132</td><td>March 12, 2027</td><td>Sept 9, 2025</td></tr>
    <tr><td>2</td><td>ADEKANMBI, SAMUEL BABATUNDE</td><td>24223151</td><td>March 4, 2026</td><td>Feb 3, 2025</td></tr>
    <tr><td>3</td><td>AKASH, AKASH</td><td>24228769</td><td>October 2, 2026</td><td>Mar 26, 2025</td></tr>
    <tr><td>4</td><td>BREESE, NICOLAS PAUL</td><td>25232460</td><td>January 29, 2027</td><td>Apr 2, 2025</td></tr>
    <tr><td>5</td><td>CLARKE, CAROLINE MICHELE (CARRIE)</td><td>23212311</td><td>January 24, 2025</td><td>Jun 12, 2024</td></tr>
    <tr><td>6</td><td>COLLETT, JENNIFER</td><td>25241601</td><td>October 26, 2027</td><td>Feb 18, 2026</td></tr>
    <tr><td>7</td><td>DARJI, ANERI CHAMPAKBHAI</td><td>24227077</td><td>July 25, 2026</td><td>Jan 1, 2025</td></tr>
    <tr><td>8</td><td>DHIMAN, KARAN VIJAY KUMAR</td><td>22204657</td><td>November 18, 2026</td><td>Nov 19, 2024</td></tr>
    <tr><td>9</td><td>EDWARDS, ADAM JAMES</td><td>24227940</td><td>September 5, 2026</td><td>Feb 6, 2025</td></tr>
    <tr><td>10</td><td>FULKER, WILLIAM LAWRENCE</td><td>94022274</td><td>March 24, 2025</td><td>—</td></tr>
    <tr><td>11</td><td>GAJJAR, JAYNI ALPESH</td><td>25235750</td><td>May 4, 2027</td><td>Sept 9, 2025</td></tr>
    <tr><td>12</td><td>GILLAN, JONATHAN MITCHELL (JON)</td><td>17157043</td><td>July 14, 2026</td><td>—</td></tr>
    <tr><td>13</td><td>GILLMAN, LAWRENCE</td><td>02072009</td><td>June 20, 2026</td><td>—</td></tr>
    <tr><td>14</td><td>GUDE, PRAVALLIKA</td><td>24230105</td><td>November 7, 2026</td><td>Mar 2, 2025</td></tr>
    <tr><td>15</td><td>GUPTA, SAGAR</td><td>24226662</td><td>July 11, 2026</td><td>Nov 26, 2025</td></tr>
    <tr><td>16</td><td>HADDOCK, DEBORAH</td><td>07099264</td><td>May 13, 2024</td><td>—</td></tr>
    <tr><td>17</td><td>IFEANYI-NWANOZIE, NISHAR IJEOMA EMELDA</td><td>25235367</td><td>April 22, 2027</td><td>Sept 8, 2025</td></tr>
    <tr><td>18</td><td>KING, KENDAL STEPHANIE</td><td>25233139</td><td>February 18, 2027</td><td>Jan 23, 2026</td></tr>
    <tr><td>19</td><td>LAITE, JAMES BRIAN</td><td>24228819</td><td>October 3, 2026</td><td>Jan 21, 2025</td></tr>
    <tr><td>20</td><td>MCNAMEE, EMILY</td><td>17159512</td><td>May 15, 2024</td><td>May 3, 2024</td></tr>
    <tr><td>21</td><td>MURAR, GURBAKSH</td><td>24224038</td><td>April 2, 2026</td><td>Aug 2, 2024</td></tr>
    <tr><td>22</td><td>NORTHAM, JORDAN RICHARD</td><td>24230642</td><td>November 21, 2026</td><td>Jan 3, 2026</td></tr>
    <tr><td>23</td><td>ODINKO, CHIDIOGO LYNDA</td><td>25237501</td><td>July 16, 2027</td><td>Dec 16, 2025</td></tr>
    <tr><td>24</td><td>PALMER, ANDREW PAUL</td><td>24224913</td><td>May 2, 2026</td><td>Jan 30, 2025</td></tr>
    <tr><td>25</td><td>PAREKH, NIDHI DINESHBHAI</td><td>24228601</td><td>September 24, 2026</td><td>Jul 4, 2025</td></tr>
  </tbody>
</table>

<div class="footer">
  Built by Maximus &nbsp;|&nbsp; Tony DeCarlo — Primerica &nbsp;|&nbsp; Data: FSRA Ontario Public Registry &nbsp;|&nbsp; April 24, 2026
</div>

</body>
</html>
"""

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "peterborough_expired_agents.pdf")
HTML(string=html_content).write_pdf(out_path)
print(f"PDF saved: {out_path}")

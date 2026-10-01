#!/usr/bin/env python3
import html
import re
import subprocess
import zipfile
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parent
FILES = [
    ROOT / "README.md",
    ROOT / "01-Rod-1APP-Training-Module.md",
    ROOT / "02-Rod-Account-Phone-Setup-Checklist.md",
    ROOT / "03-Client-Onboarding-and-Technical-Handoff-Template.md",
    ROOT / "04-1APP-Associate-Sales-Program-v3.md",
    ROOT / "05-Automation-Catalogue-Pricing-Timeframes-and-Bundles.md",
    ROOT / "06-Quote-Approval-and-Delivery-Process.md",
    ROOT / "07-Rod-Certification-Test-and-Answer-Key.md",
    ROOT / "08-Automation-Value-and-ROI-Field-Guide.md",
    ROOT / "09-Day-45-Review-and-Quote-Builder-Practical.md",
    ROOT / "10-Revenue-Reactivation-Sprint-Playbook.md",
]

CSS = r'''
@page { size: Letter; margin: .64in .68in .7in;
  @bottom-left { content: "1APP Technologies Inc. • Internal Working Draft"; font-size: 7pt; color:#667085; }
  @bottom-right { content: "Page " counter(page) " of " counter(pages); font-size: 7pt; color:#667085; }
}
* { box-sizing:border-box; }
body { font-family:Arial,Helvetica,sans-serif; color:#172033; font-size:9.2pt; line-height:1.38; }
h1 { color:#0a2d62; font-size:21pt; line-height:1.08; border-bottom:3px solid #1d63ff; padding-bottom:9px; margin:0 0 13px; }
h2 { color:#0a2d62; font-size:14pt; margin:18px 0 6px; page-break-after:avoid; }
h3 { color:#164b8f; font-size:11pt; margin:13px 0 5px; page-break-after:avoid; }
p { margin:0 0 7px; }
ul,ol { margin:0 0 8px 18px; padding:0; }
li { margin:2px 0; }
blockquote { margin:9px 0 11px; padding:9px 12px; border-left:4px solid #29a7ff; background:#eef6ff; }
code { font-family:Consolas,monospace; font-size:8.4pt; background:#eef2f7; padding:1px 3px; }
table { width:100%; border-collapse:collapse; margin:8px 0 12px; page-break-inside:auto; font-size:8.4pt; }
thead { display:table-header-group; }
tr { page-break-inside:avoid; }
th { background:#0a2d62; color:white; text-align:left; padding:5px 6px; border:1px solid #0a2d62; }
td { padding:5px 6px; border:1px solid #ced7e5; vertical-align:top; }
tr:nth-child(even) td { background:#f7f9fc; }
.notice { background:#fff5dd; border:1px solid #efc46b; color:#624300; padding:8px 10px; margin-bottom:13px; font-size:8.2pt; }
'''


def inline(value: str) -> str:
    value = html.escape(value)
    value = re.sub(r'(https?://[^\s<>,)]+)', r'<a href="\1">\1</a>', value)
    value = re.sub(r'`([^`]+)`', r'<code>\1</code>', value)
    value = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', value)
    value = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', value)
    return value


def parse_table(lines, index):
    header = [c.strip() for c in lines[index].strip().strip('|').split('|')]
    rows = []
    index += 2
    while index < len(lines) and lines[index].strip().startswith('|'):
        rows.append([c.strip() for c in lines[index].strip().strip('|').split('|')])
        index += 1
    out = ['<table><thead><tr>'] + [f'<th>{inline(c)}</th>' for c in header] + ['</tr></thead><tbody>']
    for row in rows:
        row += [''] * (len(header) - len(row))
        out += ['<tr>'] + [f'<td>{inline(c)}</td>' for c in row[:len(header)]] + ['</tr>']
    out.append('</tbody></table>')
    return ''.join(out), index


def md_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    out, index, in_ul, in_ol = [], 0, False, False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul: out.append('</ul>'); in_ul = False
        if in_ol: out.append('</ol>'); in_ol = False

    while index < len(lines):
        s = lines[index].strip()
        if not s:
            close_lists(); index += 1; continue
        if s.startswith('|') and index + 1 < len(lines) and re.match(r'^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$', lines[index + 1]):
            close_lists(); table, index = parse_table(lines, index); out.append(table); continue
        h = re.match(r'^(#{1,6})\s+(.*)$', s)
        if h:
            close_lists(); level = len(h.group(1)); out.append(f'<h{level}>{inline(h.group(2))}</h{level}>'); index += 1; continue
        if s.startswith('>'):
            close_lists(); q=[]
            while index < len(lines) and lines[index].strip().startswith('>'):
                q.append(lines[index].strip()[1:].strip()); index += 1
            out.append('<blockquote>' + ''.join(f'<p>{inline(x)}</p>' for x in q if x) + '</blockquote>'); continue
        if re.match(r'^[-*]\s+', s):
            if not in_ul: close_lists(); out.append('<ul>'); in_ul=True
            out.append('<li>'+inline(re.sub(r'^[-*]\s+','',s))+'</li>'); index += 1; continue
        if re.match(r'^\d+\.\s+', s):
            if not in_ol: close_lists(); out.append('<ol>'); in_ol=True
            out.append('<li>'+inline(re.sub(r'^\d+\.\s+','',s))+'</li>'); index += 1; continue
        close_lists(); para=[s]; index += 1
        while index < len(lines):
            n=lines[index].strip()
            if not n or n.startswith(('#','>','|')) or re.match(r'^[-*]\s+',n) or re.match(r'^\d+\.\s+',n): break
            para.append(n); index += 1
        out.append('<p>'+inline(' '.join(para))+'</p>')
    close_lists()
    return '\n'.join(out)


for md in FILES:
    raw = md.read_text(encoding='utf-8')
    title = next((x[2:].strip() for x in raw.splitlines() if x.startswith('# ')), md.stem)
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><meta name="author" content="1APP Technologies Inc."><style>{CSS}</style></head><body><div class="notice"><strong>Internal working draft.</strong> Owners must approve pricing, commission, scope, and legal terms before client or associate use.</div>{md_to_html(raw)}</body></html>'''
    html_path = md.with_suffix('.html')
    pdf_path = md.with_suffix('.pdf')
    html_path.write_text(doc, encoding='utf-8')
    subprocess.check_call(['weasyprint', str(html_path), str(pdf_path)])

master = ROOT / '1APP-Rod-Sales-and-Onboarding-System-DRAFT.pdf'
merged = fitz.open()
for md in FILES:
    src = fitz.open(md.with_suffix('.pdf')); merged.insert_pdf(src); src.close()
merged.set_metadata({'title':'1APP Rod Sales and Onboarding System — Draft','author':'1APP Technologies Inc.','subject':'Sales training, onboarding, associate program, pricing, bundles, and quote governance'})
merged.save(master); merged.close()

archive_path = ROOT / '1APP-Rod-Sales-and-Onboarding-System-DRAFT.zip'
with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
    for md in FILES:
        for f in (md, md.with_suffix('.html'), md.with_suffix('.pdf')):
            archive.write(f, f.name)
    archive.write(ROOT / '1APP-Quote-Builder.html', '1APP-Quote-Builder.html')
    archive.write(Path(__file__), Path(__file__).name)

print(master)
print(archive_path)

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
    ROOT / "01-1APP-Sales-Manager-Employment-Agreement-DRAFT.md",
    ROOT / "02-1APP-Sales-Manager-Compensation-and-KPI-Schedule-DRAFT.md",
    ROOT / "03-1APP-Sales-Manager-First-180-Days.md",
    ROOT / "04-1APP-Sales-Manager-Training-Manual.md",
    ROOT / "05-1APP-Sales-Certification-and-Scorecards.md",
    ROOT / "06-OWNER-DECISIONS-BEFORE-SIGNING.md",
    ROOT / "07-1APP-User-Access-and-Onboarding-Permissions.md",
]

CSS = r'''
@page { size: Letter; margin: 0.68in 0.72in 0.72in;
  @bottom-left { content: "1APP Technologies Inc. • Confidential Draft"; font-size: 7.5pt; color: #718096; }
  @bottom-right { content: "Page " counter(page) " of " counter(pages); font-size: 7.5pt; color: #718096; }
}
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; color: #14243a; font-size: 9.7pt; line-height: 1.43; }
h1 { font-size: 22pt; line-height: 1.08; color: #102e52; margin: 0 0 14px; padding-bottom: 10px; border-bottom: 3px solid #d9a71c; }
h2 { font-size: 14.5pt; color: #102e52; margin: 20px 0 7px; padding-top: 3px; page-break-after: avoid; }
h3 { font-size: 11.8pt; color: #174a7c; margin: 14px 0 6px; page-break-after: avoid; }
p { margin: 0 0 8px; }
ul, ol { margin: 0 0 9px 20px; padding: 0; }
li { margin: 2.5px 0; }
blockquote { margin: 10px 0 12px; padding: 10px 13px; border-left: 4px solid #d9a71c; background: #f3f7fb; color: #20364f; }
code { font-family: Consolas, monospace; font-size: 8.8pt; background: #edf2f7; padding: 1px 3px; border-radius: 3px; }
hr { border: 0; border-top: 1px solid #ccd7e4; margin: 20px 0; }
table { width: 100%; border-collapse: collapse; margin: 9px 0 14px; page-break-inside: avoid; }
th { background: #102e52; color: white; text-align: left; padding: 6px 7px; border: 1px solid #102e52; }
td { padding: 6px 7px; border: 1px solid #ccd7e4; vertical-align: top; }
tr:nth-child(even) td { background: #f7f9fc; }
.doc-meta { margin: 0 0 15px; padding: 9px 11px; border: 1px solid #d7b74e; background: #fff9df; color: #4f4214; font-size: 8.8pt; }
strong { font-weight: 700; }
'''


def inline(value: str) -> str:
    value = html.escape(value)
    value = re.sub(r'`([^`]+)`', r'<code>\1</code>', value)
    value = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', value)
    value = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', value)
    value = re.sub(r'(https?://[^\s<]+)', r'<a href="\1">\1</a>', value)
    return value


def parse_table(lines, index):
    header = [cell.strip() for cell in lines[index].strip().strip('|').split('|')]
    rows = []
    index += 2
    while index < len(lines) and lines[index].strip().startswith('|'):
        rows.append([cell.strip() for cell in lines[index].strip().strip('|').split('|')])
        index += 1
    output = ['<table><thead><tr>']
    output += [f'<th>{inline(cell)}</th>' for cell in header]
    output.append('</tr></thead><tbody>')
    for row in rows:
        row += [''] * (len(header) - len(row))
        output.append('<tr>')
        output += [f'<td>{inline(cell)}</td>' for cell in row[:len(header)]]
        output.append('</tr>')
    output.append('</tbody></table>')
    return ''.join(output), index


def md_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    output = []
    index = 0
    in_ul = False
    in_ol = False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            output.append('</ul>')
            in_ul = False
        if in_ol:
            output.append('</ol>')
            in_ol = False

    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped:
            close_lists()
            index += 1
            continue
        if stripped.startswith('|') and index + 1 < len(lines) and re.match(r'^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$', lines[index + 1]):
            close_lists()
            table, index = parse_table(lines, index)
            output.append(table)
            continue
        if stripped == '---':
            close_lists()
            output.append('<hr>')
            index += 1
            continue
        heading = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if heading:
            close_lists()
            level = len(heading.group(1))
            output.append(f'<h{level}>{inline(heading.group(2))}</h{level}>')
            index += 1
            continue
        if stripped.startswith('>'):
            close_lists()
            quote = []
            while index < len(lines) and lines[index].strip().startswith('>'):
                quote.append(lines[index].strip()[1:].strip())
                index += 1
            output.append('<blockquote>' + ''.join(f'<p>{inline(item)}</p>' for item in quote if item) + '</blockquote>')
            continue
        if re.match(r'^[-*]\s+', stripped):
            if not in_ul:
                close_lists()
                output.append('<ul>')
                in_ul = True
            output.append('<li>' + inline(re.sub(r'^[-*]\s+', '', stripped)) + '</li>')
            index += 1
            continue
        if re.match(r'^\d+\.\s+', stripped):
            if not in_ol:
                close_lists()
                output.append('<ol>')
                in_ol = True
            output.append('<li>' + inline(re.sub(r'^\d+\.\s+', '', stripped)) + '</li>')
            index += 1
            continue
        close_lists()
        paragraph = [stripped]
        index += 1
        while index < len(lines):
            nxt = lines[index].strip()
            if not nxt or nxt.startswith(('#', '>', '|', '---')) or re.match(r'^[-*]\s+', nxt) or re.match(r'^\d+\.\s+', nxt):
                break
            paragraph.append(nxt)
            index += 1
        output.append('<p>' + inline(' '.join(paragraph)) + '</p>')
    close_lists()
    return '\n'.join(output)


for markdown_path in FILES:
    markdown = markdown_path.read_text(encoding='utf-8')
    title = next((line.strip('# ').strip() for line in markdown.splitlines() if line.startswith('# ')), markdown_path.stem)
    body = md_to_html(markdown)
    document = f'''<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><meta name="author" content="1APP Technologies Inc."><style>{CSS}</style></head><body><div class="doc-meta"><strong>Confidential working draft.</strong> Owner approval and Ontario employment-law review are required before signature or use as a binding compensation plan.</div>{body}</body></html>'''
    html_path = markdown_path.with_suffix('.html')
    pdf_path = markdown_path.with_suffix('.pdf')
    html_path.write_text(document, encoding='utf-8')
    subprocess.check_call(['weasyprint', str(html_path), str(pdf_path)])
    print(pdf_path)

master_pdf = ROOT / "1APP-Sales-Manager-Hiring-and-Training-Pack-DRAFT.pdf"
merged = fitz.open()
for markdown_path in FILES:
    source = fitz.open(markdown_path.with_suffix('.pdf'))
    merged.insert_pdf(source)
    source.close()
merged.set_metadata({
    "title": "1APP Sales Manager Hiring and Training Pack — Draft",
    "author": "1APP Technologies Inc.",
    "subject": "Employment, compensation, training, certification, and access controls",
})
merged.save(master_pdf)
merged.close()
print(master_pdf)

package_zip = ROOT / "1APP-Sales-Manager-Hiring-and-Training-Pack-DRAFT.zip"
with zipfile.ZipFile(package_zip, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    for markdown_path in FILES:
        for source in (markdown_path, markdown_path.with_suffix('.html'), markdown_path.with_suffix('.pdf')):
            archive.write(source, arcname=source.name)
    archive.write(Path(__file__), arcname=Path(__file__).name)
print(package_zip)

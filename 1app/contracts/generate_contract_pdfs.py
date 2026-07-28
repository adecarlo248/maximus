#!/usr/bin/env python3
import html, re, subprocess
from pathlib import Path

ROOT = Path('/home/maximus/.openclaw/workspace')
FILES = [
    ROOT/'1app/contracts/1APP-Associate-Sales-Structure-and-Contract-Pack.md',
    ROOT/'1app/contracts/1APP-Level-1-Referral-Associate-Agreement.md',
    ROOT/'1app/contracts/1APP-Level-2-Sales-Associate-Agreement.md',
    ROOT/'1app/contracts/1APP-Level-3-Certified-Partner-Agreement.md',
    ROOT/'1app/contracts/1APP-Associate-Contracts-Full-Pack.md',
]

CSS = r'''
@page { size: Letter; margin: 0.7in 0.75in; @bottom-right { content: "Page " counter(page) " of " counter(pages); font-size: 8pt; color: #777; } }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; color: #171717; font-size: 10.5pt; line-height: 1.48; }
h1 { font-size: 23pt; line-height: 1.12; color: #0b1220; margin: 0 0 16px; padding-bottom: 10px; border-bottom: 3px solid #1f3a8a; }
h2 { font-size: 15pt; color: #111827; margin: 22px 0 8px; padding-top: 4px; page-break-after: avoid; }
h3 { font-size: 12.5pt; color: #1f2937; margin: 16px 0 7px; page-break-after: avoid; }
p { margin: 0 0 9px; }
ul, ol { margin: 0 0 10px 20px; padding: 0; }
li { margin: 3px 0; }
blockquote { margin: 10px 0 12px; padding: 10px 14px; border-left: 4px solid #1f3a8a; background: #f3f6fb; color: #1f2937; }
code { font-family: Consolas, monospace; font-size: 9.5pt; background: #f3f4f6; padding: 1px 3px; border-radius: 3px; }
hr { border: 0; border-top: 1px solid #d1d5db; margin: 22px 0; page-break-after: avoid; }
table { width: 100%; border-collapse: collapse; margin: 10px 0 16px; page-break-inside: avoid; }
th { background: #111827; color: #fff; text-align: left; font-weight: 700; padding: 7px 8px; border: 1px solid #111827; }
td { padding: 7px 8px; border: 1px solid #d1d5db; vertical-align: top; }
tr:nth-child(even) td { background: #f9fafb; }
.cover-note { font-size: 9pt; color: #6b7280; margin-bottom: 12px; }
strong { font-weight: 700; }
.doc-meta { margin: 0 0 16px; padding: 10px 12px; border: 1px solid #d1d5db; background: #f9fafb; font-size: 9.5pt; }
'''

def inline(s):
    s = html.escape(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', s)
    return s

def parse_table(lines, i):
    header = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    rows = []
    i += 2
    while i < len(lines) and lines[i].strip().startswith('|') and '|' in lines[i].strip()[1:]:
        rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
        i += 1
    out = ['<table><thead><tr>']
    out += [f'<th>{inline(c)}</th>' for c in header]
    out += ['</tr></thead><tbody>']
    for row in rows:
        out.append('<tr>')
        row = row + [''] * (len(header) - len(row))
        out += [f'<td>{inline(c)}</td>' for c in row[:len(header)]]
        out.append('</tr>')
    out.append('</tbody></table>')
    return ''.join(out), i

def md_to_html(md):
    lines = md.splitlines()
    out=[]; i=0
    in_ul=False; in_ol=False; in_block=False
    def close_lists():
        nonlocal in_ul,in_ol
        if in_ul: out.append('</ul>'); in_ul=False
        if in_ol: out.append('</ol>'); in_ol=False
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()
        if not stripped:
            close_lists(); i+=1; continue
        if stripped.startswith('```'):
            close_lists(); code=[]; i+=1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code.append(lines[i]); i+=1
            i+=1
            out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>')
            continue
        if stripped.startswith('|') and i+1 < len(lines) and re.match(r'^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$', lines[i+1]):
            close_lists(); table, i = parse_table(lines, i); out.append(table); continue
        if stripped == '---':
            close_lists(); out.append('<hr>'); i+=1; continue
        m = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if m:
            close_lists(); level=len(m.group(1)); out.append(f'<h{level}>{inline(m.group(2))}</h{level}>'); i+=1; continue
        if stripped.startswith('>'):
            close_lists(); quote=[]
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote.append(lines[i].strip()[1:].strip()); i+=1
            out.append('<blockquote>' + ''.join(f'<p>{inline(q)}</p>' for q in quote if q) + '</blockquote>')
            continue
        if re.match(r'^[-*]\s+', stripped):
            if not in_ul: close_lists(); out.append('<ul>'); in_ul=True
            out.append('<li>'+inline(re.sub(r'^[-*]\s+','',stripped))+'</li>'); i+=1; continue
        if re.match(r'^\d+\.\s+', stripped):
            if not in_ol: close_lists(); out.append('<ol>'); in_ol=True
            out.append('<li>'+inline(re.sub(r'^\d+\.\s+','',stripped))+'</li>'); i+=1; continue
        close_lists()
        para=[stripped]; i+=1
        while i < len(lines):
            nxt=lines[i].strip()
            if not nxt or nxt.startswith(('#','>','```','|','---')) or re.match(r'^[-*]\s+',nxt) or re.match(r'^\d+\.\s+',nxt): break
            para.append(nxt); i+=1
        out.append('<p>'+inline(' '.join(para))+'</p>')
    close_lists()
    return '\n'.join(out)

for md_path in FILES:
    md = md_path.read_text(encoding='utf-8')
    title = next((line.strip('# ').strip() for line in md.splitlines() if line.startswith('# ')), md_path.stem)
    body = md_to_html(md)
    html_doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><meta name="author" content="1APP Technologies Inc."><style>{CSS}</style></head><body><div class="doc-meta"><strong>Draft document.</strong> Lawyer review recommended before use. Generated for 1APP Technologies Inc.</div>{body}</body></html>'''
    html_path = md_path.with_suffix('.html')
    pdf_path = md_path.with_suffix('.pdf')
    html_path.write_text(html_doc, encoding='utf-8')
    subprocess.check_call(['weasyprint', str(html_path), str(pdf_path)])
    print(pdf_path)

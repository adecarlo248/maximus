import textwrap

text = [
    "1APP — 60-Second Pitch",
    "AI automation for trades and service businesses — built to stop missed calls and book more jobs.",
    "",
    "Quick question: if someone calls your business and you miss it, does anything automatically follow up — or does it depend on someone calling back later?",
    "",
    "At 1APP we stop missed calls from becoming lost jobs. We install and manage one simple business app that does missed-call text-backs, a 24/7 AI voice receptionist that qualifies and books, online booking and confirmations, multi-step SMS/email follow-up, appointment reminders, review requests, two-way messaging, CRM & pipeline tracking, and easy invoicing/payments — so your crew shows up to booked work instead of chasing leads.",
    "",
    "We work with trades and local service businesses and offer Starter, Growth, and Revenue Engine plans plus add-ons like website builds, social management, ads, and custom automations. Book a free 15-minute audit — we'll show three places you're leaking leads and the first fix to get more booked jobs.",
    "",
    "use1app.com • adecarlo@use1app.com • Free 15-minute audit"
]

# wrap paragraphs
wrapped_lines = []
for para in text:
    if para == "":
        wrapped_lines.append("")
        continue
    lines = textwrap.wrap(para, width=90)
    wrapped_lines.extend(lines)

# escape parentheses and backslashes for PDF
def pdf_escape(s):
    return s.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

lines_escaped = [pdf_escape(l) for l in wrapped_lines]

# start y position and leading
y_start = 720
leading = 16

# build content stream using absolute text matrix (Tm) for each line
content = []
content.append('BT')
content.append('/F1 12 Tf')
for i, ln in enumerate(lines_escaped):
    y = y_start - i * leading
    content.append('1 0 0 1 72 %d Tm' % y)
    content.append('(%s) Tj' % ln)
content.append('ET')
content_stream = '\n'.join(content) + '\n'

# Build PDF objects
objects = []
objects.append('1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n')
objects.append('2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n')
objects.append('3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>\nendobj\n')
objects.append('4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n')
stream_bytes = content_stream.encode('utf-8')
objects.append('5 0 obj\n<< /Length %d >>\nstream\n%s\nendstream\nendobj\n' % (len(stream_bytes), content_stream))

# assemble PDF
pdf = bytearray()
pdf.extend(b'%PDF-1.4\n')
offsets = []
for o in objects:
    off = len(pdf)
    offsets.append(off)
    pdf.extend(o.encode('utf-8'))

xref_offset = len(pdf)
pdf.extend(('xref\n0 %d\n' % (len(objects)+1)).encode('utf-8'))
pdf.extend(b'0000000000 65535 f \n')
for off in offsets:
    pdf.extend(('%010d 00000 n \n' % off).encode('utf-8'))

pdf.extend(('trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%EOF\n' % (len(objects)+1, xref_offset)).encode('utf-8'))

out = '1app/1app-elevator-pitch.pdf'
with open(out, 'wb') as f:
    f.write(pdf)
print('WROTE', out)

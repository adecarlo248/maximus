# Minimal PDF generator — no external libs
text = [
    "1APP — 60-Second Pitch",
    "AI automation for trades & service businesses - built to stop missed calls and book more jobs.",
    "",
    "Quick question: if someone calls your business and you miss it, does anything automatically follow up - or does it depend on someone calling back later?",
    "",
    "At 1APP we stop missed calls from becoming lost jobs. We install and manage one simple business app that does missed-call text-backs, a 24/7 AI voice receptionist that qualifies and books, online booking and confirmations, multi-step SMS/email follow-up, appointment reminders, review requests, two-way messaging, CRM & pipeline tracking, and easy invoicing/payments - so your crew shows up to booked work instead of chasing leads.",
    "",
    "We work with trades and local service businesses and offer Starter, Growth, and Revenue Engine plans plus add-ons like website builds, social management, ads, and custom automations. Book a free 15-minute audit - we'll show three places you're leaking leads and the first fix to get more booked jobs.",
    "",
    "use1app.com   adecarlo@use1app.com  ",
]

# Prepare content stream with simple line breaks and text showing using PDF text operators
lines = []
for ln in text:
    # escape parentheses
    s = ln.replace('(', '\(').replace(')', '\)')
    lines.append('(' + s + ') Tj')
    lines.append('0 -18 Td')

content_stream = 'BT /F1 12 Tf 72 720 Td\n'
content_stream += '\n'.join(lines)
content_stream += '\nET\n'

# Build PDF objects
obj = []
obj.append('%PDF-1.4\n')
# We'll fill objects later and compute offsets
objects = []
objects.append(('1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n'))
objects.append(('2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n'))
objects.append(('3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>\nendobj\n'))
objects.append(('4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n'))
# content stream length
stream_bytes = content_stream.encode('utf-8')
stream_obj = '5 0 obj\n<< /Length %d >>\nstream\n%s\nendstream\nendobj\n' % (len(stream_bytes), content_stream)
objects.append(stream_obj)

# Now assemble and compute xref
pdf_bytes = b''
pdf_bytes += obj[0].encode('utf-8')
offsets = []
for o in objects:
    offsets.append(len(pdf_bytes))
    pdf_bytes += o.encode('utf-8')

# xref
xref_offset = len(pdf_bytes)
pdf_bytes += b'xref\n0 %d\n' % (len(objects)+1)
# entry for object 0
pdf_bytes += b'0000000000 65535 f \n'
for off in offsets:
    pdf_bytes += b'%010d 00000 n \n' % off

# trailer
pdf_bytes += b'trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%EOF\n' % (len(objects)+1, xref_offset)

# write file
out = '1app/1app-elevator-pitch.pdf'
with open(out, 'wb') as f:
    f.write(pdf_bytes)
print('WROTE', out)

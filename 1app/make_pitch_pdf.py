from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

output = "1app-elevator-pitch.pdf"
text_lines = [
    "1APP — 60-Second Pitch",
    "AI automation for trades & service businesses — built to stop missed calls and book more jobs.",
    "",
    "Quick question: if someone calls your business and you miss it, does anything automatically follow up — or does it depend on someone calling back later?",
    "",
    "At 1APP we stop missed calls from becoming lost jobs. We install and manage one simple business app that does missed-call text-backs, a 24/7 AI voice receptionist that qualifies and books, online booking and confirmations, multi-step SMS/email follow-up, appointment reminders, review requests, two-way messaging, CRM & pipeline tracking, and easy invoicing/payments — so your crew shows up to booked work instead of chasing leads.",
    "",
    "We work with trades and local service businesses and offer Starter, Growth, and Revenue Engine plans plus add-ons like website builds, social management, ads, and custom automations. Book a free 15-minute audit — we’ll show three places you’re leaking leads and the first fix to get more booked jobs.",
    "",
    "use1app.com • adecarlo@use1app.com • Free 15-minute audit"
]

c = canvas.Canvas(output, pagesize=letter)
width, height = letter

# Header
c.setFont("Helvetica-Bold", 18)
c.drawString(72, height-72, text_lines[0])

c.setFont("Helvetica", 11)
c.drawString(72, height-92, text_lines[1])

# Body
c.setFont("Helvetica", 12)
y = height-130
for line in text_lines[3:]:
    # wrap long lines
    from reportlab.lib.utils import simpleSplit
    wrapped = simpleSplit(line, 'Helvetica', 12, width-144)
    for w in wrapped:
        c.drawString(72, y, w)
        y -= 16
    y -= 6

# Footer
c.setFont("Helvetica-Bold", 10)
c.drawString(72, 72, text_lines[-1])

c.showPage()
c.save()
print("WROTE", output)

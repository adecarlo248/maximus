from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import qrcode, zipfile, textwrap, math, os

BASE = Path('/home/maximus/.openclaw/workspace')
OUT = BASE / '1app' / 'email-ad-posters'
OUT.mkdir(parents=True, exist_ok=True)
TRIAL_URL = 'https://api.leadconnectorhq.com/widget/form/vQ2UQ5FjwScLQQJ4DSIG'
LOGO_PATH = BASE / 'use1app.com' / 'logo.png'

W, H = 1080, 1350

FONT_DIRS = [Path('/usr/share/fonts/truetype/dejavu'), Path('/usr/share/fonts/truetype/liberation2')]
def font(name, size):
    candidates = [
        f'DejaVuSans{name}.ttf',
        f'LiberationSans{name}.ttf',
    ]
    for d in FONT_DIRS:
        for c in candidates:
            p = d / c
            if p.exists():
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()

F_BLACK = font('-Bold', 76)
F_BOLD = font('-Bold', 50)
F_SEMI = font('-Bold', 36)
F_BODY = font('', 34)
F_SMALL = font('', 25)
F_TINY = font('', 20)

POSTERS = [
    {
        'file': '1APP-email-ad-01-missed-calls.png',
        'eyebrow': 'LOCAL BUSINESS OWNERS',
        'headline': 'MISSED CALLS ARE COSTING YOU MONEY.',
        'sub': 'If they call and nobody answers, they are probably calling your competitor next.',
        'bullets': ['Missed call text-back', 'Online booking', 'Fast lead follow-up'],
    },
    {
        'file': '1APP-email-ad-02-customer-gone.png',
        'eyebrow': 'SPEED WINS CUSTOMERS',
        'headline': 'YOUR NEXT CUSTOMER MIGHT ALREADY BE GONE.',
        'sub': 'Slow replies kill good leads. 1APP helps you respond, book, and follow up faster.',
        'bullets': ['Capture every lead', 'Book appointments online', 'Send reminders automatically'],
    },
    {
        'file': '1APP-email-ad-03-one-lead.png',
        'eyebrow': 'SIMPLE MATH',
        'headline': 'ONE MISSED LEAD CAN PAY FOR THE SYSTEM.',
        'sub': 'A single forgotten call, quote request, or follow-up can cost more than the tool that prevents it.',
        'bullets': ['Lead tracking', 'Automated follow-up', 'Review requests'],
    },
    {
        'file': '1APP-email-ad-04-competitor.png',
        'eyebrow': 'BLUNT TRUTH',
        'headline': 'YOUR COMPETITOR ANSWERS FASTER.',
        'sub': 'The business that responds first usually has the best shot at winning the customer.',
        'bullets': ['Instant missed-call SMS', 'Conversations in one place', 'No more messy follow-up'],
    },
    {
        'file': '1APP-email-ad-05-stop-leaks.png',
        'eyebrow': 'STOP THE LEAK',
        'headline': 'STOP LETTING GOOD LEADS DISAPPEAR.',
        'sub': '1APP helps local businesses capture, book, remind, follow up, and request reviews automatically.',
        'bullets': ['More leads answered', 'More appointments booked', 'Less money leaking out'],
    },
]

def rounded_rectangle(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def make_gradient():
    hf = OUT / 'higgsfield-1app-saas-ad-background.png'
    if hf.exists():
        src = Image.open(hf).convert('RGB')
        # cover-crop to poster size
        scale = max(W / src.width, H / src.height)
        src = src.resize((int(src.width * scale), int(src.height * scale)), Image.LANCZOS)
        left = (src.width - W) // 2
        top = (src.height - H) // 2
        im = src.crop((left, top, left + W, top + H))
        tint = Image.new('RGB', (W, H), '#06142b')
        im = Image.blend(im, tint, 0.42)
        return im
    im = Image.new('RGB', (W, H), '#07162d')
    pix = im.load()
    for y in range(H):
        for x in range(W):
            nx, ny = x / W, y / H
            r = int(5 + 8*nx + 12*(1-ny))
            g = int(20 + 25*nx + 30*(1-ny))
            b = int(55 + 70*nx + 35*(1-ny))
            d = math.sqrt((nx-0.88)**2 + (ny-0.82)**2)
            glow = max(0, 1 - d/0.55)
            r += int(12*glow); g += int(82*glow); b += int(150*glow)
            pix[x,y] = (min(r,255), min(g,255), min(b,255))
    return im

def wrap_text(draw, text, fnt, max_width):
    words = text.split()
    lines, cur = [], ''
    for word in words:
        test = (cur + ' ' + word).strip()
        if draw.textbbox((0,0), test, font=fnt)[2] <= max_width:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = word
    if cur: lines.append(cur)
    return lines

def draw_centered(draw, lines, y, fnt, fill, spacing=8):
    for line in lines:
        bbox = draw.textbbox((0,0), line, font=fnt)
        x = (W - (bbox[2]-bbox[0]))/2
        draw.text((x,y), line, font=fnt, fill=fill)
        y += (bbox[3]-bbox[1]) + spacing
    return y

def add_logo(im):
    logo = Image.open(LOGO_PATH).convert('RGBA')
    # crop transparent whitespace
    bbox = logo.getbbox()
    if bbox: logo = logo.crop(bbox)
    target_w = 255
    ratio = target_w / logo.width
    logo = logo.resize((target_w, int(logo.height*ratio)), Image.LANCZOS)
    im.alpha_composite(logo, ((W-logo.width)//2, 46))

def make_qr():
    qr = qrcode.QRCode(version=2, box_size=10, border=2)
    qr.add_data(TRIAL_URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color='#06142b', back_color='white').convert('RGBA')
    return img.resize((150,150), Image.NEAREST)

def create_poster(p):
    bg = make_gradient().convert('RGBA')
    # subtle glass cards / app shapes
    overlay = Image.new('RGBA', (W,H), (0,0,0,0))
    d = ImageDraw.Draw(overlay)
    for i, box in enumerate([(720,240,1030,560),(40,880,360,1190),(725,780,1025,1040)]):
        rounded_rectangle(d, box, 34, (255,255,255,18), (255,255,255,35), 2)
        for j in range(4):
            y = box[1] + 55 + j*58
            rounded_rectangle(d, (box[0]+34,y,box[2]-34,y+24), 12, (52,211,255,40))
    overlay = overlay.filter(ImageFilter.GaussianBlur(0.4))
    bg.alpha_composite(overlay)

    draw = ImageDraw.Draw(bg)
    add_logo(bg)

    # eyebrow pill
    eb = p['eyebrow']
    ebbox = draw.textbbox((0,0), eb, font=F_SMALL)
    pill_w = ebbox[2]-ebbox[0]+46
    rounded_rectangle(draw, ((W-pill_w)//2, 205, (W+pill_w)//2, 251), 23, (30, 198, 255, 235))
    draw.text(((W-(ebbox[2]-ebbox[0]))//2, 214), eb, font=F_SMALL, fill='#06142b')

    # main panel
    rounded_rectangle(draw, (70, 300, W-70, 900), 42, (255,255,255,238))
    h_lines = wrap_text(draw, p['headline'], F_BLACK, W-190)
    y = draw_centered(draw, h_lines, 350, F_BLACK, '#06142b', 10)

    sub_lines = wrap_text(draw, p['sub'], F_BODY, W-230)
    y = draw_centered(draw, sub_lines, y+26, F_BODY, '#26344f', 8)

    # bullets
    y += 22
    for b in p['bullets']:
        x = 185
        draw.ellipse((x, y+8, x+18, y+26), fill='#16c8ff')
        draw.text((x+38, y), b, font=F_SEMI, fill='#06142b')
        y += 54

    # CTA button
    rounded_rectangle(draw, (145, 950, W-145, 1048), 49, (20, 200, 255, 255))
    cta = 'START YOUR 30-DAY FREE TRIAL'
    cb = draw.textbbox((0,0), cta, font=F_BOLD)
    draw.text(((W-(cb[2]-cb[0]))//2, 976), cta, font=F_BOLD, fill='#06142b')

    # QR and link
    qr = make_qr()
    rounded_rectangle(draw, (92, 1100, 282, 1290), 22, (255,255,255,245))
    bg.alpha_composite(qr, (112,1120))
    draw.text((320, 1114), 'Scan or click the image in email', font=F_SEMI, fill='white')
    link_lines = wrap_text(draw, TRIAL_URL, F_TINY, 680)
    yy = 1165
    for line in link_lines:
        draw.text((320, yy), line, font=F_TINY, fill='#d8f6ff')
        yy += 26
    footer_lines = wrap_text(draw, '1APP: capture leads, book appointments, follow up automatically.', F_TINY, 680)
    yy = 1230
    for line in footer_lines[:2]:
        draw.text((320, yy), line, font=F_TINY, fill='#ffffff')
        yy += 25

    out = OUT / p['file']
    bg.convert('RGB').save(out, quality=95)
    return out

paths = [create_poster(p) for p in POSTERS]

# Create clickable HTML snippets for associates
html = ['<!DOCTYPE html><html><head><meta charset="utf-8"><title>1APP Clickable Email Ad Posters</title></head><body style="font-family:Arial,sans-serif;">']
html.append('<h1>1APP Clickable Email Ad Posters</h1>')
html.append(f'<p>Free trial link: <a href="{TRIAL_URL}">{TRIAL_URL}</a></p>')
for p, path in zip(POSTERS, paths):
    html.append(f'<h2>{p["headline"]}</h2>')
    html.append('<p>Copy/paste this into an HTML email block if supported:</p>')
    rel = path.name
    snippet = f'<a href="{TRIAL_URL}" target="_blank"><img src="{rel}" alt="{p["headline"]} Start your 30-day free trial" style="width:100%;max-width:540px;height:auto;border:0;display:block;"></a>'
    html.append('<pre style="white-space:pre-wrap;background:#f3f4f6;padding:12px;border:1px solid #ddd;">'+snippet.replace('<','&lt;').replace('>','&gt;')+'</pre>')
    html.append(snippet)
html.append('</body></html>')
(OUT / '1APP-clickable-email-poster-snippets.html').write_text('\n'.join(html), encoding='utf-8')

# PDF contact sheet via HTML + WeasyPrint for reliable rendering
contact_html = OUT / '1APP-email-ad-posters-pack.html'
pdf_path = OUT / '1APP-email-ad-posters-pack.pdf'
contact = ['<!DOCTYPE html><html><head><meta charset="utf-8"><title>1APP Email Ad Posters Pack</title><style>@page{size:Letter;margin:.35in}body{margin:0;font-family:Arial,sans-serif}.page{page-break-after:always;text-align:center}img{max-height:10in;max-width:7.5in}</style></head><body>']
for p in paths:
    contact.append(f'<div class="page"><img src="{p.name}" alt="1APP Email Ad Poster"></div>')
contact.append('</body></html>')
contact_html.write_text('\n'.join(contact), encoding='utf-8')
os.system(f'cd "{OUT}" && weasyprint "{contact_html.name}" "{pdf_path.name}"')

zip_path = OUT / '1APP-email-ad-posters-pack.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in paths:
        z.write(p, p.name)
    z.write(OUT / '1APP-clickable-email-poster-snippets.html', '1APP-clickable-email-poster-snippets.html')
    z.write(contact_html, contact_html.name)
    hf_bg = OUT / 'higgsfield-1app-saas-ad-background.png'
    if hf_bg.exists():
        z.write(hf_bg, hf_bg.name)
    if pdf_path.exists():
        z.write(pdf_path, pdf_path.name)

print('Created:')
for p in paths: print(p)
print(pdf_path)
print(zip_path)

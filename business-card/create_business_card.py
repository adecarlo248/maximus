from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os
import qrcode

OUT = 'business-card/output'
ASSETS = 'business-card/assets'
os.makedirs(OUT, exist_ok=True)

# Standard US business card with bleed at 300 DPI
DPI = 300
W, H = int(3.5*DPI), int(2.0*DPI)          # 1050 x 600 trim
WB, HB = int(3.75*DPI), int(2.25*DPI)       # 1125 x 675 bleed
SCALE = 2  # draw large then downsample for cleaner edges

BLUE = (0, 170, 255)
BLUE2 = (0, 118, 204)
DARK = (8, 12, 20)
DARK2 = (13, 18, 32)
TEXT = (232, 240, 248)
MUTED = (153, 170, 190)
WHITE = (255,255,255)

booking = 'https://api.leadconnectorhq.com/widget/bookings/tony-decarlo-free-demo'
phone = '+1 (705) 243-7767'
website = 'tonysbusinesssolutions.ca'
name = 'Tony DeCarlo'
company = "TONY'S BUSINESS SOLUTIONS"
tagline = 'Follow-Up Systems for Trades & Service Businesses'
cta = 'SCAN TO BOOK A FREE DEMO'

font_paths = {
    'regular': '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    'bold': '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    'condensed': '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    'mono': '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
}

def font(size, kind='regular'):
    return ImageFont.truetype(font_paths[kind], size*SCALE)

def canvas():
    w,h = WB*SCALE, HB*SCALE
    img = Image.new('RGB', (w,h), DARK)
    px = img.load()
    for y in range(h):
        for x in range(w):
            gx = x / w
            gy = y / h
            glow1 = max(0, 1 - math.sqrt((gx-0.12)**2 + (gy-0.18)**2)/0.75)
            glow2 = max(0, 1 - math.sqrt((gx-0.95)**2 + (gy-0.85)**2)/0.65)
            r = int(7 + 3*gy + 0*glow1)
            g = int(11 + 9*gx + 55*glow1 + 25*glow2)
            b = int(20 + 22*gy + 95*glow1 + 105*glow2)
            px[x,y] = (min(255,r), min(255,g), min(255,b))
    return img

def add_neon_lines(img):
    d = ImageDraw.Draw(img, 'RGBA')
    w,h = img.size
    # diagonal neon accents
    for off, alpha, width in [(0,70,7),(18,42,4),(38,26,2)]:
        d.line([(int(w*0.63)+off, -20), (w+50+off, int(h*0.58))], fill=(0,170,255,alpha), width=width*SCALE)
    for off, alpha, width in [(0,58,5),(20,35,3)]:
        d.line([(-60, int(h*0.9)+off), (int(w*0.38), h+50+off)], fill=(0,170,255,alpha), width=width*SCALE)
    # subtle grid dots
    for x in range(70*SCALE, w, 42*SCALE):
        for y in range(45*SCALE, h, 42*SCALE):
            if (x+y)//(42*SCALE) % 3 == 0:
                d.ellipse([x-1*SCALE,y-1*SCALE,x+1*SCALE,y+1*SCALE], fill=(0,170,255,22))
    return img

def paste_logo(img, center, size, glow=True):
    logo = Image.open(os.path.join(ASSETS, 'logo.png')).convert('RGBA')
    logo.thumbnail((size*SCALE, size*SCALE), Image.LANCZOS)
    if glow:
        alpha = logo.split()[-1]
        glow_img = Image.new('RGBA', img.size, (0,0,0,0))
        pos = (int(center[0]*SCALE-logo.width/2), int(center[1]*SCALE-logo.height/2))
        glow_img.paste((0,170,255,120), pos, alpha)
        glow_img = glow_img.filter(ImageFilter.GaussianBlur(18*SCALE))
        img.alpha_composite(glow_img)
    pos = (int(center[0]*SCALE-logo.width/2), int(center[1]*SCALE-logo.height/2))
    img.alpha_composite(logo, pos)

def text_center(d, xy, txt, fnt, fill, spacing=0):
    bbox = d.textbbox((0,0), txt, font=fnt)
    x = xy[0]*SCALE - (bbox[2]-bbox[0])/2
    y = xy[1]*SCALE - (bbox[3]-bbox[1])/2
    d.text((x,y), txt, font=fnt, fill=fill, spacing=spacing)

def rounded_rect(d, xy, radius, fill, outline=None, width=1):
    xy = tuple(int(v*SCALE) for v in xy)
    d.rounded_rectangle(xy, radius=int(radius*SCALE), fill=fill, outline=outline, width=max(1,int(width*SCALE)))

def crop_trim(img):
    left = int((WB-W)/2*SCALE)
    top = int((HB-H)/2*SCALE)
    return img.crop((left, top, left+W*SCALE, top+H*SCALE)).resize((W,H), Image.LANCZOS)

def down_bleed(img):
    return img.resize((WB,HB), Image.LANCZOS)

# FRONT
front = canvas().convert('RGBA')
add_neon_lines(front)
d = ImageDraw.Draw(front, 'RGBA')
# Large mark
paste_logo(front, (562, 208), 315, True)
# dark glass panel around company name
rounded_rect(d, (92, 398, 1033, 578), 26, (6,10,18,150), (0,170,255,85), 1.2)
text_center(d, (562, 434), company, font(34, 'condensed'), TEXT)
text_center(d, (562, 482), tagline, font(19, 'regular'), (185,205,225))
text_center(d, (562, 535), phone, font(28, 'bold'), BLUE)

# BACK
back = canvas().convert('RGBA')
add_neon_lines(back)
d = ImageDraw.Draw(back, 'RGBA')
# left logo ghost
paste_logo(back, (180, 156), 165, True)
# name/card info
rounded_rect(d, (70, 265, 598, 560), 26, (6,10,18,155), (0,170,255,85), 1.2)
d.text((100*SCALE, 295*SCALE), name, font=font(35,'bold'), fill=TEXT)
d.text((102*SCALE, 346*SCALE), 'Founder', font=font(18,'regular'), fill=(156,178,200))
# contact rows
contact_y = 401
for icon, line in [('CALL/TEXT', phone), ('WEB', website)]:
    d.text((102*SCALE, contact_y*SCALE), icon, font=font(13,'bold'), fill=BLUE)
    d.text((215*SCALE, (contact_y-4)*SCALE), line, font=font(22,'regular'), fill=WHITE)
    contact_y += 48
# promise
d.text((102*SCALE, 512*SCALE), 'Less chasing. Faster replies. More booked conversations.', font=font(15,'regular'), fill=(174,194,214))

# QR panel
qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=12, border=3)
qr.add_data(booking)
qr.make(fit=True)
qr_img = qr.make_image(fill_color=(8,12,20), back_color='white').convert('RGB')
qr_img = qr_img.resize((238*SCALE,238*SCALE), Image.NEAREST)
# white QR card
rounded_rect(d, (755, 112, 1042, 458), 30, (255,255,255,248), (0,170,255,125), 2)
back.alpha_composite(qr_img.convert('RGBA'), (780*SCALE, 142*SCALE))
text_center(d, (899, 507), cta, font(18,'bold'), BLUE)
text_center(d, (899, 540), 'tonysbusinesssolutions.ca', font(14,'regular'), (170,190,210))

# Export trim PNGs and bleed PNGs
front_trim = crop_trim(front)
back_trim = crop_trim(back)
front_bleed = down_bleed(front)
back_bleed = down_bleed(back)

front_trim.save(os.path.join(OUT,'tony_business_card_front_3.5x2.png'), dpi=(DPI,DPI))
back_trim.save(os.path.join(OUT,'tony_business_card_back_3.5x2.png'), dpi=(DPI,DPI))
front_bleed.save(os.path.join(OUT,'tony_business_card_front_bleed_3.75x2.25.png'), dpi=(DPI,DPI))
back_bleed.save(os.path.join(OUT,'tony_business_card_back_bleed_3.75x2.25.png'), dpi=(DPI,DPI))

# Multi-page PDF, trim size (good for Avery upload/print preview)
front_rgb = front_trim.convert('RGB')
back_rgb = back_trim.convert('RGB')
pdf_path = os.path.join(OUT,'tony_business_card_avery_front_back.pdf')
front_rgb.save(pdf_path, 'PDF', resolution=DPI, save_all=True, append_images=[back_rgb])

# Combined preview
preview = Image.new('RGB', (W*2+80, H+80), (20,24,32))
preview.paste(front_trim, (30,40))
preview.paste(back_trim, (W+50,40))
preview.save(os.path.join(OUT,'tony_business_card_preview.png'), dpi=(DPI,DPI))
print('Generated files in', OUT)
for fn in sorted(os.listdir(OUT)):
    print(fn, os.path.getsize(os.path.join(OUT,fn)))

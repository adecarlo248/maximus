from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, subprocess, os, shutil

W, H = 1080, 1920
FPS = 30
DURATION = 15
FRAMES = FPS * DURATION
OUT_DIR = Path('/home/maximus/.openclaw/workspace/tntoperators/reels/zero-risk-frames')
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = Path('/home/maximus/.openclaw/workspace/tntoperators/reels/tntoperators-zero-risk-instagram-reel.mp4')
LOGO = Path('/home/maximus/.openclaw/workspace/tntoperators/tnt-operators-logo-v2.png')

# Brand colors pulled from TNT Operators site
BG = (4, 16, 29)
BG2 = (7, 19, 33)
BLUE = (69, 199, 255)
BLUE2 = (29, 143, 255)
TEXT = (236, 248, 255)
MUTED = (150, 172, 192)
GREEN = (94, 242, 180)

FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'

bold = ImageFont.truetype(FONT_BOLD, 76)
bold_big = ImageFont.truetype(FONT_BOLD, 94)
bold_huge = ImageFont.truetype(FONT_BOLD, 116)
reg = ImageFont.truetype(FONT_REG, 44)
small = ImageFont.truetype(FONT_REG, 34)
small_bold = ImageFont.truetype(FONT_BOLD, 38)
mono = ImageFont.truetype(FONT_MONO, 56)

logo = Image.open(LOGO).convert('RGBA')
logo.thumbnail((520, 140), Image.LANCZOS)


def ease(x):
    x = max(0, min(1, x))
    return 1 - (1 - x) ** 3


def alpha_for(t, start, end, fade=0.28):
    if t < start or t > end:
        return 0
    if t < start + fade:
        return ease((t - start) / fade)
    if t > end - fade:
        return ease((end - t) / fade)
    return 1


def lerp(a, b, x):
    return a + (b - a) * x


def draw_center(draw, text, y, font, fill=TEXT, stroke=0, stroke_fill=(0,0,0), spacing=8):
    lines = text.split('\n')
    total_h = 0
    sizes = []
    for line in lines:
        box = draw.textbbox((0,0), line, font=font, stroke_width=stroke)
        w, h = box[2]-box[0], box[3]-box[1]
        sizes.append((w,h,line))
        total_h += h + spacing
    total_h -= spacing
    yy = y - total_h/2
    for w,h,line in sizes:
        draw.text(((W-w)/2, yy), line, font=font, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
        yy += h + spacing


def rounded_box(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def text_card(base, text, sub, y, a, accent=BLUE):
    overlay = Image.new('RGBA', (W,H), (0,0,0,0))
    d = ImageDraw.Draw(overlay)
    box = (86, y-170, W-86, y+210)
    rounded_box(d, box, 34, (8, 22, 40, int(220*a)), (accent[0], accent[1], accent[2], int(95*a)), 2)
    # top gleam
    d.line((box[0]+32, box[1]+2, box[2]-32, box[1]+2), fill=(255,255,255,int(45*a)), width=2)
    draw_center(d, text, y-28, bold_big, fill=(TEXT[0],TEXT[1],TEXT[2],int(255*a)), stroke=2, stroke_fill=(0,0,0,int(120*a)))
    draw_center(d, sub, y+102, reg, fill=(MUTED[0],MUTED[1],MUTED[2],int(255*a)))
    base.alpha_composite(overlay)


# Pre-render static vertical gradient once. Doing this per-pixel per-frame is painfully slow.
grad = Image.new('RGB', (1, H), BG)
gd0 = ImageDraw.Draw(grad)
for y in range(H):
    m = y / H
    gd0.point((0, y), fill=(int(lerp(BG[0], BG2[0], m)), int(lerp(BG[1], BG2[1], m)), int(lerp(BG[2], BG2[2], m))))
GRADIENT = grad.resize((W, H)).convert('RGBA')


def background(frame):
    t = frame / FPS
    img = GRADIENT.copy()
    d = ImageDraw.Draw(img)
    # grid
    grid_offset = int((t*18) % 86)
    for x in range(-86+grid_offset, W, 86):
        d.line((x,0,x,H), fill=(123,211,255,16), width=1)
    for y in range(-86+grid_offset, H, 86):
        d.line((0,y,W,y), fill=(123,211,255,14), width=1)
    # animated glows
    glow = Image.new('RGBA', (W,H), (0,0,0,0))
    gd = ImageDraw.Draw(glow)
    cx1 = int(150 + 55*math.sin(t*0.75))
    cy1 = int(260 + 65*math.cos(t*0.55))
    cx2 = int(920 + 70*math.sin(t*0.48+1.2))
    cy2 = int(1080 + 90*math.cos(t*0.42))
    gd.ellipse((cx1-370,cy1-370,cx1+370,cy1+370), fill=(29,143,255,58))
    gd.ellipse((cx2-430,cy2-430,cx2+430,cy2+430), fill=(69,199,255,45))
    glow = glow.filter(ImageFilter.GaussianBlur(82))
    img.alpha_composite(glow)
    return img


def draw_brand(img, a=1):
    overlay = Image.new('RGBA', (W,H), (0,0,0,0))
    od = ImageDraw.Draw(overlay)
    rounded_box(od, (52,54, W-52, 210), 28, (5, 16, 29, int(190*a)), (123,211,255,int(70*a)), 2)
    lg = logo.copy()
    # alpha logo
    if a < 1:
        al = lg.getchannel('A').point(lambda p: int(p*a))
        lg.putalpha(al)
    overlay.alpha_composite(lg, ((W-lg.width)//2, 82))
    img.alpha_composite(overlay)


def draw_pill(draw, x, y, txt, a, fill, w=390):
    rounded_box(draw, (x, y, x+w, y+82), 24, (8, 22, 40, int(230*a)), (fill[0],fill[1],fill[2],int(135*a)), 2)
    draw.text((x+32, y+20), txt, font=small_bold, fill=(TEXT[0],TEXT[1],TEXT[2],int(255*a)))


def frame_image(i):
    t = i / FPS
    img = background(i)
    draw_brand(img, 1)
    overlay = Image.new('RGBA', (W,H), (0,0,0,0))
    d = ImageDraw.Draw(overlay)

    # tiny category label
    d.text((82, 248), 'CREATOR BUSINESS BACKEND', font=small_bold, fill=(BLUE[0], BLUE[1], BLUE[2], 210))

    a = alpha_for(t, 0.0, 3.0)
    if a:
        y = int(640 - 40*(1-ease(min(1,t/0.45))))
        draw_center(d, 'CREATORS:', y-86, bold, fill=(BLUE[0],BLUE[1],BLUE[2],int(255*a)), stroke=2, stroke_fill=(0,0,0,int(120*a)))
        draw_center(d, "YOUR AUDIENCE\nISN'T THE BUSINESS", y+60, bold_huge, fill=(TEXT[0],TEXT[1],TEXT[2],int(255*a)), stroke=3, stroke_fill=(0,0,0,int(150*a)))

    a = alpha_for(t, 2.8, 5.7)
    if a:
        text_card(img, 'IT’S THE ASSET.', 'The money is in the backend.', 770, a, BLUE)

    a = alpha_for(t, 5.4, 9.3)
    if a:
        draw_center(d, 'WHAT WE BUILD', 525, bold_big, fill=(TEXT[0],TEXT[1],TEXT[2],int(255*a)), stroke=2, stroke_fill=(0,0,0,int(110*a)))
        items = [('OFFER', 315, 690), ('STOREFRONT', 315, 810), ('FUNNEL', 315, 930), ('FULFILLMENT', 315, 1050)]
        for idx, (txt,x,y) in enumerate(items):
            local = alpha_for(t, 5.65+idx*0.35, 9.3, fade=0.18) * a
            if local:
                draw_pill(d, x, y, '✓  ' + txt, local, GREEN, w=450)

    a = alpha_for(t, 9.0, 12.0)
    if a:
        draw_center(d, 'YOU STAY\nTHE FACE.', 645, bold_huge, fill=(TEXT[0],TEXT[1],TEXT[2],int(255*a)), stroke=3, stroke_fill=(0,0,0,int(150*a)))
        draw_center(d, 'WE BUILD THE MACHINE.', 940, bold_big, fill=(BLUE[0],BLUE[1],BLUE[2],int(255*a)), stroke=2, stroke_fill=(0,0,0,int(130*a)))

    a = alpha_for(t, 11.7, 15.0, fade=0.32)
    if a:
        # DM card
        rounded_box(d, (78, 520, W-78, 1260), 44, (6, 18, 33, int(232*a)), (BLUE[0],BLUE[1],BLUE[2],int(125*a)), 3)
        d.text((138, 592), 'READY TO MONETIZE?', font=small_bold, fill=(MUTED[0],MUTED[1],MUTED[2],int(255*a)))
        draw_center(d, "DM ME", 745, bold_huge, fill=(TEXT[0],TEXT[1],TEXT[2],int(255*a)), stroke=3, stroke_fill=(0,0,0,int(150*a)))
        # zero risk tag
        rounded_box(d, (172, 842, W-172, 990), 30, (69,199,255,int(32*a)), (GREEN[0],GREEN[1],GREEN[2],int(170*a)), 3)
        draw_center(d, "“ZERO RISK”", 900, mono, fill=(GREEN[0],GREEN[1],GREEN[2],int(255*a)), stroke=2, stroke_fill=(0,0,0,int(125*a)))
        draw_center(d, 'and I’ll show you the backend\nI’d build for your audience.', 1112, reg, fill=(TEXT[0],TEXT[1],TEXT[2],int(245*a)))
        draw_center(d, 'tntoperators.com', 1488, small_bold, fill=(BLUE[0],BLUE[1],BLUE[2],int(255*a)))

    # bottom safety/positioning line on every frame
    d.text((82, H-120), 'TNT OPERATORS', font=small_bold, fill=(TEXT[0],TEXT[1],TEXT[2],180))
    tw = d.textlength('creator-led business infrastructure', font=small)
    d.text((W-82-tw, H-114), 'creator-led business infrastructure', font=small, fill=(MUTED[0],MUTED[1],MUTED[2],165))

    img.alpha_composite(overlay)
    return img.convert('RGB')

# clear old frames
for p in OUT_DIR.glob('frame_*.png'):
    p.unlink()

for i in range(FRAMES):
    frame_image(i).save(OUT_DIR / f'frame_{i:04d}.png', quality=95)

ffmpeg = shutil.which('ffmpeg')
if not ffmpeg:
    try:
        import imageio_ffmpeg
        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        raise RuntimeError('ffmpeg not found')

cmd = [
    ffmpeg, '-y',
    '-framerate', str(FPS),
    '-i', str(OUT_DIR / 'frame_%04d.png'),
    '-f', 'lavfi', '-i', f'anullsrc=channel_layout=stereo:sample_rate=44100',
    '-shortest',
    '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
    '-preset', 'medium', '-crf', '20',
    '-c:a', 'aac', '-b:a', '128k',
    '-movflags', '+faststart',
    str(OUT)
]
subprocess.run(cmd, check=True)
print(OUT)

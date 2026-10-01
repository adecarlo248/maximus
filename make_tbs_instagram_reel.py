from moviepy import VideoFileClip, CompositeVideoClip, ImageClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import numpy as np

W, H = 1080, 1920
BLUE = (0, 170, 255, 255)
BLUE_DARK = (0, 95, 180, 255)
WHITE = (255, 255, 255, 255)
NAVY = (5, 10, 20, 210)
SOFT = (210, 230, 245, 255)

MEDIA = Path('/home/maximus/.openclaw/media/inbound')
OUT_DIR = Path('/home/maximus/.openclaw/workspace/output')
OUT_DIR.mkdir(exist_ok=True)
OUT = OUT_DIR / 'tonys-business-solutions-instagram-reel.mp4'

clips_info = [
    (MEDIA/'53b52bd8-e098-4470-8763-46621fb8770b.mp4', 'LOCAL BUSINESS OWNERS', 'Leads slipping through the cracks?'),
    (MEDIA/'42b0dd3c-cc9b-48a6-856d-1e4a2f0955a9.mp4', 'I CAN HELP WITH THAT', 'Simple AI follow-up systems that answer faster.'),
    (MEDIA/'812708f7-17a1-4295-8ed2-1a52a15be780.mp4', 'BOOK A FREE DEMO', 'tonysbusinesssolutions.ca'),
]

font_paths = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
]
font_bold = font_paths[0]
font_regular = font_paths[1]

def font(size, bold=True):
    return ImageFont.truetype(font_bold if bold else font_regular, size)

def fit_text(draw, text, max_width, start_size, min_size=28):
    size = start_size
    while size >= min_size:
        f = font(size)
        bbox = draw.textbbox((0, 0), text, font=f)
        if bbox[2] - bbox[0] <= max_width:
            return f
        size -= 2
    return font(min_size)

def rounded_rect(draw, xy, r, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

def make_overlay(duration, headline, subline, index):
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-260, -240, 560, 520), fill=(0, 170, 255, 56))
    gd.ellipse((650, 1260, 1320, 2050), fill=(0, 119, 204, 48))
    glow = glow.filter(ImageFilter.GaussianBlur(45))
    img.alpha_composite(glow)
    d = ImageDraw.Draw(img)

    # Subtle top brand chip
    rounded_rect(d, (54, 54, W-54, 142), 34, NAVY, outline=(0, 170, 255, 90), width=2)
    d.text((86, 76), "TONY'S BUSINESS SOLUTIONS", font=font(34), fill=WHITE)

    # Main caption card
    if index == 1:
        y1, y2 = 1320, 1545
        h_size = 68
    else:
        y1, y2 = 1360, 1565
        h_size = 58
    rounded_rect(d, (58, y1, W-58, y2), 40, (5, 10, 20, 226), outline=(0, 170, 255, 130), width=3)

    hf = fit_text(d, headline, W-170, h_size)
    sf = fit_text(d, subline, W-170, 34, min_size=24)
    hb = d.textbbox((0, 0), headline, font=hf)
    sb = d.textbbox((0, 0), subline, font=sf)
    hx = (W - (hb[2]-hb[0])) // 2
    sx = (W - (sb[2]-sb[0])) // 2
    d.text((hx+3, y1+45+3), headline, font=hf, fill=(0, 0, 0, 120))
    d.text((hx, y1+45), headline, font=hf, fill=WHITE)
    d.text((sx, y1+130), subline, font=sf, fill=SOFT)

    # Bottom website chip
    rounded_rect(d, (120, H-126, W-120, H-64), 28, (5, 10, 20, 205), outline=(0, 170, 255, 95), width=2)
    footer = 'tonysbusinesssolutions.ca'
    ff = font(30)
    fb = d.textbbox((0, 0), footer, font=ff)
    d.text(((W-(fb[2]-fb[0]))//2, H-111), footer, font=ff, fill=(235,245,255,240))

    return ImageClip(np.array(img)).with_duration(duration)

def prepare_clip(path, headline, subline, index):
    clip = VideoFileClip(str(path))
    # exact 9:16 upscale
    clip = clip.resized((W, H)).with_fps(30)
    overlay = make_overlay(clip.duration, headline, subline, index)
    comp = CompositeVideoClip([clip, overlay], size=(W, H)).with_duration(clip.duration)
    if clip.audio:
        comp = comp.with_audio(clip.audio)
    return comp

final_clips = [prepare_clip(*info, idx) for idx, info in enumerate(clips_info)]
final = concatenate_videoclips(final_clips, method='compose')
final.write_videofile(str(OUT), fps=30, codec='libx264', audio_codec='aac', preset='medium', bitrate='6500k', threads=4)

for c in final_clips:
    c.close()
final.close()
print(OUT)

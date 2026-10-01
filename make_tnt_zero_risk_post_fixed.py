from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont

FF = '/home/maximus/.openclaw/workspace/.venv-video-edit/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
clips = [
    '/home/maximus/.openclaw/media/inbound/cd4438ed-58d8-484d-9c57-0fae97594e5d.mp4',
    '/home/maximus/.openclaw/media/inbound/63109e92-08e7-4e38-9925-43ccae21632b.mp4',
    '/home/maximus/.openclaw/media/inbound/38af93a0-fb87-4fad-994b-5faa4d3dc3eb.mp4',
    '/home/maximus/.openclaw/media/inbound/3313dfe2-c147-4490-ae72-702204cc4d6f.mp4',
    '/home/maximus/.openclaw/media/inbound/21704b3c-9d8c-41b3-936c-b531363fa7d5.mp4',
]
out = '/home/maximus/.openclaw/workspace/tntoperators/reels/tntoperators-dm-zero-risk-instagram-post-fixed.mp4'
overlay_path = '/home/maximus/.openclaw/workspace/tntoperators/reels/tnt-zero-risk-overlay.png'
Path(out).parent.mkdir(parents=True, exist_ok=True)

W,H = 1080,1920
img = Image.new('RGBA',(W,H),(0,0,0,0))
d = ImageDraw.Draw(img)
fb = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',66)
fr = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',37)
fb2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',42)
fr2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',34)
d.rectangle((0,0,W,300), fill=(0,0,0,105))
d.rectangle((0,1600,W,1920), fill=(0,0,0,95))

def center(text,y,font,fill,stroke=3):
    box=d.textbbox((0,0),text,font=font,stroke_width=stroke)
    x=(W-(box[2]-box[0]))/2
    d.text((x,y),text,font=font,fill=fill,stroke_width=stroke,stroke_fill=(0,0,0,210))
center('DM ME ZERO RISK', 92, fb, (255,255,255,255), 4)
center('I only make money when you do.', 178, fr, (94,242,180,255), 3)
d.text((58,1740),'TNT OPERATORS',font=fb2,fill=(255,255,255,235),stroke_width=3,stroke_fill=(0,0,0,200))
d.text((58,1800),'You stay the face. We build the machine.',font=fr2,fill=(69,199,255,245),stroke_width=3,stroke_fill=(0,0,0,200))
img.save(overlay_path)

cmd = [FF, '-y', '-hide_banner']
for p in clips:
    cmd += ['-i', p]
for _ in clips:
    cmd += ['-loop', '1', '-i', overlay_path]

filters=[]
join=[]
for i in range(len(clips)):
    ov = len(clips)+i
    filters.append(
        f'[{i}:v]fps=30,setsar=1,split=2[bg{i}][fg{i}];'
        f'[bg{i}]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,'
        f'boxblur=luma_radius=28:luma_power=2,eq=brightness=-0.17:saturation=1.12[bb{i}];'
        f'[fg{i}]scale=1080:1920:force_original_aspect_ratio=decrease[ff{i}];'
        f'[{ov}:v]scale=1080:1920,format=rgba[ov{i}];'
        f'[bb{i}][ff{i}]overlay=(W-w)/2:(H-h)/2[mid{i}];'
        f'[mid{i}][ov{i}]overlay=0:0:shortest=1,format=yuv420p[v{i}]'
    )
    filters.append(f'[{i}:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,aresample=44100,asetpts=PTS-STARTPTS,volume=1.16[a{i}]')
    join.append(f'[v{i}][a{i}]')
filters.append(''.join(join) + f'concat=n={len(clips)}:v=1:a=1[vout][aout]')

cmd += ['-filter_complex',';'.join(filters),'-map','[vout]','-map','[aout]',
        '-c:v','libx264','-profile:v','high','-pix_fmt','yuv420p','-preset','medium','-crf','20',
        '-c:a','aac','-b:a','160k','-movflags','+faststart',out]
subprocess.run(cmd, check=True)
print(out)

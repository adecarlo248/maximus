from pathlib import Path
import subprocess, shlex, imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base = Path('/home/maximus/.openclaw/media/inbound')
out_dir = Path('/home/maximus/.openclaw/workspace/tntoperators/reels')
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / 'tntoperators-first-instagram-reel.mp4'

clips = [
    ('f038daf4-91e2-47be-adf3-52b6605adda2.mp4', "Most creators don't have a content problem."),
    ('23618c9a-a4c1-41c6-b82d-06347f337ed7.mp4', 'Content is the front door.'),
    ('9ceb96e4-091d-4b89-83a3-24a528fefcf8.mp4', 'Content is not the business.'),
    ('54c77224-cae0-44a0-888b-714df8b1b548.mp4', 'The real money is in the backend.'),
    ('62afabd0-a6a5-400f-a17d-7a380741318d.mp4', "Posting and praying isn't a strategy."),
    ('c8f0729b-8861-432d-b9af-73967f83da13.mp4', 'Offer. Product. Sales system. Storefront. Follow-up. Fulfillment.'),
    ('d5cad7cb-eeba-4bb9-bc2a-d1003078c902.mp4', "That's where TNT Operators comes in."),
    ('52c14a39-f0b0-40a8-8400-f45a2ae4ba8b.mp4', 'We build the business behind the brand.'),
    ('a02ce113-c5d0-44fc-9a07-a8686a428872.mp4', 'You stay the face. We build the machine.'),
    ('36e06e28-cad3-4485-9f6d-2f160c9b5e82.mp4', 'Serious creators: apply at tntoperators.com'),
]

font_bold = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
font_regular = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'

def esc(s):
    return s.replace('\\','\\\\').replace(':','\\:').replace("'", "\\'").replace(',', '\\,')

def wrap_text(text, max_chars=24):
    words = text.split()
    lines=[]; cur=''
    for w in words:
        if len((cur+' '+w).strip()) <= max_chars:
            cur=(cur+' '+w).strip()
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return '\\n'.join(lines[:3])

cmd = [ffmpeg, '-y']
for fn, _ in clips:
    cmd += ['-i', str(base / fn)]

filters=[]
concat_inputs=[]
for i,(fn,cap) in enumerate(clips):
    caption = esc(wrap_text(cap, 24))
    # Build a 9:16 vertical video, preserve audio, add subtle dark gradient and bold captions.
    vf = (
        f'[{i}:v]'
        'scale=1080:1920:force_original_aspect_ratio=increase,'
        'crop=1080:1920,setsar=1,fps=30,'
        'eq=contrast=1.06:saturation=1.08,'
        "drawbox=x=0:y=0:w=iw:h=270:color=black@0.30:t=fill,"
        "drawbox=x=0:y=1420:w=iw:h=360:color=black@0.38:t=fill,"
        f"drawtext=fontfile='{font_bold}':text='TNT OPERATORS':x=60:y=70:fontsize=46:fontcolor=white:borderw=3:bordercolor=black@0.65,"
        f"drawtext=fontfile='{font_regular}':text='CREATOR BUSINESS BACKEND':x=60:y=125:fontsize=27:fontcolor=0x43BEFF:borderw=2:bordercolor=black@0.55,"
        f"drawtext=fontfile='{font_bold}':text='{caption}':x=(w-text_w)/2:y=1480:fontsize=61:fontcolor=white:borderw=5:bordercolor=black@0.85:line_spacing=12,"
        f"drawtext=fontfile='{font_bold}':text='tntoperators.com':x=(w-text_w)/2:y=1810:fontsize=38:fontcolor=0x43BEFF:borderw=3:bordercolor=black@0.75"
        f'[v{i}]'
    )
    af = f'[{i}:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,aresample=44100,volume=1.15[a{i}]'
    filters.append(vf)
    filters.append(af)
    concat_inputs.append(f'[v{i}][a{i}]')

filters.append(''.join(concat_inputs) + f'concat=n={len(clips)}:v=1:a=1[v][a]')
filter_complex = ';'.join(filters)
cmd += ['-filter_complex', filter_complex, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-preset', 'medium', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', str(out)]
print('Running ffmpeg...')
subprocess.run(cmd, check=True)
print(out)

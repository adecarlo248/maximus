from pathlib import Path
import subprocess, imageio_ffmpeg
ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
base=Path('/home/maximus/.openclaw/media/inbound')
out_dir=Path('/home/maximus/.openclaw/workspace/tntoperators/reels'); out_dir.mkdir(parents=True, exist_ok=True)
out=out_dir/'tntoperators-first-instagram-reel-review-with-intro.mp4'
clips=[
'6a46e65a-30d9-4ea9-9b53-53115e09810c.mp4',
'f038daf4-91e2-47be-adf3-52b6605adda2.mp4',
'23618c9a-a4c1-41c6-b82d-06347f337ed7.mp4',
'9ceb96e4-091d-4b89-83a3-24a528fefcf8.mp4',
'54c77224-cae0-44a0-888b-714df8b1b548.mp4',
'62afabd0-a6a5-400f-a17d-7a380741318d.mp4',
'c8f0729b-8861-432d-b9af-73967f83da13.mp4',
'd5cad7cb-eeba-4bb9-bc2a-d1003078c902.mp4',
'52c14a39-f0b0-40a8-8400-f45a2ae4ba8b.mp4',
'a02ce113-c5d0-44fc-9a07-a8686a428872.mp4',
'36e06e28-cad3-4485-9f6d-2f160c9b5e82.mp4',
]
for c in clips:
    if not (base/c).exists():
        raise FileNotFoundError(base/c)
cmd=[ffmpeg,'-y']
for c in clips: cmd += ['-i', str(base/c)]
filters=[]; join=[]
for i in range(len(clips)):
    filters.append(f'[{i}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,eq=contrast=1.04:saturation=1.06[v{i}]')
    filters.append(f'[{i}:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,aresample=44100,volume=1.12[a{i}]')
    join.append(f'[v{i}][a{i}]')
filters.append(''.join(join)+f'concat=n={len(clips)}:v=1:a=1[v][a]')
cmd += ['-filter_complex',';'.join(filters),'-map','[v]','-map','[a]','-c:v','libx264','-profile:v','high','-pix_fmt','yuv420p','-preset','medium','-crf','20','-c:a','aac','-b:a','160k','-movflags','+faststart',str(out)]
subprocess.run(cmd, check=True)
print(out)

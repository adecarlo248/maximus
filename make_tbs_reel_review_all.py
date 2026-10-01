from pathlib import Path
import subprocess, imageio_ffmpeg
ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
base=Path('/home/maximus/.openclaw/media/inbound')
out_dir=Path('/home/maximus/.openclaw/workspace/tonys-business-solutions/reels')
out_dir.mkdir(parents=True, exist_ok=True)
out=out_dir/'tonys-business-solutions-instagram-reel-review-all-clips.mp4'
clips=[
'8475b1c7-d6ef-4573-bf25-00f1d93abe82.mp4',
'26860ab0-7c43-485b-b33b-0a13f40f5d42.mp4',
'24f2e36c-c979-4fee-a66e-c6303fde88a2.mp4',
'b5562c27-64f0-4b6a-8981-5498fb1d8b86.mp4',
'ddc9678c-7a56-40d6-b2b7-6d99358f2a2f.mp4',
'7019565b-4800-42b2-a8a0-ce444ca5df1a.mp4',
'97e5e695-d712-4d60-869d-0615707a78b5.mp4',
'367290ae-2b00-4bec-90a9-f2f03a57b37c.mp4',
'0aeee61a-2289-4ccf-92ff-4f2a1f975d10.mp4',
]
missing=[str(base/c) for c in clips if not (base/c).exists()]
if missing: raise FileNotFoundError(missing)
cmd=[ffmpeg,'-y']
for c in clips: cmd += ['-i', str(base/c)]
filters=[]; join=[]
for i in range(len(clips)):
    filters.append(f'[{i}:v]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,setsar=1,fps=30,eq=contrast=1.04:saturation=1.06[v{i}]')
    filters.append(f'[{i}:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,aresample=44100,volume=1.12[a{i}]')
    join.append(f'[v{i}][a{i}]')
filters.append(''.join(join)+f'concat=n={len(clips)}:v=1:a=1[v][a]')
cmd += ['-filter_complex',';'.join(filters),'-map','[v]','-map','[a]','-c:v','libx264','-profile:v','high','-pix_fmt','yuv420p','-preset','medium','-crf','29','-maxrate','2200k','-bufsize','4400k','-c:a','aac','-b:a','128k','-movflags','+faststart',str(out)]
subprocess.run(cmd, check=True)
print(out)

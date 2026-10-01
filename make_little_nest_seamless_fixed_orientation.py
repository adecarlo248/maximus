from pathlib import Path
import subprocess

FF = '/home/maximus/.openclaw/workspace/.venv-video-edit/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
# Tony confirmed previous output was sideways. Use the opposite orientation pass.
clips = [
    ('/home/maximus/.openclaw/media/inbound/09323bdf-c328-4b2e-88e7-28489c698955.mp4', 'transpose=1,'),
    ('/home/maximus/.openclaw/media/inbound/66c02505-0d21-4c3a-8afd-290791d1d912.mp4', 'transpose=1,'),
    ('/home/maximus/.openclaw/media/inbound/2f8c7192-1dca-4a17-915b-b65e24a96bcc.mp4', 'transpose=1,'),
    ('/home/maximus/.openclaw/media/inbound/b14a856d-bdf8-4351-9a19-9e189186ebf6.mp4', 'transpose=1,'),
]
out = '/home/maximus/.openclaw/workspace/output/little-nest-naturals-seamless-fixed-orientation.mp4'
Path(out).parent.mkdir(parents=True, exist_ok=True)

cmd = [FF, '-y', '-hide_banner']
for c, _ in clips:
    cmd += ['-noautorotate', '-i', c]

filters = []
join = []
for i, (_, rotate) in enumerate(clips):
    filters.append(
        f'[{i}:v]{rotate}fps=30,setsar=1,'
        'scale=1080:1920:force_original_aspect_ratio=increase,'
        'crop=1080:1920,setsar=1,'
        'eq=contrast=1.04:saturation=1.06:brightness=0.01,'
        'format=yuv420p,setpts=PTS-STARTPTS'
        f'[v{i}]'
    )
    filters.append(
        f'[{i}:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo,'
        'aresample=44100,highpass=f=80,lowpass=f=12000,'
        'acompressor=threshold=-18dB:ratio=2.2:attack=8:release=120:makeup=1.5,'
        'dynaudnorm=f=150:g=7:p=0.9,'
        'asetpts=PTS-STARTPTS'
        f'[a{i}]'
    )
    join.append(f'[v{i}][a{i}]')
filters.append(''.join(join) + f'concat=n={len(clips)}:v=1:a=1[vcat][acat]')
filters.append('[vcat]fade=t=in:st=0:d=0.18,fade=t=out:st=35.95:d=0.35[vout]')
filters.append('[acat]afade=t=in:st=0:d=0.12,afade=t=out:st=35.95:d=0.35[aout]')

cmd += [
    '-filter_complex', ';'.join(filters),
    '-map', '[vout]', '-map', '[aout]',
    '-r', '30',
    '-metadata:s:v:0', 'rotate=0',
    '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
    '-preset', 'medium', '-crf', '20',
    '-c:a', 'aac', '-b:a', '160k',
    '-movflags', '+faststart', out
]
subprocess.run(cmd, check=True)
print(out)

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math, random

W=H=1080
OUT=Path('/home/maximus/.openclaw/workspace/output/tnt-operators-instagram-income-graphic-v2.png')
OUT.parent.mkdir(exist_ok=True)
FONT_BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_REG='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

def font(size,bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)

def bbox(draw,text,fnt,stroke=0):
    return draw.textbbox((0,0),text,font=fnt,stroke_width=stroke)

def center_x(draw,text,fnt,stroke=0):
    b=bbox(draw,text,fnt,stroke); return (W-(b[2]-b[0]))//2

def draw_center(draw,y,text,fnt,fill,stroke_width=0,stroke_fill=None):
    draw.text((center_x(draw,text,fnt,stroke_width),y),text,font=fnt,fill=fill,stroke_width=stroke_width,stroke_fill=stroke_fill)

def rr(draw,xy,r,fill,outline=None,width=1):
    draw.rounded_rectangle(xy,radius=r,fill=fill,outline=outline,width=width)

def shadow_layer(shape_fn, blur=18, alpha=135):
    layer=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(layer,'RGBA'); shape_fn(d,alpha); return layer.filter(ImageFilter.GaussianBlur(blur))

# Premium background
img=Image.new('RGB',(W,H),(3,7,18)); pix=img.load()
for y in range(H):
    for x in range(W):
        nx=x/W; ny=y/H
        glowA=max(0,1-math.sqrt((nx-0.78)**2+(ny-0.28)**2)*2.0)
        glowB=max(0,1-math.sqrt((nx-0.25)**2+(ny-0.86)**2)*1.7)
        glowC=max(0,1-math.sqrt((nx-0.50)**2+(ny-0.50)**2)*2.5)
        r=int(3+2*glowA+5*glowB)
        g=int(7+45*glowA+22*glowB+8*glowC)
        b=int(18+125*glowA+72*glowB+28*glowC)
        pix[x,y]=(r,g,b)
img=img.convert('RGBA')
draw=ImageDraw.Draw(img,'RGBA')

# Subtle texture + diagonal lines
random.seed(7)
for _ in range(900):
    x=random.randrange(W); y=random.randrange(H); a=random.randrange(7,22)
    draw.point((x,y),fill=(255,255,255,a))
for x in range(-500,1300,96):
    draw.line((x,0,x+620,H),fill=(0,190,255,20),width=1)

# Header brand
rr(draw,(64,48,1016,122),26,(2,7,18,135),outline=(0,178,255,80),width=2)
draw.text((94,67),'TNT OPERATORS',font=font(34),fill=(233,250,255,255))
draw.text((775,73),'CREATOR BACKEND',font=font(20,False),fill=(120,222,255,235))

# Main typography left
x0=82
draw.text((x0,178),'WATCH ME',font=font(54),fill=(104,222,255,255))
draw.text((x0,252),'TURN YOUR',font=font(74),fill=(245,252,255,255))
draw.text((x0,342),'INSTAGRAM',font=font(82),fill=(245,252,255,255),stroke_width=2,stroke_fill=(0,136,255,120))
draw.text((x0,444),'INTO MONEY',font=font(76),fill=(0,218,255,255),stroke_width=2,stroke_fill=(255,255,255,70))
# Fun/professional small line
rr(draw,(84,552,502,606),24,(0,162,255,180),outline=(180,240,255,100),width=2)
draw.text((114,567),'WITHOUT THE GURU CRINGE',font=font(22),fill=(4,9,24,255))

# Visual phone/card on right
# glow burst
cx,cy=765,405
for r,a in [(260,28),(190,36),(125,50)]:
    draw.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(0,196,255,a),width=4)
for i in range(24):
    ang=2*math.pi*i/24
    draw.line((cx,cy,cx+math.cos(ang)*random.randint(90,260),cy+math.sin(ang)*random.randint(90,260)),fill=(0,205,255,42),width=3)

# phone shadow
img.alpha_composite(shadow_layer(lambda d,a: d.rounded_rectangle((650,205,966,646),radius=52,fill=(0,0,0,a)),20,155))
draw=ImageDraw.Draw(img,'RGBA')
rr(draw,(635,188,951,628),48,(9,15,33,255),outline=(88,219,255,185),width=4)
rr(draw,(661,225,925,592),30,(236,248,255,250))
# generic profile UI
rr(draw,(685,252,900,315),22,(11,26,50,255))
draw.ellipse((708,270,748,310),fill=(0,185,255,255))
draw.text((764,266),'Creator',font=font(24),fill=(242,252,255,255))
draw.text((764,293),'attention → offer',font=font(14,False),fill=(165,215,238,255))
# content blocks
for i,y in enumerate([342,424,506]):
    rr(draw,(686,y,900,y+54),14,(12,28,54,245),outline=(0,150,255,75),width=2)
    draw.rectangle((706,y+16,760,y+38),fill=(0,170+20*i,255,200))
    draw.rectangle((778,y+16,874,y+26),fill=(230,244,251,245))
    draw.rectangle((778,y+34,846,y+42),fill=(130,180,205,230))

# money stack bottom right
img.alpha_composite(shadow_layer(lambda d,a: d.rounded_rectangle((632,704,990,842),radius=34,fill=(0,0,0,a)),18,150))
draw=ImageDraw.Draw(img,'RGBA')
for j,(dx,dy) in enumerate([(0,42),(18,22),(36,0)]):
    rr(draw,(620+dx,710+dy,960+dx,800+dy),22,(0,164,255,235),outline=(203,247,255,120),width=3)
    draw.ellipse((742+dx,724+dy,826+dx,786+dy),fill=(220,249,255,225))
    draw.text((772+dx,736+dy),'$',font=font(36),fill=(2,22,45,255))
    draw.rectangle((645+dx,742+dy,710+dx,754+dy),fill=(220,249,255,190))
    draw.rectangle((862+dx,742+dy,930+dx,754+dy),fill=(220,249,255,190))

# arrow from phone to money
pts=[(790,628),(782,672),(735,704),(690,742)]
draw.line(pts,fill=(255,255,255,210),width=10,joint='curve')
draw.line(pts,fill=(0,220,255,230),width=5,joint='curve')
draw.polygon([(690,742),(700,710),(724,736)],fill=(0,220,255,245))

# bottom CTA panel
rr(draw,(78,870,1002,1008),34,(2,7,18,220),outline=(0,180,255,105),width=3)
draw.text((118,896),'You bring the audience.',font=font(36),fill=(236,249,255,255))
draw.text((118,942),'We build the offer + backend that pays.',font=font(36),fill=(0,212,255,255))
# website chip
rr(draw,(305,1020,775,1064),21,(0,162,255,205),outline=(255,255,255,80),width=1)
draw_center(draw,1029,'tntoperators.com',font(26),fill=(3,8,22,255))

img=img.convert('RGB')
img.save(OUT,quality=96)
print(OUT)

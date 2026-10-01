from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math, random

W=H=1080
OUT=Path('/home/maximus/.openclaw/workspace/output/tnt-operators-instagram-income-graphic.png')
OUT.parent.mkdir(exist_ok=True)
LOGO=Path('/home/maximus/.openclaw/workspace/tntoperators/tnt-operators-logo-v2.png')

FONT_BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_REG='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_OB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'

def font(size,bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)

def text_center(draw, y, text, fnt, fill, stroke_width=0, stroke_fill=None):
    box=draw.textbbox((0,0),text,font=fnt,stroke_width=stroke_width)
    x=(W-(box[2]-box[0]))//2
    draw.text((x,y),text,font=fnt,fill=fill,stroke_width=stroke_width,stroke_fill=stroke_fill)

def rounded_rect(draw, xy, r, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

# background gradient
img=Image.new('RGB',(W,H),(4,8,20))
pix=img.load()
for y in range(H):
    for x in range(W):
        nx=x/W; ny=y/H
        # dark navy with electric-blue glow from top-left and lower-right
        glow1=max(0,1-math.sqrt((nx-0.18)**2+(ny-0.2)**2)*2.0)
        glow2=max(0,1-math.sqrt((nx-0.82)**2+(ny-0.78)**2)*2.2)
        r=int(3 + 5*glow1 + 2*glow2)
        g=int(8 + 42*glow1 + 24*glow2)
        b=int(24 + 115*glow1 + 90*glow2)
        pix[x,y]=(r,g,b)

draw=ImageDraw.Draw(img,'RGBA')
# subtle grid
for x in range(-100,W+100,72):
    draw.line((x,0,x+280,H),fill=(0,170,255,20),width=1)
for y in range(0,H,72):
    draw.line((0,y,W,y),fill=(255,255,255,12),width=1)

# explosion/spark behind phone
cx,cy=540,520
for i in range(38):
    ang=2*math.pi*i/38
    length=random.randint(210,390)
    x2=cx+math.cos(ang)*length
    y2=cy+math.sin(ang)*length
    draw.line((cx,cy,x2,y2), fill=(0,187,255,55), width=random.randint(2,5))
for r,alpha in [(330,28),(250,42),(170,55)]:
    draw.ellipse((cx-r,cy-r,cx+r,cy+r), outline=(0,180,255,alpha), width=3)

# money/growth icons
coin_fill=(17,196,255,210)
for (x,y,s) in [(155,405,48),(890,405,42),(190,720,38),(858,700,54),(795,245,34)]:
    draw.ellipse((x-s,y-s,x+s,y+s), fill=(0,160,255,42), outline=(115,226,255,185), width=3)
    f=font(int(s*1.05))
    tb=draw.textbbox((0,0),'$',font=f)
    draw.text((x-(tb[2]-tb[0])/2,y-(tb[3]-tb[1])/2-6),'$',font=f,fill=(235,251,255,230))

# growth arrow
pts=[(705,555),(780,490),(850,520),(928,405)]
draw.line(pts, fill=(0,220,255,230), width=16, joint='curve')
draw.polygon([(928,405),(902,414),(922,438)], fill=(0,220,255,230))

# phone mockup
shadow=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(shadow,'RGBA')
sd.rounded_rectangle((355,225,725,765), radius=54, fill=(0,0,0,170))
shadow=shadow.filter(ImageFilter.GaussianBlur(24)); img=Image.alpha_composite(img.convert('RGBA'),shadow)
draw=ImageDraw.Draw(img,'RGBA')
rounded_rect(draw,(345,210,715,750),54,(8,14,31,255),outline=(88,219,255,190),width=5)
rounded_rect(draw,(370,245,690,720),34,(238,248,255,245))
# phone content, generic social feed
rounded_rect(draw,(392,270,668,330),20,(13,31,60,255))
draw.ellipse((412,286,450,324),fill=(0,178,255,255))
draw.text((463,285),'Creator Page',font=font(22),fill=(240,250,255,255))
draw.text((463,309),'27.8K followers',font=font(15,False),fill=(176,218,245,255))
for i,y in enumerate([356,472,588]):
    rounded_rect(draw,(392,y,668,y+92),18,(12,24,45,250),outline=(0,150,255,80),width=2)
    draw.rectangle((410,y+18,485,y+74),fill=(0,150+20*i,255,180))
    draw.rectangle((500,y+22,645,y+34),fill=(225,239,250,240))
    draw.rectangle((500,y+46,625,y+56),fill=(160,190,210,220))
    draw.rectangle((500,y+64,595,y+74),fill=(0,190,255,220))
# income chip
rounded_rect(draw,(418,664,642,710),23,(0,178,255,240))
draw.text((446,674),'INCOME +',font=font(25),fill=(2,9,25,255))

# logo top — clean text mark for higher contrast
rounded_rect(draw,(338,42,742,122),26,(3,8,20,155),outline=(0,190,255,95),width=2)
text_center(draw,55,'TNT OPERATORS',font(42),fill=(225,248,255,255),stroke_width=1,stroke_fill=(0,130,255,130))
draw.text((393,98),'CREATOR MONETIZATION BACKEND',font=font(15,False),fill=(140,225,255,230))

# headline block
rounded_rect(draw,(76,790,W-76,982),34,(2,7,19,220),outline=(0,180,255,120),width=3)
text_center(draw,813,'WATCH ME TURN',font(43),fill=(195,236,255,255))
text_center(draw,865,'YOUR INSTAGRAM',font(58),fill=(255,255,255,255),stroke_width=2,stroke_fill=(0,120,255,125))
text_center(draw,934,'INTO INCOME',font(58),fill=(0,212,255,255),stroke_width=1,stroke_fill=(255,255,255,60))

# service line + CTA, roomy and readable
text_center(draw,1008,'Creator offers • Whop setup • Funnels • Fulfillment',font(25,False),fill=(225,245,255,240))
rounded_rect(draw,(348,1040,732,1072),16,(0,178,255,210),outline=(255,255,255,80),width=1)
text_center(draw,1044,"LET'S BUILD THE BACKEND",font(21),fill=(2,8,22,255))

# Fun small badge
rounded_rect(draw,(88,176,324,238),29,(0,178,255,210),outline=(255,255,255,100),width=2)
draw.text((118,193),'LIGHT THE FUSE',font=font(23),fill=(2,8,22,255))

img=img.convert('RGB')
img.save(OUT,quality=95)
print(OUT)

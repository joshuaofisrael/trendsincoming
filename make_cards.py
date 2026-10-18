# Generates original text-only share cards (1200x630 PNG) and a 512px logo. Run once: python3 make_cards.py
import os,re
from PIL import Image,ImageDraw,ImageFont
exec(re.search(r"^CATS=.*$",open("build.py").read(),re.M).group(0))
INK=(22,18,31);YEL=(255,214,10);PINK=(255,79,163);CYAN=(0,212,255);WHITE=(255,255,255)
F=lambda s:ImageFont.load_default(size=s)
def card(fn,label,sub,accent):
    im=Image.new("RGB",(1200,630),YEL);d=ImageDraw.Draw(im)
    d.rectangle([40,40,1160,590],fill=WHITE,outline=INK,width=8)
    d.rectangle([56,600,1176,606],fill=INK)
    d.rectangle([40,40,1160,150],fill=INK)
    d.polygon([(90,60),(130,60),(112,95),(140,95),(95,140),(108,104),(82,104)],fill=YEL)
    d.text((160,62),"TRENDS INCOMING",font=F(58),fill=YEL)
    d.rectangle([80,200,80+28,470],fill=accent)
    size=96 if len(label)<16 else (76 if len(label)<22 else 60)
    d.text((135,215),label,font=F(size),fill=INK)
    d.text((135,215+size+30),sub,font=F(40),fill=(70,70,80))
    d.text((80,505),"trendsincoming.com",font=F(40),fill=INK)
    d.text((760,505),"Your trend curator",font=F(40),fill=accent if accent!=YEL else INK)
    im.save(f"og/{fn}.png",optimize=True)
acc=[PINK,CYAN,(0,170,90),(130,80,255)]
card("default","What's trending now","Hand-picked US trends, explained",PINK)
for i,(c,n,e) in enumerate(CATS): card(c,n.replace("&","and"),"What's trending, and why it matters",acc[i%4])
lg=Image.new("RGB",(512,512),INK);d=ImageDraw.Draw(lg)
d.polygon([(220,60),(330,60),(280,200),(370,200),(200,450),(240,270),(150,270)],fill=YEL)
lg.save("og/logo.png",optimize=True)
print("ok")

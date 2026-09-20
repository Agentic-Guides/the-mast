"""Generate THE MAST / Agentic-Guides YouTube banner (2048x1152) + profile (1024) via Pillow (CPU)."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

FONT_BD = "C:/Windows/Fonts/arialbd.ttf"
FONT_IT = "C:/Windows/Fonts/impact.ttf"
os.makedirs("C:/Users/hohoh/Desktop/the-mast/assets", exist_ok=True)

def vgrad(x0, y0, x1, y1, c0, c1):
    img = Image.new("RGB", (1, 1))
    dr = ImageDraw.Draw(img)
    dr.line([(0,0),(1,0)], fill=(x1,y1), width=1)
    return None

def banner():
    W, H = 2048, 1152
    img = Image.new("RGB", (W, H), (10, 10, 15))
    dr = ImageDraw.Draw(img, "RGBA")
    # diagonal pink->purple glow gradient
    for i in range(H):
        t = i / H
        r = int(10 + (225 - 10) * (1 - t) * 0.6)
        g = int(10 + (29 - 10) * (1 - t) * 0.8)
        b = int(20 + (120 - 20) * t * 1.2)
        dr.line([(0,i),(W,i)], fill=(r, g, b, 40))
    # big soft glow behind center
    glow = Image.new("RGBA", (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(glow)
    cx, cy = W // 2, H // 2
    for r in range(400, 150, -12):
        a = int(90 * (1 - r/400))
        gd.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(236, 72, 153, a)// 8 if False else (200, 60, 200, a))
    img = Image.alpha_composite(img.convert("RGBA"), glow)
    dr = ImageDraw.Draw(img, "RGBA")
    # === Title ===
    f_title = ImageFont.truetype(FONT_IT, 220)
    txt = "THE MAST"
    bbox = dr.textbbox((0,0), txt, font=f_title)
    tw = bbox[2]-bbox[0]
    x = (W - tw)//2
    y = 210
    # glow shadow
    dr.text((x+6, y+6), txt, font=f_title, fill=(236, 72, 153, 140))
    dr.text((x, y), txt, font=f_title, fill=(236, 72, 153, 255))
    # === Tagline ===
    f_tag = ImageFont.truetype(FONT_BD, 64)
    tag = "Your past self sets the rules. Your future self can't break them."
    tb = dr.textbbox((0,0), tag, font=f_tag)
    x2 = (W - (tb[2]-tb[0]))//2
    dr.text((x2, y + 300), tag, font=f_tag, fill=(196, 201, 216, 255))
    # === Sub ===
    f_sub = ImageFont.truetype(FONT_BD, 48)
    sub = "Human approval for irreversible agent actions."
    sb = dr.textbbox((0,0), sub, font=f_sub)
    dr.text(((W-(sb[2]-sb[0]))//2, y + 460), sub, font=f_sub, fill=(167, 139, 250, 255))
    # === handle ===
    f_hn = ImageFont.truetype(FONT_BD, 40)
    hn = "@Agentic-Guides"
    hb = dr.textbbox((0,0), hn, font=f_hn)
    dr.text(((W-(hb[2]-hb[0]))//2, y + 600), hn, font=f_hn, fill=(90, 96, 128, 255))
    # === decorative mast line ===
    dr.line([(W//2-420, y+720),(W//2-420, H-180)], fill=(120, 40, 160, 220), width=8)
    dr.line([(W//2+420, y+720),(W//2+420, H-180)], fill=(120, 40, 160, 220), width=8)
    img.convert("RGB").save("C:/Users/hohoh/Desktop/the-mast/assets/youtube-banner.png")
    print("banner saved", img.size)

def profile():
    S = 1024
    img = Image.new("RGB", (S, S), (10, 10, 15))
    dr = ImageDraw.Draw(img, "RGBA")
    # radial-ish gradient
    for r in range(S//2, 0, -2):
        a = int(160 * (1 - r/(S//2)))
        dr.ellipse([S//2-r-2, S//2-r-2, S//2+r+2, S//2+r+2], fill=(236, 72, 153, a*0)// 255 if False else (236, 72, 153, a if r > S//3 else a//2))
    # concentric pink/purple
    for r in [S//2, int(S*0.42), int(S*0.28)]:
        dr.ellipse([S//2-r, S//2-r, S//2+r, S//2+r], outline=(236, 72, 153, 160), width=18)
    # central monogram "M" mast
    f = ImageFont.truetype(FONT_IT, S//2)
    txt = "M"
    bb = dr.textbbox((0,0), txt, font=f)
    tw, th = bb[2]-bb[0], bb[3]-bb[1]
    # subtle shadow
    dr.text((S//2-tw/2+8, S//2-th/2+8), txt, font=f, fill=(236,72,153,120))
    dr.text((S//2-tw/2, S//2-th/2), txt, font=f, fill=(255,255,255,235))
    # "AST" smaller below
    f2 = ImageFont.truetype(FONT_BD, S//9)
    t2 = "AGENTIC - GUIDES"
    # crop to circle (YouTube profile is circular)
    mask = Image.new("L", (S,S), 0)
    ImageDraw.Draw(mask).ellipse([0,0,S-1,S-1], fill=255)
    img.putalpha(mask)
    img.save("C:/Users/hohoh/Desktop/the-mast/assets/profile.png")
    print("profile saved", img.size)

banner(); profile()

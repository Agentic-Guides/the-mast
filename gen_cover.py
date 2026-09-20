"""THE MAST cover image for builder.aws blog post — 1200x675, minimal text."""
from PIL import Image, ImageDraw, ImageFont
import os
W, H = 1200, 675
OS = "C:/Users/hohoh/Desktop/the-mast/assets"
os.makedirs(OS, exist_ok=True)
img = Image.new("RGB", (W, H), (10, 10, 15))
dr = ImageDraw.Draw(img, "RGBA")
# diagonal glow
for i in range(H):
    t = i / H
    r = 40 + int(120 * (1 - t))
    g = 16 + int(22 * (1 - t))
    b = 34 + int(130 * t)
    dr.line([(0, i), (W, i)], fill=(r, g, b, 120))
# central glow
for rr in range(260, 120, -10):
    a = int(60 * (1 - rr/260))
    dr.ellipse([W//2-rr, H//2-rr, W//2+rr, H//2+rr], fill=(210, 60, 180, a))
# mast pillars (vertical bars, symbol of the mast)
mx, my = W//2, H//2
for dx in (-120, 120):
    dr.rectangle([mx+dx-9, my-170, mx+dx+9, my+170], fill=(120, 40, 160, 255))
# small "THE MAST" text (minimal, allowed as it's a wordmark, but keep tiny)
f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 40)
t = "THE MAST"
tb = dr.textbbox((0,0), t, font=f)
dr.text(((W-(tb[2]-tb[0]))//2, H-120), t, font=f, fill=(236, 72, 153, 255))
img.convert("RGB").save(OS + "/cover-1200x675.png")
print("cover saved", img.size, "round bytes", round(os.path.getsize(OS+"/cover-1200x675.png")/1024,1),"KB")

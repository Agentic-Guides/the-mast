"""THE MAST cover #2 — Ulysses/Odyssey theme, distinct from #1. 1200x675."""
from PIL import Image, ImageDraw, ImageFont
import os
W, H = 1200, 675
OS = "C:/Users/hohoh/Desktop/the-mast/assets"
os.makedirs(OS, exist_ok=True)
img = Image.new("RGB", (W, H), (8, 10, 22))          # deep navy, not #1's pink glow
dr = ImageDraw.Draw(img, "RGBA")
# horizontal ocean-line gradient (calm, epic)
for x in range(W):
    t = x / W
    r = 16 + int(20 * t)
    g = 22 + int(70 * (1 - t))
    b = 48 + int(60 * t)
    dr.line([(x, 0), (x, H)], fill=(r, g, b, 255))
# a vertical "mast" line (the metaphor) with a soft moon behind
cx, cy = W // 2, H // 2
# moon
dr.ellipse([cx-70, cy-150, cx+70, cy-10], fill=(230, 235, 245, 120))
# mast (tall line)
dr.line([(cx, cy-140), (cx, cy+210)], fill=(200, 205, 220, 230), width=6)
# horizon line
dr.line([(0, cy+60), (W, cy+60)], fill=(180, 190, 210, 120), width=2)
# small "ODYSSEY" tagline
f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 34)
t = "ODYSSEY · AGENT SAFETY"
tb = dr.textbbox((0,0), t, font=f)
dr.text(((W-(tb[2]-tb[0]))//2, H-90), t, font=f, fill=(220, 225, 240, 255))
img.convert("RGB").save(OS + "/cover-ulysses-1200x675.png")
print("cover2 saved", img.size, "bytes", round(os.path.getsize(OS+"/cover-ulysses-1200x675.png")/1024,1),"KB")

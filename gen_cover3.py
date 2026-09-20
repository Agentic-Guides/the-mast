"""THE MAST cover #3 — Good Neighbor/community theme, distinct from 1&2. 1200x675."""
from PIL import Image, ImageDraw, ImageFont
import os
W, H = 1200, 675
OS = "C:/Users/hohoh/Desktop/the-mast/assets"
os.makedirs(OS, exist_ok=True)
img = Image.new("RGB", (W, H), (18, 26, 20))   # warm dark green-teal, unlike navy/pink
dr = ImageDraw.Draw(img, "RGBA")
# soft warm glow from lower-left (community/support feel)
for i in range(H):
    t = i / H
    r = 26 + int(60 * (1-t))
    g = 34 + int(80 * (1-t))
    b = 22 + int(30 * (1-t))
    dr.line([(0, i), (W, i)], fill=(r, g, b, 255))
# three pillars / guardian figures (M-of-N quorum metaphor) — three vertical bars
cols = [0.32, 0.5, 0.68]
for c in cols:
    x = int(W * c)
    dr.rectangle([x-14, H//2-140, x+14, H//2+140], fill=(70, 150, 120, 230))
# connecting bar (they act together = quorum)
dr.rectangle([int(W*0.32)-14, H//2+40, int(W*0.68)+14, H//2+56], fill=(90, 180, 150, 200))
# tagline
f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 34)
t = "GOOD NEIGHBOR · GUARDIANS"
tb = dr.textbbox((0,0), t, font=f)
dr.text(((W-(tb[2]-tb[0]))//2, H-90), t, font=f, fill=(220, 240, 230, 255))
img.convert("RGB").save(OS + "/cover-neighbor-1200x675.png")
print("cover3 saved", img.size, "bytes", round(os.path.getsize(OS+"/cover-neighbor-1200x675.png")/1024,1),"KB")

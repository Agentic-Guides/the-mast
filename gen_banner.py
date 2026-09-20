"""THE MAST YouTube banner — mobile-safe: all text inside center safe band (1546x423)."""
from PIL import Image, ImageDraw, ImageFont
import os
os.makedirs("C:/Users/hohoh/Desktop/the-mast/assets", exist_ok=True)
W, H = 2048, 1152
IMG = "C:/Users/hohoh/Desktop/the-mast/assets/youtube-banner.png"
FONT_IT = "C:/Windows/Fonts/impact.ttf"
FONT_BD = "C:/Windows/Fonts/arialbd.ttf"

img = Image.new("RGB", (W, H), (10, 10, 15))
dr = ImageDraw.Draw(img, "RGBA")
# vertical pink->purple wash
for i in range(H):
    t = i / H
    r = 28 + int(96 * (1 - t))
    g = 12 + int(28 * (1 - t))
    b = 30 + int(120 * t)
    dr.line([(0, i), (W, i)], fill=(r, g, b, 60))
# central glow
gd = ImageDraw.Draw(img, "RGBA")
for rr in range(420, 240, -14):
    a = int(70 * (1 - rr/420))
    gd.ellipse([W//2-rr, H//2-rr, W//2+rr, H//2+rr], fill=(210, 60, 180, a))

# Everything lives near vertical center (safe band ~ y 380..790)
cy = H // 2
# Title
f = ImageFont.truetype(FONT_IT, 150)
t = "THE MAST"
tb = dr.textbbox((0,0), t, font=f)
tw = tb[2]-tb[0]
x = (W-tw)//2
y = cy - 150
dr.text((x+5, y+5), t, font=f, fill=(236, 72, 153, 160))
dr.text((x, y), t, font=f, fill=(236, 72, 153, 255))
# Tagline (1 line, shorter & brighter)
f2 = ImageFont.truetype(FONT_BD, 52)
tag = "Your past self sets the rules. Your future self can't break them."
tb2 = dr.textbbox((0,0), tag, font=f2)
dr.text(((W-(tb2[2]-tb2[0]))//2, y+190), tag, font=f2, fill=(226, 230, 243, 255))
# handle
f3 = ImageFont.truetype(FONT_BD, 42)
hn = "@Agentic-Guides"
tb3 = dr.textbbox((0,0), hn, font=f3)
dr.text(((W-(tb3[2]-tb3[0]))//2, y+320), hn, font=f3, fill=(192, 168, 250, 255))
img.convert("RGB").save(IMG)
print("banner regenerated", img.size)

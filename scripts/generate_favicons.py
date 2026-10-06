"""
generate_favicons.py
Generates raster icons (favicon-16x16.png, favicon-32x32.png, favicon.ico,
apple-touch-icon.png, android-chrome-192x192.png, android-chrome-512x512.png)
and a 1200x630 Open Graph / Twitter Card social share banner (images/og-share.png).
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

def draw_icon_master(size=1024):
    """Draw high-resolution 1024x1024 master icon for crisp downscaling."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Gradient background squircle
    margin = int(size * 0.04)
    radius = int(size * 0.22)
    box = [margin, margin, size - margin, size - margin]

    # Create background mask with rounded rectangle
    bg_mask = Image.new("L", (size, size), 0)
    bg_mask_draw = ImageDraw.Draw(bg_mask)
    bg_mask_draw.rounded_rectangle(box, radius=radius, fill=255)

    # Base gradient image
    bg_grad = Image.new("RGBA", (size, size))
    for y in range(size):
        ratio = y / size
        # From #112236 (17, 34, 54) to #080E14 (8, 14, 20)
        r = int(17 * (1 - ratio) + 8 * ratio)
        g = int(34 * (1 - ratio) + 14 * ratio)
        b = int(54 * (1 - ratio) + 20 * ratio)
        for x in range(size):
            bg_grad.putpixel((x, y), (r, g, b, 255))
    
    img.paste(bg_grad, (0, 0), bg_mask)

    # Border stroke
    stroke_w = max(2, int(size * 0.024))
    draw.rounded_rectangle(box, radius=radius, outline=(0, 168, 225, 120), width=stroke_w)

    # Stylized 'P'
    # Coordinates scaled to `size`
    s = size / 512.0
    p_color = (0, 168, 225, 255)
    p_glow = (56, 189, 248, 255)
    
    # Outer 'P' shape
    p_left = int(160 * s)
    p_top = int(110 * s)
    p_width = int(244 * s)
    p_stem_w = int(72 * s)
    p_loop_h = int(206 * s)
    p_bottom = int(412 * s)

    # Draw vertical stem
    draw.rounded_rectangle([p_left, p_top, p_left + p_stem_w, p_bottom], radius=int(16*s), fill=p_color)

    # Draw loop (outer arc + inner cutout)
    loop_box = [p_left, p_top, p_left + p_width, p_top + p_loop_h]
    draw.rounded_rectangle(loop_box, radius=int(70*s), fill=p_color)

    # Cutout of loop
    cutout_margin_x = int(72 * s)
    cutout_margin_y = int(68 * s)
    cutout_box = [p_left + cutout_margin_x, p_top + cutout_margin_y, p_left + p_width - int(58*s), p_top + p_loop_h - int(66*s)]
    draw.rounded_rectangle(cutout_box, radius=int(26*s), fill=(12, 23, 36, 255))

    # Prime Arc Smile (Amber)
    arc_box = [int(130 * s), int(260 * s), int(410 * s), int(440 * s)]
    arc_w = max(2, int(26 * s))
    draw.arc(arc_box, start=35, end=145, fill=(255, 153, 0, 255), width=arc_w)

    # Arrowhead at arc right tip
    tip_x = int(396 * s)
    tip_y = int(370 * s)
    arrow_pts = [
        (tip_x + int(12*s), tip_y - int(10*s)),
        (tip_x - int(24*s), tip_y - int(14*s)),
        (tip_x - int(4*s), tip_y + int(20*s))
    ]
    draw.polygon(arrow_pts, fill=(255, 153, 0, 255))

    # Sparkle / Star top-right
    cx, cy = int(392 * s), int(124 * s)
    r1, r2 = int(26 * s), int(9 * s)
    star_pts = []
    for i in range(8):
        angle = i * math.pi / 4
        rad = r1 if i % 2 == 0 else r2
        star_pts.append((cx + int(rad * math.cos(angle)), cy + int(rad * math.sin(angle))))
    draw.polygon(star_pts, fill=(255, 179, 64, 255))

    return img

def generate_all_icons():
    print("Generating master 1024x1024 icon...")
    master = draw_icon_master(1024)

    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "apple-touch-icon.png": 180,
        "android-chrome-192x192.png": 192,
        "android-chrome-512x512.png": 512,
    }

    for filename, dim in sizes.items():
        out_path = os.path.join(BASE_DIR, filename)
        resized = master.resize((dim, dim), Image.Resampling.LANCZOS)
        resized.save(out_path, format="PNG", optimize=True)
        print(f"Saved {filename} ({dim}x{dim})")

    # Generate multi-size favicon.ico
    ico_path = os.path.join(BASE_DIR, "favicon.ico")
    ico_sizes = [(16, 16), (32, 32), (48, 48)]
    ico_images = [master.resize(s, Image.Resampling.LANCZOS) for s in ico_sizes]
    ico_images[0].save(ico_path, format="ICO", sizes=ico_sizes)
    print(f"Saved multi-resolution favicon.ico ({ico_sizes})")

def generate_og_share_image():
    """Create 1200x630 high resolution social share card (og:image)."""
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), (10, 17, 24))
    draw = ImageDraw.Draw(img)

    # 1. Background gradient from #0A1118 to #112236
    for y in range(h):
        ratio = y / h
        r = int(10 * (1 - ratio) + 16 * ratio)
        g = int(17 * (1 - ratio) + 32 * ratio)
        b = int(24 * (1 - ratio) + 52 * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # 2. Glowing atmospheric radial bursts
    # Ambient Cyan glow on left
    glow_cyan = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_cyan)
    glow_draw.ellipse([(-100, -100), (500, 500)], fill=(0, 168, 225, 45))
    glow_draw.ellipse([(800, 200), (1400, 800)], fill=(255, 153, 0, 30))
    glow_cyan = glow_cyan.filter(ImageFilter.GaussianBlur(80))
    img.paste(glow_cyan, (0, 0), glow_cyan)

    # 3. Outer border accent
    draw.rectangle([16, 16, w - 16, h - 16], outline=(0, 168, 225, 90), width=2)
    draw.line([(16, 16), (200, 16)], fill=(0, 168, 225, 255), width=4)
    draw.line([(w - 200, h - 16), (w - 16, h - 16)], fill=(255, 153, 0, 255), width=4)

    # 4. Paste Icon on Left
    icon_master = draw_icon_master(512)
    icon_resized = icon_master.resize((210, 210), Image.Resampling.LANCZOS)
    img.paste(icon_resized, (90, 170), icon_resized)

    # 5. Badges & Text (Fallback to clean geometric shapes/fonts)
    try:
        font_brand = ImageFont.truetype("arialbd.ttf", 34)
        font_badge = ImageFont.truetype("arialbd.ttf", 20)
        font_title = ImageFont.truetype("arialbd.ttf", 54)
        font_sub = ImageFont.truetype("arial.ttf", 26)
        font_footer = ImageFont.truetype("arial.ttf", 22)
    except Exception:
        font_brand = ImageFont.load_default()
        font_badge = font_brand
        font_title = font_brand
        font_sub = font_brand
        font_footer = font_brand

    # Category Pill Badge (Top)
    badge_x = 340
    badge_y = 145
    draw.rounded_rectangle([badge_x, badge_y, badge_x + 380, badge_y + 38], radius=19, fill=(16, 31, 48), outline=(0, 168, 225, 180), width=2)
    draw.text((badge_x + 20, badge_y + 8), "★ OFFICIAL 2026 EDITION • 30-DAY TRIALS", font=font_badge, fill=(56, 189, 248))

    # Main Headline
    draw.text((340, 205), "Amazon Prime Perks", font=font_title, fill=(241, 245, 249))
    draw.text((340, 270), "& Special Offers Guide", font=font_title, fill=(0, 168, 225))

    # Sub-bullet summary
    draw.text((340, 360), "• 30-Day Free Trial Strategies & Break-Even Calculator", font=font_sub, fill=(148, 163, 184))
    draw.text((340, 405), "• 50% Off Young Adult (18-24) & Prime Access (EBT/Medicaid)", font=font_sub, fill=(148, 163, 184))
    draw.text((340, 450), "• Audible 30-Day Trial, Luna Cloud Gaming, & Kindle Unlimited", font=font_sub, fill=(148, 163, 184))

    # Bottom Bar / Trust Footer
    draw.line([(90, 520), (w - 90, 520)], fill=(255, 255, 255, 35), width=1)
    draw.text((90, 545), "Prime Perks Guide — Independent Consumer Buying & Savings Hub", font=font_footer, fill=(148, 163, 184))
    draw.text((w - 380, 545), "https://primeperksguide.com", font=font_footer, fill=(255, 153, 0))

    og_out = os.path.join(IMAGES_DIR, "og-share.png")
    img.save(og_out, format="PNG", optimize=True)
    print(f"Saved Open Graph share banner: {og_out} (1200x630)")

if __name__ == "__main__":
    generate_all_icons()
    generate_og_share_image()

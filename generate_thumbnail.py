import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_og_thumbnail():
    width, height = 1200, 630
    img = Image.new("RGBA", (width, height), "#0F172A")
    draw = ImageDraw.Draw(img)

    # Background gradient: Slate dark to deep indigo
    for y in range(height):
        r = int(15 + (30 - 15) * (y / height))
        g = int(23 + (27 - 23) * (y / height))
        b = int(42 + (75 - 42) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

    # Add soft background glowing circles
    glow = Image.new("RGBA", (width, height), (0,0,0,0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([700, -100, 1300, 500], fill=(79, 70, 229, 60)) # Indigo glow
    glow_draw.ellipse([-100, 200, 400, 700], fill=(16, 185, 129, 50))  # Emerald glow
    glow_draw.ellipse([400, 400, 900, 900], fill=(236, 72, 153, 40))   # Pink glow
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)

    # Try loading fonts, fallback to default
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
        font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        font_card_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
        font_card_desc = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
        font_badge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
    except Exception:
        font_title = font_subtitle = font_card_title = font_card_desc = font_badge = ImageFont.load_default()

    # Header / Logo area
    badge_bg = (99, 102, 241, 60)
    badge_border = (129, 140, 248, 180)
    draw.rounded_rectangle([65, 30, 310, 64], radius=16, fill=badge_bg, outline=badge_border, width=2)
    draw.text((82, 38), "PORTAL GAME EDUKASI", fill="#A5B4FC", font=font_badge)

    # Main Title & Subtitle
    draw.text((65, 72), "main-edu", fill="#FFFFFF", font=font_title)
    draw.text((320, 95), "Platform Permainan Interaktif Anak: Ketangkasan, Sensorik, & Edukasi", fill="#94A3B8", font=font_subtitle)

    # 6 Game Preview Cards (2 rows x 3 columns)
    games = [
        {
            "name": "Tangkap Huruf",
            "tag": "Luar Angkasa",
            "desc": "Ketik cepat huruf & angka yang jatuh.",
            "color": (56, 189, 248), # Cyan/Sky
            "bg": (15, 23, 42, 220),
            "border": (56, 189, 248, 120),
            "preview_path": "/var/www/html/game/assets/img/preview-space.png"
        },
        {
            "name": "Tap Tap Kebun",
            "tag": "Sensorik Anak",
            "desc": "Stimulasi motorik & sensorik warna.",
            "color": (52, 211, 153), # Emerald
            "bg": (15, 23, 42, 220),
            "border": (52, 211, 153, 120),
            "preview_path": "/var/www/html/game/assets/img/preview-garden.png"
        },
        {
            "name": "Jejak Huruf",
            "tag": "Latihan Menulis",
            "desc": "Menelusuri garis pola huruf & angka.",
            "color": (251, 113, 133), # Rose
            "bg": (15, 23, 42, 220),
            "border": (251, 113, 133, 120),
            "preview_path": "/var/www/html/game/assets/img/preview-trace.png"
        },
        {
            "name": "Kartu Ingatan",
            "tag": "Latihan Mengingat",
            "desc": "Mencocokkan pasangan kartu gambar.",
            "color": (251, 191, 36), # Amber/Yellow
            "bg": (15, 23, 42, 220),
            "border": (251, 191, 36, 120),
            "preview_path": "/var/www/html/game/assets/img/preview-memory.png"
        },
        {
            "name": "Cocokkan Huruf",
            "tag": "Huruf Besar & Kecil",
            "desc": "Memasangkan huruf besar & kecil.",
            "color": (192, 132, 252), # Purple
            "bg": (15, 23, 42, 220),
            "border": (192, 132, 252, 120),
            "preview_path": "/var/www/html/game/assets/img/preview-match.png"
        },
        {
            "name": "Tebak Suara",
            "tag": "Suara Hewan",
            "desc": "Tebak hewan dari suara khasnya.",
            "color": (255, 111, 89), # Coral
            "bg": (15, 23, 42, 220),
            "border": (255, 111, 89, 120),
            "preview_path": "/var/www/html/game/assets/img/preview-sound.png"
        }
    ]

    card_w, card_h = 340, 175
    start_x = 65
    start_y = 180
    gap_x, gap_y = 25, 20

    for i, g in enumerate(games):
        col = i % 3
        row = i // 3
        x = start_x + col * (card_w + gap_x)
        y = start_y + row * (card_h + gap_y)

        # Draw card base shadow & body
        card = Image.new("RGBA", (card_w, card_h), (0,0,0,0))
        cdraw = ImageDraw.Draw(card)
        cdraw.rounded_rectangle([0, 0, card_w, card_h], radius=18, fill=g["bg"], outline=g["border"], width=2)
        img.paste(card, (x, y), card)

        # Paste preview image if exists (Left side of card)
        if os.path.exists(g["preview_path"]):
            try:
                prev = Image.open(g["preview_path"]).convert("RGBA")
                prev_w, prev_h = 135, 135
                prev = prev.resize((prev_w, prev_h), Image.Resampling.LANCZOS)
                
                mask = Image.new("L", (prev_w, prev_h), 0)
                mdraw = ImageDraw.Draw(mask)
                mdraw.rounded_rectangle([0, 0, prev_w, prev_h], radius=12, fill=255)
                
                img.paste(prev, (x + 15, y + 20), mask)
            except Exception as e:
                print("Preview error:", e)

        # Right side text inside card
        tx = x + 162
        draw.text((tx, y + 22), g["name"], fill="#F8FAFC", font=font_card_title)
        draw.text((tx, y + 54), g["tag"].upper(), fill=g["color"], font=font_badge)
        
        # Multiline description wrapping
        desc = g["desc"]
        words = desc.split()
        line1, line2 = "", ""
        for word in words:
            if len(line1 + " " + word) < 18:
                line1 += (" " if line1 else "") + word
            else:
                line2 += (" " if line2 else "") + word
        
        draw.text((tx, y + 82), line1, fill="#94A3B8", font=font_card_desc)
        if line2:
            draw.text((tx, y + 104), line2, fill="#94A3B8", font=font_card_desc)

    # Footer banner / Domain reference
    footer_text = "main-edu.webkuy.com"
    draw.text((65, 580), footer_text, fill="#A5B4FC", font=font_card_title)

    thumbnail_path = "/var/www/html/game/assets/img/thumbnail.png"
    img.save(thumbnail_path, "PNG")
    print(f"Thumbnail generated at: {thumbnail_path}")

if __name__ == '__main__':
    create_og_thumbnail()

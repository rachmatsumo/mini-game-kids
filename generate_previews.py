import os, math
from PIL import Image, ImageDraw, ImageFont

def draw_space_preview():
    w, h = 800, 450
    img = Image.new("RGBA", (w, h), (21, 14, 53, 255))
    draw = ImageDraw.Draw(img)
    
    # Stars
    import random
    random.seed(42)
    for _ in range(120):
        sx, sy = random.randint(0, w), random.randint(0, h)
        r = random.uniform(1, 3.5)
        op = random.randint(100, 255)
        draw.ellipse([sx-r, sy-r, sx+r, sy+r], fill=(255, 255, 255, op))
        
    # Planets
    draw.ellipse([620, 40, 740, 160], fill=(167, 139, 250, 200))
    draw.ellipse([80, 280, 180, 380], fill=(79, 227, 193, 160))
    
    # Falling letter blocks
    letters = [('A', 220, 120, (255, 209, 102)), ('B', 380, 70, (79, 227, 193)), ('C', 540, 160, (255, 107, 107))]
    for char, lx, ly, color in letters:
        draw.rounded_rectangle([lx-35, ly-35, lx+35, ly+35], radius=16, fill=color)
        draw.text((lx-12, ly-20), char, fill=(21, 14, 53), font_size=40)
        
    # UFO Catcher
    cx, cy = 400, 360
    draw.ellipse([cx-40, cy-35, cx+40, cy+10], fill=(79, 227, 193, 220))
    draw.ellipse([cx-70, cy-10, cx+70, cy+25], fill=(167, 139, 250, 255))
    draw.ellipse([cx-40, cy+5, cx-20, cy+18], fill=(255, 209, 102, 255))
    draw.ellipse([cx-10, cy+8, cx+10, cy+20], fill=(255, 209, 102, 255))
    draw.ellipse([cx+20, cy+5, cx+40, cy+18], fill=(255, 209, 102, 255))
    
    # Beam
    draw.polygon([(cx-10, cy-10), (cx+10, cy-10), (380, 105), (400, 105)], fill=(79, 227, 193, 80))
    
    return img

def draw_garden_preview():
    w, h = 800, 450
    img = Image.new("RGBA", (w, h), (143, 211, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Sun
    draw.ellipse([650, -30, 830, 150], fill=(255, 212, 59, 255))
    
    # Grass hills
    draw.ellipse([-100, 250, 500, 600], fill=(126, 217, 87, 255))
    draw.ellipse([300, 220, 900, 600], fill=(76, 175, 80, 255))
    
    # Cute elements: Butterfly & Balloons
    # Butterfly
    bx, by = 240, 140
    draw.ellipse([bx-45, by-35, bx, by+5], fill=(255, 107, 107, 240))
    draw.ellipse([bx, by-35, bx+45, by+5], fill=(255, 107, 107, 240))
    draw.ellipse([bx-35, by+5, bx-5, by+35], fill=(255, 143, 171, 240))
    draw.ellipse([bx+5, by+5, bx+35, by+35], fill=(255, 143, 171, 240))
    draw.ellipse([bx-6, by-40, bx+6, by+40], fill=(59, 42, 94, 255))
    
    # Balloon
    balx, baly = 560, 160
    draw.ellipse([balx-40, baly-50, balx+40, baly+50], fill=(255, 77, 109, 255))
    draw.polygon([(balx-8, baly+48), (balx+8, baly+48), (balx, baly+60)], fill=(255, 77, 109, 255))
    
    # Frog
    fx, fy = 450, 310
    draw.ellipse([fx-50, fy-35, fx+50, fy+25], fill=(92, 199, 92, 255))
    draw.ellipse([fx-35, fy-55, fx-10, fy-25], fill=(92, 199, 92, 255))
    draw.ellipse([fx+10, fy-55, fx+35, fy-25], fill=(92, 199, 92, 255))
    draw.ellipse([fx-30, fy-50, fx-15, fy-35], fill=(255, 255, 255, 255))
    draw.ellipse([fx+15, fy-50, fx+30, fy-35], fill=(255, 255, 255, 255))
    draw.ellipse([fx-25, fy-46, fx-18, fy-39], fill=(0, 0, 0, 255))
    draw.ellipse([fx+18, fy-46, fx+25, fy-39], fill=(0, 0, 0, 255))
    
    return img

def draw_trace_preview():
    w, h = 800, 450
    img = Image.new("RGBA", (w, h), (23, 39, 31, 255))
    draw = ImageDraw.Draw(img)
    
    # Chalkboard border accent
    draw.rectangle([10, 10, w-10, h-10], fill=None, outline=(111, 230, 184, 150), width=4)
    
    # Big Dotted Letter 'A'
    cx, cy = 400, 210
    pts = [
        (cx-120, cy+130), (cx-90, cy+60), (cx-60, cy-10),
        (cx-30, cy-80), (cx, cy-130), (cx+30, cy-80),
        (cx+60, cy-10), (cx+90, cy+60), (cx+120, cy+130)
    ]
    # Dotted lines
    for px, py in pts:
        draw.ellipse([px-12, py-12, px+12, py+12], fill=(255, 209, 102, 255))
        
    # Crossbar
    draw.ellipse([cx-50, cy+25, cx-26, cy+49], fill=(111, 230, 184, 255))
    draw.ellipse([cx, cy+25, cx+24, cy+49], fill=(111, 230, 184, 255))
    draw.ellipse([cx+26, cy+25, cx+50, cy+49], fill=(111, 230, 184, 255))
    
    # Tracing stroke line simulation
    draw.line([(pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), (pts[3][0], pts[3][1]), (pts[4][0], pts[4][1])], fill=(111, 230, 184, 230), width=18)

    return img

def draw_memory_preview():
    w, h = 800, 450
    img = Image.new("RGBA", (w, h), (191, 231, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Soft background clouds
    draw.ellipse([80, 40, 240, 110], fill=(255, 255, 255, 220))
    draw.ellipse([560, 50, 720, 120], fill=(255, 255, 255, 220))
    
    # Grass strip
    draw.rectangle([0, 390, w, h], fill=(143, 209, 126, 255))
    
    # Grid of cards
    card_w, card_h = 110, 120
    cols, rows = 4, 2
    gap_x, gap_y = 35, 25
    start_x = (w - (cols * card_w + (cols - 1) * gap_x)) // 2
    start_y = 110
    
    # Card faces (some flipped with animal emojis / shapes, some back)
    cards_data = [
        {"flipped": True, "color": (255, 255, 255), "accent": (255, 138, 115)}, # Coral
        {"flipped": False, "color": (91, 141, 239)},
        {"flipped": True, "color": (255, 255, 255), "accent": (79, 214, 168)},  # Mint
        {"flipped": False, "color": (91, 141, 239)},
        {"flipped": False, "color": (91, 141, 239)},
        {"flipped": True, "color": (255, 255, 255), "accent": (255, 138, 115)}, # Coral match
        {"flipped": False, "color": (91, 141, 239)},
        {"flipped": True, "color": (255, 255, 255), "accent": (255, 201, 71)},  # Yellow
    ]
    
    for idx, c in enumerate(cards_data):
        r = idx // cols
        col = idx % cols
        cx = start_x + col * (card_w + gap_x)
        cy = start_y + r * (card_h + gap_y)
        
        if c["flipped"]:
            draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=16, fill=c["color"], outline=(79, 214, 168, 255), width=3)
            # Center shape/symbol
            draw.ellipse([cx + card_w//2 - 24, cy + card_h//2 - 24, cx + card_w//2 + 24, cy + card_h//2 + 24], fill=c["accent"])
        else:
            draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=16, fill=c["color"])
            # Card back pattern
            draw.ellipse([cx + card_w//2 - 14, cy + card_h//2 - 14, cx + card_w//2 + 14, cy + card_h//2 + 14], fill=(255, 255, 255, 140))

    return img

def draw_match_preview():
    w, h = 800, 450
    img = Image.new("RGBA", (w, h), (243, 232, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Left chips (Capital letters) vs Right slots (Lowercase letters)
    chip_w, chip_h = 130, 58
    left_x = 160
    right_x = 510
    
    pairs = [
        ("A", "a", (255, 140, 107)), # Coral
        ("B", "b", (255, 200, 87)),  # Yellow
        ("C", "c", (79, 195, 182)),  # Teal
        ("D", "d", (126, 168, 255)), # Blue
    ]
    
    try:
        font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    except Exception:
        font_big = ImageFont.load_default()

    for idx, (cap, low, color) in enumerate(pairs):
        y = 70 + idx * 85
        # Left Draggable Chip
        draw.rounded_rectangle([left_x, y, left_x + chip_w, y + chip_h], radius=14, fill=color)
        draw.text((left_x + 52, y + 12), cap, fill="#FFFFFF", font=font_big)
        
        # Right Slot
        draw.rounded_rectangle([right_x, y, right_x + chip_w, y + chip_h], radius=14, fill=(255, 255, 255, 200), outline=(124, 110, 147, 120), width=2)
        draw.text((right_x + 54, y + 12), low, fill="#7C6E93", font=font_big)

    # Arrow indicator between A and a
    draw.line([(left_x + chip_w + 15, 99), (right_x - 15, 99)], fill=(79, 195, 182, 255), width=4)
    draw.polygon([(right_x - 15, 93), (right_x - 5, 99), (right_x - 15, 105)], fill=(79, 195, 182, 255))

    return img

def draw_sound_preview():
    w, h = 800, 450
    img = Image.new("RGBA", (w, h), (255, 237, 216, 255))
    draw = ImageDraw.Draw(img)
    
    # Speaker button in center top
    cx, cy = 400, 140
    r = 60
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 200, 87, 255))
    draw.ellipse([cx - r - 12, cy - r - 12, cx + r + 12, cy + r + 12], outline=(255, 200, 87, 180), width=4)
    
    # Choice animal buttons
    choices = ["🐱", "🐶", "🐮", "🐥"]
    card_w, card_h = 130, 130
    gap = 30
    start_x = (w - (4 * card_w + 3 * gap)) // 2
    y = 260
    
    for idx, emoji in enumerate(choices):
        x = start_x + idx * (card_w + gap)
        fill_col = (201, 242, 214, 255) if idx == 0 else (255, 255, 255, 220)
        border_col = (63, 191, 174, 255) if idx == 0 else (138, 117, 102, 100)
        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=20, fill=fill_col, outline=border_col, width=3)

    return img

if __name__ == '__main__':
    os.makedirs("assets/img", exist_ok=True)
    draw_space_preview().save("assets/img/preview-space.png")
    draw_garden_preview().save("assets/img/preview-garden.png")
    draw_trace_preview().save("assets/img/preview-trace.png")
    draw_memory_preview().save("assets/img/preview-memory.png")
    draw_match_preview().save("assets/img/preview-match.png")
    draw_sound_preview().save("assets/img/preview-sound.png")
    print("Preview images generated inside assets/img!")

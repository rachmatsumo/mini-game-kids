import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "/var/www/html/game/assets/img"
os.makedirs(ASSETS_DIR, exist_ok=True)

SIZE = (512, 512)

def create_rounded_mask(size, radius):
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, size[0], size[1]], radius=radius, fill=255)
    return mask

def draw_app_icon(filename, bg_color1, bg_color2, draw_func):
    img = Image.new("RGBA", SIZE, bg_color1)
    draw = ImageDraw.Draw(img)
    
    # Gradient background
    for y in range(SIZE[1]):
        r = int(bg_color1[0] + (bg_color2[0] - bg_color1[0]) * (y / SIZE[1]))
        g = int(bg_color1[1] + (bg_color2[1] - bg_color1[1]) * (y / SIZE[1]))
        b = int(bg_color1[2] + (bg_color2[2] - bg_color1[2]) * (y / SIZE[1]))
        draw.line([(0, y), (SIZE[0], y)], fill=(r, g, b, 255))
        
    draw_func(draw)
    
    # Glossy top highlight
    highlight = Image.new("RGBA", SIZE, (255, 255, 255, 0))
    h_draw = ImageDraw.Draw(highlight)
    h_draw.ellipse([-100, -200, 612, 220], fill=(255, 255, 255, 40))
    img = Image.alpha_composite(img, highlight)
    
    # Outer border shadow/stroke
    border_draw = ImageDraw.Draw(img)
    border_draw.rounded_rectangle([4, 4, SIZE[0]-4, SIZE[1]-4], radius=88, outline=(255, 255, 255, 120), width=8)
    
    mask = create_rounded_mask(SIZE, 88)
    output = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    output.paste(img, (0, 0), mask)
    
    path = os.path.join(ASSETS_DIR, filename)
    output.save(path, "PNG")
    print(f"Saved: {path}")

# 1. Space App Icon
def draw_space(draw):
    # Stars
    stars = [(100, 80, 8), (400, 90, 10), (80, 380, 6), (420, 360, 9), (250, 60, 7)]
    for sx, sy, sr in stars:
        draw.ellipse([sx-sr, sy-sr, sx+sr, sy+sr], fill=(255, 255, 255, 220))
    # Rocket Body
    draw.polygon([(256, 120), (330, 320), (182, 320)], fill=(244, 63, 94))
    draw.ellipse([216, 260, 296, 340], fill=(255, 255, 255))
    draw.ellipse([236, 280, 276, 320], fill=(14, 165, 233))
    # Rocket fins
    draw.polygon([(182, 300), (140, 360), (182, 340)], fill=(225, 29, 72))
    draw.polygon([(330, 300), (372, 360), (330, 340)], fill=(225, 29, 72))
    # Flame
    draw.polygon([(230, 340), (256, 420), (282, 340)], fill=(251, 146, 60))
    draw.polygon([(242, 340), (256, 390), (270, 340)], fill=(253, 224, 71))

draw_app_icon("app-space.png", (30, 27, 75), (124, 58, 237), draw_space)

# 2. Garden App Icon
def draw_garden(draw):
    # Sun / Sky
    draw.rectangle([0, 0, 512, 300], fill=(56, 189, 248))
    draw.ellipse([340, 40, 460, 160], fill=(250, 204, 21))
    # Grass hills
    draw.ellipse([-50, 260, 350, 550], fill=(34, 197, 94))
    draw.ellipse([150, 240, 580, 550], fill=(74, 222, 128))
    # Ladybug
    draw.ellipse([200, 260, 312, 370], fill=(239, 68, 68))
    draw.ellipse([230, 235, 282, 275], fill=(30, 41, 59))
    draw.line([(256, 265), (256, 370)], fill=(30, 41, 59), width=6)
    # Spots
    draw.ellipse([220, 290, 240, 310], fill=(30, 41, 59))
    draw.ellipse([272, 290, 292, 310], fill=(30, 41, 59))
    draw.ellipse([230, 330, 246, 346], fill=(30, 41, 59))
    draw.ellipse([266, 330, 282, 346], fill=(30, 41, 59))

draw_app_icon("app-garden.png", (16, 185, 129), (5, 150, 105), draw_garden)

# 3. Trace App Icon
def draw_trace(draw):
    # Notebook lines
    for y in range(80, 480, 80):
        draw.line([(40, y), (472, y)], fill=(226, 232, 240), width=4)
    draw.line([(100, 0), (100, 512)], fill=(248, 113, 113), width=6)
    # Big A letter trace
    draw.line([(256, 120), (160, 380)], fill=(79, 70, 229), width=28)
    draw.line([(256, 120), (352, 380)], fill=(79, 70, 229), width=28)
    draw.line([(195, 280), (317, 280)], fill=(79, 70, 229), width=24)
    # Dotted guide overlay
    dots = [(256, 120), (208, 250), (160, 380), (304, 250), (352, 380), (256, 280)]
    for dx, dy in dots:
        draw.ellipse([dx-10, dy-10, dx+10, dy+10], fill=(251, 191, 36))
    # Pencil icon
    draw.polygon([(360, 120), (430, 190), (240, 380), (180, 400), (200, 340)], fill=(245, 158, 11))

draw_app_icon("app-trace.png", (254, 243, 199), (253, 230, 138), draw_trace)

# 4. Memory App Icon
def draw_memory(draw):
    # Two cards overlapping
    # Card 1 (Back)
    draw.rounded_rectangle([80, 120, 300, 400], radius=24, fill=(99, 102, 241), outline=(255, 255, 255), width=8)
    draw.ellipse([140, 210, 240, 310], fill=(129, 140, 248))
    # Card 2 (Front - Bear Face)
    draw.rounded_rectangle([200, 80, 420, 360], radius=24, fill=(255, 255, 255), outline=(99, 102, 241), width=8)
    # Bear Ears
    draw.ellipse([220, 60, 270, 110], fill=(245, 158, 11))
    draw.ellipse([350, 60, 400, 110], fill=(245, 158, 11))
    # Bear Head
    draw.ellipse([230, 100, 390, 260], fill=(245, 158, 11))
    # Bear Snout & Eyes
    draw.ellipse([280, 170, 340, 230], fill=(254, 243, 199))
    draw.ellipse([300, 180, 320, 200], fill=(67, 20, 7))
    draw.ellipse([270, 140, 290, 160], fill=(67, 20, 7))
    draw.ellipse([330, 140, 350, 160], fill=(67, 20, 7))

draw_app_icon("app-memory.png", (129, 140, 248), (79, 70, 229), draw_memory)

# 5. Match App Icon
def draw_match(draw):
    # Puzzle Piece 1 (A)
    draw.rounded_rectangle([80, 100, 260, 280], radius=24, fill=(192, 132, 252), outline=(255, 255, 255), width=8)
    # Puzzle Piece 2 (a)
    draw.rounded_rectangle([250, 220, 430, 400], radius=24, fill=(168, 85, 247), outline=(255, 255, 255), width=8)
    # Connector glow line
    draw.line([(260, 210), (250, 220)], fill=(253, 224, 71), width=12)

draw_app_icon("app-match.png", (216, 180, 254), (147, 51, 234), draw_match)

# 6. Sound App Icon
def draw_sound(draw):
    # Speaker cone
    draw.polygon([(100, 210), (180, 210), (260, 140), (260, 370), (180, 300), (100, 300)], fill=(255, 255, 255))
    # Sound waves
    draw.arc([220, 160, 340, 350], start=-60, end=60, fill=(255, 255, 255), width=20)
    draw.arc([240, 110, 420, 400], start=-60, end=60, fill=(255, 255, 255), width=24)
    # Animal Note
    draw.ellipse([340, 120, 420, 200], fill=(254, 240, 138))

draw_app_icon("app-sound.png", (255, 111, 89), (224, 77, 54), draw_sound)

# 7. Berhitung Jari App Icon
def draw_count(draw):
    # Cute Hand Palm
    draw.ellipse([180, 240, 332, 400], fill=(255, 207, 160))
    # Extended Fingers (1, 2, 3)
    draw.rounded_rectangle([190, 120, 226, 260], radius=18, fill=(255, 207, 160))
    draw.rounded_rectangle([238, 100, 274, 260], radius=18, fill=(255, 207, 160))
    draw.rounded_rectangle([286, 120, 322, 260], radius=18, fill=(255, 207, 160))
    # Math Plus Sign
    draw.rounded_rectangle([350, 160, 430, 200], radius=10, fill=(255, 201, 60))
    draw.rounded_rectangle([370, 140, 410, 220], radius=10, fill=(255, 201, 60))

draw_app_icon("app-count.png", (76, 141, 255), (46, 111, 224), draw_count)
draw_app_icon("preview-count.png", (76, 141, 255), (46, 111, 224), draw_count)


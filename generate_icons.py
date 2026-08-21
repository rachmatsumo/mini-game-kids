import os
from PIL import Image, ImageDraw, ImageFont

def create_portal_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.05)
    r = int(size * 0.22)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=(79, 70, 229, 255))
    draw.rounded_rectangle([pad + 4, pad + 4, size - pad - 4, size - pad - 4], radius=r - 2, outline=(129, 140, 248, 255), width=max(2, size // 64))
    
    cx, cy = size // 2, size // 2
    star_r = size * 0.12
    sx, sy = cx + size * 0.18, cy - size * 0.18
    draw.ellipse([sx - star_r, sy - star_r, sx + star_r, sy + star_r], fill=(253, 224, 71, 255))
    
    cw, ch = size * 0.52, size * 0.32
    draw.rounded_rectangle([cx - cw/2, cy - ch/2, cx + cw/2, cy + ch/2], radius=int(ch*0.4), fill=(255, 255, 255, 255))
    
    dp_s = size * 0.07
    dpx, dpy = cx - size * 0.14, cy
    draw.rectangle([dpx - dp_s/3, dpy - dp_s, dpx + dp_s/3, dpy + dp_s], fill=(79, 70, 229, 255))
    draw.rectangle([dpx - dp_s, dpy - dp_s/3, dpx + dp_s, dpy + dp_s/3], fill=(79, 70, 229, 255))
    
    abx, aby = cx + size * 0.14, cy
    btn_r = size * 0.038
    draw.ellipse([abx - btn_r, aby - size * 0.06 - btn_r, abx + btn_r, aby - size * 0.06 + btn_r], fill=(239, 68, 68, 255))
    draw.ellipse([abx - btn_r, aby + size * 0.06 - btn_r, abx + btn_r, aby + size * 0.06 + btn_r], fill=(34, 197, 94, 255))
    draw.ellipse([abx - size * 0.06 - btn_r, aby - btn_r, abx - size * 0.06 + btn_r, aby + btn_r], fill=(234, 179, 8, 255))
    draw.ellipse([abx + size * 0.06 - btn_r, aby - btn_r, abx + size * 0.06 + btn_r, aby + btn_r], fill=(59, 130, 246, 255))
    return img

def create_space_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.05)
    r = int(size * 0.22)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=(21, 14, 53, 255))
    draw.rounded_rectangle([pad + 4, pad + 4, size - pad - 4, size - pad - 4], radius=r - 2, outline=(79, 227, 193, 255), width=max(2, size // 64))
    cx, cy = size // 2, size // 2
    draw.ellipse([cx - size*0.2, cy - size*0.28, cx + size*0.2, cy + size*0.05], fill=(79, 227, 193, 220))
    draw.ellipse([cx - size*0.35, cy - size*0.08, cx + size*0.35, cy + size*0.18], fill=(167, 139, 250, 255))
    draw.ellipse([cx - size*0.2, cy + size*0.02, cx - size*0.1, cy + size*0.1], fill=(255, 209, 102, 255))
    draw.ellipse([cx - size*0.05, cy + size*0.04, cx + size*0.05, cy + size*0.12], fill=(255, 209, 102, 255))
    draw.ellipse([cx + size*0.1, cy + size*0.02, cx + size*0.2, cy + size*0.1], fill=(255, 209, 102, 255))
    return img

def create_garden_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.05)
    r = int(size * 0.22)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=(143, 211, 255, 255))
    draw.rounded_rectangle([pad + 4, pad + 4, size - pad - 4, size - pad - 4], radius=r - 2, outline=(126, 217, 87, 255), width=max(2, size // 64))
    cx, cy = size // 2, size // 2
    draw.ellipse([cx - size*0.28, cy - size*0.1, cx, cy + size*0.25], fill=(76, 175, 80, 255))
    draw.ellipse([cx, cy - size*0.22, cx + size*0.28, cy + size*0.15], fill=(126, 217, 87, 255))
    draw.rectangle([cx - size*0.04, cy, cx + size*0.04, cy + size*0.3], fill=(59, 42, 94, 255))
    draw.ellipse([cx + size*0.1, cy - size*0.32, cx + size*0.32, cy - size*0.1], fill=(255, 212, 59, 255))
    return img

def create_trace_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.05)
    r = int(size * 0.22)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=(23, 39, 31, 255))
    draw.rounded_rectangle([pad + 4, pad + 4, size - pad - 4, size - pad - 4], radius=r - 2, outline=(111, 230, 184, 255), width=max(2, size // 64))
    cx, cy = size // 2, size // 2
    points = [
        (cx - size*0.22, cy + size*0.22),
        (cx - size*0.11, cy - size*0.02),
        (cx, cy - size*0.24),
        (cx + size*0.11, cy - size*0.02),
        (cx + size*0.22, cy + size*0.22),
    ]
    for px, py in points:
        draw.ellipse([px - size*0.035, py - size*0.035, px + size*0.035, py + size*0.035], fill=(255, 209, 102, 255))
    draw.ellipse([cx - size*0.08, cy + size*0.08, cx - size*0.02, cy + size*0.14], fill=(111, 230, 184, 255))
    draw.ellipse([cx + size*0.02, cy + size*0.08, cx + size*0.08, cy + size*0.14], fill=(111, 230, 184, 255))
    return img

def create_memory_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.05)
    r = int(size * 0.22)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=(191, 231, 255, 255))
    draw.rounded_rectangle([pad + 4, pad + 4, size - pad - 4, size - pad - 4], radius=r - 2, outline=(91, 141, 239, 255), width=max(2, size // 64))
    
    # 2 Memory Cards overlapping
    card_w, card_h = int(size * 0.36), int(size * 0.44)
    # Card 1 (back)
    draw.rounded_rectangle([size * 0.16, size * 0.28, size * 0.16 + card_w, size * 0.28 + card_h], radius=int(card_w*0.2), fill=(91, 141, 239, 255))
    # Card 2 (front with star/brain icon)
    draw.rounded_rectangle([size * 0.44, size * 0.22, size * 0.44 + card_w, size * 0.22 + card_h], radius=int(card_w*0.2), fill=(255, 255, 255, 255), outline=(79, 214, 168, 255), width=int(size*0.02))
    
    # Star inside front card
    cx, cy = int(size * 0.62), int(size * 0.44)
    star_r = size * 0.1
    draw.ellipse([cx - star_r, cy - star_r, cx + star_r, cy + star_r], fill=(255, 201, 71, 255))
    return img

def create_match_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.05)
    r = int(size * 0.22)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=(243, 232, 255, 255))
    draw.rounded_rectangle([pad + 4, pad + 4, size - pad - 4, size - pad - 4], radius=r - 2, outline=(124, 110, 147, 255), width=max(2, size // 64))
    
    # Drag Chip (A)
    draw.rounded_rectangle([size * 0.14, size * 0.25, size * 0.46, size * 0.75], radius=int(size*0.1), fill=(255, 140, 107, 255))
    # Target Slot (a)
    draw.rounded_rectangle([size * 0.54, size * 0.25, size * 0.86, size * 0.75], radius=int(size*0.1), fill=(255, 255, 255, 255), outline=(79, 195, 182, 255), width=int(size*0.03))
    return img

def create_sound_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.05)
    r = int(size * 0.22)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=(255, 237, 216, 255))
    draw.rounded_rectangle([pad + 4, pad + 4, size - pad - 4, size - pad - 4], radius=r - 2, outline=(138, 117, 102, 255), width=max(2, size // 64))
    
    # Speaker circle
    cx, cy = size // 2, size // 2
    cr = int(size * 0.32)
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=(255, 200, 87, 255))
    return img

if __name__ == '__main__':
    os.makedirs("assets/img", exist_ok=True)
    create_portal_icon(512).save("assets/img/icon-512.png")
    create_portal_icon(192).save("assets/img/icon-192.png")
    create_portal_icon(180).save("assets/img/apple-touch-icon.png")
    create_portal_icon(64).save("assets/img/favicon-portal.png")
    
    create_space_icon(192).save("assets/img/favicon-space.png")
    create_garden_icon(192).save("assets/img/favicon-garden.png")
    create_trace_icon(192).save("assets/img/favicon-trace.png")
    create_memory_icon(192).save("assets/img/favicon-memory.png")
    create_match_icon(192).save("assets/img/favicon-match.png")
    create_sound_icon(192).save("assets/img/favicon-sound.png")
    
    print("Assets PNG icons generated successfully inside assets/img!")

#!/usr/bin/env python3
"""
LinkedIn Post GIF - Loop Engineering Workflow
Shows the PLAN → IMPLEMENT → VERIFY → DECIDE → UPDATE → REPEAT flow
with light yellow/brown colors and animated dashed connections.
"""

import sys
import math
from pathlib import Path

# Add the slack-gif-creator to path
sys.path.insert(0, str(Path.home() / ".agents/skills/11-brand-marketing/slack-gif-creator"))

from PIL import Image, ImageDraw, ImageFont
from core.gif_builder import GIFBuilder
from core.easing import interpolate

# ─── Colors ──────────────────────────────────────────────────────────────────
BG_COLOR = (255, 251, 240)        # Light warm white
BOX_PLAN = (255, 140, 66)         # Orange
BOX_IMPL = (212, 165, 116)        # Light brown
BOX_VERIFY = (252, 165, 165)      # Light red/pink
BOX_DECIDE = (255, 224, 102)      # Light yellow
BOX_UPDATE = (255, 140, 66)       # Orange
BOX_REPEAT = (212, 165, 116)      # Light brown
TEXT_DARK = (45, 45, 45)          # Dark text
TEXT_WHITE = (255, 255, 255)      # White text
DASH_COLOR = (45, 45, 45)        # Black dashed lines
DOT_COLOR = (255, 100, 50)       # Animated dot
ACCENT = (255, 224, 102)         # Yellow accent

# ─── Dimensions ──────────────────────────────────────────────────────────────
W, H = 480, 480
FPS = 15
DURATION_S = 4
NUM_FRAMES = FPS * DURATION_S  # 60 frames

# ─── Box positions (center of each box) ─────────────────────────────────────
# Layout: Circular flow
BOX_W, BOX_H = 110, 50
BOXES = {
    'plan':     (240, 70),
    'implement': (400, 160),
    'verify':   (400, 300),
    'decide':   (240, 400),
    'update':   (80, 300),
    'repeat':   (80, 160),
}

BOX_COLORS = {
    'plan': BOX_PLAN,
    'implement': BOX_IMPL,
    'verify': BOX_VERIFY,
    'decide': BOX_DECIDE,
    'update': BOX_UPDATE,
    'repeat': BOX_REPEAT,
}

BOX_LABELS = {
    'plan': 'PLAN',
    'implement': 'IMPLEMENT',
    'verify': 'VERIFY',
    'decide': 'DECIDE',
    'update': 'UPDATE\nSTATE',
    'repeat': 'REPEAT',
}

# Order of flow
FLOW_ORDER = ['plan', 'implement', 'verify', 'decide', 'update', 'repeat']

# ─── Helper functions ────────────────────────────────────────────────────────

def draw_rounded_box(draw, center, w, h, fill, radius=10):
    """Draw a rounded rectangle centered at (cx, cy)."""
    cx, cy = center
    x1, y1 = cx - w // 2, cy - h // 2
    x2, y2 = cx + w // 2, cy + h // 2
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill)


def draw_dashed_line(draw, start, end, color, width=2, dash_len=8, gap_len=5, dash_offset=0):
    """Draw a dashed line between two points."""
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx * dx + dy * dy)
    if length == 0:
        return
    
    ux, uy = dx / length, dy / length
    
    pos = dash_offset % (dash_len + gap_len)
    while pos < length:
        seg_start = pos
        seg_end = min(pos + dash_len, length)
        
        sx = x1 + ux * seg_start
        sy = y1 + uy * seg_start
        ex = x1 + ux * seg_end
        ey = y1 + uy * seg_end
        
        draw.line([(sx, sy), (ex, ey)], fill=color, width=width)
        pos += dash_len + gap_len


def draw_arrow_head(draw, tip, direction, color, size=8):
    """Draw a small arrow head at the tip pointing in direction."""
    tx, ty = tip
    dx, dy = direction
    length = math.sqrt(dx * dx + dy * dy)
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    
    # Perpendicular
    px, py = -uy, ux
    
    # Arrow points
    base_x = tx - ux * size
    base_y = ty - uy * size
    
    p1 = (base_x + px * size * 0.4, base_y + py * size * 0.4)
    p2 = (base_x - px * size * 0.4, base_y - py * size * 0.4)
    
    draw.polygon([tip, p1, p2], fill=color)


def draw_text_centered(draw, text, center, font, fill):
    """Draw text centered at a position."""
    cx, cy = center
    lines = text.split('\n')
    total_height = 0
    line_heights = []
    line_widths = []
    
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        line_heights.append(h)
        line_widths.append(w)
        total_height += h + 2
    
    y = cy - total_height // 2
    for i, line in enumerate(lines):
        x = cx - line_widths[i] // 2
        draw.text((x, y), line, fill=fill, font=font)
        y += line_heights[i] + 2


def get_font(size):
    """Get font, trying common system fonts."""
    font_paths = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for fp in font_paths:
        if Path(fp).exists():
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()


def get_bold_font(size):
    """Get bold font."""
    font_paths = [
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for fp in font_paths:
        if Path(fp).exists():
            return ImageFont.truetype(fp, size)
    return get_font(size)


# ─── Frame generation ────────────────────────────────────────────────────────

def create_frame(frame_idx):
    """Create a single frame of the animation."""
    t = frame_idx / (NUM_FRAMES - 1)  # 0.0 to 1.0 over full animation
    
    frame = Image.new('RGB', (W, H), BG_COLOR)
    draw = ImageDraw.Draw(frame)
    
    # ─── Title ───────────────────────────────────────────────────────────
    title_font = get_bold_font(18)
    subtitle_font = get_font(11)
    
    draw_text_centered(draw, "Loop Engineering Workflow", (W // 2, 22), title_font, TEXT_DARK)
    draw_text_centered(draw, "PLAN \u2192 IMPLEMENT \u2192 VERIFY \u2192 repeat", (W // 2, 42), subtitle_font, (120, 120, 120))
    
    # ─── Draw dashed connections between boxes ───────────────────────────
    # Connections: plan->implement, implement->verify, verify->decide,
    #              decide->update, update->repeat, repeat->plan
    connections = [
        ('plan', 'implement'),
        ('implement', 'verify'),
        ('verify', 'decide'),
        ('decide', 'update'),
        ('update', 'repeat'),
        ('repeat', 'plan'),
    ]
    
    # Animated dash offset for flow effect
    dash_offset = frame_idx * 1.5
    
    for from_box, to_box in connections:
        fx, fy = BOXES[from_box]
        tx, ty = BOXES[to_box]
        
        # Calculate direction
        dx = tx - fx
        dy = ty - fy
        length = math.sqrt(dx * dx + dy * dy)
        ux, uy = dx / length, dy / length
        
        # Offset start/end to box edges
        start_x = fx + ux * (BOX_W // 2 + 2)
        start_y = fy + uy * (BOX_H // 2 + 2)
        end_x = tx - ux * (BOX_W // 2 + 2)
        end_y = ty - uy * (BOX_H // 2 + 2)
        
        draw_dashed_line(draw, (start_x, start_y), (end_x, end_y),
                        DASH_COLOR, width=2, dash_len=8, gap_len=5,
                        dash_offset=dash_offset)
        
        # Draw arrow head
        arrow_tip = (end_x, end_y)
        draw_arrow_head(draw, arrow_tip, (ux, uy), DASH_COLOR, size=8)
    
    # ─── Draw boxes ──────────────────────────────────────────────────────
    label_font = get_bold_font(11)
    
    # Determine which box is "active" (animated glow)
    # Cycle through boxes over time
    cycle_pos = (t * len(FLOW_ORDER)) % len(FLOW_ORDER)
    active_idx = int(cycle_pos)
    active_blend = cycle_pos - active_idx  # 0.0 to 1.0 blend
    
    for i, box_name in enumerate(FLOW_ORDER):
        cx, cy = BOXES[box_name]
        color = BOX_COLORS[box_name]
        
        # Glow effect on active box
        if i == active_idx:
            # Pulsing glow
            glow_size = int(4 + 3 * math.sin(active_blend * math.pi))
            glow_color = tuple(min(255, c + 30) for c in color)
            draw_rounded_box(draw, (cx, cy), BOX_W + glow_size, BOX_H + glow_size, glow_color, radius=12)
        
        draw_rounded_box(draw, (cx, cy), BOX_W, BOX_H, color, radius=10)
        draw_text_centered(draw, BOX_LABELS[box_name], (cx, cy), label_font, TEXT_WHITE if box_name != 'decide' else TEXT_DARK)
    
    # ─── Animated dot moving along the flow ──────────────────────────────
    # The dot cycles through all connections
    dot_cycle = (t * len(connections)) % len(connections)
    dot_seg = int(dot_cycle)
    dot_t = dot_cycle - dot_seg
    
    if dot_seg < len(connections):
        from_name, to_name = connections[dot_seg]
        fx, fy = BOXES[from_name]
        tx, ty = BOXES[to_name]
        
        # Ease the dot
        dot_ease = interpolate(0, 1, dot_t, 'ease_in_out')
        
        dx = tx - fx
        dy = ty - fy
        length = math.sqrt(dx * dx + dy * dy)
        ux, uy = dx / length, dy / length
        
        start_x = fx + ux * (BOX_W // 2 + 2)
        start_y = fy + uy * (BOX_H // 2 + 2)
        end_x = tx - ux * (BOX_W // 2 + 2)
        end_y = ty - uy * (BOX_H // 2 + 2)
        
        dot_x = start_x + (end_x - start_x) * dot_ease
        dot_y = start_y + (end_y - start_y) * dot_ease
        
        # Draw glowing dot
        for r in range(12, 0, -1):
            alpha = int(60 * (1 - r / 12))
            glow_c = (255, min(255, 100 + alpha), min(255, 50 + alpha))
            draw.ellipse([dot_x - r, dot_y - r, dot_x + r, dot_y + r], fill=glow_c)
        draw.ellipse([dot_x - 5, dot_y - 5, dot_x + 5, dot_y + 5], fill=DOT_COLOR)
    
    # ─── Footer ──────────────────────────────────────────────────────────
    footer_font = get_font(10)
    draw_text_centered(draw, "github.com/shivamsingh-007/loop-engineering-stucture", 
                       (W // 2, H - 22), footer_font, (150, 150, 150))
    
    return frame


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    print("Creating Loop Engineering Workflow GIF...")
    print(f"  Dimensions: {W}x{H}")
    print(f"  FPS: {FPS}")
    print(f"  Duration: {DURATION_S}s ({NUM_FRAMES} frames)")
    
    builder = GIFBuilder(width=W, height=H, fps=FPS)
    
    for i in range(NUM_FRAMES):
        frame = create_frame(i)
        builder.add_frame(frame)
        if i % 10 == 0:
            print(f"  Frame {i + 1}/{NUM_FRAMES}...")
    
    output_path = Path(__file__).parent / "loop-workflow.gif"
    
    # Save directly to avoid Unicode issues in gif_builder print
    import imageio.v3 as imageio_io
    import numpy as np
    
    # Optimize colors
    optimized = builder.optimize_colors(num_colors=128, use_global_palette=True)
    frame_duration = 1000 / FPS
    
    imageio_io.imwrite(
        output_path,
        optimized,
        duration=frame_duration,
        loop=0
    )
    
    file_size_kb = output_path.stat().st_size / 1024
    file_size_mb = file_size_kb / 1024
    
    info = {
        'path': str(output_path),
        'size_kb': file_size_kb,
        'size_mb': file_size_mb,
        'dimensions': f'{W}x{H}',
        'frame_count': len(optimized),
        'fps': FPS,
        'duration_seconds': len(optimized) / FPS,
        'colors': 128
    }
    
    print(f"\nGIF created: {output_path}")
    print(f"Size: {file_size_kb:.1f} KB ({file_size_mb:.2f} MB)")
    print(f"Frames: {len(optimized)} @ {FPS} fps")
    
    if file_size_kb > 2048:
        print(f"WARNING: File size exceeds 2MB Slack limit")
    
    return info


if __name__ == "__main__":
    main()

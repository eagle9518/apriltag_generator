import os
import argparse
from PIL import Image
parser = argparse.ArgumentParser(
    description='Combine multiple AprilTag PNGs into one SVG grid.'
)
parser.add_argument(
    'tag_files', type=str, nargs='+',
    help='Paths to AprilTag PNG files.'
)
parser.add_argument(
    'out_file', type=str,
    help='Output SVG file path.'
)
parser.add_argument(
    '--size', type=str, default='50mm',
    help='Size of each tag in the SVG (e.g., 20mm, 100px)'
)
parser.add_argument(
    '--columns', type=int, default=4,
    help='Number of tags per row in the output SVG'
)
def rgba(pixel):
    r, g, b, a = pixel
    return f'rgba({r},{g},{b},{a/255})'
def draw_tag(x_offset, y_offset, width, height, pixels):
    tag_svg = ''
    for y in range(height):
        for x in range(width):
            fill = rgba(pixels[x, y])
            tag_svg += f'<rect width="1" height="1" x="{x + x_offset}" y="{y + y_offset}" fill="{fill}"/>\n'
    return tag_svg
def main():
    args = parser.parse_args()
    tag_svgs = []
    max_width = max_height = 0
    tags_per_row = args.columns
    num_tags = len(args.tag_files)
    rows = (num_tags + tags_per_row - 1) // tags_per_row
    tag_width = tag_height = None
    for i, tag_path in enumerate(args.tag_files):
        im = Image.open(tag_path).convert("RGBA")
        w, h = im.size
        tag_width = tag_width or w
        tag_height = tag_height or h
        pixels = im.load()
        col = i % tags_per_row
        row = i // tags_per_row
        x_offset = col * (w + 2)  # +2 for spacing
        y_offset = row * (h + 2)
        tag_svgs.append(draw_tag(x_offset, y_offset, w, h, pixels))
        max_width = max(max_width, x_offset + w)
        max_height = max(max_height, y_offset + h)
    svg_header = f'<svg width="{args.size}" height="{args.size}" viewBox="0 0 {max_width} {max_height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg_content = ''.join(tag_svgs)
    svg_footer = '</svg>\n'
    with open(args.out_file, 'w') as f:
        f.write(svg_header + svg_content + svg_footer)
    print(f"Saved combined SVG with {num_tags} tags to: {args.out_file}")
if __name__ == "__main__":
    main()

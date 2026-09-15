#!/usr/bin/env python3
"""Recreate the historical pay chart. Requires Pillow; not part of the site build."""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", required=True, help="Path to a sans-serif TTF font")
    args = parser.parse_args()
    image = Image.new("RGB", (1400, 1400), "#faf9f6")
    draw = ImageDraw.Draw(image)

    def text(x, y, label, size=30, color="#243b44", anchor="la"):
        draw.text((x, y), label, font=ImageFont.truetype(args.font, size), fill=color, anchor=anchor)

    text(65, 45, "Public versus private pay", 52)
    text(65, 113, "Average annual wages · United States · 2009", 32)
    left, plot_width = 470, 800

    def panel(title, rows, top):
        text(65, top, title, 34)
        start = top + 65
        bottom = start + len(rows) * 66
        for tick in range(0, 80001, 20000):
            x = left + tick / 80000 * plot_width
            draw.line((x, start - 8, x, bottom - 17), fill="#d9dedc", width=2)
            text(x, bottom, f"${tick // 1000}k" if tick else "$0", 25, "#56666c", "ma")
        for index, (label, value, private) in enumerate(rows):
            y = start + index * 66
            text(left - 22, y + 5, label, 29, anchor="ra")
            end = left + value / 80000 * plot_width
            draw.rectangle((left, y, end, y + 42), fill="#bc693b" if private else "#356776")
            text(end + 12, y + 5, f"${value:,}", 29)

    panel("Worker groups", [
        ("Federal government workers", 67756, False),
        ("State police", 61000, False),
        ("Local firefighters", 60572, False),
        ("State government workers", 48742, False),
        ("State legislative workers", 48129, False),
        ("Government (all types)", 47552, False),
        ("Private (total sector)", 45155, True),
        ("Local government workers", 43140, False),
        ("Local schools", 41113, False),
    ], 193)
    panel("Certified public accountants (CPA)", [
        ("Private sector CPA", 71216, True),
        ("Federal government CPA", 67531, False),
        ("Local government CPA", 64050, False),
    ], 930)
    text(65, 1288, "Historical figures reproduced from this article, which cites BLS (2009).", 27)
    text(65, 1332, "Group averages; not adjusted for differences in jobs or qualifications.", 27)
    destination = Path(__file__).resolve().parents[1] / "content/posts/public-versus-private-pay/images/fedpay.jpg"
    image.save(destination, quality=92, optimize=True)
    print(destination)


if __name__ == "__main__":
    main()

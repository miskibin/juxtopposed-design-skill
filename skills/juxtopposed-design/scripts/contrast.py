#!/usr/bin/env python3
"""WCAG 2.2 contrast checker. No dependencies.

Usage:
    python contrast.py "#141619" "#f8f9fa"
    python contrast.py "#e8eaed" "#0c0e12" "#9aa0a6" "#0c0e12"   # several fg/bg pairs

Guide: body text ~7:1 (AAA), secondary text >= 4.5:1 (AA), large text and UI boundaries >= 3:1.
"""

import re
import sys


def parse_hex(value: str) -> tuple[float, float, float]:
    h = value.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError(f"not a hex color: {value!r}")
    return tuple(int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(rgb: tuple[float, float, float]) -> float:
    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg: str, bg: str) -> float:
    a, b = sorted((luminance(parse_hex(fg)), luminance(parse_hex(bg))), reverse=True)
    return (a + 0.05) / (b + 0.05)


def grade(r: float) -> str:
    if r >= 7:
        return "AAA"
    if r >= 4.5:
        return "AA"
    if r >= 3:
        return "AA large text / UI only"
    return "FAIL"


def main(argv: list[str]) -> int:
    colors = argv[1:]
    if not colors or len(colors) % 2:
        print(__doc__)
        return 2
    for fg, bg in zip(colors[::2], colors[1::2]):
        r = ratio(fg, bg)
        print(f"{fg} on {bg}: {r:.2f}:1  {grade(r)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

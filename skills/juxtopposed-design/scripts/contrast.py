#!/usr/bin/env python3
"""WCAG 2.2 contrast checker. No dependencies.

Usage:
    python contrast.py "#141619" "#f8f9fa"         # one pair
    python contrast.py --audit tokens.css          # check the token pairs in a tokens.css file

Exit code 1 if any audited pair fails its minimum.
"""

import re
import sys

# (foreground token, background token, minimum ratio, label)
AUDIT_PAIRS = [
    ("--text-main", "--bg-base", 7.0, "body text on canvas (AAA)"),
    ("--text-main", "--bg-surface", 7.0, "body text on card (AAA)"),
    ("--text-muted", "--bg-base", 4.5, "muted text on canvas (AA)"),
    ("--text-muted", "--bg-surface", 4.5, "muted text on card (AA)"),
    ("--on-primary", "--primary", 4.5, "button label on primary"),
    ("--primary", "--bg-base", 4.5, "primary fill vs canvas"),
    ("--accent", "--bg-base", 4.5, "accent as text/link on canvas"),
    ("--accent", "--bg-surface", 4.5, "accent as text/link on card"),
    ("--on-accent", "--accent", 4.5, "label on accent fill"),
]


def parse_hex(value: str) -> tuple[float, float, float]:
    h = value.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6 or not re.fullmatch(r"[0-9a-fA-F]{6}", h):
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
        return "AA-large / UI"
    return "FAIL"


def blocks(css: str) -> dict[str, dict[str, str]]:
    """Return {'light': {...}, 'dark': {...}} hex tokens from a tokens.css file."""
    themes: dict[str, dict[str, str]] = {"light": {}, "dark": {}}
    for selector, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        selector = selector.strip()
        if ":root" not in selector or ":not(" in selector:  # the media-query copy duplicates [data-theme="dark"]
            continue
        theme = "dark" if 'data-theme="dark"' in selector else "light"
        if theme is None:
            continue
        for name, val in re.findall(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\b", body):
            themes[theme][name] = val
    themes["dark"] = {**themes["light"], **themes["dark"]}
    return themes


def audit(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        themes = blocks(f.read())
    failures = 0
    for theme, tokens in themes.items():
        print(f"\n[{theme}]")
        for fg, bg, minimum, label in AUDIT_PAIRS:
            if fg not in tokens or bg not in tokens:
                continue
            r = ratio(tokens[fg], tokens[bg])
            ok = r >= minimum
            failures += not ok
            mark = "ok  " if ok else "FAIL"
            print(f"  {mark} {r:5.2f}:1 (min {minimum}) {label}: {tokens[fg]} on {tokens[bg]}")
    print(f"\n{failures} failing pair(s)")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if len(argv) == 3 and argv[1] == "--audit":
        return audit(argv[2])
    if len(argv) == 3:
        r = ratio(argv[1], argv[2])
        print(f"{r:.2f}:1  {grade(r)}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Color architecture

## Principle: judge colors in context

Picking colors as isolated swatches is the cardinal mistake — on screen, colors interact through
area, adjacency and contrast. This is the idea behind the Realtime Colors approach: apply tokens
to a full-size page layout immediately and judge there. When you generate a palette, render it on
a real layout (or `examples/demo.html`) before committing.

## 60-30-10

Borrowed from compositional theory (the uneven color weights of Mondrian-style composition):

| Share | Role | Typical token |
|---|---|---|
| ~60% | Base background — breathing space, sets the temperature of the whole project | `--bg-base` |
| ~30% | Structural color — containers, borders, nav panels, intermediate hierarchy | `--bg-surface`, `--bg-raised`, `--border-subtle` |
| ≤10% | Accent + primary CTA — focus, conversion points, active states | `--primary`, `--accent` |

Scarcity is what gives the accent its power. If more than ~10% of the screen is accent, it stops guiding the eye.

## The 4-step palette algorithm

1. **Neutrals**: background + main text. These decide legibility and reading comfort.
2. **Primary**: main action buttons.
3. **Secondary**: cards, secondary controls.
4. **Accent**: tiny interactive details (focus rings, badges, active borders, links).

Total budget: **3 to 6** controlled color variables (semantic success/warning/danger excluded).

Primary has two valid strategies:
- **Monochrome primary** (default in `tokens.css`): primary = near-black in light / near-white in dark; color lives only in `--accent`. Very calm, editorial.
- **Brand primary**: a saturated brand hue for the main CTA; then accent becomes a complementary or analogous detail color. Use when brand recognition matters.

## Dark mode

Pure `#000000` + pure `#ffffff` = 21:1. On OLED this causes **halation** — bright text glyphs
optically bleed into the black around them, causing fatigue and headaches.

Professional dark mode is a stack of tinted graphites:

| Layer | Hex (cool) | Hex (warm alt.) | Use |
|---|---|---|---|
| base | `#0c0e12` | `#121110` | page canvas |
| surface | `#14171f` | `#1a1816` | cards, panels |
| raised | `#1a1d24`–`#1e2330` | `#22201d` | popovers, menus, active card |
| border | `rgba(255,255,255,.08)` | `rgba(255,240,220,.08)` | hairlines |
| text | `#e8eaed` | `#ece8e2` | body |
| muted | `#9aa0a6` | `#a39d94` | metadata |

Rules:
- Depth = **lighter surface for higher elevation**, not shadows.
- Lift primary/accent luminance 10–15% vs light mode so they keep energy on dark backgrounds.
- Desaturate very saturated hues slightly in dark mode (pastel/neon-ish accents read better).
- Never invert light mode mechanically.

## Contrast table (WCAG 2.2)

| Token | Role | Minimum | Light default | Dark default |
|---|---|---|---|---|
| `--bg-base` | canvas, negative space | reference | `#f8f9fa` (warm off-white) | `#0c0e12` (blue-tinted graphite) |
| `--text-main` | primary text | **≥ 7:1** (AAA) | `#141619` | `#e8eaed` |
| `--text-muted` | captions, metadata | ≥ 4.5:1 (AA) | `#687076` | `#9aa0a6` |
| `--primary` | main CTA fill | ≥ 4.5:1 vs bg (label vs fill too) | `#1e2024` | `#f1f3f4` |
| `--bg-surface` | cards | ≥ 3:1 for its **border** if the boundary carries meaning | `#ffffff` | `#14171f` |
| `--accent` | focus, badges, links | ≥ 4.5:1 when used as text, ≥ 3:1 as UI boundary | `#2563eb` | `#3b82f6` |

Verify any custom palette:

```bash
python scripts/contrast.py "#141619" "#f8f9fa"
python scripts/contrast.py --audit references/tokens.css
```

## Media-adaptive color

For players/galleries: derive a tint from the artwork (dominant color, lowered saturation and
luminance for dark mode), apply it to the background with a slow (400–800 ms) crossfade — this is
ambient mood, not UI feedback, so the 250 ms limit does not apply. Re-check text contrast against
the darkest and lightest possible tint, or place text on a scrim.

# Typography

Typography is the architectural skeleton of the interface: it communicates identity and organises
attention. Build a deliberate contrast between a **display voice** and a **text voice**.

## Pairings

| Role | Faces | Where to get them |
|---|---|---|
| Display (H1/H2, hero) | Syne, Clash Display, Cabinet Grotesk | Syne: Google Fonts. Clash Display, Cabinet Grotesk, General Sans: Fontshare (free) |
| Text (body, UI) | Inter, Plus Jakarta Sans, General Sans | Google Fonts / Fontshare |
| Technical (labels, metadata, numbers, code) | JetBrains Mono | Google Fonts |

Recommended combos:
- **Editorial / expressive**: Syne 700 + Inter 400/500.
- **Product / SaaS**: Plus Jakarta Sans 700 (headings) + Inter (body).
- **Developer / technical**: Cabinet Grotesk or Plus Jakarta Sans + JetBrains Mono for labels — monospace as a carrier of engineering discipline.
- **Calm / cozy**: General Sans throughout, weights doing the hierarchy.

Never use the display face for body copy. Never apply a signature style (dot-matrix, pixel) to
functional text.

## Modular scale

Each step = previous × ratio. Base 16 px.

| Step | Major Third 1.250 (default) | Perfect Fourth 1.333 (marketing) | Minor Second 1.067 (dense admin) |
|---|---|---|---|
| −1 (micro) | 12.80 | 12.00 | 15.00 (go two steps down, 14.06, for micro labels) |
| 0 (body) | 16.00 | 16.00 | 16.00 |
| 1 (H4 / card title) | 20.00 | 21.33 | 17.07 |
| 2 (H3) | 25.00 | 28.43 | 18.21 |
| 3 (H2) | 31.25 | 37.90 | 19.43 |
| 4 (H1) | 39.06 | 50.52 | 20.73 |
| 5 (display) | 48.83 | 67.34 | 22.12 |
| 6 (hero) | 61.04 | 89.76 | 23.60 |

Round to 0.5 px or express in rem (`1.25rem`, `1.953rem`, `2.441rem`, `3.052rem`, `3.815rem`).
Use `clamp()` for fluid hero sizes, e.g. `font-size: clamp(2.441rem, 5vw + 1rem, 3.815rem)`.

## Hierarchy spec (Major Third)

| Rank | Face | Size | Weight | Line-height | Tracking | Notes |
|---|---|---|---|---|---|---|
| Display / Hero H1 | Syne / Clash Display | 48.83–61.04 px | 700 | 1.1 | −0.02 to −0.03em | max 2–3 lines |
| Section H2 | Plus Jakarta Sans / Syne | 31.25–39.06 px | 700 | 1.2 | −0.01em | standalone blocks |
| Card title H3 | Plus Jakarta Sans | 20–25 px | 600 | 1.3 | 0 | one line, high contrast |
| Body | Inter / General Sans | 16 px | 400 | 1.5–1.6 | 0 | `max-width: 65ch` |
| Microcopy / labels | JetBrains Mono / Inter | 12.8 px | 500 | 1.4 | +0.02 to +0.06em if uppercase | short phrases only |

## Measure and rhythm

- 45–75 characters per line → `max-width: 60ch–65ch` on text containers.
- Paragraph spacing ≈ 1em; heading top margin ≈ 2× bottom margin (headings belong to what follows).
- Vertical spacing on the 4/8 px scale: 4, 8, 12, 16, 24, 32, 48, 64, 96.
- Use `font-variant-numeric: tabular-nums` for anything that updates (timers, prices, tables).
- `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs.

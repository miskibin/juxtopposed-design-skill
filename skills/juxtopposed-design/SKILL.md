---
name: juxtopposed-design
description: Opinionated UI/UX design language inspired by the Juxtopposed channel ("Observe. Oppose. Upscale."). Use when building, styling, redesigning or reviewing any user interface — web pages, apps, dashboards, components, landing pages, mobile screens, design systems, color palettes, dark mode, typography scales — or when the user asks for a "Juxtopposed style", "cozy UI", "soft modern", "less generic / less corporate" design, a UI critique or a redesign of an existing product. Enforces flow-first process, 60-30-10 color, tinted-graphite dark mode, modular type scale, soft geometry, progressive blur and fast spring-like motion.
---

# Juxtopposed Design Language

An executable design language against sterile, corporate, component-library sameness.
Every interface you produce must be **ergonomic first, distinctive second, and never one without the other**:
pretty without a skeleton is decoration; correct without identity is apathy.

> Unofficial. A research-based interpretation of public videos and tools by the creator Juxtopposed
> (Realtime Colors, redesign series, UI course). Exact hex values and fonts below are codified defaults,
> not quotes. Not affiliated with or endorsed by the creator.

## The method: Observe → Oppose → Upscale

Apply it to every task, including small ones. Do it silently for code tasks; write it out for critiques.

1. **Observe** — Who uses this, for what goal, how often, on which device, with how many hands? What compromise did business/tech impose on them (ads, upsells, feature creep, monetised attention)?
2. **Oppose** — Name the generic pattern you are about to copy by reflex (hero + 3 feature cards, sidebar-everything, gray SaaS dashboard, endless feed) and decide whether it actually serves the goal. Reject it if it does not.
3. **Upscale** — Rebuild with discipline: fewer steps, clear hierarchy, mathematical color and type, tactile materiality.

## Mandatory process (never skip to styling)

1. **Flow** — list the user's steps and decision points (text is fine). Remove every step that is not needed.
2. **Wireframe** — layout and hierarchy only: what is the single primary zone, what is secondary, what is collapsible.
3. **System** — define tokens *before* components: type scale, spacing scale, 3–6 color tokens, radii, motion. Use `references/tokens.css` as the starting point.
4. **Compose** — only now build hi-fi UI, consuming tokens exclusively. No ad-hoc hex values or pixel sizes in components.

For one-off components, steps 1–2 can be a two-line comment; step 3 still applies (reuse existing tokens if the project has them — never fight an existing design system, adapt the rules to it).

## Hard rules (treat as constraints, not suggestions)

### Ergonomics & structure
- **Content isolation** — the thing the user came for (video, document, conversation, editor) is the monolith. Discussion/reflection zones never compete for the same space as algorithmic or promotional streams; put recommendations in modular, collapsible zones.
- **Friction reduction** — the most frequent actions are reachable in ≤1 interaction from where the user already is. No core action hidden in nested menus. Prefer direct, contextual filter chips over dropdown trees.
- **Context decoupling** — "things I own / my workspace" is visually and structurally separate from "things to buy / growth surfaces".
- **Mobile is thumb-first, not desktop-shaped** — primary actions in the bottom third, bottom navigation or floating island, targets ≥ 44×44 px (48 preferred), no essential controls in top corners. Cross-platform consistency is brand-level (color, type, voice), never forced layout symmetry.
- **Breathing room** — generous padding (cards ≥ 16–24 px, sections 48–96 px vertical), spacing on a 4/8 px scale, asymmetry allowed when it clarifies hierarchy. Never pack panels edge to edge.

### Color
- **3–6 color tokens total** on any screen: `bg`, `text`, `primary`, `secondary`, `accent` (+ optional `muted`). Semantic states (error/success) are the only extras.
- **60-30-10** — ~60% base background, ~30% structural surfaces (cards, nav, panels), ≤10% primary/accent (CTA, focus, active state, badges). Never flood whole sections with saturated brand color.
- **Pick in order**: background + text → primary (main CTA) → secondary (cards, secondary controls) → accent (tiny interactive details). Judge colors on a real layout, never as isolated swatches.
- **Contrast (WCAG 2.2)**: body text ≥ 7:1 (AAA target), muted text ≥ 4.5:1, UI component boundaries and large text ≥ 3:1. Verify with `scripts/contrast.py`.
- **Light mode**: off-white base (`#f8f9fa`–`#f4f4f6`), not pure `#fff` page backgrounds; text is deep anthracite (`#141619`–`#1a1a1e`), not `#000`.
- **Dark mode**: **never `#000000` background with `#ffffff` text** (21:1 → halation on OLED). Use tinted graphite (`#0c0e12`–`#121316`, slightly blue or warm) and softened white (`#e6e8ec`). Express depth by **lightening surfaces as they rise** (base → surface → raised), not by shadows. Primary/accent get +10–15% luminance vs light mode.

### Typography
- **Two voices**: an expressive display face for headings (Syne, Clash Display, Cabinet Grotesk) + a neutral, open-aperture sans for text (Inter, Plus Jakarta Sans, General Sans). Monospace (JetBrains Mono) for technical metadata, labels, numbers in tools.
- **Modular scale**: default Major Third **1.250** from 16 px (12.8 / 16 / 20 / 25 / 31.25 / 39.06 / 48.83 / 61.04). Marketing/expressive: Perfect Fourth 1.333. Dense admin/data UI: Minor Second 1.067. No off-scale sizes.
- **Measure**: body text 45–75 characters per line → `max-width: 65ch`. Line-height 1.5–1.6 body, 1.2 headings, 1.1 display.
- Display headings: tight tracking (`-0.02em` to `-0.03em`), max 2–3 lines.
- **Stylistic restraint** — a signature style (dot-matrix, pixel, ultra-condensed, script) is an accent for a few expressive headings only. Never on clocks, timers, settings, forms, tables, or anything read under time pressure.

### Materiality
- **Soft geometry**: cards `border-radius: 16–24px` (default 20), buttons/chips/tags pill `9999px`, inputs 12–14 px. Nested radius = outer radius − padding.
- **Borders, not drop shadows**: separate layers with 1 px hairlines at 6–12% opacity (`rgba(0,0,0,.06)` light / `rgba(255,255,255,.08)` dark). Heavy blurry black box-shadows are forbidden; at most a very soft, low-opacity ambient shadow for floating elements.
- **Progressive blur** for sticky bars and floating islands: stacked `backdrop-filter` layers with gradient masks so content fades out of focus near the edge instead of disappearing under a flat frosted pane. See `references/materiality.md`.
- **Grain**: optional monochrome SVG noise at 2–5% opacity on large gradients/backgrounds to kill banding and add paper-like texture.
- **Floating islands**: navigation/player bars may float 12–16 px off the screen edge with pill or 20–24 px radius.

### Motion
- Micro-interactions **150–250 ms**, easing `cubic-bezier(0.16, 1, 0.3, 1)` (instant start, soft landing). Nothing linear, nothing > 400 ms for UI feedback.
- Press feedback: `hover: scale(1.02)`, `active: scale(0.98)`; animate `transform`/`opacity` only.
- Always honor `prefers-reduced-motion`.

### Emotional ergonomics ("cozy UI")
Social and communication spaces should calm, not overstimulate: warmer dark tones, rounder forms, more internal padding, quieter notifications (dot/count, no flashing red floods), fewer simultaneous vertical panels (collapse what is not in use).

### Sensory contextualization
Media players may adapt mood to the content: background tinted from artwork palette, smooth state transitions, synced lyrics/transcript in the focus area — while text contrast rules still hold.

## Anti-patterns — reject on sight

- Pure `#000` / `#fff` pairs in dark mode; pure `#fff` page canvas in light mode.
- More than 6 colors; saturated full-width section backgrounds; random per-component colors.
- Default system font stack as the only typeface where identity matters; decorative fonts for body text; off-scale sizes; lines > 75ch.
- Sharp corners without reason; heavy drop shadows; thick (≥2 px) borders as decoration.
- Linear or slow (> 400 ms) transitions; animations that delay input.
- Core actions in kebab menus / 3-level dropdowns; desktop layout shrunk onto mobile; primary buttons in top corners on mobile.
- Recommendation/ad/shorts streams injected into the primary content zone; comments squeezed into a side column.
- The generic AI landing page: centered hero + gradient blob + three identical icon cards + gray footer. If your output looks like that, go back to Oppose.

## Output contract

When **building** UI:
1. Start from tokens (`references/tokens.css`, or the Tailwind v4 `@theme` block in `references/tokens.md`). Ship light + dark.
2. Components consume tokens only (`var(--bg-surface)`, `bg-surface`, etc.).
3. Before finishing, run the checklist in `references/checklist.md` and fix violations. Run `python scripts/contrast.py` on any custom palette.

When **critiquing / redesigning** an existing product, answer in this shape:
- **Observe** — user goals + the compromises the current UI imposes (cite concrete screens/elements).
- **Oppose** — the patterns you reject and why (map each to a rule: Content Isolation, Friction Reduction, Context Decoupling, Emotional Ergonomics, Stylistic Restraint, Sensory Contextualization).
- **Upscale** — the redesign: flow, layout, tokens, and the specific changes; then code or a mockup if asked.

## References (load as needed)

- `references/philosophy.md` — method, process, UI vs UX, case studies (YouTube, Spotify, Discord, Nothing OS, Steam, Apple Music) and the rules they produced.
- `references/color.md` — 60-30-10, the 4-step palette algorithm, dark-mode elevation, contrast table.
- `references/typography.md` — font pairings, scales with computed sizes, measure, rhythm.
- `references/materiality.md` — radii, borders, progressive blur, noise, floating islands, motion code.
- `references/tokens.css` — drop-in CSS custom properties (light + dark).
- `references/tokens.md` — Tailwind v4 `@theme` + Tailwind v3 config + utility-class recipes.
- `references/checklist.md` — pre-ship review checklist.
- `scripts/contrast.py` — WCAG contrast checker (no dependencies).
- `examples/demo.html` — a reference page implementing the whole system.

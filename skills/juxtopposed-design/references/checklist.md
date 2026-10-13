# Pre-ship checklist

Run through this before declaring any UI done. Fix every "no".

## Method
- [ ] I can state the user's primary goal on this screen in one sentence.
- [ ] I named at least one generic pattern I rejected and why (Oppose).
- [ ] The primary content is a clear monolith; secondary/promotional streams are collapsible or separate.
- [ ] The most frequent action is reachable in one interaction.

## Layout & ergonomics
- [ ] Spacing uses the 4/8 scale; cards have ≥ 16 px padding; sections breathe.
- [ ] Mobile: primary actions in the bottom third; touch targets ≥ 44 px; nothing essential in top corners.
- [ ] Mobile layout was designed for one hand, not shrunk from desktop.
- [ ] Owned content and sales/growth surfaces are separated.

## Color
- [ ] 3–6 color tokens (+ semantic states). No ad-hoc hex values in components.
- [ ] Roughly 60/30/10; accent ≤ 10% of the screen.
- [ ] Body text ≥ 7:1, muted ≥ 4.5:1, meaningful UI boundaries ≥ 3:1 (`scripts/contrast.py`).
- [ ] No pure `#000` background or pure `#fff` text in dark mode; no pure `#fff` page canvas in light mode.
- [ ] Dark mode depth comes from lighter surfaces, not shadows.
- [ ] Both light and dark themes ship and were looked at.

## Typography
- [ ] Display face for headings only; neutral sans for body; mono only for technical labels.
- [ ] All sizes come from the modular scale.
- [ ] Text containers ≤ 65ch; body line-height 1.5–1.6.
- [ ] Signature/decorative styles are not used on functional text (clocks, forms, settings, tables).

## Materiality
- [ ] Cards 16–24 px radius; buttons/chips pill.
- [ ] Layer separation via 1 px hairlines ≤ 12% opacity; no heavy drop shadows.
- [ ] Sticky/floating bars use progressive blur or a tinted scrim, with legible text.

## Motion & accessibility
- [ ] UI transitions 150–250 ms with `cubic-bezier(0.16, 1, 0.3, 1)`; none linear, none > 400 ms.
- [ ] Only transform/opacity/color animate; input is never blocked by animation.
- [ ] `prefers-reduced-motion` respected.
- [ ] Visible `:focus-visible` ring in accent; full keyboard navigation; semantic HTML and labels.

## Emotional ergonomics
- [ ] Notifications are quiet (dot/count), not flooding red.
- [ ] No more panels open at once than the task needs.
- [ ] Would this feel calm to a non-technical user?

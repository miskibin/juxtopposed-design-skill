# Digital materiality: geometry, blur, grain, motion

Soft modernism meets organic neo-brutalism: not flat and soulless, not skeuomorphic — tactile,
precise, and performant.

## Geometry

| Element | Radius |
|---|---|
| Cards, panels, modals | 16–24 px (default 20) |
| Buttons, chips, tags, segmented controls, search bars | 9999px (pill) |
| Inputs, small tiles | 12–14 px |
| Thumbnails inside cards | outer radius − card padding (min 8 px) |
| Floating islands (nav, player) | pill or 24 px |

## Separation without shadows

```css
.card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);   /* 6–12% opacity hairline */
  border-radius: var(--radius-card);
}
/* Allowed for floating elements only: very soft ambient shadow */
.floating { box-shadow: 0 1px 2px rgb(0 0 0 / .04), 0 8px 24px rgb(0 0 0 / .06); }
```

In dark mode drop shadows entirely; raise the surface color instead (`--bg-raised`).

## Progressive blur

A flat `backdrop-filter: blur()` pane makes content vanish abruptly under a milky slab. Progressive
blur stacks several blur layers, each masked to a band, so content loses focus gradually toward the
edge — like a lens.

```html
<header class="nav">
  <div class="pblur" aria-hidden="true">
    <div></div><div></div><div></div><div></div>
  </div>
  <nav class="nav-inner">…</nav>
</header>
```

```css
.nav { position: sticky; top: 0; z-index: 10; }
.pblur { position: absolute; inset: 0 0 -32px 0; pointer-events: none; }
.pblur > div { position: absolute; inset: 0; }
.pblur > div:nth-child(1) { backdrop-filter: blur(1px);
  mask-image: linear-gradient(to top, transparent 0%, #000 25%, #000 100%); }
.pblur > div:nth-child(2) { backdrop-filter: blur(2px);
  mask-image: linear-gradient(to top, transparent 25%, #000 50%, #000 100%); }
.pblur > div:nth-child(3) { backdrop-filter: blur(4px);
  mask-image: linear-gradient(to top, transparent 50%, #000 75%, #000 100%); }
.pblur > div:nth-child(4) { backdrop-filter: blur(8px);
  mask-image: linear-gradient(to top, transparent 75%, #000 100%); }
/* tint so text stays legible */
.pblur::after { content: ""; position: absolute; inset: 0;
  background: linear-gradient(to bottom, var(--bg-base) 0%, transparent 100%); opacity: .7; }
```

For a bottom bar, flip the gradient direction (`to bottom`). Add `-webkit-backdrop-filter` and
`-webkit-mask-image` for Safari. Keep to ≤4 layers for performance.

## Grain

Monochrome SVG noise removes gradient banding and adds a paper-like surface.

```css
.grain::before {
  content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 100;
  opacity: .035; mix-blend-mode: multiply;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
[data-theme="dark"] .grain::before { mix-blend-mode: screen; opacity: .04; }
```

## Floating islands

```css
.island {
  position: fixed; left: 50%; bottom: 16px; transform: translateX(-50%);
  display: flex; gap: 4px; padding: 6px;
  background: color-mix(in oklab, var(--bg-surface) 82%, transparent);
  backdrop-filter: blur(16px) saturate(1.4);
  border: 1px solid var(--border-subtle); border-radius: 9999px;
}
```

On mobile, the island holds the 3–5 primary destinations in the thumb zone.

## Motion

| Interaction | Duration | Easing |
|---|---|---|
| Hover, press, toggle, focus | 150–200 ms | `cubic-bezier(0.16, 1, 0.3, 1)` |
| Menus, popovers, tab indicator | 200–250 ms | same |
| Page/sheet transitions | ≤ 300 ms | same |
| Ambient (media tint, background) | 400–800 ms | ease-in-out — not UI feedback |

```css
:root { --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1); --dur-fast: 150ms; --dur: 200ms; --dur-slow: 250ms; }
.btn { transition: transform var(--dur) var(--ease-out-expo), background-color var(--dur) var(--ease-out-expo); }
.btn:hover  { transform: scale(1.02); }
.btn:active { transform: scale(0.98); }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition-duration: 1ms !important; animation-duration: 1ms !important; }
}
```

Animate only `transform` and `opacity` (and colors). Never delay input behind an animation.

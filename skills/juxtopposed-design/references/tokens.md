# Tokens for Tailwind and utility-class recipes

Values mirror `tokens.css`. Load `tokens.css` (or paste its `:root` blocks) first; the Tailwind
config below only maps utilities onto those variables, so light/dark switching stays in CSS.

## Tailwind v4 (`@theme`)

```css
@import "tailwindcss";
@import "./tokens.css";

@custom-variant dark (&:where([data-theme="dark"], [data-theme="dark"] *));

@theme inline {
  --color-base: var(--bg-base);
  --color-surface: var(--bg-surface);
  --color-raised: var(--bg-raised);
  --color-line: var(--border-subtle);
  --color-fg: var(--text-main);
  --color-muted: var(--text-muted);
  --color-primary: var(--primary);
  --color-on-primary: var(--on-primary);
  --color-accent: var(--accent);

  --font-display: var(--font-display);
  --font-sans: var(--font-sans);
  --font-mono: var(--font-mono);

  --radius-card: var(--radius-card);
  --ease-juxt: cubic-bezier(0.16, 1, 0.3, 1);
}
```

## Tailwind v3 (`tailwind.config.js`)

```js
export default {
  darkMode: ["selector", '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        base: "var(--bg-base)", surface: "var(--bg-surface)", raised: "var(--bg-raised)",
        line: "var(--border-subtle)", fg: "var(--text-main)", muted: "var(--text-muted)",
        primary: "var(--primary)", "on-primary": "var(--on-primary)", accent: "var(--accent)",
      },
      fontFamily: { display: "var(--font-display)", sans: "var(--font-sans)", mono: "var(--font-mono)" },
      borderRadius: { card: "20px" },
      transitionTimingFunction: { juxt: "cubic-bezier(0.16, 1, 0.3, 1)" },
      maxWidth: { measure: "65ch" },
    },
  },
};
```

## Recipes

| Element | Classes |
|---|---|
| Page | `bg-base text-fg font-sans antialiased` |
| Layout shell | `max-w-7xl mx-auto px-4 md:px-12 py-12 md:py-24` |
| Split layout | `flex flex-col md:flex-row gap-8 items-start` |
| Card | `bg-surface border border-line rounded-card p-6` |
| Raised card (dark depth) | `bg-raised border border-line rounded-card p-6` |
| Hero heading | `font-display font-bold tracking-tight text-4xl md:text-6xl leading-[1.1]` |
| Section heading | `font-display font-bold text-3xl leading-tight` |
| Body | `text-base leading-relaxed max-w-measure` |
| Meta label | `font-mono text-xs uppercase tracking-wider text-muted` |
| Primary button | `rounded-full bg-primary text-on-primary px-5 py-2.5 font-medium transition duration-200 ease-juxt hover:scale-[1.02] active:scale-[0.98]` |
| Secondary button | `rounded-full border border-line bg-surface px-5 py-2.5 transition duration-200 ease-juxt hover:bg-raised` |
| Chip / filter | `rounded-full border border-line px-3 py-1 text-sm aria-pressed:bg-primary aria-pressed:text-on-primary` |
| Input | `rounded-xl border border-line bg-surface px-4 py-2.5 focus-visible:outline-2 focus-visible:outline-accent` |
| Badge | `rounded-full bg-accent/10 text-accent px-2 py-0.5 text-xs font-medium` |
| Floating island | `fixed bottom-4 left-1/2 -translate-x-1/2 rounded-full border border-line bg-surface/80 backdrop-blur-xl p-1.5 flex gap-1` |

Forbidden utilities: `bg-black` page backgrounds, `text-white` body text in dark mode, `shadow-xl`/`shadow-2xl`, `border-2`+ as decoration, `duration-500`+ on UI feedback, `ease-linear`.

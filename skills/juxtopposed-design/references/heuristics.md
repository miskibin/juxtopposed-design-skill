# Rules of thumb

Numbers that express the principles. They are starting points with reasons, not a house style:
adapt them to the product, the brand and any existing design system. When a rule and the user's
goal conflict, the goal wins — but say why you are breaking the rule.

## Color

| Heuristic | Why |
|---|---|
| Decide colors on a realistic layout, not as swatches. | Colors change with area, neighbours and contrast. |
| Build in order: background + text → primary action → secondary surfaces → accent. | Readability first; emphasis last. |
| Keep the palette small: roughly 3–6 colors with clear roles (plus semantic states). | Every extra color dilutes meaning. |
| Distribute roughly **60 / 30 / 10**: calm base, structural surfaces, strong accent. | Scarcity is what lets the accent guide the eye. |
| Body text around 7:1 contrast, secondary text at least 4.5:1, meaningful UI boundaries at least 3:1 (WCAG). | Comfortable and accessible reading. Check with `scripts/contrast.py`. |
| Avoid extremes: not pure white canvases in light mode, not pure black with pure white in dark mode. | Maximum contrast is harsh; on OLED it causes halation and fatigue. |
| In dark mode, show depth by making higher layers slightly lighter; slightly tint the darks (cool or warm). | Shadows barely read on dark backgrounds; tinted darks feel intentional, not void. |
| Lift accents a little in dark mode. | Saturated colors lose energy on dark surfaces. |

## Typography

| Heuristic | Why |
|---|---|
| Pair an expressive voice (headlines, key moments) with a neutral, highly legible voice (everything else); optionally a monospace for technical detail. | Identity and readability without trading one for the other. |
| Use a modular scale: ~1.25 by default, ~1.33 for expressive/marketing pages, ~1.07 for dense tools. | Consistent, harmonious hierarchy; the ratio sets the drama. |
| Lines of about 45–75 characters (≈ 60–65ch containers). | The eye loses its place on longer lines. |
| Body line-height ~1.5, headings tighter. | Text breathes; headings stay compact. |
| Never put a decorative or signature style on functional text. | Style must not slow down reading under pressure. |

## Space and layout

| Heuristic | Why |
|---|---|
| Use a consistent spacing scale (e.g. multiples of 4 or 8). | Rhythm and coherence; faster decisions. |
| Give content generous breathing room; avoid panels packed edge to edge. | Density is stress. |
| One clear primary zone per screen; secondary content in its own, ideally collapsible, zones. | Attention needs a center. |
| On phones, primary actions within thumb reach (lower part of the screen), touch targets ≥ ~44 px. | One-handed use is the real context. |

## Form and material

| Heuristic | Why |
|---|---|
| Prefer softened geometry (rounded containers, pill-shaped controls) unless the brand calls for sharpness. | Sharp, hard forms read as cold and aggressive. |
| Separate layers with subtle, thin lines and tonal steps rather than heavy shadows. | Heavy shadows look dirty and dated; subtle edges stay clean. |
| Blur under floating or sticky elements should fade progressively, not cut off abruptly. | Mimics a lens; content recedes gently instead of disappearing. |
| A faint texture or grain can add warmth and remove gradient banding. | Tangible, less sterile surfaces. |

## Motion

| Heuristic | Why |
|---|---|
| Interface feedback in roughly 150–250 ms. | Feels immediate without being abrupt. |
| Fast start, gentle settle (ease-out curves such as `cubic-bezier(0.16, 1, 0.3, 1)`); avoid linear and long transitions. | Feels physical and responsive. |
| Small press/hover responses (slight scale or tone change). | The interface answers the touch. |
| Animation never blocks input; always honor reduced-motion settings. | Motion serves the user, not the other way round. |

# Philosophy, process and case studies

## Why this language exists

The modern web converges on one sterile template: the same component library, the same gray SaaS
dashboard, the same feed. Products optimise for engagement and monetisation, and the interface
absorbs the cost — attention is treated as a resource to extract. This design language is a
methodical opposition to that homogenisation.

## Observe. Oppose. Upscale.

A three-step analytic frame, not a slogan:

| Step | Question | Output |
|---|---|---|
| Observe | How do people actually use this? Which compromises were imposed by business or tech teams? | A list of user goals, habits and frictions |
| Oppose | Which patterns are copied by reflex? Which component-library defaults strip emotion from the product? | A list of rejected patterns, each with a reason |
| Upscale | How do we raise quality? | Ergonomics + mathematical color discipline + tactile digital materiality |

## UI vs UX, without jargon

- **UI** — everything the eye registers: palette, typographic micro-architecture, buttons, icons.
- **UX** — the navigation logic and information architecture deciding how effortlessly a person reaches their goal.
- Never treat them separately. Visual appeal without an ergonomic skeleton is useless decoration; a functionally correct interface without identity produces apathy and cognitive fatigue.

## The four-stage process

High-fidelity styling is **deliberately postponed**.

1. **User flow** — the sequence of mental states and decision steps, with no aesthetics.
2. **Low-fidelity wireframes** — verify spatial hierarchy and relationships between components.
3. **Modular design system** — fixed type scale, mathematical spacing system, responsive color tokens.
4. **Composition + interactive prototype** — the logical execution of decisions already made.

## Platforms

A mobile interface must first be comfortable to operate **with one hand**, and only secondarily
resemble its desktop version. Forced cross-platform symmetry that ignores thumb reach is a corporate
anti-pattern. Consistency lives in brand tokens (color, type, voice), not in identical layouts.

Thumb zones (portrait phone, one-handed):
- **Easy**: bottom-center and lower middle → primary actions, navigation, player controls.
- **Stretch**: middle band and upper-middle → content, secondary actions.
- **Hard**: top corners → nothing essential (close/back may also be gestures).

## Case studies → rules

| Product | Diagnosed problem | Redesign move | Rule |
|---|---|---|---|
| YouTube | Recommendation grid crowds the watch page; comments squeezed into a narrow side column; Shorts injected into long-form flow; compulsive scrolling by design. | Video as the central monolith of attention; wide, readable comments under the video; recommendations in modular, collapsible zones. | **Content Isolation** — discussion and reflection never compete for the same operating space as the algorithmic stream. |
| Spotify | Library fragmentation; playlist management buried in nested menus; podcasts blurring the music catalogue. | Unified card-based library; direct contextual filter chips; critical player controls surfaced; the bottom player as a flexible command center with strict metadata hierarchy. | **Friction Reduction** — media tools minimise intermediate interactions for the most frequent actions. |
| Discord | Cold, technical, claustrophobic; too many vertical panels; aggressive notifications; high entry threshold for non-technical users. | Rounder geometry, warmer dark tones, more internal padding, fewer simultaneous stimuli. | **Emotional Ergonomics** — social spaces build psychological comfort through soft form and reduced stimulus density. |
| Nothing OS | Dot-matrix type forced onto every level of the system, including clocks, timers and settings; decoding speed drops. | Dot-matrix reserved for a few expressive headings; system communication in a neutral, instantly readable sans. | **Stylistic Restraint** — a brand signature may never reduce the legibility or usability of critical functions. |
| Steam | Outdated store architecture mixed with the game library; poor type legibility; navigation chaos. | Full separation of the store from the user's library; modern cards optimised for wide screens. | **Context Decoupling** — the module managing what the user owns is visually and functionally separate from aggressive sales surfaces. |
| Apple Music | Rigid catalogue structures; lyrics hard to reach; no immersive link between mood and album. | Fluid state transitions; dynamic backgrounds from the cover palette; synced lyrics in the center. | **Sensory Contextualization** — media interfaces adapt their visual mood to the medium being presented. |

## Using the case studies

When redesigning anything, ask which of the six rules the current product violates, and say so
explicitly. The rules generalise: a project-management tool, a bank app, an IDE — each has a
primary "monolith" (content isolation), frequent actions (friction), owned-vs-sold contexts
(decoupling), a social layer (emotional ergonomics), a brand signature (restraint) and a medium
(contextualization).

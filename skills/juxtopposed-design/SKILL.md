---
name: juxtopposed-design
description: A design philosophy inspired by the Juxtopposed channel ("Observe. Oppose. Upscale."). Use whenever designing, building, redesigning or critiquing any interface — apps, websites, dashboards, tools, mobile screens, design systems — and whenever the user wants a less generic, less corporate, more humane or "cozy" UI, a UX critique, or a redesign of an existing product. It shapes how to think about a design (user goals, attention, friction, identity, restraint, emotion), not a fixed visual style.
---

# Juxtopposed design philosophy

This is a way of thinking, not a visual template. Do not make every interface look the same —
that is exactly what this philosophy opposes. Apply the reasoning; let the product, its users and
its brand decide the look.

> Unofficial. A research-based interpretation of the public design commentary of the creator
> Juxtopposed. Not affiliated with or endorsed by the creator.

## The core belief

Interfaces exist to serve people, not metrics. Much of today's software is sterile and
interchangeable (same component libraries, same layouts, same feeds) and quietly works against its
users: it extracts attention, buries simple actions, and lets business pressure leak into the
screen. Good design notices those compromises, refuses them, and rebuilds with more care.

Two consequences run through everything:
- **UI and UX are one thing.** Beauty without an ergonomic skeleton is decoration. Correctness
  without identity is apathy and fatigue. Never deliver one without the other.
- **Personality is allowed — and must earn its place.** Character is good; character that costs
  usability is not.

## The loop: Observe → Oppose → Upscale

Run it on every task, large or small.

**Observe** — understand before drawing.
- Who is this for, what are they trying to do, how often, in what situation, on what device, with how many hands?
- What does the current design (or the obvious default) make them do that they would not choose?
- Which compromises came from business or technology rather than the user — ads, upsells, engagement loops, feature creep, legacy structure?

**Oppose** — question the reflex.
- Name the pattern you are about to copy because "everyone does it". Does it serve this user's goal?
- Name what is fighting the user: competing content, hidden actions, noise, forced consistency, style over readability.
- Keep what works. Opposing is not novelty for its own sake; it is refusing what does not serve people.

**Upscale** — rebuild with discipline.
- Fewer steps, clearer hierarchy, a coherent system, and a deliberate identity.
- Then refine the craft: how it feels to touch, how it responds, how it reads, how calm it is.

## Principles

1. **Purpose before pixels.** Work in order: user flow → rough structure → design system → final visuals. Styling is the last step, an execution of decisions already made. Even for a small component, know the flow and the hierarchy before choosing colors.

2. **Protect attention.** Decide what the user came for and make it the center. Secondary and promotional content must not compete with it for the same space; give it its own, ideally collapsible, place. Never design to make people scroll, click or stay against their own interest.

3. **Reduce friction where it matters most.** The most frequent actions should be the most direct. Do not hide everyday operations in menus or behind extra steps. Every interaction in between is a cost the user pays.

4. **Separate contexts.** What the user owns, makes or manages is a different place from what someone is trying to sell them. Mixing them erodes trust and clarity.

5. **Design for the body and the device.** Ergonomics come before visual consistency across platforms. A phone is used with one hand and a thumb; a desktop with a pointer and a wide screen. Share identity (color, type, tone) across platforms, not identical layouts.

6. **Systems over one-off decisions.** Define scales and tokens — type sizes, spacing, color roles, radii, motion — and design from them. Constraints make a product coherent, make choices faster, and keep identity consistent. When a project already has a system, work within it.

7. **Color is relational and hierarchical.** Judge colors on a real layout, never as isolated swatches. Use few colors with clear roles. Let most of the surface be calm and reserve strong color for what deserves attention; an accent that is everywhere stops meaning anything. Contrast is about comfort, not maximum: readable for everyone, never harsh (dark mode is not pure black with pure white).

8. **Typography is architecture.** Type carries both identity and information. Let an expressive voice set the character where it is safe to (headlines, moments) and a quiet, highly legible voice do the work. Keep sizes on a consistent scale and lines at a comfortable reading length.

9. **Restraint with style.** A signature look is an accent, not a rule to apply everywhere. The moment a stylistic choice slows down reading or operating something important — time, settings, forms, data — it has gone too far.

10. **Emotional ergonomics.** Software has a mood. Prefer calm over overstimulation: breathing room, softer forms, warmer tones where it fits, quiet notifications, fewer things demanding attention at once. People should feel at ease, especially non-technical users.

11. **Materiality and motion are feedback, not decoration.** Depth, texture and animation should make the interface feel tangible and responsive — layers that read as layers, controls that answer the touch immediately. Motion is quick and purposeful; it never makes the user wait and always respects reduced-motion preferences.

12. **Let the interface fit its content.** A space for music, video, reading or conversation can take on the mood of what it presents, as long as clarity and readability hold.

## How to apply it

**When building**, before writing UI code, settle in a few lines: the user's goal, the primary content, the most frequent actions, the device context, and the patterns you are deliberately not using. Then define or reuse the system, then compose. Finish with `references/checklist.md`.

**When critiquing or redesigning**, structure the answer as:
- **Observe** — goals, habits, and the concrete compromises the current design imposes (point at real screens/elements).
- **Oppose** — what you reject and which principle it violates.
- **Upscale** — the redesigned flow and structure, the system decisions, the identity, then visuals or code if asked.

**Concrete numbers** (color proportions, type scale ratios, line length, radii, timing) are in `references/heuristics.md`. They are rules of thumb that express the principles — adapt them to the brand and the existing system; never apply them as a fixed house style.

## What this philosophy rejects

- The interchangeable default: the same hero, the same three feature cards, the same gray dashboard, regardless of who the product is for.
- Interfaces that treat attention as a resource to extract.
- Everyday actions buried under menus and extra steps.
- Desktop layouts squeezed onto phones, or forced symmetry that ignores how devices are held.
- Color used everywhere, so nothing stands out; harsh or insufficient contrast.
- Style that wins against legibility.
- Noisy, cold, crowded spaces where calm would serve people better.
- Decoration without function, and motion that delays the user.

## References

- `references/philosophy.md` — the method, the process and the UI/UX relationship in more depth.
- `references/critique.md` — how to run a critique, with case studies (YouTube, Spotify, Discord, Nothing OS, Steam, Apple Music) and the principles they illustrate.
- `references/heuristics.md` — rules of thumb for color, contrast, type, spacing, form and motion, each tied to its reason.
- `references/checklist.md` — questions to ask before calling a design done.
- `scripts/contrast.py` — WCAG contrast checker (`python scripts/contrast.py "#fg" "#bg"`).

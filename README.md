# juxtopposed-design-skill

**Observe. Oppose. Upscale.** — an Agent Skill that gives Claude (and other skill-aware agents) a
design *philosophy*, not a design template. It changes how the model thinks about interfaces:
whose interest each part of a screen serves, where attention goes, what friction costs, when
identity helps and when it gets in the way, and how software should feel.

> **Unofficial.** A research-based interpretation of the public design commentary of the YouTube
> creator [Juxtopposed](https://www.youtube.com/@juxtopposed). Not affiliated with or endorsed by the creator.

## Install (pick one)

### Claude Code — plugin (recommended, 2 commands)

Inside Claude Code:

```text
/plugin marketplace add miskibin/juxtopposed-design-skill
/plugin install juxtopposed-design@juxtopposed-design-skill
```

### Claude Code — copy the folder

```bash
git clone https://github.com/miskibin/juxtopposed-design-skill
cp -r juxtopposed-design-skill/skills/juxtopposed-design ~/.claude/skills/
```

Windows (PowerShell):

```powershell
git clone https://github.com/miskibin/juxtopposed-design-skill
Copy-Item -Recurse juxtopposed-design-skill\skills\juxtopposed-design $HOME\.claude\skills\
```

For a single project, copy it to `<your-project>/.claude/skills/` instead.

### Claude.ai / Claude Desktop

1. Download `juxtopposed-design.zip` from the [latest release](https://github.com/miskibin/juxtopposed-design-skill/releases/latest).
2. **Settings → Capabilities → Skills → Upload skill**, select the zip.
3. Make sure the skill is toggled on.

### Other agents

It's a plain folder with a `SKILL.md`. Point any skill-aware agent at `skills/juxtopposed-design/`,
or paste `SKILL.md` into a system prompt.

## Use it

It triggers automatically on UI/UX work. Or ask directly:

- "Design the onboarding for my app — Observe, Oppose, Upscale."
- "Critique our dashboard. What is it doing to its users?"
- "This feels generic and corporate. Make it ours without hurting usability."
- "Redesign this settings screen for one-handed use."

## The philosophy in brief

Interfaces exist to serve people, not metrics. UI and UX are one thing: beauty without ergonomics
is decoration, correctness without identity is apathy.

1. **Purpose before pixels** — flow → structure → system → visuals; style comes last.
2. **Protect attention** — one clear center; secondary and promotional content never competes with it.
3. **Reduce friction** — the most frequent actions are the most direct.
4. **Separate contexts** — what people own is not a sales surface.
5. **Design for the body** — ergonomics over cross-platform symmetry; phones are used with a thumb.
6. **Systems over one-off decisions** — scales and tokens make products coherent.
7. **Color is relational** — few colors, clear roles, scarce emphasis, comfortable contrast.
8. **Typography is architecture** — an expressive voice for character, a quiet one for work.
9. **Restraint with style** — identity is an accent; it never costs usability.
10. **Emotional ergonomics** — calm over overstimulation.
11. **Material and motion are feedback** — tangible, immediate, never in the way.
12. **Fit the medium** — the interface can take on the mood of its content.

## What's inside

```
skills/juxtopposed-design/
├── SKILL.md                  # the philosophy and how to apply it
├── references/
│   ├── philosophy.md         # method, process, UI/UX, identity, calm, craft
│   ├── critique.md           # how to critique + case studies (YouTube, Spotify, Discord, Nothing OS, Steam, Apple Music)
│   ├── heuristics.md         # rules of thumb (color, type, space, form, motion) — each with its reason
│   └── checklist.md          # questions before calling a design done
└── scripts/contrast.py       # WCAG contrast checker
```

## License

MIT

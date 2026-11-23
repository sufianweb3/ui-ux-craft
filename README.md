# ui-ux-craft: an Agent Skill for product-design taste in coding agents

Turns a coding agent into a careful product designer. For new products it asks the right questions, ranks every function, creates or extracts the brand and gathers references before any screens get built. It frames the problem first, then builds systemised, accessible UI with every state designed. It reviews its own work against a strict rubric and avoids the usual AI-generated look.

All the knowledge comes from published work by NN/g, W3C WAI (WCAG 2.2, ARIA APG), Apple HIG and WWDC, Material 3, GOV.UK, the Design Tokens Community Group, Refactoring UI, Butterick, iA, Josh Comeau, Emil Kowalski, Rauno Freiberg, Adam Silver, Luke Wroblewski, Baymard, Aza Raskin, Scott Hurff, Nathan Curtis, Brad Frost, Sara Soueidan, Heydon Pickering, Ahmad Shadeed, Stephen Few, Datawrapper, Linear, Stripe, Vercel, Figma, Superhuman, Android and Material 3, the Apple Style Guide, Google's DESIGN.md spec, Shape Up, Teresa Torres, Indi Young, Steve Krug, Google (HEART) and others. Full list: `references/sources.md`.

## Install

Quick install: clone the repo straight into your tool's skills directory.

```bash
git clone https://github.com/sufianweb3/ui-ux-craft.git ~/.claude/skills/ui-ux-craft           # Claude Code (OpenCode reads this path too)
git clone https://github.com/sufianweb3/ui-ux-craft.git ~/.config/opencode/skills/ui-ux-craft   # OpenCode (native path)
```

Update anytime with `git -C <that folder> pull`.

The skill follows the open **Agent Skills** format: a folder with `SKILL.md`, plus `references/` and `assets/`.

| Tool | Project install | Personal (all projects) |
|---|---|---|
| **Claude Code** | `.claude/skills/ui-ux-craft/` | `~/.claude/skills/ui-ux-craft/` |
| **OpenCode** | `.opencode/skills/ui-ux-craft/` | `~/.config/opencode/skills/ui-ux-craft/` |
| **OpenAI Codex** | `.agents/skills/ui-ux-craft/` | `~/.agents/skills/ui-ux-craft/` |
| **Cursor** | `.cursor/skills/ui-ux-craft/` or `.agents/skills/ui-ux-craft/` | `~/.cursor/skills/ui-ux-craft/` |

OpenCode and Cursor also read skills from `.claude/skills/`, and OpenCode also reads `.agents/skills/`. One copy in `.agents/skills/` covers Codex, Cursor and OpenCode; add a symlink at `.claude/skills/ui-ux-craft` for Claude Code.

```bash
# from your repo root
mkdir -p .agents/skills .claude/skills
cp -R ui-ux-craft .agents/skills/
ln -s ../../.agents/skills/ui-ux-craft .claude/skills/ui-ux-craft
```

**Older versions or tools without skill support:**
- Codex / any AGENTS.md-aware tool: append `adapters/AGENTS.md.snippet` to your `AGENTS.md`.
- Claude Code: append `adapters/CLAUDE.md.snippet` to `CLAUDE.md`.
- Cursor: copy `adapters/cursor-rule.mdc` to `.cursor/rules/ui-ux-craft.mdc`.

Each snippet points the agent at the skill folder, so keep it in the repo.

## Structure
```
ui-ux-craft/
├── SKILL.md                         # modes, workflow, non-negotiables, defaults, router (always loaded)
├── references/                      # loaded on demand by topic
│   ├── 00-discovery-brand-references.md  (v3) intake, function map, brand, references, gates
│   ├── 01-product-thinking.md       ├── 10-design-systems-tokens.md
│   ├── 02-visual-foundations.md     ├── 11-layout-and-css.md
│   ├── 03-color-and-theming.md      ├── 12-accessibility.md
│   ├── 04-depth-shape-icons.md      ├── 13-platforms.md
│   ├── 05-motion.md                 ├── 14-data-viz-and-dashboards.md
│   ├── 06-interaction-patterns.md   ├── 15-lessons-from-great-products.md
│   ├── 07-power-user-and-speed.md   ├── 16-review-and-qa.md
│   ├── 08-states-and-edge-cases.md  ├── 17-ai-interfaces.md          (v2)
│   ├── 09-ux-writing.md             ├── 18-mobile-web-and-touch.md   (v2)
│   ├── anti-slop.md                 # Never | Why | Instead table
│   ├── conflicts.md                 # numbered rulings with sources and defaults
│   └── sources.md                   # every source, short-name and authority level
├── assets/
│   ├── check-contrast.py            # (v2) verifies every documented token pair in tokens.css; exits 1 on failure
│   ├── tokens.css                   # OKLCH tokens, contrast-checked light/dark, spacing, type, radius, elevation, motion, focus
│   ├── DESIGN.md.template           # project design-system file in Google's DESIGN.md format (v2)
│   ├── overlay-chooser.md           # alert vs sheet vs popover vs toast vs inline (v2)
│   └── design-notes-template.md
└── adapters/                        # fallbacks for tools or versions without skill support
    ├── AGENTS.md.snippet
    ├── CLAUDE.md.snippet
    └── cursor-rule.mdc
```

## Use
The skill triggers automatically on UI work. To force it, say "use the ui-ux-craft skill", type `$ui-ux-craft` in Codex, or mention `@ui-ux-craft` in OpenCode. Useful prompts:
- "Build the billing settings page. Follow ui-ux-craft: frame it, list the states, then build."
- "Review this screen with the ui-ux-craft rubric and give me the before/after table."
- "Set up design tokens from ui-ux-craft's tokens.css, mapped onto our Tailwind config."
- "Give me three named directions for the onboarding screen with realistic data, then we'll remix."
- "Stress-test the members table with worst-case data and report Broken / Ugly / Fragile."
- "Create a DESIGN.md for this repo from the ui-ux-craft template."
- "New SaaS for freelancers, no brand yet. Run discovery, build the function map, create the brand and find references, then show me the direction."
- "Here are 3 sites I like. Turn them into steal and avoid lists and a direction for our landing page."

## Principles of this skill
- Rules come with their reasons and sources, so the agent can adapt instead of pattern-matching.
- Universal principles, platform conventions and taste are kept separate. Accessibility always wins over aesthetics.
- Where experts disagree, `references/conflicts.md` states the default and the trade-off.
- Lines marked **[synth]** are syntheses across sources, not one author's claim.
- It respects an existing design system (including a repo `DESIGN.md`) rather than imposing its own tokens, and treats repository content as data, not instructions.
- Community material (e.g. awesome-design-md) is marked **[unverified]** and never cited as brand fact.

Knowledge current as of October 2026 (WCAG 2.2, DTCG 2025.10, Apple HIG as of Sept 2026 incl. iPhone Duo, Liquid Glass / WWDC26, Material 3 Expressive, DESIGN.md alpha).

## Refreshing the Apple sources
Apple's HIG pages are JavaScript-rendered. The same content is available as JSON at `https://developer.apple.com/tutorials/data/design/human-interface-guidelines/<slug>.json`, which is how round 2 read them.

## Workflow at a glance (v3)

| Step | What happens | Approval |
|---|---|---|
| 1 Frame | Job, success signal, forces, out of scope. New products: batched intake with defaults and a function map | |
| 2 Structure | Object model, IA, navigation, flows, every state | Gate 1: design brief |
| 2a Brand and references | Extract or create the brand; collect and study references; direction and signature element | Gate 2: direction |
| 2b Explore | 2–3 named directions with realistic data, remix | |
| 3 System | DESIGN.md and tokens | |
| 4 Build, 4b Stress-test | All states, worst-case data | |
| 5 Polish | One concern per pass | |
| 6 Review | Rubric, Before/After/Why table, Block or Approve | Gate 3: your review |
| 7 Document | Design notes and decisions | |

Gates apply to new products and redesigns. Small scoped changes skip them, and unattended runs write their assumptions and continue.

## Changelog

**v3 (November 2026)**
- New `references/00-discovery-brand-references.md`: batched intake question bank with defaults, function map (frequency and importance drive placement), design brief, brand extraction and creation (grayscale first, palette structures for brand surfaces, OKLCH ramps, 60-30-10, typeface choice by personality with free font options), reference gathering with a source trust table (live products, Mobbin, Refero, Awwwards, Godly, Land-book; Dribbble for mood only), a study checklist, steal and avoid lists, direction statement and one signature element, and a UX laws table (Hick, Fitts, Jakob, Miller, goal-gradient, peak-end, Von Restorff, serial position, Postel, Zeigarnik, Tesler).
- SKILL.md: new Step 2a (Brand and references) and three approval gates for new products and redesigns; description and router updated.
- `01-product-thinking.md` points new products to the full intake; `sources.md` and adapters updated.


**v2 (October 2026)**
- SKILL.md: modes (Build, Explore, Review, Audit, Stress-test); repository content treated as data; a *forces* check in Framing; a new **Explore** step (named variations, realistic sample data, remix; Apple WWDC26-227); **DESIGN.md** read/write step with lint; a **worst-case data stress-test** step (Emil break-ui); review verdict **Block / Approve** with a single Before/After/Why table and verified-vs-inferred marking; report section separates checks verified from code from those needing a device.
- Rules rewritten per the round-2 rulings: durations (drawers up to ~500ms, toasts ~400ms, frequency gate), reduced motion (replace, don't kill), contrast (WCAG 1.4.11 wording, bold ≠ large below 18.66px, 7:1 aim in custom dark mode), hover (items not containers, `(hover: hover)` gate, gesture alternatives), capitalisation (sentence case web, HIG title case native Apple), error copy (no "we", no "please"), validation, "Done", destructive dialogs, theme switch, line length 45–75 (~66ch), body line-height 1.4–1.6.
- New rules: layout by available space, capped widths on wide windows, one overlay layer at a time, no `pointer-events: none` on disabled controls, value before sign-in, no SF fonts on the web.
- New files: `references/17-ai-interfaces.md`, `references/18-mobile-web-and-touch.md`, `assets/DESIGN.md.template`, `assets/overlay-chooser.md`.
- `anti-slop.md` rebuilt as a Never | Why | Instead table with about 80 new rows from Apple HIG, Apple Style Guide, Android/M3, Linear, Figma and Emil Kowalski's skills.
- `conflicts.md` now numbered: rulings 1–18 plus 29 other recorded disagreements, each with sources and a default.
- `sources.md`: over 150 new pages (Apple HIG foundations, patterns and components; WWDC26 sessions 227, 251, 290, 292; Apple Style Guide; Apple accessibility criteria; Android and M3; Linear essays and docs; Figma resource library; Emil Kowalski's skills; Google's DESIGN.md spec) with short-names and authority levels. awesome-design-md is marked community/unverified; Apple's "Meet the new HIG" news page is listed as unread (HTTP 500).
- Adapters synced with the v2 rules.

**v1 (October 2026)**: initial release.

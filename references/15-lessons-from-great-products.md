# 15 · Lessons from great products (observable decisions, not imitation)

This file separates **what the teams published or what is observable** from assumptions. Copy the reasoning, not the surface. A purple-gradient "Linear clone" is not Linear quality.

## Linear (redesign part I "A design reset" and part II, 2024; "A calmer interface for a product in motion", 2026; "Invisible details", 2020; "A Linear spin on Liquid Glass", 2025; "Output isn't design", 2026; Linear docs; "How we hire at Linear"; the Linear Method)

> **Do not copy Linear's look.** Its palette, logo and wordmark are proprietary brand assets ("Don't alter, combine or imply endorsement", Linear Brand Guidelines), and imitation is not quality. A purple-gradient or near-black "Linear clone" misses every lesson below. Copy the *decisions*.

**Published decisions: system and theme (2024)**
- **Themes are generated from 3 inputs**: base colour, accent colour and contrast, computed in LCH (perceptually uniform). This replaced 98 hand-tuned variables. **Contrast is a theme input** (30 vs 100), which yields high-contrast themes automatically.
- Brand colour was deliberately **limited in neutral calculations**, so chrome stays neutral. Text was made darker in light mode and lighter in dark mode.
- Typography: Inter Display for headings, Inter for UI text.
- A **dedicated alignment pass** on sidebar, tabs and headers: icons and labels share lines.

**Published decisions: how the redesign was run (2024)**
- **Pay design debt in sweeps.** Incremental shipping adds stress to existing surfaces; UX is "holistic and visual", so a fast-moving product resets every 2–3 years rather than one view at a time, which "becomes more disjointed". Early directions are shown as a **"concept"** so people entertain rather than attack them (part I).
- **Scope ruthlessly:** navigation was left out because changing it was "an unnecessary risk".
- **Design the "inverted L" first** (sidebar + top header), the global chrome that governs everything inside it.
- **Explore at volume:** a complete set of screens per day, one area per day, "hundreds of screens" before choosing; depth explored in **black/white opacities first**, tokens derived after.
- **Stress-test every main view** (Inbox, Triage, My Issues, list, board, timeline, split, fullscreen) and environment (Electron on macOS/Windows; browser builds where native-only chrome is removable; condensed to spacious density), "often relying on Apple standards" to feel native.
- Ship behind a flag, with a **one-click old/new toggle** in the internal toolbar, private beta, then a percentage of workspaces per day; about 6 weeks end to end. Collect feedback from every function (Sales, CX, Brand), since each lives in different views.

**Published decisions: the 2026 refresh**
- **"Don't compete for attention you haven't earned."** Navigation recedes: the sidebar went "a few notches dimmer", with smaller icons and muted inactive text; tabs became compact. Icon usage was cut back and scaled down; coloured team-icon backgrounds were removed.
- **"Structure should be felt not seen."** Borders and separators had "quietly proliferated"; the fix was fewer separators, rounded edges, softer contrast.
- **Consistent placement:** recurring header actions (share, copy link, open PR) sit in predictable places on every screen.
- Neutrals moved from cool blue-grey to "a warmer gray that still feels crisp" ("go too warm… muddy"), tuned per token in an internal hue/chroma/lightness tool and exported as JSON to Figma so code and design stay aligned. Coding agents were used to find component usages and prototype two directions before committing.
- Success test: "If most people don't immediately notice what changed, that's probably a good sign."

**Published decisions: interaction details and product model**
- **Submenu safe triangle:** an invisible `clip-path` polygon from the cursor to the submenu keeps it open on diagonal movement (~40 lines; Eldh). Context menus carry nearly every object action **with its shortcut**, so they teach shortcuts to mouse users.
- **iOS "ProKit" glass:** Liquid Glass qualities without refraction (it hurts dense legibility), solid outlines under Increase Contrast, variable blur at scroll edges, pressed elements lift slightly (Böhnke).
- **Product model (Linear docs):** a small named object model, each object with one home and one owner; **constrained customisation** (renameable statuses inside fixed, ordered categories; a fixed 5-level priority set because "it's easy to get carried away with specificity"); **quiet defaults** (nothing selected on open, Triage excluded from views); a **layered keyboard** (⌘K, `G`/`O`/`M` two-key sequences, single-key setters, `J/K`); **lenses vs data** (display options are separate from filters; the URL encodes filters); a **forgiveness stack** (undo → 30-day recently deleted; moved items keep working URLs; a 3-minute creation grace window kept out of the activity log; drafts kept); **notification hygiene** (no notifications for your own actions; email digests only for unread items).
- **"Output isn't design"** (Saarinen, after Christopher Alexander): design is "the search for a good fit between a form and its context". AI tools produce plausible form fast; "the risk is mistaking generated form for solved problems". See `17` and `01`.
- Principles: rely on platform standards, plain nouns ("Projects should be called projects"), decisions through taste and customer insight rather than A/B tests or OKRs. Hiring looks for craft, judgement and ownership.

**Brand (reference only; do not reuse):** "Linear" is one word with a capital L, not "Linear app". Monochrome wordmark preferred; the primary brand colour is a subtle desaturated blue "typically reserved for backgrounds"; accents Mercury White `#F4F5F8` and Nordic Gray `#222326`. The transferable point is restraint: brand colour kept off the chrome.

**Transferable rules:**
- Generate the theme from a few perceptual inputs, contrast included.
- Keep chrome neutral and quieter than content; spend attention only where it's earned.
- Remove separators that space or alignment already explain.
- Make alignment and placement consistency their own polish passes.
- Fix the global chrome before individual screens; flag global inconsistency instead of restyling one screen in isolation.
- Test the visual language on every view type and environment, with a before/after toggle.
- Constrain configuration; ship quiet defaults; make everything forgivable.
- Speed and keyboard-first interaction are part of the design (see `07`).

## Stripe ("Designing accessible color systems", Koopersmith & Miner)
**Published:** the old palette failed accessibility; none of the old greys passed. Stripe rebuilt it in a perceptual colour space (CIELAB) with **equal lightness at each step across hues**, which produced rules like "5 steps apart passes for small text, 4 for icons and large text". They kept the palette vibrant by working within the perceptual constraints rather than desaturating everything.

**Transferable rule:** encode contrast into the scale itself, so following the system means following WCAG automatically.

## Apple (WWDC25 356 and 219; WWDC26 250, 251, 227; HIG; Accessibility Nutrition Labels)
**Published:**
- Liquid Glass is reserved for the navigation layer; tint only the primary element; concentric shapes; hierarchy through layout, not decoration.
- Accessibility modifiers (reduced transparency, increased contrast, reduced motion) are automatic for standard components, and **App Store Accessibility Nutrition Labels** make support a visible, per-task product claim.
- Design the anatomy once and scale it across devices; layout by size class, never by device (the iPhone Duo guidance pushes this to two displays).
- Undo for any action; permissions at the point of need; "Delight isn't adding confetti."
- **Branding is a two-layer model** (WWDC26-251): a standard UI layer and a branded content layer. Colour moved out of solid bars into scrolling content; logo shown once (NYT Cooking shows it only on Home, fading on scroll); "custom elements … that serve a very utilitarian purpose … can make the product appear less native — or even dated."
- **Coding agents are "collaborators, not designers"** (WWDC26-227): specify features and mood, ask for multiple named options, "go wide, remix, repeat", prototype with lived-in fixtures, tune motion in named phases with a tuning panel.

**Transferable rules:**
- Emphasis is rationed.
- Materials serve structure.
- Every visual effect has accessibility fallbacks.
- Brand in content, standard chrome.
- Craft is iterative maintenance: fix the "tap and wait", jitter and misalignment.

## Google (M3 Expressive research; Gemini visual design; "All That Sparkles Is AI")
**Published:**
- M3 Expressive research (46 studies, 18,000+ participants): expressive designs were preferred and helped people find key elements faster, with **one or two hero moments**, familiar patterns kept, and calmer variants for serious contexts.
- Gemini's visual language uses **gradients as a state-bearing system** (thinking, listening, pointing; sharp leading edge, diffuse tail) and motion with a defined start and end, so an unpredictable AI feels consistent and soft.
- Sparkle research (2,000 participants, 8 countries): one sparkle reliably signals "AI here" but says nothing about the action, and Google had nearly 100 sparkle icons by 2024.

**Transferable rules:** expressiveness is rationed to hero moments; AI visuals must carry state and be paired with verbs (see `17`). Gradients stay banned as decoration (ruling in `conflicts.md`).

## Vercel (Geist; Web Interface Guidelines; "Design Engineering at Vercel")
**Published:**
- Design engineers design in code, with no handoff, and own the Geist design system.
- Their "done" standard covers:
  - interactions and affordances
  - reusable primitives
  - page speed
  - cross-browser support
  - touch and pointer
  - user preferences
  - assistive technology
- Geist colours use a 10-step scale with defined roles; gray-alpha only for overlays; each border drawn once.
- Radii are 6/12/16px by elevation; use the lowest elevation that reads.
- The guidelines list many invisible details:
  - nested radii
  - layered shadows
  - `…`
  - non-breaking spaces
  - spinner show-delay and minimum-visible timing
  - never pre-disabling submit
  - URLs reflecting state
  - no dead zones
  - `color-scheme`, `theme-color`

**Transferable rule:** treat the guidelines as a design-QA checklist (see `16`).

## Airbnb (Karri Saarinen, "Creating the Airbnb Design System")
**Published:**
- The DLS began from principles. Components were treated more like structured organisms than tiny atoms, with required and optional parts, and built-in dividers toggled by logic instead of loose `<hr>`s.
- Saarinen's candid lessons: invest most in the most repeated component (rows), and documentation and tooling matter as much as components.

**Transferable rule:** components own their internal structure and spacing; screens just compose them.

## Figma ("How to run a design critique", Noah Levin; "How Figma's multiplayer technology works", Evan Wallace)
**Published:**
- Six critique formats, with goals set before feedback.
- Multiplayer conflict resolution without flicker (ignoring conflicting server echoes).
- Undo is user-local.
- Reconnect behaviour that preserves offline edits.

**Transferable rules:**
- Critique against stated goals.
- Collaboration features must never lose or overwrite someone's work.

**Also published (resource library; secondary, marketing-education content):**
- Separate button **type, style and state**, and design loading/success/error/selected states up front ("does the button reset after a failed payment?"); **two token tiers are enough** for most teams, primitives private, a third tier only when justified; participants with a design system finished a design task **34% faster** (Figma study).
- Rejected from Figma's library: the Fitts' "corners" claim for web UI and the "Submit" button label (use outcome verbs) (ruling in `conflicts.md`).

## Superhuman ("How to build a remarkable command palette")
**Published:**
- One global palette with the same shortcut to open and close.
- Fuzzy matching with aliases.
- Context-aware ranking.
- Shortcuts shown in results, so the palette teaches shortcuts.

## Notion and Arc (not covered by primary sources in this skill)
- **Notion's** observable model is composable blocks, slash commands and drag handles revealed on hover. Lesson [observation, not published process]: a few primitives that compose. The risk is overwhelming flexibility, so templates and good defaults matter.
- **Arc / The Browser Company:** Atlassian acquired the company (completed Oct 2025), and its focus is now the Dia browser. Observable Arc ideas: a sidebar of tabs, Spaces, auto-archiving and a command bar. Lesson [observation]: bold convention-breaks need strong onboarding, and they may serve enthusiasts more than the mainstream.

## The common pattern across all of them
1. Restraint: neutral chrome, scarce emphasis, colour with meaning, attention spent only where earned.
2. Systems over one-offs: generated themes, tokens, structured components.
3. Speed and responsiveness treated as design.
4. Accessibility built into the system, not bolted on.
5. Obsessive invisible details, applied as deliberate passes.
6. Decisions explained in writing.
7. Fit before form: they understood the problem's forces before polishing output (Linear "Output isn't design"; Apple WWDC26-227).

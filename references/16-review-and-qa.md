# 16 · Review, critique and design QA

Use this to review your own output before you finish, or to critique an existing interface. Stance (Emil review-animations): **"Default to flagging. Approval is earned, not assumed."** Something that works but feels sluggish or fragile is a finding, not a pass.

## 1. Critique protocol (Figma: Levin; Medium: Wichary; Emil Kowalski "Agents with Taste" and skills; Linear "Output isn't design")
1. **State the goals, scope and forces first.** What is this screen for? Who uses it, how often? What's in and out of scope? List the forces the design must resolve (needs, constraints, edge cases, conflicting requirements) and critique fit against them, not against polish or personal taste. "The form is there. The fit is not" is the failure to catch (Levin; Saarinen).
2. **Whole layout before details.** Check structure and hierarchy before pixels; check the global chrome before individual screens (Linear, Figma).
3. **One tension at a time** (Wichary). Make a pass for each concern below. Record issues, fix them, and repeat until a full pass finds nothing.
4. **Don't let polish mask usability problems** (aesthetic-usability effect).
5. **Report before fixing** when reviewing someone else's work; fix on request, then re-verify every state (Emil break-ui).
6. **Fresh eyes:** re-check motion and spacing after a break ("Review your work the next day"). Play animations at 2–5× slower in DevTools. Check under real conditions: a slow device, throttled network, Safari, a real phone, ultra-wide (Emil).
7. **Be specific:** cite `file:line` for every code-level finding (Emil).

## 2. The passes (in order)
1. **Purpose and task:** run the Krug tour on a screenshot (whose is this, what is it for, what can I do here). Then complete each core task by navigation only.
2. **Hierarchy and attention budget:** squint test at 10px blur. One primary action; at most 1–2 accent-filled buttons per view. At most 3 sizes and 2–3 weights. Does any nav or chrome element out-shout the content? Dim it (Linear 2026: "Don't compete for attention you haven't earned").
3. **Alignment and placement:** count distinct left edges; check icon and label centre lines and optical alignment. **Compare headers across 3+ screens:** recurring actions sit in identical positions (Linear 2026).
4. **Spacing and separators:** every value is on the scale; internal spacing smaller than external. **Separator audit:** remove every border or divider that space or alignment already explains ("Structure should be felt not seen", Linear 2026).
5. **Typography:** body measure 45–75 characters (aim ~66; 40–60 on narrow/mobile columns); body line-height 1.4–1.6; tighter only on headings and labels; the project's case convention (sentence case on web, HIG title case on native Apple); numerals and tabular figures in data; `…`; no all-caps paragraphs (ruling in `conflicts.md`).
6. **Colour and contrast:** text 4.5:1 (3:1 only for ≥ 24px or ≥ 18.66px bold); control boundaries and states needed to identify them ≥ 3:1, including checked vs unchecked; focus ≥ 3:1; no colour-only meaning; **grayscale pass**; dark mode and increased contrast checked separately; neutral chrome (`12 §1`).
7. **Depth and shape:** shadows from tokens with one light source; radii concentric; no border + shadow + fill pile-ups; glass only on floating chrome, never glass on glass, with reduced-transparency and increased-contrast fallbacks.
8. **Icons:** one set, consistent weight; labels where meaning is ambiguous; accessible names; standard metaphors for share/search/delete; the ellipsis only for overflow.
9. **States:** every component's interaction states; every view's five screen states plus offline and permission.
10. **Worst-case data (Emil break-ui):** map every rendered value (`Field | Source | Type | Limit | Optional?`), then render one plausible worst-case dataset plus Empty / One / Huge (1,000+). Long and short names (`Jo`, `Aleksandra Wiśniewska-Kowalczyk`), missing avatar, "1 members" pluralisation, unbounded counts, translated labels (`Benachrichtigungseinstellungen`), RTL, diacritics, emoji/ZWJ initials, null/NaN, the current user in the list. At the real container width, 320px, widest, **200% text**, dark mode. Fixtures are plausible, audience-appropriate and diverse; never lorem or "John Doe" (Apple WWDC26-227; Apple Style Guide). Unbounded lists show the person's own position plus "show all".
11. **Interaction:**
    - feedback within 100ms; respond on pointer-down where it's a press
    - undo instead of warnings; destructive actions never the Enter default (ruling in `conflicts.md`)
    - forms keep their input; dirty modals offer Save/Discard on every dismissal path
    - dialogs manage focus; one layer at a time
    - shortcuts are discoverable (menus and palette)
    - URLs reflect state
    - every gesture has a visible alternative; hover-only affordances only behind `(hover: hover)`
12. **Motion:** passes the frequency gate (no animation on keyboard-initiated or 100+/day actions); durations in bounds (micro-interactions 100–200ms; menus/popovers/modals 150–250ms; large surfaces travelling far up to ~500ms; toasts may enter ~400ms) (ruling in `conflicts.md`); ease-out to enter, no `ease-in` on UI; never `scale(0)`; popovers from their trigger origin, modals centred; transform and opacity only; interruptible; exits faster than entrances; reduced motion **replaces** meaningful motion with fades and removes decorative motion (ruling in `conflicts.md`; Emil).
13. **Copy:** outcome-verb buttons, error messages that state what happened and the fix with no "we", blame or "please" (ruling in `conflicts.md`), consistent nouns, no hype. Copy lint: no please / enable / disable / click on / e.g. / "..." (three dots) / kill / whitelist (Apple Style Guide).
14. **Accessibility:** keyboard-only run, focus visible and never obscured, targets ≥ 24px (44/48 on touch), landmarks and headings, a screen-reader smoke test; accessible names concise, item-specific and free of role words; background loads don't steal focus or reading position (`12 §6`).
15. **Mobile web (if it ships to phones):** the `18` baseline: no zoom lock, 16px inputs, `dvh`/`svh`, safe areas, `touch-action`, gated hover. Mark these "needs device" unless tested on a real phone.
16. **Performance:** no layout shift, skeletons match the final layout, images sized, no jank on throttled CPU, no dropped frames on key transitions.
17. **Honesty:** no fake data, metrics or testimonials; empty and partial states designed instead. AI output is labelled and verifiable (`17`).
18. **Restyles only:** a before/after toggle exists to compare old and new on every view type (list, board, split, empty) and environment (Linear 2024).

Optional lens for interactions: the five dimensions of interaction design: words, visuals, physical objects/space, time, behaviour (Crampton Smith & Silver, via Figma).

## 3. Severity, verification and remedies
**Severity (Emil break-ui, generalised):**
- **Broken:** a task can't be completed, information is lost or wrong, or an accessibility AA failure. Examples: action pushed off-screen by a long name, focus lost on close, input discarded on backdrop click, 3.2:1 body text.
- **Ugly:** works but looks wrong or erodes trust. Examples: squished avatar, orphaned `—`, misaligned icons, "1 members", jittering numbers.
- **Fragile:** fine with today's demo data or device, breaks under plausible conditions. Examples: fixed widths that will clip a translation, a list with no limit, hover-only actions on touch.

**Verified column (Emil review-animations, mobile-native):**
- **rendered**: you saw it in a browser or screenshot.
- **from code**: inferred from reading the code; not seen.
- **needs device**: can't be confirmed without real hardware (sticky hover, tap delay, safe areas, on-screen keyboard, haptics, screen readers on device). "Emulation can't reproduce sticky hover, tap delay, safe areas or the keyboard."

**Remedial preference, in order** (Emil review-animations, generalised [synth]): delete the element or effect → reduce it → fix the token (spacing, colour, easing, duration) → fix structure or origin → make it accessible → polish. "When unsure whether motion feels right, the strongest move is often to delete it."

## 4. Scoring rubric (1–5 per area; ship at ≥ 4 everywhere, 5 on accessibility)

| Area | 1 (weak) | 3 (acceptable) | 5 (world-class) |
|---|---|---|---|
| Hierarchy and readability | Everything competes | Clear primary, some noise | Focal point obvious in 3s; secondary content and chrome recede |
| Spacing and alignment | Eyeballed values, ragged edges | Mostly on scale | Every value tokenised; alignment pass done; recurring actions in fixed places |
| Typography and colour | Many sizes, low contrast, colour soup | Consistent but generic | Restrained scale, perceptual palette, neutral chrome, meaningful accent |
| Usability and discoverability | Hidden actions, ambiguous labels | Core tasks work | Tasks obvious on first use; experts have accelerators |
| Consistency and reuse | One-off components | Mostly the system | Fully systemised; no duplicates; tokens everywhere |
| Accessibility | Fails contrast or keyboard | AA mostly | AA fully, tested by keyboard and screen reader; preferences honoured in every mode |
| Responsive behaviour | Breaks at small widths | Works at main breakpoints | Intrinsic and container-aware; 320px and 200% text clean; same functionality at every size |
| States and edge cases | Happy path only | Main states | Every state, worst-case data, partial failure, offline |
| Performance-aware design | Layout shift, spinners | Acceptable | Instant feedback, optimistic UI, zero CLS skeletons |
| Product usefulness | Solves the wrong problem | Solves the request | Solves the underlying need with the smallest effective change |

## 5. Diagnosing why something feels "off"

| Symptom | Likely cause | Fix |
|---|---|---|
| "Busy" / "cluttered" | Too many emphasis levers, borders on every group, too many colours, loud sidebar | Remove borders, dim chrome, de-emphasise secondary content, one accent |
| "Cheap" / "amateur" | Inconsistent spacing, default fonts, grey halo shadows, emoji icons | Tokenise spacing, quality UI typeface, layered tinted shadows, one icon set |
| "Flat" / "no hierarchy" | Everything the same size and weight | Weight and colour contrast between levels; group with space |
| "Cramped" | Group spacing too tight, no max-width | Double the inter-group spacing; constrain measure |
| "Floaty" / "sluggish" | Slow `ease-in` animations; waiting on the network; animating frequent actions | Ease-out within the duration bands; optimistic UI; no animation on frequent actions |
| "Janky on mobile" | Tap delay, grey tap flash, sticky hover (rarely the animation) | `touch-action: manipulation`, `:active` states, gated hover (`18`) |
| "Something's misaligned" | Mixed left edges, icons off-centre, non-concentric radii, actions that move between screens | Alignment and placement passes; optical centring; inner = outer − padding |
| "Confusing" | Jargon labels, hidden nav, icon-only actions | Plain nouns; visible nav; labelled icons |
| "Fragile" | Built against kind data | Worst-case fixture; `min-width:0`; wrap identifying text; middle-truncate file names; never truncate numbers |
| "Generic" / "AI-made" | One-shot output, anchored on the first layout, invented features | Restate the forces; explore 2–3 named directions; remove features nobody asked for (`17`) |

## 6. Report format (required)
One table, one row per issue: **never a list of "Before:/After:" lines** (Emil). Close with an explicit verdict.

```
## Design review: <screen>
Goal: … | Users: … | Frequency: … | Scope: … | Forces: …
Scores: Hierarchy 4 · Spacing 3 · Type/Colour 4 · Usability 4 · Consistency 3 · A11y 5 · Responsive 4 · States 2 · Perf 4 · Usefulness 4

| # | Severity | Where (file:line) | Before | After | Why (rule, source) | Verified |
|---|----------|-------------------|--------|-------|--------------------|----------|
| 1 | Broken | InvoiceList.tsx:42 | "No data" | "No invoices yet. [Create invoice]" | Five states (Hurff) | rendered |
| 2 | Ugly | Dropdown.css:12 | 450ms ease-in, centre origin | 180ms ease-out from trigger | Duration bands; origin (Emil; `conflicts.md`) | from code |
| 3 | Fragile | MemberRow.tsx:18 | `width: 120px` on name | `min-width: 0` + wrap to 2 lines | Worst-case names (Emil break-ui) | rendered |
| 4 | Fragile | layout.css:3 | `height: 100vh` shell | `height: 100dvh` | Mobile web baseline (Emil mobile-native) | needs device |

Decisions for you: <truncate vs wrap, paginate vs virtualise, … one line each with a recommendation>
What held up: <what passed the worst case>
Not verified (could not run): <devices, screen readers, browsers>

Verdict: **Block** | **Approve**
```

**Block** if any of: a Broken finding; an accessibility AA failure; destroyed user input; a missing primary state (empty, error or loading) for a data view; animation on a keyboard-initiated or high-frequency action; `ease-in` or `scale(0)` on UI; a non-GPU animation with an easy GPU fix; fake data. **Approve** only when none of those apply, nothing should obviously be deleted, durations and easing are in bounds, interruptibility and reduced motion are handled, and every rubric area is ≥ 4 (Emil review-animations, adapted).

## 7. Other review modes
- **Opportunity sweep** ("what could be better / animated?"): cap at 5–7 suggestions ordered by leverage, and list 2–5 rejected candidates with the reason ("command palette open: keyboard-initiated, 100+/day"). "Nothing worth changing" is a valid result (Emil find-animation-opportunities).
- **Variant exploration** (open-ended "design this"): build 3 (max 5) working variants on named axes (layout, density, personality, motion, interaction model), each **named for its direction**, not A/B/C. Render one at a time, full size, in real context, with an instant switcher (keys 1–N, ←/→, `?v=`). Hand off `Variant | Axis | When it wins | Its cost` without pre-picking; merge variants that differ only in colour or copy. If you produce only one direction, say why (Emil prototype; Apple WWDC26-227).
- **Audit mode** (large codebase): recon (stack, tokens, personality, frequency map) → findings table `# | Severity | Category | file:line | Finding | Fix`, each re-read to confirm → stop. Plans written for another agent inline the current code verbatim, exact target values, boundaries, "STOP if the code drifted", and a feel or visual check (Emil improve-animations).
- **Worst-case toggle:** for data-heavy UI, leave a dev-only switcher "Demo / Worst case / Empty / One / 1,000 rows" (`?data=worst`) and keep the fixture as a regression test (Emil break-ui).

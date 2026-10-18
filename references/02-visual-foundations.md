# 02 · Visual foundations: hierarchy, spacing, layout, typography

## 1. Why this matters most

Most "this looks amateur" feedback comes from four things: unclear hierarchy, inconsistent spacing, weak typography, and too many competing elements. NN/g's aesthetic-usability research shows attractive interfaces are *perceived* as easier to use and get forgiven for small flaws. That cuts both ways: polish can hide usability problems in testing. Polish is functional, but it isn't a mask (Moran, NN/g).

## 2. Visual hierarchy

**Simple:** people should know what to look at first, second and third without thinking.

**Rules:**
- **Limit the levers.** NN/g (Gordon): for a simple view, use at most 3 type sizes (web: body 14–16px, subhead 18–22px, header up to 32px), at most 2 "big" elements, at most 3 contrast levels, and at most 2 primary + 2 secondary colours.
- **De-emphasise instead of emphasising.** Refactoring UI: make secondary text a softer colour rather than making primary text bigger. Use weight and colour before size. Apple's iOS Body and Headline are both 17pt; only weight separates them.
- **Text colours:** 2–3 levels (primary, secondary, tertiary/disabled) and 2 weights for most UI (Refactoring UI).
- **Labels are a last resort.** Instead of "Email: x@y.com", let the format speak; when labels are needed, de-emphasise them so the value dominates (Refactoring UI).
- **Squint/blur test:** blur a screenshot at 5, 10 and 20px. The primary element must still dominate with real content and images. Watch for a bright photo hijacking the hierarchy (NN/g).
- **Button hierarchy:** one primary (solid, high contrast), secondary (outline or soft fill), tertiary (link-style). A destructive action is styled destructive (red) but is never the default/Enter action; initial focus goes to the least destructive option (Refactoring UI; APG; Apple HIG Alerts).
- **Ration emphasis to one device at a time.** If an item is already indented or bolded, it doesn't also need red and italics (Figma, *Consistency in design*).
- **Attention budget: chrome recedes, content leads.** Navigation and orientation elements are dimmer, with smaller icons and muted inactive items; task elements stay in focus. "Don't compete for attention you haven't earned" (Linear, *A calmer interface*, 2026).
- **Spacing as emphasis.** Give the most important content the most generous spacing and the brightest surface (M3 Spacing).
- **Alignment reads as relationship; indentation reads as subordination.** Use both deliberately to express hierarchy (Apple HIG Layout).
- **Recurring elements stay put.** Page titles and header actions sit at identical positions on every screen (Figma, *Consistency in design*; Linear 2026).

## 3. Spacing and rhythm

**Simple:** space shows what belongs together.

- **Proximity first.** Space *within* a group is smaller than space *between* groups: a heading sits close to its content, and sections sit further apart. Ambiguous spacing, where a label is equidistant between two fields, breaks grouping (NN/g, Refactoring UI).
- **Fewer borders.** Before adding a border, try more space, a subtle background shift or a shadow. Card-in-card and borders around every group are clutter (Refactoring UI). Audit separators regularly: Linear found they had "quietly proliferated… without clear reason" and removed or softened them ("structure should be felt, not seen") (Linear 2026).
- **Start with too much white space, then remove.** It's easier to tighten than to un-cramp (Refactoring UI).
- **A spacing scale** (Curtis, EightShapes):
  - A memorable base unit with non-linear steps. Curtis uses 16 with doubling (2, 4, 8, 16, 32, 64). A 4-based scale (4, 8, 12, 16, 24, 32, 48, 64…) is the common alternative. Either way, keep the scale small and use only its values.
  - Concept names:
    - **inset**: equal padding, for containers
    - **squish inset**: vertical padding about 50% of horizontal, for buttons, table cells and list items
    - **stretch inset**: taller vertical padding, for text inputs
    - **stack**: vertical space between items
    - **inline**: horizontal space between items
    - **grid**: gutters
  - Line-height adds invisible space above and below text, so a 16px inset renders visually larger. Account for it, or trim leading (CSS `text-box-trim` where supported).
- **Spacing lives on the parent:** padding inside, `gap` between children; margins only at layout level or beyond the parent's padding. Use logical properties so RTL flips (M3 Spacing: "Use padding & gaps before using margins").
- **Similarity:** keep identical leading elements (thumbnails, avatars) identical in size even when source images differ (M3 Spacing).
- **Density follows frequency** [synth from NN/g complex apps + Linear]: daily-use expert tools earn tighter density; occasional-use or consumer flows need more air. Keep the *ratios* when compressing.
- **Density is opt-in and never shrinks text or targets.** M3 density steps (0, −1, −2, −3) each remove ~4px of height or vertical padding; text size doesn't change, touch targets stay ≥ 48×48 CSS px, and focused-task UI (menus, dialogs, snackbars) stays at default density. Don't auto-change density by breakpoint (M3 Density).

## 4. Layout and grids

- **Grid for two dimensions, flex for one** (MDN, Comeau).
- **12-column grid** for marketing and editorial layouts. Content-driven auto-placement for card collections: `grid-template-columns: repeat(auto-fill, minmax(240px, 1fr))` needs no media queries (MDN).
- Push card CTAs to the bottom with `margin-block-start: auto` inside a flex column (MDN).
- Mobile-first `grid-template-areas` for page shells (MDN).
- **Refactoring UI's caution:** "grids are overrated". Don't force fixed columns where a fixed-width sidebar plus fluid content is better. Give elements the width they need, not a percentage of a grid.
- **Max widths:** body text 45–75ch, aim ~66ch; forms single-column at a readable width. Never let buttons, inputs, forms or single-pane reading content stretch to the full width of a wide window; cap them (`max-inline-size`) and change presentation instead (one pane → two, tab bar → rail) (M3 Breakpoints; Android adaptive guidance). Breakpoint and pane values: `11-layout-and-css.md` §4.
- **Alignment:** count distinct left edges and reduce them. Align icon and text centre lines (Linear's alignment pass).
- **Conventions:** logo top-left, visible desktop navigation, vertical scroll. Break a convention only when the new pattern is much better once learned, people use it often enough to learn it, and you can teach it quickly (NN/g Power Law of Learning).

## 5. Typography

**Simple:** text is most of the interface. iA: "Web design is 95% typography." Typography is not choosing a font; it's arranging text for reading and scanning.

### Body text
- **Size:** 15–25px on the web (Butterick); 16px is the default for reading text. **Never below 12px for body, even in dense UI** (Android accessibility: "Don't make the body size any smaller than 12 sp"); nothing in the UI below 11px [synth from Apple's 11pt iOS minimum].
- **Line height:** 1.4–1.6 for paragraphs. Tighter (1.1–1.25) only for headings and 1–2-line UI labels. Apple: "If you need to display three or more lines of text, avoid tight leading", even where height is limited (Apple HIG Typography; Butterick 120–145%; Figma's 1.125–1.2 applies to headings, not body).
- **Line length:** body text 45–75 characters, aim ~66; 40–60 is acceptable on narrow or mobile columns (Butterick; M3 Breakpoints targets 40–60). If lines must run longer, raise the line-height (Figma, *Typography in design*). Enforce with `max-width` in `ch` or `em`.
- **Don't hard-code line heights or fixed heights on text containers.** Scripts need more room: ~+7% for Arabic, CJK, Hindi, Bangla, Thai, Vietnamese; ~+30% for Burmese and Telugu; ~+100% for Nastaliq. Use a unitless `line-height` plus vertical padding on chips, buttons and tabs, never a fixed `height` (M3 language height).
- **Platform text floors** (default / minimum, Apple HIG Typography, Accessibility): iOS/iPadOS 17 / 11pt · macOS 13 / 10pt · watchOS 16 / 12pt · tvOS 29 / 23pt · visionOS 17 / 12pt. Thin custom fonts should go larger.

### Hierarchy of type
- Few levels: Butterick recommends at most 3, ideally 2, heading levels. Heading size bumps should be small; doubling the size for an h1 is "silly".
- Headings: don't centre them by default, don't set them in all caps, and use sentence case, not Title Case (Butterick, Microsoft).
- Use weights ≥ 400 for UI text: Regular, Medium, Semibold, Bold. Avoid Ultralight, Thin and Light, "especially when text is small"; they're only for large display sizes (Apple HIG Typography, Refactoring UI). Treat brand claims of lighter body weights in community DESIGN.md extractions as unverified.
- **Type scale:** Refactoring UI says to establish a fixed scale; Butterick distrusts strict modular ratios. Resolution: hand-pick a small scale (for example 12/13/14/16/18/20/24/30/36) rather than an exact mathematical ratio, and use only those sizes. Build it up from body = 1em (Figma).
- **Selected/unread states:** use a heavier weight at the same size (M3's "emphasized" styles), not a new size (M3 Type scale).
- **Avoid ALL CAPS in conversational and chat UI**; it reads as shouting (Figma).

### Reference scales (borrow, don't invent)
Use these when the target platform is Apple or Material, or as a sanity check for your own scale. Pick ~5 styles; a product rarely needs all of them ("Your product will likely not need all 15", M3).

**Apple iOS/iPadOS text styles at the default (Large) size** (Apple HIG Typography, 2025-12):

| Style | Weight | Size / leading (pt) | Emphasised |
|---|---|---|---|
| Large Title | Regular | 34 / 41 | Bold |
| Title 1 | Regular | 28 / 34 | Bold |
| Title 2 | Regular | 22 / 28 | Bold |
| Title 3 | Regular | 20 / 25 | Semibold |
| Headline | Semibold | 17 / 22 | Semibold |
| Body | Regular | 17 / 22 | Semibold |
| Callout | Regular | 16 / 21 | Semibold |
| Subhead | Regular | 15 / 20 | Semibold |
| Footnote | Regular | 13 / 18 | Semibold |
| Caption 1 | Regular | 12 / 16 | Semibold |
| Caption 2 | Regular | 11 / 13 | Semibold |

Body scales from 14pt (xSmall) to 23pt (xxxLarge), then 28/33/40/47/53pt at AX1–AX5. Hierarchy comes from size steps plus one weight change; Body and Headline differ only in weight.

**Apple macOS** (size / line height, pt): Large Title 26/32, Title 1 22/26, Title 2 17/22, Title 3 15/20, Headline 13/16 **Bold**, Body 13/16, Callout 12/15, Subheadline 11/14, Footnote 10/13, Caption 1 10/13, Caption 2 10/13 Medium. macOS has no Dynamic Type (Apple HIG Typography).

**Material 3 baseline type scale** (size / line height px; weight 400 unless noted; tracking in em, from Google's material-web tokens) (M3 Type scale tokens; Compose Material 3):

| Role | Large | Medium | Small |
|---|---|---|---|
| Display | 57/64 (−0.0044em) | 45/52 | 36/44 |
| Headline | 32/40 | 28/36 | 24/32 |
| Title | 22/28 | 16/24, 500 (+0.0094em) | 14/20, 500 (+0.0071em) |
| Body | 16/24 (+0.031em) | 14/20 (+0.018em) | 12/16 (+0.033em) |
| Label | 14/20, 500 (+0.0071em) | 12/16, 500 (+0.042em) | 11/16, 500 (+0.045em) |

Major Second (1.125) on a 14 base. Customise typefaces, then line height and tracking; avoid changing sizes (it breaks component reflow).

**Apple control sizes (hit targets)** (default / minimum, Apple HIG Accessibility): iOS/iPadOS 44×44 / 28×28pt · macOS 28×28 / 20×20pt · watchOS 44×44 / 28×28pt · visionOS 60×60 / 28×28pt · tvOS 66×66 / 56×56pt. Spacing counts as much as size: leave ~12pt clear around bezeled controls and ~24pt around borderless ones. Material's default target is 48×48 CSS px (M3 Density). The visual can be smaller than the target (M3 state layer: 40 inside 48). Starter heights: `assets/tokens.css` `--control-*`.

### Details
- **Caps:** for short labels only, with letter-spacing 0.05–0.12em (Butterick). Never letterspace lowercase.
- **Tracking:** tighten large display text slightly (general practice, roughly −0.015em at 24–40px and −0.02 to −0.03em at 48px+ [synth; Emil apple-design]); body 0; short all-caps labels positive. Never one letter-spacing for every size.
  - **Apple's SF Pro table is not a general rule.** It is +41/1000em at 6pt, 0 at 12pt, **negative from 13–23pt** (−26 at 17pt), **positive again from 24–76pt** (peak +14 at 28–30pt), and 0 at 80pt+. It exists to match SF's variable optical sizes in mockups. Don't port it to Inter, Geist or any other family; follow that foundry's optical-size and tracking guidance (Apple HIG Typography).
  - **Don't ship SF Pro or SF Symbols in a web app** (Apple's licence restricts them to Apple-platform apps). Use `system-ui, -apple-system` to reach the system font on Apple devices, and an equivalent icon set (Apple HIG Typography, SF Symbols).
  - Inter has optical sizes (text vs display); `font-optical-sizing: auto` where the font supports it.
- **Numbers:** `font-variant-numeric: tabular-nums` for tables, prices, timers and counters; `slashed-zero` for codes and IDs (MDN, Andersson/Inter).
- **Fonts:**
  - Use one UI family: a system stack (SF Pro), Inter, IBM Plex or similar.
  - Optionally add a display cut for large headings (Linear uses Inter Display for headings and Inter for UI).
  - Avoid Arial and Times as deliberate choices (Butterick).
  - Never mix more than two families.
  - Use a fallback stack with similar metrics to reduce layout shift (Emil).
- **Emphasis:** bold for UI emphasis, italic for citations or stress. Reserve underline for links (Emil, Butterick).
- **Punctuation:** `…` not `...`, curly quotes, a non-breaking space in `10 MB` (Vercel).
- **Dynamic Type / zoom:** at 200% text size nothing truncates, secondary items stack under the main text, columns reduce, and primary content stays on top (Apple HIG).
  - Scale content more than chrome: people "don't expect the tab titles to increase in size". Show as much useful text at the largest accessibility size as at the largest standard size.
  - Don't truncate in scrollable regions unless the full text is one tap away.
  - Interface icons that carry meaning grow with the text (Apple HIG Typography).
- **Widows and orphans** ("danglies", May-Li Khoe via Figma): `text-wrap: pretty` on paragraphs, `balance` on headings [synth implementation].

## 6. Composition rules of thumb (and when to adapt)

| Rule | Adapt when |
|---|---|
| One primary action per view | A comparison table may repeat one CTA per column, all styled the same |
| 3 type sizes in a view | Dense dashboards may need a 4th small size for metadata; keep weights consistent |
| 45–75 characters per line (aim ~66) | 40–60 on narrow/mobile columns; data tables and code views are not prose |
| Proximity before borders | Dense tables need row separators or zebra striping for scanning |
| Visible navigation | Single-purpose flows (checkout, onboarding) may hide global navigation deliberately |

## 7. Verification checklist
- [ ] Squint test passes at 10px blur.
- [ ] Every spacing value is a token from the scale (grep for stray px values).
- [ ] ≤ 3 sizes and ≤ 2–3 weights in a typical view; no weights below 400 for UI text.
- [ ] Body measure 45–75 characters (40–60 on narrow columns) at every breakpoint; paragraph line-height 1.4–1.6.
- [ ] No body text < 12px, no UI text < 11px; no fixed `height` on text containers.
- [ ] No Apple SF tracking values applied to non-SF fonts; no SF font files shipped on the web.
- [ ] Squint: no nav or chrome element out-shouts the content; recurring header actions sit in identical positions across 3+ screens.
- [ ] Inner group spacing < outer group spacing everywhere.
- [ ] Numbers in tables use tabular figures.
- [ ] Headings in sentence case and left-aligned unless there's a deliberate reason.

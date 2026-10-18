# 12 · Accessibility (WCAG 2.2 AA as the baseline)

**Status (Oct 2026):** WCAG 2.2 (W3C Recommendation, Oct 2023) is the standard to meet. SC 4.1.1 Parsing was removed. WCAG 3 is a Working Draft (reworked September 2026) and won't replace 2.x for years; don't treat it as normative (W3C WAI). On Apple platforms, the **Accessibility Nutrition Label** criteria (App Store Connect) are the concrete pass/fail bar for claiming support; they're used below as a checklist for web too.

Accessibility is a design input, not a final checklist. Put contrast-safe pairs into the tokens, focus styles into the base CSS, and keyboard behaviour into the component contracts. "For many, accessibility is a necessity. For others, it's a practicality" (captions in a noisy room) (Apple Accessibility docs).

## 1. Perceivable
- **Contrast (WCAG 1.4.3 / 1.4.11):**
  - Text 4.5:1; large text 3:1. "Large" means ≥ 24px regular or **≥ 18.66px (14pt) bold**. Bold below that size is *not* large text and still needs 4.5:1. (Apple's Accessibility Inspector treats any-size bold as 3:1; this skill doesn't follow that, see `conflicts.md`.)
  - **UI components: the visual information needed to identify a control and its state needs 3:1** against adjacent colours (control boundaries when they're the only cue, focus rings, state indicators, informative icons, chart marks). A standalone control identified by its icon or label (a FAB) may have a lower-contrast container; **clustered controls** (button rows, segmented options) each need ≥ 3:1 container separation so people can tell them apart (WCAG 1.4.11; M3 Color contrast).
  - **The difference between states** (checked vs unchecked, selected vs not) also needs 3:1, not a faint tint (Apple Sufficient Contrast criteria).
  - Aim for **7:1 on custom small-text pairs in dark mode** where feasible (Apple HIG Dark Mode). Not rounded: 4.49:1 fails. See `03-color-and-theming.md`.
  - **Check every mode separately:** light, dark, increased contrast, and translucent surfaces against their worst-case backdrop. "Many developers use gray-on-black for dark mode reading … more difficult to read for those with low vision" (Apple Sufficient Contrast criteria). If the default theme fails, an increased-contrast scheme that meets the minimums is the fallback, not an excuse.
- **Never colour alone** (SC 1.4.1): error = colour + icon + text. Links in body text need **more than one affordance** (colour plus underline or weight) (Android a11y). Chart series labelled directly or patterned.
- **Grayscale test:** the UI must be fully usable in grayscale. "If you can't use your own app in grayscale, rethink your app's design." Colour-vision deficiency affects "up to 10% of some populations". Fix with shape, icon, label, position or order; **don't remove colour, just don't rely on it**. Order chart colours the same as the legend. A "differentiate without colour" setting is a stop-gap; the default design should already pass (Apple Differentiate Without Color criteria). Problem pairs include red/green and **blue/orange** (Apple HIG Accessibility). A useful CVD test pair: `#FFA800` / `#4AC200` (Figma a11y).
- **Text alternatives:** meaningful `alt`; `alt=""` for decorative images, which must be ignored completely by assistive tech; icon-only buttons have `aria-label` matching their tooltip. Charts get a chart accessibility API or "a reasonably complete text alternative" (Apple VoiceOver criteria; see `14 §5`).
- **Structure:** one `<h1>`, headings in order, landmarks (`<header> <nav> <main> <aside> <footer>`), lists as lists, tables with `<th scope>`.
- **Reflow** (SC 1.4.10): content works at 320 CSS px (400% zoom) without two-dimensional scrolling. Exempt: maps, data tables, video, complex toolbars. Their surrounding headings, search and pagination are not exempt.
- **Text spacing** (SC 1.4.12): layout survives line-height 1.5, paragraph spacing 2×, letter spacing 0.12em and word spacing 0.16em. Don't fix heights on text boxes.
- **Larger text: ≥ 200%** (140% on watchOS) without overlap or ambiguity-causing truncation (Apple HIG Accessibility; Apple Larger Text criteria):
  - **Scale primary content first.** Repeated, predictable chrome (back buttons, tab bar labels) may stay small but needs a large-content alternative (tooltip, label view, Large Content Viewer). Primary action buttons may go full width.
  - **Side-by-side elements stack** at large sizes; drop columns (2 → 1); rows grow in height; single-line rows become multi-line (Apple HIG Layout).
  - Prefer wrapping to 2+ lines. Truncate only when the full text is reachable elsewhere (a detail view).
  - Show as much text at the largest accessibility size as at the largest standard size (Apple HIG Typography).
  - Test **long-word languages, RTL, and scripts with tall ascenders, descenders and diacritics**; fixed heights clip them.
  - **Browser zoom or Hover Text alone doesn't count** as text-size support. Use `rem`/`em` for type and spacing that should scale. Support Dynamic Type on iOS (body reaches > 300% at AX5) and `sp` units on Android.
  - Minimum sizes: iOS 11pt, macOS 10pt, watchOS 12pt (Apple HIG Accessibility); Android body never below 12sp (Android a11y).
- **Content on hover or focus** (SC 1.4.13): tooltips are dismissible (Esc), hoverable and persistent.
- **Media:** no autoplaying audio or video without controls; offer a global autoplay opt-out; captions, audio descriptions and transcripts; respect flashing-light reduction (Apple HIG Accessibility).

## 2. Operable
- **Keyboard everything** (SC 2.1.1), with no keyboard traps. Standard keys and shortcuts keep working with a screen reader on, and don't override system shortcuts (Apple VoiceOver criteria; Apple HIG Accessibility).
- **Keyboard model** (APG):
  - **Tab** moves between components; **arrow keys** move within composite widgets (toolbar, tablist, radio group, menu, listbox, grid, tree), so each has one tab stop.
  - Use **roving tabindex** or `aria-activedescendant`.
  - **No positive `tabindex`.**
  - Don't autofocus on load except on single-purpose pages.
- **Focus visible** (SC 2.4.7). Recommended style (Sara Soueidan):
  - `:focus-visible` with `outline` ≥ 2px solid, `outline-offset: 2px`, ≥ 3:1 against adjacent colours (aligned with SC 2.4.13 AAA focus appearance). Figma uses 3px + 3px offset; both comply.
  - A dashed outline needs ≥ 4px; an inset ring needs ≥ 3px.
  - Use `outline`, not only `box-shadow`, because outlines survive Windows forced-colours mode.
  - Where surfaces vary (light buttons on dark, brand colours), use a **two-tone ring**: `outline: 3px solid #000; box-shadow: 0 0 0 6px #fff`, or an accent ring with an offset gap.
  - Never `outline: none` without a replacement. Browser defaults are often < 3:1 on coloured buttons, so replace them with a tested ring.
  - Remote/D-pad and spatial UIs: focus feedback must be instant and bold, and never colour alone (use scale or outline) (Android TV; Apple HIG Layout tvOS).
- **Focus not obscured** (SC 2.4.11, new in 2.2): sticky headers, footers, cookie banners and chat widgets must not cover the focused element. Use `scroll-padding` (technique C43), close non-modal popovers on blur or Esc, and un-fix sticky bars at small or zoomed viewports (C34).
- **Focus order and stability** (SC 2.4.3; APG, Pickering; Apple VoiceOver criteria):
  - Order follows the visual order, forward *and* backward, with no skipping and no loops.
  - Closing a dialog or menu returns focus to its trigger.
  - Opening a modal or changing screens moves focus into the new content.
  - Deleting a list item moves focus to the next item, or to the previous one or the list heading.
  - Route changes in single-page apps move focus to the new `<h1>` or `<main>` and announce the page.
  - **Loading more content (infinite scroll, live refresh, background updates) never moves focus or the screen-reader reading position.**
  - Invisible, off-screen or background content is unreachable; modals make the background `inert`, and Esc closes them.
  - `document.activeElement` must never fall to `<body>`.
- **Target size** (SC 2.5.8, new in 2.2): ≥ 24×24 CSS px, or enough spacing that a 24px circle centred on each target doesn't overlap another. Implement with `min-width`/`min-height` (C42). Inline text links are exempt. Platform defaults to aim for:

  | Platform | Default | Minimum |
  |---|---|---|
  | iOS / iPadOS / watchOS | 44×44pt | 28×28pt |
  | macOS | 28×28pt | 20×20pt |
  | visionOS | 60×60pt | 28×28pt |
  | tvOS | 66×66pt | 56×56pt |
  | Android / Material | 48×48dp ("at least 48x48 CSS pixels" on web) | 48dp even if it extends past the visual |
  | Web touch | 44–48px (`pointer: coarse`) | 24px (WCAG AA) |

  (Apple HIG Accessibility; M3 Density; Android a11y.) **Spacing is as important as size:** ~12pt clear space around bezeled controls, ~24pt around borderless ones. The visual can be smaller than the hit area (M3: 40 inside 48), but expanded hit areas must not overlap neighbours. Density modes are opt-in and never shrink touch targets below 48. Lift the target to the whole row where it makes sense (a `<label>` wrapping the row and its checkbox) (Compose a11y).
- **Gestures and dragging** (SC 2.5.7, new in 2.2): **every drag, swipe, pinch or long-press has a visible, single-pointer control alternative** (swipe-to-delete plus a delete button; swipe-to-dismiss plus a close button). Long-press, hover and context-menu actions are also reachable as normal focusable actions (custom actions / a menu button). Use the simplest gesture for frequent actions; no custom multi-finger gestures. Anything that relies on edge swipes needs a button (Assistive Access has none) (Apple HIG Accessibility; Apple VoiceOver criteria; Android a11y; ruling in `conflicts.md`).
- **Pointer cancellation:** actions fire on up-event, so people can slide off to cancel.
- **Timing:** minimise auto-dismissing UI; prefer explicit dismissal. Toasts carrying actions stay until acted on or dismissed, and pause on hover and focus (Apple HIG Accessibility).
- **Motion:** honour `prefers-reduced-motion` as **replacement, not removal** (Apple Reduced Motion criteria; Apple HIG Accessibility; ruling in `conflicts.md`):
  - **Remove** decorative and ongoing motion, and everything in the trigger list: scaling, spinning, peripheral motion, parallax, animated blur and depth-of-field, z-axis depth changes, multi-axis or multi-speed motion, vortex effects, auto-advancing carousels.
  - **Replace** meaningful motion (a status change like "added to cart", a hierarchy transition) with a **dissolve, highlight fade or colour shift**. Replace x/y/z slides with fades; no blur-in/out; tighten springs (no bounce); keep gesture-tracked motion 1:1.
  - "Don't remove or modify all animations prematurely." Never make motion the only information channel; announce changes non-visually too. Allow cancelling mid-animation.
  - Avoid full-viewport moving backgrounds and slow oscillations near 0.2 Hz (Emil apple-design).
  - No content flashing more than 3 times per second. Pause controls for auto-moving content longer than 5s.
- **Skip link** to `<main>` on content-heavy pages.

## 3. Understandable
- `lang` on `<html>`; labels and instructions for every input (SC 3.3.2); error identification and suggestions in text (SC 3.3.1, 3.3.3).
- **Consistent help** (SC 3.2.6, new in 2.2): help and contact links sit in the same relative place on every page.
- **Redundant entry** (SC 3.3.7, new in 2.2): don't make people re-type information they've already given; auto-fill it or offer to reuse it.
- **Accessible authentication** (SC 3.3.8, new in 2.2): no cognitive tests (puzzles, transcribing) for login. Allow paste and password managers. Offer magic links or passkeys.
- No change of context on focus or input: a `<select>` that navigates on change fails SC 3.2.2.
- **Predictable gestures:** a gesture or key that works one way elsewhere on the platform works the same way in your product (Apple "Delivering an exceptional accessibility experience").

## 4. Robust: ARIA rules (W3C APG "Read Me First")
- **"No ARIA is better than bad ARIA."** Use native elements first: `<button>`, `<a href>`, `<input type=checkbox>`, `<dialog>`, `<details>`.
- **"A role is a promise."** Any custom role (tab, menu, listbox, grid, slider) commits you to its full keyboard behaviour. Building a custom component? Read the platform component's implementation and copy its accessibility behaviour (Compose a11y).
- Accessible name includes the visible label text (SC 2.5.3). Don't put `aria-label` text that contradicts what's on screen.
- **Accessible names (Apple VoiceOver criteria):**
  - Concise: "New message", not "Press to compose a new message".
  - Meaningful out of context: no "Click here" or "Learn more".
  - **Item-specific for repeated or destructive actions**: "Delete Blue T-shirt", not five "Delete" buttons.
  - **Never include the role or state** ("Unsubscribe checkbox, checkbox", `aria-label="Delete button"`). Role and state come from semantics; update state after interaction.
  - State the outcome ("Open this article") rather than "activate" (Compose a11y `onClickLabel`).
  - Group label + value into one stop ("Name, Rex": `<dl>` or a single accessible name); a clickable card or row is one stop with a meaningful name.
- `div` or `span` buttons need `role="button"`, `tabindex="0"`, and Enter and Space handling. Just use `<button>`.
- **Toggles (Heydon Pickering):**
  - **Toggle button:** `<button aria-pressed="true|false">` with a label that does *not* change ("Mute").
  - **Switch:** `role="switch" aria-checked`, labelled by an adjacent visible label, for on/off settings. Show a text or glyph state too (Apple "On/Off Labels").
  - **Never change both the label and the state.**
  - State is never conveyed by colour alone.
- **Navigation is not an ARIA menu (Pickering):**
  - Site navigation is `<nav><ul><li><a>`.
  - The hamburger is a `<button aria-expanded>` *inside* the `<nav>`, toggling `hidden`.
  - Reserve `role="menu"` for application command menus with full arrow-key and Esc behaviour and focus return.
  - Use `menuitemradio` + `aria-checked` for persistent choices.
- **Carousels:** one tab stop with previous/next buttons (or arrow keys), `role="group"` + `aria-roledescription="carousel"`; per-item actions reachable for every item, not only at the end (Apple sample, web translation [synth]).
- **Disabled controls:** prefer `aria-disabled="true"` (still focusable, with an explanation available) when people need to discover that a control exists, such as toolbar actions or menu items (APG). Never `pointer-events: none` on a disabled control; explain why it's disabled (ruling in `conflicts.md`). Disabled controls are contrast-exempt but should remain legible.
- **Live regions:** `role="status"` (polite) for toasts, transient banners and "Saved", announced "in a timely but non-disruptive manner"; `role="alert"` only for urgent errors. Keep the region in the DOM before injecting text (Apple VoiceOver criteria).
- **Selection ≠ focus;** style both distinctly.

## 5. Preferences, situations and inclusion
- Design for permanent, temporary and situational limits: one hand on a bus, glare outdoors, a noisy room, slow 3G, a broken trackpad. What helps permanent disability usually helps everyone. [synth; consistent with the WAI personas used in "What's New in WCAG 2.2"]
- **Honour system settings; don't make people set them twice.** An in-app control is fine only if it's equal or more granular (Apple Nutrition Label criteria, all). Don't gate accessibility features behind self-identifying as disabled; many older users wouldn't tick that box (Figma a11y).
- Web equivalents of the Apple settings:

  | Apple setting | Web signal | Do |
  |---|---|---|
  | Reduce Motion | `prefers-reduced-motion: reduce` | Replace slides/scale/springs with fades (§2) |
  | Increase Contrast | `prefers-contrast: more` | Near-solid backgrounds, **defined borders**; translucent/glass surfaces gain solid outlines (Linear iOS / Böhnke) |
  | Reduce Transparency | `prefers-reduced-transparency: reduce` | Solid surface, no `backdrop-filter` |
  | Dark Mode | `prefers-color-scheme` | Separately checked palette, not inversion |
  | Button Shapes | (none) | Links and buttons always have a non-colour affordance (underline, border) |
  | On/Off Labels | (none) | Switches show text or glyph state |
  | Classic Invert / high contrast | `forced-colors: active` | System colours, `outline`, no meaning in backgrounds |

- **Zoom and text-size controls you build** reflow content instead of enabling 2-D panning, offer a non-gesture control, and persist the chosen scale. Whole-UI scaling suits visual layouts (feeds, grids); text-only scaling suits reading (Compose scalable content).
- **Never disable browser zoom** (`user-scalable=no`, `maximum-scale=1`) (Emil mobile-native; see `18`).
- **Inclusive content:** address people as "you"; diverse fixture names; no idioms or jokes in core UI; gender-neutral wording (Apple HIG Inclusion; Apple Style Guide).

## 6. Testing protocol
Method from Apple "Performing accessibility testing for your app", adapted for web. Write the matrix down; re-run it every release ("Set a goal to make your app more accessible to more people in every release").
0. **List the main tasks per screen**, including first-run opt-out, sign-in and password reset, the **empty state**, undo, and **exiting without saving**. Every task must be completable with each setting and each assistive technology alone.
1. **Keyboard only:** Tab through everything, operate every control, open and close every overlay; focus is always visible and never lost or obscured.
2. **One setting at a time × every main task:** bold/larger text (200%), button shapes, increased contrast, reduced transparency, differentiate without colour / grayscale, colour filters, reduced motion, dim flashing lights, captions. Then **the combinations**: dark + increased contrast + reduced transparency; Bold Text + Increase Contrast + Reduce Transparency all on; Increase Contrast on with Reduce Transparency off (Apple Sufficient Contrast criteria; Apple HIG Dark Mode).
3. **Screen reader pass with the screen off:** VoiceOver Screen Curtain on iOS (three-finger triple-tap); on macOS toggle VoiceOver with Cmd-F5; NVDA on Windows. Check headings list, landmarks, form labels, names and states, reading order, error announcements, and that background loads don't reset position. VoiceOver, Voice Control and Switch Control need **real devices**, not the Simulator.
4. **Voice control pass:** "Show numbers" / "Show names", then "Tap ___" on every control. Visible label must match the accessible name.
5. Zoom to 200% text and 400% page (320px). Check reflow, stacking, nothing clipped or overlapping.
6. Contrast-check every token pair in every mode, plus focus ring, control borders and state differences.
7. Emulate reduced motion, forced colours, grayscale and colour-vision deficiencies in DevTools.
8. Run axe or Lighthouse, ideally `@axe-core/playwright` in CI. Treat passing as necessary, not sufficient.
9. Report each task × setting as pass/fail; list what needs a device you didn't have.

## 7. Base CSS
```css
:focus-visible { outline: 2px solid var(--color-focus-ring); outline-offset: 2px; border-radius: inherit; }
.surface-varied :focus-visible { outline: 3px solid #000; box-shadow: 0 0 0 6px #fff; }
@media (forced-colors: active) { :focus-visible { outline-color: Highlight; } }
.icon-button { min-width: 24px; min-height: 24px; }            /* 44px on coarse pointers */
@media (pointer: coarse) { .icon-button { min-width: 44px; min-height: 44px; } }
.visually-hidden { position:absolute; width:1px; height:1px; margin:-1px; padding:0; overflow:hidden;
                   clip: rect(0 0 0 0); white-space:nowrap; border:0; }

/* Glass / translucent chrome fallbacks (Apple HIG Materials; Linear iOS) */
.glass { background: color-mix(in oklch, var(--color-bg-surface) 72%, transparent); backdrop-filter: blur(20px); }
@media (prefers-reduced-transparency: reduce) { .glass { background: var(--color-bg-surface); backdrop-filter: none; } }
@media (prefers-contrast: more) { .glass { background: var(--color-bg-surface); outline: 1px solid var(--color-border-strong); } }

/* Reduced motion: replace movement, keep meaning (ruling in `conflicts.md`) */
@media (prefers-reduced-motion: reduce) {
  .slide-in, .sheet-enter { animation: none; transition: opacity 150ms ease; transform: none; }
  .parallax, .auto-advance, .ambient-motion { animation: none; }
}
```

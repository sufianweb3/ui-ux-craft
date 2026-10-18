# 05 · Motion and micro-interactions

## 1. Gate: should this animate at all?
Two failure modes, and the first is worse: animating something that shouldn't move, then animating it with the wrong ingredients (Emil, animate).

### 1a. Frequency decides first (Emil, emil-design-eng)

| How often people see it | Motion |
|---|---|
| 100+ times a day (keyboard shortcuts, command palette open/close, list highlight moving with arrow keys) | None. Ever. ("Raycast has no open/close animation.") |
| Tens of times a day (hover, list navigation, tab switches, context menus) | Remove, or nearly imperceptible (< 150ms, opacity/colour only) |
| Occasional (modals, drawers, toasts, popovers) | Standard durations below |
| Rare / first time (onboarding, completion, celebrations) | The only tier where delight is allowed |

- Keyboard-initiated actions never animate. Tab switches never slide; tabs are peers, not a hierarchy (Emil, animate-expo).
- Rauno: high-frequency actions should feel instant; novelty wears off. Apple: "In apps, generally avoid adding motion to UI interactions that occur frequently" (Apple HIG Motion).

### 1b. Name the purpose in one word (Emil, animate)
Before writing motion code, name its purpose: **feedback · spatial consistency · state indication · preventing a jarring change · explanation · delight** (delight only at the rare tier). If you can't name one, don't animate. "If the purpose is just 'it looks cool' and the user will see it often, don't animate."
- Data the user is reading or acting on doesn't move for style. A functional chart in a banking app gets no decorative motion (Emil).
- Motion is never the only carrier of information; pair it with a state change, text, or haptics (Apple HIG Motion).
- "Don't add motion for the sake of adding motion." Excessive animation can make people physically uncomfortable (Apple HIG Motion).

## 2. Duration (Emil; NN/g; Apple; binding defaults)

| Element | Duration | Notes |
|---|---|---|
| Button press, toggle, checkbox | 100–160ms | `:active` scale 0.97, 160ms `--ease-out` |
| Hover colour/opacity | 100–150ms `ease` | behind `(hover: hover) and (pointer: fine)` |
| Tooltips, small popovers | 125–200ms | after the first, neighbours open instantly (0ms) |
| Dropdowns, selects, menus, popovers | 150–250ms | from the trigger origin, from `scale(0.95)` |
| Modals / dialogs | 200–250ms | 250ms from `scale(0.96)`, centred origin; backdrop opacity 250ms |
| Toasts | ~400ms `ease` | a deliberate personality exception (Sonner); exit faster |
| Drawers, sheets, large surfaces travelling far | up to ~500ms on `--ease-drawer` | they move their own height; shorter if they travel less |
| Accordions (height) | ~200ms `--ease-out` | measure height in JS; never animate to `auto` |
| Marketing / explanatory | can be longer | never in product chrome |

- **Routine product UI stays under 300ms.** Only large surfaces that travel far (drawers, sheets, ~500ms) and toasts (~400ms) go longer, and only because the element's size and distance make shorter look abrupt. Anything seen hundreds of times a day gets minimal or no animation (decisions; Emil; NN/g allows 100–400ms, up to 500ms for drag).
- **Exits faster than entrances** (~20% shorter). NN/g example: 300ms in, 200–250ms out (Emil, NN/g).
- **Larger elements and longer travel take slightly longer**; small elements are fast (Emil; Material's size-based tiers).
- Spinners: if something must spin, spin it fast. A slow spinner looks like it's struggling (Emil).
- **Asymmetric timing:** slow where the user decides, fast where the system responds. Hold-to-confirm fills over 2s `linear` (progress shouldn't ease) and snaps back in 200ms `--ease-out` on release (Emil).
- **Stagger** 30–80ms per item (50ms default), decorative only, never blocking input (Emil).
- **Cohesion:** a playful product can be bouncier; a professional dashboard is crisp and fast. "When unsure whether motion feels right, the strongest move is often to delete it" (Emil, review-animations).

## 3. Easing (Emil)
- **Entering or exiting** → strong custom **ease-out** (fast start; the eye settles on the resting position).
- **Moving or morphing on screen** → **ease-in-out**.
- **Drawers and sheets** → the iOS-like drawer curve.
- **Hover colour or opacity change** → `ease`.
- **Constant motion** (spinner, marquee, hold-to-confirm progress) → `linear`.
- **Default** → ease-out.
- Never use plain `ease-in` for UI. A 300ms ease-in dropdown feels slower than a 300ms ease-out one. Built-in CSS curves are usually too weak for deliberate motion.
- Need another curve? Take it from easing.dev or easings.co; never hand-invent one. Five hand-typed beziers that almost match is a consolidation finding (Emil).

**Conflict:** NN/g allows ease-in on exits. Resolution: ease-out for UI enter and exit. Reserve ease-in only for elements accelerating fully off-screen where responsiveness doesn't matter.

Tokens (Emil Kowalski's published curves; the drawer curve is from the Ionic Framework; all in `assets/tokens.css`):
```css
--ease-out:    cubic-bezier(0.23, 1, 0.32, 1);    /* enter / exit */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);   /* on-screen movement */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);    /* drawers, sheets */
--dur-press: 160ms; --dur-tooltip: 125ms; --dur-popover: 200ms; --dur-modal: 250ms;
--dur-toast: 400ms; --dur-drawer: 500ms; --stagger: 50ms;
```

### Springs
- Material 3 replaced fixed easing and duration tokens with a **spring physics** system in 2025: spatial springs (position, size) may overshoot; effects springs (opacity, colour) must not.
- For gestures and interruptible motion, prefer real springs (Motion, WAAPI with a spring library, SwiftUI springs). CSS transitions can't inherit a finger's velocity (Apple via Emil).
- Default to **critically damped** (`bounce: 0`, damping ratio 1.0, response ~0.3–0.4s). Use bounce 0.1–0.3 (damping ~0.8) only when the gesture itself carried momentum (a flick); avoid bounce in most UI (Emil; Apple via Emil).
- When you must use CSS, Material publishes spring-mimicking beziers, e.g. standard spatial `cubic-bezier(0.27, 1.06, 0.18, 1)` and effects `cubic-bezier(0.31, 0.94, 0.34, 1)` at 150ms. M3's longer spatial durations (350–750ms) belong to expressive hero moments, not routine UI.
- **Never overshoot opacity or colour.** No y-values > 1 in their curves.

### Choosing the tool (Emil, animate): stop at the first that fits
1. CSS transition: hover, press, toggle. Transitions retarget mid-flight, so they're interruptible.
2. `@starting-style`: entry animation without JS.
3. CSS animation: predetermined motion that must stay smooth while the main thread is busy.
4. Web Animations API: JS control with CSS performance.
5. Motion (motion.dev): springs, layout animations, exit animations, gestures.

If the task needs a *component* (toast, drawer, menu, dialog, command palette), use a maintained accessible primitive (Radix, Base UI, React Aria; Sonner for toasts) instead of hand-rolling it (Emil, pick-ui-library).

## 4. Implementation rules and recipes
- **Animate `transform` and `opacity`.** `clip-path` is the sanctioned fourth property (reveals, tab highlights, hold-to-confirm, comparison sliders). `height` only for accordions. Never `transition: all`; list each property (Vercel, Emil).
- Prefer CSS transitions over keyframes for toggled UI; keyframes restart from zero when interrupted. No `@keyframes` on rapidly re-triggered elements (toasts, toggles) (Emil).
- **Interruptible always.** Accept input during animations; never make people wait for one to finish. "Let people cancel motion" (Apple HIG Motion, Rauno).
- **Natural entrances:** start from `scale(0.95)` (popovers), `0.96` (modals) or `0.97` (tooltips, press) plus `opacity: 0`, never `scale(0)`. Pure-fade entrances with no transform read as limp in standard mode (Emil, review-animations).
- **Origin-aware:** popovers and menus scale from their trigger (`transform-origin` from Radix/Base UI variables such as `--radix-popover-content-transform-origin` or `--transform-origin`). **Modals are exempt and stay centred** (Emil).
- **Exit the way it entered.** A toast that slides in from the bottom leaves through the bottom; a sheet revealed by sliding down doesn't dismiss sideways (Emil; Apple HIG Motion).
- **Move by percentages:** `translateY(100%)` moves an element by its own height (how Sonner and Vaul work) (Emil).
- If hover causes flicker, animate a child element rather than the hovered parent (Emil).
- A small blur bridge (2–5px, never > 20px) can smooth a crossfade (Emil).
- **Tooltips:** delay the first one (~300–500ms). Once one is open, show neighbours instantly with no animation (`[data-instant] { transition-duration: 0ms }`) (Emil, Vercel).
- **Input-dependent intensity:** motion may be more emphatic for direct touch and more subdued for mouse or trackpad (Apple HIG Motion, Liquid Glass behaviour).
- **Common fate:** elements animating together read as related, so don't animate unrelated items in sync (Figma, Gestalt).
- **Icon micro-animations:** bounce once = "it happened"; pulse/breathe = ongoing activity (recording, syncing); replace = state change; wiggle = something easily overlooked. Sparingly, never on high-frequency actions (Apple HIG SF Symbols).
- **Hover motion** only behind `@media (hover: hover) and (pointer: fine)`; touch gets an `:active` press state (Emil, mobile-native).

```css
.popover {
  transform-origin: var(--radix-popover-content-transform-origin, top center);
  transition: transform var(--dur-popover) var(--ease-out), opacity var(--dur-popover) var(--ease-out);
}
.popover[data-state="closed"] { transform: scale(var(--scale-enter-popover)); opacity: 0; }
.dialog { transition: transform var(--dur-modal) var(--ease-out), opacity var(--dur-modal) var(--ease-out); }
.dialog[data-state="closed"] { transform: scale(var(--scale-enter-modal)); opacity: 0; }   /* centred */
.sheet { transition: transform var(--dur-drawer) var(--ease-drawer); }
.sheet[data-state="closed"] { transform: translateY(var(--offset-sheet)); }
.btn:active { transform: scale(var(--scale-press)); transition: transform var(--dur-press) var(--ease-out); }
```
The scale and offset tokens collapse to `1` / `0` under reduced motion, so the same rules become fades (§5).

### clip-path recipes (Emil)
- **Reveal:** `clip-path: inset(0 0 100% 0)` → `inset(0)`.
- **Tab highlight:** duplicate the tab list, style the copy as active, and clip it to the active tab; transition the clip 250ms `--ease-in-out`. Text colour changes cleanly under the pill.
- **Hold-to-confirm (destructive):** overlay from `inset(0 100% 0 0)` → `inset(0)` over 2s `linear` while pressed; release snaps back in 200ms `--ease-out`.
- **Comparison slider:** `inset(0 50% 0 0)` driven by the handle.
- **Scroll reveal:** clip-path ~600ms `--ease-in-out`, marketing surfaces only, fire once.

### Gesture physics (Apple WWDC18 "Designing Fluid Interfaces", via Emil apple-design; verify numbers before citing them as Apple's)
- **Respond on pointer-down**, track 1:1 during the drag, commit on release. Keep the grab offset; use `setPointerCapture`; guard against multi-touch (`if (isDragging) return`).
- **Start from the presentation (current on-screen) value**, never the target, so a grabbed animation never jumps.
- **Hand off release velocity** to the spring. Normalised: `v / (target − current)` (50px/s over 100px = 0.5).
- **Project the landing point** and snap to the nearest target: `project(v) = (v / 1000) * d / (1 − d)`, with `d ≈ 0.998` (normal), `0.99` (snappier).
- **Commit vs reverse by velocity sign**, not by position. Velocity dismissal: `|distance| / elapsedMs > ~0.11` dismisses regardless of distance (Emil, Sonner).
- **Separate X and Y springs** for 2D motion.
- **Rubber-band at edges** instead of hard stops: `(o · D · 0.55) / (D + 0.55 · |o|)` for overshoot `o` over dimension `D`.
- ~10px of movement before committing to a drag direction; detect plausible gestures in parallel and cancel the losers.
- **Drawer curve from the M3/Android side:** map gesture progress through a decelerate curve (`cubic-bezier(0, 0, 0, 1)`), never raw linear; scale the surface toward ~90%; commit past a threshold (Android uses 35% for full-screen predictive back); on early release animate back and undo all state changes (Android Predictive back).
- Every swipe, drag or pinch has a visible button alternative (Apple HIG Accessibility; WCAG 2.5.7).

### Tuning key moments (Apple WWDC26-227)
Describe hero transitions as named phases ("1: card expands to detail; 2: rows stagger in"). Expose each phase's duration, easing (or spring stiffness, damping, mass), delay and stagger as tokens, and tune them in a dev-only panel beside the UI. The usual fix is shorter delays and stagger.

## 5. Reduced motion (Apple Reduced Motion criteria; Apple HIG Accessibility; web.dev; Emil)
**Simple:** fewer and gentler, not zero. Remove decorative motion; replace meaningful motion with a fade, dissolve, highlight or colour change.

- **Remove (decorative):** parallax, scroll-jacking, auto-advancing carousels and any ongoing motion (stop it, or give it a stop control), background loops, shimmer, multi-axis or multi-speed motion, spinning and vortex effects, animated blur and depth-of-field, full-viewport moving backgrounds, slow oscillation near 0.2 Hz.
- **Replace (meaningful):** status changes ("added to cart"), hierarchy transitions, opening a sheet or dialog. Swap x/y/z translation and scaling for a short opacity fade (~150–200ms) or a colour/highlight change. Don't animate z-depth or scale. Tighten springs to remove bounce. Gesture-driven motion still tracks the finger 1:1. Remove blur-in/out. "Never remove the feedback itself."
- "Don't remove or modify all animations prematurely" (Apple): a blanket `transition-duration: 0.01ms !important` kills the very fades that should remain. Don't ship it as the default.
- Large surfaces: fade them in place rather than sliding them during big repositions; ease dark↔light theme changes (Apple via Emil).
- Spinners and progress indicators are meaningful; keep them.
- JavaScript animations check `matchMedia('(prefers-reduced-motion: reduce)')` and listen for changes. Respect the OS setting; an in-app control must be equal or more granular (Apple Nutrition Label criteria).
- WCAG: no autoplaying motion longer than 5 seconds without a pause control (2.2.2); no flashing (2.3.1).

Pattern: drive motion *amounts* through tokens, then neutralise the amounts, not the transitions (`assets/tokens.css`):
```css
@media (prefers-reduced-motion: reduce) {
  :root {
    --scale-press: 1; --scale-enter-popover: 1; --scale-enter-modal: 1; --scale-enter-tooltip: 1;
    --offset-enter: 0px; --offset-sheet: 0px; --stagger: 0ms;
    --dur-drawer: 200ms; --dur-toast: 200ms;   /* fades don't need large-surface timing */
  }
  html { scroll-behavior: auto; }
  [data-motion="decorative"], [data-motion="decorative"]::before, [data-motion="decorative"]::after { animation: none !important; }
}
```
Opacity and colour transitions keep running, so state changes still read. Motion libraries: use their reduced-motion hook (e.g. Motion's `useReducedMotion`) to swap transforms for opacity.

**Related preferences** (ship them with the motion, Apple via Emil; Apple HIG Materials):
- `prefers-reduced-transparency: reduce` → solid backgrounds, no blur.
- `prefers-contrast: more` → near-solid backgrounds and defined borders.

## 6. Loading motion (Vercel, Hurff)
- **Skeletons mirror the final layout exactly**, so content arrives with zero layout shift.
- **Spinner show-delay** of 150–300ms, so fast responses never flash a spinner, and a **minimum visible time** of 300–500ms once shown, so it doesn't flicker (Vercel).
- Loading buttons keep their label and add an indicator. Disable re-submit, keep the width stable.

## 6a. Performance (Emil, animation-performance)
- **Frame budget:** 16.7ms at 60Hz, **8ms at 120Hz**. "Design against the smaller number." A layout recalculation on a complex page can exceed 100ms.
- **Property tiers:**
  - Composite only (cheapest): `transform`, `opacity`; also `filter`, `clip-path`, `background-color` in current engines, support uneven.
  - Paint + composite: `box-shadow`, `border-radius`, `color`.
  - Layout + paint + composite: `width`, `height`, `padding`, `margin`, `top`, `left`, `border-width`.
- **Swaps:** width/height/padding → `scale()`; top/left/margin → `translate()`; display/visibility → opacity; **`box-shadow` → `filter: drop-shadow()`** ("the one people miss").
- **React:** never `setState` per frame; write `ref.current.style.transform` or use a motion value.
- **Never drive child transforms through an inherited CSS variable on a parent:** every descendant recalculates (Vaul lagged past ~20 items). Set `transform` on the element itself.
- Motion's `x`/`y`/`scale` shorthands are CSS-variable-based and not hardware-accelerated; under main-thread load use `transform: "translateX(…)"` (a Vercel dashboard tab indicator dropped frames until it moved to CSS).
- Blur under 20px (2–5px softens a crossfade). Limit simultaneous blur and glass effects (Apple, Applying Liquid Glass).
- **`will-change`** only after you see a 1px shift or measure dropped frames, on the animating element only, never on `*` or large containers.
- **Diagnose in this order:** properties → busy main thread → re-renders per frame → gets worse as content grows (inherited var) → animated CSS variable → blur → `will-change`.
- Confirm with a DevTools Performance recording; remote-debug a mid-range phone. CPU throttling models a slow CPU, not a weak GPU.
- Dropped frames damage how people perceive the product "even if they couldn't pinpoint exactly why" (Apple WWDC26-251).

## 7. Test and review
- Play animations at 2–5× duration or 10% speed in the DevTools Animations panel; step frame by frame. Spam the trigger: it must never restart from zero (Emil).
- Test gestures on a real device (emulation can't reproduce touch feel). Test reduced motion, reduced transparency and increased contrast (DevTools Rendering panel), Safari, iOS Low Power Mode (which can throttle animations), and CPU/network throttling.
- Review animations again the next day with fresh eyes (Emil).
- Report each finding as verified (rendered/measured) or inferred from code (Emil).
- Spec handoff as a timeline: element, trigger, property, duration in ms, easing as cubic-bezier or spring parameters (NN/g).

## 8. Verification
- [ ] Purpose named in one word and frequency tier recorded for every animation; nothing on keyboard or 100+/day actions.
- [ ] Routine UI < 300ms; menus/popovers/modals 150–250ms; only drawers/sheets (≤ 500ms) and toasts (~400ms) longer; exits shorter than entrances.
- [ ] No `transition: all`, no `ease-in`, no `scale(0)`; only transform, opacity (and clip-path) animated.
- [ ] Popovers scale from the trigger origin; modals stay centred; exits leave the way they entered.
- [ ] `prefers-reduced-motion` removes travel/scale/parallax/blur but keeps short fades; no blanket 0.01ms kill switch.
- [ ] Hover motion gated by `(hover: hover) and (pointer: fine)`.
- [ ] No overshoot on opacity or colour; springs critically damped unless the gesture carried momentum.
- [ ] No animated `box-shadow`, `height` (outside accordions) or layout properties; no per-frame `setState`.
- [ ] Every gesture has a visible control alternative.

## 9. Glossary (terms from Emil, animation-vocabulary; definitions paraphrased)
- **Origin-aware:** an element grows from the control that triggered it.
- **Continuity transition:** an element persists across states so the eye can follow it.
- **Direction-aware:** content slides one way going forward and the opposite way going back.
- **Shared element transition:** one element morphs between two views.
- **Layout animation:** animating a change in position or size caused by layout.
- **Stagger:** a delay between items in a group entrance.
- **Orchestration:** sequencing several animations as one.
- **Rubber-banding:** resistance past a boundary that snaps back.
- **Momentum:** motion that continues after release with the gesture's velocity.
- **Interruptible:** it can be grabbed or reversed mid-flight without a jump.
- **Perceptual duration:** when a spring *feels* finished, before it mathematically settles.
- **Asymmetric easing/timing:** different curves or durations for in vs out.
- **Tabular numbers:** fixed-width digits so animating counters don't jitter.
- **Jank:** visible stutter from missed frames.
- **Compositing:** browser work done on the GPU layer, without layout or paint.

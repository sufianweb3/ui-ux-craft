# 18 · Mobile web and touch

Most "janky on mobile" reports are "a 300ms tap delay, a gray flash on tap, or a hover state that won't let go", not animation problems. Fix the platform layer with meta tags and CSS, not JavaScript (Emil mobile-native). Ship this baseline **before the first component**.

Sources: Emil Kowalski `mobile-native`, `apple-design`, `emil-design-eng` skills; Android edge-to-edge, accessibility and predictive-back guides; Apple HIG Accessibility, Layout; WCAG 2.2 (2.5.7, 2.5.8, 1.4.4, 1.4.10). Web mappings of native guidance are marked [synth].

## 1. Hard rules (Emil mobile-native)
1. **Every fix ships with its reason.** `user-select: none` on body text is a defect; on a button it's correct.
2. **Media queries over device sniffing.** Capabilities (`hover`, `pointer`, width), never UA strings or `isMobile` (Apple HIG Layout; Android adaptive).
3. **Touch and mouse aren't exclusive.** Tablets with trackpads, touch laptops: support both at once.
4. **Never disable zoom.** `user-scalable=no` and `maximum-scale=1` are accessibility failures (WCAG 1.4.4). Fix input zoom with 16px text instead.
5. **Test on hardware.** Emulation can't reproduce sticky hover, tap delay, safe areas or the on-screen keyboard. Say which fixes you couldn't verify ("needs device", `16 §3`).

## 2. Baseline
```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff">  <!-- match the header, not the brand -->
<meta name="theme-color" media="(prefers-color-scheme: dark)"  content="#0a0a0a">
```
```css
html {
  -webkit-tap-highlight-color: transparent;  /* then give every tappable element an :active state */
  -webkit-text-size-adjust: 100%;
  overscroll-behavior: none;                 /* app shells only; drop for document sites where pull-to-refresh is welcome */
}
input, textarea, select { font-size: 16px; }            /* < 16px makes iOS zoom on focus; or apply under (pointer: coarse) only */
button, a, [role="button"], label {
  touch-action: manipulation;                           /* removes double-tap-zoom delay */
}
button, [role="button"] {                               /* controls only, never body text */
  user-select: none; -webkit-user-select: none; -webkit-touch-callout: none;
}
.scroll-region { overscroll-behavior: contain; }        /* inner scrollers don't chain to the page */
.app-shell { height: 100dvh; }                          /* app shells, drawers, full-screen sheets */
.hero      { min-height: 100svh; }                      /* marketing heroes: dvh shifts layout mid-scroll */
.bottom-bar {
  padding-bottom: max(12px, env(safe-area-inset-bottom, 0px));
  padding-inline: max(16px, env(safe-area-inset-left, 0px)) max(16px, env(safe-area-inset-right, 0px));
}
.carousel { touch-action: pan-y; scroll-snap-type: x mandatory; overflow-x: auto; }
.carousel > * { scroll-snap-align: start; }

/* Press feedback for touch and mouse */
.pressable { transition: transform 160ms cubic-bezier(0.23, 1, 0.32, 1); }
.pressable:active { transform: scale(0.97); }

/* Hover only where hover exists */
@media (hover: hover) and (pointer: fine) {
  .item:hover { background: var(--color-bg-hover); }
}
```

## 3. Symptom → fix (Emil mobile-native)
| Symptom | Fix |
|---|---|
| Sticky hover after tap | Put every `:hover` rule inside `@media (hover: hover) and (pointer: fine)` (Tailwind v4 `hover:` already compiles to `(hover: hover)`; v3 needs `future.hoverOnlyWhenSupported`) |
| Grey flash on tap | `-webkit-tap-highlight-color: transparent`, plus an `:active` state on every tappable element |
| Laggy tap | `touch-action: manipulation`; give feedback on `:active` / `pointerdown` within 100–160ms, ease-out |
| Page zooms when an input is focused | Input text ≥ 16px (never fix by disabling zoom) |
| Layout jumps or is cut off by browser bars | `100dvh` for app shells and drawers; `min-height: 100svh` for heroes; avoid `lvh` and bare `100vh` |
| Content under the notch / home indicator | `viewport-fit=cover` + `env(safe-area-inset-*)` with a `0px` fallback; without the meta tag, env values are 0 |
| Keyboard covers the input | `interactive-widget=resizes-content` (Android resizes the layout viewport); scroll the focused field into view; never hide inputs behind the keyboard (Android layout basics) |
| Pull-to-refresh hijacks a custom scroller | `overscroll-behavior: none` on `html, body` (app shells), `contain` on inner scrollers; **never** `touchmove` + `preventDefault()` |
| Long-press selects button text | `user-select: none; -webkit-touch-callout: none` on controls only, never `body` |
| Horizontal carousel blocks vertical scroll | `touch-action: pan-y` on the carousel; `none` only for full custom gestures; prefer native scroll snap |
| Status bar colour clashes | Per-scheme `theme-color` matched to the header colour |
| Wrong keyboard | `type="email"`/`tel`/`url`; `inputmode="numeric"` (codes) / `"decimal"` (amounts); `autocomplete` tokens (`one-time-code`, `email`, `street-address`); `autocapitalize="none" autocorrect="off"` on usernames and codes; `enterkeyhint="send"/"search"/"done"/"next"` |

## 4. Touch targets and spacing
- **Touch targets 44×44 (Apple) / 48×48 (Material) CSS px**, even when the visible glyph is 20–24px; the hit area may exceed the visual, but expanded areas must not overlap neighbours. WCAG AA floor is 24×24 with spacing (`12 §2`) (Apple HIG Accessibility; M3 Density; Android a11y).
- **Spacing counts as much as size:** ~12pt clear around bezeled controls, ~24pt around borderless ones (Apple HIG Accessibility).
- Enlarge hit areas with padding or a pseudo-element, not by scaling the visual (Emil animate-expo, web mapping [synth]):
  ```css
  .icon-btn { position: relative; inline-size: 24px; block-size: 24px; }
  .icon-btn::before { content: ""; position: absolute; inset: -10px; }   /* 44px hit area */
  ```
- **Reach:** primary actions low and central on phones; on large tablets and unfolded foldables the top ~25% is hard to reach; nothing essential flush against the very bottom edge (Apple Designing for iOS; M3 Breakpoints).
- Separate destructive actions from frequent ones ("quit lives apart to prevent accidental clicks", Figma).

## 5. Gestures
- **Every gesture has a visible control alternative** (swipe-to-delete + a delete button; swipe-to-dismiss + a close button; pinch-zoom + zoom buttons). Long-press and hover actions are also reachable from a visible menu button (WCAG 2.5.7; Apple HIG Accessibility; Android a11y; ruling in `conflicts.md`).
- **No hover-only affordances on touch.** A "•••" that appears only on hover is unreachable; show it always on coarse pointers (Emil break-ui).
- Keep tap and drag targets out of the **screen-edge system gesture zones** (back swipe, home indicator) (Android edge-to-edge, web mapping [synth]).
- **Response on pointer-down**, commit on pointer-up; slide off to cancel (WCAG pointer cancellation). Feedback during a drag is continuous and 1:1, never only at the end (Emil apple-design).
- Gesture mechanics (Emil apple-design, emil-design-eng):
  - keep the grab offset (don't snap the element's centre to the finger); `setPointerCapture`
  - ~10px movement threshold before committing to a direction; detect competing gestures in parallel and cancel the losers
  - decide commit vs revert by **velocity sign and magnitude**, not position alone (velocity > ~0.11 px/ms dismisses regardless of distance)
  - rubber-band at boundaries instead of hard stops; guard against multi-touch while dragging
  - animate from the current on-screen value, never restart from the target; interruptible at any instant
- **Drag-to-dismiss sheets and drawers** follow Android's predictive-back contract: progress-driven preview mapped through a decelerate curve (`cubic-bezier(0, 0, 0, 1)`), surface scales toward ~90%, commit past a threshold, full revert and state undo on cancel (Android Predictive back, web mapping [synth]).
- Pay the double-tap delay only where double-tap actually exists (Emil apple-design).

## 6. Layout on small screens
- One column under ~600px; margins 16px, then 24px from 600px (M3 Breakpoints).
- Edge-to-edge: backgrounds and dividers bleed to the screen edge; text and controls are inset by safe areas (Android edge-to-edge).
- Body text 16px default, never below 12px; line length 40–60 characters on narrow columns (ruling in `conflicts.md`; Android a11y).
- Text scales: `rem` for type, no fixed heights on text containers, layouts survive 200% text (`12 §1`).
- Bottom sheets on compact widths replace popovers and menus (M3 Breakpoints; Apple HIG Popovers).
- Tabs and peer destinations don't slide laterally; only hierarchy moves (Android Translate designs; Emil animate-expo).
- Copy can be selected where people may reuse it (errors, IDs, addresses); turn `user-select` off only on control labels (Apple HIG Labels).

## 7. Testing (Emil mobile-native)
- Run the dev server on `0.0.0.0` and open it by LAN IP on a real phone; debug with Safari's Develop menu (iOS) or `chrome://inspect` (Android).
- Use a few-years-old phone, not only a flagship. Test with the keyboard open, landscape once, dark mode, 200% text, and installed-PWA mode if relevant.
- Check: no sticky hover, no grey flash, instant press feedback, no zoom on input focus, pinch-zoom still works, nothing under the notch or home indicator, the focused input stays above the keyboard, inner scrollers don't drag the page, the carousel doesn't block vertical scroll.
- **Report format:** what was wrong / what changed / **what needs a phone** (Emil mobile-native).

## 8. Anti-patterns
- `user-scalable=no`, `maximum-scale=1`; 14px inputs that zoom iOS.
- Ungated `:hover`; grey tap flash; no `:active` state.
- `100vh` app shells; `dvh` heroes that jump mid-scroll.
- `user-select: none` on `body`; `touchmove` + `preventDefault()`.
- Swipe-only or long-press-only actions; hover-only row actions.
- `isMobile` / UA sniffing for layout; features removed on small screens instead of moved into overflow.
- Bottom bars with no safe-area padding; brand-coloured `theme-color` that clashes with the header.

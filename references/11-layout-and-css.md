# 11 · Layout and CSS: from design tool to production code

## 1. Figma Auto Layout → CSS (Figma Help Center; [synth] mapping)

| Figma | CSS |
|---|---|
| Auto layout horizontal / vertical | `display:flex; flex-direction: row / column` |
| Wrap | `flex-wrap: wrap` |
| Grid flow (2025+) | `display:grid` |
| Gap between items | `gap` |
| Padding | `padding` (use logical `padding-inline` / `padding-block`) |
| Hug contents | intrinsic size (no width; `width: fit-content` if needed) |
| Fill container | `flex: 1 1 0` (in flex) / `1fr` (in grid) / `align-self: stretch` |
| Fixed | explicit `width`/`height` (rare for text containers) |
| Min / max width | `min-width` / `max-width` |
| Alignment | `justify-content` / `align-items` |
| Space between | `justify-content: space-between` |
| Ignore auto layout (absolute) | `position:absolute` inside a `position:relative` parent |
| Variables / modes | CSS custom properties redefined per `[data-theme]` |

Never give text containers a fixed height; text must be able to grow (Figma, WCAG reflow; M3 language height).

### Android layout weight → flexbox (Android LinearLayout; [synth] mapping)
Weight says how leftover space is shared. Default weight 0 means "take only your content size".

| Android (LinearLayout / Compose `Modifier.weight`) | CSS |
|---|---|
| `0dp` + `weight 1` on each child (equal columns regardless of content) | `flex: 1 1 0` + `min-width: 0` |
| `wrap_content` + `weight N` (share *leftover* space by ratio; 1, 1, 2 → ¼, ¼, ½ of the leftover) | `flex: N 1 auto` (columns differ if content differs) |
| `weight 0` / no weight | `flex: none` (`0 0 auto`) |
| `gravity` on the parent | `justify-content` / `align-items` |
| `layout_gravity` on a child | `align-self` |
| Message body fills the rest (`0dp` + weight 1) | `flex: 1 1 0; min-height: 0` |

Check: with uneven content, `flex: 1 1 0` siblings measure identical widths; `flex: 1 1 auto` siblings don't. Using `auto` basis when you meant equal columns is the classic mistake.

## 2. Flexbox essentials (Josh Comeau, "Interactive Guide to Flexbox")
- Flex is for **one dimension**. Items have a *hypothetical size* (`flex-basis`, or their content), then **grow** to fill or **shrink** to fit.
- **The min-width gotcha:** flex items default to `min-width: auto`, so long text or inputs overflow. Add `min-width: 0` to flex children holding long text or inputs, then truncate with `overflow:hidden; text-overflow:ellipsis; white-space:nowrap`.
- `flex-shrink: 0` on icons and avatars so they never squash into ovals.
- Use `gap`, not margins, between items: padding and gap on the parent, margins only at layout level (M3 Spacing). Use **auto margins** (`margin-inline-start: auto`) to push a group to the far end.
- Intrinsic wrapping with no media queries: `flex: 1 1 240px` on children plus `flex-wrap: wrap` (Comeau, after Adam Argyle).

## 3. Grid essentials (Comeau; MDN; Shadeed)
- Grid is for **two dimensions** and page shells.
- Use **`fr`, not `%`**, for tracks. Percentages plus gap overflow.
- Card collections: `grid-template-columns: repeat(auto-fit, minmax(min(240px, 100%), 1fr))`. The `min()` prevents overflow on tiny screens.
- Full-bleed child: `grid-column: 1 / -1`.
- Named areas for shells:
```css
.app { display:grid; grid-template-columns: 240px minmax(0,1fr); grid-template-rows: auto 1fr;
       grid-template-areas: "side top" "side main"; min-height: 100dvh; }
```
- `minmax(0, 1fr)` stops wide content (tables, code) from blowing out the track.
- **Don't reorder interactive content visually** with `order`, `grid-auto-flow: dense` or explicit placement. Tab and reading order follow the DOM. CSS `reading-flow` is not cross-browser yet (as of May 2026).
- **Split panes:** a thin 1px divider; `minmax()` limits on each pane so the divider never vanishes; a keyboard-operable resize handle (`role="separator"` with `aria-valuenow`) (Apple HIG Split views). In two flexible panes keep the divider visually centred, even with a nav rail (M3 Breakpoints).
- **Scrolling:** never nest scroll containers on the same axis. Show partial content at edges (a peeking next card) to signal more. Programmatic scroll moves as little as needed (`scrollIntoView({ block: 'nearest' })`). Paged scrolling keeps an overlap of one line or row (Apple HIG Scroll views).
- **Sticky headers:** a separating effect only when content is underneath, one per view; prefer a scroll-edge fade over a slab + divider (Apple HIG Layout, Scroll views; recipe in `assets/tokens.css`).

## 4. Responsive strategy
1. **Intrinsic first** (wrapping flex, auto-fit grids, `clamp()`), so the layout needs no breakpoints.
2. **Container queries for components** (Ahmad Shadeed): a card changes layout based on *its container*, so the same component works in a sidebar and in a main column.
```css
.card-wrap { container: card / inline-size; }
@container card (min-width: 420px) { .card { grid-template-columns: 160px 1fr; } }
.card-title { font-size: clamp(1rem, 0.9rem + 1.2cqi, 1.375rem); }
```
   Rules: wrap the component in a container element. A container can't be sized by its own content, and it can't query itself. Use `cqi` (container inline size) units with `clamp()` for fluid internals. Treat style queries as progressive enhancement.
3. **Media queries for the page shell** (sidebar collapses to a drawer or tab bar) and for user preferences (`prefers-color-scheme`, `prefers-reduced-motion`, `prefers-contrast`, `pointer: coarse`, `hover: hover`).
4. **Adapt by available space, not by device sniffing.** Functionality never disappears at small sizes; it moves into a tab bar, overflow menu or sheet. "Don't change your app's functionality based on the space it occupies"; only how much is visible changes (Apple HIG Layout; Android adaptive). No `navigator.userAgent` or `isTablet` logic for layout.
5. **Page-shell breakpoints, when you need them: Material's 600 / 840 / 1200 / 1600px** (compact < 600, medium 600–839, expanded 840–1199, large 1200–1599, extra-large ≥ 1600) (M3 Breakpoints; Android window size classes).

| Width | Margins | Panes | Navigation | Notes |
|---|---|---|---|---|
| < 600 | 16px | 1 | bottom bar (3–5) | full-screen dialogs, bottom sheets |
| 600–839 | 24px | 1 (2 only for low-density content, e.g. settings, 50/50) | rail | basic dialogs, menus instead of bottom sheets |
| 840–1199 | 24px | 2 recommended | rail | fixed side pane 360px |
| 1200–1599 | 24px | 2 | expanded rail / sidebar | fixed side pane 412px |
| ≥ 1600 | 24px | up to 3 (never more) | sidebar | side sheet as third pane, max 400px |

   - Pane gap 24px. Use height only for edge cases: under 480px tall (phone landscape), no two-pane layout.
   - **Moving up a breakpoint, decide what to reveal, divide, resize, reposition and swap.** "Additional space doesn't just mean making the same thing bigger." Swap only functionally equivalent components (nav bar → rail; bottom sheet → menu; never a button → chip) (M3 Breakpoints).
   - **Never stretch** buttons, inputs, forms or single-pane reading content to the full window width; cap with `max-inline-size` and change presentation instead (Android adaptive).
   - Reachability on large touch screens: limit interactions in the top 25% and right at the bottom edge (M3 Breakpoints).
   - **Resize is a state change:** selection, scroll position, form input and open panes survive breakpoint changes (Android canonical layouts).
   - Apple's equivalent is size classes (compact/regular); map them to the same width queries and container queries. Layout responds to size, never idiom or orientation (Apple HIG Layout).
6. **Safe areas (mobile web):** `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`; backgrounds bleed edge to edge; inset interactive content with `env(safe-area-inset-*)`; keep tap and drag targets out of screen-edge gesture zones (Android edge-to-edge; Apple HIG Layout; [synth] web mapping). Never disable zoom. Full touch baseline: `18-mobile-web-and-touch.md`.
7. Test at **320, 375, 768, 1024, 1440 and 1920px**, at the breakpoint boundaries **599/600, 839/840, 1199/1200, 1599/1600**, at Android's large-screen sizes **841×701 (foldable), 1024×640, 1280×800, 1600×900**, and at 200% text and 400% zoom (M3 Breakpoints; Android large-screen testing).

## 5. Modern CSS defaults worth using
```css
:root { color-scheme: light dark; -webkit-text-size-adjust: 100%; }
html { scroll-padding-top: var(--header-height, 0px); }   /* sticky headers don't hide focus (WCAG 2.4.11, C43) */
body { min-height: 100dvh; text-rendering: optimizeLegibility; -webkit-font-smoothing: antialiased; }
img, video, svg { max-width: 100%; height: auto; display: block; }
:where(input, button, textarea, select) { font: inherit; color: inherit; }
p, li, dd { max-width: 66ch; overflow-wrap: break-word; }   /* body 45–75ch */
.num { font-variant-numeric: tabular-nums; }
```
- Use **logical properties** (`margin-inline`, `padding-block`, `inset-inline-start`) for right-to-left support.
- Use `dvh`/`svh` units for mobile viewport heights.
- Use `:focus-visible` (not `:focus`) for keyboard rings.
- Use `@media (hover: hover) and (pointer: fine)` to scope hover effects, so touch devices don't get sticky hovers; give touch an `:active` state instead (Emil, mobile-native). Hover and press styling go on actionable items, never on whole toolbars, dialogs or nav containers (M3 States).
- Leave `user-select` on for content people may copy (errors, IDs, addresses, captions); turn it off only on control labels (Apple HIG Labels).
- Honour user preferences in CSS: `prefers-color-scheme`, `prefers-reduced-motion`, `prefers-reduced-transparency`, `prefers-contrast`, `forced-colors` (all handled in `assets/tokens.css`).
- Use `accent-color` to theme native checkboxes and radios cheaply.

## 6. Tailwind and utility-first projects
- Put tokens in the theme config or `@theme` (Tailwind v4) as CSS variables. Don't use arbitrary values (`p-[13px]`, `text-[#7a7a7a]`) except for one-off measured exceptions with a comment.
- Extract repeated utility clusters into components, not `@apply` soup.
- Keep class order consistent (use the Prettier plugin) [synth].

## 7. DevTools as a design tool [synth; widely taught practice]
- Inspect real products to understand *why* they work: computed spacing, type, colours, timing curves in the Animations panel.
- Use the contrast picker in Elements, the Rendering panel (emulate `prefers-reduced-motion`, `prefers-color-scheme`, vision deficiencies, forced colours), and the Performance panel for long tasks and layout shift.
- Use Lighthouse and axe for automated checks, but automation finds only part of accessibility issues; keyboard-test manually.

## 8. Verification
- [ ] No horizontal page scroll at 320px; tables scroll in their own container.
- [ ] Flex children with text have `min-width: 0`; icons have `flex-shrink: 0`.
- [ ] Grid tracks use `fr`/`minmax(0,1fr)`; no `%` + gap overflow.
- [ ] DOM order matches visual order.
- [ ] Components adapt with container queries where reused in different widths.
- [ ] Hover styles scoped to `(hover: hover) and (pointer: fine)`; no hover on containers.
- [ ] No same-axis nested scrollers; split-pane dividers never collapse to zero.
- [ ] Shell checked at 599/600, 839/840, 1199/1200, 1599/1600: pane count, nav component, 16→24px margins, state preserved.
- [ ] No full-width buttons, inputs or reading columns on wide windows.

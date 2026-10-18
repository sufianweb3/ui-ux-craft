# 03 · Colour systems, contrast, dark mode, theming

## 1. Principles

**Simple:** use mostly neutrals, one accent for action and focus, and reserved colours for status. Make sure everything readable meets contrast.

**Professional:**
- **Colour is a system, not a palette.** Build:
  - a neutral ramp
  - one accent ramp
  - semantic ramps for success, warning, danger and info
  - **roles** that map ramp steps to jobs
- **Neutral, low-chroma chrome; colour belongs to content and meaning.** Linear deliberately limited how much brand colour went into its neutral calculations. Apple: tint only the primary action, and "imbue colour in the content layer" (WWDC25).
- **Emphasis is scarce.** When everything is coloured, nothing stands out (Few, Apple, Google research).
- **Accent on the primary action's background, not everywhere.** Colour the *background* of the one primary action, not its glyph or label, and only one control: "Refrain from adding color to the background of multiple controls." Beyond that, the accent marks selection, unread/new badges and status, never static text (Apple HIG Color, Branding; WWDC26-251).
- **One colour, one meaning.** If the accent marks interactive elements, never use it on non-interactive text. Keep semantic colours few and fixed app-wide (the same error red everywhere). Never repurpose a role: no separator colour as text, no secondary-label colour as a background (Apple HIG Color; Android Colour).
- **Muted containers, one vivid action.** Full-strength primary/secondary/tertiary everywhere looks oversaturated. Use container (muted) tones for most coloured surfaces and keep the vibrant primary for the single most prominent action (Android Colour).
- **Saturation carries meaning.** Vivid red reads as a warning; desaturate red for non-error uses and recheck contrast (Figma colour theory). Don't use colour-wheel harmony schemes for product chrome; they suit brand and illustration (Figma; [synth]).
- **Gradients are not decoration.** Allowed only as an established brand asset, or as one consistent, deliberate signal of an AI/generative *state* (listening, thinking, generating) with a static fallback; never as generic hero, button or card decoration (Google Design: Gemini; see `17-ai-interfaces.md`).
- **Colour psychology is weaker than convention and context.** Red means destructive or error, green means success, amber means caution. Don't fight these conventions.

## 2. Contrast (WCAG 2.2: the hard floor)
- **Text:** ≥ 4.5:1.
- **Large text** (≥ 24px regular, or ≥ 18.66px / 14pt bold): ≥ 3:1. (SC 1.4.3) Bold alone does **not** make text "large": Apple's Accessibility Inspector treats any bold text as 3:1, but the WCAG threshold is the one to follow.
- **Non-text** (SC 1.4.11): ≥ 3:1 for the visual information *needed to identify* a UI component and its state: input and control boundaries when they're the only indicator, state indicators (checkmarks, toggle thumbs, selected fills), the **difference between states** (checked vs unchecked), focus rings, and informative icons or chart marks (WCAG 1.4.11; Apple Sufficient Contrast criteria).
  - A standalone control identified by its icon or label (a FAB, a filled button) doesn't need a 3:1 container edge; clustered controls (button rows, segmented options) do need ≥ 3:1 separation so people can tell them apart (M3 Color contrast).
  - Example: a `#767676` input border on white.
  - Light grey hairlines like `#e5e5e5` fail as the *only* boundary of an input.
- Ratios are **not rounded**: 4.47:1 fails.
- **Not exempt:** placeholder text that conveys information, hover and focus text, brand colours, and "trusted by" logo walls greyed out until hover.
- **Exempt:** truly disabled controls, decorative graphics and logotypes. But exempt doesn't mean invisible; keep disabled items legible.
- Always set foreground and background together, so a user stylesheet or dark mode can't create an invisible pair.
- **APCA vs WCAG:** Radix and Vercel reference APCA, a proposed newer perceptual contrast method. WCAG 2.2 ratios are the conformance requirement today. Meet WCAG 2.2 and optionally also check APCA.
- **Aim higher in dark mode.** For custom foreground/background pairs, aim for 7:1 on small text where feasible, especially in dark mode; 4.5:1 remains the floor. Grey-on-black body text is a common failure for low-vision readers (Apple HIG Dark Mode; Apple Sufficient Contrast criteria).
- **Translucency counts.** Text on glass or blur must pass against the *worst-case* backdrop (brightest and busiest content that can scroll under it) (Apple HIG Materials; Apple Sufficient Contrast criteria).

### Worked example: platform default colours are not text colours
Apple's default system colours fail small-text contrast on white (computed from Apple's published 2025 RGB values, Apple HIG Color):

| Apple colour | Default on white | Increased-contrast variant on white |
|---|---|---|
| Blue (0,136,255) | 3.52:1 ✗ | 4.57:1 (30,110,244) |
| Red (255,56,60) | 3.57:1 ✗ | 4.56:1 (233,21,45) |
| Green (52,199,89) | 2.22:1 ✗ | 4.54:1 (0,137,50) |
| Orange (255,141,40) | 2.31:1 ✗ | 4.55:1 (197,83,0) |

The bright defaults are for fills, icons and large text; the increased-contrast set is tuned to just clear 4.5:1 and is the text-safe set. Lesson for any palette: bright hues for fills, darker steps for text. Never hard-code Apple's values; "the actual color values may fluctuate from release to release" (Apple HIG Color).

**CVD test pair:** `#FFA800` orange vs `#4AC200` green look nearly identical under protanopia. About 1 in 12 men and 1 in 200 women have a colour-vision deficiency (Figma accessible design). Pass a grayscale check: the UI must stay usable with colour removed (Apple Differentiate Without Color criteria).

## 3. Build ramps in a perceptual colour space

**Why:** in HSL, "50% lightness" yellow and blue have wildly different perceived brightness, so the same step has different contrast for each hue. Stripe found none of its old greys passed. It rebuilt the palette in a perceptually uniform space so every hue's step N has the same lightness. That gives a simple rule: **any two steps ≥ 5 apart pass for small text; ≥ 4 apart pass for icons and large text** (Stripe).

- Use **OKLCH** in CSS: `oklch(L C H)`. Evil Martians (Sitnik) moved from RGB/HSL to OKLCH: predictable lightness, easy derived states, P3 support. LCH has a blue→purple hue shift that OKLCH fixes.
- **Never** generate shades with Sass `darken()`/`lighten()` or HSL arithmetic (muddy results, inconsistent contrast).
- Keep chroma high enough that hues stay distinguishable, but reduce it near very light and very dark ends to stay in gamut.
- **Wide gamut:** sRGB first, P3 override inside `@media (color-gamut: p3)`. Interpolate gradients `in oklab`. Lint gamut with `stylelint-gamut` (Evil Martians).

### Step roles (pick one model and use it consistently)
Explore hierarchy and elevation with black/white opacities first, then derive tokens; tune neutrals per token in hue, chroma and lightness. Linear's 2026 neutrals moved from cool blue-grey to a warmer, less saturated grey ("too warm… looks muddy") (Linear 2026 refresh).

- **Radix 12-step:**
  - 1–2: app and subtle backgrounds
  - 3–5: component backgrounds at rest, hover and active
  - 6–8: borders, from subtle to strong focus
  - 9–10: solid fills and their hover
  - 11–12: low- and high-contrast text
- **Vercel Geist 10-step:**
  - 1–3: component backgrounds (default, hover, active)
  - 4–6: borders
  - 7–8: high-contrast solids
  - 9–10: text
  - Gray-alpha only for overlays; draw each border once.
- **Material 3 roles:** pairs such as `surface`/`on-surface`, `primary`/`on-primary`, `primary-container`/`on-primary-container`. Never pair across roles. Use `outline` for interactive boundaries and `outline-variant` only for decorative dividers. Note that Material's pairs promise only 3:1; check small text against 4.5:1 yourself.

## 4. Semantic tokens (what components use)

```css
--color-bg-app; --color-bg-surface; --color-bg-surface-raised; --color-bg-subtle;
--color-bg-hover; --color-bg-active; --color-bg-selected;
--color-text-primary; --color-text-secondary; --color-text-tertiary; --color-text-disabled;
--color-text-on-accent; --color-text-link;
--color-border-subtle;   /* dividers, decorative ≥ ~1.3:1 */
--color-border-control;  /* inputs, checkboxes ≥ 3:1 */
--color-border-strong;
--color-accent; --color-accent-hover; --color-accent-active; --color-accent-subtle;
--color-focus-ring;
--color-success-*, --color-warning-*, --color-danger-*, --color-info-*  /* each: fg, bg-subtle, border, solid */
```

## 5. Derive states instead of hand-picking them
- Hover is one ramp step up (Radix: 3→4, 9→10), or relative colour: `oklch(from var(--btn-bg) calc(l - 0.05) c h)` (Evil Martians).
- Hover, active and focus should have *more* contrast than rest, not less (Vercel).
- One hover rule can serve every variant through a custom property: `.btn { background: var(--btn-bg); } .btn:hover { background: oklch(from var(--btn-bg) calc(l - 0.04) c h); }`.
- **Alternative: Material's state layer.** An overlay of the *content* colour (`currentColor`) between container and content at **hover 8%, focus 10%, pressed 10%, dragged 16%**; disabled content at 38%. One rule works on any container colour without per-variant hover tokens. Only one hover, focus, pressed and dragged element at a time; style the actionable items, never whole toolbars, dialogs or nav containers (M3 States). Pick one technique per system: state layers suit many container colours; ramp steps suit tightly tuned palettes.
```css
.btn { position: relative; isolation: isolate; }
.btn::before { content: ""; position: absolute; inset: 0; border-radius: inherit; background: currentColor;
               opacity: 0; transition: opacity 120ms ease; z-index: -1; pointer-events: none; }
@media (hover: hover) and (pointer: fine) { .btn:hover::before { opacity: var(--state-hover, .08); } }
.btn:focus-visible::before { opacity: var(--state-focus, .10); }   /* plus the ≥ 2px focus ring */
.btn:active::before { opacity: var(--state-pressed, .10); }
```
- Disabled states are exempt from contrast (WCAG; "Disabled states don't need to meet Material's contrast requirements", M3 States) but stay legible.

## 6. Coloured backgrounds
- Reduce text contrast with the background's hue, not grey. Use white at reduced opacity, or a lighter tint of the same hue; grey text on colour looks dirty (Refactoring UI).
- Tint borders and shadows to the surface hue (Vercel, Comeau).

## 7. Dark mode, increased contrast and themes
- **Follow the OS by default.** Respect `prefers-color-scheme` and react live to changes without a reload. Apple: "Avoid offering an app-specific appearance setting". If the product needs a theme switch (common on the web), offer **System (default) / Light / Dark**. Never lock the app to light (Apple HIG Dark Mode; Android Themes).
- **Four values per colour token:** light, dark, increased-contrast light and increased-contrast dark (`@media (prefers-contrast: more)`). "Even if your app ships in a single appearance mode, provide both light and dark colors" (Apple HIG Color; Adopting Liquid Glass). `assets/tokens.css` ships all four, with computed ratios.
- **Generate themes from a few inputs.** Linear went from 98 hand-set variables to 3 inputs (base, accent, contrast) in LCH, producing light, dark and high-contrast themes from one generator.
- Switch themes by redefining **semantic tokens** under `[data-theme="dark"]` or `@media (prefers-color-scheme: dark)`, never with per-component media queries (Evil Martians, Curtis).
- Dark mode isn't inversion:
  - Raised surfaces get *lighter* in dark mode.
  - Shadows read weakly in dark mode, so use surface steps and subtle borders.
  - Desaturate and lighten accents.
  - Avoid pure `#000` backgrounds and pure white body text for long reading [synth, common practice].
  - Verify elevation still reads in dark mode (Vercel). Raised layers (popovers, sheets) use the lighter "elevated" background set; a custom background can break that depth cue (Apple HIG Dark Mode, base vs elevated).
  - Dim content images with white backgrounds slightly in dark mode so they don't glow (`filter: brightness(.9)` or a tinted container) (Apple HIG Dark Mode; [synth] CSS).
  - Some icons need separate light and dark assets (a dark outline on light, a border on dark) (Apple HIG Dark Mode).
- Set `color-scheme: light dark` (or `dark`) on `:root` so native controls and scrollbars match. Set `<meta name="theme-color">` to the page background (Vercel).
- Make text darker in light mode and lighter in dark mode when you need to raise contrast (Linear).
- Respect `prefers-contrast: more` (darker text in light, lighter in dark, control-strength borders, near-opaque glass with a solid outline) and `forced-colors: active` (Apple HIG Color; Linear iOS).
- **Test the combinations, not just each setting:** dark + increased contrast + reduced transparency together, and increased contrast with reduced transparency off. Dark-on-dark text is the usual failure (Apple HIG Dark Mode; Apple Sufficient Contrast criteria).

## 8. Status colour
- Status always gets redundancy: colour + icon + text. Red/green alone fails colour-blind users (WCAG 1.4.1, Few, NN/g).
- Keep semantic hues consistent everywhere. Don't use the danger hue for a brand accent.

## 9. Verification
- [ ] Every text/background pair in all four contexts (light, dark, light + IC, dark + IC) has been computed against 4.5:1 (or 3:1 for large text). Compute OKLCH values after conversion to sRGB (browsers clip or gamut-map out-of-gamut colours), never by eye.
- [ ] Accent appears only on the primary action's background, links, selection, focus and status; never on static text.
- [ ] Theme follows the OS; any switch offers System / Light / Dark with System as default.
- [ ] Control borders, focus ring, checkbox and toggle states ≥ 3:1 against adjacent colours.
- [ ] No hex or rgb literals in components; only semantic tokens.
- [ ] Status never relies on colour alone.
- [ ] Dark, light and high-contrast themes generated from the same token source.
- [ ] Gradients interpolated in oklab; P3 values have sRGB fallbacks.

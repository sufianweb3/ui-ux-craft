# 04 · Depth, elevation, shape, icons, polish

## 1. Elevation and shadows (Comeau, Vercel Geist, Refactoring UI)

**Why shadows exist:** they say "this is closer to you". Closer things get noticed first. Use shadows for only two purposes: to raise the prominence of a specific element (a dialog above a page, a popover above content) and to make the interface feel tactile (Comeau).

**Rules:**
- **One light source.** Every shadow in the app shares the same x:y offset ratio. Comeau's examples use vertical offset = 2× horizontal (light from the top-left); Vercel's are vertical-only. Pick one and keep it.
- **Layer shadows.** Use 2–5 shadows with doubling offsets and blur instead of one big fuzzy shadow (technique credited to Tobias Ahlin).
- **Tint the shadow to the surface.** Transparent black desaturates coloured backgrounds. Match the hue with lower saturation and lightness, via a `--shadow-color` custom property set per surface.
- **2–3 elevation tokens** (small, medium, large). Higher elevation means larger offset and blur and lower alpha per layer.
- **Lowest elevation that still reads.** Don't stack elevations. Tie elevation to z-index: card < popover/menu < dialog < toast (Vercel).
- Pair a shadow with a subtle **semi-transparent border** for crisp edges on light backgrounds (Vercel). But don't put border + heavy shadow + background shift on the same element (Refactoring UI).
- **Offset over blur:** a y-offset reads as light from above; big blur or spread with no offset reads as a grey halo (Refactoring UI).
- **Separate by tone first, shadow second.** Default separation is a surface-tone difference; use visible shadows only (a) to protect elements over busy imagery or (b) to lift on interaction. "When it comes to applying shadows, less is more" (M3 Elevation).
- **Material 3 benchmark:** six levels at 0 / 1 / 3 / 6 / 8 / 12dp. Resting UI uses only levels 0–3; 4–5 only while hovered or dragged; hover/focus raises one level. Modal scrim = 32% (`--scrim`). Smaller, sharper shadow = closer (M3 Elevation). Consistent with the 2–3 token rule above.
- **Don't animate multi-layer `box-shadow`.** It's a paint-tier property. Animate `filter: drop-shadow()` instead, or the opacity of a pseudo-element that holds the larger shadow (Emil animation-performance; Comeau).
- `filter: drop-shadow()` follows an element's real shape (tooltip arrows, transparent images). Safari can lag when the element contains text inputs (Comeau).
- **Dark mode:** shadows weaken, so lean on lighter raised surfaces and borders, and verify (Vercel). A common high-end treatment: dark themes drop shadows and use a 3–4-step lighter surface ladder plus hairlines; light themes use an inset 1px ring (~8% ink) plus 2–3 stacked low-alpha drops rather than one heavy drop (pattern in community DESIGN.md extractions, unverified; consistent with Comeau and Vercel).

```css
:root {
  --shadow-color: 220 15% 30%;              /* H S L, matches the neutral surface */
  --elev-1: 0 1px 1px hsl(var(--shadow-color) / 0.06), 0 1px 2px hsl(var(--shadow-color) / 0.06);
  --elev-2: 0 1px 2px hsl(var(--shadow-color) / 0.07), 0 2px 4px hsl(var(--shadow-color) / 0.07),
            0 4px 8px hsl(var(--shadow-color) / 0.07);
  --elev-3: 0 1px 2px hsl(var(--shadow-color) / 0.06), 0 2px 4px hsl(var(--shadow-color) / 0.06),
            0 4px 8px hsl(var(--shadow-color) / 0.06), 0 8px 16px hsl(var(--shadow-color) / 0.06),
            0 16px 32px hsl(var(--shadow-color) / 0.06);
}
```
(Structure follows Comeau's layered approach; alphas are restrained defaults to tune per surface.)

## 1a. Materials, glass and translucency (Apple HIG Materials; Adopting Liquid Glass; Apple via Emil)
**Simple:** glass is for the floating control layer, never for content.

- **Functional layer only.** Translucent material (`backdrop-filter`) belongs to nav bars, toolbars, tab bars, sheets and popovers floating above content. "Don't use Liquid Glass in the content layer." Never on content cards. Exception: a slider or toggle may look glassy only while being dragged (Apple HIG Materials).
- **Sparingly, and never stacked.** Limit glass to "the most important functional elements"; never layer glass on glass, or a light translucent surface on another. Group adjacent glass controls in one container so they blend and morph together; limit simultaneous blur effects for performance (Adopting Liquid Glass; Applying Liquid Glass to custom views; Apple via Emil).
- **Variant by purpose.** Frosted ("regular") for anything with much text (alerts, sidebars, popovers); "clear" only over photos or video, adding a **35% black dim layer** (`--scrim-media`) when the media is bright. Choose a material by purpose, never by the tint it imparts. Keep tertiary/quaternary text off the thinnest materials (Apple HIG Materials).
- **The container owns the material.** Remove custom backgrounds from floating bars and from popover/sheet content. Large glass panels use a rounded rectangle, not a capsule. Hide a whole unavailable toolbar slot rather than leaving an empty pill (Adopting Liquid Glass; Applying Liquid Glass).
- **Scroll-edge fade, not slab + divider.** Under a sticky header, use a fade or blur mask at the scroll edge that appears only when content is underneath, instead of an opaque bar plus a 1px divider. "Instead of applying a solid or semi-opaque background color beneath controls, use a scroll edge effect" (Apple HIG Layout).
- **Colour on glass:** glass has no inherent colour. Tint only what truly needs emphasis (primary action, status); over colourful content keep bars monochrome; the resting state (top of scroll) must be legible (Apple HIG Color).
- **Dense pro tools:** blur, masking and lighting for depth, **no refraction** (it hurts legibility); a variable blur at scroll edges (Böhnke, Linear).
- **Web recipe [synth]:** `backdrop-filter: blur(20px) saturate(180%)` over a ~60–80% opaque surface (Apple via Emil). Over blur, raise text contrast and use a slightly heavier weight.
- **Fallbacks are mandatory:**
  - `@media (prefers-reduced-transparency: reduce)` → opaque surface, no blur.
  - `@supports not (backdrop-filter: …)` → opaque surface.
  - `@media (prefers-contrast: more)` → near-opaque background plus a solid outline (Linear iOS; Apple via Emil).
  - All three ship in `assets/tokens.css` (`.glass`).
- **Glass and motion:** materialise glass (animate blur + scale together) rather than plain-fading it (Apple via Emil); under reduced motion, a fade.

## 2. Shape and radius
- **Concentric corners:** inner radius = outer radius − padding (never inner > outer). A capsule's radius = height / 2. Pinched or flared nested corners are a tell of carelessness (Apple WWDC25 "concentricity"; Vercel "nested radii").
- **A small radius set mapped to size and elevation.** Geist uses 6 / 12 / 16px by elevation level. Typical scale: 4 (chips, small inputs), 6–8 (buttons, inputs), 12 (cards, popovers), 16 (dialogs, sheets), full (pills, avatars).
- **Platform:** Apple uses capsules for touch controls but rations them in dense desktop UI. Material 3 Expressive deliberately mixes round and square shapes for tension. Choose per platform and density, then stay consistent.
- **Material 3 roundedness scale** (dp ≈ px): None 0 · Extra small 4 · Small 8 · Medium 12 · Large 16 · Large increased 20 · Extra large 28 · Extra large increased 32 · Extra extra large 48 · Full. On Material products, map components to these steps rather than inventing values. M3 buttons default to Full; remap if the product needs less rounding (M3 Shape).
- **No large radii on dense content.** "Be careful not to apply large or full corners to information-dense components, such as cards." Desktop-dense UIs favour small radii (M3 Shape).
- **Inner corners:** tightly grouped controls (segmented or split buttons, menus) can use large outer and small inner corners (M3 Shape).
- **Expressive shapes** (blobs, irregular forms) only on visual elements (media, avatars, hero moments), never on text-heavy containers (M3 Shape).
- **One CTA radius grammar per screen:** all pills or all rounded rectangles; don't mix a pill CTA with 6px buttons in one view [synth; pattern in community DESIGN.md files, unverified].

## 3. Icons
- **One family, one stroke weight**, consistent size, detail and perspective. Match icon weight to adjacent text weight (Apple HIG Icons).
- **Use icons at their drawn size** (16, 20, 24). Don't scale a 16px glyph up to 64px; use a larger-size set or put it inside a tinted shape (Refactoring UI).
- **Optically centre** asymmetric glyphs; a play triangle needs a nudge to the right. Use padding, not a bigger icon (Apple).
- **Standard metaphors** (Apple HIG Icons standard-symbol table): More = ellipsis (overflow menus only, nothing else), Share = square + up-arrow, Filter = three decreasing lines, Delete = trash, Compose = square + pencil, Duplicate = plus on stacked squares, Undo/Redo = U-turn arrows, Account = person in circle, Search = magnifying glass. Standard actions keep the platform's own glyph even in a custom icon set; never re-skin familiar icons creatively (Apple WWDC25/26-251, 292). SF Symbols are licensed for Apple-platform apps only; on the web use the equivalent glyph from the project's icon library.
- **Variants carry meaning:** outline in toolbars, lists and next to text; filled for the selected state (tab bars, selected nav); enclosed (in a circle or square) for legibility at tiny sizes; a slash for unavailable (Apple HIG Icons, SF Symbols).
- **Fewer, smaller icons in dense UI.** No decorative coloured icon chips; icons are for recognition at a glance (Linear 2026).
- **Custom sets:** recognisable, consistent, not overly detailed so they hold up small. Bake optical-centring padding into the asset; use SVG snapped to whole-pixel control points at 1x (Apple HIG Icons, Images; WWDC26-251).
- **Label icons** unless the glyph is universally understood. Google's research found removing text labels from email actions hurt usability. Icon-only buttons need `aria-label` and a tooltip.
- **Vector only.** No text baked into icons. Status icons must not look like buttons (web.dev offline guidance).
- **No emoji as icons** in product UI [synth extending Refactoring UI's "everything has an intended size" and Apple's consistency rules].

## 4. Premium polish details (Vercel Web Interface Guidelines, Emil, Rauno)
- **Hit area ≥ visual.** A 16px icon button gets ≥ 24px (desktop) or 44px (touch) of hit area via padding or `::before { inset: -8px }`. The visible state layer can be smaller than the target (M3: 40 inside 48); set explicit minimum sizes so expanded hit areas never overlap neighbours (Compose a11y). Platform target tables: `02-visual-foundations.md`.
- **Optical alignment:** align text baselines and icon centres, not bounding boxes. Small nudges (±1px) are allowed when the eye says so.
- **Pressed feedback:** `:active { transform: scale(0.97) }` (range 0.95–0.98; Figma uses 0.98) with `transition: transform 160ms var(--ease-out)`. Feedback fires on pointer-down, not release (Emil; Apple via Emil).
- **Focus rings** are crisp and consistent. See `12-accessibility.md`.
- **No dead zones:** whole rows, whole checkbox labels and whole cards (when they're links) are clickable (Vercel).
- **Anti-aliasing:** animate a wrapper, not the text node. If text shimmers, try `will-change: transform` or `translateZ(0)` (Vercel, Emil).
- **Avoid gradient banding** from CSS masks; use background images where needed (Vercel).
- **Scrollbars:** test with macOS "Always show scrollbars" and on Windows. Don't let a scrollbar break the layout; consider `scrollbar-gutter: stable` (Vercel; property recommendation is [synth]).
- **Restraint test:** remove one decorative element at a time. If nothing is lost, keep it removed (Rams: "as little design as possible").

## 5. Verification
- [ ] Every `box-shadow` comes from elevation tokens; same x:y ratio everywhere; no `rgba(0,0,0,…)` shadows on coloured surfaces.
- [ ] Nested radii are concentric (inner = outer − padding).
- [ ] One icon set and stroke weight; icon-only buttons have accessible names.
- [ ] Hit areas meet target sizes.
- [ ] No element carries border + shadow + background shift at once without a reason.
- [ ] Every `backdrop-filter` sits on nav, toolbar, sheet or popover, never on a card in a scrolling list; no glass on glass.
- [ ] Glass has reduced-transparency, no-support and increased-contrast fallbacks; text on it passes over the brightest and busiest backdrop.
- [ ] Sticky headers use a scroll-edge fade, not an always-on slab + divider.
- [ ] ≤ 3 elevation levels at rest; shadows only for busy backdrops or interaction lift.

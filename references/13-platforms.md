# 13 · Platform conventions

Universal principles (hierarchy, contrast, feedback, Fitts, Hick) apply everywhere. Conventions differ by platform. Follow the target platform's conventions unless you can name the cost of breaking one and the gain from it. Mobile **web** specifics (viewport, 16px inputs, safe areas, touch-action, hover gating) live in `18-mobile-web-and-touch.md`; AI features in `17-ai-interfaces.md`.

## 0. Cross-platform rules (Apple HIG Layout, Designing for iPhone Duo; M3 Breakpoints; Android adaptive)
- **Layout responds to available space, never to device type, idiom, orientation or user agent.** Size classes / window size classes / container queries decide; `isTablet` and UA sniffing don't.
- **Functionality is identical at every size.** Only how much is visible changes (tab bar ↔ sidebar, overflow ↔ visible, 1 pane ↔ 2). Every action stays reachable at the narrowest width (visible or in the one overflow menu).
- **On resize, prefer small adjustments to rearrangement.** Controls keep their relative positions; selection, scroll, form input and open panes survive (Apple HIG iPhone Duo; Android canonical layouts).
- **Put controls next to the content they affect**, not all in a global bar (Apple HIG iPhone Duo).
- **Separate controls from content by layer, not slabs:** floating or sticky chrome with a scroll-edge fade or blur instead of an opaque bar plus divider; content and backgrounds extend under bars, interactive content is inset from system UI (Apple HIG Layout; Android edge-to-edge).
- **Every gesture has a visible control alternative**; hover-only affordances exist only behind `(hover: hover)` (ruling in `conflicts.md`).
- **Theme follows the OS by default.** If a theme switch exists, offer System (default) / Light / Dark. Never lock to light (Apple HIG Dark Mode; Android Themes; ruling in `conflicts.md`).
- **Brand lives in the content layer; chrome stays standard.** Accent on the primary action's *background*, the selected state, unread/new and status badges, not on every control or on static text. No brand-coloured solid nav bars, no logo on every screen, no branded splash. Brand treatment differs per platform; don't clone the website (Apple WWDC26-251; Apple HIG Branding, Color).
- **Standard actions keep platform icons** even when custom-drawn: share, search (magnifier), delete. NYT Cooking draws a different Share icon for iOS, Android and the web (Apple WWDC26-251).
- **Ergonomics set density** (Apple "Designing for…" primers): viewing distance iPhone ≤ 1–2ft, iPad ≤ ~3ft, Mac ~1–3ft, Watch ≤ 1ft, TV ~3m. Sessions: Watch < 1 min; Mac minutes to hours of deep work. Desktop web follows the macOS rules (shallow hierarchy, little modality, every command reachable from a menu or ⌘K with shortcuts shown); mobile web follows the iOS rules (few controls, primary actions low and central) [synth].

## 1. Apple: iOS, iPadOS, macOS, watchOS (HIG; WWDC25 356/219; WWDC26 250/251/292; Adopting Liquid Glass)

**Current state (Oct 2026):** iOS/iPadOS 27 and macOS 27 (UI kits Sept 2026); **Liquid Glass** (introduced WWDC25) is still the design language; WWDC26 added principles sessions, not a new visual style. SF Symbols 8 (7,000+ symbols, 9 weights, 3 scales); Icon Composer 2 (layered icons with light, dark, clear and tinted appearances). The HIG was redesigned in June 2026 and the **design principles are now a HIG page** (Apple Design "What's new"; Apple HIG Design principles). Apple says system colour values change per release: read them from the platform, don't hard-code "Apple hex values" (Apple HIG Color).

### Liquid Glass
- **A functional layer for controls and navigation only.** It floats above content (bars, tab bars, sidebars, floating controls). Never make content cards out of glass, and **never stack glass on glass**. For things placed on glass, use fills or vibrancy. "Limit these effects to the most important functional elements" (Adopting Liquid Glass).
- **Two variants, never mixed.** *Regular* (adaptive, frosted) is the default and the one for text-heavy floating UI. *Clear* is more transparent; use it only over rich media with bold content on top, with a ~35% black dim layer when the media is bright (Apple HIG Materials).
- Low-contrast text roles never sit on the thinnest materials; check contrast against the worst-case backdrop (Apple HIG Materials).
- **Let the system own backgrounds.** Remove custom backgrounds from bars, bar buttons, popovers and sheets; custom bars with content scrolling beneath them register a scroll edge effect. Group adjacent custom glass in one container; limit simultaneous effects for performance (Adopting Liquid Glass).
- **Tint selectively.** Only the primary action ("When every element is tinted, nothing stands out"). Exactly one tinted primary in a toolbar, on the trailing side (Apple HIG Buttons, Toolbars).
- **Custom colours need four values:** light, dark, increased-contrast light, increased-contrast dark (Adopting Liquid Glass; Apple HIG Color).
- **Concentricity.** Shapes are *fixed*, *capsule* (radius = ½ height) or *concentric* (inner = parent radius − padding). Use a fallback radius for components that can appear nested or standalone. Check content near the rounder sheet corners.
- **Scroll edge effects** replace hard dividers under floating UI. One per view; don't mix soft and hard styles.
- **Don't hard-code control metrics**; there's a new extra-large control size and system sizes change (Adopting Liquid Glass).
- **Toolbars:** group by what items affect; ≤ 3 groups; leading = back/sidebar/title (< 15 chars, never the app name); centre = common tools (collapse first); trailing = search, inspectors, More, primary. **Don't mix text and icon items that share a background.** Every icon has an accessibility label. **Hide whole items**, never leaving an empty glass pill. Top context-menu actions match the item's swipe actions (Apple HIG Toolbars; Adopting Liquid Glass).
- **Modality.** Interrupting task = sheet with a dimming layer; parallel task = no dimming. **Half sheets are inset; full-height sheets turn more opaque.** Action sheets, menus and popovers **spring from the control that invoked them**, and the rest of the UI stays interactive (Adopting Liquid Glass).
- **Lists and forms** have larger rows and padding; **section headers are title-style, not all caps** (Adopting Liquid Glass).
- **Pro and dense apps ("ProKit" discipline):** adapt glass with no refraction (it hurts legibility in dense UI), precise blur, solid outlines under Increase Contrast, variable blur at scroll edges (Linear iOS / Böhnke). A pro app may exceed the 5-item tab bar if it expands like iPad's tab bar → sidebar.
- Accessibility settings to honour: Reduce Transparency (frostier/solid), Increase Contrast (mostly black/white plus borders), Reduce Motion (no elastic effects). Web mirrors: `prefers-reduced-transparency`, `prefers-contrast`, `prefers-reduced-motion` (see `12 §5`).

### Typography and icons
- SF Pro with Dynamic Type text styles. Defaults/minimums: iOS 17/11pt, macOS 13/10pt, watchOS 16/12pt. Weights Regular–Bold for UI; avoid Ultralight, Thin and Light. No tight leading on 3+ lines (Apple HIG Typography).
- **SF tracking is built into the font and size-specific:** negative from roughly 13–23pt, positive from 24–76pt. It applies to SF only; **don't port the table to Inter, Geist or other fonts**, and don't claim "Apple uses negative tracking at large sizes" (Apple HIG Typography; ruling in `conflicts.md`).
- **Licensing:** don't ship SF fonts or SF Symbols in web apps. Use `system-ui` / `-apple-system` font stacks and an open icon set (ruling in `conflicts.md`).
- Custom brand fonts are fine for headings but **must support Dynamic Type** (wrap, don't truncate). System variants (Rounded, Compact, New York, width variants) give hierarchy on their own (Apple WWDC26-251).
- Alerts and onboarding text bolder and left-aligned (WWDC25).
- Icons: same SF Symbols across devices; outline in toolbars and lists, filled for selected states; text labels when no clear shorthand exists (Edit, Select); never restyle standard metaphors (Apple HIG Icons, SF Symbols).
- **Capitalisation:** native Apple UI uses title-style for buttons, menu items and section headers; never all caps. Web/SaaS default stays sentence case. Follow the project's existing convention first (ruling in `conflicts.md`).

### iOS
- Limit on-screen controls; make secondary actions discoverable "with minimal interaction". Easiest reach is the middle and bottom of the display. Support swipe-back and row swipe actions (each with a visible alternative) (Apple Designing for iOS).
- Navigation: tab bar for 3–5 top-level sections, holding navigation, never actions; never disable or hide a tab; single-word labels; per-tab state kept; badges only for critical items. The **search tab sits at the trailing end**. Navigation stack with back swipe. Sheets for focused tasks. Tab-bar accessory only for persistent features such as playback. Tab bar may minimise on scroll (Apple HIG Tab bars; Adopting Liquid Glass).
- Search placement: bottom toolbar preferred on iOS; the focused field slides above the keyboard (WWDC26-292; Adopting Liquid Glass).
- Use platform data (payments, biometrics, location) with permission instead of making people type it. Permissions only at the point of need, after a related action, with a specific reason; a pre-permission explainer has exactly one button ("Continue", never "Allow") (Apple HIG Privacy).
- Touch targets ≥ 44×44pt (28pt minimum); respect safe areas.
- Native Apple apps may disable Continue until required data is present (HIG); explain why it's disabled (ruling in `conflicts.md`).
- "Done" is the standard confirm in Apple-style sheets, paired with Cancel; Back moves between steps and never dismisses; never show all three (Apple HIG Sheets; ruling in `conflicts.md`).

### iPhone Duo (Apple HIG "Designing for iPhone Duo", page published 2026-09-09; device release date unverified)
- A dual-display, hinged iPhone: compact width on the outer display, regular width on the inner. Toolbars, tab bars and navigation can move to a **vertical bar on the side**.
- **Don't design per pose.** Build one resizable layout with size classes, margins and safe areas. Avoid fixed widths and display-specific dependencies. You may add one level of hierarchy on the larger display (list → list + detail).
- Keep functionality and element state identical across displays and poses; favour small adjustments over rearrangement.
- Grids spanning the fold: **even number of columns**; keep important elements clear of the fold.
- **Toolbar overflow:** items overflow bottom-to-top; assign visibility priority by group, then item; frequent actions and status-bearing items (badges) stay visible longest. Navigation-focused views overflow toolbar items and keep the tab bar; task-focused views minimise the tab bar and keep the toolbar.
- **Every toolbar item has a title and a symbol** (titles appear in overflow). **The ellipsis is reserved for overflow**; other menus get a distinct symbol; one overflow menu only.
- Vertical bar order: primary navigation (Back/Close) at the top, then prominent actions (Done). Vertical controls stay on the same physical side in RTL.

### iPadOS
- Use the large display to elevate content, "minimizing modal interfaces and full-screen transitions". Sidebar and tab bar are one navigation element that scales with the canvas (Apple Designing for iPadOS).
- **Support arbitrary window sizes** (fluid down to a minimum, no preset sizes), pointer, keyboard, Pencil, and multitasking (Adopting Liquid Glass).
- Search: trailing toolbar in split views; sidebar search filters the sidebar (WWDC26-292).
- Sidebars: ≤ 2 levels, visible by default, collapsible, critical items away from the bottom (Apple HIG Sidebars).

### macOS
- "Present more content in fewer nested levels and with less need for modality, while maintaining a comfortable information density." Resizable, hideable, movable windows and full screen (Apple Designing for macOS).
- **Command-complete:** every command lives in the menu bar, with its shortcut shown. Context menus may omit shortcut hints and show only the most relevant items, but every context-menu command must also be reachable in the main UI (Apple HIG Menus, Context menus; ruling in `conflicts.md`).
- Keyboard-first, high-precision pointer editing; support customisable toolbars; right-click context menus everywhere an object appears, the same menu each time.
- Sidebar plus toolbar layout; rounded-rectangle controls in dense inspectors, capsules only for standout actions. Hit targets default 28×28pt (minimum 20pt).
- **Don't put critical controls or information at a window's bottom edge** (people drag windows partly off-screen); avoid the camera housing (Apple HIG Layout).
- Windows: open a new window only to keep context (compose beside the message); offer "Open in new window" rather than doing it by default. Status bars hold only counts. Show focused vs unfocused panes differently (Apple HIG Windows).
- ⌘, opens Settings; reopen to the last pane; don't copy OS-level settings (Apple HIG Settings).
- Electron/desktop + web builds: make native-only chrome (back/forward, tabs) removable for the browser build, and lean on Apple standards for a native feel (Linear redesign).

### watchOS and tvOS (brief)
- **watchOS:** glanceable single-screen interactions, "a simple gesture or two"; minimise depth; complications and notifications often matter more than the app; ≤ 3 glyph buttons or 2 text buttons per row, text buttons usually full width; text up to 140% (Apple Designing for watchOS; HIG Layout, Accessibility).
- **tvOS:** safe area 60pt top/bottom, 80pt sides; grid gutters 40pt horizontal, ≥ 100pt vertical; equal peek on both sides; focus shown by scale and motion, never colour alone; targets 66pt (56pt min) (Apple HIG Layout, Accessibility).

### Principles (WWDC26 250; HIG Design principles page, 2026-06-08)
- **Purpose:** decide what not to build.
- **Agency:** undo for any action; interrupt only before a big mistake; guided flows easy to skip or escape; recovery never costs work.
- **Responsibility:** no permission prompts at launch; ask at the point of need with the reason. Guard AI features against wrong or unsafe output with previews and confirmations (see `17`).
- **Familiarity:** things that look the same behave the same.
- **Flexibility:** design for each device's strengths.
- **Simplicity ≠ minimal:** the most important item is the most obvious one.
- **Craft:** the tells of a rushed product are tap-and-wait, jittery scrolling, misaligned icons, and layouts that break on rotation. "Delayed load times or dropped frames translate poorly" (WWDC26-251).
- **Delight** "isn't by adding confetti"; don't mistake delight for decoration. It's the sum of the other principles.

## 2. Android: Material 3, M3 Expressive and adaptive layouts (m3.material.io; developer.android.com)
- **M3 Expressive (May 2025)** is an evolution *within* Material 3, not "M4": new and updated components, shape morphing, **spring-based motion**. Google's research (46 studies, 18,000+ participants) found expressive designs preferred and faster to scan, but cautioned: **one or two hero moments** per product, don't replace familiar patterns, calmer variants in serious contexts such as finance.
- **Colour roles:** `primary`/`on-primary`, `container`/`on-container`, `surface` tones; `outline` for interactive boundaries, `outline-variant` for decoration. Use container (muted) tones for most coloured surfaces; keep vibrant primary for the single most prominent action. Few semantic colours, one meaning each. Dynamic colour can come from the wallpaper (Android Colour).

### Adaptive layout (M3 Breakpoints; Android window size classes, canonical layouts)
- **Width breakpoints:** Compact < 600dp · Medium 600–839 · Expanded 840–1199 · Large 1200–1599 · Extra-large ≥ 1600. Height (edge cases only): compact < 480, medium 480–899, expanded ≥ 900; a landscape phone is medium width but compact height, so no two-pane there.
- **Margins** 16dp at compact, 24dp from medium up; **24dp spacer** between panes. Panes: compact 1; medium 1 (2 only for low-density content like settings, 50/50); expanded/large 2 recommended; XL up to 3; **never more than 3**. Fixed pane 360dp (expanded) / 412dp (large+); side sheet as third pane max 400dp.
- **Navigation by width:** navigation bar (3–5 destinations) < 600 → nav rail ≥ 600 → expanded rail at large+. `NavigationSuiteScaffold` uses a bar if width *or* height is compact. **No bottom navigation bar on large screens.**
- **Canonical layouts:** list-detail, feed, supporting pane. List-detail on resize: expanded → narrow keeps the **detail**; narrow list → expanded shows a **placeholder** detail; when only detail shows, Back returns to the list.
- **Moving up a breakpoint, decide what to reveal, divide, resize, reposition, swap.** "Additional space doesn't just mean making the same thing bigger." **Swap only functionally equivalent components** (nav bar → rail, full-screen dialog → basic dialog, bottom sheet → menu/side sheet); never a button → chip.
- **Never stretch buttons, inputs, forms or single-pane content full width**; cap with a max width and change presentation instead.
- **Pass all data a component could need at any size**; components decide layout from the width they're given (`BoxWithConstraints` ≈ container queries), not window metrics.
- **Don't lock orientation or aspect ratio** (letterboxing; Play lowers large-screen discoverability; Android 16 ignores the locks at sw ≥ 600dp).
- **Reachability:** on medium/landscape tablets and unfolded foldables the top 25% is likely out of reach; also avoid essential controls flush with the bottom edge.
- Grids: 8dp for layout, 4dp inside components; fonts in `sp`, everything else `dp`; 4 columns on phones, 8 on unfolded foldables.
- Quality tiers: Adaptive ready (full-window, basic keyboard/mouse/stylus) → optimized → differentiated (multitasking, postures, drag-and-drop, stylus). Test sizes: foldable 841×701, 8″ tablet 1024×640, 10.5″ 1280×800, Chromebook 1600×900; frame designs at 412dp and test at 360dp.

### Edge-to-edge and system bars (Android edge-to-edge)
- **Enforced on Android 15**; call `enableEdgeToEdge()` for older versions. Backgrounds and dividers draw edge-to-edge; text and buttons are inset.
- Three insets: **system bars** (tappable UI avoids them), **system gestures** (no tap or drag targets there; OS gestures win), **display cutout** (inset critical UI; solid app-bar backgrounds may draw into it).
- Transparent status bar when nothing scrolls under it; translucent protection when content does. One protection per pane; don't stack two. With gesture nav keep the bottom transparent; with three-button nav add a scrim when the bottom bar animates away.

### Predictive back (Android Predictive back)
- People preview the back destination before committing; cancelling is fully reversible.
- Full-screen: exit scale 100% → 90%, enter 110% → 100%, cross-fade threshold at **35%** progress; commit interpolator `(0.1, 0.1, 0, 1)`.
- Map gesture progress through a decelerate curve (`PathInterpolator(0, 0, 0, 1)`), not raw linear. Fling: absorb velocity, then commit. Release before threshold: return swiftly and undo any state change.
- Don't suggest that completing back dismisses an item in the gesture's direction.
- Web drag-to-dismiss sheets follow the same contract [synth] (see `05`).

### Porting checklist: iOS ↔ Android (Android "Translate iOS designs")
Keep content parity; swap idioms. Brand comes through colour, type and shape.
- [ ] Tab bar → navigation bar (≤ 5); profile/settings to the top app bar; consider a FAB for the one primary action.
- [ ] Navbar → top app bar, **title left-aligned**; nav icon left, actions right; large titles → large flexible app bar that collapses on scroll.
- [ ] **Up ≠ Back:** up moves up the hierarchy; system Back goes back in history and can leave the app.
- [ ] Full-screen modals close with **×**; text Cancel/Done → icons.
- [ ] Sheets → full-screen dialog or bottom sheet; action/activity sheets → bottom sheets; alerts → dialogs; **segmented controls → tabs**.
- [ ] Lists: sparse dividers, **no disclosure chevrons**, 8dp grid.
- [ ] SF → Roboto (or brand font); SF Symbols → Material Symbols, one style; ripple feedback (only in Material-styled apps); container transform / shared axis / fade-through motion.
- [ ] Neither platform slides laterally between top-level destinations; tabs don't slide.
- [ ] Targets 48dp; text in sp; body ≥ 12sp.
- [ ] Reverse direction (Android → iOS): back chevron with title, title-style section headers, swipe-back, sheets with Cancel/Done.

### Android quality, onboarding and accessibility
- No payment prompt right after launch; deep links land on the exact content; support the system share sheet, backup/restore of sign-in and settings, PiP for video (Android Quality: UX).
- Show value before asking for permissions or an account; permission priming at the moment of need; persistent Skip / Log in; no decorative progress illustrations; never pre-fill passwords; don't stretch inputs on expanded screens (Android Onboarding).
- Targets 48dp; links have more than one affordance; every gesture has a visible equivalent; consider haptics as a second channel (Android a11y).
- **Hover, focus and pressed state layers belong to actionable items, never to whole containers** (toolbars, dialogs, sheets, nav containers); one hovered/focused/pressed element at a time (M3 States; ruling in `conflicts.md`).
- Remote/D-pad (TV): instant, distinct focus feedback; text and targets for ~3m viewing; treat personal info carefully on a communal screen (Android TV).

## 3. Web apps and SaaS
- Use a **left sidebar** for many sections, a top bar for search, account and context, and breadcrumbs for deep objects (NN/g menus). Page-shell breakpoints, if you need them: 600 / 840 / 1200 / 1600px (M3; see `11 §4`).
- **Learnability and efficiency together.**
  - Defaults and empty states teach newcomers.
  - Shortcuts, the ⌘K palette and bulk actions serve experts (NN/g complex apps; Superhuman). Show shortcuts in app menus and the palette (ruling in `conflicts.md`).
- **Settings:**
  - Prefer detection and good defaults to settings; keep settings few.
  - Options for a task (sort, filter, density, columns) live on the screen they affect, not in Settings.
  - Don't copy OS-level preferences: follow `prefers-color-scheme` / `prefers-reduced-motion`, with "System" as the default theme choice.
  - ⌘/Ctrl+, opens Settings; reopen to the last section; each section has its own URL (Apple HIG Settings).
  - Group by user goal, not by internal system; left sub-navigation for many sections; 15+ items → subscreens (Android Settings).
  - Pick one save model per page: autosave with a status indicator, or an explicit "Save changes" with an unsaved-changes guard. Show a dirty indicator only when autosave is off (Apple HIG File management).
  - Put destructive settings in a separated "Danger zone" [synth; widespread convention].
- **Accounts:** let people use the core product before signing in where possible; ask at the moment an account is needed (for example at purchase), explaining the benefit; guest checkout then "create account" after. Prefer passkeys. Identity-provider buttons get equal size and prominence. **Account deletion** (not just deactivation) is self-serve from Settings, as easy as sign-up, with a completion date and a notification when done; explain billing consequences (Apple HIG Managing accounts; Apple SIWA HIG).
- **Notifications:** map every type to a tier: passive (digest), active (default), time-sensitive (needs action within ~1h), critical (safety). Never use a higher tier than the content deserves. Marketing needs explicit opt-in, never the urgent tier, and every type is adjustable in-app (Apple HIG Managing notifications). No self-notifications for your own actions; send email digests only for items still unread (Linear docs).
- **Roles and permissions:** explain why something is unavailable and who can grant access.
- The URL reflects state, so links can be shared (Vercel). URLs survive moves and renames by redirecting (Linear docs).

## 4. Enterprise and complex applications (NN/g, Kaplan; Apple macOS; Linear) [partly synth]
- **Density is expected**, but salience comes from removing noise, not adding emphasis.
- **Staged disclosure** and flexible pathways. Non-linear wizards with back, skip and save-as-draft.
- **Accelerators:** keyboard shortcuts, saved views, bulk editing, templates.
- **Long sessions:** autosave, recoverable state, audit trails, notes and annotations, export.
- Hover or side-panel detail instead of navigating away. Tables are the workhorse (see `06 §5`).
- **Constrained customisation** beats infinite options: fixed, ordered status categories with renameable statuses; a fixed small priority set; reserved names. Keep lenses (views, display options) separate from data (filters) (Linear docs).

## 5. E-commerce and checkout (Baymard Institute, "Checkout UX 2025")
- Make **guest checkout** the most prominent option. Don't put an account wall before purchase.
- **Show delivery dates, not speeds** ("Arrives Thu, Oct 23", not "3–5 business days"). Show cutoff countdowns in the user's time zone.
- Show all fulfilment options (shipping, pickup) at the shipping step.
- Quantity: +/- buttons plus a field that selects its content on focus.
- **Mark both required and optional fields** (Baymard found many people miss required fields). Hide rarely-used fields (Address line 2, company) behind a link.
- Use a checkbox for binary choices, not a dropdown.
- **Adaptive, specific errors** for each sub-rule. Explain why a phone number is needed.
- Password rules: a reasonable minimum (Baymard suggests 6–8 characters) instead of complex rule checklists.
- Show trust signals and total cost (tax, shipping) before the final step.

## 6. Marketing sites and landing pages [synth from the hierarchy, typography and honesty sources]
- One message per section and **one primary CTA** repeated consistently. The headline says what the product does for whom, in plain words.
- Expressive typography and imagery are welcome here, but performance (LCP, CLS) and contrast still apply. Real product screenshots beat abstract gradients.
- **Honesty:** no fake logos, invented metrics or testimonials (Rams #6). Use real numbers with sources, or none.
- Motion: scroll-triggered reveals only if subtle and reduced-motion-safe. No scroll-jacking. Heroes use `min-height: 100svh`, not `100vh` (see `18`).

## 7. When to break a convention (NN/g, Budiu "Power Law of Learning")
Break it only if all of these hold:
1. The new pattern is **substantially** better once learned.
2. People use the product often enough to learn it.
3. You can help them learn quickly, through progressive hints and repetition rather than tutorials.

Linear's keyboard-first model passed this test because its audience lives in the keyboard. Linear's custom iOS glass took "the harder path" only because Apple's stock tab bar couldn't change shape or behaviour (Linear iOS / Böhnke).

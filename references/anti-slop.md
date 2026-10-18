# Anti-slop: what AI-generated interfaces get wrong

Each row names something to **never** ship, why it fails, and what to do **instead**. Avoid all of these unless the user explicitly asks for them. Sources are short-names from `sources.md`; **[synth]** marks a synthesis across sources; **[unverified]** marks patterns seen only in community extractions (awesome-design-md).

Use this file as the Never-ship self-check before reporting work (Emil's "Never | Instead" pattern), and in Review mode cite the row you are applying.

## Visual

| Never | Why | Instead |
|---|---|---|
| Purple/blue gradient hero, gradient text, glow, "AI sparkle" decoration | Decoration without function; dates fast (Rams #5/#7/#10) | Neutral chrome, a real product screenshot, one accent. Gradients only as an established brand asset or one consistent AI-state signal (conflicts #6, `17-ai-interfaces.md`) |
| Sparkle icon on every AI-ish button with no verb; ambient animated gradients tied to no AI state | A bare sparkle says "AI" but not what will happen; overuse erodes it (Pozos & Schmidt; Google Gemini design) | One consistent AI marker plus a verb label ("Summarise"); motion only for listening/thinking/generating, with start, end and a reduced-motion fallback |
| Glassmorphism on content cards, list rows or hero panels; glass on glass; glass on every control | Muddies hierarchy; Apple reserves glass for the functional navigation layer (Apple HIG Materials, Adopting Liquid Glass) | Solid surfaces for content; translucency only on floating nav, toolbars, sheets, with an opaque fallback for `prefers-reduced-transparency` |
| Clear glass over bright imagery with no dim layer; tertiary text on the thinnest material | Text becomes illegible (Apple HIG Materials) | Frosted variant for text-heavy UI; ~35% black dim layer over bright media; check contrast on the worst-case backdrop |
| Glass refraction in dense data UI | Hurts legibility (Böhnke, Linear) | Blur, mask and light without refraction; solid outlines under `prefers-contrast: more` |
| Opaque slab plus 1px divider under every sticky header | Heavy; a hard line where none is needed (Apple HIG Layout; Apple via Emil) | Scroll-edge fade or blur that appears only when content is underneath |
| Everything in a bordered card; card inside card | Common-region overuse; noise (Refactoring UI, NN/g) | Group with spacing and background shifts; containers sparingly |
| Separators and borders everywhere | They "quietly proliferated… without clear reason" (Linear 2026 refresh) | Space and alignment first; remove or soften the rest |
| Shadows on everything; one heavy `0 4px 6px rgba(0,0,0,.1)` halo; > 3 elevation levels at rest | No light model; desaturates colour (Comeau, M3 Elevation) | 2–3 layered, tinted elevation tokens; tone before shadow; lowest elevation that reads |
| Border + shadow + background shift on the same element | Triple separation reads heavy (Refactoring UI) | Pick one, two at most |
| Random radii; non-concentric nested corners; same radius on parent and child | Looks pinched or flared (Apple, Vercel, M3 Shape) | Small radius set; inner = outer − padding |
| Pill or `rounded-3xl` radii on dense data cards; a pill CTA mixed with 6px buttons on one screen | Wastes space; no shape grammar (M3 Shape; awesome-design-md patterns [unverified]) | Small/medium radius on dense containers; one CTA radius grammar per screen |
| Magic-number spacing (13, 22, 28px), random hex | Nothing must be arbitrary (Rams #8, Curtis) | Tokens only |
| Brand tint bleeding into every grey; brand colour on every icon, control and static text | Chrome competes with content; colour loses meaning (Linear, Apple HIG Color/Branding) | Low-chroma neutrals; accent on the primary action's background, selection and status only |
| Brand-coloured solid nav and tab bars; logo in header, sidebar and footer; branded splash screen | Letterboxes content; feels slow (Apple WWDC26-251, HIG Branding, HIG Launching) | Standard chrome, colour in the content layer, logo once (may fade on scroll); first paint = first screen |
| Bright, equal-weight sidebar and nav | Competes for attention it hasn't earned (Linear 2026 refresh) | Dim nav, mute inactive items, smaller icons |
| Decorative icon on every row; coloured icon chips | Noise; icons are for recognition (Linear 2026 refresh) | Fewer, smaller, monochrome icons |
| HSL/`darken()` palettes; neon or muddy shades | Inconsistent contrast across hues (Stripe, Evil Martians) | Perceptual OKLCH ramps with a shared lightness curve |
| Too many semantic colours; the same status in different colours on different screens | Meaning becomes unlearnable (Android Colour) | Few semantic colours, one meaning each, app-wide |
| Light grey text failing 4.5:1; grey text on colour | Unreadable; WCAG failure | Text tokens checked for contrast; same-hue tints on colour |
| Grey-on-black dark-mode body text; contrast checked only in light mode | Fails low-vision users (Apple Sufficient Contrast criteria) | Check dark and increased-contrast modes separately; aim 7:1 for custom dark pairs |
| Apple system blue/green/orange copied as small text on white | 3.5:1 / 2.2:1 / 2.3:1 [computed]; Apple's values also change per release (Apple HIG Color) | Use bright hues for fills and large text, darker or increased-contrast steps for text; never hard-code Apple's values |
| Checkbox or toggle states that differ only by a faint tint; red/green dots with no shape or label difference | State unreadable; fails colour-blind users (Apple Sufficient Contrast and Differentiate Without Color criteria) | ≥ 3:1 between states; add shape, icon or label; pass the grayscale test |
| Thin (100–300) weights for UI text; oversized h1 (2×+ body) | Legibility loss; hierarchy shouting (Apple, Butterick) | ≥ 400 for UI text; modest heading steps; weight before size |
| Centred multi-line body text and headings everywhere | No reading edge (Butterick, Mailchimp) | Left-aligned text; centre only short, deliberate elements |
| Edge-to-edge text lines > 75 characters; single-column content stretched across 1400px | Exhausting to read (Butterick, M3) | ~66ch measure (45–75; 40–60 on narrow columns) |
| Tight leading on 3+ lines; fixed `height` on text containers | Clips diacritics and tall scripts (Apple HIG Typography, M3 language height) | Paragraph line-height 1.4–1.6; unitless line-height plus padding |
| Mixed Title Case and sentence case within one element type; ALL-CAPS headings or section headers; untracked caps | Inconsistent, slower reading (Apple HIG Writing, Adopting Liquid Glass, Butterick) | One case style per element type: sentence case on the web, HIG title case on native Apple UI (conflicts #1); caps only for short tracked labels |
| Font salad (> 2 families) or Arial/Times by default | No typographic intent | One quality UI family (+ an optional display cut) |
| Porting SF Pro's tracking table onto Inter or Geist; shipping SF Pro or SF Symbols in a web app | The table matches SF's optical sizes only; the fonts are licensed for Apple platforms (Apple HIG Typography) | Follow the font foundry's guidance; use the project's icon library |
| Proportional digits in tables and counters | Numbers jitter and misalign (MDN, Inter) | `tabular-nums` |
| Emoji as icons or bullets; mixed icon sets; upscaled tiny icons; geometrically centred play/download glyphs | Inconsistent weight and metaphor; looks off (Apple HIG Icons, Refactoring UI) | One icon family at drawn sizes; optical centring baked into the asset |
| A novel glyph for a standard action (search, share, delete) | People don't recognise it (Apple WWDC26-251, 292) | The platform's standard metaphor, even in a custom set |
| Multiple competing primary buttons; 3+ accent-filled buttons; buttons of different sizes in one choice set | Nothing stands out (Von Restorff, Apple HIG Buttons, Few) | One primary per view; prefer by style, not size |
| Fake metrics, testimonials, logos; lorem ipsum shipped | Dishonest (Rams #6); erodes trust | Real data or a designed empty/partial state |
| Decorative icons and illustrations on KPI cards | Slows visual search (NN/g Kaplan, Few) | Numbers with context; neutral styling |
| Labels that repeat self-explanatory media (a title repeated under its cover) | Redundant noise (Apple 227) | Remove the duplicate; keep the accessible name |

## Layout and responsive

| Never | Why | Instead |
|---|---|---|
| `isMobile` / user-agent layout logic; layouts that branch on device or orientation | Breaks on resize, foldables and split screens (Apple HIG Layout, Android adaptive) | Branch on container or viewport width |
| Features hidden or removed at small widths | Functionality must be identical at every size (Apple HIG iPhone Duo, Layout) | Move actions to overflow; every action stays reachable |
| Layouts that lose selection, scroll or input on resize | Resize is a state change (Android canonical layouts) | Preserve state across breakpoints |
| Full-width buttons and inputs on desktop or tablet | Forms become hard to scan (Android adaptive) | Cap width; change presentation instead |
| Bottom tab bar kept on wide screens | Wastes space; wrong idiom (M3, Android) | Rail or sidebar ≥ 600px |
| Nested scroll containers on the same axis; carousels with no peek | Unpredictable scrolling; hidden content (Apple HIG Scroll views) | One scroller per axis; show partial content at edges |

## Interaction and behaviour

| Never | Why | Instead |
|---|---|---|
| One-shot generated layout with invented features (polls, galleries, leaderboards nobody asked for) and arbitrary navigation | Anchors on an arbitrary structure; feature creep (Apple 227) | Specify features and mood; explore 2–3 named directions; remix |
| Generated screen that looks finished but ignores edge cases | "The form is there. The fit is not." (Saarinen) | List forces and misfits; stress-test with worst-case data |
| UI designed only against tidy demo data ("Jane Doe, 12 members") | Ships "1 members", squished avatars, wrapped badges, raw `NaN` (Emil break-ui) | Worst-case fixture at the data boundary; `Intl.PluralRules`/`NumberFormat` |
| Unbounded lists (members, leaderboards, history) with no "you are #N" summary | The person's own item gets buried (Apple 227) | Show their position plus "Show all" |
| Animations on high-frequency or keyboard actions (command palette, shortcuts, list navigation, tab switches) | Feels slow after the 10th time (Emil, Rauno, Apple) | No animation; instant. Tabs never slide |
| Floaty 400–600ms animations on routine UI; `ease-in`; built-in `ease-out` on deliberate motion; hand-invented "familiar" beziers | Sluggish, generic (Emil, NN/g, Vercel) | Durations per conflicts #4; Emil's published curves |
| `transition: all`; animating `box-shadow`, `height`, `padding`, `margin`, `left`; `will-change` everywhere; per-frame `setState` | Jank; layout and paint thrash (Emil animation-performance, Vercel) | `transform`/`opacity`/clip-path; animate `filter: drop-shadow()`; write styles via refs; `will-change` only after measuring |
| `scale(0)` pop-ins; pure fades with no transform; centre-origin dropdowns | Unnatural (Emil) | `scale(.95)` + fade from the trigger origin; modals stay centred |
| `@keyframes` on toasts and toggles; non-interruptible animation | Restarts on interrupt; blocks input (Emil, Apple, Rauno) | CSS transitions or springs that retarget |
| Everything entering at once, or stagger > 80ms per item that blocks interaction | Noise or waiting (Emil) | 30–80ms decorative stagger that never blocks input |
| Exit via a different edge than entry; same speed for press and hold | Breaks spatial model (Emil, Apple HIG Motion) | Exit along the entry path; slow where the user decides, fast where the system responds |
| Ignoring `prefers-reduced-motion`; parallax; scroll-jacking; autoplay or auto-advancing carousels; animated blur | Vestibular harm, loss of control (web.dev, WCAG, Apple Reduced Motion criteria) | Remove decorative motion; pause controls |
| "Reduced motion" implemented by deleting all transitions and feedback; blur or slide transitions left on under reduced motion | Either loses meaning or still moves (Apple Reduced Motion criteria, Emil) | Replace meaningful motion with fade, dissolve or colour change (conflicts #5) |
| A haptic or sound on every interaction | Becomes noise (Apple via Emil, Emil animate-expo) | Once per meaningful action, same frame as the visual, never the only feedback |
| Spinner on a blank page; spinners flashing for 50ms | Users "watch the clock" (Hurff); flicker (Vercel) | Layout-matching skeletons; show-delay + minimum visible time |
| Progress bar that races to 90% then stalls; spinner morphing into a bar; "Loading…" on long tasks; no Cancel | Feels deceptive or frozen (Apple HIG Progress indicators) | Honest determinate progress, a specific label ("Importing 3 of 12 files…"), Cancel |
| Logo splash screen; launch screen that doesn't match the first screen | Feels slow; flashes (Apple HIG Launching) | First paint = first screen |
| Only the happy path; "Nothing here" empty states; crucial info only in an empty state | Dead ends; info vanishes once content exists (Hurff, Apple HIG Writing) | Five states; empty states with a next action |
| Infinite scroll or background loads that reset focus or reading position | Strands screen-reader and keyboard users (Apple VoiceOver criteria) | Preserve focus and position; announce politely |
| Placeholder-only labels; float labels | Labels vanish; contrast fails (Silver) | Persistent label above the input |
| Submit disabled until valid; `pointer-events: none` on disabled controls; disabled with no reason | No explanation; kills the reason tooltip (Silver, Vercel, Figma) | Enabled submit then clear errors; if disabled, explain why nearby (conflicts #3) |
| A disabled FAB or floating primary left on screen | Looks broken (M3 States) | Hide it until available |
| Validation on focus or first keystroke | Premature errors (Wroblewski, Baymard, NN/g) | On submit, then on blur/live once a field has errored (conflicts #3) |
| "Something went wrong", "Invalid input", "Oops!", "We're having trouble…", "Error 329347" | No fix offered; "we" centres the product (GOV.UK, NN/g, Apple HIG Writing/Alerts) | What happened + how to fix: "Couldn't save changes. Check your connection and try again." |
| Clearing input after an error; a popover or drawer that drops typed input on outside click | Destroys work (Hurff, GOV.UK, Apple HIG Popovers) | Preserve every value; save on auto-close; discard only on Cancel |
| "Are you sure?" on every delete; alerts for routine, undoable actions | Habituation makes it useless (Raskin, Apple HIG Alerts) | Act + Undo; confirm only irreversible, unexpected or high-cost actions |
| Enter/Return bound to a red destructive button; destructive button styled as primary default; Cancel as default | People hit the prominent button without reading (Apple HIG Buttons/Alerts, APG) | Focus the least destructive option; destructive styled but never default (conflicts #10) |
| Modal, alert or permission prompt on first load | Interruption without cause (Apple HIG Alerts, Onboarding, WWDC26) | Inline status; ask at the point of need with the reason |
| Modal from a modal; popover cascades; two alerts at once | People lose their place (Apple HIG Modality, Popovers) | One layer at a time (`assets/overlay-chooser.md`) |
| A warning shown in a popover or tooltip | Too easy to miss (Apple HIG Popovers) | Inline status or alert, by severity |
| Hover-only menus and row actions; ungated `:hover` that sticks on touch; hover styles on whole containers | Excludes touch and keyboard; noisy (NN/g, WCAG 2.5.7, M3 States, Emil mobile-native) | Click-activated; visible actions; hover on items only, behind `(hover: hover) and (pointer: fine)` |
| Swipe-only, drag-only or pinch-only actions | Excludes many users (WCAG 2.5.7, Apple HIG Accessibility, Android) | A visible button or menu alternative for every gesture |
| Toasts or banners that auto-dismiss before they can be read or acted on | Lost information (Apple HIG Accessibility) | Explicit dismissal for actionable toasts; pause on hover/focus |
| Submenus that close on diagonal mouse travel | Forces an L-shaped path (Eldh, Linear) | Safe-area triangle |
| Hand-rolled `<div>` dropdown, dialog or toast | No focus management (Emil pick-ui-library, APG) | Maintained accessible primitive (Radix, Base UI, React Aria; Sonner) |
| `div onClick` buttons and links; `outline: none` | Not keyboard accessible (APG, Vercel) | Native `<button>`/`<a>`; visible `:focus-visible` |
| `user-scalable=no`, `maximum-scale=1`; inputs under 16px on iOS; grey tap flash; `100vh` app shells; `user-select: none` on body | Blocks zoom; iOS zooms inputs; shells jump under browser chrome (Emil mobile-native) | Mobile web baseline (`18-mobile-web-and-touch.md`); `dvh`/`svh` |
| `user-select: none` on error text, IDs or addresses | People can't copy what they need (Apple HIG Labels) | Leave text selectable; disable only on control labels |
| Hamburger menu on desktop; novel navigation | Hidden nav loses usage (Wroblewski, NN/g) | Visible primary nav; conventions |
| Tab bars with disabled, hidden or unlabelled tabs; actions in a tab bar; red badges for non-critical counts | Unstable navigation (Apple HIG Tab bars) | Always-present labelled tabs with explained empty states |
| ARIA `role="menu"` on site navigation | Wrong semantics (Pickering) | `<nav>` + list of links |
| Icon-only toolbars with no labels, titles or tooltips; toolbar icons in outlined circles; a text button touching an icon button; 4+ toolbar groups | Mystery meat; noise (Budiu, Google research, Apple HIG Toolbars) | Every item has a title (accessible name, tooltip, overflow label); borderless icons; ≤ 3 spaced groups |
| Ellipsis on non-overflow menus; two competing overflow menus; header actions that move between screens | Breaks learned positions (Apple HIG iPhone Duo, Linear 2026) | One ellipsis overflow; recurring actions in identical positions |
| Menu group where some items have icons and others don't; submenus 2+ levels deep; kebab menus hiding primary actions; dropdowns with 1–2 items | Inconsistent, undiscoverable (Apple HIG Menus, Pull-down buttons) | All icons or none per group; 1 submenu level; primary actions visible; plain buttons under 3 items |
| Context menus that are the only path to a command, or appear on an object in some places but not others | Undiscoverable (Apple HIG Context menus) | Every command also in visible UI; same menu everywhere |
| Segmented controls mixing icons and text, unequal widths, or 6+ segments on mobile | Hard to scan (Apple HIG Segmented controls) | ≤ 5 segments on mobile, equal widths, all text or all icons |
| Switches for form fields that need Submit; switches whose state shows only through colour | Wrong control; fails colour-blind users (Apple HIG Toggles) | Checkbox for submitted forms; visible on/off shape |
| Coach-mark tours, multi-slide onboarding that returns after being skipped, setup wizards before first use | People skip them; tutorials don't teach (NN/g, Hurff, Apple HIG Onboarding) | Contextual tips at the point of need; never re-show once skipped |
| Rating or NPS prompt on first visit or mid-task | Invites negative ratings (Apple HIG Ratings) | After a success moment, rate-limited |
| Pre-permission modal with "Allow" or two buttons; vague purpose strings ("for a better experience") | Imitates the system; no real reason (Apple HIG Privacy) | One "Continue" button; one specific, active sentence of purpose |
| Sign-in wall before value; account before checkout; one identity provider's button smaller than the others; account deletion only via support | Abandonment; unfair; hostile (Apple Sign in with Apple HIG, HIG Managing accounts) | Explore and buy as a guest first; equal provider buttons; self-serve deletion |
| Hidden or ambiguous search: unclear scope, endless suggestions, filters only as tokens, a blank no-results pane | People can't tell what or whether they searched (Apple WWDC26-292) | Scoped placeholder, capped suggestions, visible filters, no-results view that echoes the query |
| Command palette with exact-match search, no shortcuts shown | Unforgiving, doesn't teach (Superhuman) | Fuzzy + aliases + shortcut hints |
| Filters and display options mixed in one control; filter state lost on reload or share; state not in the URL | Refresh, back and share break (Linear docs, Vercel) | Filters change the set, display options change the view; main state in the URL |
| Unlimited custom priorities and statuses | "Easy to get carried away with specificity" (Linear docs) | Small fixed sets, renamable within fixed categories |
| Notifying people of their own actions; email for items already read; marketing on the urgent tier | Noise (Linear docs, Apple HIG Managing notifications) | Suppress self-notifications; digest only unread; tier by real urgency |
| "Unsaved •" indicator when the app autosaves | Contradicts the save model (Apple HIG File management) | Show a dirty state only when autosave is off |
| Settings pages full of toggles the app could detect; sort and filter options buried in Settings | Burden on the user (Apple HIG Settings, Android Settings) | Good defaults; task options on the screen they affect |
| Charts that need hover to reveal the key number; odd tick steps (1, 6, 11); stacked colours with no separators | Hides the takeaway (Apple HIG Charts) | Headline states the takeaway; familiar ticks; 1–2px separators |
| Decorative progress (an illustration change per step) instead of a real stepper | Doesn't show position (Android onboarding) | "Step 2 of 4" stepper |
| iOS idioms in Android builds (row chevrons, centred titles, "Cancel/Done" text in the bar) | Feels foreign (Android translate-designs) | Platform-native equivalents (`13-platforms.md`) |
| Flipping every icon in RTL, including checkmarks, logos and clocks; reversing digits | Wrong meaning (Apple HIG Right to left) | Mirror only directional icons, navigation and progress |
| A brand's DESIGN.md, palette or "look" (Linear, Stripe, Apple) copied wholesale as your product's identity | Imitation, not quality (Linear brand; awesome-design-md is unverified) [synth] | Reproduce decisions, not surfaces (SKILL §4) |
| Alias chains in tokens; every primitive exposed to consumers | Hard to maintain (Figma token architecture) | Semantic → primitive only; keep primitives private |

## Copy

| Never | Why | Instead |
|---|---|---|
| "Supercharge your workflow", "Seamless", "Unlock" | Says nothing | Say what it does, plainly |
| "Submit", "OK", "Yes/No", "Click here", "Learn more" alone; "Let's do it!" | Unclear outcome (Silver, Apple HIG Writing/Alerts) | Outcome verbs; descriptive links. "OK" only for a purely informational alert; "Done" only in Apple-style sheets paired with Cancel (conflicts #9) |
| "Success" as a confirmation | Names no outcome (Figma button states) | "Saved", "Sent" |
| "Please…", "We recommend…", "We couldn't…", "Error: …" in UI | Wordy, product-centred (Apple Style Guide, HIG Writing) | Direct, reader-centred copy (conflicts #2) |
| "Enable/Disable", "Click on", "Tap on", "e.g.", "i.e.", "etc.", "...", "Oops!!" | Off-voice, imprecise (Apple Style Guide) | Turn on/off; click; tap; full words; `…` |
| master/slave, whitelist/blacklist, kill, sanity check, dummy | Non-inclusive (Apple Style Guide) | main, allow list/deny list, stop, check, placeholder |
| Clever or branded feature names that need explaining; labels that judge the user at zero ("Spending Power: 0") | Sets the wrong expectation (Apple WWDC26-290) | Plain, industry-standard terms in trust contexts; the sentence test |
| Settings labelled "Manage…", "Change…", "Select…"; screens called "Options" or "Preferences" | Generic verbs carry no meaning (Android Settings) | Label = the thing ("Notifications"); supporting text shows current status |
| `aria-label="Delete button"`; repeated "Delete" with no object | Role is announced twice; ambiguous (Apple VoiceOver criteria) | "Delete Blue T-shirt from cart"; role and state come from semantics |
| Emoji and exclamation marks in UI copy; idioms and humour in core UI or errors | Grates on repetition; doesn't translate (Apple HIG Inclusion) | Calm, specific language |
| "Your Dashboard / Your Projects" everywhere; mixing "my" and "your" | Possessive clutter (Apple HIG Writing) | "Projects"; possessives sparingly |
| Inconsistent names for the same thing | Users think they're different things | One term per concept |
| Directional copy ("in the right panel") | Breaks on resize and for screen readers | Name the control |
| "Loading…", "Authenticating…" on long tasks | Vague (Apple HIG Progress indicators) | Name the task and progress |

## Process

| Never | Why | Instead |
|---|---|---|
| Building the literal request instead of the underlying problem | Solves the wrong thing (Singer) | Frame the need first |
| Polishing before validating the premise | Wasted craft (Soleio, Covert) | Structure, then surface |
| Mushy compromise designs; rationale without rejected alternatives | No decision was made (Soleio, NN/g) | Record options rejected and why |
| Three "variants" that differ only in accent colour, named Option A/B/C; pre-picking a favourite | Not real exploration (Emil prototype, Apple 227) | 2–3 directions on named axes, named for their direction |
| Delegating critical thinking to the tool; anchoring on the first output | Arbitrary result (Apple 227) | Go wide, remix, repeat |
| Restyling one screen in isolation in an inconsistent product | Grows design debt (Saarinen, *A design reset*) | Flag system-level debt; fix tokens, chrome, headers |
| Fake personas with stock photos and demographics; fixtures of one demographic | Stereotypes, not insight (Indi Young, Apple HIG Inclusion) | Behaviour-based personas; diverse fixtures |
| Vanity metrics (page views) presented as UX success | Doesn't measure experience (Rodden et al.) | HEART-style goals, signals, metrics |
| Claiming checks you didn't run; reporting motion feel from code alone | Dishonest (Emil) | Mark verified vs inferred; list what needs a device |

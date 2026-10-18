# 06 · Core interaction patterns

Forms, validation, buttons and their states, selects and controls, dialogs and overlays, menus, notifications, tables and views, navigation, search, settings, sign-in.

Capitalisation in examples follows the web default (sentence case). On native Apple platforms use HIG title case for buttons, menus and section headers; follow the project's existing convention first.

## 1. Forms (Adam Silver, GOV.UK Design System, Luke Wroblewski, Baymard)

### Structure
- **One column.** Multi-column forms cause skipped fields and break reading order (Silver). Exception: a tightly related pair (first/last name, city/postcode) may share a row on wide layouts if it reflows to one column (Android Onboarding).
- **Cap form width** on wide windows (`max-inline-size`); never stretch inputs or buttons across an expanded screen (Android Onboarding). Avoid one input per screen *and* one endless scroll; break long flows into a few steps, each showing "Step 2 of 4" (Android Onboarding, Figma UI principles).
- **Every input has a visible `<label>` above it.** Hint text sits between the label and the input, linked with `aria-describedby`. **Never use the placeholder as the label**: it disappears, often fails contrast, and looks pre-filled. Avoid float labels too, since they shrink the label and collide with autofill (Silver).
- **Width reflects expected length** (postcode short, street long). Inputs **≥ 44px tall** (Silver).
- **Optional vs required:** Silver marks only optional fields with "(optional)", and better still asks fewer questions or uses a yes/no with conditional reveal. Baymard's checkout data (people missing required fields) supports marking *both* in long checkout forms. Pick one convention per product and apply it consistently. Don't put a red asterisk on every field with a legend.
- **Use the right `type`, `inputmode` and `autocomplete`** (`email`, `tel`, `one-time-code`, `street-address`) so autofill and mobile keyboards work [synth; widely documented web practice, consistent with WCAG 1.3.5].
- **Be forgiving** (GOV.UK, NN/g Slips, Silver):
  - Trim whitespace.
  - Accept spaces, dashes and brackets in phone and card numbers.
  - Accept apostrophes and diacritics in names.
  - Don't use `maxlength`, which silently truncates pastes; show a character count or an error instead.
  - Don't split inputs, except day/month/year for memorable dates.
- **Don't block paste** anywhere, especially in passwords and auth (WCAG 3.3.8).
- **Don't ask for what the system can give** (location, contacts, calendar, with permission); prefer a choice (picker, menu) to free text. **Never prefill a password field** (Apple HIG Entering data, Android Onboarding).

### Buttons in forms
- **Keep submit enabled (web default).** A disabled submit gives no reason why. Let people submit and then show errors (Silver, Vercel). Exception debated by Hurff: an empty chat "Send" can be disabled because the reason is self-evident.
- **Native Apple apps** may follow HIG: make Next/Continue available only once required data is entered, on short steps where what's missing is obvious (Apple HIG Entering data).
- **Whenever a control is disabled, say why** next to it (or in a focusable tooltip). Use `aria-disabled="true"` plus a click guard, so it stays focusable and can explain itself. **Never `pointer-events: none` on a disabled control**: it kills the hover tooltip that explains it (Figma Button states [synth caution]).
- Primary button aligned to the left edge of the inputs. "Back" is a link at the top-left. Cancel is less prominent, after the primary (Silver, Wroblewski).
- Labels are outcome verbs: "Save and continue", "Create account". Not "Submit" (Figma's endorsement of "Submit" is rejected).

### Validation timing (debated; this is the reconciled default)
- **Web baseline: validate on submit, then on blur or live once a field has been touched and has errored.** Native Apple apps may validate as soon as a value is entered and gate Continue on required data (Apple HIG Entering data).
- On submit, keep all input. Always validate on the server as well (GOV.UK, Silver).
- **Inline validation** only for fields with hidden constraints (username availability, password rules, character limits). Validate on blur, or after a debounce once the user pauses. Never validate on focus or the first keystroke (Wroblewski: "after" timing beat "while" and "before"; Baymard: blur, then re-validate on each keystroke once an error is showing so it clears the moment it's fixed).
- **Positive green ticks:** Baymard favours them; Wroblewski found them confusing on easy fields like names ("valid or correct?"). Use them only on hard fields such as a new password or username.

### Error display (GOV.UK pattern)
1. Re-render with values preserved. Prefix `document.title` with "Error: ".
2. **Error summary** at the top of `<main>` titled "There is a problem", linking to each field. Move focus to the summary.
3. **Inline message** for each field between the hint and the input, with a visually hidden "Error:" prefix, linked through `aria-describedby`. Add a red left border on the field group.
4. Use `<form novalidate>` and custom messages, not native bubbles mixed with custom styles.
5. Copy: see `09-ux-writing.md`, e.g. "Enter your date of birth", "Date of birth must be in the past".

## 1a. Buttons: type, style, state (Figma Button states, Apple HIG Buttons)

Separate **type** (role: submit, toggle, CTA, destructive), **style** (primary, secondary, ghost) and **state** (its condition now).

| State | Selector | Treatment |
|---|---|---|
| Default | `.btn` | Clearly clickable at rest; no "mystery meat" that only reveals itself on hover |
| Hover | `:hover` inside `@media (hover: hover)` | Subtle fill shift; never the only signal |
| Pressed | `:active` | Darker fill or `scale(0.97–0.98)`, on pointer-down. **Every custom button has one** (Apple HIG Buttons) |
| Focus | `:focus-visible` | ≥ 2px outline + offset (Figma uses 3px + 3px) |
| Disabled | `[aria-disabled="true"]` | Muted, `cursor: not-allowed`, reason shown nearby; still focusable; no `pointer-events: none` |
| Loading | `.is-loading` / `aria-busy` | Spinner inside the button, progressive label ("Checking out…"); block re-submission |
| Success | `.is-success` | Brief; label is the outcome ("Saved", "Sent"), never "Success" |
| Error | `.is-error` | **Resets to clickable**; inline message with cause + fix |
| Selected (toggle) | `[aria-pressed="true"]` | Stays on until toggled off; differs by more than colour |

- **Contrast 4.5:1 for the label in every state** (except disabled); state transitions 100–200ms (Figma).
- **1–2 accent-filled buttons per view; in a toolbar, exactly one,** on the trailing side (Apple HIG Buttons, Toolbars).
- **Mark the preferred choice by style, not size.** Buttons in one choice set share a size (Apple HIG Buttons).
- **Destructive buttons are styled destructive but are never the default.** Enter must never trigger a destructive action (Apple HIG Buttons/Alerts, APG).
- Append "…" to a label that opens a view asking for more input ("Rename…", "Export…"); not to buttons that act immediately (Apple HIG Buttons, Menus).
- **Add a tooltip to a toggle** when its icon changes between states, the action is hard to undo, or it affects something off-screen (Figma).
- Draw a state diagram per screen: one variation per relevant button-state combination ("payment fails: does the button reset? where does the message go?") (Figma).

## 2. Selects, comboboxes, autocomplete
- 2–5 options → radio buttons (all visible, one click). Many options → `<select>` or, for long lists, an accessible autocomplete (Silver: selects are often a last resort).
- **Combobox (W3C APG pattern):**
  - Focus stays in the input.
  - `role="combobox"`, `aria-expanded`, `aria-controls` pointing to a `role="listbox"`.
  - `aria-activedescendant` tracks the highlighted option.
  - `aria-autocomplete="list"` (or `"both"`).
  - Arrow keys move through options, Enter selects, **Esc closes and restores the previous value**.
  - Never swallow native text-editing keys (Home, End, arrow-left and arrow-right inside the text).
- Prefer a tested library implementation (Radix, React Aria, Headless UI, Ariakit) over hand-rolled widgets [synth].

### Control chooser (Apple HIG Toggles, Segmented controls, Steppers, Sliders, Token fields, Pickers; Android Settings)

| Need | Control | Numbers and rules |
|---|---|---|
| One on/off, applied instantly | Switch (`role="switch"`) in a settings row | iOS: switches live in list rows; outside lists use a toggle button (`aria-pressed`) |
| One on/off, submitted with a form | Checkbox | Never a single radio for one option (Android Settings) |
| Parent/child settings | Checkboxes, child indented | Parent shows `indeterminate` (–) when children differ; a parent switch disables its children |
| 2–5 exclusive options, all visible | Radio group | > ~5 → select |
| 2–5 closely related views or values, compact | Segmented control | ≤ 5 on mobile, ≤ 7 wide; equal widths; all text or all icons; never mix selection with actions |
| Many exclusive options | Select / pop-up button | Shows current value; sensible default; "Custom…" for rare extras. Very long → searchable combobox |
| Commands related to one button | Dropdown (pull-down) button | ≥ 3 items, otherwise plain buttons; never hide a view's primary actions in it |
| Small numeric changes | Stepper beside an editable field | Shift = ×10 [synth] |
| Continuous or imprecise range | Slider + exact-value field | Min on the leading side; live feedback; `aria-valuetext` |
| Several entities in one field | Token field | Comma/Enter creates a token; Backspace removes; each token has a menu or remove button |
| Date or time | Typed entry + picker in context | Locale order; reduce minute granularity (0/15/30/45) when sensible |

- **On/off state is visible without colour** (fill, shape, checkmark, dot). Test in greyscale (Apple HIG Toggles).
- Switches and checkboxes never live in toolbars or status bars (Apple HIG Toggles).

## 3. Dialogs (W3C APG, NN/g)
- `role="dialog"` (or native `<dialog>` with `showModal()`), `aria-modal="true"`, `aria-labelledby` the title.
- On open, focus moves inside: to the first field, or to the least destructive button for irreversible confirmations. **Tab wraps** inside the dialog, **Esc closes**, a visible close button is present, and **focus returns to the trigger** on close.
- Use modals only for interruptions that need a decision. For editing a record while referring to other rows, use a **non-modal side panel** (NN/g data tables).
- No modal for routine confirmations; prefer undo (see `07`).
- **Choose the overlay with `assets/overlay-chooser.md`** (alert vs action sheet vs sheet/dialog vs popover vs side panel vs inline).
- **One layer at a time.** Never open a modal, sheet or popover from another one; close the first, then open the next. Only an alert may sit on top (Apple HIG Modality, Sheets, Popovers).
- **Every dismissal path of a dirty dialog** (Esc, backdrop, swipe, ×) offers Save / Discard / Keep editing. A non-modal popover that closes itself keeps what was typed (Apple HIG Modality, Popovers).
- **Title a dialog with its task.** One path through it; no "app within your app" (Apple HIG Modality).
- **Button semantics:** Cancel/Close = dismiss without saving; Done = complete and dismiss; Back = previous step, never dismisses. Pair Done with Cancel or Back, never all three (Apple HIG Sheets).
- **Destructive confirmations:** focus the least destructive option; Enter never triggers the destructive action; the destructive button is styled destructive but isn't the default (APG; Apple HIG Alerts). Esc (and ⌘. on Mac) cancels.

## 3a. Menus, context menus, submenus (Apple HIG Menus, Context menus, Pull-down & Pop-up buttons; Eldh)

### All menus
- Items are **verbs without articles** ("View settings", not "View the settings"). "…" when the item needs more input. Most important items first. Separators between related groups; keep related commands together even if one is rare.
- **Icons for every item in a group, or none.** Standard actions use standard glyphs.
- **Toggle items:** one item with a changing label ("Show map" ↔ "Hide map"; add a verb if ambiguous: "Turn HDR on") or `menuitemcheckbox` with a checkmark. Offer "Clear all" when several toggles can be on.
- ARIA: menu-button pattern, `role="separator"`, shortcut in `<kbd>` and `aria-keyshortcuts` [synth]. Site navigation is not a menu (see `01 §5`).

### App menus, dropdowns and the command palette
- **Show keyboard shortcuts right-aligned** (Apple HIG Menus; NN/g accelerators).
- **Dim unavailable items; don't hide them** (`aria-disabled="true"`, still focusable). A menu whose items are all unavailable still opens.

### Context (right-click) menus
- Only the most relevant commands for that object, ≤ ~3 groups. **Hide** unavailable items. Destructive items last, in red. Title only when it clarifies scope ("3 items").
- The same menu on that object everywhere; every command is also reachable in visible UI (no hidden-only actions).
- Shortcuts **may be omitted** (Apple). Show them when the context menu is the product's main command surface, as in Linear, where it teaches shortcuts to mouse users (Eldh).
- The top actions match the object's swipe or quick actions (Apple Adopting Liquid Glass).

### Submenus
- Only when a term repeats in > 2 items ("Sort by ▸"). **One level deep.** > ~5 items → make a separate menu. Open on click or arrow key (Apple HIG Menus; NN/g, see `01 §5`).
- **Safe triangle:** keep a submenu open while the pointer travels diagonally towards it. Render an invisible polygon from the cursor to the submenu's near corners (`clip-path: polygon()`, ~40 lines; measure with `getBoundingClientRect()`). Test: move diagonally to the submenu's last item; it must stay open (Eldh, Linear 2020).

## 4. Notifications, toasts, alerts, tooltips
- Match the vehicle to severity (NN/g error guidelines):
  - inline message: field or section problem
  - banner: page- or system-level non-blocking issue
  - toast: confirmation of an action, ideally with **Undo**
  - modal: only for severe or blocking issues
- **Match intrusiveness to significance** (Apple HIG Feedback). Put passive status next to what it describes ("Updated just now · 3 unread").
- **Confirm completion only for significant tasks** (a payment, a send to many people). People expect success; tell them about failure. No success toast for routine save or toggle (Apple HIG Feedback).
- **Warn only about unexpected, irreversible data loss.** Don't warn when data loss is the expected result (moving to Trash) (Apple HIG Feedback).
- **When a command can't run, say why** ("Can't route to and from the same location") (Apple HIG Feedback).
- Feedback uses several channels (text, icon, colour; sound or haptics on devices) so it survives muted devices and screen readers (Apple HIG Feedback).
- Toasts: announce through an ARIA live region (`role="status"` for polite, `role="alert"` only for urgent). **Minimise time-boxed UI** (Apple HIG Accessibility): a toast with an action stays until dismissed or long enough to act (≥ ~5–10s), pausing on hover, focus and hidden tab [synth from WCAG 2.2.1; Sonner]. Toasts may enter in ~400ms.
- Status needs colour + icon + text.
- **Tooltips** hold supplementary information only, never essential instructions. They need keyboard focus support and hover persistence (WCAG 1.4.13). Prefer inline help (Vercel).
- Tooltip copy: start with a verb ("Restore default settings"), ≤ 60–75 characters, don't repeat the control's name, a fragment without a full stop; it may change with state. A control that needs a long tooltip needs simplifying (Apple HIG Offering help).
- **Tips** (coach marks for one feature): 1–2 sentences; only for features that take ≤ 3 actions; shown only to people who haven't used the feature; at most ~1 tip per 24h; dismissible; may link to the setting. No promotion (Apple HIG Offering help).

## 4a. Notification system rules (Linear Notifications/Inbox; Apple HIG Managing notifications)

- **One inbox receives everything.** Push, email and chat integrations are opt-in channels that link back to it.
- **Map every notification type to a tier:** passive (digest, view at leisure) · active (default) · time-sensitive (needs action now or within ~1h: security, delivery) · critical (health or safety; extremely rare). Never use a higher tier than the content deserves; **marketing is opt-in and never urgent**.
- **Never notify people about their own actions.**
- **Auto-subscribe on create, assign and @mention.** A mention in a thread subscribes to that thread only.
- **Email digests are delayed by urgency and sent only if the item is still unread.**
- Separate a **Priority** view from everything else; let people tune its filter.
- **Snooze** until a time or new activity, whichever comes first; accept typed times ("next quarter", "Jan 3 10am").
- Every type can be changed in-app, in Settings.

## 5. Data tables (NN/g, Laubheimer: four user tasks)
Tasks to support: **find and filter, compare, view or edit a single row, take batch actions.**
- First column is the **human-readable identifier** (name, not an auto ID). Order columns by importance.
- **Sticky header row** and, for wide tables, a sticky first column. Zebra stripes or row borders, plus row hover.
- Numeric columns right-aligned with tabular figures. Text left-aligned. Headers aligned like their data [synth; common practice consistent with tabular-nums guidance].
- Sorting: clickable headers with a visible direction indicator and `aria-sort`.
- Filtering: visible filter controls; **active filters shown as removable chips** with "Clear all"; a "filtered" indicator; filter state in the URL (Vercel: the URL reflects state).
- Row detail: a side panel (keeps context) or a dedicated page. Avoid modals for deep edits.
- **Batch actions:** row checkboxes plus "Select all", a selection count, and actions in a bar above the table. Report partial failures ("18 of 20 updated. 2 failed: Retry").
- Avoid hover-only row actions (invisible to touch and keyboard). Offer column hide and reorder without requiring drag.
- **Tables over cards** when people need to compare.
- **Selection feedback by meaning:** a navigation list keeps the selected row highlighted, also while focus is in the detail pane (dimmer "inactive selection" style); an option list shows a checkmark (Apple HIG Lists and tables).
- Clicking a sorted header again reverses the sort. Columns are resizable. **Middle-truncate** values that differ at the end (file names, paths). An ⓘ button reveals details; a chevron means drill-in. Alternating row backgrounds for wide multi-column tables (Apple HIG Lists and tables).
- **Don't reflow a list under the pointer** when new data arrives, except in response to an explicit action (Apple HIG Collections).
- At small widths, put the table in its own horizontal scroll container; the page itself must not scroll sideways (WCAG 1.4.10).

## 5a. Views: filters ≠ display options (Linear Filters and Display options docs)

- **Filters decide *which items* appear. Display options decide *how* they appear.** Keep them as separate controls.
- **Filters as sentences:** each filter reads "Property · operator · value" ("Assignee is Andreas"). Only the operator and value are clickable. The operator adapts to the values: is / is not → is either of / is not; labels: includes any / all / none; dates: before / after.
- **Quick filter by value:** typing "High" or a username in the filter menu offers it directly, skipping the category step. Nested AND/OR lives behind "Advanced".
- **Encode the main filters in the URL** so a copied link reapplies them. View options and temporary filters stay out (Linear Filters).
- **Display options:** layout (list / board / timeline), grouping and sub-grouping, ordering (reversible except manual), show empty groups, and which properties show on each item.
- **Group headers are sticky** with a count; clicking toggles count ↔ sum (estimates).
- **Ordering by status in lists:** closest-to-done first, completed and canceled last. Boards keep workflow order.
- **Personal changes persist automatically.** Offer "Set as default" (shared with the workspace) and "Reset to default".
- Task-specific options (sort, filter, density, columns) live on the screen they affect, **not in Settings** (Apple HIG Settings, Android Settings).

## 6. Navigation, tabs, sidebars
- See `01-product-thinking.md §5` for menu rules.
- **Tabs:** for peer views of the same object. `role="tablist"`/`tab`/`tabpanel`, arrow keys between tabs, one tab stop (APG). Put the active tab in the URL.
- **Sidebar:** 5–9 top-level items, grouped. The current item has `aria-current="page"` and a visual state beyond colour alone.
- Navigation uses real `<a href>` links (middle-click, open in new tab, prefetch). Never a `div onClick` (Vercel).
- **Mobile tab bar:** navigation only, never actions; always visible except under a modal; 3–5 single-word labelled tabs; **never disable or hide a tab** (show an explained empty state); no "More" overflow tab; each tab keeps its own sub-route and scroll; badges only for critical or actionable items (Apple HIG Tab bars).
- **Sidebar:** ≤ 2 levels (deeper → add a list column, i.e. a split view); collapsible with a button + shortcut, persisted, **visible by default**; monochrome icons; no critical actions only at the bottom (Apple HIG Sidebars). Navigation recedes so content leads: dimmer inactive text, smaller icons (Aufmann & Heckel, Linear 2026).
- **Header/toolbar zones:** leading [back · sidebar toggle · title ≤ ~15 chars, never the product name] / centre [common tools, which collapse first into overflow] / trailing [search · inspector toggles · More · one primary]. ≤ 3 groups; space text buttons apart from icon buttons; borderless icons, each with a text title for its accessible name, tooltip and overflow label (Apple HIG Toolbars, iPhone Duo).
- **Recurring header actions sit in the same position on every screen** (Aufmann & Heckel, Linear 2026).
- **One overflow menu, marked with an ellipsis**; use the ellipsis for nothing else. Frequent and badged items overflow last (Apple HIG iPhone Duo).
- **Put controls next to the content they affect** (list controls above the list), not in a global bar (Apple HIG iPhone Duo).
- **Hover, focus and press style the actionable items, not their containers.** Never highlight a whole toolbar, sheet or nav. One element is hovered, focused or pressed at a time (M3 States).
- **Hover-only affordances only behind `@media (hover: hover)`, and every swipe, drag or pinch has a visible control alternative** (WCAG 2.5.7; Apple HIG Accessibility; Android accessibility).

## 7. Search, filter, sort (Apple WWDC26-292, Apple HIG Searching/Search fields, Linear Search, Hurff, NN/g)

### Placement and scope
- Search is visible where it's a primary task (a magnifying glass plus a field, not a hidden icon on desktop).
- **Placement communicates scope.** One global search location (top bar, a search tab or a /search page). Section search sits directly above the section and filters only it.
- **The placeholder names the scope:** "Search invoices", not "Search".
- **Keep the standard anatomy:** magnifying glass (a custom icon must closely resemble it), label/placeholder, clear (×) whenever there's text, Esc to clear or close. Use `<search>` or `role="search"` + `<input type="search">` [synth].
- A dedicated search view focuses the field on arrival, except on touch-only devices (Apple HIG Search fields).

### While typing
- **Search as people type** (debounced). Highlight matched terms. Preserve the query and scope in the URL.
- **Recent searches on focus**, before typing. Be selective (consider only results people opened); each is removable, plus "Clear all". History is private; let people clear it (Apple WWDC26-292).
- **Suggestions complete what's typed**; visually distinguish the typed part from the predicted part; cap at ~5–8 so results stay dominant [synth; Apple gives no number]. Combobox pattern (`aria-autocomplete="list"`).
- **Start broad, then narrow:** default to the broadest scope; offer a scope control (All / This folder) and only the filters relevant to the query. Filter tokens inside the field are a power feature, **never the only filter UI** (Apple WWDC26-292).

### Ranking and power use (Linear Search)
- Rank active work first: in progress and unstarted, then backlog, completed, canceled, archived.
- Accept exact and shorthand IDs (`LIN-123`, `lin123`); an ID + Enter opens the object. Quotes force an exact match.
- `@`-mentioning a person or status inside search turns it into a filter chip.
- ⌘/Ctrl+F gives in-view search as a temporary filter; Esc clears it.

### No results
- **Echo the query** so typos are visible, suggest corrections and offer to clear filters. A search icon + title + subtitle; never a blank pane or a dead end (Apple WWDC26-292, Hurff).

## 8. Anchoring
- Long-press and swipe actions follow the gesture rule in §6 (visible alternative required).
- Menus, popovers and action sheets anchor to the control that opened them; content outside a non-modal menu stays interactive (Apple Adopting Liquid Glass).

## 9. Settings screens (Apple HIG Settings, Android Settings)

- **Prefer detection and good defaults to settings; keep settings few.** Defaults are what most people would choose: neutral, low-risk, low on battery and data, interrupting only when important (Android Settings).
- **Settings hold infrequent, general options** (account, notifications, keymaps). Frequent options live in context (captions on the player; sort and filter on the list).
- **Don't duplicate OS preferences** (theme, motion, text size, accessibility). Follow `prefers-color-scheme` / `prefers-reduced-motion`; if a theme switch exists, offer System (default) / Light / Dark.
- **Entry points:** ⌘/Ctrl+, opens Settings. Call it "Settings", never "Options" or "Preferences". In a drawer, it sits after everything except Help & Feedback. Reachable when signed out (Android Settings).
- **15+ settings → group into subscreens;** add search for deep hierarchies. **The row label that opens a subscreen matches its title.** Each section has its own URL; reopen to the last section.
- **Dependencies:** the dependent setting sits below its parent and says why it's unavailable; a parent switch disables its children.
- **Controls:** switch or checkbox for on/off; radios in a child screen or dialog for one-of-N; slider for imprecise ranges (see the control chooser in §2).
- **Labels** describe what the setting does when on; supporting text shows **status**, not a description. Copy rules in `09 §6a`.
- Wide windows: list–detail; never stretch single-pane settings full width.

## 10. Sign-in and account screens (Apple SIWA, Apple HIG Managing accounts, Android Onboarding)

Timing (value first, guest checkout, defer optional data) is a product decision: see `01 §11`.
- **Provider buttons are equal:** same height, width and radius, all visible without scrolling, in a consistent order, each with a text label ("Continue with Apple", "Continue with Google"). Logo-only only if all are logo-only.
- **Sign in with Apple:** black or white only (white on dark; black or outlined white on light), title "Sign in with Apple" / "Sign up with Apple" / "Continue with Apple" used consistently, minimum **140×30**, clear space ≥ **1/10 of its height**, official artwork only, never recoloured.
- **Name the method on the button** ("Sign in with passkey") and offer only methods available on this device (Apple HIG Managing accounts).
- **State password rules up front;** keep "Forgot password" reachable; mask sensitive input by default; `autocomplete="current-password"` / `"new-password"` / `"one-time-code"` (Android Onboarding).
- After SSO, ask only for legally required fields, each with a reason and a required/optional marker. Show the current method in account settings ("Signed in with Apple").
- Confirm minor actions with a toast, not a dialog (Android Onboarding).

## 11. Verification
- [ ] Labels visible above inputs; no placeholder-only fields.
- [ ] Submit enabled; errors preserve input; error summary + inline messages + focus management.
- [ ] Dialogs trap focus, close on Esc and return focus to the trigger.
- [ ] Comboboxes follow APG keyboard behaviour.
- [ ] Tables have a human-readable first column, sticky header, aria-sort, visible filters and batch actions.
- [ ] Every navigation item is a real link; current location indicated.
- [ ] Disabled controls explain why; none use `pointer-events: none`; every custom button has pressed and focus states; ≤ 2 accent-filled buttons per view.
- [ ] No overlay opens from another overlay; every dirty dialog guards all dismissal paths; Done is paired with Cancel; Enter never confirms a destructive action.
- [ ] Menu groups are all-icons or no-icons; dropdowns have ≥ 3 items; submenus are 1 level and survive diagonal travel.
- [ ] Filters and display options are separate controls; main filters are in the URL.
- [ ] Search placeholder states the scope; recents removable; suggestions capped; no-results echoes the query.
- [ ] Every notification type has a tier; no self-notifications; marketing is opt-in.
- [ ] Provider sign-in buttons measure equal; core content renders signed out where possible.
- [ ] Settings labels match subscreen titles; no OS preference duplicated; task options live in context.

# 07 · Power users, speed and perceived performance

This covers command palettes, keyboard shortcuts, drag and drop, multi-select, undo, creation and drafts, optimistic UI and response-time budgets.

## 1. Response-time budget (Nielsen; Vercel; Hurff)

| Delay | User perception | What to do |
|---|---|---|
| ≤ 0.1s | Instantaneous; feels like direct manipulation | Visual feedback on every input within this window |
| ≤ 1s | Flow uninterrupted, but delay noticed | No spinner needed; optimistic UI for mutations |
| 1–10s | Attention strains | Busy indicator (skeleton or spinner with show-delay) |
| > 10s | Users leave the task | Determinate progress, time estimate, **Cancel**, and the ability to keep working |

- Progress must be honest and evenly paced; rules in `08 §1` (Apple HIG Progress indicators).

- Vercel: network mutations should complete or *appear* to complete in **under 500ms**. Use optimistic updates.
- Doherty threshold (Laws of UX): around 400ms keeps people productive.
- The same Laws of UX page notes that deliberate delay can raise perceived value. Use that "labour illusion" only for rare, high-stakes results (a security scan), never for routine tasks.

## 2. Optimistic UI (Atlassian, Hurff/Krieger, Wallace/Figma)
- For likes, moves, renames, toggles and reorders: **apply the change locally at once**, sync in the background, and reconcile.
- On failure, show an **inline, retryable state**: the item dims, shows an alert icon and offers "Retry". Never silently drop the user's change.
- Distinguish "saved locally, will sync" from "saved" (web.dev offline guidance).
- Figma's multiplayer model: the client ignores server echoes that conflict with its own pending local changes, which prevents flicker. Undo and redo are **user-local** and must never overwrite other people's later edits (Wallace).

## 3. Undo over warnings (Aza Raskin)
- **"Never use a warning when you mean undo."** People act out of habit: they confirm dialogs automatically, so warnings stop protecting them.
- Pattern: perform the action immediately, show a toast "Deleted 'Q3 plan' · Undo" (about 5–10s, pausing on hover and focus [synth]), soft-delete on the server, and keep a Trash or Archive.
- Keep confirmations only for actions that are **irreversible and unexpected or high-cost** (delete an organisation, wipe data). Never confirm an action whose data loss is the expected result (moving to Trash) (Apple HIG Feedback/Alerts).
- In a confirmation: name the object and its consequences; **focus the least destructive option; Enter never triggers the destructive action; the destructive button is styled destructive but isn't the default** (APG; Apple HIG Alerts). Type-to-confirm is for truly catastrophic actions only.
- Undo for everything is part of Apple's principles too: forgiveness over interruption (WWDC26).

### The forgiveness stack (Linear delete/archive docs)
1. **⌘/Ctrl+Z immediately** after delete, move or bulk edit (toast with Undo).
2. **"Recently deleted"** for a fixed window (Linear: 30 days), restorable by the user.
3. **Permanent** only after that, and labelled as unrecoverable "including by support".
- Prefer automatic archiving (keeps history) to a manual archive action that clutters the workspace.
- Moves that change an object's ID keep old URLs redirecting and old IDs searchable (see `08 §1`).

### Undo details (Apple HIG Undo and redo)
- **Label undo by its target:** "Undo rename", "Redo bold", "Undo address change".
- **Show the result:** if the change was off-screen, scroll to and highlight it, or people press undo again.
- **Multi-level history** back to a logical point (open or save), without arbitrary limits. Offer "Revert to saved" where it makes sense.
- **Coalesce continuous adjustments** into one step: one slider drag or one typed word = one undo.
- Use the standard shortcuts (⌘Z / ⇧⌘Z; Ctrl+Z / Ctrl+Shift+Z or Ctrl+Y) and never redefine them. Dedicated undo buttons only when needed, with standard icons, in the toolbar.
- Undo is **user-local** in multiplayer (Wallace, §2).

## 4. Command palette (Superhuman: Boucher; Linear; NN/g accelerators)
1. **Same shortcut opens and closes** it from anywhere: ⌘K on macOS, Ctrl+K on Windows and Linux. Closing restores the previous focus.
2. **One central palette covers every action.** Register commands alongside their shortcuts in one registry, decoupled from the UI components.
3. **Fuzzy, case-insensitive matching with aliases.** Show matches as "Title (alias)" so people learn the canonical name.
4. **Curated defaults when the query is empty:** recent items and the most likely actions.
5. **Context-aware ranking:** commands relevant to the current selection or page come first.
6. **Show each command's shortcut** in the results, so the palette teaches shortcuts.
7. **Scope prefixes:** typing `i ` limits results to issues, `p ` projects, `u ` users, and so on; an object ID + Enter opens it directly (Linear Search).
8. Don't animate open and close; it's a high-frequency action (Emil, Rauno).

Accessibility: combobox + listbox pattern (APG), `aria-activedescendant` for the highlighted option, and a visible focus/highlight state.

## 5. Keyboard shortcuts (NN/g accelerators; Apple macOS HIG; Linear)
- Accelerators are **alternatives, never the only way**. Every shortcut action is also reachable through visible UI.
- **Discoverable:** show shortcuts right-aligned in app menus, dropdowns and the command palette, and in tooltips, but not *only* in tooltips, which touch users never see. Context menus may omit them (Apple HIG Context menus); show them there when the context menu is the main command surface (Eldh, Linear). Teach them just in time, right after someone uses the slow path. A `?` cheat sheet lists them all.
- Never override platform shortcuts: ⌘/Ctrl + C, V, X, Z, A, P, F, W, T, L.
- Single-key shortcuts (Linear style: `C` create, `/` search) only when focus isn't in a text field. Make them remappable or disable-able if they could conflict with assistive tech (WCAG 2.1.4).
- Give visible feedback when a shortcut fires.
- Desktop and productivity apps should be **command-complete**: every command in a menu bar or palette with a shortcut (Apple macOS HIG).
- Standard keys: ⌘/Ctrl+, opens Settings; Esc (and ⌘. on Mac) cancels a dialog; Space plays or pauses media (Apple HIG Settings, Alerts, Playing video).

### Reference keyboard model (Linear docs)
| Layer | Keys | Notes |
|---|---|---|
| Global | ⌘/Ctrl+K command menu · `/` search · `?` shortcut list · `C` create · Esc back or clear selection | Available from anywhere |
| Go to (sequence) | `G` then letter: `G I` inbox, `G M` my items | Two-key mnemonic by verb |
| Open picker (sequence) | `O` then letter: `O U` user, `O L` label, `O S` settings | |
| Relate (sequence) | `M` then letter: `M B` blocked by, `M R` related | |
| Property verbs | `P` priority · `L` label · `F` filter · `H` snooze · Shift+letter for more | Act on the highlighted or selected item |
| Lists | `J/K` or ↑/↓ move · `X` select · Shift+arrows extend · ⌘A select all (filtered) · Option+↑/↓ reorder | |
| Queues | `1` accept · `2` decline · `3` duplicate | Numbered keys for repeated triage decisions |
| Peek | Space toggles a preview; hold Space for a temporary peek | |
| View | ⌘/Ctrl+B list ↔ board · Shift+V display options · ⌘/Ctrl+I details panel | |

Single letters fire only when focus isn't in a text field (WCAG 2.1.4).

## 6. Selection and bulk actions
- **Nothing is selected by default.** Hovering or arrowing **highlights** an item; actions apply to the highlighted item when nothing is selected (Linear Select issues).
- Reveal the row checkbox on hover near the left edge (and always on touch and keyboard focus). With a selection, show a bulk-action bar (Linear puts it at the **bottom**). Right-click acts on the whole selection (Linear).
- Shift-click selects a range, ⌘/Ctrl-click toggles one item, and a header checkbox selects all on the page, with an offer to "Select all 2,431".
- When there's a selection, show a bulk-action bar with the count. Esc clears the selection.
- **Selection ≠ focus:** style them differently. Only let selection follow focus when the change is instant (APG).
- Report partial results for bulk operations and offer retry for the failures.

## 7. Drag and drop (Atlassian Pragmatic drag and drop guidelines)
- **Drag handle** on the left of the item: always visible if dragging is the item's primary action. If it's secondary, reveal it on hover or focus, and switch to a grab cursor after an 800ms delay. Handle target ≥ 24×24px.
- **Drag preview:** offset 16px horizontally and 8px vertically from the pointer, at most 280×280px, showing at most 3 pieces of information, with no rotation.
- **Original item** stays in place at 40% opacity.
- **Drop indicator:** a 2px line with an 8px terminal dot; target highlight transition ~350ms.
- **On drop:** update optimistically and flash the moved item for ~700ms to confirm where it landed.
- **Every move is also available without dragging**, through a menu ("Move up", "Move to…") or keyboard. This is required by WCAG 2.5.7.
- Auto-scroll near container edges.
- Start the drag preview after ~3px of movement; make it translucent so targets stay visible (Apple HIG Drag and drop).
- **Highlight a drop target only while hovered and able to accept** the item; otherwise show nothing or a "not allowed" cursor.
- Invalid or failed drop: animate back to the source (or fade out).
- Default semantics: same container = move; different container = copy; Alt/Option at drop forces copy.
- Multi-item drags show a count badge (updated if the target accepts only some). After the drop, keep the dropped items selected.
- **Every drop is undoable**; a drop that can't be undone is confirmed first. Slow drops show a placeholder with progress at the drop location (Apple HIG Drag and drop).

## 7a. Creation and drafts (Linear Issues docs; Apple HIG File management)
- **Treat edits in the first ~3 minutes after creation as part of creation**, not activity-log noise.
- **Keep a local draft** when the composer is dismissed by navigation and reopen it next time; on explicit close of a non-empty composer, offer "Save as draft".
- **Support prefilled creation URLs** (`/new?title=…&priority=…&assignee=me`).
- Always offer a visible Create (+) in addition to the shortcut and menu command (Apple HIG File management).
- Autosave rules are in `08 §5a`.

## 8. Perceived performance (Vercel; Hurff; Linear)
- Skeletons that match the final layout; zero layout shift (reserve image dimensions, font fallback metrics).
- Prefetch likely next routes on hover or intent. Make interactions feel instant with local-first data where possible. Linear built a sync engine so the UI works off local state.
- Never block the whole UI with a modal spinner during network calls. Queue the work and let people continue (web.dev offline guidance).
- Virtualise long lists. Keep the main thread free; input handlers stay under 50ms [synth; standard web performance guidance].
- Measure on low-end devices with CPU and network throttling (Vercel).

## 9. Verification
- [ ] Every input shows feedback within 100ms; mutations feel instant (optimistic) with visible failure and retry.
- [ ] Reversible destructive actions use undo, not confirmation.
- [ ] ⌘K palette covers all actions, uses fuzzy matching, shows shortcuts, restores focus, and has no animation.
- [ ] Shortcuts discoverable in menus; no platform shortcuts overridden.
- [ ] Drag and drop has a handle, drop indicator and non-drag alternative; every drop is undoable.
- [ ] Undo is labelled by its target, reveals off-screen changes, and coalesces continuous drags into one step.
- [ ] Delete follows the forgiveness stack (undo → recently deleted → permanent, labelled).
- [ ] Nothing selected by default; highlight vs selection styled differently; Esc clears.
- [ ] Shortcuts shown in app menus and the palette; single-key shortcuts inactive in text fields.

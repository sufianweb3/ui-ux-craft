# Overlay chooser: alert · action sheet · sheet/dialog · popover · side panel · inline

Use this before you add anything that floats over content. Start at the top and stop at the first row that fits. Most "I need a modal" moments end at **inline**, **toast + Undo** or **side panel**.

Sources: Apple HIG Alerts, Action sheets, Sheets, Popovers, Modality, Feedback; W3C APG Dialog; NN/g error guidelines; Raskin. Rules marked [synth] are inferred for the web.

## 1. Decision table

| If the content is… | Use | Not |
|---|---|---|
| Status or information that needs no decision (saved, synced, offline, 3 unread) | **Inline status** next to what it describes, or a **banner** for page/system level | An alert or popover just to inform |
| Confirmation of a routine or reversible action (delete email, archive, move) | Act immediately + **toast with Undo** | "Are you sure?" |
| Critical, usually unexpected, actionable, and **irreversible** | **Alert** (small modal dialog) | Alert on page load; alert for undoable actions |
| Choices about an action the person **just started** ("Discard changes / Save draft / Keep editing") | **Action sheet** (web: small confirm anchored to the trigger) | A centred alert |
| A short, scoped task tied to the current context (rename, invite, edit one record's details) | **Sheet / dialog** titled with the task | A full page; a nested modal |
| Editing a record while referring to the list behind it; repeated input-and-observe (find & replace, formatting, inspector) | **Non-modal side panel / panel** | A modal that hides the context |
| A small amount of related info or controls, anchored to its trigger (date picker, filter options, quick settings) | **Popover** (bottom sheet at compact widths) | Popover for warnings; popover on phones |
| A long, complex or multistep task (compose, photo edit, onboarding, checkout) | **Full page / full-screen modal / new window** | A sheet with sub-navigation ("app within your app") |
| Commands for an object | **Menu** (dropdown or context menu), see `references/06-interaction-patterns.md §3a` | A popover of buttons |

## 2. Rules per overlay

### Alert (Apple HIG Alerts; APG)
- **Only** for critical, actionable, usually unexpected information. Never on page or app load; never merely to inform; never for common undoable actions.
- Title ≤ 2 lines saying what happened and why; optional short text; **≤ 3 buttons**; never scrolls.
- Buttons: 1–2 word verbs tied to the text; "OK" only when it purely informs; never Yes/No; dismiss = "Cancel".
- **Destructive:** focus the least destructive option; **Enter never triggers the destructive action**; style it destructive but never make it the default. Cancel is never the default either; to force reading, have no default.
- Esc (and ⌘. on Mac) cancels. Only one alert at a time; an alert may sit above another overlay.
- Warning icon only for unexpected data loss.

### Action sheet / anchored confirm (Apple HIG Action sheets)
- Choices about an action the person just initiated. Short title on one line; message only if needed.
- Destructive choice styled destructive; Cancel last. Never scrolls.
- Web [synth]: a small dialog or popover anchored to the trigger, with explicit choices ("Discard changes", "Save draft", "Keep editing").

### Sheet / dialog (Apple HIG Sheets, Modality; APG Dialog)
- Titled with its task. One path through it; no buttons that could be mistaken for dismissal.
- **Cancel/Close** = dismiss without saving · **Done** = complete and dismiss · **Back** = previous step, never dismisses. Pair Done with Cancel or Back; never show all three.
- **One at a time.** If an action inside needs another sheet, close the first.
- **Dirty-state guard on every dismissal path** (Esc, backdrop, swipe, ×): Save / Discard / Keep editing.
- Mobile: bottom sheet with medium (~half) and large (full) detents and a grabber that is also a keyboard-operable button [synth].
- APG: `<dialog>` with `showModal()` or `role="dialog"` + `aria-modal="true"` + `aria-labelledby`; focus moves inside; Tab wraps; Esc closes; focus returns to the trigger.

### Popover (Apple HIG Popovers)
- Points at its trigger without covering it or essential content. Sized to content; animate size changes.
- Closes on outside click or on selection; **multi-select popovers stay open** until explicit dismissal.
- **Save input when a non-modal popover auto-closes**; discard only on explicit Cancel.
- **One popover at a time; never cascade.** Clicking another trigger closes this one *and* opens that one in a **single click** (don't swallow the click on outside-dismiss) [synth web detail].
- Never for warnings. At compact widths (< ~600px) use a bottom sheet instead [synth].
- Don't say "popover" in help text; name the task.

### Side panel / non-modal panel (NN/g data tables; Apple HIG Sheets)
- Keeps the list or document usable behind it. No scrim. Changes apply live or with an explicit Save in the panel.
- Esc closes and returns focus to the item that opened it. Selection in the list stays highlighted.

### Toast and banner (NN/g; Apple HIG Feedback, Accessibility)
- Toast: confirmation of an action, ideally with **Undo**. `role="status"`. With an action, it stays until dismissed or long enough to act, pausing on hover, focus and hidden tab. Minimise time-boxed UI.
- Banner: page- or system-level, non-blocking issue, with the fix or a link. `role="status"`, or `role="alert"` only if urgent.
- Don't confirm routine success at all; confirm significant completions (payments) and every failure.

## 3. Motion (see `references/05-motion.md`)
- Menus, popovers and dialogs: 150–250ms. Sheets and drawers travelling far: up to ~500ms. Toasts may enter ~400ms. Anything opened hundreds of times a day (command palette): minimal or no animation.
- Popovers scale from their trigger (`transform-origin`); centred modals stay centred. Dismiss along the axis the overlay entered on.
- Reduced motion: replace movement with a fade; don't remove the feedback.

## 4. Checklist per overlay
- [ ] It's the lightest overlay that fits (table in §1); not used merely to inform.
- [ ] Titled with its task (sheets/dialogs) or its consequence (alerts).
- [ ] One layer at a time; nothing opens from inside it except an alert.
- [ ] Esc closes it; focus moves in on open and returns to the trigger on close.
- [ ] Every dismissal path of a dirty overlay offers Save / Discard; auto-closing popovers keep input.
- [ ] Done is paired with Cancel (or Back); never Cancel + Done + Back together.
- [ ] No destructive default; Enter never confirms a destructive action; least destructive option focused.
- [ ] Popovers switch to another popover in one click; compact widths get a bottom sheet.
- [ ] Anchored overlays point at their trigger and don't cover it.
- [ ] Works at 320px, 200% text, keyboard only, and with a screen reader.

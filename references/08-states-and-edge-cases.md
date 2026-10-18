# 08 · States and edge cases

Most "awkward" interfaces only designed the ideal state (Scott Hurff, *The UI Stack*). Production UI designs every state, and the transitions between them.

## 1. The five screen states (Hurff)

| State | What it is | Rules |
|---|---|---|
| **Ideal** | The happy path with typical content | Design it last, after the others reveal constraints [synth] |
| **Empty** | Nothing to show yet | Three kinds: **first use**, **user-cleared** (inbox zero, celebrate), and **no results** (echo the query, suggest fixes, offer to clear filters). Always give a specific next action as a button or link. Never a bare "Nothing here". Empty states are temporary: never put crucial information there that disappears once content exists (Apple HIG Writing). |
| **Loading** | Waiting for data | Skeletons that mirror the layout, not a spinner on a blank page. Show-delay of 150–300ms, minimum visible time of 300–500ms (Vercel). Progressive loading: show what you have. A blank screen reads as a bug (Apple HIG Loading). |
| **Partial** | Some content: 1 item, half a profile, a chart with 2 points | Must look intentional. Nudge toward completion without nagging. |
| **Error** | Something failed | Say what happened and what to do. Keep user input. Offer retry. Inline near the cause where possible. |

### Honest progress (Apple HIG Progress indicators, Loading)
- **Prefer determinate progress.** Switch indeterminate → determinate (within the same bar style) once the duration is known. **Never morph a spinner into a bar** or back.
- **Pace progress honestly and evenly.** Not 90% in 5 seconds and then 5 minutes for the rest. Keep it moving; if it stalls, say why and what to do.
- **Describe the task, not "Loading…":** "Importing 3 of 12 files…", "Checking your card…". Don't label small inline spinners; the person just triggered them.
- **Offer Cancel** when stopping has no side effects; add **Pause** when cancelling would lose progress; confirm a cancel that loses work.
- Keep progress indicators in a consistent location across the app.
- Pull-to-refresh complements automatic refresh, never replaces it; its label carries value ("Updated 5 min ago"), not instructions.

### First paint (Apple HIG Launching)
- The first paint matches the first screen: same background per theme, same frame. **No logo splash and no text-only launch screen.** A brand moment, if any, belongs at the start of onboarding.

Add, where relevant:
- **Offline** (web.dev): say what state the app is in **and what still works**, in plain action language; avoid the bare word "offline". Show "Last updated 3 min ago". Don't grey everything out, which reads as disabled. Queue changes and say "Saved on this device. Will sync when you're back online." Use tap-to-refresh rather than replacing content someone is reading.
- **Permission denied:** explain why, who to ask, and offer a "Request access" action. Don't 404.
- **Rate-limited / quota reached:** when they can retry, and how to upgrade, if relevant.
- **Concurrent edits:** show presence (who else is here). Resolve conflicts without losing work, using last-writer-wins at property level as Figma does. Never let one person's undo overwrite another's edits (Wallace).
- **Partial failure in bulk:** "18 of 20 archived. 2 couldn't be archived: [Retry] [View]".
- **Long-running jobs:** progress, ability to leave, notification when done.
- **Stale data:** "last updated" times and an explicit refresh.
- **Resize is a state.** Window resize, rotation and fold are state transitions: preserve selection, scroll, form input and open panes across breakpoints. List–detail: narrowing keeps the detail; widening from list-only shows a placeholder detail ("Select a conversation") (Android canonical layouts).
- **URL permanence.** When an object moves or is renamed, old URLs redirect and old IDs stay searchable (Linear Issues).
- **Graded time-based status.** Due date: red when today or overdue, orange within 7 days, grey otherwise; the tooltip shows the exact date and days remaining. SLA risk: grey → yellow → orange → red (> 1 week, ≤ 1 week, ≤ 1 day, breached). Always colour + icon + tooltip (Linear Issue properties).
- **The current user in a list:** label them "You", and hide actions that can't apply to yourself (remove yourself as owner, message yourself) (Emil break-ui).

## 2. Content extremes (Frost, Apple, Vercel)
Test every component with:
- Very short and very long text (a 3-character name and a 340-character title; long unbroken URLs and emails). Use `overflow-wrap: anywhere` or `break-word`, truncate with a tooltip or expansion, and use `min-width: 0` on flex children.
- 0, 1, 2, 10 and 10,000 items (pagination or virtualisation).
- Missing avatars and images (initials fallback, reserved aspect ratio).
- Large numbers (1,234,567 with locale formatting), negative numbers and zero.
- Localisation: text expansion of 30%+, right-to-left languages (logical properties `margin-inline-start`), and dates and times with time zones specified (Microsoft style).
- 200% text size and 320px width.
- Slow network, failure at every request, and double-clicks on submit (idempotency, disable re-submit while pending).
- Admin and non-admin variants; first-run vs power user.

"The component isn't badly built; it was built against kind data." Demo data is chosen, usually unnoticed, to make the design look good. The breaks that ship are rarely the 5,000-character name; they're "the short name that leaves an orphaned dash, the missing avatar, the count of exactly 1 ('1 members'), the empty list, the badge whose text got translated" (Emil break-ui).

### 2a. Worst-case catalogue (Emil break-ui CATALOG, condensed)
Every value must be plausible or the schema's real limit; nonsense ("aaaa…") proves nothing. Use `example.com` / `.test` domains.

| Field type | Values to test |
|---|---|
| Names | `Aleksandra Wiśniewska-Kowalczyk` · `Christopher Alexander Montgomery III` · `Jo` · `J` · `Đặng Thị Ngọc Hân` · `王秀英` · `نور الهدى عبد الرحمن` (needs `dir="auto"`) · `María José de la Cruz y Fernández` · `🦊 Fox` (`.charAt(0)` → �) · `👩🏽‍💻 Priya` (ZWJ) · `  Sam   Lee ` (whitespace) · missing |
| Emails, IDs, files | `bartholomew.fitzgerald@northwind-industries-holdings.example.com` · `a@b.co` · `first.last+billing-notifications@example.com` · a long URL · a UUID · `Q3 Board Deck — FINAL (revised) v12 [approved by legal].pdf` |
| Labels and text | `Benachrichtigungseinstellungen` (30 chars, no spaces) · French +30% · 12 tags (→ "+8") · empty or whitespace-only title · `<script>alert(1)</script>` · a newline in a single-line field · a 2,000-character paste |
| Numbers | 0 · 1 · 1,284 · 1,000,000 · 12345678.9 as currency · −42.5 · 0.1 + 0.2 · 142% / −3% · null / NaN · de-DE vs en-US · 99 → 100 live |
| Collections | 0 · 1 · page size · page size + 1 · 1,000+ · one item 10× larger · duplicate names |
| Time | now · 12 days ago · future dates · 1970-01-01 · a time-zone day boundary · 1,284 hours (durations that never roll up) |
| Media | 404 image · no avatar · 4000×200 and 200×4000 · transparent or dark logo in dark mode · slow image without `aspect-ratio` |
| States | every enum value at once · no permission · the current user in the list |
| Environment | 320px · a 280px sidebar placement · 2560px · 200% zoom · dark mode · RTL · touch (hover-only ••• unreachable) |

### 2b. Truncate, wrap or clamp: decide per field (Emil break-ui)
- **Wrap** identifying text (names, titles). Two lines is fine; four means the column is too narrow.
- **End-truncate** secondary metadata, with access to the full value.
- **Middle-truncate** values that differ at the end: file names, paths, hashes, emails sharing a domain (Emil; Apple HIG Lists and tables).
- **Clamp** card previews (`line-clamp: 2`).
- **Never truncate numbers, amounts, dates or anything people compare.**
- Every truncation has an escape: `title`/tooltip plus the full value elsewhere. Don't truncate in a scrollable region unless the full text is one tap away (Apple HIG Typography).

### 2c. Format through the platform, not string concatenation (Emil break-ui)
| Need | Use |
|---|---|
| Plurals ("1 member", not "1 members") | `Intl.PluralRules` |
| Locale separators; compact `1M` only where precision doesn't matter | `Intl.NumberFormat` |
| "just now", not "0 seconds ago"; switch to an absolute date after about a week | `Intl.RelativeTimeFormat` |
| Dates and times, with an explicit zone for scheduled times | `Intl.DateTimeFormat` |
| Initials: first + last grapheme, fallback icon | `Intl.Segmenter` |
| User text with markup characters | Escape once, at render |

### 2d. Failure signatures: symptom → fix (Emil break-ui)
| Symptom | Fix |
|---|---|
| Avatar squished | `flex-shrink: 0` on the avatar |
| Text overflows its flex/grid cell | `min-width: 0` on the flex child; `minmax(0, 1fr)` in grids |
| Email or URL overflows | `overflow-wrap: anywhere` |
| Trailing action pushed off the row | `min-width: 0` on the middle, `flex-shrink: 0` on the action |
| Badge wraps | `white-space: nowrap; flex-shrink: 0`, and decide what yields instead |
| Avatar adrift beside a 3-line name | `align-items: flex-start` |
| Last row cut off | Visible scrollbar or a fade mask |
| Mid-word break in a heading | Replace `word-break: break-all` with `overflow-wrap: anywhere` |
| Wrong initials (emoji, multi-part names) | `Intl.Segmenter`, first + last word, fallback icon |
| Orphaned "—" for missing data | Omit the line, or reserve the height intentionally |
| "1 members" | `Intl.PluralRules` |
| Numbers jitter as they update | `font-variant-numeric: tabular-nums` |
| Raw numbers or NaN | `Intl.NumberFormat`; guard null |
| Translated label overflows | Content width + `min-width`, never a fixed `width` |
| Clipped diacritics (Vietnamese, Thai) | Looser line-height; no fixed heights or clipping on text boxes |
| Broken avatar image | `onError` → initials; `object-fit: cover` |
| Truncation with no escape | `title`/tooltip + full value elsewhere |
| 1,000 rows stutter | Virtualise or paginate |
| Raw `<b>`, `&amp;` or `**` on screen | Escape once at render |

### 2e. Stress-test procedure (Emil break-ui)
1. **Map every rendered value:** `Field | Source | Type | Limit | Optional?`, including counts, relative times, badges, tooltips, avatars and list length. Flag frontend/backend limit mismatches ("a 50-character input that saves to a 255-character column"). No limit found = "unbounded", which is a finding.
2. **Build a worst-case fixture** beside the demo data, plus Empty / One / Huge (1,000+). Change the data at the boundary (fixture, mock, props), never the markup. Spread failures across rows in one dataset.
3. **Dev-only toggle:** "Demo / Worst case / Empty / One / 1,000 rows", or `?data=worst`. Plain chrome, no animation, never shipped.
4. **Break it** at the real container width, 320px, the widest layout, 200% zoom, dark mode and RTL.
5. **Report before fixing:** `# | Severity (Broken / Ugly / Fragile) | Field | Value | What happens | Fix (file:line)`, then "Decisions for you" (truncate vs wrap, paginate vs virtualise; one line each with a recommendation), then "What held up".
6. Fix on request, re-verify every state including Demo, and keep the fixture as a regression test.

### 2f. Right-to-left details (Apple HIG Right to left)
- **Mirror:** back/next arrows, progress bars, sliders (including the order of their numerals) and icons depicting motion or text direction.
- **Don't mirror:** logos, checkmarks, clocks, photos, or the digits within a number.
- Align paragraphs of 3+ lines by their own language; use one alignment for every item in a list. Increase Arabic or Hebrew ~2pt beside all-caps Latin.
- Implementation [synth]: logical properties, `:dir(rtl)` with an `.icon--directional` class, `<bdi>` or `dir="auto"` for user strings.

## 3. Error prevention (NN/g, Laubheimer: slips vs mistakes, after Norman)
- **Slips** are unconscious errors by people who know what they want, often experts on autopilot. **Mistakes** come from a wrong mental model.
- Prevent slips with:
  - **constraints** (disable impossible dates, limit inputs to valid ranges)
  - **suggestions** (autocomplete, "did you mean")
  - **good defaults** (sensible presets, remembered choices)
  - **forgiving formats**
  - **spacing destructive actions away from frequent ones**
  - **undo**
- Prevent mistakes with clear labels, previews, the system status shown, and conventions.

## 4. Error recovery
- **Never destroy user input**: not on validation error, failed request, reload, navigation away (warn about unsaved changes) or reconnect. Re-apply offline edits on reconnect (Hurff/Raskin, GOV.UK, Baymard, Wallace).
- Error copy says what happened, why if useful, and how to fix it, in plain words. Offer a one-click fix when you can guess ("Did you mean gmail.com?") (NN/g).
- Errors are visible (high-contrast, close to the source), redundant (icon + text + colour) and announced (`aria-live`, focus moves to the summary).
- Scale severity to impact: don't use a red full-page error for a failed avatar upload.

## 5. System status (Nielsen heuristic #1)
- Always show what's happening:
  - saving and saved indicators ("Saving…" with the ellipsis character, then "Saved")
  - sync state
  - background job progress
  - who else is present
- Reflect state in the URL (tabs, filters, pagination, selected item), so refresh, back and share work (Vercel).

## 5a. Saving and restoring (Apple HIG File management, Launching, Multitasking)
- **Autosave by default**, while editing and on blur, close and `visibilitychange`. People should be confident their work is kept unless they cancel or delete it.
- **Show an unsaved-changes dot only when autosave is off;** under autosave it implies an action is needed. Remove "Edited" or "Unsaved" as soon as a save completes.
- **On reload or relaunch, restore granular state:** route, selection, open panels, scroll position, drafts.
- **When the tab is hidden,** pause media and timers that need attention, keep user-started jobs running, and notify on completion only for important jobs the person started.
- Never ask "Resume playback?"; resume from where they left off (Apple HIG Playing video).

## 6. State matrix template
For each component or view, fill this in before coding:

```
View: <name>
| State          | Trigger                    | UI                                   | Copy                            | Actions          |
|----------------|----------------------------|--------------------------------------|---------------------------------|------------------|
| Loading        | first fetch                | skeleton (3 rows, same layout)       | —                               | —                |
| Empty: first   | 0 items, never created     | illustration-free text + primary CTA | "Create your first project"     | Create project   |
| Empty: filter  | 0 results                  | inline message                       | "No projects match 'foo'"       | Clear filters    |
| Partial        | 1 item                     | normal list                          | —                               | —                |
| Ideal          | n items                    | list + bulk bar on selection         | —                               | …                |
| Error          | fetch failed               | inline banner, keep cached data      | "Couldn't load projects. Check your connection and try again." | Retry |
| Offline        | navigator.onLine=false     | banner, edits queued                 | "Changes will sync when online" | —                |
| No permission  | 403                        | explanation                          | "Ask an admin for access"       | Request access   |
```

- **Explode the state combinations.** For each screen, enumerate one variation per relevant control-state combination ("payment fails: does the button reset? where does the message go?") before building (Figma Button states).
- **Rage clicks** in analytics usually mean a broken loading or disabled state (Figma).

## 7. Verification
- [ ] Every data view implements empty (three kinds), loading, partial, error and ideal states.
- [ ] Empty states have a specific next action; no dead ends.
- [ ] Inputs survive errors and reloads.
- [ ] Components tested with extreme content, 200% text and 320px width.
- [ ] Bulk operations report partial failure.
- [ ] Worst-case fixture exists (catalogue in §2a); every field has a truncate/wrap/clamp decision; no numbers or dates truncated.
- [ ] Counts, numbers and dates go through `Intl` formatters; no "1 members", "0 seconds ago" or NaN.
- [ ] Progress is determinate where possible, honestly paced, task-labelled and cancellable.
- [ ] Hard reload: first paint matches the first screen; route, scroll and drafts restored; no dirty dot under autosave.
- [ ] Resizing across breakpoints keeps selection, input and scroll.

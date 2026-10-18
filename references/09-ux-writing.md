# 09 · UX writing and content design

Words are interface. A label that's slightly off makes a perfect layout fail. Sources: Microsoft Writing Style Guide, Mailchimp Content Style Guide, GOV.UK, NN/g, Adam Silver, Apple HIG Writing/Alerts/Sheets/Privacy, Apple Style Guide (2026), Apple WWDC26-290 "Craft clear names", Android Settings/Onboarding, Linear, Figma.

## 1. Voice and tone
- **Voice stays constant; tone adapts to how the reader feels in the moment.** Someone recovering a hacked account needs calm and precision, not jokes (Mailchimp; Apple HIG Writing).
- **Clear beats clever.** If you're unsure whether something is funny, keep a straight face. No forced humour or idioms in core UI; they translate badly and grate on repetition (Mailchimp, NN/g, GOV.UK, Apple HIG Inclusion).
- Warm and crisp: get to the point, use "you", use contractions, including negative ones ("You don't have access") (Microsoft, Mailchimp, Apple Style Guide). GOV.UK avoids negative contractions for clarity; follow the product's own voice.
- **No "we" in system, error or instructional copy.** Write about the user's thing or the product: "Unable to load content", not "We're having trouble loading this content"; "For best results, use an image at least 600 × 600 pixels", not "We recommend…". Reserve "we" for where the company genuinely speaks (emails, policies) (Apple HIG Writing, Apple Style Guide).
- Address people as "you", never "the user". Use possessives sparingly ("Favorites", not "Your favorites") and never switch between "my" and "your" (Apple HIG Writing).
- **No hype:** "Supercharge your workflow!", "Unlock the power of…", "Seamless". Say what it does (Mailchimp, Microsoft).
- Plain words: "buy" not "purchase", "help" not "assist", "about" not "approximately" (GOV.UK). If you can use fewer words, do; read it aloud (Apple HIG Writing).

## 2. Mechanics (defaults)
- **Capitalisation:** follow the project's existing convention first. Otherwise **sentence case** for headings, buttons, menu items, labels and tabs on the web and in SaaS (Microsoft). **Native Apple-platform UI follows HIG title case** for buttons, menus and section headers (alert buttons and slider labels stay sentence case). Pick one style per element type and never use all caps for section headers (Apple HIG Writing; Mailchimp uses title case for page titles and global nav).
- No end punctuation on headings, buttons, labels or single-sentence tooltips.
- **Front-load keywords**; start instructions with the verb ("Enter your email", not "Your email should be entered here").
- Active voice. Sentences of 25 words or fewer (GOV.UK).
- **Numbers:** numerals in UI ("3 projects", "Delete 3 files") for scannability. Spelling out one–nine is Apple's rule for running prose only (Microsoft; Apple Style Guide). "%" in tables and tight UI.
- **Dates and times:** format with the user's locale (`Intl.DateTimeFormat`); always give a time zone for scheduled times ("8:30 a.m. PT" in US English; ISO 8601 dates and 24-hour times with a UTC offset for international or technical audiences). "Daylight saving time", not "savings" (Microsoft; Apple Style Guide).
- No directional language ("in the right sidebar", "click the blue button"), since layouts and abilities vary (Mailchimp).
- **Descriptive link text**: not "click here" or "learn more" alone, but "Learn more about billing" (Mailchimp, WCAG 2.4.4).
- Typography: `…` (the single character), curly quotes, en dash for ranges (2–4) and as a minus sign (–1), non-breaking space before units (Vercel; Apple Style Guide).
- **"…" on a command means more input follows** ("Rename…", "Export…"); not on items that act immediately (Apple HIG Menus).
- No emoji in product UI copy unless it's the brand's established voice.
- **One name per concept everywhere.** Use standard nouns: "Projects should be called projects" (Linear). Don't append "app" to a product name (Linear brand). Reserve built-in concept names so user-created labels can't collide (Linear). Avoid branded jargon labels. Naming new features: `01 §4b` (Apple WWDC26-290).
- **Device vocabulary:** "tap" on touch, "click" on pointer devices, or neutral "select"/"choose" when you can't know. Never "tap on" or "click on" (Apple HIG Offering help, Apple Style Guide).

## 3. Buttons and actions
- **Outcome verbs**: "Create project", "Save changes", "Delete 3 files", "Send invite". "Send" beats "Let's do it!" (Silver, Microsoft, Apple HIG Writing).
- **Never "Submit", "Yes", "No" or "Click here"** (Figma's "Submit" is rejected).
- **"OK"** only on an alert that purely informs (Apple HIG Alerts).
- **"Done"** is allowed as the standard confirm in Apple-style sheets and editors, paired with "Cancel" (or "Back"). Elsewhere prefer an outcome verb (Apple HIG Sheets).
- **The dismiss-without-saving button is always "Cancel".**
- Alert buttons are 1–2 words tied to the alert text ("Reply", "Ignore", "Erase") (Apple HIG Alerts).
- Destructive buttons name the object: "Delete project", not "Delete".
- Paired buttons are parallel: "Discard changes" / "Keep editing".
- **Multi-step flows:** start with "Get started", use one step verb throughout ("Continue" *or* "Next", never both), finish with "Done" (Apple HIG Writing).
- **Sign-in buttons name the method** ("Sign in with passkey", "Continue with Apple"), and only methods available on this device. Don't call app credentials a "passcode" (Apple HIG Managing accounts).
- Loading labels name the task: "Saving…", "Creating project…", "Importing 3 of 12 files…", not a bare "Loading…" (Vercel; Apple HIG Progress indicators).
- **Success copy names the outcome:** "Saved", "Sent", "Invite sent to dana@example.com"; never "Success!" (Figma Button states).

## 4. Error messages (GOV.UK, NN/g, Apple HIG Writing/Alerts)
Formula: **what happened + how to fix it**, in the label's own words, specific to the failure. No "we", no blame, no "please".
- Empty field → an instruction: "Enter your first name".
- Too long → a description: "First name must be 35 characters or less".
- Wrong format → the pattern: "Enter an email address in the correct format, like name@example.com".
- Out of range → the rule: "Date of birth must be in the past".
- **Instruct, don't scold:** "Use only letters for your name", not "Don't use numbers or symbols". "Choose a password with at least 8 characters", not "Password too short". State password rules up front (Apple HIG Writing, Android Onboarding).
- **Never** "Invalid input", "Invalid name", "Error 0x80…" (unless with a human explanation), "Oops!", "Uh-oh", "Please", "Sorry", "!", blame ("You entered…") or ALL CAPS.
- **System errors:** what happened, whether data is safe, what to do now, and a way out: **"Couldn't save changes. Check your connection and try again."** With a local draft: "Couldn't save changes. Your draft is kept on this device. [Try again]".
- If copy can't fix a frequent error, redesign the interaction (Apple HIG Writing).
- Keep a straight face; humour is reserved for very rare, catastrophic outages, if at all (NN/g).

### 4a. Alert titles and text (Apple HIG Alerts)
- The title says what happened, in what context and why, in **≤ 2 lines**. Never "Error" or "Error 329347 occurred".
- Informative text only if it adds value. Don't explain the buttons; if you must reference one, use its exact title and the verb "choose".
- Direct, neutral, never accusatory, and never playing down the severity.

## 5. Empty states, onboarding, tips and permissions
- Say what the place is for and the single next step: "No invoices yet. Invoices you send will appear here. [Create invoice]". Never put crucial information in an empty state; it disappears (Apple HIG Writing).
- No-results: echo the query and offer alternatives: "No results for 'recipts'. Did you mean 'receipts'?"
- Contextual tips at the moment of need beat upfront tutorials and coach-mark tours (NN/g, Hurff, Apple HIG Onboarding). **Tip copy:** 1–2 sentences, direct and action-oriented, no promotion (Apple HIG Offering help). Eligibility and frequency rules: `06 §4`.
- **Tooltips:** start with a verb, ≤ 60–75 characters, don't repeat the control's name, no full stop (Apple HIG Offering help).
- **Permission purpose strings:** one specific, active sentence in sentence case, ending with a period. "The app records during the night to detect snoring sounds." Not "Microphone access is needed for a better experience" (vague, passive) or "Turn on microphone access" (no reason) (Apple HIG Privacy).
- **Pre-permission explainers:** one button, "Continue" or "Next", never "Allow" (Apple HIG Privacy). Timing: `01 §11`.
- Ask for data at the point of need, with the reason and a required/optional marker (Apple SIWA; Baymard: explain why a phone number is needed).

## 6. Microcopy for trust
- Before risky actions, say what will happen and whether it can be undone. Call permanent actions permanent ("This can't be undone, including by support") (Linear).
- Prices, limits and data use stated plainly. Show delivery *dates*, not "3–5 business days" (Baymard).
- Confirmation copy is specific: "Invite sent to dana@example.com".

### 6a. Settings labels (Android Settings; Apple HIG Writing)
- **Most important word first;** describe what the setting does when on; the off state is implied.
- **Neutral, not negative:** "Block calls", not "Don't allow calls" or "Never…".
- **Impersonal nouns** ("Notifications", not "Notify me"); if you must address the user, "you", never "I/me".
- **No generic verbs:** Set, Change, Edit, Modify, Manage, Use, Select, Choose. Don't repeat the section title.
- **Supporting text shows status** ("On for 3 projects"), not a description; omit it when the label suffices.
- The row label that opens a subscreen **matches the subscreen title**. Link directly to a setting instead of describing where it is.

## 7. Verbs and terms (Apple Style Guide)
| Use | Not |
|---|---|
| Turn on / turn off | Enable / disable |
| Unavailable, off, inactive | Disabled (in copy; the code attribute is fine) |
| **Choose** a menu item; **select** an object, checkbox or text | Pick, check |
| Selected / deselected (checkbox, in instructions) | Checked / unchecked |
| **Enter** information (any method); **type** characters; **press** keys | Hit, input |
| Tap / click | Tap on / click on / click and drag |
| Sign in to / sign out of | Sign into / log off |
| For example / that is / and so on | e.g. / i.e. / etc. |
| Rewrite the sentence | and/or |
| Stop, cancel, force quit | Kill |
| Message, alert, or just say what happened | Error message |
| Dialog | Dialog box |

## 8. Inclusive language (Apple Style Guide "Writing inclusively")
- No violent, oppressive or ableist tech terms: kill, hang, master/slave, sanity check, grandfathered. Use allow list / deny list, main branch, list–detail, placeholder/sample instead of "dummy".
- Colours never stand for good or bad (blacklist, white hat). No idioms.
- **Example and fixture names reflect diverse cultures and name orders** (not "John Doe"); see the catalogue in `08 §2a`.
- Use singular "they"; never infer pronouns from a name or appearance.

## 9. Accessibility in copy (Mailchimp "Writing for Accessibility"; Apple VoiceOver criteria)
- Plain language, clear headings in order, descriptive alt text (convey the meaning, not "image of"), and don't use colour words as the only reference.
- Accessible names match visible labels (WCAG 2.5.3 Label in Name).
- **Accessible names are concise** ("New message", not "Press to compose a new message"), make sense out of context, **name the object for repeated or destructive actions** ("Delete Blue T-shirt from cart"), and never include the role or state ("Unsubscribe checkbox"); semantics supply those (Apple VoiceOver criteria).

## 10. Copy lint
Grep UI strings before finishing. Each hit needs a reason or a rewrite. [synth from Apple Style Guide, Apple HIG Writing, Android Settings, GOV.UK, Mailchimp]

```
# Banned or suspect in UI copy (case-insensitive)
\b(please|sorry|oops|uh-oh|whoops)\b
\bwe('re|'ll|'ve)?\b                           # no "we" in system/error copy
\b(enable|disable)d?\b                          # → turn on / turn off / unavailable
\b(click|tap) on\b|\bclick and drag\b|\bhit\b
\b(e\.g\.|i\.e\.|etc\.|and/or)
\b(invalid|error occurred|something went wrong)\b
^(submit|yes|no|ok)$                            # whole button labels; OK only on info alerts
\bclick here\b|^learn more$
\.\.\.                                          # three dots → … (U+2026)
!{1,}\s*$                                       # exclamation marks in UI
\b(kill|whitelist|blacklist|master|slave|dummy|sanity check|grandfathered)\b
\b(supercharge|unlock the power|seamless|revolutionary|effortless)\b
\b(manage|modify|change|edit|set) \w+$          # generic verbs in settings labels
\b(don't allow|never|notify me)\b               # negative/personal settings labels
\bYour (favorites|projects|files)\b             # possessive nav labels
\b1 (members|items|files|projects)\b|0 seconds ago
John Doe|Jane Smith|Lorem ipsum
```

## 11. Verification
- [ ] Every button is an outcome verb in the project's case convention; no Submit / Yes / No; OK only on informational alerts; Done only paired with Cancel.
- [ ] Every error states what happened and the fix; no "we", no blame, no "please", no generic errors.
- [ ] No hype words, no "click here", no directional language.
- [ ] Terminology consistent across UI, routes and docs; new names pass `01 §4b`.
- [ ] Empty states name a next action and hold no crucial information.
- [ ] Multi-step flows: Get started → one step verb → Done.
- [ ] Settings labels lead with the key word, are neutral and impersonal, and use status as supporting text.
- [ ] Permission copy: one specific active sentence; explainer has one "Continue" button.
- [ ] Copy lint (§10) passes or each hit is justified.

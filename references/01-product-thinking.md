# 01 · Product thinking, research, IA and flows

Use this file before building any feature, page or app, and whenever a request is vague. Good UI comes after a correctly framed problem. Polish can make an unvalidated premise look convincing, but "pretty things can lie" (Covert).

## 1. Frame the problem before pixels

**Simple version:** find out what people are really trying to get done, decide what success looks like, and choose the smallest thing that achieves it.

**Professional version:**
- **Business problem vs user need.** Portigal plans research by separating the *inward* business question ("why are trials not converting?") from the *outward* user question ("what are people trying to accomplish in their first week?"). Before building, write both down, plus how you will know you succeeded.
- **Disguised solutions.** A request like "add a calendar" may really mean "I need to see free time." Ask "what's really going wrong?" and "when did you last need this?" Singer's examples: a request for a calendar became "see free spaces", and a six-week permissions project became a one-day warning on the archive button.
- **Opportunity test.** Torres: a good opportunity can be solved in more than one way. If the "need" has only one possible solution, it's a solution in disguise. Generate 2–3 candidate solutions and name the **riskiest assumption** in each.
- **Four risks.** Cagan: check *value* (will they choose to use it?), *usability* (can they?), *feasibility* (can we build it?) and *viability* (does it work for the business?). Building is cheap now; deciding what to build is the job (Cagan & Baxley, 2025).
- **Question the premise.** Soleio, via Julie Zhuo: "Should this exist at all? Does it respect the user's trust?" Before polishing, ask whether the feature serves the user or only the business (the Share Bar example).
- **List the forces the design must fit** (user goals, constraints, conflicting requirements, habits, edge cases) and judge the output against them, not against how polished it looks. "The risk is mistaking generated form for solved problems." (Saarinen, *Output isn't design*, after Alexander)
- **Privacy is a product decision.** Collect only what the feature needs, at the moment it needs it. Prefer scoped, one-time access (a "Current location" button) and passkeys over standing permissions and passwords (Apple HIG Privacy). See §11.

### Questions an agent should ask (at most 2–3, only if they change the build)
1. Who is the primary user, and how often do they use this: daily power use or occasional? (This sets density and learnability.)
2. What is the one task this screen must make easy?
3. Which platform or stack, and is there an existing design system or brand?

4. For open-ended visual work: what mood should it evoke ("warm coffee shop" vs "paper and typography")? Mood is the cheapest high-signal style input (Apple WWDC26-227).

If you can't ask, state your assumptions explicitly at the top of your response and proceed.

For a **new product, site or full redesign**, use the batched intake, function map, brand and reference steps in `00-discovery-brand-references.md` instead of this short list.

## 2. Bound the work (Shape Up)

- **Appetite:** fixed time, variable scope. Decide how much the problem is worth, then design to fit.
- **Explicit lists:** **Out of scope**, **Rabbit holes + patches** (risky unknowns and how you'll sidestep them), **Nice-to-haves cut**.
- **Reject grab-bags** like "redesign X" or "v2.0". Split them into single-problem projects.
- **Right level of abstraction:** wireframes too early over-specify; one-line ideas under-specify. Shape with breadboards and fat-marker sketches.

## 3. Understand users without fake personas

- Indi Young: demographic personas (stock photo, age, income) mislead and duplicate the same user type. Describe users as **thinking styles** in a context: their reasoning, reactions and guiding principles, written in the first person.
- **Four forces of progress** (Moesta & Spiek): *push* of the current situation + *pull* of the new solution, against *anxiety* about the new and the *habit* of the present. Onboarding usually sells pull and ignores anxiety and habit. Reduce anxiety with undo, previews, guarantees and clear data/export policy. Reduce habit with import/migration, familiar patterns and small reversible steps.
- **Testing:** Nielsen's curve shows ~5 users find most usability problems *per round*, so run several small rounds rather than one big one. Test more people when there are distinct user groups (~3–4 each). Fixes can create new problems, so re-test.

## 4. Information architecture

- **Nouns and verbs.** Write the object model as sentences ("An author can publish a post"). Keep a **controlled vocabulary**: words we say and words we don't. Use one term per concept across labels, routes, components and docs. (Covert)
- **Try 2–3 structures** (by object, by task, by status; broad-shallow vs narrow-deep) before choosing. Make your classification rules explicit; ambiguity hides in simplicity. (Covert)
- **Users' mental models, not your org chart or database.** Card sorting reveals groupings: open, closed or hybrid sorts, 30–50 cards, ~15+ participants for qualitative work. Avoid "Misc/Other/More" buckets and jargon or "cute" labels. Front-load key words. (NN/g: Tankala & Sherwin; Cagan & Baxley on Conway's Law)
- **Tree-test your own navigation.** For each core task, phrase it without the label's words and check there is one unambiguous first click (NN/g's *directness*). (Laubheimer)

## 4a. Object model and constrained configuration (Linear docs)

Linear's quality is mostly *product decisions*, not styling. Reproduce the decisions.

- **Write a small, named object model as nested sentences.** "Issues track work; teams own workflows; cycles plan short-term work; projects group issues around a deliverable; initiatives group projects around a goal; views navigate all of it." (Linear Conceptual model)
- **One home, one owner.** An object belongs to exactly one container (an issue to one team, at most one project) and has one owner ("a single lead field to keep ownership of the project clear").
- **Separate data from lenses.** Views, filters and display options organise the work; they "do not change the work itself". Filters choose *which items*; display options choose *how they look* (see `06 §5a`).
- **Constrain customisation.** Let people rename members inside **fixed, ordered categories** (statuses: Backlog → Unstarted → Started → Completed → Canceled). Keep small option sets fixed: Linear has exactly five priorities because "it's easy to get carried away with specificity… diminishing returns". "No value" sorts last.
- **Reserve built-in concept names** (status, priority, assignee, project…) so user-created labels can't collide with them.
- **Quiet defaults.** Nothing selected when a list opens. Out-of-workflow items (Triage, completed, archived) hidden until requested. New items get a sensible default status.
- **Match precision to certainty.** Plans accept fuzzy dates (year, half, quarter, month, day) (Linear Projects).
- **Call permanent actions permanent.** Prefer archive (keeps history) to delete; when delete is irreversible, say so, "including by support" (Linear labels). The forgiveness stack is in `07 §3`.

## 4b. Naming features, settings and nav labels (Apple WWDC26-290)

"Naming is as fundamental to the experience of your app as the layout." Judge every new name against three criteria, weighted by context (a guide, not a rulebook):

| Criterion | Question | Fails when |
|---|---|---|
| **Belongs** | Does it fit the app's voice and its existing nouns? | It collides with a term used elsewhere in the app |
| **Sets the right expectation** | Does it deliver what the reader predicts? | It's clever, technical, or a judgment ("Spending Power" at zero) |
| **Works everywhere** | Does it translate and fit every platform and market? | It's an idiom, pun or untranslatable compound |

- **Trust contexts (money, health, security) favour plain industry-standard terms:** "Balance", not "Spending Power" or "Current Funds".
- **Use a verb when the feature is something people *do*:** "Enhance Dialogue", not "Vocal isolation" (engineering noun).
- **Clever tier or plan names add a learning curve** ("Lightweight/Heavyweight" vs "Basic Access/All Access"). If you choose them anyway, you owe an explanation.
- **Process:** define the audience → Think / Feel / Do brainstorm, one idea per note, unfiltered → cluster into themes → cut vague or untranslatable names → **sentence test** ("Turn on ___", "Search for ___", "Check out ___"; say it aloud).
- **Check each name at zero, empty and error values.** Record rejected names in the design notes.
- Copy-level rules (one name per concept, reserved terms) are in `09 §2`.

## 5. Navigation rules (NN/g menu guidelines, Wroblewski)

- Keep primary navigation **visible**. No hamburger menu on desktop. Hidden navigation measurably reduces engagement ("Obvious always wins").
- Apps: left-side vertical nav for many sections. Mobile: a visible tab bar for 3–5 key sections.
- **Show the current location** with `aria-current="page"`, a visual state and breadcrumbs on deep hierarchies.
- Submenus open on **click**, not hover, with a caret. No multi-level cascading flyouts.
- Labels in plain words; don't replace menu text with icons.
- Navigation contrast must hold; no transparent nav over busy hero images.
- Long pages: consider a sticky header, but un-stick it at small or zoomed viewports (WCAG reflow).
- Code: site navigation is `<nav>` + list of links, **not** `role="menu"` (Pickering).

## 6. Flows: breadboards and wireflows

- **Breadboard** (Singer): Places → Affordances (buttons, fields, copy) → Connections. Write it as text before building:
  ```
  [Projects list] -- "New project" --> [Create dialog: name*, template] -- "Create project" --> [Project page (empty state)]
  ```
- **Wireflow** (NN/g): every hotspot → its resulting state, including feedback, loading, empty, error and success. Then build exactly those states.
- **Journey map** (NN/g, Gibbons) for multi-step, multi-session experiences: one actor, one scenario, phases, actions, mindset, emotional lows, and opportunities with metrics. Design for the lows.
- **Complex/pro applications** (NN/g, Kaplan):
  - live previews and safe experimentation (undo, drafts)
  - progressive disclosure
  - in-context accelerator hints
  - non-linear wizards with back and skip
  - notes and annotations
  - export paths
  - detail on hover or in a side panel
  - salience achieved by removing noise, not adding emphasis

## 7. Success metrics (HEART, Rodden, Hutchinson & Fu, Google)

- Categories: **Happiness, Engagement, Adoption, Retention, Task success**. Pick the ones that matter and say why you're leaving others out.
- Process: **Goals → Signals → Metrics.**
  - Normalise: per user, percentages, ratios.
  - Include failure signals: abandonment, undo, errors, time on task.
- Page views and raw counts are ambiguous; they are not UX success.
- Separate adoption (new users of a feature) from retention (who comes back). Define what "active" means, the denominator and the time window.
- Retention benchmarks vary by business type (Rachitsky & Winters). Treat them as directional.
- Root work in a **product outcome** (a change in customer behaviour) rather than a feature-usage vanity metric (Torres).
- Metrics complement judgement and taste; they don't replace them. Linear explicitly decides through taste and customer insight, without A/B tests.

## 8. Prioritising (when many asks compete)

- **RICE** (McBride, Intercom): (Reach × Impact × Confidence) ÷ Effort. Be honest about confidence (100/80/50%).
- Torres: choose which *opportunity* to pursue without considering effort; rank the *solutions* to it with effort.

## 9. Self-usability test (Krug's script, adapted for agents)

1. **Tour:** from a screenshot of the landing view alone, answer: *whose is this, what is it for, what can I do here, where would I start?* If any answer is unclear, the hierarchy or copy has failed.
2. **Tasks:** for each core task, complete it using navigation only (no search, no URL typing). Note every hesitation, wrong first click or ambiguous label.
3. **Slow-motion walk:** step through each use case start to finish, including errors and empty data, to find holes. (Singer)
4. **Rounds:** fix, then re-run. At least 2 rounds.

## 10. Document the reasoning (case-study quality)

Use `assets/design-notes-template.md`. The structure, from NN/g's portfolio research and Soleio's hiring bar:
- Problem and hypothesis
- Constraints
- Options considered, **including rejected ones and why**
- Decision and trade-offs
- Evidence
- Metric to watch
- What's deliberately not in the design

Lead with the core message and give detail on demand. Own the direction instead of producing a compromise that tries to please everyone. Avoid tidy "everything went well" narratives.

## 11. Onboarding, accounts and permissions are product decisions

Every gate before value costs users. Decide what must happen *before* use and what can happen *in context* (Android Onboarding).

### Sign-in timing
- **Show value before asking for an account or a permission.** "Always follow the value proposition with the action." (Android Onboarding) "Delay sign-in as long as possible." (Apple HIG Managing accounts, Apple SIWA)
- **Require an account only if core functionality needs it.** When you ask, say what it buys them ("Sign in to sync across devices").
- **Commerce: guest checkout first.** Offer account creation on the confirmation page, prefilled from the order; never re-ask for name or email already given (Apple SIWA).
- After sign-in or sign-up, **land people in the product**. Ask for optional data later, at the point it helps, with the reason and a required/optional marker. Declining never blocks a feature (Apple SIWA).
- Prefer passkeys, SSO, biometrics and autofill. After SSO, don't ask for a password or replace a private relay email (Apple SIWA, Android Onboarding).
- **Leaving is as easy as joining:** self-serve account *deletion* (not just deactivation) from Settings in ≤ 2 steps, with a completion date, a notification when done, and what happens to billing (Apple HIG Managing accounts).
- Button and screen rules for sign-in are in `06 §10`.

### Onboarding
- **Learn by doing.** Prefer context-specific tips near the relevant UI over an upfront tour; let people safely perform the action instead of reading about it (Apple HIG Onboarding; NN/g).
- **Postpone non-essential setup and ship good defaults** so most people start immediately. A new user reaches core value with zero required configuration beyond the account (Apple HIG Onboarding).
- If a walkthrough is unavoidable: brief, a preview of real content rather than static slides, a **persistent Skip**, and saved progress so people can resume. Use standard progress indicators, not a decorative illustration per step (Android Onboarding).
- **A skipped tutorial is never re-shown automatically** but stays reachable from Help or Settings (Apple HIG Onboarding).
- No legal walls, downloads or brand splash blocking the first use. A brand moment, if any, belongs at the start of onboarding, not at launch (Apple HIG Launching).

### Permissions
- **Ask at the moment of need, after a related action.** Never at launch unless the product can't work without it, and never as a bulk request (Apple HIG Privacy, Android Onboarding).
- **A pre-permission explainer has exactly one button**, "Continue" or "Next", that opens the system prompt. **Never "Allow"** (a look-alike primes accidental taps), no second action, no incentives, no images of the system alert (Apple HIG Privacy).
- Purpose-string copy is in `09 §5`.

### Feedback and ratings
- Ask for ratings, NPS or feedback **only after a success moment, at a natural break, never mid-task or on first use**, and at least 1–2 weeks apart (Apple HIG Ratings and reviews; Apple's own prompt is capped at 3 per year).

## 12. Prune the edges: attention budget and design debt

- **Software degrades "one useful feature at a time".** Every new capability adds stress to existing surfaces (Aufmann & Heckel, Linear 2026).
- **"Don't compete for attention you haven't earned."** Task content leads; navigation and orientation recede. Visual rules for this are in `02` and `16` (Linear 2026).
- **Settings are a last resort.** Detect what you can and ship defaults the most people would choose; task options live on the screen they affect (Apple HIG Settings, Android Settings; see `06 §9`).
- **Plan resets.** Fast-moving products need a holistic design reset every few years. When asked to restyle one screen of an inconsistent product, flag the system-level debt and propose token, chrome and header fixes, not a one-off (Saarinen, *A design reset*).
- **A good refresh is barely noticed:** "If most people don't immediately notice what changed, that's probably a good sign." Keep a before/after toggle while restyling (Linear 2026).


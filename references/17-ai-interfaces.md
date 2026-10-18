# 17 · AI interfaces (and designing *with* AI)

Two jobs share this file: **designing AI features** (assistants, generated content, AI actions, AI indicators) and **how a coding agent should produce UI** so it isn't "an unrefined, first-pass generated interface".

Sources: Google Design, "Illustrating the Gemini app" (Gemini design team, Anna Sera Garcia); Rose Pozos & Lennard Schmidt, "All That Sparkles Is AI" (Google UX Research); Apple WWDC26-227 "Create UI prototypes using agents in Xcode"; Apple WWDC26-250 "Principles of great design" (Responsibility); Apple WWDC26-290 "Craft clear names"; Karri Saarinen, "Output isn't design" (Linear, 2026); Apple VoiceOver and Reduced Motion criteria. Not yet read: Google PAIR Guidebook, NN/g "The Proliferation and Problem of the Sparkles Icon" (candidates for a later batch). Rules inferred rather than sourced are marked [synth].

## Part A: designing AI features

### 1. Disclose AI, then say what it will do (Pozos & Schmidt)
- Studies with **2,000 participants in 8 countries**: a **single sparkle** reliably signals "AI here". But it carries **no specific meaning** about the action (generate, analyse, edit), and ubiquity erodes it. Google had **nearly 100** sparkle icons in 2024, growing up to 37% per quarter.
- **Use one consistent AI marker across the product, and pair it with a verb label**: "Summarise", "Suggest reply", "Draft with AI". The icon alone isn't a label. Icon-only AI buttons still need an accessible name stating the action.
- **Context determines comprehension:** placement, adjacent text and the app's purpose matter. A mic + sparkle beat a plain mic for signalling AI voice input.
- **Don't put a sparkle on everything.** Mark AI where AI is involved in the result, not every feature that uses ML somewhere.
- Name AI features for what they do for the person, not the technology ("Enhance Dialogue", not "Vocal isolation"). Use a verb when it's something people *do*; in trust contexts (money, health) the plain industry term beats brand expression; names must hold at zero, empty and error values (Apple WWDC26-290).

### 2. Design for verification, not just generation
- Users don't distinguish ML from generative AI: **"I only care if it's right."** What they need is to know AI was involved and to be able to trust or check the output (Pozos & Schmidt).
- **Guard against wrong or unsafe output with previews and confirmations** (Apple WWDC26-250 Responsibility). Concretely [synth from those sources]:
  - **Preview before apply**: generated edits show as a diff or draft the person accepts, edits or discards. Never silently overwrite user content.
  - **Undo is one step away** after applying, labelled by the action ("Undo rewrite").
  - **Show sources** for factual claims and link them; say when there are none.
  - **Editable output**: the person can change the result in place, and regenerate without losing their edits.
  - **Consequential actions** an AI proposes (sending, paying, deleting, publishing) need an explicit human confirmation showing exactly what will happen.
  - Keep the person's input visible and re-usable (redundant entry, WCAG 3.3.7).

### 3. Make the process visible: named AI states (Google Design: Gemini)
- An AI tool keeps changing, so trust comes from **consistency, transparency of process, and softness**. "When a system is hard to approach, the design must be soft": forgive mistakes, anticipate confusion, invite exploration, with clear language and transparent signalling.
- **Visualise process** (listening, thinking, synthesising) so the system feels "alive" rather than "impenetrable". Every animation has a **defined start and end point**, with directional flow that mirrors the person's action ("anticipation, then release"). "Movement in Gemini is not merely decorative; it's an essential guiding element."
- **Define a state model and give each state one consistent treatment** [synth]:

  | State | Show | Controls | Screen reader |
  |---|---|---|---|
  | Idle | AI entry point with verb label | — | Accessible name states the action |
  | Listening (voice) | Distinct listening indicator (Gemini: rippling radial form) | Stop | "Listening" (polite) |
  | Thinking / working | Process indicator; optional step text ("Searching 12 sources") | **Stop / Cancel** | "Working" once, not on every tick |
  | Streaming | Text appears progressively; indicator at the insertion point | Stop | Announce on completion, not per token |
  | Done | Indicator stops; actions (Copy, Retry, Edit, Undo, sources) | — | "Response ready" (polite) |
  | Error | Plain message: what happened + what to do; input preserved | Retry | `role="alert"` only if urgent |
  | Cancelled / partial | Keep the partial output, marked as incomplete | Continue / Retry | — |

- **Motion with no state is decoration.** The indicator stops when its state ends; it never loops while idle.
- Long waits follow `08` loading rules: show something immediately, prefer determinate progress where you can measure it, and always offer Cancel.

### 4. Gradients: an AI-state signal, never decoration (ruling in `conflicts.md`)
- Gemini's foundational visual is the **gradient**: "a trash can is a thing, a gradient is a vibe". Gemini uses gradients **functionally, as context builders and pointers**: "sharp, almost opaque leading edges that diffuse at the tail" direct attention; concentrated vs diffused gradients mark distinct states (Google Design: Gemini).
- **The rule for this skill:** gradients remain banned as decoration (hero backgrounds, buttons, cards, text). A gradient is allowed only when it is (a) an established brand asset, or (b) **one deliberate, consistent signal of an AI/generative state** (listening, thinking, generating, pointing at an AI result). It must:
  1. map to a named state in §3, so removing it would remove information;
  2. be the same treatment everywhere that state appears;
  3. stop when the state ends;
  4. have a **reduced-motion fallback**: a static indicator plus text ("Generating…"), no animated gradient (Apple Reduced Motion criteria; [synth] fallback);
  5. keep text on or near it at full contrast (no text over the animated gradient).
- Never on content cards, never as a generic "AI vibe" wash behind a page, never purple-blue by default because "that's what AI looks like".

### 5. Shape, motion and voice (Google Design: Gemini; Apple; [synth])
- Gemini's foundation shape is the **circle**; buttons and containers echo it with rounded corners. Transferable rule: AI surfaces stay consistent with the product's existing system ("learn once and apply that knowledge repeatedly"). Don't invent a separate visual language for the AI corner of the app.
- **No personified, static assistant characters** (Clippy is Gemini's named contrast). Use honest, product-voiced copy; don't pretend the AI has feelings [synth].
- **Introduce AI features in context**: a tooltip or subtle motion cue at the point of use, animated icons to mark a new feature, never an upfront slideshow (Android Onboarding; Gemini).
- Respect the same accessibility as any UI: live regions polite, **streaming or background updates never move focus or the reading position**, Stop reachable by keyboard, transient banners announced politely (Apple VoiceOver criteria).

### 6. Chat and streaming implementation notes [synth]
- Stop button replaces Send while generating; Esc stops too. Keep the input editable while streaming where the model allows queuing.
- Don't auto-scroll if the person has scrolled up to read; show a "Jump to latest" control instead.
- Reserve space or animate height smoothly to avoid layout shift as text streams; render markdown incrementally without reflowing earlier paragraphs.
- Wrap streamed content in a region with `aria-busy="true"` while streaming and announce once on completion; don't put the stream itself in an `aria-live` region.
- Code blocks: copy button, language label, horizontal scroll inside the block, never page-level.
- Timestamps and model/version labels only where they help verification.

## Part B: designing *with* AI (rules for the coding agent)

### 7. Output isn't design (Saarinen, after Christopher Alexander)
- Design is "the search for a good fit between a form and its context". Context is the full set of forces: needs, technical constraints, conflicting requirements, habits, edge cases. "Bad design appears where those forces remain unresolved."
- AI tools "generate plausible outputs quickly, but they do not necessarily help you understand the underlying problem". Products "look polished… but begin to unravel the moment you actually use them… **The form is there. The fit is not.**"
- **Agent rule [synth from author]:** before producing UI, write down the forces and likely misfits (user goals, constraints, edge cases, conflicting requirements). Judge the output against them, not against how polished it looks. Record them in the design notes.

### 8. The WWDC26-227 prototyping method (Apple: "collaborators, not designers")
"Because it's never been easier to produce an app, designing with intention is critical to standing out." "Do not delegate critical thinking to these tools… you always have final say."
1. **Be specific about features and high-level points up front.** Vague prompts produce an arbitrary layout, **guessed features** nobody asked for (polls, galleries, leaderboards) and **anchoring** on a flawed start that leads to feature creep. Don't invent features; ask.
2. **Give stylistic cues and mood** ("the warm atmosphere of a coffee shop", "the feeling of paper and beautiful typography").
3. **"Most importantly, ask for multiple options."** For open-ended UI, produce **2–3 genuinely divergent directions, each with its own name**, behind a dev-only switcher, separate routes or stories (see `16 §7`).
4. **Remix:** combine the named elements the person likes into named hybrids. Mantra: **"go wide, remix, repeat."** Then refine by simplifying and removing redundancy.
5. **Make it feel lived in.** Keep realistic, audience-plausible sample data in **its own reusable fixtures file** (`fixtures/*.ts`), never lorem ipsum. Name the edge cases explicitly: blank slate, unbounded lists (always show the person's own position plus "show all"), long input (decide truncate vs wrap), missing images. Remove labels that duplicate self-explanatory media.
6. **Tune key moments in phases.** Name each animation phase ("phase 1: transition to detail; phase 2: rows stagger in"), expose its parameters (duration and easing, or spring stiffness/damping/mass, delays, stagger) as tokens, and for key moments build a **dev-only tuning panel** laid out beside the UI, not as a modal. "Nothing beats real-world use."

**Deliverable for an exploratory task:** more than one named direction (or the reason why not), a fixtures file covering empty, long and unbounded cases, and animation phases with their parameters as tokens.

## 9. Anti-patterns
- A sparkle on every button; a bare sparkle with no verb; AI marked inconsistently across screens.
- Gradients, glows or shimmer used as "AI decoration" with no state behind them; animated gradients that ignore reduced motion; text over moving gradients.
- AI output applied directly to user content with no preview, diff or undo; consequential AI actions without confirmation.
- No Stop/Cancel while generating; spinners that loop forever; errors that discard the prompt.
- Auto-scroll that yanks the reader to the bottom; streaming that moves screen-reader focus.
- Personified mascots; fake "typing" delays for effect; unsourced factual claims presented as certain.
- One-shot generated layouts with invented features, lorem fixtures, anchoring on the first output (Apple WWDC26-227).

## 10. Verification
- [ ] One AI marker, used consistently, always paired with a verb label or accessible name.
- [ ] Every AI state (idle, listening, thinking, streaming, done, error, cancelled) has a defined visual, control and announcement.
- [ ] Every gradient or AI animation maps to a state, stops when the state ends, and has a static + text fallback under `prefers-reduced-motion`.
- [ ] Generated changes are previewed, editable and undoable; consequential actions are confirmed; sources shown where facts are claimed.
- [ ] Stop works by click and Esc; prompt input survives errors; streaming doesn't steal focus or scroll.
- [ ] For open-ended UI: forces listed, ≥ 2 named directions explored (or reason given), fixtures cover empty/long/unbounded.

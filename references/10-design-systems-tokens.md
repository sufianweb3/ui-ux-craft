# 10 · Design systems, tokens and component architecture

## 1. Mental model (Brad Frost, Atomic Design)
- Interfaces are built from parts: **atoms** (button, input, label), **molecules** (search field = label + input + button), **organisms** (header, data table), **templates** (page structure with placeholders) and **pages** (templates with real content).
- It's not a linear process. Move between the part and the whole constantly, and test components inside real pages with real content.
- Design for **content extremes** (short and long titles, 1 vs 10 items, empty and first-run, admin variants), not lorem ipsum.
- Many teams organise as Foundations (tokens, type, icons) → Components → Patterns (forms, empty states, tables) → Templates [synth]. Airbnb's DLS treated components more like organisms with clear structure than as tiny atoms. Invest most in the most-repeated component, such as rows and cells (Karri Saarinen).

## 2. Token tiers
```
Primitive (raw scale)  →  Semantic (role/intent)        →  Component (scoped)
--color-gray-900          --color-text-primary             --button-color-text
--color-blue-600          --color-accent                   --button-primary-color-background
--space-4 (16px)          --space-inset-md                 --card-padding
--radius-3 (12px)         --radius-surface                 --dialog-radius
--duration-200            --motion-duration-standard       --popover-duration
```
- **Start with two tiers** (primitive → semantic). Add a component tier only when one semantic role must render differently across components, or while decisions are still settling: "Only add one when you can justify it" (Figma, *Design token architecture*). Curtis and DTCG describe three tiers; this is the conflicts.md default.
- **Components never use primitives or raw values.** They use semantic tokens, optionally through component tokens (Curtis; DTCG Color module's base → alias → component model).
- **No alias chains.** A semantic token references a primitive (or a literal) directly, never another semantic token. Component tokens reference semantic tokens (Figma, *Design tokens*).
- **Keep primitives private.** Hide them from publishing (Figma variables `hiddenFromPublishing`; in code, a `--p-` prefix and a lint rule) so consumers only see decisions (Figma).
- **Start component-local; promote to global once ≥ 3 components share the decision.** Don't globalise prematurely (Curtis).
- Themes and modes (light, dark, high contrast, density, brand) **redefine semantic tokens**. Keep the mode out of token names where values switch by context (Curtis; DTCG Resolver; Figma variable modes).
- **Every semantic colour has four mode values:** light, dark, increased-contrast light, increased-contrast dark (Apple HIG Color; Adopting Liquid Glass). In Figma, that's a collection with four modes; in CSS, the base blocks plus `@media (prefers-contrast: more)` overrides (see `assets/tokens.css`).
- **Motion and preference tokens are tokens too:** durations, curves, and motion *amounts* (scale-from, offset) so that reduced motion can neutralise amounts without deleting fades (`05-motion.md` §5).

## 3. Naming (Nathan Curtis, "Naming Tokens in Design Systems")
Order: **namespace → object → base (category · concept · property) → modifiers (variant · state · scale · mode)**. Use only as many levels as needed. Name by role, `category/role/variant` (`color/text/disabled`), never by appearance (`gray-text`) (Curtis; Figma).
```
--acme-button-primary-color-background-hover
  ns   object variant category property   state
--color-feedback-danger-text
--space-inset-squish-md
```
- **Don't abbreviate** (`background`, not `bg`) in the canonical source. Tailwind-style aliases can map to it.
- **Avoid homonyms:** `type` (typography or kind?) and `text` (colour or content?).
- **Avoid sequential names** (`gray-1`, `gray-2`) that can't accept a step in between. Use ordered numeric steps (100…900) or proportional names (`space-1x`, `space-2x`) (DTCG Color module; Curtis prefers proportional names for space).
- Don't bake the mode into every name (`…-default-on-light`) when values only switch by theme.

## 4. Token format (Design Tokens Community Group, Format 2025.10, first stable version)
- JSON with `$value`, `$type` and `$description`. **Groups** nest tokens. **Aliases** reference other tokens: `"{color.blue.600}"`.
- Types include `color`, `dimension` (units `px` or `rem` only), `fontFamily`, `fontWeight`, `duration`, `cubicBezier`, `number`, and composites (`shadow`, `typography`, `border`, `transition`, `gradient`).
- No circular references. It's a W3C Community Group report, not a W3C Standard; drafts after 2025.10 are previews.
- Pipeline: DTCG JSON → a transformer (Style Dictionary or similar) → CSS custom properties, Tailwind theme, iOS and Android outputs. One source, many platforms.
- **Tokens live in git.** CI runs check → build per platform → test (including the contrast check) → publish. Brand-level changes need human approval and a visual preview; announce changes (changelog, chat, PR comment). Encode the token taxonomy in the agent's rules so it never hard-codes values (Figma).
- **Project file for agents:** if the repo has a `DESIGN.md` (Google Labs DESIGN.md format: YAML tokens + ordered prose sections), read it first and treat its tokens as the system; otherwise start one from `assets/DESIGN.md.template` and lint it with `npx @google/design.md lint DESIGN.md` (Google Labs DESIGN.md spec, alpha).

```json
{
  "color": {
    "gray": { "50": { "$type": "color", "$value": "oklch(0.985 0.002 260)" } },
    "text": { "primary": { "$type": "color", "$value": "{color.gray.950}", "$description": "Body and headings" } }
  },
  "space": { "4": { "$type": "dimension", "$value": { "value": 16, "unit": "px" } } }
}
```

## 5. Component API and architecture
For each component define:
- **Purpose**, and when *not* to use it.
- **Anatomy:** named parts and slots, both required and optional. Components own their structure: built-in dividers toggled by props instead of free-floating `<hr>`s (Saarinen/Airbnb).
- **Variants** (visual intent: primary, secondary, ghost, danger), **sizes** (sm, md, lg mapped to control heights) and **states** (default, hover, active, focus-visible, disabled, loading, selected, invalid).
- **Props named like code** and matching the design tool: `variant`, `size`, `disabled`, `loading`, `iconStart`, `iconEnd`, `asChild`/polymorphic `as`. Booleans are adjectives (`disabled`, `fullWidth`).
- **Accessibility contract:** role, keyboard behaviour, ARIA attributes, focus management, accessible name source.
- **Content guidelines:** label rules, max length, truncation behaviour.
- **Do / Don't examples.**

**Composition over configuration:** prefer composable parts (`<Dialog.Root><Dialog.Trigger/><Dialog.Content/>`) over a mega-component with 30 props. Behaviour primitives (Radix, React Aria, Ariakit) plus your styling is a strong default [synth].

**Avoid variant explosion:** if a variant only differs by one property, use a prop or a token, not a new component.

## 6. Example: Button contract
```
Button
- variant: primary | secondary | ghost | danger     (one primary per view)
- size: sm (28px) | md (36px) | lg (44px touch)
- states: hover (+1 step), active (scale .97), focus-visible (2px ring, 2px offset), disabled (aria-disabled when discoverability matters), loading (spinner + label kept, width stable)
- a11y: native <button type="button|submit">; icon-only requires aria-label; min target 24×24
- content: outcome verb, sentence case, ≤ 3 words typical
- tokens: --button-{variant}-color-{background|text|border}-{state}, --button-radius, --button-padding-inline
```

## 7. Governance (Curtis, "Team Models for Scaling a Design System")
- Models:
  - **Solitary:** one team's system, imposed on others. Doesn't scale.
  - **Centralised:** a dedicated team serves product teams.
  - **Federated:** designers from product teams contribute and decide together.
- Most mature systems combine a central core with federated contribution.
- For an agent working in a codebase: **record decisions centrally**, in token files and component docs. Don't fork components locally. Propose additions to the system instead of one-off overrides.

## 7a. Platform reference scales
When the product targets a platform, adopt its published scales instead of inventing near-copies:
- **Apple:** text styles and control sizes (`02-visual-foundations.md` §5); system colours with four appearances, never hard-coded (`03-color-and-theming.md`); materials (`04-depth-shape-icons.md` §1a). Don't hard-code control metrics; let system size changes flow through (Adopting Liquid Glass).
- **Material 3:** type scale (15 styles + emphasized), roundedness 0/4/8/12/16/20/28/32/48/full, elevation 0/1/3/6/8/12dp, state layers 8/10/10/16% with disabled 38%, breakpoints 600/840/1200/1600 (M3 Type scale, Shape, Elevation, States, Breakpoints). Opt-in tokens in `assets/tokens.css`.
- Always ship a static fallback scheme where colours are dynamic (Material You); otherwise you get the baseline palette (Compose Material 3).
- **Tooling idea:** a dev-toolbar editor for per-token hue/chroma/lightness with JSON export back to the design tool (Linear 2026).
- **Why bother:** in Figma's study, participants with a design system completed a design objective 34% faster (Figma, via *UI design principles*).

## 8. Handoff and multi-platform
- Specs reference tokens, not pixel values. Annotate behaviour, states, edge cases, focus order and screen-reader labels.
- Share tokens and principles across platforms. Let components adapt to native idioms: an iOS switch and an Android switch both use the brand tokens but behave natively.
- Keep tokens identical across code, design tool and docs (Curtis; WCAG 3.2.6 consistent help).

## 9. Verification
- [ ] No hex, rgb or px literals in components (grep), except in token definitions.
- [ ] Every component documents variants, sizes, states and its a11y contract.
- [ ] Theme switch changes only semantic tokens; every colour token has light, dark and both increased-contrast values.
- [ ] No semantic → semantic alias chains; primitives aren't consumed by components.
- [ ] If `DESIGN.md` exists, code tokens match it and it lints clean.
- [ ] Token names follow one convention without abbreviations or homonyms.
- [ ] No duplicate components that differ by a single property.

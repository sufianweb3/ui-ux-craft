# 00 · Discovery, function map, brand and references

Use this file for a **new product, a new site or a full redesign**: anything where the brand, the direction or the feature priorities are not yet settled. For a single component or a fix inside an existing system, skip it and use the project's tokens.

It covers the parts of the workflow that come before `01-product-thinking.md` structure work becomes screens: asking the right questions, ranking every function, creating or extracting a brand, and turning references into specific decisions. It ends in two approval gates so expensive design work is never built on a guessed direction.

## 1. Intake: one batch, with defaults

**Simple:** read everything you were given, then ask only what is missing, all at once, with a suggested answer for each.

**Professional:**
- **Read first.** Files, URLs, screenshots, the repo, an existing DESIGN.md. Never ask for something you can find (Emil, *Agents with Taste*: give the agent context, not guesses).
- **Scale the questions to the job.** A component or a scoped change: SKILL.md's 2–3 question rule applies. A new product or full redesign: one batch of up to ~10, because a wrong brand or audience guess costs days.
- **Offer a default for every question** so the user can skim and confirm in seconds. Use a multiple-choice question tool when the harness has one.
- **Unattended:** don't stall. Take the most reasonable reading, list assumptions at the top of the design brief and continue.

### Question bank (ask only what is missing)

| Area | Questions |
|---|---|
| Product | What is it in one sentence? Platform (web, iOS, Android, desktop)? New build or redesign? Which screens are in scope? |
| Users | Who, and how expert? Context of use (rushed, one-handed on a phone, at a desk all day, daily power use)? Top 3 tasks? Accessibility needs? |
| Business | The one main goal or conversion? How is success measured? Competitors? |
| Brand | Existing guidelines, logo, colours or fonts? Three personality adjectives? The emotion it should evoke (calm, energise, trust, thrill, delight)? (Apple HIG Design principles: *identify the emotion you want to inspire*) |
| References | Sites or apps they like, and **what specifically** about each? Anything they dislike? |
| Content | Is real copy, data and imagery available? Languages, RTL? |
| Constraints | Stack and component library? Light, dark or both? Density (compact pro tool or spacious consumer)? Deadline? |

## 2. Function map: locate every function before drawing

**Simple:** list every feature, how often it's used and how much it matters. Prominence on screen follows from that ranking.

**Professional:** hierarchy on screen comes straight from this table, so a layout drawn without it guesses at what matters (NN/g: define the content hierarchy and the main takeaway before designing).

| Function | User goal | Who | Frequency | Importance | Where it lives |
|---|---|---|---|---|---|
| Create invoice | Get paid | Owner | Daily | High | Dashboard primary action |
| Export CSV | Share data | Accountant | Monthly | Medium | Overflow menu |

Pair it with the object model in `01 §4`: objects (nouns) usually become navigation; actions (verbs) usually become buttons.

**Placement rules:**
- **Frequent and important:** most prominent, top-leading or in thumb reach, one click away (Fitts, Apple HIG Layout reading order).
- **Important but rare** (billing, delete account): findable, not prominent; protect destructive ones (`06`, `07 §3`).
- **Rare and minor:** progressive disclosure: settings, overflow, "Advanced" (Apple HIG Layout, Figma UI design principles).
- **Pareto:** a few functions carry most use. Spend design effort and testing there (Laws of UX).
- Frequency also sets motion: the frequency gate in SKILL.md rule 18 reads its numbers from this column.

## 3. Gate 1: design brief

After the function map and `01` structure work (IA, navigation, flows, screen list), present one brief and get approval or changes before any visual work. Skip the gate for small scoped tasks; in unattended runs, write assumptions and continue.

```
# Design brief: <product>
Assumptions: <only if unattended or unanswered>
One-liner:
Users and context:
Primary goal / success signal:
Function map: <table>
Sitemap and navigation pattern:
Top flows: <task: step > step > success | error paths>
Screen list: <screen: purpose | one primary action | blocks in order | states>
Out of scope:
Open questions:
```

## 4. Brand system

### 4a. Brand guidelines exist: extract and obey
- Turn colours, fonts, logo rules, tone and existing components into tokens (`10`, `assets/tokens.css`) and record them in DESIGN.md.
- **Contrast-check every brand colour** in its intended roles (`03 §2`). If one fails as text or button fill, keep it for large surfaces and illustration, and propose an accessible variant for text and controls. Flag it; never silently change a brand.
- Brand lives in content and a few hero moments, not on every control (`03 §1`, Apple WWDC26-251).

### 4b. No guidelines: create a small, defensible brand

**Colour process**
1. **Start in grayscale.** Get hierarchy working with lightness alone; colour later reinforces it (Figma *types of colour palettes*; Refactoring UI).
2. **Pick one primary hue** from the personality and emotion in the intake. Check cultural meaning for global audiences (red is danger in some places, luck or rising prices in others; Apple HIG Color).
3. **Choose a palette structure for brand surfaces** (marketing, illustration, hero moments). Product chrome stays neutral plus one accent either way (`03 §1`).

   | Type | Feel | Typical fit |
   |---|---|---|
   | Monochromatic | Clean, calm, rarely clashes | Productivity, finance, health dashboards |
   | Analogous | Natural, soft | Wellness, lifestyle, natural products |
   | Complementary | Bold, high contrast | Attention-grabbing marketing |
   | Split complementary | Contrast that's easier to balance | Creative tools, education |
   | Triadic | Vibrant, playful (let one colour dominate) | Kids, games, creative platforms |

   (Figma, *types of colour palettes*)
4. **Build ramps in OKLCH** per `03 §3`: a neutral ramp tinted very slightly toward the primary's temperature, the accent ramp and the four semantic ramps.
5. **Distribute roughly 60-30-10:** ~60% dominant (neutral surfaces), ~30% secondary (structure such as sidebars and cards), ~10% accent for the few things that must stand out (Figma UI design principles). A starting proportion, not a quota.
6. **Muted for area, saturated for points.** Large areas use muted tones; saturation is a spotlight for small elements (NN/g *why does design look good*; Android Colour).
7. **Supply light, dark and increased-contrast values for every role** (`03 §7`, Apple HIG Color).
8. **Run `assets/check-contrast.py`** on the token pairs before showing the direction.

**Typography**
- **One family is enough for most products; at most two** (display plus text). Pair by contrast (serif display with sans text) or use one superfamily. Similar x-heights make pairs sit together (NN/g, Apple HIG Typography: minimise typefaces).
- **Choose by personality, not habit.** Inter and `system-ui` suit dense product UI where neutrality is the point; on brand and marketing surfaces they read as the default. Free options with character [synth]:
  - Sans: Geist, Manrope, Plus Jakarta Sans, DM Sans, Satoshi, General Sans
  - Serif display: Fraunces, Instrument Serif, Newsreader, Playfair Display
  - Mono: JetBrains Mono, Geist Mono, IBM Plex Mono
  - Sources: Google Fonts, Fontshare. Check the licence; never ship SF fonts on the web (`02 §5`).
- Scale, line height, measure and tracking follow `02 §5`. Marketing and editorial can use a larger ratio (1.333–1.5) than product UI.

**Other tokens:** spacing, radius, elevation and motion come from `assets/tokens.css`. Pick one **radius personality** (sharp 0–4px serious or editorial, 6–12px friendly SaaS, 16px+ soft consumer) and keep it across the product.

## 5. References

**Simple:** use the user's references first. If they have none, collect 5 to 8 good ones, write down exactly what to borrow and what to avoid, then agree a direction.

### 5a. Ask first
The user's references beat yours. Ask what exactly they like about each: "I like Linear" can mean the density, the dark palette or the keyboard speed.

### 5b. If they have none, collect 5–8
Use a browser or web fetch. Grade sources by how much they can be trusted as evidence of shipped, working design:

| Source | Use for | Trust |
|---|---|---|
| Live products in the same category, plus best-in-class adjacent products | Patterns that survive real users and data | High |
| Mobbin (mobbin.com), Refero (refero.design) | Real app screens and flows: onboarding, settings, dashboards, tables, empty states | High. Free browsing is limited; never depend on paid access |
| Awwwards, Godly (godly.website), Land-book, Minimal Gallery, Lapa Ninja, SiteInspire | Marketing sites: art direction, type, motion, scroll | High for marketing, low for product UI |
| Apple HIG, Material 3 | Platform conventions, sizes, components | Authoritative for native apps (`13`) |
| Dribbble, Behance, Pinterest | Mood and colour only | Low: many shots are unshipped concepts that break with real content. Never cite as a pattern source |

### 5c. Study each one, in words
Write answers, not just screenshots:
- **Hierarchy:** where does the eye land first, and why?
- **Typography:** which faces, sizes and weights? Why do they work?
- **Colour:** which colours are used, and which are deliberately absent?
- **Spacing and layout:** why is this section separated from that one? Why is content placed here, not centred?
- **Interaction and motion:** what happens on hover, press, scroll and wait? What moves and what stays still?
- **Personality:** what makes it recognisable rather than generic?
- **Restraint:** what did the designer leave out?

(Emil, *Developing Taste*: ask why you respond to something, and dissect products rather than just using them.)

### 5d. Turn references into decisions
- **Steal list:** specific decisions, each with a reason. "Linear: 13px UI labels at weight 500, because the product is dense and used all day."
- **Avoid list:** what doesn't fit these users or this brand.
- **Borrow by layer:** structure from one reference, type from another, motion from a third. Never copy a whole layout, logo, copy, imagery or brand identity.
- **Direction statement** (2–3 sentences) plus **one signature element**: a single distinctive motif that makes the product recognisable (an unusual type pairing, a shape language, one colour used boldly in one place, a memorable interaction). One is enough; several is noise. It must pass the anti-slop table, not be a gradient-and-glow default.

> Example: "Calm, editorial finance tool for freelancers. Warm off-white surfaces, ink-navy text, one saffron accent reserved for money-in moments. Signature: large serif numerals for every amount."

## 6. Gate 2: direction

Present the token sheet, the reference board with steal and avoid lists and the direction statement. If you can render, include a small style tile: type scale, palette swatches, a button, an input and a card, in light and dark. Get approval before building full screens, because changing direction after screens exist is expensive.

The approved direction feeds **Explore** (SKILL.md Step 2b): named variants vary layout, density and interaction model within it, not the brand.

## 7. UX laws to apply while structuring

The ones most often useful at this stage (Laws of UX; NN/g). Doherty and response times are in `07`.

| Law | Apply as |
|---|---|
| Hick's | Fewer choices per decision; stage complex choices; highlight a recommended option |
| Fitts's | Big, close targets for frequent actions; thumb zones on touch (edge claims for web in `conflicts.md` #15) |
| Jakob's | Follow conventions people know; spend novelty only where it adds value |
| Miller's / working memory | Chunk into groups; keep needed information visible across steps |
| Goal-gradient | Show progress and steps remaining |
| Peak-end | Design one memorable high point and a satisfying end state |
| Von Restorff | The one element that differs gets noticed; reserve it for the key action |
| Serial position | Put key items first or last in lists and menus |
| Postel's | Accept messy input formats, store and show clean ones |
| Zeigarnik | Resume prompts for unfinished tasks (drafts, setup, carts) |
| Paradox of the active user | People skip tutorials; teach in context with empty states and hints |
| Tesler's | Move unavoidable complexity onto the system: smart defaults, inference, autofill |

## 8. Checklist
- [ ] Questions batched, each with a default; nothing asked that the inputs already answered
- [ ] Function map covers every function with frequency and importance
- [ ] Gate 1 brief approved (or assumptions written for unattended runs)
- [ ] Brand extracted and contrast-checked, or created with OKLCH ramps and light, dark and increased-contrast values
- [ ] At most 2 typefaces, chosen for personality, licence checked
- [ ] References studied in words, with steal and avoid lists; nothing copied wholesale; Dribbble used for mood only
- [ ] Direction statement plus one signature element that passes anti-slop
- [ ] Gate 2 direction approved before full screens

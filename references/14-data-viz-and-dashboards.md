# 14 · Data visualisation and dashboards

Sources: Stephen Few, "Common Pitfalls in Dashboard Design"; Lisa Charlotte Muth (Datawrapper), "Why not to use two axes" (2018) and the July 2026 update; Cole Nussbaumer Knaflic, "Be gone, dual y-axis!"; Edward Tufte's concepts; Apple HIG "Charting data" (pattern) and "Charts" (component).

## 1. What a dashboard is (Few)
- A **single screen** that someone reads in three steps: **overview → focus on what needs attention → drill down for detail**.
- It answers specific questions. Before building, list the top 3–5 questions the dashboard must answer in about 5 seconds [synth]. Then design for those questions.
- **Chart only when there's a takeaway.** A chart is visually prominent; data that only needs to be *provided* belongs in a sortable, searchable list or table (Apple HIG Charting data).

## 2. Dashboard rules (Few's 13 pitfalls, restated as rules)
1. Fit on one screen. Don't make people scroll or page to see the overview.
2. **Every number needs context:** a target, the prior period, a trend, or a status. A big number alone is meaningless.
3. Use decision-level precision ("$1.2M", not "$1,234,567.89").
4. Express variance directly (%, or deviation around a zero line) instead of making people subtract.
5. Choose the right chart:
   - bars for comparing categories, parts of a whole, or sums per period
   - lines for change over time and trend (slope)
   - points/dots for relationships, outliers, clusters and distributions; combine (points on a line) only when it adds clarity (Apple HIG Charts)
   - Prefer common types. If you must use a novel encoding, teach it (Apple's Activity rings animate one at a time to map ring → metric) (Apple HIG Charting data).
   - Avoid pies and donuts when you need labels to read them, gauges and speedometers, traffic-light skeuomorphism, and 3D charts.
6. **Bars start at zero.** Truncated bar axes lie. **Line charts may use a non-zero baseline** when the meaningful differences sit far from zero (resting vs active heart rate). This refines Few, who targets bars. Use a **fixed axis range** when the bounds mean something (0–100%, battery) and a dynamic range otherwise, so marks fill the plot (Apple HIG Charts).
7. Don't add variety for its own sake. Repeating the same chart type is fine, and consistency speeds comparison. **Charts of the same dataset, or with a similar purpose, keep the same type, colours, annotations and layout** (small → expanded views look identical) (Apple HIG Charting data).
8. Place items for comparison side by side. Arrange by importance: the most important goes top-left.
9. **Subdued, neutral palette plus one highlight colour.** Colour encodes meaning, never decoration. "When everything is visually prominent, nothing stands out."
10. No decorative clutter: backgrounds, borders, gradients, ornaments, icons on KPI cards (NN/g Kaplan also warns against decorative icons on dashboards).
11. Make the most important information visually salient through position and size, not effects.
12. Make drill-down obvious and consistent. Reveal detail progressively: macro (totals, averages) → useful subsets → individual points (Apple HIG Charting data).

## 3. Honest, readable charts
- **Headline states the takeaway.** Every chart gets a title (and optional subtitle) that summarises the main message before people look ("Chance of light rain in the next hour"). The headline doesn't replace accessibility labels (Apple HIG Charts).
- **Dual axes:**
  - The default is to avoid them, because arbitrary scales create fake correlations and crossovers. Use small multiples, an indexed chart (both series rebased to 100), or one series plus annotation instead (Muth 2018; Knaflic).
  - Datawrapper's 2026 update allows dual axes for numerate audiences when the series have different units (°C/°F, Pareto charts), the scales are aligned, the zero is shared, there are no fake crossovers, axis labels are coloured to match their series, and units appear in the title, legend or values.
- **Ticks use familiar sequences** (0, 5, 10; not 1, 6, 11). Tailor grid-line density to the task; interactive charts need fewer, lighter grid lines (Apple HIG Charts).
- **Separators between contiguous colour areas:** 1–2px surface-colour gaps between stacked segments (Apple HIG Charts).
- **Alignment:** align the chart's leading edge with surrounding content; consider putting the Y axis on the trailing side so tick labels don't protrude past the leading edge (Apple HIG Charts).
- **Compact widths:** maximise plot width, keep Y labels short, put units in the title, and place long category labels inside the plot if they don't obscure data (Apple HIG Charts).
- **Size to function:** a small chart is a glanceable preview of a larger one; a large chart has room for labels, annotations and scope changes (Apple HIG Charting data).
- **Tufte's concepts:**
  - Maximise the **data-ink ratio** by removing non-data ink.
  - Avoid **chartjunk**.
  - Use **small multiples** for comparison.
  - **Graphical integrity:** show data variation, not design variation.
- **Plot the real data first**, before committing to a chart design (Knaflic).
- Label directly on the chart where possible instead of using a separate legend [synth; consistent with data-ink guidance].
- **Never colour alone:** pair colour with shape or pattern (Apple Health uses two point shapes for blood pressure), labels or position. Order series colours the same as the legend. Chart marks need 3:1 contrast against the background (Few; WCAG 1.4.1, 1.4.11; Apple Differentiate Without Color criteria). Consider letting people customise chart colours (Apple HIG Accessibility).

## 4. Interaction
- **Interaction is optional, never required to see critical information.** No key number hidden behind hover or scrub (Apple HIG Charts).
- **The whole plot area is the hit target:** people scrub anywhere instead of tapping tiny marks; a scrubbing indicator shows the value (Apple HIG Charts).
- Hover crosshair with values, brushing to zoom, filters that update every tile consistently, and filter state kept in the URL.
- **Keyboard:** focus moves along the X axis, or between subsets of values for large datasets; arrow keys step, with an `aria-live` readout [synth web mapping of Apple HIG Charts].
- **Changes:** animate mark and axis changes *and* announce them non-visually for screen-reader and reduced-motion users (Apple HIG Charts).
- Show time zones and data freshness ("Updated 2 min ago").

## 5. Accessibility and labels (Apple HIG Charts; Apple VoiceOver criteria)
- Give each chart a **chart overview** (type, what each axis represents, bounds) plus per-mark or per-group labels depending on purpose (summarise segments for an elevation profile; label each bar for daily steps). A small chart used as a button gets one high-level label.
- **Label writing rules:**
  - context first, then value
  - **exact values, no subjective words** ("rapidly", "almost")
  - **unambiguous formats** ("June 6", not "6/6"; "60 minutes", not "60m")
  - describe what each series *represents*, not its colour
  - consistent axis order
- **Hide visible axis and tick text from assistive tech** when marks carry labels, so values aren't read twice.
- Web: static SVG `role="img"` + `aria-labelledby` pointing at the title/summary; or `<figure>` + `<figcaption>` plus a visually hidden data table. Interactive charts: a focusable plot with arrow-key navigation; axis `<text>` `aria-hidden="true"` [synth].
- Make tooltips reachable by keyboard; never show information in a hover tooltip alone.

## 6. Implementation notes
- **Numbers:** numerals, tabular figures, right-aligned in tables, locale formatting (`Intl.NumberFormat`), units included. Never truncate numbers, amounts or dates (Emil break-ui).
- **Empty and partial data:** design a chart with 0, 1 and 2 points so it doesn't look broken (Hurff). Test null/NaN, negative values, one huge outlier and 1,000+ points (Emil break-ui).
- **Loading:** use skeleton axes or frames, not a blank card with a spinner.

## 7. Verification
- [ ] The overview fits on one screen and answers the stated questions.
- [ ] Every chart has a headline stating its takeaway; plain lookup data is a table, not a chart.
- [ ] Every KPI has a comparison (target, prior period, trend).
- [ ] Bars start at zero; a non-zero line baseline is deliberate; fixed ranges where bounds mean something.
- [ ] Ticks are round sequences; stacked segments have separators; no 3D charts, gauges or label-dependent pies.
- [ ] Neutral palette plus one highlight; no rainbow default; usable in grayscale; colour order matches the legend.
- [ ] Sibling charts share type, palette and annotations.
- [ ] No dual axis unless every safeguard is met.
- [ ] Nothing critical requires hover or scrub; scrub works anywhere in the plot.
- [ ] Each chart has a text alternative with exact, unambiguous values; keyboard can reach values; axis labels aren't read twice.

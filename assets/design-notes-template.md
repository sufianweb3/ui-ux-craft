# Design notes: <feature / screen>

**Problem.** <Who> needs to <job> so they can <outcome>. Evidence: <user quote, data, bug report, or "assumption, unvalidated">.

**Success looks like.** Goal → signal → metric (HEART), e.g. Task success → "created first project" → % of new workspaces creating a project in 24h. Plus one qualitative check.

**Constraints.** Platform, existing design system, technical limits, deadline / appetite.

**Out of scope.** <deliberately not doing, and why>

**Structure.** Object model (nouns + verbs) and breadboard:
```
[Place] -- affordance --> [Place]
```

**Options considered.**
| Option | Pros | Cons | Verdict |
|---|---|---|---|
| A | | | Chosen |
| B | | | Rejected because … |

**Decision and trade-offs.** <what we gave up and why it's acceptable>

**States covered.** Ideal · Empty (first use / cleared / no results) · Loading · Partial · Error · Offline · No permission

**Accessibility.** Contrast checked · keyboard path · focus management · targets · reduced motion · reflow 320px / 200% text · screen-reader labels

**Risks and rabbit holes.** <unknowns and the patch for each>

**Open questions for the user.** <only what changes the build>

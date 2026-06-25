---
name: competitive-analysis
description: >-
  Compares ACC.org structure, patterns, and experience to peer medical
  associations using the ACC redesign competitive landscape. Use when
  benchmarking competitors (AHA, AMA, ESC, HFSA, HRS, AAN, ACS), heuristic
  reviews, redesign discovery, or asking how peers handle membership, products,
  or readability.
disable-model-invocation: false
---

# Competitive Analysis

Understand **how peer associations structure sites and experiences** so ACC refactors align with modern medical-association patterns — not ACC legacy habits.

Source: [Competitive Analysis — ACC Redesign](https://acc-style.github.io/BrainDump/work/acc/projects/acc-redesign/discovery/competitive-analysis.html)

**Pair with:** [readability](../readability/SKILL.md) (copy scores) · [refactor](../refactor/SKILL.md) (structure) · [acc-ux-designer](../acc-ux-designer/SKILL.md) (UI)

## Process outline

```
1. Identify peer org and page type (membership, product, journal, etc.)
2. Select comparison lens (see lenses below)
3. Capture raw notes — structure, nav, hero, CTAs, word count
4. Map trends — what do leaders do consistently?
5. Translate — specific recommendations for ACC prototype
```

## Competitor landscape

### Direct membership competitors (cardiology / cardiovascular)

| Org | Code | Notes |
|-----|------|-------|
| American Heart Association | AHA | Public-facing, emotionally engaging; strong readability |
| European Society of Cardiology | ESC | Highly scannable, concise copy |
| American Medical Association | AMA | Excellent readability; actionable tone |
| Heart Failure Society of America | HFSA | Approachable pro + patient balance |
| Heart Rhythm Society | HRS | Strong scannability; shorten sentences |

### Adjacent professional associations (similar offerings)

| Org | Code | Notes |
|-----|------|-------|
| American Academy of Neurology | AAN | Top readability scores; crisp tone |
| American College of Surgeons | ACS | Professional; heavier for newcomers |

### Internal / related ACC properties

| Property | Role |
|----------|------|
| **JACC** | Journal — separate brand/experience from acc.org |
| ACC main site | Membership, education, guidelines hub |

### Not in core set (context only)

ABIM, APA, ASH, ASCO, ISHLT — referenced in discovery but not primary benchmarks.

Full list: [competitors.md](competitors.md)

## Comparison lenses

| Lens | Repo / doc reference | Use when |
|------|----------------------|----------|
| **Readability** | [readability/benchmarks.md](../readability/benchmarks.md) | Copy audits — ACC scored 22 vs leaders 37 |
| **Brand & personality** | `__ui_playground/Charts-Quadrant-Brand.html` | Tone, audience focus |
| **Member experience** | `__ui_playground/Charts-Quadrant-Member.html` | Login, join, member hub flows |
| **Journal vs main site** | `__ui_playground/Charts-Quadrant-Journal.html` | JACC vs acc.org split |
| **Strategic emphasis** | `__ui_playground/Charts-Radial-Select-Effort.html` | Initiative prioritization |
| **UI patterns** | Discovery UI notes (article teasers, primary nav) | Component-level steals |

## What to capture per competitor page

```markdown
## [Org] — [Page type] — [URL]

### Structure
- Hero type (anchor / section / product / other)
- Nav depth, breadcrumbs, sidebar?
- Chunk pattern (cards, tabs, hub CTAs)

### Copy
- Approx word count
- Reading level impression
- CTA labels (verbatim)

### Notable wins
- …

### ACC gap
- …
```

## Trends from readability study

Leaders (AMA, AAN, HFSA) share:

- **Even scores** across all 8 readability criteria — not just good layout
- **~500–700 words** on comparable pages vs ACC ~1,470
- **Welcoming professional tone** — expert but not academic
- **Clear CTAs** with action verbs

ACC gaps to close in prototypes:

- Reduce academic/insider tone on **initiatives and products**
- Shorten sentences and define jargon ([readability](../readability/SKILL.md))
- Keep refactor chunking ([refactor](../refactor/SKILL.md)) — ACC already scores 4 on scannability

## Heuristic references

Discovery cites Nielsen Norman Group:

- [How to conduct a heuristic evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/)
- [Ten usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)

Use for UX reviews alongside readability scoring.

## Login & membership patterns

From discovery notes: peers often connect **login to membership** explicitly ("Member Login"). Compare when refactoring member flows — see `_member_section_prototype/`.

## Output for ACC work

When analysis completes, deliver:

1. **Comparison table** — org × structure × word count × standout pattern
2. **Steal list** — 3–5 patterns to prototype in `_collections/__prototypes/`
3. **ACC avoid list** — legacy habits peers don't use
4. **Link to refactor/readability** — structural + copy changes for implementation

## Additional resources

- [competitors.md](competitors.md) — full org list and categories
- [ACC redesign discovery hub](https://acc-style.github.io/BrainDump/work/acc/projects/acc-redesign/discovery/competitive-analysis.html)

# Competitor Reference List

Source: [Competitive Analysis](https://acc-style.github.io/BrainDump/work/acc/projects/acc-redesign/discovery/competitive-analysis.html)

## Tier 1 — Primary benchmarks (readability scored)

Use for copy and structure comparisons on membership, education, and professional marketing pages.

| Org | Full name | Readability | Words (sample) | Strength |
|-----|-----------|-------------|----------------|----------|
| AMA | American Medical Association | 37 | 930 | Actionable, accessible |
| AAN | American Academy of Neurology | 37 | 530 | Crisp, welcoming |
| HFSA | Heart Failure Society of America | 37 | 570 | Pro + patient balance |
| AHA | American Heart Association | 35 | 870 | Engaging, public-facing |
| ESC | European Society of Cardiology | 35 | 460 | Concise, scannable |
| HRS | Heart Rhythm Society | 31 | — | Strong scan; shorten sentences |
| ACS | American College of Surgeons | 29 | 660 | Professional, dense for newcomers |
| **ACC** | **American College of Cardiology** | **22** | **1,470** | Technical, insider-focused |

Scores: [readability/benchmarks.md](../readability/benchmarks.md)

## Tier 2 — Landscape (not always scored)

| Org | Relationship to ACC |
|-----|---------------------|
| AHA Professional | AHA membership / professional subsite |
| JACC | Internal — journal vs main site tension |

## Tier 3 — Not in core competitive set

Tracked in discovery; use for niche comparisons only.

| Org | Domain |
|-----|--------|
| ABIM | Board certification (partner, not competitor) |
| APA | American Psychological Association |
| ASH | American Society of Hematology |
| ASCO | American Society of Clinical Oncology |
| ISHLT | Heart and lung transplantation |

## When to compare which peer

| ACC page you're building | Compare first |
|--------------------------|---------------|
| Membership / Join Us | AMA, AAN, AHA, ACS |
| Disease / patient education hub | HFSA, AHA |
| International professional audience | ESC |
| Arrhythmia / EP products | HRS |
| Heart failure programs | HFSA |
| Broad medical society tone | AMA, AAN |
| Concise product marketing | ESC, AAN |

## Discovery artifacts in this repo

| Chart | Path |
|-------|------|
| Brand quadrant | `__ui_playground/Charts-Quadrant-Brand.html` |
| Member experience | `__ui_playground/Charts-Quadrant-Member.html` |
| Journal vs main | `__ui_playground/Charts-Quadrant-Journal.html` |
| Strategic emphasis | `__ui_playground/Charts-Radial-Select-Effort.html` |

## Analysis workflow reminder

1. Pick **2–3 peers** from table above (not all eight)
2. Same **page type** (apples to apples — membership hub vs membership hub)
3. Capture structure + copy + word count
4. Feed findings into [refactor](../refactor/SKILL.md) + [readability](../readability/SKILL.md)

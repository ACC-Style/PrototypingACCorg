---
name: readability
description: >-
  Evaluates and improves ACC web copy using the redesign readability checklist
  and competitive benchmarks. Scores reading level, sentence length, jargon,
  scannability, and CTA clarity; rewrites refactored content for product pages,
  brochureware, and initiatives. Use when editing page copy, readability audits,
  competitive writing standards, or improving refactored HTML text output.
disable-model-invocation: false
---

# Readability & Web Writing

Improve **product pages, brochureware, and initiatives** — not clinical science reference content, which may stay technical by design.

Official sources:
- [Readability Checklist & Rating Scale](https://acc-style.github.io/BrainDump/work/acc/projects/acc-redesign/discovery/rules/readability-evaluation-checklist-and-rating-scale.html)
- [Competitive Readability Scoring](https://acc-style.github.io/BrainDump/work/acc/projects/acc-redesign/discovery/data/readability-comparison-scoring.html)

**Pair with:** [refactor](../refactor/SKILL.md) (structure) · [competitive-analysis](../competitive-analysis/SKILL.md) (competitor patterns)

## Scope

| In scope | Out of scope |
|----------|----------------|
| Product pages, CMP/MOC hubs, membership, education marketing | Guideline body text, deep clinical reference |
| Brochureware, initiative landing pages | Journal article science (JACC) |
| Refactored chunk copy (headlines, cards, CTAs) | Content where medical precision overrides plain language |

## ACC benchmark context

ACC ranked **8th of 8** peers in competitive readability (**22/40** — average; leaders score **37**).

| ACC weak spot | Score | Peer leaders (AMA, AAN, HFSA) |
|---------------|-------|-------------------------------|
| Reading level | 2 | 4 |
| Vocabulary | 2 | 4 |
| Jargon | 2 | 4 |
| Sentence length | 2 | 5 |
| Scannability | 4 | 5 |
| CTA clarity | 4 | 5 |

ACC also leads in **word count** (~1,470 words vs ESC ~460). Refactor structure **and** cut copy.

Full benchmark table: [benchmarks.md](benchmarks.md)

## Workflow

```
Readability pass:
- [ ] 1. Scope — confirm page type is in scope (not clinical science)
- [ ] 2. Score — rate 8 criteria 1–5 (see checklist.md)
- [ ] 3. Diagnose — note total band + lowest criteria
- [ ] 4. Refactor structure — run refactor skill if not done
- [ ] 5. Rewrite — apply rewrite-guide.md per chunk
- [ ] 6. Re-score — target 29+ (Good) for initiatives; 35+ for key product hubs
- [ ] 7. Summarize — stakeholder table with before/after scores
```

## Quick evaluation (8 criteria × 1–5)

See [checklist.md](checklist.md) for full scale definitions.

| # | Criterion | Target for ACC initiatives |
|---|-----------|----------------------------|
| 1 | Reading level | 8th–10th grade (score 4) |
| 2 | Sentence length | 15–20 words avg. (score 4) |
| 3 | Paragraph density | 2–4 sentences; brief blocks (score 4–5) |
| 4 | Vocabulary | Mostly simple; clinical terms when needed (score 4) |
| 5 | Jargon | Define on first use; `<abbr>` for acronyms (score 4) |
| 6 | Sentence structure | Active voice (score 4–5) |
| 7 | Scannability | Headings, lists, chunks — leverage refactor UI (score 4–5) |
| 8 | CTA clarity | Action verb + outcome; one job per button (score 5) |

**Total score bands:**

| Score | Band |
|-------|------|
| 7–14 | Needs significant improvement |
| 15–21 | Below average — requires revision |
| 22–28 | Average — minor edits (ACC's current zone) |
| 29–35 | Good — minor tweaks |
| 36–40 | Excellent — peer-leading |

## Rewriting refactored output

After [refactor](../refactor/SKILL.md) chunks content, apply [rewrite-guide.md](rewrite-guide.md):

1. **Cut first** — aim for peer word-count range (500–700 words per major view; hub intros <150 words)
2. **Lead with outcome** — what the user gets, not organizational history
3. **One idea per chunk** — card title = benefit; body = one sentence
4. **Define then use** — MOC, CMP, SAP, CME spelled out once with `<abbr title="…">`
5. **Active verbs** — "Enroll in CMP" not "Enrollment can be completed by members"
6. **CTA pairs** — button label matches destination action; no vague "Learn More" without context in surrounding heading

## Output format for audits

```markdown
## Readability audit: [Page name]

**Scope:** Product / Initiative / Brochureware
**Word count:** [n] (target: [range])

| Criterion | Score | Note |
|-----------|-------|------|
| Reading level | /5 | |
| … | | |
| **Total** | **/40** | **[band]** |

### Priority fixes
1. …

### Rewritten chunks
[headline / card / CTA copy suggestions]
```

## Anti-patterns (ACC-specific)

- Putting rewritten copy **inside images** instead of HTML — unreadable to search and assistive tech; use overlays or lockups ([imagery.md](../acc-ux-designer/imagery.md))
- Opening with mission statements before user benefit
- 3+ sentences before first scannable heading
- Undefined ACC, MOC, ABIM, SAP on first mention
- Passive institutional voice ("The College believes…")
- Matching ACC word count (~1,500) when peers use ~500
- Improving UI chunks but leaving dense prose inside each card
- Applying plain-language rules to guideline evidence tables

## Additional resources

- [checklist.md](checklist.md) — full 1–5 rubric per criterion
- [rewrite-guide.md](rewrite-guide.md) — rewrite tactics by chunk type
- [benchmarks.md](benchmarks.md) — peer scores and word counts

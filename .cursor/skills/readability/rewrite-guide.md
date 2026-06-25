# Rewrite Guide — Refactored Copy

Apply after [refactor](../refactor/SKILL.md) structures the page. Targets peer leaders (AMA, AAN, HFSA) per [benchmarks.md](benchmarks.md).

## Principles

1. **Benefit before institution** — user outcome first, ACC mission second (or omit)
2. **Shorter than ACC legacy** — if over ~700 words on a hub, cut or move to child pages
3. **Write for scan, then read** — headings and card titles must stand alone
4. **Define, then abbreviate** — `<abbr title="Maintenance of Certification">MOC</abbr>` once per view
5. **Active voice** — "You enroll" / "Members access" not "Enrollment is offered"

## By chunk type

### Hero / section intro

| Before (ACC pattern) | After |
|----------------------|-------|
| 3 paragraphs of mission + history | 1 sentence benefit + optional 1 sentence proof |
| "The American College of Cardiology envisions…" | "Stay board-certified with less hassle." |

**Target:** ≤40 words in hero CTA description (`data-item="cta-description"`).

### Hub CTA cards (process-stage / audience)

| Field | Rule | Example |
|-------|------|---------|
| Title | 3–6 words, stage or audience | "Already Enrolled" |
| Body | 1 sentence, ≤20 words | "See this year's topics and launch your SAP." |
| Button | Verb + object | "Next Steps" / "Enroll Now" — not "Click Here" |

### Card grid items

```
Title:   [Benefit or topic name]
Body:    One sentence, active voice, ≤25 words
Button:  btn-shade — "Start Course" / "View Schedule"
```

Remove second sentences — link to child page for depth.

### Lists (icon-decorated, features)

- **Bold lead-in** + em dash or period + short clause
- Max **12 words** after lead-in
- Parallel grammar across items

```html
<p><span class="font_bold">Annual assessment.</span> Pass one focused exam each year.</p>
```

### CTAs

| Score 5 pattern | Score 1–2 pattern |
|-----------------|-------------------|
| "Enroll in CMP" | "Submit" |
| "Launch ACCSAP" | "Learn More" (alone, no context) |
| "Join the WIC Section" | "Click for information" |

Use [icons.md](../acc-ux-designer/icons.md) only when dictionary supports the action.

### Jargon & acronyms

Required clinical terms: define once in intro or footnote.

```html
<abbr title="Collaborative Maintenance Pathway">CMP</abbr>
```

Drop: insider phrases ("the College", "FIT" without context) unless audience is certain.

### Headings

- `font_display` headings: **sentence case** or title case consistently
- State **what user finds**, not internal org names
- Bad: "ACC Distinguished Awards Program Information"
- Good: "Apply for Distinguished Awards"

## Sentence surgery

| Problem | Fix |
|---------|-----|
| >25 words | Split into two sentences |
| Passive | Flip to active |
| Nested clauses | One idea per sentence |
| "In order to" | "To" |
| "It is important to note that" | Delete |
| Trailing "respectively" | Restructure list |

## Word-count budget (refactored page)

| Zone | Max words |
|------|-----------|
| Hero title + CTA block | 60 |
| Intro below hero | 100 |
| Per card in grid | 35 |
| Full hub (marketing) | 500–700 |
| Section child | 400 |

Move overflow to child URLs per [refactor process-stage](../refactor/strategies.md) pattern.

## Re-score after rewrite

Re-run [checklist.md](checklist.md). Expect gains in:

- Sentence length (+1–2)
- Reading level (+1–2)
- Vocabulary & jargon (+1–2)
- Paragraph density (+1) when prose shortened

Scannability should already be 4+ if refactor UI applied.

**Target:** 29+ total for shipped initiative pages; 35+ for flagship product hubs.

## Clinical science exception

Guideline summaries, evidence tables, and CME learning objectives may retain higher reading level and terminology. Flag as **out of scope** in audit; do not force 6th-grade simplification on clinical accuracy.

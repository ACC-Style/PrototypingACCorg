# Workflows

How to choose a path and finish work in this repo.

## Deliverable types

| Type | Goal | Location | Layout |
|------|------|----------|--------|
| **Gold pattern** | Canonical reusable UI | `_ui_gold_standard/` | `ui/tripple_slot` |
| **Concept page** | Full-page idea, ACC shell | `__prototypes/` | `arches`, `ui/*`, `acc/fullscreen` |
| **Generator** | CSV/form → CMS HTML | `__generators/` | `playground` |
| **Playground experiment** | Quick test, discardable | `__ui_playground/` | varies |
| **Production handoff** | Paste into ACC CMS | Output from generator | N/A — flat HTML |

## Standard design process

### 1. Discover
- User goal, audience, content type (list, hero, form, card grid)
- Existing ACC.org page or internal prototype to echo
- Open nearest gold-standard file

### 2. Structure
- Sketch regions: hero → content → CTA → ancillary
- Pick grid: `columns_1 columns_2:md` default; increase columns for card galleries
- Assign heading levels

### 3. Compose
- Apply `reading-typography` + `wrapper-container`
- Layer surfaces: `bg_white`, borders, `shadow_bevel-light`
- Add responsive classes at `:md` and `:lg`

### 4. Wire behavior
- Static only → stop at HTML
- Sort/filter/state → `data-component` + IIFE script (see `award_schedule.html`)
- Data-driven → CSV + Liquid loop or generator form

### 5. Validate
- Visual: compare to gold reference spacing and type scale
- Responsive: check single-column mobile, multi-column desktop
- CMS: copy output renders without Jekyll; script is self-contained
- Accessibility: heading order, link text, aria on badges

## Generator workflow

1. Add CSV schema to `_data/{name}.csv` if data-driven
2. Create `__generators/{name}.html` with `layout: playground`
3. Document columns in left aside (`Expected columns` list)
4. Build `subs/{card}.html` for repeated units
5. Preview driver: parse input → render HTML → optional `init*` runtime
6. CMS output textarea: flat HTML + serialized runtime script

### Generator UI layout

```
aside (left)                    main (right)
├── CSV paste / form            └── sticky live preview
├── column schema
└── CMS output copy box
```

## Concept → production promotion

When a concept graduates:

1. Move or copy pattern to `_ui_gold_standard/` if it is a reusable block
2. Extract repeated markup to `subs/` or `_includes/Blocks/`
3. If authors need CSV authoring → build generator
4. Document `notes:` and add row to [examples.md](examples.md)

## Sorting & list behavior (DateList pattern)

| Section | Sort |
|---------|------|
| Open | Alphabetical by title |
| Upcoming | Chronological, then alpha |
| Past | Reverse chronological, then alpha |

Title sort ignores leading "The" and "ACC".

## Files to touch by task

| Task | Files |
|------|-------|
| New card look | `_ui_gold_standard/`, maybe `subs/` |
| New page | `__prototypes/`, `_data/` if needed |
| New CMS tool | `__generators/`, `_data/*.csv`, `subs/` |
| Shared block | `_includes/Blocks/`, PageBlocks data |
| Runtime behavior | IIFE inside generator; serialize for CMS copy |

## Questions to ask the user when ambiguous

1. Is this a **reference pattern**, **full page**, or **CMS builder**?
2. Does content come from **CSV**, **manual CMS HTML**, or **fixed copy**?
3. Is **client-side runtime** required (dates, filters, tabs)?
4. Should it match an **existing ACC.org URL**?

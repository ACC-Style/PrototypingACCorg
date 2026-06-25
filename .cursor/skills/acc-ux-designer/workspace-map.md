# Workspace Map

Where work lives and how it ships.

## Collections (authoring)

| Collection folder | URL prefix | Use for |
|-------------------|------------|---------|
| `_collections/_ui_gold_standard/` | `/ui-gold/:path/` | Canonical UI patterns; highest visual fidelity |
| `_collections/__prototypes/` | `/acc/:path/` | Full page concepts, PageBlocks, ACC flows |
| `_collections/__generators/` | `/generators/:path/` | Interactive builders; CMS HTML output |
| `_collections/__ui_playground/` | `/ui/:path/` | Experiments, charts, throwaway tests |
| `_collections/_member_section_prototype/` | `/MemberSection/:path/` | Gated member experiences |
| `_collections/_annual_meeting_prototype/` | `/AnnualMeeting/:path/` | Annual meeting flows |
| `_collections/_ncd/` | `/NCD/:path/` | NCD academy |

Config: `_config.yml` (`collections_dir`, `permalink` per collection).

Build output: `docs/` (GitHub Pages).

## Shared infrastructure

| Path | Role |
|------|------|
| `_layouts/` | Page shells — `arches.html`, `playground.html`, `ui/tripple_slot.html`, `acc/fullscreen.html` |
| `_includes/` | Fragments — `arches-head.html`, `Blocks/*`, `URL.html`, `MicroSite/*` |
| `_data/` | CSV/YAML driving generators and PageBlocks |
| `assets/css/` | Local Arches copies (`acc_boot.css`, `acc_uc.css`) for reference |

## Layout picker

| Layout | When |
|--------|------|
| `ui/tripple_slot` | Gold-standard showcase with name/position header |
| `ui/fullscreen_slot` | Full-bleed concepts (heroes, landing sections) |
| `ui/dual_slot` | Side-by-side comparison |
| `playground` | Generators — sidebar nav, `data-note="Copy Me"` wrapper |
| `arches` | Production-like ACC page shell |
| `acc/fullscreen` | ACC fullscreen with optional `masthead` |

## Standard page front matter

```yaml
---
layout: ui/tripple_slot
name: "Human-readable title"
position: "Short description for the UI header"
notes: "Optional usage guidance shown in layout"
csv_file: "award-schedule"   # generators only — links _data file in sidebar
---
```

## Generator anatomy

```
__generators/
├── {name}.html          # playground page + preview driver
└── subs/
    ├── date-card.html   # single card partial ({% include_relative %})
    └── event-card.html
```

Data: `_data/{name}.csv` referenced by `csv_file` in front matter.

## Liquid helpers

```liquid
{% include URL.html url='https://www.acc.org/...' %}
{% include URL.html media='{GUID}' %}
{% include_relative subs/date-card.html item=item %}
{% include Blocks/FollowUpCTA.html data_path="Blocks.FollowUpCTA" %}
```

## Local preview

Jekyll serves collection pages at their permalink under `baseurl`.
Generator pages expose live preview in-page; gold pages render static HTML in the layout slot.

# Collection Partials vs Global Includes

Where prototype markup lives — and how to promote a pattern when a second project needs it.

---

## Decision rule

| Scope | Location | Liquid tag | Document in |
|-------|----------|------------|-------------|
| **Cross-project** — reusable by any collection, generator, or layout | `_includes/` (e.g. `MicroSite/`, `Blocks/`, `arches-*.html`) | `{% include Path/file.html %}` | [components.md](components.md), [microsite-patterns.md](microsite-patterns.md) |
| **Single initiative** — UI tied to one collection's data shape, nav, or bespoke interaction | `_collections/{collection}/partials/` | `{% include_relative partials/file.html %}` | That collection's `content-collection.md` |

**Do not** add project-specific paths under `_includes/` (e.g. `Clinician-Wellbeing/`).

**Do not** branch global includes on one project's name. Generic optional params (e.g. `hero_image_dir`, `hero_image_ext`) are fine when any collection can pass them from YAML or front matter.

**Before creating a collection partial**, check:

1. `MicroSite/` — heroes, teasers
2. `Blocks/` — FollowUpCTA, UL_IconHeadlineText, etc.
3. Gold-standard / peer collection pages — same IA role?

If a global include exists, wire it with `_data/{Initiative}/` and front matter. Only add a partial when markup is truly unique to that initiative.

When a second collection needs the same bespoke component, **promote** it: move to `_includes/`, generalize data hooks, and add it to the UX skill component catalog.

---

## Why `include_relative`

Jekyll's `{% include_relative %}` resolves paths from the **current collection page file**, not from `_includes/`. That keeps initiative-specific sidebars, zone blocks, and interactive widgets co-located with the pages and data that drive them.

Layouts in `_layouts/` **cannot** use `include_relative` for collection partials. Prefer **`Global/sidebar`** for spoke pages (sidebar + content grid in one layout). Use collection `partials/spoke-layout-open.html` only when the sidebar zone needs initiative-specific blocks below the nav (e.g. Clinical Solutions callouts).

1. Spoke page uses `layout: Global/sidebar` with `sidebar_data_path` + nav keys in front matter; body is zones only.
2. Or legacy: thin layout + `partials/spoke-layout-open.html` that includes `MicroSite/sidebar-nav.html` and any sidebar extras.
3. Page body zones use global `{% include Blocks/... %}` or `{% include_relative partials/... %}` when no global pattern fits.

---

## Reference implementations

### Clinical Solutions

```
_collections/_clinical_solutions/
  Concept-Clinical-Solutions-Chronic-Coronary.html
  partials/
    spoke-layout-open.html      ← MicroSite/sidebar-nav + sidebar callouts + <main>
    spoke-layout-close.html
    topic-resource-sections.html
    follow-up-cta.html          ← inline-param CTA (no Blocks data yet)
    …
```

```liquid
{%- include_relative partials/spoke-layout-open.html -%}
{%- include_relative partials/spoke-intro-zone.html -%}
…
{%- include_relative partials/spoke-layout-close.html -%}
```

Layout: `arches-clinical-solutions` — `masthead: empty.html`; hero optional via layout params.

### Clinician Well-Being

```
_collections/__clinical-wellbeing/
  partials/
    mini-z-assessment.html      ← interactive JS (initiative-only)
    toolkit-citation.html       ← initiative-specific attribution copy
```

**Everything else uses global includes + `_data/ClinicianWellBeing/`:**

| Pattern | Global include |
|---------|----------------|
| Hub / spoke heroes | `MicroSite/heroimage.dynamic.html`, `MicroSite/heroimage.micro.dynamic.html` |
| Spoke shell + sidebar | `Global/sidebar` layout + `MicroSite/sidebar-nav.html` |
| Linked / key-point grids | `Blocks/GridListLinkedIconText.html` |
| Hub fork cards | `Blocks/HubForkCards.html` |
| Stat row | `Blocks/StatRow.html` |
| Accordions | `Blocks/AccordionStack.html` |
| Small image-text panel | `Blocks/SmallImageTextPanel.html` |
| Follow-up CTA | `Blocks/FollowUpCTA.html` |

### Member Section prototype

`_collections/_member_section_prototype/PageBlocks/` — same `include_relative` pattern from concept pages.

### Generators

`__generators/subs/` — `include_relative` from the generator HTML file (not a collection, but same locality rule).

---

## Global includes to reuse (not duplicate)

| Need | Use |
|------|-----|
| Section hero (hub root) | `MicroSite/heroimage.dynamic.html` — pass `hero_image_base`, optional `hero_image_dir`, `hero_image_ext` |
| Micro hero (spoke) | `MicroSite/heroimage.micro.dynamic.html` via `masthead:` + layout/front matter |
| Spoke page shell | `Global/sidebar` | `sidebar_data_path`, `nav_active_key`, `masthead`, `hero_data_path` |
| Side navigation | `MicroSite/sidebar-nav.html` + `data_path`, `active_key`, `sub_active_key` |
| Linked icon grid (microsite) | `Blocks/GridListLinkedIconText.html` + `pages_data_path` for `url_key` |
| Hub fork cards | `Blocks/HubForkCards.html` |
| Horizontal stat row | `Blocks/StatRow.html` |
| YAML-driven accordions | `Blocks/AccordionStack.html` |
| Small image-text panel | `Blocks/SmallImageTextPanel.html` (inline params) |
| Follow-up CTA (data-driven) | `Blocks/FollowUpCTA.html` + `_data/{Initiative}/follow_up_ctas.yml` |
| Icon headline lists (generic) | `Blocks/UL_IconHeadlineText.html` |
| Arches chrome | `arches-head.html`, `arches-header.html`, `arches-footer.html` |

Initiative-specific art paths belong in `_data/{Initiative}/hero.yml` (or page front matter), passed into global heroes — not in collection `hero-images.html` partials.

---

## Judgment checklist for new microsites

1. Create `_collections/{name}/partials/` only when you identify markup with **no** reasonable global pattern.
2. Prefer `{% include MicroSite/... %}` and `{% include Blocks/... %}` with `_data/{name}/` first.
3. Use `{% include MicroSite/... %}` and `{% include Blocks/... %}` with `_data/{name}/` first; `{% include_relative partials/... %}` only when no global pattern fits.
4. Keep `_layouts/arches-{name}.html` thin — pass masthead hero params from layout; no `{% include CollectionName/... %}`.
5. Note partial paths in `{name}/content-collection.md` (red meta line).
6. Promote to `_includes/` + skill docs when a second project needs the same component.

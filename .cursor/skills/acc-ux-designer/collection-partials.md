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

Layouts in `_layouts/` **cannot** use `include_relative` for collection partials. Spoke shells therefore live in the collection:

1. Thin layout (`arches-clinical-wellbeing`, `arches-clinical-solutions`) — header, **masthead hero** (global `MicroSite/`), `{{ content }}`, footer.
2. Collection page opens shell + sidebar via `partials/spoke-layout-open.html`.
3. Page body zones use global `{% include Blocks/... %}` or `{% include_relative partials/... %}` when no global pattern fits.
4. `partials/spoke-layout-close.html` closes the grid.

---

## Reference implementations

### Clinical Solutions

```
_collections/_clinical_solutions/
  Concept-Clinical-Solutions-Chronic-Coronary.html
  partials/
    spoke-layout-open.html      ← sidebar + <main>
    spoke-layout-close.html
    sidebar-nav.html
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
  Concept-Clinician-Well-Being.html          ← hub: fullscreen, global section hero in body
  Concept-Clinician-Well-Being-Mental-Health.html
  partials/
    spoke-layout-open.html
    spoke-layout-close.html
    sidebar-nav.html
    icon-grid.html              ← url_key resolution + linked/unlinked modes
    hub-fork-cards.html
    stat-row.html
    accordion-stack.html
    feature-panel.html
    mini-z-assessment.html      ← interactive JS
    toolkit-citation.html
```

**Heroes (global, not partials):**

- Hub root: `{% include MicroSite/heroimage.dynamic.html %}` with `hero_image_dir` / `hero_image_ext` from `_data/ClinicianWellBeing/hero.yml`
- Spokes: `masthead: MicroSite/heroimage.micro.dynamic.html` — layout passes hero vars + hub back-link

**Follow-up CTAs (global):** `{% include Blocks/FollowUpCTA.html data_path="ClinicianWellBeing.follow_up_ctas.{key}" cta_type="bevel" %}`

Data: `_data/ClinicianWellBeing/*.yml`

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
| Follow-up CTA (data-driven) | `Blocks/FollowUpCTA.html` + `_data/{Initiative}/follow_up_ctas.yml` |
| Icon headline lists (generic) | `Blocks/UL_IconHeadlineText.html` |
| Arches chrome | `arches-head.html`, `arches-header.html`, `arches-footer.html` |

Initiative-specific art paths belong in `_data/{Initiative}/hero.yml` (or page front matter), passed into global heroes — not in collection `hero-images.html` partials.

---

## Judgment checklist for new microsites

1. Create `_collections/{name}/partials/` only when you identify markup with **no** reasonable global pattern.
2. Prefer `{% include MicroSite/... %}` and `{% include Blocks/... %}` with `_data/{name}/` first.
3. Use `{% include_relative partials/... %}` for sidebar nav, layout shells, and truly bespoke zones.
4. Keep `_layouts/arches-{name}.html` thin — pass masthead hero params from layout; no `{% include CollectionName/... %}`.
5. Note partial paths in `{name}/content-collection.md` (red meta line).
6. Promote to `_includes/` + skill docs when a second project needs the same component.

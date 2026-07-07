# Global page layouts

Standard ACC microsite shells — replace per-project layouts and manual `spoke-layout-open` / `spoke-layout-close` includes.

`acc/fullscreen` and `acc/sidebar` now use the same `_includes/Global/*` helpers.

---

## Layouts

| Layout | Use for |
|--------|---------|
| `Global/fullscreen` | Concept **root** — masthead hero + full-width body |
| `Global/sidebar` | **Spoke** pages — micro masthead + left sidebar + content grid |

Legacy alias: `arches-clinical-wellbeing` → `Global/sidebar` (deprecated).

---

## Front matter — hero (both layouts)

| Key | Purpose |
|-----|---------|
| `masthead` | Optional override — default `MicroSite/heroimage.dynamic.html` (section hero). Spokes: `MicroSite/heroimage.micro.dynamic.html`. No hero: `empty.html` |
| `hero_data_path` | YAML defaults for art — e.g. `ClinicianWellBeing.hero` |
| `hero_content_path` | Section hero copy — e.g. `ClinicianWellBeing.hub` → `hero.title`, `hero.cta_*` |
| `pages_data_path` | Pages map — e.g. `ClinicianWellBeing.pages` |
| `hero_cta_url_key` | Key in pages map for section hero CTA link (e.g. `tools`) |
| `hub_url_path` | Hub URL for micro hero back link — e.g. `ClinicianWellBeing.pages.hub` |
| `hero-title`, `hero-cta-text`, `hero-cta-link`, … | Page overrides (win over YAML) |
| `parent-page`, `parent-link` | Section hero breadcrumb |

Resolved by `_includes/Global/masthead-render.html`:

1. Resolves YAML + front matter into **parent-scope** variables (`hero_title`, `cta_title`, …).
2. Includes masthead partial **without** params (Jekyll drops params on dynamic/multi-line includes).
3. Hero partials read `include.*` **or** parent assigns — use `page['hero-title']` bracket form for hyphenated keys.

Legacy layouts that call `{% include {{ page.masthead }} hero_title=page.hero-title %}` still work via `include.*` params.

---

## Front matter — sidebar (`Global/sidebar` only)

| Key | Purpose |
|-----|---------|
| `sidebar_data_path` | YAML nav — e.g. `ClinicianWellBeing.sidebar` → `MicroSite/sidebar-nav.html` |
| `nav_active_key` | Front-matter field name for active top item (e.g. `wellbeing_nav`) |
| `nav_sub_active_key` | Front-matter field name for active child (e.g. `wellbeing_nav_sub`) |
| `sidebar_aria_label` | Optional `aria-label` on `<nav>` |

**Sidebar YAML rule:** every item with `children` must have a unique `key` — collapse targets use `#childNavCollapse-{key}` (not a shared class).

---

## Spoke page example

```yaml
---
layout: Global/sidebar
masthead: MicroSite/heroimage.micro.dynamic.html
hero_data_path: ClinicianWellBeing.hero
hub_url_path: ClinicianWellBeing.pages.hub
sidebar_data_path: ClinicianWellBeing.sidebar
nav_active_key: wellbeing_nav
nav_sub_active_key: wellbeing_nav_sub
sidebar_aria_label: Clinician Well-Being
wellbeing_nav: tools
wellbeing_nav_sub: mental_health
hero-title: Care for Yourself
hero-cta-text: Get Support
hero-cta-link: https://example.org/
---
```

Body is **zones only** — no layout wrappers.

---

## Hub root example

```yaml
---
layout: Global/fullscreen
hero_data_path: ClinicianWellBeing.hero
hero_content_path: ClinicianWellBeing.hub
hero-title: Clinician Well-Being
hero-cta-title: Self Care is also part of the job.
hero-cta-description: Burnout is not a personal failing…
hero-cta-button-text: Explore Resources
hero-cta-link: "#"
parent_link: https://www.acc.org/
parent-page: ACC.org
---
```

Default masthead is **section hero** (`MicroSite/heroimage.dynamic.html`) — omit `masthead` unless overriding.

---

## Global includes

| File | Role |
|------|------|
| `Global/masthead-render.html` | Masthead + YAML/param resolution |
| `MicroSite/sidebar-nav.html` | YAML-driven side nav (`data_path`, `active_key`, `sub_active_key`) |
| `Global/resolve-data-path.html` | Dotted path → `resolved_data` |
| `Global/page-shell-styles.html` | Page-layout grid + hero-image-cta CSS |
| `arches-bootstrap.html` | Bootstrap 5.0.2 JS bundle (via `arches-footer.html`; load once per page) |

**Bootstrap:** Arches CSS (`arches-head.html` → 5.0.0) + `arches-bootstrap.html` (5.0.2 bundle). Do not add a second `<script>` in layout files — `arches-footer.html` already includes it.

Older layouts (`arches-sidebar`, member section) still use inline `sidebarArray` front matter — migrate new work to `Global/sidebar` + YAML.

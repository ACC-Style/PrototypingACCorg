# Hero Graphic Treatments

ACC uses **three hero types**. Pick based on **site-structure role**, not page length or visual preference.

| Type | When | Grid template | Child echo? |
|------|------|---------------|-------------|
| **Anchor** | Major capstone / silo entry | `hero-area` | No — globally shared domain brand |
| **Section** | Initiative audience banding + conversion | `hero-image-cta` | **Yes** — micro banner on children |
| **Product** | Product name + branding | `hero-image-cta` | **No** — children use standard page chrome |

## Decision tree

```
Where does this page sit in IA?

Top-level silo capstone (About ACC, major domain entry)?
  → Anchor Hero

Parent of a related page family with shared initiative branding?
  → Section Hero on parent
  → Micro Section Hero on children under that parent

Standalone product or product family root (SAP, CMP, course)?
  → Product Hero on product page
  → No hero echo on product child pages
```

---

## 1. Anchor Hero

**Reserved for major capstone pages** — top of silos in site structure.

### Purpose

- Establish the **domain brand** (globally shared ACC treatment — not section- or product-specific art)
- Feature the **most important business goal** for that silo in a dedicated promo zone
- Intro copy + featured CTA cutout — not just a title band

### Live example

[About ACC](https://www.acc.org/About-ACC)

### Technical pattern

- `grid-template="hero-area"`
- Grid areas: `background`, `breadcrumb`, `title`, `feature-cutout` / `cta`, `intro`, curves
- `hero-color-splash` background — domain gradient + optional imagery
- `data-item` hooks: hero curves, feature container, business-goal CTA
- Uses **`c_acc` / domain brand** — same visual language site-wide for anchor tier

### Repo references

| File | Notes |
|------|-------|
| `_ui_gold_standard/Concept-Anchor-Hero.html` | Gold standard — feature cutout + intro |
| `__prototypes/PageBlocks/HeroArea.html` | Parameterized anchor block |
| `__prototypes/Concept-EDU-MEETING.html` | Concept using `hero-area` |

### Rules

- Do **not** use for section initiatives or product pages
- Business-goal CTA lives in the **feature cutout** — primary conversion for the silo
- Breadcrumb is minimal (home/back) — not section micro-nav

```html
<div grid-template="hero-area" class="grid relative isolation_isolate …">
  <div grid-area="background" class="hero-color-splash …"></div>
  <div grid-area="breadcrumb">…</div>
  <div grid-area="title"><h1>…</h1></div>
  <div grid-area="feature-cutout">
    <!-- Featured business goal + btn -->
  </div>
  <div grid-area="intro" class="reading-typography">…</div>
</div>
```

---

## 2. Section Hero

**Small banding treatment** to isolate an **audience** and show that concepts and pages are co-related.

### Purpose

- Visual + nav anchor for an **initiative** (Membership Join Us, WIC section, education program)
- **Micro-navigation** — breadcrumb back to parent; sidebar on deeper children
- **Required CTA** — the major goal or conversion for this initiative
- Section can have **its own** hero imagery/branding (unlike anchor’s global domain brand)

### Live examples

| Role | URL |
|------|-----|
| Section parent | [Membership / Join Us](https://www.acc.org/membership/join-us) |
| Section child | [FACC](https://www.acc.org/Membership/Join-Us/FACC) |

### Section parent (full hero)

- `grid-template="hero-image-cta"` with `id="hero"` and `class="font_3:lg font_2:md font_1"`
- Grid areas: `background`, `breadcrumb`, `title`, `cta`
- `data-item="responsive-hero-image"` — breakpoint art inside `grid-area="background"`
- `data-item="hero-image-breadcrumb-nav"` — back link; parent name as plain text after `|`
- `data-item="hero-title"` — word spans (`<span class="text">`) for overlay chips via acc_boot CSS
- **`data-item="cta-callout"`** — **required** — `cta-title`, `cta-description`, `btn-primary` conversion
- Overlay scrims come from acc_boot `::after` on `hero-image-breadcrumb-nav`, `hero-title span`, and `cta-callout` — not manual `bg_acc` divs

### Section child (micro banner)

Pages under the section parent use a **thin micro hero** that **echoes** the section branding:

- `grid-template="hero-image-cta"` + `template-option="micro"`
- Same responsive image family as parent (sliced thinly)
- Short title + optional compact CTA
- Mobile back arrow to parent (`display_none:md` + `fa-arrow-left`)
- Set via layout `masthead: MicroSite/heroimage.micro.dynamic.html`

### Repo references

| File | Notes |
|------|-------|
| `__prototypes/MicroSite/heroimage.html` | Full section hero + CTA overlay |
| `_member_section_prototype/PageBlocks/heroimage.dynamic.html` | Dynamic section hero |
| `__prototypes/MicroSite/heroimage.micro.dynamic.html` | **Micro banner** for children |
| `__prototypes/MicroSite/heroimage.micro.ux.html` | Micro with inline CTA |
| `_member_section_prototype/3.1.0_about.html` | Child page using `masthead: …micro.dynamic.html` |

### Rules

- **CTA is mandatory** on section parent — never ship a section hero without conversion goal
- Child pages **must** use micro echo — users should recognize they’re still in the initiative
- Section branding ≠ anchor domain brand — initiative-specific creative is OK
- Pair with sidebar / anchor nav on deeper section trees when needed

```html
<!-- Section parent -->
<div grid-template="hero-image-cta" id="hero" class="font_3:lg font_2:md font_1">
  <div grid-area="background">
    <picture data-item="responsive-hero-image">…</picture>
  </div>
  <div grid-area="breadcrumb">
    <nav data-item="hero-image-breadcrumb-nav">…Back</a> | Parent name</nav>
  </div>
  <div grid-area="title">
    <h1 data-item="hero-title"><span class="text">Section</span> <span class="text">Title</span></h1>
  </div>
  <div grid-area="cta">
    <div data-item="cta-callout">
      <h2 data-item="cta-title">…</h2>
      <p data-item="cta-description">…</p>
      <a class="br_white-3 btn btn-primary c_white expanded-click-area shadow_overlap-bold">…</a>
    </div>
  </div>
</div>

<!-- Section child — micro -->
<div grid-template="hero-image-cta" template-option="micro" class="…">
  <!-- same image family, thin band, back link, short title -->
</div>
```

---

## 3. Product Hero

**Product branding and name** — for product roots (SAP, CMP, courses, tools).

### Purpose

- Identify the **product** visually and in the title
- Product-specific creative (not global anchor brand, not section initiative band)
- Conversion CTA when appropriate (Purchase, Enroll, Launch) — tied to product action

### Live example

[ACCSAP](https://www.acc.org/Education-and-Meetings/Products-and-Resources/SAP/ACCSAP)

### Technical pattern

- `grid-template="hero-image-cta"`
- `data-item="responsive-hero-image"` — product artwork
- `data-item="hero-title"` / `page-title` — product name
- Optional `data-item="cta-callout"` for product conversion
- Breadcrumb back to product category (Education and Meetings, SAP family)

### Children of product pages

**Do not** use the section micro-banner echo pattern. Product child pages use normal page chrome (breadcrumb, content header) — **no thin sliced hero** repeating product art.

This is a key difference from Section heroes.

### Repo references

| File | Notes |
|------|-------|
| `__prototypes/_archive/CMP-Marketing.html` | Product hero + CTA callout |
| `__ui_playground/CMP/heroimage.html` | Product CMP hero |
| `__prototypes/MicroSite/heroimage.basic.ai.html` | Product-style — title band, no section CTA overlay |
| `__prototypes/Course-Compact.html` | Course product listing hero |

### Rules

- Product-specific imagery — not shared anchor `hero-color-splash`
- Name the product clearly in `hero-title`
- Do **not** add `template-option="micro"` echo on SAP/CMP/course child pages
- Deep product content (modules, FAQs) starts below hero without micro band

```html
<div grid-template="hero-image-cta" id="hero" class="font_3:lg font_2:md font_1">
  <div grid-area="background">
    <picture data-item="responsive-hero-image">…</picture>
  </div>
  <nav data-item="hero-image-breadcrumb-nav" class="c_white-8">…</nav>
  <h1 data-item="hero-title">ACCSAP</h1>
  <div grid-area="cta">
    <div data-item="cta-callout">…optional product CTA…</div>
  </div>
</div>
```

---

## Comparison summary

| | Anchor | Section | Product |
|--|--------|---------|---------|
| **IA level** | Silo capstone | Initiative / audience family | Product root |
| **Brand** | Global domain | Section-specific | Product-specific |
| **Featured business CTA** | Yes (cutout) | **Required** (overlay) | Optional (product action) |
| **Child echo** | N/A | Micro banner | None |
| **Grid** | `hero-area` | `hero-image-cta` | `hero-image-cta` |
| **Micro-nav** | Minimal | Breadcrumb + sidebar | Category breadcrumb only |

## `data-item` reference

| Attribute | Used in |
|-----------|---------|
| `hero-image-cta` | Section + Product root (`grid-template`) |
| `responsive-hero-image` | Section + Product |
| `hero-image-breadcrumb-nav` | Section + Product |
| `hero-title` | Section + Product (word spans for chip overlay) |
| `cta-callout` / `cta-title` / `cta-description` | Section (required), Product (optional) |
| `hero-area` grid template | Anchor only |
| `template-option="micro"` | Section children only |

## Anti-patterns

- **Hero artwork with titles, taglines, or CTAs burned in** — use `responsive-hero-image` for atmosphere only; put `hero-title`, `cta-callout`, and links in HTML ([imagery.md](imagery.md))
- Anchor hero on a product or section child page
- Section hero **without** a `cta-callout`
- Micro banner echo on **product** children (sections only)
- Product-specific art on **anchor** capstone pages
- Using `hero-area` for Join Us, FACC, or ACCSAP — wrong tier
- Inventing a fourth hero type — fit page to IA role first

## Pairing with refactor skill

- **Anchor / Section parent** — short intro below hero; chunk body per [refactor](../refactor/SKILL.md)
- **Section child** — micro banner + content; skip repeating parent CTA copy
- **Product** — hero names product; process-stage CTAs (CMP pattern) live in body grid

# Cross-Domain Branding

Official reference: [Cross Domain Designs](https://assets.acc.org/Arches/Latest/docs/section-crossdomaindesigns.html)

Arches names colors and fonts by **functional role**, not by the literal hue. Markup uses `primary`, `accent`, `font_display`, etc. — a **domain branding modifier** (brand stylesheet) resolves those tokens to the correct palette and typefaces when rendered on ACC.org, CardioSmart, CVQuality, Virtual, etc.

**Build once, adapt per domain.** Do not hardcode hex values or assume `secondary` always looks the same.

## Functional color roles

| Token | Role |
|-------|------|
| `primary` | Main brand color — headers, key CTAs, strong brand moments |
| `secondary` | Second brand color — **varies by domain**; on flagship ACC it is grey — use sparingly |
| `accent` | Emphasis, flags, markers, hover fills |
| `highlight` | Reserved — see usage tier below |
| `info` | Reserved — see usage tier below |
| `shade`, `black`, `white` | Neutrals — surfaces, borders, muted text, neutral buttons (see **transparent modifiers** below) |
| `acc` | Global ACC brand token (ACC portfolio) |

Stepped modifiers apply to brand roles: `bg_primary-n1`, `c_shade-n2`, etc.

**Black and white are different** — their modifiers use **transparent rgba**, not opaque mixes. See [Black & white layering](#black--white-transparent-layering) below.

### Action colors (separate system)

Not design-brand colors — for interaction feedback only.  
See [Action Colors](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-designbase-colors-actions.html) and [design-system.md](design-system.md).

`alert`, `warning`, `success`, `navigation`

## ACC flagship — color usage order

When building for **ACC.org** (default in this repo), prefer tokens in this order:

| Priority | Tokens | Typical use |
|----------|--------|-------------|
| 1 | **Primary** | Colored headers (`bg_primary-n1`), primary CTAs (`btn-primary`), strong links |
| 2 | **Shade / black / white** | Card surfaces, panels (`bg_white`, `bg_black-1`), meta text (`c_shade-n2`), borders (`br_black-3`), neutral buttons (`btn-shade`) |
| 3 | **Accent** | Flag lists (`c_accent-n3`), hover states (`h:bg_accent-5`), list markers (`marker_accent`) |
| 4 | **Secondary** | **Sparingly** — on ACC, secondary is grey; avoid where shade/black already suffice |
| 5 | **Highlight / info** | **Rarely** — reserve for notifications, popups, alerts, and dialog UI |

```html
<!-- Typical ACC card — primary + neutrals + accent hover -->
<article class="bg_white shadow_bevel-light h:bg_accent-5">
  <h2 class="bg_primary-n1 c_white font_display">…</h2>
  <p class="c_shade-n2">…</p>
  <a class="btn btn-shade">…</a>
</article>

<!-- Avoid: bg_secondary or bg_highlight on a standard content card -->
```

**Highlight** and **info** overlap the “system chrome” tier — treat like action colors in restraint: only when the UI is explicitly a notification, modal, popup, or alert surface.

## Black & white transparent layering

Unlike `primary`, `accent`, and other brand roles (which mix opaque tints), **`black` and `white` modifiers are transparent** — each step is an `rgba()` alpha of the base black (`#131212`) or white.

This is intentional: it allows **layering on colored backgrounds** without blocking what sits beneath.

### Modifier scale

| Step | Approx. alpha | Typical use |
|------|---------------|-------------|
| `0` | 0% | Fully transparent |
| `-_01`, `-_05` | ~0.5–0.75% | Barely-there veil (`bg_black-_05`) |
| `1` | ~2.5% | Subtle panel tint (`bg_black-1`) |
| `2` | ~10% | Light wash |
| `3` | ~25% | Borders, disabled states (`br_black-3`) |
| `4`–`6` | 38–62% | Scrim, image overlays (`bg_black-4` + blend) |
| `7`–`8` | 75–90% | Muted text on light (`c_black-7`, `c_black-8`) |
| `9` | ~97.5% | Near-solid |
| `none` | 100% | Solid `c_black` / `c_white` |

Applies to `c_`, `bg_`, and `br_` prefixes: `c_white-8`, `bg_black-_05`, `br_black-2`.

### When to use transparent black/white

| Pattern | Classes | Effect |
|---------|---------|--------|
| Subtle panel on white page | `bg_black-1` | Light grey wash — reads as neutral surface |
| Panel **on brand color** | `bg_black-1` or `bg_white-2` on `bg_primary-n1` | Tint shows through — harmonizes with header |
| Hero breadcrumb / meta on photo | `c_white-8` | Soft white text over imagery |
| Accordion / inset content | `bg_black-_05` | Embossed inset over parent surface |
| Image scrim | `bg_black-4 bg-blend_multiply` | Darken photo while keeping image visible |
| De-emphasized helper text | `c_black-7` | Muted copy without a new color role |

```html
<!-- Hero: transparent white text over colored/image background -->
<nav class="c_white-8">
  <a class="c_white-8 h:c_white">Home</a>
</nav>

<!-- Inset panel: black veil layers on whatever is behind -->
<div class="bg_black-_05 br_radius p_4 shadow_emboss-light">…</div>

<!-- Colored header with transparent black child panel -->
<header class="bg_primary-n1 c_white">
  <aside class="bg_black-1 p_3 font-size_down">Metadata sits on tinted primary</aside>
</header>
```

### Black/white vs shade

| Token | Behavior | Prefer when |
|-------|----------|-------------|
| `black` / `white` + step | **Transparent** rgba — layers on color | On colored backgrounds, heroes, overlays, scrims |
| `shade` + step | **Opaque** neutral mix | Muted text on white (`c_shade-n2`), flat grey UI |

Do not substitute `bg_shade-2` when you need a **tinted overlay** on primary or imagery — use `bg_black-N` or `bg_white-N`.

### Reversed text panels

For full panels (not hero breadcrumbs), put **`reading-typography` + `color_inherit` + `c_{role}`** on the same element as **`bg_{role}`** so headings, paragraphs, and lists inherit when you swap palette. Do not wrap an extra unstyled `div` inside a `wrapper-container` section.

```html
<section class="bg_primary-n2 br_round c_white color_inherit reading-typography p_4 wrapper-container">…</section>
```

Full pattern, examples, and anti-patterns: [design-system.md — Reversed text panels](design-system.md#reversed-text-panels-color-on-color).

## Functional font roles

| Class | Role | ACC | CardioSmart | CVQuality | Virtual |
|-------|------|-----|-------------|-----------|---------|
| `font_display` | Display / headings | Maven Pro | Maven Pro | Maven Pro | Libre Franklin |
| `font_copy` | Body copy | Open Sans | Open Sans | Lato | Open Sans |
| `font_accent` | Accent emphasis | Roboto Slab | Roboto Slab | Roboto Slab | Roboto Slab |
| `font_ui` | UI chrome | Open Sans | Open Sans | Lato | Open Sans |

Use role classes — never embed brand-specific `font-family` in markup.

```html
<h2 class="font_display font_3">Heading</h2>
<p class="font_copy lh_3">Body</p>
<span class="font_accent">Label emphasis</span>
```

## Domain modifiers in practice

### Brand stylesheets

Each domain ships its own Arches brand build (`acc_boot.css` + brand theme). This repo loads **ACC 5.0.0** by default via `_includes/arches-head.html`.

When prototyping another domain, swap the brand CSS bundle — markup (`c_primary`, `font_display`) stays the same.

### Product color codes (not cross-domain brand)

Separate stylesheets for **object semantics** within a domain:

| Stylesheet | Use |
|------------|-----|
| `color-code_credits.css` | CME / accreditation |
| `color-code_LOE_COR.css` | Guidelines LOE & COR |
| `color-code_journals.css` | Journal branding |
| `color-code_social.css` | Social |

These are domain-specific **meaning** colors, not the cross-domain `primary`/`accent` roles.  
See [color codes](https://assets.acc.org/Arches/Latest/docs/color_codes/).

Data reference: `_data/colors.csv`

## Decision checklist

```
Choosing a color token:
- [ ] Is this user/system feedback?        → action color (alert/warning/success)
- [ ] Is this a notification/modal/dialog? → highlight or info
- [ ] Is this main brand emphasis?           → primary
- [ ] Is this neutral structure/text?        → shade / black / white
- [ ] Is this emphasis within content?       → accent
- [ ] Is secondary the only option left?     → use sparingly on ACC
```

## Anti-patterns

- **Readable copy inside image files** on heroes or cards — scrims and `c_white-8` are for HTML type over art, not a substitute for exporting text as graphics ([imagery.md](imagery.md))
- Hex or RGB in markup instead of functional tokens
- `bg_secondary` or `c_secondary` as a default fill — especially on ACC (grey secondary)
- `highlight` / `info` on marketing cards, heroes, or list items
- `font-family` inline styles instead of `font_display` / `font_copy` / `font_accent` / `font_ui`
- Confusing product `color-code_*` classes with brand `primary` / `accent` roles
- Using opaque `shade` or solid `c_white` when a **transparent** `c_white-8` / `bg_black-1` layer is needed on color or imagery
- `bg_white` or `bg_black-none` on colored surfaces when a tinted transparent layer would blend better

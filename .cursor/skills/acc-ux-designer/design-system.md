# Design System — Project Conventions

Arches utility **syntax and anatomy** live in [arches-utilities.md](arches-utilities.md) (sourced from [official docs](https://assets.acc.org/Arches/Latest/docs/utility_classes/section-anatomy.html)).  
This file covers how this **repo** applies Arches to prototypes, generators, and CMS output.

## CDN (production parity)

```
https://assets.acc.org/Arches/5.0.0/dist/css/acc_boot.css
https://assets.acc.org/Arches/5.0.0/dist/css/acc_uc.css
```

Loaded in `_includes/arches-head.html`. Local reference: `assets/css/`.

## Semantic wrappers (repo-specific)

| Class | Role |
|-------|------|
| `reading-typography` | Prose defaults — links, lists, paragraph rhythm |
| `wrapper-container` | Content width alignment inside cards/sections |
| `font-size_up` / `font-size_down` | Relative type scale on a subtree |
| `isolate_isolation` | Stacking context for layered cards |

Set scale on a container:

```html
<div class="reading-typography font-size_up" style="--custom-font-size-up: 1.125;">
```

## Typography (repo usage)

Fonts use the same **functional roles** as cross-domain colors — see [cross-domain-branding.md](cross-domain-branding.md).

| Role | Class | Use |
|------|-------|-----|
| Display / headings | `font_display` | `h1`–`h4`, card titles, hero headlines |
| Body | `font_copy` | Prose, descriptions |
| Accent emphasis | `font_accent` | Labels, callouts, slab emphasis |
| UI chrome | `font_ui` | Nav, buttons, compact UI labels |
| Size down/up | `font-size_down`, `font-size_up`, `font-size_up-1`, `font-size_up-2` |
| Weight | `font_light`, `font_regular`, `font_bold`, `font_xbold` |
| Line height | `lh_1`, `lh_2`, `lh_3` |
| Wrap | `wrap_pretty`, `wrap_balance`, `nowrap` |

Heading in a card: `h4 lh_1 wrap_pretty m_0 font_display`

Font steps use the Arches `font_N` scale — see stepped value table in [arches-utilities.md](arches-utilities.md).

## Color (repo usage)

Cross-domain functional naming and ACC usage order: [cross-domain-branding.md](cross-domain-branding.md)  
Action colors (feedback only): [Design Base — Action Colors](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-designbase-colors-actions.html)

Arches colors are **role names**, not fixed hues — `primary`, `accent`, etc. resolve per domain brand stylesheet. This repo defaults to **ACC.org**.

### ACC usage priority (most → least)

1. **Primary** — headers, primary CTAs, brand moments  
2. **Shade / black / white** — surfaces, borders, muted text, `btn-shade`; **black/white steps are transparent** for layering on color (see [cross-domain-branding.md](cross-domain-branding.md))  
3. **Accent** — flags, markers, `h:bg_accent-5`  
4. **Secondary** — **sparingly** (on ACC, secondary is grey)  
5. **Highlight / info** — **rarely** — notifications, popups, alerts, dialogs only  

```html
<h2 class="bg_primary-n1 c_white font_3 font_display p_3 p_4:lg">Title</h2>
<strong class="c_shade-n2 font-size_down">…</strong>
<div class="bg_black-1 br-b_1 br_black-3 br_solid">…</div>
<nav class="c_white-8">…</nav>              <!-- transparent white on hero/color -->
<div class="bg_black-_05 p_4 br_radius">…</div> <!-- subtle veil over parent -->
```

**Black/white modifiers = transparent rgba** — use for layering on colored backgrounds. **Shade** = opaque neutral for flat UI on white.

Stepped modifiers: `-n1`…`-n5` (darker), `-1`…`-5` (lighter).

### Action colors (feedback only)

**Not for general UI.** Bootstrap-aligned; respond to user input and messaging:

| Role | Token | Use when |
|------|-------|----------|
| Error / destructive | `alert` | Validation errors, failed actions, critical messages |
| Caution | `warning` | Warnings, non-blocking issues, status badges (e.g. "Open") |
| Confirmation | `success` | Success states, completed actions |
| Navigation feedback | `navigation` | Navigation-specific system feedback |

Bootstrap equivalents (`btn-danger`, `alert-warning`, etc.) — feedback only.

Product semantics: `color-code_*.css` — see [cross-domain-branding.md](cross-domain-branding.md).

## Spacing (repo defaults)

Arches steps `0`–`5` (see anatomy doc). This repo commonly uses:

| Use | Classes |
|-----|---------|
| Card padding | `p_4`, `p-x_4 p-y_3` |
| Section gap | `gap_4`, `gap_5:lg` |
| Section margin | `m-b_4`, `m-t_0` |
| Negative overlap | `m-b_n3`, `m-x_n4` |

Breakpoints: `:md` (640px), `:lg` (1024px) — mobile-first.

## Grid & flex

```html
<div class="grid columns_1 columns_2:md columns_3:lg gap_4 gap-y_3">
<div class="flex flex_column flex_row:md items_center justify_between gap_3">
```

Named grids (heroes): see [heroes.md](heroes.md) — `grid-template="hero-area"` (Anchor) vs `hero-image-cta` (Section/Product)

## Surfaces & borders

```html
<div class="bg_white br_1 br_black-3 br_radius br_solid shadow_bevel-light">
<footer class="br-t_1 br_black-2 br_dotted p-y_3">
```

Shadows: `shadow_bevel-light`, `shadow_bevel-bold`, `shadow_overlap-light`  
Hover: `h:bg_accent-5`, `h:bg_primary-5`, `h:undecorated`

## Buttons

Bootstrap + UC combined. **Default supporting action:** `btn-shade` (light grey background, black text — lower contrast than `btn-secondary`, reads better on white cards).

| Role | Classes | When |
|------|---------|------|
| Primary CTA | `btn btn-primary` | Main action — Apply, Start, Submit |
| **Supporting / secondary** | `btn btn-shade` | **Preferred** — card footers, course links, generator controls, neutral CTAs |
| High-contrast secondary | `btn btn-secondary` | Use sparingly when shade is too subtle |
| Outline / tertiary | `btn btn-sm btn-outline-shade` | Learn More, low-emphasis footer actions |
| Large submit | `btn btn-lg btn-primary` | Forms, login |
| Text link | `btn btn-link link` | Inline text actions |
| Hit area | `expanded-click-area`, `expanded-click-area-beforeAlt` | Stretch tap target over a bounded region — see below |

```html
<a href="#" class="btn btn-shade btn-sm expanded-click-area">Start Course</a>
<a href="#" class="btn btn-primary">Apply Now</a>
<a href="#" class="btn btn-sm btn-outline-shade">Learn More</a>
```

### Expanded click area

`expanded-click-area` adds a `::after` pseudo-element that is **absolutely positioned** (`inset: 0`) to enlarge the tap/click target beyond the visible link or button text.

**The pseudo-element positions against the nearest positioned ancestor.** If that ancestor is too large — or is the page shell — the invisible hit zone can cover the entire viewport.

**Rule:** Wrap the control in a container with `relative` (and usually `isolation_isolate` or `z_1` stacking) so the expanded area is bounded to the card, row, or footer you intend.

```html
<!-- Card footer — hit zone = footer only -->
<footer class="relative isolation_isolate br-t_1 br_black-2 p-y_3">
  <a href="#" class="btn btn-shade expanded-click-area">Start Here</a>
</footer>

<!-- Full-row card link — hit zone = card -->
<article class="relative isolation_isolate br_radius shadow_bevel-light h:bg_accent-5">
  <a href="#" class="block p_4 undecorated expanded-click-area">
    <h3>Title</h3>
    <p>Description</p>
  </a>
</article>
```

| Do | Don't |
|----|-------|
| Put `relative` on the **smallest** wrapper that should receive the click | Put `expanded-click-area` on a link inside an unpositioned `<main>` or page grid |
| Use `isolation_isolate` / `z_1` when overlapping content must stay clickable | Assume the class only affects the link's own box |

Same rule applies to `expanded-click-area-beforeAlt` (uses `::before` instead of `::after`).

Reusable class bundles: `_includes/css-bundles/` (e.g. `sm-btn.txt`)

## Lists

| Class | Effect |
|-------|--------|
| `ul_none` | Unstyled list |
| `ul_inline-pipe` | Inline with pipe separators |
| `ul_list-comma` | Comma-separated inline |
| `marker_accent` | Colored list markers |

## Links

`not-link`, `undecorated`, `link`, `opacity_7`

Off-domain links: append `far fa-external-link` per [icons.md](icons.md).

## Icons

Font Awesome Pro 5.15.1 — concepts mapped in the [ACC Icon Dictionary](https://acc-style.github.io/IconDictionary/).  
Full markup rules and quick-reference table: [icons.md](icons.md).

## Imagery

Images are used **sparingly** — branding, audience grounding, humanization. Never bake headlines, body copy, or CTAs into image files; layer real HTML on photos or beside them. Full rules: [imagery.md](imagery.md).

## Anti-patterns

- **Text baked into images** — headlines, paragraphs, or CTAs as pixels (SEO, a11y, responsive); use HTML overlays or lockups instead — see [imagery.md](imagery.md)
- Raw Bootstrap `row`/`col` when `grid columns_*` suffices
- Inline `style` except `--custom-font-size-up` and rare `clamp()` on date badges
- Hardcoded hex colors — use functional `c_*` / `bg_*` tokens
- **Action colors** (`alert`, `warning`, `success`, `navigation`) for decoration — feedback only
- **`highlight` / `info`** outside notifications, popups, alerts, or dialogs
- **Overusing `secondary`** on ACC — grey secondary; prefer shade/black/white first
- Guessing class names — grep `acc_uc.css` or copy from gold standard
- Missing `reading-typography` on long prose blocks

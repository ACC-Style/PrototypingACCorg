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

## Reversed text panels (color-on-color)

A **reversed panel** is a block where the surface is a brand color and body copy reads in a contrasting text color (usually white on `bg_primary-n*` or `bg_accent-n*`).

**Put these three on the same container** — the `<section>`, `<aside>`, or `<article>` that owns the panel — so all semantic children inherit when you swap themes:

| Class | Role |
|-------|------|
| `reading-typography` | Prose rhythm for `h2`–`p`, lists, links inside the panel |
| `color_inherit` | Children inherit the container's text color |
| `c_{role}` | Text color token — e.g. `c_white` on primary/accent backgrounds |

Also on that **same** element: `bg_{role}`, padding, radius, shadow, and `wrapper-container` when the panel should align to content width.

```html
<!-- Good — one surface; swap bg + c_ together to retheme -->
<section
  class="bg_primary-n2 br_round c_white color_inherit p_4 p_5:lg reading-typography shadow_bevel-light wrapper-container">
  <h2 class="font_display m-t_0">Start Here — Safety Comes First</h2>
  <p class="font-size_down-1 lh_2 m-b_3">If you feel unsafe…</p>
  <ul class="columns_1 columns_2:md columns_3:lg gap-x_5 gap-y_3 grid ul_none">
    <li class="flex flex_row gap_3 items_start">
      <i class="far fa-circle-check opacity_8 flex_none" aria-hidden="true"></i>
      <span>Write down what happened.</span>
    </li>
  </ul>
</section>

<aside class="bg_accent-n2 br_radius c_white color_inherit p_4 p_5:lg reading-typography shadow_bevel-light sticky t_3">
  <h2 class="font_display m-t_0">Important Note</h2>
  <p class="font-size_down-1 lh_2 m-b_0">Disclaimer copy…</p>
</aside>
```

```html
<!-- Avoid — extra wrapper; color not on the semantic panel root -->
<section class="wrapper-container reading-typography">
  <div class="bg_primary-n2 c_white p_4">…</div>
</section>

<!-- Avoid — sprinkling c_white on every child instead of color_inherit on the panel -->
<section class="bg_primary-n2 p_4">
  <h2 class="c_white">…</h2>
  <p class="c_white">…</p>
</section>
```

| Do | Don't |
|----|-------|
| `reading-typography` + `color_inherit` + `c_white` on the **panel root** | Nest a bare `div` only for background while outer `section` stays uncolored |
| Use `c_white-8` / `c_white-9` only for **de-emphasis** (icons, meta) | Repeat `c_white` on every `h2`, `p`, `li`, `span` |
| Use **`opacity_8`** (or similar) on icons inside the panel — they inherit the root `c_*` and soften | Hard-code `c_white-8` on every icon when `color_inherit` already sets panel text |
| Change `bg_primary-n2` + `c_white` together to retheme | Mix `color_inherit` without a `c_*` text token on the same node |

**Icon de-emphasis:** On a reversed panel with `color_inherit` + `c_white` on the root, icons inherit white. Add `opacity_8` (or `opacity_9`) on the `<i>` instead of a separate `c_white-8` — the icon stays in sync if you swap the panel's `c_*` token.

```html
<i class="far fa-circle-check font_4 opacity_8 flex_none m-t_1" aria-hidden="true"></i>
```

See also [cross-domain-branding.md](cross-domain-branding.md) — transparent `c_white-8` on heroes vs opaque reversed panels.

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

**The pseudo-element positions against the nearest positioned ancestor.** If that ancestor is too large — or is the page shell — the invisible hit zone can cover the entire viewport and **overlap other clickable items**.

#### Required pairing

`expanded-click-area` must appear on the same element as **`btn`** (any variant), **`not-link`**, or **`btn-link`**. Never on a bare anchor or unstyled link.

```html
<a href="#" class="btn btn-shade expanded-click-area">Start Here</a>
<a href="#" class="expanded-click-area not-link h:undecorated">Card title + description</a>
<a href="#" class="btn btn-link link expanded-click-area">Learn more</a>
```

#### Required `relative` wrapper

**Always** wrap the expanded control in a `relative` container at some point in the ancestry — the smallest region that should receive the click (card, row, footer, list item). Use `isolation_isolate` when neighbors must stay independently clickable.

When multiple expanded controls share a page, each needs its own bounded `relative` wrapper so hit zones do not bleed into adjacent links or buttons.

```html
<!-- Card footer — hit zone = footer only -->
<footer class="relative isolation_isolate br-t_1 br_black-2 p-y_3">
  <a href="#" class="btn btn-shade expanded-click-area">Start Here</a>
</footer>

<!-- Full-row card link — hit zone = card -->
<article class="relative isolation_isolate br_radius shadow_bevel-light h:bg_accent-5">
  <a href="#" class="expanded-click-area not-link h:undecorated block p_4">
    <h3>Title</h3>
    <p>Description</p>
  </a>
</article>
```

| Do | Don't |
|----|-------|
| Pair with `btn`, `not-link`, or `btn-link` | Put `expanded-click-area` on a bare `<a>` |
| Put `relative` on the **smallest** wrapper that should receive the click | Put `expanded-click-area` on a link inside an unpositioned `<main>` or page grid |
| Give each expanded control its own bounded `relative` wrapper when neighbors are also clickable | Let multiple expanded hit zones share one unbounded ancestor |
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
- **Reversed panels** without `reading-typography` + `color_inherit` + `c_*` on the same node as `bg_*` — see [Reversed text panels](design-system.md#reversed-text-panels-color-on-color)

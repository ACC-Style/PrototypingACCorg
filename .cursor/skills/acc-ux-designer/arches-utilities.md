# Arches Utility Classes

Official docs: [Arches Documentation](https://assets.acc.org/Arches/Latest/docs/)  
Anatomy reference: [Utility Class Anatomy](https://assets.acc.org/Arches/Latest/docs/utility_classes/section-anatomy.html)

This workspace loads `acc_boot.css` + `acc_uc.css` (currently 5.0.0 CDN in `_includes/arches-head.html`).
Compose UI from utility classes — one class, one style. Do not invent CSS unless scoped to a generator preview.

## Class anatomy (read right to left)

Every utility follows this **ordered construction**:

```
[State:][StyleName][-Modifier]_[Value][-ValueModifier][:Breakpoint]
```

| Segment | Rule | Example |
|---------|------|---------|
| **State** | Optional; ends with `:` | `h:` → `:hover` |
| **Style name** | Shorthand for CSS property | `bg`, `p`, `m`, `c`, `font`, `br` |
| **Name modifier** | Optional; starts with `-` | `-t` top, `-x` horizontal, `-b` bottom |
| **Divider** | `_` means "equals" (value follows) | `p_4` → padding = step 4 |
| **Value** | Stepped number, keyword, or color role | `4`, `primary`, `solid`, `radius` |
| **Value modifier** | Optional; starts with `-` | `-n2` darker shade, `-5` lighter tint |
| **Breakpoint** | Optional; starts with `:` | `:md`, `:lg` |

### Worked examples

| Intent | Class | Decomposed |
|--------|-------|------------|
| Primary bg, darker on hover | `h:bg_primary-n2` | `h:` + `bg` + `_` + `primary` + `-n2` |
| 1rem top padding at md+ | `p-t_4:md` | `p` + `-t` + `_` + `4` + `:md` |
| Horizontal padding (this repo) | `p-x_4` | `p` + `-x` + `_` + `4` |
| Bottom margin negative overlap | `m-b_n3` | `m` + `-b` + `_` + `n3` |
| White text | `c_white` | `c` + `_` + `white` |
| Rounded border | `br_radius` | `br` + `_` + `radius` |

**Typing tip:** axis shortcuts (`-x`, `-y`, `-t`, `-r`, `-b`, `-l`) keep markup short vs four separate sides.

## Style name shorthand

| CSS property | Short | Has color modifier? | Stepped values? |
|--------------|-------|---------------------|-----------------|
| background-color | `bg` | yes | |
| color | `c` | yes | |
| border (color/width/radius) | `br` | yes | yes |
| margin | `m` | | yes |
| padding | `p` | | yes |
| font-size / family / weight / style | `font` | | yes |
| line-height | `lh` | | yes |
| width | `w` | | |
| max-width | `max-w` | | alt values |
| height | `h` | | |
| flex | `flex` | | |
| justify-content | `justify` | | |
| display | *(bare value)* | | alt values |
| position | *(bare value)* | | |
| top / right / bottom / left | `t` / `r` / `b` / `l` | | |
| overflow | `overflow` | | alt values |
| clear | `clear` | | |
| float | `float` | | |

## Name modifiers (sides & corners)

| Modifier | Applies to |
|----------|------------|
| `-t` | top |
| `-b` | bottom |
| `-l` | left |
| `-r` | right |
| `-x` | left + right |
| `-y` | top + bottom |
| `-tl` | top-left (border-radius) |
| `-tr` | top-right |
| `-bl` | bottom-left |
| `-br` | bottom-right |

## Stepped values (spacing, type, color)

Global spacing base **X = 1rem**.

| Step | Margin (incl. negative) | Padding | Line-height | Border-width | Color modifier |
|------|-------------------------|---------|-------------|--------------|----------------|
| `n5` | −2 × X | — | — | — | mix 90% black |
| `n4` | −1 × X | — | — | — | mix 70% black |
| `n3` | −0.5 × X | — | — | — | mix 50% black |
| `n2` | −0.25 × X | — | — | — | mix 30% black |
| `n1` | −0.1 × X | — | — | — | mix 10% black |
| `0` | 0 | 0 | 0 | 0 | base color |
| `1` | 0.1 × X | 0.1 × X | 1 | 1px | mix 10% white |
| `2` | 0.25 × X | 0.25 × X | 1.45 | 3px | mix 30% white |
| `3` | 0.5 × X | 0.5 × X | 1.65 | 5px | mix 50% white |
| `4` | **1 × X (1rem)** | **1 × X** | 1.75 | 0.5rem | mix 70% white |
| `5` | 2 × X | 2 × X | 2 | 1rem | mix 90% white |

**Default padding/gap in this repo:** `p_4`, `gap_4`, `m-b_4` (1rem).  
Newer builds may also expose step `6` — prefer `4`/`5` unless matching existing markup.

### Color value modifiers on roles

Pattern: `{role}` with optional `-n1`…`-n5` (darker) or `-1`…`-5` (lighter).

Roles are **functional** — the same class resolves to different hues per domain brand.  
Full hierarchy and font mapping: [cross-domain-branding.md](cross-domain-branding.md)

**ACC usage order:** `primary` → `shade`/`black`/`white` → `accent` → `secondary` (sparingly) → `highlight`/`info` (notifications/dialogs only)

```html
bg_primary-n1   <!-- header bands -->
bg_black-1      <!-- subtle panels -->
c_shade-n2      <!-- muted meta text -->
h:bg_accent-5   <!-- card hover -->
```

**Action colors** (feedback only): `alert`, `warning`, `success`, `navigation`

**Black/white** steps (`c_white-8`, `bg_black-1`, `bg_black-_05`) use **transparent rgba** — for layering on color/imagery. **Shade** and brand roles use opaque mixes.

Black/white alpha steps: `0`, `-_01`, `-_05`, `1`…`9`, `none` (solid).

## Alternate keyword values

### Border radius (`br_`)

| Value | Result |
|-------|--------|
| `square` | 0 |
| `radius` | 5px / global radius |
| `round` | 25px |
| `circle` | 100% |

### Border style (`br_`)

`solid`, `dashed`, `none`

### Display

`block`, `inline`, `inline-block`, `flex`, `none`  
Also responsive: `display_none:md`, `flex:md`

### max-width (`max-w_`)

Steps in **rem** — readable zones: `max-w_45`–`max-w_70`; page shells often `max-w_75`.

### Overflow

`auto`, `hidden`, `ellipsis`, `visible`, `scroll`, `clip`, `unset`

## Interaction states

| Prefix | Pseudo | Used in production |
|--------|--------|-------------------|
| `h:` | `:hover` | yes — `h:bg_accent-5`, `h:undecorated` |
| `a:` | `:active` | partial |
| `v:` | `:visited` | not used |

## Breakpoints

| Suffix | min-width | Used |
|--------|-----------|------|
| *(none)* | 0 | default (mobile-first) |
| `:sm` | 480px (30em) | rarely |
| `:md` | 640px (40em) | **yes** |
| `:lg` | 1024px | **yes** |

Apply mobile layout first, add `:md` / `:lg` overrides:

```html
<div class="flex flex_column flex_row:md gap_3 gap_4:lg p_4 p_5:lg">
<div class="grid columns_1 columns_2:md columns_3:lg gap_4">
```

## Reserved naming (components & states)

Use these words consistently — do not invent synonyms:

| Suffix / word | Meaning |
|---------------|---------|
| `-container` | UI wrapper |
| `-group` | repeatable collection |
| `-item` | child of container/group |
| `-separator` | visual break between items |

State classes: `is-active`, `is-current`, `is-selected`, `is-disabled`, `is-complete`, `show`, `hide`

Do not confuse **state classes** with **action color tokens** (`alert`, `warning`, `success`) — action colors are for user/system feedback per [Action Colors](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-designbase-colors-actions.html).

## Domain color codes

Separate stylesheets for product semantics — see [Color Codes](https://assets.acc.org/Arches/Latest/docs/color_codes/):

| Stylesheet | Use |
|------------|-----|
| `color-code_credits.css` | CME / accreditation |
| `color-code_LOE_COR.css` | Guidelines LOE & COR |
| `color-code_journals.css` | Journal branding |
| `color-code_social.css` | Social |

## Arches + Bootstrap in this repo

- `acc_boot.css` — Bootstrap base (buttons: `btn btn-primary`, grid legacy)
- `acc_uc.css` — utilities (primary composition layer)
- Prefer **`grid columns_*`** and **`flex`** over Bootstrap `row`/`col`
- Buttons: combine `btn` variants with UC spacing/sizing

## Quick compose patterns

```html
<!-- Card surface -->
<div class="bg_white br_1 br_black-3 br_radius br_solid shadow_bevel-light p_4">

<!-- Section with responsive gutters -->
<section class="reading-typography wrapper-container p-x_4 p-x_5:lg m-b_5">

<!-- Interactive row — relative bounds the ::after hit zone -->
<div class="relative isolation_isolate">
  <a class="block p_4 h:bg_accent-5 undecorated expanded-click-area" href="…">…</a>
</div>

<!-- Supporting CTA on white surface -->
<a class="btn btn-shade btn-sm expanded-click-area" href="…">Start Course</a>

<!-- Muted caption -->
<p class="c_shade-n2 font-size_down lh_3 m_0">
```

## When unsure

1. Check [section-anatomy](https://assets.acc.org/Arches/Latest/docs/utility_classes/section-anatomy.html) for shorthand tables
2. Grep `assets/css/acc_uc.css` for the exact class name
3. Copy classes from `_collections/_ui_gold_standard/` — do not guess syntax

---
name: Brand Theme Generator
overview: Build an interactive brand theme generator tool at `_collections/_annual_meeting_prototype/brand-generrator.liquid` that lets users pick colors and fonts via UI controls, dynamically updating the CSS custom properties defined in `_includes/annual/root.html` so they can preview rebranding in real-time.
todos:
  - id: build-generator-page
    content: Build the full brand-generrator.liquid file with HTML structure, control panel inputs (color pickers, font selects, range slider), live preview section, and generated code output block
    status: completed
  - id: implement-js-logic
    content: "Write the vanilla JS: hexToHSL conversion, CSS variable updater, dynamic Google Font link injection, fallback chain builder, and code output regeneration"
    status: completed
  - id: add-preview-section
    content: Create the live preview area with sample headings, body text, buttons, and color swatches that respond to CSS variable changes
    status: completed
isProject: false
---

# Brand Theme Generator Tool

## Architecture

The tool lives in [`_collections/_annual_meeting_prototype/brand-generrator.liquid`](_collections/_annual_meeting_prototype/brand-generrator.liquid) using the existing `playground` layout. It will contain:

1. **A control panel** (sidebar or top panel) with inputs for each configurable token
2. **A live preview area** showing sample page elements styled by CSS variables
3. **A generated `<style>` block** (read-only code output) mirroring the format of [`_includes/annual/root.html`](_includes/annual/root.html)

## CSS Variables to Control

Derived from the existing `:root` block:

- **Page max width** -- `--page-max-width` (range slider, 900px-1600px)
- **Page Backdrop color** -- `--page-backdrop-color` (single color picker, set as a single color variable). This is the color **beyond the page edges** — the browser gutters left/right of the centered content column (e.g. the dark green flanking the white page on ACC.27). Applied to `body` (or the full-bleed stage behind the page); the page surface itself stays white / content-colored.
- **Brand/ACC color** -- `--acc-h/s/l` (single color picker, decomposed to HSL)
- **Primary color** -- `--primary-h/s/l` (color picker)
- **Accent color** -- `--accent-h/s/l` (color picker)
- **Highlight color** -- `--highlight-h/s/l` (color picker)
- **Secondary color** -- `--secondary-h/s/l` (color picker)
- **Shade color** -- `--shade-h/s/l` — **auto-derived from Primary**, not a free picker. Formula: a **50% lightness mid-grey** (`#808080` / `hsl(0 0% 50%)`) mixed with **5% Primary** (RGB/sRGB mix ≈ `color-mix(in srgb, var(--primary) 5%, hsl(0 0% 50%) 95%)`). Result is a near-neutral warmed or cooled slightly by the primary hue. Recomputed whenever Primary changes; shown read-only in the control panel.
- **Font: Accent** -- `--font-family_accent` (Google Fonts picker, serif category)
- **Font: Display** -- `--font-family_display` (Google Fonts picker, sans-serif category)
- **Font: Copy/UI** -- `--font-family_copy` / `--font-family_ui` (Google Fonts picker, sans-serif category)

System state colors (success, warning, alert, info) will be left at defaults but could be optionally exposed. **Shade is not a free system default** — it is derived from Primary as above.

## Input Controls Design

### Color Pickers
- Use native `<input type="color">` elements
- On change, convert hex to HSL using vanilla JS (`hexToHSL` utility function)
- Write decomposed `--*-h`, `--*-s`, `--*-l` values onto `document.documentElement.style`
- The composed `--*` variable automatically updates via `hsl(var(--*-h), var(--*-s), var(--*-l))`

### Font Family Picker
- A `<select>` dropdown with curated Google Fonts grouped by category:
  - **Serif/Slab** (for accent): Roboto Slab, Playfair Display, Merriweather, Lora, etc.
  - **Sans-serif** (for display/copy/ui): Maven Pro, Open Sans, Inter, Lato, Montserrat, Raleway, etc.
- On change, dynamically inject a `<link>` to load the chosen Google Font CSS
- Build the fallback chain based on font category:
  - Serif: `"[chosen]", "Times New Roman", "Lucida Bright", Georgia, serif`
  - Sans-serif: `"[chosen]", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`
  - Slab-serif: `"[chosen]", "Times New Roman", "Lucida Bright", Georgia, serif, "slab"`

### Page Max Width
- `<input type="range">` with min 900, max 1600, step 50, showing the current value in px

## Live Preview

A section below/beside the controls containing sample elements that use the CSS variables:
- Include this html this will showcase the branding graphic that we have from creative.
```html
<picture class="bg_no-repeat brand-header col_all row_all w_100" aria-hidden="true">
<source media="(min-width: 1040px)" srcset="https://www.acc.org/-/media/ScientificSessions/BannerImages/header1040.jpg">
<source media="(min-width: 992px)" srcset="https://www.acc.org/-/media/ScientificSessions/BannerImages/header1000.jpg">
<source media="(min-width: 781px)" srcset="https://www.acc.org/-/media/ScientificSessions/BannerImages/header980.jpg">
<source media="(min-width: 500px)" srcset="https://www.acc.org/-/media/ScientificSessions/BannerImages/header780.jpg">
<img src="https://www.acc.org/-/media/ScientificSessions/BannerImages/header320.jpg" alt="" class="bg_no-repeat w_100">
</picture>
```
- **Main nav (Arches pattern)** — live preview uses the current `#header_nav-arches` DOM (not Bootstrap `navbar` / `navbar-collapse`). Color / type tokens exercised by the pattern:
  - Bar / collapse shell: `bg_acc`, `bg_acc-n1`, `font_accent`
  - Toggle: `h:bg_accent-4`, `a:bg_primary-n1`, `a:c_acc-2`, `c_white`
  - Links: `a:bg_primary-n1`, `h:bg_accent-n1`, `c_white`
  - Submenu panel: `bg_white`, `font_copy` / `font_ui`, items `h:bg_accent-4`, `a:bg_primary-3`
```html
<nav id="header_nav-arches" class="flex_auto p_0 bg_acc font_2 font_1:md relative" aria-label="Main navigation">
  <!-- toggle row + navbar-collapse-arches + navbar-nav-arches tabs / submenu panels -->
</nav>
```
- Heading (font_display), subheading (font_accent), body text (font_copy)
- Buttons styled with `--primary`, `--accent`, `--shade`
- A card/container constrained to `--page-max-width`
- Color swatches showing all active color tokens
- **Page backdrop demo** — preview stage uses `--page-backdrop-color` as the full-bleed background; the white `.brand-preview-page` column is centered at `--page-max-width`, so left/right gutters show the backdrop (same relationship as body vs page on ACC.27)


## Generated Output

A `<pre><code>` block at the bottom that renders the full `:root { ... }` style block reflecting the current selections (same format as `root.html`), so users can copy-paste the result.

## File Changes

### Primary file: `_collections/_annual_meeting_prototype/brand-generrator.liquid`

This single file will contain all the HTML, CSS, and JavaScript for the tool. The front matter will use `layout: playground`.

### No changes to existing files

The existing `root.html`, layouts, and includes remain untouched. The generator is a standalone utility.

## Key Implementation Details

- **hexToHSL JS function**: converts `#rrggbb` from the color picker to `{ h: "XXdeg", s: "XX%", l: "XX%" }`
- **updateCSSVariable(prefix, hsl)**: sets `--{prefix}-h`, `--{prefix}-s`, `--{prefix}-l` on `:root`
- **Font loading**: dynamically appends `<link>` elements for Google Fonts API URLs on font selection change
- **Code output sync**: on any input change, regenerate the text content of the code output block
- All state lives in the DOM and JS variables (no framework needed)

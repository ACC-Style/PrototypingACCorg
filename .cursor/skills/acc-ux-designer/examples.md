# Examples Index

Start here when implementing. Open the file, copy structure, adapt content.

## Gold standard (highest fidelity)

| File | Pattern |
|------|---------|
| `_collections/_ui_gold_standard/card-segmented.html` | Colored header card + footer CTA + metadata aside |
| `_collections/_ui_gold_standard/photo-text-lockup.html` | Image + HTML text (not text-in-image) + pipe-linked actions |
| `_collections/_ui_gold_standard/Concept-Anchor-Hero.html` | **Anchor hero** — capstone silo, feature cutout, domain brand |

Archive (still useful): `_ui_gold_standard/_archive/follow-up-cta.html`, `card-basic.html`, `split-content-block-thirds.html`

## Prototypes

| File | Pattern |
|------|---------|
| `__prototypes/MicroSite/heroimage.html` | **Section hero** — full band + required CTA overlay |
| `__prototypes/MicroSite/heroimage.micro.dynamic.html` | **Section child** — micro banner echo |
| `__prototypes/_archive/CMP-Marketing.html` | **Product hero** — product name + branding |
| `__prototypes/Concept-EDU-MEETING.html` | Full concept using `hero-area` grid |
| `__prototypes/Course-Compact.html` | Topic + article cards |
| `__prototypes/CTA-Gallery.html` | CTA variations |
| `__prototypes/PageBlocks/Cards.html` | Data-driven card grid from `site.data` |

## Generators (CMS output)

| File | Pattern |
|------|---------|
| `__generators/award_schedule.html` | DateList/DateCard + CSV + runtime IIFE |
| `__generators/international_event_list.html` | Event cards from CSV |
| `__generators/ListGenerator.html` | Icon-decorated lists |
| `__generators/Person-Cards.html` | Person cards with `<template>` |
| `__generators/Follow Up CTA.html` | CTA block builder |
| `__generators/SponsorBlocks.html` | Tiered sponsor grids |

Sub-partials: `__generators/subs/date-card.html`, `event-card.html`, `faq.html`

## Member / gated

| File | Pattern |
|------|---------|
| `_member_section_prototype/0_page-blocker-login.html` | Login roadblock grid |
| `_member_section_prototype/3.0_home.html` | Member home |

## Snippet: section intro

```html
<section class="reading-typography wrapper-container m-b_5">
  <h2 class="font_display font_3 m-b_3">Section Title</h2>
  <p class="c_shade-n2 m-b_4">Supporting copy.</p>
  <div class="grid columns_1 columns_2:md gap_4">
    <!-- cards -->
  </div>
</section>
```

## Snippet: sticky generator preview header

```html
<section class="bg_white br_1 br_black-3 br_round br_solid overflow_hidden sticky t_3 z_1">
  <header class="bg_black-1 br-b_1 br_black-3 br_solid font_bold p_4">Live preview</header>
  <div class="bg_black-1 br-b_1 br_black-3 br_dashed p_4">
    <div id="previewArea" class="reading-typography wrapper-container"></div>
  </div>
</section>
```

## Snippet: playground form field

```html
<label class="font_bold font-size_down" for="fieldId">Label</label>
<textarea id="fieldId" class="br_1 br_black-3 br_round br_solid font_n1 m_0 min-h_20 p_3 w_100" rows="14"></textarea>
```

## Adding new examples

When you ship a pattern worth reusing:
1. Add a row to the table above
2. If it introduces a new component contract, document it in [components.md](components.md)
3. For complex flows, add a `patterns/{name}.md` file and link from SKILL.md

# Component Patterns

## Attribute layers

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `data-component` | Named component root; CMS + JS entry | `DateList`, `DateCard`, `EventCard` |
| `data-role` | Functional sub-region | `source`, `open`, `card-footer`, `flag-list` |
| `data-item` | Hero/CTA semantic regions | `hero-title`, `cta-callout` |
| `data-element` | Table/structural parts | `data-table`, `tagline` |
| `label="…"` | Dev/CMS annotation (not `data-*`) | `label="Cards"` |

Prefer `data-component` on the outermost interactive unit authors will recognize.

## Expanded click area

Use `expanded-click-area` (or `expanded-click-area-beforeAlt`) when a small visible control should receive clicks across a larger region — e.g. a footer button that activates the whole card.

The utility uses an absolutely positioned pseudo-element. **Bound the click zone** with a `relative` wrapper around the intended target area. Without it, the pseudo-element can expand to a distant positioned ancestor and hijack clicks across the page.

```html
<div class="relative isolation_isolate br_1 br_black-3 br_radius br_solid">
  <h2 class="bg_primary-n1 c_white font_3 font_display p_3 p_4:lg">Title</h2>
  <p class="p_4 reading-typography m_0">…</p>
  <footer class="relative isolation_isolate br-t_1 br_black-2 br_dotted grid items_center justify_center p-y_3">
    <a href="#" class="btn btn-shade expanded-click-area">Start Here</a>
  </footer>
</div>
```

For a full-card link, put `relative` on the card and `expanded-click-area` on the `<a>` inside it. See [design-system.md](design-system.md#expanded-click-area).

## Segmented card

Reference: `_collections/_ui_gold_standard/card-segmented.html`

```html
<div class="br_1 br_black-3 br_radius br_solid isolation_isolate relative">
  <h2 class="bg_primary-n1 c_white font_3 font_display p_3 p_4:lg">Title</h2>
  <ul class="font_copy p_4 reading-typography ul_none">…</ul>
  <footer class="relative isolation_isolate br-t_1 br_black-2 br_dotted grid items_center justify_center p-y_3">
    <a href="#" class="btn btn-shade expanded-click-area">Start Here</a>
  </footer>
  <aside class="bg_black-2 br-t_1 br_solid p_3 font-size_down-2">…</aside>
</div>
```

## Photo + text lockup

Reference: `_collections/_ui_gold_standard/photo-text-lockup.html`

Preferred alternative to **text-in-image** tiles: photo carries mood or humanization; headline, body, and links stay in HTML beside the image. See [imagery.md](imagery.md).

```html
<div class="columns_1 columns_4:sm grid:sm flex flex_column gap_4 …">
  <div class="p-x_4">
    <img class="br_radius w_100 aspect_1x1 bg_cover shadow_bevel-light" alt="…" src="…">
  </div>
  <div class="col-start_2 col-end_end">
    <h4 class="font_display">…</h4>
    <p>…</p>
    <ul class="ul_inline-pipe">
      <li><a class="expanded-click-area-beforeAlt">Learn More<i class="fas fa-arrow-right p-x_3"></i></a></li>
    </ul>
  </div>
</div>
```

## Date card (CMS-portable)

Reference: `__generators/subs/date-card.html`, `award_schedule.html`

```html
<article class="bg_white br_round flex flex_column shadow_bevel-light wrapper-container h:bg_accent-5"
         data-component="DateCard"
         data-end-date="MM-DD"
         data-action-url="…"
         data-learn-more-url="…">
  <div class="flex flex_row:md flex_column gap-x_4 gap-y_3 p_4 flex_1">
    <div class="flex_none" style="width: clamp(120px, 15vw, 140px);">
      <div class="cal-date text_center">
        <a class="aspect_4x3 block btn btn-primary c_white expanded-click-area flex flex_column font-size_down justify_center" …>
          <span class="aspect_3x1 block br-b_2 br_solid font-size_up-1 font_xbold grid items_center m-t_auto p-x_4 text_center">
            <span class="nowrap">Jul - Sep</span>
          </span>
          <span class="block flex_none font-size_up-1 m-b_auto p-y_1">2026</span>
        </a>
      </div>
    </div>
    <div class="flex_auto flex flex_column gap-y_3">
      <header>…flags…<h3 data-type="title">…</h3></header>
      <main class="reading-typography font-size_down flex_1">…</main>
      <footer data-role="card-footer">…</footer>
    </div>
  </div>
</article>
```

## Date list runtime

`data-component="DateList"` with flat `data-role="source"` list.
Runtime script partitions into Open / Upcoming / Past, applies status styling, injects footers.

Config on root: `data-heading-open`, `data-open-label`, `data-action-label`, etc.

## Flag list (inline pipes)

```html
<ul class="ul_inline-pipe font_n3 c_accent-n3 items_center w_auto font_bold m-t_0 m-b_3 flex" data-role="flag-list">
  <li>International</li>
  <li class="no-after">Early Career</li>
</ul>
```

## Icon-decorated list chunk

Use dictionary icons for each row concept — see [icons.md](icons.md).

```liquid
{% include Blocks/IconDecoratedLists.html data_path="Blocks.IconDecoratedLists" %}
```

```html
<i class="c_accent-n1 far fa-book-medical font_4 m-r_3" aria-hidden="true"></i>
```

## Hero treatments

Three IA-driven types — **do not mix**. Full spec: [heroes.md](heroes.md)

| Type | Template | CTA | Child echo |
|------|----------|-----|------------|
| Anchor (capstone silo) | `grid-template="hero-area"` | Featured business goal in cutout | — |
| Section (initiative) | `hero-image-cta` | **Required** `cta-overlay` | Micro banner (`template-option="micro"`) |
| Product | `hero-image-cta` | Product action (optional) | **None** |

Gold anchor: `_ui_gold_standard/Concept-Anchor-Hero.html`  
Section: `__prototypes/MicroSite/heroimage.html` + `heroimage.micro.dynamic.html`  
Product: `__prototypes/_archive/CMP-Marketing.html`, `MicroSite/heroimage.basic.ai.html`

## Follow-up CTA

```liquid
{% include Blocks/FollowUpCTA.html data_path="Blocks.FollowUpCTA" button_type="primary" cta_type="bevel" %}
```

## Page blocker / login

Reference: `_collections/_member_section_prototype/0_page-blocker-login.html`

Uses `grid-template-page-blocker` and gated content patterns.

## Generator panel chrome

Interactive builders use:

```html
<section class="bg_white br_1 br_black-3 br_round br_solid overflow_hidden">
  <header class="bg_black-1 br-b_1 br_black-3 br_solid font_bold p_4">…</header>
  <div class="flex flex_column gap_4 p_4">…</div>
</section>
```

Preview area: `#previewArea` inside sticky header section.

## Component checklist

- [ ] Root `data-component` if JS or CMS authoring depends on it
- [ ] `data-type="title"` / `data-type="description"` on list card fields
- [ ] Footer actions only when status warrants (open items)
- [ ] `aria-label` on date badges and icon-only buttons
- [ ] `target="_blank"` on external ACC links where prototypes already do

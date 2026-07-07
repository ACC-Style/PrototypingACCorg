# Refactor UI Patterns

Map content chunks to Arches markup already in this repo.  
Apply [acc-ux-designer](../acc-ux-designer/design-system.md) color and button rules.

## Pattern index

| Pattern | Best for | Ref |
|---------|----------|-----|
| Topic hub tiles | Hub & spoke, skip nav | `Course-Compact.html` |
| Card grid | Parallel items, scanability | `PageBlocks/Cards.html` |
| Segmented card | One topic + list + CTA + meta | `card-segmented.html` |
| Photo + text lockup | Feature highlight chunk | `photo-text-lockup.html` |
| Icon decorated list | Benefits, features (no wall of bullets) | `PageBlocks/IconDecoratedLists.html` |
| Follow-up CTA row | Section closer, next step | `Blocks/FollowUpCTA.html` |
| Page blocker | Audience gate + teaser | `0_page-blocker-login.html` |
| Section teaser | Show value before join/login | `AccessBarred.SectionTeaser.html` |
| **Process-stage CTA fork** | Product journey hub — stage cards → child pages | CMP hub, `CMP-Marketing.html` |
| **Journey wizard widget** | Current step in product process | `CMP/interactive_wizard.html` |
| **Enrolled Next Steps card** | Numbered actions for active users | `CTA-Gallery.html` |
| Anchor / jump nav | Return visitors, long pages | `AnchorPageNav.html` |
| Date/status lists | Time-sliced content | `award_schedule.html` |
| Hero + short intro | Replace long header prose — pick correct hero tier first | [heroes.md](../acc-ux-designer/heroes.md) |
| **Microsite pattern set** | Initiative hub + sub pages (root hero, micro branding, linked grids, footer CTA) | [microsite-patterns.md](../acc-ux-designer/microsite-patterns.md) |
| Accordion (strategic) | Return-visit / reference depth on product pages | [accordions.md](accordions.md), `SAP/wrap-up-content.html` |

## Topic hub tiles

Skimmable branch picker — icon, title, count, hover.

```html
<nav aria-label="Topics">
  <ul class="columns_2 columns_4:md gap_3 grid ul_none m_0 p_0">
    <li>
      <a href="#section-id" class="bg_black-1 br_round display_block p_4 h:bg_accent-5 not-link h:undecorated">
        <i class="c_accent-n1 far fa-university font_4" aria-hidden="true"></i>
        <strong class="block font_display font-size_up">Topic Name</strong>
        <span class="c_black-7 font-size_down-2">Short count or descriptor</span>
      </a>
    </li>
  </ul>
</nav>
```

Reference: `__prototypes/Course-Compact.html`

## Card grid chunk

One idea per card; grid scales by breakpoint.

```liquid
{% include Blocks/Cards.html data_path="Blocks.Cards" grid_modifier="columns_3:lg columns_2:md columns_1 gap_4 grid" %}
```

Or hand-roll:

```html
<div class="grid columns_1 columns_2:md columns_3:lg gap_4">
  <article class="bg_white br_1 br_black-3 br_radius br_solid p_4 shadow_bevel-light flex flex_column gap_3">
    <h3 class="h4 font_display m_0">Chunk title</h3>
    <p class="font-size_down m_0 flex_1">One or two sentences max.</p>
    <a class="btn btn-shade btn-sm expanded-click-area m-t_auto" href="#">Action</a>
  </article>
</div>
```

## Segmented card chunk

Colored header = skim label; body = supporting points; footer = single action.

Reference: `_ui_gold_standard/card-segmented.html`

## Section shell

Wrap refactored chunks:

```html
<section class="reading-typography wrapper-container m-b_5">
  <header class="m-b_4">
    <h2 class="font_display font_3 m-t_0 m-b_2">Section title</h2>
    <p class="c_shade-n2 m_0">One sentence — why this section exists.</p>
  </header>
  <!-- chunks -->
</section>
```

## Intro compression

**Legacy pattern (avoid):**

```html
<h2>Title</h2>
<p>Paragraph 1…</p>
<p>Paragraph 2…</p>
<p>Paragraph 3…</p>
<!-- then content -->
```

**Refactored pattern:**

```html
<h2 class="font_display m-b_3">Title</h2>
<p class="m-b_4">One combined lead sentence.</p>
<!-- immediate hub tiles or card grid -->
```

Move background/history copy to **About** child page or collapsed aside.

## Audience fork (blocker)

Teaser shows value; gate shows requirement; help shows escape hatch.

```html
<section grid-template="page-blocker" class="bg_secondary-1 grid-template-page-blocker">
  <!-- AccessBarred.SectionTeaser, join CTA, NeedHelp -->
</section>
```

Reference: `_member_section_prototype/1_page-blocker-member.html`

## Process-stage CTA fork (product journey hub)

Divide by **where the user is in the product**, not only by login. Hub foreshadows the journey; each stage gets its own page for IA, CMS, and campaign deep links.

**Live reference:** [Collaborative Maintenance Pathway](https://www.acc.org/Education-and-Meetings/Maintenance-of-Certification-Information-Hub/Collaborative-Maintenance-Pathway)

```html
<!-- Hub: three parallel stage cards after short intro -->
<div class="grid columns_1 columns_3:lg gap_4">
  <article class="bg_white br_1 br_black-3 br_radius br_solid p_4 flex flex_column shadow_bevel-light">
    <h3 class="font_bold font_display m-t_0">What is the CMP?</h3>
    <p class="flex_1">Discover how the CMP works and view topics by year and specialty.</p>
    <a href="…/What-is-the-CMP" class="btn btn-shade m-t_auto expanded-click-area">Learn More</a>
  </article>
    <article class="bg_white br_1 br_black-3 br_radius br_solid p_4 flex flex_column shadow_bevel-light">
    <h3 class="font_bold font_display m-t_0">Enroll in the CMP</h3>
    <p class="flex_1">Verify eligibility and begin enrollment.</p>
    <a href="…/Enroll-in-the-CMP" class="btn btn-primary m-t_auto expanded-click-area">Enroll Now</a>
    <small class="text_center c_shade-n2">Login required.</small>
  </article>
  <article class="bg_white br_1 br_black-3 br_radius br_solid p_4 flex flex_column shadow_bevel-light">
    <h3 class="font_bold font_display m-t_0">Already Enrolled</h3>
    <p class="flex_1">Next steps and current-year topics by specialty.</p>
    <a href="…/Already-Enrolled-in-the-CMP" class="btn btn-shade m-t_auto expanded-click-area">Next Steps</a>
  </article>
</div>
```

**Design rules:**

- Hub holds **overview only** — dates, SAP matrices, assessment windows live on stage-specific child pages
- One **primary** CTA per stage card (`btn-primary` on the main conversion step; `btn-shade` on explore/return paths)
- Hero may reinforce entry CTA (`Get Started` / `Enroll`) for users who already know their intent
- Sidebar or embedded **wizard** reflects authenticated state (Login → Eligibility → Progress → Status)

**Prototype refs:** `__prototypes/_archive/CMP-Marketing.html`, `__ui_playground/CMP-Wizard.html`, `__ui_playground/CMP/heroimage.html`

## Enrolled-user Next Steps card

For users already in the product — numbered steps, status badge, product-specific links. Avoids re-reading enrollment content.

Reference: `__prototypes/CTA-Gallery.html` — `amsproductid="CMP"` article with "CMP Next Steps", enrolled badge, numbered launch steps.

## Skip link for return visitors

Place **before** intro prose:

```html
<nav aria-label="Jump to">
  <ul class="ul_inline-pipe font-size_down">
    <li><a href="#open-items">Open</a></li>
    <li><a href="#resources">Resources</a></li>
  </ul>
</nav>
```

For large taxonomy pages, see `AnchorPageNav.html` sidebar + section structure.

## Strategic accordion (product pages)

Use native `<details>` / `<summary>` for **second-visit and reference** content only — not to shorten first-pass value. Shared labels across a product line, stable `id` on bodies for deep links, no JS-driven disclosure.

Full rules: [accordions.md](accordions.md)  
Refs: [ACCSAP](https://www.acc.org/Education-and-Meetings/Products-and-Resources/SAP/ACCSAP), `__prototypes/SAP/wrap-up-content.html`, `__ui_playground/_archive/Accordion.html`

## List chunk (icon + headline + text)

```liquid
{% include Blocks/IconDecoratedLists.html data_path="Blocks.IconDecoratedLists" %}
```

Each row: icon + **bold lead** + short body — not multi-sentence bullets.

## Section rhythm

Between major chunks on a refactored page:

- `m-b_5` or `m-b_6:lg` between sections
- `gap_4` / `gap_5:lg` inside grids
- `p-x_4 p-x_5:lg` horizontal gutters
- Optional `FollowUpCTA` once per major section — not per card

## When NOT to use a pattern

| Avoid | Instead |
|-------|---------|
| Accordion for main navigation | Hub tiles or child pages |
| Accordion to hide first-visit value | Keep visible; accordion only reference depth ([accordions.md](accordions.md)) |
| JS accordion widgets | Native `<details>` / `<summary>` |
| Tabs with 8+ panels | Hub & spoke |
| `btn-secondary` for every card | `btn-shade` supporting actions |
| Full prose in hero | Title + one line; detail below fold |
| Single `reading-typography` div wrapping entire page | Section per chunk with headers |

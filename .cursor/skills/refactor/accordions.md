# Strategic Accordions

ACC uses accordions **strategically** on product pages and brochureware — not as a shortcut to shorten pages.  
Live reference: [ACCSAP](https://www.acc.org/Education-and-Meetings/Products-and-Resources/SAP/ACCSAP)

## Five rules

| # | Rule | Implication |
|---|------|-------------|
| 1 | **Native HTML only** | Use `<details>` / `<summary>`. Do not use JavaScript accordion widgets, plugins, or click handlers to show/hide body content. |
| 2 | **Shared label patterns** | When the same accordion types appear across a product family, use **identical summary labels** (CMS consistency, user recognition). |
| 3 | **Deep-link IDs** | Put a stable `id` on the revealed content container so URLs like `#credit-information` open the right panel. |
| 4 | **Second-visit / deep-info only** | Hidden content is for return visitors or users who need reference detail — not first-pass decision-making. |
| 5 | **Not a length hack** | If content is valuable on first visit, keep it **visible and scrollable**. Accordions defer depth; they do not bury primary value. |

## When to use

**Good candidates (hide in accordion):**

- Table of contents / curriculum outline
- Learner objectives
- Credit / CME / MOC boilerplate
- Release and expiration dates
- Refund policy
- FAQ answers
- Faculty lists, long accreditation blocks
- Compliance or legal detail a purchaser confirms once

**Keep visible (do not accordion):**

- Product value proposition and who it's for
- Primary purchase / enroll CTA context
- Pricing headline and key benefits
- Anything needed for a **first-time** explore → decide → act path
- Copy that competitors surface on the skim path (see [readability benchmarks](../readability/benchmarks.md))

## Shared SAP product labels

Use these **exact summary labels** across SAP and sibling product pages when the content type matches:

| Summary label | Typical content |
|---------------|-----------------|
| **Table of Contents** | Curriculum / module list |
| **Learner Objectives** | "Upon completion, learners should be able to…" |
| **Credit Information** | Joint accreditation, ABIM MOC, designation statements |
| **Release Date & CME/MOC Expiration Date** | Product version dates |
| **Refund Policy** | 7-day / credit-claim rules |

Prototype: `_collections/__prototypes/SAP/wrap-up-content.html`

FAQ pages use question-as-summary pattern; keep questions consistent across products when the FAQ is shared.

Prototype: `_collections/__prototypes/_archive/SAP-FAQ.html`

## Markup — native `<details>`

**Minimum (SAP product wrap-up):**

```html
<details class="m-b_3">
  <summary class="p-x_3 link"><strong>Credit Information</strong></summary>
  <div id="credit-information" class="p_3 br_radius bg_black-1 reading-typography">
    <!-- reference content -->
  </div>
</details>
```

**Styled product accordion** (sticky summary, inset body, grouped `name`):

Reference: `_collections/__ui_playground/_archive/Accordion.html`

```html
<details accordion name="product-details" class="isolation_isolate m-b_3">
  <summary class="sticky inset_0 b_auto z_3 bg_white h:bg_primary-5 c_primary-n2 br_radius shadow_bevel-light br_solid br_1 br_black-2">
    <hgroup class="flex flex_row">
      <span class="fa-stack flex_shrink m_2 br_radius" aria-hidden="true">…</span>
      <h3 class="flex_auto m-y_2 inline-block self_center">Credit Information</h3>
    </hgroup>
  </summary>
  <div data-container id="credit-information"
    class="z_0 bg_black-_05 br-bl_radius br-br_radius m-x_3:md p_3 p_4:md reading-typography shadow_emboss-light m-b_2">
    <!-- reference content -->
  </div>
</details>
```

### What counts as "no JavaScript accordion"

| Allowed | Not allowed |
|---------|-------------|
| `<details>` / `<summary>` native toggle | Custom accordion components driven by click JS |
| CSS for open/closed styling (`details[open]`, `[accordion]` attr) | Replacing `<details>` with div + `display:none` toggled by script |
| Optional **hash helper** that sets `details.open = true` when URL has `#id` | Accordion behavior that **requires** JS to open at all |

The hash helper in `Accordion.html` only **opens** a panel when linked — it does not replace native disclosure.

## Deep linking

1. Assign `id` on the **revealed content** `div` (kebab-case, stable across publishes).
2. Match marketing/support links: `…/ACCSAP#credit-information`
3. Ensure `scroll-margin` on content below summary so sticky headers do not cover the target (`summary + * { scroll-margin-block-start: … }` in accordion CSS).
4. Prefer IDs on accordion **bodies**, not on `<summary>`, so the user lands in the expanded content.

## Refactor workflow placement

Accordions come **after** chunking — never as step 1:

1. Chunk page into skim-visible cards, hero, CTAs
2. Classify remaining blocks: first-visit vs return-visit / reference
3. Move reference blocks into accordions **or** child pages
4. Apply shared labels + IDs
5. Run [readability pass](../readability/SKILL.md) — hiding dense prose in accordions does **not** improve readability scores; rewrite and cut first

## Anti-patterns

- One mega-accordion hiding an unmaintained wall of text — **chunk first**, then optionally collapse reference sections
- Different labels for the same content type on sibling SAP pages ("CME Info" vs "Credit Information")
- Accordion for primary navigation — use hub tiles or child pages ([patterns.md](patterns.md))
- Hiding the only CTA or pricing context to "clean up" the page
- JS-only accordion with no progressive enhancement fallback

## Related

- [strategies.md](strategies.md) — progressive disclosure
- [patterns.md](patterns.md) — pattern index
- [readability/checklist.md](../readability/checklist.md) — accordion does not fix dense copy scores

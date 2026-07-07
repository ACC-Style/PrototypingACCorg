# Microsite UI Patterns

Standard ACC patterns for **initiative microsites** — connected content families with a concept root and sub pages. Read this when building hub/spoke pages (e.g. Clinician Well-Being, Career Path).

Official Arches docs: [boot_acc components](https://assets.acc.org/Arches/Latest/docs/boot_acc/)

Pair with [heroes.md](heroes.md) for hero tier rules (Section hero + micro echo).

---

## Page shell decision tree

```
Is this the concept ROOT (main entry for the initiative)?
  → Fullscreen layout (no left sidebar)
  → Hero Image with CTA
  → Two-lane forks, linked icon grids (3–7), quotes, key-point grids

Is this a SUB PAGE under the concept?
  → Layout gains left sidebar + side navigation
  → Micro Branding with CTA Button (branding echo)
  → Body patterns below
  → Optional Follow Up CTA at page end

How many featured items in a group?
  → Fewer than 3     → Small Image-Text Panel (one per feature)
  → 3 to 7           → Grid List with Linked Descriptions
  → Key concepts     → Grid List with Descriptions (icon + text, not all linked)

Is content 4th priority or boilerplate/legal?
  → Accordion (rare — last resort)
```

---

## Pattern catalog

| Pattern | When to use | Docs |
|---------|-------------|------|
| **Hero Image with CTA** | Concept **root** — fullscreen microsite entry; connected content section with mission + primary conversion | [item-component-microsite-heroimagewithcta.html](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-component-microsite-heroimagewithcta.html) |
| **Micro Branding with CTA Button** | **Sub pages** — thin hero echo of parent branding; page adds sidebar + side nav | [item-component-microsite-microbrandingwithbuttton.html](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-component-microsite-microbrandingwithbuttton.html) |
| **Follow Up CTA — Beveled Card** | **End of sub page** when a primary callback action is needed | [item-recipes-page-followupcta-beveledcard.html](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-recipes-page-followupcta-beveledcard.html) |
| **Small Image-Text Panel with CTA** | **Fewer than 3** featured items in a group — one panel per feature | [item-recipes-page-panel-small-image-text-cta.html](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-recipes-page-panel-small-image-text-cta.html) |
| **Decorative Quote** | Humanizing voice — impact, quality, member/faculty perspective (not ACC marketing alone) | [item-recipes-quote-decrative.html](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-recipes-quote-decrative.html) |
| **Accordion** | **Rare.** 4th-priority content that must exist but is too long for the page — boilerplate, legal | [item-component-accordion.html](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-component-accordion.html) |
| **Grid List with Descriptions** | **Key points** or major concept callouts — icon + header + description | [item-recipes-gridlist-icontext.html](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-recipes-gridlist-icontext.html) |
| **Grid List with Linked Descriptions** | **3–7** featured items — scannable, graphic impact, human context for why to click | [item-recipes-gridlist-linkedicontext.html](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-recipes-gridlist-linkedicontext.html) |

---

## 1. Hero Image with CTA (concept root)

**Use on:** Main root of a concept microsite. Page is **fullscreen** (no sidebar).

**Purpose:** Hero for a **section of connected content** — mission statement + primary CTA that engages users with the page goal.

**Technical:**
- `grid-template="hero-image-cta"`
- `data-item="responsive-hero-image"` — breakpoint art
- `data-item="hero-image-breadcrumb-nav"` — back to parent silo
- `data-item="hero-title"` / page title
- `data-item="cta-callout"` — `cta-title`, `cta-description`, `btn-primary`

**Repo:** `__prototypes/MicroSite/heroimage.html`, [heroes.md § Section Hero](heroes.md)

**Do not use on** sub pages (use micro branding instead).

---

## 2. Micro Branding with CTA Button (sub pages)

**Use on:** Sub pages under the concept root.

**Purpose:** Visual **echo of parent branding** so users know they are still in the initiative. Page shell gains **left sidebar + side navigation**.

**Technical:**
- `grid-template="hero-image-cta"` + `template-option="micro"`
- Same responsive image family as parent (sliced thin)
- `data-item="hero-title"` — short title; mobile back arrow to root
- Compact optional `btn-primary` in `grid-area="cta"`

**Layout:** `masthead: MicroSite/heroimage.micro.dynamic.html` on spoke pages. Layout passes `hero_title`, `hero_image_base`, optional `hero_image_dir` / `hero_image_ext`, `cta_text`, `cta_link`, and `parent_link` (hub URL). Defaults come from `_data/{Initiative}/hero.yml` when the layout assigns them.

**Repo:** `_includes/MicroSite/heroimage.micro.dynamic.html` (global); initiative art via `hero.yml` + params — not collection hero partials.

---

## 3. Follow Up CTA — Beveled Card (sub page footer)

**Use on:** **End of sub page** when a single primary callback is warranted.

**Purpose:** Page-break engagement — elevated white card on shaded background; strong visual hierarchy for one next action.

**Technical:**
- `label="CTA_follow_up"`
- `data-item="cta"` with `cta-title`, `cta-description`
- `shadow_bevel-light`, `bg_white`, `btn-primary btn-lg`, `expanded-click-area`

**When to skip:** If the page already has a clear terminal action or user is mid-journey (don't stack multiple primary CTAs).

---

## 4. Small Image-Text Panel with CTA (1–2 features)

**Use on:** Grouping of **fewer than 3** featured items.

**Purpose:** One horizontal image + text + single CTA per feature — campaigns, programs, highlighted pathways.

**Technical:**
- `label="CTA-Callout"`
- Grid: image column (~375px) + content column
- `h4` headline, short body, `btn-shade` CTA

**Example grouping:** Cardio Renew + one other program; two policy spotlight panels.

---

## 5. Decorative Quote

**Use on:** Hub or spoke when content needs a **human voice**.

**Purpose:** Show impact, quality, or initiative value through member/faculty quote — avoids feeling like pure ACC marketing.

**When:** Faculty pull quotes (Cardio Renew), member perspective, initiative impact statements.

**Docs:** [item-recipes-quote-decrative.html](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-recipes-quote-decrative.html)

**Rule:** Quote text in HTML — never baked into hero or panel images ([imagery.md](imagery.md)).

---

## 6. Accordion (rare)

**Use on:** Content that is **4th in priority** but must remain on the page — too long for body copy.

**Typical contents:** Boilerplate, legal, toolkit citation blocks, lengthy references.

**Prefer instead:** Child page, Follow Up CTA to destination, or cut content per [refactor accordions](../refactor/accordions.md).

**Docs:** [item-component-accordion.html](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-component-accordion.html)

Use native `<details>` / `<summary>` when prototyping unless CMS requires the boot_acc accordion component.

---

## 7. Grid List with Descriptions (key points)

**Use on:** **Major callouts** — key points, concept summaries, non-navigational highlights.

**Purpose:** Icon + header + description grid. Items may include inline action links but are not full-card links.

**Technical:**
- `bg_black-1 br_radius` section wrapper
- `columns_2:lg columns_3:xl` grid
- Icon (`font_7`) + `font_display` title + description

**Example:** Burnout three dimensions (exhaustion, cynicism, inefficacy); quadruple aim; three reciprocal workplace domains.

---

## 8. Grid List with Linked Descriptions (3–7 features)

**Use on:** **3–7** featured items needing scanability and click context.

**Purpose:** Each row/card is fully clickable (`expanded-click-area`); hover state signals interactivity. Icon + title + human context for why to click.

**Technical:**
- Same grid shell as icon-text list
- `<a class="expanded-click-area not-link h:undecorated">` wraps title + description
- `h:bg_primary-4` hover on `<li>`

**Example:** Hub fork — Tools for Today / Shaping the Future + three Tools branches (5 items); Hot Topics list.

---

## Clinician Well-Being — pattern map (draft)

| Page | Shell | Patterns |
|------|-------|----------|
| **Hub** (concept root) | Fullscreen | Hero Image with CTA · two-lane Linked Icon Grid (2) · Linked Icon Grid for Tools branches (3) · Grid List icon-text for burnout dimensions · Decorative Quote (Cardio Renew faculty) · Small Image-Text Panel for Cardio Renew if solo feature |
| **Tools for Today** (spoke) | Sidebar + micro hero | Micro Branding · Linked Icon Grid (3 branches) · body chunks · Follow Up CTA → hub or Cardio Renew |
| **Mental Health & Burnout** | Sidebar + micro hero | Micro Branding · Grid List key points (burnout definition, stigma barriers) · prose zones · Follow Up CTA (Physician Support Line / Toolkit) |
| **Strengthen Your Workplace** | Sidebar + micro hero | Micro Branding · Grid List key points (3 reciprocal domains) · intervention lists · Follow Up CTA (Toolkit download) |
| **Protect Yourself & Others** | Sidebar + micro hero | Micro Branding · trust pillars grid · Small Image-Text for crisis comms PDF · Follow Up CTA |
| **Shaping the Future** | Sidebar + micro hero | Micro Branding · Small Image-Text panels for policy statements (<3) · Linked grid for partnerships · Follow Up CTA → advocacy |
| **Cardio Renew** | Product-style or micro | See [heroes.md § Product](heroes.md) — may differ from section microsite |

---

## Anti-patterns

- Micro branding on the **concept root** (use full Hero Image with CTA)
- Full hero on **sub pages** without sidebar (use micro + side nav)
- Linked Icon Grid for only **1–2** items (use Small Image-Text Panel each)
- Small Image-Text Panel for **4+** equal items (use Linked Icon Grid)
- Accordion for content that should be **visible** on first visit ([refactor accordions](../refactor/accordions.md))
- Multiple Follow Up CTAs on one sub page
- Decorative quotes that repeat body copy already above the fold

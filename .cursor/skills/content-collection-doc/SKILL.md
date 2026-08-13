---
name: content-collection-doc
description: >-
  Creates Content Collection Documents from ACC HTML prototypes or Whimsical
  wireframes. Captures end-user copy plus collector/DEV notes for multi-team
  handoff, authored as Word-safe Markdown. Use when building a content doc,
  content collection document, prototype-to-content handoff, or Ticket/Legend
  content package for Sitecore production.
disable-model-invocation: false
---

# Content Collection Document

Turn a prototype (default) or Whimsical wireframe into a **Content Collection Document** that pairs with the design and collects everything needed to produce the webpage. The doc travels across teams; Word is the collaboration end-state.

## When to use

- User asks for a content doc / content collection document from a prototype or wire
- Handoff from UX prototype → content / web production
- Document must support Sitecore build with ARCHES patterns

## Output location & naming

| Rule | Value |
|------|--------|
| **Save path** | `E:\REPO\ObsidianSecondBrain\Work\ACC\Projects\Content Collection Documents\` |
| **Document name** | **Page Name** (same as the page title / prototype `name`). For a **suite**, use the hub / root page name. |
| **File name** | `{Page Name}.md` (safe characters; keep readable) |
| **Source of truth** | **HTML prototype** by default. Use Whimsical (or other) only when the user says so at kickoff. |

Prototype content scope: everything between:

```html
<!-- Content Collection Starts Here -->
<!-- Content Collection Ends Here -->
```

Resolve `{% include %}` / `{% include_relative %}` partials into the collected content. Ignore chrome outside the markers. Do **not** include local repo source-file paths in the doc (prototype URL / Ticket references are enough).

## Document shape (TOC)

1. **Cover** — Document name (Page Name); `Updated {Month D, YYYY}`
2. **Contents**
   - Legend
   - Content Brief
   - Ticket *(last — filled last)*

### Multi-page suite (one document)

When the user asks for a **suite** / set of related pages in a single document:

- **One file**, named after the hub / root (e.g. `Clinician Well-Being.md`).
- **Confirm the page list first** (user verifies) before writing landmarks. Source of Sitecore nesting: **live sidebar** (or sidebar YAML), not hub cards or leftover prototype files.
- **Page title + tree label:** each page heading is `# {Page Name} ({sidebar / tree label})`.
- **Contents** lists each page under Content Brief in **tree order** (parent, then children, depth-first).
- **Delineation:** `<div style="page-break-before: always;"></div>` then `---` then the next `# {Page Name} ({tree label})`. Green tree-position note under the H1.
- **One suite-level** Content Brief intro (ASCII tree + shared chrome) **before** the first page H1. **One Ticket** at the end covering all pages.
- **Sitecore tree:** ASCII box-drawing tree (not HTML). Trailing `/` on nodes that have children. Start from ACC when the user gives a site path. **Site Structure / Placement** on each page repeats the tree and marks the current page with `← this page`.

```
ACC/
└── Tools and Practice Support/
    └── Clinician/
        └── Well-Being/
            ├── Self Care/
            │   └── Burn Out Survey
            ├── Team Support/
            │   └── Uncivil Behavior
            ├── Protect Patients & Peers
            └── Shaping the Future
```
- Omit prototype pages that are **not** in the verified tree (orphans / deleted intermediaries).
- Do not invent a separate nav dataset — Sitecore left nav **is** the content tree.

## Legend (required structure)

**How to use this document:**

- **Red text** — Landmark titles, UI element / slot labels, developer notes (including `{DEV: }`).
- **Green text** — UX & content-collector context: background, orientation to prototype/wire, limitations, and **constraints** (e.g. max chars).
- **`{DEV: }`** — Curly braces = inline developer notes. Only red inline notes use the `DEV:` prefix.
- **Yellow highlights** — UX still needs to address (e.g. missing URLs).
- **Pink highlights** — SMEs still need to address (e.g. missing resources, images, confirm text).
- **Standard (black) text** — End-user / shippable content (including meta title & meta description *values*).

### Word-safe color markup

| Role | Markup |
|------|--------|
| Red | `<span style="color:#8B0000">…</span>` |
| Green | `<span style="color:#006400">…</span>` |
| Yellow (UX) | `<mark>…</mark>` |
| Pink (SME) | `<span style="background-color:#FFC0CB">…</span>` |

### Markdown + color structure (critical)

Put Markdown syntax **outside** the color span:

```markdown
## <span style="color:#8B0000">Hero Image + CTA Overlay</span>

**<span style="color:#8B0000">CTA Title</span>**  
<span style="color:#006400">(Max: 80 chars)</span>  
75+ Years of Cardiovascular Publishing
```

Wrong: wrapping `##` or `**` inside the span; wrong: `<span>## Title</span>`.

## Content Brief rules

### Section order

1. `# Content Brief`
2. `# {Page Name}` (H1 — page title). Suite: `# {Page Name} ({tree label})`
3. `## Meta Content` — purpose, audience, placement, meta fields, layout overview, prototype link
4. Landmarks (each `##` with **red** title text)
5. Optional Open Items
6. `## Ticket` (document-level; listed last in TOC)

### Color assignment

| Kind | Color |
|------|--------|
| Landmark titles | **Red** |
| UI slot / element labels (CTA Title, Breadcrumb, etc.) | **Red** |
| `{DEV: …}` notes | **Red** |
| UX / collector context (purpose, audience, orientation, limitations) | **Green** |
| Constraints (max chars, pattern notes that constrain the slot) | **Green** |
| Shippable copy & meta *values* | **Black** |

### Constraints before content

Always state the **rule/constraint before** the content it governs. Do not repeat the element name inside the constraint when the red label already names it:

```markdown
**<span style="color:#8B0000">CTA Description</span>**  
<span style="color:#006400">(Max: 150 chars)</span>  
The JACC family of journals…
```

Not: `Description (Max: 150 chars)` under a label already called CTA Description.  
Defaults: Headline slots `(Max: 80 chars)`; description-length slots `(Max: 150 chars)`.

### Meta Content

Under `## Meta Content`, use **green** labels/context for collector fields. Meta Title and Meta Description **values** are black. Put `(Max: 150 chars)` (green) *before* the meta description value.

### Landmarks

- Group zones / logical sections (`id`, `data-jump-section`, `zone-label`, sticky nav targets).
- Landmark `##` title text is **red**.
- Green intro under the landmark orients collector to prototype/wire (no local file paths).
- **Prototype deep link (HTML prototypes):** In each landmark that has a section `id` / jump target, include a clickable link using `prototypeBaseUrl#id` so collectors can open the exact page location.
  - Example: `[Open in prototype](https://acc-style.github.io/PrototypingACCorg/acc/Journal-TextEdit/#Why-Publishing)`
  - Place the link in **green** collector context near the top of the landmark (under the red landmark title).
  - **Skip deep links** when no section id is needed:
  - **Hero Image + CTA Overlay** (and similar Sitecore chrome/renderings)
  - **Above-the-fold / start-of-page** zones (e.g. Introduction + Quick Links) — orientation note is enough; do not flag missing ids as UX yellow items
- Sub-UI: red slot label → green constraint → black content.
- Icons: Font Awesome **class names** (e.g. `fa-users`, `fa-lightbulb`) — put in `{DEV: Icon: fa-…}` on the item, not as a wide table column.
- Links/images: use `{DEV: Link: …}` and `{DEV: Img Src: …}` on the item (not wide URL columns).
- Pattern Library when useful: https://assets.acc.org/Arches/Latest/docs/

### Tables (Word-safe)

- **Max 3 columns.** Wider tables are hard to edit/read in Word — do not use them.
- Prefer **stacked item blocks** or lists for repeating cards/grids.
- **UI Component / layout pattern notes** (e.g. “Icon + text grid with expanded click area jump links”) belong in `{DEV: …}`, not a table and not a multi-column matrix.

**Repeating card / grid pattern (preferred):**

```markdown
**<span style="color:#8B0000">Card Title</span>**  
<span style="color:#006400">(Max: 80 chars)</span>  
Why We Publish  

<span style="color:#006400">(Max: 150 chars)</span>  
**Mission & Impact**: How publishing advances…  

<span style="color:#8B0000">{DEV: Icon: fa-lightbulb; Jump: #Why-Publishing; Shade jump-link card }</span>
```

**Journal / media item pattern:**

```markdown
#### JACC

Top research across all cardiovascular medicine…

**Best for:** All cardiovascular professionals  

<span style="color:#8B0000">{DEV: Link: https://www.jacc.org/journal/jacc; Img Src: https://…/logo-JACC-….png }</span>
```

### Inline DEV notes

```
{DEV: Button, Primary, URL: https://…, FUNCTION: navigate, Label: Go to JACC}
{DEV: Add image to right of text: https://www.acc.org/-/media/…jpg}
{DEV: Anchor ID: #Why-Publishing}
```

#### Button colors

| Color | Use |
|-------|-----|
| **Primary** | Page primary action. With audience breakdowns, may be section primary. |
| **Shade** | Off / secondary actions |
| **Secondary** / **Accent** | Rare split-primary; use sparingly |

`{DEV: Button, Primary|Secondary|Shade|Accent, URL, FUNCTION, & Label}`

#### Personalization & purchase

`{DEV: Personalization — if logged-in user has product code, switch UI from Purchase to Launch}`

#### Details & summaries

`{DEV: UI Pattern — summary/details accordions; marketing-friendly short IDs (no spaces) for deep links}`

## Ticket section (last)

Boilerplate + page-specific. Contacts: **ECDS Lead / UX: Matt Watier, Rowena**.

### Acceptance Criteria (always include)

- Construct the page based on best Sitecore Practices
- Base all content on *this Document* vs Wires
- Use golden standard patterns from the ARCHES pattern library
- Plus page-specific criteria

## Workflow checklist

```
- [ ] Confirm source (prototype default)
- [ ] Extract between Content Collection markers (+ partials)
- [ ] Cover + TOC: Legend, Content Brief, Ticket (last)
- [ ] Legend
- [ ] Content Brief: H1, Meta Content (green context / black values), red landmarks, green constraints before black copy, {DEV:}
- [ ] FA class names; Link: / Img Src: for media rows
- [ ] Yellow UX / pink SME gaps
- [ ] Ticket
- [ ] Save as {Page Name}.md under Obsidian path
- [ ] Suite: confirm page list + tree; page-break between pages; one Ticket
- [ ] Iterate; update this skill when rules change
```

## Iteration

When the user corrects output, **update this skill** so the next run matches. Prefer short rule additions over long prose.

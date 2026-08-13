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

### Prototype URLs (hosted only)

**Never** put local addresses in the document (`http://127.0.0.1:…`, `http://localhost:…`, file paths). Always use the **hosted** GitHub Pages base:

`https://acc-style.github.io/PrototypingACCorg/`

| Use | Example |
|-----|---------|
| **Prototype** (after page H1) | `https://acc-style.github.io/PrototypingACCorg/clinical-wellbeing/Concept-Clinician-Well-Being/` |
| Landmark deep link | `https://acc-style.github.io/PrototypingACCorg/clinical-wellbeing/Concept-Clinician-Well-Being/#why-wellbeing` |
| Ticket reference | Same hosted hub URL |

You may **open** a local Jekyll server to inspect the prototype while collecting; the **links you write** must still be hosted.

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
- **Delineation:** `<div style="page-break-before: always;"></div>` then `---` then the next `# {Page Name} ({tree label})`. Hosted **Prototype** link immediately under the H1 (before Meta Content).
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
### <span style="color:#8B0000">Hero Image + CTA Overlay</span>

**<span style="color:#8B0000">CTA Title</span>** <span style="color:#006400">(Max: 80 chars)</span>  
75+ Years of Cardiovascular Publishing
```

Wrong: wrapping `##` or `**` inside the span; wrong: `<span>## Title</span>`.

## Content Brief rules

### Section order

1. `# Content Brief`
2. `# {Page Name}` (H1 — page title). Suite: `# {Page Name} ({tree label})`
3. **Prototype** link (hosted GitHub Pages URL) — directly after the H1, before Meta Content
4. `## Meta Content` — H3s in this order: Page Purpose, Primary Audience, Meta Title, Meta Description, Site Structure / Placement
5. `## Page Content` — starts with **Page Layout (zones)**, then one `###` per zone
6. Optional Open Items
7. `## Ticket` (document-level; listed last in TOC)

### Color assignment

| Kind | Color |
|------|--------|
| Landmark titles (zone H3s) | **Red** |
| Site Structure / Placement (Meta H3) | **Red** |
| UI slot / element labels (CTA Title, Breadcrumb, etc.) | **Red** |
| `{DEV: …}` notes | **Red** |
| UX / collector context (purpose, audience, orientation, limitations) | **Green** |
| Constraints (max chars, pattern notes that constrain the slot) | **Green** |
| Shippable copy & meta *values* | **Black** |

### Constraints before content

Always state the **rule/constraint before** the content it governs. Put the **red slot label and green constraint on the same line** to keep the document short. Do not repeat the element name inside the constraint when the red label already names it:

```markdown
**<span style="color:#8B0000">Section Heading</span>** <span style="color:#006400">(Max: 80 chars)</span>  
Why ACC Cares for You

**<span style="color:#8B0000">CTA Description</span>** <span style="color:#006400">(Max: 150 chars)</span>  
The JACC family of journals…
```

Keep the colors: red label, green `(Max: … chars)`, then black copy on the next line (hard line break after the constraint).  
Not: `Description (Max: 150 chars)` under a label already called CTA Description.  
Not: label on one line and `(Max: 80 chars)` on the next.  
Defaults: Headline slots `(Max: 80 chars)`; description-length slots `(Max: 150 chars)`.

### Meta Content

`## Meta Content` is an H2. Its fields are **H3s in this order**:

1. `### Page Purpose` (green)
2. `### Primary Audience` (green)
3. `### Meta Title` (green heading; **value is black**)
4. `### Meta Description` (green heading + `(Max: 150 chars)` on the same line; **value is black**)
5. `### Site Structure / Placement` (**red** heading; ASCII tree with `← this page`)

**Prototype does not live here.** Put the hosted prototype URL **directly after the page H1** and before `## Meta Content`:

```markdown
# Care for Yourself (Self Care)

**<span style="color:#006400">Prototype</span>**  
<span style="color:#006400">https://acc-style.github.io/PrototypingACCorg/clinical-wellbeing/Concept-Clinician-Well-Being-Mental-Health/</span>

## Meta Content

### <span style="color:#006400">Page Purpose</span>
```

#### Page Purpose & Primary Audience

Keep both **concise** (one or two sentences). When the user supplies UX value / audience research, **use it** to aim the copy—do not paste the research into the document.

- **Page Purpose** — what we hope users get: feel seen, know where to start, stay in the work more sustainably. Name the College’s role only as it serves the user.
- **Primary Audience** — who this page is for, in plain language. Prefer the page’s primary people (e.g. clinical leaders on a team page) over listing every suite audience.

Do **not** put Page Layout (zones) here — that belongs at the start of Page Content.

### Page Content

`## Page Content` is an H2. It starts with **Page Layout (zones)** (green numbered list), then one **H3 per zone**. Zone H3 title text is **red** and **must match** the Page Layout list (same wording). Do not rename a zone to a generic pattern name (e.g. do not use `Hero Image + CTA Overlay` when the zone list says `Micro hero + back to Team Support`).

```markdown
## Page Content

**<span style="color:#006400">Page Layout (zones)</span>**

1. <span style="color:#006400">Hero image with CTA overlay</span>
2. <span style="color:#006400">Introduction + Cardio Safe aside</span>

---

### <span style="color:#8B0000">Hero image with CTA overlay</span>
```

Sub-slots inside a zone (accordion panels, questions) stay `####`.

### Landmarks (zone H3s)

- Group zones / logical sections (`id`, `data-jump-section`, `zone-label`, sticky nav targets).
- Green intro under the H3 orients collector to prototype/wire (no local file paths).
- **Prototype deep link (HTML prototypes):** In each landmark that has a section `id` / jump target, include a clickable link using the **hosted** `https://acc-style.github.io/PrototypingACCorg/{collection-path}/#id` (never `127.0.0.1` / `localhost`).
  - Example: `[Open in prototype](https://acc-style.github.io/PrototypingACCorg/acc/Journal-TextEdit/#Why-Publishing)`
  - Place the link in **green** collector context near the top of the landmark (under the red H3).
  - **Skip deep links** when no section id is needed:
  - **Hero / micro hero chrome** (and similar Sitecore renderings)
  - **Above-the-fold / start-of-page** zones (e.g. Introduction + Quick Links) — orientation note is enough; do not flag missing ids as UX yellow items
- Sub-UI: red slot label and green constraint **on the same line**, then black content on the next line.
- Icons: Font Awesome **class names** (e.g. `fa-users`, `fa-lightbulb`) — put in `{DEV: Icon: fa-…}` on the item, not as a wide table column.
- Links/images: use `{DEV: Link: …}` and `{DEV: Img Src: …}` on the item (not wide URL columns).
- Pattern Library when useful: https://assets.acc.org/Arches/Latest/docs/

### Tables (Word-safe)

- **Max 3 columns.** Wider tables are hard to edit/read in Word — do not use them.
- Prefer **stacked item blocks** or lists for repeating cards/grids.
- **UI Component / layout pattern notes** (e.g. “Icon + text grid with expanded click area jump links”) belong in `{DEV: …}`, not a table and not a multi-column matrix.

**Repeating card / grid pattern (preferred):**

```markdown
**<span style="color:#8B0000">Card Title</span>** <span style="color:#006400">(Max: 80 chars)</span>  
Why We Publish  

**<span style="color:#8B0000">Body</span>** <span style="color:#006400">(Max: 150 chars)</span>  
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
- [ ] Prototype + deep-link URLs: hosted GitHub Pages only (never 127.0.0.1 / localhost)
- [ ] Extract between Content Collection markers (+ partials)
- [ ] Cover + TOC: Legend, Content Brief, Ticket (last)
- [ ] Legend
- [ ] Content Brief: H1; Prototype URL; `## Meta Content` H3s (Purpose, Audience, Title, Description, Site Structure in red); `## Page Content` (zones list first); zone H3s
- [ ] FA class names; Link: / Img Src: for media rows
- [ ] Yellow UX / pink SME gaps
- [ ] Ticket
- [ ] Save as {Page Name}.md under Obsidian path
- [ ] Suite: confirm page list + tree; page-break between pages; one Ticket
- [ ] Iterate; update this skill when rules change
```

## Iteration

When the user corrects output, **update this skill** so the next run matches. Prefer short rule additions over long prose.

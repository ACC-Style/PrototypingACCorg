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
| **Document name** | **Page Name** (same as the page title / prototype `name`) |
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
2. `# {Page Name}` (H1 — page title)
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
- **Prototype deep link (HTML prototypes):** In each landmark, include a clickable link using `prototypeBaseUrl#id` so collectors can open the exact page location. Prefer the section’s `id` / jump target from the prototype. If a zone has no id, link the prototype base URL and note the missing id in yellow for UX.
  - Example: `[Open in prototype](https://acc-style.github.io/PrototypingACCorg/acc/Journal-TextEdit/#Why-Publishing)`
  - Place the link in **green** collector context near the top of the landmark (under the red landmark title).
- Sub-UI: red slot label → green constraint → black content.
- Icons: Font Awesome **class names** (e.g. `fa-users`, `fa-lightbulb`).
- Links/images in tables: use **`Link:`** and **`Img Src:`** columns (not a bare “URL” dump).
- Pattern Library when useful: https://assets.acc.org/Arches/Latest/docs/

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
- [ ] Iterate; update this skill when rules change
```

## Iteration

When the user corrects output, **update this skill** so the next run matches. Prefer short rule additions over long prose.

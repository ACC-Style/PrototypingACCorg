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
| **Suite folder** | Split / multi-doc packages go in a **named subfolder** (e.g. `WIC\`). Single-page docs stay at the root unless the user names a folder. |
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

Write them as Markdown links, not a labeled two-line URL:

```markdown
[Prototype](https://acc-style.github.io/PrototypingACCorg/clinical-wellbeing/Concept-Clinician-Well-Being/)
```

| Use | Example |
|-----|---------|
| **Page** (immediately after the page H1) | `[Prototype](https://acc-style.github.io/PrototypingACCorg/…/)` |
| **Landmark** (section `id`) | `[Prototype](https://acc-style.github.io/PrototypingACCorg/…/#why-wellbeing)` |
| **Ticket** | Same hosted URLs as Markdown links |

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
- **Delineation:** `<div style="page-break-before: always;"></div>` then `---` then the next `# {Page Name} ({tree label})`. `[Prototype](hosted-url)` immediately under the H1 (before Meta Content).
- **One suite-level** Content Brief intro **before** the first page H1: `###` Sitecore tree, then `####` shared chrome (header graphic, repeating CTAs, Need Help). Keep it compact — no long orientation essays. **One Ticket** at the end covering all pages.
- Do **not** repeat shared chrome (micro hero, DocMatter, Need Help) as empty zones on every child page when it is already in that suite intro. Keep a child-page Micro hero zone only when it has page-specific slots (e.g. a unique hero title).
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

### Split suite (core + satellite docs)

When the user asks to **break a collection into separate documents**:

- **Core document** — named after the hub / root, or `{Hub} - Core Pages.md` when the user uses that pattern. Includes the hub / shared pages the user names. One Ticket at the end. Save the **core + satellite files in one suite folder** under the Content Collection Documents path (do not scatter them at the root).
- **Dynamic listing pages** — Meta Content + intro zone only. Do **not** transcribe feed items. Close the listing zone with `{DEV: FEED}`. Optional: item anatomy / facet labels as DEV notes.
- **Specialized feature / detail pages** — one document per page, content-only. Short Ticket that points back to the core document (do not repeat suite acceptance criteria, contacts, or shared chrome). Note shared hero/sidebar in green and send collectors to the core file.

Personalization and page variants are **prototype-specific**. Do not assume access-state homes, numbered state files, or that meta can or cannot change. Follow the grouping the user gives for that collection.

## Legend (required structure)

Use the **colored** bullets in the document (collectors read Word). Do not add extra process essays to the Legend.

```markdown
## Legend

How to use this document:

- <span style="color:#8B0000">Red text – Landmark titles, UI element / slot labels, and developer notes (including {DEV: }).</span>
- <span style="color:#006400">Green text – UX & content-collector context (background, orientation, limitations) and constraints (e.g. max characters).</span>
- <span style="color:#8B0000">{DEV: } – Curly braces denote inline developer notes (e.g. button colors, URLs, etc.)</span>
- <mark>Yellow highlights denote items UX Team still need to address (e.g. missing URLs)</mark>
- <span style="background-color:#FFC0CB">Pink highlights denote items for SMEs still need to address (e.g. missing resources, images, confirm text, etc.)</span>
- Text for content will use standard document headers and formatting.
```

Repeatable-template collections also add the EVERGREEN ZONE / EVERGREEN bullets (see below). Do **not** add a “standard black text” essay — shippable copy is already the uncolored body.

### Word-safe color markup

| Role | Markup |
|------|--------|
| Red | `<span style="color:#8B0000">…</span>` |
| Green | `<span style="color:#006400">…</span>` |
| Yellow (UX) | `<mark>…</mark>` |
| Pink (SME) | `<span style="background-color:#FFC0CB">…</span>` |
| EVERGREEN ZONE | `**<span style="background:rgba(136, 49, 204, 0.2)">EVERGREEN ZONE</span>**` on its own line, immediately after the zone / landmark heading (use this for repeating template UI) |
| EVERGREEN (single slot) | `**<span style="background:rgba(136, 49, 204, 0.2)">EVERGREEN</span>**` on its own line, immediately before the red slot label — only when the rest of that zone is section-authored |

### Markdown + color structure (critical)

Put Markdown syntax **outside** the color span:

```markdown
### <span style="color:#8B0000">State 0 — Need to log in</span>

**<span style="color:#8B0000">Section Name (H1)</span>** <span style="color:#006400">(Max: 80 chars)</span> · **<span style="color:#8B0000">Teaser Body</span>** <span style="color:#006400">(Max: 150 chars)</span>

# Women In Cardiology
This section offers women cardiologists opportunities to strengthen their professional support system and skills.

## Log In to Access This Content
This content is reserved for members of the ACC community.

Log In <span style="color:#8B0000">{DEV: Button, Primary, URL: ACC login, FUNCTION: authenticate then return to this Section URL, Label: Log In }</span>
```

Wrong: wrapping `##` or `**` inside the span; wrong: `<span>## Title</span>`.  
Wrong: a red slot label, then one line of copy, then another red label — that ping-pong is hard to copy.

## Content Brief rules

### Section order

1. `# Content Brief`
2. `# {Page Name}` (H1 — page title). Suite: `# {Page Name} ({tree label})`
3. `[Prototype](hosted-url)` — directly after the H1, before Meta Content (one line; no labeled “Prototype” heading)
4. `## Meta Content` — H3s in this order: Page Purpose, Primary Audience, Meta Title, Meta Description, Site Structure / Placement. Put the **value on the next line** with **no blank line** after the H3.
5. `## Page Content` — **Page Layout (zones)**, then real heading levels for landmarks (`#` / `##` / `###`) with **dark red** title text. Body copy under them is black.
6. Optional Open Items
7. `## Ticket` (document-level; listed last in TOC)

### Color assignment

| Kind | Color |
|------|--------|
| Landmark / zone / section titles | **Red** — real header level, color on the title text: `## <span style="color:#8B0000">Need Help?</span>` |
| On-page body copy (paragraphs, lists, names) | **Black** |
| Site Structure / Placement (Meta H3) | **Red** |
| UI slot / element labels | **Red** — batch above a copy block when a constraint is needed; do not label every sentence |
| `{DEV: …}` notes | **Red** |
| UX / collector context (purpose, audience, orientation, limitations) | **Green** |
| Constraints (max chars, pattern notes that constrain the slot) | **Green** |
| Shippable copy & meta *values* | **Black** |
| Repeatable-template chrome (EVERGREEN ZONE) | **Purple background** on `EVERGREEN ZONE` after the landmark heading |
| Single template slot (EVERGREEN) | **Purple background** on `EVERGREEN` in front of one red slot in a mixed zone |

### Constraints before content

Batch **slot labels + constraints above** a content block, then write the **shippable copy as real Markdown headings** matching the UI (`#` = page H1, `##` = section / h2, `###` = subsection / h3). Body copy follows the heading as normal paragraphs. `{DEV: }` trails the line it annotates.

Do **not** sandwich every sentence between a red label and a value.

```markdown
**<span style="color:#8B0000">Roadblock Heading</span>** <span style="color:#006400">(Max: 80 chars)</span> · **<span style="color:#8B0000">Roadblock Body</span>**

## <span style="color:#8B0000">Log In to Access This Content</span>
This content is reserved for members of the ACC community. Log in to access these resources and more exclusive member perks.

Log In <span style="color:#8B0000">{DEV: Button, Primary, URL: ACC login, Label: Log In }</span>
```

When the visible heading **is** the landmark, skip a separate unlabeled zone title — use the real heading **in dark red**:

`## <span style="color:#8B0000">Why Should You Join?</span>`

Combine landmarks that are one visual unit (H1 + teaser body; heading + body + CTA; Need Help heading + links).

Keep `{DEV: }` and yellow/pink notes **out of** the copy block when they would interrupt a heading + paragraph the collector needs to paste.

Defaults: Headline slots `(Max: 80 chars)`; description-length slots `(Max: 150 chars)`. Put those on the batched label line, not on a line by themselves.

### Density (page space)

The document is a collector worksheet, not an agent runbook.

- Prefer `###` / `####` over extra labeled paragraphs.
- One blank line between blocks. No extra blank after an H3 before its value.
- Green text = **constraints** and short orientation only. Do not paste process rules collectors cannot act on (e.g. “no section id / deep link required”, long EVERGREEN how-to, “Sitecore rendering…”).
- Do not duplicate a page `[Prototype](url)` inside every zone when Meta Content already has it. Landmark links stay as `[Prototype](url#id)`.
- If a `[Prototype](url)` already shows the view, do **not** add a **UI visible** inventory of chrome. The link is the explanation. Keep Rule / Page Purpose / Primary Audience.

### Repeatable templates (EVERGREEN) — rare

Use this **only** when the collection is a template reused across many sites (e.g. all ~22 Member Sections). Do not invent EVERGREEN tags on one-off pages.

- **Repeated UI** — put `**<span style="background:rgba(136, 49, 204, 0.2)">EVERGREEN ZONE</span>**` on its **own line immediately after** the zone / landmark heading (`###` or `####`). Do **not** tag every slot inside it. Optional green note: which slots are in the zone vs section-authored.
- **Single slot in a mixed zone** — put `**<span style="background:rgba(136, 49, 204, 0.2)">EVERGREEN</span>**` on its own line immediately before that red slot label.
- Mark **immutable template chrome** only: roadblock instructions, Need Help / Member Care, join/unlock bands, listing-page intros, DocMatter closer, zone labels (Announcements, Resources, Library), Work Groups chrome (“Getting Involved?”, status chip string). Do **not** mark Section Benefits items, chair names/roles, or other section-authored lists.
- **Do not mark** section-authored copy (mission/focus cards, chair letter, quotes, initiative names), **data-model** fields (names, photos, work-group titles/bodies), or feed items.
- Tokens such as section name, acronym, and hashtag may sit inside an otherwise-evergreen sentence. Keep the zone (or slot) mark; add a short green note that only the token swaps. Do not glue that note onto the shippable line.
- Add these Legend bullets:

`**<span style="background:rgba(136, 49, 204, 0.2)">EVERGREEN ZONE</span>** A landmark or repeating UI block whose slots are shared template chrome. Do not rewrite the slots inside it.`

`**<span style="background:rgba(136, 49, 204, 0.2)">EVERGREEN</span>** A single immutable slot inside a mixed zone (the rest of that zone is section-authored).`

Example — whole landmark:

```markdown
## <span style="color:#8B0000">Unlock This Content</span>

**<span style="background:rgba(136, 49, 204, 0.2)">EVERGREEN ZONE</span>**
```

**Want to gain access to all of the exclusive content and more?** Manage your membership today to join this Member Section and unlock all the benefits.

Manage Membership <span style="color:#8B0000">{DEV: Button, Shade, URL: membership management, Label: Manage Membership }</span>
```

### Meta Content

`## Meta Content` is an H2. Its fields are **H3s in this order**:

1. `### Page Purpose` (green)
2. `### Primary Audience` (green)
3. `### Meta Title` (green heading; **value is black**)
4. `### Meta Description` (green heading + `(Max: 150 chars)` on the same line; **value is black**)
5. `### Site Structure / Placement` (**red** heading; ASCII tree with `← this page`)

**Prototype does not live here.** Put `[Prototype](hosted-url)` **directly after the page H1** and before `## Meta Content`:

```markdown
# Care for Yourself (Self Care)

[Prototype](https://acc-style.github.io/PrototypingACCorg/clinical-wellbeing/Concept-Clinician-Well-Being-Mental-Health/)

## Meta Content

### <span style="color:#006400">Page Purpose</span>
```

#### Page Purpose & Primary Audience

Keep both **concise** (one or two sentences). When the user supplies UX value / audience research, **use it** to aim the copy—do not paste the research into the document.

- **Page Purpose** — what we hope users get: feel seen, know where to start, stay in the work more sustainably. Name the College’s role only as it serves the user.
- **Primary Audience** — who this page is for, in plain language. Prefer the page’s primary people (e.g. clinical leaders on a team page) over listing every suite audience.

Do **not** put Page Layout (zones) here — that belongs at the start of Page Content.

### Page Content

`## Page Content` is an H2. It starts with **Page Layout (zones)** (green numbered list of **visible** landmarks). Then write those landmarks with **real heading levels** (`#` / `##` / `###`). The **title text is dark red**; paragraphs under it stay black.

`## <span style="color:#8B0000">Why Should You Join?</span>`

Do not add a second unlabeled heading that repeats the same landmark name. Do not rename a landmark to a generic pattern name (e.g. do not use `Hero Image + CTA Overlay` when the page heading is `Why Should You Join?`).

### Landmarks (zone headings)

- Group by UI landmarks. Combine adjacent slots that collectors copy as one unit (heading + body + CTA).
- Shippable headings use real Markdown levels matching the HTML (`h1` → `#`, `h2` → `##`, `h3` → `###`). Put the **dark red** span on the title text: `## <span style="color:#8B0000">Need Help?</span>`. Body copy under the heading stays black.
- Keep green under a landmark **short**. Skip agent-only notes.
- **Prototype deep link:** `[Prototype](https://acc-style.github.io/PrototypingACCorg/{collection-path}/#id)` near the landmark. Never `127.0.0.1` / `localhost`.
  - Example: `[Prototype](https://acc-style.github.io/PrototypingACCorg/acc/Journal-TextEdit/#Why-Publishing)`
  - **Skip** deep links on hero / micro hero chrome and above-the-fold start-of-page — do not flag missing ids as yellow UX items.
- `{DEV: }` on the same line as the button, link, or icon it describes.
- Icons: Font Awesome class names in `{DEV: Icon: fa-…}`.
- Links/images: `{DEV: Link: …}` and `{DEV: Img Src: …}`.
- Pattern Library when useful: https://assets.acc.org/Arches/Latest/docs/

### Tables (Word-safe)

- **Max 3 columns.** Wider tables are hard to edit/read in Word — do not use them.
- Prefer **stacked item blocks** or lists for repeating cards/grids.
- **UI Component / layout pattern notes** (e.g. “Icon + text grid with expanded click area jump links”) belong in `{DEV: …}`, not a table and not a multi-column matrix.

**Repeating card / grid pattern (preferred):**

```markdown
### Why We Publish
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
- [ ] `[Prototype](hosted-url)` after each page H1; landmark `#id` links the same way (never 127.0.0.1 / localhost)
- [ ] Extract between Content Collection markers (+ partials)
- [ ] Cover + TOC: Legend, Content Brief, Ticket (last)
- [ ] Legend (colored bullets; EVERGREEN ZONE / EVERGREEN only on repeatable templates)
- [ ] Suite Content Brief: `###` tree + `####` shared chrome (compact)
- [ ] Each page: H1; Prototype link; `## Meta Content`; `## Page Content` with real heading levels for on-page copy; `{DEV: }` on the content line
- [ ] FA class names; Link: / Img Src: for media rows
- [ ] Yellow UX / pink SME gaps
- [ ] Ticket (hosted Markdown links)
- [ ] Save as {Page Name}.md under Obsidian path
- [ ] Suite: confirm page list + tree; page-break between pages; one Ticket
- [ ] Iterate; update this skill when rules change
```

## Iteration

When the user corrects output, **update this skill** so the next run matches. Prefer short rule additions over long prose.

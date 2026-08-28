---
name: content-collection-doc
description: >-
  Creates Content Collection Documents from ACC HTML prototypes or Whimsical
  wireframes. Captures end-user copy plus collector/DEV notes for multi-team
  handoff. Colors via Obsidian REGEX Marker tokens ({LM}, {DEV:}, {UX:}, {SME:},
  Document Labels). Use when building a content doc, content collection
  document, prototype-to-content handoff, or Ticket/Legend content package
  for Sitecore production. Attaches [UI Pattern - Name](url) from the boot_acc
  dictionary. Unmatched UI gets {UX: find a referenced defined pattern}. Access
  rules use {Rule: }. Never use HTML color spans or <mark>.
disable-model-invocation: false
---

# Content Collection Document

Turn a prototype (default) or Whimsical wireframe into a **Content Collection Document** that pairs with the design and collects everything needed to produce the webpage. Author in **plain Markdown**; Obsidian **REGEX Marker** (`regex_mark`) applies color from tokens and Document Labels. Do **not** wrap titles or notes in HTML `<span>` / `<mark>` / `</mark>`.

Plugin rules: [regex-mark.md](regex-mark.md). Pattern lookup: [pattern-dictionary.md](pattern-dictionary.md).

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
| **Page** (immediately after the page heading) | `[Prototype](https://acc-style.github.io/PrototypingACCorg/…/)` |
| **Landmark** (section `id`) | `[Prototype](https://acc-style.github.io/PrototypingACCorg/…/#why-wellbeing)` |
| **Ticket** | Same hosted URLs as Markdown links |

You may **open** a local Jekyll server to inspect the prototype while collecting; the **links you write** must still be hosted.

## REGEX Marker coloring

Color is **pattern-matched**, not styled in the file. Write the token; the plugin paints the match.

### What colors, and how far

| Write | Class (color) | Match span |
|-------|----------------|------------|
| `{DEV: …}` | `dev-note` (dark red) | The brace block only |
| `{Rule: …}` | `dev-note` (dark red) | The brace block only — access / personalization rule |
| `^@^` at end of line | `dev-note` (dark red) | Start of line → marker. **Hidden** in reading view |
| `(DEV) …` | `dev-note` (dark red) | `(DEV)` through end of line |
| `(Constraint) …` | `content-note` (green) | `(Constraint)` through end of line |
| `(Content)` | `content-note` (green) | The token only — UI delineator before shippable copy |
| `{Repeat: Name}` | `repeated-ui-note` (gray, white text) | The brace block only — delimiter between repeating blobs. Name the UI (`Card`, `Step`, `Panel`, `Accordion`). Use `{Repeat: UI}` when it is just a blob |
| `(Max: …)` / `(Min: …)` | `content-note` (green) | The parenthetical (case-insensitive; any `Max:` or `Min:` inside `()`) |
| `(Context) …` | `context-note` (green) | `(Context)` through end of line |
| `Locked Content` / `Locked Zone` | `evergreen-note` (blue, white text) | Those words only. Locked Member Section template; do not rewrite from SME comments. |
| `{UX: …}` | `ux-note` (yellow) | The brace block only (same idea as `{DEV: }`) |
| `{SME: …}` | `sme-note` (magenta) | The brace block only (same idea as `{DEV: }`) |
| `{LM}` | `landmark` (dark red) | Start of line → `{LM}`. **Hidden** in reading view. Put it at the **end** of the title line; notes after it stay uncolored (or use their own token) |
| `State: …` | `landmark` (dark red) | Whole line. Optional `#`–`######` before `State:`. Numbers are optional (`State: Need to log in`, `State: Not purchased`) |
| `Page: …` | `landmark` (dark red) | Whole line. Optional `#`–`######` before `Page:` (`# Page: Women in Cardiology`) |

Highlight tints use Word color names (`yellow`, `magenta`, `blue` + white text) so they survive copy to Word. Dark green does not map; use blue for `Locked Zone` / `Locked Content`.

Unmarked body copy is shippable (standard Markdown, no color).

**Do not** use HTML color spans or `<mark>`. **Do not** put `{LM}` at the start of a line (only text *before* `{LM}` is painted). `{DEV: }`, `{Rule: }`, `{UX: }`, `{SME: }`, and `{Repeat: }` cannot contain `}` or wrap to a new line.

### Document Labels (canonical vocabulary)

These **exact strings** color as `landmark` wherever they appear. Use them as headings / field names — do **not** invent synonyms (e.g. not “Sitecore tree”, not “SEO title”, not “IA placement”).

| Document Label | Use for |
|----------------|---------|
| **Legend** | How-to-read this document |
| **Content Brief** | Collected page content (the body of the worksheet) |
| **SiteCore Tree** | Suite-level ASCII content tree |
| **Meta Title** | Sitecore / browser title value |
| **Meta Description** | Sitecore / search description value |
| **Site Structure / Placement** | Per-page tree with `← this page` |
| **Personalization States** | Access / personalization state block |

Line prefixes (also landmarks; not the same as Document Labels but always use this spelling):

- `# Page: {Page Name}` — page delineation (write `# Page:`; plugin allows `#`–`######`)
- `State: {label}` — a personalization / access **zone**. Numbers optional. Examples: `State: Need to log in`, `State: Not purchased`, `State: 0 - Need to log in`

**`State:` (locked):** Always write `State:` (never `State 3:` with the colon after the number). Treat each state as a **zone** (pattern/slots + Content). Use a real heading level for the outline (`### State: Need to log in`) — the plugin allows optional `#` prefixes. Do **not** put `{LM}` on a `State:` line.

**`Page:` (locked):** `# Page: {Page Name}`. The plugin allows optional `#` prefixes.

**Not** Document Labels (do not expect auto-color): Site Purpose, Site Audience, Page Purpose, Primary Audience, Page Content, Ticket, Page Layout. Site Purpose / Site Audience (suite) and Page Purpose / Primary Audience (page) use the same black-label + `(Context)` pattern — they are **not** Document Labels. Slot limits use `(Max: )` / `(Min: )` or `(Constraint)`. Do **not** add a `UI description` heading — pattern, slots, and constraints sit directly under the landmark.

## Document shape (TOC)

All top-level items are **H1**. Each nested level drops one heading level. **No ATX headings** (`#` / `##` / `###` …) inside `(Content)` — those become Word Heading styles and ruin the TOC. Shippable title lines are **bold** (or plain). Collector headings are the only outline Word should see (TOC Heading 1–3).

1. Cover (page/suite name + `Updated {date}`) — already the first `#`
2. `# Contents`
3. `# Legend`
4. `# Content Brief`
	1. **Site Purpose** (Context): … *(one line; label black, note green)* — NOT a heading, same pattern as Page Purpose
	2. **Site Audience** (Context): … *(one line)*
	3. `## SiteCore Tree` *(suite only, before the first page)*
	4. Shared chrome *(suite only)* → `## Shared UI {LM}` with numbered items as `### 1. Item`
	5. Also keep existing suite intro piece at H2: `## State: Personalization` (suite pointer)
5. `# Page: {Name}` *(repeat, tree order — sibling of Content Brief, NOT nested under it as a heading)*
	1. Prototype link (not a heading)
	2. `## Meta Content`
		1. **Page Purpose** (Context): … *(one line; label black, note green)* — NOT H3
		2. **Primary Audience** (Context): … *(one line)* — NOT H3
		3. `### Meta Title (Max: 80 chars)`
		4. `### Meta Description (Max: 150 chars)`
		5. `### Site Structure / Placement`
		6. `### State: Personalization` *(if variants)*
	3. `## Page Content`
		1. Zone *(repeat; a `State:` is a zone)*
			1. `Locked Zone` *(if template chrome — precedes the zone; not a heading)*
			2. Landmark `{LM}` **or** `State: {label}` → `###` under Page Content
				1. Nested Landmark `{LM}` **or** Sub UI `{LM}` (optional) **or** child of `State:Label` → `####`
					1. Deeper nested UI → `#####` (e.g. Triple Card under a landmark that is already `####`)
					2. Pattern + slots — `[UI Pattern - Name](url)` + stacked slots/`(Max:)`/`(Constraint)` directly under the landmark (no `UI description` heading); unmatched → `{UX: find a referenced defined pattern}`
			3. `(Content)` — shippable copy. **No ATX headings.** On-page titles are **bold** (or plain). Heading rank lives on the landmark / slot (`Page Title {LM}`, `Section Heading {LM}`), not as `#` / `##` in the paste. Repeating blobs: `{Repeat: Card}` (or `Step` / `Panel` / `Accordion` / `UI`) between items.
6. `# Ticket` *(one per document; last)*
	- Ticket children (`Description`, `References`, `Page Location`, `Acceptance Criteria`, `Vanities`, `Contact Information`, `Images`) stay `##` under `# Ticket`

### Multi-page suite (one document)

When the user asks for a **suite** / set of related pages in a single document:

- **One file** for a suite unless the user asks to split **and** a page is complex enough to stand alone. Simple feature pages (a few landmarks) stay in the hub document. Named after the hub / root (e.g. `Clinician Well-Being.md` or `{Hub} - Core Pages.md`).
- **Confirm the page list first** (user verifies) before writing landmarks. Source of Sitecore nesting: **live sidebar** (or sidebar YAML), not hub cards or leftover prototype files.
- **Page title:** each page heading is `# Page: {Page Name}`. Include `({sidebar / tree label})` after the name when the tree label differs from the page name.
- **Contents** lists Legend, Content Brief (Site Purpose, Site Audience, SiteCore Tree, State: Personalization, Shared UI), then each **page name as a sibling of Content Brief** (tree order: parent, then children, depth-first), then Ticket.
- **Delineation:** `<div style="page-break-before: always;"></div>` then `---` then the next `# Page: {Page Name}`. `[Prototype](hosted-url)` immediately under the page heading (before Meta Content).
- **One suite-level** Content Brief intro **before** the first `# Page:`. Compact landmarks — not an essay:

```markdown
**Site Purpose** (Context): One Section home for leadership, work groups, resources, and initiatives.
**Site Audience** (Context): ACC members in this Section, and visitors who need to log in or join.

## SiteCore Tree
(tree)

## State: Personalization
{DEV: This page has personalization look for RULEs in the content area}

## Shared UI {LM}

(Context) Define shared chrome once here. On each page, cite the item number in visual order. Do not repeat the UI or copy.

### 1. Item A
[UI Pattern - Name](url)
(Content)
…

### 2. Item B
[UI Pattern - Name](url)
(Content)
…
{Rule: Where and how this item is shared (which pages / states).}
```

`State: Personalization` = this suite/page has access variants; collectors look for `{Rule:}` on the `State:` zones in **Page Content**. Do **not** list every access state (Need to log in, Need membership, …) in the suite intro or Meta. **Shared UI** is one landmark with numbered items. Each item is pattern + `(Content)` plus `{Rule:}` for where it appears. On a page, write `Shared UI — N. Item name` in visual order. Do **not** repeat shared chrome (micro hero, DocMatter, Need Help) as full zones on child pages. Keep a child-page Micro hero zone only when it has page-specific slots (e.g. a unique hero title or a swapped CTA). **One Ticket** at the end covering all pages.
- **SiteCore Tree:** ASCII box-drawing tree (not HTML). Trailing `/` on nodes that have children. Start from ACC when the user gives a site path. **Site Structure / Placement** on each page repeats the tree and marks the current page with `← this page`.

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

When the user asks to **break a collection into separate documents** (only if a page is large/complex enough that a split helps):

- **Core document** — named after the hub / root, or `{Hub} - Core Pages.md`. Includes the hub / shared pages. One Ticket at the end. Save **all files in one suite folder**.
- **Dynamic listing pages** — Meta Content + intro zone only. Do **not** transcribe feed items. Close the listing zone with `(DEV) FEED`. Optional: item anatomy / facet labels as DEV notes.
- **Specialized feature / detail pages** — one document per page only when the user splits. Same H1 shape as core. Omit SiteCore Tree / Shared UI (those live in core). Short Ticket that points back to the core document.

**Default:** keep feature pages in the hub document. Do not split a suite just because a page is a child in the tree.

Personalization and page variants are **prototype-specific**. Do not assume access-state homes, numbered state files, or that meta can or cannot change. Follow the grouping the user gives for that collection.

## Legend (required structure)

Write this Legend **verbatim** (tokens self-color). Parent bullets = color + meaning for a reader. Italic sub-bullets = the Markdown that produces that color. Never use `<mark>`, `</mark>`, or color `<span>`s.

```markdown
# Legend

How to use this document:

- **Dark red** — Landmarks, slot labels, Document Labels, developer notes, and access rules
  - *End a UI landmark line with `{LM}`*
  - *`{DEV: …}` after a control (button, link, icon)*
  - *`{Rule: …}` for who sees this view (Sitecore personalization / access)*
  - *Document Labels: Legend, Content Brief, SiteCore Tree, Meta Title, Meta Description, Site Structure / Placement, Personalization States*
  - *Personalization zones start with `State:` (numbers optional — `State: Need to log in`, `State: Not purchased`)*
  - *Pages start with `# Page: {Name}`*
- **Green** — Collector context and constraints (not shippable copy)
  - *`(Context)` then the orientation sentence*
  - *`(Constraint)` then a non-length rule*
  - *`(Max: N chars)` or `(Min: …)` on the slot line — estimate N from that UI element*
  - *`(Content)` on its own line to start the shippable copy for that UI*
- **Gray** (white text) — `{Repeat: Name}` between repeating content blobs
  - *`{Repeat: Card}` / `{Repeat: Step}` / `{Repeat: Panel}` / `{Repeat: Accordion}` / `{Repeat: Category}` — name the UI. Use `{Repeat: UI}` when it is just a blob*
- **Yellow** — `{UX: UX still needs to answer}`
- **Magenta** — `{SME: SME still needs to answer}`
- **Blue** (white text) — Locked Member Section template (same for WIC, Imaging, and other Sections). Do not rewrite from SME comments. Section name / acronym / hashtag tokens may still swap.
  - *`Locked Zone` on its own line immediately before a repeating UI block*
  - *`Locked Content` on its own line immediately before one immutable slot*
- **Black (unmarked)** — Shippable copy for the webpage
  - *Bold title lines and ordinary paragraphs — not Markdown `#` headings (those are document structure for Word TOC)*
```

Repeatable-template collections also add the Locked Zone / Locked Content bullets (see below).

## Content Brief rules

### Section order

Contents, Legend, Content Brief, Pages, and Ticket are **H1**. Ticket is `# Ticket`.

1. `# Contents`
2. `# Legend`
3. `# Content Brief` — **Site Purpose** / **Site Audience** one-liners (not headings). Suite: then `## SiteCore Tree`, `## State: Personalization`, `## Shared UI {LM}` with `### 1. Item`
4. `# Page: {Page Name}` (H1 sibling of Content Brief). Suite: `# Page: {Page Name} ({tree label})` when the tree label differs
5. `[Prototype](hosted-url)` — directly after the page heading, before Meta Content (one line; no labeled “Prototype” heading)
6. `## Meta Content` — H2 (separates meta from Page Content). One-line purpose/audience, then H3s: **Meta Title**, **Meta Description**, **Site Structure / Placement**. If the page has access variants, one `### State: Personalization` pointer (not a four-state index). Values on the next line with **no blank line** after an H3.
7. `## Page Content` — H2. Zones in visual order. A `State:` is a zone. Top-level zones are `###` (`### State:` or `### Landmark {LM}`). Nested Landmark / Sub UI / child of `State:` is `####`; deeper nested UI is `#####`. Each zone: optional `Locked Zone` **before** the landmark/`State:`, then pattern + slots, then `(Content)`.
8. Optional Open Items
9. `# Ticket` (document-level; last in TOC). Children (`## Description`, `## References`, `## Page Location`, `## Acceptance Criteria`, `## Vanities`, `## Contact Information`, `## Images`) stay H2 under `# Ticket`

### Color assignment (what to write)

| Kind | Write |
|------|--------|
| Landmark / zone / section titles | Heading + `{LM}`, **or** a Document Label, **or** `# Page:` / `State: {label}` |
| UI slot / element labels | Stacked under the landmark with constraints on the same line; `{LM}` on the slot line |
| Pattern reference | `[UI Pattern - {Name}](arches-url)` from [pattern-dictionary.md](pattern-dictionary.md). No match: `{UX: find a referenced defined pattern}` |
| `{Rule: …}` | Who sees this view (personalization / access). Not `{DEV: Rule: …}` |
| On-page body copy | Unmarked Markdown |
| `(DEV) …` | Developer note with no control label (token through end of line) |
| `{DEV: …}` | **Controls inline** — after the visible label on the shippable line |
| `^@^` | Whole-line DEV note when the marker should hide in reading view |
| `(Context)` | Purpose, audience, orientation, limitations |
| `(Content)` | UI delineator — shippable copy for that landmark starts on the next line |
| `{Repeat: Name}` | Between repeating content blobs (not before the first, not after the last). Name the UI; `{Repeat: UI}` if unnamed |
| `(Constraint)` / `(Max: )` / `(Min: )` | Slot limits and pattern constraints |
| `{UX: …}` / `{SME: …}` | Open UX / SME items. Unmatched UI: `{UX: find a referenced defined pattern}` |
| `Locked Zone` / `Locked Content` | Locked Member Section template copy and chrome. Do not rewrite from SME comments. |
| Shippable copy & meta *values* | Unmarked |

### Zone anatomy (locked)

Order inside **Page Content**. `Locked Zone` (when used) **precedes** the zone — it is not inside `(Content)`.

```markdown
Locked Zone

#### State: Need to log in
{Rule: Visitor is not authenticated.}

[UI Pattern - Hero Image with CTA](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-component-microsite-heroimagewithcta.html)
Eyebrow {LM} (Max: 24 chars)
Section Name {LM} (Max: 40 chars)
Teaser Body {LM} (Max: 120 chars)
Roadblock Heading {LM} (Max: 55 chars)
Roadblock Body {LM} (Max: 140 chars)
CTA Label {LM} (Max: 20 chars)
(Constraint) CTA label is template chrome

(Content)
**Women In Cardiology**
This section offers women cardiologists opportunities to strengthen their professional support system and skills.

Join Now {DEV: Button, Primary, URL: …, Label: Join Now }
```

1. **`Locked Zone`** — own line **before** the zone when the whole zone is template chrome. Single immutable slot in a mixed zone: `Locked Content` on its own line immediately before that slot label (still with the other slots under the landmark).
2. **Zone landmark** — UI element: heading + `{LM}`. Personalization: `State: {label}` (a zone, not a meta-only list). Name UI landmarks for the on-page title, not the Arches pattern.
3. **`{Rule: }`** — on a `State:` zone, the Sitecore/access condition. Example: `{Rule: Visitor is not authenticated.}`
4. **Pattern + slots** (no `UI description` heading)
   - **Pattern:** `[UI Pattern - {Name}](url)` from [pattern-dictionary.md](pattern-dictionary.md). No match → `{UX: find a referenced defined pattern}` (keep the zone prototype `#id` nearby). Do not invent a pattern name. Do not write a “UI visible” inventory.
   - **Slot labels + constraints, stacked** directly under the landmark. Each slot on its own line: `Section Name {LM} (Max: 40 chars)`. Character limits: `(Max: N chars)` / `(Min: )`. Non-length rules: `(Constraint) …`. **Estimate N from that UI element** (type size, column width, typical line count). Do **not** copy `(Max: 80 chars)` / `(Max: 150 chars)` onto every headline/body. Meta Title / Meta Description stay 80 / 150 (SEO). Long-form (letters, FAQ answers, mission paragraphs) omit a Max. Starting points: [pattern-dictionary.md](pattern-dictionary.md) slot-length table.
5. **`(Content)`** — shippable copy only, grouped. **No ATX headings** (`#` / `##` / `###`). On-page titles are **bold** (or plain). Heading rank is on the landmark or slot line, not in the paste. Controls **inline** on the shippable line. Nested UI: **Sub Landmark** `{LM}` then that sub-UI’s slots + copy kept together. Repeating items: `{Repeat: Card}` (or `Step` / `Panel` / `Accordion` / `Category`) on its own line **between** blobs — not before the first, not after the last. Use `{Repeat: UI}` when it is just a blob.
6. **`---` between combos.** After a landmark’s `(Content)` (and before the next UI element), put a horizontal rule. Place it before `Locked Zone` / `Locked Content` when those precede the next landmark. Do **not** add a second `---` when one is already there (access states, page breaks). Do **not** put `---` before the first UI on a page / in a `State:`.

```markdown
(Content)
**Section Benefits**
Professional Online Community {DEV: Icon: fa-users }

---

Locked Zone
#### Work Groups {LM}
```

Keep `### State:` (and other top-level zones) under `## Page Content`. Nested landmarks drop a level (`####` then `#####`). The example `#### Work Groups {LM}` is only correct when it is nested under a parent zone (a `State:` or another landmark). A sibling zone under Page Content is `### Work Groups {LM}`.

Do **not** sandwich every sentence between a label and a value. Keep `{UX: }` / `{SME: }` / extra `(DEV)` out of `(Content)` when they would interrupt paste. Controls stay **inline** in `(Content)`.

### Density (page space)

The document is a collector worksheet, not an agent runbook.

- Prefer `###` / `####` over extra labeled paragraphs.
- One blank line between blocks. No extra blank after an H3 before its value.
- `---` between each UI + `(Content)` combo, before the next landmark starts.
- `(Context)` / `(Constraint)` = **short** orientation and limits only. Do not paste process rules collectors cannot act on (e.g. “no section id / deep link required”, long Locked Content how-to, “Sitecore rendering…”).
- Do not duplicate a page `[Prototype](url)` inside every zone when Meta Content already has it. Landmark links stay as `[Prototype](url#id)`.
- If a `[Prototype](url)` already shows the view, do **not** add a **UI visible** inventory. Use `[UI Pattern - Name](url)` plus a short `(Context)` line instead.

### Repeatable templates (Locked Zone / Locked Content)

**Locked Zone** and **Locked Content** mark locked Member Section template. It is the generic design — the same UI and sentences used for WIC, Imaging, and every other Section. Do **not** update it from SME comments, even when SMEs ask to cut, rewrite, or replace that copy. Only tokens swap (section name, acronym, hashtag). Section-authored copy (mission cards, chair letter, work-group bodies, featured initiatives) is unmarked and *is* what SMEs change.

Use `Locked Zone` / `Locked Content` when the collection is a Member Section (or another template reused across many sites). Do not invent these tags on one-off pages.

- **Whole template zone** — put `Locked Zone` on its **own line immediately before** the zone landmark. Do **not** tag every slot inside it. Optional `(Constraint)` under the landmark: which slots are in the zone vs section-authored.
- **Single slot in a mixed zone** — put `Locked Content` on its own line immediately before that slot label.
- Mark **immutable template chrome** only: roadblock instructions, Need Help / Member Care, join/unlock bands, listing-page intros, DocMatter closer, zone labels (Announcements, Resources, Library), Work Groups chrome (“Getting Involved?”, status chip string), Home intro body (“Stay up to date with Section-specific…”). Do **not** mark Section Benefits items, chair names/roles, or other section-authored lists.
- **Do not mark** section-authored copy (mission/focus cards, chair letter, quotes, initiative names), **data-model** fields (names, photos, work-group titles/bodies), or feed items.
- Tokens such as section name, acronym, and hashtag may sit inside an otherwise-locked sentence. Keep the zone (or slot) mark; add a short `(Constraint)` that only the token swaps. Do not glue that note onto the shippable line.
- **SME intake:** Skip comments that rewrite Locked Zone / Locked Content copy. Record them only if the user explicitly overrides the template. Shared UI items that are template chrome follow the same lock.
- Add these Legend bullets:

`Locked Zone` A repeating UI block locked in the Member Section design. Shared across Sections (WIC, Imaging, …). Do not apply SME rewrites.

`Locked Content` A single locked slot inside a mixed zone. Generic template content, not Section-authored.

Example — whole landmark:

```markdown
Locked Zone

### Unlock This Content {LM}

[UI Pattern - Follow Up CTA — Beveled Card](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-recipes-page-followupcta-beveledcard.html)
**Headline** {LM} (Max: 40 chars)
**Body** {LM} (Max: 180 chars)

(Content)
**Want to gain access to all of the exclusive content and more?** Manage your membership today to join this Member Section and unlock all the benefits.

Manage Membership {DEV: Button, Shade, URL: membership management, Label: Manage Membership }
```

### Meta Content

`## Meta Content` is an H2 (keeps meta visually separate from `## Page Content`). Compact fields:

```markdown
## Meta Content
**Page Purpose** (Context): Help clinicians feel seen and know where to start.
**Primary Audience** (Context): Clinical leaders looking for a first step.
### Meta Title (Max: 80 chars)
Care for Yourself
### Meta Description (Max: 150 chars)
…
### Site Structure / Placement
```

1. **Page Purpose** / **Primary Audience** — one line each: black label, then `(Context):` sentence (label stays black; the note greens). Do **not** use separate headings for these.
2. `### Meta Title (Max: 80 chars)` — Document Label; **value unmarked** on the next line
3. `### Meta Description (Max: 150 chars)` — Document Label; **value unmarked**
4. `### Site Structure / Placement` — ASCII tree with `← this page`
5. `### State: Personalization` — only when the page has variants. One pointer; do **not** list each access state here. `{Rule: }` and full UI live on the `State:` zones in **Page Content**.

```markdown
### State: Personalization
{DEV: This page has personalization look for RULEs in the content area}
```

**Prototype does not live here.** Put `[Prototype](hosted-url)` **directly after the page heading** and before `## Meta Content`:

```markdown
# Page: Care for Yourself (Self Care)

[Prototype](https://acc-style.github.io/PrototypingACCorg/clinical-wellbeing/Concept-Clinician-Well-Being-Mental-Health/)

## Meta Content

**Page Purpose** (Context): Help clinicians feel seen and know where to start.
```

#### Page Purpose & Primary Audience

Keep both **concise** (one or two sentences). When the user supplies UX value / audience research, **use it** to aim the copy—do not paste the research into the document.

- **Page Purpose** — what we hope users get: feel seen, know where to start, stay in the work more sustainably. Name the College’s role only as it serves the user.
- **Primary Audience** — who this page is for, in plain language. Prefer the page’s primary people (e.g. clinical leaders on a team page) over listing every suite audience.

Do **not** put Page Layout (zones) here — zones belong in Page Content.

### Page Content

`## Page Content` is an H2. Write **zones** in visual order using [Zone anatomy](#zone-anatomy-locked). Personalization **is** a zone: `### State: {label}` then pattern/slots + `(Content)`. Top-level zones under Page Content are `###`. Nested Landmark / Sub UI / child of `State:` drops to `####`; deeper nested UI drops to `#####`. Do not rename a landmark to a generic pattern name. Put the pattern on `[UI Pattern - {Name}](url)`. **No ATX headings inside `(Content)`.**

Optional short numbered list of visible zone names at the top of Page Content only when the page is long or personalized. Prefer the zones themselves.

### Landmarks (zone headings)

- Group by UI landmarks. Combine adjacent slots that collectors copy as one unit (heading + body + CTA).
- Shippable titles live in `(Content)` as **bold** (or plain) — never `#` / `##` / `###`. Word TOC uses collector headings only (Heading 1–3).
- Nested Landmark / Sub UI `{LM}` is a collector heading **before** `(Content)` and drops one level from its parent zone (`####` under `###`, `#####` under `####`). Do **not** put ATX headings after `(Content)`.
- Keep `(Context)` **short**. Skip agent-only notes.
- **Prototype deep link:** `[Prototype](https://acc-style.github.io/PrototypingACCorg/{collection-path}/#id)` near the zone when the pattern is unmatched (`{UX: find a referenced defined pattern}`), or when a `#id` exists. Never `127.0.0.1` / `localhost`.
  - Example: `[Prototype](https://acc-style.github.io/PrototypingACCorg/acc/Journal-TextEdit/#Why-Publishing)`
  - **Skip** deep links on hero / micro hero chrome and above-the-fold start-of-page — do not flag missing ids as `{UX: }` items.
- Controls **inline** in `(Content)`. `{DEV: }` mid-line after the visible label. `(DEV)` on its own line only when there is no control label.
- Icons: Font Awesome class names in `{DEV: Icon: fa-…}` or `(DEV) Icon: fa-…`.
- Links/images: `{DEV: Link: …}` / `{DEV: Img Src: …}` inline, or `(DEV)` if the note is a full line.
- Pattern lookup: [pattern-dictionary.md](pattern-dictionary.md). Index: https://assets.acc.org/Arches/Latest/docs/boot_acc/index.html

### Tables (Word-safe)

- **Max 3 columns.** Wider tables are hard to edit/read in Word — do not use them.
- Prefer **stacked item blocks** or lists for repeating cards/grids.
- **UI Component / layout pattern notes** (e.g. “Icon + text grid with expanded click area jump links”) belong in `(DEV)`, not a table and not a multi-column matrix.

**Repeating card / grid pattern (preferred):**

```markdown
### Why We Publish {LM}

[UI Pattern - Grid List with Linked Descriptions](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-recipes-gridlist-linkedicontext.html)

(Content)
**Mission & Impact** {LM} How publishing advances… {DEV: Icon: fa-lightbulb; Jump: #Why-Publishing }

{Repeat: Card}

**Education** {LM} How publishing trains… {DEV: Icon: fa-graduation-cap; Jump: #Education }
```

**Journal / media item (Sub Landmark):**

```markdown
**JACC** {LM} Top research across all cardiovascular medicine. **Best for:** All cardiovascular professionals {DEV: Link: https://www.jacc.org/journal/jacc; Img Src: https://…/logo-JACC-….png }
```

### Inline DEV notes

Controls sit **inline** on the shippable Content line:

```
Join Now {DEV: Button, Primary, URL: https://…, FUNCTION: navigate, Label: Join Now }
```

Own-line `(DEV)` only when there is no control label:

```
(DEV) Add image to right of text: https://www.acc.org/-/media/…jpg
(DEV) Anchor ID: #Why-Publishing
```

`^@^` at end of line: whole-line DEV note with the marker hidden in reading view.

#### Button colors

| Color | Use |
|-------|-----|
| **Primary** | Page primary action. With audience breakdowns, may be section primary. |
| **Shade** | Off / secondary actions |
| **Secondary** / **Accent** | Rare split-primary; use sparingly |

`(DEV) Button, Primary|Secondary|Shade|Accent, URL, FUNCTION, & Label`

#### Personalization & purchase

`{Rule: Logged-in user has product code}` then the matching `State: Purchased` / `State: Not purchased` zones. Controls still use `{DEV: }`.

#### Details & summaries

`[UI Pattern - Accordion](https://assets.acc.org/Arches/Latest/docs/boot_acc/item-component-accordion.html)` under the landmark. `(DEV)` only for extra build notes (short IDs, no spaces).

## Ticket section (last)

`# Ticket` is an H1 (last in the document). Children stay `##`. Boilerplate + page-specific. Contacts: **ECDS Lead / UX: Matt Watier, Rowena**.

### Acceptance Criteria (always include)

- Construct the page based on best Sitecore Practices
- Base all content on *this Document* vs Wires
- Use golden standard patterns from the ARCHES pattern library
- Plus page-specific criteria

## Workflow checklist

```
- [ ] Confirm source (prototype default)
- [ ] `[Prototype](hosted-url)` after each `# Page:`; landmark `#id` links the same way (never 127.0.0.1 / localhost)
- [ ] Extract between Content Collection markers (+ partials)
- [ ] Major zones are H1: `# Contents`, `# Legend`, `# Content Brief`, `# Page:` (repeat), `# Ticket` (last)
- [ ] Legend: `# Legend`; color + meaning parent bullets; italic token subs; no `<mark>` / color spans
- [ ] Document Labels spelled exactly: Legend, Content Brief, SiteCore Tree, Meta Title, Meta Description, Site Structure / Placement, Personalization States
- [ ] Content Brief: **Site Purpose** / **Site Audience** one-liners (black label + `(Context)`; not Document Labels). Suite intro: `## SiteCore Tree`; `## State: Personalization` + `{DEV: This page has personalization look for RULEs in the content area}` (not a four-state `{Rule:}` index); `## Shared UI {LM}` with numbered items as `### 1. Item`; `Locked Zone` / `Locked Content` for locked Member Section template (do not apply SME rewrites)
- [ ] Each page: `# Page: {Name}`; Prototype; `## Meta Content` (one-line purpose/audience — not headings; then `### Meta Title` / Description / Site Structure / State: Personalization); `## Page Content`; top-level zones `###` (`### State:` or `### Landmark {LM}`); nested Landmark / Sub UI `####`; deeper nested UI `#####`; `{Rule: }` on `State:` zones; `[UI Pattern - Name](url)` + stacked slots under the landmark (no `UI description` heading); `(Max: N)` estimated per slot (not 80/150 everywhere); `(Content)` then grouped copy, **bold titles (no ATX headings)**, `{Repeat: Card}` (or Step / Panel / Accordion / UI) between repeating blobs, controls inline
- [ ] Unmatched UI: `{UX: find a referenced defined pattern}`; FA class names; Link: / Img Src: for media rows
- [ ] `{UX: }` / `{SME: }` gaps
- [ ] Ticket: `# Ticket`; children stay `##` (`Description`, `References`, `Page Location`, `Acceptance Criteria`, `Vanities`, `Contact Information`, `Images`); hosted Markdown links
- [ ] Save as {Page Name}.md under Obsidian path
- [ ] Suite: confirm page list + tree; keep simple feature pages in the hub file; page-break between pages; pages are H1 siblings of Content Brief; one `# Ticket`
- [ ] Iterate; update this skill when rules change
```

## Iteration

When the user corrects output, **update this skill** so the next run matches. Prefer short rule additions over long prose.

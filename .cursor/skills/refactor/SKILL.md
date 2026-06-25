---
name: refactor
description: >-
  Systematically breaks dense, long-winded ACC legacy content into skimmable
  chunked UI — for personalization, guided processes, audience splits, product-
  journey stages, return-visitor shortcuts, and scanability. Use when refactoring
  overloaded pages, wall-of-text content, legacy ACC.org pages, CMP/MOC product
  hubs, content architecture, chunking, readability improvement, or when the
  user names refactor or skimmable design.
disable-model-invocation: false
---

# Content Refactor

A core ACC design principle: move away from **long-winded, dense online representation** toward **skimmable, chunked content display**.

Use this skill when a page, section, or CMS block has **too much content in one place** and needs to be systematically broken into smaller pieces.

## What refactor solves

| Goal | Refactor tactic |
|------|-----------------|
| **Personalization** | Separate chunks authors can show/hide per audience or profile |
| **Guided process** | Ordered steps with clear entry, progress, and next action |
| **Audience division** | Parallel paths (member vs public, role, topic branches) |
| **Process-stage division** | CTAs that route users by where they are in a product journey |
| **Return-visitor skip** | Jump nav, anchors, deep links to last state, teasers not full body |
| **Scanability** | Headlines, cards, lists, short blocks — prose only where depth is needed |

## When to invoke

- Legacy page is a wall of text or one endless scroll
- User asks to **refactor**, **chunk**, **break down**, or make content **skimmable**
- Multiple audiences **or product stages** share one URL
- Content mixes overview + deep detail + CTAs without hierarchy
- Same page serves first-time visitors and return visitors poorly

**Pair with:** [acc-ux-designer](../acc-ux-designer/SKILL.md) for Arches markup and delivery path.  
**Copy quality:** [readability](../readability/SKILL.md) after chunking · [competitive-analysis](../competitive-analysis/SKILL.md) for peer patterns.

## Refactor workflow

Copy and track:

```
Refactor progress:
- [ ] 1. Audit — inventory content, audiences, and jobs-to-be-done
- [ ] 2. Classify — assign each block a refactor strategy (see strategies.md)
- [ ] 3. Chunk — one idea per card/section; cut or defer depth
- [ ] 4. Pattern — pick UI pattern per chunk (see patterns.md)
- [ ] 5. Wire — nav, anchors, skip paths, optional gates
- [ ] 6. **Readability pass** — score and rewrite copy ([readability](../readability/SKILL.md))
- [ ] 7. Validate — scan test, mobile chunk count, return-visitor path, readability target 29+
```

### Step 1 — Audit the overload

For each content block, note:

- **Audience** — who is this for?
- **Intent** — learn, decide, act, browse?
- **Frequency** — first visit vs return?
- **Depth** — overview (skim) or reference (read)?

Flag blocks that fail the **5-second skim test** — no clear headline, no visual break, or multiple ideas in one paragraph.

### Step 2 — Choose a strategy

See [strategies.md](strategies.md) for full detail. Pick **one primary strategy per page**:

| Strategy | Signal |
|----------|--------|
| **Hub & spoke** | Many equal topics — user picks a branch |
| **Progressive disclosure** | Overview first; detail on demand |
| **Audience fork** | Distinct paths (login, member, section, role) |
| **Process steps** | Linear or mostly-linear workflow |
| **Teaser + destination** | Summary here; full content on child page |

### Step 3 — Chunking rules

1. **One job per chunk** — one card, one list item, one section header
2. **Headline first** — `font_display` title before any paragraph
3. **Cap prose** — if >3 sentences in a skim zone, split or move to detail
4. **Action visible** — each chunk ends with link, button, or next step
5. **Defer depth** — move long copy to child page, strategic accordion ([accordions.md](accordions.md)), or PDF
6. **Repeatable units** — same card/list pattern for parallel items (courses, awards, topics)

### Step 4 — Apply Arches patterns

Map chunks to patterns in [patterns.md](patterns.md). Prefer existing PageBlocks and gold-standard markup.

### Step 5 — Validate

- **Skim path:** Can someone grasp the page in 10 seconds from headings + cards only?
- **Return path:** Can a repeat visitor jump past intro copy?
- **Mobile:** Do chunks stack as single-column cards without horizontal scroll?
- **Audience:** Are forks obvious before users read paragraphs?

## Output by deliverable

| Output | Where |
|--------|-------|
| Refactor plan (markdown) | Chat or brief in page `notes:` front matter |
| Chunked prototype | `_collections/__prototypes/` |
| Reusable block | `_includes/Blocks/` or `PageBlocks/` + `_data/` |
| Gold pattern | `_collections/_ui_gold_standard/` |

## Anti-patterns

- Replacing a text wall with a **text-in-image** graphic — same SEO, a11y, and responsive problems; chunk into HTML ([imagery.md](../acc-ux-designer/imagery.md))
- Refactoring into **more paragraphs** instead of fewer, larger chunks
- One accordion hiding an entire unmaintained wall of text — chunk **before** collapsing; see [accordions.md](accordions.md)
- Using accordions to **shorten** the page when first-visit users need that content — keep valuable copy visible
- JS accordion widgets instead of native `<details>` / `<summary>`
- Forcing linear steps when users need a **hub** (topic picker)
- Hiding the only CTA below fold after chunking — per-chunk actions
- Using action colors or highlight/info for decorative chunk borders — see acc-ux-designer

## Additional resources

- [strategies.md](strategies.md) — refactor goals and tactics
- [patterns.md](patterns.md) — UI patterns in this repo
- [accordions.md](accordions.md) — strategic disclosure on product pages
- [examples.md](examples.md) — reference pages

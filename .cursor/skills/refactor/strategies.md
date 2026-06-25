# Refactor Strategies

Tactics for breaking overloaded content into smaller, purposeful pieces.

## 1. Scanability (default goal)

**Problem:** Dense prose, buried links, no visual hierarchy.

**Tactics:**

- Replace paragraph lists with **icon-decorated lists** or **card grids**
- Lead with **display headings** (`font_display`); body stays `font_copy`
- Use **short supporting line** under title — not a second paragraph in the skim zone
- Break long pages into **labeled sections** with `m-b_5` rhythm between them
- Meta / dates / flags as **inline pipes** or small type (`font-size_down`, `c_shade-n2`)

**Before → after:**

```
BEFORE: 3 paragraphs intro + 12 links in a bullet list
AFTER:  H2 + 1 sentence intro + 4 topic cards with title + 1 line + CTA each
```

## 2. Personalization

**Problem:** One page serves users who need different subsets of content.

**Tactics:**

- Split into **independent PageBlocks** authors can reorder or omit in CMS
- **Data-driven cards** from CSV/YAML (`site.data`) — swap rows per campaign
- **Conditional includes** in Liquid for member state (see member section prototypes)
- **Separate teasers** per segment with shared hub page

**Signals:** "Members see X, public sees Y", regional variants, role-based modules.

## 3. Guided process (step-through)

**Problem:** User must complete or understand a sequence (apply, enroll, configure).

**Tactics:**

- **Numbered or staged sections** with clear "current step" styling (`is-current`)
- **One primary CTA per stage** — `btn-primary` forward, `btn-shade` back/skip
- **Progress or section labels** in header (Version, Step 2 of 4)
- **Roadblock / gate** only when the step truly requires it — not for all content

**Pattern refs:** segmented card with footer CTA, page blocker flow, wizard-style prototypes.

## 4. Audience & process-stage division

**Problem:** Mixed audiences on one URL — **or** users at different points in the same product journey (exploring vs enrolling vs already enrolled).

Not all division is login-based. Many users are authenticated but need **different content based on where they are in a process** (eligibility, enrollment, active participation, renewal).

### Access-based division

- **Fork early** — hero or first screen presents paths, not a long shared intro
- **Page blockers** with teaser for gated content (`grid-template-page-blocker`)
- **Distinct child pages** per access level instead of inline walls of text

**Pattern refs:** `_member_section_prototype/0_page-blocker-login.html`, `1_page-blocker-member.html`

### Process-stage division (product journey)

**Problem:** One dense page tries to explain the whole product lifecycle to everyone.

**Tactics:**

- **Process CTA cards** on a hub — one card per journey stage, each linking to a dedicated child page
- **Foreshadow the journey** on the hub (short intro + stage cards) without full detail for every stage
- **Chunk IA across pages** — each stage gets its own URL for CMS, SEO, and **direct marketing back to last state**
- **State-aware widgets** — wizard/progress UI shows current step (login → eligibility → progress → status)
- **"Next Steps" CTAs** for enrolled users — numbered actions, not re-reading enrollment copy

**Canonical example:** [Collaborative Maintenance Pathway hub](https://www.acc.org/Education-and-Meetings/Maintenance-of-Certification-Information-Hub/Collaborative-Maintenance-Pathway)

Hub presents three parallel CTAs:

| Stage | User need | Typical CTA |
|-------|-----------|-------------|
| Exploring | What is this? | Learn More → `What-is-the-CMP` |
| Ready to start | Am I eligible? Enroll | Enroll Now → `Enroll-in-the-CMP` |
| Active participant | What do I do this year? | Next Steps → `Already-Enrolled-in-the-CMP` |

Each child page holds **only** that stage's content — assessment dates, SAP links, and deep detail move off the hub.

**Why this is two-fold:**

1. **Foreshadows** the full process so new users understand the arc without reading everything
2. **Enables** chunked IA, personalized widgets, and campaign deep links that return users to their current step

**Pattern refs:** `__prototypes/_archive/CMP-Marketing.html`, `CTA-Gallery.html` (CMP Next Steps card), `CMP/interactive_wizard.html`, `__ui_playground/CMP-Wizard.html`

### Parallel hubs (topic branching)

- Topic nav tiles when division is by **subject** not **stage** (Arrhythmias | Heart Failure | Prevention)
- **Pattern refs:** `Course-Compact.html`

## 5. Return-visitor skip & deep-link state

**Problem:** Repeat users re-read intro copy to reach tools, lists, or **their current product step**.

**Tactics:**

- **Deep-link child pages** per process stage — market directly to enrolled vs exploring URLs
- **In-page anchor nav** — topic tiles linking to `#section-id`
- **Sticky or jump nav** for long reference pages (`AnchorPageNav.html`)
- **State widgets** that open on the user's current step (CMP wizard, enrolled Next Steps card)
- **Collapse secondary intro** — move mission copy below the actionable grid
- **Date/status lists** with runtime sort (open/upcoming/past) — users go straight to relevant slice

**Pattern refs:** `Course-Compact.html` topic nav, `award_schedule.html` DateList, CMP `Already-Enrolled` child page, `CTA-Gallery.html` CMP Next Steps

## 6. Hub & spoke (topic branching)

**Problem:** Many peer topics; no single linear story.

**Tactics:**

- **Hub page:** short intro + grid of topic entry cards
- **Spoke pages:** one topic depth per URL
- **Counts or badges** on hub tiles ("12 courses") for scan value
- **Breadcrumb back** to hub on every spoke

**Pattern refs:** `Course-Compact.html`, `ClinicalTopicAlpha.html`, `CTA-Gallery.html`

## 7. Progressive disclosure

**Problem:** Some users need depth; most need summary only.

**Tactics:**

- **Card front:** title + 1–2 lines + CTA
- **Detail:** child page or accordion body — not inline in hub
- **Segmented card:** colored header (skim) → body list → footer CTA → optional aside (meta)
- **Follow-up CTA row** at section end for next logical action only
- **Strategic accordions** on product pages — native HTML, shared labels, deep-link IDs; see [accordions.md](accordions.md)

**Accordion gate:** Only collapse content for **second-time visitors** or **reference readers**. Valuable first-visit copy stays visible and scrollable — accordions are not a device to make the page shorter.

**Pattern refs:** `card-segmented.html`, `photo-text-lockup.html`, `FollowUpCTA.html`, `SAP/wrap-up-content.html`

## Choosing a primary strategy

```
Mostly peer topics?           → Hub & spoke
Sequential product lifecycle? → Process-stage CTA cards + child pages (CMP pattern)
Sequential task?              → Guided process / wizard widget
Different access levels?      → Audience division (login / member blockers)
Same page, mixed depth?       → Progressive disclosure
Long reference doc?           → Return-visitor skip + deep-link state
CMS needs modular authoring?  → Personalization (PageBlocks)
```

Multiple strategies can combine — e.g. hub & spoke **with** anchor skip on the hub.

## Content cut checklist

When chunking, ask for each paragraph:

1. Can this become a **card title**?
2. Can this become a **single list item** with bold lead-in?
3. Should this move to a **child page**?
4. Is this **audience-specific** — fork instead of inline?
5. Is this **repeat-visitor noise** — demote below jump nav?

If none apply and it stays prose, keep it in a `reading-typography` block — but limit to one dense prose zone per view.

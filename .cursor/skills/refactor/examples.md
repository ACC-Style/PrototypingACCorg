# Refactor Examples

Before/after references in this workspace.

## Process-stage division — CMP (Collaborative Maintenance Pathway)

**Live hub:** [Collaborative Maintenance Pathway](https://www.acc.org/Education-and-Meetings/Maintenance-of-Certification-Information-Hub/Collaborative-Maintenance-Pathway)

| File | What was refactored |
|------|---------------------|
| `__prototypes/_archive/CMP-Marketing.html` | Hub hero + **three stage CTA cards** (Learn / Enroll / Already Enrolled) + topic/date matrix on child content |
| `__ui_playground/CMP-Wizard.html` | Main prose + sidebar **journey wizard** (step chevrons, state per login/eligibility/progress) |
| `__prototypes/CMP/interactive_wizard.html` | Wizard states: locked → loading → status with product list |
| `__prototypes/CTA-Gallery.html` | **CMP Next Steps** card for enrolled users — numbered SAP launch steps |
| `__prototypes/EDU/products.html` | CMP promo chunk with pipe-linked CTAs to hub and MOC info |

**Takeaway:** Audience division is **journey-stage**, not just login. Hub CTAs foreshadow the process, chunk content across IA/child pages, and enable marketing deep links back to a user's last state (exploring, enrolling, enrolled).

## Hub & spoke — course catalog

| File | What was refactored |
|------|---------------------|
| `__prototypes/Course-Compact.html` | Long intro compressed; **topic hub tiles** (Arrhythmias, HF, Prevention) with anchor jump; course cards grouped by `#section-id` |

**Takeaway:** User picks a topic in 4 tiles — skips reading full catalog intro.

## Time-sliced lists — awards

| File | What was refactored |
|------|---------------------|
| `__generators/award_schedule.html` | Flat CSV source → runtime **Open / Upcoming / Past** sections; cards scannable; return visitors go to open slice |

**Takeaway:** One dense schedule becomes three skim lists sorted by relevance to today.

## Strategic accordions — SAP product pages

**Live:** [ACCSAP](https://www.acc.org/Education-and-Meetings/Products-and-Resources/SAP/ACCSAP)

| File | What was refactored |
|------|---------------------|
| `__prototypes/SAP/wrap-up-content.html` | Visible "who should use" + benefits; **shared-label** `<details>` for TOC, objectives, credit, dates, refund |
| `__prototypes/_archive/SAP-FAQ.html` | FAQ as native `<details>`; question-as-summary |
| `__ui_playground/_archive/Accordion.html` | Styled accordion + `id` on bodies + hash deep-link open |

**Takeaway:** First-visit value stays on the scroll path; reference and compliance detail collapses with consistent labels and linkable IDs. See [accordions.md](accordions.md).

## Audience division — member content

| File | What was refactored |
|------|---------------------|
| `_member_section_prototype/0_page-blocker-login.html` | Login gate before any dense member UI |
| `_member_section_prototype/1_page-blocker-member.html` | Section membership fork with **teaser** + single join CTA |
| `PageBlocks/_global/AccessBarred.SectionTeaser.html` | Preview chunk shown before access |

**Takeaway:** Fork early; don't bury member-only content in long public copy.

## Card grids — parallel items

| File | What was refactored |
|------|---------------------|
| `__prototypes/PageBlocks/Cards.html` | Data-driven card grid from `site.data` |
| `__prototypes/PageBlocks/Cards_Images.html` | Image + title + blurb chunks |
| `__prototypes/CTA-Gallery.html` | CTA variations as comparable chunks |

## Single-topic depth — segmented card

| File | What was refactored |
|------|---------------------|
| `_ui_gold_standard/card-segmented.html` | Header (label) + scannable list + footer CTA + meta aside |

**Takeaway:** One clinical topic as one chunk with clear action — not an essay.

## Long taxonomy — jump navigation

| File | What was refactored |
|------|---------------------|
| `__prototypes/AnchorPageNav.html` | Massive topic tree with nav + anchored sections |
| `__prototypes/ClinicalTopicAlpha.html` | Alpha-nav for browse/skip |

**Takeaway:** Return visitors and power users jump; intro stays minimal.

## Section closer — next step

| File | What was refactored |
|------|---------------------|
| `_includes/Blocks/FollowUpCTA.html` | End-of-section CTA row — one chunk prompting next action |
| `__prototypes/PageBlocks/CTA_Callouts.html` | Callout chunks |

## Hero compression

| File | What was refactored |
|------|---------------------|
| `_ui_gold_standard/Concept-Anchor-Hero.html` | Title + breadcrumb in grid hero — not paragraphs in hero |
| `__prototypes/Concept-EDU-MEETING.html` | Full concept with feature cards below short hero |

## Refactor audit template

Use when starting a legacy page refactor:

```markdown
## Page: [name / URL]

### Audiences & journey stages
- Access level (public / member / section):
- Product stage (exploring / enrolling / active / renewal):

### Jobs to be done
- First visit:
- Return visit (deep-link target URL):

### Overload inventory
| Block | Words (est) | Strategy | Target pattern |
|-------|-------------|----------|----------------|
| Intro | | Compress | Hero + 1 line |
| … | | Hub & spoke | Topic tiles |

### Skip / deep-link path
- Return visitors land at (URL or widget state):
- Anchor / nav:

### Child pages needed
- 
```

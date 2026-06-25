---
published: false
---

# Cardiology as a Career Path — Content Collection & Refactor Plan

## Legend

- <span style="color:red">Red text — metadata, layout notes, UI slots, developer instructions.</span>
- <span style="color:red">{ } — inline production notes (URLs, component behavior).</span>
- <mark>Yellow — UX open items.</mark>
- <span style="background-color:#ffc0cb">Pink — SME content gaps.</span>

---

## Refactor Summary

<span style="color:red">**Source section**</span>  
https://www.acc.org/Tools-and-Practice-Support/Cardiology-as-a-Career-Path and child pages (legacy `arches-cardiology` microsite in `_archive/CardiologyCareers*`).

<span style="color:red">**Primary strategy**</span>  
**Hub & spoke** with **audience fork** (where you are now) and **process-stage division** (training milestones on physician path). Progressive disclosure for CV Team role reference (category groupings + native `<details>`, not 22 stacked Bootstrap accordions).

<span style="color:red">**Business goals**</span>

1. Strengthen the cardiovascular talent pipeline — attract students, trainees, and allied professionals before they choose another specialty.
2. Position ACC as the career companion from exploration through leadership — not only a membership org for established cardiologists.
3. Route users to ACC programs (Young Scholars, FIT resources, leadership academies, clinical trials program) and membership entry points.
4. Consolidate inspiration content (personal stories + video gallery) so motivation and practical next steps sit on one journey.

<span style="color:red">**User goals**</span>

| Audience | Job to be done |
|----------|----------------|
| High school / college students | Understand what cardiology is and whether it fits their interests |
| Medical students & residents | Find training-stage resources, timelines, and peer advice |
| CV Team prospects (NP, RN, PA, pharmacy, tech) | Discover roles beyond physician and see education paths |
| Clinical research–curious clinicians | Learn how to move into trial leadership and funding |
| Early / mid-career professionals | Find leadership development and mentorship programs |
| Return visitors | Jump past intro copy to their pathway or training stage |

<span style="color:red">**Legacy problems addressed**</span>

- Hub page mixed overview, inspiration, and CTAs without a clear first action.
- CV Team page was a 600+ line accordion wall — unmaintainable and fails the 5-second skim test.
- Physician pathway was an undifferentiated link list by training stage.
- Video gallery and personal stories duplicated “why cardiology” intent on separate URLs.
- Development programs appeared on hub copy and a separate page without journey context.

---

## Information Architecture (refactored)

| Page | File | Strategy |
|------|------|----------|
| **Hub** | `Concept-Career-Path.html` | Hub & spoke — audience fork, pathway picker, inspiration teaser |
| **Start Here** | `Concept-Career-Path-Start.html` | **Guided audience fork** — persona self-select → 3 actionable next steps per segment |
| **Physician Pathway** | `Concept-Career-Path-Physician.html` | Process steps by training stage |
| **CV Team Pathway** | `Concept-Career-Path-CVTeam.html` | Hub tiles by role category + reference disclosure |
| **Clinical Research** | `Concept-Career-Path-ClinicalResearch.html` | Teaser + destination (education, awards, publications) |
| **Level Up (bridge)** | `Concept-Career-Path-Leadership.html` | Thin crossroads CTA only — **canonical catalog:** [Professional Development Programs](https://www.acc.org/Education-and-Meetings/Professional-Development-Programs) |
| **Inspiration** | `Concept-Career-Path-Inspiration.html` | Unified stories + video gallery |
| **Contact** | `Concept-Career-Path-Contact.html` | Single-purpose support CTA |

<span style="color:red">**Prototype partials**</span> — `_includes/Career-Path/*.html`

---

# Hub Page — Cardiology as a Career Path

<span style="color:red">**Meta title**</span>  
Cardiology as a Career Path | American College of Cardiology

<span style="color:red">**Meta description**</span>  
Explore cardiology careers, training pathways, CV Team roles, leadership programs, and stories from ACC members — whether you are a student, trainee, or considering a career change.

<span style="color:red">**Layout zones**</span>

1. Section hero + CTA (“Find Your Pathway”)
2. Intro + quick links sidebar
3. Section nav value cards (jump links)
4. “Where are you now?” audience fork
5. “Choose a pathway” stage cards
6. “Why cardiology?” compressed value + story teaser
7. “A day in the life” profile cards
8. Sticky section nav

---

## Zone 1: Hero

<span style="color:red">**H1**</span>  
Cardiology as a Career Path

<span style="color:red">**CTA title**</span>  
Find Your Pathway

<span style="color:red">**CTA description**</span>  
Heart disease is the world’s leading killer — and cardiology needs you. Start with the pathway that matches where you are today.

<span style="color:red">**CTA button**</span>  
How to Get Started → `{ Concept-Career-Path-Start.html }`

<span style="color:red">**Breadcrumb**</span>  
Tools & Practice Support → `{ parent: https://www.acc.org/Tools-and-Practice-Support }`

---

## Zone 4: Audience fork

<span style="color:red">**H2**</span>  
Where Are You Now?

| Card | Descriptor | Link |
|------|------------|------|
| Exploring as a student | High school or college — learn what cardiology is | `#Explore` + Young Scholars on Start page |
| In training | Medical student, resident, or fellow | `Concept-Career-Path-Physician.html` |
| CV Team professional | Nurse, NP, PA, pharmacist, technologist, or allied role | `Concept-Career-Path-CVTeam.html` |
| Growing your career | Leadership, teaching, or new role — professional development | Hub `#Level-Up` → [PDP on ACC.org](https://www.acc.org/Education-and-Meetings/Professional-Development-Programs) |

---

## Zone 5: Pathway stage cards

| Card | Body | Primary CTA |
|------|------|-------------|
| Physician Pathway | Many subspecialties; training from medical school through advanced fellowship | Explore Physician Path |
| CV Team Pathway | Nurses, NPs, PAs, pharmacists, and technologists who deliver care alongside physicians | Explore CV Team Roles |
| Clinical Research Pathway | Trial coordinators, investigators, and principal investigators | Explore Clinical Research |

---

# Level Up — Crossroads CTA (integrated)

<span style="color:red">**Do not duplicate**</span> the program catalog from [Professional Development Programs](https://www.acc.org/Education-and-Meetings/Professional-Development-Programs) on career-path pages.

<span style="color:red">**Strategy**</span>  
Teaser + crossroads framing on hub and pathway pages; single primary CTA to ACC PDP hub. Partial: `Career-Path/level-up-cta.html` (`default` on hub, `compact` on Physician / CV Team / Clinical Research).

<span style="color:red">**Placements**</span>

| Page | Variant | Role |
|------|---------|------|
| Hub | `default` (`#Level-Up`) | Full crossroads section + audience fit sidebar |
| Physician pathway | `compact` | Post-training career transition |
| CV Team pathway | `compact` | Leadership + certificates secondary link |
| Clinical research | `compact` | Investigator leadership transition |
| Start (resident/fellow step 3) | inline link | Direct to ACC PDP |
| Leadership bridge page | `default` | Optional bookmark URL; same CTA only |

---

# Start Here Page — Guided Audience Fork

<span style="color:red">**Page purpose**</span>  
Conversion routing — user arrives with intent to act, not to browse. They self-identify in one click and receive **three concrete next steps** scoped to their persona. This page deliberately does **not** repeat hub pathway cards or generic ACC value props.

<span style="color:red">**Strategy**</span>  
Audience fork (first screen) + guided process (numbered steps per segment) + progressive disclosure (detail lives on child pages).

<span style="color:red">**Audiences (6 personas)**</span>

| Persona | What they need | Primary deep link |
|---------|----------------|-------------------|
| High school | Exposure before committing to long training | Inspiration + Young Scholars |
| College / pre-med | Confirm fit + structured early programs | Young Scholars + Physician overview |
| Medical student | Peer community + specialty exploration | Free membership + med student resources |
| Resident / fellow | Stage-specific match/application tools | Physician training stages |
| CV Team | Role discovery + credentialing | CV Team role guide + certificates |
| Research / career change | Trials path + alternative careers | Clinical research + alt careers |

<span style="color:red">**Escape hatch**</span>  
"Still not sure?" — `Career-Path/follow-up-cta-pagedivider.html` (Arches Page Divider Follow-Up CTA recipe).

<span style="color:red">**Partial**</span>  
`Career-Path/start-guided.html`

---

# Child page content notes

Detailed copy for child pages lives in prototype HTML partials. SMEs should validate:

- <span style="background-color:#ffc0cb">Young Scholars Program URL and eligibility</span>
- <span style="background-color:#ffc0cb">Medical student / resident membership join URLs</span>
- <span style="background-color:#ffc0cb">Hero image set for Career Path microsite</span>
- <span style="background-color:#ffc0cb">Contact form integration on Contact page</span>

---

## Readability & validation targets

- Hub skim path: headings + cards only — grasp page in &lt;10 seconds
- CV Team reference: category browse first; role detail on demand
- Return visitors: jump nav + pathway switcher on child pages
- Target readability score 29+ on skim zones ([readability skill](../.cursor/skills/readability/SKILL.md))

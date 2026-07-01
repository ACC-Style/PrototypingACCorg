# Clinician Well-Being — Wireframe v1

**Status:** Prototype · Refactor step 5–6  
**Collection:** `_collections/__clinical-wellbeing/` → `/clinical-wellbeing/:path/`  
**Start here:** [hub.html](hub.html) → `/clinical-wellbeing/hub/`  
**Site map (Whimsical):** [ACC Clinician Well-Being sitemap](https://whimsical.com/americancollegeofcardiologyfnd/acc-clinician-well-being-sitemap-MWQ7A9DBJ5BQ7V3EbYawgR)

---

## Refactor progress

```
Refactor progress:
- [x] 1. Audit — content, audiences, jobs-to-be-done
- [x] 2. Classify — primary strategy selected
- [x] 3. Chunk — zones defined below
- [x] 4. Pattern — Arches patterns mapped
- [x] 5. Wire — this document + HTML wireframe
- [ ] 6. Readability pass
- [ ] 7. Validate — skim test, mobile, return-visitor path
```

---

## Audit summary

| Block (legacy) | Audience | Intent | Depth | Action |
|----------------|----------|--------|-------|--------|
| Hero image (text in image) | All clinicians | Orient | Skim | Replace with Section Hero + HTML headline |
| Cardio Renew promo | Mid-career members | Decide / act | Overview | Featured initiative card → product page |
| Hot Topics link list | Mixed | Browse | Skim | Split into Featured + Latest collections |
| Three image tiles (Resources, DocMatter, D&I) | Mixed | Route | Skim | Need-based topic hub tiles |
| Education & Resources page | Mixed | Browse / learn | Reference | Spoke page with grouped collections |
| COVID-era pages (5) | — | — | — | Retire or refresh into Burnout spoke |
| Cardio Renew product page | Eligible members | Enroll | Deep | Keep; refactor as Product Hero page |
| CardioSafe (planned) | CV clinicians | Learn / act | Mixed | Major spoke; build placeholder now |

**Primary user need:** “I am under pressure in clinical work. I want to know ACC understands it and has resources that can help — without stigma or digging through links.”

**Primary strategy:** **Hub & spoke** — organize by clinician need, not business line. Combine with **return-visitor skip** (jump nav) and **progressive disclosure** (overview on hub, depth on spokes).

**Layouts:** Hub → `acc/fullscreen` (Career Path pattern) · Spokes → `arches-clinical-solutions` (Clinical Solutions spoke pattern)
**Includes:** `_includes/Clinician-Wellbeing/` · **Partials:** `partials/` (mirrors `_clinical_solutions/partials/`)

**Proposed IA:** Tools → Practice Support → Support Resources → Clinician Well-Being (redirect from `/Features/2019/07/clinican-well-being-portal/`)

---

## Page suite — wireframe scope

| Page | v1 wireframe | Notes |
|------|--------------|-------|
| **Landing hub** | Yes | Main deliverable |
| Burnout & Resilience | Outline only | Spoke; refresh retired COVID content |
| Cardio Renew | Reference existing | Product page refactor (separate pass) |
| CardioSafe / Mistreatment | Placeholder card | Late 2026; structure now |
| Education & Resources | Merged into hub + spoke | Retire standalone link-list page |
| Advocacy & system support | Hub tile + section teaser | May grow to spoke later |
| Webinars & articles | Hub collection zone | Scalable list pattern |

---

## Landing hub — content zones

### Zone map (desktop)

```
┌─────────────────────────────────────────────────────────────┐
│  ZONE 1 · Section Hero                                      │
│  [breadcrumb]  Tools › Practice Support › …                 │
│  [photo bg]  H1: Clinician Well-Being                       │
│  [CTA panel] You are not alone. + 1-line sub + Explore CTA  │
└─────────────────────────────────────────────────────────────┘
┌──────────────────────────────┬──────────────────────────────┐
│  ZONE 2 · Story intro        │  ZONE 2b · Quick paths       │
│  Why this matters (2 ¶ max)  │  Sticky sidebar:             │
│  + 3 icon facts              │  • I need help now           │
│                              │  • Explore programs          │
│                              │  • Browse education          │
└──────────────────────────────┴──────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│  ZONE 3 · Find support by need (topic hub tiles)            │
│  [tile] Burnout    [tile] Mistreatment  [tile] Culture       │
│  [tile] Career     [tile] Admin burden  [tile] Education    │
│  [tile] Advocacy   [tile] Connect peers                     │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│  ZONE 4 · Featured initiatives (2–3 segmented cards)        │
│  Cardio Renew | CardioSafe (coming) | Mental Health course  │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│  ZONE 5 · Latest from ACC (webinars + articles)             │
│  Grouped list w/ title + 1-line “what you’ll learn” + link  │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│  ZONE 6 · ACC’s commitment (mission + work group)           │
│  Short prose + optional member quote + link to About/metrics  │
└─────────────────────────────────────────────────────────────┘
│  ZONE 7 · Sticky jump nav (scroll-spy) — return visitors    │
└─────────────────────────────────────────────────────────────┘
```

### Zone detail

#### Zone 1 — Section Hero

| Element | Working copy | Pattern |
|---------|--------------|---------|
| Breadcrumb parent | Practice Support (or Tools) | `hero-image-cta` |
| H1 | Clinician Well-Being | HTML on photo — no text in image |
| CTA title | You are not alone. | `cta-overlay` panel |
| CTA body | ACC is committed to helping cardiovascular clinicians address burnout, reduce system pressures, and sustain meaningful careers in patient care. | 1–2 sentences |
| Primary CTA | Find support | Anchor to Zone 3 |
| Imagery | People-focused clinicians | [imagery.md](../../.cursor/skills/acc-ux-designer/imagery.md) |

#### Zone 2 — Story intro + quick paths

| Element | Working copy | Pattern |
|---------|--------------|---------|
| H2 | Why clinician well-being matters | `font_display` |
| Body | Burnout is widespread in cardiology. It is not an individual failure — pressures come from patients, colleagues, workload, data burden, and systems of care. Healthier clinicians deliver better cardiovascular care. | Max 2 short paragraphs |
| Icon facts (3) | Embedded in ACC strategic plan · Workforce sustainability · Evidence-based interventions | Icon decorated list |
| Quick paths sidebar | I need help now → Burnout tile · Explore programs → Zone 4 · Browse education → Zone 5 | Sticky `cta-overlay` (Journal pattern) |

#### Zone 3 — Find support by need

**Pattern:** Topic hub tiles (`Course-Compact.html`)

| Tile | Routes to | Descriptor |
|------|-----------|------------|
| Burnout & resilience | Burnout spoke | Recognize, cope, recover |
| Patient mistreatment | CardioSafe spoke | Respond & report |
| Workplace culture | Resources / policy statements | Respect & inclusion |
| Career flexibility | Policy + webinars | Sustain your career |
| Administrative burden | NCDR / QI links (TBD) | Reduce friction |
| Education & webinars | Education spoke | Courses & learning |
| Advocacy & systems | Advocacy teaser / external | Root causes |
| Connect with peers | DocMatter community | Discuss with colleagues |

#### Zone 4 — Featured initiatives

**Pattern:** Segmented cards (`card-segmented.html`) or photo + text lockup

| Card | Status | CTA |
|------|--------|-----|
| Cardio Renew | Live program | Learn more → product page |
| CardioSafe | Coming late 2026 | Preview resources |
| NCD Academy — Mental Health | Live | Start course |

#### Zone 5 — Latest webinars & articles

**Pattern:** Grouped collection — not raw links. Optional DateList sort for webinars.

- Group by topic (Burnout · Leadership · Career · Policy)
- Each item: title + 1-line value prop + type badge (Webinar / Article)

#### Zone 6 — ACC’s commitment

- Why ACC invests (from SME notes — strategic plan, metrics)
- Clinician Well-Being work group attribution
- Optional: single member quote (humanize)

#### Zone 7 — Jump nav

**Pattern:** `jump-nav/jump-nav.html` — sections: Why · Find support · Programs · Latest · Our commitment

---

## Spoke outlines (v2)

### Burnout & Resilience

- Section Hero echo (micro)
- Intro: recognize burnout, causes, you are not alone
- Resource cards: toolkit, infographic, refreshed COVID-era guides
- Webinar/article collection filtered to topic
- External: NAM Collaborative link

### CardioSafe (placeholder)

- Section Hero echo
- Problem statement: patient-initiated mistreatment
- Module grid (4 × 15 min) — placeholder cards
- Institution vs individual paths
- Reporting best practices

---

## Whimsical build checklist

Use the existing [sitemap board](https://whimsical.com/americancollegeofcardiologyfnd/acc-clinician-well-being-sitemap-MWQ7A9DBJ5BQ7V3EbYawgR) and add a **Landing hub wireframe** frame with:

1. One full-width mobile frame (320px)
2. One desktop frame (1200px)
3. Gray boxes for hero image / cards — label zones 1–7
4. Annotations for open questions (pink): Cardio Renew cadence, CardioSafe timing, workforce spoke ownership
5. Link arrows from hub tiles to spoke page frames

---

## Open questions (block content, not structure)

- Final elevator pitch sign-off (Stephanie / Aly)
- Cardio Renew: annual vs recurring program?
- CardioSafe module list and grant deliverables
- Which COVID-era pages to refresh vs retire
- Workforce / career flexibility — separate spoke or cross-link only?
- Final nav label under Practice Support

---

## Next steps

1. Review wireframe with Jackie / Stephanie
2. Readability pass on working copy
3. High-fi polish on hub + spoke pages in this collection
4. Spoke wireframes (Burnout, CardioSafe)
5. Content collection document (JOURNALS `content-collection.md` format)

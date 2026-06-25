---
published: false
---

# Clinical Solutions for Everyday Practice — Content Collection & Refactor Plan

## Legend

- <span style="color:red">Red text — metadata, layout notes, UI slots, developer instructions.</span>
- <span style="color:red">{ } — inline production notes (URLs, component behavior).</span>
- <mark>Yellow — UX open items.</mark>
- <span style="background-color:#ffc0cb">Pink — SME content gaps.</span>

---

## Refactor Summary

<span style="color:red">**Source section**</span>  
https://www.acc.org/Tools-and-Practice-Support/Features/Clinical-Solutions and child pages (one level deep, audited June 2025).

<span style="color:red">**Primary strategy**</span>  
**Hub & spoke** (clinical topic branches) combined with an **intent fork** (what kind of resource you need) and **progressive disclosure** on spoke pages. Replace Bootstrap accordion walls with visible resource-type zones, native `<details>` only for long reference lists, and return-visitor jump navigation.

<span style="color:red">**Content separation principle**</span>  
Clinical Solutions and [Clinical Topics](https://www.acc.org/Clinical-Topics) serve different jobs — **do not merge or duplicate**:

| Property | Clinical Solutions | Clinical Topics |
|----------|-------------------|-----------------|
| **Job** | Curated **implementation** sets for prioritized care gaps | **Dynamic topic hubs** aggregating ACC content by clinical tag |
| **Content** | Hand-picked ECDPs, tools, roundtables, CardioSmart links | Coveo-fed Latest, Guidelines, JACC, Education, Meetings, Images, Resources |
| **Maintenance** | Editorial curation per solution set | Auto-updates as tagged content publishes |
| **User moment** | “I need the pathway/tool for this problem” | “What’s new and authoritative on this topic?” |

**Bolster Clinical Solutions** with **related-content callouts** — CTA links to matching Clinical Topics pages where they exist, so users can move from **actionable implementation** to **broader topic context** without leaving the ACC ecosystem.

<span style="color:red">**Lessons carried from Career Path prototype**</span>

| Career Path pattern | Clinical Solutions application |
|---------------------|--------------------------------|
| Hub audience fork before prose | Intent fork on hub: guidance vs tools vs patient materials vs implementation |
| Image-only pathway banners → text cards | Topic grid with title, one-line descriptor, and format badges — not banner images alone |
| CV Team accordion wall → category browse + disclosure | Spoke pages: resource-type sections visible first; collapse only dense lists |
| Return-visitor jump nav + pathway switcher | Sticky resource-type nav on every spoke; hub topic filter for repeat visits |
| Teaser + destination (PDP crossroads) | Link out to JACC guidance overview, Guidelines hub, and **Clinical Topics** — do not duplicate feeds |
| Consistent spoke template | One repeatable topic page pattern across all 12 active topics |

<span style="color:red">**Business goals**</span>

1. Position ACC Clinical Solutions as the **practical implementation layer** on top of guidelines — where clinicians find ECDPs, tools, and patient resources for a given care problem.
2. Increase use of high-value outputs (ECDPs, AUC, CardioSmart tools, mobile apps) by making them findable in under 10 seconds.
3. Support ACC strategic priorities by surfacing prioritized topics with clear goals and measurable care-gap framing.
4. Route patient-facing needs to CardioSmart without mixing clinician and patient journeys on the same skim path.
5. **Cross-link to Clinical Topics** where a supportive match exists — deepen the experience with dynamically updated guidelines, education, and news without hosting that content on Clinical Solutions pages.

<span style="color:red">**Assumed primary audience**</span>  
**Practicing cardiovascular clinicians and care-team members** who already know the clinical topic and arrive to **act** — download a pathway, open a calculator, print a patient handout, or cite an ECDP. Secondary audience: **clinic and program leaders** implementing systems-of-care models.

| Audience | Job to be done | Typical entry |
|----------|----------------|---------------|
| Attending / fellow | Apply latest ECDP or CCG at point of care | Topic spoke → Clinical Guidance |
| APP / pharmacist / RN | Find team-based tools and patient education | Topic spoke → Clinician or Patient Resources |
| Clinic director / quality lead | Implement pathways across a service line | Systems of Care spoke; roundtable PDFs |
| Return visitor | Jump directly to a known resource type or document | Spoke jump nav or hub topic picker |
| <mark>Patient / caregiver</mark> | <mark>Not primary for this hub — route to CardioSmart</mark> | <mark>Escape hatch CTA, not hub hero</mark> |

<span style="color:red">**Legacy problems addressed**</span>

- **Hub** mixes mission copy (4 paragraphs) with a **vertical stack of image-only banners** — fails skim test, poor accessibility, no format or freshness signals.
- **Spoke pages** share the same shape (intro + goals + accordion wall) but **hide all resources behind collapsed panels** — repeat users must click through 5–7 sections to scan what exists.
- **Inconsistent resource taxonomy** — panel labels vary by topic (e.g., Immunization adds CDC SAIP and Educational Initiatives; Systems of Care adds Expert Consensus Systems of Care Documents).
- **Scale imbalance** — Primary Prevention (~44 links, 7 panels) vs Chronic Coronary Disease (~5 links, 3 panels) get the same UX weight.
- **Additional Topics** is a catch-all bucket mixing unrelated ECDPs/AUCs — functions as an archive, not a clinical topic.
- **Orphan / hidden topics** — Lipids and Diabetes banners are commented out on the hub; Lipids URL 404s; diabetes content partially lives under Primary Prevention tools.
- **Deep links** — many resources point to JACC DOIs, PDFs, and mobile apps with no on-page indication of format until expand.

---

## Content audit (source, one level deep)

### Hub

| Element | Current state |
|---------|---------------|
| H1 | Clinical Solutions for Everyday Practice (header image alt text) |
| Intro | 4 paragraphs on ACC mission, solution-set activities, JACC editorial link, topic list preamble |
| Navigation | 12 linked topic banners (2 commented out: Lipids, Diabetes) |
| CTA | None — user must scroll image stack |

### Active topic spokes (12)

| Topic | Panels | ~Links | Notes |
|-------|--------|--------|-------|
| Primary Prevention of CV Disease | 7 | 44 | Richest set; ECDP, CCG, tools, CardioSmart, roundtables, forums |
| Procedural Intervention in Valve Disease | 7 | 42 | Includes AUC |
| Medication Management in HF | 6 | 23 | |
| Optimization of Hospitalization for Heart Failure | 7 | 17 | Policy statements |
| Management of Anticoagulation/Antithrombotic Therapy | 7 | 41 | |
| Chronic Coronary Disease | 3 | 5 | Thin — AUC + CardioSmart + other |
| Management of Patients With Cardiac Amyloidosis | 5 | 8 | CCG + ECDP |
| HCM | 5 | 28 | |
| Management of COVID-19 in Patients with CVD | 7 | 26 | |
| Advancing Adult Immunization | 7 | 86 | Unique sections (CDC SAIP, educational initiatives) |
| Systems of Care | 7 | 21 | Systems-of-care documents panel |
| Additional Topics | 6 | 25 | Multi-topic archive |

### Inactive / broken (not on hub)

| Topic | Status |
|-------|--------|
| Medication Management of Lipids | Hub link commented out; URL 404 |
| Management of CVD Risk in Patients With Diabetes | Hub link commented out; <span style="background-color:#ffc0cb">confirm redirect or restore</span> |

### Recurring resource types (normalize in refactor)

| Legacy panel label | Refactor zone | Primary user |
|--------------------|---------------|--------------|
| Expert Consensus Decision Pathways | Clinical Guidance | Clinician |
| Concise Clinical Guidance | Clinical Guidance | Clinician |
| Appropriate Use Criteria | Clinical Guidance | Clinician |
| Health Policy Statements | Clinical Guidance | Leader / clinician |
| Clinical Guidance / CDC SAIP | Clinical Guidance | Clinician |
| Clinician Tools | Point-of-Care Tools | Clinician / care team |
| CardioSmart Patient Tools | Patient Resources | Care team → patient |
| Heart House Roundtables | Implementation & Policy | Leader / clinician |
| Heart House Patient Forums | Implementation & Policy | Leader / clinician |
| Educational Initiatives | Implementation & Policy | Clinician |
| Expert Consensus Systems of Care Documents | Implementation & Policy | Leader |
| Other Resources | Other Resources | Mixed |

---

## Information Architecture (refactored)

| Page | File (proposed) | Strategy |
|------|-----------------|----------|
| **Hub** | `Concept-Clinical-Solutions.html` | Hub & spoke — intent fork + topic grid grouped by clinical domain |
| **Topic spokes (×12)** | `Concept-Clinical-Solutions-{Topic}.html` | Teaser + destination — unified template, topic-specific data |
| **Find a Resource** (optional) | `Concept-Clinical-Solutions-Find.html` | Guided intent fork — “I need…” → topic + resource type <mark>evaluate after hub usability test</mark> |
| **About Clinical Solutions** | Fold into hub zone or short aside | Progressive disclosure — mission copy demoted below topic grid |

<span style="color:red">**Do not build**</span> separate pages for individual ECDPs or PDFs — those remain external destinations (JACC, PDF, CardioSmart, mobile apps).

<span style="color:red">**Prototype partials**</span> — `_collections/_clinical_solutions/partials/*.html` (use `{% include_relative %}` from collection pages)  
<span style="color:red">**Data (future)**</span> — `_data/ClinicalSolutions/topics.yml`, `resources.yml`

---

# Clinical Topics integration — mapping & callouts

<span style="color:red">**Pattern**</span>  
Teaser + destination (same as Career Path PDP crossroads). Clinical Solutions pages **never embed** Coveo topic feeds — they **call out** to the live Clinical Topics hub with a short value line and primary CTA.

<span style="color:red">**Component**</span> — `partials/clinical-topics-callout.html`  
Follow-up CTA / segmented-card aside pattern. Variants: `default` (spoke sidebar or post-intro), `compact` (hub topic card footer link).

**Callout anatomy**

| Element | Spec |
|---------|------|
| Eyebrow | `Explore the broader topic` |
| Title | Clinical Topics page name (e.g., *Prevention*) |
| Body | 1 sentence — what the user gets dynamically (guidelines, JACC, education, latest news) |
| CTA | `View Prevention Clinical Topic →` `{ Clinical Topics URL }` |
| Optional secondary | Deep link to a Clinical Topics sub-page when tighter fit |

**Example copy (Primary Prevention spoke)**  
*Stay current on prevention — guidelines, JACC articles, education, and the latest news, updated as ACC publishes.*

---

## Solution set → Clinical Topics mapping

Primary match = main callout CTA. Secondary = optional compact link in related-content row or Additional Topics tag routing.

| Clinical Solutions spoke | Primary Clinical Topics match | URL | Secondary matches |
|--------------------------|------------------------------|-----|-------------------|
| Primary Prevention of CV Disease | Prevention | [/Clinical-Topics/Prevention](https://www.acc.org/Clinical-Topics/Prevention) | [Dyslipidemia](https://www.acc.org/Clinical-Topics/Dyslipidemia), [Diabetes and Cardiometabolic Disease](https://www.acc.org/Clinical-Topics/Diabetes-and-Cardiometabolic-Disease), [Prevention/Hypertension](https://www.acc.org/Clinical-Topics/Prevention/Hypertension) |
| Advancing Adult Immunization | Geriatric Cardiology | [/Clinical-Topics/Geriatric-Cardiology](https://www.acc.org/Clinical-Topics/Geriatric-Cardiology) | [Prevention](https://www.acc.org/Clinical-Topics/Prevention), [Cardiovascular Care Team](https://www.acc.org/Clinical-Topics/Cardiovascular-Care-Team) — <span style="background-color:#ffc0cb">no dedicated immunization topic; confirm SME preferred primary</span> |
| Medication Management in HF | Heart Failure and Cardiomyopathies | [/Clinical-Topics/Heart-Failure-and-Cardiomyopathies](https://www.acc.org/Clinical-Topics/Heart-Failure-and-Cardiomyopathies) | [Chronic Heart Failure](https://www.acc.org/Clinical-Topics/Heart-Failure-and-Cardiomyopathies/Chronic-Heart-Failure) |
| Optimization of Hospitalization for HF | Heart Failure and Cardiomyopathies | [/Clinical-Topics/Heart-Failure-and-Cardiomyopathies](https://www.acc.org/Clinical-Topics/Heart-Failure-and-Cardiomyopathies) | [Acute Heart Failure](https://www.acc.org/Clinical-Topics/Heart-Failure-and-Cardiomyopathies/Acute-Heart-Failure) |
| Procedural Intervention in Valve Disease | Valvular Heart Disease | [/Clinical-Topics/Valvular-Heart-Disease](https://www.acc.org/Clinical-Topics/Valvular-Heart-Disease) | [Interventions and Structural Heart Disease](https://www.acc.org/Clinical-Topics/Invasive-Cardiovascular-Angiography-and-Intervention/Interventions-and-Structural-Heart-Disease), [Cardiac Surgery and VHD](https://www.acc.org/Clinical-Topics/Cardiac-Surgery/Cardiac-Surgery-and-VHD) |
| HCM | Heart Failure and Cardiomyopathies | [/Clinical-Topics/Heart-Failure-and-Cardiomyopathies](https://www.acc.org/Clinical-Topics/Heart-Failure-and-Cardiomyopathies) | [Sports and Exercise Cardiology](https://www.acc.org/Clinical-Topics/Sports-and-Exercise-Cardiology) |
| Cardiac Amyloidosis | Heart Failure and Cardiomyopathies | [/Clinical-Topics/Heart-Failure-and-Cardiomyopathies](https://www.acc.org/Clinical-Topics/Heart-Failure-and-Cardiomyopathies) | — |
| Chronic Coronary Disease | Stable Ischemic Heart Disease | [/Clinical-Topics/Stable-Ischemic-Heart-Disease](https://www.acc.org/Clinical-Topics/Stable-Ischemic-Heart-Disease) | [Chronic Angina](https://www.acc.org/Clinical-Topics/Stable-Ischemic-Heart-Disease/Chronic-Angina), [Interventions and Coronary Artery Disease](https://www.acc.org/Clinical-Topics/Invasive-Cardiovascular-Angiography-and-Intervention/Interventions-and-Coronary-Artery-Disease) |
| Anticoagulation / Antithrombotic Therapy | Anticoagulation Management | [/Clinical-Topics/Anticoagulation-Management](https://www.acc.org/Clinical-Topics/Anticoagulation-Management) | [Anticoagulation and Atrial Fibrillation](https://www.acc.org/Clinical-Topics/Anticoagulation-Management/Anticoagulation-Management-and-Atrial-Fibrillation), [Pulmonary Hypertension and VTE](https://www.acc.org/Clinical-Topics/Pulmonary-Hypertension-and-Venous-Thromboembolism) — note existing [Anticoagulation Solution Set](https://www.acc.org/Clinical-Topics/Anticoagulation-Management/Anticoagulation-Solution-Set) child page |
| Systems of Care | Cardiovascular Care Team | [/Clinical-Topics/Cardiovascular-Care-Team](https://www.acc.org/Clinical-Topics/Cardiovascular-Care-Team) | <span style="background-color:#ffc0cb">cvquality.acc.org / NCDR for registry & QI — external, not Clinical Topics</span> |
| COVID-19 in Patients with CVD | COVID-19 Hub | [/Clinical-Topics/COVID-19-Hub](https://www.acc.org/Clinical-Topics/COVID-19-Hub) | — |
| Additional Topics | *Tag-driven — no single hub* | [/Clinical-Topics](https://www.acc.org/Clinical-Topics) index as fallback | Per-item routing below |

### Additional Topics — per-item Clinical Topics routing

Use tag chips on the Additional Topics spoke; each chip links to the best Clinical Topics match:

| Archive item theme | Clinical Topics destination |
|--------------------|----------------------------|
| Maternal / postpartum CV care | <span style="background-color:#ffc0cb">No dedicated women's CV topic — link [Prevention](https://www.acc.org/Clinical-Topics/Prevention) or SME to nominate hub</span> |
| Myocarditis | [Heart Failure and Cardiomyopathies](https://www.acc.org/Clinical-Topics/Heart-Failure-and-Cardiomyopathies) |
| Acute chest pain / ED pathway | [Acute Coronary Syndromes](https://www.acc.org/Clinical-Topics/Acute-Coronary-Syndromes) |
| Multimodality imaging AUC | [Noninvasive Imaging](https://www.acc.org/Clinical-Topics/Noninvasive-Imaging) |
| ICD / CRT / pacing AUC | [Arrhythmias and Clinical EP / Implantable Devices](https://www.acc.org/Clinical-Topics/Arrhythmias-and-Clinical-EP/Implantable-Devices) |
| Peripheral artery intervention | [Vascular Medicine](https://www.acc.org/Clinical-Topics/Vascular-Medicine) |
| Tobacco cessation (duplicate ECDP) | [Prevention / Smoking](https://www.acc.org/Clinical-Topics/Prevention/Smoking) |

### Retired / hidden solution sets

| Clinical Solutions (inactive) | Clinical Topics match |
|-------------------------------|----------------------|
| Medication Management of Lipids | [Dyslipidemia](https://www.acc.org/Clinical-Topics/Dyslipidemia) |
| Management of CVD Risk in Patients With Diabetes | [Diabetes and Cardiometabolic Disease](https://www.acc.org/Clinical-Topics/Diabetes-and-Cardiometabolic-Disease) |

<span style="color:red">**Bidirectional linking**</span>  
Clinical Topics nav already links to the [Clinical Solutions hub](https://www.acc.org/Tools-and-Practice-Support/Features/Clinical-Solutions). Refactor should **strengthen the return path** — each spoke callout makes the relationship explicit. Where Clinical Topics has a solution-set child page (e.g., Anticoagulation), both URLs should cross-reference.

---

# Hub Page — Clinical Solutions for Everyday Practice

<span style="color:red">**Meta title**</span>  
Clinical Solutions for Everyday Practice | American College of Cardiology

<span style="color:red">**Meta description**</span>  
Evidence-based clinical solution sets for high-value cardiovascular topics — ECDPs, tools, patient resources, and implementation guides for everyday practice.

<span style="color:red">**Layout zones**</span>

1. Section hero + primary CTA (“Browse by Topic”)
2. Intent fork — what do you need?
3. Topic grid — grouped clinical domains (text cards, not image-only)
4. About this program — compressed mission (2 sentences) + link to JACC editorial
5. Return-visitor quick links — popular tools + Guidelines hub + **Clinical Topics index**
6. Sticky section nav (topics + intent)

---

## Zone 1: Hero

<span style="color:red">**H1**</span>  
Clinical Solutions for Everyday Practice

<span style="color:red">**Supporting line**</span>  
Practical, evidence-based resources ACC prioritizes to close care gaps — organized by clinical topic and resource type.

<span style="color:red">**CTA button**</span>  
Browse Topics → `{ #Topics }`

<span style="color:red">**Breadcrumb**</span>  
Tools & Practice Support → `{ parent: https://www.acc.org/Tools-and-Practice-Support }`

---

## Zone 2: Intent fork

<span style="color:red">**H2**</span>  
What Do You Need?

| Card | Descriptor | Behavior |
|------|------------|----------|
| Clinical guidance | ECDPs, concise guidance, AUC, policy statements | Hub filter or scroll to topics; spoke default section `#guidance` |
| Point-of-care tools | Apps, calculators, pocket guides, order sets | Hub filter; spoke section `#tools` |
| Patient resources | CardioSmart handouts, action plans, infographics | Hub filter; spoke section `#patient` + CardioSmart escape hatch |
| Implementation support | Roundtables, patient forums, systems-of-care documents | Hub filter; spoke section `#implementation` |

<span style="color:red">**Note**</span>  
This is an **intent** fork, not a role fork — same clinician may need multiple cards. Cards set **scroll/filter state** on the topic grid rather than routing to a separate silo.

---

## Zone 3: Topic grid

<span style="color:red">**H2**</span>  
Clinical Topics

Group cards for scanability (collapsible group headers on mobile):

### Prevention & risk

| Card | One-line descriptor | Spoke |
|------|---------------------|-------|
| Primary Prevention of CV Disease | Lifetime risk assessment, lipids, diabetes risk, lifestyle | `Primary-Prevention` |
| Advancing Adult Immunization | Immunization standards and CV patient vaccination | `Immunization` |

### Heart failure

| Card | One-line descriptor | Spoke |
|------|---------------------|-------|
| Medication Management in HF | GDMT optimization and prescribing gaps | `HF-Medications` |
| Optimization of Hospitalization for HF | Inpatient and transition-of-care pathways | `HF-Hospitalization` |

### Structural heart & cardiomyopathy

| Card | One-line descriptor | Spoke |
|------|---------------------|-------|
| Procedural Intervention in Valve Disease | TAVR, TMVR, and valve intervention decisions | `Valve-Disease` |
| HCM | Diagnosis and management of hypertrophic cardiomyopathy | `HCM` |
| Cardiac Amyloidosis | Detection, typing, and treatment pathways | `Amyloidosis` |

### Coronary & antithrombotic care

| Card | One-line descriptor | Spoke |
|------|---------------------|-------|
| Chronic Coronary Disease | Diagnosis and initial treatment of chronic CAD | `Chronic-Coronary` |
| Anticoagulation / Antithrombotic Therapy | Peri-procedural and long-term antithrombotic management | `Anticoagulation` |

### Systems & emerging areas

| Card | One-line descriptor | Spoke |
|------|---------------------|-------|
| Systems of Care | Team-based CV intervention models | `Systems-of-Care` |
| COVID-19 in Patients with CVD | CV considerations in COVID-19 management | `COVID-CVD` |
| Additional Topics | Maternal CV care, myocarditis, imaging AUC, and more | `Additional-Topics` |

<span style="color:red">**Card anatomy**</span>  
Title · 1-line descriptor · badge row (`ECDP`, `Tools`, `CardioSmart`, `PDF`) · link to spoke · **optional footer link** to matched Clinical Topics page (`Explore topic →`)

<span style="color:red">**Hub escape hatch**</span>  
Secondary CTA row below topic grid: *Looking for guidelines, education, and news on a clinical topic?* → [Browse Clinical Topics](https://www.acc.org/Clinical-Topics)

<span style="color:red">**Retired topics**</span>  
<span style="background-color:#ffc0cb">Lipids and Diabetes — SME decision: restore as spokes, merge into Primary Prevention, or redirect.</span>

---

## Zone 4: About (demoted)

<span style="color:red">**H2**</span>  
How ACC Builds Clinical Solutions

**Copy (target ≤2 sentences)**  
ACC selects high-value topics and develops coordinated outputs — including Heart House roundtables, ECDPs, AUC, decision support, and clinician and patient tools — to transform cardiovascular care.

**Link**  
Read *Empowering the Profession: The ACC's Commitment to Cutting-Edge Clinical Guidance* → `{ JACC editorial DOI }`

---

# Spoke Page — Unified Topic Template

<span style="color:red">**Strategy**</span>  
Progressive disclosure + return-visitor skip. **First screen** shows topic purpose and **visible resource-type summary cards** with counts. **Below the fold**, each resource type expands into a scannable list — not a collapsed accordion wall.

<span style="color:red">**Layout zones**</span>

1. Hero (topic title — text over image, not image-as-title)
2. Topic snapshot — 2-sentence intro + up to 3 goal bullets
3. **Clinical Topics callout** — primary related topic CTA (sidebar on desktop, inline after snapshot on mobile)
4. Sticky jump nav — Guidance · Tools · Patient · Implementation · Other
5. Resource-type sections (visible headers, lists below)
6. Related Clinical Solutions topics (2–3 cards) + optional secondary Clinical Topics links
7. Hub back-link + Guidelines hub CTA

---

## Zone 2: Topic snapshot (example — Primary Prevention)

**Intro (rewrite for readability)**  
Cardiovascular prevention works best when risk is found early and managed over a lifetime. This solution set helps clinicians assess risk, start the right therapies, and coordinate team-based prevention.

**Goals (from source, tightened)**

- Guide early risk assessment and interventions with lifetime benefit in mind
- Support team-based prevention that lowers cumulative risk
- Promote equitable cardiovascular health across the lifespan

---

## Zone 3–4: Resource sections (pattern)

Replace legacy Bootstrap panels with **segmented sections**. Each section:

| Element | Spec |
|---------|------|
| H3 | Resource type name |
| Count | `(12 resources)` in `font-size_down` |
| List item | Title · year badge · format icon (Journal / PDF / App / External) |
| Optional | Key Takeaways PDF linked inline beside journal citation |
| Long lists (>8) | Native `<details>` per sub-year or sub-type — not whole-section collapse |

### Section order (default)

1. **Clinical Guidance** — ECDPs, CCG, AUC, policy statements
2. **Point-of-Care Tools** — ACC apps, pocket guides, estimators
3. **Patient Resources** — CardioSmart (opens external where appropriate)
4. **Implementation & Policy** — Roundtables, forums, educational initiatives
5. **Other Resources** — only if needed

<span style="color:red">**Immunization exception**</span>  
CDC SAIP maps to Clinical Guidance; Educational Initiatives maps to Implementation — same template, topic-specific YAML rows.

<span style="color:red">**Thin topics**</span>  
Chronic Coronary (~5 links): consider **compact spoke** layout — single column, no empty section headers, related topics emphasized.

---

## Zone 5: Related content

**Two related-content rows — keep separate:**

### A. Related Clinical Solutions (internal spokes)

| Primary topic | Suggested related spokes |
|---------------|--------------------------|
| Primary Prevention | Anticoagulation, HF Medications, Immunization |
| HF Medications | HF Hospitalization, Systems of Care |
| Valve Disease | HCM, Amyloidosis, Additional Topics (imaging AUC) |
| Additional Topics | Tag-filter UX; <mark>long-term: split items into proper spokes</mark> |

### B. Related Clinical Topics (external dynamic hubs)

Use `clinical-topics-callout.html` with mapping table above. Examples:

| Spoke | Callout title | CTA destination |
|-------|---------------|-----------------|
| Primary Prevention | Prevention Clinical Topic | `/Clinical-Topics/Prevention` |
| HF Medications | Heart Failure and Cardiomyopathies | `/Clinical-Topics/Heart-Failure-and-Cardiomyopathies` |
| Anticoagulation | Anticoagulation Management | `/Clinical-Topics/Anticoagulation-Management` |
| Immunization | Geriatric Cardiology | `/Clinical-Topics/Geriatric-Cardiology` <span style="background-color:#ffc0cb">pending SME</span> |

<span style="color:red">**Do not**</span> list individual guidelines or JACC articles on Clinical Solutions spokes — that is what Clinical Topics feeds deliver dynamically.

---

# Additional Topics — Special handling

<span style="color:red">**Problem**</span>  
Additional Topics is an **archive of disparate outputs** (maternal CV care, myocarditis, chest pain ED pathway, ICD/AUC, etc.) — not a clinical condition.

<span style="color:red">**Refactor approach**</span>

1. **Short term:** Keep as spoke but lead with **resource-type browse** and **tag chips** (Maternal, Imaging, Emergency, etc.) so users filter before reading.
2. **Long term:** <span style="background-color:#ffc0cb">SME content strategy — migrate items to condition-specific spokes or a Guidelines/ECDP finder.</span>

---

# Cross-links — do not duplicate

| Destination | Use on Clinical Solutions |
|-------------|---------------------------|
| [Clinical Topics hub](https://www.acc.org/Clinical-Topics) | Hub escape hatch; Additional Topics fallback; per-spoke callout CTAs |
| [Clinical Topics — matched topic](https://www.acc.org/Clinical-Topics/Prevention) | Spoke callout + optional hub card footer — see mapping table |
| [ACC Guidelines Hub](https://www.acc.org/Guidelines) | Hub quick link; spoke sidebar secondary |
| JACC editorial on clinical guidance | Hub “About” zone only |
| CardioSmart | Patient Resources section + labeled external CTA |
| Mobile Resources / individual apps | Linked from Tools sections only |
| Quality Programs / Heart House | Implementation section context line |
| cvquality.acc.org / NCDR | Systems of Care spoke only — external QI/registry |

---

# Proposed file map (collection `clinical_solutions`)

```
_collections/_clinical_solutions/
  Clinical-Solutions/
    content-collection.md          ← this plan
  partials/                        ← collection-local partials (include_relative)
  Concept-Clinical-Solutions.html
  Concept-Clinical-Solutions-*.html
_data/ClinicalSolutions/
  topics.yml
  resources.yml
```

<span style="color:red">**Permalink**</span>  
`/clinical-solutions/:path/` (see `_config.yml`)

---

# Readability & validation targets

- Hub skim path: intent cards + topic titles only — grasp page in **&lt;10 seconds**
- Spoke skim path: jump nav + section headers + resource counts — find right **resource type** without expanding accordions
- Return visitors: deep-linkable `#guidance`, `#tools`, `#patient`, `#implementation` on every spoke
- Intro zones: target readability score **29+** on skim copy ([readability skill](../../.cursor/skills/readability/SKILL.md))
- Mobile: topic grid stacks as single-column cards; jump nav becomes horizontal scroll chips
- Accessibility: no information conveyed by banner image alone — title and descriptor always in HTML text

---

# SME & UX open items

- <span style="background-color:#ffc0cb">Restore, redirect, or retire Lipids and Diabetes topic pages</span>
- <span style="background-color:#ffc0cb">Confirm whether COVID-19 topic remains actively maintained or should move to archive</span>
- <span style="background-color:#ffc0cb">Content strategy for Additional Topics — permanent archive vs split</span>
- <span style="background-color:#ffc0cb">Confirm primary Clinical Topics match for Immunization (Geriatric Cardiology vs Prevention)</span>
- <span style="background-color:#ffc0cb">Maternal/postpartum CV content in Additional Topics — nominate Clinical Topics destination</span>
- <mark>Validate intent fork vs topic-first navigation with 3–5 clinician interviews</mark>
- <mark>Hero imagery — reuse ACC Clinical Solutions art without text baked into images</mark>
- <mark>Decide if “Find a Resource” guided page is needed or if hub filters are sufficient</mark>

---

## Refactor progress

```
- [x] 1. Audit — inventory content, audiences, and jobs-to-be-done
- [x] 2. Classify — assign each block a refactor strategy
- [ ] 3. Chunk — one idea per card/section; cut or defer depth
- [ ] 4. Pattern — pick UI pattern per chunk
- [ ] 5. Wire — nav, anchors, skip paths, optional filters
- [ ] 6. Readability pass — score and rewrite copy
- [ ] 7. Validate — scan test, mobile chunk count, return-visitor path
```

---
published: false
title: Clinician Well-Being — Prototype TOC
---

# Clinician Well-Being — Prototype TOC

SME presentation map: **Page → Zone (`id`) → UI Item → Content Collection**

**Live prototype paths** (Jekyll): `/clinical-wellbeing/Concept-Clinician-Well-Being/` and child pages.

**Content source:** [content-collection.md](content-collection.md)

---

## Concept-Clinician-Well-Being.html

**Layout:** `Global/fullscreen` (concept root — no sidebar)  
**URL:** `/clinical-wellbeing/Concept-Clinician-Well-Being/`

### Zone: `hero` — Hero + Primary CTA

- **UI Item:** Hero Image with CTA (`MicroSite/heroimage.dynamic.html` + `_data/ClinicianWellBeing/hero.yml`)
  - **Copy:** `_data/ClinicianWellBeing/hub.yml`
  - **Content Collection:**
    - `data-item="page-title"` → **H1:** Clinician Well-Being
    - `data-item="cta-title"` → **H2:** Self Care is also part of the job
    - `data-item="cta-description"` → Practical resources can help you recover, recharge, and sustain your career…
    - `btn-primary` → **Button label:** Explore Resources
    - `href` → `/clinical-wellbeing/Concept-Clinician-Well-Being-Tools/`

### Zone: `intro` — Why ACC Cares for You

- **UI Item:** Two-column intro + Cardio Renew aside
  - **Content Collection:**
    - **H2:** Why ACC Cares for You
    - **Body:** Cardiovascular professionals carry high-stakes responsibility…
    - **Aside H3:** Cardio Renew
    - **Aside CTA:** Learn More → ACC Cardio Renew program page

### Zone: `why-wellbeing` — Evidence

- **UI Item:** Stat row (`Blocks/StatRow.html` — 3 stats across, teal number · divider · text)
  - **Content Collection:**
    - **H2:** Why Cardiologist Well-Being Needs Urgent Attention
    - **Stat 1:** 40%* — of cardiologists reported work-related burnout / (2018 Medscape data, ACC Toolkit)
    - **Stat 2:** 17% — would consider professional mental health support
    - **Stat 3:** 2× — greater suicide risk than the general public

### Zone: `hub-fork` — Two-Lane Entry

- **UI Item:** Fork cards with CTA buttons (`Blocks/HubForkCards.html`, 2 items — whole card links to spoke)
  - **Content Collection:**
    - **H2:** How The College is Supporting Clinician Well-Being
    - **Intro:** The ACC is committed to the problems of today and the solutions of tomorrow.
    - **Card 1:** Tools for Today → `/clinical-wellbeing/Concept-Clinician-Well-Being-Tools/`
    - **Card 2:** Shaping the Future → `/clinical-wellbeing/Concept-Clinician-Well-Being-Future/`

### Zone: `tools-branches` — Tools for Today children

- **UI Item:** Grid List with Linked Descriptions (3 items)
  - **Content Collection:**
    - **H2:** Choose Your Path
    - **Card:** Care for Yourself → spoke URL
    - **Card:** Strengthen Your Team → spoke URL
    - **Card:** Protect Patients & Peers → spoke URL

### Zone: `hub-toolkit-citation` — Attribution

- **UI Item:** Toolkit citation aside
  - **Content Collection:**
    - Link to ACC Clinician Well-Being Toolkit (PPT) + contributor credit

---

## Concept-Clinician-Well-Being-Tools.html

**Layout:** `Global/sidebar` (sidebar + micro hero)
**URL:** `/clinical-wellbeing/Concept-Clinician-Well-Being-Tools/`

### Zone: `hero` — Micro Branding

- **UI Item:** Micro Branding with CTA Button (`masthead: MicroSite/heroimage.micro.dynamic.html`)
  - **Art:** Text-free `WellBeing_*` JPG crops via `hero.yml` (`hero_image_dir` / `hero_image_ext` params).
  - **Content Collection:**
    - `data-item="hero-title"` → **H1:** Tools for Today
    - `btn-primary` → **Button label:** Download Toolkit
    - Mobile back arrow → hub

### Zone: `tools-intro` — Introduction

- **UI Item:** Reading typography
  - **Content Collection:**
    - **Body:** Burnout is treatable and preventable — but not by willpower alone…

### Zone: `tools-branches` — Three Branches

- **UI Item:** Grid List with Linked Descriptions (3 items)
  - **Content Collection:** Same three branch cards as hub

### Zone: `featured-resources` — Text links

- **UI Item:** Reading typography list
  - **Content Collection:**
    - **H2:** Start Anywhere
    - Three annotated links to deep spokes

### Zone: `tools-follow-up` — Follow Up CTA

- **UI Item:** Follow Up CTA — Beveled Card
  - **Content Collection:**
    - **Title:** Need a Cohort Experience?
    - **Subtitle:** Go deeper with peers
    - **Body:** Cardio Renew seven-month program…
    - `btn-primary` → **Button label:** Learn About Cardio Renew

---

## Concept-Clinician-Well-Being-Mental-Health.html

**Layout:** `Global/sidebar`  
**URL:** `/clinical-wellbeing/Concept-Clinician-Well-Being-Mental-Health/`

### Zone: `hero` — Micro Branding

- **UI Item:** Micro Branding with CTA Button (`masthead: MicroSite/heroimage.micro.dynamic.html`)
  - **Art:** Text-free `WellBeing_*` JPG crops via `hero.yml` (`hero_image_dir` / `hero_image_ext` params).
  - **Content Collection:**
    - **H1:** Care for Yourself
    - `btn-primary` → **Button label:** Get Support
    - `href` → Physician Support Line

### Zone: `mental-health-intro` — Introduction

- **UI Item:** Reading typography
  - **Content Collection:**
    - **Body:** Stress keeps you going. Burnout depletes you…

### Zone: `recognize-burnout` — Burnout Dimensions

- **UI Item:** Grid List with Descriptions (3 items)

### Zone: `burnout-screen` — Mini Z CTA

- **UI Item:** Primary callout → interactive assessment page
  - **Link:** `/clinical-wellbeing/Concept-Clinician-Well-Being-Mini-Z/`
  - **Button:** Start Mini Z Assessment

### Zone: `coping-guides` — Evergreen coping detail

- **UI Item:** Accordion stack (`Blocks/AccordionStack.html`, `mental_health_accordions.yml`)
  - **Panels:** (Screen for Burnout moved to dedicated Mini Z page)

### Zone: `mental-health-follow-up` — Follow Up CTA

- **UI Item:** Follow Up CTA — Beveled Card
  - **Content Collection:**
    - **Title:** Download the ACC Toolkit
    - `btn-primary` → **Button label:** Download Toolkit (PPT)

### Zone: `toolkit-citation` — Attribution

- **UI Item:** Toolkit citation aside

---

## Concept-Clinician-Well-Being-Mini-Z.html

**Layout:** `Global/sidebar`  
**URL:** `/clinical-wellbeing/Concept-Clinician-Well-Being-Mini-Z/`

### Zone: `hero` — Micro Branding

- **UI Item:** Micro Branding — **H1:** Screen for Burnout

### Zone: `mini-z-assessment` — Interactive Mini Z 2.0

- **UI Item:** Radio-button form (`mini-z-assessment.html`) + live scoring
  - **Data:** `_data/ClinicianWellBeing/mini_z.yml`
  - **Scoring:** Total 10–50; **below 40** → elevated burnout stress alert; **40+** → supportive range (per Mini Z PDF)
  - **Subscales:** Q1–5 supportive environment; Q6–10 pace & EMR stress
  - **Q2 alert** if value 1 or 2

### Zone: `mini-z-support` — Help links

- Physician Support Line · 988 · NCD course

---

## Concept-Clinician-Well-Being-Workplace.html

**Layout:** `Global/sidebar`  
**URL:** `/clinical-wellbeing/Concept-Clinician-Well-Being-Workplace/`

### Zone: `hero` — Micro Branding

- **UI Item:** Micro Branding with CTA Button (`masthead: MicroSite/heroimage.micro.dynamic.html`)
  - **Art:** Text-free `WellBeing_*` JPG crops via `hero.yml` (`hero_image_dir` / `hero_image_ext` params).
  - **Content Collection:**
    - **H1:** Strengthen Your Team
    - `btn-primary` → **Button label:** Download Toolkit

### Zone: `workplace-intro` — Introduction

- **UI Item:** Reading typography
  - **Content Collection:**
    - **Body:** Telling burned-out clinicians to "be more resilient" is not enough…

### Zone: `workplace-domains` — Three Reciprocal Domains

- **UI Item:** Grid List with Descriptions (3 items)
  - **Content Collection:**
    - **H2:** Three Domains of Workplace Well-Being
    - **Item:** Workplace Efficiency
    - **Item:** Culture of Wellness
    - **Item:** Personal Resilience (Organizational)

### Zone: `workplace-guides` — Toolkit + communication detail

- **UI Item:** Accordion stack (`Blocks/AccordionStack.html`, `workplace_accordions.yml`)
  - **Panels:**
    - Make Practice Sustainable *(Toolkit, open by default)*
    - Create a Culture Where Well-Being Is Expected *(Toolkit)*
    - Communicate With Clarity When Your Team Is Under Stress *(Crisis Communication — trust pillars, planning, key principles)*
    - Support the Whole Clinician *(organizational resilience)*
    - Employee Assistance Programs (EAP)
    - What ACC Chapters Can Do

### Zone: `workplace-follow-up` — Follow Up CTA

- **UI Item:** Follow Up CTA — Beveled Card
  - **Content Collection:**
    - **Title:** Facilitate a Local Conversation
    - `btn-primary` → **Button label:** Download Toolkit (PPT)

### Zone: `toolkit-citation` — Attribution

---

## Concept-Clinician-Well-Being-Protect.html

**Layout:** `Global/sidebar`  
**URL:** `/clinical-wellbeing/Concept-Clinician-Well-Being-Protect/`

### Zone: `hero` — Micro Branding

- **UI Item:** Micro Branding with CTA Button (`masthead: MicroSite/heroimage.micro.dynamic.html`)
  - **Art:** Text-free `WellBeing_*` JPG crops via `hero.yml` (`hero_image_dir` / `hero_image_ext` params).
  - **Content Collection:**
    - **H1:** Protect Patients & Peers
    - `btn-primary` → **Button label:** NCD Mental Health Course

### Zone: `protect-intro` — Introduction

- **UI Item:** Reading typography

### Zone: `trust-pillars` — Leadership Communication

- **UI Item:** Grid List with Descriptions (4 items)
  - **Content Collection:**
    - **H2:** Four Trust Pillars for Team Communication
    - Caring · Dedication · Competence · Honesty

### Zone: `crisis-communication` — Crisis Comms

- **UI Item:** Reading typography + PDF link
  - **Content Collection:**
    - **H2:** Communicating With Your Team in High-Stress Times
    - Crisis Communication Infographic (PDF)

### Zone: `ncd-course` — Patient Mental Health

- **UI Item:** Small Image-Text Panel with CTA
  - **Content Collection:**
    - **H3:** Recognize and Respond to Patient Mental Health
    - `btn-shade` → **Button label:** View NCD Course

### Zone: `confront-stigma` — Peer Support

- **UI Item:** Reading typography
  - **Content Collection:**
    - **H2:** When a Colleague Is Struggling
    - Infographic link, EAP, normalize conversation

### Zone: `protect-follow-up` — Follow Up CTA

- **UI Item:** Follow Up CTA — Beveled Card
  - **Content Collection:**
    - **Title:** Lead a Team Conversation
    - `btn-primary` → **Button label:** Back to Tools for Today

---

## Concept-Clinician-Well-Being-Future.html

**Layout:** `Global/sidebar`  
**URL:** `/clinical-wellbeing/Concept-Clinician-Well-Being-Future/`

### Zone: `hero` — Micro Branding

- **UI Item:** Micro Branding with CTA Button (`masthead: MicroSite/heroimage.micro.dynamic.html`)
  - **Art:** Text-free `WellBeing_*` JPG crops via `hero.yml` (`hero_image_dir` / `hero_image_ext` params).
  - **Content Collection:**
    - **H1:** Shaping the Future
    - `btn-primary` → **Button label:** Workforce Advocacy
    - `href` → Bolster the Workforce advocacy page

### Zone: `future-intro` — North Star

- **UI Item:** Reading typography
  - **Content Collection:**
    - **Body:** Tools help you today. Policy and advocacy change the system tomorrow.
    - **North star statement**

### Zone: `career-flexibility` — Policy Panel 1

- **UI Item:** Small Image-Text Panel with CTA
  - **Content Collection:**
    - **H3:** Career Flexibility in Cardiology
    - `btn-shade` → **Button label:** Read Policy Statement
    - `href` → JACC DOI

### Zone: `civility-policy` — Policy Panel 2

- **UI Item:** Small Image-Text Panel with CTA
  - **Content Collection:**
    - **H3:** Respect, Civility & Inclusion in the CV Workplace
    - `btn-shade` → **Button label:** Read Policy Statement

### Zone: `workforce-advocacy` — Advocacy

- **UI Item:** Reading typography
  - **Content Collection:**
    - **H2:** Advocating for the Workforce
    - Link: Bolster the Workforce Now and For the Future

### Zone: `partnerships` — Partnerships Grid

- **UI Item:** Grid List with Linked Descriptions (3 items)
  - **Content Collection:**
    - **H2:** National & Global Partnerships
    - NAM Change Maker · NAM Action Collaborative · Global Joint Opinion

### Zone: `future-follow-up` — Follow Up CTA

- **UI Item:** Follow Up CTA — Beveled Card
  - **Content Collection:**
    - **Title:** Policy Sets the Direction
    - **Subtitle:** Practice starts with you
    - `btn-primary` → **Button label:** Explore Tools for Today

### Zone: `toolkit-citation` — Attribution

---

## Sidebar navigation (all sub pages)

- **UI Item:** Side navigation (`Global/sidebar` + `sidebar_data_path` → `MicroSite/sidebar-nav.html`)
  - **Content Collection:**
    - **Root:** Clinician Well-Being → hub
    - **Items:** Overview · Tools for Today (children: Mental Health, Workplace, Protect) · Shaping the Future

---

## SME review prompts

1. Does the **two-lane fork** (Tools vs Future) match how members arrive?
2. Are the **three Tools branches** the right split, or should anything move?
3. Is **workplace content** substantive enough, or still too thin?
4. Which **stats** need updated sources beyond Toolkit (2018 Medscape)?
5. **Cardio Renew** — correct prominence on hub vs program page only?

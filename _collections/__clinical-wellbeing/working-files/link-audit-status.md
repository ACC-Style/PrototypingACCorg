---
published: false
title: Clinician Well-Being — Link Audit Status
created: 2026-07-07
updated: 2026-07-07
---

# Clinician Well-Being — Link Audit Status

Working record for the **content-collection vs. prototype** link compare.  
**Source inventories:** [content-collection.md](content-collection.md), legacy Hot Topics / Education & Resources, [prototype-toc.md](prototype-toc.md).

**Compare rule:** Items in [Excluded](#excluded-from-missing-links-compare) and [Backlog](#backlog--not-wire-as-external-links) do **not** count as prototype gaps.

---

## Excluded from "missing links" compare

User decision (2026-07-07). Do **not** wire these as prototype CTAs or accordion links.

| Link | Reason |
|------|--------|
| [AMA Mini Z](https://www.ama-assn.org/practice-management/physician-health/mini-z-burnout-survey) | Replaced by internal [Mini Z page](/clinical-wellbeing/Concept-Clinician-Well-Being-Mini-Z/). AMA URL may appear as a **source cite only** on that page — not a primary CTA. |
| [Maslach Burnout Inventory](https://www.mindgarden.com/117-maslach-burnout-inventory) | Excluded — commercial/third-party instrument; not a prototype destination. |
| [AHA Physician Alliance Well-Being Playbook](https://www.aha.org/physicians/well-playbook) | Excluded — external AHA resource; not wiring in this microsite. |
| [AHA physician suicide prevention resources](https://www.aha.org/news/insights-and-analysis/2019-09-17-suicide-prevention-resources-available-help-physicians) | Excluded — external AHA resource. |
| [Suicide Prevention Resource Center (sprc.org)](https://www.sprc.org/) | Excluded — external; 988 / PSL / ACC counseling article cover support in prototype. |
| [Practice Made Perfect — well-being in crisis](https://www.acc.org/latest-in-cardiology/articles/2020/03/23/15/00/practice-made-perfect-well-being-during-a-time-of-crisis) | Excluded — COVID-era podcast; not evergreen for this build. |
| [NEJM Catalyst — reciprocal domains](https://catalyst.nejm.org/doi/full/10.1056/CAT.17.0429) | Excluded — NEJM is blocked; Toolkit attribution text may cite Bohman et al. without a live NEJM link. |

---

## Backlog — not wire as external links now

Interesting for a later pass; **document only** until content strategy is set.

| Item | URL | Notes |
|------|-----|-------|
| **Total Leadership** (Friedman) | [PDF](https://www.totalleadership.org/wp-content/uploads/2018/10/Total-Leadership-in-People-and-Strategy-Journal-Fall-2018.pdf) | Prefer a **cannibalized ACC web page** on **Strengthen Your Team** (Workplace spoke) — self-leadership / Be Real · Be Whole content — rather than linking out to PDF. |
| **Burden of Battle** (Mediasite) | [Recording](https://acc.mediasite.com/mediasite/play/6d6c0b8c82134618977452e0abd568fe1d?autoStart=true) | Potential Workplace / DEI context (trauma, equity, workforce). Listed in content-collection under culture-of-wellness related resources; not wired yet. |

---

## Still missing — high-value gaps (worth wiring)

These remain in content-collection / legacy audit but are **not yet in prototype YAML or pages**. Prioritized for a future wiring pass.

| # | Link | Suggested home |
|---|------|----------------|
| 1 | [Prevalence and Professional Impact of Mental Health Conditions Among Cardiologists (JACC)](https://www.jacc.org/doi/full/10.1016/j.jacc.2022.11.025) | Hub — evidence / stats zone |
| 2 | [Mental Health Conditions Among Cardiologists: Silent Suffering (JACC editorial)](https://www.jacc.org/doi/full/10.1016/j.jacc.2022.11.026) | Hub — evidence / stats zone |
| 3 | [*Cardiology* — Physician Burnout: An Enemy We Must Recognize to Battle (2024)](https://www.acc.org/Latest-in-Cardiology/Articles/2024/02/01/01/42/from-the-member-sections-physician-burnout-an-enemy-we-must-recognize-to-battle) | Hub — hot topics / evidence |
| 4 | [Webinar: Embracing Career Flexibility as an Organizational Value](https://www.acc.org/Education-and-Meetings/Meetings/Meeting-Items/2023/07/01/01/Webinar-Embracing-Career-Flexibility-as-an-Organizational-Value) | Future spoke — supporting webinars under career-flexibility policy |
| 5 | [Webinar: Advocating for Career Flexibility for Early Career and FIT Members](https://www.acc.org/Education-and-Meetings/Meetings/Meeting-Items/2023/10/01/01/Webinar-Advocating-For-Career-Flexibility) | Future spoke — supporting webinars |
| 6 | [ACC DocMatter Community](https://www.acc.org/Membership/ACC-DocMatter-Community) | Hub — Connect / community zone |
| 7 | [Member Hub Well-Being and Burnout Interest Group](https://memberhub.acc.org/groups/home/43) | Hub — Connect / community zone |

**High-value gap count: 7**

---

## Still missing — lower priority

General ACC education / legacy index; not in current prototype scope unless SME asks.

| Link | Notes |
|------|-------|
| [Resources & Events (legacy well-being portal index)](https://www.acc.org/Features/2019/07/clinican-well-being-portal/Resources-and-Events) | Legacy index page; microsite replaces IA |
| ACC Scientific Session | General ACC education — Hot Topics carry-over |
| ACC Anywhere | General ACC education — Hot Topics carry-over |
| Practice Made Perfect podcast index | Distinct from excluded crisis episode |

**Lower-priority gap count: 4**

---

## Summary counts

| Category | Count |
|----------|------:|
| Excluded from compare | 7 |
| Backlog (document only) | 2 |
| **Still missing — high-value** | **7** |
| Still missing — lower priority | 4 |
| **Total open gaps (high + lower)** | **11** |

*Prior compare (pre-exclusions): ~19 named destinations not wired → **7 excluded** + **2 backlog** → **11 remaining** (7 high-value + 4 lower priority).*

---

## Wired in prototype (reference)

Core destinations already in `_data/ClinicianWellBeing/` and concept pages (~35+ URLs): Toolkit PPT, Cardio Renew, NCD Mental Health, well-being infographic, Bolster the Workforce, Member Sections, D&I, State Chapters, JACC policy statements (Future), HPS uncivil behavior PDF, NAM partnerships, three coaching webinars, PSL / 988 / CSTS / counseling resources, crisis communication PDF, internal Mini Z, uncivil-behavior spoke, etc.

See parent chat audit (2026-07-07) for full used list.

---

## Related files

- [content-collection.md](content-collection.md) — master link inventory (includes excluded URLs in draft copy)
- [prototype-toc.md](prototype-toc.md) — zone map for wiring decisions
- `_data/ClinicianWellBeing/mini_z.yml` — internal Mini Z; AMA cite as source only
- `raw-files/Clinician Well Being/Audit.md` — legacy IA audit (page list, not link matrix)

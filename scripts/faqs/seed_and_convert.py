#!/usr/bin/env python3
"""Seed ACC.26 FAQ CSVs from approved markdown, then build nested JSON.

Run `python3 scripts/faqs/seed_and_convert.py --seed` for the annual seed,
or omit --seed to rebuild nested.json from the editable CSV files.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "_data" / "annual_meeting" / "faqs"
SOURCES = {
    "faculty": Path.home() / "Downloads" / "ACC.26 Faculty FAQs.md",
    "abstracts-cases": Path.home() / "Downloads" / "ACC.26 Submissions FAQ Page_Revised.md",
    "lbct": Path.home() / "Downloads" / "ACC.26 LBCT FAQs Web Copy.md",
}
SPOKE_FIELDS = [
    "spoke_id", "spoke_sort", "spoke_label", "hub_blurb", "seo_title",
    "seo_meta_description", "seo_h1", "canonical_path", "date_modified",
    "robots", "status", "cross_banner", "cross_banner_href",
]
GROUP_FIELDS = ["spoke_id", "group_id", "group_label", "group_sort", "group_intro", "status"]
ITEM_FIELDS = [
    "spoke_id", "group_id", "item_id", "question", "answer_text",
    "answer_html", "item_sort", "related_spoke_id", "related_group_id",
    "status", "notes", "primary_query",
]

SPOKES = [
    {
        "spoke_id": "abstracts-cases", "spoke_sort": 1, "spoke_label": "Abstracts & Cases",
        "hub_blurb": "For abstract, complex clinical case, and CV Team submitters",
        "seo_title": "ACC.26 Abstract & Case Submission FAQs",
        "seo_meta_description": "Fees, eligibility, deadlines, portal help, and acceptance rules for ACC.26 abstract and complex clinical case submissions.",
        "seo_h1": "ACC.26 Abstract & Case Submission FAQs",
        "canonical_path": "/AnnualMeeting/faqs/abstracts-and-cases/", "date_modified": "2026-07-24",
        "robots": "index,follow", "status": "ready",
        "cross_banner": "Submitting a Late-Breaking Clinical Trial? See LBCT FAQs.",
        "cross_banner_href": "/AnnualMeeting/faqs/late-breaking-clinical-trials/",
    },
    {
        "spoke_id": "faculty", "spoke_sort": 2, "spoke_label": "Faculty",
        "hub_blurb": "For invited faculty, chairs, presenters, and panelists",
        "seo_title": "ACC.26 Faculty FAQs",
        "seo_meta_description": "Invitation, disclosures, complimentary registration, travel, session prep, and Speaker Service Center guidance for ACC.26 faculty.",
        "seo_h1": "ACC.26 Faculty FAQs", "canonical_path": "/AnnualMeeting/faqs/faculty/",
        "date_modified": "2026-07-24", "robots": "index,follow", "status": "ready",
        "cross_banner": "Also presenting accepted science? See Abstracts & Cases or LBCT acceptance FAQs.",
        "cross_banner_href": "/AnnualMeeting/faqs/",
    },
    {
        "spoke_id": "lbct", "spoke_sort": 3, "spoke_label": "Late-Breaking Clinical Trials",
        "hub_blurb": "For Late-Breaking Clinical Trial submitters and presenters",
        "seo_title": "ACC.26 Late-Breaking Clinical Trial FAQs",
        "seo_meta_description": "Fees, embargo rules, deadlines, disclosures, and acceptance guidance for ACC.26 Late-Breaking Clinical Trial submissions.",
        "seo_h1": "ACC.26 Late-Breaking Clinical Trial FAQs",
        "canonical_path": "/AnnualMeeting/faqs/late-breaking-clinical-trials/", "date_modified": "2026-07-24",
        "robots": "index,follow", "status": "ready",
        "cross_banner": "Submitting an abstract or complex case? See Abstracts & Cases FAQs.",
        "cross_banner_href": "/AnnualMeeting/faqs/abstracts-and-cases/",
    },
]

GROUPS = {
    "faculty": [
        ("invitation-disclosures", "Invitation & disclosures"),
        ("registration-benefits", "Registration & faculty benefits"),
        ("travel-hotel-visa", "Travel, hotel & visa"),
        ("preparing-session", "Preparing your session"),
        ("onsite-speaker-center", "Onsite & Speaker Service Center"),
    ],
    "abstracts-cases": [
        ("fees", "Fees"), ("eligibility", "Eligibility & prior presentation"),
        ("deadlines", "Deadlines & changes before close"), ("what-where", "What & where to submit"),
        ("authors-institutions", "Authors & institutions"), ("technical", "Technical & completion"),
        ("after-deadline", "After the deadline"), ("acceptance", "Acceptance, registration & publication"),
    ],
    "lbct": [
        ("fees", "Fees"), ("eligibility", "Eligibility & embargo"),
        ("deadlines", "Deadlines & changes before close"), ("what-where", "What & where to submit"),
        ("authors-institutions", "Authors, institutions & disclosures"), ("technical", "Technical & completion"),
        ("after-deadline", "After the deadline"), ("acceptance", "Acceptance, registration & publication"),
    ],
}

HEADING_MAP = {
    "faculty": {
        "Invitation and Disclosure": "invitation-disclosures", "Registration": "registration-benefits",
        "Faculty Benefit": "registration-benefits", "Travel, Hotel and Visa": "travel-hotel-visa",
        "Session and Presentation": "preparing-session", "Onsite": "onsite-speaker-center",
    },
    "abstracts-cases": {
        "Fee": "fees", "Eligibility": "eligibility", "Deadline": "deadlines",
        "General Submission": "what-where", "Author and Institution": "authors-institutions",
        "Technical and Process": "technical", "Post-Deadline": "after-deadline", "Acceptance": "acceptance",
    },
    "lbct": {
        "Fee": "fees", "Eligibility": "eligibility", "Deadline": "deadlines",
        "General Submission": "what-where", "Author and Institution": "authors-institutions",
        "Technical and Process": "technical", "Post-Deadline": "after-deadline", "Acceptance": "acceptance",
    },
}


def clean_markdown(text: str) -> str:
    """Turn source markdown into editable plain text without changing wording."""
    text = text.strip()
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    # Joplin/markdown mailto links → bare email (plain_to_html will linkify)
    text = re.sub(r"\[_?([^\]\n]+?)_?\]\(mailto:([^)]+)\)", r"\2", text)
    text = re.sub(r"\[([^\]]+)]\((https?://[^)]+)\)", r"\1 (\2)", text)
    text = re.sub(r"<(https?://[^>]+)>", r"\1", text)
    text = text.replace("**", "").replace("_", "").replace("\\$", "$").replace("\\*", "*")
    return re.sub(r"[ \t]+\n", "\n", text).strip()


def plain_to_html(text: str) -> str:
    """Escape plain text; render paragraphs, bullet lists, emails, and HTTPS URLs."""
    text = text.replace("\\$", "$")
    def linkify(value: str) -> str:
        value = html.escape(value)
        # Markdown-style links that survived cleaning
        value = re.sub(
            r"\[([^\]]+)]\((https?://[^)\s]+|mailto:[^)]+)\)",
            lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', value,
        )
        value = re.sub(
            r"(?<![\"'=])(https://[^\s<]+)",
            r'<a href="\1">\1</a>', value,
        )
        value = re.sub(
            r"(?<![\w:/\">])([\w.+-]+@[\w.-]+\.[A-Za-z]{2,})",
            r'<a href="mailto:\1">\1</a>', value,
        )
        # Drop leftover "(mailto:…)" artifacts next to an already-linked address
        value = re.sub(r'(</a>)\s*\(mailto:[^)]+\)', r"\1", value)
        return value

    blocks, paragraph, list_items = [], [], []
    def flush() -> None:
        nonlocal paragraph, list_items
        if paragraph:
            blocks.append(f"<p>{'<br>'.join(linkify(line) for line in paragraph)}</p>")
            paragraph = []
        if list_items:
            blocks.append("<ul>" + "".join(f"<li>{linkify(item)}</li>" for item in list_items) + "</ul>")
            list_items = []
    for line in text.strip().splitlines():
        bullet = re.match(r"^\s*(?:-|•)\s+(.+)$", line)
        if bullet:
            if paragraph:
                flush()
            list_items.append(bullet.group(1))
        elif line.strip():
            if list_items:
                flush()
            paragraph.append(line.strip())
        else:
            flush()
    flush()
    return "".join(blocks)


def answer_html(source_answer: str, question: str) -> tuple[str, str]:
    """Return editable text and display HTML, retaining the source eligibility table."""
    if "<table>" in source_answer:
        before, rest = re.split(r'<div class="joplin-table-wrapper">', source_answer, maxsplit=1)
        table_html, after = rest.split("</div>", maxsplit=1)
        table_html = (
            table_html.strip()
            .replace("&nbsp;", " ")
            .replace("<p>", "")
            .replace("</p>", "")
        )
        table_html = re.sub(r"</?div[^>]*>", "", table_html).strip()
        rendered = (
            plain_to_html(clean_markdown(before))
            + table_html
            + plain_to_html(clean_markdown(after))
        )
        return (
            "See the eligible/not-eligible criteria table for submission requirements.",
            rendered,
        )
    plain = clean_markdown(source_answer)
    return plain, plain_to_html(source_answer)


def parse_questions(spoke_id: str, source: Path) -> list[dict[str, str]]:
    lines = source.read_text(encoding="utf-8").splitlines()
    found, group_id, question, answer = [], "", None, []

    def commit() -> None:
        nonlocal question, answer
        if question and group_id:
            raw = "\n".join(answer).strip()
            text, rendered = answer_html(raw, question)
            found.append({"group_id": group_id, "question": question, "answer_text": text, "answer_html": rendered})
        question, answer = None, []

    for line in lines:
        stripped = line.strip()
        heading = re.match(r"^\*{0,2}(?:\d+\\?\.\s*)?(.+?) (?:Related )?Questions\*{0,2}$", stripped)
        if heading:
            commit()
            title = heading.group(1).replace("**", "").strip()
            group_id = next((v for k, v in HEADING_MAP[spoke_id].items() if title.startswith(k)), "")
            continue
        if spoke_id == "abstracts-cases":
            q = re.match(r"^-\s+\*\*_(.+?)_\*\*$", stripped)
        else:
            q = re.match(r"^\*\*(.+?)\*\*$", stripped)
        if q:
            commit()
            question = q.group(1).strip()
            continue
        if question:
            answer.append(line)
    commit()
    return found


def slug(value: str) -> str:
    value = value.lower().replace("acc.26", "acc26").replace("lbct", "lbct")
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value)).strip("-")


def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def seed() -> Counter:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    missing = [str(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("Source markdown not found: " + ", ".join(missing))
    group_rows = [
        {"spoke_id": spoke, "group_id": gid, "group_label": label, "group_sort": sort,
         "group_intro": "", "status": "ready"}
        for spoke, groups in GROUPS.items() for sort, (gid, label) in enumerate(groups, 1)
    ]
    items, counts = [], Counter()
    prefixes = {"faculty": "fac", "abstracts-cases": "abs", "lbct": "lbct"}
    overrides = {
        ("faculty", "I can't find my original ACC.26 faculty invitation. Is there an easy way for me to access it?"): "fac-inv-access-invitation",
        ("abstracts-cases", "Is there a submission fee?"): "abs-fee-submission-fee",
        ("lbct", "What is the deadline for submission?"): "lbct-dead-deadline",
    }
    for spoke_id, source in SOURCES.items():
        sort_by_group = Counter()
        for item in parse_questions(spoke_id, source):
            group_id = item["group_id"]
            sort_by_group[group_id] += 1
            item["spoke_id"] = spoke_id
            item["item_id"] = overrides.get(
                (spoke_id, item["question"]),
                f"{prefixes[spoke_id]}-{slug(group_id)[:14]}-{slug(item['question'])}",
            )
            item["item_sort"] = sort_by_group[group_id] * 10
            item["related_spoke_id"] = ""
            item["related_group_id"] = ""
            item["status"] = "ready"
            item["notes"] = ""
            item["primary_query"] = item["question"].rstrip("?")
            if item["question"] == "If I submit my abstract or case to ACC.26, am I allowed to submit it to other conferences or journals?":
                item["related_spoke_id"], item["related_group_id"] = "lbct", "eligibility"
            items.append(item)
            counts[spoke_id] += 1
    write_csv(DATA_DIR / "spokes.csv", SPOKE_FIELDS, SPOKES)
    write_csv(DATA_DIR / "groups.csv", GROUP_FIELDS, group_rows)
    write_csv(DATA_DIR / "items.csv", ITEM_FIELDS, items)
    write_documentation()
    build_nested()
    return counts


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA_DIR / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_nested() -> dict:
    spokes, groups, items = read_csv("spokes.csv"), read_csv("groups.csv"), read_csv("items.csv")
    valid_groups = {(group["spoke_id"], group["group_id"]) for group in groups}
    item_ids = [item["item_id"] for item in items]
    if len(item_ids) != len(set(item_ids)):
        raise ValueError("item_id values must be unique.")
    invalid = [item["item_id"] for item in items if (item["spoke_id"], item["group_id"]) not in valid_groups]
    if invalid:
        raise ValueError("Items reference missing spoke/group pairs: " + ", ".join(invalid))
    visible = {"ready", "published"}
    groups_by_spoke = {}
    for group in groups:
        if group["status"] in visible:
            groups_by_spoke.setdefault(group["spoke_id"], []).append(group)
    items_by_group = {}
    for item in items:
        if item["status"] in visible:
            items_by_group.setdefault((item["spoke_id"], item["group_id"]), []).append(item)
    output_spokes = []
    for spoke in sorted((s for s in spokes if s["status"] in visible), key=lambda s: int(s["spoke_sort"])):
        spoke_out = dict(spoke)
        spoke_out["spoke_sort"] = int(spoke_out["spoke_sort"])
        spoke_out["groups"] = []
        for group in sorted(groups_by_spoke.get(spoke["spoke_id"], []), key=lambda g: int(g["group_sort"])):
            group_out = {key: group[key] for key in ("group_id", "group_label", "group_intro")}
            group_out["group_sort"] = int(group["group_sort"])
            group_out["items"] = [
                {
                    "item_id": item["item_id"], "question": item["question"],
                    "answer_html": item["answer_html"] or plain_to_html(item["answer_text"]),
                    "item_sort": int(item["item_sort"]), "related_spoke_id": item["related_spoke_id"],
                    "related_group_id": item["related_group_id"],
                }
                for item in sorted(items_by_group.get((spoke["spoke_id"], group["group_id"]), []), key=lambda i: int(i["item_sort"]))
            ]
            spoke_out["groups"].append(group_out)
        output_spokes.append(spoke_out)
    payload = {"generated_at": datetime.now(timezone.utc).isoformat(), "spokes": output_spokes}
    (DATA_DIR / "nested.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return payload


def write_documentation() -> None:
    (DATA_DIR / "README.md").write_text("""# ACC.26 FAQ content workflow

## Hub content
- SEO title: ACC.26 Scientific Session FAQs
- H1: ACC.26 FAQs
- Canonical path: `/AnnualMeeting/faqs/`
- Intro: Find answers by your role. Choose Faculty, Abstracts & Cases, or Late-Breaking Clinical Trials.

## Editorial files and schemas
SMEs should edit the CSV files in Excel and export each worksheet as **CSV UTF-8** (not XLSX). Do not reorder or rename headers.

- `spokes.csv`: one row per role page; includes display order, hub copy, SEO, canonical, robots, status, and cross-link banner fields.
- `groups.csv`: `spoke_id`, group ID/label/order, optional intro, and status.
- `items.csv`: one row per FAQ. Keep `question` in its interrogative form. Put readable source text in `answer_text`; use `answer_html` only when formatting such as the Abstracts eligibility table is required.

CSV uses standard escaping: quote fields containing commas or line breaks and double embedded quotes. Stable IDs are content keys: do not change `spoke_id`, `group_id`, or `item_id` when editing copy.

## SME conventions
- Preserve approved question and answer meaning. Verify dates, fees, contacts, links, and embargo wording with the owning program team.
- Use `ready` for demo-approved content and `published` for live-approved content. Other statuses are omitted from `nested.json`.
- Add cross-journey context through `related_spoke_id` and `related_group_id`; do not duplicate another spoke's answer.
- `answer_html` takes precedence. When it is blank, the converter makes paragraphs and bullet lists from `answer_text`, escaping text and linking email addresses and HTTPS URLs.

## Annual refresh
1. Obtain the approved Faculty, Abstracts/Cases, and LBCT source copy.
2. Update CSV rows while retaining IDs and group mapping; add rows for genuinely new FAQs.
3. Reconfirm the content-hygiene flags in `CONTENT_FLAGS.md`.
4. Run `python3 scripts/faqs/seed_and_convert.py` to validate and rebuild `nested.json`.
5. Review generated HTML, SEO fields, counts, and source-owner approval before setting production content to `published`.
""", encoding="utf-8")
    (DATA_DIR / "CONTENT_FLAGS.md").write_text("""# ACC.26 FAQ content hygiene flags

| Area | Source of truth / conflict | Required action |
|---|---|---|
| LBCT deadline | FAQ source says **Tue. Nov. 18, 2025, 1 p.m. ET**; prototype `011_submit_late-breaking.html` shows Thu. Nov. 20. | Treat the FAQ source as authoritative until SME sign-off. |
| Abstracts deadline | FAQ source says **Sept. 30, 2025, 1 p.m. ET**; prototype `014` shows Oct. 2. | Flag for SME confirmation. |
| Faculty childcare | Source is a soft pointer: “Please visit the ACC.26 website for more information.” | Do not imply a confirmed provider, schedule, or registration path without program-owner confirmation. |
| Abstracts dates | Robin/Rebekah are expected to refresh Abstracts dates in mid-August. | Hold production-final approval until that date pass; the current seed can be used for a demo/prototype. |

**Status:** Demo/prototype content is OK. Production-final content is pending the SME date pass.
""", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", action="store_true", help="Recreate CSVs from the approved source markdown.")
    args = parser.parse_args()
    counts = seed() if args.seed else Counter(item["spoke_id"] for item in read_csv("items.csv"))
    if not args.seed:
        build_nested()
    print("FAQ item counts: " + ", ".join(f"{spoke}={count}" for spoke, count in sorted(counts.items())))
    try:
        from export_html_blobs import main as export_blobs
        export_blobs()
    except Exception as exc:  # pragma: no cover - optional companion script
        print(f"HTML blob export skipped: {exc}")


if __name__ == "__main__":
    main()

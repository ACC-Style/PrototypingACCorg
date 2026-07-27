#!/usr/bin/env python3
"""Export CMS-ready FAQ HTML blobs from nested.json (no Jekyll required).

Item markup and runtime shim are loaded from `_includes/annual/` so they stay
aligned with the Jekyll includes used by FAQ pages and the generator.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "_data" / "annual_meeting" / "faqs"
NESTED = DATA_DIR / "nested.json"
BLOB_DIR = DATA_DIR / "blobs"
INCLUDES = ROOT / "_includes" / "annual"
ITEM_INCLUDE = INCLUDES / "faq-item.html"
RUNTIME_INCLUDE = INCLUDES / "faq-runtime.html"


def load_runtime() -> str:
    """Return faq-runtime.html for CMS paste (strip leading HTML comment only)."""
    text = RUNTIME_INCLUDE.read_text(encoding="utf-8")
    return re.sub(r"^<!--.*?-->\s*", "", text, count=1, flags=re.S).strip() + "\n"


def render_item(item: dict) -> str:
    """Mirror `_includes/annual/faq-item.html` with Python (no Liquid at export time)."""
    q_attr = html.escape(item["question"], quote=True)
    q_text = html.escape(item["question"])
    iid = html.escape(item["item_id"])
    answer = item.get("answer_html") or ""
    # Keep class strings in sync with faq-item.html
    return f"""<details
  class="m-b_4 grid columns_1 columns_3:lg gap_4:lg"
  data-component="FaqItem"
  data-item="faq-qa"
  data-faq-question="{q_attr}"
  id="q-{iid}">
  <summary class="p-x_3 p-y_2 link c_primary-n2 h:bg_primary-5 br_radius col-start_1:lg col-end_2:lg">
    <h3 class="font_copy font_bold inline m_0 font-size_up">{q_text}</h3>
  </summary>
  <div
    class="p_3 p-x_4:md reading-typography bg_black-1 br_radius col-start_2:lg col-end_end:lg"
    data-role="faq-answer"
    id="a-{iid}">
{answer}
  </div>
</details>
"""


def render_spoke(spoke: dict) -> str:
    parts: list[str] = [
        f'<div data-component="FaqSpoke" data-spoke="{html.escape(spoke["spoke_id"])}" data-role="faq-spoke-body" class="reading-typography">',
        f'<header class="m-b_4"><h1 class="c_primary font_display">{html.escape(spoke["seo_h1"])}</h1>',
        f'<p>{html.escape(spoke.get("seo_meta_description", ""))}</p>',
        f'<p class="font-size_down c_black-7">Updated <time datetime="{html.escape(spoke.get("date_modified", ""))}">{html.escape(spoke.get("date_modified", ""))}</time></p></header>',
    ]
    banner = (spoke.get("cross_banner") or "").strip()
    href = (spoke.get("cross_banner_href") or "").strip()
    if banner and href:
        parts.append(
            f'<div class="m-b_4 p_3 bg_accent-5 br_radius" data-role="faq-cross-banner" role="note">'
            f'<p class="m_0"><a class="link font_bold" href="{html.escape(href)}">{html.escape(banner)}</a></p></div>'
        )
    parts.append('<nav class="m-b_4 p_3 bg_black-1 br_radius" aria-label="On this page" data-role="faq-jump-nav">')
    parts.append('<p class="font_bold m-b_2 m-t_0">On this page</p><ul class="ul_none grid gap_2 m_0">')
    for group in spoke.get("groups", []):
        gid = html.escape(group["group_id"])
        parts.append(f'<li><a class="link" href="#g-{gid}">{html.escape(group["group_label"])}</a></li>')
    parts.append("</ul></nav>")

    for group in spoke.get("groups", []):
        gid = html.escape(group["group_id"])
        parts.append(
            f'<section class="m-b_5" data-component="FaqGroup" data-role="faq-group" '
            f'id="g-{gid}" aria-labelledby="h-{gid}">'
        )
        parts.append(f'<h2 id="h-{gid}" class="c_primary font_display m-b_3">{html.escape(group["group_label"])}</h2>')
        for item in group.get("items", []):
            parts.append(render_item(item))
        parts.append("</section>")

    parts.append("</div>")
    parts.append(load_runtime())
    return "\n".join(parts)


def main() -> None:
    if not RUNTIME_INCLUDE.exists():
        raise FileNotFoundError(f"Missing shared runtime include: {RUNTIME_INCLUDE}")
    if not ITEM_INCLUDE.exists():
        raise FileNotFoundError(f"Missing shared item include: {ITEM_INCLUDE}")

    data = json.loads(NESTED.read_text(encoding="utf-8"))
    BLOB_DIR.mkdir(parents=True, exist_ok=True)
    meta_lines = [
        "# FAQ CMS blobs\n",
        "Paste each `*-blob.html` into the matching CMS richtext area.\n",
        "\nShared sources:\n",
        f"- `{ITEM_INCLUDE.relative_to(ROOT)}` (item markup; keep Python render_item in sync)\n",
        f"- `{RUNTIME_INCLUDE.relative_to(ROOT)}` (CSS/JS shim; inlined into every blob)\n",
    ]
    for spoke in data["spokes"]:
        slug = spoke["canonical_path"].strip("/").split("/")[-1]
        path = BLOB_DIR / f"{slug}-blob.html"
        path.write_text(render_spoke(spoke), encoding="utf-8")
        meta_lines.append(
            f"- `{path.name}` → `{spoke['canonical_path']}` · title `{spoke['seo_title']}`\n"
        )
        print(f"Wrote {path.relative_to(ROOT)}")
    (BLOB_DIR / "README.md").write_text("".join(meta_lines), encoding="utf-8")


if __name__ == "__main__":
    main()

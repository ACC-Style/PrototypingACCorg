#!/usr/bin/env python3
"""Export CMS-ready FAQ HTML blobs from nested.json (no Jekyll required).

Markup is split to match the generator copy areas:
  - jump nav + filter
  - FAQ body (groups + items)
  - runtime styles + script
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
    return f"""<details
  class="m-b_4 m-b_5:lg gap_4:lg font_accent font_medium"
  data-component="FaqItem"
  data-item="faq-qa"
  data-faq-question="{q_attr}"
  id="q-{iid}">
  <summary class="p-x_3 p-y_2 link c_secondary-n3 br_0 br_none br_secondary-3 br_solid:lg br-r_2 wrap_balance">
    <h3 class="font_copy font_bold inline m_0 font-size_up sticky:lg t_3:lg">{q_text}</h3>
  </summary>
  <div
    class="p_3 reading-typography wrap_pretty"
    data-role="faq-answer"
    id="a-{iid}">
{answer}
  </div>
</details>
"""


def render_jump_nav(spoke: dict) -> str:
  sid = html.escape(spoke["spoke_id"])
  lines = [
      '<nav class="m-b_4 p_3 bg_black-1 br_radius sticky t_3" aria-label="On this page" data-role="faq-jump-nav">',
      '<p class="font_bold m-b_2 m-t_0">On this page</p>',
      '<ul class="ul_none grid gap_2 m_0" data-role="faq-jump-list">',
  ]
  for group in spoke.get("groups", []):
      gid = html.escape(group["group_id"])
      label = html.escape(group["group_label"])
      lines.append(
          f'<li class="m_0 p_0"><a class="link a:bg_secondary-n2 a:c_white block p-x_3 p-y_2" '
          f'href="#g-{gid}" data-role="faq-jump-link">{label}</a></li>'
      )
  lines.extend([
      "</ul>",
      f'<div class="m-t_4 flex flex_column gap_2" data-role="faq-filter-bar">',
      f'<label class="font_bold" for="faq-filter-{sid}">Filter questions</label>',
      f'<input id="faq-filter-{sid}" type="search" class="br_1 br_black-3 br_solid br_radius p_3 w_100" '
      'data-role="faq-filter" placeholder="Type to filter…" autocomplete="off">',
      '<p class="font-size_down c_black-7 m_0" data-role="faq-filter-status" aria-live="polite"></p>',
      "</div>",
      "</nav>",
  ])
  return "\n".join(lines) + "\n"


def render_body(spoke: dict) -> str:
    parts = [
        f'<div class="wrapper-container" data-component="FaqSpoke" data-spoke="{html.escape(spoke["spoke_id"])}" '
        'data-role="faq-spoke-body">',
    ]
    for group in spoke.get("groups", []):
        gid = html.escape(group["group_id"])
        parts.append(
            f'<section class="m-b_5" data-component="FaqGroup" data-role="faq-group" '
            f'id="g-{gid}" aria-labelledby="h-{gid}">'
        )
        parts.append(
            f'<h2 id="h-{gid}" class="m-b_4 m-b_5:lg p-b_3 br-b_1 br_black-3 br_solid">'
            f'{html.escape(group["group_label"])}</h2>'
        )
        parts.append('<div data-role="faq-items">')
        for item in group.get("items", []):
            parts.append(render_item(item))
        parts.append("</div></section>")
    parts.append("</div>")
    return "\n".join(parts) + "\n"


def render_spoke(spoke: dict) -> str:
    return render_jump_nav(spoke) + render_body(spoke) + load_runtime()


def main() -> None:
    if not RUNTIME_INCLUDE.exists():
        raise FileNotFoundError(f"Missing shared runtime include: {RUNTIME_INCLUDE}")

    data = json.loads(NESTED.read_text(encoding="utf-8"))
    BLOB_DIR.mkdir(parents=True, exist_ok=True)
    meta_lines = [
        "# FAQ CMS blobs\n",
        "Paste blocks from the generator (`__generators/Annual-Meeting-FAQs.html`) or these files:\n",
        "- `*-jump-nav.html` — sticky sidebar\n",
        "- `*-body.html` — groups + Q&A\n",
        "- `*-runtime.html` — shared styles + script (same for all spokes)\n",
        "- `*-blob.html` — combined legacy paste\n",
        "\nShared sources:\n",
        f"- `{INCLUDES.relative_to(ROOT)}/faq-*.html`\n",
    ]
    runtime_once = load_runtime()
    (BLOB_DIR / "faq-runtime.html").write_text(runtime_once, encoding="utf-8")

    for spoke in data["spokes"]:
        slug = spoke["canonical_path"].strip("/").split("/")[-1]
        (BLOB_DIR / f"{slug}-jump-nav.html").write_text(render_jump_nav(spoke), encoding="utf-8")
        (BLOB_DIR / f"{slug}-body.html").write_text(render_body(spoke), encoding="utf-8")
        (BLOB_DIR / f"{slug}-blob.html").write_text(render_spoke(spoke), encoding="utf-8")
        meta_lines.append(f"- `{slug}` → `{spoke['canonical_path']}` · `{spoke['seo_title']}`\n")
        print(f"Wrote {slug}-jump-nav.html, {slug}-body.html, {slug}-blob.html")

    (BLOB_DIR / "README.md").write_text("".join(meta_lines), encoding="utf-8")


if __name__ == "__main__":
    main()

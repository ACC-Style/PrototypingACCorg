# ACC.26 FAQ content workflow

## Shared design & runtime (edit once)

| File | Used by |
|------|---------|
| `_includes/annual/faq-item.html` | FAQ spoke pages, generator CMS blob |
| `_includes/annual/faq-runtime.html` | FAQ spoke pages, generator CMS blob, `blobs/*-blob.html` |

`Copy CMS HTML` on the generator inlines both the rendered items and the runtime shim so Web Production pastes a self-contained richtext payload.

## Hub content
- SEO title: ACC.26 Scientific Session FAQs
- H1: ACC.26 FAQs
- Canonical path: `/AnnualMeeting/faqs/`
- Intro: Find answers by your role. Choose Faculty, Abstracts & Cases, or Late-Breaking Clinical Trials.

## Editorial files and schemas
SMEs should edit the CSV files in Excel and export each worksheet as **CSV UTF-8** (not XLSX). Do not reorder or rename headers.

- `spokes.csv`: one row per role page; includes display order, hub copy, SEO, canonical, robots, status, and cross-link banner fields.
- `groups.csv`: `spoke_id`, group ID/label/order, optional intro, and status.
- `items.csv`: one row per FAQ. Columns: `spoke_id,group_id,item_id,question,answer_html,item_sort,status`. Put the published answer in **`answer_html`** (semantic HTML).

CSV uses standard escaping: quote fields containing commas or line breaks and double embedded quotes. Stable IDs are content keys: do not change `spoke_id`, `group_id`, or `item_id` when editing copy.

## SME conventions
- Preserve approved question and answer meaning. Verify dates, fees, contacts, links, and embargo wording with the owning program team.
- Use `ready` for demo-approved content and `published` for live-approved content. Other statuses are omitted from `nested.json`.
- **`answer_html` is required** and is what pages/CMS blobs render. Prefer `<p>`, `<ul>/<li>`, `<strong>`, `<em>`, and `<a>`. Do not leave raw Markdown (`**`, `_`) in this field.

## Day-to-day edit loop
1. Edit `items.csv` → update `answer_html` (and question/status as needed).
2. Run `python3 scripts/faqs/seed_and_convert.py` to rebuild `nested.json` (+ blobs when Python export is available).
3. Preview the FAQ spoke pages.

## Annual refresh
1. Obtain the approved Faculty, Abstracts/Cases, and LBCT source copy.
2. Update CSV rows while retaining IDs and group mapping; add rows for genuinely new FAQs. Store answers as HTML in `answer_html`.
3. Reconfirm the content-hygiene flags in `CONTENT_FLAGS.md`.
4. Run `python3 scripts/faqs/seed_and_convert.py` to validate and rebuild `nested.json`.
5. Review generated HTML, SEO fields, counts, and source-owner approval before setting production content to `published`.

Optional one-time seed from Joplin Markdown (writes HTML into the CSV): `python3 scripts/faqs/seed_and_convert.py --seed`.

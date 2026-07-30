# ACC Annual Scientific Session FAQ content workflow

## Shared design & runtime (edit once)

| File | Used by |
|------|---------|
| `_includes/annual/faq-item.html` | FAQ Q&A markup |
| `_includes/annual/faq-group.html` | FAQ group sections |
| `_includes/annual/faq-spoke-body.html` | Main FAQ column (groups + items) |
| `_includes/annual/faq-jump-nav.html` | Sticky jump nav + filter |
| `_includes/annual/faq-runtime.html` | Shared styles + script |

The generator (`_collections/__generators/Annual-Meeting-FAQs.html`) exposes separate copy areas per spoke: **jump nav**, **FAQ body**, and **runtime**.

## Hub content
- SEO title: ACC Annual Scientific Session FAQs
- H1: ACC Annual Scientific Session FAQs
- Canonical path: `/AnnualMeeting/faqs/`
- Intro: Find answers by your role. Choose Faculty, Abstracts & Cases, or Late-Breaking Clinical Trials.

## Editorial files (Jekyll `_data`)
Edit CSV files in Excel and export each worksheet as **CSV UTF-8** (not XLSX). Do not reorder or rename headers.

Jekyll loads them directly:

| File | Loaded as |
|------|-----------|
| `spokes.csv` | `site.data.annual_meeting.faqs.spokes` |
| `groups.csv` | `site.data.annual_meeting.faqs.groups` |
| `items.csv` | `site.data.annual_meeting.faqs.items` |

- `spokes.csv`: one row per role page; includes display order, hub copy, SEO, canonical, robots, status, and cross-link banner fields.
- `groups.csv`: `spoke_id`, group ID/label/order, optional intro, and status.
- `items.csv`: one row per FAQ. Put the published answer in **`answer_html`** (semantic HTML).

CSV uses standard escaping: quote fields containing commas or line breaks and double embedded quotes. Stable IDs are content keys: do not change `spoke_id`, `group_id`, or `item_id` when editing copy.

## Status values
`status` works the same way in all three CSVs (spoke, group, and item rows).

| Status | Renders? | Use for |
|--------|----------|---------|
| `ready` | Yes | Approved content. The only value that renders. |
| `hold` | No | Drafted or unapproved content you want to keep in the sheet. |
| `delete` | No | Content queued for removal. The generator lists these `item_id`s in a red alert so someone can delete the rows. |

Anything else (including a blank cell) is treated as not ready and will not render.

## SME conventions
- Preserve approved question and answer meaning. Verify dates, fees, contacts, links, and embargo wording with the owning program team.
- **`answer_html` is required** and is what pages/CMS blobs render. Prefer `<p>`, `<ul>/<li>`, `<strong>`, `<em>`, and `<a>`. Do not leave raw Markdown (`**`, `_`) in this field.

## Day-to-day edit loop
1. Edit `items.csv` (and `spokes.csv` / `groups.csv` as needed).
2. Rebuild / refresh the Jekyll site.
3. Preview FAQ pages or copy CMS blocks from the generator.

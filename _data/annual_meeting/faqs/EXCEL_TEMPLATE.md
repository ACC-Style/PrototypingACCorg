# ACC Annual Scientific Session FAQ — Excel workbook template (SME)

Use this as the column contract for `ACC-Session-FAQ-Content.xlsx`. Export each sheet to CSV into `_data/annual_meeting/faqs/`, then rebuild / refresh the Jekyll site.

## Sheets

### Spokes
`spoke_id,spoke_sort,spoke_label,hub_blurb,seo_title,seo_meta_description,seo_h1,canonical_path,date_modified,robots,status,cross_banner,cross_banner_href`

### Groups
`spoke_id,group_id,group_label,group_sort,group_intro,status`

### Items
`spoke_id,group_id,item_id,question,answer_html,item_sort,status`

## SME rules
- Keep questions in interrogative form.
- Put the published answer in **`answer_html`** (semantic HTML: `<p>`, lists, `<strong>`, `<em>`, links).
- Do not change `item_id` after publish (deep links).
- `status` accepts `ready` (renders), `hold` (not ready yet), or `delete` (queued for removal). Only `ready` renders; `delete` rows are listed in an alert on the generator page.

Full workflow: [README.md](./README.md) · Hygiene flags: [CONTENT_FLAGS.md](./CONTENT_FLAGS.md)

Seeded CSVs in this folder are the current demo source of truth until an `.xlsx` is circulated to Robin/Rebekah.

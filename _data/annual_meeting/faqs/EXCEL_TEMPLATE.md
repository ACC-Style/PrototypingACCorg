# ACC.26 FAQ — Excel workbook template (SME)

Use this as the column contract for `ACC26-FAQ-Content.xlsx`. Export each sheet to CSV into `_data/annual_meeting/faqs/`, then run:

```bash
python3 scripts/faqs/seed_and_convert.py
```

## Sheets

### Spokes
`spoke_id,spoke_sort,spoke_label,hub_blurb,seo_title,seo_meta_description,seo_h1,canonical_path,date_modified,robots,status,cross_banner,cross_banner_href`

### Groups
`spoke_id,group_id,group_label,group_sort,group_intro`

### Items
`spoke_id,group_id,item_id,question,answer_text,answer_html,item_sort,related_spoke_id,related_group_id,status,notes,primary_query`

## SME rules
- Keep questions in interrogative form.
- Prefer `answer_text` (plain). Use `answer_html` only for tables/complex markup.
- Do not change `item_id` after publish (deep links).
- Set `status` to `ready` when Web Production may publish.

Full workflow: [README.md](./README.md) · Hygiene flags: [CONTENT_FLAGS.md](./CONTENT_FLAGS.md)

Seeded CSVs in this folder are the current demo source of truth until an `.xlsx` is circulated to Robin/Rebekah.

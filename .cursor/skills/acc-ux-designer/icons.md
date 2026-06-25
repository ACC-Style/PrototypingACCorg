# ACC Icon Dictionary (Font Awesome)

Official reference: [ACC Icon Dictionary](https://acc-style.github.io/IconDictionary/)

Font Awesome is ACC's shared **visual language** for concepts. Before picking an icon, **look up the concept** in the dictionary — do not invent arbitrary `fa-*` choices.

Loaded via `_includes/arches-head.html`:

```
https://pro.fontawesome.com/releases/v5.15.1/css/all.css
```

## Markup conventions

```html
<!-- Default UI icon — regular weight -->
<i class="far fa-calendar-alt p-r_3" aria-hidden="true"></i>

<!-- Solid — nav home, stacked base layers -->
<i class="fas fa-home" aria-hidden="true"></i>

<!-- Brand / social -->
<i class="fab fa-linkedin" aria-hidden="true"></i>

<!-- Topic tile / list icon with accent color -->
<i class="c_accent-n1 far fa-book-medical font_4 m-r_3" aria-hidden="true"></i>

<!-- Action affordance on link (not decorative concept) -->
Learn More<i class="fas fa-arrow-right p-x_3" aria-hidden="true"></i>
```

| Rule | Detail |
|------|--------|
| **Weight** | `far` (regular) for most UI concepts; `fas` when dictionary specifies solid |
| **Decorative** | `aria-hidden="true"` when icon repeats adjacent text |
| **Spacing** | `p-r_3`, `p-x_3`, `m-r_3` between icon and label |
| **Color** | `c_accent-n1` on topic/list icons; inherit link color on inline actions |
| **Stacked** | **Sparingly** — product concepts only; copy markup from dictionary |
| **Illustrations** | Icons >150px use illustration assets per dictionary — not scaled FA |

## Dictionary usage rules

- **External link** — append `far fa-external-link` to links leaving ACC domain
- **Download** — `far fa-arrow-to-bottom` (or `fa-file-pdf`) must pair with file name or type
- **Upload** — `far fa-arrow-to-top` must pair with expected asset type
- **Add** — `far fa-plus` with "Add [item]" button copy
- **Remove/Cancel** — `far fa-times` with Cancel or "Remove [item]"
- **Lock** — `far fa-lock` after text for gated content
- **List bullets** — browser bullets; no custom bullet icon

## Quick reference — common concepts

Look up full synonyms, stacked variants, and usage notes in the [dictionary](https://acc-style.github.io/IconDictionary/).

### Navigation & chrome

| Concept | Icon |
|---------|------|
| Home | `fas fa-home` |
| Search | `far fa-search` |
| Login | `far fa-sign-in` |
| Logout | `far fa-sign-out` |
| My Account | `far fa-user-circle` |
| Cart | `far fa-shopping-cart` |
| Notification | `far fa-bell` |
| External link | `far fa-external-link` |
| Expand / Collapse | `far fa-plus` / `far fa-minus` |
| More / Less text | `far fa-chevron-down` / `far fa-chevron-up` (see dictionary) |
| Filter | `far fa-filter` |
| Sort | `far fa-sort` |
| Tooltip / help | `far fa-question` |

### Events & time

| Concept | Icon |
|---------|------|
| Event / date | `far fa-calendar-alt` |
| Meetings | `far fa-calendar-day` |
| Time | `far fa-clock` |
| Live stream | `far fa-video` |
| Webinar | `far fa-desktop-alt` |
| Meeting on Demand | stacked `fa-calendar` + `fa-play-circle` |
| On Demand | stacked `fa-rectangle-wide` + `fa-play-circle` |

### Education & CME

| Concept | Icon |
|---------|------|
| Educational activities | `far fa-university` |
| Self-paced learning | `far fa-book-reader` |
| Online course | stacked `fa-browser` + `fa-graduation-cap` |
| Micro learning | stacked `fa-search` + `fa-book-reader` |
| Credit / certificate | `far fa-file-certificate` |
| Certified education | stacked `fa-badge` + `fa-book-reader` |
| Accreditation | `far fa-award` |
| Award (trophy) | `far fa-trophy` |
| Expert analysis | `far fa-user-chart` |
| Patient case quiz | `far fa-notes-medical` |

### Clinical & guidelines content

| Concept | Icon |
|---------|------|
| Guideline | `far fa-book-medical` |
| Guideline hub | `fab fa-hubspot` |
| Decision aid | `far fa-sitemap` |
| Discussion guide | `far fa-user-md-chat` |
| Action plan | `far fa-file-signature` |
| Fact sheet | `far fa-ballot-check` |
| Infographic | `far fa-file-chart-pie` |
| Clinical toolkit | stacked `fa-box` + `fa-tools` |
| Clinical trials | `far fa-microscope` |
| Registry (NCDR) | stacked `fa-file` + `fa-cog` |
| Risk calculator | `far fa-calculator` |
| Career & practice resources | stacked `fa-clipboard` + `fa-tasks` |
| Resources (CV) | stacked `fa-clipboard` + `fa-heart` |
| Patient resources | stacked `fa-clipboard` + `fa-user` |

### Content types & media

| Concept | Icon |
|---------|------|
| Generic article | `far fa-file-medical-alt` |
| News article | `far fa-newspaper` |
| Section news | `far fa-scroll` |
| Announcement | `far fa-megaphone` |
| Featured | `far fa-star` |
| Editor's pick | `far fa-thumbs-up` |
| PDF | `far fa-file-pdf` |
| Audio / podcast | `far fa-headphones` / `far fa-podcast` |
| Video | `far fa-photo-video` |
| Image | `far fa-image` |
| Slideshow | `fab fa-slideshare` |
| JACC CME/MOC | `far fa-book-open` |
| Worksheet | `far fa-tasks` |
| Bookmark / save | `far fa-bookmark` |

### People & access

| Concept | Icon |
|---------|------|
| User | `far fa-user` |
| Users / members | `far fa-users` |
| Editor in chief | `far fa-users-medical` |
| Expert panel | `far fa-users-class` |
| Patient story | `far fa-address-card` |
| Lock (gated) | `far fa-lock` |
| Brute force lock | stacked `fa-lock` + `fa-ban` |
| Registered / purchased | `far fa-check-circle` |

### Actions

| Concept | Icon |
|---------|------|
| Download | `far fa-arrow-to-bottom` |
| Upload | `far fa-arrow-to-top` |
| Print | `far fa-print` |
| Share | `far fa-share-square` |
| Add | `far fa-plus` |
| Remove / cancel | `far fa-times` |

### Social

| Network | Icon |
|---------|------|
| Facebook | `fab fa-facebook-square` |
| Twitter | `fab fa-twitter-square` |
| LinkedIn | `fab fa-linkedin` |
| YouTube | `fab fa-youtube-square` |
| Instagram | `fab fa-instagram-square` |
| RSS | `far fa-rss-square` |

## Stacked icons

Reserved for **product-level concepts** (Online Course, Registry, On Demand, etc.). Copy the full `fa-stack` markup from the dictionary — do not improvise stack composition.

```html
<span class="fa-stack">
  <i class="fa-browser far fa-stack-2x"></i>
  <i style="top: 7%;font-size: 90%;" class="fa-graduation-cap fas c_primary fa-stack-1x"></i>
</span>
```

## When the dictionary has no entry

1. Search [Icon Dictionary](https://acc-style.github.io/IconDictionary/) by synonym
2. Check nearest prototype in `_collections/` for established usage
3. Prefer a **simple `far` icon** over stacked or novel choices
4. Flag missing entry for the design team — dictionary is actively maintained

## Anti-patterns

- Random `fa-heart` / `fa-heartbeat` for topics when dictionary defines a closer concept
- Solid `fas` everywhere — dictionary defaults to `far` for UI
- Stacked icons for simple list decoration
- Icon with no semantic match in dictionary
- Forgetting `fa-external-link` on off-domain links
- Decorative icons without `aria-hidden="true"`

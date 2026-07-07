# Imagery

ACC prototypes use images **sparingly**. Graphics are hard to source and maintain; reach for layout, typography, and Arches utilities before adding art.

## When images earn a place

| Purpose | Examples |
|---------|----------|
| **Branding** | Domain hero splash, product artwork, logo lockups |
| **Audience grounding** | Clinical context, conference setting, specialty imagery |
| **Humanization** | Faculty, members, patients (with purposeful alt text) |

If copy is the message, use HTML — not a graphic.

## Anti-pattern: text baked into images

**Do not** use images that contain headlines, body copy, CTAs, dates, or labels rendered as pixels.

This pattern is still common on legacy ACC.org. It is an active anti-pattern for new work:

| Problem | Why it matters |
|---------|----------------|
| **SEO** | Search engines cannot index text trapped in raster/vector art |
| **Accessibility** | Screen readers get poor or missing content; users cannot resize or reflow text |
| **Responsive design** | Text does not scale with viewport or user font settings; teams ship multiple fixed crops instead of one flexible layout |

**Reject or refactor** deliverables that rely on:

- Hero banners with titles or taglines burned in
- Infographic-style panels where paragraphs live inside the PNG/JPG
- “Downloadable” tiles whose only readable content is inside the image
- Product or event cards where the card title exists only in artwork

When reviewing legacy pages, prefer refactoring to HTML chunks ([refactor](../refactor/SKILL.md)) rather than recreating the same text-in-image layout.

## Preferred pattern: HTML layered on imagery

Separate **visual atmosphere** (photo, gradient, brand art) from **readable content** (real headings, links, buttons).

| Pattern | Reference |
|---------|-----------|
| Hero title + CTA over photo | [heroes.md](heroes.md) — `grid-template="hero-image-cta"`, `hero-title`, `cta-callout`, `c_white-8` |
| Photo beside copy | `_collections/_ui_gold_standard/photo-text-lockup.html` |
| Text on tinted overlay | [cross-domain-branding.md](cross-domain-branding.md) — `bg_black-4 bg-blend_multiply` + HTML type |
| Responsive art only | `<picture data-item="responsive-hero-image">` — breakpoints swap **image**, not text |

```html
<!-- Good: image is atmosphere; copy is HTML -->
<div grid-template="hero-image-cta" id="hero" class="font_3:lg font_2:md font_1">
  <div grid-area="background">
    <picture data-item="responsive-hero-image">
      <img alt="" src="…" class="flex_100">
    </picture>
  </div>
  <div grid-area="title">
    <h1 data-item="hero-title" class="c_white"><span class="text">Real</span> <span class="text">heading</span></h1>
  </div>
  <div grid-area="cta">
    <div data-item="cta-callout" class="c_white">
      <p data-item="cta-description">Supporting copy crawlers and assistive tech can read.</p>
      <a class="br_white-3 btn btn-primary c_white" href="…">Start here</a>
    </div>
  </div>
</div>
```

```html
<!-- Bad: do not ship — headline exists only inside the image file -->
<img src="hero-with-title-and-cta-baked-in.jpg" alt="Join ACC Today — Become a member">
```

## `alt` text discipline

| Image role | `alt` |
|------------|-------|
| Decorative atmosphere (hero photo, texture) | `alt=""` when adjacent HTML carries the message |
| Informative (person, diagram, meaningful scene) | Concise description of what the image adds — not a transcript of overlaid HTML |
| Never | Long `alt` strings that duplicate visible headings beside or on top of the image |

## Checklist

```
- [ ] No headlines, body copy, or CTAs exist only inside image files
- [ ] Hero/product art uses HTML overlays or adjacent copy blocks
- [ ] Decorative images use empty alt; informative images have purposeful alt
- [ ] Image is justified (branding, grounding, or humanization) — not a substitute for layout
- [ ] `<picture>` / responsive srcsets change art, not text crops
```

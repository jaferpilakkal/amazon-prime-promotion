# SEO Optimization & Favicon Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the Prime Perks Guide website into a fully SEO-optimized, search-engine-ready platform with production-grade metadata, Open Graph cards, Twitter cards, rich JSON-LD schema (FAQPage, WebSite, Organization, BlogPosting, Breadcrumbs), XML sitemap, robots.txt, and a custom branded SVG/PNG/ICO favicon system.

**Architecture:** A static-first SEO architecture comprising:
1. Multi-resolution favicon package (`favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `site.webmanifest`) matching the Prime Perks dark/cyan/amber brand.
2. High-resolution Open Graph social sharing image (`images/og-share.png`, 1200x630).
3. Search crawler directives via `robots.txt` and `sitemap.xml` covering all 9 site URLs.
4. Comprehensive `<head>` SEO suite on all 9 HTML documents (canonical, Open Graph, Twitter Cards, robots directives, mobile theme-color).
5. Rich JSON-LD structured data on all pages for Google SERP features (FAQ accordions, article rich cards, site search/organization).

**Tech Stack:** Semantic HTML5, SVG, Python (Pillow for crisp icon rasterization and ICO generation), JSON-LD (Schema.org), XML (Sitemaps 0.9).

**Spec:** [docs/superpowers/specs/2026-10-05-amazon-prime-promotion-design.md](file:///c:/Users/jafer/OneDrive/Desktop/amazon%20promotion/docs/superpowers/specs/2026-10-05-amazon-prime-promotion-design.md)

## Global Constraints

- Domain canonical base: `https://primeperksguide.com`
- Brand colors: Primary Dark `#0A1118`, Prime Cyan `#00A8E1`, Amazon Amber `#FF9900`, Text `#F1F5F9`.
- Zero broken links or external runtime dependencies.
- Zero placeholder or "TODO" values anywhere in code or metadata.
- All JSON-LD structured data must strictly validate as compliant JSON.
- All 9 pages must receive identical favicon and meta infrastructure with tailored page-level titles, descriptions, canonicals, and schemas.

---

### Task 1: Generate Branded Favicon Suite & Open Graph Social Banner

**Files:**
- Create: `favicon.svg`
- Create: `scripts/generate_favicons.py`
- Create: `favicon.ico` (multi-resolution 16x16, 32x32, 48x48)
- Create: `favicon-16x16.png`
- Create: `favicon-32x32.png`
- Create: `apple-touch-icon.png` (180x180)
- Create: `android-chrome-192x192.png`
- Create: `android-chrome-512x512.png`
- Create: `site.webmanifest`
- Create: `images/og-share.png` (1200x630 social share card)

**Interfaces:**
- Produces: Vector and raster icons referenced by `<link rel="icon">`, `<link rel="apple-touch-icon">`, `<link rel="manifest">`, and `<meta property="og:image">`.

- [ ] **Step 1: Create `favicon.svg` with modern Prime Perks Guide branding**

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E1A27" />
      <stop offset="100%" stop-color="#0A1118" />
    </linearGradient>
    <linearGradient id="primeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00C8FF" />
      <stop offset="100%" stop-color="#00A8E1" />
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFA826" />
      <stop offset="100%" stop-color="#FF9900" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background squircle with subtle border -->
  <rect x="16" y="16" width="480" height="480" rx="112" fill="url(#bgGrad)" stroke="#00A8E1" stroke-width="8" stroke-opacity="0.3" />

  <!-- Distinctive Stylized 'P' Monogram -->
  <path d="M 160 120 L 290 120 C 356 120 400 160 400 220 C 400 280 356 320 290 320 L 228 320 L 228 392 C 228 405 217 416 204 416 L 184 416 C 171 416 160 405 160 392 Z" fill="url(#primeGrad)" />
  <path d="M 228 184 L 285 184 C 318 184 336 200 336 220 C 336 240 318 256 285 256 L 228 256 Z" fill="#0A1118" />

  <!-- Dynamic Prime Arc Smile in Vibrant Amber -->
  <path d="M 148 376 C 220 440 330 436 396 364" fill="none" stroke="url(#amberGrad)" stroke-width="26" stroke-linecap="round" filter="url(#glow)" />
  <!-- Arrow head at the end of the arc -->
  <path d="M 402 360 L 366 358 L 388 388 Z" fill="url(#amberGrad)" />

  <!-- Top-right perks spark -->
  <circle cx="390" cy="130" r="14" fill="#FFA826" filter="url(#glow)" />
</svg>
```

- [ ] **Step 2: Create Python script `scripts/generate_favicons.py` to render PNGs, ICO, and OG banner**

Write `scripts/generate_favicons.py` using Pillow (`PIL`) to render:
- `favicon-16x16.png`
- `favicon-32x32.png`
- `favicon.ico` containing sizes (16, 32, 48)
- `apple-touch-icon.png` (180x180)
- `android-chrome-192x192.png`
- `android-chrome-512x512.png`
- `images/og-share.png` (1200x630 pixel social banner with dark background, glowing gradients, brand logo, headline "Amazon Prime Perks & Special Offers Guide (2026)", value badges, and domain url)

- [ ] **Step 3: Run the script to generate all icon files and verify their existence**

Run `python scripts/generate_favicons.py` and verify all icon files are generated and non-empty.

- [ ] **Step 4: Create `site.webmanifest`**

Create `site.webmanifest` with full metadata:
```json
{
  "name": "Prime Perks Guide",
  "short_name": "Prime Perks",
  "description": "Independent guide to Amazon Prime benefits, 30-day trials, student discounts, and member savings.",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0A1118",
  "theme_color": "#0A1118",
  "icons": [
    {
      "src": "/favicon-16x16.png",
      "sizes": "16x16",
      "type": "image/png"
    },
    {
      "src": "/favicon-32x32.png",
      "sizes": "32x32",
      "type": "image/png"
    },
    {
      "src": "/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    },
    {
      "src": "/apple-touch-icon.png",
      "sizes": "180x180",
      "type": "image/png"
    }
  ]
}
```

---

### Task 2: Create Search Discovery Infrastructure (`robots.txt` & `sitemap.xml`)

**Files:**
- Create: `robots.txt`
- Create: `sitemap.xml`

**Interfaces:**
- Consumes: Site URL structure
- Produces: Standardized crawler directives and indexable URL list for Googlebot, Bingbot, and search indexers.

- [ ] **Step 1: Create `robots.txt`**

```txt
User-agent: *
Allow: /

Sitemap: https://primeperksguide.com/sitemap.xml
```

- [ ] **Step 2: Create `sitemap.xml` with all 9 site URLs**

Include standard `urlset` with `loc`, `lastmod`, `changefreq`, and `priority`:
- `/` (priority 1.0, daily)
- `/blog.html` (priority 0.9, weekly)
- `/blog-prime-worth-it-2026.html` (priority 0.8, weekly)
- `/blog-prime-discount-young-adult-access.html` (priority 0.8, weekly)
- `/blog-audible-free-trial-guide.html` (priority 0.8, weekly)
- `/contact.html` (priority 0.6, monthly)
- `/disclosure.html` (priority 0.5, monthly)
- `/privacy.html` (priority 0.5, monthly)
- `/terms.html` (priority 0.5, monthly)

---

### Task 3: Optimize Core Landing Page (`index.html`)

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: Favicon assets, `images/og-share.png`, site metadata, FAQ content.
- Produces: Fully SEO-optimized `<head>` with canonical link, Open Graph tags, Twitter card tags, robots directives, theme color, complete favicon suite, and rich JSON-LD structured data (`WebSite`, `Organization`, `FAQPage`, and `ItemList`).

- [ ] **Step 1: Update `index.html` head section with canonical, favicon suite, OG tags, Twitter tags, and theme-color**

Add:
- `<link rel="canonical" href="https://primeperksguide.com/">`
- `<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">`
- `<meta name="theme-color" content="#0A1118">`
- Favicons:
  - `<link rel="icon" type="image/svg+xml" href="favicon.svg">`
  - `<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">`
  - `<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">`
  - `<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">`
  - `<link rel="manifest" href="site.webmanifest">`
- Open Graph tags:
  - `og:site_name`: Prime Perks Guide
  - `og:title`: Amazon Prime Perks & Special Offers Guide (2026) | 30-Day Free Trials
  - `og:description`: Complete independent guide to Amazon Prime membership benefits, 30-day free trials, student & young adult discounts, Audible credits, and member savings.
  - `og:url`: https://primeperksguide.com/
  - `og:type`: website
  - `og:image`: https://primeperksguide.com/images/og-share.png
  - `og:image:width`: 1200
  - `og:image:height`: 630
  - `og:locale`: en_US
- Twitter Cards:
  - `twitter:card`: summary_large_image
  - `twitter:title`: Amazon Prime Perks & Special Offers Guide (2026)
  - `twitter:description`: Complete independent guide to Amazon Prime benefits, 30-day free trials, student discounts, and member savings.
  - `twitter:image`: https://primeperksguide.com/images/og-share.png

- [ ] **Step 2: Add comprehensive JSON-LD Structured Data to `index.html`**

Inject JSON-LD schemas:
1. `WebSite` with SearchAction
2. `Organization` with logo, name, and URL
3. `FAQPage` featuring all 6 FAQs from the accordion (trial rules, cancellation, young adult requirements, Prime Access verification, etc.) for Google Rich Snippets
4. `ItemList` representing the curated Prime promotional programs

---

### Task 4: Optimize Blog Hub & Article Pages (`blog.html`, 3 articles)

**Files:**
- Modify: `blog.html`
- Modify: `blog-prime-worth-it-2026.html`
- Modify: `blog-prime-discount-young-adult-access.html`
- Modify: `blog-audible-free-trial-guide.html`

**Interfaces:**
- Consumes: Favicon suite, article metadata, breadcrumb structure.
- Produces: Removal of placeholder `🌿` leaf emoji favicon; insertion of proper favicon suite; addition of Open Graph, Twitter cards, robots directives, theme color; and enriched JSON-LD structured data with BreadcrumbList schema.

- [ ] **Step 1: Update `blog.html`**
- Replace emoji favicon with full branded favicon suite (`favicon.svg`, `favicon-32x32.png`, `apple-touch-icon.png`, `site.webmanifest`).
- Add Open Graph & Twitter card tags pointing to `images/og-share.png`.
- Add robots tag (`index, follow, max-image-preview:large`).
- Add BreadcrumbList schema (`Home > Buying Guides`).

- [ ] **Step 2: Update `blog-prime-worth-it-2026.html`**
- Replace emoji favicon with branded favicon suite and `site.webmanifest`.
- Add Open Graph and Twitter Card tags pointing to `https://primeperksguide.com/images/prime-worth-it-guide.jpg`.
- Add robots tag (`index, follow, max-image-preview:large`).
- Enhance JSON-LD `BlogPosting` with BreadcrumbList (`Home > Guides > Is Prime Worth It in 2026?`), word count, and article body summary.

- [ ] **Step 3: Update `blog-prime-discount-young-adult-access.html`**
- Replace emoji favicon with branded favicon suite and `site.webmanifest`.
- Add Open Graph and Twitter Card tags pointing to `https://primeperksguide.com/images/young-adult-access-guide.jpg`.
- Add robots tag (`index, follow, max-image-preview:large`).
- Enhance JSON-LD `BlogPosting` with BreadcrumbList (`Home > Guides > 50% Off Young Adult & Prime Access Guide`).

- [ ] **Step 4: Update `blog-audible-free-trial-guide.html`**
- Replace emoji favicon with branded favicon suite and `site.webmanifest`.
- Add Open Graph and Twitter Card tags pointing to `https://primeperksguide.com/images/audible-trial-guide.jpg`.
- Add robots tag (`index, follow, max-image-preview:large`).
- Enhance JSON-LD `BlogPosting` with BreadcrumbList (`Home > Guides > Audible 30-Day Free Trial Guide`).

---

### Task 5: Optimize Compliance & Contact Pages (`contact.html`, `disclosure.html`, `privacy.html`, `terms.html`)

**Files:**
- Modify: `contact.html`
- Modify: `disclosure.html`
- Modify: `privacy.html`
- Modify: `terms.html`

**Interfaces:**
- Consumes: Favicon suite, site metadata.
- Produces: Proper canonical links, favicon suite, Open Graph tags, Twitter tags, robots directives, and WebPage / ContactPage JSON-LD schemas.

- [ ] **Step 1: Update `contact.html`**
- Add canonical link `https://primeperksguide.com/contact.html`.
- Add favicon suite and manifest.
- Add robots tag, Open Graph tags, Twitter card tags.
- Add `ContactPage` JSON-LD schema with publisher contact info.

- [ ] **Step 2: Update `disclosure.html`**
- Add canonical link `https://primeperksguide.com/disclosure.html`.
- Add favicon suite and manifest.
- Add robots tag, Open Graph tags, Twitter card tags.
- Add `WebPage` JSON-LD schema.

- [ ] **Step 3: Update `privacy.html`**
- Add canonical link `https://primeperksguide.com/privacy.html`.
- Add favicon suite and manifest.
- Add robots tag, Open Graph tags, Twitter card tags.
- Add `WebPage` JSON-LD schema.

- [ ] **Step 4: Update `terms.html`**
- Add canonical link `https://primeperksguide.com/terms.html`.
- Add favicon suite and manifest.
- Add robots tag, Open Graph tags, Twitter card tags.
- Add `WebPage` JSON-LD schema.

---

### Task 6: Audit, Validation, and Testing Suite

**Files:**
- Create: `scripts/verify_seo.py`
- Test: All 9 HTML files, `robots.txt`, `sitemap.xml`, favicon assets

**Interfaces:**
- Consumes: Generated HTML files, icon files, sitemap.
- Produces: Automated report verifying that 100% of pages contain:
  1. Valid Title tag
  2. Valid Meta Description
  3. Canonical link matching file route
  4. Favicon links (`favicon.svg`, `favicon-32x32.png`, `apple-touch-icon.png`)
  5. Open Graph tags (`og:title`, `og:description`, `og:image`, `og:url`)
  6. Twitter Card tags
  7. Valid, error-free JSON-LD schemas (parsed and verified with `json.loads`)
  8. Exactly one `<h1>` per page
  9. Zero placeholder emoji or missing resources

- [ ] **Step 1: Write and run `scripts/verify_seo.py`**
- [ ] **Step 2: Confirm all 9 pages pass all SEO criteria with zero warnings or errors**

---

# Design Specification: Amazon Prime Promotional Landing Page & Compliance Suite

**Date:** 2026-10-05  
**Project:** Amazon Prime Ecosystem Promotional Website  
**Status:** Approved  

---

## 1. Project Overview & Objectives
A high-converting, aesthetically premium one-page website promoting the Amazon Prime ecosystem and specialized Amazon Associates programs (Audible, Kindle Unlimited, Prime Gaming, Young Adult, Prime Access, and Amazon Business). The site is engineered to pass Amazon Associates manual website compliance audits on the first submission with full FTC disclosure and legal documentation.

### Core Goals:
1. **High Visual Impact:** Sleek Cinematic Dark Mode (`#0A1118`, Prime Cyan `#00A8E1`, Amazon Amber `#FF9900`) inspired by Prime Video and modern tech landing pages.
2. **Associates Compliance:** Prominent top disclosure banner, legal footer disclaimers, and dedicated standalone compliance pages (`disclosure.html`, `privacy.html`, `terms.html`, `contact.html`).
3. **Offer Coverage:** Exact alignment with the provided Amazon Associates promotional campaigns with **zero** mention of publisher bounty rates.
4. **Interactive Engagement:** Category filter tabs, real-time annual savings calculator, pricing frequency toggle, and FAQ accordion.
5. **Pragmatic Architecture:** Zero-build vanilla web stack (HTML5, Vanilla CSS, Vanilla JS) for immediate deployment.

---

## 2. File & Directory Structure

```text
/
├── index.html              # Main promotional landing page & offers hub
├── disclosure.html         # Amazon Associates & FTC affiliate disclosure
├── privacy.html            # Comprehensive privacy policy (cookies, tracking, CCPA/GDPR)
├── terms.html              # Terms of service, pricing disclaimer, trademarks
├── contact.html            # Publisher info, support inquiry form & about statement
├── css/
│   └── style.css           # Design tokens, reset, typography, layout, animations
├── js/
│   ├── config.js           # Centralized affiliate tag configuration
│   └── main.js             # Filter tabs, savings calculator, plan toggle, mobile nav
└── assets/                 # SVGs and brand iconography
```

---

## 3. Targeted Offers & Link Specifications

All outbound affiliate links include `target="_blank" rel="nofollow sponsored noopener"` and automatically append the associate tag configured in `js/config.js`.

| Category | Offer Name | Target URL | Highlight / Key Value Prop |
| :--- | :--- | :--- | :--- |
| **Prime Core** | Prime 30-Day Free Trial | `https://www.amazon.com/prime` | 30 days free, fast shipping, Prime Video, ad-free music |
| **Prime Core** | Prime Annual & Monthly | `https://www.amazon.com/prime` | $139/yr ($40+ savings) or $14.99/mo |
| **Student / YA** | Prime for Young Adults | `https://www.amazon.com/joinyoungadult` | 6-month trial, 50% off ($7.49/mo), for ages 18–24 & students |
| **Assistance** | Prime Access | `https://amazon.com/qualify` | 50%+ discount ($6.99/mo) for SNAP/EBT, Medicaid, etc. |
| **Gaming** | Prime Gaming & Luna | `https://amazon.com/playluna` | Luna cloud gaming, free monthly Twitch sub, exclusive loot |
| **Audiobooks** | Audible Standard Trial | `https://www.amazon.com/hz/audible/mlp` | 30-day free trial with 1 audiobook credit |
| **Audiobooks** | Audible Premium Plus (Annual) | `https://www.amazon.com/hz/audible/mlp/membership/premiumplus/annual` | 12 credits upfront + full audio catalog access |
| **Audiobooks** | Audible Premium Plus (Monthly) | `https://www.amazon.com/hz/audible/mlp/membership/premiumplus/monthly` | 1 credit/month + unlimited Plus catalog |
| **Audiobooks** | Audible 12-Month Gift | `https://www.amazon.com/hz/audible/gift-membership-detail` | 12-month prepaid gift plan for any reader |
| **Reading** | Kindle Unlimited (24-Month) | `https://www.amazon.com/gp/kindle/ku/gift_landing` | Over 4 million titles, audiobooks, and magazines |
| **Business** | Amazon Business Account | `https://business.amazon.com/` | Free multi-user procurement, bulk quantity discounts |

*Note: No publisher dollar bounty amounts appear anywhere on the site or in source code.*

---

## 4. Page Breakdown & Components

### A. Main Page (`index.html`)
1. **Top Disclosure Bar:** Fixed/sticky subtle notice: *"Independent Guide: As an Amazon Associate, we earn from qualifying purchases through our links at no extra cost to you. [Learn More](disclosure.html)"*
2. **Navigation Bar:** Logo (Prime Perks Guide), smooth-scroll links (*Benefits, Special Offers, Calculator, Pricing, FAQ*), and primary CTA button (*"Start 30-Day Trial"*).
3. **Hero Section:**
   - Badge: *"Updated for 2026 • 30-Day Free Trial Available"*
   - Headline: *"Unlock the Best of Shopping, Entertainment, and Everyday Savings"*
   - Subhead: *"Fast, free delivery on millions of items, exclusive award-winning movies and TV shows, ad-free music, and member-only deals all in one subscription."*
   - Dual CTAs: Primary *"Start 30-Day Free Trial"* + Secondary *"Explore All Offers"*
   - Trust Badges: Fast 1-Day Delivery, 100M+ Songs, 4K HDR Originals, Cancel Anytime.
4. **Core Benefits Pillar Grid (The 4 Pillars):**
   - *Fast & Free Delivery:* Same-Day & One-Day shipping, grocery delivery via Amazon Fresh.
   - *Prime Video & Luna Gaming:* Award-winning originals, live sports, and cloud gaming.
   - *Music & Reading:* 100M songs ad-free, rotating digital magazines & Kindle titles.
   - *Exclusive Savings & Prime Day:* Early access to Lightning Deals and annual Prime Day savings.
5. **Offers Hub (Category Filtered Grid):**
   - Filter Buttons: *All Offers, Prime Memberships, Young Adults & Students, Audiobooks & Reading, Gaming, Business*.
   - Dynamic rendering/filtering of all 11 Associate programs with badges, bullet points, and high-contrast CTA buttons.
6. **Interactive Prime Value & Savings Calculator:**
   - Sliders:
     - Monthly Amazon Deliveries (0 to 15 orders)
     - Weekly Video Streaming Hours (0 to 25 hours)
     - Monthly Books / Audiobooks (0 to 6 titles)
   - Dynamic real-time calculation of estimated annual value vs. $139 Prime cost.
7. **Membership Pricing & Comparison:**
   - Toggle: *Billed Annually ($139/yr)* vs. *Billed Monthly ($14.99/mo)*.
   - Comparative Cards: Standard Prime, Prime Young Adult ($7.49/mo), and Prime Access ($6.99/mo).
8. **Interactive FAQ Accordion:**
   - Trial cancellation rules, payment verification, Young Adult age requirements, EBT eligibility.
9. **Amazon Associates Compliant Footer:**
   - Amazon Associate Statement: *"As an Amazon Associate, we earn from qualifying purchases."*
   - Trademark Attribution: *"Amazon, Prime, Audible, Kindle, and all related logos are trademarks of Amazon.com, Inc. or its affiliates."*
   - Quick Links: Home, Benefits, Offers, Disclosure, Privacy Policy, Terms of Service, Contact Us.

### B. Legal & Compliance Pages
- **`disclosure.html`**: Complete FTC compliance guide, explaining affiliate relationships, commission structures (at $0 extra cost to visitors), pricing volatility disclaimer, and editorial independence.
- **`privacy.html`**: Cookies policy (detailing Amazon 24-hour cookie tracking), analytical data logging, user data rights (GDPR/CCPA), third-party affiliate link clauses.
- **`terms.html`**: Terms of use, intellectual property protection, warranty disclaimers, external links liability waiver.
- **`contact.html`**: Publisher transparency statement, contact inquiry form, direct email contact, and physical/mailing address placeholder to satisfy Amazon reviewer scrutiny.

---

## 5. Technical Implementation Details

### Configuration (`js/config.js`)
```javascript
const SITE_CONFIG = {
  associateTag: 'primeperks-20', // User replaces with their real associate tag
  siteName: 'Prime Perks Guide',
  contactEmail: 'support@savvyfindsonline.com',
  enableAffiliateTagging: true
};
```
A helper function `getAffiliateUrl(baseUrl)` appends `?tag=${SITE_CONFIG.associateTag}` cleanly.

### Visual Styling Tokens (`css/style.css`)
- **Backgrounds:** `--bg-dark: #0A1118`, `--bg-surface: #101F30`, `--bg-card: #15263C`
- **Brand Colors:** `--prime-blue: #00A8E1`, `--prime-cyan-glow: rgba(0, 168, 225, 0.35)`, `--amazon-amber: #FF9900`
- **Text:** `--text-main: #F2F5F8`, `--text-muted: #94A3B8`
- **Fonts:** Display: `'Outfit', sans-serif`; Body: `'Inter', sans-serif`
- **Transitions:** Standard cubic bezier `ease-out`, 0.25s micro-transitions on interactive states.

---

## 6. Verification & Launch Checklist
1. All 11 Associate programs functional with valid Amazon URLs.
2. FTC & Amazon Operating Agreement disclosure clearly visible above the fold and in the footer.
3. All legal pages (`disclosure.html`, `privacy.html`, `terms.html`, `contact.html`) fully written with zero placeholder text.
4. Mobile responsiveness tested across standard breakpoints (375px, 768px, 1200px).
5. Zero build step: files can be immediately viewed locally or deployed to any static host.

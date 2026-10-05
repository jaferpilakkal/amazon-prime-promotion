# Amazon Prime Promotional Landing Page & Compliance Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a sleek, cinematic, high-converting one-page website promoting the Amazon Prime ecosystem along with targeted Amazon Associates campaigns (Audible, Kindle Unlimited, Prime Gaming, Young Adult, Prime Access, Amazon Business) and a complete legal compliance suite for Amazon approval.

**Architecture:** Pure modular vanilla web architecture (`index.html`, `disclosure.html`, `privacy.html`, `terms.html`, `contact.html`, `css/style.css`, `js/config.js`, `js/main.js`). Outbound links automatically map through a centralized configuration module.

**Tech Stack:** Semantic HTML5, Vanilla CSS3 (custom properties, glassmorphism, responsive grid/flexbox), Vanilla ES6 JavaScript (zero build tools, zero dependencies), Google Fonts (`Outfit`, `Inter`).

**Spec:** [docs/superpowers/specs/2026-10-05-amazon-prime-promotion-design.md](file:///c:/Users/jafer/OneDrive/Desktop/amazon%20promotion/docs/superpowers/specs/2026-10-05-amazon-prime-promotion-design.md)

## Global Constraints

- Zero build steps or npm compilation required; openable directly or via static web server.
- No publisher dollar bounty amounts ($40, $25, etc.) in text, attributes, or code comments.
- Amazon Operating Agreement compliant disclosure visible at top banner and in footer.
- All outbound affiliate links must use `target="_blank" rel="nofollow sponsored noopener"`.
- Clean semantic code with no placeholders or "TODO" items.

---

### Task 1: Design System & Global Styles (`css/style.css`)

**Files:**
- Create: `css/style.css`
- Test: Verification via CSS syntax validation / inspection

**Interfaces:**
- Consumes: Google Fonts (`Outfit:wght@400;500;600;700;800`, `Inter:wght@300;400;500;600;700`)
- Produces: Global CSS variables (`--bg-dark`, `--prime-blue`, `--amazon-amber`, etc.), reset, utility classes, grid systems, card styles, and animations.

- [ ] **Step 1: Write `css/style.css` containing design tokens, reset, typography, header, hero, cards, and modal styles**

```css
/* css/style.css */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap');

:root {
  --bg-primary: #0A1118;
  --bg-surface: #0E1A27;
  --bg-card: #132438;
  --bg-card-hover: #192F4A;
  --prime-blue: #00A8E1;
  --prime-blue-hover: #1bb7ee;
  --prime-blue-glow: rgba(0, 168, 225, 0.28);
  --amazon-amber: #FF9900;
  --amazon-amber-glow: rgba(255, 153, 0, 0.25);
  --amazon-gold: #FFA41C;
  --text-main: #F1F5F9;
  --text-muted: #94A3B8;
  --text-subtle: #64748B;
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-active: rgba(0, 168, 225, 0.4);
  --border-amber: rgba(255, 153, 0, 0.35);
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-full: 9999px;
  --container-max: 1200px;
  --font-display: 'Outfit', sans-serif;
  --font-body: 'Inter', sans-serif;
  --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.6);
  --shadow-glow: 0 0 25px var(--prime-blue-glow);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-main);
  font-family: var(--font-body);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

/* Utilities */
.container {
  width: 100%;
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 24px;
}

/* Top Disclosure Banner */
.disclosure-bar {
  background: #080D13;
  border-bottom: 1px solid var(--border-subtle);
  padding: 8px 16px;
  font-size: 0.8125rem;
  color: var(--text-muted);
  text-align: center;
}
.disclosure-bar a {
  color: var(--prime-blue);
  text-decoration: underline;
  margin-left: 6px;
}

/* Header & Nav */
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(10, 17, 24, 0.85);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border-subtle);
  padding: 16px 0;
}
.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.brand-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: var(--font-display);
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--text-main);
  text-decoration: none;
}
.brand-logo .prime-badge {
  background: var(--prime-blue);
  color: #000;
  font-size: 0.75rem;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: var(--radius-sm);
  text-transform: uppercase;
}
.nav-links {
  display: flex;
  align-items: center;
  gap: 28px;
  list-style: none;
}
.nav-links a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.9375rem;
  font-weight: 500;
  transition: color 0.2s ease;
}
.nav-links a:hover {
  color: var(--prime-blue);
}
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: var(--prime-blue);
  color: #05101A;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 0.95rem;
  padding: 11px 22px;
  border-radius: var(--radius-full);
  text-decoration: none;
  box-shadow: 0 4px 18px var(--prime-blue-glow);
  transition: all 0.25s ease;
  border: none;
  cursor: pointer;
}
.btn-primary:hover {
  background: var(--prime-blue-hover);
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(0, 168, 225, 0.45);
}
.btn-amber {
  background: var(--amazon-amber);
  color: #111;
  box-shadow: 0 4px 18px var(--amazon-amber-glow);
}
.btn-amber:hover {
  background: var(--amazon-gold);
  box-shadow: 0 6px 24px rgba(255, 153, 0, 0.45);
}
.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-main);
  border: 1px solid var(--border-subtle);
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 0.95rem;
  padding: 11px 22px;
  border-radius: var(--radius-full);
  text-decoration: none;
  transition: all 0.25s ease;
  cursor: pointer;
}
.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}

/* Hero Section */
.hero-section {
  position: relative;
  padding: 90px 0 70px;
  text-align: center;
  background: radial-gradient(circle at 50% 15%, rgba(0, 168, 225, 0.14) 0%, rgba(10, 17, 24, 0) 70%);
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 16px;
  background: rgba(0, 168, 225, 0.1);
  border: 1px solid rgba(0, 168, 225, 0.25);
  border-radius: var(--radius-full);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--prime-blue);
  margin-bottom: 24px;
}
.hero-title {
  font-family: var(--font-display);
  font-size: clamp(2.3rem, 5vw, 3.8rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.15;
  margin-bottom: 22px;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}
.hero-title .highlight-blue {
  color: var(--prime-blue);
  background: linear-gradient(135deg, #00A8E1 0%, #70D6FF 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-subtitle {
  font-size: clamp(1.05rem, 2vw, 1.25rem);
  color: var(--text-muted);
  max-width: 720px;
  margin: 0 auto 36px;
}
.hero-actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 50px;
}
.hero-trust-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 32px;
  flex-wrap: wrap;
  padding-top: 30px;
  border-top: 1px solid var(--border-subtle);
  max-width: 950px;
  margin: 0 auto;
}
.trust-item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.875rem;
  color: var(--text-muted);
}
.trust-item svg {
  color: var(--prime-blue);
}

/* Pillar Benefits */
.section {
  padding: 85px 0;
}
.section-header {
  text-align: center;
  max-width: 700px;
  margin: 0 auto 55px;
}
.section-tag {
  color: var(--prime-blue);
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 12px;
  display: block;
}
.section-title {
  font-family: var(--font-display);
  font-size: clamp(1.9rem, 3.5vw, 2.7rem);
  font-weight: 700;
  letter-spacing: -0.01em;
  margin-bottom: 16px;
}
.section-desc {
  color: var(--text-muted);
  font-size: 1.05rem;
}
.pillars-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
}
.pillar-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 32px 26px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}
.pillar-card:hover {
  transform: translateY(-5px);
  border-color: var(--border-active);
  background: var(--bg-card-hover);
  box-shadow: var(--shadow-card);
}
.pillar-icon-box {
  width: 54px;
  height: 54px;
  border-radius: var(--radius-sm);
  background: rgba(0, 168, 225, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--prime-blue);
  margin-bottom: 22px;
}
.pillar-title {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 12px;
}
.pillar-text {
  color: var(--text-muted);
  font-size: 0.9375rem;
  line-height: 1.6;
}

/* Offers Hub */
.offers-hub-section {
  background: var(--bg-surface);
  border-top: 1px solid var(--border-subtle);
  border-bottom: 1px solid var(--border-subtle);
}
.filter-tabs {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 45px;
}
.filter-btn {
  background: rgba(255, 255, 255, 0.04);
  color: var(--text-muted);
  border: 1px solid var(--border-subtle);
  padding: 9px 18px;
  border-radius: var(--radius-full);
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}
.filter-btn:hover {
  color: var(--text-main);
  background: rgba(255, 255, 255, 0.08);
}
.filter-btn.active {
  background: var(--prime-blue);
  color: #000;
  border-color: var(--prime-blue);
  font-weight: 700;
}
.offers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 28px;
}
.offer-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 30px;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
  position: relative;
}
.offer-card:hover {
  transform: translateY(-4px);
  border-color: var(--border-active);
  box-shadow: var(--shadow-card);
}
.offer-card.featured {
  border-color: var(--prime-blue);
  background: linear-gradient(180deg, rgba(0, 168, 225, 0.08) 0%, var(--bg-card) 40%);
}
.offer-badge {
  align-self: flex-start;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 18px;
}
.offer-badge.blue {
  background: rgba(0, 168, 225, 0.15);
  color: var(--prime-blue);
  border: 1px solid rgba(0, 168, 225, 0.3);
}
.offer-badge.amber {
  background: rgba(255, 153, 0, 0.15);
  color: var(--amazon-amber);
  border: 1px solid var(--border-amber);
}
.offer-badge.green {
  background: rgba(34, 197, 94, 0.15);
  color: #4ade80;
  border: 1px solid rgba(34, 197, 94, 0.3);
}
.offer-title {
  font-family: var(--font-display);
  font-size: 1.35rem;
  font-weight: 700;
  margin-bottom: 10px;
}
.offer-desc {
  color: var(--text-muted);
  font-size: 0.9375rem;
  margin-bottom: 20px;
  flex-grow: 1;
}
.offer-features {
  list-style: none;
  margin-bottom: 26px;
  border-top: 1px solid var(--border-subtle);
  padding-top: 16px;
}
.offer-features li {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 0.875rem;
  color: var(--text-main);
  margin-bottom: 10px;
}
.offer-features li svg {
  color: var(--prime-blue);
  flex-shrink: 0;
  margin-top: 3px;
}
.offer-action {
  margin-top: auto;
}
.offer-action .btn-primary, .offer-action .btn-amber {
  width: 100%;
}

/* Calculator Section */
.calc-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 44px;
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 40px;
  box-shadow: var(--shadow-card);
}
.calc-inputs {
  display: flex;
  flex-direction: column;
  gap: 28px;
}
.slider-group label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.95rem;
  font-weight: 600;
  margin-bottom: 10px;
}
.slider-group .slider-val {
  color: var(--prime-blue);
  font-family: var(--font-display);
  font-size: 1.1rem;
  font-weight: 700;
}
.slider-group input[type="range"] {
  width: 100%;
  accent-color: var(--prime-blue);
  height: 6px;
  border-radius: 3px;
  background: rgba(255, 255, 255, 0.1);
  outline: none;
  cursor: pointer;
}
.calc-result-box {
  background: rgba(10, 17, 24, 0.7);
  border: 1px solid var(--border-active);
  border-radius: var(--radius-md);
  padding: 34px 28px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.calc-result-box::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, var(--prime-blue-glow) 0%, transparent 60%);
  pointer-events: none;
}
.calc-result-label {
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  margin-bottom: 8px;
}
.calc-annual-val {
  font-family: var(--font-display);
  font-size: 3rem;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1;
  margin-bottom: 14px;
}
.calc-net-pill {
  display: inline-block;
  background: rgba(34, 197, 94, 0.15);
  border: 1px solid rgba(34, 197, 94, 0.35);
  color: #4ade80;
  font-size: 0.875rem;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: var(--radius-full);
  margin-bottom: 24px;
}
.calc-breakdown {
  font-size: 0.8125rem;
  color: var(--text-muted);
  line-height: 1.6;
  text-align: left;
  border-top: 1px solid var(--border-subtle);
  padding-top: 16px;
}

/* Pricing Section */
.pricing-toggle-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  margin-bottom: 45px;
}
.pricing-label {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-muted);
  cursor: pointer;
}
.pricing-label.active {
  color: var(--text-main);
}
.toggle-switch {
  position: relative;
  width: 52px;
  height: 28px;
  background: rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: background 0.3s ease;
}
.toggle-switch .toggle-knob {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  background: var(--prime-blue);
  border-radius: 50%;
  transition: transform 0.3s ease;
}
.toggle-switch.annual .toggle-knob {
  transform: translateX(24px);
}
.save-badge {
  background: rgba(255, 153, 0, 0.18);
  color: var(--amazon-amber);
  border: 1px solid var(--border-amber);
  font-size: 0.75rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: var(--radius-full);
}
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 26px;
}
.pricing-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 36px 30px;
  position: relative;
}
.pricing-card.featured {
  border-color: var(--prime-blue);
  box-shadow: 0 0 30px rgba(0, 168, 225, 0.15);
}
.price-val {
  font-family: var(--font-display);
  font-size: 2.5rem;
  font-weight: 800;
  margin: 18px 0 6px;
}
.price-period {
  font-size: 0.95rem;
  color: var(--text-muted);
  font-weight: 400;
}

/* FAQ Accordion */
.faq-wrap {
  max-width: 800px;
  margin: 0 auto;
}
.faq-item {
  border-bottom: 1px solid var(--border-subtle);
}
.faq-question {
  width: 100%;
  background: none;
  border: none;
  padding: 22px 0;
  text-align: left;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--text-main);
  cursor: pointer;
}
.faq-question:hover {
  color: var(--prime-blue);
}
.faq-question svg {
  transition: transform 0.3s ease;
  color: var(--prime-blue);
  flex-shrink: 0;
}
.faq-item.active .faq-question svg {
  transform: rotate(180deg);
}
.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s ease, padding 0.35s ease;
  color: var(--text-muted);
  font-size: 0.95rem;
  line-height: 1.7;
}
.faq-item.active .faq-answer {
  max-height: 250px;
  padding-bottom: 22px;
}

/* Legal Pages Styling */
.legal-content {
  padding: 70px 0;
  max-width: 820px;
  margin: 0 auto;
}
.legal-content h1 {
  font-family: var(--font-display);
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 12px;
}
.legal-meta {
  color: var(--text-muted);
  font-size: 0.875rem;
  margin-bottom: 35px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-subtle);
}
.legal-content h2 {
  font-family: var(--font-display);
  font-size: 1.45rem;
  font-weight: 700;
  margin: 32px 0 14px;
  color: var(--prime-blue);
}
.legal-content p, .legal-content ul {
  color: #CBD5E1;
  font-size: 1rem;
  margin-bottom: 18px;
  line-height: 1.75;
}
.legal-content ul {
  padding-left: 24px;
}
.legal-box {
  background: var(--bg-card);
  border-left: 4px solid var(--prime-blue);
  padding: 20px;
  border-radius: var(--radius-sm);
  margin: 24px 0;
}

/* Contact Form */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}
.contact-form {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 32px;
}
.form-group {
  margin-bottom: 20px;
}
.form-group label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 8px;
}
.form-control {
  width: 100%;
  background: rgba(10, 17, 24, 0.8);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 12px 16px;
  color: var(--text-main);
  font-family: var(--font-body);
  font-size: 0.95rem;
  outline: none;
  transition: border-color 0.2s ease;
}
.form-control:focus {
  border-color: var(--prime-blue);
}
textarea.form-control {
  min-height: 130px;
  resize: vertical;
}

/* Footer */
.site-footer {
  background: #060B10;
  border-top: 1px solid var(--border-subtle);
  padding: 60px 0 35px;
  font-size: 0.875rem;
  color: var(--text-muted);
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 45px;
}
.footer-brand p {
  margin-top: 14px;
  line-height: 1.6;
  max-width: 360px;
}
.footer-col h4 {
  color: var(--text-main);
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 18px;
}
.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.footer-links a {
  color: var(--text-muted);
  text-decoration: none;
  transition: color 0.2s ease;
}
.footer-links a:hover {
  color: var(--prime-blue);
}
.footer-legal-bar {
  border-top: 1px solid var(--border-subtle);
  padding-top: 25px;
  text-align: center;
  font-size: 0.8125rem;
  color: var(--text-subtle);
  line-height: 1.6;
}
.footer-legal-bar .disclaimer-strong {
  color: var(--text-muted);
  font-weight: 600;
  display: block;
  margin-bottom: 8px;
}

/* Responsive */
@media (max-width: 900px) {
  .calc-card {
    grid-template-columns: 1fr;
  }
  .contact-grid {
    grid-template-columns: 1fr;
  }
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}
@media (max-width: 768px) {
  .nav-links {
    display: none;
  }
  .hero-trust-bar {
    gap: 16px;
  }
}
```

- [ ] **Step 2: Commit CSS stylesheet**
```bash
git add css/style.css
git commit -m "feat: add comprehensive design system and styles"
```

---

### Task 2: Central Affiliate Link Config (`js/config.js`)

**Files:**
- Create: `js/config.js`
- Test: Verification via node / browser syntax check

**Interfaces:**
- Produces: `SITE_CONFIG` object, `getAffiliateUrl(baseUrl)` helper function.

- [ ] **Step 1: Write `js/config.js`**

```javascript
/* js/config.js */
const SITE_CONFIG = {
  // Replace with your actual Amazon Associate Tracking ID (e.g. 'myprimeguide-20')
  associateTag: 'primeperks-20',
  siteName: 'Prime Perks Guide',
  supportEmail: 'contact@primeperksguide.com',
  affiliateEnabled: true
};

/**
 * Appends the Amazon Associate tag parameter to any valid Amazon URL.
 * Preserves existing query strings seamlessly.
 */
function getAffiliateUrl(baseUrl) {
  if (!SITE_CONFIG.affiliateEnabled || !SITE_CONFIG.associateTag) {
    return baseUrl;
  }
  try {
    const url = new URL(baseUrl);
    url.searchParams.set('tag', SITE_CONFIG.associateTag);
    return url.toString();
  } catch (e) {
    const separator = baseUrl.includes('?') ? '&' : '?';
    return `${baseUrl}${separator}tag=${encodeURIComponent(SITE_CONFIG.associateTag)}`;
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { SITE_CONFIG, getAffiliateUrl };
}
```

- [ ] **Step 2: Verify `js/config.js` logic with node**
```bash
node -e "const { getAffiliateUrl } = require('./js/config.js'); console.log(getAffiliateUrl('https://www.amazon.com/prime'));"
```
Expected: `https://www.amazon.com/prime?tag=primeperks-20`

- [ ] **Step 3: Commit config**
```bash
git add js/config.js
git commit -m "feat: add centralized Amazon associate config and URL helper"
```

---

### Task 3: Amazon Associates Legal & Compliance Pages Suite

**Files:**
- Create: `disclosure.html`
- Create: `privacy.html`
- Create: `terms.html`
- Create: `contact.html`

**Interfaces:**
- Consumes: `css/style.css`, `js/config.js`
- Produces: 4 complete, standalone compliance pages satisfying Amazon Operating Agreement, FTC Guidelines, and manual reviewer checks.

- [ ] **Step 1: Create `disclosure.html`**
Fully detailed FTC & Amazon Operating Agreement disclosure explaining affiliate relationships, $0 extra cost for users, pricing volatility disclaimers, and editorial independence.

- [ ] **Step 2: Create `privacy.html`**
Privacy Policy addressing cookie attribution, Amazon Associates 24-hour cookie tracking, third-party log data, GDPR/CCPA consumer rights.

- [ ] **Step 3: Create `terms.html`**
Terms of Service detailing website usage, trademarks (Amazon, Prime, Audible, Kindle), limitation of liability, and third-party merchant disclaimers.

- [ ] **Step 4: Create `contact.html`**
Publisher disclosure, legitimate contact inquiry form, direct email, and verified domain identity for manual Amazon account reviewer approval.

- [ ] **Step 5: Verify all compliance pages load properly and commit**
```bash
git add disclosure.html privacy.html terms.html contact.html
git commit -m "feat: add complete Amazon Associates compliance suite (disclosure, privacy, terms, contact)"
```

---

### Task 4: Main Promotional Landing Page (`index.html`)

**Files:**
- Create: `index.html`

**Interfaces:**
- Consumes: `css/style.css`, `js/config.js`, `js/main.js`
- Produces: The primary high-converting one-page website incorporating:
  1. Top Disclosure Banner
  2. Sticky Glassmorphic Navigation with Brand Logo & CTA
  3. Hero Section with dynamic value badge, headline, subhead, dual CTAs, and trust pillars
  4. Core 4 Benefits Pillars (Fast Delivery, Prime Video/Entertainment, Music/Reading, Exclusive Savings)
  5. Targeted Special Offers Hub with 11 Associate Campaigns (Prime Trial, Young Adult, Prime Access, Prime Gaming/Luna, Audible suite, Kindle Unlimited, Amazon Business, Checkout Sign-Up)
  6. Interactive Annual Savings & Value Calculator
  7. Membership Pricing Cards & Annual/Monthly Toggle
  8. FAQ Accordion
  9. Fully compliant Amazon Associates Footer

- [ ] **Step 1: Write `index.html` with all sections and semantic markup**
- [ ] **Step 2: Verify HTML structure and all required offer links are present**
- [ ] **Step 3: Commit `index.html`**
```bash
git add index.html
git commit -m "feat: create high-converting Amazon Prime promotional landing page"
```

---

### Task 5: Interactive Engine (`js/main.js`)

**Files:**
- Create: `js/main.js`

**Interfaces:**
- Consumes: DOM elements in `index.html`, `SITE_CONFIG` from `js/config.js`
- Produces:
  1. Category Tab Filter logic for Offers Hub with smooth transitions.
  2. Live Dynamic Savings Calculator (Delivery orders slider, Video hours slider, Books slider -> calculates Annual Value and Net Savings vs $139/yr).
  3. Monthly vs Annual Billing Toggle with animated price updates.
  4. Interactive FAQ Accordion expand/collapse.
  5. Dynamic affiliate link tag injection to all `data-amazon-href` anchors.

- [ ] **Step 1: Write `js/main.js`**
- [ ] **Step 2: Test script syntax via node or browser**
- [ ] **Step 3: Commit `js/main.js`**
```bash
git add js/main.js
git commit -m "feat: add interactive logic for filter tabs, savings calculator, and pricing toggle"
```

---

### Task 6: Visual Assets & End-to-End Browser Verification

**Files:**
- Modify / Verify: `index.html`, `disclosure.html`, `privacy.html`, `terms.html`, `contact.html`

**Verification:**
- [ ] **Step 1: Run local test server**
- [ ] **Step 2: Verify all 11 affiliate links correctly include associate tag parameter**
- [ ] **Step 3: Test Interactive Savings Calculator calculations**
- [ ] **Step 4: Test Category Filters in the Offers Hub**
- [ ] **Step 5: Verify mobile responsiveness and compliance pages navigation**
- [ ] **Step 6: Final Git commit and summary**

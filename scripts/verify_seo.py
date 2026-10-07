"""
verify_seo.py
Comprehensive automated auditor for SEO readiness, metadata compliance,
favicon integration, and JSON-LD syntax validity across all site pages.
"""

import os
import re
import json
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = [
    "index.html",
    "blog.html",
    "blog-prime-worth-it-2026.html",
    "blog-prime-discount-young-adult-access.html",
    "blog-audible-free-trial-guide.html",
    "blog-best-audiobooks-2026.html",
    "blog-top-fantasy-audiobooks-2026.html",
    "blog-book-vs-audiobook-guide.html",
    "blog-best-audiobook-narrators-2026.html",
    "blog-bestselling-audiobooks-trends.html",
    "blog-most-anticipated-audiobooks-late-2026.html",
    "blog-viral-booktok-audiobooks.html",
    "blog-classic-audiobooks-2026.html",
    "blog-audiobooks-productivity-habits.html",
    "blog-audible-deals-credits-guide.html",
    "contact.html",
    "disclosure.html",
    "privacy.html",
    "terms.html"
]

REQUIRED_ASSETS = [
    "favicon.svg",
    "favicon.ico",
    "favicon-16x16.png",
    "favicon-32x32.png",
    "apple-touch-icon.png",
    "android-chrome-192x192.png",
    "android-chrome-512x512.png",
    "site.webmanifest",
    "images/og-share.png",
    "robots.txt",
    "sitemap.xml"
]

def check_assets():
    print("=== 1. Checking Static SEO & Favicon Assets ===")
    missing = []
    for asset in REQUIRED_ASSETS:
        full_path = os.path.join(BASE_DIR, asset)
        if not os.path.isfile(full_path):
            missing.append(asset)
            print(f"  [FAIL] Missing asset: {asset}")
        else:
            size = os.path.getsize(full_path)
            print(f"  [PASS] {asset} exists ({size:,} bytes)")
    return len(missing) == 0

def check_robots_and_sitemap():
    print("\n=== 2. Validating robots.txt & sitemap.xml ===")
    robots_path = os.path.join(BASE_DIR, "robots.txt")
    with open(robots_path, "r", encoding="utf-8") as f:
        robots_txt = f.read()
    
    assert "Sitemap: https://savvyfindsonline.com/sitemap.xml" in robots_txt, "robots.txt missing Sitemap directive"
    print("  [PASS] robots.txt is valid and points to sitemap")

    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    urls = [loc.text for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    print(f"  [PASS] sitemap.xml parsed successfully ({len(urls)} URLs found)")
    
    expected_paths = [
        "https://savvyfindsonline.com/",
        "https://savvyfindsonline.com/blog.html",
        "https://savvyfindsonline.com/blog-prime-worth-it-2026.html",
        "https://savvyfindsonline.com/blog-prime-discount-young-adult-access.html",
        "https://savvyfindsonline.com/blog-audible-free-trial-guide.html",
        "https://savvyfindsonline.com/blog-best-audiobooks-2026.html",
        "https://savvyfindsonline.com/blog-top-fantasy-audiobooks-2026.html",
        "https://savvyfindsonline.com/blog-book-vs-audiobook-guide.html",
        "https://savvyfindsonline.com/blog-best-audiobook-narrators-2026.html",
        "https://savvyfindsonline.com/blog-bestselling-audiobooks-trends.html",
        "https://savvyfindsonline.com/blog-most-anticipated-audiobooks-late-2026.html",
        "https://savvyfindsonline.com/blog-viral-booktok-audiobooks.html",
        "https://savvyfindsonline.com/blog-classic-audiobooks-2026.html",
        "https://savvyfindsonline.com/blog-audiobooks-productivity-habits.html",
        "https://savvyfindsonline.com/blog-audible-deals-credits-guide.html",
        "https://savvyfindsonline.com/contact.html",
        "https://savvyfindsonline.com/disclosure.html",
        "https://savvyfindsonline.com/privacy.html",
        "https://savvyfindsonline.com/terms.html"
    ]
    for ep in expected_paths:
        assert ep in urls, f"Missing {ep} in sitemap"
    print(f"  [PASS] All {len(expected_paths)} URLs registered in sitemap.xml")

def audit_html_pages():
    print("\n=== 3. Auditing HTML Head Metadata, Favicons & Schema ===")
    total_errors = 0

    for page in PAGES:
        filepath = os.path.join(BASE_DIR, page)
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()

        errors = []

        # 1. Title tag
        title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        if not title_match or not title_match.group(1).strip():
            errors.append("Missing or empty <title>")
        
        # 2. Meta description
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
        if not desc_match or not desc_match.group(1).strip():
            errors.append("Missing <meta name='description'>")

        # 3. Canonical tag
        canon_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', html, re.IGNORECASE)
        if not canon_match:
            errors.append("Missing <link rel='canonical'>")

        # 4. Favicon links
        if 'favicon.svg' not in html:
            errors.append("Missing favicon.svg link")
        if 'site.webmanifest' not in html:
            errors.append("Missing site.webmanifest link")
        if 'apple-touch-icon' not in html:
            errors.append("Missing apple-touch-icon link")

        # 5. Open Graph tags
        for og in ["og:title", "og:description", "og:image", "og:url"]:
            if og not in html:
                errors.append(f"Missing {og} tag")

        # 6. Twitter Card tags
        for tw in ["twitter:card", "twitter:title", "twitter:description", "twitter:image"]:
            if tw not in html:
                errors.append(f"Missing {tw} tag")

        # 7. Robots & Theme-Color
        if 'name="robots"' not in html:
            errors.append("Missing robots meta tag")
        if 'name="theme-color"' not in html:
            errors.append("Missing theme-color meta tag")

        # 8. Single H1 tag check
        h1_matches = re.findall(r"<h1\b", html, re.IGNORECASE)
        if len(h1_matches) != 1:
            errors.append(f"Expected exactly 1 <h1>, found {len(h1_matches)}")

        # 9. No placeholder leaf emoji
        if "🌿" in html:
            errors.append("Found placeholder leaf emoji '🌿' in head/favicon")

        # 10. JSON-LD Structured Data
        json_ld_matches = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
        if not json_ld_matches:
            errors.append("Missing JSON-LD structured data")
        else:
            for idx, block in enumerate(json_ld_matches):
                try:
                    parsed = json.loads(block.strip())
                    # verify context
                    if "@context" not in parsed:
                        errors.append(f"JSON-LD block {idx} missing @context")
                except Exception as e:
                    errors.append(f"JSON-LD block {idx} invalid JSON: {e}")

        if errors:
            print(f"  [FAIL] {page}:")
            for err in errors:
                print(f"    - {err}")
            total_errors += len(errors)
        else:
            print(f"  [PASS] {page} (Title, Meta, Canon, Favicons, OG, Twitter, Schema, H1 valid)")

    return total_errors == 0

def run_all():
    assets_ok = check_assets()
    check_robots_and_sitemap()
    html_ok = audit_html_pages()
    
    print("\n===============================")
    if assets_ok and html_ok:
        print("[SUCCESS] ALL SEO & FAVICON AUDITS PASSED 100%!")
        print("The website is fully SEO-ready for production deployment.")
    else:
        print("[ERROR] SOME CHECKS FAILED.")
        exit(1)

if __name__ == "__main__":
    run_all()

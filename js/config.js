/**
 * Amazon Associates & Site Configuration
 * Verified Associate Tag: tubejaf-20
 */
const SITE_CONFIG = {
  associateTag: 'tubejaf-20',
  siteName: 'Prime Perks Guide',
  supportEmail: 'contact@primeperksguide.com',
  affiliateEnabled: true
};

/**
 * Appends the Amazon Associate tag parameter to any valid Amazon URL.
 * Preserves pre-built Amazon shortlinks (e.g. link.amazon / amzn.to) which already embed tracking IDs.
 * @param {string} baseUrl
 * @returns {string}
 */
function getAffiliateUrl(baseUrl) {
  if (!baseUrl) return '#';
  if (!SITE_CONFIG.affiliateEnabled || !SITE_CONFIG.associateTag) {
    return baseUrl;
  }
  // Official Amazon shortlinks already embed the affiliate tracking ID and cryptographic hash
  if (baseUrl.includes('link.amazon') || baseUrl.includes('amzn.to')) {
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

// Global browser window export and CommonJS module export for testing
if (typeof window !== 'undefined') {
  window.SITE_CONFIG = SITE_CONFIG;
  window.getAffiliateUrl = getAffiliateUrl;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { SITE_CONFIG, getAffiliateUrl };
}

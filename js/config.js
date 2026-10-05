/**
 * Amazon Associates & Site Configuration
 * Update `associateTag` below with your registered Amazon Associates Store/Tracking ID.
 */
const SITE_CONFIG = {
  // Replace with your real Amazon Associate Tag (e.g. 'yourtag-20')
  associateTag: 'primeperks-20',
  siteName: 'Prime Perks Guide',
  supportEmail: 'contact@primeperksguide.com',
  affiliateEnabled: true
};

/**
 * Appends the Amazon Associate tag parameter to any valid Amazon URL.
 * Safely preserves existing query parameters.
 * @param {string} baseUrl
 * @returns {string}
 */
function getAffiliateUrl(baseUrl) {
  if (!baseUrl) return '#';
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

// Global browser window export and CommonJS module export for testing
if (typeof window !== 'undefined') {
  window.SITE_CONFIG = SITE_CONFIG;
  window.getAffiliateUrl = getAffiliateUrl;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { SITE_CONFIG, getAffiliateUrl };
}

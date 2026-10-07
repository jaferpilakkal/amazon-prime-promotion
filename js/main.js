/**
 * Prime Perks Guide - Interactive Engine
 */

document.addEventListener('DOMContentLoaded', () => {
  initAffiliateLinks();
  initCategoryFilters();
  initSavingsCalculator();
  initPricingToggle();
  initFaqAccordion();
  initMobileNav();
  initTrialModal();
});

/**
 * 1. Automatically formats all affiliate links with the configured Amazon Associates tag
 */
function initAffiliateLinks() {
  const amazonLinks = document.querySelectorAll('a[data-amazon-href]');
  amazonLinks.forEach(link => {
    const rawUrl = link.getAttribute('data-amazon-href');
    if (rawUrl && typeof getAffiliateUrl === 'function') {
      link.href = getAffiliateUrl(rawUrl);
    }
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'nofollow sponsored noopener');
  });
}

/**
 * 2. Category Tab Filter for Offers Hub
 */
function initCategoryFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const offerCards = document.querySelectorAll('.offer-card');

  if (!filterBtns.length || !offerCards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      offerCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/**
 * 3. Interactive Prime Annual Savings Calculator
 */
function initSavingsCalculator() {
  const sliderOrders = document.getElementById('sliderOrders');
  const sliderStreaming = document.getElementById('sliderStreaming');
  const sliderBooks = document.getElementById('sliderBooks');

  if (!sliderOrders || !sliderStreaming || !sliderBooks) return;

  const valOrders = document.getElementById('valOrders');
  const valStreaming = document.getElementById('valStreaming');
  const valBooks = document.getElementById('valBooks');

  const calcAnnualValue = document.getElementById('calcAnnualValue');
  const calcNetPill = document.getElementById('calcNetPill');
  const breakdownShipping = document.getElementById('breakdownShipping');
  const breakdownStreaming = document.getElementById('breakdownStreaming');
  const breakdownReading = document.getElementById('breakdownReading');

  function calculateSavings() {
    const orders = parseInt(sliderOrders.value, 10);
    const streaming = parseInt(sliderStreaming.value, 10);
    const books = parseInt(sliderBooks.value, 10);

    // Update slider label texts
    valOrders.textContent = `${orders} order${orders === 1 ? '' : 's'}`;
    valStreaming.textContent = `${streaming} hour${streaming === 1 ? '' : 's'}`;
    valBooks.textContent = `${books} title${books === 1 ? '' : 's'}`;

    // Estimated annual dollar valuations:
    // Shipping: $5 per order savings * 12 months
    const shippingAnnual = orders * 5 * 12;
    // Streaming & Gaming: standalone benchmark of $12-$15/mo scaled by usage + Luna cloud
    const streamingAnnual = Math.round(streaming * 1.5 * 12) + 40;
    // Digital reading & audiobooks: average $12 per book/audiobook * 12 months
    const readingAnnual = books * 12 * 12;
    // Member-only discounts & Prime Day benchmark
    const memberDealsAnnual = 150;

    const totalAnnualValue = shippingAnnual + streamingAnnual + readingAnnual + memberDealsAnnual;
    const standardPrimeCost = 139;
    const netGain = totalAnnualValue - standardPrimeCost;

    calcAnnualValue.textContent = `$${totalAnnualValue}`;
    if (netGain >= 0) {
      calcNetPill.textContent = `+$${netGain} Net Gain vs $139 Prime`;
      calcNetPill.style.color = 'var(--accent-positive-text)';
      calcNetPill.style.background = 'var(--accent-positive-bg)';
      calcNetPill.style.borderColor = 'var(--accent-positive-border)';
    } else {
      calcNetPill.textContent = `Breakeven Value`;
    }

    breakdownShipping.textContent = `$${shippingAnnual} / yr`;
    breakdownStreaming.textContent = `$${streamingAnnual} / yr`;
    breakdownReading.textContent = `$${readingAnnual} / yr`;
  }

  sliderOrders.addEventListener('input', calculateSavings);
  sliderStreaming.addEventListener('input', calculateSavings);
  sliderBooks.addEventListener('input', calculateSavings);

  calculateSavings();
}

/**
 * 4. Annual vs. Monthly Pricing Switcher
 */
function initPricingToggle() {
  const toggle = document.getElementById('pricingToggle');
  const labelAnnual = document.getElementById('labelAnnual');
  const labelMonthly = document.getElementById('labelMonthly');

  const priceStandard = document.getElementById('priceStandard');
  const periodStandard = document.getElementById('periodStandard');
  const priceYoungAdult = document.getElementById('priceYoungAdult');
  const periodYoungAdult = document.getElementById('periodYoungAdult');

  if (!toggle) return;

  let isAnnual = true;

  function updatePricing() {
    if (isAnnual) {
      toggle.classList.add('annual');
      labelAnnual.classList.add('active');
      labelMonthly.classList.remove('active');

      if (priceStandard) priceStandard.textContent = '$139';
      if (periodStandard) periodStandard.textContent = 'per year ($11.58 / month equivalent)';

      if (priceYoungAdult) priceYoungAdult.textContent = '$69';
      if (periodYoungAdult) periodYoungAdult.textContent = 'per year ($5.75 / month equivalent)';
    } else {
      toggle.classList.remove('annual');
      labelAnnual.classList.remove('active');
      labelMonthly.classList.add('active');

      if (priceStandard) priceStandard.textContent = '$14.99';
      if (periodStandard) periodStandard.textContent = 'per month (cancel anytime)';

      if (priceYoungAdult) priceYoungAdult.textContent = '$7.49';
      if (periodYoungAdult) periodYoungAdult.textContent = 'per month (cancel anytime)';
    }
  }

  toggle.addEventListener('click', () => {
    isAnnual = !isAnnual;
    updatePricing();
  });

  if (labelAnnual) {
    labelAnnual.addEventListener('click', () => {
      isAnnual = true;
      updatePricing();
    });
  }

  if (labelMonthly) {
    labelMonthly.addEventListener('click', () => {
      isAnnual = false;
      updatePricing();
    });
  }
}

/**
 * 5. Interactive FAQ Accordion
 */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (question) {
      question.addEventListener('click', () => {
        const isOpen = item.classList.contains('active');
        faqItems.forEach(i => i.classList.remove('active'));
        if (!isOpen) {
          item.classList.add('active');
        }
      });
    }
  });
}

/**
 * 6. Mobile Navigation
 */
function initMobileNav() {
  const toggleBtn = document.getElementById('mobileNavToggle');
  const navLinks = document.getElementById('navLinks');

  if (!toggleBtn || !navLinks) return;

  toggleBtn.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
    });
  });

  document.addEventListener('click', (e) => {
    if (!toggleBtn.contains(e.target) && !navLinks.contains(e.target) && navLinks.classList.contains('open')) {
      navLinks.classList.remove('open');
    }
  });
}

/**
 * 7. Interactive Free Trial Modal
 */
function initTrialModal() {
  const modal = document.getElementById('trialModal');
  const closeBtn = document.getElementById('modalCloseBtn');
  const modalConfirmBtn = document.getElementById('modalConfirmBtn');

  if (!modal || !closeBtn) return;

  closeBtn.addEventListener('click', () => {
    modal.classList.remove('open');
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('open');
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      modal.classList.remove('open');
    }
  });
}

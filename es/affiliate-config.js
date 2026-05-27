// Affiliate Configuration — Candy AI Porn
const AFFILIATE_BASE = 'https://www.ourdreamersai.com/7S8HPQB/3QQG7/';
const OFFERS = {
  women:   AFFILIATE_BASE + '?source=candyai_modal_women',
  men:     AFFILIATE_BASE + '?source=candyai_modal_men',
  anime:   AFFILIATE_BASE + '?source=candyai_modal_anime',
  default: AFFILIATE_BASE + '?source=candyai_direct'
};

window.goToOffer = function(preference) {
  const url = OFFERS[preference] || OFFERS.default;
  window.open(url, '_blank');
};

document.addEventListener('DOMContentLoaded', function () {
  const overlay  = document.getElementById('modal-overlay');
  const modal    = document.getElementById('preference-modal');
  const closeBtn = document.getElementById('modal-close');

  function openModal()  { overlay.classList.add('active'); modal.classList.add('active'); }
  function closeModal() { overlay.classList.remove('active'); modal.classList.remove('active'); }

  // Auto-open 1x per session after 3s
  if (!sessionStorage.getItem('modalShown')) {
    setTimeout(function () {
      openModal();
      sessionStorage.setItem('modalShown', 'true');
    }, 3000);
  }

  closeBtn.addEventListener('click', closeModal);
  overlay.addEventListener('click', closeModal);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeModal();
  });

  // Preference buttons → goToOffer + close
  document.querySelectorAll('.pref-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      goToOffer(this.getAttribute('data-preference'));
      closeModal();
    });
  });

  // All CTA buttons → direct offer, NO modal
  document.querySelectorAll('[data-open-modal]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      goToOffer('default');
    });
  });
});

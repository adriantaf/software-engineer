import { registerSW } from 'virtual:pwa-register';

const updateSW = registerSW({
  immediate: true,
  onNeedRefresh() {
    const banner = document.getElementById('pwa-update');
    if (banner) banner.hidden = false;
  },
});

function bindUpdateButton() {
  const btn = document.getElementById('pwa-update-btn');
  if (!btn || btn.dataset.bound === '1') return;
  btn.dataset.bound = '1';
  btn.addEventListener('click', () => {
    void updateSW(true);
  });
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bindUpdateButton);
  } else {
    bindUpdateButton();
  }
}

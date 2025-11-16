// Persist and restore scroll position per page
(function () {
  function key() {
    return 'mdbook:scroll:' + location.pathname + location.hash;
  }

  function save() {
    try {
      localStorage.setItem(key(), String(window.scrollY || document.documentElement.scrollTop || 0));
    } catch (_) {}
  }

  function restore() {
    try {
      var v = localStorage.getItem(key());
      if (v) {
        var y = parseInt(v, 10) || 0;
        window.scrollTo({ top: y, behavior: 'instant' in window ? 'instant' : 'auto' });
      }
    } catch (_) {}
  }

  document.addEventListener('DOMContentLoaded', function () {
    // Defer a tick so mdBook finishes layout
    setTimeout(restore, 0);
    window.addEventListener('scroll', function () {
      // throttle a bit
      if (save._t) return;
      save._t = setTimeout(function () { save._t = null; save(); }, 200);
    }, { passive: true });
    window.addEventListener('beforeunload', save);
  });
})();


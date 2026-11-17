// easy2live 官網共用腳本：深色模式切換、頁首陰影、作品集燈箱
(function () {
  var root = document.documentElement;

  // 深色模式：預設跟系統，手動切換後記住
  var btn = document.querySelector('[data-theme-toggle]');
  if (btn) {
    btn.addEventListener('click', function () {
      var sysDark = matchMedia('(prefers-color-scheme: dark)').matches;
      var cur = root.dataset.theme || (sysDark ? 'dark' : 'light');
      var next = cur === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
      btn.setAttribute('aria-label', next === 'dark' ? '切換成淺色模式' : '切換成深色模式');
    });
  }

  // 捲動後頁首加底線
  var hd = document.querySelector('header.site');
  if (hd) {
    var onScroll = function () { hd.classList.toggle('scrolled', window.scrollY > 8); };
    addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // 手機選單：點選連結後收起
  document.querySelectorAll('.menu a').forEach(function (a) {
    a.addEventListener('click', function () { a.closest('details').open = false; });
  });

  // 作品集燈箱
  var items = Array.prototype.slice.call(document.querySelectorAll('.gallery [data-full]'));
  var box = document.querySelector('.lightbox');
  if (!items.length || !box || !box.showModal) return;
  var img = box.querySelector('img'), count = box.querySelector('.count'), idx = 0;
  function show(i) {
    idx = (i + items.length) % items.length;
    var it = items[idx];
    img.src = it.dataset.full;
    img.alt = it.querySelector('img').alt;
    count.textContent = (idx + 1) + ' / ' + items.length + (it.dataset.date ? '　' + it.dataset.date : '');
  }
  items.forEach(function (it, i) {
    it.addEventListener('click', function () { show(i); box.showModal(); });
  });
  box.querySelector('.prev').addEventListener('click', function () { show(idx - 1); });
  box.querySelector('.next').addEventListener('click', function () { show(idx + 1); });
  box.querySelector('.close').addEventListener('click', function () { box.close(); });
  box.addEventListener('click', function (e) { if (e.target === box) box.close(); });
  box.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') show(idx - 1);
    if (e.key === 'ArrowRight') show(idx + 1);
  });
  var x0 = null;
  box.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  box.addEventListener('touchend', function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
    x0 = null;
  });
})();

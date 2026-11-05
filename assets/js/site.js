/* Dispare Trading — site behaviour. No third-party requests, no personal data. */
(function () {
  "use strict";
  var doc = document.documentElement;
  var lang = doc.lang === "en" ? "en" : "ru";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function store(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  /* ---------- manual language switch: remember the choice ---------- */
  document.querySelectorAll("[data-set-lang]").forEach(function (a) {
    a.addEventListener("click", function () { store("dt-lang", a.getAttribute("data-set-lang")); });
  });

  /* ---------- header on scroll ---------- */
  var header = document.querySelector(".site-header");
  function onScroll() { if (header) header.classList.toggle("is-scrolled", window.scrollY > 6); }
  document.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- mobile menu ---------- */
  var toggle = document.querySelector(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () { document.body.classList.remove("menu-open"); toggle.setAttribute("aria-expanded", "false"); });
    });
  }

  /* ---------- live status strip (Moscow time, warehouse hours) ---------- */
  var HOLIDAYS = ["2026-11-04", "2027-01-01", "2027-01-02", "2027-01-03", "2027-01-04", "2027-01-05", "2027-01-06", "2027-01-07", "2027-01-08", "2027-02-23", "2027-03-08", "2027-05-01", "2027-05-09", "2027-06-12", "2027-11-04"];
  var T = {
    ru: { open: "Склад открыт", closed: "Склад закрыт", back: "ответим в рабочее время", until: "работаем до 18:00" },
    en: { open: "Warehouse open", closed: "Warehouse closed", back: "we reply during business hours", until: "open until 18:00" }
  }[lang];
  var pill = document.querySelector("[data-status-pill]");
  var clock = document.querySelector("[data-msk-clock]");
  var note = document.querySelector("[data-status-note]");
  function msk() {
    var parts = {};
    new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Moscow", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", weekday: "short", hour12: false })
      .formatToParts(new Date()).forEach(function (p) { parts[p.type] = p.value; });
    return parts;
  }
  function tick() {
    if (!pill) return;
    var p = msk();
    var h = parseInt(p.hour, 10) % 24, wd = p.weekday, date = p.year + "-" + p.month + "-" + p.day;
    var open = ["Sat", "Sun"].indexOf(wd) === -1 && HOLIDAYS.indexOf(date) === -1 && h >= 10 && h < 18;
    pill.classList.toggle("is-open", open);
    pill.lastChild.textContent = open ? T.open : T.closed;
    if (clock) clock.textContent = (h < 10 ? "0" + h : h) + ":" + p.minute;
    if (note) note.textContent = open ? T.until : T.back;
  }
  tick();
  setInterval(tick, 20000);

  /* ---------- year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- copy INN ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var v = b.getAttribute("data-copy"), label = b.textContent;
      var done = function () { b.classList.add("ok"); b.textContent = lang === "en" ? "Copied" : "Скопировано"; setTimeout(function () { b.classList.remove("ok"); b.textContent = label; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(v).then(done, function () {}); else done();
    });
  });

  /* ---------- shop search (article goes to the partner store) ---------- */
  var form = document.querySelector("[data-shop-search]");
  if (form) {
    form.addEventListener("submit", function (e) {
      var q = (form.querySelector("input").value || "").replace(/[^0-9A-Za-zА-Яа-я\-\.\s]/g, "").trim();
      if (!q) { e.preventDefault(); form.querySelector("input").focus(); return; }
      form.querySelector("input").value = q;
    });
  }

  /* ---------- reveal on scroll ---------- */
  doc.classList.add("js");
  var revealEls = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    revealEls.forEach(function (el) {
      var sib = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
      el.style.transitionDelay = Math.min(sib, 5) * 70 + "ms";
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }
  /* safety net: never leave content hidden */
  setTimeout(function () { revealEls.forEach(function (el) { if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("is-visible"); }); }, 1500);

  /* ---------- hero: dimension lines draw, wheel turns with scroll ---------- */
  var hv = document.querySelector(".hero-visual");
  if (hv) {
    hv.querySelectorAll(".dim").forEach(function (p) { try { p.style.setProperty("--len", Math.ceil(p.getTotalLength())); } catch (e) {} });
    requestAnimationFrame(function () { setTimeout(function () { hv.classList.add("is-drawn"); }, 250); });
    var wheel = hv.querySelector(".wheel");
    if (wheel && !reduce) {
      var base = 0, last = performance.now(), ticking = false;
      var spin = function (now) {
        base += (now - last) * 0.004; last = now;
        wheel.style.transform = "rotate(" + (base + window.scrollY * 0.25) + "deg)";
        requestAnimationFrame(spin);
      };
      requestAnimationFrame(spin);
      if (window.matchMedia("(hover: hover)").matches) {
        document.querySelector(".hero").addEventListener("mousemove", function (e) {
          if (ticking) return; ticking = true;
          requestAnimationFrame(function () {
            var r = hv.getBoundingClientRect();
            var x = (e.clientX - (r.left + r.width / 2)) / r.width, y = (e.clientY - (r.top + r.height / 2)) / r.height;
            hv.style.transform = "translate(" + x * 10 + "px," + y * 10 + "px)";
            ticking = false;
          });
        });
      }
    }
  }

  /* ---------- stamp prints once ---------- */
  var stamp = document.querySelector(".stamp");
  if (stamp) {
    if ("IntersectionObserver" in window && !reduce) {
      var so = new IntersectionObserver(function (en) { if (en[0].isIntersecting) { stamp.classList.add("is-in"); so.disconnect(); } }, { threshold: 0.6 });
      so.observe(stamp);
    } else stamp.classList.add("is-in");
  }

  /* ---------- process line fills as you scroll ---------- */
  var steps = document.querySelector(".steps");
  if (steps && !reduce) {
    var prog = steps.querySelector(".progress");
    var upd = function () {
      var r = steps.getBoundingClientRect(), vh = window.innerHeight;
      var p = Math.max(0, Math.min(1, (vh * 0.85 - r.top) / (r.height + vh * 0.35)));
      if (prog) prog.style.setProperty("--p", p.toFixed(3));
    };
    document.addEventListener("scroll", upd, { passive: true }); upd();
  }
})();

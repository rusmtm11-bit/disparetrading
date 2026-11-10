/* Dispare Trading. No third-party requests, no personal data. */
(function () {
  "use strict";
  var lang = document.documentElement.lang === "en" ? "en" : "ru";

  /* Manual language choice wins over auto-detection on later visits */
  document.querySelectorAll("[data-set-lang]").forEach(function (a) {
    a.addEventListener("click", function () { try { localStorage.setItem("dt-lang", a.getAttribute("data-set-lang")); } catch (e) {} });
  });

  /* Mobile menu */
  var burger = document.querySelector(".burger");
  if (burger) {
    burger.addEventListener("click", function () {
      var open = document.body.classList.toggle("menu-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      burger.textContent = open ? burger.getAttribute("data-close") : burger.getAttribute("data-open");
    });
  }

  /* Warehouse status by Moscow time: Mon-Fri 10:00-18:00, public holidays closed */
  var HOLIDAYS = ["2026-11-04", "2027-01-01", "2027-01-02", "2027-01-03", "2027-01-04", "2027-01-05", "2027-01-06", "2027-01-07", "2027-01-08", "2027-02-23", "2027-03-08", "2027-05-01", "2027-05-09", "2027-06-12", "2027-11-04"];
  var TXT = {
    ru: { open: "Склад работает до 18:00", soon: "Склад откроется в 10:00", closed: "Склад откроется в понедельник", holiday: "Сегодня выходной день" },
    en: { open: "Warehouse open until 18:00 MSK", soon: "Warehouse opens at 10:00 MSK", closed: "Warehouse opens on Monday", holiday: "Public holiday in Russia" }
  }[lang];
  function moscow() {
    var o = {};
    new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Moscow", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", weekday: "short", hour12: false })
      .formatToParts(new Date()).forEach(function (p) { o[p.type] = p.value; });
    return o;
  }
  function status() {
    var m = moscow(), h = parseInt(m.hour, 10) % 24, day = m.year + "-" + m.month + "-" + m.day;
    var weekend = m.weekday === "Sat" || m.weekday === "Sun", fri = m.weekday === "Fri";
    var open = false, text;
    if (HOLIDAYS.indexOf(day) !== -1) text = TXT.holiday;
    else if (weekend || (fri && h >= 18)) text = TXT.closed;
    else if (h < 10) text = TXT.soon;
    else if (h < 18) { text = TXT.open; open = true; }
    else text = TXT.soon;
    document.querySelectorAll("[data-status]").forEach(function (el) { el.textContent = text; el.classList.toggle("is-open", open); });
  }
  status();
  setInterval(status, 60000);

  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* Copy buttons (INN, company details) */
  document.querySelectorAll("[data-copy]").forEach(function (b) {
    var label = b.textContent;
    b.addEventListener("click", function () {
      var done = function () { b.classList.add("done"); b.textContent = lang === "en" ? "Copied" : "Скопировано"; setTimeout(function () { b.classList.remove("done"); b.textContent = label; }, 1800); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(b.getAttribute("data-copy")).then(done, function () {});
    });
  });

  /* Part number search: tidy the input, then the form opens the partner store */
  var form = document.querySelector("[data-search]");
  if (form) {
    var input = form.querySelector("input");
    form.addEventListener("submit", function (e) {
      var q = (input.value || "").replace(/[^0-9A-Za-zА-Яа-яЁё]/g, "");
      if (!q) { e.preventDefault(); input.focus(); return; }
      input.value = q;
    });
  }
})();

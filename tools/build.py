#!/usr/bin/env python3
"""Static site generator for disparetrading.ru.

Edit texts in tools/content.py, then run:
    python3 tools/build.py            # writes the site into the repository root
    python3 tools/build.py --preview  # writes a self-contained preview into _preview/
                                      # (relative links, no auto language redirect to the live domain)
Only the standard library is used; GitHub Pages serves the generated .html files as they are.
"""
import os, sys, html, json, shutil
sys.path.insert(0, os.path.dirname(__file__))
from content import PAGES, STR, CATS, ORDER  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOMAIN = "https://disparetrading.ru"
SHOP = "https://shop.disparetrading.ru"
PREVIEW = "--preview" in sys.argv
OUT = os.path.join(ROOT, "_preview") if PREVIEW else ROOT
LANGS = ("ru", "en")


def path_of(lang, slug):
    """Public clean URL path, e.g. /catalog, /en/catalog, /, /en/."""
    base = "/" if lang == "ru" else "/en/"
    return base if slug == "index" else base + slug


def file_of(lang, slug):
    return (slug + ".html") if lang == "ru" else ("en/" + slug + ".html")


def href(cur_lang, lang, slug, anchor=""):
    if not PREVIEW:
        return path_of(lang, slug) + anchor
    up = "../" if cur_lang == "en" else ""
    return up + file_of(lang, slug) + anchor


def asset(cur_lang, p):
    if not PREVIEW:
        return "/assets/" + p
    return ("../" if cur_lang == "en" else "") + "assets/" + p


MARK = ('<svg viewBox="0 0 24 24" fill="none" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M7 10h3v-3l-3.5 -3.5a6 6 0 0 1 8 8l6 6a2 2 0 0 1 -3 3l-6 -6a6 6 0 0 1 -8 -8l3.5 3.5"/></svg>')

CIS_TZ = ("^(Europe\\/(Moscow|Kaliningrad|Samara|Volgograd|Saratov|Ulyanovsk|Astrakhan|Kirov|Simferopol|Minsk|Chisinau)|"
          "Asia\\/(Yekaterinburg|Omsk|Novosibirsk|Barnaul|Tomsk|Novokuznetsk|Krasnoyarsk|Irkutsk|Chita|Yakutsk|Khandyga|"
          "Vladivostok|Ust-Nera|Magadan|Sakhalin|Srednekolymsk|Kamchatka|Anadyr|Almaty|Qostanay|Aqtobe|Aqtau|Atyrau|Oral|"
          "Qyzylorda|Bishkek|Tashkent|Samarkand|Dushanbe|Ashgabat|Yerevan|Baku))$")

# Runs before the page paints: marks JS on, picks the language once per session.
# Rules: a manual choice (saved when the visitor clicks RU/EN) always wins; otherwise
# Russia + CIS time zones or a Russian browser language -> Russian, everything else -> English.
# Search engine bots are never redirected. Nothing leaves the browser.
HEAD_JS = ("(function(){var d=document.documentElement;d.classList.add('js');"
           "if(/bot|crawl|spider|slurp|yandex|google|bing|baidu|duckduck|facebookexternal|telegram|whatsapp|vkshare|lighthouse|headless|prerender|preview/i.test(navigator.userAgent))return;"
           "var L=d.lang,w=null;try{w=localStorage.getItem('dt-lang')}catch(e){}"
           "if(!w){try{if(sessionStorage.getItem('dt-auto'))return;sessionStorage.setItem('dt-auto','1')}catch(e){}"
           "var tz='';try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}"
           "var nl=(navigator.languages&&navigator.languages[0])||navigator.language||'';"
           "w=(/" + CIS_TZ + "/.test(tz)||/^ru/i.test(nl))?'ru':'en'}"
           "if(w!==L&&(w==='ru'||w==='en')){var a=document.querySelector('link[rel=alternate][hreflang='+w+']');"
           "if(a)location.replace(a.getAttribute('href')+location.hash)}})();")


def head(lang, slug, page):
    s = STR[lang]
    title = html.escape(page["title"])
    desc = html.escape(page["desc"])
    canon = DOMAIN + path_of(lang, slug)
    alt = []
    for l in LANGS:
        alt.append('<link rel="alternate" hreflang="%s" href="%s">' % (l, href(lang, l, slug) if PREVIEW else DOMAIN + path_of(l, slug)))
    alt.append('<link rel="alternate" hreflang="x-default" href="%s">' % (href(lang, "ru", slug) if PREVIEW else DOMAIN + path_of("ru", slug)))
    noindex = '<meta name="robots" content="noindex">' if slug == "404" else ""
    org = {
        "@context": "https://schema.org", "@type": "Organization",
        "name": "Dispare Trading", "legalName": s["legal_name_schema"], "url": DOMAIN + path_of(lang, "index"),
        "logo": DOMAIN + "/assets/img/icon-512.png", "taxID": "7733483947", "vatID": "7733483947",
        "email": "distribution@disparetrading.ru", "telephone": "+7-993-903-70-79",
        "address": {"@type": "PostalAddress", "streetAddress": s["schema_street"], "addressLocality": s["schema_city"],
                    "postalCode": "125424", "addressCountry": "RU"},
        "contactPoint": {"@type": "ContactPoint", "telephone": "+7-993-903-70-79", "contactType": "sales",
                         "email": "distribution@disparetrading.ru", "availableLanguage": ["Russian", "English"]},
        "sameAs": [SHOP + "/"],
    }
    og_img = DOMAIN + "/assets/img/og-%s.png" % lang
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{noindex}
<link rel="canonical" href="{canon}">
{''.join(alt)}
<meta name="theme-color" content="#f5f2ec" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1c1915" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dispare Trading">
<meta property="og:locale" content="{'ru_RU' if lang == 'ru' else 'en_US'}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="{asset(lang, 'img/icon.svg')}">
<link rel="icon" type="image/png" sizes="32x32" href="{asset(lang, 'img/icon-32.png')}">
<link rel="apple-touch-icon" href="{asset(lang, 'img/icon-180.png')}">
<link rel="preload" href="{asset(lang, 'fonts/manrope-' + ('cyrillic' if lang == 'ru' else 'latin') + '-wght-normal.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{asset(lang, 'fonts/inter-' + ('cyrillic' if lang == 'ru' else 'latin') + '-wght-normal.woff2')}" as="font" type="font/woff2" crossorigin>
<script>{HEAD_JS}</script>
<link rel="stylesheet" href="{asset(lang, 'css/site.css')}?v=2">
<script type="application/ld+json">{json.dumps(org, ensure_ascii=False)}</script>
</head>
"""


def header(lang, slug):
    s = STR[lang]
    nav = []
    for key in ("about", "catalog", "delivery", "warranty", "contacts"):
        cur = ' aria-current="page"' if key == slug else ""
        nav.append(f'<li><a href="{href(lang, lang, key)}"{cur}>{s["nav"][key]}</a></li>')
    other = "en" if lang == "ru" else "ru"
    switch_slug = "index" if slug == "404" else slug
    if lang == "ru":
        lang_sw = (f'<span aria-current="true">RU</span>'
                   f'<a href="{href(lang, "en", switch_slug)}" hreflang="en" lang="en" data-set-lang="en" title="English version">EN</a>')
    else:
        lang_sw = (f'<a href="{href(lang, "ru", switch_slug)}" hreflang="ru" lang="ru" data-set-lang="ru" title="Русская версия">RU</a>'
                   f'<span aria-current="true">EN</span>')
    return f"""<body>
<a class="skip-link" href="#main">{s['skip']}</a>
<div class="status" role="status" aria-live="off">
  <div class="container">
    <span class="status-pill" data-status-pill><i></i><span>{s['status_hours']}</span></span>
    <span>{s['msk']} <b data-msk-clock>—</b></span>
    <span class="status-hours" data-status-note>{s['hours_short']}</span>
    <span class="status-legal">{s['status_legal']}</span>
  </div>
</div>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{href(lang, lang, 'index')}" aria-label="Dispare Trading — {s['home']}">
      <span class="brand-mark">{MARK}</span>
      <span class="brand-word">Dispare<small>TRADING</small></span>
    </a>
    <nav aria-label="{s['nav_label']}" id="site-nav">
      <ul class="nav-links">
        {''.join(nav)}
        <li class="mobile-only"><a class="btn btn-shop" href="{SHOP}/" target="_blank" rel="noopener"><span class="tag">SHOP</span>{s['shop_btn']} <span class="arrow">→</span></a></li>
      </ul>
    </nav>
    <div class="nav-right">
      <a class="nav-phone" href="tel:+79939037079">+7 993 903-70-79</a>
      <div class="lang" role="group" aria-label="{s['lang_label']}">{lang_sw}</div>
      <a class="btn btn-shop btn-sm" href="{SHOP}/" target="_blank" rel="noopener"><span class="tag">SHOP</span>{s['shop_btn']} <span class="arrow">→</span></a>
      <a class="btn btn-primary btn-sm btn-contact" href="{href(lang, lang, 'contacts')}">{s['contact_btn']}</a>
      <button class="menu-toggle" aria-label="{s['menu']}" aria-expanded="false" aria-controls="site-nav"><span></span></button>
    </div>
  </div>
</header>
"""


def footer(lang):
    s = STR[lang]
    nav = "".join(f'<li><a href="{href(lang, lang, k)}">{s["nav"][k]}</a></li>' for k in ("about", "catalog", "delivery", "warranty", "contacts"))
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="{href(lang, lang, 'index')}"><span class="brand-mark">{MARK}</span><span class="brand-word">Dispare<small>TRADING</small></span></a>
        <p>{s['footer_about']}</p>
      </div>
      <div><h4>{s['f_nav']}</h4><ul>{nav}</ul></div>
      <div><h4>{s['f_docs']}</h4><ul>
        <li><a href="{href(lang, lang, 'privacy')}">{s['privacy']}</a></li>
        <li><a href="{href(lang, lang, 'contacts', '#requisites')}">{s['requisites']}</a></li>
        <li><a href="{SHOP}/" target="_blank" rel="noopener">{s['shop_btn']} ↗</a></li>
      </ul></div>
      <div><h4>{s['f_contacts']}</h4><ul>
        <li><a href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a></li>
        <li><a href="tel:+79939037079">+7 993 903-70-79</a></li>
        <li>{s['hours']}</li>
        <li>{s['warehouse_addr']}</li>
      </ul></div>
    </div>
    <div class="footer-legal">
      <span>© <span data-year>2026</span> {s['legal_line']}</span>
      <span>{s['footer_white']}</span>
    </div>
  </div>
</footer>
<script src="{asset(lang, 'js/site.js')}?v=2" defer></script>
</body>
</html>
"""


def ctx(lang):
    """Helpers available to page bodies as {placeholders}."""
    c = {"shop": SHOP, "mail": "distribution@disparetrading.ru", "tel": "+79939037079"}
    for k in ORDER:
        c["u_" + k] = href(lang, lang, k)
    c["u_other_index"] = href(lang, "en" if lang == "ru" else "ru", "index")
    return c


def render_cats(lang, mode):
    s = STR[lang]
    out = []
    for i, cat in enumerate(CATS, 1):
        name, text = cat[lang]
        code = "%s-%02d" % ("К" if lang == "ru" else "C", i)
        if mode == "home":
            out.append(f'<a class="cat-card" href="{href(lang, lang, "catalog", "#" + cat["id"])}" data-reveal>'
                       f'<span class="code"><span>{code}</span><span>{cat["tag"][lang]}</span></span>{cat["icon"]}'
                       f'<h3>{name}</h3><p>{text}</p><span class="more">{s["more"]} <span>→</span></span></a>')
        else:
            subj = html.escape(s["mail_subject_cat"] % name)
            out.append(f'<div class="cat-card" id="{cat["id"]}" data-reveal>'
                       f'<span class="code"><span>{code}</span><span>{cat["tag"][lang]}</span></span>{cat["icon"]}'
                       f'<h3>{name}</h3><p>{cat["long"][lang]}</p>'
                       f'<div class="cat-actions"><a class="link" href="{SHOP}/" target="_blank" rel="noopener">{s["find_in_shop"]} ↗</a>'
                       f'<a class="link" href="mailto:distribution@disparetrading.ru?subject={subj}">{s["request_quote"]}</a></div></div>')
    return "".join(out)


def build():
    if PREVIEW and os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "en"), exist_ok=True)
    for lang in LANGS:
        for slug in ORDER + ["404"]:
            if slug == "404" and lang == "en":
                continue
            page = PAGES[slug][lang]
            c = ctx(lang)
            c["cats_home"] = render_cats(lang, "home")
            c["cats_full"] = render_cats(lang, "full")
            body = page["body"].format(**c)
            doc = head(lang, slug, page) + header(lang, slug) + '<main id="main">\n' + body + "\n</main>\n" + footer(lang)
            target = os.path.join(OUT, file_of(lang, slug))
            with open(target, "w", encoding="utf-8") as f:
                f.write(doc)
    # sitemap with language alternates
    urls = []
    for lang in LANGS:
        for slug in ORDER:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{DOMAIN}{path_of(l, slug)}"/>' for l in LANGS)
            pr = "1.0" if slug == "index" else ("0.4" if slug == "privacy" else "0.8")
            urls.append(f"  <url><loc>{DOMAIN}{path_of(lang, slug)}</loc>{alts}<changefreq>monthly</changefreq><priority>{pr}</priority></url>")
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sm)
    if PREVIEW:
        shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    print("built", OUT)


if __name__ == "__main__":
    build()

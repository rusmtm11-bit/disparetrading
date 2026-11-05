# -*- coding: utf-8 -*-
"""All site texts, Russian and English side by side.
Page bodies are str.format templates: {u_catalog}, {shop}, {mail}, {cats_home} etc. are filled by build.py.
Do not use literal curly braces in bodies."""

ORDER = ["index", "about", "catalog", "delivery", "warranty", "contacts", "privacy"]

# ---------------------------------------------------------------- shared strings
STR = {
    "ru": {
        "skip": "Перейти к содержимому", "home": "главная", "nav_label": "Основная навигация", "menu": "Меню",
        "lang_label": "Язык сайта",
        "nav": {"about": "О компании", "catalog": "Каталог", "delivery": "Оплата и доставка", "warranty": "Гарантии", "contacts": "Контакты"},
        "shop_btn": "Магазин для партнёров", "contact_btn": "Связаться",
        "status_hours": "Склад", "msk": "МСК", "hours_short": "Пн–Пт 10:00–18:00",
        "status_legal": "ООО «ДИСПЭР» · ИНН 7733483947 · работаем с НДС",
        "footer_about": "Импорт и оптовая поставка автозапчастей и шин для юридических лиц и ИП. Договор, НДС, ЭДО — каждая сделка по закону.",
        "f_nav": "Разделы", "f_docs": "Документы", "f_contacts": "Контакты",
        "privacy": "Политика обработки персональных данных", "requisites": "Реквизиты компании",
        "hours": "Пн–Пт, 10:00–18:00 (МСК)",
        "warehouse_addr": "Склад: д. Кузяево, с2, Дмитровский м. о., Московская область",
        "legal_line": "ООО «ДИСПЭР» · ИНН 7733483947 · ОГРН 1267700136582",
        "footer_white": "Работаем строго в белую",
        "more": "Подробнее", "find_in_shop": "Найти в магазине", "request_quote": "Запросить КП",
        "mail_subject_cat": "Запрос КП: %s",
        "legal_name_schema": "ООО «ДИСПЭР»",
        "schema_street": "ш. Волоколамское, д. 71, к. 4, помещ. 70К", "schema_city": "Москва",
    },
    "en": {
        "skip": "Skip to content", "home": "home", "nav_label": "Main navigation", "menu": "Menu",
        "lang_label": "Site language",
        "nav": {"about": "About", "catalog": "Catalogue", "delivery": "Payment & delivery", "warranty": "Warranty", "contacts": "Contacts"},
        "shop_btn": "Partner store", "contact_btn": "Contact us",
        "status_hours": "Warehouse", "msk": "Moscow time", "hours_short": "Mon–Fri 10:00–18:00",
        "status_legal": "DISPER LLC · Tax ID (INN) 7733483947 · VAT registered",
        "footer_about": "Import and wholesale supply of auto parts and tyres to businesses in Russia. Contract, VAT, electronic documents — every deal by the book.",
        "f_nav": "Sections", "f_docs": "Documents", "f_contacts": "Contacts",
        "privacy": "Personal data policy", "requisites": "Company details",
        "hours": "Mon–Fri, 10:00–18:00 (Moscow time)",
        "warehouse_addr": "Warehouse: Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region, Russia",
        "legal_line": "DISPER LLC (ООО «ДИСПЭР») · INN 7733483947 · OGRN 1267700136582",
        "footer_white": "Fully compliant, fully documented",
        "more": "Learn more", "find_in_shop": "Find in the store", "request_quote": "Request a quote",
        "mail_subject_cat": "Quote request: %s",
        "legal_name_schema": "DISPER LLC (ООО «ДИСПЭР»)",
        "schema_street": "71 Volokolamskoe Highway, bldg 4, premises 70K", "schema_city": "Moscow",
    },
}

# ---------------------------------------------------------------- category icons
def _ico(inner):
    return '<svg viewBox="0 0 44 44" fill="none" stroke-width="1.5" aria-hidden="true">' + inner + "</svg>"

CATS = [
    {"id": "engine", "tag": {"ru": "ДВС", "en": "ENGINE"},
     "icon": _ico('<rect class="i" x="10" y="14" width="24" height="18" rx="2"/><rect class="a" x="14" y="8" width="16" height="6" rx="1"/><line class="i" x1="16" y1="20" x2="28" y2="20"/><line class="i" x1="16" y1="25" x2="28" y2="25"/>'),
     "ru": ("Двигатель и ДВС", "Поршневая группа, ГРМ, прокладки, турбины."),
     "en": ("Engine", "Pistons and rings, timing parts, gaskets, turbochargers."),
     "long": {"ru": "Поршневая группа, ГРМ (ремни, цепи, ролики), прокладки, турбины, системы охлаждения.",
              "en": "Pistons and rings, timing belts, chains and pulleys, gaskets, turbochargers, cooling systems."}},
    {"id": "transmission", "tag": {"ru": "КПП", "en": "DRIVETRAIN"},
     "icon": _ico('<circle class="i" cx="22" cy="22" r="10"/><circle class="a" cx="22" cy="22" r="3.6"/><g class="i"><line x1="22" y1="9" x2="22" y2="13"/><line x1="22" y1="31" x2="22" y2="35"/><line x1="9" y1="22" x2="13" y2="22"/><line x1="31" y1="22" x2="35" y2="22"/></g>'),
     "ru": ("Трансмиссия и мосты", "КПП, сцепление, раздатки, полуоси."),
     "en": ("Transmission & axles", "Gearboxes, clutches, transfer cases, drive shafts."),
     "long": {"ru": "КПП (МКПП/АКПП), сцепление, раздаточные коробки, редукторы, полуоси, приводные валы.",
              "en": "Manual and automatic gearboxes, clutches, transfer cases, differentials, half-shafts, drive shafts."}},
    {"id": "chassis", "tag": {"ru": "ШИНЫ", "en": "TYRES"},
     "icon": _ico('<circle class="i" cx="22" cy="22" r="12"/><circle class="a" cx="22" cy="22" r="5"/><circle class="f" cx="22" cy="22" r="1.6"/>'),
     "ru": ("Ходовая часть и шины", "Рычаги, амортизаторы, ступицы, шины."),
     "en": ("Suspension & tyres", "Control arms, shock absorbers, hubs, tyres."),
     "long": {"ru": "Рычаги, амортизаторы, стойки, сайлентблоки, ступицы, подшипники; шины основных типоразмеров.",
              "en": "Control arms, shock absorbers, struts, bushings, hubs, bearings; tyres in common sizes."}},
    {"id": "brakes", "tag": {"ru": "ТОРМОЗА", "en": "BRAKES"},
     "icon": _ico('<circle class="i" cx="22" cy="22" r="12"/><circle class="a" cx="22" cy="22" r="12" stroke-dasharray="1 5"/><rect class="f" x="19" y="19" width="6" height="6"/>'),
     "ru": ("Тормозная система", "Диски, колодки, суппорты, барабаны."),
     "en": ("Brakes", "Discs, pads, calipers, drums."),
     "long": {"ru": "Диски, колодки, суппорты, барабаны, тормозные шланги и трубки, датчики износа.",
              "en": "Discs, pads, calipers, drums, brake hoses and lines, wear sensors."}},
    {"id": "electric", "tag": {"ru": "ЭЛЕКТРИКА", "en": "ELECTRICS"},
     "icon": _ico('<path class="a" d="M23 8L12 24h9l-2 12 13-18h-9l2-10z" stroke-linejoin="round"/>'),
     "ru": ("Электрика и оптика", "Генераторы, стартеры, датчики, фары."),
     "en": ("Electrics & lighting", "Alternators, starters, sensors, headlights."),
     "long": {"ru": "Генераторы, стартеры, датчики, проводка, фары, фонари.",
              "en": "Alternators, starters, sensors, wiring, headlights, tail lights."}},
    {"id": "consumables", "tag": {"ru": "ТО", "en": "SERVICE"},
     "icon": _ico('<path class="i" d="M22 8c5 6 8 10.5 8 15a8 8 0 1 1-16 0c0-4.5 3-9 8-15z"/><path class="a" d="M18 25a4 4 0 0 0 4 4"/>'),
     "ru": ("Расходники и фильтры", "Масла, фильтры, ремни, свечи — крупный и мелкий опт."),
     "en": ("Service parts & filters", "Oils, filters, belts, spark plugs — in any wholesale volume."),
     "long": {"ru": "Моторные и трансмиссионные масла, масляные, воздушные и салонные фильтры, ремни, свечи зажигания.",
              "en": "Engine and transmission oils, oil, air and cabin filters, belts, spark plugs."}},
]

# ---------------------------------------------------------------- hero illustration (shared)
def hero_svg(l1, l2, l3, aria):
    return f"""<svg viewBox="0 0 480 440" role="img" aria-label="{aria}">
  <circle class="hv-line" cx="240" cy="220" r="170" fill="none" stroke-width="1"/>
  <g class="wheel">
    <circle class="hv-gold" cx="240" cy="220" r="150" fill="none" stroke-width="1.5" stroke-dasharray="2 7"/>
    <circle class="hv-paper-fill hv-ink" cx="240" cy="220" r="112" stroke-width="1.5"/>
    <circle class="hv-ink" cx="240" cy="220" r="112" fill="none" stroke-width="11" stroke-dasharray="4 14" opacity=".55"/>
    <circle class="hv-ink" cx="240" cy="220" r="84" fill="none" stroke-width="1"/>
    <g class="hv-ink" stroke-width="1.5">
      <line x1="240" y1="136" x2="240" y2="174"/><line x1="240" y1="266" x2="240" y2="304"/>
      <line x1="156" y1="220" x2="194" y2="220"/><line x1="286" y1="220" x2="324" y2="220"/>
      <line x1="180.6" y1="160.6" x2="207.5" y2="187.5"/><line x1="272.5" y1="252.5" x2="299.4" y2="279.4"/>
      <line x1="299.4" y1="160.6" x2="272.5" y2="187.5"/><line x1="207.5" y1="252.5" x2="180.6" y2="279.4"/>
    </g>
    <circle class="hv-ink-fill" cx="240" cy="220" r="46"/>
    <circle class="hv-gold" cx="240" cy="220" r="46" fill="none" stroke-width="2"/>
    <g transform="translate(240,220) scale(2.6) translate(-12,-12)">
      <path class="hv-gold" d="M7 10h3v-3l-3.5 -3.5a6 6 0 0 1 8 8l6 6a2 2 0 0 1 -3 3l-6 -6a6 6 0 0 1 -8 -8l3.5 3.5" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <circle class="hv-gold-fill" cx="240" cy="70" r="4"/><circle class="hv-gold-fill" cx="390" cy="220" r="4"/>
    <circle class="hv-gold-fill" cx="240" cy="370" r="4"/><circle class="hv-gold-fill" cx="90" cy="220" r="4"/>
  </g>
  <path class="hv-accent dim" d="M70 50 V110 M62 50 H78 M62 110 H78" fill="none" stroke-width="1.2"/>
  <path class="hv-line dim" d="M70 80 H150" fill="none" stroke-width="1"/>
  <text class="hv-label hv-tag" x="82" y="70">{l1}</text>
  <path class="hv-accent dim" d="M410 330 V400 M402 330 H418 M402 400 H418" fill="none" stroke-width="1.2"/>
  <path class="hv-line dim" d="M330 365 H410" fill="none" stroke-width="1"/>
  <text class="hv-label hv-tag" x="408" y="425" text-anchor="end">{l2}</text>
  <path class="hv-gold dim" d="M300 44 H462" fill="none" stroke-width="1"/>
  <text class="hv-label hv-label-strong hv-tag" x="462" y="34" text-anchor="end">{l3}</text>
</svg>"""


# ---------------------------------------------------------------- shared blocks
def shop_band(t):
    return f"""<section class="section" aria-labelledby="shop-h">
  <div class="container">
    <div class="shop" data-reveal>
      <div>
        <div class="graph">{t['g']}</div>
        <h2 id="shop-h">{t['h']}</h2>
        <p style="margin-top:14px">{t['p']}</p>
        <ul class="shop-list"><li>{t['l1']}</li><li>{t['l2']}</li><li>{t['l3']}</li></ul>
      </div>
      <div>
        <form class="shop-search" action="{{shop}}/search" method="get" target="_blank" data-shop-search role="search">
          <label for="pcode">{t['label']}</label>
          <div class="row">
            <input id="pcode" name="pcode" type="search" inputmode="text" autocomplete="off" spellcheck="false" placeholder="{t['ph']}" maxlength="40" required>
            <button class="btn btn-light" type="submit">{t['btn']} <span class="arrow">→</span></button>
          </div>
          <div class="shop-links">
            <a href="{{shop}}/" target="_blank" rel="noopener">{t['open']} ↗</a>
            <a href="{{shop}}/reg" target="_blank" rel="noopener">{t['reg']} ↗</a>
          </div>
          <p class="shop-note">{t['note']}</p>
        </form>
      </div>
    </div>
  </div>
</section>"""


def stamp_svg(ring, core, sub, aria):
    return f"""<svg class="stamp" viewBox="0 0 200 200" role="img" aria-label="{aria}">
  <defs><path id="stamp-ring" d="M100,100 m-75,0 a75,75 0 1,1 150,0 a75,75 0 1,1 -150,0"/></defs>
  <circle cx="100" cy="100" r="93" stroke-width="2.6"/><circle cx="100" cy="100" r="86" stroke-width=".8"/>
  <circle cx="100" cy="100" r="60" stroke-width="1.2"/>
  <text font-size="10.5" letter-spacing="1.3"><textPath href="#stamp-ring">{ring}</textPath></text>
  <text class="core" x="100" y="99" text-anchor="middle" font-size="17">{core}</text>
  <text x="100" y="119" text-anchor="middle" font-size="10" letter-spacing="1.6">{sub}</text>
</svg>"""


def cta(h, p, mail_subject, b1, b2, shop):
    return f"""<section class="section" style="padding-top:0">
  <div class="container">
    <div class="cta" data-reveal>
      <div><h2>{h}</h2><p>{p}</p></div>
      <div class="cta-actions">
        <a class="btn btn-primary" href="mailto:{{mail}}?subject={mail_subject}">{b1}</a>
        <a class="btn btn-outline" href="tel:{{tel}}">{b2}</a>
        <a class="btn btn-shop" href="{{shop}}/" target="_blank" rel="noopener"><span class="tag">SHOP</span>{shop} <span class="arrow">→</span></a>
      </div>
    </div>
  </div>
</section>"""


def page_hero(crumb_home, crumb_home_url, crumb, graph, h1, p):
    return f"""<section class="page-hero ledger">
  <div class="container" data-reveal>
    <div class="crumbs"><a href="{crumb_home_url}">{crumb_home}</a><span>/</span><span>{crumb}</span></div>
    <div class="graph">{graph}</div>
    <h1>{h1}</h1>
    <p>{p}</p>
  </div>
</section>"""


MAP = ('<iframe class="map-frame" src="https://yandex.ru/map-widget/v1/?text=%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20'
       '%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%2C%20%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3%2C%20'
       '%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BD%D1%8F%20%D0%9A%D1%83%D0%B7%D1%8F%D0%B5%D0%B2%D0%BE%2C%20%D1%812" title="%s" loading="lazy"></iframe>')
MAP_LINK = "https://yandex.ru/maps/?text=%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%2C%20%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3%2C%20%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BD%D1%8F%20%D0%9A%D1%83%D0%B7%D1%8F%D0%B5%D0%B2%D0%BE"

MARQUEE = {
    "ru": ["Двигатель и ДВС", "Трансмиссия", "Ходовая часть", "Шины", "Тормозная система", "Электрика и оптика", "Фильтры", "Масла и расходники"],
    "en": ["Engine", "Transmission", "Suspension", "Tyres", "Brakes", "Electrics & lighting", "Filters", "Oils & service parts"],
}


def marquee(lang):
    items = "".join(f'<span class="marquee-item">{x}</span>' for x in MARQUEE[lang])
    return f'<div class="marquee" aria-hidden="true"><div class="marquee-track">{items}{items}</div></div>'


# ================================================================= PAGES
PAGES = {}

# ---------------------------------------------------------------- HOME
PAGES["index"] = {
    "ru": {
        "title": "Dispare Trading — автозапчасти и шины оптом для бизнеса, строго в белую",
        "desc": "ООО «ДИСПЭР»: импорт и оптовая поставка автозапчастей и шин юрлицам и ИП. Договор, НДС, УПД через ЭДО, склад в Московской области, доставка по России. Магазин для партнёров — shop.disparetrading.ru.",
        "body": f"""<section class="hero ledger">
  <div class="container hero-grid">
    <div data-reveal>
      <div class="graph">00 / Импорт · опт · B2B</div>
      <h1>Автозапчасти и шины оптом — <em>строго в&nbsp;белую</em></h1>
      <p class="hero-sub">Сами импортируем товар — таможенное оформление на нашу компанию, — храним на складе в Московской области и поставляем юрлицам и ИП по договору с НДС.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="mailto:{{mail}}?subject=%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81%20%D0%9A%D0%9F">Запросить КП</a>
        <a class="btn btn-shop" href="{{shop}}/" target="_blank" rel="noopener"><span class="tag">SHOP</span>Магазин для партнёров <span class="arrow">→</span></a>
      </div>
      <dl class="hero-facts">
        <div><dt>Форма работы</dt><dd>Договор · НДС · УПД</dd></div>
        <div><dt>Склад</dt><dd>Московская область</dd></div>
        <div><dt>Доставка</dt><dd>Любой регион России</dd></div>
      </dl>
    </div>
    <div class="hero-visual" data-reveal>{hero_svg("ЗАПЧАСТИ / ШИНЫ", "СКЛАД · МОСКОВСКАЯ ОБЛ.", "ДОГОВОР · НДС · ЭДО", "Схематичное колесо с гаечным ключом — знак Dispare Trading")}</div>
  </div>
</section>
{marquee("ru")}
{shop_band(dict(g="01 / Магазин для партнёров", h="Знаете артикул? Заказывайте в магазине для партнёров",
                p="shop.disparetrading.ru — наш интернет-магазин для постоянных клиентов: цены, наличие и заказ в пару кликов.",
                l1="Поиск по артикулу и VIN", l2="Подбор запчастей по автомобилю", l3="Корзина, заказы и их история в личном кабинете",
                label="Поиск по артикулу", ph="Например, 0446533480", btn="Найти", open="Перейти в магазин", reg="Регистрация",
                note="Откроется в новой вкладке на shop.disparetrading.ru."))}
<section class="section section-alt" aria-labelledby="trust-h">
  <div class="container">
    <div class="section-head" data-reveal>
      <div class="graph">02 / Прозрачность</div>
      <h2 id="trust-h">Работаем строго в белую — и это можно проверить за минуту</h2>
      <p>Каждая сделка оформляется по закону: договор, безналичная оплата с НДС, закрывающие документы через ЭДО.</p>
    </div>
    <div class="trust-wrap">
      <div class="stamp-col">
        {stamp_svg("ООО «ДИСПЭР» · ИНН 7733483947 · РАБОТАЕМ С НДС ·", "ПРОВЕРЕНО", "ОСНО · ДОГОВОР · ЭДО", "Печать: ООО «ДИСПЭР», ИНН 7733483947, работаем с НДС")}
        <p class="stamp-caption">ООО «ДИСПЭР» — юридическое лицо на общей системе налогообложения, плательщик НДС.</p>
      </div>
      <div>
        <div class="ledger-grid">
          <div class="cell" data-reveal><div class="n">Г-01</div><h3>ООО на ОСНО, с НДС</h3><p class="fig">ИНН 7733483947 <button class="copy" type="button" data-copy="7733483947">Копировать</button></p><a href="https://egrul.nalog.ru/" target="_blank" rel="noopener">Проверить в ФНС ↗</a></div>
          <div class="cell" data-reveal><div class="n">Г-02</div><h3>Договор поставки</h3><p>Цены, сроки и гарантия закреплены в договоре.</p><p class="fig">Договор · счёт · УПД</p></div>
          <div class="cell" data-reveal><div class="n">Г-03</div><h3>Электронный документооборот</h3><p>Обмениваемся документами с электронной подписью — без потерь и ожидания почты.</p><p class="fig">УПД через оператора ЭДО</p></div>
          <div class="cell" data-reveal><div class="n">Г-04</div><h3>Импорт на нашу компанию</h3><p>Таможенное оформление — на ООО «ДИСПЭР». Копии таможенных документов на партию — по запросу.</p></div>
          <div class="cell" data-reveal><div class="n">Г-05</div><h3>Только безналичный расчёт</h3><p>Оплата на расчётный счёт компании. Наличные без документов не принимаем.</p><p class="fig">Р/с в АО «ТБанк»</p></div>
          <div class="cell" data-reveal><div class="n">Г-06</div><h3>Гарантия по закону</h3><p>Порядок работы с браком прописан в договоре и соответствует ГК РФ.</p><a href="{{u_warranty}}">Условия гарантии →</a></div>
        </div>
        <p class="trust-pledge" data-reveal>Не работаем за наличные без документов и не продаём товар без таможенного оформления. Нужен поставщик, с которым спокойно пройдёт любая проверка, — давайте работать.</p>
      </div>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="cat-h">
  <div class="container">
    <div class="section-head" data-reveal>
      <div class="graph">03 / Каталог</div>
      <h2 id="cat-h">Основные категории поставок</h2>
      <p>Открытого прайса здесь нет: цена зависит от объёма партии и курса. Ищите позиции в магазине для партнёров или пришлите список — подготовим коммерческое предложение.</p>
    </div>
    <div class="cat-grid">{{cats_home}}</div>
  </div>
</section>
<section class="section on-dark" aria-labelledby="steps-h">
  <div class="container">
    <div class="section-head" data-reveal>
      <div class="graph">04 / Как мы работаем</div>
      <h2 id="steps-h">От заявки до отгрузки — четыре понятных шага</h2>
    </div>
    <div class="steps"><div class="progress"></div>
      <div class="step" data-reveal><div class="step-num">01</div><h3>Заявка</h3><p>Присылаете список артикулов, VIN или марку и модель — подбираем варианты.</p></div>
      <div class="step" data-reveal><div class="step-num">02</div><h3>КП и договор</h3><p>Готовим коммерческое предложение, заключаем договор поставки, выставляем счёт с НДС.</p></div>
      <div class="step" data-reveal><div class="step-num">03</div><h3>Оплата</h3><p>Безналичный расчёт на счёт компании. Порядок оплаты закрепляем в договоре.</p></div>
      <div class="step" data-reveal><div class="step-num">04</div><h3>Отгрузка</h3><p>Самовывоз со склада или транспортная компания в любой регион. УПД — через ЭДО.</p></div>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="aud-h">
  <div class="container">
    <div class="section-head" data-reveal>
      <div class="graph">05 / С кем работаем</div>
      <h2 id="aud-h">Поставляем бизнесу, которому важны документы</h2>
    </div>
    <div class="aud" data-reveal>
      <div><div class="k">А-01</div><h3>СТО и автосервисы</h3><p>Регулярные поставки запчастей и расходников под ремонт.</p></div>
      <div><div class="k">А-02</div><h3>Сети автосервисов</h3><p>Стабильные поставки и единый порядок документов.</p></div>
      <div><div class="k">А-03</div><h3>Магазины и дистрибьюторы</h3><p>Партии для перепродажи с полным пакетом документов.</p></div>
      <div><div class="k">А-04</div><h3>Корпоративные автопарки</h3><p>Обслуживание парка по договору, с НДС.</p></div>
    </div>
  </div>
</section>
{cta("Готовы обсудить поставку?", "Пришлите список позиций на почту — ответим в рабочее время и подготовим предложение под ваш объём.", "%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81%20%D0%9A%D0%9F", "Написать на почту", "Позвонить", "Магазин")}""",
    },
    "en": {
        "title": "Dispare Trading — wholesale auto parts and tyres in Russia, fully compliant",
        "desc": "DISPER LLC imports and supplies auto parts and tyres wholesale to businesses in Russia. Written contract, VAT invoicing, electronic documents, warehouse in the Moscow region, delivery across Russia.",
        "body": f"""<section class="hero ledger">
  <div class="container hero-grid">
    <div data-reveal>
      <div class="graph">00 / Import · wholesale · B2B</div>
      <h1>Wholesale auto parts and tyres — <em>fully compliant</em></h1>
      <p class="hero-sub">We import goods ourselves — cleared through customs in our company's name — store them at our warehouse in the Moscow region and supply businesses under contract, with VAT invoicing.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="mailto:{{mail}}?subject=Quote%20request">Request a quote</a>
        <a class="btn btn-shop" href="{{shop}}/" target="_blank" rel="noopener"><span class="tag">SHOP</span>Partner store <span class="arrow">→</span></a>
      </div>
      <dl class="hero-facts">
        <div><dt>Terms</dt><dd>Contract · VAT · e-docs</dd></div>
        <div><dt>Warehouse</dt><dd>Moscow region, Russia</dd></div>
        <div><dt>Delivery</dt><dd>Anywhere in Russia</dd></div>
      </dl>
    </div>
    <div class="hero-visual" data-reveal>{hero_svg("PARTS / TYRES", "WAREHOUSE · MOSCOW REGION", "CONTRACT · VAT · E-DOCS", "A stylised wheel with a wrench — the Dispare Trading mark")}</div>
  </div>
</section>
{marquee("en")}
{shop_band(dict(g="01 / Partner store", h="Know the part number? Order in our partner store",
                p="shop.disparetrading.ru is our online store for regular customers: prices, stock and ordering in a few clicks. The store interface is in Russian.",
                l1="Search by part number and VIN", l2="Parts lookup by vehicle", l3="Cart, orders and order history in your account",
                label="Part number search", ph="e.g. 0446533480", btn="Search", open="Open the store", reg="Register",
                note="Opens in a new tab on shop.disparetrading.ru (in Russian)."))}
<section class="section section-alt" aria-labelledby="trust-h">
  <div class="container">
    <div class="section-head" data-reveal>
      <div class="graph">02 / Transparency</div>
      <h2 id="trust-h">Fully compliant — and you can verify it in a minute</h2>
      <p>Every deal is done by the book: a written contract, bank transfer with VAT, and closing documents exchanged electronically.</p>
    </div>
    <div class="trust-wrap">
      <div class="stamp-col">
        {stamp_svg("DISPER LLC · INN 7733483947 · VAT REGISTERED ·", "VERIFIED", "CONTRACT · VAT · E-DOCS", "Seal: DISPER LLC, tax ID 7733483947, VAT registered")}
        <p class="stamp-caption">DISPER LLC (ООО «ДИСПЭР») is a Russian legal entity on the general taxation system and a VAT payer.</p>
      </div>
      <div>
        <div class="ledger-grid">
          <div class="cell" data-reveal><div class="n">G-01</div><h3>Registered LLC, VAT payer</h3><p class="fig">INN 7733483947 <button class="copy" type="button" data-copy="7733483947">Copy</button></p><a href="https://egrul.nalog.ru/" target="_blank" rel="noopener">Check in the tax register ↗</a></div>
          <div class="cell" data-reveal><div class="n">G-02</div><h3>Supply contract</h3><p>Prices, lead times and warranty are set out in a written contract.</p><p class="fig">Contract · invoice · UPD</p></div>
          <div class="cell" data-reveal><div class="n">G-03</div><h3>Electronic documents</h3><p>We exchange documents with electronic signatures — nothing gets lost in the post.</p><p class="fig">UPD via an EDI operator</p></div>
          <div class="cell" data-reveal><div class="n">G-04</div><h3>Imported in our name</h3><p>Customs clearance is done in the name of DISPER LLC. Copies of customs documents for a batch are available on request.</p></div>
          <div class="cell" data-reveal><div class="n">G-05</div><h3>Bank transfers only</h3><p>Payments go to the company's bank account. We never accept undocumented cash.</p><p class="fig">Account at T-Bank JSC</p></div>
          <div class="cell" data-reveal><div class="n">G-06</div><h3>Statutory warranty</h3><p>Defect handling is set out in the contract in line with the Russian Civil Code.</p><a href="{{u_warranty}}">Warranty terms →</a></div>
        </div>
        <p class="trust-pledge" data-reveal>We never take undocumented cash and never sell goods that have not cleared customs. If you need a supplier who passes any audit, let's work together.</p>
      </div>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="cat-h">
  <div class="container">
    <div class="section-head" data-reveal>
      <div class="graph">03 / Catalogue</div>
      <h2 id="cat-h">Main product categories</h2>
      <p>There is no public price list here: prices depend on batch size and exchange rates. Search the partner store or send us your list — we will prepare a quote.</p>
    </div>
    <div class="cat-grid">{{cats_home}}</div>
  </div>
</section>
<section class="section on-dark" aria-labelledby="steps-h">
  <div class="container">
    <div class="section-head" data-reveal>
      <div class="graph">04 / How we work</div>
      <h2 id="steps-h">From request to shipment in four clear steps</h2>
    </div>
    <div class="steps"><div class="progress"></div>
      <div class="step" data-reveal><div class="step-num">01</div><h3>Request</h3><p>Send us a list of part numbers, a VIN or the make and model — we find the options.</p></div>
      <div class="step" data-reveal><div class="step-num">02</div><h3>Quote and contract</h3><p>We prepare a commercial offer, sign a supply contract and issue a VAT invoice.</p></div>
      <div class="step" data-reveal><div class="step-num">03</div><h3>Payment</h3><p>Bank transfer to the company account. Payment terms are fixed in the contract.</p></div>
      <div class="step" data-reveal><div class="step-num">04</div><h3>Shipment</h3><p>Pick-up from the warehouse or a carrier to any region. UPD sent electronically.</p></div>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="aud-h">
  <div class="container">
    <div class="section-head" data-reveal>
      <div class="graph">05 / Who we work with</div>
      <h2 id="aud-h">We supply businesses that care about paperwork</h2>
    </div>
    <div class="aud" data-reveal>
      <div><div class="k">A-01</div><h3>Repair shops</h3><p>Regular supplies of parts and consumables for repairs.</p></div>
      <div><div class="k">A-02</div><h3>Service chains</h3><p>Steady supply and one consistent set of documents.</p></div>
      <div><div class="k">A-03</div><h3>Retailers and distributors</h3><p>Batches for resale with a full document package.</p></div>
      <div><div class="k">A-04</div><h3>Corporate fleets</h3><p>Fleet maintenance supplies under contract, with VAT.</p></div>
    </div>
  </div>
</section>
{cta("Ready to discuss a supply?", "Email us your list of items — we reply during business hours (Moscow time) with an offer for your volume.", "Quote%20request", "Email us", "Call", "Store")}""",
    },
}

# ---------------------------------------------------------------- ABOUT
PAGES["about"] = {
    "ru": {
        "title": "О компании — Dispare Trading (ООО «ДИСПЭР»)",
        "desc": "Dispare Trading — импортёр и оптовый поставщик автозапчастей и шин. Таможенное оформление на свою компанию, склад в Московской области, работа по договору с НДС.",
        "body": page_hero("Главная", "{u_index}", "О компании", "О компании", "Dispare Trading — импортёр и оптовый поставщик автозапчастей",
                          "Сами везём товар из-за рубежа, оформляем его на свою компанию и поставляем бизнесу по России. Меньше звеньев в цепочке — понятнее цена и документы.") + """
<section class="section">
  <div class="container two-col">
    <div data-reveal>
      <div class="graph">01 / Чем мы занимаемся</div>
      <h2 style="margin-bottom:18px">Импорт и оптовая дистрибуция</h2>
      <p>Dispare Trading (ООО «ДИСПЭР») импортирует автозапчасти и шины и поставляет их оптом по России. Работаем с автосервисами, сетями СТО, магазинами, дистрибьюторами и другими компаниями, которым нужны стабильные поставки в договорном формате.</p>
      <p>Товар проходит таможню на нашу компанию, хранится на складе в Московской области и проверяется перед отгрузкой. В России между таможней и вами — только мы, поэтому за каждую позицию отвечаем сами.</p>
    </div>
    <div data-reveal>
      <div class="graph">02 / Принципы работы</div>
      <ol class="principles">
        <li><div><b>Прозрачные документы</b><span>Договор, счёт, УПД и закрывающие документы — по каждой сделке.</span></div></li>
        <li><div><b>Только белые расчёты</b><span>Безналичная оплата на счёт компании с НДС. Наличные без документов не принимаем.</span></div></li>
        <li><div><b>Ответственность за качество</b><span>Гарантия и порядок работы с браком закреплены в договоре.</span></div></li>
        <li><div><b>Долгосрочные отношения</b><span>Ориентируемся на постоянных партнёров, а не на разовые сделки.</span></div></li>
        <li><div><b>ЭДО и маркировка</b><span>Ведём электронный документооборот с контрагентами; для товаров, подлежащих маркировке, работаем с «Честным знаком».</span></div></li>
      </ol>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head" data-reveal><div class="graph">03 / Логистика</div><h2>Импорт, склад, отгрузка</h2></div>
    <div class="tiles">
      <div class="tile" data-reveal><div class="n">Л-01</div><h3>Импорт</h3><p>Закупка у проверенных зарубежных поставщиков, таможенное оформление на ООО «ДИСПЭР».</p></div>
      <div class="tile" data-reveal><div class="n">Л-02</div><h3>Склад</h3><p>Приёмка, проверка и хранение товара на складе в Московской области.</p></div>
      <div class="tile" data-reveal><div class="n">Л-03</div><h3>Отгрузка</h3><p>Самовывоз или отправка транспортной компанией в любой регион России.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container two-col">
    <div data-reveal>
      <div class="graph">04 / Карточка компании</div>
      <h2 style="margin-bottom:14px">Проверьте нас до первой сделки</h2>
      <p>Все данные открыты. Выписку из ЕГРЮЛ можно получить бесплатно на сайте ФНС по ИНН.</p>
      <p><a class="link" href="https://egrul.nalog.ru/" target="_blank" rel="noopener">Открыть сервис ФНС ↗</a> &nbsp; <a class="link" href="{u_contacts}#requisites">Все реквизиты →</a></p>
    </div>
    <table class="sheet" data-reveal>
      <tr><th>Наименование</th><td>ООО «ДИСПЭР»</td></tr>
      <tr><th>ИНН / КПП</th><td class="mono">7733483947 / 773301001</td></tr>
      <tr><th>ОГРН</th><td class="mono">1267700136582</td></tr>
      <tr><th>Налогообложение</th><td>Общая система (ОСНО), плательщик НДС</td></tr>
      <tr><th>Юридический адрес</th><td>125424, г. Москва, ш. Волоколамское, д. 71, к. 4, помещ. 70К</td></tr>
      <tr><th>Склад</th><td>Московская обл., Дмитровский м. о., д. Кузяево, с2</td></tr>
    </table>
  </div>
</section>
""" + cta("Хотите стать партнёром?", "Расскажите о компании и потребностях в поставках — обсудим условия сотрудничества.", "%D0%A1%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE", "Написать на почту", "Позвонить", "Магазин"),
    },
    "en": {
        "title": "About — Dispare Trading (DISPER LLC)",
        "desc": "Dispare Trading is an importer and wholesale supplier of auto parts and tyres in Russia. Customs clearance in our own name, a warehouse in the Moscow region, contracts with VAT.",
        "body": page_hero("Home", "{u_index}", "About", "About us", "Dispare Trading — auto parts importer and wholesale supplier",
                          "We bring goods from abroad, clear them through customs in our own name and supply businesses across Russia. Fewer links in the chain means clearer prices and paperwork.") + """
<section class="section">
  <div class="container two-col">
    <div data-reveal>
      <div class="graph">01 / What we do</div>
      <h2 style="margin-bottom:18px">Import and wholesale distribution</h2>
      <p>Dispare Trading (DISPER LLC, ООО «ДИСПЭР») imports auto parts and tyres and supplies them wholesale across Russia. Our customers are repair shops, service chains, retailers, distributors and other companies that need steady supplies under a contract.</p>
      <p>Goods clear customs in our company's name, are stored at our warehouse in the Moscow region and are checked before shipment. Inside Russia, there is nobody between customs and you but us — so we take responsibility for every item.</p>
    </div>
    <div data-reveal>
      <div class="graph">02 / How we operate</div>
      <ol class="principles">
        <li><div><b>Transparent paperwork</b><span>Contract, invoice, UPD and closing documents for every deal.</span></div></li>
        <li><div><b>Clean payments only</b><span>Bank transfer to the company account with VAT. No undocumented cash.</span></div></li>
        <li><div><b>Responsibility for quality</b><span>Warranty and defect handling are written into the contract.</span></div></li>
        <li><div><b>Long-term partnerships</b><span>We focus on regular partners rather than one-off deals.</span></div></li>
        <li><div><b>E-documents and product marking</b><span>We exchange documents electronically with counterparties and use the national "Chestny Znak" marking system for goods that require it.</span></div></li>
      </ol>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head" data-reveal><div class="graph">03 / Logistics</div><h2>Import, warehouse, shipment</h2></div>
    <div class="tiles">
      <div class="tile" data-reveal><div class="n">L-01</div><h3>Import</h3><p>Purchasing from vetted foreign suppliers, customs clearance in the name of DISPER LLC.</p></div>
      <div class="tile" data-reveal><div class="n">L-02</div><h3>Warehouse</h3><p>Receiving, inspection and storage at our warehouse in the Moscow region.</p></div>
      <div class="tile" data-reveal><div class="n">L-03</div><h3>Shipment</h3><p>Pick-up or dispatch by a carrier to any region of Russia.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container two-col">
    <div data-reveal>
      <div class="graph">04 / Company card</div>
      <h2 style="margin-bottom:14px">Check us before the first deal</h2>
      <p>All our details are public. An extract from the Russian state register of legal entities (EGRUL) is available free of charge on the Federal Tax Service website by tax ID.</p>
      <p><a class="link" href="https://egrul.nalog.ru/" target="_blank" rel="noopener">Open the tax service ↗</a> &nbsp; <a class="link" href="{u_contacts}#requisites">All company details →</a></p>
    </div>
    <table class="sheet" data-reveal>
      <tr><th>Legal name</th><td>DISPER LLC (ООО «ДИСПЭР»)</td></tr>
      <tr><th>INN / KPP</th><td class="mono">7733483947 / 773301001</td></tr>
      <tr><th>OGRN</th><td class="mono">1267700136582</td></tr>
      <tr><th>Taxation</th><td>General taxation system (OSNO), VAT payer</td></tr>
      <tr><th>Registered address</th><td>71 Volokolamskoe Highway, bldg 4, premises 70K, Moscow 125424, Russia</td></tr>
      <tr><th>Warehouse</th><td>Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region</td></tr>
    </table>
  </div>
</section>
""" + cta("Want to become a partner?", "Tell us about your company and supply needs — we will discuss the terms.", "Partnership", "Email us", "Call", "Store"),
    },
}

# ---------------------------------------------------------------- CATALOG
PAGES["catalog"] = {
    "ru": {
        "title": "Каталог: категории поставок автозапчастей и шин — Dispare Trading",
        "desc": "Двигатель, трансмиссия, ходовая часть и шины, тормоза, электрика, расходники. Оптовые поставки юрлицам по договору с НДС. Поиск по артикулу — в магазине для партнёров.",
        "body": page_hero("Главная", "{u_index}", "Каталог", "Каталог", "Категории поставок",
                          "Открытого прайса на сайте нет — стоимость зависит от объёма партии, комплектации и курса валют. Ищите позиции по артикулу в магазине для партнёров или пришлите список — подготовим коммерческое предложение.") + """
<section class="section">
  <div class="container"><div class="cat-grid">{cats_full}</div></div>
</section>
""" + shop_band(dict(g="Магазин для партнёров", h="Цены и наличие — в магазине для партнёров",
                     p="Ищите по артикулу или VIN, собирайте корзину и оформляйте заказ сами — без ожидания менеджера.",
                     l1="Поиск по артикулу и VIN", l2="Подбор по автомобилю", l3="История заказов в личном кабинете",
                     label="Поиск по артикулу", ph="Например, 0446533480", btn="Найти", open="Перейти в магазин", reg="Регистрация",
                     note="Откроется в новой вкладке на shop.disparetrading.ru.")).replace('class="section"', 'class="section" style="padding-top:0"', 1) + """
""" + cta("Не нашли нужную категорию?", "Работаем и с индивидуальными запросами — пришлите VIN, марку и модель или артикулы, подберём поставку.", "%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81%20%D0%BF%D0%BE%D0%B4%D0%B1%D0%BE%D1%80%D0%B0", "Написать на почту", "Позвонить", "Магазин"),
    },
    "en": {
        "title": "Catalogue: auto parts and tyre categories — Dispare Trading",
        "desc": "Engine, transmission, suspension and tyres, brakes, electrics, service parts. Wholesale supply to businesses under contract with VAT. Part-number search in the partner store.",
        "body": page_hero("Home", "{u_index}", "Catalogue", "Catalogue", "Product categories",
                          "There is no public price list on the website — prices depend on batch size, configuration and exchange rates. Search by part number in the partner store or send us your list and we will prepare a quote.") + """
<section class="section">
  <div class="container"><div class="cat-grid">{cats_full}</div></div>
</section>
""" + shop_band(dict(g="Partner store", h="Prices and stock — in the partner store",
                     p="Search by part number or VIN, build a cart and place the order yourself, without waiting for a manager. The store interface is in Russian.",
                     l1="Search by part number and VIN", l2="Lookup by vehicle", l3="Order history in your account",
                     label="Part number search", ph="e.g. 0446533480", btn="Search", open="Open the store", reg="Register",
                     note="Opens in a new tab on shop.disparetrading.ru (in Russian).")).replace('class="section"', 'class="section" style="padding-top:0"', 1) + """
""" + cta("Can't find the category you need?", "We also handle custom requests — send a VIN, make and model or part numbers and we will source the supply.", "Sourcing%20request", "Email us", "Call", "Store"),
    },
}

# ---------------------------------------------------------------- DELIVERY
PAGES["delivery"] = {
    "ru": {
        "title": "Оплата и доставка — Dispare Trading",
        "desc": "Безналичная оплата с НДС, договор поставки, УПД через ЭДО. Самовывоз со склада в Московской области или доставка транспортной компанией в любой регион России.",
        "body": page_hero("Главная", "{u_index}", "Оплата и доставка", "Условия сотрудничества", "Оплата и доставка",
                          "Работаем с юридическими лицами и индивидуальными предпринимателями по стандартной для B2B схеме: договор, безналичная оплата, отгрузка выбранным способом.") + """
<section class="section">
  <div class="container two-col">
    <div data-reveal>
      <div class="graph">01 / Оплата</div>
      <table class="sheet">
        <tr><th>Форма расчёта</th><td>Безналичный расчёт на расчётный счёт компании</td></tr>
        <tr><th>Налогообложение</th><td>Работаем с НДС, выставляем счета-фактуры и УПД</td></tr>
        <tr><th>Кто может заказать</th><td>Юридические лица и индивидуальные предприниматели по договору</td></tr>
        <tr><th>Документы</th><td>Договор поставки, счёт на оплату, закрывающие документы после отгрузки</td></tr>
        <tr><th>Документооборот</th><td>Электронный документооборот (ЭДО) с контрагентами</td></tr>
        <tr><th>Маркировка</th><td>Для товаров, подлежащих обязательной маркировке, — через систему «Честный знак»</td></tr>
      </table>
      <p class="notice">Порядок оплаты (предоплата, постоплата, частичная предоплата) фиксируется в договоре и может обсуждаться индивидуально для постоянных партнёров.</p>
    </div>
    <div data-reveal>
      <div class="graph">02 / Доставка</div>
      <table class="sheet">
        <tr><th>Самовывоз</th><td>Со склада: Московская область, Дмитровский муниципальный округ, д. Кузяево, с2</td></tr>
        <tr><th>Доставка ТК</th><td>Транспортной компанией по выбору клиента в любой регион России</td></tr>
        <tr><th>Сроки</th><td>Зависят от наличия позиции на складе и выбранной транспортной компании</td></tr>
        <tr><th>Упаковка</th><td>По требованиям транспортной компании</td></tr>
      </table>
      <p class="notice">Доставка транспортной компанией оплачивается отдельно по тарифам перевозчика, если иное не согласовано в договоре.</p>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container two-col">
    <div data-reveal>
      <div class="graph">03 / Самовывоз</div>
      <h2 style="margin-bottom:14px">Склад — пункт самовывоза</h2>
      <p>Московская область, Дмитровский муниципальный округ, деревня Кузяево, с2. Перед выездом согласуйте время получения заказа с менеджером.</p>
      <a class="btn btn-outline" href="__MAPLINK__" target="_blank" rel="noopener">Открыть в Яндекс Картах ↗</a>
    </div>
    <div data-reveal>__MAP_RU__</div>
  </div>
</section>
""" + cta("Уточним детали под ваш заказ", "Сообщите объём и регион доставки — рассчитаем сроки и стоимость.", "%D0%A0%D0%B0%D1%81%D1%87%D1%91%D1%82%20%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%B8", "Написать на почту", "Позвонить", "Магазин"),
    },
    "en": {
        "title": "Payment and delivery — Dispare Trading",
        "desc": "Bank transfer with VAT, supply contract, UPD via electronic document exchange. Pick-up from our Moscow-region warehouse or delivery by carrier anywhere in Russia.",
        "body": page_hero("Home", "{u_index}", "Payment & delivery", "Terms of cooperation", "Payment and delivery",
                          "We work with companies and sole proprietors under the standard B2B scheme: a contract, bank transfer and shipment by the method you choose.") + """
<section class="section">
  <div class="container two-col">
    <div data-reveal>
      <div class="graph">01 / Payment</div>
      <table class="sheet">
        <tr><th>Payment method</th><td>Bank transfer to the company account</td></tr>
        <tr><th>Taxation</th><td>VAT included; we issue VAT invoices and UPD (universal transfer documents)</td></tr>
        <tr><th>Who can order</th><td>Legal entities and sole proprietors under contract</td></tr>
        <tr><th>Documents</th><td>Supply contract, invoice, closing documents after shipment</td></tr>
        <tr><th>Document exchange</th><td>Electronic document exchange (EDI) with counterparties</td></tr>
        <tr><th>Product marking</th><td>Via the national "Chestny Znak" system for goods subject to mandatory marking</td></tr>
      </table>
      <p class="notice">Payment terms (prepayment, deferred payment or partial prepayment) are fixed in the contract and can be agreed individually for regular partners.</p>
    </div>
    <div data-reveal>
      <div class="graph">02 / Delivery</div>
      <table class="sheet">
        <tr><th>Pick-up</th><td>From the warehouse: Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region</td></tr>
        <tr><th>By carrier</th><td>A transport company of your choice, to any region of Russia</td></tr>
        <tr><th>Lead time</th><td>Depends on stock availability and the chosen carrier</td></tr>
        <tr><th>Packaging</th><td>According to the carrier's requirements</td></tr>
      </table>
      <p class="notice">Carrier delivery is paid separately at the carrier's rates unless agreed otherwise in the contract.</p>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container two-col">
    <div data-reveal>
      <div class="graph">03 / Pick-up</div>
      <h2 style="margin-bottom:14px">Warehouse and pick-up point</h2>
      <p>Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region, Russia. Please agree the pick-up time with your manager before you come.</p>
      <a class="btn btn-outline" href="__MAPLINK__" target="_blank" rel="noopener">Open in Yandex Maps ↗</a>
    </div>
    <div data-reveal>__MAP_EN__</div>
  </div>
</section>
""" + cta("Let's work out the details of your order", "Tell us the volume and delivery region — we will calculate lead time and cost.", "Delivery%20quote", "Email us", "Call", "Store"),
    },
}

# ---------------------------------------------------------------- WARRANTY
PAGES["warranty"] = {
    "ru": {
        "title": "Гарантии и возврат — Dispare Trading",
        "desc": "Гарантия на поставляемые автозапчасти и шины, порядок возврата и замены брака по договору поставки и ГК РФ.",
        "body": page_hero("Главная", "{u_index}", "Гарантии", "Гарантии", "Гарантии и возврат",
                          "Поставляем товар с гарантией и решаем вопросы брака и возврата в соответствии с законодательством РФ — без затяжных согласований.") + """
<section class="section">
  <div class="container two-col">
    <div class="prose" data-reveal>
      <h2>Гарантийные обязательства</h2>
      <p>На поставляемые товары предоставляется гарантия, срок и условия которой фиксируются в договоре поставки и/или сопроводительных документах на конкретную партию. Гарантия распространяется на производственный брак и несоответствие товара заявленным характеристикам.</p>
      <h2>Что считается браком</h2>
      <ul>
        <li>Производственный дефект, не связанный с нарушением условий транспортировки, хранения или установки покупателем.</li>
        <li>Несоответствие товара артикулу или характеристикам, указанным в заказе и сопроводительных документах.</li>
        <li>Некомплектность поставки по вине поставщика.</li>
      </ul>
      <h2>Правовая основа</h2>
      <p>Отношения сторон при выявлении недостатков товара регулируются Гражданским кодексом РФ (прежде всего положениями о договоре поставки) и, применительно к отдельным случаям, Законом РФ «О защите прав потребителей». Сроки предъявления претензий и порядок их рассмотрения фиксируются в договоре с каждым партнёром.</p>
    </div>
    <div data-reveal>
      <div class="graph">Порядок возврата и замены</div>
      <ol class="principles">
        <li><div><b>Заявка</b><span>Сообщите о браке менеджеру или на <a class="link" href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a>: описание дефекта, номер заказа, фото или видео.</span></div></li>
        <li><div><b>Проверка</b><span>Рассматриваем обращение и при необходимости согласовываем осмотр или экспертизу.</span></div></li>
        <li><div><b>Решение</b><span>Замена, возврат денег или устранение недостатка — по ГК РФ и договору поставки.</span></div></li>
        <li><div><b>Возврат товара</b><span>Обратная транспортировка согласовывается индивидуально; расходы — по закону и договору.</span></div></li>
      </ol>
      <table class="sheet" style="margin-top:28px">
        <tr><th>Срок рассмотрения</th><td>Определяется договором поставки</td></tr>
        <tr><th>Способы решения</th><td>Замена, возврат средств, устранение недостатка</td></tr>
        <tr><th>Контакт</th><td><a href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a><br><a href="tel:+79939037079">+7 993 903-70-79</a></td></tr>
      </table>
    </div>
  </div>
</section>
""" + cta("Есть вопрос по гарантии?", "Опишите ситуацию — подскажем порядок действий и сроки.", "%D0%93%D0%B0%D1%80%D0%B0%D0%BD%D1%82%D0%B8%D1%8F", "Написать на почту", "Позвонить", "Магазин"),
    },
    "en": {
        "title": "Warranty and returns — Dispare Trading",
        "desc": "Warranty on supplied auto parts and tyres; how defective goods are returned and replaced under the supply contract and the Russian Civil Code.",
        "body": page_hero("Home", "{u_index}", "Warranty", "Warranty", "Warranty and returns",
                          "Our goods come with a warranty, and we handle defects and returns in line with Russian law — without lengthy approvals.") + """
<section class="section">
  <div class="container two-col">
    <div class="prose" data-reveal>
      <h2>Warranty obligations</h2>
      <p>Supplied goods carry a warranty whose term and conditions are set out in the supply contract and/or the accompanying documents for a specific batch. The warranty covers manufacturing defects and goods that do not match the stated specifications.</p>
      <h2>What counts as a defect</h2>
      <ul>
        <li>A manufacturing defect not caused by improper transport, storage or installation by the buyer.</li>
        <li>Goods that do not match the part number or specifications stated in the order and accompanying documents.</li>
        <li>An incomplete delivery through the supplier's fault.</li>
      </ul>
      <h2>Legal basis</h2>
      <p>The parties' relations when a defect is found are governed by the Civil Code of the Russian Federation (primarily its provisions on supply contracts) and, in certain cases, by the Russian Consumer Rights Protection Act. Claim deadlines and the claim procedure are fixed in the contract with each partner.</p>
    </div>
    <div data-reveal>
      <div class="graph">Return and replacement procedure</div>
      <ol class="principles">
        <li><div><b>Claim</b><span>Report the defect to your manager or to <a class="link" href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a>: describe the defect, give the order number, attach photos or video.</span></div></li>
        <li><div><b>Review</b><span>We review the claim and, if needed, arrange an inspection or expert examination.</span></div></li>
        <li><div><b>Resolution</b><span>Replacement, refund or repair — under the Russian Civil Code and the supply contract.</span></div></li>
        <li><div><b>Return shipping</b><span>Returning the goods is agreed case by case; costs are allocated by law and the contract.</span></div></li>
      </ol>
      <table class="sheet" style="margin-top:28px">
        <tr><th>Review period</th><td>Set by the supply contract</td></tr>
        <tr><th>Remedies</th><td>Replacement, refund, repair</td></tr>
        <tr><th>Contact</th><td><a href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a><br><a href="tel:+79939037079">+7 993 903-70-79</a></td></tr>
      </table>
    </div>
  </div>
</section>
""" + cta("A question about the warranty?", "Describe the situation — we will explain the procedure and timing.", "Warranty", "Email us", "Call", "Store"),
    },
}

# ---------------------------------------------------------------- CONTACTS
_REQ_RU = [("Полное наименование", "Общество с ограниченной ответственностью «ДИСПЭР»", False),
           ("Юридический адрес", "125424, Россия, г. Москва, вн.тер.г. муниципальный округ Покровское-Стрешнево, ш. Волоколамское, д. 71, к. 4, помещ. 70К", False),
           ("ИНН", "7733483947", True), ("КПП", "773301001", True), ("ОГРН", "1267700136582", True),
           ("Расчётный счёт", "40702810110002096461", True), ("Банк", "АО «ТБанк»", False), ("БИК", "044525974", True),
           ("ИНН банка", "7710140679", True), ("Корр. счёт", "30101810145250000974", True),
           ("Адрес банка", "127287, г. Москва, ул. Хуторская 2-я, д. 38А, стр. 26", False)]
_REQ_EN = [("Full legal name", "Limited Liability Company DISPER (Общество с ограниченной ответственностью «ДИСПЭР»)", False),
           ("Registered address", "71 Volokolamskoe Highway, bldg 4, premises 70K, Pokrovskoe-Streshnevo municipal district, Moscow 125424, Russia", False),
           ("INN (tax ID)", "7733483947", True), ("KPP", "773301001", True), ("OGRN (registration no.)", "1267700136582", True),
           ("Settlement account (RUB)", "40702810110002096461", True), ("Bank", "T-Bank JSC (АО «ТБанк»)", False), ("BIC", "044525974", True),
           ("Bank INN", "7710140679", True), ("Correspondent account", "30101810145250000974", True),
           ("Bank address", "38A 2nd Khutorskaya St, bldg 26, Moscow 127287, Russia", False)]


def _req(rows):
    mono = ' class="mono"'
    return "".join("<tr><th>%s</th><td%s>%s</td></tr>" % (k, mono if m else "", v) for k, v, m in rows)


def _req_text(rows):
    import html as _h
    return _h.escape("\n".join(f"{k}: {v}" for k, v, _ in rows), quote=True)


PAGES["contacts"] = {
    "ru": {
        "title": "Контакты и реквизиты — Dispare Trading (ООО «ДИСПЭР»)",
        "desc": "Телефон, почта, адрес склада и полные реквизиты ООО «ДИСПЭР» для договора. Работаем Пн–Пт, 10:00–18:00 по Москве.",
        "body": page_hero("Главная", "{u_index}", "Контакты", "Контакты", "Свяжитесь с нами",
                          "Отвечаем в рабочее время. Для юридических лиц готовим договор и коммерческое предложение после получения списка нужных позиций.") + """
<section class="section" id="connect">
  <div class="container two-col">
    <div data-reveal>
      <div class="graph">01 / Связь</div>
      <div class="contact-big">
        <a href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a>
        <a class="mono" href="tel:+79939037079">+7 993 903-70-79</a>
      </div>
      <table class="sheet">
        <tr><th>Режим работы</th><td>Пн–Пт, 10:00–18:00 (МСК)</td></tr>
        <tr><th>Склад / самовывоз</th><td>Московская область, Дмитровский муниципальный округ, д. Кузяево, с2</td></tr>
        <tr><th>Интернет-магазин</th><td><a href="{shop}/" target="_blank" rel="noopener">shop.disparetrading.ru ↗</a></td></tr>
      </table>
      <div class="hero-actions" style="margin-top:22px">
        <a class="btn btn-primary" href="mailto:{mail}?subject=%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81%20%D0%9A%D0%9F">Запросить КП</a>
        <a class="btn btn-outline" href="tel:{tel}">Позвонить</a>
      </div>
    </div>
    <div data-reveal>__MAP_RU__</div>
  </div>
</section>
<section class="section section-alt" id="requisites">
  <div class="container">
    <div class="section-head" data-reveal>
      <div class="graph">02 / Реквизиты для договора</div>
      <h2>ООО «ДИСПЭР»</h2>
      <p><button class="copy" type="button" data-copy="__REQTXT_RU__">Скопировать все реквизиты</button></p>
    </div>
    <table class="sheet" data-reveal>__REQ_RU__</table>
  </div>
</section>
""",
    },
    "en": {
        "title": "Contacts and company details — Dispare Trading (DISPER LLC)",
        "desc": "Phone, email, warehouse address and full company details of DISPER LLC for contracts. Office hours Mon–Fri, 10:00–18:00 Moscow time.",
        "body": page_hero("Home", "{u_index}", "Contacts", "Contacts", "Get in touch",
                          "We reply during business hours (Moscow time). For companies, we prepare a contract and a commercial offer once we receive your list of items.") + """
<section class="section" id="connect">
  <div class="container two-col">
    <div data-reveal>
      <div class="graph">01 / Contact</div>
      <div class="contact-big">
        <a href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a>
        <a class="mono" href="tel:+79939037079">+7 993 903-70-79</a>
      </div>
      <table class="sheet">
        <tr><th>Office hours</th><td>Mon–Fri, 10:00–18:00 (Moscow time, UTC+3)</td></tr>
        <tr><th>Warehouse / pick-up</th><td>Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region, Russia</td></tr>
        <tr><th>Online store</th><td><a href="{shop}/" target="_blank" rel="noopener">shop.disparetrading.ru ↗</a> (in Russian)</td></tr>
        <tr><th>Languages</th><td>Russian, English (by email)</td></tr>
      </table>
      <div class="hero-actions" style="margin-top:22px">
        <a class="btn btn-primary" href="mailto:{mail}?subject=Quote%20request">Request a quote</a>
        <a class="btn btn-outline" href="tel:{tel}">Call</a>
      </div>
    </div>
    <div data-reveal>__MAP_EN__</div>
  </div>
</section>
<section class="section section-alt" id="requisites">
  <div class="container">
    <div class="section-head" data-reveal>
      <div class="graph">02 / Company details for contracts</div>
      <h2>DISPER LLC (ООО «ДИСПЭР»)</h2>
      <p><button class="copy" type="button" data-copy="__REQTXT_EN__">Copy all details</button></p>
    </div>
    <table class="sheet" data-reveal>__REQ_EN__</table>
  </div>
</section>
""",
    },
}

# ---------------------------------------------------------------- PRIVACY (text unchanged in substance until the RKN package is filed)
PAGES["privacy"] = {
    "ru": {
        "title": "Политика обработки персональных данных — Dispare Trading",
        "desc": "Политика ООО «ДИСПЭР» в отношении обработки персональных данных в соответствии с 152-ФЗ.",
        "body": page_hero("Главная", "{u_index}", "Политика", "Документы", "Политика в отношении обработки персональных данных",
                          "Действует в соответствии с Федеральным законом от 27.07.2006 № 152-ФЗ «О персональных данных».") + """
<section class="section"><div class="container"><div class="prose" data-reveal>
<h2>1. Общие положения</h2>
<p>Настоящая Политика определяет порядок обработки и защиты персональных данных физических лиц (далее — «Субъекты персональных данных»), которые могут быть получены оператором персональных данных при использовании сайта disparetrading.ru (далее — «Сайт»), в том числе при заполнении форм обратной связи.</p>
<p>Оператором персональных данных является: <strong>Общество с ограниченной ответственностью «ДИСПЭР» (ООО «ДИСПЭР»), ИНН 7733483947, КПП 773301001, ОГРН 1267700136582, юридический адрес: 125424, Россия, г. Москва, вн.тер.г. муниципальный округ Покровское-Стрешнево, ш. Волоколамское, д. 71, к. 4, помещ. 70К</strong> (далее — «Оператор»).</p>
<h2>2. Какие данные обрабатываются</h2>
<p>При заполнении формы заявки на Сайте Оператор может обрабатывать следующие персональные данные:</p>
<ul><li>имя;</li><li>номер телефона;</li><li>адрес электронной почты;</li><li>наименование компании (при указании);</li><li>иные данные, которые Субъект персональных данных добровольно указывает в тексте сообщения.</li></ul>
<p>Сайт не запрашивает специальные категории персональных данных (сведения о здоровье, религиозных убеждениях и т.п.).</p>
<h2>3. Цели обработки персональных данных</h2>
<ul><li>обработка заявок и обращений, поступивших через формы на Сайте;</li><li>подготовка коммерческого предложения и заключение договора поставки;</li><li>обратная связь с Субъектом персональных данных, включая направление ответов на запросы;</li><li>исполнение обязательств по заключённым договорам.</li></ul>
<h2>4. Правовые основания обработки</h2>
<p>Обработка персональных данных осуществляется на основании согласия Субъекта персональных данных, выражаемого путём проставления отметки в форме на Сайте (ст. 6, 9 152-ФЗ), а также в целях исполнения договора, стороной которого является Субъект персональных данных.</p>
<h2>5. Порядок и условия обработки</h2>
<p>Обработка персональных данных осуществляется с использованием средств автоматизации и без таковых, включая сбор, запись, систематизацию, накопление, хранение, уточнение, извлечение, использование, передачу (предоставление, доступ), обезличивание, блокирование, удаление и уничтожение персональных данных.</p>
<p>Персональные данные обрабатываются и хранятся на территории Российской Федерации в соответствии с требованиями ч. 5 ст. 18 152-ФЗ. Передача персональных данных третьим лицам, в том числе трансграничная передача, без отдельного согласия Субъекта персональных данных не осуществляется, за исключением случаев, прямо предусмотренных законодательством РФ.</p>
<h2>6. Срок обработки и хранения</h2>
<p>Персональные данные обрабатываются в течение срока, необходимого для достижения целей обработки, указанных в разделе 3 настоящей Политики, а также в течение сроков хранения документов, установленных законодательством РФ (в том числе бухгалтерским и налоговым). Согласие на обработку персональных данных может быть отозвано Субъектом персональных данных в любой момент.</p>
<h2>7. Права субъекта персональных данных</h2>
<p>Субъект персональных данных имеет право:</p>
<ul><li>получать информацию, касающуюся обработки его персональных данных;</li><li>требовать уточнения, блокирования или уничтожения персональных данных в случае, если они являются неполными, устаревшими, неточными, незаконно полученными или не являются необходимыми для заявленной цели обработки;</li><li>отозвать согласие на обработку персональных данных;</li><li>обжаловать действия или бездействие Оператора в уполномоченный орган по защите прав субъектов персональных данных (Роскомнадзор) или в судебном порядке.</li></ul>
<h2>8. Меры по защите персональных данных</h2>
<p>Оператор принимает необходимые организационные и технические меры для защиты персональных данных от неправомерного или случайного доступа, уничтожения, изменения, блокирования, копирования, распространения, а также от иных неправомерных действий третьих лиц.</p>
<h2>9. Использование cookie и аналогичных технологий</h2>
<p>Сайт может использовать файлы cookie и аналогичные технологии для обеспечения корректной работы форм и, при подключении, для сбора обезличенной статистики посещаемости. Cookie не используются для установления личности посетителя без его добровольного указания контактных данных в форме.</p>
<h2>10. Согласие на обработку персональных данных</h2>
<p>Заполняя форму на Сайте и устанавливая соответствующую отметку, Субъект персональных данных подтверждает, что:</p>
<ul><li>ознакомлен с настоящей Политикой и согласен с её условиями;</li><li>даёт согласие на обработку указанных им персональных данных в целях, перечисленных в разделе 3;</li><li>предоставленные данные являются достоверными и относятся лично к нему.</li></ul>
<h2>11. Изменение Политики</h2>
<p>Оператор вправе вносить изменения в настоящую Политику. Актуальная версия Политики всегда доступна по адресу disparetrading.ru/privacy.</p>
<h2>12. Контакты по вопросам обработки персональных данных</h2>
<table class="sheet">
<tr><th>Оператор</th><td>ООО «ДИСПЭР», ИНН 7733483947, ОГРН 1267700136582</td></tr>
<tr><th>Юридический адрес</th><td>125424, Россия, г. Москва, вн.тер.г. муниципальный округ Покровское-Стрешнево, ш. Волоколамское, д. 71, к. 4, помещ. 70К</td></tr>
<tr><th>Email</th><td><a href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a></td></tr>
<tr><th>Телефон</th><td><a href="tel:+79939037079">+7 993 903-70-79</a></td></tr>
<tr><th>Склад</th><td>Московская область, Дмитровский муниципальный округ, д. Кузяево, с2</td></tr>
</table>
</div></div></section>
""",
    },
    "en": {
        "title": "Personal data policy — Dispare Trading",
        "desc": "DISPER LLC's policy on the processing of personal data under Russian Federal Law No. 152-FZ.",
        "body": page_hero("Home", "{u_index}", "Policy", "Documents", "Personal data processing policy",
                          "This is a translation for convenience. The Russian version, adopted under Federal Law No. 152-FZ of 27.07.2006 \"On Personal Data\", prevails.") + """
<section class="section"><div class="container"><div class="prose" data-reveal>
<h2>1. General provisions</h2>
<p>This Policy sets out how personal data of individuals ("Data Subjects") that the personal data operator may receive through the website disparetrading.ru (the "Website"), including through feedback forms, is processed and protected.</p>
<p>The personal data operator is <strong>Limited Liability Company DISPER (ООО «ДИСПЭР»), INN 7733483947, KPP 773301001, OGRN 1267700136582, registered address: 71 Volokolamskoe Highway, bldg 4, premises 70K, Pokrovskoe-Streshnevo municipal district, Moscow 125424, Russia</strong> (the "Operator").</p>
<h2>2. Data processed</h2>
<p>When a request form on the Website is filled in, the Operator may process the following personal data:</p>
<ul><li>name;</li><li>phone number;</li><li>email address;</li><li>company name (if provided);</li><li>any other data the Data Subject voluntarily includes in the message.</li></ul>
<p>The Website does not request special categories of personal data (such as health or religious beliefs).</p>
<h2>3. Purposes of processing</h2>
<ul><li>handling requests and enquiries received through forms on the Website;</li><li>preparing commercial offers and concluding supply contracts;</li><li>communicating with the Data Subject, including replying to enquiries;</li><li>performing obligations under concluded contracts.</li></ul>
<h2>4. Legal grounds</h2>
<p>Personal data is processed on the basis of the Data Subject's consent, given by ticking the box in the form on the Website (Articles 6 and 9 of Law 152-FZ), and for the performance of a contract to which the Data Subject is a party.</p>
<h2>5. Procedure and conditions</h2>
<p>Personal data is processed with and without automation, including collection, recording, systematisation, accumulation, storage, clarification, retrieval, use, transfer (provision, access), depersonalisation, blocking, deletion and destruction.</p>
<p>Personal data is processed and stored in the Russian Federation in accordance with Part 5 of Article 18 of Law 152-FZ. Personal data is not transferred to third parties, including cross-border, without the Data Subject's separate consent, except where expressly required by Russian law.</p>
<h2>6. Retention period</h2>
<p>Personal data is processed for as long as necessary to achieve the purposes listed in section 3 of this Policy and for the document retention periods established by Russian law (including accounting and tax law). The Data Subject may withdraw consent at any time.</p>
<h2>7. Rights of the Data Subject</h2>
<p>The Data Subject has the right to:</p>
<ul><li>receive information about the processing of their personal data;</li><li>demand that personal data be clarified, blocked or destroyed if it is incomplete, outdated, inaccurate, unlawfully obtained or not necessary for the stated purpose;</li><li>withdraw consent to processing;</li><li>appeal against the Operator's actions or inaction to the authorised body for the protection of data subjects' rights (Roskomnadzor) or in court.</li></ul>
<h2>8. Security measures</h2>
<p>The Operator takes the necessary organisational and technical measures to protect personal data against unlawful or accidental access, destruction, modification, blocking, copying, dissemination and other unlawful actions of third parties.</p>
<h2>9. Cookies and similar technologies</h2>
<p>The Website may use cookies and similar technologies to make forms work correctly and, if enabled, to collect anonymised visit statistics. Cookies are not used to identify a visitor unless the visitor voluntarily provides contact details in a form.</p>
<h2>10. Consent to processing</h2>
<p>By filling in a form on the Website and ticking the relevant box, the Data Subject confirms that they:</p>
<ul><li>have read this Policy and agree to its terms;</li><li>consent to the processing of the personal data they have provided for the purposes listed in section 3;</li><li>have provided accurate data that relates to them personally.</li></ul>
<h2>11. Changes to the Policy</h2>
<p>The Operator may amend this Policy. The current version is always available at disparetrading.ru/privacy (Russian) and disparetrading.ru/en/privacy (English translation).</p>
<h2>12. Contact for personal data matters</h2>
<table class="sheet">
<tr><th>Operator</th><td>DISPER LLC (ООО «ДИСПЭР»), INN 7733483947, OGRN 1267700136582</td></tr>
<tr><th>Registered address</th><td>71 Volokolamskoe Highway, bldg 4, premises 70K, Moscow 125424, Russia</td></tr>
<tr><th>Email</th><td><a href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a></td></tr>
<tr><th>Phone</th><td><a href="tel:+79939037079">+7 993 903-70-79</a></td></tr>
<tr><th>Warehouse</th><td>Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region, Russia</td></tr>
</table>
</div></div></section>
""",
    },
}

# ---------------------------------------------------------------- 404 (bilingual, served for any missing URL)
PAGES["404"] = {
    "ru": {
        "title": "Страница не найдена — Dispare Trading",
        "desc": "Такой страницы нет. Перейдите на главную или в магазин для партнёров.",
        "body": """<section class="nf ledger"><div class="container">
  <div class="code">404</div>
  <h1 style="font-size:clamp(1.6rem,3vw,2.2rem)">Такой страницы нет · Page not found</h1>
  <p>Возможно, ссылка устарела. Начните с главной или найдите деталь по артикулу в магазине для партнёров.<br>The link may be outdated. Start from the home page or search the partner store.</p>
  <div class="hero-actions" style="justify-content:center">
    <a class="btn btn-primary" href="/">На главную</a>
    <a class="btn btn-outline" href="/en/">English site</a>
    <a class="btn btn-shop" href="{shop}/" target="_blank" rel="noopener"><span class="tag">SHOP</span>Магазин <span class="arrow">→</span></a>
  </div>
</div></section>""",
    },
}

# ---------------------------------------------------------------- post-processing of placeholders that contain braces/percent signs
for _slug, _p in PAGES.items():
    for _lang, _pg in _p.items():
        b = _pg["body"]
        b = b.replace("__MAPLINK__", MAP_LINK)
        b = b.replace("__MAP_RU__", MAP.replace("%s", "Карта склада Dispare Trading", 1) if "%s" in MAP else MAP)
        b = b.replace("__MAP_EN__", MAP.replace("%s", "Map of the Dispare Trading warehouse", 1) if "%s" in MAP else MAP)
        b = b.replace("__REQ_RU__", _req(_REQ_RU)).replace("__REQ_EN__", _req(_REQ_EN))
        b = b.replace("__REQTXT_RU__", _req_text(_REQ_RU)).replace("__REQTXT_EN__", _req_text(_REQ_EN))
        _pg["body"] = b

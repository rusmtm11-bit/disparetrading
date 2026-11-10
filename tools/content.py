# -*- coding: utf-8 -*-
"""All site texts, Russian and English side by side.
Page bodies are str.format templates: {u_catalog}, {shop}, {mail}, {tel}, {cats_home}, {cats_full}, {sticker}
are filled in by build.py. Do not use literal curly braces in bodies."""
import html as _html
from legal import PRIVACY_RU, PRIVACY_EN, _REQ_RU, _REQ_EN

ORDER = ["index", "about", "catalog", "delivery", "warranty", "contacts", "privacy"]

STR = {
    "ru": {
        "skip": "Перейти к содержимому", "nav_label": "Разделы сайта", "menu": "Меню", "close": "Закрыть",
        "lang_label": "Язык сайта",
        "nav": {"about": "О компании", "catalog": "Каталог", "delivery": "Оплата и доставка", "warranty": "Гарантия", "contacts": "Контакты"},
        "shop_btn": "Магазин для партнёров",
        "hours": "Пн–Пт, 10:00–18:00 по Москве",
        "footer_about": "Импорт и оптовые поставки автозапчастей и шин для автосервисов, магазинов и автопарков.",
        "f_nav": "Разделы", "f_docs": "Документы", "f_contacts": "Связаться",
        "privacy": "Политика обработки персональных данных", "requisites": "Реквизиты компании",
        "warehouse_addr": "Склад: Московская обл., Дмитровский м. о., д. Кузяево, с2",
        "legal_line": "ООО «ДИСПЭР», ИНН 7733483947, ОГРН 1267700136582",
        "find_in_shop": "Смотреть в магазине", "request_quote": "Запросить предложение",
        "mail_subject_cat": "Запрос предложения: %s",
        "legal_name_schema": "ООО «ДИСПЭР»",
        "schema_street": "ш. Волоколамское, д. 71, к. 4, помещ. 70К", "schema_city": "Москва",
    },
    "en": {
        "skip": "Skip to content", "nav_label": "Site sections", "menu": "Menu", "close": "Close",
        "lang_label": "Site language",
        "nav": {"about": "About", "catalog": "Catalogue", "delivery": "Payment and delivery", "warranty": "Warranty", "contacts": "Contacts"},
        "shop_btn": "Partner store",
        "hours": "Mon–Fri, 10:00–18:00 Moscow time",
        "footer_about": "Import and wholesale supply of auto parts and tyres for repair shops, retailers and fleets in Russia.",
        "f_nav": "Sections", "f_docs": "Documents", "f_contacts": "Contact",
        "privacy": "Personal data policy", "requisites": "Company details",
        "warehouse_addr": "Warehouse: Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region",
        "legal_line": "DISPER LLC (ООО «ДИСПЭР»), INN 7733483947, OGRN 1267700136582",
        "find_in_shop": "View in the store", "request_quote": "Request a quote",
        "mail_subject_cat": "Quote request: %s",
        "legal_name_schema": "DISPER LLC (ООО «ДИСПЭР»)",
        "schema_street": "71 Volokolamskoe Highway, bldg 4, premises 70K", "schema_city": "Moscow",
    },
}

CATS = [
    {"id": "engine",
     "ru": ("Двигатель", "Поршневая группа, ГРМ, прокладки, турбины."),
     "en": ("Engine", "Pistons and rings, timing parts, gaskets, turbochargers."),
     "long": {"ru": "Поршневая группа, ремни, цепи и ролики ГРМ, прокладки, турбины, система охлаждения.",
              "en": "Pistons and rings, timing belts, chains and pulleys, gaskets, turbochargers, cooling system."}},
    {"id": "transmission",
     "ru": ("Трансмиссия и мосты", "Коробки передач, сцепление, раздатки, полуоси."),
     "en": ("Transmission and axles", "Gearboxes, clutches, transfer cases, drive shafts."),
     "long": {"ru": "Механические и автоматические коробки, сцепление, раздаточные коробки, редукторы, полуоси, приводные валы.",
              "en": "Manual and automatic gearboxes, clutches, transfer cases, differentials, half-shafts, drive shafts."}},
    {"id": "chassis",
     "ru": ("Подвеска и шины", "Рычаги, амортизаторы, ступицы, шины ходовых размеров."),
     "en": ("Suspension and tyres", "Control arms, shock absorbers, hubs, tyres in common sizes."),
     "long": {"ru": "Рычаги, амортизаторы, стойки, сайлентблоки, ступицы и подшипники, шины ходовых размеров.",
              "en": "Control arms, shock absorbers, struts, bushings, hubs and bearings, tyres in common sizes."}},
    {"id": "brakes",
     "ru": ("Тормоза", "Диски, колодки, суппорты, барабаны."),
     "en": ("Brakes", "Discs, pads, calipers, drums."),
     "long": {"ru": "Диски, колодки, суппорты, барабаны, шланги и трубки, датчики износа.",
              "en": "Discs, pads, calipers, drums, hoses and lines, wear sensors."}},
    {"id": "electric",
     "ru": ("Электрика и свет", "Генераторы, стартеры, датчики, фары."),
     "en": ("Electrics and lighting", "Alternators, starters, sensors, headlights."),
     "long": {"ru": "Генераторы, стартеры, датчики, проводка, фары и фонари.",
              "en": "Alternators, starters, sensors, wiring, headlights and tail lights."}},
    {"id": "consumables",
     "ru": ("Расходники для ТО", "Масла, фильтры, ремни, свечи — от коробки до паллеты."),
     "en": ("Service parts", "Oils, filters, belts, spark plugs, from a box to a pallet."),
     "long": {"ru": "Моторные и трансмиссионные масла, фильтры масляные, воздушные и салонные, ремни, свечи зажигания.",
              "en": "Engine and transmission oils, oil, air and cabin filters, belts, spark plugs."}},
]

# ---------------------------------------------------------------- supplier sticker (EAN-13 of 20 + INN, internal-use prefix)
_EAN = "2077334839475"


def _bars():
    L = {'0': '0001101', '1': '0011001', '2': '0010011', '3': '0111101', '4': '0100011', '5': '0110001', '6': '0101111', '7': '0111011', '8': '0110111', '9': '0001011'}
    R = {k: ''.join('1' if c == '0' else '0' for c in v) for k, v in L.items()}
    G = {k: v[::-1] for k, v in R.items()}
    P = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', 'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL']
    c = _EAN
    bits = '101' + ''.join((L if p == 'L' else G)[d] for p, d in zip(P[int(c[0])], c[1:7])) + '01010' + ''.join(R[d] for d in c[7:]) + '101'
    rects, x = [], 0
    while x < len(bits):
        if bits[x] == '1':
            w = 1
            while x + w < len(bits) and bits[x + w] == '1':
                w += 1
            rects.append('<rect x="%d" y="0" width="%d" height="64"/>' % (x, w))
            x += w
        else:
            x += 1
    return '<svg viewBox="0 0 %d 64" preserveAspectRatio="none" aria-hidden="true">%s</svg>' % (len(bits), "".join(rects))


def sticker(lang):
    if lang == "ru":
        t = dict(a="Поставщик", b="Пн–Пт, 10:00–18:00", who="ООО «ДИСПЭР»", rows=[("ИНН", "7733483947"), ("ОГРН", "1267700136582"), ("Налоги", "ОСНО, плательщик НДС"), ("Склад", "Московская обл.")],
                 shop="Перейти в магазин для партнёров", aria="Наклейка поставщика: ООО «ДИСПЭР», ИНН 7733483947")
    else:
        t = dict(a="Supplier", b="Mon–Fri, 10:00–18:00", who="DISPER LLC", rows=[("Tax ID (INN)", "7733483947"), ("Reg. no. (OGRN)", "1267700136582"), ("Taxes", "General regime, VAT payer"), ("Warehouse", "Moscow region")],
                 shop="Go to the partner store", aria="Supplier label: DISPER LLC, tax ID 7733483947")
    dl = "".join(f'<dt>{k}</dt><dd class="num">{v}</dd>' if v[0].isdigit() else f'<dt>{k}</dt><dd>{v}</dd>' for k, v in t["rows"])
    digits = f'<span>{_EAN[0]}</span><span>{_EAN[1:7]}</span><span>{_EAN[7:]}</span>'
    return (f'<aside class="sticker" aria-label="{t["aria"]}"><div class="row"><span>{t["a"]}</span><span class="status" data-status>{t["b"]}</span></div>'
            f'<p class="who">{t["who"]}</p><dl>{dl}</dl>'
            f'<div class="bars">{_bars()}<div class="digits">{digits}</div></div>'
            f'<div class="check"><a href="https://shop.disparetrading.ru/" target="_blank" rel="noopener">{t["shop"]}</a></div></aside>')


# ---------------------------------------------------------------- building blocks
def head_block(home, crumb, h1, p):
    return f"""<section class="head"><div class="wrap">
  <div class="crumbs"><a href="{{u_index}}">{home}</a> / {crumb}</div>
  <h1>{h1}</h1>
  <p>{p}</p>
</div></section>"""


def reach(h, p, hours_label, hours, wh_label, wh):
    return f"""<section class="sec"><div class="wrap reach">
  <div>
    <h2>{h}</h2>
    <p class="muted">{p}</p>
    <div class="big"><a href="mailto:{{mail}}">distribution@disparetrading.ru</a><a href="tel:{{tel}}">+7 993 903-70-79</a></div>
  </div>
  <table class="facts"><tr><th>{hours_label}</th><td>{hours}</td></tr><tr><th>{wh_label}</th><td>{wh}</td></tr></table>
</div></section>"""


MAP_SRC = ("https://yandex.ru/map-widget/v1/?text=%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%2C%20"
           "%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3%2C%20%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BD%D1%8F%20"
           "%D0%9A%D1%83%D0%B7%D1%8F%D0%B5%D0%B2%D0%BE%2C%20%D1%812")
MAP_LINK = ("https://yandex.ru/maps/?text=%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%2C%20"
            "%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3%2C%20%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BD%D1%8F%20"
            "%D0%9A%D1%83%D0%B7%D1%8F%D0%B5%D0%B2%D0%BE")


def _map(title):
    return f'<iframe class="map" src="{MAP_SRC}" title="{title}" loading="lazy"></iframe>'


def _req(rows):
    return "".join('<tr><th>%s</th><td%s>%s</td></tr>' % (k, ' class="num"' if m else "", v) for k, v, m in rows)


def _req_text(rows):
    return _html.escape("\n".join("%s: %s" % (k, v) for k, v, _ in rows), quote=True)


Q_RU = "%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81%20%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F"  # «Запрос предложения»
Q_EN = "Quote%20request"

RU_REACH = ("Режим работы", "Пн–Пт, 10:00–18:00 по Москве", "Склад и самовывоз", "Московская обл., Дмитровский м. о., д. Кузяево, с2")
EN_REACH = ("Office hours", "Mon–Fri, 10:00–18:00 Moscow time (UTC+3)", "Warehouse and pick-up", "Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region")

PAGES = {}

# ================================================================= HOME
PAGES["index"] = {
    "ru": {
        "title": "Dispare Trading — автозапчасти и шины оптом по договору с НДС",
        "desc": "ООО «ДИСПЭР» ввозит и поставляет оптом автозапчасти и шины для автосервисов, магазинов и автопарков. Договор, НДС, УПД через ЭДО, склад в Московской области, отгрузка по России.",
        "body": """<section class="box"><div class="wrap">
  <div>
    <h1>Автозапчасти и шины оптом для бизнеса</h1>
    <p class="lead">Сами ввозим товар, оформляем его на таможне на свою компанию и отгружаем со склада в Московской области. Работаем по договору, только безналом и с НДС, документы отправляем через ЭДО.</p>
    <form class="search" action="{shop}/search" method="get" target="_blank" role="search" data-search>
      <label for="pcode">Найти запчасть по артикулу</label>
      <div class="search-row">
        <input id="pcode" name="pcode" type="search" autocomplete="off" spellcheck="false" placeholder="Например, 1350550030" maxlength="40" required>
        <button class="btn" type="submit">Найти</button>
      </div>
      <small>Результаты откроются в нашем магазине для партнёров: цены, наличие, заказ.</small>
    </form>
    <p class="alt">Нет артикула? Пришлите VIN или список позиций на <a href="mailto:{mail}?subject=""" + Q_RU + """">distribution@disparetrading.ru</a>, подберём и пришлём предложение.</p>
  </div>
  {sticker}
</div></section>

<section class="sec"><div class="wrap">
  <div class="intro"><h2>Как проходит поставка</h2></div>
  <ol class="steps">
    <li><span class="n">1</span><h3>Заявка</h3><p>Присылаете артикулы, VIN или марку и модель. Если позиция есть в магазине, можно сразу оформить заказ там.</p></li>
    <li><span class="n">2</span><h3>Предложение и договор</h3><p>Готовим предложение под ваш объём, подписываем договор поставки.</p></li>
    <li><span class="n">3</span><h3>Счёт и оплата</h3><p>Выставляем счёт с НДС. Оплата на расчётный счёт, порядок прописан в договоре.</p></li>
    <li><span class="n">4</span><h3>Отгрузка</h3><p>Самовывоз со склада или транспортная компания в ваш регион. УПД приходит через ЭДО.</p></li>
  </ol>
</div></section>

<section class="sec"><div class="wrap split">
  <div>
    <h2>Документы по каждой сделке</h2>
    <p class="muted">Мы не берём наличные без документов и не продаём товар, который не прошёл таможню. Все реквизиты компании открыты, а цены и наличие можно посмотреть в магазине для партнёров.</p>
    <div class="actions"><a class="btn btn-quiet" href="{shop}/" target="_blank" rel="noopener">Магазин для партнёров</a><a class="btn btn-quiet" href="{u_contacts}#requisites">Реквизиты</a></div>
  </div>
  <ul class="docs">
    <li><div><b>Договор поставки</b><span>Цены, сроки, порядок оплаты и гарантия.</span></div></li>
    <li><div><b>Счёт с НДС</b><span>Оплата только на расчётный счёт компании в АО «ТБанк».</span></div></li>
    <li><div><b>УПД через ЭДО</b><span>С электронной подписью, без бумажной почты.</span></div></li>
    <li><div><b>Копии таможенных документов</b><span>По запросу на любую партию.</span></div></li>
  </ul>
</div></section>

<section class="sec"><div class="wrap">
  <div class="intro"><h2>Что поставляем</h2><p>Открытого прайса на сайте нет: цена зависит от объёма и курса. Актуальные цены и наличие смотрите в <a href="{shop}/" target="_blank" rel="noopener">магазине для партнёров</a>.</p></div>
  <div class="goods">{cats_home}</div>
  <p style="margin-top:28px"><a href="{u_catalog}">Весь каталог категорий</a></p>
</div></section>
""" + reach("Пришлите список артикулов", "Ответим в рабочее время и подготовим предложение под ваш объём. С автосервисами, магазинами и автопарками работаем по одному договору на все поставки.", *RU_REACH),
    },
    "en": {
        "title": "Dispare Trading — wholesale auto parts and tyres in Russia",
        "desc": "DISPER LLC imports and supplies auto parts and tyres wholesale to repair shops, retailers and fleets in Russia. Written contract, VAT invoicing, electronic documents, warehouse in the Moscow region.",
        "body": """<section class="box"><div class="wrap">
  <div>
    <h1>Wholesale auto parts and tyres for business</h1>
    <p class="lead">We import goods ourselves, clear customs in our company's name and ship from our warehouse in the Moscow region. Every deal runs on a written contract, bank transfer and VAT, with documents exchanged electronically.</p>
    <form class="search" action="{shop}/search" method="get" target="_blank" role="search" data-search>
      <label for="pcode">Find a part by part number</label>
      <div class="search-row">
        <input id="pcode" name="pcode" type="search" autocomplete="off" spellcheck="false" placeholder="e.g. 1350550030" maxlength="40" required>
        <button class="btn" type="submit">Search</button>
      </div>
      <small>Results open in our partner store, with prices, stock and ordering. The store is in Russian.</small>
    </form>
    <p class="alt">No part number? Send a VIN or a list of items to <a href="mailto:{mail}?subject=""" + Q_EN + """">distribution@disparetrading.ru</a> and we will reply with an offer.</p>
  </div>
  {sticker}
</div></section>

<section class="sec"><div class="wrap">
  <div class="intro"><h2>How a supply works</h2></div>
  <ol class="steps">
    <li><span class="n">1</span><h3>Request</h3><p>Send part numbers, a VIN or the make and model. If the item is in the store, you can order there straight away.</p></li>
    <li><span class="n">2</span><h3>Offer and contract</h3><p>We prepare an offer for your volume and sign a supply contract.</p></li>
    <li><span class="n">3</span><h3>Invoice and payment</h3><p>We issue a VAT invoice. Payment goes to the company bank account on the terms in the contract.</p></li>
    <li><span class="n">4</span><h3>Shipment</h3><p>Pick-up from the warehouse or a carrier to your region. The UPD transfer document arrives electronically.</p></li>
  </ol>
</div></section>

<section class="sec"><div class="wrap split">
  <div>
    <h2>Documents for every deal</h2>
    <p class="muted">We never take undocumented cash and never sell goods that have not cleared customs. Our company details are public, and prices and stock are in the partner store.</p>
    <div class="actions"><a class="btn btn-quiet" href="{shop}/" target="_blank" rel="noopener">Partner store</a><a class="btn btn-quiet" href="{u_contacts}#requisites">Company details</a></div>
  </div>
  <ul class="docs">
    <li><div><b>Supply contract</b><span>Prices, lead times, payment terms and warranty.</span></div></li>
    <li><div><b>VAT invoice</b><span>Payment only to the company account at T-Bank JSC.</span></div></li>
    <li><div><b>UPD via electronic exchange</b><span>Signed electronically, no paper post.</span></div></li>
    <li><div><b>Copies of customs documents</b><span>On request, for any batch.</span></div></li>
  </ul>
</div></section>

<section class="sec"><div class="wrap">
  <div class="intro"><h2>What we supply</h2><p>There is no public price list: prices depend on volume and exchange rates. See current prices and stock in the <a href="{shop}/" target="_blank" rel="noopener">partner store</a>.</p></div>
  <div class="goods">{cats_home}</div>
  <p style="margin-top:28px"><a href="{u_catalog}">All product categories</a></p>
</div></section>
""" + reach("Send us your list of part numbers", "We reply during business hours with an offer for your volume. Repair shops, retailers and fleets get one contract for all supplies.", *EN_REACH),
    },
}

# ================================================================= ABOUT
PAGES["about"] = {
    "ru": {
        "title": "О компании — Dispare Trading (ООО «ДИСПЭР»)",
        "desc": "Dispare Trading ввозит и поставляет оптом автозапчасти и шины. Таможенное оформление на свою компанию, склад в Московской области, договор и НДС.",
        "body": head_block("Главная", "О компании", "Импортёр и оптовый поставщик автозапчастей",
                           "Сами везём товар из-за рубежа, оформляем его на свою компанию и поставляем бизнесу по России. Чем короче цепочка, тем понятнее цена и документы.") + """
<section class="sec"><div class="wrap split">
  <div>
    <h2>Чем занимаемся</h2>
    <p>Dispare Trading (ООО «ДИСПЭР») ввозит автозапчасти и шины и поставляет их оптом по России. Наши клиенты — автосервисы, сети СТО, магазины, дистрибьюторы и компании с собственными автопарками.</p>
    <p>Товар проходит таможню на нашу компанию, хранится на складе в Московской области и проверяется перед отгрузкой. В России между таможней и вами только мы, поэтому за каждую позицию отвечаем сами.</p>
  </div>
  <ul class="plain">
    <li><b>Документы по каждой сделке</b><span>Договор, счёт, УПД и закрывающие документы.</span></li>
    <li><b>Только безналичный расчёт</b><span>Оплата на счёт компании с НДС, без наличных.</span></li>
    <li><b>Гарантия в договоре</b><span>Порядок работы с браком прописан заранее.</span></li>
    <li><b>ЭДО и маркировка</b><span>Документы через оператора ЭДО; товары, подлежащие маркировке, проводим через «Честный знак».</span></li>
  </ul>
</div></section>
<section class="sec"><div class="wrap split">
  <div>
    <h2>Карточка компании</h2>
    <p class="muted">Данные компании открыты. Полные реквизиты для договора — на странице контактов.</p>
    <div class="actions"><a class="btn btn-quiet" href="{shop}/" target="_blank" rel="noopener">Магазин для партнёров</a><a class="btn btn-quiet" href="{u_contacts}#requisites">Все реквизиты</a></div>
  </div>
  <table class="facts">
    <tr><th>Наименование</th><td>ООО «ДИСПЭР»</td></tr>
    <tr><th>ИНН / КПП</th><td class="num">7733483947 / 773301001</td></tr>
    <tr><th>ОГРН</th><td class="num">1267700136582</td></tr>
    <tr><th>Налогообложение</th><td>Общая система, плательщик НДС</td></tr>
    <tr><th>Юридический адрес</th><td>125424, г. Москва, ш. Волоколамское, д. 71, к. 4, помещ. 70К</td></tr>
    <tr><th>Склад</th><td>Московская обл., Дмитровский м. о., д. Кузяево, с2</td></tr>
  </table>
</div></section>
""" + reach("Хотите работать с нами?", "Расскажите о компании и о том, что вы закупаете. Обсудим условия и подготовим договор.", *RU_REACH),
    },
    "en": {
        "title": "About — Dispare Trading (DISPER LLC)",
        "desc": "Dispare Trading imports and supplies auto parts and tyres wholesale in Russia. Customs clearance in our own name, a warehouse in the Moscow region, contracts with VAT.",
        "body": head_block("Home", "About", "Auto parts importer and wholesale supplier",
                           "We bring goods from abroad, clear them through customs in our own name and supply businesses across Russia. A shorter chain means clearer prices and paperwork.") + """
<section class="sec"><div class="wrap split">
  <div>
    <h2>What we do</h2>
    <p>Dispare Trading (DISPER LLC, ООО «ДИСПЭР») imports auto parts and tyres and supplies them wholesale across Russia. Our customers are repair shops, service chains, retailers, distributors and companies with their own fleets.</p>
    <p>Goods clear customs in our company's name, are stored at our warehouse in the Moscow region and are checked before shipment. Inside Russia there is nobody between customs and you but us, so we answer for every item.</p>
  </div>
  <ul class="plain">
    <li><b>Documents for every deal</b><span>Contract, invoice, UPD and closing documents.</span></li>
    <li><b>Bank transfers only</b><span>Payment to the company account with VAT, no cash.</span></li>
    <li><b>Warranty in the contract</b><span>Defect handling is agreed in advance.</span></li>
    <li><b>E-documents and product marking</b><span>Documents go through an EDI operator; goods that require it are registered in Russia's "Chestny Znak" marking system.</span></li>
  </ul>
</div></section>
<section class="sec"><div class="wrap split">
  <div>
    <h2>Company card</h2>
    <p class="muted">Our company data is public. Full details for contracts are on the contacts page.</p>
    <div class="actions"><a class="btn btn-quiet" href="{shop}/" target="_blank" rel="noopener">Partner store</a><a class="btn btn-quiet" href="{u_contacts}#requisites">All company details</a></div>
  </div>
  <table class="facts">
    <tr><th>Legal name</th><td>DISPER LLC (ООО «ДИСПЭР»)</td></tr>
    <tr><th>INN / KPP</th><td class="num">7733483947 / 773301001</td></tr>
    <tr><th>OGRN</th><td class="num">1267700136582</td></tr>
    <tr><th>Taxation</th><td>General regime, VAT payer</td></tr>
    <tr><th>Registered address</th><td>71 Volokolamskoe Highway, bldg 4, premises 70K, Moscow 125424, Russia</td></tr>
    <tr><th>Warehouse</th><td>Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region</td></tr>
  </table>
</div></section>
""" + reach("Want to work with us?", "Tell us about your company and what you buy. We will discuss terms and prepare a contract.", *EN_REACH),
    },
}

# ================================================================= CATALOG
PAGES["catalog"] = {
    "ru": {
        "title": "Каталог автозапчастей и шин — Dispare Trading",
        "desc": "Двигатель, трансмиссия, подвеска и шины, тормоза, электрика, расходники для ТО. Оптовые поставки по договору с НДС. Цены и наличие — в магазине для партнёров.",
        "body": head_block("Главная", "Каталог", "Что поставляем",
                           "Открытого прайса на сайте нет: цена зависит от объёма партии и курса валют. Цены и наличие смотрите в магазине для партнёров или пришлите список, и мы подготовим предложение.") + """
<section class="sec"><div class="wrap"><div class="catlist">{cats_full}</div></div></section>
""" + reach("Не нашли нужное?", "Пришлите VIN, марку и модель или список артикулов. Подберём и пришлём предложение с ценами и сроками.", *RU_REACH),
    },
    "en": {
        "title": "Auto parts and tyre catalogue — Dispare Trading",
        "desc": "Engine, transmission, suspension and tyres, brakes, electrics, service parts. Wholesale supply under contract with VAT. Prices and stock in the partner store.",
        "body": head_block("Home", "Catalogue", "What we supply",
                           "There is no public price list: prices depend on batch size and exchange rates. Check prices and stock in the partner store, or send us your list and we will prepare an offer.") + """
<section class="sec"><div class="wrap"><div class="catlist">{cats_full}</div></div></section>
""" + reach("Can't find what you need?", "Send a VIN, the make and model or a list of part numbers. We will source the items and send an offer with prices and lead times.", *EN_REACH),
    },
}

# ================================================================= DELIVERY
PAGES["delivery"] = {
    "ru": {
        "title": "Оплата и доставка — Dispare Trading",
        "desc": "Безналичная оплата с НДС, договор поставки, УПД через ЭДО. Самовывоз со склада в Московской области или доставка транспортной компанией в любой регион России.",
        "body": head_block("Главная", "Оплата и доставка", "Оплата и доставка",
                           "Работаем с компаниями и ИП по обычной для опта схеме: договор, оплата по счёту, отгрузка удобным вам способом.") + """
<section class="sec"><div class="wrap split">
  <div><h2>Оплата</h2><p class="muted">Порядок оплаты (предоплата, отсрочка или частичная предоплата) прописываем в договоре. Для постоянных партнёров обсуждаем индивидуально.</p></div>
  <table class="facts">
    <tr><th>Как платить</th><td>Безналичный расчёт на расчётный счёт компании</td></tr>
    <tr><th>НДС</th><td>Работаем с НДС, выставляем счета-фактуры и УПД</td></tr>
    <tr><th>Кто может заказать</th><td>Юридические лица и ИП по договору</td></tr>
    <tr><th>Документы</th><td>Договор поставки, счёт, закрывающие документы после отгрузки</td></tr>
    <tr><th>Документооборот</th><td>Через оператора ЭДО</td></tr>
    <tr><th>Маркировка</th><td>Товары, подлежащие обязательной маркировке, проводим через «Честный знак»</td></tr>
  </table>
</div></section>
<section class="sec"><div class="wrap split">
  <div><h2>Доставка</h2><p class="muted">Доставку транспортной компанией оплачиваете по тарифам перевозчика, если в договоре не договорились иначе.</p></div>
  <table class="facts">
    <tr><th>Самовывоз</th><td>Склад: Московская обл., Дмитровский м. о., д. Кузяево, с2. Время согласуйте с менеджером.</td></tr>
    <tr><th>Транспортная компания</th><td>Любая на ваш выбор, в любой регион России</td></tr>
    <tr><th>Сроки</th><td>Зависят от наличия на складе и выбранного перевозчика</td></tr>
    <tr><th>Упаковка</th><td>По требованиям транспортной компании</td></tr>
  </table>
</div></section>
<section class="sec"><div class="wrap split">
  <div><h2>Склад</h2><p>Московская область, Дмитровский муниципальный округ, деревня Кузяево, с2.</p><p><a href="__MAPLINK__" target="_blank" rel="noopener">Открыть в Яндекс Картах</a></p></div>
  __MAP_RU__
</div></section>
""",
    },
    "en": {
        "title": "Payment and delivery — Dispare Trading",
        "desc": "Bank transfer with VAT, supply contract, UPD via electronic exchange. Pick-up from our Moscow-region warehouse or delivery by carrier anywhere in Russia.",
        "body": head_block("Home", "Payment and delivery", "Payment and delivery",
                           "We work with companies and sole proprietors on the usual wholesale terms: a contract, payment against an invoice and shipment by the method you choose.") + """
<section class="sec"><div class="wrap split">
  <div><h2>Payment</h2><p class="muted">Payment terms (prepayment, deferred or partial prepayment) are set in the contract and can be agreed individually for regular partners.</p></div>
  <table class="facts">
    <tr><th>How to pay</th><td>Bank transfer to the company account</td></tr>
    <tr><th>VAT</th><td>VAT included; we issue VAT invoices and UPD transfer documents</td></tr>
    <tr><th>Who can order</th><td>Companies and sole proprietors under contract</td></tr>
    <tr><th>Documents</th><td>Supply contract, invoice, closing documents after shipment</td></tr>
    <tr><th>Document exchange</th><td>Through an EDI operator</td></tr>
    <tr><th>Product marking</th><td>Goods subject to mandatory marking go through Russia's "Chestny Znak" system</td></tr>
  </table>
</div></section>
<section class="sec"><div class="wrap split">
  <div><h2>Delivery</h2><p class="muted">Carrier delivery is paid at the carrier's rates unless the contract says otherwise.</p></div>
  <table class="facts">
    <tr><th>Pick-up</th><td>Warehouse: Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region. Agree the time with your manager.</td></tr>
    <tr><th>By carrier</th><td>Any transport company you choose, to any region of Russia</td></tr>
    <tr><th>Lead time</th><td>Depends on stock and the chosen carrier</td></tr>
    <tr><th>Packaging</th><td>To the carrier's requirements</td></tr>
  </table>
</div></section>
<section class="sec"><div class="wrap split">
  <div><h2>Warehouse</h2><p>Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region, Russia.</p><p><a href="__MAPLINK__" target="_blank" rel="noopener">Open in Yandex Maps</a></p></div>
  __MAP_EN__
</div></section>
""",
    },
}

# ================================================================= WARRANTY
PAGES["warranty"] = {
    "ru": {
        "title": "Гарантия и возврат — Dispare Trading",
        "desc": "Гарантия на автозапчасти и шины, порядок возврата и замены брака по договору поставки и Гражданскому кодексу РФ.",
        "body": head_block("Главная", "Гарантия", "Гарантия и возврат",
                           "Поставляем товар с гарантией. Вопросы брака и возврата решаем по договору и Гражданскому кодексу, без долгих согласований.") + """
<section class="sec"><div class="wrap split">
  <div class="prose">
    <h2>Гарантия</h2>
    <p>Срок и условия гарантии указаны в договоре поставки или в документах на конкретную партию. Гарантия распространяется на производственный брак и на товар, который не соответствует заявленным характеристикам.</p>
    <h2>Что считается браком</h2>
    <ul>
      <li>Производственный дефект, если он не связан с нарушением условий перевозки, хранения или установки покупателем.</li>
      <li>Товар не соответствует артикулу или характеристикам из заказа и сопроводительных документов.</li>
      <li>Некомплектная поставка по вине поставщика.</li>
    </ul>
    <h2>На чём основано</h2>
    <p>Отношения сторон регулирует Гражданский кодекс РФ, прежде всего глава о договоре поставки, а в отдельных случаях и закон «О защите прав потребителей». Сроки претензий и порядок их рассмотрения прописываем в договоре с каждым партнёром.</p>
  </div>
  <div>
    <h2>Как вернуть или заменить</h2>
    <ol class="seq">
      <li><div><b>Сообщите о браке</b><span>Менеджеру или на <a href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a>: описание дефекта, номер заказа, фото или видео.</span></div></li>
      <li><div><b>Мы проверим</b><span>Рассмотрим обращение и при необходимости договоримся об осмотре или экспертизе.</span></div></li>
      <li><div><b>Решение</b><span>Замена, возврат денег или устранение недостатка по договору и ГК РФ.</span></div></li>
      <li><div><b>Возврат товара</b><span>Доставку обратно согласуем отдельно, расходы распределяются по закону и договору.</span></div></li>
    </ol>
  </div>
</div></section>
""" + reach("Вопрос по гарантии?", "Опишите ситуацию, и мы подскажем, что делать и сколько это займёт.", *RU_REACH),
    },
    "en": {
        "title": "Warranty and returns — Dispare Trading",
        "desc": "Warranty on auto parts and tyres; how defective goods are returned and replaced under the supply contract and the Russian Civil Code.",
        "body": head_block("Home", "Warranty", "Warranty and returns",
                           "Our goods come with a warranty. We handle defects and returns under the contract and the Russian Civil Code, without lengthy approvals.") + """
<section class="sec"><div class="wrap split">
  <div class="prose">
    <h2>Warranty</h2>
    <p>The warranty term and conditions are set out in the supply contract or in the documents for a specific batch. The warranty covers manufacturing defects and goods that do not match the stated specifications.</p>
    <h2>What counts as a defect</h2>
    <ul>
      <li>A manufacturing defect not caused by improper transport, storage or installation by the buyer.</li>
      <li>Goods that do not match the part number or specifications in the order and accompanying documents.</li>
      <li>An incomplete delivery through the supplier's fault.</li>
    </ul>
    <h2>Legal basis</h2>
    <p>The parties' relations are governed by the Civil Code of the Russian Federation, primarily its chapter on supply contracts, and in some cases by the Russian consumer protection law. Claim deadlines and the claim procedure are set in the contract with each partner.</p>
  </div>
  <div>
    <h2>How to return or replace</h2>
    <ol class="seq">
      <li><div><b>Report the defect</b><span>To your manager or to <a href="mailto:distribution@disparetrading.ru">distribution@disparetrading.ru</a>: a description, the order number, photos or video.</span></div></li>
      <li><div><b>We review it</b><span>We look at the claim and, if needed, arrange an inspection or expert examination.</span></div></li>
      <li><div><b>Resolution</b><span>Replacement, refund or repair under the contract and the Civil Code.</span></div></li>
      <li><div><b>Return shipping</b><span>Agreed case by case; costs are allocated by law and the contract.</span></div></li>
    </ol>
  </div>
</div></section>
""" + reach("A question about the warranty?", "Describe the situation and we will tell you what to do and how long it takes.", *EN_REACH),
    },
}

# ================================================================= CONTACTS
PAGES["contacts"] = {
    "ru": {
        "title": "Контакты и реквизиты — Dispare Trading (ООО «ДИСПЭР»)",
        "desc": "Телефон, почта, адрес склада и полные реквизиты ООО «ДИСПЭР» для договора. Работаем Пн–Пт, 10:00–18:00 по Москве.",
        "body": head_block("Главная", "Контакты", "Контакты",
                           "Отвечаем в рабочее время. Пришлите список позиций, и мы подготовим предложение и договор.") + """
<section class="sec" id="connect"><div class="wrap reach">
  <div>
    <h2>Напишите или позвоните</h2>
    <div class="big"><a href="mailto:{mail}">distribution@disparetrading.ru</a><a href="tel:{tel}">+7 993 903-70-79</a></div>
  </div>
  <table class="facts">
    <tr><th>Режим работы</th><td>Пн–Пт, 10:00–18:00 по Москве</td></tr>
    <tr><th>Склад и самовывоз</th><td>Московская обл., Дмитровский м. о., д. Кузяево, с2</td></tr>
    <tr><th>Магазин для партнёров</th><td><a href="{shop}/" target="_blank" rel="noopener">shop.disparetrading.ru</a></td></tr>
  </table>
</div></section>
<section class="sec" id="requisites"><div class="wrap split">
  <div>
    <h2>Реквизиты для договора</h2>
    <p class="muted">Для вашей бухгалтерии можно скопировать всё одним нажатием.</p>
    <p><button class="btn btn-quiet" type="button" data-copy="__REQTXT_RU__">Скопировать реквизиты</button></p>
  </div>
  <table class="facts">__REQ_RU__</table>
</div></section>
<section class="sec"><div class="wrap">__MAP_RU__<p style="margin-top:14px"><a href="__MAPLINK__" target="_blank" rel="noopener">Открыть в Яндекс Картах</a></p></div></section>
""",
    },
    "en": {
        "title": "Contacts and company details — Dispare Trading (DISPER LLC)",
        "desc": "Phone, email, warehouse address and full company details of DISPER LLC for contracts. Mon–Fri, 10:00–18:00 Moscow time.",
        "body": head_block("Home", "Contacts", "Contacts",
                           "We reply during business hours, Moscow time. Send us your list of items and we will prepare an offer and a contract. We read and answer email in English.") + """
<section class="sec" id="connect"><div class="wrap reach">
  <div>
    <h2>Email or call us</h2>
    <div class="big"><a href="mailto:{mail}">distribution@disparetrading.ru</a><a href="tel:{tel}">+7 993 903-70-79</a></div>
  </div>
  <table class="facts">
    <tr><th>Office hours</th><td>Mon–Fri, 10:00–18:00 Moscow time (UTC+3)</td></tr>
    <tr><th>Warehouse and pick-up</th><td>Kuzyaevo village, bldg 2, Dmitrovsky district, Moscow region</td></tr>
    <tr><th>Partner store</th><td><a href="{shop}/" target="_blank" rel="noopener">shop.disparetrading.ru</a> (in Russian)</td></tr>
  </table>
</div></section>
<section class="sec" id="requisites"><div class="wrap split">
  <div>
    <h2>Company details for contracts</h2>
    <p class="muted">Copy everything in one click for your accounts team.</p>
    <p><button class="btn btn-quiet" type="button" data-copy="__REQTXT_EN__">Copy company details</button></p>
  </div>
  <table class="facts">__REQ_EN__</table>
</div></section>
<section class="sec"><div class="wrap">__MAP_EN__<p style="margin-top:14px"><a href="__MAPLINK__" target="_blank" rel="noopener">Open in Yandex Maps</a></p></div></section>
""",
    },
}

# ================================================================= PRIVACY
PAGES["privacy"] = {
    "ru": {
        "title": "Политика обработки персональных данных — Dispare Trading",
        "desc": "Политика ООО «ДИСПЭР» в отношении обработки персональных данных в соответствии с 152-ФЗ.",
        "body": head_block("Главная", "Политика", "Политика обработки персональных данных",
                           "Действует в соответствии с Федеральным законом от 27.07.2006 № 152-ФЗ «О персональных данных».")
                + '\n<section class="sec"><div class="wrap"><div class="prose">\n' + PRIVACY_RU + "</div></div></section>\n",
    },
    "en": {
        "title": "Personal data policy — Dispare Trading",
        "desc": "DISPER LLC's policy on the processing of personal data under Russian Federal Law No. 152-FZ.",
        "body": head_block("Home", "Policy", "Personal data policy",
                           "This English translation is provided for convenience. The Russian version, adopted under Federal Law No. 152-FZ \"On Personal Data\", prevails.")
                + '\n<section class="sec"><div class="wrap"><div class="prose">\n' + PRIVACY_EN + "</div></div></section>\n",
    },
}

# ================================================================= 404
PAGES["404"] = {
    "ru": {
        "title": "Страница не найдена — Dispare Trading",
        "desc": "Такой страницы нет. Перейдите на главную или в магазин для партнёров.",
        "body": """<section class="lost"><div class="wrap">
  <div class="code">404</div>
  <h1>Такой страницы нет</h1>
  <p class="muted">Возможно, ссылка устарела. Начните с главной или найдите деталь по артикулу в магазине для партнёров.</p>
  <p class="muted" lang="en">Page not found. The link may be outdated: try the home page or the English version.</p>
  <div class="actions"><a class="btn" href="/">На главную</a><a class="btn btn-quiet" href="/en/">English version</a><a class="btn btn-quiet" href="{shop}/" target="_blank" rel="noopener">Магазин для партнёров</a></div>
</div></section>""",
    },
}

# ---------------------------------------------------------------- placeholders with % signs or quotes
for _p in PAGES.values():
    for _lang, _pg in _p.items():
        b = _pg["body"]
        b = b.replace("__MAPLINK__", MAP_LINK)
        b = b.replace("__MAP_RU__", _map("Склад Dispare Trading на карте")).replace("__MAP_EN__", _map("Dispare Trading warehouse on the map"))
        b = b.replace("__REQ_RU__", _req(_REQ_RU)).replace("__REQ_EN__", _req(_REQ_EN))
        b = b.replace("__REQTXT_RU__", _req_text(_REQ_RU)).replace("__REQTXT_EN__", _req_text(_REQ_EN))
        _pg["body"] = b

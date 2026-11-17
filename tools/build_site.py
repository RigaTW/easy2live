"""easy2live 官網產生器。

所有頁面的文字都在這支檔案裡，改完執行：
    python tools/build_site.py
就會重新產生網站根目錄下的 HTML、sitemap.xml。
圖片清單來自 assets/img/manifest.json。
"""
import hashlib, html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://easy2live.net'
EMAIL = 'service@easy2live.net'
MANIFEST = json.load(open(os.path.join(ROOT, 'assets/img/manifest.json'), encoding='utf-8'))

def ver(path):
    return hashlib.md5(open(os.path.join(ROOT, path), 'rb').read()).hexdigest()[:8]

CSS_V, JS_V = ver('assets/css/site.css'), ver('assets/js/site.js')
e = html.escape

# ---------- App 資料 ----------
APPS = {
  'baby': dict(
    slug='easy2baby', name='輕鬆寶貝', en='Easy2Baby', theme='t-baby',
    icon='/assets/img/apps/easy2baby-icon.webp',
    status='● iOS 與 Android 已上架', lead='把每一天，收進成長相簿。',
    desc='告別紙本手寫。單手記下餵食、睡眠、換尿布，再把照片收成家人看得到的成長時間軸。',
    ticks=['單手記下餵食、睡眠、換尿布', '身高體重生長曲線、餵藥鬧鐘', '一人訂閱，全家共享相簿'],
    stores=[('apple', '在 App Store 下載', 'App Store', 'https://apps.apple.com/tw/app/easy2baby/id6760773878'),
            ('play', '在 Google Play 下載', 'Google Play', 'https://play.google.com/store/apps/details?id=com.easy2live.easy2baby')],
    shots=[('/assets/img/apps/easy2baby-1.webp', '今日入口：相簿、年齡、飲食尿布睡眠健康'),
           ('/assets/img/apps/easy2baby-2.webp', '家人與寶寶資料')],
    feat=[('bottle', '餵食追蹤', '親餵左右時長、瓶餵奶量、副食品。'),
          ('moon', '生活作息', '睡眠區間、換尿布，看一整天的節奏。'),
          ('clock', '強制鬧鐘', '下一餐或餵藥間隔，時間到就推播。'),
          ('chart', '生長曲線', '身高、體重、頭圍。紀錄不能代替醫師。'),
          ('photo', '月曆相簿', '以月曆看每天的照片，並排成成長時間軸。'),
          ('people', '家庭共享', '多寶寶、跨裝置，用邀請一起記。')],
    plan=dict(title='免費開始，一人訂閱全家共享',
              text='基礎紀錄與相簿免費使用，家人人數不限。升級 Pro 或 Premium 後，爸媽、阿公阿嬤、保母一起用。實際方案以 App 內顯示為準。',
              ticks=['最大 200 GB 雲端空間、最長 3 分鐘 1080p 影片', '回顧影片匯出、AI 智慧相簿、足跡地圖、那年今天', '自訂浮水印', 'Premium 可免費試用 7 天']),
    faq=[('免費版和 Pro、Premium 差在哪？', '照顧紀錄、生長曲線、相簿與家人共享都能免費使用。升級後一人訂閱全家共享，解鎖更大空間、更長更清晰的影片、回顧影片、AI 相簿與浮水印；Premium 可免費試用 7 天。以 App 內顯示為準。'),
         ('生長曲線、體溫、疫苗提醒是醫療建議嗎？', '不是。這些是照顧者自己留下的紀錄與提醒，不能取代醫師。'),
         ('iOS 和 Android 都有嗎？', '都有。本頁上方的兩個按鈕就是 App Store 與 Google Play 的下載連結。')],
    help=[('常見問題', '方案、醫療提醒、支援平台', '#faq'),
          ('隱私權政策與條款', 'rigatw.github.io/easy2baby-legal', 'https://rigatw.github.io/easy2baby-legal/'),
          ('寫信給我們', EMAIL, 'mailto:' + EMAIL)],
    privacy='https://rigatw.github.io/easy2baby-legal/',
    page_title='Easy2Baby 輕鬆寶貝｜寶寶成長紀錄與家庭共享相簿',
    page_desc='Easy2Baby 輕鬆寶貝：單手記下餵食、睡眠、換尿布，生長曲線、餵藥鬧鐘，照片收成全家共享的成長相簿。iOS 與 Android 已上架。'),
  'ride': dict(
    slug='easy2ride', name='車伴', en='Easy2Ride', theme='t-ride',
    icon='/assets/img/apps/easy2ride-icon.webp',
    status='● 即將上架', lead='找車友、一起騎，安心上路。',
    desc='機車保養提醒、騎乘紀錄，找車友揪團、組車隊。給每一位騎士的愛車與路上夥伴。',
    ticks=['保養紀錄、證件到期提醒、油耗花費', '騎乘路線與里程，騎完做成重播影片', '揪團、車隊聊天室、集合點天氣'],
    stores=[('apple', '即將上架', 'App Store', ''), ('play', '即將上架', 'Google Play', '')],
    shots=[],
    feat=[('wrench', '照顧愛車', '保養紀錄、證件到期提醒、油耗與花費、記停車位置。'),
          ('route', '記錄每一趟', '路線、里程、爬升，騎完做成重播影片。'),
          ('people', '一起騎', '揪團、車隊聊天室、集合點天氣，活動當天看誰到了。'),
          ('shield', '安心上路', '手機驗證、公開揪團不開放一對一私訊，可檢舉與封鎖。')],
    plan=None, faq=[],
    help=[('支援與常見問題', 'easy2ride.web.app/support', 'https://easy2ride.web.app/support'),
          ('隱私權政策', 'easy2ride.web.app/privacy', 'https://easy2ride.web.app/privacy'),
          ('寫信給我們', EMAIL, 'mailto:' + EMAIL)],
    privacy='https://easy2ride.web.app/privacy',
    page_title='車伴 Easy2Ride｜機車保養提醒、騎乘紀錄與揪團車隊',
    page_desc='車伴 Easy2Ride：機車保養與證件到期提醒、騎乘路線紀錄與重播影片、找車友揪團與車隊聊天室。即將在 App Store 與 Google Play 上架。'),
  'deli': dict(
    slug='easy2delivery', name='Easy2Delivery', en='易送　外送路徑規劃助手', theme='t-deli',
    icon='/assets/img/apps/easy2delivery-icon.webp',
    status='● Android 已上架', lead='配送不繞路，準時不辛苦。',
    desc='給外送員、快遞司機與物流士的路徑規劃工具。截圖就能辨識地址，多點路線自動排好，再一鍵交給 Google Maps 或導航王。',
    ticks=['截圖自動辨識地址，多筆一次加入', '多點路徑自動排序，也能手動拖曳', '一鍵跳 Google Maps 或導航王'],
    stores=[('play', '在 Google Play 下載', 'Google Play', 'https://play.google.com/store/apps/details?id=com.rigataiwan.easy2delivery')],
    shots=[('/assets/img/apps/easy2delivery-hero.webp', '路線地圖'),
           ('/assets/img/apps/easy2delivery-list.webp', '路徑清單'),
           ('/assets/img/apps/easy2delivery-scan.webp', '拍照辨識地址'),
           ('/assets/img/apps/easy2delivery-nav.webp', '切換導航工具'),
           ('/assets/img/apps/easy2delivery-delivery.webp', '訂單介面'),
           ('/assets/img/apps/easy2delivery-station.webp', '安插加油站與換電站')],
    feat=[('camera', '截圖辨識地址', '截下 Lalamove、Uber Eats、foodpanda 等訂單畫面，自動抓出地址，可預覽、可修改。'),
          ('route', '多點路徑最佳化', '5 單或 50 單都自動排出最順的跑法，也能手動拖曳調整順序。'),
          ('list', '先取後送', '同一筆訂單一定先取件再送件，多單重疊時也不會排錯。'),
          ('nav', '一鍵導航', '點路徑清單裡的地址，直接開 Google Maps 或導航王，不用複製貼上。'),
          ('bolt', '安插能源站', '快沒油沒電時，沿路幫你插入加油站或 Gogoro 換電站。'),
          ('people', '雲端同步', '用 Google、Facebook 或 Email 登入，資料跟著帳號走。')],
    plan=dict(title='免費下載，需要再升級',
              text='基本的地址辨識、路徑規劃與導航串接免費使用。訂閱後解鎖更多進階功能，實際方案以 App 內顯示為準。',
              ticks=['更多路徑與站點數', '無廣告體驗']),
    faq=[('支援哪些導航軟體？', '支援 Google Maps 與導航王 TM 版（需另外安裝），可以在 App 內一鍵切換。'),
         ('iOS 和 Android 都可以用嗎？', '目前提供 Android 版，可在 Google Play 下載。'),
         ('付費訂閱和免費版差在哪？', '免費版就能辨識地址、規劃路線並開啟導航。訂閱後支援更多路徑與站點數，並且沒有廣告。實際方案以 App 內顯示為準。')],
    help=[('意見回饋', 'easy2live.net/easy2delivery/feedback', '/easy2delivery/feedback.html'),
          ('隱私權政策', 'easy2live.net/easy2delivery/privacy', '/easy2delivery/privacy.html'),
          ('寫信給我們', EMAIL, 'mailto:' + EMAIL)],
    privacy='/easy2delivery/privacy.html',
    page_title='Easy2Delivery 易送｜外送路徑規劃助手',
    page_desc='Easy2Delivery 易送：給外送員、快遞與物流司機的路徑規劃工具。截圖自動辨識地址、多點路徑最佳化、一鍵開啟 Google Maps 或導航王。Android 版已在 Google Play 上架。'),
}
ORDER = ['baby', 'ride', 'deli']

ICONS = {
  'clock': '<circle cx="18" cy="18" r="11"/><path d="M18 11v7l5 3"/>',
  'route': '<path d="M6 28c6-2 4-10 12-12s6-8 12-10"/><circle cx="6" cy="28" r="2.5"/><circle cx="30" cy="6" r="2.5"/>',
  'people': '<circle cx="12" cy="13" r="5"/><circle cx="24" cy="13" r="5"/><path d="M4 30c1-5 4-8 8-8s7 3 8 8M16 30c1-5 4-8 8-8s7 3 8 8"/>',
  'shield': '<path d="M18 5l11 4v8c0 7-5 12-11 14C12 29 7 24 7 17V9z"/><path d="M13 18l4 4 6-7"/>',
  'bottle': '<path d="M14 5h8M15 5v5l-3 4v15a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V14l-3-4V5"/><path d="M12 20h12"/>',
  'moon': '<path d="M27 21A11 11 0 1 1 15 7a9 9 0 0 0 12 14z"/>',
  'photo': '<rect x="5" y="7" width="26" height="22" rx="4"/><path d="M5 13h26M11 4v6M25 4v6"/><circle cx="18" cy="21" r="3"/>',
  'chart': '<path d="M6 30V6M6 30h24"/><path d="M10 24l6-7 5 4 8-10"/>',
  'camera': '<rect x="5" y="10" width="26" height="18" rx="3"/><path d="M13 10l2-4h6l2 4"/><circle cx="18" cy="19" r="5"/>',
  'nav': '<path d="M18 4l10 26-10-6-10 6z"/>',
  'bolt': '<path d="M20 4L9 20h8l-2 12 12-17h-8z"/>',
  'wrench': '<path d="M22 6a7 7 0 0 0-6 9L6 25a3 3 0 0 0 4 4l10-10a7 7 0 0 0 9-6l-4 1-3-3 1-4z"/>',
  'truck': '<path d="M3 9h18v15H3zM21 14h6l5 5v5H21z"/><circle cx="9" cy="27" r="3"/><circle cx="26" cy="27" r="3"/>',
  'list': '<rect x="7" y="5" width="22" height="27" rx="3"/><path d="M12 13h12M12 19h12M12 25h7"/>',
}

SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="i-apple" viewBox="0 0 24 24"><path d="M16.4 12.6c0-2.6 2.1-3.8 2.2-3.9-1.2-1.8-3.1-2-3.7-2-1.6-.2-3.1.9-3.9.9-.8 0-2-.9-3.4-.9-1.7 0-3.3 1-4.2 2.6-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8 1.6 0 2 .8 3.4.8 1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9-.1 0-2.7-1-2.7-4.1zM13.9 5c.7-.9 1.2-2 1-3.2-1 0-2.3.7-3 1.6-.7.8-1.2 2-1.1 3.1 1.2.1 2.3-.6 3.1-1.5z"/></symbol>
<symbol id="i-play" viewBox="0 0 24 24"><path d="M3.6 2.2c-.3.3-.4.7-.4 1.2v17.2c0 .5.1.9.4 1.2l9.6-9.8-9.6-9.8zm10.7 10.9 2.8 2.9-11.5 6.6 8.7-9.5zm0-2.2L5.6 1.4l11.5 6.6-2.8 2.9zm3.9 4.4 2.9-1.7c.8-.5.8-1.6 0-2.1l-2.9-1.7-3.1 3.2 3.1 2.3z"/></symbol>
</svg>'''

# ---------- 共用片段 ----------
def head(title, desc, path, extra=''):
    url = SITE + path
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="easy2live">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta property="og:locale" content="zh_TW">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D1320" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&display=swap">
<link rel="stylesheet" href="/assets/css/site.css?v={CSS_V}">
{extra}</head>
<body>
<a class="skip" href="#main">跳到主要內容</a>
{SPRITE}
'''

THEME_BTN = '''<button class="icon-btn" type="button" data-theme-toggle aria-label="切換深色或淺色模式">
<svg class="theme-light" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/></svg>
<svg class="theme-dark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
</button>'''

def header(current=''):
    def cur(k):
        return ' aria-current="page"' if k == current else ''
    app_links = ''.join(f'<a href="/{APPS[k]["slug"]}/"{cur(k)}>{e(APPS[k]["name"])}</a>' for k in ORDER)
    return f'''<header class="site"><div class="wrap">
  <a class="logo" href="/" aria-label="easy2live 首頁">easy<span class="two">2</span>live</a>
  <nav aria-label="主選單">
    <a class="hide-sm" href="/#apps">App</a>
    <a class="hide-sm" href="/design/"{cur('design')}>空間設計</a>
    <a class="hide-sm" href="/#contact">聯絡</a>
    {THEME_BTN}
    <details class="menu"><summary class="icon-btn" aria-label="開啟選單"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></summary>
      <div class="panel">{app_links}<a href="/design/">空間設計</a><a href="/#contact">聯絡</a></div>
    </details>
  </nav>
</div></header>
'''

def footer():
    apps = ''.join(f'<a href="/{APPS[k]["slug"]}/">{e(APPS[k]["name"] if k != "baby" else "Easy2Baby 輕鬆寶貝")}{" Easy2Ride" if k == "ride" else ""}</a>' for k in ORDER)
    priv = ''.join(f'<a href="{APPS[k]["privacy"]}">{e(APPS[k]["en"] if k == "baby" else APPS[k]["name"])}</a>' for k in ORDER)
    return f'''<div class="wrap"><footer class="site">
  <div><a class="logo" href="/">easy<span class="two">2</span>live</a><p>台灣的獨立 App 工作室<br>© 2026 easy2live</p></div>
  <div><h2>App</h2>{apps}</div>
  <div><h2>隱私權政策</h2>{priv}</div>
  <div><h2>其他</h2><a href="/design/">空間設計</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</footer></div>
<script src="/assets/js/site.js?v={JS_V}" defer></script>
</body>
</html>
'''

def store_buttons(a):
    out = []
    for icon, small, label, url in a['stores']:
        inner = f'<svg aria-hidden="true"><use href="#i-{icon}"/></svg><span><small>{e(small)}</small>{label}</span>'
        out.append(f'<a class="store" href="{url}" rel="noopener">{inner}</a>' if url else f'<span class="store soon">{inner}</span>')
    return ''.join(out)

def phone(src, alt, cls='', lazy=True):
    load = ' loading="lazy"' if lazy else ''
    return f'<div class="phone {cls}"><div class="screen"><img src="{src}" alt="{e(alt)}" width="360" height="780"{load}></div></div>'

def placeholder_phone(a, cls=''):
    # 還沒有截圖的 App：用圖示代替，不放假畫面
    return f'<div class="phone placeholder {cls}"><div class="screen" style="background:var(--ride)"><div><img src="{a["icon"]}" alt="" width="96" height="96" style="margin:0 auto 14px"><div style="font-weight:700">{e(a["name"])}</div><div style="font-size:13px;opacity:.8">即將上架</div></div></div></div>'

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

# ---------- 首頁 ----------
def build_home():
    b, r, d = APPS['baby'], APPS['ride'], APPS['deli']
    stage = (placeholder_phone(r, 's1') +
             phone(b['shots'][0][0], 'Easy2Baby 畫面', 's2', lazy=False) +
             phone(d['shots'][0][0], 'Easy2Delivery 畫面', 's3', lazy=False))
    trust = ''.join(f'<a href="/{APPS[k]["slug"]}/"><i class="dot" style="--c:var(--{ {"baby":"baby","ride":"ride","deli":"deli"}[k]})"></i>{e(APPS[k]["en"] if k=="baby" else APPS[k]["name"])}　{ "iOS 與 Android 已上架" if k=="baby" else ("即將上架" if k=="ride" else "Android 已上架")}</a>' for k in ORDER)
    products = []
    for i, k in enumerate(ORDER):
        a = APPS[k]
        shots = ''.join(phone(s, f'{a["name"]} 畫面：{c}') for s, c in a['shots'][:2]) or placeholder_phone(a)
        ticks = ''.join(f'<li>{e(t)}</li>' for t in a['ticks'])
        products.append(f'''<article class="product {a["theme"]}{" flip" if i == 1 else ""}">
  <div class="info">
    <div class="app-head"><div class="app-ic"><img src="{a["icon"]}" alt="" width="72" height="72"></div><h3>{e(a["name"])}<small>{e(a["en"])}</small></h3></div>
    <span class="status">{a["status"]}</span>
    <p class="tag">{e(a["lead"])}</p>
    <ul class="ticks">{ticks}</ul>
    <div class="stores">{store_buttons(a)}<a class="more" href="/{a["slug"]}/">了解 {e(a["en"] if k == "baby" else a["name"])}</a></div>
  </div>
  <div class="shot">{shots}</div>
</article>''')
    design_cover = MANIFEST['design'][13]['thumb']  # 客廳
    ld = json.dumps({"@context": "https://schema.org", "@type": "Organization", "name": "easy2live", "url": SITE,
                     "logo": SITE + "/apple-touch-icon.png", "email": EMAIL}, ensure_ascii=False)
    page = head('easy2live｜把生活的小麻煩，做成好用的 App',
                'easy2live 是台灣的獨立 App 工作室：Easy2Baby 輕鬆寶貝、車伴 Easy2Ride、Easy2Delivery，以及空間設計作品。',
                '/', f'<script type="application/ld+json">{ld}</script>\n')
    page += header() + f'''<main id="main">
<div class="wrap">
  <section class="hero">
    <div>
      <h1><span class="nw">把生活的小麻煩，</span><span class="nw">做成好用的 App。</span></h1>
      <p>easy2live 是台灣的獨立 App 工作室。記錄寶寶成長、照顧愛車和一起騎車、規劃外送路線：每一個 App 都從自己的日常出發。</p>
      <div class="cta"><a class="btn primary" href="#apps">看所有 App</a><a class="btn ghost" href="#contact">聯絡我們</a></div>
    </div>
    <div class="stage" aria-hidden="true">{stage}</div>
  </section>
  <div class="trust">{trust}</div>

  <div class="sec-title" id="apps"><h2>我們的 App</h2><p>免費下載，需要進階功能再訂閱。</p></div>
  {"".join(products)}

  <section class="about" id="about">
    <div>
      <h2>做 App 的人，<br>本業是室內設計。</h2>
      <p>easy2live 的開發者也是一位設計師爸爸。對空間與生活細節的在意，同樣放進每一個 App 的介面裡。</p>
    </div>
    <div class="works one">
      <a class="work" href="/design/"><img src="{design_cover}" alt="室內設計作品" width="720" height="405" loading="lazy"><div><b>空間設計</b><span>{len(MANIFEST["design"])} 張室內設計作品</span></div></a>
    </div>
  </section>

  <section class="contact" id="contact">
    <div><h2>有問題或想合作？</h2><p>App 使用問題、功能建議、設計委託，都可以寫信來。</p></div>
    <div>
      <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
      <div class="chips"><a class="btn ghost sm" href="/easy2baby/#faq">Easy2Baby 常見問題</a><a class="btn ghost sm" href="https://easy2ride.web.app/support">車伴支援</a><a class="btn ghost sm" href="/easy2delivery/feedback.html">Easy2Delivery 意見回饋</a></div>
    </div>
  </section>
</div>
</main>
''' + footer()
    write('index.html', page)

# ---------- App 介紹頁 ----------
def build_app(k):
    a = APPS[k]
    shots = a['shots']
    hero_shots = ''.join(phone(s, f'{a["name"]} 畫面：{c}', lazy=False) for s, c in shots[:2]) or placeholder_phone(a)
    feat = ''.join(f'<div><svg viewBox="0 0 36 36" aria-hidden="true">{ICONS[i]}</svg><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, t, d in a['feat'])
    four = ' four' if len(a['feat']) == 4 else ''
    screens = ''
    if len(shots) > 2:
        figs = ''.join(f'<figure>{phone(s, a["name"] + " 畫面：" + c)}<figcaption>{e(c)}</figcaption></figure>' for s, c in shots)
        screens = f'<div class="sec-title"><h2>介面</h2></div><div class="screens">{figs}</div>'
    plan = ''
    if a['plan']:
        p = a['plan']
        plan = f'''<section class="plan" style="margin-top:72px"><div><h2>{e(p["title"])}</h2><p>{e(p["text"])}</p></div><ul class="ticks">{"".join(f"<li>{e(t)}</li>" for t in p["ticks"])}</ul></section>'''
    faq = ''
    if a['faq']:
        qs = ''.join(f'<details><summary>{e(q)}</summary><p>{e(ans)}</p></details>' for q, ans in a['faq'])
        faq = f'<div class="sec-title" id="faq"><h2>常見問題</h2></div><div class="faq">{qs}</div>'
    help_ = ''.join(f'<a href="{u}"><b>{e(t)}</b><span>{e(d)}</span></a>' for t, d, u in a['help'])
    others = ''.join(f'<a href="/{APPS[o]["slug"]}/"><img src="{APPS[o]["icon"]}" alt="" width="56" height="56" loading="lazy"><div><b>{e(APPS[o]["name"])}</b><span>{e(APPS[o]["lead"])}</span></div></a>' for o in ORDER if o != k)
    page = head(a['page_title'], a['page_desc'], f'/{a["slug"]}/')
    page += header(k) + f'''<main id="main" class="{a["theme"]}">
<section class="ap-hero"><div class="wrap">
  <div class="info">
    <div class="big-ic"><img src="{a["icon"]}" alt="{e(a["name"])} 圖示" width="96" height="96"></div>
    <h1>{e(a["name"])}<small>{e(a["en"])}</small></h1>
    <span class="status">{a["status"]}</span>
    <p class="lead">{e(a["lead"])}</p>
    <p class="desc">{e(a["desc"])}</p>
    <div class="stores">{store_buttons(a)}</div>
  </div>
  <div class="shot">{hero_shots}</div>
</div></section>
<div class="wrap">
  <section class="feat{four}">{feat}</section>
  {screens}
  {plan}
  {faq}
  <div class="sec-title"><h2>支援與隱私</h2></div>
  <section class="help">{help_}</section>
  <div class="sec-title" style="padding-top:56px"><h2>其他 App</h2></div>
  <div class="others">{others}</div>
</div>
</main>
''' + footer()
    write(f'{a["slug"]}/index.html', page)

# ---------- Easy2Delivery 隱私權政策、意見回饋 ----------
def build_delivery_docs():
    crumb = '<div class="crumb"><a href="/">easy2live</a>　/　<a href="/easy2delivery/">Easy2Delivery</a></div>'
    privacy = head('隱私權政策｜Easy2Delivery', 'Easy2Delivery 隱私權政策：我們收集哪些資訊、如何使用與保護，以及您的權利。', '/easy2delivery/privacy.html')
    privacy += header('deli') + f'''<main id="main" class="wrap"><article class="doc">
{crumb}
<h1>隱私權政策</h1>
<p><strong>生效日期：2026 年 2 月 16 日</strong></p>
<p>Easy2Delivery（以下簡稱「本應用程式」）非常重視您的隱私權。本隱私權政策將說明我們如何收集、使用及保護您的個人資訊。</p>
<h2>1. 我們收集的資訊</h2>
<p>為了提供完整的服務，本應用程式可能會要求您提供或授權使用以下資訊：</p>
<ul>
<li><strong>1.1 位置資訊（Location Data）：</strong>用於提供即時導航、路徑規劃、計算預計到達時間（ETA）以及排序配送站點。若開啟「導航模式」，本應用程式可能會在背景持續存取您的位置，以確保在螢幕關閉時仍能提供功能。</li>
<li><strong>1.2 相機權限（Camera）：</strong>用於掃描 QR Code、拍攝貨運單據或是辨識地址文字（OCR）。除非您主動上傳設定為大頭貼，否則影像不會被永久儲存在我們的伺服器上。</li>
<li><strong>1.3 使用者個人資料（User Data）：</strong>若您選擇登入，我們會收集您的姓名、Email、手機號碼及大頭貼，用於建立帳戶及同步訂單紀錄。</li>
</ul>
<h2>2. 資訊使用方式</h2>
<p>我們收集的資訊僅用於提供與維護核心功能、個人化使用體驗及改善服務品質。我們不會將您的個人資訊出售或出租給任何第三方。</p>
<h2>3. 資料安全</h2>
<p>我們採取符合業界標準的安全措施（如 HTTPS 加密傳輸）來保護您的資料安全。但請諒解，網際網路傳輸無法保證 100% 安全。</p>
<h2>4. 您的權利</h2>
<p>您可以隨時在裝置設定中撤銷權限，或申請刪除您的帳戶及相關資料（請透過 App 內聯絡方式聯繫）。</p>
<h2>5. 政策變更</h2>
<p>我們可能會不時更新本政策。建議您定期查看本頁面以了解任何變更。</p>
<h2>6. 聯絡我們</h2>
<p>如果您對本隱私權政策有任何疑問，請聯繫我們：<br>Email：<a href="mailto:{EMAIL}">{EMAIL}</a></p>
</article></main>
''' + footer()
    write('easy2delivery/privacy.html', privacy)

    def mailto(subject):
        from urllib.parse import quote
        return f'mailto:{EMAIL}?subject={quote("[Easy2Delivery] " + subject)}'
    fb = head('意見回饋｜Easy2Delivery', '對 Easy2Delivery 有建議或遇到問題？寫信告訴我們。', '/easy2delivery/feedback.html')
    fb += header('deli') + f'''<main id="main" class="wrap"><article class="doc">
{crumb}
<h1>意見回饋</h1>
<p>使用上有建議，或遇到 Bug？寫信告訴我們。回報問題時，附上手機型號、Android 版本和畫面截圖，會更快找到原因。</p>
<div class="card">
  <p style="margin-top:0">選一個類型，會用你的郵件軟體開好一封信：</p>
  <div class="chips">
    <a class="btn primary sm" href="{mailto('問題回報')}">回報問題或 Bug</a>
    <a class="btn ghost sm" style="color:var(--ink)" href="{mailto('功能建議')}">功能建議</a>
    <a class="btn ghost sm" style="color:var(--ink)" href="{mailto('其他')}">其他</a>
  </div>
  <p style="margin-bottom:0">也可以直接寫信到 <a href="mailto:{EMAIL}">{EMAIL}</a>。</p>
</div>
</article></main>
''' + footer()
    write('easy2delivery/feedback.html', fb)

# ---------- 作品集 ----------
LIGHTBOX = '''<dialog class="lightbox" aria-label="放大檢視">
  <button class="prev" type="button" aria-label="上一張">‹</button>
  <img src="" alt="">
  <button class="next" type="button" aria-label="下一張">›</button>
  <button class="close" type="button" aria-label="關閉">✕</button>
  <div class="count"></div>
</dialog>'''

def build_gallery(kind):
    items = MANIFEST[kind]
    if kind == 'design':
        title, h1, desc, path, cur = '空間設計｜easy2live', '空間設計', '住宅與商業空間的室內設計作品，從平面配置、材質到光線，把日子住得舒服。', '/design/', 'design'
        alt = '室內設計作品'
    else:
        title, h1, desc, path, cur = '影像紀錄｜easy2live', '影像紀錄', '生活裡的光影與片刻，依拍攝日期排列。', '/photography/', 'photo'
        alt = '影像紀錄'
    cells = []
    for i, it in enumerate(items):
        th, tw = (it['h'], it['w'])
        sw, sh = 720, round(720 * th / tw) if tw >= th else 720
        if tw < th:
            sw, sh = round(720 * tw / th), 720
        date = it.get('date', '')
        label = f'{alt} {i + 1}' + (f'（{date}）' if date else '')
        d = f' data-date="{date}"' if date else ''
        tag = f'<span class="date">{date}</span>' if date else ''
        cells.append(f'<button type="button" data-full="{it["src"]}"{d} aria-label="放大 {e(label)}"><img src="{it["thumb"]}" alt="{e(label)}" width="{sw}" height="{sh}" loading="lazy">{tag}</button>')
    # 影像紀錄是家人生活照：網站上看得到，但不讓搜尋引擎收錄
    extra = '<meta name="robots" content="noindex">\n' if kind == 'photo' else ''
    page = head(title, desc, path, extra)
    page += header(cur) + f'''<main id="main" class="wrap">
<div class="gallery-head"><h1>{h1}</h1><p>{e(desc)}</p></div>
<div class="gallery">{"".join(cells)}</div>
{LIGHTBOX}
</main>
''' + footer()
    write(path.strip('/') + '/index.html', page)

def build_404():
    page = head('找不到這個頁面｜easy2live', '找不到這個頁面。', '/404.html')
    page += header() + '''<main id="main" class="wrap"><section class="notfound">
<h1>找不到這個頁面</h1>
<p>網址可能打錯了，或這個頁面已經搬家。</p>
<div class="cta" style="justify-content:center"><a class="btn primary" href="/">回到首頁</a><a class="btn ghost" href="/#apps">看所有 App</a></div>
</section></main>
''' + footer()
    write('404.html', page)

def build_meta():
    urls = ['/', '/easy2baby/', '/easy2ride/', '/easy2delivery/', '/easy2delivery/privacy.html', '/easy2delivery/feedback.html', '/design/']
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE}{u}</loc></url>\n' for u in urls) + '</urlset>\n'
    write('sitemap.xml', sm)
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')

if __name__ == '__main__':
    build_home()
    for k in ORDER:
        build_app(k)
    build_delivery_docs()
    build_gallery('design')
    build_404()
    build_meta()
    print('done')

/* =========================================
   Easy2Delivery 網站文字內容設定檔
   說明：您只需要修改冒號後面的引號內文字即可。
   注意：如果要換行 可以使用 <br> 標籤
========================================= */

const SITE_CONTENT = {
    // 1. 導覽列與全局設定
    brandNameBase: "Easy",
    brandNameNum: "2",
    brandNameSuffix: "Delivery",
    navLink1: "核心亮點",
    navLink2: "介面展示",
    navLink3: "訂閱會員",
    btnGooglePlay: "Google Play 免費下載",

    // 2. 首頁主視覺 (Hero Section)
    heroBadge: "全新外送物流路徑規劃APP",
    heroTitleLine1: "配送不繞路",
    heroTitleLine2: "準時不辛苦", // 會自動套用黃金漸層
    heroSubtitle: "為台灣外送員與貨運物流打造的嚴謹配送路徑優化系統。透過「先取後送」演算法，為您省下無謂的油耗與時間。",
    heroBtnText: "即將上架，敬請期待",
    heroTrustText: "超過 <strong>100+</strong> 使用者搶先預約",

    // 3. 核心技術與優勢 (Features Section)
    featuresTitle: "核心技術與優勢",
    featuresSubtitle: "結合台灣在地化實務需求，提供最符合外送情境的高效工具。",

    feature1Title: "嚴謹演算法：先取後送",
    feature1Desc: "確保外送訂單中「取件後才能送件」的嚴格邏輯。系統強制要求同筆訂單的取件優先，並在多單重疊時算出最順路徑，過濾邏輯錯誤，大幅提升效率與能源消耗。",

    feature2Title: "機車與汽貨車雙棲",
    feature2Desc: "機車專屬窄巷優化；汽貨車迴避禁行與小巷，各自動態計算最佳路徑。",

    feature3Title: "智慧辨識，解放雙手",
    feature3Desc: "領先業界的 OCR 引擎，拍照或截圖即可提取地址建立訂單。",

    feature4Title: "自由切換導航工具",
    feature4Desc: "提供極致直覺的介面，不強迫改變使用習慣。支援一鍵無縫串聯 Google Maps 或 導航王TM。",

    // 4. 實戰功能展示 (Showcase Section)
    showcaseTitle: "強大的實戰功能展示",
    showcaseSubtitle: "專為效率而生，從取件到送達，每個環節都為您精心設計。",

    showcase1Title: "智能辨識與批次匯入",
    showcase1Desc: "支援鏡頭直接掃描包裹地址或 QR Code，更提供文字批次貼上功能。系統會自動辨識並幫您將多筆取件/送件地址一次加入路線清單。",

    showcase2Title: "彈性路線與無縫導航整合",
    showcase2Desc: "清楚瀏覽包含多達數十個停靠點的「路徑清單」。提供外送、貨運等多樣模式與配送方式，隨時拖曳排序、一鍵清空或重新規劃。導航時，更可自由選擇跳轉至 Google Maps（單站/全路徑(10站點)）或導航王 TM，給您最大的操作自由。",

    showcase3Title: "專為實戰打造的路徑規劃介面",
    showcase3Desc: "專為外送、物流設計，清晰顯示取件送件點、下一站地址、預計抵達時間。結合台灣窄巷與大馬路的情境化考量，讓您輕鬆掌握最佳送件歷程，每張單都萬無一失。",

    showcase4Title: "確保能源無虞：即時安插加油站/換電站",
    showcase4Desc: "機車或汽貨車快沒油/沒電了？隨時點擊「搜尋加油站/GORORO換電站」選單，系統會自動考量目前的規劃路線，為您安插最佳停靠站，徹底告別續航焦慮。",

    // 5. 訂閱會員 (Pro Section)
    proTitle: "高級訂閱服務",
    proSubtitle: "解鎖進階功能，包含無限制路線規劃、專屬訂閱會員外觀，開啟優質路徑規劃體驗。",
    proBenefit1: "無上限多點路徑規劃",
    proBenefit2: "專屬黃金漸層會員卡",
    proBenefit3: "路徑規劃歷史、APP設定雲端備份",
    proBtnText: "立即升級",
    proCardName: "Easy2Delivery", // 卡片左上角名字

    // 6. 行動呼籲 (CTA Section)
    ctaTitle: "準備好提升你的外送效率了嗎？",
    ctaSubtitle: "即刻加入嚴謹路徑規劃的行列，體驗前所未有的優質演算法。",

    // 7. 常見問題 (FAQ Section)
    faqTitle: "常見問題",
    faqSubtitle: "有任何疑問嗎？看看這裡有沒有您需要的解答。",

    faq1Question: "支援哪些導航軟體？",
    faq1Answer: "<p>我們目前深度整合 <strong>Google Maps</strong> 以及 <strong>導航王 TM</strong>。您可以隨時在 APP 內一鍵切換，針對不同路況偏好選擇最適合您的導航引擎。</p>",

    faq2Question: "雙系統（iOS/Android）都可以用嗎？",
    faq2Answer: "<p>Easy2Delivery 目前只推出 Android 版本，目前正積極針對介面與效能優化。iOS版本尚未有開發計畫，如後續有新消息會在官網公布給大家知道！</p>",

    faq3Question: "付費訂閱和免費版的差別在哪裡？",
    faq3Answer: "<p>免費版提供基礎貨運模式路徑規劃(限制為四個站點)與無縫導航功能。升級為「高級訂閱服務」後，您將解鎖外送模式的嚴謹演算法，確保取件點優先於送貨點的前提條件與無上限多點路徑規劃、歷史紀錄與設定的雲端備份，以及專屬的訂閱會員外觀。</p>",

    // 8. 頁尾 (Footer)
    footerSlogan: "生活不該只有趕路，更該有輕鬆生活的溫度。",
    footerPrivacy: "隱私權政策 (Privacy Policy)",
    footerFeedback: "意見回饋 (Feedback)",
    footerCopyright: "© 2026 Easy2live.net | Easy2Delivery | Design DAD Project. Version: v1.0.25-beta."
};
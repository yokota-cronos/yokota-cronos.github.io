---
permalink: /
title: "生体データ通信インフラの無線フルボディ化"
seo_title: "生体データ通信インフラの無線フルボディ化"
excerpt: "Full-body Wireless Data and Power Networking"
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

<div class="hero-slideshow" aria-label="プロジェクト写真">
  <img class="hero-slide is-active" src="{{ base_path }}/images/hero/front1.jpg" alt="">
  <img class="hero-slide" loading="lazy" src="{{ base_path }}/images/hero/front2.jpg" alt="">
</div>

{% assign news = site.data.news | sort: "key" | reverse %}
<div class="news-carousel-wrap">
  <button class="news-arrow news-arrow--left" type="button" aria-label="前のニュース" hidden>&#8249;</button>
  <div class="news-carousel" id="newsCarousel">
{% for n in news limit:12 %}
  {% if n.url and n.url != "" %}<a class="news-card" href="{{ n.url }}" target="_blank" rel="noopener">{% else %}<div class="news-card">{% endif %}
    {% if n.category and n.category != "" %}{% case n.category %}{% when "受賞" %}{% assign badgeCls = "award" %}{% when "告知" %}{% assign badgeCls = "info" %}{% when "発表" %}{% assign badgeCls = "talk" %}{% when "採択" %}{% assign badgeCls = "grant" %}{% else %}{% assign badgeCls = "info" %}{% endcase %}<span class="news-badge news-badge--{{ badgeCls }}">{{ n.category }}</span>{% endif %}
    {% if n.image and n.image != "" %}<img class="news-thumb" loading="lazy" src="{{ base_path }}/images/news/{{ n.image }}" alt="">{% else %}<div class="news-thumb news-thumb--ph"></div>{% endif %}
    <div class="news-card-body">
      <div class="news-card-title">{{ n.title }}</div>
      <div class="news-card-date">{{ n.date }}</div>
    </div>
  {% if n.url and n.url != "" %}</a>{% else %}</div>{% endif %}
{% endfor %}
  </div>
  <button class="news-arrow news-arrow--right" type="button" aria-label="次のニュース" hidden>&#8250;</button>
</div>
{% if news.size > 4 %}<p class="news-more"><a href="{{ base_path }}/news/">View all news →</a></p>{% endif %}

<script>
(function () {
  var wrap = document.querySelector('.news-carousel-wrap');
  if (!wrap) return;
  var track = wrap.querySelector('.news-carousel');
  var left  = wrap.querySelector('.news-arrow--left');
  var right = wrap.querySelector('.news-arrow--right');

  function isPC() { return window.innerWidth >= 769; }

  function layout() {
    // いったんリセットして自然な位置を測る
    wrap.style.width = '';
    wrap.style.marginLeft = '';
    wrap.style.paddingLeft = '';
    wrap.style.paddingRight = '';
    if (isPC()) {
      var vw = document.documentElement.clientWidth;          // スクロールバー幅を除いた表示幅
      var l  = Math.max(0, wrap.getBoundingClientRect().left);// コンテンツ左端＝自然な左端
      wrap.style.width = vw + 'px';                           // 端から端まで
      wrap.style.marginLeft = (-l) + 'px';                    // ビューポート左端へ寄せる
      wrap.style.paddingLeft = l + 'px';                      // 先頭カードをコンテンツ左端に揃える
      wrap.style.paddingRight = l + 'px';
    }
    update();
  }

  function step() {
    var c = track.querySelector('.news-card');
    var w = c ? c.getBoundingClientRect().width : 300;
    return Math.max(w + 22, track.clientWidth * 0.8);
  }

  function update() {
    if (!left || !right) return;
    var max = track.scrollWidth - track.clientWidth - 1;
    var on = isPC();
    left.hidden  = !on || track.scrollLeft <= 0;
    right.hidden = !on || track.scrollLeft >= max;
  }

  if (left)  left.addEventListener('click',  function () { track.scrollBy({ left: -step(), behavior: 'smooth' }); });
  if (right) right.addEventListener('click', function () { track.scrollBy({ left:  step(), behavior: 'smooth' }); });
  track.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', layout);
  window.addEventListener('load', layout);
  layout();
})();
</script>

<span id="overview"></span>

皮膚の変形にも追従できる薄く軽い「スキンイメージャー」が、24時間365日、あなたの身体の声を聴き続けます。そんな未来の実現に向け、私たちは衣服そのものを安全な「二次元無線通信・給電インフラ」へと変貌させる、新たな生体データ通信システムに挑んでいます。周囲の空間から完全にアイソレートされた服型インフラが、スキンイメージャーへW級の安全なワイヤレス給電を常時行い、そこから溢れ出る大容量の生体データをMbps級の超セキュアな高速通信でクラウドへと紡ぎ続けます。目指すのは「病院に通う医療」から「日常に溶け込む予防医療」への転換です。病院インフラを社会へ分散させ、過疎地や災害現場でも誰もが最先端の医療アクセスを享受できる世界へ。二次元無線技術とスキンエレクトロニクスが融合する新時代を切り拓き、未来を担う次世代の人材を育成します。

この壮大なビジョンを共に社会実装へと導く、情熱を持ったポスドクおよびRA（リサーチアシスタント）を募集しています。現在は、東京大学（横田研究室）、高知工科大学（野田研究室）、公立はこだて未来大学（石田研究室）の各研究室にてメンバーを募集中です。専門分野の枠を超え、世界を変える次世代の医療・通信インフラを一緒に創り上げましょう。

<p class="keywords">キーワード： 生体データ通信、全身無線通信・給電服、メアンダコイル、二次元無線技術、スキンエレクトロニクス、NFC VHBR（高速NFC）</p>

<div class="concept-figs">
  <a class="concept-fig" href="https://arxiv.org/abs/2503.13240" target="_blank" rel="noopener"><img loading="lazy" src="{{ base_path }}/images/concept/concept1.jpg" alt="皮膚近傍に電磁界を閉じ込める「全身無線通信・給電服」"></a>
  <a class="concept-fig" href="https://www.nature.com/articles/s41928-019-0354-7" target="_blank" rel="noopener"><img loading="lazy" src="{{ base_path }}/images/concept/concept2.jpg" alt="医療インフラを病院から日常へ"></a>
  <div class="concept-fig"><img loading="lazy" src="{{ base_path }}/images/concept/concept3.jpg" alt="挑戦：3次元から2次元の無線通信・給電技術へ"></div>
  <div class="concept-fig"><img loading="lazy" src="{{ base_path }}/images/concept/concept4.jpg" alt="標準化戦略：次世代のNFCを目指して"></div>
</div>

<div class="ext-links">
  <a class="ext-gh ext-mail" href="mailto:takahashi@akg.t.u-tokyo.ac.jp" title="Contact"><i class="fas fa-envelope" aria-hidden="true"></i><span class="sr-only">Contact</span></a>
  <a class="ext-gh" href="https://github.com/yokota-cronos" target="_blank" rel="noopener" title="GitHub"><i class="fab fa-github" aria-hidden="true"></i><span class="sr-only">GitHub</span></a>
  <a class="ext-cronos" href="https://www.jst.go.jp/kisoken/cronos/" target="_blank" rel="noopener" title="JST CRONOS"><img src="{{ base_path }}/images/cronos_logo.jpg" alt="JST CRONOS"></a>
  <a class="ext-gh ext-picoring" href="https://picoring.github.io/" target="_blank" rel="noopener" title="PiCoRing"><i class="fas fa-ring" aria-hidden="true"></i><span class="sr-only">PiCoRing</span></a>
</div>

<h2 id="team">Team</h2>

<div class="member-grid">
{% for m in site.data.members %}
  <div class="member-card{% if m.bio and m.bio != '' %} has-bio{% endif %}" tabindex="0">
    <img class="member-photo" loading="lazy" src="{{ base_path }}/images/members/{{ m.photo }}" alt="{{ m.name_ja }}">
    <div class="member-name">{{ m.name_ja }}{% if m.bio and m.bio != "" %} <span class="bio-hint" title="経歴を表示">ⓘ</span>{% endif %}</div>
    <div class="member-name-en">{{ m.name_en }}</div>
    <div class="member-role">{{ m.role }}</div>
    <div class="member-aff">{{ m.affiliation | replace: ' ', '<br>' }}</div>
    <div class="member-links">
      {% if m.email and m.email != "" %}<a class="ico ico-mail" href="mailto:{{ m.email }}" title="Email"><i class="fas fa-envelope" aria-hidden="true"></i><span class="sr-only">Email</span></a>{% endif %}
      {% if m.scholar and m.scholar != "" %}<a class="ico ico-scholar" href="{{ m.scholar }}" title="Google Scholar" target="_blank" rel="noopener"><i class="ai ai-google-scholar" aria-hidden="true"></i><span class="sr-only">Google Scholar</span></a>{% endif %}
      {% if m.acm and m.acm != "" %}<a class="ico ico-acm" href="{{ m.acm }}" title="ACM Digital Library" target="_blank" rel="noopener"><i class="ai ai-acmdl" aria-hidden="true"></i><span class="sr-only">ACM Digital Library</span></a>{% endif %}
      {% if m.researchgate and m.researchgate != "" %}<a class="ico ico-rg" href="{{ m.researchgate }}" title="ResearchGate" target="_blank" rel="noopener"><i class="ai ai-researchgate" aria-hidden="true"></i><span class="sr-only">ResearchGate</span></a>{% endif %}
      {% if m.researchmap and m.researchmap != "" %}<a class="ico ico-rmap" href="{{ m.researchmap }}" title="researchmap" target="_blank" rel="noopener"><span class="rmap-txt" aria-hidden="true">rm</span><span class="sr-only">researchmap</span></a>{% endif %}
      {% if m.website and m.website != "" %}<a class="ico ico-web" href="{{ m.website }}" title="Webpage" target="_blank" rel="noopener"><i class="fas fa-globe" aria-hidden="true"></i><span class="sr-only">Webpage</span></a>{% endif %}
      {% if m.x and m.x != "" %}<a class="ico ico-x" href="{{ m.x }}" title="X" target="_blank" rel="noopener"><i class="fab fa-x-twitter" aria-hidden="true"></i><span class="sr-only">X</span></a>{% endif %}
      {% if m.instagram and m.instagram != "" %}<a class="ico ico-ig" href="{{ m.instagram }}" title="Instagram" target="_blank" rel="noopener"><i class="fab fa-instagram" aria-hidden="true"></i><span class="sr-only">Instagram</span></a>{% endif %}
      {% if m.linkedin and m.linkedin != "" %}<a class="ico ico-li" href="{{ m.linkedin }}" title="LinkedIn" target="_blank" rel="noopener"><i class="fab fa-linkedin-in" aria-hidden="true"></i><span class="sr-only">LinkedIn</span></a>{% endif %}
    </div>
    {% if m.bio and m.bio != "" %}<div class="member-bio" role="tooltip">{{ m.bio }}</div>{% endif %}
  </div>
{% endfor %}
</div>

<h2 id="publication">Publication</h2>

{% assign pubs = site.data.publications | sort: "year" | reverse %}
{% assign pubgroups = pubs | group_by: "year" | sort: "name" | reverse %}
{% for grp in pubgroups %}
<h3 class="year-head">{{ grp.name }}</h3>
<div class="pub-list2">
{% for p in grp.items %}
  {% if p.title and p.title != "" %}
  <div class="pub-entry">
    {% assign yt = p.youtube | default: p.video %}{% assign pgif = "" %}{% if yt and yt != "" %}{% if yt contains "v=" %}{% assign vid = yt | split: "v=" | last | split: "&" | first %}{% elsif yt contains "youtu.be/" %}{% assign vid = yt | split: "youtu.be/" | last | split: "?" | first %}{% else %}{% assign vid = "" %}{% endif %}{% if vid and vid != "" %}{% assign pgif = site.data.pub_gifs[vid] %}{% endif %}{% endif %}
    {% if pgif and pgif != "" %}<div class="pub-gif"><a href="{{ yt }}" target="_blank" rel="noopener" title="YouTube で再生">{% if pgif contains "http" %}<img loading="lazy" src="{{ pgif }}" alt="">{% else %}<img loading="lazy" src="{{ base_path }}/images/publications/{{ pgif }}" alt="">{% endif %}<span class="pub-gif-play" aria-hidden="true">▶</span></a></div>{% endif %}
    <div class="pub-main">
      {% if p.authors and p.authors != "" %}{% assign fn = p.first_authors | default: "" | replace: ", ", "|" | replace: ",", "|" | strip %}{% assign first_norm = "|" | append: fn | append: "|" %}{% assign cn = p.corresponding_authors | default: "" | replace: ", ", "|" | replace: ",", "|" | strip %}{% assign corr_norm = "|" | append: cn | append: "|" %}{% capture authorsfmt %}{% assign alist = p.authors | split: "," %}{% for a in alist %}{% assign an = a | strip %}{% if an != "" %}{% assign parts = an | split: " " %}{% for part in parts %}{% if part != "" %}{% if forloop.last %}{{ part }}{% else %}{{ part | slice: 0 }}. {% endif %}{% endif %}{% endfor %}{% assign namekey = "|" | append: an | append: "|" %}{% if first_norm contains namekey %}*{% endif %}{% if corr_norm contains namekey %}†{% endif %}{% unless forloop.last %}, {% endunless %}{% endif %}{% endfor %}{% endcapture %}<div class="pub-authors">{{ authorsfmt | strip }}</div>{% endif %}
      <div class="pub-title">{{ p.title | markdownify | remove: "<p>" | remove: "</p>" | strip }}</div>
      {% assign venue = p.publisher | default: p.venue %}{% if venue and venue != "" %}<div class="pub-venue"><span class="pub-venue-name">{{ venue }}</span>{% if p.volume and p.volume != "" %}, {{ p.volume }}{% if p.number and p.number != "" %}({{ p.number }}){% endif %}{% elsif p.number and p.number != "" %}, Article No. {{ p.number }}{% endif %}{% if p.pages and p.pages != "" %}, pp.{{ p.pages }}{% endif %}{% if p.year and p.year != "" %} ({{ p.year }}){% endif %}</div>{% endif %}
      <div class="pub-links">
        {% assign pdf = p.pdf | default: p.paper %}{% if pdf and pdf != "" %}{% if pdf contains "http" %}<a href="{{ pdf }}"{% else %}<a href="{{ base_path }}/paper/{{ pdf }}"{% endif %} target="_blank" rel="noopener">PDF</a>{% endif %}
        {% assign doi = p.doi | default: p.url %}{% if doi and doi != "" %}<a href="{{ doi }}" target="_blank" rel="noopener">DOI</a>{% endif %}
        {% if p.arxiv and p.arxiv != "" %}<a href="{{ p.arxiv }}" target="_blank" rel="noopener">arXiv</a>{% endif %}
        {% if p.code and p.code != "" %}<a href="{{ p.code }}" target="_blank" rel="noopener">Code</a>{% endif %}
        {% assign yt = p.youtube | default: p.video %}{% if yt and yt != "" %}<a href="{{ yt }}" target="_blank" rel="noopener">YouTube</a>{% endif %}
        {% if p.press and p.press != "" %}<a href="{{ p.press }}" target="_blank" rel="noopener">Press</a>{% endif %}
        {% if p.media and p.media != "" %}{% assign mediaurls = p.media | newline_to_br | replace: "<br />", " " | replace: "<br>", " " | replace: ",", " " | replace: ";", " " | replace: "|", " " | split: " " %}{% for murl in mediaurls %}{% assign m = murl | strip %}{% if m != "" and m contains "http" %}{% assign mhost = m | split: "//" | last | split: "/" | first | replace: "www.","" %}{% assign mname = mhost | split: "." | first | capitalize %}<a href="{{ m }}" target="_blank" rel="noopener">Media ({{ mname }})</a>{% endif %}{% endfor %}{% endif %}
        {% if p.bibtex and p.bibtex != "" %}<a href="#" class="pub-bib" role="button">BibTeX</a>{% endif %}
      </div>
      {% if p.bibtex and p.bibtex != "" %}<pre class="bib-pre" hidden>{{ p.bibtex | escape }}</pre>{% endif %}
    </div>
    {% if p.image and p.image != "" %}
    <div class="pub-thumb">{% if p.image contains "http" %}<img loading="lazy" src="{{ p.image }}" alt="">{% else %}<img loading="lazy" src="{{ base_path }}/images/publications/{{ p.image }}" alt="">{% endif %}</div>
    {% endif %}
  </div>
  {% endif %}
{% endfor %}
</div>
{% endfor %}

<h2 id="award">Award</h2>

{% assign awards = site.data.awards | sort: "year" | reverse %}
{% assign awgroups = awards | group_by: "year" | sort: "name" | reverse %}
{% for grp in awgroups %}
<h3 class="year-head">{{ grp.name }}</h3>
<ul class="pub-list">
{% for a in grp.items %}
  <li>
    {% assign who = a.recipient | default: a.authors %}<span class="pub-body">{% if a.url and a.url != "" %}<a href="{{ a.url }}" target="_blank" rel="noopener"><strong>{{ a.title }}</strong></a>{% else %}<strong>{{ a.title }}</strong>{% endif %}{% if who and who != "" %} — {{ who }}{% endif %}{% if a.organization and a.organization != "" %}（{{ a.organization }}）{% endif %}</span>
  </li>
{% endfor %}
</ul>
{% endfor %}

<h2 id="access">Access</h2>

<div class="loc-grid">
  <div class="loc-card">
    <span class="loc-badge">メイン拠点 / Main</span>
    <a class="loc-map-link" href="https://maps.app.goo.gl/PxrPWSs3PryMg9fM9" target="_blank" rel="noopener" title="Google マップで開く"><iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=35.9034904,139.9385322&z=17&output=embed"></iframe></a>
    <div class="loc-name">東京大学 柏キャンパス</div>
    <div class="loc-addr">〒277-8568 千葉県柏市柏の葉5-1-5<br>東京大学　柏キャンパス　第２総合研究棟 117号室<br>高橋 亮</div>
  </div>
  <div class="loc-card">
    <a class="loc-map-link" href="https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E6%96%87%E4%BA%AC%E5%8C%BA%E5%BC%A5%E7%94%9F2-11-16+%E6%9D%B1%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%9C%AC%E9%83%B7%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%91%E3%82%B9+%E5%B7%A5%E5%AD%A6%E9%83%A810%E5%8F%B7%E9%A4%A8" target="_blank" rel="noopener" title="Google マップで開く"><iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E6%9D%B1%E4%BA%AC%E9%83%BD%E6%96%87%E4%BA%AC%E5%8C%BA%E5%BC%A5%E7%94%9F2-11-16+%E6%9D%B1%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%9C%AC%E9%83%B7%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%91%E3%82%B9+%E5%B7%A5%E5%AD%A6%E9%83%A810%E5%8F%B7%E9%A4%A8&z=16&output=embed"></iframe></a>
    <div class="loc-name">東京大学 本郷キャンパス（浅野地区）横田研究室</div>
    <div class="loc-addr">〒113-0032 東京都文京区弥生2-11-16<br>東京大学　工学部10号館 3F 330号室<br>Tel: 03-5841-6709</div>
  </div>
  <div class="loc-card">
    <a class="loc-map-link" href="https://www.google.com/maps/search/?api=1&query=%E9%AB%98%E7%9F%A5%E7%9C%8C%E9%A6%99%E7%BE%8E%E5%B8%82%E5%9C%9F%E4%BD%90%E5%B1%B1%E7%94%B0%E7%94%BA%E5%AE%AE%E3%83%8E%E5%8F%A3185+%E9%AB%98%E7%9F%A5%E5%B7%A5%E7%A7%91%E5%A4%A7%E5%AD%A6" target="_blank" rel="noopener" title="Google マップで開く"><iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E9%AB%98%E7%9F%A5%E7%9C%8C%E9%A6%99%E7%BE%8E%E5%B8%82%E5%9C%9F%E4%BD%90%E5%B1%B1%E7%94%B0%E7%94%BA%E5%AE%AE%E3%83%8E%E5%8F%A3185+%E9%AB%98%E7%9F%A5%E5%B7%A5%E7%A7%91%E5%A4%A7%E5%AD%A6&z=15&output=embed"></iframe></a>
    <div class="loc-name">高知工科大学 システム工学群 野田研究室</div>
    <div class="loc-addr">〒782-8502 高知県香美市土佐山田町宮ノ口185<br>高知工科大学 A棟A405電子事務室<br>野田 聡人<br>Tel: 0887-53-1010</div>
  </div>
  <div class="loc-card">
    <a class="loc-map-link" href="https://www.google.com/maps/search/?api=1&query=%E5%8C%97%E6%B5%B7%E9%81%93%E5%87%BD%E9%A4%A8%E5%B8%82%E4%BA%80%E7%94%B0%E4%B8%AD%E9%87%8E%E7%94%BA116-2+%E5%85%AC%E7%AB%8B%E3%81%AF%E3%81%93%E3%81%A0%E3%81%A6%E6%9C%AA%E6%9D%A5%E5%A4%A7%E5%AD%A6" target="_blank" rel="noopener" title="Google マップで開く"><iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E5%8C%97%E6%B5%B7%E9%81%93%E5%87%BD%E9%A4%A8%E5%B8%82%E4%BA%80%E7%94%B0%E4%B8%AD%E9%87%8E%E7%94%BA116-2+%E5%85%AC%E7%AB%8B%E3%81%AF%E3%81%93%E3%81%A0%E3%81%A6%E6%9C%AA%E6%9D%A5%E5%A4%A7%E5%AD%A6&z=15&output=embed"></iframe></a>
    <div class="loc-name">公立はこだて未来大学 システム情報科学部 石田研究室</div>
    <div class="loc-addr">〒041-8655 北海道函館市亀田中野町116-2<br>公立はこだて未来大学 石田 繁巳<br>Tel: 0138-34-6477</div>
  </div>
</div>

<div class="acknowledgement">
  <img class="ack-logo" loading="lazy" src="{{ base_path }}/images/cronos_logo.jpg" alt="JST CRONOS">
  <p class="ack-text">本プロジェクトは、JST CRONOS 2025年度採択課題「生体データ通信インフラの無線フルボディ化」（JST CRONOS JPMJCS25N4）の支援を受けたものです。</p>
</div>

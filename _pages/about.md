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

<h2 id="news">News</h2>

{% assign news = site.data.news | sort: "key" | reverse %}
<div class="news-grid">
{% for n in news limit:4 %}
  {% if n.url and n.url != "" %}<a class="news-card" href="{{ n.url }}" target="_blank" rel="noopener">{% else %}<div class="news-card">{% endif %}
    {% if n.image and n.image != "" %}<img class="news-thumb" loading="lazy" src="{{ base_path }}/images/news/{{ n.image }}" alt="">{% else %}<div class="news-thumb news-thumb--ph"></div>{% endif %}
    <div class="news-card-body">
      <div class="news-card-title">{{ n.title }}</div>
      <div class="news-card-text">{{ n.text }}</div>
      <div class="news-card-date">{{ n.date }}</div>
    </div>
  {% if n.url and n.url != "" %}</a>{% else %}</div>{% endif %}
{% endfor %}
</div>
{% if news.size > 4 %}<p class="news-more"><a href="{{ base_path }}/news/">View all news →</a></p>{% endif %}

<span id="overview"></span>

皮膚に溶け込む超薄型センサー「スキンイメージャー」が、24時間365日、あなたの身体の声を聴き続ける。そんな未来の実現に向け、私たちは衣服そのものを安全な「二次元無線通信・給電インフラ」へと変貌させる、物理層からMAC層にわたる新設計に挑んでいます。周囲の空間から完全にアイソレートされた服型インフラが、5〜6個のセンサーへ5W級のワイヤレス給電を常時行い、そこから溢れ出る大容量の生体データを50 Mbps級の超セキュアなストリーミングで半日以上クラウドへと紡ぎ続けます。目指すのは「病院に通う医療」から「日常に溶け込む予防医療」への転換です。病院インフラを社会へ分散させ、過疎地や災害現場でも誰もが最先端の医療アクセスを享受できる世界へ。二次元無線技術とスキンエレクトロニクスが融合する新時代を切り拓き、未来を担う次世代の人材を育成します。

この壮大なビジョンを共に社会実装へと導く、情熱を持ったポスドクおよびRA（リサーチアシスタント）を募集しています。現在は、東京大学（横田研究室）、高知工科大学（野田研究室）、公立はこだて未来大学（石田研究室）の各研究室にてメンバーを募集中です。専門分野の枠を超え、世界を変える次世代の医療・通信インフラを一緒に創り上げましょう。

<p class="keywords">キーワード： 生体データ通信、全身無線通信・給電服、メアンダコイル、二次元無線技術、スキンエレクトロニクス、NFC VHBR（高速NFC）</p>

<div class="ext-links">
  <a class="ext-gh" href="https://github.com/yokota-cronos" target="_blank" rel="noopener" title="GitHub"><i class="fab fa-github" aria-hidden="true"></i><span class="sr-only">GitHub</span></a>
  <a class="ext-cronos" href="https://www.jst.go.jp/kisoken/cronos/" target="_blank" rel="noopener" title="JST CRONOS"><img src="{{ base_path }}/images/cronos_logo.jpg" alt="JST CRONOS"></a>
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
      {% if m.researchmap and m.researchmap != "" %}<a class="ico ico-rmap" href="{{ m.researchmap }}" title="researchmap" target="_blank" rel="noopener"><span class="rmap-txt" aria-hidden="true">rm</span><span class="sr-only">researchmap</span></a>{% endif %}
      {% if m.website and m.website != "" %}<a class="ico ico-web" href="{{ m.website }}" title="Webpage" target="_blank" rel="noopener"><i class="fas fa-globe" aria-hidden="true"></i><span class="sr-only">Webpage</span></a>{% endif %}
      {% if m.x and m.x != "" %}<a class="ico ico-x" href="{{ m.x }}" title="X" target="_blank" rel="noopener"><i class="fab fa-x-twitter" aria-hidden="true"></i><span class="sr-only">X</span></a>{% endif %}
      {% if m.linkedin and m.linkedin != "" %}<a class="ico ico-li" href="{{ m.linkedin }}" title="LinkedIn" target="_blank" rel="noopener"><i class="fab fa-linkedin-in" aria-hidden="true"></i><span class="sr-only">LinkedIn</span></a>{% endif %}
    </div>
    {% if m.bio and m.bio != "" %}<div class="member-bio" role="tooltip">{{ m.bio }}</div>{% endif %}
  </div>
{% endfor %}
</div>

<h2 id="publication">Publication</h2>

{% assign pubs = site.data.publications | sort: "year" | reverse %}
<div class="pub-list2">
{% for p in pubs %}
  <div class="pub-entry">
    <div class="pub-main">
      {% if p.authors and p.authors != "" %}<div class="pub-authors">{{ p.authors }}</div>{% endif %}
      <div class="pub-title">{{ p.title }}</div>
      {% assign venue = p.publisher | default: p.venue %}{% if venue and venue != "" %}<div class="pub-venue">{{ venue }}</div>{% endif %}
      <div class="pub-links">
        {% assign pdf = p.pdf | default: p.paper %}{% if pdf and pdf != "" %}{% if pdf contains "http" %}<a href="{{ pdf }}"{% else %}<a href="{{ base_path }}/paper/{{ pdf }}"{% endif %} target="_blank" rel="noopener">PDF</a>{% endif %}
        {% assign doi = p.doi | default: p.url %}{% if doi and doi != "" %}<a href="{{ doi }}" target="_blank" rel="noopener">DOI</a>{% endif %}
        {% if p.arxiv and p.arxiv != "" %}<a href="{{ p.arxiv }}" target="_blank" rel="noopener">arXiv</a>{% endif %}
        {% if p.code and p.code != "" %}<a href="{{ p.code }}" target="_blank" rel="noopener">Code</a>{% endif %}
        {% assign yt = p.youtube | default: p.video %}{% if yt and yt != "" %}<a href="{{ yt }}" target="_blank" rel="noopener">YouTube</a>{% endif %}
        {% if p.press and p.press != "" %}<a href="{{ p.press }}" target="_blank" rel="noopener">Press</a>{% endif %}
        {% if p.media and p.media != "" %}{% assign mhost = p.media | split: "//" | last | split: "/" | first | replace: "www.","" %}{% assign mname = mhost | split: "." | first | capitalize %}<a href="{{ p.media }}" target="_blank" rel="noopener">Media ({{ mname }})</a>{% endif %}
      </div>
    </div>
    {% if p.image and p.image != "" %}
    <div class="pub-thumb">{% if p.image contains "http" %}<img loading="lazy" src="{{ p.image }}" alt="">{% else %}<img loading="lazy" src="{{ base_path }}/images/publications/{{ p.image }}" alt="">{% endif %}</div>
    {% endif %}
  </div>
{% endfor %}
</div>

<h2 id="award">Award</h2>

{% assign awards = site.data.awards | sort: "year" | reverse %}
<ul class="pub-list">
{% for a in awards %}
  <li>
    <span class="pub-year">{{ a.year }}</span>
    {% assign who = a.recipient | default: a.authors %}<span class="pub-body">{% if a.url and a.url != "" %}<a href="{{ a.url }}" target="_blank" rel="noopener"><strong>{{ a.title }}</strong></a>{% else %}<strong>{{ a.title }}</strong>{% endif %}{% if who and who != "" %} — {{ who }}{% endif %}{% if a.organization and a.organization != "" %}（{{ a.organization }}）{% endif %}</span>
  </li>
{% endfor %}
</ul>

<h2 id="location">Location</h2>

<div class="loc-grid">
  <div class="loc-card">
    <span class="loc-badge">メイン拠点 / Main</span>
    <a class="loc-map-link" href="https://maps.app.goo.gl/PxrPWSs3PryMg9fM9" target="_blank" rel="noopener" title="Google マップで開く"><iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=35.9034904,139.9385322&z=17&output=embed"></iframe></a>
    <div class="loc-name">東京大学 柏キャンパス</div>
    <div class="loc-addr">〒277-8568 千葉県柏市柏の葉5-1-5<br>第２総合研究棟 117号室</div>
  </div>
  <div class="loc-card">
    <a class="loc-map-link" href="https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E6%96%87%E4%BA%AC%E5%8C%BA%E5%BC%A5%E7%94%9F2-11-16+%E6%9D%B1%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%9C%AC%E9%83%B7%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%91%E3%82%B9+%E5%B7%A5%E5%AD%A6%E9%83%A810%E5%8F%B7%E9%A4%A8" target="_blank" rel="noopener" title="Google マップで開く"><iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E6%9D%B1%E4%BA%AC%E9%83%BD%E6%96%87%E4%BA%AC%E5%8C%BA%E5%BC%A5%E7%94%9F2-11-16+%E6%9D%B1%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%9C%AC%E9%83%B7%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%91%E3%82%B9+%E5%B7%A5%E5%AD%A6%E9%83%A810%E5%8F%B7%E9%A4%A8&z=16&output=embed"></iframe></a>
    <div class="loc-name">東京大学 本郷キャンパス（浅野地区）横田研究室</div>
    <div class="loc-addr">〒113-0032 東京都文京区弥生2-11-16<br>工学部10号館 3F 330号室</div>
  </div>
  <div class="loc-card">
    <a class="loc-map-link" href="https://www.google.com/maps/search/?api=1&query=%E9%AB%98%E7%9F%A5%E7%9C%8C%E9%A6%99%E7%BE%8E%E5%B8%82%E5%9C%9F%E4%BD%90%E5%B1%B1%E7%94%B0%E7%94%BA%E5%AE%AE%E3%83%8E%E5%8F%A3185+%E9%AB%98%E7%9F%A5%E5%B7%A5%E7%A7%91%E5%A4%A7%E5%AD%A6" target="_blank" rel="noopener" title="Google マップで開く"><iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E9%AB%98%E7%9F%A5%E7%9C%8C%E9%A6%99%E7%BE%8E%E5%B8%82%E5%9C%9F%E4%BD%90%E5%B1%B1%E7%94%B0%E7%94%BA%E5%AE%AE%E3%83%8E%E5%8F%A3185+%E9%AB%98%E7%9F%A5%E5%B7%A5%E7%A7%91%E5%A4%A7%E5%AD%A6&z=15&output=embed"></iframe></a>
    <div class="loc-name">高知工科大学 システム工学群 野田研究室</div>
    <div class="loc-addr">〒782-8502 高知県香美市土佐山田町宮ノ口185<br>野田 聡人</div>
  </div>
  <div class="loc-card">
    <a class="loc-map-link" href="https://www.google.com/maps/search/?api=1&query=%E5%8C%97%E6%B5%B7%E9%81%93%E5%87%BD%E9%A4%A8%E5%B8%82%E4%BA%80%E7%94%B0%E4%B8%AD%E9%87%8E%E7%94%BA116-2+%E5%85%AC%E7%AB%8B%E3%81%AF%E3%81%93%E3%81%A0%E3%81%A6%E6%9C%AA%E6%9D%A5%E5%A4%A7%E5%AD%A6" target="_blank" rel="noopener" title="Google マップで開く"><iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E5%8C%97%E6%B5%B7%E9%81%93%E5%87%BD%E9%A4%A8%E5%B8%82%E4%BA%80%E7%94%B0%E4%B8%AD%E9%87%8E%E7%94%BA116-2+%E5%85%AC%E7%AB%8B%E3%81%AF%E3%81%93%E3%81%A0%E3%81%A6%E6%9C%AA%E6%9D%A5%E5%A4%A7%E5%AD%A6&z=15&output=embed"></iframe></a>
    <div class="loc-name">公立はこだて未来大学 システム情報科学部 石田研究室</div>
    <div class="loc-addr">〒041-8655 北海道函館市亀田中野町116-2<br>石田 繁巳</div>
  </div>
</div>

<div class="acknowledgement">
  <img class="ack-logo" loading="lazy" src="{{ base_path }}/images/cronos_logo.jpg" alt="JST CRONOS">
  <p class="ack-text">本プロジェクトは、JST CRONOS 2025年度採択課題「生体データ通信インフラの無線フルボディ化」（JST CRONOS JPMJCS25N4）の支援を受けたものです。</p>
</div>

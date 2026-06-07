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

<div class="hero">
  <p class="hero-program">JST CRONOS・2025年度 中尾領域（AREA 1, PO: 中尾）</p>
  <h1 class="hero-title">生体データ通信インフラの無線フルボディ化</h1>
  <p class="hero-subtitle">Full-body Wireless Data and Power Networking</p>
</div>

<h2 id="overview">プロジェクト概要 / Overview</h2>

皮膚に密着する「スキンイメージャー」の大容量生体データを半日以上クラウドへ連続ストリーミングする、**服型の生体データ通信インフラ**を実現します。周囲の空間とアイソレートした服型の**二次元無線通信・給電インフラ**を、物理層から MAC 層まで設計します。

<blockquote class="grand-challenge">
5〜6 つの「スキンイメージャー」を<strong>半日以上連続駆動</strong>するために、<strong>50 Mbps 級のセキュアな無線通信</strong>と <strong>5 W 級の安全な給電</strong>ができる<strong>「全身無線通信・給電服」</strong>を実現する。<br>
<span class="en">We realize <em>"full-body wireless data and power clothing"</em> capable of secure wireless communication at <strong>50 Mbps</strong> and safe wireless power at <strong>5 W</strong>, to continuously operate <em>"skin imagers"</em> around the body.</span>
</blockquote>

病後の通院治療から日常の**予防医療**へ。病院インフラの分散化や過疎地・災害現場での代替医療、二次元無線技術×スキンエレクトロニクスの人材育成を目指します。

<h2 id="members">メンバー / Team</h2>

<div class="member-grid">
{% for m in site.data.members %}
  <div class="member-card{% if m.bio and m.bio != '' %} has-bio{% endif %}" tabindex="0">
    {% if m.bio and m.bio != "" %}<div class="member-bio" role="tooltip">{{ m.bio }}</div>{% endif %}
    <img class="member-photo" src="{{ base_path }}/images/members/{{ m.photo }}" alt="{{ m.name_ja }}">
    <div class="member-name">{{ m.name_ja }}{% if m.bio and m.bio != "" %} <span class="bio-hint" title="経歴を表示">ⓘ</span>{% endif %}</div>
    <div class="member-name-en">{{ m.name_en }}</div>
    <div class="member-role">{{ m.role }}</div>
    <div class="member-aff">{{ m.affiliation }}</div>
    <div class="member-links">
      {% if m.email and m.email != "" %}<a class="ico ico-mail" href="mailto:{{ m.email }}" title="Email"><i class="fas fa-envelope" aria-hidden="true"></i><span class="sr-only">Email</span></a>{% endif %}
      {% if m.researchmap and m.researchmap != "" %}<a class="ico ico-rmap" href="{{ m.researchmap }}" title="researchmap" target="_blank" rel="noopener"><span class="rmap-txt" aria-hidden="true">rm</span><span class="sr-only">researchmap</span></a>{% endif %}
      {% if m.website and m.website != "" %}<a class="ico ico-web" href="{{ m.website }}" title="Webpage" target="_blank" rel="noopener"><i class="fas fa-globe" aria-hidden="true"></i><span class="sr-only">Webpage</span></a>{% endif %}
      {% if m.x and m.x != "" %}<a class="ico ico-x" href="{{ m.x }}" title="X" target="_blank" rel="noopener"><i class="fab fa-x-twitter" aria-hidden="true"></i><span class="sr-only">X</span></a>{% endif %}
      {% if m.linkedin and m.linkedin != "" %}<a class="ico ico-li" href="{{ m.linkedin }}" title="LinkedIn" target="_blank" rel="noopener"><i class="fab fa-linkedin-in" aria-hidden="true"></i><span class="sr-only">LinkedIn</span></a>{% endif %}
    </div>
  </div>
{% endfor %}
</div>

<h2 id="publications">Publications</h2>

<p class="data-note">※ 業績はスプレッドシートで管理し、1日1回 自動でこのページに反映されます。</p>

{% assign pubs = site.data.publications | sort: "year" | reverse %}
<ul class="pub-list">
{% for p in pubs %}
  <li>
    <span class="pub-year">{{ p.year }}</span>
    <span class="pub-body">{{ p.authors }}, {% if p.url and p.url != "" %}<a href="{{ p.url }}" target="_blank" rel="noopener"><strong>{{ p.title }}</strong></a>{% else %}<strong>{{ p.title }}</strong>{% endif %}{% if p.venue and p.venue != "" %}, <em>{{ p.venue }}</em>{% endif %}.</span>
  </li>
{% endfor %}
</ul>

<h2 id="awards">Awards / 受賞</h2>

{% assign awards = site.data.awards | sort: "year" | reverse %}
<ul class="pub-list">
{% for a in awards %}
  <li>
    <span class="pub-year">{{ a.year }}</span>
    <span class="pub-body">{% if a.url and a.url != "" %}<a href="{{ a.url }}" target="_blank" rel="noopener"><strong>{{ a.title }}</strong></a>{% else %}<strong>{{ a.title }}</strong>{% endif %}{% if a.recipient and a.recipient != "" %} — {{ a.recipient }}{% endif %}{% if a.organization and a.organization != "" %}（{{ a.organization }}）{% endif %}</span>
  </li>
{% endfor %}
</ul>

<h2 id="locations">活動場所 / Locations</h2>

<div class="loc-grid">
  <div class="loc-card">
    <span class="loc-badge">メイン拠点 / Main</span>
    <iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E5%8D%83%E8%91%89%E7%9C%8C%E6%9F%8F%E5%B8%82%E6%9F%8F%E3%81%AE%E8%91%895-1-5+%E6%9D%B1%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%9F%8F%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%91%E3%82%B9&z=16&output=embed"></iframe>
    <div class="loc-name">東京大学 柏キャンパス</div>
    <div class="loc-addr">〒277-8568 千葉県柏市柏の葉5-1-5<br>第２総合研究棟 117号室</div>
  </div>
  <div class="loc-card">
    <iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E6%9D%B1%E4%BA%AC%E9%83%BD%E6%96%87%E4%BA%AC%E5%8C%BA%E5%BC%A5%E7%94%9F2-11-16+%E6%9D%B1%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%9C%AC%E9%83%B7%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%91%E3%82%B9+%E5%B7%A5%E5%AD%A6%E9%83%A810%E5%8F%B7%E9%A4%A8&z=16&output=embed"></iframe>
    <div class="loc-name">東京大学 本郷キャンパス（浅野地区）</div>
    <div class="loc-addr">〒113-0032 東京都文京区弥生2-11-16<br>工学部10号館 3F 330号室</div>
  </div>
  <div class="loc-card">
    <iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E9%AB%98%E7%9F%A5%E7%9C%8C%E9%A6%99%E7%BE%8E%E5%B8%82%E5%9C%9F%E4%BD%90%E5%B1%B1%E7%94%B0%E7%94%BA%E5%AE%AE%E3%83%8E%E5%8F%A3185+%E9%AB%98%E7%9F%A5%E5%B7%A5%E7%A7%91%E5%A4%A7%E5%AD%A6&z=15&output=embed"></iframe>
    <div class="loc-name">高知工科大学 システム工学群</div>
    <div class="loc-addr">〒782-8502 高知県香美市土佐山田町宮ノ口185<br>野田 聡人</div>
  </div>
  <div class="loc-card">
    <iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E5%8C%97%E6%B5%B7%E9%81%93%E5%87%BD%E9%A4%A8%E5%B8%82%E4%BA%80%E7%94%B0%E4%B8%AD%E9%87%8E%E7%94%BA116-2+%E5%85%AC%E7%AB%8B%E3%81%AF%E3%81%93%E3%81%A0%E3%81%A6%E6%9C%AA%E6%9D%A5%E5%A4%A7%E5%AD%A6&z=15&output=embed"></iframe>
    <div class="loc-name">公立はこだて未来大学 システム情報科学部</div>
    <div class="loc-addr">〒041-8655 北海道函館市亀田中野町116-2<br>石田 繁巳</div>
  </div>
</div>

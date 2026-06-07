---
permalink: /
title: "生体データ通信インフラの無線フルボディ化"
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

本プロジェクトは、ヒトの皮膚に密着する「スキンイメージャー」から得られる大容量の生体データを、半日以上にわたり連続的にクラウドへストリーミングするための、**服型の生体データ通信インフラ**を実現します。

<blockquote class="grand-challenge">
ヒトの皮膚の色々な場所にある 5〜6 つの「スキンイメージャー」を<strong>半日以上連続駆動</strong>するために、<strong>50 Mbps 級のセキュアな無線通信</strong>と <strong>5 W 級の安全な給電</strong>ができる<strong>「全身無線通信・給電服」</strong>を実現する。<br>
<span class="en">We realize <em>"full-body wireless data and power clothing"</em> capable of secure wireless communication at <strong>50 Mbps</strong> and safe wireless power at <strong>5 W</strong>, to continuously operate <em>"skin imagers"</em> around the body.</span>
</blockquote>

### 研究概要 / Summary

- 薄く皮膚に密着できる**スキンイメージャー**を使って、生体データの病的なゆらぎを検知することで、日常での**予防医療**が期待できる。
- スキンイメージャーからの大容量の生体データを効率的にクラウドへストリーミングするために、**服型の生体データ通信インフラ**を間に構築する。
- 具体的には、周囲の空間伝送型の無線技術とは**アイソレートされた**、服型の**二次元無線通信・給電インフラ**を目指す。
- この環境下で、5〜6 つのスキンイメージャーの通信の挙動を同期制御できる**物理層**から、ヒトの動きなどを考慮した**MAC 層**を含めた、「全身無線通信・給電服」と「二次元通信・給電用プロトコル」を設計する。

### 想定する社会的インパクト / Social Impact

- 病後の通院治療から、日常での**予防医療へのシフト**
- 病院インフラの分散化や、**過疎地・災害現場での代替医療**
- 二次元無線技術とスキンエレクトロニクスの両分野で卓越した人材の育成

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
      {% if m.website and m.website != "" %}<a href="{{ m.website }}" title="Website" target="_blank" rel="noopener"><i class="fas fa-globe" aria-hidden="true"></i><span class="sr-only">Website</span></a>{% endif %}
      {% if m.x and m.x != "" %}<a href="{{ m.x }}" title="X" target="_blank" rel="noopener"><i class="fab fa-x-twitter" aria-hidden="true"></i><span class="sr-only">X</span></a>{% endif %}
      {% if m.researchmap and m.researchmap != "" %}<a href="{{ m.researchmap }}" title="researchmap" target="_blank" rel="noopener"><i class="fas fa-address-card" aria-hidden="true"></i><span class="sr-only">researchmap</span></a>{% endif %}
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

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
  <p class="hero-program">JST CRONOS 2025 · Area 1 (PO: Nakao)</p>
  <h1 class="hero-title">Full-body Wireless Data and Power Networking</h1>
</div>

<span id="overview"></span>

皮膚に密着する「スキンイメージャー」の大容量生体データを半日以上クラウドへ連続ストリーミングする、服型の生体データ通信インフラを実現します。周囲の空間とアイソレートした服型の二次元無線通信・給電インフラを、物理層から MAC 層まで設計します。5〜6 つの「スキンイメージャー」を半日以上連続駆動するために、50 Mbps 級のセキュアな無線通信と 5 W 級の安全な給電ができる「全身無線通信・給電服」を実現します。病後の通院治療から日常の予防医療へ。病院インフラの分散化や過疎地・災害現場での代替医療、二次元無線技術×スキンエレクトロニクスの人材育成を目指します。

<p class="keywords">キーワード： 生体データ通信、全身無線通信・給電服、メアンダコイル、二次元無線技術、スキンエレクトロニクス、NFC VHBR（高速NFC）</p>

<div class="ext-links">
  <a class="ext-gh" href="https://github.com/yokota-cronos" target="_blank" rel="noopener" title="GitHub"><i class="fab fa-github" aria-hidden="true"></i><span class="sr-only">GitHub</span></a>
  <a class="ext-cronos" href="https://www.jst.go.jp/kisoken/cronos/" target="_blank" rel="noopener" title="JST CRONOS"><img src="{{ base_path }}/images/cronos_logo.jpg" alt="JST CRONOS"></a>
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
      {% if p.venue and p.venue != "" %}<div class="pub-venue">{{ p.venue }}</div>{% endif %}
      <div class="pub-links">
        {% if p.paper and p.paper != "" %}{% if p.paper contains "http" %}<a href="{{ p.paper }}"{% else %}<a href="{{ base_path }}/paper/{{ p.paper }}"{% endif %} target="_blank" rel="noopener">Paper</a>{% endif %}
        {% assign doi = p.doi | default: p.url %}{% if doi and doi != "" %}<a href="{{ doi }}" target="_blank" rel="noopener">DOI</a>{% endif %}
        {% if p.video and p.video != "" %}<a href="{{ p.video }}" target="_blank" rel="noopener">Video</a>{% endif %}
        {% if p.code and p.code != "" %}<a href="{{ p.code }}" target="_blank" rel="noopener">Code</a>{% endif %}
        {% if p.project and p.project != "" %}<a href="{{ p.project }}" target="_blank" rel="noopener">Project</a>{% endif %}
        {% if p.news and p.news != "" %}<a href="{{ p.news }}" target="_blank" rel="noopener">News</a>{% endif %}
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
    <span class="pub-body">{% if a.url and a.url != "" %}<a href="{{ a.url }}" target="_blank" rel="noopener"><strong>{{ a.title }}</strong></a>{% else %}<strong>{{ a.title }}</strong>{% endif %}{% if a.recipient and a.recipient != "" %} — {{ a.recipient }}{% endif %}{% if a.organization and a.organization != "" %}（{{ a.organization }}）{% endif %}</span>
  </li>
{% endfor %}
</ul>

<h2 id="location">Location</h2>

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
    <div class="loc-name">東京大学 本郷キャンパス（浅野地区）横田研究室</div>
    <div class="loc-addr">〒113-0032 東京都文京区弥生2-11-16<br>工学部10号館 3F 330号室</div>
  </div>
  <div class="loc-card">
    <iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E9%AB%98%E7%9F%A5%E7%9C%8C%E9%A6%99%E7%BE%8E%E5%B8%82%E5%9C%9F%E4%BD%90%E5%B1%B1%E7%94%B0%E7%94%BA%E5%AE%AE%E3%83%8E%E5%8F%A3185+%E9%AB%98%E7%9F%A5%E5%B7%A5%E7%A7%91%E5%A4%A7%E5%AD%A6&z=15&output=embed"></iframe>
    <div class="loc-name">高知工科大学 システム工学群 野田研究室</div>
    <div class="loc-addr">〒782-8502 高知県香美市土佐山田町宮ノ口185<br>野田 聡人</div>
  </div>
  <div class="loc-card">
    <iframe class="loc-map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://maps.google.com/maps?q=%E5%8C%97%E6%B5%B7%E9%81%93%E5%87%BD%E9%A4%A8%E5%B8%82%E4%BA%80%E7%94%B0%E4%B8%AD%E9%87%8E%E7%94%BA116-2+%E5%85%AC%E7%AB%8B%E3%81%AF%E3%81%93%E3%81%A0%E3%81%A6%E6%9C%AA%E6%9D%A5%E5%A4%A7%E5%AD%A6&z=15&output=embed"></iframe>
    <div class="loc-name">公立はこだて未来大学 システム情報科学部 石田研究室</div>
    <div class="loc-addr">〒041-8655 北海道函館市亀田中野町116-2<br>石田 繁巳</div>
  </div>
</div>

<div class="acknowledgement">
  <img class="ack-logo" loading="lazy" src="{{ base_path }}/images/cronos_logo.jpg" alt="JST CRONOS">
  <p class="ack-text">本プロジェクトは、JST CRONOS 2025年度採択課題「生体データ通信インフラの無線フルボディ化」（JST CRONOS JPMJCS25N4）の支援を受けたものです。</p>
</div>

---
title: "Campaign Journals"
layout: git-wiki-default
published: true
---

# Campaign Journals

The official record of the Usurper's Bane mercenary company. Here you can find all session reports, story prologues, and chronicles of our journey through the tainted lands.

## All Entries

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a> 
    {% if post.date %}<small>— {{ post.date | date: "%-d %B %Y" }}</small>{% endif %}
    {% if post.type %} <span style="font-size: 11px; background-color: var(--ctp-main-surface1); padding: 2px 6px; border-radius: 4px; color: var(--ctp-main-subtext0);">{{ post.type }}</span>{% endif %}
  </li>
{% endfor %}
</ul>

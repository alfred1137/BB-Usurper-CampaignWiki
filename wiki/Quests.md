---
title: "Quests"
layout: git-wiki-default
published: true
---

The journey of the Usurper's Bane is marked by many trials, from personal arcs to the grand mandate of the Great Raven.

{% assign subcategories = "Main Quest,[Character Arc]({{ site.baseurl }}/Character%20Arc),Side Quest" | split: "," %}

{% for subcat in subcategories %}
## {{ subcat }}s

<ul>
{% assign items = site.pages | where: "category", "Quests" | where: "subcategory", subcat | sort: "title" %}
{% for item in items %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>
{% endfor %}

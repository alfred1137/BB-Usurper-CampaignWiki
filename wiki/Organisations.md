---
title: "Organisations"
layout: git-wiki-default
---

# Organisations

Various factions and groups vie for power and survival in this tainted world.

{% assign subcategories = "Mercenary Company" | split: "," %}

{% for subcat in subcategories %}
## {{ subcat }}s

<ul>
{% assign items = site.pages | where: "category", "Organisations" | where: "subcategory", subcat | sort: "title" %}
{% for item in items %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>
{% endfor %}

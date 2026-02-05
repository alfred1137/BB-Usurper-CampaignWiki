---
title: "Locations"
layout: git-wiki-default
published: true
---

# Locations

The world of Battle Brothers is vast and unforgiving. From the northern fortresses to the southern city-states, these are the places where our story unfolds.

{% assign subcategories = "Settlement,Point of Interest" | split: "," %}

{% for subcat in subcategories %}
## {{ subcat }}s

<ul>
{% assign items = site.pages | where: "category", "Locations" | where: "subcategory", subcat | sort: "title" %}
{% for item in items %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>
{% endfor %}

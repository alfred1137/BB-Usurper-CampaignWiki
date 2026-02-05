---
title: "Races"
layout: git-wiki-default
published: true
---

# Races and Classes

A guide to the various inhabitants of the world, including the diverse human classes and the monstrous threats that roam the wild.

{% assign subcategories = "Major Race,Special Class,Undead,Greenskin,Monster,Unique" | split: "," %}

{% for subcat in subcategories %}
## {{ subcat }}s

<ul>
{% assign items = site.pages | where: "category", "Races" | where: "subcategory", subcat | sort: "title" %}
{% for item in items %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>
{% endfor %}

---
title: "The Usurper's Bane"
layout: git-wiki-default
category: Organisations
subcategory: Mercenary Company
published: true
---

The Company of the main characters.

## Company Members

{% assign subcategories = "Protagonist,Party Member" | split: "," %}

{% for subcat in subcategories %}
### {{ subcat }}s

<ul>
{% assign members = site.pages | where: "category", "Characters" | where: "subcategory", subcat | where: "affiliation", "The Usurper's Bane" | sort: "title" %}
{% for member in members %}
  <li>
    <a href="{{ member.url | relative_url }}">{{ member.title }}</a>
    {% if member.alias and member.alias != "" %} (<i>{{ member.alias }}</i>){% endif %}
    {% if member.is_dead %} 💀{% endif %}
  </li>
{% endfor %}
</ul>
{% endfor %}

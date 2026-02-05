---
title: "Characters"
layout: git-wiki-default
published: true
---

# Characters

Welcome to the character directory of the Usurper's Bane Campaign. Here you can find information on the protagonists, the brave members of the mercenary company, and the formidable foes they face.

{% assign subcategories = "Protagonist,Party Member,Antagonist,Support Character" | split: "," %}

{% for subcat in subcategories %}
## {{ subcat }}s

<ul>
{% assign items = site.pages | where: "category", "Characters" | where: "subcategory", subcat | sort: "title" %}
{% for item in items %}
  <li>
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
    {% if item.alias and item.alias != "" %} (<i>{{ item.alias }}</i>){% endif %}
    {% if item.is_dead %} 💀{% endif %}
  </li>
{% endfor %}
</ul>
{% endfor %}

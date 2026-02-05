---
title: "The Usurper's Bane"
layout: git-wiki-default
category: [Organisations]({{ site.baseurl }}/Organisations)
subcategory: Mercenary Company
published: true
---

The Usurper's Bane is a mercenary company led by the Abyssal [Mage]({{ site.baseurl }}/Mage), [HiYun]({{ site.baseurl }}/HiYun), and his lieutenant, [NeCola]({{ site.baseurl }}/NeCola) the [Vatt'ghern]({{ site.baseurl }}/Vatt%27ghern). Founded on the outskirts of the Southern Wilds with a handful of desperate fishermen, the company has grown into a formidable regional power with a mission to topple the Usurper King and purge his chaotic influence from the world.

## History

The company began as a ragtag group of "fodder" recruits, often marked by the Raven's Blessing to increase their durability. Through a series of brutal contracts and supernatural encounters, the group hardened into a true fighting force. They have conquered northern champions, survived southern arenas, and successfully navigated the madness of the Chaos Plague.

## Notable Achievements

* **Champion Slayers**: Defeated legendary foes like Bakh Lob the Boil Burster and Borealis the Primal.
* **The Company Standard**: Officially raised a banner in the northern hills, signaling their transition from wandering vagabonds to a professional outfit.
* **Mastery of the Trial**: Successfully guided [NeCola]({{ site.baseurl }}/NeCola) through the [Trial of the Grasses]({{ site.baseurl }}/Trial%20of%20the%20Grasses) and began experimenting with advanced mutations like the Geist Mutagen.

## Company Members

{% assign subcategories = "Protagonist,Party Member" | split: "," %}

{% for subcat in subcategories %}
### {{ subcat }}s

<ul>
{% assign members = site.pages | where: "category", "[Characters]({{ site.baseurl }}/Characters)" | where: "subcategory", subcat | where: "affiliation", "The Usurper's Bane" | sort: "title" %}
{% for member in members %}
  <li>
    <a href="{{ member.url | relative_url }}">{{ member.title }}</a>
    {% if member.alias and member.alias != "" %} (<i>{{ member.alias }}</i>){% endif %}
    {% if member.is_dead %} 💀{% endif %}
  </li>
{% endfor %}
</ul>
{% endfor %}
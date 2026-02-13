---
title: "TEMPLATE - Session Journal Entry"
layout: git-wiki-post
type: Session
published: false
---


main body goes here

---

<table border="0">
  <tr>
    <td>⏏️ Return to catalogue</td>
    <td>|</td>
    <td style="text-align: right;">➡️ Read next chapter</td>
  </tr>
  <tr>
    <td><a href="{{ '/CampaignJournals/' | relative_url }}">Campaign Journals</a></td>
    <td>|</td>
    <td style="text-align: right;">
      {% if page.next and page.next.published != false %}
        <a href="{{ page.next.url | relative_url }}">{{ page.next.title }}</a>
      {% else %}
        Coming soon...
      {% endif %}
    </td>
  </tr>
</table>

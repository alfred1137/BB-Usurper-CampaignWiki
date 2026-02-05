---
title: "Campaign Journals"
layout: git-wiki-default
published: true
permalink: /CampaignJournals/
---

The official record of the Usurper's Bane mercenary company. Here you can find all session reports, story prologues, and chronicles of our journey through the tainted lands.

<table id="journal-table" class="w3-table w3-bordered w3-hoverable sortable-table">
  <thead>
    <tr class="w3-light-grey">
      <th style="cursor: pointer; width: 120px;">Date ↕</th>
      <th style="cursor: pointer;">Title ↕</th>
      <th style="cursor: pointer; width: 100px;">Type ↕</th>
    </tr>
  </thead>
  <tbody>
    {% assign sorted_posts = site.posts | sort: 'date' %}
    {% for post in sorted_posts %}
      {% if post.title != "Campaign Journals" %}
      <tr>
        <td>{{ post.date | date: "%Y-%m-%d" }}</td>
        <td><a href="{{ post.url | relative_url }}">{{ post.title }}</a></td>
        <td>
          {% if post.type %}
            <span style="font-size: 11px; background-color: var(--ctp-main-surface1); padding: 2px 6px; border-radius: 4px; color: var(--ctp-main-subtext0);">{{ post.type }}</span>
          {% endif %}
        </td>
      </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>

<script>
document.querySelectorAll('.sortable-table th').forEach(header => {
  header.addEventListener('click', () => {
    const table = header.closest('table');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const index = Array.from(header.parentElement.children).indexOf(header);
    const isAscending = header.classList.contains('th-sort-asc');
    
    table.querySelectorAll('th').forEach(th => th.classList.remove('th-sort-asc', 'th-sort-desc'));
    header.classList.toggle('th-sort-asc', !isAscending);
    header.classList.toggle('th-sort-desc', isAscending);
    
    rows.sort((a, b) => {
      const aText = a.children[index].textContent.trim();
      const bText = b.children[index].textContent.trim();
      
      // Numerical comparison for dates if first column
      if (index === 0) {
        return isAscending ? (aText < bText ? 1 : -1) : (aText > bText ? 1 : -1);
      }
      
      return isAscending ? bText.localeCompare(aText) : aText.localeCompare(bText);
    });
    
    tbody.append(...rows);
  });
});
</script>

<style>
.sortable-table th:hover {
  background-color: var(--ctp-main-surface0) !important;
}
.th-sort-asc::after { content: " ▲"; font-size: 10px; }
.th-sort-desc::after { content: " ▼"; font-size: 10px; }
</style>
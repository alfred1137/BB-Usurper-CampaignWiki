import os
import re

def update_nav_to_liquid(filepath):
    filename = os.path.basename(filepath)
    if "template" in filename.lower():
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The new Liquid table content
    liquid_table = """<table border="0">
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
</table>"""

    # Regex to match the existing table (handling potential typos and variations)
    # Matches <table ... </table> where it contains "Campaign Jounrals" or "Campaign Journals"
    table_pattern = re.compile(r'(<table\s+border="0">.*?Campaign\s+Jou.*?rnals.*?</table>)', re.DOTALL | re.IGNORECASE)

    if table_pattern.search(content):
        # Replace existing table
        new_content = table_pattern.sub(liquid_table, content)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Verified {filename}")
    else:
        # If no table found, append it if it looks like a session post
        # Heuristic: filename contains 'session' or 'prologue'
        if "session" in filename.lower() or "prologue" in filename.lower():
            if content.strip().endswith('---'):
                new_content = content.strip() + "\n\n" + liquid_table + "\n"
            else:
                new_content = content.strip() + "\n\n---\n\n" + liquid_table + "\n"
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Appended navigation to {filename}")

def main():
    base_dir = '_posts'
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                update_nav_to_liquid(os.path.join(root, file))

if __name__ == "__main__":
    main()

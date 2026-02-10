import os
import re

def get_session_info(filepath):
    filename = os.path.basename(filepath)
    if "template" in filename.lower():
        return None
    
    # Try to find session number or prologue
    # Session numbers can be in filename or title
    session_num = None
    if "prologue" in filename.lower():
        session_num = 0
    else:
        # Match 'session-X' or 'session-X.md'
        match = re.search(r'session-(\d+)', filename.lower())
        if match:
            session_num = int(match.group(1))
        else:
            # Check content for session number in title
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                title_match = re.search(r'title:\s*"(.*Session (\d+).*)"', content)
                if title_match:
                    session_num = int(title_match.group(2))
                
    if session_num is None:
        return None

    # Get title
    title = ""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        title_match = re.search(r'title:\s*"(.*)"', content)
        if title_match:
            title = title_match.group(1).split('"')[0]
            
    return {
        'num': session_num,
        'title': title,
        'path': filepath,
        'rel_to_posts': os.path.relpath(filepath, '_posts').replace('\\', '/')
    }

def update_nav(current_file, next_file):
    with open(current_file['path'], 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the navigation table
    # Specifically the NEXT part or the existing next title
    # The table structure:
    # <tr>
    #   <td>Campaign Jounrals</td>
    #   <td>|</td>
    #   <td style="text-align: right;">NEXT</td>
    # </tr>
    
    # Let's target the 3rd td in the second tr of the table
    # We look for a table that has '➡️ Read next chatper' or 'Campaign Jounrals'
    
    # First, construct the link
    # We'll use relative paths between files
    target_rel_path = os.path.relpath(next_file['path'], os.path.dirname(current_file['path'])).replace('\\', '/')
    
    # Clean up title for link text (remove internal markdown links like [Text](URL))
    clean_title = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', next_file['title'])
    link = f"[{clean_title}]({target_rel_path})"
    
    # Pattern to find the table and the cell to replace
    # We identify the table, then look for the second row's last cell.
    table_pattern = re.compile(r'(<table.*?>.*?➡️ Read next chatper.*?</tr>\s*<tr>\s*<td>Campaign Jounrals</td>\s*<td>\|</td>\s*<td.*?>)(.*?)(</td>\s*</tr>\s*</table>)', re.DOTALL | re.IGNORECASE)
    
    if table_pattern.search(content):
        new_content = table_pattern.sub(r'\1' + link + r'\3', content)
        if new_content != content:
            with open(current_file['path'], 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {current_file['rel_to_posts']} -> {next_file['rel_to_posts']}")
        else:
            print(f"No changes needed for {current_file['rel_to_posts']}")
    else:
        # If the table isn't present, maybe we should add it?
        # The user said "Notice how there is a navigation feature... update all posts"
        # If it's missing in drafts, maybe I should append it.
        # But for now, let's only update where it exists or provide a way to add it.
        
        # Check if the file has the '---' separator at the end
        if '---' in content:
            # Let's try to append it if it's missing but we have a next post
            table_template = f"""
---

<table border="0">
  <tr>
    <td>⏏️ Return to catalogue</td>
    <td>|</td>
    <td style="text-align: right;">➡️ Read next chatper</td>
  </tr>
  <tr>
    <td>Campaign Jounrals</td>
    <td>|</td>
    <td style="text-align: right;">{link}</td>
  </tr>
</table>
"""
            # Append if no table found
            if '<table' not in content:
                with open(current_file['path'], 'a', encoding='utf-8') as f:
                    f.write(table_template)
                print(f"Added navigation table to {current_file['rel_to_posts']} -> {next_file['rel_to_posts']}")

def main():
    base_dir = '_posts'
    posts = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                info = get_session_info(os.path.join(root, file))
                if info:
                    posts.append(info)
                    
    # Sort by session number
    posts.sort(key=lambda x: x['num'])
    
    for i in range(len(posts) - 1):
        update_nav(posts[i], posts[i+1])
        
    # For the last post, we might want to ensure it has a table but with placeholder
    # Or just leave it. If it has NEXT, replace with nothing or "Coming Soon"
    last_post = posts[-1]
    # (Optional: handle last post)

if __name__ == "__main__":
    main()

import os
import re
import urllib.parse
from pathlib import Path

def apply_links():
    wiki_dir = Path("wiki")
    posts_dir = Path("_posts")
    
    # 1. Gather entities
    entities = {}
    for ext in [".md"]:
        for file in wiki_dir.rglob(f"*{ext}"):
            if file.name == "example-page.md" or file.name == ".gitkeep":
                continue
            name = file.stem
            entities[name] = file.as_posix()

    if not entities:
        print("No entities found in wiki/")
        return

    # Sort entities by length descending to match longer names first
    sorted_names = sorted(entities.keys(), key=len, reverse=True)
    
    # Files to scan and update
    files_to_update = list(posts_dir.rglob("*.md")) + list(wiki_dir.rglob("*.md"))
    
    total_replacements = 0

    for file_path in files_to_update:
        if file_path.name == "example-page.md":
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        current_entity_name = file_path.stem
        
        link_placeholders = {}
        
        def protect_link(link_str):
            placeholder = f"__LINK_PLACEHOLDER_{len(link_placeholders)}__"
            link_placeholders[placeholder] = link_str
            return placeholder

        # 1. Identify and fix/protect existing links
        # Regex for [text](url) or ![alt](url)
        fixed_links_in_file = 0
        def link_handler(match):
            nonlocal fixed_links_in_file
            full_match = match.group(0)
            prefix_bracket = match.group(1) # '[' or '!['
            link_text = match.group(2)
            link_url = match.group(4)
            
            # If it's a wiki link (ends in .md), fix it
            if not prefix_bracket.startswith("!") and (".md" in link_url):
                # Extract the basename from the URL
                # We need to unquote it first to handle encoded spaces
                unquoted_url = urllib.parse.unquote(link_url)
                target_name = Path(unquoted_url).stem
                
                if target_name in entities:
                    encoded_name = urllib.parse.quote(target_name).replace("%2F", "/")
                    new_link = f"[{link_text}]({{{{ site.baseurl }}}}/{encoded_name})"
                    if new_link != full_match:
                        fixed_links_in_file += 1
                        return protect_link(new_link)
            
            return protect_link(full_match)

        # Regex: (!?\[)([^\]]*)(\]\()([^\)]+)(\))
        content = re.sub(r'(!?\[)([^\]]*)(\]\()([^\)]+)(\))', link_handler, content)

        replacements_in_file = 0
        
        # 2. Apply new links to remaining text
        for name in sorted_names:
            if name == current_entity_name and "wiki" in file_path.parts:
                continue
            
            if len(name) < 3: continue
            
            # Pattern to match the name as a whole word
            pattern = re.compile(r'\b' + re.escape(name) + r'\b')
            
            encoded_name = urllib.parse.quote(name).replace("%2F", "/")
            replacement = f"[{name}]({{{{ site.baseurl }}}}/{encoded_name})"
            
            def name_replacer(match):
                nonlocal replacements_in_file
                replacements_in_file += 1
                return protect_link(replacement)
            
            content = pattern.sub(name_replacer, content)

        # 3. Restore placeholders
        # Since we might have placeholders in a specific order, let's restore them
        # We use a loop because placeholders are unique and don't contain other placeholders
        for placeholder, original_link in link_placeholders.items():
            content = content.replace(placeholder, original_link)
            
        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Updated {file_path.as_posix()} ({fixed_links_in_file} fixed, {replacements_in_file} new)")
            total_replacements += fixed_links_in_file + replacements_in_file

    print(f"\nDone! Applied {total_replacements} links across the wiki.")

if __name__ == "__main__":
    apply_links()
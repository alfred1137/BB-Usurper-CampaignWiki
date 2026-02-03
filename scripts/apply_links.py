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
        
        # We'll use a placeholder system to avoid double-linking or linking inside existing links
        # 1. Find all existing links and replace them with placeholders
        link_placeholders = {}
        def link_replacer(match):
            placeholder = f"__LINK_PLACEHOLDER_{len(link_placeholders)}__"
            link_placeholders[placeholder] = match.group(0)
            return placeholder
        
        # Match [text](url)
        content = re.sub(r'\[[^\]]+\]\([^\)]+\)', link_replacer, content)
        # Match [text] (reference link) - optionally
        # content = re.sub(r'\[[^\]]+\]', link_replacer, content)

        replacements_in_file = 0
        
        for name in sorted_names:
            if name == current_entity_name and "wiki" in file_path.parts:
                continue
            
            if len(name) < 3: continue
            
            # Determine relative path to the entity
            target_path = entities[name]
            depth = len(file_path.parent.parts)
            rel_prefix = "../" * depth
            full_rel_path = rel_prefix + target_path
            
            # URL encode spaces and special characters
            encoded_rel_path = urllib.parse.quote(full_rel_path)
            encoded_rel_path = encoded_rel_path.replace("%2E%2E/%2E%2E/", "../../")
            encoded_rel_path = encoded_rel_path.replace("%2E%2E/", "../")
            encoded_rel_path = encoded_rel_path.replace("%2F", "/")
            
            replacement = f"[{name}]({encoded_rel_path})"
            
            # Pattern to match the name as a whole word, not preceded by [ or followed by ]( or )
            # We already replaced existing links with placeholders, so we just need whole word match.
            pattern = re.compile(r'\b' + re.escape(name) + r'\b')
            
            # We only want to replace if it's not already part of a placeholder
            new_content = ""
            last_end = 0
            for match in pattern.finditer(content):
                start, end = match.span()
                # Check if it's inside a placeholder (it shouldn't be because placeholders don't have word boundaries that match names)
                # But just in case, we check if the match is exactly a placeholder
                
                # Append text since last match
                new_content += content[last_end:start]
                
                # Double check: if it's already a link we should skip it.
                # Since we replaced existing links, we just check if it's part of a word that looks like a placeholder.
                # Actually, our placeholder is like __LINK_PLACEHOLDER_0__, which won't match '\bName\b'.
                
                new_content += replacement
                replacements_in_file += 1
                last_end = end
                
            new_content += content[last_end:]
            content = new_content

        # Restore placeholders
        for placeholder, original_link in link_placeholders.items():
            content = content.replace(placeholder, original_link)
            
        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Updated {file_path.as_posix()} ({replacements_in_file} links)")
            total_replacements += replacements_in_file

    print(f"\nDone! Applied {total_replacements} links across the wiki.")

if __name__ == "__main__":
    apply_links()

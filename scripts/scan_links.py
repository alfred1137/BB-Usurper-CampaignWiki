import os
import re
import urllib.parse
from pathlib import Path

def scan_links():
    wiki_dir = Path("wiki")
    posts_dir = Path("_posts")
    
    # 1. Gather entities
    entities = {}
    for ext in [".md"]:
        for file in wiki_dir.rglob(f"*{ext}"):
            if file.name == "example-page.md":
                continue
            name = file.stem
            # Store the relative path from the root
            entities[name] = file.as_posix()

    if not entities:
        print("No entities found in wiki/")
        return

    # Sort entities by length descending to match longer names first
    sorted_names = sorted(entities.keys(), key=len, reverse=True)
    
    # Files to scan
    files_to_scan = list(posts_dir.rglob("*.md")) + list(wiki_dir.rglob("*.md"))
    
    matches_found = []

    for file_path in files_to_scan:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Skip the entity's own file
        current_entity_name = file_path.stem
        
        for name in sorted_names:
            if name == current_entity_name and "wiki" in file_path.parts:
                continue
                
            # Skip very short common names if desired, but for now we follow the user's intent
            if len(name) < 3: continue
            
            pattern = re.compile(r'\b' + re.escape(name) + r'\b')
            
            for match in pattern.finditer(content):
                start, end = match.span()
                
                # Simple check for existing link context (200 chars around)
                context_window = content[max(0, start-100):end+100]
                # If name is inside [ ] and followed by (
                if re.search(r'\[[^\]]*' + re.escape(name) + r'[^\]]*\]\(', context_window):
                    continue
                
                # If name is inside [ ] (reference link)
                if re.search(r'\[' + re.escape(name) + r'\]', content[max(0, start-5):end+5]):
                    continue
                    
                # Get context
                line_start = content.rfind('\n', 0, start) + 1
                line_end = content.find('\n', end)
                if line_end == -1: line_end = len(content)
                line_content = content[line_start:line_end].strip()
                
                line_num = content.count('\n', 0, start) + 1
                
                # Determine relative path to the entity
                target_path = entities[name]
                
                # Calculate relative path from file_path to target_path
                # file_path is e.g. _posts/2026-01-01-post.md
                # target_path is e.g. wiki/characters/HiYun.md
                
                try:
                    # Logic for relative path:
                    # If in _posts/, we are 1 level deep. Need to go up 1 level to root.
                    # If in wiki/characters/, we are 2 levels deep. Need to go up 2 levels to root.
                    
                    depth = len(file_path.parent.parts)
                    rel_prefix = "../" * depth
                    full_rel_path = rel_prefix + target_path
                    
                    # URL encode spaces
                    encoded_rel_path = urllib.parse.quote(full_rel_path)
                    # But we want to preserve / and ..
                    encoded_rel_path = encoded_rel_path.replace("%2E%2E/%2E%2E/", "../../")
                    encoded_rel_path = encoded_rel_path.replace("%2E%2E/", "../")
                    encoded_rel_path = encoded_rel_path.replace("%2F", "/")
                except Exception:
                    encoded_rel_path = target_path # Fallback

                matches_found.append({
                    "file": file_path.as_posix(),
                    "line": line_num,
                    "name": name,
                    "target": encoded_rel_path,
                    "context": line_content
                })

    if not matches_found:
        print("No potential links found.")
        return

    print(f"Found {len(matches_found)} potential links:")
    # Group by file for easier review
    current_file = None
    for m in matches_found:
        if m['file'] != current_file:
            print(f"\n📂 File: {m['file']}")
            current_file = m['file']
        print(f"   L{m['line']}: '{m['name']}' -> {m['target']}")
        print(f"      Context: {m['context']}")


if __name__ == "__main__":
    scan_links()

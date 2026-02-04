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
                
                # The target URL is simply the basename with site.baseurl
                encoded_name = urllib.parse.quote(name)
                target_url = f"{{{{ site.baseurl }}}}/{encoded_name}"

                matches_found.append({
                    "file": file_path.as_posix(),
                    "line": line_num,
                    "name": name,
                    "target": target_url,
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

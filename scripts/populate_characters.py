
import os
import re
import collections

# Config
LOG_DIR = r"d:\Git\BB-Usurper-CampaignWiki\.log"
CHAR_DIR = r"d:\Git\BB-Usurper-CampaignWiki\wiki\characters"
TEMPLATE_FILE = os.path.join(CHAR_DIR, "99 Bro Template.md")

JUNK_WORDS = {
    "character", "name", "units", "kills", "damage", "xp", "taken", "health", "injuries", "morale",
    "healthy", "injured", "critical", "deceased", "excellent", "rising", "steady", "heroic",
    "role", "class", "survivor", "fodder", "none", "objective", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
}

def get_existing_characters():
    chars = set()
    if os.path.exists(CHAR_DIR):
        for f in os.listdir(CHAR_DIR):
            if f.endswith(".md") and f != "99 Bro Template.md":
                # Store full filename without extension
                chars.add(f.replace(".md", ""))
    return chars

def extract_names_from_logs():
    # Map name -> session_id (integer)
    # We want names from later sessions to override earlier ones
    candidates = {}
    
    table_row_re = re.compile(r"\|\s*([A-Za-z0-9\s'-]+?)\s*\|\s*\d+\s*\|")
    
    # Process files in order
    files = sorted([f for f in os.listdir(LOG_DIR) if f.endswith(".md")], key=lambda x: extract_session_num(x))
    
    for f in files:
        session_num = extract_session_num(f)
        path = os.path.join(LOG_DIR, f)
        
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = table_row_re.findall(content)
            
            for m in matches:
                name = m.strip()
                # Basic filter
                if not name: continue
                # Title casing
                name_title = name.title()
                
                # Check junk
                first_word = name_title.split()[0].lower()
                if first_word in JUNK_WORDS: continue
                if any(c.isdigit() for c in name): continue # Skip "Level 11" etc if filtered poorly
                
                # Store with session num
                candidates[name_title] = session_num
                
    return candidates

def extract_session_num(filename):
    # session-10-log.md
    m = re.search(r"session-(\d+)", filename)
    if m:
        return int(m.group(1))
    return 0

def create_character_file(name, template_content):
    filename = f"{name}.md"
    path = os.path.join(CHAR_DIR, filename)
    
    if os.path.exists(path):
        print(f"Skipping {filename} (Exists)")
        return
    
    # Replace template placeholders
    content = template_content.replace('title: "BRO TEMPLATE"', f'title: "{name}"')
    
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created {filename}")
    except Exception as e:
        print(f"Error creating {filename}: {e}")

def main():
    print("Reading template...")
    try:
        with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except Exception as e:
        print(f"Error reading template: {e}")
        return

    existing = get_existing_characters()
    existing_lower = {e.lower() for e in existing}
    
    candidates_map = extract_names_from_logs()
    
    # Group candidates by First Word to handle deduplication and matching
    groups = collections.defaultdict(list) # first_word -> list of (name, session_num)
    
    for name, session_num in candidates_map.items():
        first_word = name.split()[0]
        groups[first_word].append((name, session_num))
        
    created_count = 0
    
    for first_word, entries in groups.items():
        # 1. Check if ANY existing character matches this First Word group
        # Broad check: is "First Word" a prefix of any existing char? or contained?
        # "NeCola" exists -> matches group "Necola" (Necola The Silver Sword)
        is_covered = False
        first_word_lower = first_word.lower()
        
        for ex in existing_lower:
            # Check overlap
            ex_first = ex.split()[0]
            if ex_first == first_word_lower:
                is_covered = True
                break
            if first_word_lower == "lady" and "lady" in ex: # Lady Amelia
                is_covered = True # Wait, if Lady Amelia exists, we skip Lady Amelia A?
                # Ideally yes.
                break
                
        if is_covered:
            # We assume this group is represented by an existing file
            continue
            
        # 2. Select best candidate from group
        # Prefer latest session, then longest name?
        # Sort by Session Desc, then Length Desc
        entries.sort(key=lambda x: (x[1], len(x[0])), reverse=True)
        best_name = entries[0][0]
        
        # Double check exact existence again just in case
        if best_name.lower() in existing_lower:
            continue
            
        create_character_file(best_name, template_content)
        created_count += 1
        
    print(f"Finished. Created {created_count} new character files.")

if __name__ == "__main__":
    main()

import os
import json
import re
import shutil
from pathlib import Path
from datetime import datetime

# Configuration
SOURCE_DIR = Path(r"d:\Git\BB-Usurper-CampaignWiki\.gemini\kanka-bkup")
TARGET_DIR = Path(r"d:\Git\BB-Usurper-CampaignWiki")
POSTS_DIR = TARGET_DIR / "_posts"
WIKI_DIR = TARGET_DIR / "wiki"
ASSETS_DIR = TARGET_DIR / "assets"

# Kanka entity types to Wiki folders or special handling
ENTITY_TYPES = {
    "characters": "characters",
    "locations": "locations",
    "races": "races",
    "organisations": "organisations",
    "quests": "quests",
    "journals": "_posts"
}

# Mappings
id_to_name = {}
id_to_type = {}
uuid_to_filename = {}
uuid_to_orig_name = {}

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    return text

def html_to_md(html):
    if not html:
        return ""
    # Very basic HTML to MD conversion
    md = html
    # Strip spans and divs but keep content
    md = re.sub(r'</?(span|div|font)[^>]*>', '', md, flags=re.IGNORECASE)
    
    md = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<br\s*/?>', r'\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'* \1', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<ul[^>]*>(.*?)</ul>', r'\1\n', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<ol[^>]*>(.*?)</ol>', r'\1\n', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'> \1\n', md, flags=re.IGNORECASE|re.DOTALL)
    md = re.sub(r'<hr\s*/?>', r'---\n', md, flags=re.IGNORECASE)
    
    # Handle Tables (very basic)
    md = re.sub(r'<table[^>]*>.*?</table>', lambda m: "\n[Table omitted - see original]\n", md, flags=re.IGNORECASE|re.DOTALL)

    # Handle Kanka Image Tags in Entries
    def replace_img(match):
        uuid = re.search(r'data-gallery-id="([^"]+)"', match.group(0))
        if uuid:
            uuid = uuid.group(1)
            filename = uuid_to_filename.get(uuid)
            if filename:
                return f'![{uuid_to_orig_name.get(uuid, "Image")}](/assets/images/placeholder_{uuid})'
        # Fallback to src
        src = re.search(r'src="([^"]+)"', match.group(0))
        if src:
            return f'![Image]({src.group(1)})'
        return ""

    md = re.sub(r'<img[^>]+>', replace_img, md)

    # Handle Links (<a> tags)
    def replace_a(match):
        text = match.group(1)
        href = re.search(r'href="([^"]+)"', match.group(0))
        if href:
            h = href.group(1)
            # Check if it's an internal Kanka link that should be resolved
            # Often these look like /w/campaign_id/entities/id or similar
            # But the user also has [type:id] format which resolve_links handles.
            # We'll just keep the text for now if it's complex, or convert to wiki link if simple
            return text
        return text

    md = re.sub(r'<a[^>]*>(.*?)</a>', replace_a, md, flags=re.IGNORECASE|re.DOTALL)
    
    # Clean up remaining tags
    md = re.sub(r'<[^>]+>', '', md)
    # Unescape common HTML entities
    md = md.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
    
    return md.strip()

def get_metadata_md(data):
    lines = []
    
    # Common fields
    etype = data.get('entity', {}).get('type') or data.get('type')
    if etype: lines.append(f"**Type**: {etype}")
    
    # Character specific
    if 'sex' in data and data['sex']: lines.append(f"**Sex**: {data['sex']}")
    if 'age' in data and data['age']: lines.append(f"**Age**: {data['age']}")
    if 'title' in data and data['title']: lines.append(f"**Title**: {data['title']}")
    if 'is_dead' in data and data['is_dead']: lines.append("**Status**: 💀 Dead")

    # Attributes
    attrs = data.get('entity', {}).get('entityAttributes', [])
    if attrs:
        attr_lines = []
        for attr in attrs:
            val = attr.get('value')
            if val is not None and str(val).strip():
                attr_lines.append(f"| {attr['name']} | {val} |")
        if attr_lines:
            lines.append("\n### Attributes")
            lines.append("| Name | Value |")
            lines.append("| --- | --- |")
            lines.extend(attr_lines)

    # Memberships
    mships = data.get('organisationMemberships') or data.get('organisation_memberships')
    if mships:
        lines.append("\n### Memberships")
        for m in mships:
            oid = m.get('organisation_id')
            oname = id_to_name.get(oid, f"Organisation {oid}")
            role = m.get('role', 'Member')
            lines.append(f"* **{oname}**: {role}")

    return "\n".join(lines) + "\n\n" if lines else ""

def write_md_file(target_path, title, content, metadata_md="", image_header=""):
    with open(target_path, 'w', encoding='utf-8') as out:
        out.write("---\n")
        out.write(f"title: \"{title}\"\n")
        # Determine layout based on path
        if "_posts" in str(target_path):
            out.write("layout: git-wiki-post\n")
        else:
            out.write("layout: git-wiki-default\n")
        out.write("---\n\n")
        out.write(image_header)
        out.write(metadata_md)
        out.write(content)

def resolve_links(md):
    # Kanka links: [character:123], [location:456], [journal:789], etc.
    def replace_link(match):
        etype = match.group(1)
        eid = match.group(2)
        name = id_to_name.get(int(eid))
        if name:
            return f"[[{name}]]"
        return match.group(0)

    return re.sub(r'\[(character|location|journal|race|organisation|quest|creature):(\d+)\]', replace_link, md)

def build_mappings():
    print("Building mappings...")
    # Gallery mappings
    gallery_dir = SOURCE_DIR / "gallery"
    for f in gallery_dir.glob("*.json"):
        with open(f, 'r', encoding='utf-8') as jf:
            data = json.load(jf)
            if 'id' in data:
                uuid = data['id']
                ext = data['ext']
                uuid_to_filename[uuid] = f"{uuid}.{ext}"
                uuid_to_orig_name[uuid] = data['name']

    # Entity mappings
    for etype, target in ENTITY_TYPES.items():
        edir = SOURCE_DIR / etype
        if not edir.exists(): continue
        for f in edir.glob("*.json"):
            with open(f, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
                # Kanka links in entries use the entity_id (entity.id in JSON)
                eid = data.get('entity', {}).get('id')
                name = data.get('name')
                # Some fields like memberships use the type-specific ID
                type_id = data.get('id')
                
                if name:
                    if eid: id_to_name[int(eid)] = name
                    if type_id: id_to_name[int(type_id)] = name
                    if eid: id_to_type[int(eid)] = etype

def process_entity_content(data, target_base_dir, is_post=False):
    title = data['name']
    entry = data.get('entry') or data.get('entity', {}).get('entry', '')
    created_at = data.get('created_at', '2024-01-01T00:00:00Z')
    date_str = created_at.split('T')[0]
    
    slug = slugify(title)
    if is_post:
        filename = f"{date_str}-{slug}.md"
    else:
        filename = f"{clean_filename(title)}.md"
    
    content = html_to_md(entry)
    content = resolve_links(content)
    
    # Move images in content
    def fix_img_path(match):
        placeholder = match.group(1)
        uuid = placeholder.replace('placeholder_', '')
        fname = uuid_to_filename.get(uuid)
        if fname:
            src = SOURCE_DIR / "gallery" / fname
            dest_dir = ASSETS_DIR / "_posts"
            dest_dir.mkdir(parents=True, exist_ok=True)
            if src.exists():
                shutil.copy2(src, dest_dir / fname)
            return f"![](/assets/_posts/{fname})"
        return match.group(0)

    content = re.sub(r'!\[.*?\]\(/assets/images/(placeholder_[^)]+)\)', fix_img_path, content)

    # Entity profile image
    image_header = ""
    img_uuid = data.get('entity', {}).get('image_uuid')
    if img_uuid:
        fname = uuid_to_filename.get(img_uuid)
        if fname:
            src = SOURCE_DIR / "gallery" / fname
            dest_dir = ASSETS_DIR / "images"
            dest_dir.mkdir(parents=True, exist_ok=True)
            if src.exists():
                shutil.copy2(src, dest_dir / fname)
            image_header = f"![{title}](/assets/images/{fname})\n\n"

    metadata_md = get_metadata_md(data)
    
    write_md_file(target_base_dir / filename, title, content, metadata_md, image_header)
    
    # Process nested posts
    nested_posts = data.get('entity', {}).get('posts', [])
    for p in nested_posts:
        p_created = p.get('created_at', created_at)
        p_date = p_created.split('T')[0]
        p_slug = slugify(p['name'])
        p_filename = f"{p_date}-{p_slug}.md"
        
        p_content = html_to_md(p.get('entry', ''))
        p_content = resolve_links(p_content)
        # Fix images in nested post too
        p_content = re.sub(r'!\[.*?\]\(/assets/images/(placeholder_[^)]+)\)', fix_img_path, p_content)
        
        write_md_file(POSTS_DIR / p_filename, p['name'], p_content)

def clean_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def migrate_journals():
    print("Migrating journals...")
    journal_dir = SOURCE_DIR / "journals"
    if not journal_dir.exists(): return
    
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    
    for f in journal_dir.glob("*.json"):
        with open(f, 'r', encoding='utf-8') as jf:
            data = json.load(jf)
            process_entity_content(data, POSTS_DIR, is_post=True)

def migrate_entities():
    print("Migrating other entities...")
    for etype, target in ENTITY_TYPES.items():
        if etype == "journals": continue
        
        edir = SOURCE_DIR / etype
        if not edir.exists(): continue
        
        target_subdir = WIKI_DIR / etype
        target_subdir.mkdir(parents=True, exist_ok=True)
        
        for f in edir.glob("*.json"):
            with open(f, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
                process_entity_content(data, target_subdir, is_post=False)

if __name__ == "__main__":
    print("Cleaning up wiki/ directory for re-organization...")
    if WIKI_DIR.exists():
        for f in WIKI_DIR.rglob("*.md"):
            if f.name != "example-page.md":
                f.unlink()
    
    # Clean up posts too, except examples
    if POSTS_DIR.exists():
        for f in POSTS_DIR.glob("*.md"):
            if "example-post" not in f.name:
                f.unlink()

    build_mappings()
    migrate_journals()
    migrate_entities()
    print("Migration complete!")

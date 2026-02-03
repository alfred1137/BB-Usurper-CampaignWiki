import os
import json
import re
import shutil
from pathlib import Path
from datetime import datetime

# Configuration
SOURCE_DIR = Path(r"d:\Git\BB-Usurper-CampaignWiki\.agent\kanka-bkup")
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
id_to_rel_path = {} # store relative path from root
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
            # Memberships will be resolved later in process_entity_content via resolve_links
            lines.append(f"* [[{oname}]]: {role}")

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

def resolve_links(md, current_file_path):
    def quote_path(path):
        return path.replace(' ', '%20')

    def replace_kanka_link(match):
        etype = match.group(1)
        eid = int(match.group(2))
        name = id_to_name.get(eid)
        target_rel_path = id_to_rel_path.get(eid)
        
        if name and target_rel_path:
            root = TARGET_DIR
            target_abs = root / target_rel_path
            current_dir = Path(current_file_path).parent
            
            try:
                rel_link = os.path.relpath(target_abs, current_dir).replace('\\', '/')
                return f"[{name}]({quote_path(rel_link)})"
            except ValueError:
                return f"[{name}]({{{{ site.baseurl }}}}/{quote_path(target_rel_path)})"
        
        return match.group(0)

    # First handle [type:id]
    md = re.sub(r'\[(character|location|journal|race|organisation|quest|creature):(\d+)\]', replace_kanka_link, md)
    
    # Also handle [[Name]] if we have a name-to-path mapping
    name_to_path = {name: path for eid, name in id_to_name.items() for path in [id_to_rel_path.get(eid)] if path}
    
    def replace_wiki_link(match):
        name = match.group(1)
        target_rel_path = name_to_path.get(name)
        if target_rel_path:
            root = TARGET_DIR
            target_abs = root / target_rel_path
            current_dir = Path(current_file_path).parent
            try:
                rel_link = os.path.relpath(target_abs, current_dir).replace('\\', '/')
                return f"[{name}]({quote_path(rel_link)})"
            except ValueError:
                return f"[{name}]({{{{ site.baseurl }}}}/{quote_path(target_rel_path)})"
        return match.group(0)

    md = re.sub(r'\[\[(.*?)\]\]', replace_wiki_link, md)
    
    return md

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

    # Pass 1: Name and Type
    for etype, target in ENTITY_TYPES.items():
        edir = SOURCE_DIR / etype
        if not edir.exists(): continue
        for f in edir.glob("*.json"):
            with open(f, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
                eid = data.get('entity', {}).get('id')
                name = data.get('name')
                type_id = data.get('id')
                if name:
                    if eid: id_to_name[int(eid)] = name; id_to_type[int(eid)] = etype
                    if type_id: id_to_name[int(type_id)] = name

    # Pass 2: Path
    for etype, target in ENTITY_TYPES.items():
        edir = SOURCE_DIR / etype
        if not edir.exists(): continue
        for f in edir.glob("*.json"):
            with open(f, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
                eid = data.get('entity', {}).get('id')
                type_id = data.get('id')
                name = data.get('name')
                if etype == "journals":
                    created_at = data.get('created_at', '2024-01-01T00:00:00Z')
                    date_str = created_at.split('T')[0]
                    slug = slugify(name)
                    rel_path = f"_posts/{date_str}-{slug}.md"
                else:
                    rel_path = f"wiki/{etype}/{clean_filename(name)}.md"
                if eid: id_to_rel_path[int(eid)] = rel_path
                if type_id: id_to_rel_path[int(type_id)] = rel_path

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
    
    target_full_path = target_base_dir / filename
    content = html_to_md(entry)
    content = resolve_links(content, target_full_path)
    
    def fix_img_path(match):
        placeholder = match.group(1)
        uuid = placeholder.replace('placeholder_', '')
        fname = uuid_to_filename.get(uuid)
        if fname:
            src = SOURCE_DIR / "gallery" / fname
            dest_dir = ASSETS_DIR / "_posts"
            dest_dir.mkdir(parents=True, exist_ok=True)
            if src.exists(): shutil.copy2(src, dest_dir / fname)
            return f"![]({{{{ site.baseurl }}}}/assets/_posts/{fname})"
        return match.group(0)

    content = re.sub(r'!\[.*?\]\(/assets/images/(placeholder_[^)]+)\)', fix_img_path, content)

    image_header = ""
    img_uuid = data.get('entity', {}).get('image_uuid')
    if img_uuid:
        fname = uuid_to_filename.get(img_uuid)
        if fname:
            src = SOURCE_DIR / "gallery" / fname
            dest_dir = ASSETS_DIR / "images"
            dest_dir.mkdir(parents=True, exist_ok=True)
            if src.exists(): shutil.copy2(src, dest_dir / fname)
            image_header = f"![{title}]({{{{ site.baseurl }}}}/assets/images/{fname})\n\n"

    metadata_md = get_metadata_md(data)
    metadata_md = resolve_links(metadata_md, target_full_path)
    write_md_file(target_full_path, title, content, metadata_md, image_header)
    
    nested_posts = data.get('entity', {}).get('posts', [])
    for p in nested_posts:
        p_created = p.get('created_at', created_at)
        p_date = p_created.split('T')[0]; p_slug = slugify(p['name'])
        p_full_path = POSTS_DIR / f"{p_date}-{p_slug}.md"
        p_content = resolve_links(html_to_md(p.get('entry', '')), p_full_path)
        p_content = re.sub(r'!\[.*?\]\(/assets/images/(placeholder_[^)]+)\)', fix_img_path, p_content)
        write_md_file(p_full_path, p['name'], p_content)

def clean_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def migrate_journals():
    print("Migrating journals...")
    journal_dir = SOURCE_DIR / "journals"
    if not journal_dir.exists(): return
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    for f in journal_dir.glob("*.json"):
        with open(f, 'r', encoding='utf-8') as jf:
            process_entity_content(json.load(jf), POSTS_DIR, is_post=True)

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
                process_entity_content(json.load(jf), target_subdir, is_post=False)

if __name__ == "__main__":
    if WIKI_DIR.exists():
        for f in WIKI_DIR.rglob("*.md"):
            if f.name != "example-page.md": f.unlink()
    if POSTS_DIR.exists():
        for f in POSTS_DIR.glob("*.md"):
            if "example-post" not in f.name: f.unlink()
    build_mappings()
    migrate_journals()
    migrate_entities()
    print("Migration complete!")

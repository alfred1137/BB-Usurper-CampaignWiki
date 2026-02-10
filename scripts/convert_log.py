import re
import html
import sys
import os
from pathlib import Path

def clean_html(text):
    # Basic HTML to Markdown conversion
    text = re.sub(r'<(?:br|p)>', '\n', text)
    text = re.sub(r'</b>|</strong>', '**', text)
    text = re.sub(r'<b>|<strong>', '**', text)
    text = re.sub(r'</i>|</em>', '*', text)
    text = re.sub(r'<i>|<em>', '*', text)
    text = re.sub(r'<[^>]+>', '', text)
    return html.unescape(text).strip()

def process(filepath, output_path):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Find all messages in order
    matches = re.finditer(r'class=\"(query-text|model-response-text)[^>]*>(.*?)</div>', content, re.DOTALL)
    
    output = []
    # Derive title from filename
    filename = Path(filepath).stem.replace('-', ' ').title()
    output.append(f"# {filename}\n")
    
    for match in matches:
        role_class = match.group(1)
        text = match.group(2)
        
        if role_class == 'query-text':
            output.append("## User")
        else:
            output.append("## Gemini")
            
        output.append(clean_html(text))
        output.append("\n---\n")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(output))
    
    print(f"Successfully converted messages to {output_path}")

def get_latest_log():
    log_dir = Path('.html-log')
    if not log_dir.exists():
        return None
    
    logs = list(log_dir.glob('*-log.html'))
    if not logs:
        return None
        
    # Sort by modification time to get the latest
    return max(logs, key=os.path.getmtime)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        process(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        input_path = sys.argv[1]
        output_path = str(Path(input_path).with_suffix('.md'))
        process(input_path, output_path)
    else:
        latest = get_latest_log()
        if latest:
            output_path = str(latest.with_suffix('.md'))
            print(f"No arguments provided. Processing latest log: {latest}")
            process(str(latest), output_path)
        else:
            print("Usage: python scripts/convert_log.py [input_html] [output_md]")
            print("No log files found in .html-log/")



import re
import html
import sys

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
    filename = filepath.split('\\')[-1].split('/')[-1].replace('.html', '').replace('-', ' ').title()
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

if __name__ == '__main__':
    if len(sys.argv) > 2:
        process(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        input_path = sys.argv[1]
        output_path = input_path.rsplit('.', 1)[0] + '.md'
        process(input_path, output_path)
    else:
        # Fallback to defaults if no args provided (optional, keeps old behavior if desired)
        default_input = r'\\tangshome\home\Drive\99 Shared\Games\Battle Brothers\RotU+PoV-Campaign\Story\Log\session-2-log.html'
        default_output = default_input.replace('.html', '.md')
        process(default_input, default_output)


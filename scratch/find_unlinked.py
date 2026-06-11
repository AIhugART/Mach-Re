import os
import re
import sys

# Reconfigure stdout to use utf-8 to avoid UnicodeEncodeError on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "C:/Stable_Diffusion/MACH_RE"
html_files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]

print("Scanning for unlinked inline citations [N] in HTML files...")

for filename in html_files:
    filepath = os.path.join(workspace_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for line_num, line in enumerate(lines, 1):
        matches = re.finditer(r'\[(\d+)\]', line)
        for m in matches:
            num = m.group(1)
            # Check if this [N] is linked
            # E.g. <a href="#nguon-N">[N]</a>
            is_linked = f'href="#nguon-{num}"' in line or f"href='#nguon-{num}'" in line or f'id="nguon-{num}"' in line
            is_in_table = "nguon-" in line or "Nguồn Trích Dẫn" in line or "Nguon Trich Dan" in line
            
            # Additional check: verify if the bracket itself is inside an anchor tag
            # by checking if `<a` is before it and `</a>` is after it in the line.
            # E.g. <a ...>[N]</a>
            is_hyperlinked = False
            for link_match in re.finditer(r'<a\s+[^>]*href=["\']#nguon-' + num + r'["\'][^>]*>(\[' + num + r'\]|' + num + r')</a>', line):
                is_hyperlinked = True
                
            if not is_linked and not is_in_table and not is_hyperlinked:
                print(f"File: {filename} | Line: {line_num} | Bracket: [{num}] | Line Content: {line.strip()}")

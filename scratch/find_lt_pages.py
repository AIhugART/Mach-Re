import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def find_lt_pages(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    page_header_pat = re.compile(r'^##\s+TRANG\s+(\d+)', re.IGNORECASE)
    
    # Collect all headers
    headers = []
    for idx, line in enumerate(lines):
        line_num = idx + 1
        m = page_header_pat.match(line.strip())
        if m:
            headers.append((line_num, int(m.group(1))))
            
    def get_current_header(line_num):
        for i, h in enumerate(headers):
            if i + 1 < len(headers):
                if h[0] < line_num < headers[i+1][0]:
                    return h[1]
            else:
                if line_num > h[0]:
                    return h[1]
        return None

    matches = []
    for idx, line in enumerate(lines):
        line_num = idx + 1
        line_str = line.strip()
        if line_str.startswith('<'):
            header = get_current_header(line_num)
            matches.append((line_num, header, line_str[:60]))
            
    print(f"Stray '<' lines and their pages:")
    for lm, h_num, snippet in matches:
        print(f"  - Page {h_num} (Line {lm}): '{snippet}...'")
        
    page_list = sorted(list(set(h_num for _, h_num, _ in matches)))
    print(f"\nUnique pages containing stray '<': {page_list}")

if __name__ == '__main__':
    find_lt_pages('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

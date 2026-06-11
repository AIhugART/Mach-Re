import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def analyze_offsets(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    page_header_pat = re.compile(r'^##\s+TRANG\s+(\d+)', re.IGNORECASE)
    digit_line_pat = re.compile(r'^\s*(\d+)\s*$')
    inline_pat = re.compile(r'^(.*?)\s+(\d+)$')
    
    # 1. Collect all headers and their line positions
    headers = []
    for idx, line in enumerate(lines):
        line_num = idx + 1
        m = page_header_pat.match(line.strip())
        if m:
            headers.append((line_num, int(m.group(1))))
            
    # Helper to find which header number a line falls under
    def get_current_header(line_num):
        for i, h in enumerate(headers):
            # If line is before the next header, it belongs to the current header
            if i + 1 < len(headers):
                if h[0] < line_num < headers[i+1][0]:
                    return h[1]
            else:
                if line_num > h[0]:
                    return h[1]
        return None

    # 2. Collect all printed page numbers (both standalone and inline)
    page_leaks = {} # header_num -> list of (line_num, val, is_standalone)
    
    for idx, line in enumerate(lines):
        line_num = idx + 1
        line_str = line.strip()
        
        # Standalone check
        m_stand = digit_line_pat.match(line_str)
        if m_stand:
            val = int(m_stand.group(1))
            if 1 <= val <= 600:
                header = get_current_header(line_num)
                if header:
                    if header not in page_leaks:
                        page_leaks[header] = []
                    page_leaks[header].append((line_num, val, True))
                    continue
                    
        # Inline check (exclude headers, and TOC lines at the end)
        if not line_str.startswith('#') and line_num < 7650:
            m_inline = inline_pat.match(line.rstrip('\r\n'))
            if m_inline:
                val = int(m_inline.group(2))
                if 1 <= val <= 600:
                    header = get_current_header(line_num)
                    if header:
                        # Exclude cases where it's part of the text (like "có 47" at line 5222, which has header 382)
                        # We can check the offset. If offset makes sense compared to neighbors, or is typical (like 2, 3, 10, 11),
                        # it's likely a page leak.
                        if header not in page_leaks:
                            page_leaks[header] = []
                        page_leaks[header].append((line_num, val, False))

    print("Header No. | Printed Page No. | Line No. | Standalone? | Offset")
    print("-" * 65)
    for header in sorted(page_leaks.keys()):
        for line_num, val, is_standalone in page_leaks[header]:
            offset = header - val
            print(f"TRANG {header:<4} | Page {val:<12} | Line {line_num:<8} | {'Yes' if is_standalone else 'No':<11} | {offset}")

if __name__ == '__main__':
    analyze_offsets('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

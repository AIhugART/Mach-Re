import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def map_page_offsets(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    page_header_pat = re.compile(r'^##\s+TRANG\s+(\d+)', re.IGNORECASE)
    digit_line_pat = re.compile(r'^\s*(\d+)\s*$')
    
    # Track page headers and their line indices
    headers = [] # list of (line_num, page_num)
    for idx, line in enumerate(lines):
        line_num = idx + 1
        m = page_header_pat.match(line.strip())
        if m:
            headers.append((line_num, int(m.group(1))))
            
    # Function to get the page header active at a given line number
    def get_current_header_info(line_num):
        # Find the last header that appears before or at this line number
        active_header = None
        next_header = None
        for i, h in enumerate(headers):
            if h[0] < line_num:
                active_header = h
                if i + 1 < len(headers):
                    next_header = headers[i+1]
            else:
                break
        return active_header, next_header

    # Let's check the standalone digit lines (which are verified to be footers)
    offsets = []
    print("Mapping standalone page number footers:")
    for idx, line in enumerate(lines):
        line_num = idx + 1
        m = digit_line_pat.match(line)
        if m:
            val = int(m.group(1))
            if 1 <= val <= 600:
                active, next_h = get_current_header_info(line_num)
                if active:
                    # Usually, the printed page number is at the bottom of the page,
                    # so the header active for this line is the one the number belongs to.
                    offset = active[1] - val
                    offsets.append((line_num, active[1], val, offset))
                    
    # Print the first few and last few mappings, and group by offset
    offset_groups = {}
    for lm, h_num, p_num, off in offsets:
        if off not in offset_groups:
            offset_groups[off] = []
        offset_groups[off].append((lm, h_num, p_num))
        
    print(f"Total mapped footers: {len(offsets)}")
    for off, items in sorted(offset_groups.items()):
        print(f"Offset {off}: {len(items)} pages (e.g. TRANG {items[0][1]} has printed page {items[0][2]} at line {items[0][0]})")

if __name__ == '__main__':
    map_page_offsets('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

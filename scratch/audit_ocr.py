import re
import sys
import os

def audit_ocr(file_path):
    print(f"Auditing file: {file_path}")
    if not os.path.exists(file_path):
        print("File not found!")
        return

    # Regular expression to match page headers
    # Standard format seems to be "## TRANG <number>"
    page_regex = re.compile(r'^##\s+TRANG\s+(\d+)', re.IGNORECASE)
    
    pages = []
    # Read the file line by line
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    print(f"Total lines: {len(lines)}")
    
    current_page = None
    page_content_start_line = 0
    page_data = {} # page_num -> list of dicts with {line_num, content_len, lines_count}
    
    for idx, line in enumerate(lines):
        line_num = idx + 1
        match = page_regex.match(line.strip())
        if match:
            # We found a new page header
            page_num = int(match.group(1))
            if current_page is not None:
                # Store content length of the previous page
                content = "".join(lines[page_content_start_line:idx]).strip()
                page_data[current_page][-1]['content_len'] = len(content)
                page_data[current_page][-1]['lines_count'] = idx - page_content_start_line
                page_data[current_page][-1]['end_line'] = idx
                
            current_page = page_num
            page_content_start_line = idx + 1
            
            if page_num not in page_data:
                page_data[page_num] = []
            page_data[page_num].append({
                'start_line': line_num,
                'content_len': 0,
                'lines_count': 0,
                'end_line': 0
            })
            pages.append((page_num, line_num))
            
    # Don't forget the last page
    if current_page is not None:
        content = "".join(lines[page_content_start_line:]).strip()
        page_data[current_page][-1]['content_len'] = len(content)
        page_data[current_page][-1]['lines_count'] = len(lines) - page_content_start_line
        page_data[current_page][-1]['end_line'] = len(lines)

    # 1. Check duplicate page markers
    duplicates = {}
    for p_num, occurrences in page_data.items():
        if len(occurrences) > 1:
            duplicates[p_num] = occurrences
            
    # 2. Check missing page markers between 1 and 585
    expected_pages = set(range(1, 586))
    actual_pages = set(page_data.keys())
    missing_pages = sorted(list(expected_pages - actual_pages))
    
    # 3. Check for out of order pages
    out_of_order = []
    prev_page = 0
    for p_num, line_num in pages:
        if p_num < prev_page:
            out_of_order.append((p_num, line_num, f"Page {p_num} at line {line_num} appeared after page {prev_page}"))
        prev_page = p_num

    # 4. Check for abnormally short pages (excluding pages that might naturally be short, like table of contents, introduction if short, but we'll flag any page with < 300 characters as a warning)
    short_pages = []
    for p_num, occurrences in page_data.items():
        for idx, occ in enumerate(occurrences):
            # If the page has less than 250 characters, flag it. (excluding front matter pages if we want, but let's list them first)
            if occ['content_len'] < 250:
                short_pages.append((p_num, occ['start_line'], occ['content_len'], occ['end_line']))

    # Print summary
    print("\n--- AUDIT SUMMARY ---")
    print(f"Total unique page markers found: {len(actual_pages)}")
    print(f"Total page markers instances (including duplicates): {len(pages)}")
    
    print(f"\n--- DUPLICATE PAGES ({len(duplicates)}) ---")
    for p_num, occurrences in sorted(duplicates.items()):
        print(f"Page {p_num} appears {len(occurrences)} times:")
        for o in occurrences:
            print(f"  - Lines {o['start_line']}-{o['end_line']} (Length: {o['content_len']} chars, {o['lines_count']} lines)")
            
    print(f"\n--- MISSING PAGES ({len(missing_pages)}) ---")
    print(missing_pages)
    
    print(f"\n--- OUT OF ORDER PAGES ({len(out_of_order)}) ---")
    for p_num, line_num, msg in out_of_order:
        print(f"  - Line {line_num}: Page {p_num} ({msg})")
        
    print(f"\n--- ABNORMALLY SHORT PAGES (Length < 250 chars) ({len(short_pages)}) ---")
    for p_num, start_line, length, end_line in sorted(short_pages, key=lambda x: x[0]):
        print(f"  - Page {p_num} (Lines {start_line}-{end_line}): {length} chars")

if __name__ == '__main__':
    file_path = './documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md'
    audit_ocr(file_path)

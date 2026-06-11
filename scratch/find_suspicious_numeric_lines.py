import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def find_suspicious_lines(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    digit_line_pat = re.compile(r'^\s*(\d+)\s*$')
    
    suspicious = []
    normal_page_numbers = []
    
    for idx, line in enumerate(lines):
        line_num = idx + 1
        m = digit_line_pat.match(line)
        if m:
            val = m.group(1)
            val_int = int(val)
            if 1 <= val_int <= 600:
                # Check surrounding context
                prev_line_1 = lines[idx-1].strip() if idx > 0 else ""
                prev_line_2 = lines[idx-2].strip() if idx > 1 else ""
                next_line_1 = lines[idx+1].strip() if idx < len(lines)-1 else ""
                next_line_2 = lines[idx+2].strip() if idx < len(lines)-2 else ""
                
                # Check if it looks like a typical footer (near page breaks or empty lines)
                is_footer = False
                
                # If it's adjacent to a page break "---" or "## TRANG", or if there is an empty line on either side
                if (prev_line_1 == "" or prev_line_1 == "---" or prev_line_1.startswith("## TRANG") or
                    next_line_1 == "" or next_line_1 == "---" or next_line_1.startswith("## TRANG")):
                    is_footer = True
                
                if is_footer:
                    normal_page_numbers.append((line_num, val_int, line.strip(), prev_line_1, next_line_1))
                else:
                    suspicious.append((line_num, val_int, line.strip(), prev_line_1, next_line_1))
                    
    print(f"Total digit-only lines: {len(normal_page_numbers) + len(suspicious)}")
    print(f"Normal page-number footers: {len(normal_page_numbers)}")
    print(f"Suspicious/Embedded digit-only lines: {len(suspicious)}")
    for lm, val, content, prev, next_ in suspicious:
        print(f"  - Line {lm}: '{content}' (value: {val})")
        print(f"    Before: '{prev}'")
        print(f"    After:  '{next_}'")

if __name__ == '__main__':
    find_suspicious_lines('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

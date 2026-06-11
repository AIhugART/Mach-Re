import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def find_inline_numeric_leaks(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    inline_pat = re.compile(r'^(.*?)\s+(\d+)$')
    
    matches = []
    # The table of contents is typically at the end of the book.
    # Let's inspect where it starts. Let's check lines up to line 7650 to ignore the actual TOC.
    for idx, line in enumerate(lines):
        line_num = idx + 1
        line_str = line.rstrip('\r\n')
        m = inline_pat.match(line_str)
        if m:
            prefix = m.group(1)
            val = m.group(2)
            val_int = int(val)
            if 1 <= val_int <= 600:
                # Ignore headers, and ignore lines containing "Chương" followed by numbers (like Table of Contents)
                if prefix.strip().startswith('#') or "Mục lục" in line_str or line_num > 7650:
                    continue
                # Also ignore lines that contain a colon before the number like "Chương I: 12" just in case
                if prefix.strip().endswith(':'):
                    continue
                matches.append((line_num, val_int, line_str, prefix))
                
    out_file = 'scratch/all_inline_numeric_leaks.txt'
    with open(out_file, 'w', encoding='utf-8') as out_f:
        out_f.write(f"Total lines in source: {len(lines)}\n")
        out_f.write(f"Found {len(matches)} lines ending with an inline page number:\n\n")
        for lm, val, line_str, prefix in matches:
            out_f.write(f"--- Line {lm} (Value: {val}) ---\n")
            out_f.write(f"Line:   '{line_str}'\n")
            out_f.write(f"Prefix: '{prefix}'\n\n")
            
    print(f"Audit completed. Results written to {out_file}")

if __name__ == '__main__':
    find_inline_numeric_leaks('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

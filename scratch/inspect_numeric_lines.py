import re
import sys

# Ensure UTF-8 output on Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def find_numeric_lines(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    print(f"Total lines: {len(lines)}")
    
    # Pattern to match a line that consists solely of a number, possibly with spaces
    digit_line_pat = re.compile(r'^\s*(\d+)\s*$')
    
    matches = []
    for idx, line in enumerate(lines):
        line_num = idx + 1
        m = digit_line_pat.match(line)
        if m:
            val = m.group(1)
            val_int = int(val)
            if 1 <= val_int <= 600:
                # Get context
                prev_lines = [lines[i].strip() for i in range(max(0, idx-2), idx)]
                next_lines = [lines[i].strip() for i in range(idx+1, min(len(lines), idx+3))]
                matches.append((line_num, val_int, line.strip(), prev_lines, next_lines))
                
    out_file = 'scratch/all_numeric_lines.txt'
    with open(out_file, 'w', encoding='utf-8') as out_f:
        out_f.write(f"Total lines in source: {len(lines)}\n")
        out_f.write(f"Found {len(matches)} lines containing only a printed page number:\n\n")
        for lm, val, content, prev_l, next_l in matches:
            out_f.write(f"--- Line {lm} (Value: {val}) ---\n")
            out_f.write(f"Before: {prev_l}\n")
            out_f.write(f"Line:   '{content}'\n")
            out_f.write(f"After:  {next_l}\n\n")
            
    print(f"Audit completed. Results written to {out_file}")

if __name__ == '__main__':
    find_numeric_lines('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

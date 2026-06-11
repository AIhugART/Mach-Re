import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def find_dash_leaks(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    # Pattern to match a line that starts with one or more dashes and ends with digits, possibly with spaces
    pat = re.compile(r'^\s*-+\s*\d+\s*$')
    
    matches = []
    for idx, line in enumerate(lines):
        line_num = idx + 1
        line_str = line.strip()
        if pat.match(line_str):
            prev_lines = [lines[i].strip() for i in range(max(0, idx-2), idx)]
            next_lines = [lines[i].strip() for i in range(idx+1, min(len(lines), idx+3))]
            matches.append((line_num, line_str, prev_lines, next_lines))
            
    print(f"Found {len(matches)} lines matching dash-numeric pattern:")
    for lm, line_str, prev, next_ in matches:
        print(f"--- Line {lm} ---")
        print(f"Before: {prev}")
        print(f"Line:   '{line_str}'")
        print(f"After:  {next_}")

if __name__ == '__main__':
    find_dash_leaks('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

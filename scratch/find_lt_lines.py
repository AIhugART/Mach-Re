import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def find_lt_lines(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    matches = []
    for idx, line in enumerate(lines):
        line_num = idx + 1
        line_str = line.strip()
        if line_str.startswith('<'):
            matches.append((line_num, line.rstrip('\r\n')))
            
    print(f"Found {len(matches)} lines starting with '<':")
    for lm, content in matches:
        print(f"Line {lm}: '{content}'")

if __name__ == '__main__':
    find_lt_lines('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def search_pattern(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines):
        if 'downloaded' in line.lower() or 'pdf' in line.lower():
            # Exclude lines that are part of normal content (like referring to pdf files in a standard way, if any)
            print(f"Line {idx+1}: {line.strip()}")

if __name__ == '__main__':
    search_pattern('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

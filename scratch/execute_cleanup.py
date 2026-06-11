import re
import sys
import shutil
import os

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def execute_cleanup(file_path):
    # Make a backup
    backup_path = file_path + '.bak2'
    shutil.copy2(file_path, backup_path)
    print(f"Backup created at: {backup_path}")
    
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    page_header_pat = re.compile(r'^##\s+TRANG\s+(\d+)', re.IGNORECASE)
    digit_line_pat = re.compile(r'^\s*(\d+)\s*$')
    inline_pat = re.compile(r'^(.*?)\s+(\d+)$')
    
    # 1. Collect all page headers and their positions
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

    # 2. Process lines
    new_lines = []
    changes_count = 0
    
    for idx, line in enumerate(lines):
        line_num = idx + 1
        line_str = line.rstrip('\r\n')
        line_stripped = line_str.strip()
        
        # 2a. Standalone digit-only footers
        m_stand = digit_line_pat.match(line_stripped)
        if m_stand:
            val = int(m_stand.group(1))
            if 1 <= val <= 600:
                changes_count += 1
                # We do not append anything to new_lines (remove line)
                continue
                
        # 2b. Standalone punctuation-digit footer (line 411: "30)")
        if line_stripped == '30)' and line_num == 411:
            changes_count += 1
            continue

        # 2c. Watermark line (line 2926)
        if 'downloaded 71862.pdf at Sun Jul 08' in line_str and line_num == 2926:
            changes_count += 1
            continue

        # 2d. Watermark suffix line (line 2952)
        if 'downloaded 71862.pdf at Sun Jul 08' in line_str and line_num == 2952:
            new_line = line_str.replace(' 2012 downloaded 71862.pdf at Sun Jul 08 00:17:07 ICT 235', '')
            changes_count += 1
            new_lines.append(new_line + '\n')
            continue
            
        # 2e. Inline page leaks
        if not line_stripped.startswith('#') and line_num < 7650:
            m_inline = inline_pat.match(line_str)
            if m_inline:
                prefix = m_inline.group(1)
                val = int(m_inline.group(2))
                
                header = get_current_header(line_num)
                if header:
                    is_leak = False
                    if header - 2 == val:
                        is_leak = True
                    elif header - 24 == val:
                        is_leak = True
                    elif header == 31 and val == 20: # Special OCR error
                        is_leak = True
                        
                    if is_leak:
                        changes_count += 1
                        new_lines.append(prefix + '\n')
                        continue
                        
        new_lines.append(line)
        
    # Write the cleaned lines back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print(f"Cleanup executed successfully. Total edits made: {changes_count}")
    print(f"New line count: {len(new_lines)} (original: {len(lines)})")

if __name__ == '__main__':
    execute_cleanup('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

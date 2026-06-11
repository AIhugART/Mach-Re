import re
import sys
import shutil

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def clean_stray_lt(file_path):
    # Create backup first
    backup_path = file_path + '.bak3'
    shutil.copy2(file_path, backup_path)
    print(f"Backup created at: {backup_path}")
    
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    new_lines = []
    changes = []
    
    # Pattern to match lines starting with '<th' or '<than' or '<the'
    # We want to be safe and only strip if it is a leading '<' followed by alphabetic characters starting with 't' or 'th'
    pat = re.compile(r'^<([tT][hH]?\w+)')
    
    for idx, line in enumerate(lines):
        line_num = idx + 1
        m = pat.match(line)
        if m:
            word = m.group(1)
            # Replace the leading '<' with nothing
            new_line = line[1:]
            changes.append((line_num, line.rstrip('\r\n'), new_line.rstrip('\r\n')))
            new_lines.append(new_line)
        else:
            new_lines.append(line)
            
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print(f"Cleanup of stray '<' completed. Total edits: {len(changes)}")
    for lm, orig, new_str in changes:
        print(f"Line {lm}:")
        print(f"  Orig: '{orig[:100]}...'")
        print(f"  New:  '{new_str[:100]}...'")
        print()

if __name__ == '__main__':
    clean_stray_lt('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

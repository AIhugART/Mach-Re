import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def dry_run_cleanup(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    page_header_pat = re.compile(r'^##\s+TRANG\s+(\d+)', re.IGNORECASE)
    digit_line_pat = re.compile(r'^\s*(\d+)\s*$')
    inline_pat = re.compile(r'^(.*?)\s+(\d+)$')
    
    # 1. First pass: Collect all page headers and their positions
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

    # 2. Second pass: Process lines
    new_lines = []
    changes = []
    
    for idx, line in enumerate(lines):
        line_num = idx + 1
        line_str = line.rstrip('\r\n')
        line_stripped = line_str.strip()
        
        # 2a. Standalone digit-only footers
        m_stand = digit_line_pat.match(line_stripped)
        if m_stand:
            val = int(m_stand.group(1))
            if 1 <= val <= 600:
                changes.append({
                    'line_num': line_num,
                    'type': 'remove_standalone',
                    'original': line_str,
                    'new': None,
                    'reason': f'Standalone page footer value {val}'
                })
                continue
                
        # 2b. Standalone punctuation-digit footer (line 411: "30)")
        if line_stripped == '30)' and line_num == 411:
            changes.append({
                'line_num': line_num,
                'type': 'remove_standalone_punct',
                'original': line_str,
                'new': None,
                'reason': 'Standalone page footer 30)'
            })
            continue

        # 2c. Watermark line (line 2926)
        if 'downloaded 71862.pdf at Sun Jul 08' in line_str and line_num == 2926:
            changes.append({
                'line_num': line_num,
                'type': 'remove_watermark_line',
                'original': line_str,
                'new': None,
                'reason': 'Watermark stamp line'
            })
            continue

        # 2d. Watermark suffix line (line 2952)
        if 'downloaded 71862.pdf at Sun Jul 08' in line_str and line_num == 2952:
            new_line = line_str.replace(' 2012 downloaded 71862.pdf at Sun Jul 08 00:17:07 ICT 235', '')
            changes.append({
                'line_num': line_num,
                'type': 'clean_watermark_suffix',
                'original': line_str,
                'new': new_line,
                'reason': 'Watermark stamp suffix'
            })
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
                    # Expected printed page numbers:
                    # - Introduction: header_num - 24
                    # - Main body: header_num - 2
                    # - Special OCR error: TRANG 31, read as 20 instead of 29
                    is_leak = False
                    if header - 2 == val:
                        is_leak = True
                    elif header - 24 == val:
                        is_leak = True
                    elif header == 31 and val == 20: # Special OCR error
                        is_leak = True
                        
                    if is_leak:
                        changes.append({
                            'line_num': line_num,
                            'type': 'clean_inline_leak',
                            'original': line_str,
                            'new': prefix,
                            'reason': f'Inline page leak {val} under TRANG {header}'
                        })
                        new_lines.append(prefix + '\n')
                        continue
                        
        new_lines.append(line)
        
    print(f"Dry-run report: {len(changes)} changes identified.")
    for c in changes:
        print(f"Line {c['line_num']} ({c['type']}):")
        print(f"  Orig: '{c['original']}'")
        if c['new'] is not None:
            print(f"  New:  '{c['new']}'")
        print(f"  Why:  {c['reason']}")
        print()

if __name__ == '__main__':
    dry_run_cleanup('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

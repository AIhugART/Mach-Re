import re
import os
import sys

def find_loops(text, threshold=20):
    """Finds if a sequence of words of length >= threshold repeats in the text."""
    words = re.findall(r'\w+', text.lower())
    n = len(words)
    for length in range(threshold, min(50, n // 2)):
        for i in range(n - 2 * length):
            seq = words[i:i+length]
            for j in range(i + length, n - length):
                if words[j:j+length] == seq:
                    return f"Repeated sequence of {length} words starting at word {i} and {j}: {' '.join(seq)}"
    return None

def analyze_document(file_path, report_path):
    if not os.path.exists(file_path):
        print("File not found.")
        return
        
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
        
    # Split content by page headers
    page_markers = list(re.finditer(r'^##\s+TRANG\s+(\d+)', content, re.MULTILINE | re.IGNORECASE))
    
    pages = []
    for i in range(len(page_markers)):
        start_idx = page_markers[i].end()
        end_idx = page_markers[i+1].start() if i + 1 < len(page_markers) else len(content)
        
        page_num = int(page_markers[i].group(1))
        page_text = content[start_idx:end_idx].strip()
        # Remove trailing separator '---' if it exists at the end of the page
        if page_text.endswith('---'):
            page_text = page_text[:-3].strip()
            
        pages.append({
            'page_num': page_num,
            'start_line': content.count('\n', 0, page_markers[i].start()) + 1,
            'text': page_text,
            'length': len(page_text),
            'words': len(page_text.split())
        })
        
    # Run audit rules
    damaged_pages = []
    
    # Track page sequences
    seen_pages = {}
    
    for idx, p in enumerate(pages):
        p_num = p['page_num']
        p_len = p['length']
        p_words = p['words']
        p_text = p['text']
        
        issues = []
        
        # Rule 1: Duplicate Page Header
        if p_num in seen_pages:
            issues.append(f"Duplicate page marker. Previous occurrence at line {seen_pages[p_num]['start_line']}")
        else:
            seen_pages[p_num] = p
            
        # Rule 2: Exceptionally Short Content (excluding colophon at the end and front matter)
        is_front_back_matter = p_num <= 5 or p_num >= 581
        if p_len < 250 and not is_front_back_matter:
            issues.append(f"Abnormally short content: {p_len} characters ({p_words} words)")
            
        # Rule 3: Exceptionally Long Content (possible page merging)
        if p_len > 2200:
            issues.append(f"Abnormally long content: {p_len} characters ({p_words} words)")
            
        # Rule 4: Text loop detection
        loop = find_loops(p_text)
        if loop:
            issues.append(f"Loop detected: {loop}")
            
        # Rule 5: Specific known bad signs
        dangling_words = ['thì', 'lí', 'và', 'của', 'là', 'nhưng', 'để', 'trong', 'với', 'cho', 'một', 'các']
        last_word = p_text.split()[-1].lower() if p_text.split() else ''
        last_word_clean = re.sub(r'[^\w\s]', '', last_word)
        if last_word_clean in dangling_words and not is_front_back_matter and p_len < 600:
            issues.append(f"Ends with dangling word: '{last_word}' (likely truncated)")
            
        if issues:
            damaged_pages.append({
                'page_num': p_num,
                'start_line': p['start_line'],
                'length': p_len,
                'words': p_words,
                'issues': issues,
                'snippet': p_text[:200].replace('\n', ' ') + "..."
            })
            
    # Write report to file in UTF-8
    with open(report_path, 'w', encoding='utf-8') as rf:
        rf.write(f"# OCR QUALITY AUDIT REPORT\n\n")
        rf.write(f"Total potential page issues found: **{len(damaged_pages)}**\n\n")
        rf.write(f"| Page | Start Line | Length (chars) | Issues | Snippet |\n")
        rf.write(f"|---|---|---|---|---|\n")
        for dp in damaged_pages:
            issues_str = "; ".join(dp['issues'])
            # Clean snippet for markdown display
            snippet_clean = dp['snippet'].replace('|', '\\|')
            rf.write(f"| {dp['page_num']} | {dp['start_line']} | {dp['length']} | {issues_str} | {snippet_clean} |\n")
            
    print(f"Audit completed. Report written to {report_path}")

if __name__ == '__main__':
    analyze_document('./documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md', './scratch/comprehensive_ocr_audit_results.md')

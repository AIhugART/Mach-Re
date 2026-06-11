import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def find_inline_numeric_leaks(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    # Pattern to match lines that end with a space followed by a 1-3 digit number (not part of list numbers, or specific headers)
    # We want to be careful: e.g. "thế kỷ XIX" or "(1)" are normal.
    # A line like "các bà lễ chùa, các 388" ends with a space and "388"
    # Let's match a line that ends with: space, then a number of 1-3 digits.
    # We exclude lines that look like:
    # - "chương 1", "chương I", "chương 2"
    # - list items starting with numbers
    # - lines ending with years like "1930", "1945", etc. (values >= 1000)
    # - lines ending with common citations like "(1)", "(2)", etc. (though these are captured if they don't have parentheses)
    # Let's match any line ending with \s+\d+ where the number is between 1 and 600.
    inline_pat = re.compile(r'^(.*?)\s+(\d+)$')
    
    matches = []
    for idx, line in enumerate(lines):
        line_num = idx + 1
        line_str = line.rstrip('\r\n')
        m = inline_pat.match(line_str)
        if m:
            prefix = m.group(1)
            val = m.group(2)
            val_int = int(val)
            if 1 <= val_int <= 600:
                # Let's check if the prefix ends with punctuation or is a header
                if prefix.strip().startswith('#'):
                    continue
                # If prefix ends with a word, and the number is 1-600, it's likely a page leak
                # Let's show it so we can audit
                matches.append((line_num, val_int, line_str, prefix))
                
    print(f"Found {len(matches)} lines ending with an inline page number:")
    for lm, val, line_str, prefix in matches:
        print(f"  - Line {lm}: '{line_str}' -> Prefix: '{prefix}' | Page: {val}")

if __name__ == '__main__':
    find_inline_numeric_leaks('documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md')

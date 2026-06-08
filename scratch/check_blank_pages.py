import re

def check_blanks():
    with open(r"C:\Stable_Diffusion\MACH_RE\documents\public_documents\ban_sac.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find all page blocks: ## TRANG (\d+)\n(.*?)\n---
    # We use re.DOTALL to match newlines in the content
    pattern = re.compile(r"## TRANG (\d+)\n(.*?)(?=\n---|\Z)", re.DOTALL)
    matches = pattern.findall(content)
    
    print(f"Total pages found in file: {len(matches)}")
    
    blank_pages = []
    filled_pages = []
    
    for page_num_str, page_content in matches:
        page_num = int(page_num_str)
        # Clean up whitespace
        cleaned = page_content.strip()
        if not cleaned:
            blank_pages.append(page_num)
        else:
            filled_pages.append(page_num)
            
    print(f"Filled pages ({len(filled_pages)}): {filled_pages[:10]} ...")
    print(f"Blank pages ({len(blank_pages)}): {blank_pages}")
    
if __name__ == "__main__":
    check_blanks()

import re

file_path = "c:\\Stable_Diffusion\\MACH_RE\\documents\\public_documents\\BanSacVanHoaVietNam_Phan_Ngoc.md"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Split content by TRANG headers
pages = re.split(r"^## TRANG (\d+)\n", content, flags=re.MULTILINE)

# pages[0] is the intro
# pages[1] is "1", pages[2] is text of page 1, etc.
page_dict = {}
for i in range(1, len(pages), 2):
    page_num = int(pages[i])
    page_text = pages[i+1]
    page_dict[page_num] = page_text

print("Pages 1 to 50 status (checking for $\\text{):")
for p in range(1, 51):
    if p in page_dict:
        text = page_dict[p]
        has_latex = "$\\text{" in text or "\\text{" in text
        print(f"Page {p:02d}: has_latex={has_latex}, length={len(text)} chars")
    else:
        print(f"Page {p:02d}: NOT FOUND")

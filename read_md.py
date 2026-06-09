import re

file_path = "c:\\Stable_Diffusion\\MACH_RE\\documents\\public_documents\\BanSacVanHoaVietNam_Phan_Ngoc.md"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

trang_pattern = re.compile(r"^## TRANG (\d+)", re.IGNORECASE)
matches = []
for idx, line in enumerate(lines):
    m = trang_pattern.match(line)
    if m:
        matches.append((idx + 1, line.strip()))

print(f"Found {len(matches)} TRANG headers:")
for m in matches[:20]:
    print(f"  Line {m[0]}: {m[1]}")
if len(matches) > 20:
    print(f"  ... and {len(matches) - 20} more.")

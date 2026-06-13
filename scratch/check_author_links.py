import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "C:/Stable_Diffusion/MACH_RE"
html_files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]

FILE_SOURCES = {
    "index.html": ["ashby", "prasad_2023"],
    "why.html": ["putnam", "ostrom", "nagarjuna", "dharmakirti"],
    "what.html": ["phan_ngoc", "ashby", "weick", "levi_strauss", "whitehead", "nagarjuna"],
    "when.html": ["bui_2023"],
    "who.html": ["phan_ngoc", "bui_2023", "phan_2003", "quang_2002", "npt_2021", "robertson_2015", "wiredu_1996", "lederach_1997", "assmann", "berdyaev_1947", "nodia_2009", "valkonen_2014", "smidchens_2014"],
    "how.html": ["phan_ngoc", "ashby", "weick", "nagarjuna"],
    "axioms.html": ["phan_ngoc", "ashby", "weick", "nagarjuna", "ntl_1975", "udah_2025", "lefa_2015"],
    "axiom_1.html": ["whitehead", "phan_ngoc", "ashby", "weick", "nagarjuna", "ntl_1975", "nvn_1928", "emirbayer_1997", "dewey_bentley_1949"],
    "axiom_2.html": ["phan_ngoc", "levi_strauss", "ashby", "ntl_1975"],
    "axiom_3.html": ["heidegger", "bergson", "assmann", "benjamin", "halbwachs", "luhmann", "barbour", "eliade", "udah_2025", "lefa_2015"],
    "axiom_4.html": ["ashby", "phan_ngoc", "ntl_1975"],
    "axiom_derived.html": ["udah_2025", "lefa_2015"],
    "upgrade.html": ["nagarjuna", "dharmakirti"],
    "axiom_conflict.html": ["nagarjuna", "dharmakirti"],
    "mach_re_homologous.html": ["udah_2025", "lefa_2015", "taylor_2013", "litana_1998", "akande_2019", "abimbola_1976", "peel_2000"],
    "axiom_3_cultural_comparison.html": ["udah_2025", "lefa_2015"],
    "luu_tru.html": ["okeefe_nadel", "tulving", "vygotsky", "halbwachs", "luhmann"],
    "ubuntu.html": ["udah_2025", "lefa_2015", "mbigi_1997", "samkange_1980", "tutu_2000", "ramose_2002"],
}

# Source display names to look for
KEYWORDS = {
    "phan_ngoc": ["Phan Ngọc", "Phan Ngoc"],
    "ashby": ["Ashby"],
    "weick": ["Weick", "Orton"],
    "nagarjuna": ["Nāgārjuna", "Nagarjuna", "Trung quán", "Trung Quán"],
    "dharmakirti": ["Dharmakīrti", "Dharmakirti", "Nhận thức luận Phật giáo", "pramāṇa", "Pramāṇa"],
    "levi_strauss": ["Lévi-Strauss", "Levi-Strauss"],
    "whitehead": ["Whitehead"],
    "ntl_1975": ["Nguyễn Tấn Long", "Phan Canh", "Thi ca bình dân"],
    "nvn_1928": ["Nguyễn Văn Ngọc", "Nam An"],
    "emirbayer_1997": ["Emirbayer", "relational sociology"],
    "dewey_bentley_1949": ["Dewey", "Bentley"],
    "udah_2025": ["Udah"],
    "lefa_2015": ["Lefa"],
    "heidegger": ["Heidegger"],
    "bergson": ["Bergson"],
    "assmann": ["Assmann"],
    "benjamin": ["Benjamin"],
    "halbwachs": ["Halbwachs"],
    "luhmann": ["Luhmann"],
    "barbour": ["Barbour"],
    "eliade": ["Eliade"],
    "ostrom": ["Ostrom"],
    "putnam": ["Putnam"],
    "okeefe_nadel": ["O'Keefe", "Nadel"],
    "tulving": ["Tulving"],
    "vygotsky": ["Vygotsky"],
    "mbigi_1997": ["Mbigi"],
    "samkange_1980": ["Samkange"],
    "tutu_2000": ["Tutu", "Forgiveness"],
    "ramose_2002": ["Ramose"],
    "taylor_2013": ["Taylor"],
    "litana_1998": ["Li Tana"],
    "akande_2019": ["Akande"],
    "abimbola_1976": ["Abimbola"],
    "peel_2000": ["Peel"],
    "bui_2023": ["Trang Bui", "Bui, T.", "Trang Bùi"],
    "phan_2003": ["Phan, P. C.", "Phan, 2003", "Peter C. Phan"],
    "quang_2002": ["Quang & Vuong", "Quang, T.", "Truong Quang"],
    "npt_2021": ["Nguyễn Phú Trọng", "Nguyen Phu Trong", "npt_2021"],
    "robertson_2015": ["Robertson", "robertson_2015"],
    "wiredu_1996": ["Wiredu", "wiredu_1996"],
    "lederach_1997": ["Lederach", "lederach_1997"],
    "berdyaev_1947": ["Berdyaev", "berdyaev_1947"],
    "nodia_2009": ["Nodia", "nodia_2009"],
    "valkonen_2014": ["Valkonen", "valkonen_2014"],
    "smidchens_2014": ["Šmidchens", "Smidchens", "smidchens_2014"],
}

out_path = os.path.join(workspace_dir, "scratch/author_mentions_report.txt")
out_lines = []

for filename, sources in FILE_SOURCES.items():
    if not sources:
        continue
    filepath = os.path.join(workspace_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    out_lines.append("\n" + "="*80)
    out_lines.append(f"FILE: {filename}")
    out_lines.append("="*80)
    
    # We want to check only the body text (before the bibliography)
    body_lines = []
    for line in lines:
        if "Nguồn Trích Dẫn" in line or "Nguon Trich Dan" in line:
            break
        body_lines.append(line)
        
    for idx, source_key in enumerate(sources, 1):
        keywords = KEYWORDS.get(source_key, [])
        found_mentions = []
        for line_num, line in enumerate(body_lines, 1):
            for kw in keywords:
                if kw in line:
                    # check if already linked in this line
                    linked = f'href="#nguon-{idx}"' in line or f"href='#nguon-{idx}'" in line
                    found_mentions.append((line_num, kw, linked, line.strip()))
                    break
        
        out_lines.append(f"\nSource: {source_key} (should be linked as [{idx}])")
        if found_mentions:
            for l_num, kw, linked, text in found_mentions:
                status = "✅ linked" if linked else "❌ NOT linked"
                out_lines.append(f"  Line {l_num:4d} | {kw:15s} | {status} | {text[:100]}...")
        else:
            out_lines.append("  ❌ No mentions found in body text!")

with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print(f"Report written to {out_path}")

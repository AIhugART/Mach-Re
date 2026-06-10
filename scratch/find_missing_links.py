import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = "C:/Stable_Diffusion/MACH_RE"
html_files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]

# Mappings from file_sources
FILE_SOURCES = {
    "index.html": ["ashby", "prasad_2023"],
    "why.html": ["putnam", "ostrom", "nagarjuna", "dharmakirti"],
    "what.html": ["phan_ngoc", "ashby", "weick", "levi_strauss", "whitehead", "nagarjuna", "hountondji", "wiredu", "hutchins"],
    "when.html": [],
    "who.html": ["phan_ngoc"],
    "how.html": ["phan_ngoc", "ashby", "weick", "nagarjuna"],
    "axioms.html": ["phan_ngoc", "ashby", "weick", "nagarjuna", "ntl_1975", "udah_2025", "lefa_2015"],
    "axiom_1.html": ["whitehead", "phan_ngoc", "ashby", "weick", "nagarjuna", "ntl_1975"],
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
    "relational_and_distributed_philosophy.html": ["hountondji", "wiredu", "hutchins", "oruka", "dewey_bentley", "cadiere_1958", "ryle_1949", "aristotle_metaphysics", "descartes_meditations", "henrich_2015"],
    "yoruba.html": ["akande_2019", "abimbola_1976", "peel_2000", "bewaji_2004", "idowu_1962", "gbadegesin_1991", "abiodun_2014"],
}

print("Checking which files are missing inline citation links in their text body...")

for filename, sources in FILE_SOURCES.items():
    if not sources:
        continue
    filepath = os.path.join(workspace_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We strip the bibliography section itself to check only the body text
    body_content = content
    bib_match = re.search(r'(?:<!-- NGUỒN TRÍCH DẪN -->|<section[^>]*>\s*<h2>Nguồn Trích Dẫn</h2>|<h2[^>]*>Nguồn Trích Dẫn</h2>)', content, re.IGNORECASE)
    if bib_match:
        body_content = content[:bib_match.start()]
        
    missing_links = []
    for idx, source_key in enumerate(sources, 1):
        # We expect a link like href="#nguon-idx" in the body
        link_pattern = f'href="#nguon-{idx}"'
        link_pattern_alt = f"href='#nguon-{idx}'"
        
        if link_pattern not in body_content and link_pattern_alt not in body_content:
            missing_links.append(f"{source_key} (should be linked as [{idx}])")
            
    if missing_links:
        print(f"\nFILE: {filename}")
        for m in missing_links:
            print(f"  - Missing link for: {m}")

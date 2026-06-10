import os
import re
import sys

# Reconfigure stdout to use utf-8 to avoid UnicodeEncodeError on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]

# Master sources registry - strict APA 7th Edition
SOURCES = {
    "phan_ngoc": "[N] Phan Ngọc. (1998). <em>Bản sắc văn hóa Việt Nam</em>. NXB Văn hóa - Thông tin.",
    "ashby": "[N] Ashby, W. R. (1956). <em>An Introduction to Cybernetics</em>. Chapman &amp; Hall. <a href=\"http://ashby.info/intro.html\" target=\"_blank\" rel=\"noopener noreferrer\">http://ashby.info/intro.html</a>",
    "weick": "[N] Orton, J. D., &amp; Weick, K. E. (1990). Loosely coupled systems: A reconceptualization. <em>Academy of Management Review</em>, <em>15</em>(2), 203–223.",
    "nagarjuna": "[N] Nāgārjuna (thế kỷ II–III). <em>Mūlamadhyamakakārikā</em> (Căn bản Trung quán luận tụng).",
    "dharmakirti": "[N] Dharmakīrti (thế kỷ VII). <em>Pramāṇavārttika</em> — Nhận thức luận Phật giáo.",
    "levi_strauss": "[N] Lévi-Strauss, C. (1958). <em>Anthropologie structurale</em>. Plon.",
    "whitehead": "[N] Whitehead, A. N. (1929). <em>Process and Reality</em>. Macmillan.",
    "ntl_1975": "[N] Nguyễn Tấn Long &amp; Phan Canh. (1975). <em>Thi ca bình dân Việt Nam</em> (Q1–Q3). NXB Khoa học Xã hội.",
    "udah_2025": "[N] Udah, H., Tusasiirwe, S., Mugumbate, R., &amp; Gatwiri, K. (2025). Ubuntu philosophy, values, and principles: An opportunity to do social work differently. <em>Journal of Social Work</em>, pp. 1–19. <a href=\"https://doi.org/10.1177/14680173241312749\" target=\"_blank\" rel=\"noopener noreferrer\">https://doi.org/10.1177/14680173241312749</a>",
    "lefa_2015": "[N] Lefa, B. J. (2015). <em>Ubuntu in South African Education</em>. Cape Peninsula University of Technology.",
    "heidegger": "[N] Heidegger, M. (1927). <em>Sein und Zeit</em>. Max Niemeyer.",
    "bergson": "[N] Bergson, H. (1889). <em>Essai sur les données immédiates de la conscience</em>. Félix Alcan.",
    "assmann": "[N] Assmann, J. (1992). <em>Das kulturelle Gedächtnis</em>. C.H. Beck.",
    "benjamin": "[N] Benjamin, W. (1940). Über den Begriff der Geschichte (Theses on the Philosophy of History).",
    "halbwachs": "[N] Halbwachs, M. (1925). <em>Les cadres sociaux de la mémoire</em>. Félix Alcan.",
    "luhmann": "[N] Luhmann, N. (1984). <em>Soziale Systeme</em>. Suhrkamp.",
    "barbour": "[N] Barbour, J. (1999). <em>The End of Time</em>. Oxford University Press.",
    "eliade": "[N] Eliade, M. (1957). <em>The Sacred and the Profane</em>. Harcourt, Brace &amp; World.",
    "ostrom": "[N] Ostrom, E. (1990). <em>Governing the Commons</em>. Cambridge University Press.",
    "putnam": "[N] Putnam, R. D. (2000). <em>Bowling Alone</em>. Simon &amp; Schuster.",
    "okeefe_nadel": "[N] O'Keefe, J., &amp; Nadel, L. (1978). <em>The Hippocampus as a Cognitive Map</em>. Oxford University Press.",
    "tulving": "[N] Tulving, E., &amp; Pearlstone, Z. (1966). Availability versus accessibility of information in memory for words. <em>Journal of Verbal Learning and Verbal Behavior</em>, <em>5</em>(4), 381–391.",
    "vygotsky": "[N] Vygotsky, L. S. (1934). <em>Thought and Language</em>. MIT Press (English trans. 1962).",
    
    # Newly integrated for Ubuntu and Homologous
    "mbigi_1997": "[N] Mbigi, L. (1997). <em>Ubuntu: The African Dream in Management</em>. Knowledge Resources.",
    "samkange_1980": "[N] Samkange, S., &amp; Samkange, T. M. (1980). <em>Hunhuism or Ubuntuism: A Zimbabwe Indigenous Political Philosophy</em>. Graham Publishing.",
    "tutu_2000": "[N] Tutu, D. (2000). <em>No Future Without Forgiveness</em>. Doubleday.",
    "ramose_2002": "[N] Ramose, M. B. (2002). The philosophy of Ubuntu and Ubuntu as a philosophy. In P. H. Coetzee &amp; A. P. J. Roux (Eds.), <em>Philosophy from Africa</em> (2nd ed., pp. 230–238). Oxford University Press.",
    "taylor_2013": "[N] Taylor, K. W. (2013). <em>A History of the Vietnamese</em>. Cambridge University Press. ISBN 9780521699150. — Chronology of Vietnamese southward territorial expansion from the Lý dynasty (1069) through the Nguyễn period; episodic in nature across seven centuries.",
    "litana_1998": "[N] Li Tana. (1998). <em>Nguyễn Cochinchina: Southern Vietnam in the Seventeenth and Eighteenth Centuries</em>. Cornell Southeast Asia Program. ISBN 9780877277224. — Documents the final phases of Nam tiến (Mekong Delta, ~1620–1757) and the portable, nuclear-family structure of Vietnamese settlement under the Nguyễn lords.",
    "akande_2019": "[N] Akande, A. O. (2019). Ará Òrun Kìn-ìn Kin-in: Òyó-Yòrùbá Egúngún Masquerade in Communion and Maintenance of Ontological Balance. <em>Genealogy</em>, <em>3</em>(1), 7. <a href=\"https://doi.org/10.3390/genealogy3010007\" target=\"_blank\" rel=\"noopener noreferrer\">https://doi.org/10.3390/genealogy3010007</a> — Ethnographic study of Egungun as embodied ancestor (physical return, judgment, blessings); Egungun society as cross-lineage institution; sacred grove; diaspora continuity.",
    "abimbola_1976": "[N] Abimbola, W. (1976). <em>Ifa: An Exposition of Ifa Literary Corpus</em>. Oxford University Press Nigeria. ISBN 9780195751994. — Standard scholarly reference on Ifa divination system, role of babalawo (specialist priest), Ofo (ancestral curse/oath), and Ẹ̀jọ́ (traditional Yoruba justice) as mediated through ancestral authority.",
    "peel_2000": "[N] Peel, J. D. Y. (2000). <em>Religious Encounter and the Making of the Yoruba</em>. Indiana University Press. ISBN 0-253-33794-1. — Authoritative account of Yoruba ancestral ontology: ancestors as independent entities (not relational patterns), elderhood power extending into death, asymmetric living–ancestor relations."
}

# File to sources mapping
FILE_SOURCES = {
    "index.html": ["ashby", "prasad_2023"],
    "why.html": ["putnam", "ostrom", "nagarjuna", "dharmakirti"],
    "what.html": ["phan_ngoc", "ashby", "weick", "levi_strauss", "whitehead", "nagarjuna"],
    "when.html": [],  # no external research citations
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
}

# Add local sources
SOURCES["prasad_2023"] = "[N] Prasad, H. S. (2023). The Buddhist pramāṇa-epistemology, logic, and language: With reference to Vasubandhu, Dignāga, and Dharmakīrti. <em>Studia Humana</em>, <em>12</em>(1-2), pp. 21–52. <a href=\"https://doi.org/10.2478/sh-2023-0004\" target=\"_blank\" rel=\"noopener noreferrer\">https://doi.org/10.2478/sh-2023-0004</a>"

if __name__ == "__main__":
    print("Syncing citation tables across all HTML files via plan/add_citation_tables.py...")
    
    for filename in html_files:
        if filename == "when.html":
            continue
            
        filepath = os.path.join(workspace_dir, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        pattern = r'(<section[^>]*>\s*<h2[^>]*>Nguồn Trích Dẫn</h2>\s*<div[^>]*>)(.*?)(</div>\s*</section>)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            prefix = match.group(1)
            suffix = match.group(3)
            
            sources_keys = FILE_SOURCES.get(filename, [])
            if not sources_keys:
                continue
                
            new_paragraphs = []
            for i, key in enumerate(sources_keys, 1):
                if key not in SOURCES:
                    print(f"ERROR: Key '{key}' not found in SOURCES!")
                    continue
                entry = SOURCES[key].replace("[N]", f"[{i}]")
                new_paragraphs.append(f"    <p id=\"nguon-{i}\">{entry}</p>")
                
            new_inner_content = "\n" + "\n".join(new_paragraphs) + "\n  "
            new_section = prefix + new_inner_content + suffix
            
            updated_content = content[:match.start()] + new_section + content[match.end():]
            
            with open(filepath, "w", encoding="utf-8", newline="\n") as f:
                f.write(updated_content)
                
            print(f"  ✅ Synced: {filename}")
        else:
            print(f"  ⚠️ Could not find section in: {filename}")

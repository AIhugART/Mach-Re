"""
Script hỗ trợ thêm bảng "Nguồn Trích Dẫn" vào HTML files.
KHÔNG tự động chạy — chỉ in ra những gì cần làm để review thủ công.
"""

# Master source registry — all distinct external sources across HTML files
SOURCES = {
    # Vietnamese cultural anthropology
    "phan_ngoc": "[N] Phan Ngọc (1998). <em>Bản sắc văn hóa Việt Nam</em>. NXB Văn hóa - Thông tin, Hà Nội.",
    # Cybernetics
    "ashby": "[N] Ashby, W. R. (1956). <em>An Introduction to Cybernetics</em>. Chapman &amp; Hall, London.",
    # Organizational theory
    "weick": "[N] Orton, J. D., &amp; Weick, K. E. (1990). Loosely coupled systems: A reconceptualization. <em>Academy of Management Review</em>, 15(2), 203–223.",
    # Buddhist philosophy
    "nagarjuna": "[N] Nāgārjuna (thế kỷ II–III). <em>Mūlamadhyamakakārikā</em> (Căn bản Trung quán luận tụng).",
    "dharmakirti": "[N] Dharmakīrti (thế kỷ VII). <em>Pramāṇavārttika</em> — Nhận thức luận Phật giáo.",
    # Structural anthropology
    "levi_strauss": "[N] Lévi-Strauss, C. (1958). <em>Anthropologie structurale</em>. Plon, Paris.",
    # Process philosophy
    "whitehead": "[N] Whitehead, A. N. (1929). <em>Process and Reality</em>. Macmillan, New York.",
    # Ca dao corpus
    "ntl_1975": "[N] Nguyễn Tấn Long &amp; Phan Canh (1975). <em>Thi ca bình dân Việt Nam</em> (Q1–Q3). NXB Khoa học Xã hội, Hà Nội.",
    # Ubuntu sources
    "udah_2025": "[N] Udah, H., Tusasiirwe, S., Mugumbate, R., &amp; Gatwiri, K. (2025). Ubuntu philosophy, values, and principles: An opportunity to do social work differently. <em>Journal of Social Work</em>, pp. 1–19. https://doi.org/10.1177/14680173241312749",
    "lefa_2015": "[N] Lefa, B. J. (2015). <em>Ubuntu in South African Education</em>. Cape Peninsula University of Technology.",
    # Continental philosophy
    "heidegger": "[N] Heidegger, M. (1927). <em>Sein und Zeit</em>. Max Niemeyer, Halle.",
    "bergson": "[N] Bergson, H. (1889). <em>Essai sur les données immédiates de la conscience</em>. Félix Alcan, Paris.",
    "assmann": "[N] Assmann, J. (1992). <em>Das kulturelle Gedächtnis</em>. C.H. Beck, München.",
    "benjamin": "[N] Benjamin, W. (1940). Über den Begriff der Geschichte (Theses on the Philosophy of History).",
    "halbwachs": "[N] Halbwachs, M. (1925). <em>Les cadres sociaux de la mémoire</em>. Félix Alcan, Paris.",
    "luhmann": "[N] Luhmann, N. (1984). <em>Soziale Systeme</em>. Suhrkamp, Frankfurt.",
    "barbour": "[N] Barbour, J. (1999). <em>The End of Time</em>. Oxford University Press.",
    "eliade": "[N] Eliade, M. (1957). <em>The Sacred and the Profane</em>. Harcourt, Brace &amp; World, New York.",
    # Political theory
    "ostrom": "[N] Ostrom, E. (1990). <em>Governing the Commons</em>. Cambridge University Press.",
    "putnam": "[N] Putnam, R. D. (2000). <em>Bowling Alone</em>. Simon &amp; Schuster, New York.",
    # Cognitive science
    "okeefe_nadel": "[N] O'Keefe, J., &amp; Nadel, L. (1978). <em>The Hippocampus as a Cognitive Map</em>. Oxford University Press.",
    "tulving": "[N] Tulving, E., &amp; Pearlstone, Z. (1966). Availability versus accessibility of information in memory for words. <em>Journal of Verbal Learning and Verbal Behavior</em>, 5(4), 381–391.",
    "vygotsky": "[N] Vygotsky, L. S. (1934). <em>Thought and Language</em>. MIT Press (English trans. 1962).",
}

# File → sources mapping
FILE_SOURCES = {
    "index.html": ["ashby"],
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
    "mach_re_homologous.html": ["udah_2025", "lefa_2015"],
    "axiom_3_cultural_comparison.html": ["udah_2025", "lefa_2015"],
    "luu_tru.html": ["okeefe_nadel", "tulving", "vygotsky", "halbwachs", "luhmann"],
    "ubuntu.html": ["udah_2025", "lefa_2015"],  # already done
}

def generate_citation_table(file_name):
    """Generate HTML for Nguồn Trích Dẫn section."""
    sources_keys = FILE_SOURCES.get(file_name, [])
    if not sources_keys:
        return None

    lines = []
    lines.append('<!-- NGUỒN TRÍCH DẪN -->')
    lines.append('<section style="margin-bottom:24px">')
    lines.append('  <h2>Nguồn Trích Dẫn</h2>')
    lines.append('  <div class="cite-box" style="font-size:.88rem;line-height:1.8;color:var(--text-muted)">')

    for i, key in enumerate(sources_keys, 1):
        entry = SOURCES[key].replace("[N]", f"[{i}]")
        lines.append(f'    <p id="nguon-{i}">{entry}</p>')

    lines.append('  </div>')
    lines.append('</section>')
    return '\n'.join(lines)

# Main: print report
if __name__ == "__main__":
    for fname, sources in FILE_SOURCES.items():
        status = "✅ done" if fname == "ubuntu.html" else ("⚠️ no citations" if not sources else "❌ needs table")
        print(f"{status:20s} {fname:45s} sources: {len(sources)}")

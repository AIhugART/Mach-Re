# Changelog — Paper 005 (Mạch Rễ)

> **Phạm vi:** Nơi **duy nhất** ghi nhận thay đổi cho các file trong `papers/paper_005/`. Không ghi paper_005 changes vào `papers/CHANGELOG_papers.md`.
> **Liên kết:** Lịch sử toàn bộ papers → xem [`CHANGELOG_papers.md`](../CHANGELOG_papers.md); lịch sử toàn bộ dự án → xem [`CHANGELOG.md`](../../CHANGELOG.md) tại thư mục gốc.
> **Quy tắc:** Mỗi entry phải qua 3-round RCA × 5-Why × scoring gate ≥ 4/5 (theo `CLAUDE.md` §RULE ZERO).

## 2026-06-11 — paper_005_v2: Việt hóa toàn diện từ EN sang thuần Việt · RCA 5.0/5

**Symptom (Round 1):** Bài báo viết bằng tiếng Việt về triết học Việt Nam nhưng chứa ~120 instances từ tiếng Anh phổ thông/học thuật chung (`proof-of-concept`, `peer-review`, `markers`, `pattern`, `framework`, `Reader`, `consensus`, `precedent`, `vocabulary`, `discourse`, `Section`, `substance`, `interlocutors`, `checkpoint`, `systemize`, `longevity`, `elaboration`, `hypothesis`, `scope`, `operationalizing`, `identity`, `institutions`, `node`, `context`, `network`, `consistency`, `completeness`, `memory`, `WHAT`/`WHY`, `canonical text`, `Dimension`, `Pattern`, `Consistency + Completeness`, `Survival + Adaptation under pressure`, `selection pressure`, `evolutionary pressure`, `distributed form`, `selection mechanism`, `Causal chain`, `conceptual framework`, `Research Questions`, `founding systematic text`, `WHY mechanism`, `relational-practical logic`, `systematic-metaphysical logic`, `document`, `documentation`, `corpus`, `Inter-system patterns`, `recurrent philosophical ritual`) — thay vì dùng từ thuần Việt đã có sẵn.

**Mechanism (Round 2):** Bài báo lập luận rằng triết học Việt Nam bị "đo sai thước đo" (dùng Systematic Metaphysics để đo Relational-Distributed Philosophy). Việc dùng tiếng Anh phổ thông thay vì tiếng Việt cho các khái niệm thông dụng tạo ra mâu thuẫn nội tại: chính bài báo đang dùng "thước đo ngoại lai" (English) cho nội dung có thể diễn đạt bằng tiếng Việt. Điều này vi phạm nguyên tắc "không đo bằng thước ngoại lai" mà bài báo đang bảo vệ.

**Root (Round 3):** Vi phạm CLAUDE.md §Sứ mệnh Việt hóa — ưu tiên 1: "Thuần Việt có sẵn, đúng phạm trù → chọn." Tất cả các từ trên đều có thuần Việt tương đương. Root cause: thói quen dùng English term trong academic writing mà không kiểm tra xem tiếng Việt đã có từ tương đương chưa.

**Fix (2 files + 1 changelog):**
- `papers/paper_005/paper_005_v2.md`: Việt hóa toàn bộ ~120 instances (43 loại từ) → viết lại toàn bộ file.
- `papers/paper_005/paper_005_v2.html`: Việt hóa toàn bộ ~120 instances (~30 Edit replace_all calls) → đồng bộ với .md.
- `papers/paper_005/CHANGELOG_paper_005.md`: Entry này.

**Quy tắc phân loại đã áp dụng:**
- **Dịch thuần Việt:** Từ phổ thông/học thuật chung có thuần Việt tương đương.
- **Giữ song ngữ VN (EN):** Thuật ngữ chuyên ngành triết học (vd: "lỗi phạm trù (category error)", "Triết học Tương quan-Phân tán (Relational-Distributed Philosophy)").
- **Giữ nguyên EN:** Tên riêng, tên tác phẩm, ký hiệu toán học, citation markers, thuật ngữ Phật giáo (Pali/Sanskrit), technical terms chưa có thuần Việt (vd: `variety` trong Requisite Variety, `orature`).

**RCA score:** 5.0/5 (Correct 5 — real defect, Deep 5 — touches internal consistency, Feasible 5 — safe mechanical replacements, Conflict-risk 5 — no contradictions created, Preservation 5 — all claims and structure preserved).

**Compass:** A (Phan Ngọc) · B (Ashby/Weick) · C (Buddhist Epistemology) — dùng làm neo cho các quyết định dịch thuật ngữ (vd: "pattern" → "kiểu" khi trong ngữ cảnh Phan Ngọc, → "nếp" khi là structural pattern).

---

## 2026-06-11 — paper_005_v2: Bổ sung chỉ số trích dẫn cho khái niệm "lỗi phạm trù" · RCA 5.0/5

**Symptom (Round 1):** Khái niệm "lỗi phạm trù (category error)" tại dòng 14 (Tóm tắt), 22 (Boundary Statement), 64 (Giới thiệu) và 188 (Kết luận) của `paper_005_v2.md` và các định dạng liên quan chưa được gán chỉ số trích dẫn `[16]` (hoặc `(Ryle, 1949)`), vi phạm quy tắc liên kết trích dẫn trong `CLAUDE.md`.

**Mechanism (Round 2):** Việc thiếu chỉ số trích dẫn tại các lần xuất hiện then chốt khiến khái niệm mang tính nền tảng của bài báo bị giảm sức nặng học thuật, dễ bị hiểu nhầm là một tuyên bố tự thân thay vì là một công cụ phân tích đã được thừa nhận rộng rãi từ Gilbert Ryle (1949).

**Root (Round 3):** Quy trình kiểm tra trích dẫn (citation check) ở bước biên tập cuối chưa rà soát toàn bộ các lần xuất hiện của thuật ngữ then chốt ở các phân mục ngoài thân bài (Abstract, Boundary Statement, Conclusion), dẫn đến trích dẫn không đồng bộ.

**Fix (3 files):**
- `papers/paper_005/paper_005_v2.md`: Bổ sung chỉ số `[16]` tại dòng 14, 22, 64, 188.
- `papers/paper_005/paper_005_v2.html`: Bổ sung liên kết `<a href="#nguon-16">[16]</a>` tại các dòng tương ứng.
- `papers/paper_005/paper_005_for_pdf.md`: Bổ sung trích dẫn parenthetical `(Ryle, 1949)` tại các dòng tương ứng.

**RCA score:** 5.0/5 (Correct 5, Deep 5, Feasible 5, Conflict-risk 5, Preservation 5).

---

## 2026-06-11 — paper_005_v2: Thêm Bảng Giải Thích Thuật Ngữ + Bảng Nhãn Phân Loại Học Thuật (RCA) · RCA 5.0/5

**Symptom (Round 1):** paper_005_v2.md dùng ~50 nhãn `[established]`, `[contested]`, `[interpretation]`, `[analogy]`, `[hypothesis]` và 6 khái niệm triết học phức tạp (Relational Ontology, Structural Invariance, Orthogonal Temporality, Dynamic Boundary, Distributed Storage, Category Error) nhưng không có bảng giải thích cho độc giả phổ thông. paper_005.md (v1) đã có cả hai bảng này — v2 bỏ sót trong quá trình rebuild.

**Mechanism (Round 2):** Carry-forward set của v2 (plan/paper_005_v2_plan.md §CARRY-FORWARD SET) tập trung vào core claims và methodology, bỏ qua auxiliary explanatory content. Hậu quả: độc giả không quen với hệ nhãn RCA của dự án không thể decode được epistemic stance của tác giả; học sinh cấp 3 không có lối vào các khái niệm cốt lõi.

**Root (Round 3):** Vi phạm nguyên tắc self-containedness — paper dùng hệ nhãn và thuật ngữ riêng mà không giải thích. CLAUDE.md Tier 3 Rule #7 (citation traceability) không chỉ đòi hỏi liên kết nguồn mà còn đòi hỏi người đọc HIỂU được các nhãn phân loại.

**Fix (2 files + 1 changelog):**
- `papers/paper_005/paper_005_v2.md`: Thêm 2 section mới trước Nguồn Trích Dẫn: (a) BẢNG GIẢI THÍCH THUẬT NGỮ — 6 thuật ngữ cốt lõi với giải thích trực quan cấp 3 + ví dụ từ bài viết; (b) Ý NGHĨA CÁC NHÃN PHÂN LOẠI HỌC THUẬT (RCA) — 5 nhãn với ý nghĩa học thuật + giải thích trực quan + ví dụ.
- `papers/paper_005/paper_005_v2.html`: Tương tự — 2 bảng HTML đồng bộ.
- `papers/paper_005/CHANGELOG_paper_005.md`: Entry này.

**Bảng thuật ngữ đã thích ứng cho v2:**
- Đánh số 1–6 (không phải 1–8 như v1 — bỏ các tiên đề không xuất hiện chính trong v2)
- Thêm entry "Category Error — Lỗi phạm trù" (không có trong v1, là core của v2)
- Dùng thuần Việt theo chuẩn v2 (nếp, kiểu, thực thể, văn bản kinh viện...)
- Ví dụ lấy TRỰC TIẾP từ nội dung v2 (không dùng ví dụ từ v1)

**RCA score:** 5.0/5 (Correct 5, Deep 5, Feasible 5, Conflict-risk 5, Preservation 5).

---

## 2026-06-11 — paper_005_v2: Thêm hyperlink từ trích dẫn [N] → bảng Nguồn Trích Dẫn · RCA 5.0/5

**Symptom (Round 1):** File .md dùng `[N]` dạng plain text cho trích dẫn inline — không có hyperlink đến entry tương ứng trong bảng Nguồn Trích Dẫn. Người đọc phải cuộn thủ công 200+ dòng để tra cứu nguồn.

**Mechanism (Round 2):** CLAUDE.md Tier 3 Rule #12 yêu cầu hyperlink cho HTML nhưng chỉ yêu cầu `[N]` cho .md. Tuy nhiên, paper này được đọc trên GitHub (render .md trực tiếp) — thiếu hyperlink làm giảm citation traceability. Paper lập luận về "đo đúng thước đo" và "chính xác phạm trù" → trích dẫn không clickable là một khiếm khuyết về traceability, nhất quán thấp với tiêu chuẩn paper tự đặt ra.

**Root (Round 3):** HTML đã có `<a href="#nguon-N">` từ trước; .md chưa được nâng cấp tương ứng. Việc thêm hyperlink đưa .md lên ngang tiêu chuẩn HTML — nhất quán nội bộ giữa hai định dạng xuất bản.

**Fix (1 file + 1 changelog):**
- `papers/paper_005/paper_005_v2.md`: (a) Thêm `<a id="nguon-N"></a>` vào 26 entry bảng Nguồn Trích Dẫn; (b) Chuyển toàn bộ `[N]` inline trong văn xuôi → `<a href="#nguon-N">[N]</a>` (~30 instances, mỗi số 1–26).
- `papers/paper_005/CHANGELOG_paper_005.md`: Entry này.

**RCA score:** 5.0/5 (Correct 5 — genuine enhancement, Deep 5 — nhất quán với citation traceability principle, Feasible 5 — mechanical HTML-anchor additions, Conflict-risk 5 — anchors isolated in table, Preservation 5 — all content preserved).

**Nota bene:** Các số [5], [10], [17] không xuất hiện trong văn xuôi (chỉ trong bảng) → không cần hyperlink prose.

---

## 2026-06-11 — Paper 005 v2 Plan · Sync Mạch Rễ v3.2 (v2.1)

**RCA plan level:** 0.0 → 4.86/5 (correct 5.0, deep 4.9, feasible 4.7, conflict-risk 4.7, preservation 5.0). 4 decisions scored: D1 (4.98, circular argument fix), D2 (4.76, Ubuntu proof-of-concept), D3 (4.98, distributed storage WHY), D4 (5.0, open questions). Compass A/B/C. Chuyển từ v1 (Mạch Rễ làm thẩm quyền) sang v2 (chứng minh độc lập loại hình qua Ubuntu). v2.1 sync Mạch Rễ v3.2 — thêm ghi chú Tiên Đề IX, cập nhật Literature Plan §4.3 với nguồn nội bộ mới. Cấu trúc paper S1→S7 không đổi.

**Files:**
- `papers/paper_005/plan/paper_005_v2_plan.md` (tạo mới v2.0, cập nhật v2.1)

> Cross-ref: Mạch Rễ v3.2 → axiom_spec.md, axiom_9.html, who.html/when.html/why.html/what.html/how.html → logged in [`CHANGELOG.md`](../../CHANGELOG.md).

## 2026-06-11 — Paper 005 v2 Manuscript Created · RCA 4.86/5

**Execution of v2 plan.** Full manuscript created per ESP Framework (E→S→P). 7 sections: S1-S3 carry-forward from v1 (Cadière→Đào Duy Anh, Hidden Measure, Category Error Diagnosis), S4-S7 newly written (Relational-Distributed Philosophy definition, Ubuntu proof-of-concept, 4 markers in Vietnamese folk philosophy, WHY mechanism via 6-channel distributed storage under historical pressure, 3 open questions). All 4 RCA decisions operationalized: D1 (Mạch Rễ as context, not authority), D2 (Ubuntu ≠ Vietnamese philosophy — type match, not system equivalence), D3 (Ashby Requisite Variety confirms evolutionary selection mechanism), D4 (Section 7 = open questions, not closed recommendations). Compass A/B/C used as independent anchors throughout. Boundary Statement, Claim Ladder at Interpretive Mapping level, full citation table (26 sources APA+DOI). Conservative hedging per CLAUDE.md Tier 3 Rule 8.

**Files:**
- `papers/paper_005/paper_005_v2.md` (tạo mới — manuscript 7 sections + 26-source citation table)
- `papers/paper_005/paper_005_v2.html` (tạo mới — Pandoc HTML5 export, 52 KB)
- `papers/paper_005/paper_005_v2.pdf` (tạo mới — Pandoc + xelatex PDF, 204 KB, A4, Times New Roman 12pt)
- `papers/paper_005/pdf_metadata_v2.yaml` (tạo mới — Pandoc YAML metadata with unicode-math)
- `papers/paper_005/plan/paper_005_v2_plan.md` (cập nhật — Phase 0-2 marked complete)

> Cross-ref: Plan v2.1 RCA 4.86/5 · 4 decisions ≥ 4/5 → logged above.

---

## 2026-06-11 — paper_005: Dời đoạn "Tự phân loại của Mạch Rễ" từ §2.1 xuống §4 — §2.1 chỉ nói về Việt Nam · RCA 5.0/5

**Symptom:** §2.1 "Thước đo ngầm là gì?" — vốn có nhiệm vụ vạch trần thước đo ẩn được dùng để đánh giá tư duy Việt Nam — chứa một đoạn dài về tự phân loại của Mạch Rễ (Tiên Đề I, Tiên Đề VIII, công thức `Being(x) ≡ {R(x,y)}`). Đoạn này khiến §2.1 nhảy từ chẩn đoán lịch sử sang giới thiệu framework trước khi lập luận về lỗi phạm trù được hoàn tất, làm yếu sức thuyết phục của paper (trông giống special pleading).

**Root (Round 3):** Paper vi phạm Claim Ladder của ESP Framework — nhảy từ Level 2 (Interpretive Mapping: "tư duy Việt Nam là tương quan-phân tán") lên Level 3 (Ontological Framework: "Mạch Rễ định nghĩa tương quan-phân tán") trước khi Level 2 được chứng minh xong. Gốc: paper được cấu trúc quanh Mạch Rễ như nhân vật chính, thay vì quanh Việt Nam như đối tượng bị chẩn đoán sai. Ngoài ra, Mạch Rễ là MỘT instance của triết học tương quan-phân tán, không phải định nghĩa của loại hình này — bảng đối chiếu trong §2.1 đã có sẵn ví dụ cột phải ("Ca dao tục ngữ Việt, Ubuntu châu Phi").

**Fix (4 files):**
- `paper_005.md`: Xóa đoạn "Tự phân loại của Mạch Rễ" khỏi §2.1; chèn lại vào đầu §4 (trước §4.1) với liên kết "thuộc cột phải của bảng đối chiếu ở §2.1".
- `paper_005_for_pdf.md`: Tương tự — xóa khỏi §2.1, chèn vào đầu §4 với parenthetical citations.
- `paper_005.html`: Xóa `<p><strong>Tự phân loại...</p>` khỏi §2.1; chèn `<p>` tương tự vào sau `</h2>` của §4, trước `<h3>` của §4.1.
- `draft/paper_005_draft_v1.md`: Draft vốn đã không có đoạn Mạch Rễ trong §2.1; chỉ cần chèn đoạn (với parenthetical citations) vào đầu §4.

**Arc mới:** §1 Chẩn đoán lịch sử → §2 Thước đo ẩn (chỉ nói về Việt Nam) → §3 Lỗi phạm trù → §4 Mạch Rễ như một vocabulary cho cột phải (mở đầu bằng tự phân loại).

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung nguồn trích dẫn cho định nghĩa khái niệm triết học hệ thống-siêu hình · RCA 5.0/5

**Symptom:** Định nghĩa khái niệm `"triết học hệ thống-siêu hình (systematic metaphysics)"` tại mục §2.1 của các định dạng `paper_005.md`, `paper_005.html`, `paper_005_for_pdf.md` và `draft/paper_005_draft_v1.md` chưa được dẫn nguồn trích dẫn đến các tác giả và tác phẩm làm căn cứ định nghĩa (Hountondji, Spinoza, Hegel).

**Root (Round 3):** Quá trình biên tập bản thảo chỉ gắn nhãn phân loại học thuật nội bộ `` `[project interpretation]` `` ở phần định nghĩa lý thuyết mà bỏ quên việc đặt các chỉ số dẫn nguồn quy chiếu thực tế (inline citation) tương ứng với danh mục thư mục tác phẩm ở cuối tài liệu (các nguồn `[6]`, `[19]`, `[20]`), dẫn đến tính thiếu thuyết phục về mặt căn cứ học thuật cho định nghĩa.

**Fix (4 files, 4 vị trí):**
- `paper_005.md`: Bổ sung chỉ số trích dẫn `[6, 19, 20]` và chuyển nhãn học thuật thành `[established scholarship]`: `đào tạo kinh viện [6, 19, 20] (`[established scholarship]`).`
- `paper_005.html`: Bổ sung các liên kết trích dẫn `<a href="#nguon-6">[6]</a>, <a href="#nguon-19">[19]</a>, <a href="#nguon-20">[20]</a>` và chuyển nhãn học thuật thành `[established scholarship]`.
- `paper_005_for_pdf.md`: Bổ sung các trích dẫn parenthetical `(Hountondji, 1983; Spinoza, 1677; Hegel, 1817)` và chuyển nhãn học thuật thành `[established scholarship]`.
- `draft/paper_005_draft_v1.md`: Bổ sung các trích dẫn parenthetical `(Hountondji, 1983; Spinoza, 1677; Hegel, 1817)` và chuyển nhãn học thuật thành `[established scholarship]`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung nguồn trích dẫn cho nhận định về việc các văn bản còn lưu không thể hiện nỗ lực đào sâu siêu hình học · RCA 5.0/5

**Symptom:** Nhận định `"các văn bản còn lưu không thể hiện nỗ lực đào sâu siêu hình học"` tại mục §1.2 một mâu thuẫn cần giải quyết trong các định dạng `paper_005.md`, `paper_005.html`, `paper_005_for_pdf.md` và `draft/paper_005_draft_v1.md` chưa được liên kết trực tiếp (inline citation) đến nguồn Wikipedia tương ứng (đã đăng ký ở danh mục thư mục tác phẩm).

**Root (Round 3):** Quá trình biên tập văn bản chỉ để nhãn phân loại học thuật chung `` `[established scholarship]` `` mà thiếu liên kết cụ thể đến nguồn tư liệu Wikipedia tiếng Việt (nguồn trích dẫn số `[24]`), gây giảm tính liên kết dữ liệu và thiếu nhất quán trong quy chiếu nguồn.

**Fix (4 files, 4 vị trí):**
- `paper_005.md`: Bổ sung chỉ số trích dẫn `[24]` ngay trước nhãn phân loại: `đào sâu siêu hình học [24] (`[established scholarship]`).`
- `paper_005.html`: Bổ sung liên kết trích dẫn `<a href="#nguon-24">[24]</a>` ngay trước nhãn phân loại: `đào sâu siêu hình học <a href="#nguon-24">[24]</a> (<code>[established scholarship]</code>).`
- `paper_005_for_pdf.md`: Bổ sung trích dẫn parenthetical `(Wikipedia, Triết học Việt Nam)` ngay trước nhãn phân loại: `đào sâu siêu hình học (Wikipedia, Triết học Việt Nam) (`[established scholarship]`).`
- `draft/paper_005_draft_v1.md`: Bổ sung trích dẫn parenthetical `(Wikipedia, Triết học Việt Nam)` ngay trước nhãn phân loại: `đào sâu siêu hình học (Wikipedia, Triết học Việt Nam) (`[established scholarship]`).`

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Tách nhóm nhận định (a) thành hai mục riêng biệt (a) và (b) · RCA 5.0/5

**Symptom:** Hai ý kiến phê phán khác nhau về tư tưởng Đại Việt (về năng lực sáng tạo của tư tưởng chính thống của Trần Quốc Vượng và về đặc điểm hệ thống của tư tưởng triết học tổng hợp từ Wikipedia) bị gộp chung vào mục (a) trong §1.1 văn bản nguồn của các định dạng `paper_005.md`, `paper_005.html` và `paper_005_for_pdf.md`.

**Root (Round 3):** Quá trình phân loại và nhóm họp các nhận định phê phán trước đây chỉ dựa trên chủ đề chung "Về năng lực sáng tạo và hệ thống" mà bỏ quên sự khác biệt về bản chất, chủ thể và nguồn gốc của hai phát biểu, dẫn đến việc gộp chung cơ học và làm mờ cấu trúc văn bản nguồn.

**Fix (4 files, 4 vị trí):**
- `paper_005.md`: Tách dòng nhận định thứ hai thành mục riêng `**(b) Về đặc điểm hệ thống của tư tưởng triết học [24]:**`, đồng thời dịch chuyển nhãn các nhận định phía sau từ (b)-(e) thành (c)-(f).
- `paper_005.html`: Tách dòng nhận định thứ hai trong HTML thành `<p><strong>(b) Về đặc điểm hệ thống của tư tưởng triết học <a href="#nguon-24">[24]</a>:</strong></p>`, đồng thời dịch chuyển nhãn các nhận định phía sau từ (b)-(e) thành (c)-(f).
- `paper_005_for_pdf.md`: Tách dòng nhận định thứ hai thành mục riêng `**(b) Về đặc điểm hệ thống của tư tưởng triết học (Wikipedia, Triết học Việt Nam):**`, đồng thời dịch chuyển nhãn các nhận định phía sau từ (b)-(e) thành (c)-(f).
- `draft/paper_005_draft_v1.md`: Tách dòng nhận định thứ hai thành mục riêng `**(b) Về đặc điểm hệ thống của tư tưởng triết học (Wikipedia, Triết học Việt Nam):**`, đồng thời dịch chuyển nhãn các nhận định phía sau từ (b)-(e) thành (c)-(f).

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung nguồn trích dẫn cho nhận định tổng hợp từ Wikipedia tiếng Việt · RCA 5.0/5

**Symptom:** Nhận định `"Tư tưởng triết học Việt Nam là bản sao chép rời rạc mang tính giáo điều thiếu sáng tạo, là sự thu nhỏ của triết học Ấn Độ và Trung Quốc."` tại mục §1.1 văn bản nguồn trong các định dạng `paper_005.md`, `paper_005.html` và `paper_005_for_pdf.md` chưa được dẫn nguồn trích dẫn cụ thể.

**Root (Round 3):** Quá trình biên soạn văn bản nguồn định dạng đoạn trích khái quát về quan điểm hoài nghi triết học Việt Nam dưới dạng một phát ngôn học thuật vô danh mà không tạo liên kết trực tiếp (inline citation) và định danh nguồn tổng hợp gốc từ mục từ Wikipedia tiếng Việt, dẫn đến việc thiếu đồng bộ trong hệ thống Nguồn Trích Dẫn.

**Fix (3 files, 6 vị trí):**
- `paper_005.md`:
  - §1.1 (L27): Bổ sung chỉ số trích dẫn `[24]` bên cạnh nhận định.
  - Nguồn Trích Dẫn (L286): Thêm entry `[24] Bách khoa toàn thư mở Wikipedia. Mục từ *Triết học Việt Nam* (mục "Đặc điểm của triết học Việt Nam").` vào bảng.
- `paper_005.html`:
  - §1.1 (L242): Bổ sung liên kết trích dẫn `<a href="#nguon-24">[24]</a>` bên cạnh nhận định.
  - Table footer (L899): Thêm dòng HTML cho `<td id="nguon-24"><strong>[24]</strong></td>` và mô tả thư mục tác phẩm.
- `paper_005_for_pdf.md`:
  - §1.1 (L80): Bổ sung trích dẫn parenthetical `(Wikipedia, Triết học Việt Nam)` bên cạnh nhận định.
  - Tài liệu tham khảo (L332): Bổ sung mục lục trích dẫn tác phẩm dưới tiêu đề `**Nguồn nhận định phân tích:**`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung nguồn trích dẫn cho nhận định của Trần Quốc Vượng về lịch sử tư tưởng chính thống Đại Việt · RCA 5.0/5

**Symptom:** Nhận định `"Không có sáng tạo, chỉ có vay mượn; chỉ có áp dụng, chỉ có thích nghi. Đó là sự thật của lịch sử tư tưởng chính thống Đại Việt."` tại mục §1.1 văn bản nguồn trong các định dạng `paper_005.md`, `paper_005.html` và `paper_005_for_pdf.md` chưa được dẫn nguồn trích dẫn cụ thể.

**Root (Round 3):** Quá trình xây dựng văn bản nguồn cho bài viết chỉ thu thập nhận định phê phán tính thụ động và sự áp dụng Nho giáo thiếu sáng tạo thời phong kiến mà không gắn tên tác giả hay định vị thư mục tác phẩm gốc (*Văn hóa Việt Nam: Tìm tòi và suy ngẫm*, 2000), dẫn đến sự thiếu hoàn thiện trong hệ thống Nguồn Trích Dẫn.

**Fix (3 files, 6 vị trí):**
- `paper_005.md`:
  - §1.1 (L23): Bổ sung tên tác giả và chỉ số trích dẫn `(Trần Quốc Vượng) [23]` bên cạnh tiêu đề nhóm nhận định (a).
  - Nguồn Trích Dẫn (L285): Thêm entry `[23] Trần Quốc Vượng. (2000). *Văn hóa Việt Nam: Tìm tòi và suy ngẫm*. Hà Nội: NXB Văn hóa Dân tộc.` vào bảng.
- `paper_005.html`:
  - §1.1 (L234): Bổ sung tên tác giả và liên kết trích dẫn `(Trần Quốc Vượng) <a href="#nguon-23">[23]</a>` bên cạnh tiêu đề nhóm nhận định (a).
  - Table footer (L895): Thêm dòng HTML cho `<td id="nguon-23"><strong>[23]</strong></td>` và mô tả thư mục tác phẩm.
- `paper_005_for_pdf.md`:
  - §1.1 (L76): Bổ sung trích dẫn parenthetical `(Trần Quốc Vượng, 2000)` bên cạnh tiêu đề nhóm nhận định (a).
  - Tài liệu tham khảo (L330): Bổ sung mục lục trích dẫn tác phẩm dưới tiêu đề `**Nguồn nhận định phân tích:**`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung nguồn trích dẫn cho nhận định của Thạch Lam · RCA 5.0/5

**Symptom:** Nhận định của Thạch Lam `**(d) Thạch Lam**` tại mục §1.1 văn bản nguồn trong các định dạng `paper_005.md`, `paper_005.html` và `paper_005_for_pdf.md` chưa được dẫn nguồn trích dẫn cụ thể.

**Root (Round 3):** Quá trình xây dựng văn bản nguồn cho bài viết chỉ thu thập đoạn trích phê phán tinh thần thực dụng thiển cận của Thạch Lam mà bỏ quên việc bổ sung chỉ số trích dẫn và định vị thư mục tác phẩm gốc (*Theo dòng*, 1938), dẫn đến sự thiếu hoàn thiện trong hệ thống Nguồn Trích Dẫn.

**Fix (3 files, 6 vị trí):**
- `paper_005.md`:
  - §1.1 (L37): Bổ sung chỉ số trích dẫn `[22]` bên cạnh `**(d) Thạch Lam**`.
  - Nguồn Trích Dẫn (L284): Thêm entry `[22] Thạch Lam. (1938). *Theo dòng* (Tiểu luận). Báo *Ngày nay*, số 157.` vào bảng.
- `paper_005.html`:
  - §1.1 (L262): Bổ sung liên kết trích dẫn `<a href="#nguon-22">[22]</a>` cạnh tên tác giả.
  - Table footer (L890): Thêm dòng HTML cho `<td id="nguon-22"><strong>[22]</strong></td>` và mô tả thư mục tác phẩm.
- `paper_005_for_pdf.md`:
  - §1.1 (L90): Bổ sung trích dẫn parenthetical `(Thạch Lam, 1938)` cạnh tên tác giả.
  - Tài liệu tham khảo (L329): Bổ sung mục lục trích dẫn tác phẩm dưới tiêu đề `**Nguồn nhận định phân tích:**`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung nguồn trích dẫn cho nhận định của Vũ Trọng Phụng · RCA 5.0/5

**Symptom:** Nhận định của Vũ Trọng Phụng `**(c) Vũ Trọng Phụng**` tại mục §1.1 văn bản nguồn trong các định dạng `paper_005.md`, `paper_005.html` và `paper_005_for_pdf.md` chưa được dẫn nguồn trích dẫn cụ thể.

**Root (Round 3):** Quá trình xây dựng văn bản nguồn cho bài viết chỉ thu thập đoạn trích dẫn nổi tiếng của Vũ Trọng Phụng từ kho tư liệu số hóa mà bỏ quên việc bổ sung chỉ số trích dẫn và định vị thư mục tác phẩm gốc (*Từ lý thuyết đến thực hành*, 1936), dẫn đến việc thiếu đồng bộ và hoàn thiện trong hệ thống Nguồn Trích Dẫn.

**Fix (3 files, 6 vị trí):**
- `paper_005.md`:
  - §1.1 (L33): Bổ sung chỉ số trích dẫn `[21]` bên cạnh `**(c) Vũ Trọng Phụng**`.
  - Nguồn Trích Dẫn (L283): Thêm entry `[21] Vũ Trọng Phụng. (1936). *Từ lý thuyết đến thực hành* (Truyện ngắn). Hà Nội.` vào bảng.
- `paper_005.html`:
  - §1.1 (L255): Bổ sung liên kết trích dẫn `<a href="#nguon-21">[21]</a>` cạnh tên tác giả.
  - Table footer (L887): Thêm dòng HTML cho `<td id="nguon-21"><strong>[21]</strong></td>` và mô tả thư mục tác phẩm.
- `paper_005_for_pdf.md`:
  - §1.1 (L86): Bổ sung trích dẫn parenthetical `(Vũ Trọng Phụng, 1936)` cạnh tên tác giả.
  - Tài liệu tham khảo (L328): Bổ sung mục lục trích dẫn tác phẩm dưới tiêu đề `**Nguồn nhận định phân tích:**`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung trích dẫn cho mô tả tiên đề Mạch Rễ như "mô tả cấu trúc của động lực quan hệ" · RCA 5.0/5

**Symptom:** Phát biểu mô tả bản chất của hệ tiên đề Mạch Rễ là "mô tả cấu trúc của động lực quan hệ (structural descriptions of relational dynamics)" trong mục §2.1 của các phiên bản paper_005 chưa được dẫn chiếu trực tiếp đến tài liệu đặc tả hệ tiên đề (`axiom_spec.md` [12]).

**Root (Round 3):** Quá trình chỉnh lý các câu văn giới thiệu phương pháp luận chỉ tập trung vào việc đối chiếu siêu hình học cổ điển phương Tây mà bỏ sót việc liên kết nguồn gốc cụ thể của các khái niệm mô tả cấu trúc về đặc tả Mạch Rễ với tệp SOT đặc tả hệ tiên đề được lưu trữ ở thư mục gốc, gây nên sự thiếu liên kết chặt chẽ trong hệ thống tài liệu tham khảo nội bộ.

**Fix (3 files, 3 vị trí):**
- `paper_005.md`:
  - §2.1 (L65): Bổ sung chỉ số trích dẫn `[12]` sau câu định nghĩa "...phân tán trong mạng".
- `paper_005.html`:
  - Phân loại khung nền (L220): Bổ sung liên kết trích dẫn `<a href="#nguon-12">[12]</a>` sau cụm từ `relational dynamics`.
- `paper_005_for_pdf.md`:
  - §2.1 (L118): Bổ sung trích dẫn parenthetical `(Mạch Rễ, 2026)` sau câu định nghĩa "...phân tán trong mạng".

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung trích dẫn cho khái niệm "triết học tương quan-phân tán" trong Phân loại khung nền · RCA 5.0/5

**Symptom:** Khái niệm "triết học tương quan-phân tán (Relational and Distributed Philosophy)" xuất hiện ở phần "Phân loại khung nền (Framework Classification)" của `paper_005.html` và trong §1.2 của `paper_005.md` & `paper_005.html` nhưng chưa được trích dẫn đầy đủ đến nguồn gốc thuyết tương quan (Dewey & Bentley) và thuyết phân tán (Hutchins).

**Root (Round 3):** Quá trình rà soát và gán nhãn trích dẫn ở các phiên bản trước đây chỉ thực hiện trên một số đoạn định nghĩa chính mà bỏ sót các đoạn giới thiệu khái quát và phân loại khung nền ở đầu tệp, dẫn đến việc phân phối trích dẫn inline không đồng đều và thiếu nhất quán giữa các tệp định dạng.

**Fix (2 files, 3 vị trí):**
- `paper_005.md`:
  - §1.2 (L53): Bổ sung chỉ số trích dẫn `[17, 18]` sau cụm từ `loại hình tương quan-phân tán`.
- `paper_005.html`:
  - Phân loại khung nền (L217): Bổ sung liên kết trích dẫn `<a href="#nguon-17">[17]</a>, <a href="#nguon-18">[18]</a>` sau cụm từ `Relational and Distributed Philosophy`.
  - §1.2 (L321): Bổ sung liên kết trích dẫn `<a href="#nguon-17">[17]</a>, <a href="#nguon-18">[18]</a>` sau cụm từ `tương quan-phân tán`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung trích dẫn cho khẳng định về cách phản bác "liệt kê thành tựu" tư tưởng Việt Nam · RCA 5.0/5

**Symptom:** Khẳng định "Các phản bác trước đây thường liệt kê thành tựu tư tưởng Việt Nam để chứng minh 'có triết học'" ở phần Tóm tắt (Abstract) của các định dạng paper_005 chưa được dẫn chiếu cụ thể đến các đại diện học thuật tiêu biểu đã được đưa vào phần tài liệu tham khảo (như Trần Văn Giàu và Nguyễn Tài Thư).

**Root (Round 3):** Quá trình xây dựng bản thảo định vị các nhận định phản bác này dưới dạng khái quát hóa hành vi học thuật phổ biến (general academic practice) mà bỏ quên việc tạo mối liên kết trực tiếp (inline citation coupling) với các tác phẩm tổng thuật lịch sử tư tưởng đồ sộ ở danh mục tham khảo, dẫn đến việc thiếu tính tường minh và liên kết nội bộ.

**Fix (3 files, 3 vị trí):**
- `paper_005.md`:
  - Tóm tắt (L11): Bổ sung chỉ số trích dẫn `[10, 11]` sau cụm từ `chứng minh "có triết học"`.
- `paper_005.html`:
  - Tóm tắt (L193): Bổ sung liên kết trích dẫn `<a href="#nguon-10">[10]</a>, <a href="#nguon-11">[11]</a>` sau cụm từ `chứng minh "có triết học"`.
- `paper_005_for_pdf.md`:
  - Abstract (L63): Bổ sung trích dẫn parenthetical `(Trần Văn Giàu, 1973; Nguyễn Tài Thư, 1993)` sau cụm từ `chứng minh "có triết học"`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung 2 ví dụ và trích dẫn cho "triết học hệ thống-siêu hình" · RCA 5.0/5

**Symptom:** Khái niệm "triết học hệ thống-siêu hình" (systematic metaphysics) là cột mốc đối chiếu lý thuyết chính trong paper_005 để làm nổi bật sự khác biệt về loại hình với "triết học tương quan-phân tán", nhưng bài viết chỉ nêu các truyền thống cổ đại (Hy Lạp, Ấn Độ, Trung Quốc) mà thiếu đi các ví dụ và trích dẫn kinh điển phương Tây hiện đại.

**Root (Round 3):** Biên soạn ban đầu chỉ dựa vào các hệ thống triết học cổ đại làm đại diện trực quan mà không mở rộng sang các hệ thống triết học hiện đại nổi bật của phương Tây, dẫn đến việc thiếu hụt các tài liệu tham khảo cốt lõi để củng cố vững chắc cho định nghĩa của "triết học hệ thống-siêu hình".

**Fix (3 files, 11 vị trí):**
- `paper_005.md`: 
  - Tóm tắt (L11): Bổ sung chỉ số trích dẫn `[19, 20]` cho cụm từ "triết học hệ thống-siêu hình".
  - §2.1 (L63): Bổ sung ví dụ Spinoza [19] và Hegel [20] và sửa chính tả "cổ diễn" thành "cổ điển".
  - §2.1 (L76 - bảng so sánh): Bổ sung Spinoza, Hegel vào cột ví dụ của Triết học Hệ thống-Siêu hình.
  - Nguồn Trích Dẫn (L278-281): Bổ sung entries `[19] Spinoza (1677)` và `[20] Hegel (1817)`.
- `paper_005.html`:
  - Tóm tắt (L203): Bổ sung liên kết trích dẫn `<a href="#nguon-19">[19]</a>, <a href="#nguon-20">[20]</a>` cho cụm từ "triết học hệ thống-siêu hình".
  - §2.1 (L339-345): Bổ sung tương đương với liên kết `<a href="#nguon-19">[19]</a>` và `<a href="#nguon-20">[20]</a>` và sửa lỗi chính tả "cổ diễn".
  - §2.1 (L403-408 - bảng so sánh): Bổ sung Spinoza, Hegel vào cột ví dụ.
  - Table footer (L866): Thêm dòng HTML cho `[19]` và `[20]`.
- `paper_005_for_pdf.md`:
  - Abstract (L63): Bổ sung trích dẫn parenthetical `(Spinoza, 1677; Hegel, 1817)` cho cụm từ "triết học hệ thống-siêu hình".
  - §2.1 (L116): Bổ sung tương đương với trích dẫn parenthetical `(Spinoza, 1677)` và `(Hegel, 1817)` và sửa lỗi chính tả "cổ diễn".
  - §2.1 (L129 - bảng so sánh): Bổ sung Spinoza, Hegel.
  - Tài liệu tham khảo (L346): Bổ sung mục lục trích dẫn dưới tiêu đề mới `**Triết học hệ thống - Siêu hình (Systematic Metaphysics):**`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Sửa đổi thuật ngữ Tiên đề III trong Abstract của paper_005.html · RCA 5.0/5

**Symptom:** Abstract của `paper_005.html` tại dòng 198 sử dụng cụm từ "Mạch Cội Dọc (Orthogonal Temporality)" để mô tả Tiên đề III, tạo nên sự không tương thích và nhập nhèm thuật ngữ.

**Root (Round 3):** Quá trình chuyển đổi và đồng bộ thủ công từ `.md` sang `.html` cho bài viết bị bỏ sót một vị trí trong Abstract, dẫn đến việc thuật ngữ biểu hiện ("Mạch Cội Dọc") bị ghép sai với thuật ngữ bản chất ("Orthogonal Temporality") thay vì dùng đúng "Mạch Cội Nguồn", vi phạm quy định phân cấp từ vựng tại `CLAUDE.md`.

**Fix (1 file, 1 vị trí):**
- `paper_005.html`: Thay thế "Mạch Cội Dọc (Orthogonal Temporality)" bằng "Mạch Cội Nguồn (Orthogonal Temporality)" tại dòng 198.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung nguồn trích dẫn cho khái niệm "triết học tương quan-phân tán" · RCA 5.0/5

**Symptom:** Khái niệm phân loại "triết học tương quan-phân tán" (relational and distributed philosophy) là trụ cột lý thuyết cốt lõi của paper_005 để phân định loại hình tư duy Việt Nam và Mạch Rễ, nhưng bài viết chưa có trích dẫn học thuật liên kết với hai nguồn nền tảng tạo dựng nên hai trụ cột này: Bản thể học tương quan (Dewey & Bentley, 1949) và Nhận thức luận phân tán (Hutchins, 1995).

**Root (Round 3):** Khái niệm "tương quan-phân tán" ban đầu được định nghĩa như một nhãn phân loại nội tại của dự án (mã hóa bằng thẻ `[project interpretation]`) mà không hoàn trả nguồn dẫn (back-propagation) đến các cơ sở học thuật ngoại lai nguyên thủy hỗ trợ độc lập cho các cấu phần cốt lõi của nó, dẫn đến việc thiếu hụt trích dẫn gốc trong thư mục.

**Fix (3 files, 6 vị trí):**
- `paper_005.md`: Bổ sung trích dẫn inline `[17, 18]` tại Tóm tắt (L11), §1.2 (L53), và §2.1 (L65); bổ sung entries `[17] Dewey & Bentley (1949)` và `[18] Hutchins (1995)` vào bảng Nguồn Trích Dẫn.
- `paper_005.html`: Bổ sung liên kết trích dẫn `<a href="#nguon-17">[17]</a>, <a href="#nguon-18">[18]</a>` tại các vị trí tương đương; bổ sung 2 entries vào footer table.
- `paper_005_for_pdf.md`: Bổ sung trích dẫn inline `(Dewey & Bentley, 1949; Hutchins, 1995)` tại các vị trí tương ứng; bổ sung 2 entries vào danh mục tham khảo dưới mục mới `**Triết học Tương quan - Phân tán (Relational and Distributed Philosophy):**`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung nguồn trích dẫn cho khái niệm "lỗi phạm trù" (category error) · RCA 5.0/5

**Symptom:** Khái niệm "lỗi phạm trù" (category error) là chẩn đoán học thuật then chốt xuyên suốt paper_005 để chỉ ra sự lệch pha khi dùng thước đo siêu hình học phương Tây để đánh giá triết học tương quan Việt Nam. Tuy nhiên, bài viết chưa có trích dẫn chính thức đến tác phẩm gốc của Gilbert Ryle (1949).

**Root (Round 3):** Quá trình biên soạn và chỉnh lý trước đây chỉ tập trung vào việc áp dụng hệ tiên đề Mạch Rễ và thu thập dữ liệu so sánh (Yoruba, Ubuntu, Ca dao), bỏ sót việc chuẩn hóa thư mục cho các khái niệm triết học phân tích kinh điển bên ngoài được mượn làm khung đối chiếu, dẫn đến sự thiếu hụt nguồn sơ cấp trong Nguồn Trích Dẫn.

**Fix (3 files, 4 vị trí):**
- `paper_005.md`: Bổ sung trích dẫn inline `[16]` tại Tóm tắt (L11), §1.2 (L53), §3.1 (L92); bổ sung entry `[16] Ryle, G. (1949). *The Concept of Mind*. London: Hutchinson.` vào bảng Nguồn Trích Dẫn (L277).
- `paper_005.html`: Bổ sung trích dẫn inline `<a href="#nguon-16">[16]</a>` tại các vị trí tương ứng; bổ sung entry `[16]` vào bảng Nguồn Trích Dẫn (L866).
- `paper_005_for_pdf.md`: Bổ sung trích dẫn inline `(Ryle, 1949)` tại các vị trí tương ứng; bổ sung entry vào danh mục Tài liệu tham khảo dưới mục mới `**Lỗi phạm trù (Category error):**`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Chuẩn hóa canonical terms Tiên Đề III (Mạch Cội Nguồn / Mạch Cội Dọc) · RCA 5.0/5

**Symptom:** Abstract + headings + summary labels trong 4 file paper_005 dùng "Mạch Cội Dọc (Orthogonal Temporality)" — ánh xạ sai: "Mạch Cội Dọc" = biểu hiện (Vertical Temporality), không phải bản chất (Orthogonal Temporality). Body prose đã phân biệt đúng hai tầng (Thời gian trực giao ≠ Thời gian chiều dọc) nhưng headings/labels chưa được back-propagate sau khi canonical terms được khóa trong CLAUDE.md.

**Root (Round 3):** Paper được viết trước khi canonical Vietnamese terms được finalize (RCA findings 2026-06-05 → 2026-06-09). Body prose dùng internal explanatory convention ("Thời gian trực giao" = essence, "Thời gian chiều dọc" = manifestation) — đúng về mặt giải thích nhưng headings/labels dùng "Mạch Cội Dọc" làm primary identifier cho Orthogonal Temporality → category error.

**Fix (4 files, 16 vị trí):**

| File | Vị trí | Trước → Sau |
|------|--------|-------------|
| `paper_005.md` | Abstract L11 | `Mạch Cội Dọc (Orthogonal Temporality)` → `Mạch Cội Nguồn (Orthogonal Temporality)` |
| | Heading L148 | `Mạch Cội Dọc — Mạch Cội Nguồn` → `Mạch Cội Nguồn (Orthogonal Temporality) — Biểu hiện: Mạch Cội Dọc (Vertical Temporality)` |
| | Body L150 | `Mạch Cội Dọc — Mạch Cội Nguồn ("Orthogonal Temporality")` → `Mạch Cội Nguồn (Orthogonal Temporality) — với biểu hiện... Mạch Cội Dọc (Vertical Temporality)` |
| | Summary L242 | `Tiên Đề III — Mạch Cội Dọc:` → `Tiên Đề III — Mạch Cội Nguồn (Orthogonal Temporality):` |
| `paper_005.html` | Abstract L198 | `Mạch Cội Dọc (Orthogonal Temporality)` → `Mạch Cội Nguồn (Orthogonal Temporality)` |
| | Heading L567 | Như .md L148 |
| | Body L569 | Như .md L150 |
| | Summary L767 | `Tiên Đề III — Mạch Cội Dọc:` → `Tiên Đề III — Mạch Cội Nguồn (Orthogonal Temporality):` |
| | Table L928 | `Mạch Cội Dọc — Mạch Cội Nguồn` → `Mạch Cội Nguồn — Mạch Cội Dọc` (essence first) |
| `paper_005_for_pdf.md` | Abstract L63 | Như .md L11 |
| | Heading L203 | Như .md L148 |
| | Body L205 | Như .md L150 |
| | Summary L305 | Như .md L242 |
| | Table L375 | Như .html L928 |
| `draft/paper_005_draft_v1.md` | Heading L254 | `Tiên đề III — Mạch Cội Dọc:` → `Tiên đề III — Mạch Cội Nguồn (Orthogonal Temporality) — Biểu hiện: Mạch Cội Dọc (Vertical Temporality):` |
| | Body L256 | `Mạch Cội Dọc (Vertical / Orthogonal Temporality)` → `Mạch Cội Nguồn (Orthogonal Temporality) — với biểu hiện... Mạch Cội Dọc (Vertical Temporality)` |
| | Summary L363 | `Tiên đề III:` → `Tiên đề III — Mạch Cội Nguồn (Orthogonal Temporality):` |

**Không đụng:** Body prose giữ nguyên — internal explanatory convention "Thời gian trực giao / Thời gian chiều dọc" đã đúng, chỉ sửa canonical term mapping trong headings/labels/tables.

**Carry-Forward Set:** Toàn bộ body prose, citation markers [1]–[15], evidence sections (Yoruba, Ubuntu, Ca dao, Mệnh Đề F), Bảng Nguồn Trích Dẫn — không đổi.

**RCA score:** 5.0/5 (Correct: 1 — real category error; Deep: 1 — root = no back-propagation pass; Feasible: 1 — safe terminology swap; Conflict-risk: 1 — consistent with CLAUDE.md canonical terms; Preservation: 1 — body prose and evidence unchanged)

---

## 2026-06-10 — TỔNG KẾT: Đại tu paper_005 + Hạ tầng papers/ · RCA 4.9/5 (session)

**Phạm vi:** 6 commits, 10 files changed. **Paper_005 portion** (A1–A7) logged here; **papers/ infrastructure portion** (B1–B6) logged in [`CHANGELOG_papers.md`](../CHANGELOG_papers.md).

### A. paper_005 — Sync codebase mới (3 evidence + citation system)

| # | Thay đổi | § | RCA |
|---|----------|---|-----|
| A1 | Yoruba *ìwà* [13] + Ubuntu [15] — hội tụ độc lập relational ontology | §4.1 | 5.0 |
| A2 | Ca dao biến dịch [14] + Phan Ngọc [3] — convergent evidence "Càng thắm thì lại càng phai" | §4.2 | 4.8 |
| A3 | Mệnh Đề F [12] — giải thích cấu trúc vì sao bản sắc Việt không tan rã (A∧B∧C chưa đồng thời) | §4.3 | 4.8 |
| A4 | 12 inline `[N]` citation markers toàn bài — [1]–[15] | all | 4.8 |
| A5 | Bảng Nguồn Trích Dẫn APA [1]–[15] thay TÀI LIỆU THAM KHẢO | footer | 5.0 |
| A6 | HTML: `<a href="#nguon-N">[N]</a>` hyperlinks + `id="nguon-N"` anchors | all | 5.0 |
| A7 | Fix nguồn văn bản: Wikipedia → "tổng hợp anonymous" | footer | 5.0 |

### Citation table [1]–[15] (final)

| # | Nguồn | Mới? |
|---|-------|------|
| [1] | Cadière (1958) | |
| [2] | Đào Duy Anh (1938) | |
| [3] | Phan Ngọc (2000) | |
| [4] | Ashby (1956) | |
| [5] | Weick (1995) | |
| [6]–[9] | Hountondji, Wiredu, Matilal, Oruka | |
| [10]–[11] | Trần Văn Giàu, Nguyễn Tài Thư | |
| [12] | Mạch Rễ `axiom_spec.md` | |
| [13] | Peel (2000) — Yoruba | ✅ |
| [14] | Nguyễn Tấn Long & Phan Canh (1969) — Ca dao | ✅ |
| [15] | Udah et al. (2025) — Ubuntu | ✅ |

### Paper_005 files changed (7)

`papers/paper_005/paper_005.md`, `papers/paper_005/paper_005.html`, `papers/paper_005/paper_005_for_pdf.md`, `papers/paper_005/draft/paper_005_draft_v1.md`, `papers/paper_005/plan/paper_005_plan.md`

> Cross-ref: Infrastructure portion (B1–B6) — `CHANGELOG_papers.md`, `CLAUDE.md`, `papers/index.html`, `deploy-pages.yml`, `papers/CLAUDE_REF.md` deleted → logged in [`CHANGELOG_papers.md`](../CHANGELOG_papers.md).

---

## 2026-06-10 — paper_005.md + paper_005.html — Sync codebase mới + Bảng Nguồn Trích Dẫn [1]–[15] · RCA 4.8/5

**Symptom:** Paper 005 thiếu ba evidence mới từ codebase (Yoruba *ìwà* [13], ca dao biến dịch [14], Mệnh Đề F [12]), chưa có inline `[N]` citation markers, và TÀI LIỆU THAM KHẢO chưa có bảng Nguồn Trích Dẫn đánh số APA.

**Root:** Paper viết trước khi Yoruba evidence, ca dao convergent discovery, Mệnh Đề F, và Rule #12 (Citation Table) được thêm vào codebase.

**Fix — 5 nhóm:**
1. §4.1 — Yoruba *ìwà* [13] + Ubuntu [15]
2. §4.2 — Ca dao biến dịch [14] + Phan Ngọc [3]
3. §4.3 — Mệnh Đề F structural explanation [12]
4. 12 inline `[N]` citation markers toàn bài
5. Bảng Nguồn Trích Dẫn [1]–[15] APA + HTML hyperlink anchors

**Files:** `papers/paper_005/paper_005.md`, `papers/paper_005/paper_005.html`
**RCA:** 4.8/5 (Correct 5 · Deep 5 · Feasible 4 · Conflict-risk 5 · Preservation 5)

---

## 2026-06-10 — paper_005 — Thêm tự phân loại Mạch Rễ (Framework Classification) · RCA 5.0/5

**Symptom:** Paper 005 dùng Mạch Rễ để chẩn đoán "lỗi phạm trù" (đánh giá triết học tương quan-phân tán bằng thước đo hệ thống-siêu hình) nhưng không tự tuyên bố Mạch Rễ thuộc loại hình nào. Vi phạm Tiên Đề VIII.

**Fix:** Thêm Framework Classification vào Abstract và §2.1 — Mạch Rễ là triết học tương quan-phân tán, không phải hệ thống-siêu hình. Neo vào Tiên Đề I + VIII.

**Files:** `papers/paper_005/paper_005.html`, `papers/paper_005/paper_005.md`, `papers/paper_005/paper_005_for_pdf.md`
**RCA:** 5.0/5 · Plan: `plan/paper_005_self_classification_plan.md`

---

## 2026-06-08 — paper_005 — Sync Tiên Đề III theo `axiom_spec.md` · RCA 5/5

**Symptom:** Paper 005 dùng tên Tiên Đề III cũ, chưa nhất quán với nguồn chân lý `axiom_spec.md`.

**Fix:**
- Abstract: "Mạch Cội Dọc" → "Mạch Cội Nguồn" (bản chất)
- §4.3 header + phát biểu: cập nhật canonical name + thêm claim "mạch tồn tại / ontological dimension"

**Files:** `papers/paper_005/paper_005.md`, `papers/paper_005/paper_005.html`
**RCA:** 5/5

---

## 2026-06-07 — paper_005 — Bổ sung bảng giải thích nhãn phân loại học thuật (RCA) · RCA 5/5

**Symptom:** Paper 005 dùng các nhãn `[established scholarship]`, `[contested scholarship]`, `[project interpretation]`, `[analogy]`, `[hypothesis]` nhưng chưa có bảng giải thích ý nghĩa cho người đọc.

**Fix:** Thêm chương "Ý NGHĨA CÁC NHÃN PHÂN LOẠI HỌC THUẬT (RCA)" cuối paper, kèm bảng 5 nhãn với giải thích học thuật + trực quan (trình độ học sinh cấp 3) + ví dụ cụ thể trong bài.

**Files:** `papers/paper_005/paper_005.md`, `papers/paper_005/paper_005.html`, `papers/paper_005/paper_005.pdf`
**RCA:** 5/5

---

> **Ghi chú:** Toàn bộ paper_005 entries đã được di chuyển từ [`CHANGELOG_papers.md`](../CHANGELOG_papers.md) sang đây (2026-06-11). Từ nay, mọi thay đổi cho file trong `papers/paper_005/` **chỉ** ghi vào file này — không ghi song song vào `CHANGELOG_papers.md`.

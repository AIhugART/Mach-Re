# Changelog — Papers (Mạch Rễ)

> **Phạm vi:** Nơi **duy nhất** ghi nhận thay đổi cho các file trong `papers/`. Không ghi paper changes vào `CHANGELOG.md` gốc.
> **Liên kết:** Lịch sử toàn bộ dự án (axiom, HTML nodes, audit, evidence) → xem [`CHANGELOG.md`](../CHANGELOG.md) tại thư mục gốc.
> **Quy tắc:** Mỗi entry phải qua 3-round RCA × 5-Why × scoring gate ≥ 4/5 (theo `CLAUDE.md` §RULE ZERO).

## 2026-06-11 — Phase 7 completion: paper_009 title V4 fix · RCA 4.4/5

**Triple compass:** A (Phan Ngọc) — title is the paper's public face; "Giao Diện Sống" imports computer-interface frame, failing Việt hóa rule 1. B (Ashby) — Requisite Variety: body already uses canonical names, title was the single stale artifact. C (Buddhist epistemology) — Pramāṇa: a title that doesn't match the framework's own naming standard is deceptive at the point of first contact.

**RCA R3 (root):** Title was set before Phase 1b naming RCA completed (2026-06-11). Body text (written after Phase 1b) already uses "Gặp Nhau Giữ Gốc — Không Của Ai, Nhờ Cả Hai" in §3.2 — title was the lone stale artifact.

**Scoring: 4.4/5** → fix (Correct 4, Deep 4, Feasible 5, Conflict-risk 4 [papers/index.html sync], Preservation 5).

**Files sửa:**
- `papers/paper_009/paper_009_draft.md` line 5: `"Giao Diện Sống"` → `"Gặp Nhau Giữ Gốc (Living Interface)"`
- `papers/index.html` line 267: same title fix (tiered routing exception — this is a papers-scope change affecting the papers index, recorded here)

**Phase 7 deliverable status:** paper_009_draft.md is fully v3.2-compliant — ESP Layer E ✓, Boundary Statement ✓, graded C1 ✓, canonical names in body ✓, epistemic marks ✓, falsification conditions ✓, APA citation table ✓, author metadata ✓. No further Phase 7 work required.

---


## 2026-06-11 — Phase 8c: paper_009 thuần-Việt gloss "nhận thức luận (mạch biết)" · RCA 4.8/5

Part of naming RCA (la bàn Phan Ngọc): "nhận thức luận" → thuần-Việt gloss "mạch biết" (4.8/5).
- `paper_009_draft.md` line 94: "nhận thức luận (mạch biết)"

> Cross-ref tầng root: dictionary_rule.md §4 canonical gloss table + axiom_9.html + axiom_spec.md → logged in [`CHANGELOG.md`](../CHANGELOG.md).

---

## 2026-06-11 — Phase 8a: paper_009 V4 name fix "Gặp Nhân" → "Gặp Nhau" · RCA 5.0/5

**Symptom:** `paper_009_draft.md` dùng "Gặp Nhân Giữ Gốc" (Phase 7 viết theo session summary lỗi) thay vì canonical "Gặp Nhau Giữ Gốc" từ `dictionary_rule.md §9`. Gloss đi kèm cũng sai: "gặp người khác" → phải là "gặp nhau, reciprocal".

**RCA R3 (root):** V4 rule không được kiểm tra tại Phase 7. "Nhau" = hai hệ gặp lẫn nhau (inter-system reciprocal) — đúng ngữ nghĩa IX; "Nhân" = người — sai phạm trù.

**Scoring: 5.0/5** → fix.

**Files sửa:**
- `papers/paper_009/paper_009_draft.md` line 78: `"Gặp Nhân Giữ Gốc"` → `"Gặp Nhau Giữ Gốc"` + gloss "gặp người khác" → "gặp nhau, reciprocal"
- `papers/paper_009/paper_009_draft.md` line 200: `Gặp Nhân Giữ Gốc` → `Gặp Nhau Giữ Gốc`

> Cross-ref tầng root: `axiom_spec.md` + `index.html` + CHANGELOG entry → logged in [`CHANGELOG.md`](../CHANGELOG.md) (Phase 8a).

---

## 2026-06-11 — paper_009 (TẠO MỚI): "Ngoại Giao Cây Tre như Giao Diện Sống" · ESP E 4.8/5 + RCA 4.8/5

**ESP Layer E (bắt buộc trước prose — Tier 3 Rule #1):**
- L1–L4 RCA Stack: Bamboo Diplomacy thiếu formal structural account → Việt Nam-VIII + US-chưa-VIII → C1-min → P* = identity-preserving inter-system encounter. IX formalize gap này.
- Claim Ladder: **Interpretive Mapping [interpretation]** — an toàn, rõ ràng definitions.
- Boundary Statement in §2: NOT-claim / CLAIM list explicit.
- Score E: 4.8/5 → proceed to prose.

**Files tạo:**
- `papers/paper_009/paper_009_draft.md` — full prose paper (bilingual VI/EN)
- `papers/index.html` — Paper 009 card added (purple #5a3070)

**Routing tiered changelog:** ONLY `papers/CHANGELOG_papers.md`. Root `CHANGELOG.md` không nhận entry này.

**RCA score: 4.8/5.** Phase 7 → COMPLETE.

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

**Symptom:** Định nghĩa khái niệm `“triết học hệ thống-siêu hình (systematic metaphysics)”` tại mục §2.1 của các định dạng `paper_005.md`, `paper_005.html`, `paper_005_for_pdf.md` và `draft/paper_005_draft_v1.md` chưa được dẫn nguồn trích dẫn đến các tác giả và tác phẩm làm căn cứ định nghĩa (Hountondji, Spinoza, Hegel).

**Root (Round 3):** Quá trình biên tập bản thảo chỉ gắn nhãn phân loại học thuật nội bộ `` `[project interpretation]` `` ở phần định nghĩa lý thuyết mà bỏ quên việc đặt các chỉ số dẫn nguồn quy chiếu thực tế (inline citation) tương ứng với danh mục thư mục tác phẩm ở cuối tài liệu (các nguồn `[6]`, `[19]`, `[20]`), dẫn đến tính thiếu thuyết phục về mặt căn cứ học thuật cho định nghĩa.

**Fix (4 files, 4 vị trí):**
- `paper_005.md`: Bổ sung chỉ số trích dẫn `[6, 19, 20]` và chuyển nhãn học thuật thành `[established scholarship]`: `đào tạo kinh viện [6, 19, 20] (`[established scholarship]`).`
- `paper_005.html`: Bổ sung các liên kết trích dẫn `<a href="#nguon-6">[6]</a>, <a href="#nguon-19">[19]</a>, <a href="#nguon-20">[20]</a>` và chuyển nhãn học thuật thành `[established scholarship]`.
- `paper_005_for_pdf.md`: Bổ sung các trích dẫn parenthetical `(Hountondji, 1983; Spinoza, 1677; Hegel, 1817)` và chuyển nhãn học thuật thành `[established scholarship]`.
- `draft/paper_005_draft_v1.md`: Bổ sung các trích dẫn parenthetical `(Hountondji, 1983; Spinoza, 1677; Hegel, 1817)` và chuyển nhãn học thuật thành `[established scholarship]`.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — paper_005: Bổ sung nguồn trích dẫn cho nhận định về việc các văn bản còn lưu không thể hiện nỗ lực đào sâu siêu hình học · RCA 5.0/5

**Symptom:** Nhận định `“các văn bản còn lưu không thể hiện nỗ lực đào sâu siêu hình học”` tại mục §1.2 một mâu thuẫn cần giải quyết trong các định dạng `paper_005.md`, `paper_005.html`, `paper_005_for_pdf.md` và `draft/paper_005_draft_v1.md` chưa được liên kết trực tiếp (inline citation) đến nguồn Wikipedia tương ứng (đã đăng ký ở danh mục thư mục tác phẩm).

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

**Symptom:** Nhận định `“Tư tưởng triết học Việt Nam là bản sao chép rời rạc mang tính giáo điều thiếu sáng tạo, là sự thu nhỏ của triết học Ấn Độ và Trung Quốc.”` tại mục §1.1 văn bản nguồn trong các định dạng `paper_005.md`, `paper_005.html` và `paper_005_for_pdf.md` chưa được dẫn nguồn trích dẫn cụ thể.

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

**Symptom:** Nhận định `“Không có sáng tạo, chỉ có vay mượn; chỉ có áp dụng, chỉ có thích nghi. Đó là sự thật của lịch sử tư tưởng chính thống Đại Việt.”` tại mục §1.1 văn bản nguồn trong các định dạng `paper_005.md`, `paper_005.html` và `paper_005_for_pdf.md` chưa được dẫn nguồn trích dẫn cụ thể.

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
  - Tóm tắt (L193): Bổ sung liên kết trích dẫn `<a href="#nguon-10">[10]</a>, <a href="#nguon-11">[11]</a>` sau cụm từ `chứng minh “có triết học”`.
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

## 2026-06-10 — TỔNG KẾT: Đại tu paper_005 + Hạ tầng papers/ · RCA 4.9/5 (session)

**Phạm vi:** 6 commits, 10 files changed.

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

### B. Hạ tầng papers/

| # | Thay đổi | RCA |
|---|----------|-----|
| B1 | Tạo `CHANGELOG_papers.md` — changelog riêng cho papers | 4.8 |
| B2 | Di chuyển 5 paper entries từ `CHANGELOG.md` → `CHANGELOG_papers.md` (exclusive) | 5.0 |
| B3 | Cập nhật `CLAUDE.md` Document Contract Rules: paper changes → chỉ `CHANGELOG_papers.md` | 5.0 |
| B4 | Link `CHANGELOG_papers.md` từ `papers/index.html` footer | — |
| B5 | Xóa `papers/CLAUDE_REF.md` — file CLAUDE.md của dự án VVV-QMRF (không liên quan) | 5.0 |
| B6 | Fix `deploy-pages.yml` — thêm `papers/**` vào paths trigger | 5.0 |

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

### Files changed (10)

`papers/paper_005/paper_005.md`, `papers/paper_005/paper_005.html`, `papers/CHANGELOG_papers.md`, `papers/index.html`, `CHANGELOG.md`, `CLAUDE.md`, `.github/workflows/deploy-pages.yml` (+ `papers/CLAUDE_REF.md` deleted)

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

## 2026-06-07 — paper_003 — Thêm Bảng Giải Thích Thuật Ngữ (Glossary) · RCA 5/5

**Symptom:** Paper 003 dùng nhiều thuật ngữ chuyên môn (Bản thể học liên chủ thể, Mạch cội nguồn, Bất biến cấu trúc…) nhưng chưa có định nghĩa đơn giản hóa cho độc giả phổ thông.

**Fix:** Thêm bảng glossary cuối bài, trước tài liệu tham khảo. Mỗi thuật ngữ kèm giải thích ở trình độ học sinh cấp 3.

**Files:** `papers/paper_003/paper_003_draft.md`
**RCA:** 5/5

---

## 2026-06-07 — paper_005 — Bổ sung bảng giải thích nhãn phân loại học thuật (RCA) · RCA 5/5

**Symptom:** Paper 005 dùng các nhãn `[established scholarship]`, `[contested scholarship]`, `[project interpretation]`, `[analogy]`, `[hypothesis]` nhưng chưa có bảng giải thích ý nghĩa cho người đọc.

**Fix:** Thêm chương "Ý NGHĨA CÁC NHÃN PHÂN LOẠI HỌC THUẬT (RCA)" cuối paper, kèm bảng 5 nhãn với giải thích học thuật + trực quan (trình độ học sinh cấp 3) + ví dụ cụ thể trong bài.

**Files:** `papers/paper_005/paper_005.md`, `papers/paper_005/paper_005.html`, `papers/paper_005/paper_005.pdf`
**RCA:** 5/5

---

> **Ghi chú:** Toàn bộ paper entries đã được di chuyển từ [`CHANGELOG.md`](../CHANGELOG.md) sang đây (2026-06-10). Từ nay, mọi thay đổi cho `papers/` **chỉ** ghi vào file này — không ghi song song vào `CHANGELOG.md` gốc.

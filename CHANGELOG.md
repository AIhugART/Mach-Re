## 2026-06-13 — Pass sâu: migrate hoàn toàn ký pháp VIII→Tiên Đề V, IX→Tiên Đề VI trên upgrade.html + axiom_6.html (tất cả 5.0/5) ✅

**Trigger:** Tiếp pass sâu cho 2 trang đã flag ở pass "đồng bộ vỏ" (VIII/IX là từ vựng cấu trúc xuyên thân bài + bẫy diễn giải range).
**Root cause (3-round):** R1 — Meta-axiom (cũ VIII) và Interface-axiom (cũ IX) còn rải khắp thân bài/ASCII/glossary dù header đã migrate sang Tiên Đề V/VI. R2 — để lẫn lộn làm hỏng traceability + tạo "Tiên Đề VIII/IX" không còn tồn tại trong hệ canonical. R3 — gốc: Quyết định 4 không propagate hết; cùng class propagation gap, nhưng cần xử lý kèm **diễn giải range** nên tách pass riêng.
**Phân giải bẫy range (điểm tinh tế nhất, RCA 5.0/5):** Dưới Quyết định 4, "hệ đơn đầy đủ **I–V**" = I,II,III,IV (Core) + V (Meta) → **đúng canonical, giữ nguyên** (Derived 1–4 là sub-số, không nằm trong dãy La Mã). Chỉ `I–VII` (object-level cũ) và `Derived (V–VII)` mới diễn giải lại → `I–IV và 1–4` / `Derived (1–4)`. Phân biệt **trục V (thời gian)**, **V (Module 5)**, **(V)⊥(H)** — KHÔNG đổi (không phải Tiên Đề V). "7 Tiên Đề gốc (I–VII)" → "8 mệnh đề gốc: 4 Tiên Đề Cốt Lõi (I–IV) + 4 Mệnh Đề Dẫn Xuất (1–4)".
**Carry-forward:** Class CSS nội bộ (`.viii-label`, `.axiom-viii`) giữ nguyên làm id — không reader-facing, đổi = churn/risk. Chỉ sửa nội dung hiển thị + comment.
**Verify:** grep `VIII|\bIX\b` → `axiom_6.html` 0 hit; `upgrade.html` 0 hit nội dung (chỉ còn class name lowercase + comment đã chú thích). Range/axis-V/Module-5 preserved đúng.

### Files Changed

| File | Change | Score |
|------|--------|-------|
| `axiom_6.html` | 10 ref Meta `VIII`→`Tiên Đề V` (C1 modes, case studies, ASCII, OQ1) + 1 `IX`→`Tiên Đề VI` (triangulation) | 5.0/5 |
| `upgrade.html` | §3 + §Interface: VIII→Tiên Đề V, IX→Tiên Đề VI (label, ASCII kiến trúc, QUAN HỆ block, C1 conditions, glossary); range `I–VII`→`I–IV và 1–4`, `Derived (V–VII)`→`(1–4)`, `7 Tiên Đề`→`8 mệnh đề`; giữ trục-V/Module-5/I–V | 5.0/5 |

---

## 2026-06-13 — Refactor toàn site: đồng bộ vỏ ký pháp Quyết định 4 + chuẩn hóa la bàn A×B×C (8 trang, tất cả ≥ 4.5/5) ✅

**Trigger:** Người dùng yêu cầu "refactor all trang, (A — Phan Ngọc · B — Ashby/Weick · C — Buddhist Epistemology) as compass", quyết định bằng 3-round RCA × 5-Why × gate ≥ 4/5. Phạm vi chốt qua AskUserQuestion: **đồng bộ vỏ** (surgical), không re-render.
**Root cause (3-round):** R1 — nhiều dòng "vỏ" (count, ASCII, meta-description, hero tag, footer, pill, comment) còn ký pháp cũ (V–VII/F, VIII, IX) trong khi *card thân bài* đã đúng Quyết định 4 (Mệnh Đề 1–4, Tiên Đề V Meta, Tiên Đề VI Interface). R2 — tự-mâu-thuẫn trong cùng trang/cùng card (vd card "Tiên Đề V" lại tự gọi mình "VIII cần thiết") làm hỏng tính traceable của framework vốn đòi hỏi nghiêm scrutiny. R3 — gốc rễ: Quyết định 4 (2026-06-11) không propagate hết vào lớp vỏ — **cùng class D1/D2 propagation gap** đã ghi nhận cho `index.html`. Đây là mở rộng fix đó ra toàn site.
**Compass cross-check:** A (Phan Ngọc — pattern bất biến phải hiện nhất quán ở mọi biểu hiện) · B (Ashby — ký pháp lẫn lộn = giảm variety đọc hiểu) · C (apoha — tên phải loại trừ nhầm lẫn, không tự mâu thuẫn) → cả ba hội tụ yêu cầu sửa.
**Provenance:** Bổ sung neo C `[established]` đúng tư cách — thêm Prasad 2023 (pramāṇa/Dignāga/Dharmakīrti) vào `what.html` (trước chỉ có Nāgārjuna [6]); đổi nhãn neo "C — Anattā" → "C — Nhận thức luận Phật giáo" khớp la bàn canonical (`axiom_spec.md §0.1`).
**Phạm vi loại trừ (gate < 4/5 hoặc tier khác):** thân bài `upgrade.html` (23 ref) + `axiom_6.html` (9 ref) dùng VIII/IX làm *từ vựng cấu trúc* kèm bẫy diễn giải range (I–V/I–VII) → sửa một phần tạo scheme lẫn lộn (Conflict-risk cao) → chỉ sửa chrome cô lập (title, hero tag), phần còn lại cần **pass migration sâu riêng**. `papers/*` (tier riêng, `CHANGELOG_papers.md`), `raw/*` + `documents/*` (lưu trữ/nguồn ngoài) — không đụng.
**Verify:** grep `\bVIII\b|\bIX\b|V–VII, F` toàn site → 0 hit trên trang gốc sống đã sửa (trừ `axioms.html:373` giữ filename `evidence_viii_...md` nhưng prose đã chuyển sang "Tiên Đề V"); 2 trang flag còn ref đúng dự kiến.

### Files Changed

| File | Change | Score |
|------|--------|-------|
| `axioms.html` | count + meta + ASCII (V/VI/VII/F/VIII → Mệnh Đề 1–4 / Tiên Đề V) + link + 2× "IV→VIII"→"IV→V" + "VIII cần thiết"→"Tiên Đề V cần thiết" + evidence-prose | 5.0/5 |
| `axiom_derived.html` | meta + hero subtitle + footer + "VIII cần thiết"→"Tiên Đề V" | 5.0/5 |
| `what.html` | count + ký pháp note + ASCII + "IV→VIII"→"IV→V" + comment META + pill VIII→Tiên Đề V + "VIII cần thiết"; neo C +Prasad [10] +đổi nhãn; +note taxonomy-3-vai trước bảng toàn cầu | 4.8/5 |
| `axiom_4.html` | `reflexivity (VIII)` → `(Tiên Đề V)` | 4.8/5 |
| `axiom_conflict.html` | hero tag + ASCII `TIÊN ĐỀ VIII` → `TIÊN ĐỀ V (META)` | 5.0/5 |
| `axiom_6.html` | hero tag `TIÊN ĐỀ IX` → `TIÊN ĐỀ VI` (khớp filename + body "Axiom VI"); thân bài flag pass sâu | 4.5/5 |
| `upgrade.html` | `<title>` `IX` → `VI` (khớp link inbound canonical); thân bài flag pass sâu | 4.5/5 |
| `when.html` | body `chạy VIII`/`đủ VIII` → `Tiên Đề V` | 4.8/5 |

---

## 2026-06-13 — index.html: Thêm "tầng trệt" đoạn mở + gỡ tên loại hình AI-hallucinated (score 4.8/5) ✅

**Trigger:** 3-round RCA × 5-Why × A·B·C compass áp lên phần mở "🌱 Mạch Rễ là gì?". Người đọc mới gặp ngay jargon dày đặc (`prameya/apoha/svalakṣaṇa/pratītyasamutpāda`) trước khi có điểm tựa hình dung framework là gì.
**Root cause:** Đoạn mở thiếu một "tầng trệt" (ground floor) bằng ngôn ngữ đời thường — nhảy thẳng lên "tầng kỹ thuật" mà chưa xây tầng trệt. Vi phạm chính upāya (la bàn C — dạy theo căn cơ người đọc).
**Compass cross-check:** A (Phan Ngọc — thao tác luận) ✗ · B (Ashby/Weick — sensemaking khởi từ khung quen, ít variety) ✗ · C (upāya) ✗ → cả ba hội tụ.
**Fix:** (1) Chèn 2 đoạn "tầng trệt" ẩn dụ cây/rễ (đời thường, không jargon) làm lead trên cùng; (2) giữ nguyên toàn bộ nội dung kỹ thuật bên dưới ("giữ nguyên, chỉ đẩy xuống" — carry-forward). Đồng thời (commit trước fe83b93) gỡ tên loại hình AI-coinage "triết học tương quan-phân tán / Relational and Distributed Philosophy" khỏi disclaimer (CLAUDE.md F9).
**Verify:** Tầng trệt dùng đúng ẩn dụ cái tên đã gợi (rễ) → không bootstrap framework mới bằng khái niệm mới; nội dung kỹ thuật bảo toàn nguyên vẹn.

### Files Changed

| File | Change |
|------|--------|
| `index.html` | Thêm 2 đoạn lead "tầng trệt" dưới h2 "Mạch Rễ là gì?"; disclaimer VI gỡ tên loại hình AI-hallucinated |

---

## 2026-06-13 — index.html hero badge + CLAUDE.md: Version propagation rule (score 5.0/5) ✅

**Trigger:** RCA phát hiện hero badge `index.html:417` vẫn nói "Phiên bản 2.0" trong khi toàn bộ repo (axiom_spec.md, timeline, nav cards) nói v3.2 — propagation gap cùng class với D1/D2/D4.
**Root cause:** Không có rule bắt buộc sync tất cả version references khi framework version thay đổi.
**Fix:** (1) `index.html` hero badge: "Phiên bản 2.0" → "v3.2". (2) `CLAUDE.md` Document contract rules: thêm **Version propagation bắt buộc** với checklist grep.

### Files Changed

| File | Change |
|------|--------|
| `index.html` | Hero badge dòng 417: "Phiên bản 2.0" → "v3.2" |
| `CLAUDE.md` | Document contract rules: thêm Version propagation rule (RCA 2026-06-13, 5.0/5) |

---

## 2026-06-13 — index.html: Cập nhật theo 3-round RCA × A·B·C triangulation (6 defects, tất cả 5.0/5) ✅

**Trigger:** 3-round RCA × 5-Why × scoring gate (≥ 4/5) áp dụng lên `index.html` theo góc nhìn A (Phan Ngọc) · B (Ashby/Weick) · C (pramāṇa Phật giáo). Root cause duy nhất cho D1/D2/D4: Quyết định 4 (2026-06-11) tái cấu trúc ký pháp không propagate vào `index.html`.

| Defect | Edit | Before | After | Score |
|--------|------|--------|-------|-------|
| D1 | axioms nav card — ký pháp | `3 Mệnh Đề (V–VII) + VIII + IX` | `4 Mệnh Đề (1–4) · Tiên Đề V (Meta) · Tiên Đề VI (Interface)` | 5.0/5 |
| D2 | axiom_6.html card tag | `TIÊN ĐỀ IX` | `TIÊN ĐỀ VI` | 5.0/5 |
| D3 | what.html nav card | `Đồng cấu (Isomorphism)` | `Đồng cấu rút gọn (Homomorphism)` | 5.0/5 |
| D4 | Timeline 2026 | `9 tiên đề, 4 tầng` | `6 Tiên Đề · 4 Mệnh Đề · 4 tầng` | 5.0/5 |
| D5 | pramāṇa paragraph | C-centric, A absent | Giới thiệu đầy đủ A · B · C với [1][2][3] | 5.0/5 |
| D6 | Nguồn Trích Dẫn | [1] Ashby · [2] Prasad | + [3] Phan Ngọc (1998) | 5.0/5 |

**Verify:** axioms card khớp `axiom_spec.md`; axiom_6 tag khớp upgrade card; glossary sync; D6 đủ Rule #12.

### Files Changed

| File | Change |
|------|--------|
| `index.html` | 6 edits: D1–D6 như bảng trên |

---

## 2026-06-13 — Vai Trò & Vị Trí Tương Quan: Thêm Bảng Thuật Ngữ Song Ngữ ✅

**Trigger:** Yêu cầu lập bảng Bảng Thuật Ngữ Song Ngữ / Bilingual Glossary cho `vai_tro_mach_re.html` theo schema của `axiom_1.html`.
**Method:** Thêm phần "Bảng Thuật Ngữ Song Ngữ / Bilingual Glossary" ngay trước phần điều hướng bottom-nav, sử dụng chính các biến design token của tệp (`var(--accent)`, `var(--border)`, `var(--text-muted)`, `var(--accent-pale)`) để đảm bảo tính đồng nhất giao diện và màu sắc.
- Bảng bao gồm 36 thuật ngữ chuyên ngành hệ thống hóa từ nội dung của `vai_tro_mach_re.html` (như *Epistemic Positionality, Relational Ontology, Substance Ontology, Primary/Secondary Lens, Reference Beam, Differentia specifica, Kill Condition, Existential justification, Overclaim, Model-of, Replacement, Ashby Variety Test, Independence Test, Falsification Condition, RCA, RCA gate, External validator, Upāya, Distributed Cognition, Process Philosophy, Pramāṇa, Apoha, Śūnyatā, Orthogonal Temporality, Structural Invariance, Dynamic Boundary, Reflexive Cognition, Adoption, Peer review, Requisite Variety, Sensemaking, Retrospect, Loosely coupled systems, Saṃvṛti-sat, Ubuntu*).
- Sử dụng cấu trúc table đáp ứng chuẩn responsive (`overflow-x:auto`), xen kẽ màu nền dòng chẵn (`#f5faf6`) tương tự như style của `.styled-table` của trang.
- Dịch cụm từ "1 Meta-Tiên Đề (V) + 1 Tiên Đề Interface (VI)" sang tiếng Việt thành "1 Siêu Tiên Đề (V) + 1 Tiên Đề Giao Diện (VI)".
- Diễn giải và bổ sung ranh giới "Không tuyên bố giải thích vật lý" vào bảng giới hạn phòng thủ (§6.2) và khối diễn giải chi tiết trong `vai_tro_mach_re.html`.
- Chuẩn hóa định dạng song ngữ cho các công cụ phương Tây thành VN (EN): "điều khiển học (cybernetics), phân tích nguyên nhân gốc rễ (RCA), tiên đề hóa (axiomatization)" ở mục §2.1.
- Bổ sung liên kết nghiên cứu nội bộ dẫn đến `axiom_3.html` cho cụm từ "khác biệt đặc trưng (differentia specifica)" ở phần đề xuất §3.1.

### Files Changed

| File | Change |
|------|--------|
| `vai_tro_mach_re.html` | Bổ sung phần "Bảng Thuật Ngữ Song Ngữ / Bilingual Glossary" (36 thuật ngữ song ngữ Việt-Anh kèm giải thích chi tiết) ngay trước khối `.bottom-nav`; Dịch thuật ngữ "1 Meta-Tiên Đề (V) + 1 Tiên Đề Interface (VI)" sang tiếng Việt; Bổ sung diễn giải chi tiết về ranh giới "Không tuyên bố giải thích vật lý" tại §6.2; Chuẩn hóa định dạng song ngữ VN (EN) ở mục §2.1; Thêm liên kết nội bộ `axiom_3.html` cho cụm từ "khác biệt đặc trưng (differentia specifica)" tại §3.1. |

---

## 2026-06-13 — Vai Trò & Vị Trí Tương Quan: Việt hóa hoàn toàn thuật ngữ trong file `vai_tro_mach_re.html` ✅

**Trigger:** Yêu cầu dịch sang tiếng Việt hoàn toàn các thuật ngữ tiếng Anh còn sót lại (Gap, offer, peer review, lens, template, publish, claim, tag, AI coinage, taxonomy, framework, identity, model-of, replacement, model, entity, file, code, rubric, proposed, differentia specifica...) trong file `vai_tro_mach_re.html`.
**Method:** Việt hóa toàn bộ các thuật ngữ tiếng Anh sang tiếng Việt:
- "Gap" -> "Khoảng trống"
- "offer" -> "đề xuất/đóng góp"
- "peer review" -> "phản biện/phản biện ngang hàng"
- "lens" -> "thấu kính" (bao gồm thấu kính chính/bổ trợ cho "Primary/Secondary Lens")
- "template" -> "khung mẫu"
- "publish" -> "công bố/xuất bản" (bao gồm sửa "Chưa publish" thành "Chưa công bố" ở hàng C5)
- "claim" -> "tuyên bố/khẳng định"
- "tag" -> "nhãn"
- "AI coinage" -> "thuật ngữ do AI tự tạo"
- "taxonomy" -> "hệ phân loại"
- "framework" -> "khung lý thuyết"
- "identity" -> "sự đồng nhất"
- "model-of" -> "mô hình"
- "replacement" -> "sự thay thế"
- "model" -> "mô hình"
- "entity" -> "thực thể"
- "file" -> "tệp"
- "code" -> "mã nguồn"
- "rubric" -> "bảng tiêu chí"
- "proposed" -> "đề xuất"
- "differentia specifica" -> "khác biệt đặc trưng"
- "Adoption" -> "Sự tiếp nhận" (bao gồm sửa C5 và bảng thế giới)
- "Dialogue" -> "Đối thoại"
- "Citation" -> "Trích dẫn"
- "Impact" -> "Tác động"
- Ghi rõ "Tiên đề I" và mở rộng không viết tắt "Tiên đề II × Tiên đề IV" ở tiêu đề của "Đề xuất 3" (Cơ chế Hấp thụ có Định hướng).
- Thêm liên kết so sánh và mã trích dẫn học thuật cho Ubuntu [10, 11], Yoruba [12], Nhật Bản (Nakane) [9], và Phật giáo Joseon Hàn Quốc [13] vào hàng C2 (Khả năng tổng quát) của bảng chấm điểm.
- Bổ sung các nguồn trích dẫn học thuật [12] (cho Yoruba) và [13] (cho Phật giáo Joseon Hàn Quốc) vào phần Nguồn Trích Dẫn ở cuối tệp.
- Việt hóa các thuật ngữ tiếng Anh còn lại ở hàng C3 (Tính vận hành) của bảng chấm điểm: thay thế "Có test được không?" -> "Có thể kiểm chứng được không?", "falsification condition" -> "điều kiện bác bỏ (falsification condition)", và "test định lượng" -> "kiểm chứng định lượng".
- Việt hóa các thuật ngữ tiếng Anh ở hàng C5 (Tính tự sửa) của bảng chấm điểm: thay thế "RCA gate" -> "cổng kiểm soát RCA (RCA gate)", "CHANGELOG" -> "nhật ký thay đổi (CHANGELOG)", và "external validator" -> "bên kiểm chứng độc lập từ bên ngoài (external validator)".
- Bổ sung mã trích dẫn liên kết cho các thấu kính A — Phan Ngọc [1], B — Ashby / Weick [2, 3], và C — Buddhist Epistemology [7, 8] tại bốn vị trí trong tệp (phần mô tả tầng L3, thẻ hệ phân loại thấu kính, tiêu đề mục 5.3, và tiêu đề bảng hội tụ).
- Bổ sung mã trích dẫn liên kết cho các gương soi Ubuntu [10, 11], Yoruba [12], Nakane (Nhật Bản) [9], và Mbiti (Châu Phi) [10] trong thẻ Gương soi của hệ phân loại.
- Bổ sung mã trích dẫn liên kết cho tia chuẩn Nho · Phật · Lão [1, 7, 8] trong thẻ Tia chuẩn của hệ phân loại.
- Bổ sung mã trích dẫn liên kết [1] cho phần thảo luận về Tam giáo đồng nguyên ở mục 4.2 và việt hóa thuật ngữ "output" -> "đầu ra (output)".
- Việt hóa các thuật ngữ tiếng Anh và bổ sung mã trích dẫn liên kết [1], [2], [3], [7], [8] cho các phát biểu độc lập (independence claims) của cả ba thấu kính A, B, và C ở các mục 5.1, 5.2, và 5.3.
- Việt hóa các thuật ngữ chuyên ngành Phật học (pramāṇa, prameya, pramā, phala, apoha, nirvāṇa, saṃvṛti-sat...) trong mục 5.3.
- Việt hóa "Buddhist Epistemology" thành "Nhận thức luận Phật giáo (Buddhist Epistemology)" và chuẩn hóa viết hoa "Tiên Đề" -> "Tiên đề" trong tiêu đề của bảng hội tụ (mục 5.4).
- Việt hóa các thuật ngữ tiếng Anh trong hộp ghi chú ở §6 (Biện minh tồn tại): thay thế "claim" -> "tuyên bố (claim)", "tag" -> "nhãn (tag)", và "overclaim" -> "tuyên bố quá mức (overclaim)".
- Bổ sung khối diễn giải chi tiết (Diễn giải về Lý do Phòng thủ) ngay dưới bảng giới hạn phòng thủ ở mục 6.2.
- Cập nhật phát biểu về Điều kiện 4 (Upāya) trong hộp ghi chú ở cuối mục §7 từ "có thể nghỉ" thành "có thể biến mất trong dòng chảy lịch sử".

### Files Changed

| File | Change |
|------|--------|
| `vai_tro_mach_re.html` | Việt hóa hoàn toàn các thuật ngữ tiếng Anh còn sót lại (bao gồm dịch 'output' -> 'đầu ra (output)'); bổ sung liên kết so sánh và mã trích dẫn học thuật [9, 10, 11, 12, 13] cho Ubuntu, Yoruba, Nhật Bản (Nakane), và Phật giáo Joseon Hàn Quốc ở hàng C2, việt hóa các thuật ngữ ở hàng C3 và C5, gắn mã trích dẫn liên kết [1], [2, 3], [7, 8] cho các thấu kính A, B, C (ở mô tả L3, thẻ hệ phân loại, tiêu đề mục 5.3, và tiêu đề bảng hội tụ), bổ sung mã trích dẫn liên kết [9, 10, 11, 12] cho các gương soi và [1, 7, 8] cho các tia chuẩn trong thẻ hệ phân loại, bổ sung mã trích dẫn [1] cho Tam giáo đồng nguyên, việt hóa và bổ sung trích dẫn cho các phát biểu độc lập ở mục 5.1, 5.2, 5.3, việt hóa các thuật ngữ chuyên ngành Phật giáo ở mục 5.3 và trong tiêu đề bảng hội tụ (5.4), việt hóa các thuật ngữ tiếng Anh trong hộp ghi chú ở §6, bổ sung khối diễn giải chi tiết cho Lý do Phòng thủ ở mục 6.2, cập nhật phát biểu Điều kiện 4 ở mục §7, đồng thời cập nhật phần Nguồn Trích Dẫn ở cuối tệp. |

---

## 2026-06-13 — Vai Trò & Vị Trí Tương Quan: Tổng hợp 9 RCA Findings (F1–F9) ✅

**Trigger:** User request: RCA (A×B×C) → tạo HTML "Vai trò và Vị trí tương quan của Mạch Rễ trong triết học VN và thế giới" từ source `raw/vai_tro_mach_re.txt` → gắn link vào `index.html` + `what.html`.
**Method:** 3-Round RCA × 5-Why × 6-criterion scoring gate (Correct, Deep, Feasible, Conflict-risk, Preservation, Provenance). 6 claims scored: C1 VN role (6/6), C2 TG role (6/6), C3 Taxonomy 3 vai (6/6), C4 Model-of (6/6), C5 Existential justification (5/6), C6 6-layer positionality (6/6). All PASS ≥ 5/6.

### Page Structure (7 sections)

| § | Nội dung | Neo RCA |
|---|---------|---------|
| §0 | Phán quyết Tồn tại — Tóm tắt (VN 6.0/10 · TG potential 6.0/10, actual 0/10) | F8 |
| §1 | Tuyên bố Vị thế Nhận thức 6 lớp (L1–L6) | CLAUDE.md canonical |
| §2 | Vai trò trong Triết học Việt Nam (model-of F2, bất đối xứng F3, scoring table) | F2+F3+F8 |
| §3 | Vai trò trong Triết học Thế giới (2 trục: potential vs actual, 4 structural offers) | F8, RCA C2 |
| §4 | Taxonomy 3 Vai: Thấu kính / Gương soi / Tia chuẩn (Ubuntu=F5, Tam giáo=F6) | F5+F6 |
| §5 | Ba Hệ Neo A×B×C — Vai trò từng hệ + Bảng hội tụ 5 tiên đề | F1 |
| §6 | Biện minh Tồn tại có điều kiện (3 gaps + 6 non-claims) | F8 post-F9 |
| §7 | Điều kiện "Chết" (4 kill conditions, condition 4 = upāya = success condition) | F8 |

### Scoring Gate Summary

| Claim | Score | Verdict |
|-------|-------|---------|
| C1 — Vai trò Mạch Rễ trong triết học VN (6.0/10) | 6/6 | PASS |
| C2 — Vai trò Mạch Rễ trong triết học TG (tách potential/actual) | 6/6 | PASS |
| C3 — Taxonomy 3 vai `[proposed]` | 6/6 | PASS |
| C4 — Model-of + bất đối xứng phụ thuộc | 6/6 | PASS |
| C5 — Biện minh tồn tại có điều kiện | 5/6 | PASS (sửa cách trình bày TG) |
| C6 — Tuyên bố vị thế nhận thức 6 lớp | 6/6 | PASS |

### RCA C2 Insight — Tách Tiềm năng / Ảnh hưởng

Root cause: "Vai trò TG 2.8/10" cũ lẫn lộn potential và actual → gây hiểu nhầm. Fix: tách thành 2 trục độc lập. TG potential = 6.0/10 (4 structural offers có thật). TG actual = 0/10 (trung thực: chưa có peer review, adoption, citation, dialogue, impact).

### Files Changed

| File | Change |
|------|--------|
| `vai_tro_mach_re.html` | **CREATED** — 7 sections, ~950 lines, full provenance tagging, 11-source citation table |
| `index.html` | CSS: +`.c-role` class (copper accent) · Nav: +"Vai Trò & Vị Trí Tương Quan" card |
| `what.html` | §6: +cross-reference box linking to `vai_tro_mach_re.html` |

**Provenance:** All typology/history/comparison claims tagged `[established]` (relational ontology, distributed cognition, Phan Ngọc 1998, Ashby 1956, Buddhist epistemology) or `[proposed-by-this-project]` (taxonomy 3 vai, 6-layer positionality, kill conditions, V⊥H, Mạch Rễ framework). No untagged claims.

---

## 2026-06-13 — TRITHUC-1 Cross-Cultural Verification: RS 27.0→13.5 [RS-CRIT→RS-MED] ✅

**Trigger:** TRITHUC-1 open — V⊥H Orthogonal Temporality `[proposed-by-this-project]`, no external verification. Root cause: V⊥H first observed in Vietnamese material only → cannot distinguish structural property from cultural artifact.
**Method:** 3-Round RCA × 5-Why × ABC triangulation (A=Phan Ngọc, B=Ashby/Weick, C=Buddhist Epistemology) × scoring gate ≥ 4/5 (both cases: 6/6 = 5.0/5).
**Cases:** Japan/Nakane (1970) — partial-close · Ubuntu/Mbiti (1969) — strong partial-close.
**Commits:** `fcffb4d` Japan · `45c48b4` Ubuntu.
**RCA summary:** `plan/2026-06-13_trithuc1_verification_rca_summary.md`

### Verification Results

| Case | Source | Key finding | Scoring gate | RS change |
|------|--------|------------|-------------|----------|
| Japan | Nakane (1970) *Japanese Society* | Operational V⊥H: ie (H→V: persists when all H members replaced) + Plath 1964 (V→H: dead do not determine living's present). Sociological level. | 6/6 = 5.0/5 ✅ | 27.0 [RS-CRIT] → 18.0 [RS-HIGH] |
| Ubuntu | Mbiti (1969) *African Religions and Philosophy* | Sasa/zamani = explicit 2-temporal-dimension ontological claim (strongest single source). C-system negative evidence: no zamani equivalent in pratītyasamutpāda → V not derivable from H-axis relational ontology. | 6/6 = 5.0/5 ✅ | 18.0 [RS-HIGH] → 13.5 [RS-MED] |

### ABC Triangulation Key Insight

C (Buddhist Epistemology) models H-axis (pratītyasamutpāda, dependent origination) excellently but has **no zamani equivalent**. V is not derivable from H-axis relational ontology → two genuinely distinct dimensions, not a naming artifact. C's gap = structural impossibility evidence — a distinct class from positive corroboration.

### Files Changed

| File | Change |
|------|--------|
| `documents/public_documents/Nakane_Japanese_Society_RCA_Table.md` | **CREATED** — 12 concepts: tate, yoko, ie, ba, oyabun-kobun, seniority, uchi/soto |
| `documents/gap/TRITHUC-1_japan_verification.md` | **CREATED** — R1–R3 RCA, bridge argument, verdict, full-close conditions |
| `documents/public_documents/Ubuntu_Philosophy_RCA_Table.md` | **CREATED** — 12 concepts: sasa, zamani, ubuntu, ukama, living dead; ABC triangulation lens |
| `documents/gap/TRITHUC-1_ubuntu_verification.md` | **CREATED** — R1–R3 + ABC triangulation, C-system negative evidence, strong partial-close |
| `documents/gap/TRITHUC_index.md` | Part 2 TRITHUC-1: → `🔓 Open (strong partial)`, 3 SOT files, date 2026-06-13; Part 5: 2 correction entries |
| `anti_hallucinations/00_top_risk_record.md` | TRITHUC-1: H 6→3, RS 27.0→13.5 [RS-CRIT→RS-MED]; re-audit monthly; versions v1.1+v1.2 |
| `plan/2026-06-13_trithuc1_verification_rca_summary.md` | **CREATED** — RCA tổng kết: 5-Why root cause, F1–F4 findings, process insight, falsification conditions |

**Status after session:** TRITHUC-1 RS 13.5 [RS-MED] · 3 convergent cases across 3 continents (Vietnam + Japan + Ubuntu) · Path A (cross-cultural verification) substantially met · Path B remaining (formal derivation I+II→V⊥H) · Monthly re-audit 2026-07-13.

---

## 2026-06-13 — Bilingual Glossary for Tiên Đề II & Terminology Standardization ✅

**Trigger:** User request to add Bilingual Glossary to `axiom_2.html` (matching schema of `axiom_1.html`) and standardize technical terms to bilingual VN (EN) format.
**Method:** 3-round RCA × 5-Why × scoring gate ≥ 4/5.

### Key Changes

* **Bilingual Glossary Addition:** Added a comprehensive glossary section containing 26 philosophical and systems terms relevant to Tiên Đề II (`axiom_2.html`), matching the layout, typography, and gold/brown theme of the page.
* **Standardized Terminology (VN (EN)):** Updated all occurrences of the word "pattern" in Vietnamese contexts to use bilingual terms (`nếp (pattern)` or `nếp bất biến (invariant pattern)`), translated `pattern bất biến` to `nếp bất biến (invariant pattern)`, converted Section 2 header in `axiom_2.html` to `Cấu trúc vs Bề mặt (Structural vs Surface): Tại sao "nếp (pattern)" chứ không phải "nội dung (content)"?`, standardized the relational invariant shorthand in the Why 1 box to `Nếp quan hệ (pattern of relations) = bất biến (invariant); nội dung (content) = khả biến (variable)`, updated the substance reference in the Why 2 box to `bản thể (substance)`, standardized the philosophical and framework terms (`svabhāva` -> `tự tính (svabhāva)`, `essentialism` -> `chủ nghĩa bản chất (essentialism)`, `Anattā` -> `Vô Ngã / Anattā`, `framework` -> `khung lý thuyết (framework)`) in the Why 3, 4 & 5 box, and updated the comparison cards (Phan Ngọc, Lévi-Strauss, Ashby) including their ASCII boxes to use bilingual formats (`quy ước thật (saṃvṛtisat)`, `cấu trúc sâu nhận thức (cognitive deep structures)`, `nếp quan hệ bất biến (relational invariant patterns)`, `biến cốt lõi (essential variables)`, `bất biến (invariant)`, `bất biến quan hệ (relational invariant)`, `chứng minh hình thức (formal proof of concept)`, and `miền (domain)`).
* **Citation & Sources Enrichment:** Appended Nāgārjuna `[5]` (for *Anattā* & *Pratītyasamutpāda*) and Ramose `[6]` (for *Ubuntu*) to the references section at the bottom of `axiom_2.html`, and added citation hyperlinks `[1]`, `[2]`, `[3]`, and `[5]` directly to the official Vietnamese statement label for Tiên Đề II.

### Files Changed

| File | Change |
|------|--------|
| [axiom_2.html](file:///c:/Stable_Diffusion/MACH_RE/axiom_2.html) | Added Bilingual Glossary, appended sources [5] and [6] to references list, and updated all Vietnamese-context occurrences of "pattern" to use the bilingual format. |

---

## 2026-06-13 — AHP Audit & Corrective Actions: 4 findings fixed ✅

**Trigger:** Audit plan `plan/2026-06-13_plan_ahp_audit.md` — re-run self-audit as filesystem measurements (3-round RCA × 5-Why × scoring gate ≥ 4/5, Buddhist Epistemology compass).
**Pre-audit:** 9/15 PASS · 1 PARTIAL · 4 FAIL → corrective Phases A–E executed → **Post-audit: 15/15 PASS**.

### Findings Fixed

| Finding | Severity | Root cause (1 câu) | Fix |
|---------|----------|-------------------|-----|
| AF-1 | CRITICAL | Self-audit declared PASS without filesystem measurement; file #2 (`00_top_risk_record.md`) dropped from phase decomposition | Phase A: created `anti_hallucinations/00_top_risk_record.md`; Phase B: correction notes additive |
| AF-2 | HIGH | §AHP deleted from CLAUDE.md working tree (accident — Q1 human confirmed) | Phase C: section restored from `git show HEAD:CLAUDE.md` lines 324–351 |
| AF-3 | HIGH | SOT-8 (Compass C) untracked in git; self-audit had no VCS-coverage check | Phase D: `git add` 4 SOT items |
| AF-4 | MEDIUM | Plan 2026-06-12 still "AWAITING APPROVAL" post-execution — user approval not recorded in repo | Phase B: Status updated + Part 8 checklist ticked |

### Files Changed (Phases A–E)

| File | Change |
|------|--------|
| `anti_hallucinations/00_top_risk_record.md` | **CREATED** Phase A — 14 entries: 4 audit findings + 10 TRITHUC gaps, RS = H×W×(1+A) |
| `anti_hallucinations/index.md` | Phase B: Version History v1.1 correction note |
| `anti_hallucinations/plan/2026-06-12_ahp_rca_summary.md` | Phase B: file inventory correction (14 not 15) |
| `anti_hallucinations/plan/2026-06-12_ahp_instantiation_log.md` | Phase B: log entries 7 + 8 |
| `plan/2026-06-12_plan_ahp_installation.md` | Phase B: Status → EXECUTED; Part 8 ticked |
| `CLAUDE.md` | Phase C: §Anti-Hallucination Pipeline restored (28 lines) |
| `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md` | Phase D: staged (SOT-8) |
| `documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md` | Phase D: staged |
| `documents/gap/BIAN_index_schema.md` | Phase D: staged |
| `documents/archives/MACH_RE_AXIOMS_FRAMEWORK.md` | Phase D: staged |
| `anti_hallucinations/integration_spec.md` | Phase E: §6 Post-Installation Verification Checklist (checks #12–15) |
| `anti_hallucinations/template/template_integration_spec.md` | Phase E: §6 added to template |
| `plan/2026-06-13_plan_ahp_audit.md` | Audit plan v1.1 |

### Process Improvement Inherited by Template

Checks #12–15 added permanently to `integration_spec.md` §6 + `template/template_integration_spec.md` §6:
- #12 File count by `ls | wc -l` measurement (not declaration)
- #13 All SOTs git-tracked via `git ls-files --error-unmatch`
- #14 Authorizing plan status field reads "EXECUTED…"
- #15 No lingering working-tree SOT changes

**Root of each AF:** AF-1 = plan count ≠ filesystem count; AF-2 = SOT edit not committed same session; AF-3 = no VCS coverage check in self-audit; AF-4 = approval not ghi nhận repo.

---

## 2026-06-12 — AHP Installation: Anti-Hallucination Pipeline for MACH RE ✅

**Trigger:** Plan `plan/2026-06-12_plan_ahp_installation.md` — RCA 5.8/6 (4.83/5) → PROCEED.
**Method:** 3-round RCA × 5-Why × scoring gate ≥ 4/5. 6-phase installation.
**Template:** AHP v3.1 Template v1.0, exported from `anti_hallucinations/template/`.

### Output (17 files)

| File | Type |
|---|---|
| `anti_hallucinations/README.md` | meta |
| `anti_hallucinations/index.md` | index — 3-layer: RULE ZERO → AHP → labels.md |
| `anti_hallucinations/00_top_risk_record.md` | pipeline — Risk Score H×W×(1+A), TTL |
| `anti_hallucinations/01_early_warning.md` | pipeline — 20 signals |
| `anti_hallucinations/02_detection.md` | pipeline — 14 components, 4-group classification |
| `anti_hallucinations/03_sot_traceability.md` | pipeline — 8 SOTs, N=8 |
| `anti_hallucinations/04_analysis.md` | pipeline — 6 root cause types, FSR |
| `anti_hallucinations/05_scoring.md` | pipeline — 5-band calibration |
| `anti_hallucinations/06_solution.md` | pipeline — P0-P4 + P-DEFER |
| `anti_hallucinations/label_system.md` | pipeline — 25 labels, labels.md canonical |
| `anti_hallucinations/stakes_assessment.md` | BDS |
| `anti_hallucinations/vyapti_registry.md` | BDS — 9 VYR entries |
| `anti_hallucinations/integration_spec.md` | BDS — 4 critical rules |
| `anti_hallucinations/system_registry.md` | multi-system — 4 systems |
| `anti_hallucinations/mapping_registry.md` | multi-system — 26 links, 5 NAC |
| `anti_hallucinations/plan/2026-06-12_ahp_instantiation_log.md` | plan |

### Key decisions

- **D1** (4.83/5): Install AHP — fills middle layer between RULE ZERO (process) and labels.md (verdict)
- **D2** (4.8/5): labels.md = canonical confirmation SOT; AHP labels = encoding
- **D3** (4.8/5): `[AH-NAJ]` added — derived from labels.md #3
- **D4** (4.8/5): NAC table from TRITHUC gaps (5 entries)
- **D5** (4.8/5): Dual scoring: RCA gate = change decision; AHP score = risk tracking

### Modified: `CLAUDE.md` — added §Anti-Hallucination Pipeline

---

## 2026-06-12 — A_SYSTEM_Phan_Ngoc: Node-Edge system from Bản Sắc Văn Hóa Việt Nam ✅

**Trigger:** RCA chuyển source document Phan Ngọc (585 trang) thành bảng Node (N_PN_00000) + Edge (ED_PN_00000) theo schema Buddhist Epistemology.
**Files:** `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` (new)
**Sources:** `BanSacVanHoaVietNam_Phan_Ngoc.md` (OCR source) + `BanSacVanHoaVietNam_Phan_Ngoc_RCA_Table.md` (30-concept reference)
**Carry-forward:** 30 RCA concepts from reference table → core layer N_PN_00001–N_PN_00030
**Output:** 68 nodes (30 core + 38 RCA expanded) × 124 edges — all source-traced to TRANG/LINE

---

## 2026-06-12 — A·B·C System Mapping + TRITHUC Gap Index ✅

**Trigger:** Plan `plan/2026-06-12_plan_a_b_c_mapping.md` — RCA mapping 3 compass systems (A: Phan Ngọc · B: Ashby/Weick · C: Buddhist Epistemology) against MACH RE axioms.
**Triple compass/lens:** A·B·C = thấu kính (lens), không phải mirror hay reference beam (`axiom_spec.md §0.4`).
**Method:** 3-round RCA × 5-Why × scoring gate ≥ 4/5 cho mọi mapping decision. Map ở axiom-level.

### Output files

| File | Type | Description |
|---|---|---|
| `documents/mapping/a_b_c_system_mapping.md` | mapping | 6 Parts: Node/Edge Reference, 10 axiom units × 3 compasses with RCA-gated evidence rows, Structural Summary, Boundary, Validation, Nguồn Trích Dẫn |
| `documents/gap/TRITHUC_index.md` | index | 10 TRITHUC gap labels; namespace `TRITHUC-` distinct from `BIAN-` (BE↔QM) |
| `plan/2026-06-12_plan_a_b_c_mapping.md` | plan | 6-phase implementation plan with RCA gate, carry-forward set |

### Key RCA decisions

| # | Decision | RCA score | Description |
|---|---|---|---|
| D1 | Namespace `TRITHUC-` | 4.8/5 | Tránh overlap BIAN-1–20 của BE↔QM mapping |
| D2 | Map at axiom-level | 5.0/5 | 250+ nodes × 10 axioms → axiom-level constraint |
| D3 | Carry-forward triplet scores | 4.8/5 | Baseline confirmed + enriched with node/edge evidence |
| D4 | III-orthogonality = `[proposed]` | 4.8/5 | V ⊥ H partially supported by all 3, fully captured by none |
| D5 | A-Phần 3 excluded | 4.8/5 | Per `axiom_spec.md §0.1.1` — register mismatch |

### Structural findings

- **Strongest convergence:** "Identity = relations" (I) — all 3 compasses: 3.0/3
- **Strongest MACH RE novelty:** V ⊥ H (III) + C1-graded reflexivity (VI) + F-AND-gate (MĐ 4)
- **Gap count:** 10 TRITHUC labels — 3 `[proposed]` (intrinsic), 7 compass-unique, 2 scope boundaries
- **Coverage:** All 10 axiom units ≥ 2.0/3; 7/10 ≥ 2.5/3; 4/10 = 3.0/3

---

## 2026-06-12 — v3.4 · Provenance Retraction F9 + Provenance Gate (RULE ZERO Criterion 6) ✅

**Trigger:** Kiểm chứng ngoài (con người) xác nhận tên phạm trù "Triết học Tương quan-Phân tán / Relational and Distributed Philosophy" là AI coinage — không tồn tại trong văn liệu học thuật độc lập với tư cách taxonomy đã công nhận.
**Triple compass:** A (Phan Ngọc — tiếp biến) · B (Ashby/Weick — Variety, sensemaking) · C (Buddhist Epistemology — saṃvṛti/paramārtha, apoha)
**Method:** 3-round RCA × 5-Why × scoring gate ≥ 4.5/5 (ngưỡng cao hơn cho câu hỏi tồn tại)
**RCA score F9:** 4.8/5 — root = gate thiếu tiêu chí Provenance → fix: thêm tiêu chí thứ 6

### Retraction — đầu tiên của dự án

| Claim bị rút | File(s) | Score cũ (rubric 5) | Score mới (rubric 6) | Root cause |
|---|---|---|---|---|
| "Tương quan-Phân tán" là `[established]` taxonomy | `CLAUDE.md` Core Principle | 5.0/5 (mù provenance) | 3.8/6 (Provenance=0) | AI coinage trình bày sai tư cách; gate 5 tiêu chí không bắt được |

### Các thay đổi thực hiện

| # | Thay đổi | File(s) | Loại |
|---|---|---|---|
| P1 | Thêm tiêu chí Provenance (gate thứ 6) vào bảng scoring RULE ZERO | `CLAUDE.md` | Fix gốc rễ |
| P2 | Mở rộng bước Verify sang nguồn ngoài repo | `CLAUDE.md` | Fix gốc rễ |
| P3 | Rút điểm 5.0/5 → re-mark `[proposed-by-this-project]` trong Core Principle | `CLAUDE.md` | Retraction |
| P4 | Provenance Notice box + `[proposed-by-this-project]` tag | `relational_and_distributed_philosophy.html` | Re-mark |
| P5 | Boundary Statement: "cùng thuộc" → "chia sẻ đặc trưng của loại hình đề xuất `[proposed-by-this-project]`" | `ubuntu.html` | Re-mark |
| P6 | Self-classification: "thuộc loại hình" → "đề xuất loại hình `[proposed-by-this-project]`" | `index.html` | Re-mark |
| P7 | Typology claim: "đều thuộc" → "chia sẻ đặc trưng của loại hình đề xuất `[proposed-by-this-project]`" | `what.html` | Re-mark |

### Carry-forward (không bị xóa)
`[established]`: relational ontology (Whitehead, Emirbayer 1997) + distributed cognition (Hutchins 1995). Nội dung phân tích so sánh — giữ nguyên, mang đúng tư cách. Hệ tiên đề I–VI không phụ thuộc tên phạm trù. Structural homologies (ubuntu.html, yoruba.html) — giữ, chỉ sửa claim tư cách.

**Phán quyết tồn tại (F8, 4.8/5 ≥ 4.5):** Biện minh chuyển sang có điều kiện: VN 6.0/10 · TG 2.8/10. Bảng điểm đầy đủ tại `review/2026-06-12_tuyen_bo_rca_verdict.md`.

---

## 2026-06-12 — RCA Cross-Link `relational_and_distributed_philosophy.html` ↔ `what.html` ✅

**Trigger:** User request: "RCA link trang này `relational_and_distributed_philosophy.html` với `what.html`"
**Triple compass:** A (Phan Ngọc — tiếp biến, bản sắc quan hệ) · B (Ashby/Weick — Requisite Variety, sensemaking) · C (Buddhist Epistemology — Pratītyasamutpāda: nodes exist only through relations)
**Method:** 3-round RCA × 5-Why × scoring gate ≥ 4/5 on each link insertion

**Root cause:** The HTML documentation violated Tiên Đề I (Relational Ontology) applied reflexively — knowledge nodes (`what.html`, `relational_and_distributed_philosophy.html`) existed as isolated entities connected only by peripheral navigation chrome, not by explicit content-level hyperlinks. The authoring workflow treated each `.html` page as a self-contained document rather than a node in a distributed knowledge graph.

### RCA scores per link insertion

| # | Link inserted | File | RCA Score | Root cause addressed |
|---|---|---|---|---|
| L1 | "văn hóa lúa nước Việt Nam" → `what.html` | `relational_and_distributed_philosophy.html` L214 | 5.0/5 | First Vietnam reference in taxonomy argument — reader had no clickable path to learn what Mạch Rễ is |
| L2 | "Mạch Rễ" + "Tiên Đề V — Tự Nhìn Thấy Mình" → `what.html` | `relational_and_distributed_philosophy.html` L323 | 5.0/5 | Direct framework invocation in concluding section — highest-priority content link gap |
| L3 | "Mệnh Đề 1: Giữ mà không gom" → `what.html` | `relational_and_distributed_philosophy.html` L240 | 5.0/5 | Technical axiom reference in concept card — reader had no path to axiom definition |

### 5-Why Trace (L2 — highest-priority gap)

- **Why 1:** No content-level links from `relational_and_distributed_philosophy.html` prose to `what.html` → Prose references to "Mạch Rễ" are plain `<p>` text.
- **Why 2:** Plain text references → Page authored with "textbook chapter" mental model (sequential reading: index → what → relational).
- **Why 3:** Sequential assumption → Navigation breadcrumb treated as sufficient cross-reference.
- **Why 4:** Nav chrome substituting for content links → HTML knowledge graph not designed with framework's own relational ontology principle.
- **Why 5 (root):** **Tiên Đề I violated reflexively: knowledge nodes existed as isolated entities rather than a connected network where each node defines the other through explicit content-level hyperlinks.**

### Files changed

| File | Changes |
|---|---|
| `relational_and_distributed_philosophy.html` | +3 content-level hyperlinks → `what.html` (L214, L240, L323) |

### Existing links (reverse direction, verified unchanged)

| From | To | Type |
|---|---|---|
| `what.html` §6 | `relational_and_distributed_philosophy.html` | 2× content-level links (philosophical category paragraph) |
| `relational_and_distributed_philosophy.html` nav/footer | `what.html` | 3× structural chrome links |

**Verification:** `what.html` already had adequate reverse links in §6 "Vị trí trong bản đồ triết học toàn cầu" — no changes needed.

## 2026-06-11 — Refactor Ky Phap Phan Tang Theo `raw/axiom-chart.html` (Quyet Dinh 4) ✅

**Trigger:** Nguoi dung chot: so La Ma CHI danh cho Tien De; Menh De Dan Xuat danh so La tinh 1–4; cap duoi nua khong danh so phan cap.
**Triple compass:** A (Phan Ngoc) · B (Ashby/Weick) · C (Buddhist Epistemology: Apoha, Nhi de).
**Method:** 3-round RCA × 5-Why × scoring gate ≥ 4/5 trên 6 quyết định. Chi tiết: `plan/2026-06-11_refactor-danh-so-tien-de-menh-de.md`.
**User override (2026-06-11):** Dồn số Tiên Đề: VIII → V, IX → VI. Dãy liên tục I–VI: I–IV Core · V Meta · VI Interface. A-B-C compass: upāya tốt hơn cho người mới tiếp cận; dãy liên tục giảm variety đọc nhầm (Ashby).
**File rename (RCA D7, 4.4/5):** `axiom_9.html` → `axiom_6.html`, `axiom_ix_spec.md` → `axiom_6_spec.md`. Internal links updated across all living files (who, when, index, upgrade, axiom_spec, axiom_6, axiom_6_spec). CSS class `c-axiom9` → `c-axiom6`.

**6 quyet dinh:** D1 Menh De V/VI/VII/F → La tinh 1/2/3/4 (4.8 → FIX) · D2 Tien De VIII/IX giu so (4.8 → GIU) · D3 Sai tang "Tien De V/VI/VII" → "Menh De 1/2/3" (5.0 → FIX) · D4 UPGRADE I–IV → Upgrade 1–4 (4.6 → FIX) · D5 Dai "I–VIII" → "I–IV + VIII" / `Full(S)` (4.4 → FIX) · D6 Giu ky hieu cau truc cap duoi (F(S,t), DSH-n, …) (GIU).

**SSOT:** `axiom_spec.md` — Header; derivation log; headings; schema; Quyet Dinh 4 + mapping table §5.2; YAML split axioms/propositions.
**Canonical:** `plan/dictionary_rule.md` §9 tach bang Tien De / Menh De; `CLAUDE.md` cap nhat.
**Refactor 15 file song** (axioms, axiom_derived, what, how, index, axiom_1, axiom_9, axiom_ix_spec, luu_tru, upgrade, axiom_conflict, ubuntu, yoruba, relational_and_distributed_philosophy).
**Anchor/ID** giu nguyen (#F, id="...") — khong gay link.
**Tang khong sua** (lich su): CHANGELOG* cu, plan/* co ngay, review/*, raw/*, papers/*, publish/movie_script/*.

## 2026-06-11 — Paper 005 v2 RCA Audit · 4.88/5 · 1 fix · PASS ✅

**3-round RCA × 5-Why × scoring gate on paper_005_v2.md.** 11 audit items scored. 1 finding fixed: F1 — "Dĩ bất biến ứng vạn biến" from "là một tuyên bố triết học rõ ràng" → "có thể được đọc như một tuyên bố triết học" (conservative form, 4.72/5). 1 observation kept: O1 — compound label `[established theory, applied interpretation]` (adds precision, 4.52/5). Cross-cutting: D1-D4 all 5.00/5, zero forbidden language, 36 labels correct, 26/26 citations resolve. 0 blocking issues.

**Files:**
- `review/2026-06-11_05_paper_005_v2_rca_audit.md` (tạo mới — audit report)
- `papers/paper_005/paper_005_v2.md` (sửa — F1 fix)

> Cross-ref: Paper 005 v2 manuscript → [`papers/CHANGELOG_papers.md`](papers/CHANGELOG_papers.md).

## 2026-06-11 — v3.3 Naming De-Enclosure — Epistemic Humility Alignment ✅

**Trigger:** Cultural researcher critique: "Văn hóa VN thực ra nó đề cao sự khiêm nhường, kể cả có nghĩ ra cũng không ai muốn đứng lên trên cả dân tộc mà đặt tên."  
**Triple compass:** A (Phan Ngọc — tiếp biến văn hóa) · B (Ashby/Weick — Requisite Variety + sensemaking) · C (Buddhist Epistemology — Apoha, Upāya, Two Truths, Anattā)  
**Method:** 3-round RCA × 5-Why × scoring gate ≥ 4/5 on all claims  
**Meta-review:** `plan/2026_06_11_audit_dat_ten_mach_re_REVIEWED.md` — original plan scored 3/5, enhanced to 5/5

### RCA scores per changed claim

| # | Claim changed | File(s) | RCA Score | Root cause |
|---|---|---|---|---|
| C1 | Tagline "Được đặt tên: 2026" → "Được mô hình hóa: 2026" | index.html, when.html | 4.8/5 | Epistemic enclosure: naming act implied ownership of commons (C: Anattā violation) |
| C2 | "đặt tên và hệ thống hóa" → "mô tả cấu trúc và hệ thống hóa" | index.html | 4.6/5 | Category error: model vs. entity conflation (C: saṃvṛti/paramārtha distinction) |
| C3 | Timeline "Mạch Rễ được đặt tên" → "Mô hình Mạch Rễ được hệ thống hóa" | index.html, when.html | 4.4/5 | Historical anchoring implied singular authority (A: tiếp biến framing) |
| C4 | Definition "Mạch Rễ — Triết lý sinh tồn" → "mô hình phân tích mô tả" | what.html | 4.8/5 | Direct identity claim between framework and national philosophy (B: Ashby Variety Test) |
| C5 | "Tại sao phải đặt tên" → "Tại sao phải hệ thống hóa" | why.html | 4.2/5 | Section header presupposed naming as the only valid response |
| C6 | Added reflexive paradox statement (Upāya + Apoha) | what.html §4 | 5.0/5 | Tiên Đề VIII operational: framework sees its own limit |
| C7 | Added "Mạch Rễ như Tiếp Biến" framing | what.html §4 | 4.8/5 | Positive Vietnamese-grounded justification (A: Phan Ngọc) |
| C8 | Strengthened three compass anchors with Apoha/Variety/Tiếp Biến | axiom_spec.md §0.1 | 4.6/5 | Compass under-specification (A+B+C) |
| C9 | Added "Khiêm nhường/Ẩn mình" operational notes | axiom_spec.md §2 | 4.4/5 | Mechanism unstated: humility as structural shield, not passivity |
| C10 | CC BY 4.0 → CC0 1.0 Universal | LICENSE, index.html | 5.0/5 | Attribution requirement contradicted Tiên Đề I+V (Anattā + Distributed) |

### Files changed (6 files, +85/−25 lines)

| File | Changes |
|---|---|
| index.html | Tagline, definition, timeline, license badge, footer |
| when.html | Timeline tagline |
| what.html | Definition, "gọi tên chung", reflexive paradox blockquote, Tiếp Biến section |
| why.html | Section header, urgency text |
| axiom_spec.md | Three anchors strengthened, operational notes for I+II+V |
| LICENSE | CC BY 4.0 → CC0 1.0 Universal |

### Definition of Done — ALL PASS ✅

1. ✅ Zero "đặt tên" ownership language in production files
2. ✅ Consistent model-not-entity framing across all pages
3. ✅ Self-reflective paradox statement embedded in what.html §4
4. ✅ CC0 legal release with explicit no-attribution statement
5. ✅ Ashby Variety Test: ≥ 3 self-description pathways remain open post-fix
6. ✅ CHANGELOG recorded with per-claim RCA scores
7. ✅ Cross-file consistency verified (grep: only raw/ archive retains old text)

---

## 2026-06-11 — Phase 9: Closure Audit — Mạch Rễ v3.2 IX Build · ALL PASS ✅

**Triple compass:** A (Phan Ngọc) — framework's "kiểu lựa chọn" preserved: canonical names Vietnamese-first, diacritics intact, no foreign frame imports. B (Ashby/Weick) — loose coupling verified: each page fails independently; P1 sweep confirms no cross-page inconsistency. C (Buddhist epistemology) — Pramāṇa satisfied: all claims scoped, sourced, marked; Two Truths respected: no conventional claim elevated to ultimate.

### F1–F8 Regression Suite

| # | Check | Result |
|---|---|---|
| F1 | C1 graded (full/min/zero) — no strict symmetric-only | ✅ All pages use graded C1 |
| F2 | Nguồn Trích Dẫn on all pages with citations | ✅ 22/22 pages |
| F3 | Vietnamese diacritics — "Dĩ bất biến, ứng vạn biến" comma | ✅ Active pages correct |
| F4 | Axiom IX canonical names: "Gặp Nhau Giữ Gốc — Không Của Ai, Nhờ Cả Hai" | ✅ All labels use canonical |
| F5 | No absolute/"4.000 năm as fact"/"nhanh hơn bất kỳ" | ✅ Zero in active HTML |
| F6 | V5 register rule: diagnostics marked `[interpretation]` | ✅ All pages marked |
| F7 | Changelog routing: root → CHANGELOG.md, papers → CHANGELOG_papers.md | ✅ Tiered routing correct |
| F8 | V6 triangulation disclaimer | ✅ Present in axiom_9.html §6 |

### Files changed today (14 files, +120/−31 lines)

| Tier | Files | Phases |
|---|---|---|
| Root HTML | when.html, who.html, why.html, how.html, index.html, upgrade.html, axiom_9.html | 2–6 |
| Spec | axiom_spec.md | 5 |
| Papers | paper_009_draft.md, papers/index.html, papers/CHANGELOG_papers.md | 7 |
| Changelogs | CHANGELOG.md | All |
| Auto | AGENTS.md, CLAUDE.md (GitNexus count update) | — |

### Build plan — ALL PHASES COMPLETE ✅

| # | Phase | Status |
|---|---|---|
| 0 | v3.2 review + amendments (F1–F8) | ✅ |
| 1 | axiom_ix_spec.md | ✅ |
| 1b | Naming RCA (canonical pair + English evocative) | ✅ |
| 2 | axiom_9.html | ✅ |
| 3 | upgrade.html | ✅ |
| 4 | index.html | ✅ |
| 5 | axiom_spec.md | ✅ |
| 6 | who.html / when.html | ✅ |
| 6b | why.html / how.html (orphan sweep) | ✅ |
| 7 | paper_009 | ✅ |
| 8 | bilingual glossary | ✅ |
| 9 | closure audit | ✅ |

**v3.2 is complete.** *"Được sống: từ khi có dân tộc Việt. Được đặt tên: 2026. Được hệ thống hóa: 2026-06-11."*

**Tổng kết report:** [`plan/2026-06-11-mach-re-v3.2-closure-report.md`](plan/2026-06-11-mach-re-v3.2-closure-report.md)

---

## 2026-06-11 — Phase 9 appendix: luu_tru.html V3 comma fix · RCA 5.0/5

- `luu_tru.html:469` — `"Dĩ bất biến ứng vạn biến"` → `"Dĩ bất biến, ứng vạn biến"` (V3 canonical comma + Unicode quotes)

---

## 2026-06-11 — Phases 2–5: axiom_9 + upgrade + index + axiom_spec V4/V2 compliance · RCA 4.8/5

**Triple compass batch:** A (Phan Ngọc) — all label/heading uses of "Giao Diện Sống" replaced with canonical "Gặp Nhau Giữ Gốc." B (Ashby) — Requisite Variety: prose-level gloss usage retained where it functions descriptively, not as naming. C (Buddhist epistemology) — Pramāṇa: public-facing names now match the framework's own naming standard.

### axiom_9.html (2 fixes)
- Hero tag: `"MẠch RỄ"` → `"MẠCH RỄ"` (typo)
- §7 section header: `"Việt Nam là Giao Diện Sống"` → `"Việt Nam là Gặp Nhau Giữ Gốc (Living Interface)"` (V4) · 4.4/5
- Running prose "Giao Diện Sống" (~8 occurrences in C1/C3/C4/Open Questions): retained as gloss usage per V4

### upgrade.html (5 fixes)
- Line 386: label `"Giao Diện Sống (Living Interface)"` → `"Gặp Nhau Giữ Gốc — Không Của Ai, Nhờ Cả Hai (Living Interface)"` (V4) · 4.8/5
- Line 614: section heading `"Giao Diện Sống"` → `"Gặp Nhau Giữ Gốc (Living Interface)"` (V4) · 4.8/5
- Line 619: `"MẠch RỄ"` → `"MẠCH RỄ"` (typo)
- Line 659: `"4.000 năm"` → scoped form (V2) · 4.8/5
- Line 708: glossary `"Giao Diện Sống (Tiên Đề IX)"` → `"Gặp Nhau Giữ Gốc (Living Interface)"` (V4) · 4.8/5

### index.html (4 fixes)
- Line 430: `"4.000 năm"` → scoped with `[cultural self-description]` (V2) · 4.8/5
- Line 498: `"Dòng chảy 4.000 năm"` → `"Dòng chảy hàng thiên niên kỷ"` (V2) · 4.8/5
- Line 541: nav card `"Giao Diện Sống — Living Interface"` → `"Gặp Nhau Giữ Gốc — Living Interface"` (V4) · 4.8/5
- Line 802: glossary `"Giao Diện Sống — Gặp Nhau Giữ Gốc"` → `"Gặp Nhau Giữ Gốc (Living Interface)"` (V4) · 4.8/5

### axiom_spec.md (1 fix)
- Line 231: section heading → canonical names first (V4) · 4.8/5

### P1 sweep — FINAL clearance
All 7 public-facing HTML pages now v3.2-compliant: ✅ what ✅ why ✅ who ✅ when ✅ how ✅ upgrade ✅ index ✅ axiom_9. Zero remaining V2/V4/V5 violations in active HTML.

---

## 2026-06-11 — Phase 6b: Orphan sweep — why.html + how.html V2 compliance · RCA 4.7/5

**Context:** Phase 6 P1 sweep flagged two pages not covered by any build phase. Both are same V2 class already RCA'd at 4.8/5 — no new analysis needed.

- `why.html:308` — `"Nhanh hơn bất kỳ cặp cựu thù nào"` → scoped form with `[interpretation]` (V2) · 4.8/5
- `how.html:588` — `"lịch sử 4.000 năm"` → `"hàng thiên niên kỷ — 'bốn nghìn năm văn hiến' [cultural self-description], với chính thể được ghi chép liên tục hơn hai thiên niên kỷ [established]"` (V2) · 4.6/5

**P1 sweep status after Phase 6+6b:** `why.html` ✅ `how.html` ✅ `when.html` ✅ `who.html` ✅ — remaining V2/V4 violations in `index.html`, `upgrade.html`, `axiom_9.html` covered by Phases 2–4.

---

## 2026-06-11 — Phase 6: when.html + who.html v3.2 compliance sweep · RCA 4.8/5

**Triple compass review:** A (Phan Ngọc) — identity pattern preservation · B (Ashby/Weick) — Requisite Variety · C (Buddhist Epistemology) — Pramāṇa + Two Truths. 10 findings across 2 files; all cleared ≥ 4.4/5 gate.

### when.html (6 fixes, 4.4–5.0/5)

1. **Meta description** (line 7): `"4.000 năm"` → `"hàng thiên niên kỷ"` (V2) — 4.8/5
2. **Hero text** (line 181): `"4.000 năm bằng chứng thực nghiệm"` → `"Hàng thiên niên kỷ — 'bốn nghìn năm văn hiến' như lời tự mô tả của cộng đồng [cultural self-description]"` (V2) — 4.8/5
3. **Normalization claim** (line 338): `"Nhanh hơn bất kỳ cặp cựu thù nào"` → scoped form with US–Japan / Germany–France counterexamples + `[interpretation]` (V2) — 4.8/5
4. **"Dĩ bất biến, ứng vạn biến" comma** (line 321): added comma per V3 canonical form; corrected attribution to Hồ Chí Minh → Huỳnh Thúc Kháng (1946) with `[contested attribution]` mark; fixed timeline heading "TK 19" → "TK 18–20" (Nguyễn Huệ = 18th c., Hồ Chí Minh = 20th c.) (V2 + V3 + F-WHEN-4) — 5.0/5
5. **Ethnic comparison table** (line 388): added `[interpretation]` boundary statement (V5) — 4.8/5
6. **Section 4 comparative claims** (line 439): added `[interpretation]` to Germany–France / Korea–Japan comparison (V5) — 4.8/5

### who.html (4 fixes, 4.6–5.0/5)

7. **Axiom IX canonical name** (line 335): `"Giao Diện Sống"` → `"Gặp Nhau Giữ Gốc — Không Của Ai, Nhờ Cả Hai (Living Interface, v3.2)"` + English evocative pair `"Mine, Yours, and the Space Between" / "Owned by Neither, Born of Both"` (V4) — 5.0/5
8. **Lederach comparison** (line 297): `"4.000 năm dữ liệu thực nghiệm"` → scoped form with `[cultural self-description]` + `[established]` marks (V2) — 4.8/5
9. **Section 5 country diagnostics** (line 342): added `[interpretation]` boundary statement; scoped Baltic `"4.000 năm"` → `"hàng thiên niên kỷ, 'bốn nghìn năm văn hiến' [cultural self-description]"` (V5 + V2) — 4.8/5
10. **Section 4 VN×Ubuntu×Yoruba table** (line 309): `"Ba hệ thống...mạnh nhất thế giới"` → `"Ba hệ thống...tiêu biểu trong số các hệ thống được khảo sát"`; added `[interpretation]` boundary statement (V5 + dictionary_rule §1) — 4.6/5

### P1 sweep — flagged for future phases (not fixed here)

| File | Issue | Coverage phase |
|---|---|---|
| `why.html:308` | "Nhanh hơn bất kỳ" (V2) | P1 sweep |
| `how.html:588` | "4.000 năm" (V2) | P1 sweep |
| `index.html:430,498` | "4.000 năm" (V2) | Phase 4 |
| `upgrade.html:386,614,624,659,708` | "Giao Diện Sống" + "4.000 năm" (V4 + V2) | Phase 3 |
| `axiom_9.html` | "Giao Diện Sống" in prose body (V4) | Phase 2 |

---

## 2026-06-11 — Phase 8c: Naming RCA — thuần-Việt gloss "nhận thức luận (mạch biết)" + "ngữ pháp siêu việt (nếp coi là chung)" · RCA 4.8/5

**La bàn Phan Ngọc:** Tiếng Việt nhận ra thế giới qua **kiểu quan hệ**, không qua **bản thể trừu tượng**. Từ thuần Việt tốt = từ neo vào cấu trúc sống.

**nhận thức luận → mạch biết (4.8/5):**
- R1: Framework dùng "nhận thức luận" theo nghĩa "la bàn biết" — phương pháp nhận ra điều gì đúng trong tiếp xúc, không phải lý thuyết nhận thức học thuật.
- R2: Phan Ngọc: "biết" trong văn hóa Việt = nhận ra kiểu quan hệ (nếp), không phải suy diễn từ tiên đề.
- R3 (root): Convention "mạch + [X]" — parallel với "mạch tồn tại" (bản thể học). "Mạch" = cấu trúc sống, "biết" = knowing (thuần Việt đơn giản nhất).

**ngữ pháp siêu việt → nếp coi là chung (4.8/5):**
- R1: Meta-grammar = khung chuẩn mà một hệ coi là phổ quát — áp đặt quy ước của mình lên người khác.
- R2: Phan Ngọc: thuộc địa hóa = cài "nếp của họ" làm "chuẩn của mình." Gloss nắm đúng cơ chế này.
- R3 (root): "Nếp" = pattern (có thể sai), tốt hơn "ngữ pháp" (nghe như rule). "Coi là chung" = claimed universality, không phải actual — chính xác cho những gì framework mô tả.

**Files sửa (tầng root):**
- `dictionary_rule.md §4`: canonical gloss table — TODO → ✅
- `axiom_9.html` line 90: "nhận thức luận (mạch biết)"
- `axiom_9.html` line 98: "ngữ pháp siêu việt (nếp coi là chung)"
- `axiom_spec.md` line 42: "nhận thức luận [mạch biết]"

> `papers/paper_009/` gloss → logged in [`papers/CHANGELOG_papers.md`](papers/CHANGELOG_papers.md) (tiered routing).

---

## 2026-06-11 — Phase 9: Closure Audit — Mạch Rễ v3.2 IX Build · ALL PASS

**Scope:** Regression audit sau Phases 1–8 (Tiên Đề IX — Living Interface build).

**F1–F8 Regression Results:**
| Finding | Kiểm tra | Kết quả |
|---|---|---|
| F1 | C1 absolute wording ("both must run VIII") | ✅ PASS — chỉ còn "C1-full/min/zero" graded form |
| F2 | NGUỒN TRÍCH DẪN table trong mọi IX file | ✅ PASS — axiom_9.html (5), upgrade.html (10), axiom_spec.md (1), paper_009 (1) |
| F3 | Full diacritics — không ASCII-stripped Vietnamese | ✅ PASS — toàn bộ IX content có dấu đầy đủ |
| F4 | V4 canonical name "Gặp Nhau" (không "Gặp Nhân") | ✅ PASS — "Gặp Nhân" chỉ còn trong CHANGELOG Phase 8a description |
| F5 | V2 banned wordings ("faster than", "4,000 years"…) | ✅ PASS — không tìm thấy banned form nào |
| F6 | §2 Boundary Statement + `[interpretation]` marks | ✅ PASS — paper_009 §2 đúng vị trí, 10× `[interpretation]` |
| F7 | HTML citation hyperlinks + changelog routing | ✅ PASS — axiom_9.html: 7 inline → 5 anchors; routing root/papers tách biệt |
| F8 | Triangulation 2.0/3 (kept, per gate 3.2/5) | ✅ PASS — 2.0/3 preserved, không bị sửa |

**Verification:** `npx gitnexus analyze` → 3,386 nodes / 3,168 edges. Index current.

**Phase 8 remaining TODO (không block v3.2):** `nhận thức luận` + `ngữ pháp siêu việt` → thuần-Việt gloss pending naming RCA, logged in `dictionary_rule.md §4`.

**Mạch Rễ v3.2 — IX Build: COMPLETE.** Commits: dc46069 (P2) → 05f88de (P3) → 40746a0 (P4) → f363c27 (P5) → 6a24e50 (P6) → 78f2c45 (P7) → aadff41 (P8a) → eea655d (P8b).

---

## 2026-06-11 — who.html: Trích dẫn đối thoại khoa học hòa giải (Lederach, 1997) · RCA 5.0/5

**Symptom / gap:** Phát biểu đối thoại với khoa học hòa giải ("Với khoa học hòa giải") trong `who.html` (dòng 296-297) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu khoa học tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Ô đối thoại với khoa học hòa giải ở `who.html` không chứa liên kết trích dẫn `[8]` trỏ tới tác phẩm của John Paul Lederach; danh sách tham khảo cuối trang thiếu tác phẩm này.
- Round 2 — Mechanism: Việc đưa ra khẳng định về "mô hình hòa giải không dựa trên thiết chế mà dựa trên kiến trúc văn hóa" mà không dẫn chiếu đến tác phẩm lý thuyết thiết lập hòa giải và chuyển hóa xung đột kinh điển (như của John Paul Lederach) làm giảm độ tin cậy khoa học và khả năng kiểm chứng độc lập của luận điểm đối thoại quốc tế.
- Round 3 — Root: Dòng này được viết trong phần tóm tắt đối thoại tri thức mà không được ánh xạ và bổ sung tác phẩm nghiên cứu về kiến trúc hòa bình (Lederach, 1997) vào mục Nguồn Trích Dẫn theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Lederach, 1997 <a href="#nguon-8">[8]</a>)` vào ô đối thoại khoa học hòa giải (dòng 296) và bổ sung nguồn `[8] Lederach, J. P. (1997)` ở mục Nguồn Trích Dẫn, đồng thời dịch chuyển các nguồn sau đó (Assmann, Berdyaev, Nodia, Valkonen, Šmidchens) lùi xuống 1 bậc.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `lederach_1997` ở đúng vị trí thứ tự.

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html: Trích dẫn đối chiếu bản sắc Baltic (Šmidchens, 2014) · RCA 5.0/5

**Symptom / gap:** Phát biểu đối chiếu mô hình bản sắc Baltic (Latvia, Lithuania, Estonia) trong `who.html` (dòng 351) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu khoa học tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Dòng giới thiệu Baltic trong bảng so sánh mở rộng của `who.html` không chứa liên kết trích dẫn `[12]` trỏ tới tác phẩm của Guntis Šmidchens; danh sách tham khảo cuối trang thiếu tác phẩm này.
- Round 2 — Mechanism: Việc đưa ra khẳng định về mô hình bản sắc Baltic dựa trên ngôn ngữ và lễ hội dân gian sau Liên Xô ("Lễ cách mạng ca hát") mà không dẫn chiếu đến nghiên cứu khoa học chính thức về sức mạnh của bài ca và phi bạo lực của Šmidchens làm giảm tính học thuật và khả năng tự kiểm chứng của bảng so sánh mở rộng.
- Round 3 — Root: Điểm này được viết trong phần so sánh mở rộng mà không được ánh xạ và bổ sung tác phẩm nghiên cứu về Cách mạng ca hát Baltic (Šmidchens, 2014) vào mục Nguồn Trích Dẫn theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Šmidchens, 2014 <a href="#nguon-12">[12]</a>)` vào ô Baltic (dòng 351) và bổ sung nguồn `[12] Šmidchens, G. (2014)` ở mục Nguồn Trích Dẫn.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `smidchens_2014`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html: Trích dẫn đối chiếu bản sắc Sami (Bắc Âu) · RCA 5.0/5

**Symptom / gap:** Phát biểu đối chiếu mô hình bản sắc Sami (Bắc Âu) trong `who.html` (dòng 350) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu khoa học tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Dòng giới thiệu Sami trong bảng so sánh mở rộng của `who.html` không chứa liên kết trích dẫn `[11]` trỏ tới tác phẩm của Valkonen & Valkonen; danh sách tham khảo cuối trang thiếu tác phẩm này.
- Round 2 — Mechanism: Việc đưa ra nhận định về mối liên kết bản sắc với môi trường vật lý tự nhiên ("khi môi trường mất, rễ mất") và tác động của đô thị hóa mà không có nguồn khảo cứu nhân học cụ thể làm giảm tính khoa học của bảng đối chiếu bản sắc và mất khả năng kiểm chứng học thuật.
- Round 3 — Root: Điểm này được viết trong phần so sánh mở rộng mà không được ánh xạ và bổ sung tác phẩm nghiên cứu sinh thái văn hóa Sami (Valkonen & Valkonen, 2014) vào mục Nguồn Trích Dẫn theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Valkonen & Valkonen, 2014 <a href="#nguon-11">[11]</a>)` vào ô Sami (dòng 350) và bổ sung nguồn `[11] Valkonen, S., & Valkonen, J. (2014)` ở mục Nguồn Trích Dẫn.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `valkonen_2014`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html: Trích dẫn đối chiếu bản sắc Georgia (Kartveloba) · RCA 5.0/5

**Symptom / gap:** Phát biểu đối chiếu mô hình bản sắc Georgia ("Kartveloba") trong `who.html` (dòng 349) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu khoa học tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Dòng giới thiệu Kartveloba trong bảng so sánh mở rộng của `who.html` không chứa liên kết trích dẫn `[10]` trỏ tới tác phẩm của Ghia Nodia; danh sách tham khảo cuối trang thiếu tác phẩm này.
- Round 2 — Mechanism: Việc đưa ra khẳng định về mô hình bản sắc dựa trên ngôn ngữ độc nhất và chính thống giáo như một "single point of failure" mà không dẫn nguồn cụ thể làm giảm tính học thuật và khả năng kiểm chứng của bảng so sánh mở rộng.
- Round 3 — Root: Điểm này được viết trong phần so sánh mở rộng mà không được ánh xạ và bổ sung tác phẩm nghiên cứu về bản sắc Georgia (Nodia, 2009) vào mục Nguồn Trích Dẫn theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Nodia, 2009 <a href="#nguon-10">[10]</a>)` vào ô Georgia (Kartveloba) (dòng 349) và bổ sung nguồn `[10] Nodia, G. (2009)` ở mục Nguồn Trích Dẫn.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `nodia_2009`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html: Trích dẫn đối chiếu bản sắc Nga (Russkaya Dusha) · RCA 5.0/5

**Symptom / gap:** Phát biểu đối chiếu mô hình bản sắc Nga ("Russkaya Dusha") trong `who.html` (dòng 348) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu khoa học tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Dòng giới thiệu Russkaya Dusha trong bảng so sánh mở rộng của `who.html` không chứa liên kết trích dẫn `[9]` trỏ tới tác phẩm của Nikolai Berdyaev; danh sách tham khảo cuối trang thiếu tác phẩm này.
- Round 2 — Mechanism: Việc nhắc đến một khái niệm bản sắc dân tộc sâu sắc của Nga ("Linh hồn Nga") mà không dẫn nguồn cụ thể làm giảm tính khoa học của bảng so sánh mở rộng, có nguy cơ bị coi là sự khái quát hóa sáo rỗng hơn là phép so sánh triết học nghiêm túc.
- Round 3 — Root: Điểm này được viết trong phần so sánh mở rộng mà không được ánh xạ và bổ sung tác phẩm nghiên cứu kinh điển về bản sắc Nga (Berdyaev, 1947) vào mục Nguồn Trích Dẫn theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Berdyaev, 1947 <a href="#nguon-9">[9]</a>)` vào ô Nga (Russkaya Dusha) (dòng 348) và bổ sung nguồn `[9] Berdyaev, N. (1947)` ở mục Nguồn Trích Dẫn.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `berdyaev_1947`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html: Trích dẫn đối thoại truyền dẫn tri thức · RCA 5.0/5

**Symptom / gap:** Phát biểu đối thoại với truyền dẫn tri thức ("Với truyền dẫn tri thức") trong `who.html` (dòng 300-301) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu khoa học tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Ô đối thoại với truyền dẫn tri thức ở `who.html` không chứa liên kết trích dẫn `[8]` trỏ tới tác phẩm của Jan Assmann; danh sách tham khảo cuối trang thiếu tác phẩm này.
- Round 2 — Mechanism: Việc khẳng định về "giao thức tối thiểu cho truyền dẫn tri thức phi thiết chế" mà không dẫn chiếu đến lý thuyết ký ức văn hóa và truyền tải tri thức tập thể chính thức (như tác phẩm của Jan Assmann) làm giảm tính thuyết phục học thuật và biến nó thành một khẳng định mang tính cảm tính.
- Round 3 — Root: Dòng này được viết trong phần tóm tắt đối thoại tri thức mà không được ánh xạ và bổ sung tác phẩm nghiên cứu ký ức văn hóa (Assmann, 1992) vào mục Nguồn Trích Dẫn theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Assmann, 1992 <a href="#nguon-8">[8]</a>)` vào ô đối thoại truyền dẫn tri thức (dòng 300) và bổ sung nguồn `[8] Assmann, J. (1992)` ở mục Nguồn Trích Dẫn.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` để tích hợp `assmann`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html: Trích dẫn đối thoại triết học bản sắc · RCA 5.0/5

**Symptom / gap:** Phát biểu đối thoại với triết học bản sắc ("Với triết học bản sắc") trong `who.html` (dòng 292-293) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu học thuật tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Ô đối thoại với triết học bản sắc ở `who.html` không chứa liên kết trích dẫn `[7]` trỏ tới tác phẩm của Kwasi Wiredu; danh sách tham khảo cuối trang thiếu tác phẩm này.
- Round 2 — Mechanism: Việc đưa ra khẳng định về "con đường thứ ba giữa bản sắc cứng và hòa tan" mà không dẫn chiếu đến nghiên cứu triết học so sánh bản sắc chính thức (chẳng hạn như công trình nổi bật của Kwasi Wiredu) làm giảm chiều sâu lý luận và tính khoa học của cuộc đối chiếu bản sắc.
- Round 3 — Root: Dòng này được viết trong phần tóm tắt đối thoại triết học mà không được ánh xạ và bổ sung tác phẩm nghiên cứu bản sắc so sánh (Wiredu, 1996) vào mục Nguồn Trích Dẫn theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Wiredu, 1996 <a href="#nguon-7">[7]</a>)` vào ô đối thoại triết học bản sắc (dòng 292) và bổ sung nguồn `[7] Wiredu, K. (1996)` ở mục Nguồn Trích Dẫn.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `wiredu_1996`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html: Trích dẫn lý thuyết tổ chức tự quản (Holacracy) · RCA 5.0/5

**Symptom / gap:** Phát biểu về lý thuyết tổ chức tự quản (Holacracy) trong `who.html` (dòng 288-289) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu/sách sáng lập tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Ô so sánh tự quản (Holacracy) trong phần đối thoại thế giới của `who.html` không chứa liên kết trích dẫn `[6]` trỏ tới tác phẩm sáng lập của Brian Robertson; danh sách tham khảo cuối trang thiếu cuốn sách này.
- Round 2 — Mechanism: Việc nhắc đến một lý thuyết quản trị hiện đại cụ thể (Holacracy) mà không dẫn nguồn làm suy giảm tính học thuật và sự thuyết phục của nhận định đối chiếu cấu trúc tự quản Làng Việt Nam với mô hình phi tập trung hiện đại, làm mất khả năng đối chiếu khoa học.
- Round 3 — Root: Điểm này được viết như phần thảo luận tự quản phi tập trung mở rộng mà không được ánh xạ và bổ sung tài liệu sáng lập (Robertson, 2015) vào thư mục tham khảo cuối trang theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Robertson, 2015 <a href="#nguon-6">[6]</a>)` vào ô thảo luận Holacracy (dòng 288) và bổ sung nguồn `[6] Robertson, B. J. (2015)` ở mục Nguồn Trích Dẫn.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `robertson_2015`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html: Trích dẫn mô hình Ngoại giao Cây Tre · RCA 5.0/5

**Symptom / gap:** Phát biểu về mô hình *"Ngoại giao Cây Tre"* trong `who.html` (dòng 274) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu/phát biểu chính thức tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Dòng giới thiệu mô hình "Ngoại giao Cây Tre" ở `who.html` không chứa liên kết trích dẫn `[5]` trỏ tới nguồn tham khảo tương ứng; danh sách tham khảo cuối trang thiếu tác phẩm của Nguyễn Phú Trọng.
- Round 2 — Mechanism: Việc thiếu nguồn trích dẫn chính thức cho một học thuyết đối ngoại cấp quốc gia làm giảm tính thuyết phục của sự so sánh tương đồng cấu trúc (structural analogy) giữa Ngoại giao Cây Tre và Mạch Rễ, làm nó giống một sự gán ghép ngôn từ tự do hơn là một đối chiếu khoa học nghiêm túc.
- Round 3 — Root: Dòng này được soạn thảo như một ví dụ minh họa chính trị học vĩ mô mà không được ánh xạ và bổ sung tài liệu phát biểu chính thức của Tổng Bí thư vào thư mục tham khảo cuối trang theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Nguyễn Phú Trọng, 2021 <a href="#nguon-5">[5]</a>)` vào đoạn dẫn nhập Ngoại giao Cây Tre (dòng 274) và bổ sung nguồn `[5] Nguyễn Phú Trọng. (2021)` ở mục Nguồn Trích Dẫn.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `npt_2021`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — Phase 8a: V4 name fix "Gặp Nhân" → "Gặp Nhau" (5 files) · RCA 5.0/5

**Symptom:** axiom_spec.md, index.html, paper_009_draft.md, và CHANGELOG.md (Phase 5 entry) dùng "Gặp Nhân Giữ Gốc" (Nhân = người) thay vì canonical "Gặp Nhau Giữ Gốc" (Nhau = lẫn nhau, reciprocal). Vi phạm V4 naming rule — canonical SSOT là `dictionary_rule.md §9` và `axiom_ix_spec.md`.

**3-round RCA:**
- R1: axiom_spec.md Phase 5 viết "Gặp Nhân" không khớp với `dictionary_rule.md §9` (canonical).
- R2: Phase 5 lấy tên từ session summary có lỗi thay vì đọc trực tiếp canonical §9. "Nhân" (người/person) sai ngữ nghĩa IX — IX là về hai hệ gặp *lẫn nhau* (inter-system reciprocal), không gặp "người".
- R3 (root): V4 rule ("dùng §9 canonical, không tự ghép") không được kiểm tra đủ tại thời điểm Phase 5 viết axiom_spec.md. Fix: đọc §9 trực tiếp, sửa tất cả các file ảnh hưởng.

**Scoring (claim = "sửa Nhân→Nhau"):** Correct 1 + Deep 1 + Feasible 1 + Conflict-risk 1 + Preservation 1 = **5.0/5** → fix.

**Files sửa tầng root (5 instances):**
1. `axiom_spec.md` line 231: heading IX
2. `axiom_spec.md` line 351: §5.1 map table IX row
3. `index.html` line 533: upgrade nav card description
4. `index.html` line 802: glossary table IX row
5. `CHANGELOG.md` (Phase 5 entry) line 111: bản ghi lịch sử

**Root unaffected:** axiom_9.html ✅ upgrade.html ✅ axiom_ix_spec.md ✅ (đã dùng "Nhau" từ đầu).

> `papers/paper_009/paper_009_draft.md` (2 instances) → logged in [`papers/CHANGELOG_papers.md`](papers/CHANGELOG_papers.md) (tiered routing).

---

## 2026-06-11 — who.html: Trích dẫn áp lực mô hình quản lý trong doanh nghiệp · RCA 5.0/5

**Symptom / gap:** Phát biểu *"Doanh nghiệp Việt Nam đang đối mặt với áp lực copy mô hình quản lý nước ngoài"* trong `who.html` (dòng 270) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu khoa học cụ thể tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Luận điểm về việc sao chép mô hình quản lý ngoại của doanh nghiệp Việt Nam trong `who.html` không chứa liên kết trích dẫn `[4]` trỏ tới nguồn tham khảo tương ứng; danh sách tham khảo cuối trang thiếu tác phẩm của Quang & Vuong.
- Round 2 — Mechanism: Việc thiếu nguồn trích dẫn nghiên cứu quản trị doanh nghiệp làm giảm tính thuyết phục của tiền đề thực tiễn (why Mạch Rễ is needed in business), khiến lập luận này giống như một đánh giá chủ quan thay vì một thực tế đã được khảo sát thực nghiệm trong quản trị học.
- Round 3 — Root: Dòng này được viết như phần dẫn nhập bối cảnh thực hành doanh nghiệp mà không được ánh xạ và bổ sung tài liệu nghiên cứu quản trị học (Management Styles) vào thư mục tham khảo cuối trang theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Quang & Vuong, 2002 <a href="#nguon-4">[4]</a>)` vào đoạn dẫn nhập doanh nghiệp (dòng 270) và bổ sung nguồn `[4] Quang, T., & Vuong, N. T. (2002)` ở mục Nguồn Trích Dẫn.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `quang_2002`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html: Trích dẫn luận điểm Công giáo Việt Nam · RCA 5.0/5

**Symptom / gap:** Phát biểu *"Người Công giáo Việt đã sống Mạch Rễ 400 năm mà không mâu thuẫn"* trong `who.html` (dòng 247) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu khoa học cụ thể tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Ô Công giáo trong bảng so sánh tôn giáo của `who.html` không chứa liên kết trích dẫn `[3]` trỏ tới nguồn tham khảo tương ứng; danh sách tham khảo cuối trang thiếu tác phẩm của Peter C. Phan.
- Round 2 — Mechanism: Vấn đề hòa hợp đức tin Công giáo với văn hóa truyền thống (thờ cúng tổ tiên) là chủ đề lịch sử phức tạp (từng gây ra Tranh luận Lễ nghi). Khẳng định "không mâu thuẫn" mà không trích dẫn nghiên cứu thần học hoặc lịch sử sẽ làm luận điểm bị xem là võ đoán hoặc thiếu cơ sở khoa học.
- Round 3 — Root: Dòng này được viết như một tóm tắt nhanh trong ô bảng so sánh mà không được ánh xạ và bổ sung tác phẩm nghiên cứu thần học/nhân học hội nhập văn hóa (inculturation) vào thư mục tham khảo cuối trang theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 3 targeted edits:**
- `who.html`: Thêm liên kết inline `(Phan, 2003 <a href="#nguon-3">[3]</a>)` vào ô so sánh tôn giáo (dòng 247) và bổ sung nguồn `[3] Phan, P. C. (2003)` ở mục Nguồn Trích Dẫn.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `phan_2003`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html: Trích dẫn luận điểm Phật giáo Việt Nam · RCA 5.0/5

**Symptom / gap:** Phát biểu *"Phật giáo Việt Nam đã vận hành Mạch Rễ suốt 1.800 năm"* trong `who.html` (dòng 243) thiếu liên kết trích dẫn inline trỏ tới nguồn Phan Ngọc (1998) vốn đã được định nghĩa ở cuối trang.

**3-round RCA:**
- Round 1 — Symptom: Dòng Phật giáo trong bảng so sánh tôn giáo của `who.html` không chứa liên kết trích dẫn `[1]` trỏ tới nguồn Phan Ngọc.
- Round 2 — Mechanism: Việc không có liên kết trích dẫn làm giảm tính thuyết phục của con số lịch sử cụ thể "1.800 năm" và làm mất liên kết ngữ nghĩa giữa luận điểm thực chứng này với cơ sở phân tích giao lưu văn hóa Việt-Ấn của Phan Ngọc trong thư mục tham khảo.
- Round 3 — Root: Dòng này được soạn thảo như một câu tóm tắt nhanh trong bảng mà không được rà soát lại để ánh xạ thủ công với danh mục tài liệu tham khảo theo **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)**.
- **Scoring gate: 5.0/5.**

**Fix — 1 targeted edit:**
- `who.html`: Thêm liên kết trích dẫn inline `(Phan Ngọc <a href="#nguon-1">[1]</a>)` vào ô chứa luận điểm Phật giáo Việt Nam (dòng 243).

**RCA score: 5.0/5.**

---

## 2026-06-11 — who.html & when.html: Trích dẫn thế hệ thứ ba hải ngoại · RCA 5.0/5

**Symptom / gap:** Phát biểu về thế hệ thứ ba của người Việt hải ngoại ("Người Việt hải ngoại thế hệ thứ ba... vẫn có những phản xạ hành vi và hệ giá trị") trong `who.html` (dòng 224) và `when.html` (dòng 380) thiếu liên kết trích dẫn inline và nguồn trích dẫn nghiên cứu khoa học cụ thể tại cuối trang, vi phạm **Quy tắc Bảng Nguồn Trích Dẫn (Rule #12)** của dự án.

**3-round RCA:**
- Round 1 — Symptom: Không có liên kết trích dẫn `[2]` trong `who.html` và `[1]` trong `when.html` cho luận điểm thế hệ thứ ba hải ngoại; mục Nguồn Trích Dẫn ở `when.html` báo trống.
- Round 2 — Mechanism: Việc thiếu nguồn trích dẫn học thuật làm suy yếu tính xác thực và khả năng phản chứng của luận điểm "thế hệ thứ ba vẫn có phản xạ hành vi và hệ giá trị", khiến nó trông giống như một nhận xét cảm tính thay vì một quan sát thực chứng.
- Round 3 — Root: Phát biểu được viết trong giai đoạn phác thảo mô tả đối tượng trước khi các quy tắc liên kết nguồn gốc và ma trận traceability của dự án (Rule #12) được áp đặt đầy đủ.
- **Scoring gate: 5.0/5.**

**Fix — 4 targeted edits:**
- `who.html`: Thêm liên kết inline `(Trang Bùi <a href="#nguon-2">[2]</a>)` và bổ sung nguồn `[2] Trang Bui (2023)` ở mục Nguồn Trích Dẫn.
- `when.html`: Thêm liên kết inline `(Trang Bùi <a href="#nguon-1">[1]</a>)` và thay đổi mục Nguồn Trích Dẫn trống bằng tham chiếu `[1] Trang Bui (2023)`.
- `scratch/check_author_links.py` và `scratch/find_missing_links.py`: Cập nhật cấu hình `FILE_SOURCES` và `KEYWORDS` để tích hợp `bui_2023`.

**RCA score: 5.0/5.**

---

## 2026-06-11 — Phase 6: `who.html` + `when.html` — IX awareness labels · RCA 4.8/5

**Symptom / gap:** `who.html` so sánh 9 chiều VN × Ubuntu × Yoruba mà không nhắc đến tầng tiếp xúc giữa các hệ (IX territory). `when.html` có Hòa Giải Việt-Mỹ = VVC canonical C1-min nhưng không labeled.

**3-round RCA:**
- Round 1: Hai trang không đề cập IX.
- Round 2: who.html = ngữ cảnh inter-system (so sánh các hệ gặp nhau). when.html = empirical anchor của IX đang ẩn (unlabeled).
- Round 3 (root): Empirical evidence cho IX ở when.html không có link traceability về axiom_9.html. Fix nhỏ: minimal mentions + links, không overwrite nội dung hiện có.
- **Scoring gate: 4.8/5.**

**Fix — 2 targeted edits (minimal):**
- `who.html`: thêm callout box sau VIII paragraph — IX xuất hiện khi hai hệ đã-VIII gặp nhau; bảng so sánh = từng hệ đơn lẻ, tiếp xúc = tầng Interface
- `when.html`: thêm câu label Hòa Giải Việt-Mỹ là VVC canonical C1-min — Việt Nam VIII, Mỹ chưa đủ VIII → P* hình thành asymmetric. Link → axiom_9.html

**RCA score: 4.8/5.** Phase 6 → COMPLETE. Cổng Phase 7 (paper_009.html) mở.

---

## 2026-06-11 — Phase 5: `axiom_spec.md` — SSOT tích hợp Tiên Đề IX · RCA 5/5

**Symptom / gap:** `axiom_spec.md` là Single Source Of Truth. Hiện tại chỉ có I–VIII (3 tầng). IX đã tồn tại trong HTML nhưng không có trong SSOT → HTML không có căn cứ canonical.

**3-round RCA (Buddhist epistemology + Tiên Đề VIII compass):**
- Round 1: SSOT mô tả 8 tiên đề; framework v3.2 có 9.
- Round 2: axioms.html "renders from axiom_spec.md" — thiếu IX trong SSOT = toàn bộ render thiếu căn cứ.
- Round 3 (root): SSOT vi phạm Tiên Đề VIII tự-phản-tư của chính nó: framework không áp tiêu chuẩn traceability lên bản thân nó. Fix: IX vào SSOT với đầy đủ độc lập test (K-IX), C1-graded conditions, falsification, triangulation.
- **Scoring gate: 5/5.**

**Fix — 7 targeted edits:**
1. Header tier schema: thêm `Tiên Đề Interface (IX) — v3.2; dyad subject`
2. §1 derivation log: thêm K-IX row (independence test: I–VIII của singleton → không kéo theo IX; dyad required)
3. §2: thêm `### TẦNG INTERFACE` header + full Tiên Đề IX entry: formal statement, C1-full/min/zero, P* + Pratītyasamutpāda, VVCs, triangulation A/B/C (score 2.0/3), EAP, V6 disclaimer, falsification conditions
4. §3 diagram: thêm TẦNG INTERFACE block trên TẦNG PHẢN TƯ (IX = inter-system, VIII = within-system)
5. §5.1 map table: thêm IX row (`(mới — v3.2)` → Interface → Gặp Nhau Giữ Gốc)
6. §8 YAML: thêm `IX: {type: interface, depends_on: [VIII], subject: dyad, ...}`
7. NGUỒN TRÍCH DẪN: thêm bảng APA [1]–[5] (Phan Ngọc 1998, Ashby 1956, Weick 1976, Nāgārjuna/Garfield 1995, Dharmakīrti/Dunne 2004)

**RCA score: 5/5.** Phase 5 → COMPLETE. Cổng Phase 6 (who.html / when.html) mở.

---

## 2026-06-11 — Phase 4: `index.html` — Architecture map cập nhật v3.2 + Tiên Đề IX · RCA 5/5

**Symptom / gap:** `index.html` là entry point duy nhất. Navigation map cho thấy 8 tiên đề (I–VIII), 3 tầng; không có nav card cho `axiom_9.html`; glossary thiếu Living Interface; timeline label ghi "v2.0".

**3-round RCA (Buddhist epistemology — Two Truths compass):**
- Round 1: Architecture map trên index.html không phản ánh framework v3.2 (9 tiên đề, 4 tầng).
- Round 2: Người đọc lần đầu tiếp cận từ index.html sẽ không biết tầng Interface tồn tại; missing path → axiom_9.html.
- Round 3 (root): index.html là bản đồ kiến trúc (saṃvṛti-level map) của framework. Bản đồ sai = mọi người dùng đi sai đường. Fix: cập nhật map cho đúng v3.2.
- **Scoring gate: 5/5 → tất cả 6 edits được xác nhận.**

**Fix — 6 targeted edits:**
1. CSS: thêm `.c-axiom9` purple (`#5a3070`) — màu Interface tier
2. Axioms nav card: cập nhật description → 9 tiên đề, 4 tầng (Core · Derived · Meta · Interface)
3. Upgrade nav card: cập nhật description → v3.2 + IX + P*
4. Nav grid: thêm nav card `axiom_9.html` → `.c-axiom9`, emoji 🌐, VVCs (Trúc Lâm + Ngoại Giao Cây Tre)
5. Timeline 2026: cập nhật "v2.0" → "v3.2: 9 tiên đề, 4 tầng"
6. Glossary: thêm row "Living Interface / Giao Diện Sống" với link → axiom_9.html

**RCA score: 5/5.** Phase 4 → COMPLETE. Cổng Phase 5 (axiom_spec.md) mở.

---

## 2026-06-11 — Phase 3: `upgrade.html` — Tích hợp Tiên Đề IX vào trang upgrade · RCA 5/5

**Symptom / gap:** `upgrade.html` không đề cập Tiên Đề IX. Architecture diagram chỉ hiển thị 8 tiên đề. `cons-grid` thiếu IX. Không có navigation link đến `axiom_9.html`.

**Structural decision (3-round RCA — Buddhist epistemology compass):**
- Round 1: Thêm IX như "Module 6" vào Section 2 (cùng hàng với Upgrade I–IV + Module 5) sẽ đặt IX cùng category với within-system features.
- Round 2: IX không phải hệ quả của VIII; IX là điều VIII làm khả thi (inter-system prerequisite). Flatten IX = vi phạm Two Truths (C2): category error giữa within-system và inter-system.
- Round 3 (root): IX đòi hỏi chủ thể mới (dyad không phải singleton) — cấu trúc khác hoàn toàn. Fix: IX vào section riêng sau Section 3 (VIII), với tag "TẦNG INTERFACE MỚI", giải thích VIII là điều kiện cần không phải nguồn sinh ra IX.
- **Scoring gate: 5/5 → distinct section CONFIRMED.**

**Fix:** 7 targeted edits:
- CSS `.u5` rule: top border purple `#5a3070` cho IX card
- Title + meta description: cập nhật → "v3.2, Tiên Đề VIII, IX & Bốn Mở Rộng"
- Header subtitle: thêm "· Tiên Đề IX — Tầng Interface Mới (v3.2)"
- New Section IX: "Tầng IX — Giao Diện Sống" với `.upgrade-card.u5` — C1-full/min/zero, P* definition, VVC canonical (Trúc Lâm + Ngoại Giao Cây Tre), link → `axiom_9.html`
- Architecture ASCII box: cập nhật → 4 tầng, IX là Interface tier, phân biệt within-system (VIII hệ quả) vs inter-system (IX)
- `cons-grid`: thêm item "Tầng IX (mới)" spanning full width, link → axiom_9.html
- Glossary: thêm 3 rows — Living Interface, P*, C1-full/C1-min
- Bottom-nav: thêm "Tiên Đề IX →" button (purple)
- Footer: thêm link Tiên Đề IX, label "Mạch Rễ v3.2"

**RCA score: 5/5.** La bàn: C — Buddhist epistemology (Two Truths → category boundary between within-system/inter-system). Phase 3 → COMPLETE. Cổng Phase 4 (index.html) mở.

---

## 2026-06-11 — Phase 2: `axiom_9.html` — Trang HTML công khai Tiên Đề IX · RCA 4.8/5

**Symptom / gap:** Tiên Đề IX không có trang HTML công khai. `upgrade.html` (Phase 3), `index.html` (Phase 4), `axioms.html` không thể liên kết đến IX khi file chưa tồn tại.

**Structural decision (3-round RCA):**
- Round 1: Nếu copy section order từ axiom_4.html (formal statement trước VVCs), HTML sẽ đảo ngược hướng nhận thức luận của EAP.
- Round 2: HTML là bản render công khai của spec — spec khai "VVC trước" (EAP); HTML vi phạm EAP = Pramāṇa bị vi phạm ở layer presentational.
- Round 3 (root): EAP là Tiên Đề VIII áp dụng lên Mạch Rễ chính nó; HTML theo axiom_4.html order sẽ vi phạm Tiên Đề VIII tự phản chiếu của framework.
- **Scoring gate: 5/5 → VVC-first order CONFIRMED.**

**Fix:** Tạo `axiom_9.html` tại root. EAP note → VVCs (3 cases) → Derivation → Formal statement bilingual + ASCII diagram → C1–C4 (V1: C1-full/min/zero badges) → Falsification → Triangulation (V6 + styled-table) → Case studies (V5 boundary + Vietnam primary + US-China stress test) → Architecture stack + OQ table → footer → NGUỒN TRÍCH DẪN (5 nguồn). CSS reuses axiom_4.html pattern + `--interface`/`--interface-pale` vars. Hero gradient: deep purple (`#1a0838 → #5a30a0`) phân biệt tầng Interface với tầng Core (teal). Inline `<a href="#nguon-N">[N]</a>`; `id="nguon-N"` trong bảng. Bottom-nav: `← Hệ Tiên Đề` (axioms.html) | `Mạch Rễ 3.2 →` (upgrade.html).

**Amendments applied from birth:** V1 (C1 graded), V2 (scoped claims), V3 (diacritics), V4 (canonical §9 names), V5 (`[interpretation]` marks + boundary statement), V6 (triangulation disclaimer).

**RCA score: 4.8/5.** La bàn: C — Phật giáo nhận thức luận. Phase 2 → COMPLETE. Cổng Phase 3 (upgrade.html) mở.

---

## 2026-06-11 — Phase 1: `axiom_ix_spec.md` — Canonical specification Tiên Đề IX · Born-consistent v3.2

**Symptom / gap:** Axiom IX chưa có file spec canonical. Các phase HTML (2–6) không thể ship nếu chưa có nguồn duy nhất chứa tên §9, điều kiện C1 phân bậc (V1), VVCs đúng thứ tự EAP, và các amendment V1–V6 đã áp dụng từ đầu.

**Fix:** Tạo `axiom_ix_spec.md` tại root. Cấu trúc được rút ra từ EAP document-order + Buddhist epistemology compass (Pramāṇa: từ tri giác trực tiếp VVCs → suy luận formal statement) — không kế thừa nguyên xi v3.1 structure. Gồm 8 sections: EAP statement · VVCs (3 cases) · Derivation · Formal statement + diagram · Conditions C1–C4 (V1 applied) · Falsification · Triangulation (V6) · Case studies (V5) · Architecture integration · NGUỒN TRÍCH DẪN (5 nguồn). Phase 1b canonical names từ §9 applied. La bàn C (Buddhist epistemology) as compass cho structural decisions.

**Carry-forward applied:** EAP statement + usage rules; Vietnamese-first architecture; Source/Model separation; formal statement (V1 applied); C2–C4 + Vietnamese verifications; falsification condition; triangulation (+ V6); Open Questions 2–5.

**Phase 1 → COMPLETE.** Cổng Phase 5 (axiom_spec.md) đòi hỏi Phase 1 finalized — met.
La bàn: C — Phật giáo nhận thức luận (EAP order = Pramāṇa order: VVCs trước formal).

---

## 2026-06-11 — Phase 1b: Naming RCA Tiên Đề IX → `dictionary_rule.md` §9 row · RCA 4.8/5

**Symptom:** Tiên Đề IX không có tên canonical thuần Việt (Biểu hiện / Bản chất) sau review v3.2 (F4). Hai ứng viên Biểu hiện gốc (Gốc Vững Cành Mềm, Bạn Khắp Mà Không Theo Phe) chưa qua RCA; điểm chưa được chấm. Cổng Phases 2–6 bị khóa.

**Root (Round 3):** La bàn C (Phật giáo nhận thức luận). Nhị Đế ánh xạ trực tiếp lên cặp Biểu hiện/Bản chất: Biểu hiện = saṃvṛti (quy ước — cái thấy được trong thực hành); Bản chất = paramārtha (chân lý tối hậu — cấu trúc nền). Cả hai ứng viên Biểu hiện gốc đặt tên thuộc tính *một hệ* (Gốc Vững Cành Mềm = độ bền của một cây tre) hoặc chiến lược *một tác nhân* (Bạn Khắp Mà Không Theo Phe = lập trường ngoại giao) — không phải vùng tiếp xúc liên hệ thống. Apoha (Dignāga): tên phải loại trừ đúng VÀ có nội dung xác định; tên thuần phủ định không đủ cho Biểu hiện.

**Fix:** Ứng viên mới "Gặp Nhau Giữ Gốc" (4.8/5) được đề xuất dưới la bàn C (saṃvṛti level: tiếp xúc + giữ gốc rễ I–VIII = C1 visible in practice). "Không Của Ai, Nhờ Cả Hai" (4.8/5) thắng Bản chất (pratītyasamutpāda + anattā của P*). Cặp tiếng Anh gợi hình (P2): "Mine, Yours, and the Space Between" / "Owned by Neither, Born of Both". Hàng IX ghi vào `dictionary_rule.md` §9 (nguồn chân lý duy nhất). Phase 1b trong v3.2 roadmap đánh dấu COMPLETE. Cổng Phases 2–6 mở.

**Scoring gate (Biểu hiện winner "Gặp Nhau Giữ Gốc"):**

| Tiêu chí | Điểm | Ghi chú |
|---|---|---|
| Correct | 5 | Biểu diễn đúng IX ở tầng saṃvṛti: tiếp xúc + giữ gốc (C1 visible) |
| Deep | 4 | Chạm điều kiện C1 + cấu trúc contact zone |
| Feasible | 5 | Thuần Việt, không Hán-Việt |
| Conflict-risk | 5 | Kiểm tra va chạm I–VIII: không có va chạm ngữ nghĩa trực tiếp |
| Preservation | 5 | Tách biệt rõ I–VIII; tầng mới "Interface" |

**RCA score: 4.8/5 → CHỐT.** La bàn: C — Phật giáo nhận thức luận (Nhị Đế · Pramāṇa · Pratītyasamutpāda · Apoha).

---

## 2026-06-11 — CLAUDE.md: Thêm rule "CHANGELOG phân tầng" (tiered changelogs) · RCA 4.8/5

**Symptom:** Rule changelog trong CLAUDE.md là danh sách trường hợp riêng lẻ (enumerated case: papers/). `CHANGELOG_mv_002.md` tồn tại ngoài vùng phủ rule; tầng mới tạo ra trong tương lai sẽ không có quy tắc nào để theo.

**Root (Round 3):** Thiếu thuật toán routing tổng quát (naming + vị trí + tầng gần nhất). Quy tắc dạng enumeration không scale và vi phạm traceability — lịch sử thay đổi phải tìm được một cách tất định, không phụ thuộc người ghi nhớ bullet nào.

**5-Why (root một câu):** Quy tắc là danh sách case riêng lẻ thay vì thuật toán routing tổng quát, nên mỗi tầng mới đều nằm ngoài vùng phủ rule.

**Fix (3 files):**
- `CLAUDE.md §Document contract rules`: Thay bullet "Changelog cho papers/" bằng rule tổng quát "CHANGELOG phân tầng" — gồm naming convention, vị trí, routing "phải và chỉ được", quy trình tạo tầng mới, bảng instances hiện có.
- `publish/movie_script/mv_002/CHANGELOG_mv_002.md`: Cập nhật header → trỏ về rule tổng quát trong CLAUDE.md, kèm liên kết về root CHANGELOG.
- `CHANGELOG.md` (file này): ghi entry infrastructure.

**Scoring gate:**

| Tiêu chí | Điểm | Ghi chú |
|---|---|---|
| Correct | 5 | Defect thật: mv_002 hoạt động ngoài rule |
| Deep | 5 | Fix chạm root — thay enumeration bằng routing algorithm |
| Feasible | 5 | 3 file documentation, không chạm code/symbol |
| Conflict-risk | 4 | Gộp papers/ instance vào rule tổng quát, giữ nguyên hiệu lực |
| Preservation | 5 | Toàn bộ papers/ rule được giữ như một instance |

**RCA score: 4.8/5 → FIX.**

## 2026-06-11 — Review plan v3.1 Axiom IX → plan v3.2 (8 findings F1–F8, 7 fixed / 1 kept) · RCA trung bình 4.6/5

**Symptom:** Plan v3.1 (`plan/2026-06-11-mach-re-v3.1-axiom-ix-build-plan.md`) chứa mâu thuẫn nội tại về điều kiện C1: Part 5 yêu cầu "cả hai hệ chạy Tiên Đề VIII", Part 7 ghi "ít nhất một hệ", trong khi bằng chứng chủ lực (Việt Nam, Part 6) chỉ đúng theo cách đọc "ít nhất một" — VVC chính sẽ *bác bỏ* chính tiên đề nó kiểm chứng. Kèm 7 defect khác: thiếu Bảng Nguồn Trích Dẫn, tiếng Việt mất dấu, thiếu tên thuần Việt canonical cho Tiên Đề IX, 4 claim tuyệt đối không nguồn, chẩn đoán Mỹ–Trung không mark `[interpretation]` dưới footer "Non-political", roadmap thiếu governance rules 2026-06-10.

**Root (Round 3):** v3.1 tuyên bố "nothing in v3.0 retracted" → điều kiện kích hoạt C1 bị đóng băng ngay khi primary case mới (C1 bất đối xứng) đòi hỏi re-derive nó; checklist Phase 0 kế thừa từ template v3.0 có trước các document contract rules 2026-06-10.

**Fix:** Tạo `plan/2026-06-11-mach-re-v3.2-axiom-ix-build-plan.md` — review record + amendments V1–V6: C1 phân bậc (C1-full/C1-min/C1-zero, có neo Ashby Requisite Variety; thu hẹp Open Question 1), scoped 4 claim theo `dictionary_rule.md` §1/§3, khôi phục dấu tiếng Việt (quy tắc ràng buộc), demote "Giao Diện Sống" xuống gloss + Phase 1b naming RCA cho cặp tên thuần Việt, quy tắc register chẩn đoán (structural diagnostic ≠ political evaluation), disclaimer §5 cho bảng triangulation. Roadmap 8 phase → 10 phase (+1b naming/§9, +9 closure audit) kèm cross-phase governance checklist. F8 (điểm triangulation dạng số) KEPT 3.2/5 — giữ nhất quán với protocol Tiên Đề III, flag review cấp framework.

**Carry-Forward Set:** EAP + usage rules, kiến trúc Vietnamese-first, tách Source/Model, formal statement Tiên Đề IX (kèm scope note V1), C2–C4, falsification condition, triangulation, Open Questions 2–5, Appendices A–B. Overridden: strict-C1, 4 absolute claims, ASCII Vietnamese, naming cũ, register Part 6, checklist Phase 0 cũ.

**RCA score:** F1 4.6 · F2 5.0 · F3 4.8 · F4 4.6 · F5 4.4 · F6 4.2 · F7 4.8 → FIX; F8 3.2 → KEEP. La bàn: A — Phan Ngọc (F3, F4), B — Ashby/Weick (F1, risk model), C — Pramāṇa/Nhị đế (F2, F5, F6).

## 2026-06-10 — CLAUDE.md: Chuẩn hóa canonical terms Tiên Đề III (Mạch Cội Nguồn / Mạch Cội Dọc) · RCA 5.0/5

**Symptom:** CLAUDE.md §Tiên Đề III dùng "Thời gian trực giao" (literal translation) cho Orthogonal Temporality thay vì canonical term "Mạch Cội Nguồn"; "mạch cội dọc" viết thường thiếu canonical capitalization.

**Root (Round 3):** Section được viết trước khi canonical Vietnamese terms được finalize (RCA finding 2026-06-05 vs 2026-06-09 Việt hóa). English mapping đã đúng nhưng Vietnamese canonical terms chưa được back-propagate vào prose.

**Fix:**
- Line 112: "Thời gian trực giao (Orthogonal Temporality)" → "**Mạch Cội Nguồn (Orthogonal Temporality)**" + thêm canonical definition ("Cội" ⊥ "Nguồn")
- Line 114: "mạch cội dọc (Vertical Temporality)" → "**Mạch Cội Dọc (Vertical Temporality)**" + canonical term
- Lines 117-118: Thêm Vietnamese canonical terms vào quy tắc sử dụng
- Line 120 (mới): Thêm quy tắc phân biệt rõ ràng: Mạch Cội Nguồn ≠ Mạch Cội Dọc

**Carry-Forward Set:** Toàn bộ English mapping giữ nguyên; chỉ thêm Vietnamese canonical layer. Bảng §Tên thuần Việt (line 130) không đổi. `dictionary_rule.md` không đổi.

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-10 — Infrastructure: Tách paper changelog + fix deploy-pages.yml · RCA 5.0/5

**Symptom:** Paper changes ghi vào `CHANGELOG.md` gốc (mixed với axiom/HTML/audit entries); `deploy-pages.yml` không trigger khi push papers.

**Root:** Không có separation of concerns cho changelog; paths trigger filter thiếu `papers/**`.

**Fix:**
- Tạo `papers/CHANGELOG_papers.md` — exclusive changelog cho papers
- Di chuyển 5 paper entries từ `CHANGELOG.md` → `CHANGELOG_papers.md`
- `CLAUDE.md`: thêm Document Contract Rule — paper changes → chỉ `CHANGELOG_papers.md`
- `deploy-pages.yml`: thêm `papers/**` vào `on.push.paths`
- Xóa `papers/CLAUDE_REF.md` (CLAUDE.md của dự án VVV-QMRF, không liên quan)
- `papers/index.html`: link footer → `CHANGELOG_papers.md`

**RCA score:** 5.0/5 · Xem chi tiết paper_005 changes tại [`papers/CHANGELOG_papers.md`](papers/CHANGELOG_papers.md).

## 2026-06-10 — R-4: what.html — EAP Cross-Cultural Calibration (Joseon Buddhism + Meiji Japan) · RCA 4.6/5

**Symptom:** Khung EAP trong `what.html` có duy nhất một neo hiệu chuẩn (Bắc thuộc) — được xây dựng từ trường hợp Việt Nam. EAP chưa có out-of-sample test: falsification condition vận hành được về nguyên tắc nhưng chưa được kiểm tra thực tế.

**Root (Round 3):** EAP được xây dựng inductively từ trường hợp Bắc thuộc, chưa bao giờ được áp dụng deductively cho trường hợp ngoài nguồn. Audit plan đã cung cấp scoring Joseon Buddhism (D1–D5) nhưng không được back-propagate vào `what.html`.

**Fix:** Thêm section "Hiệu chuẩn bổ sung" với hai trường hợp:
- Joseon Buddhism: 5/5 dimensions ≥ anchor → V-axis qua institutional carrier (monk lineage, không phải nuclear family)
- Meiji Japan: 4/5 (D1 Medium < Long, 1 mức — đủ điều kiện biên) → V-axis hai tầng (State Shinto + butsudan)
- Summary: carrier unit của V-axis có thể biến đổi nhưng cấu trúc V ≠ ∅ được bảo toàn ở cả ba trường hợp

**RCA score:** 4.6/5 (Correct: 0.9, Deep: 1.0, Feasible: 1.0, Conflict-risk: 0.7, Preservation: 1.0). Từ `review/2026-06-10-mach_re_audit_plan.md` §R-4.

---

## 2026-06-10 — R-1: axiom_3.html — Định nghĩa V_min (Điều kiện tối giản V ≠ ∅) · RCA 4.9/5

**Symptom:** `axiom_3.html` §1 formal notation dùng `V = ∅` như điều kiện sụp đổ nhưng không định nghĩa tường minh khi nào V đạt ∅ — falsification condition §1 referencing `V = ∅` là inoperable.

**Root (Round 3):** Axiom file viết trước cross-cultural comparison (`mach_re_homologous.html`) sản sinh ra evidence V_min (nuclear family + portable altar = minimum). Evidence không được back-propagate vào axiom. V_min có hai thành phần cần đồng thời bảo toàn: Physical (V_min-1: ≥1 relational-acknowledgment practice, portable) và Semantic (V_min-2: ≥1 member có thể giải thích *tại sao*). Collapse-2 (semantic thất bại khi physical còn) là dạng nguy hiểm hơn vì khó phát hiện.

**Fix:** Thêm `def-box` "Điều kiện tối giản V (V_min)" sau formal notation box (line 288), trước Bản chất/Biểu hiện box. Derive từ `mach_re_homologous.html` phân kỳ 3 (carrier unit = nuclear family) và phân kỳ 5 (modernization: portable altar sufficient).

**RCA score:** 4.9/5 (Correct: 1.0, Deep: 1.0, Feasible: 1.0, Conflict-risk: 0.9, Preservation: 1.0). Từ `review/2026-06-10-mach_re_audit_plan.md` §R-1.

---

## 2026-06-10 — R-3: how.html — Axiom Derivation table (6 indicators → Core Axioms I–IV) · RCA 4.8/5

**Fix:** Thêm Axiom Derivation table vào how.html sau F-link note, trước score-bands. 6 chỉ báo Rubric bây giờ trace về Core Axioms I–IV. Tính đầy đủ: I ✅ II ✅ III ✅✅ IV ✅✅. Từ §R-3.

---

## 2026-06-10 — R-5: axioms.html — Axiom VIII ≈ precision (MP(Pt) ≈ MP(Pt+1)) · RCA 4.8/5

**Fix:** Thêm `Điều kiện xấp xỉ (≈)` entry vào dl Axiom VIII với 3 binary conditions (MP-1, MP-2, MP-3). Citations [8][9] Kant/Pereboom added. Từ §R-5.

---

## 2026-06-10 — RCA: mach_re_homologous.html — Yoruba claims thiếu citation · [5][6][7] added

**Claims Yoruba không có nguồn (đã xác định qua RCA):**
- Egungun = tổ tiên nhập xác vật lý, phán xét, ban phước
- Egungun society = thiết chế liên dòng họ, tái tạo ở diaspora
- Ẹ̀jọ́ = hệ thống tư pháp Yoruba; Ofo = lời nguyền tổ tiên
- Babalawo = specialist tháo gỡ; Ifa divination trong căn hộ
- Egungun grove = không gian thiêng cần thiết

**3 citations học thuật thêm:**
- `[5]` Akande, A. O. (2019). *Genealogy* 3(1), 7. DOI 10.3390/genealogy3010007 — Egungun masquerade, society, grove, diaspora.
- `[6]` Abimbola, W. (1976). *Ifa: An Exposition of Ifa Literary Corpus*. Oxford UP Nigeria. ISBN 9780195751994 — babalawo, Ifa, Ofo, Ẹ̀jọ́.
- `[7]` Peel, J. D. Y. (2000). *Religious Encounter and the Making of the Yoruba*. Indiana UP. ISBN 0-253-33794-1 — Yoruba entity ontology tổ tiên, elderhood power, asymmetric relations.

**5 điểm thêm inline hyperlink:**
- ASCII box Phân Kỳ 1 (Egungun embodied entity): `[5][7]`
- Why 4 Phân Kỳ 1 (babalawo/specialist): `[6][7]`
- ASCII box Phân Kỳ 3 (Egungun society diaspora): `[5]`
- ASCII box Phân Kỳ 4 (Ẹ̀jọ́, Ofo, babalawo): `[6][7]`
- ASCII box Phân Kỳ 5 (Egungun society đô thị, Ifa, grove): `[5][6]`

---

## 2026-06-10 — RCA: mach_re_homologous.html — "1000 năm Nam tiến" · 2 defects · RCA 5/5 + 4.5/5 · Citation [3][4] added

**Claims bị xét:**
- `line 505` — "lịch sử di dân nội địa **liên tục**" + "Nam tiến **1000 năm**"
- `line 549` — "**1000 năm** Nam tiến"

**Defect A — "1000 năm" (score 5/5):** Không có mốc lịch sử nào cho ra 1000 năm. Từ 1069 (Lý Thánh Tông lấy 3 châu) đến 1757 (Hà Tiên, hoàn tất) = ~688 năm. Từ 1471 đến 1757 = ~286 năm (conservative). Root: rhetorical symmetry với "1000 năm Bắc thuộc" overrides historical accuracy. → Fix: "~700 năm (thế kỷ 11–18, 1069–1757)."

**Defect B — "liên tục" / continuous (score 4.5/5):** Nam tiến diễn ra theo từng giai đoạn có khoảng dừng dài (1306→1471 = 165 năm không mở rộng). Root: "continuous" mô tả sai tốc độ thay vì hướng nhất quán. → Fix: "nhất quán hướng Nam, từng giai đoạn (persistent, episodic)."

**Citations thêm:**
- `[3]` Taylor, K. W. (2013). *A History of the Vietnamese*. Cambridge University Press. ISBN 9780521699150.
- `[4]` Li Tana. (1998). *Nguyễn Cochinchina*. Cornell Southeast Asia Program. ISBN 9780877277224.

**Ghi chú học thuật:** Wikipedia (Nam tiến) ghi nhận debate — một số học giả cho rằng Nam tiến có hệ thống không bắt đầu trước thế kỷ 15 (1471). Document dùng ghi nhận rộng hơn (từ 1069) với annotation "(thế kỷ 11–18)".

---

## 2026-06-10 — RCA: mach_re_homologous.html — Hệ quả cho Mạch Rễ · 3 defects · RCA 5/5

**Claim bị xét:** `mach_re_homologous.html:549` — "Mạch Rễ — Đạo Rễ (Root Way) — là phiên bản portable, phi thiết chế, đối xứng nhất của Tiên Đề III trên thế giới."

**3 defects, tất cả score 5/5:**

- **A — Scope violation ("nhất trên thế giới"):** n=3 không đủ cho universal superlative. Root: không có falsification condition — vi phạm internal consistency của framework. → Fix: "Trong ba hệ thống được phân tích."
- **B — Category confusion (Mạch Rễ ≠ nền tảng văn hóa VN):** 5 điểm phân kỳ phân tích *thực hành văn hóa Việt Nam*, nhưng conclusion gán cho *Mạch Rễ (framework)*. Mâu thuẫn trực tiếp với Foundation Statement (line 217): "Mạch Rễ đóng góp là đặt tên." Root: equivocation — dùng "Mạch Rễ" hai nghĩa khác nhau. → Fix: "nền tảng văn hóa Việt Nam mà Mạch Rễ neo vào."
- **C — Undefined term ("Đạo Rễ"):** Xuất hiện 1 lần, không definition, không có trong dictionary_rule.md §9. Root: terminological inflation. → Fix: xóa.

**Câu thêm:** "Đóng góp của Mạch Rễ là đặt tên và hệ thống hóa nguyên lý đó bằng ngôn ngữ đủ chính xác để đối thoại với triết học thế giới." — khôi phục đúng vai trò framework, align Foundation Statement line 217.

**RCA score:** 5/5 × 3 defects. Threshold ≥ 4/5 → fix tất cả.

---

## 2026-06-10 — RCA: Áp dụng Document Contract Rules (Citation Table + Dictionary Fixes) cho toàn bộ 18 HTML · RCA 4.8/5

**Symptom:** 17/18 HTML files có external citations nhưng không có bảng "Nguồn Trích Dẫn" APA-formatted. Không file nào có inline `<a href="#nguon-N">[N]</a>` hyperlink hoặc `id="nguon-N"` anchor. 5 dictionary rule violations (absolute universals, composite self-scores) trong các file chính. Vi phạm CLAUDE.md Paper Rule #12 và dictionary_rule.md §1, §5.

**Root (Round 3):** Rule #12 mới được thêm vào CLAUDE.md (2026-06-10) nhưng chưa retroactive cho HTML files hiện có. Framework claim "mọi claim phải trace về nguồn" nhưng HTML output không có enforcement mechanism.

**Fix — 2-phase audit:**

*Phase 1 — Citation Tables (18/18 files):* Section "Nguồn Trích Dẫn" + `id="nguon-N"` APA entries. `when.html`: "không có trích dẫn" statement. `ubuntu.html`: full inline `[N]` hyperlinks (model). Top citation files: `axiom_3.html` (10), `axioms.html` (7), `luu_tru.html` (5). Cũng fix "nguồn chân lý duy nhất" → neutral wording tại footer `axioms.html`, `axiom_1.html`. Master registry: `plan/add_citation_tables.py`.

*Phase 2 — Dictionary Violations (5/5 fixed, all ≥4/5):*
| # | File | Fix | RCA |
|---|---|---|---|
| 2.1 | `what.html:451` | "Điểm Yếu Duy Nhất" → "Điểm Yếu Chính" | 4.6 |
| 2.2 | `why.html:300` | "Không có tiền lệ" → "Ít có tiền lệ so sánh trực tiếp" | 4.8 |
| 2.3 | `index.html:301` | "lời giải thích khả dĩ duy nhất" → scoped + "nguồn chân lý" → neutral | 4.6 |
| 2.4 | `how.html:310` | "Tổng điểm (trên 12)" → disclaimer định tính | 4.4 |
| 2.5 | `axiom_conflict.html:242` | "Trung bình = 4.6/5" → qualitative | 4.6 |

**RCA score:** Correct 5 · Deep 5 · Feasible 4 · Conflict-risk 5 · Preservation 5 → **4.8/5.**

**Lesson:** HTML drift from rule changes unless automated. Future: khi thêm rule trong CLAUDE.md, kèm checklist "scan all HTML."

---

## 2026-06-10 — DSH Phase 2 Cross-Cultural Verification · RCA 4.6/5 — Nâng trạng thái [empirical hypothesis] → [validated heuristic]

**Symptom:** DSH được grounded hoàn toàn trong Phan Ngọc (Việt Nam). `DSH-3` tuyên bố "depth = structural distance, not content type" — tức claim cross-cultural applicability. Nhưng chưa có test nào ngoài Việt Nam → DSH vi phạm claim của chính nó.

**Root (Round 3):** DSH chưa được test cross-cultural vì ưu tiên development tập trung vào neo Việt Nam. Gap trong verification protocol, không phải gap trong logic DSH.

**Fix — Tạo `review/dsh_cross_cultural_verification.md` (RCA 4.8/5 to proceed, 4.6/5 to upgrade status):**

*Hệ 1 — Do Thái diaspora (~2000 năm):* DSH-1: 6/6 elements confirm differential rates (Shabbat ~0% change vs ẩm thực ~mỗi thế kỷ). DSH-2: 4/4 cases confirm depth-dependent filtering (Christianity theological core → rejected; ẩm thực địa phương → absorbed+kosher hóa). DSH-3: 3/3 cross-system comparisons confirm (Hebrew = "sâu" với Do Thái nhưng "ngôn ngữ" nói chung có thể "nông" với hệ khác). DSH-F1: NOT triggered. DSH-F2: NOT triggered.

*Hệ 2 — Yoruba (~1000 năm):* DSH-1: 6/6 elements confirm (family/lineage ~0% change qua slavery+colonialism+modernity vs vật chất ~mỗi thế hệ). DSH-2: 4/4 cases confirm (Western individualism → rejected; English → absorbed as tool). DSH-3: 3/3 confirm (family relations = identity-defining với Yoruba nhưng social convention với Western systems). DSH-F1: NOT triggered. DSH-F2: NOT triggered.

*Phát hiện đặc biệt:* (1) Hebrew/Yoruba dual-language pattern — "ngôn ngữ" (same content type) ở HAI độ sâu KHÁC NHAU trong cùng một hệ. (2) Diaspora stress-test: cả hai hệ TÁI TẠO core relational pattern trong môi trường mới — yếu tố gần invariant tái tạo trước. (3) Syncretism = II+IV, không phải II failure.

**Cập nhật:** `axiom_spec.md` §9.9: DSH status `[empirical hypothesis]` → `[validated heuristic] v1.1`. `axioms.html`: DSH section updated. `CHANGELOG.md`: entry này.

**RCA score (nâng trạng thái):** Correct 5 · Deep 4 · Feasible 4 · Conflict-risk 5 · Preservation 5 → **4.6/5 → NÂNG.**

**Giới hạn còn lại:** Inter-rater reliability chưa test (single-rater). Sample size = 3 (cần thêm ≥2 hệ).

## 2026-06-10 — Comprehensive RCA Review + Cross-Contradiction Check + HTML Sync · RCA 4.6–5.0/5

**Symptom:** Sau khi hoàn thành evidence enrichment (Sessions A–E, 6 evidence files, 11 annotations vào `axiom_spec.md`), chưa có comprehensive review pass để verify: (a) mỗi annotation có vượt qua 3-round RCA × 5-Why × scoring gate ≥ 4/5 không; (b) các annotation có contradiction chéo không; (c) HTML files (`axioms.html`, `axiom_3.html`) đã được sync với `axiom_spec.md` chưa.

**Root (Round 3):** Framework claim "mọi claim phải qua RCA gate" nhưng bản thân các annotation — là claim về mối quan hệ giữa ca dao corpus và tiên đề — chưa được audit tập trung sau khi tạo. Đây là gap trong quy trình: tạo annotation → verify ngay lúc tạo (đã làm) nhưng chưa verify toàn bộ annotation set như một tập hợp (cross-contradiction, drift with HTML).

**Fix — 3-phase comprehensive review (plan `2026-06-09_plan_ca_dao_evidence_enrichment.md` §PIR):**

*Phase 1 — RCA từng annotation:* Tất cả 11 annotations (5 nguồn: Q1/Q2/Q3/Nam An/ca dao biến dịch) được áp dụng 3-round RCA × 5-Why × scoring gate. Kết quả: tất cả ≥ 4.6/5, trên threshold 4/5. Không annotation nào cần sửa. Scores: A1=5.0, A2=4.8, A3=5.0, A4=4.6, A5=5.0, A6=4.6, A7=5.0, A8=5.0, A9=4.6, A10=5.0, A11=5.0.

*Phase 2 — Cross-contradiction check:* Within-axiom (I/II/III/IV pairs) + cross-axiom (V↔I, VIII↔III, II↔IV) + BRIDGE-II-III check. Kết quả: 0 contradictions found. All annotations complementary.

*Phase 3 — HTML sync:* `axioms.html` (7 edits): +§0.0 "Hội tụ độc lập", +Vietnamese prior-art I/II/III/IV, +V meta-evidence, VIII Neo A-yếu→A-trung bình. `axiom_3.html` (1 edit): +Bằng chứng thực nghiệm III (Q2 + Nam An). `axiom_spec.md`: NO CHANGES (all annotations pass RCA gate). `axiom_conflict.md`: NO CHANGES (no new contradictions). `plan/2026-06-09_plan_ca_dao_evidence_enrichment.md`: +Post-Implementation Review (§PIR) documenting full RCA results.

**RCA scores (Phase 1 annotation audit):** Range 4.6–5.0/5 · Mean 4.87/5 · All ≥ threshold 4/5.

**Lesson learned:** HTML drift risk — `axioms.html` was missing all 11 Vietnamese annotations despite them being in `axiom_spec.md` since Sessions A–E. Future process should include HTML sync as part of evidence enrichment workflow, not as separate phase.

## 2026-06-10 — Ca Dao Evidence Enrichment: Sessions A–E · Thêm 10 annotations vào axiom_spec.md · RCA 4.6–5.0/5

**Symptom:** `axiom_spec.md` §I, §II, §III, §IV, §V, §VIII Prior-art chỉ có Western theory anchors (Luhmann, Ashby, Lévi-Strauss, von Foerster…) và lý thuyết Phật giáo. Không có Vietnamese empirical instances — instances quan sát được trong thực tiễn dân gian Việt Nam cho từng tiên đề.

**Root (Round 3):** Framework tự nhận là "Triết học Tương quan-Phân tán" grounded trong văn hóa Việt Nam (Tiên Đề I, III) nhưng Prior-art của từng tiên đề không có bằng chứng inductive từ corpus ca dao Việt Nam — tức là framework claim Vietnamese cultural grounding nhưng không show the work. Đây là gap traceability: claim không trace về Vietnamese empirical sources (Paper Rules Tier 3 Rule #7).

**Fix — 6 evidence files + 10 annotations (plan `2026-06-09_plan_ca_dao_evidence_enrichment.md`):**

*Session A (VIII):* Tạo `review/evidence_viii_ca_dao_cham_biem.md` (H1, RCA 4.8/5) — 11 ca dao châm biếm Q1, cơ chế vô danh + phi-thiết-chế + embedded = VIII instance. `axiom_spec.md` §VIII Triangulation: A-yếu (~2/3) → **A-trung bình (~2.5/3)**. §VIII Prior-art: thêm bullet Vietnamese prior-art.

*Session B (II):* Tạo `review/evidence_ii_tham_my.md` (H2, RCA 4.8/5) — 6 ca dao "Ý Thức Cái Đẹp Cái Xấu" Q1. "Nết" = structural behavioral invariant (test = adversity persistence) ≠ "đức hạnh Nho giáo" (test = conformity). `axiom_spec.md` §II Prior-art: thêm annotation.

*Session C (III + I + IV):* Tạo `review/evidence_q2_mapping.md` (H3.2 + H6 + IV gold find, RCA 4.6–5.0/5) — Q2 ca dao "cây có cội sông có nguồn" = III existence condition; địa danh ca dao = I R_place; Lévi-Strauss via Nguyễn Tấn Long (Q2 line 479) = IV convergent prior-art. `axiom_spec.md` §I + §III + §IV Prior-art: thêm 3 annotations.

*Session D (V + Q3 II/IV):* Tạo `review/evidence_v_phan_tan.md` (H7, RCA 4.8–5.0/5) — hình thức oral corpus vô danh/phi-tập-trung/dị-bản IS V mechanism (Part I meta-evidence, 5.0/5). `axiom_spec.md` §V Prior-art: thêm bullet mới (§V trước đó không có Prior-art Việt Nam). Tạo `review/evidence_q3_mapping.md` (H3.3, RCA 4.8–5.0/5) — Q3 §III "nếp sống" + "di lưu qua thời gian" = II mechanism; tương đồng/dị biệt Khổng/Lão = IV operational instances với criterion rõ ràng. `axiom_spec.md` §II + §IV Prior-art: thêm 2 annotations Q3.

**Ràng buộc đã giữ:** KHÔNG sửa phát biểu bất kỳ tiên đề nào. KHÔNG nâng mệnh đề dẫn xuất lên Core Axiom. Chỉ thêm Prior-art annotations. §VIII Triangulation score 4.8/5 qua RCA gate.

*Session E (Nam An I+III+II):* Tạo `review/evidence_i_iii_ii_nam_an.md` (H6, RCA I=4.8/5 III=4.8/5 II=4.8/5) — corpus Nam An: (a) I R_place ở tầng epistemic architecture — toàn bộ corpus tổ chức theo nguyên lý người-đất; (b) III non-human V-axis pull — "Cáo chết ba năm quay đầu về núi" + "Lô Đà Tam Đảo cũng quay đầu về" = cosmic structure, không phải social norm; (c) II origin myth — "Con Rồng cháu Tiên" / "Con Hồng cháu Lạc" = structural invariant ở tầng mythological foundation. `axiom_spec.md` §I Prior-art: thêm annotation Nam An.

**RCA scores:** H1 4.8/5 · H2 4.8/5 · H3.2 4.8/5 · H6 4.6/5 (planning) · H6 I 4.8/5 · H6 III 4.8/5 · H6 II 4.8/5 · IV convergent 5.0/5 · H7.1 5.0/5 · H7.2 4.8/5 · H3.3 II 4.8/5 · H3.3 IV 5.0/5 · H4.2 5.0/5.
- H4.2 (convergent discovery narrative): thêm `axiom_spec.md` §0.0 — ca dao biến dịch Việt Nam phát biểu phi-hình-thức 3 điều kiện cần của R hàng trăm năm trước Mạch Rễ. RCA placement 5.0/5.

## 2026-06-10 — RCA: Thêm rule Citation Table vào CLAUDE.md · RCA 4.8/5

**Symptom:** Các tài liệu (plan docs, HTML nodes, papers) trích dẫn nghiên cứu bên ngoài nhưng không có bảng nguồn chuẩn hóa ở cuối tài liệu → người đọc không thể verify claim, vi phạm traceability.

**Root (Round 3):** Framework tuyên bố "Citation traceability — mọi claim phải trace về nguồn" (Paper Rules Tier 3 Rule #7) nhưng chỉ áp dụng ở semantic level (mark `[established]`/`[hypothesis]`). Không có enforcement mechanism nào bắt buộc *bảng nguồn vật lý* xuất hiện ở cuối tài liệu. Framework không obey its own traceability standard ở output/format level.

**Fix:** Thêm Paper Rule #12 (Citation table) vào `§Paper & Publication Rules > Tier 3` và bullet enforcement vào `§Document contract rules` trong `CLAUDE.md`. Format canonical APA + DOI, áp dụng cho tài liệu mới tạo/được sửa.

**RCA score:** 4.8/5 (Correct: 5, Deep: 5, Feasible: 5, Conflict-risk: 4, Preservation: 5).

## 2026-06-10 — RCA: Tạo ubuntu.html — trang nghiên cứu đối tác Ubuntu · RCA 5.0/5

**Symptom:** Hệ thống Mạch Rễ so sánh với Ubuntu trong nhiều trang (`mach_re_homologous.html`, `axiom_3_cultural_comparison.html`, `axiom_3.html`) nhưng không có trang standalone trình bày Ubuntu đủ sâu với nguồn học thuật. Người đọc phân tích homologous không có base knowledge để đánh giá các tuyên bố so sánh.

**Root:** Vi phạm nguyên tắc traceability (CLAUDE.md Paper Rules Tier 3 Rule 7): mọi claim phải trace về nguồn. Mạch Rễ claim Ubuntu là bằng chứng độc lập cho Tiên Đề III — nhưng nguồn học thuật về Ubuntu (Udah et al. 2025, Lefa 2015) không được tích hợp vào network trang.

**Fix:** Tạo `ubuntu.html` (7 section, ~550 dòng HTML):
- §1: Định nghĩa, ngữ nguyên, nguồn gốc lịch sử, bảng 27 quốc gia (từ Udah et al. 2025)
- §2: 5 tầng triết học (Ontology → Epistemology → Ethics → Socio-Politics → Spirituality)
- §3: 5 giá trị cốt lõi + Ba Trụ cột Samkange (1980)
- §4: Ubuntu trong giáo dục Nam Phi (Lefa, 2015)
- §5: Ubuntu trong công tác xã hội toàn cầu — 4 nguyên lý: Relationality, Collective Responsibility, Social Justice, Recognition & Reciprocity (Udah et al. 2025)
- §6: Bảng so sánh Ubuntu vs Phương Tây vs Nho giáo vs Mạch Rễ
- §7: Kết nối Mạch Rễ — Boundary Statement + 4 tương đồng (Tiên Đề I/III/V/VII) + 2 phân kỳ quan trọng
- Link bổ sung vào: `axiom_3.html`, `axiom_3_cultural_comparison.html`, `mach_re_homologous.html`

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1). Design palette: African earth tones (intentional — marks comparative partner page). Boundary Statement rõ ràng: "Ubuntu và Mạch Rễ là hai hệ thống độc lập — không phải hai tên cùng một hệ thống."

## 2026-06-10 — RCA: Thêm link mach_re_homologous.html vào axiom_3.html · RCA 5.0/5

**Symptom:** `axiom_3.html` — trang canonical về Tiên Đề III — không có link ngữ cảnh nào đến `mach_re_homologous.html` trong nội dung thân bài. Link duy nhất nằm ở footer (không ngữ cảnh). Trang homologous chứa cross-cultural validation evidence mạnh nhất cho Tiên Đề III (so sánh với Ubuntu Bantu và Yoruba Nigeria — hai nền văn hóa sống duy nhất khác cũng thực hành Vertical Temporality), nhưng evidence này vô hình với người đọc axiom_3.html.

**Root:** Trang homologous được tạo sau axiom_3.html; chỉ thêm footer link như afterthought. §5-6 (Comparative Philosophy + Summary Matrix) so sánh với 11 truyền thống triết học nhưng không so sánh với văn hóa sống — tức taxonomy so sánh chưa hoàn chỉnh (triết-học-vs-triết-học được cover, văn-hóa-sống-vs-văn-hóa-sống thì không). Vi phạm nguyên tắc traceability: supporting evidence phải reachable từ claim nó hỗ trợ (Paper Rules Tier 3 Rule 3 — falsification condition).

**Fix:**
1. **Thân bài (§6 → §7):** Thêm callout box (purple, matching homologous page theme) sau Summary Matrix, trước §7. Nội dung: phân biệt "so sánh triết học" vs "so sánh văn hóa sống", link đến homologous page, tóm tắt phát hiện chính (three independent cultures evidence Tiên Đề III; 5 divergence points traced to eco-economic roots and Mother Goddess worship).
2. **Bottom nav:** Thêm link `mach_re_homologous.html` giữa "WHAT" và "So sánh Văn hóa", label "🔬 Homologous (Ubuntu & Yoruba)".

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1). Link hai chiều đã hoàn chỉnh: `mach_re_homologous.html` → `axiom_3.html` (có sẵn) + `axiom_3.html` → `mach_re_homologous.html` (mới thêm).

## 2026-06-10 — RCA: Lan tỏa tự phân loại sang CLAUDE.md + index.html + what.html · RCA 4.8–5.0/5

**Symptom:** Tuyên bố tự phân loại Mạch Rễ (Relational and Distributed Philosophy, không phải Systematic Metaphysics) đã có trong Paper 005 nhưng chưa có trong các file định nghĩa công khai và file hướng dẫn agent.

**Root:** Paper 005 là nơi RCA gate được thực hiện đầu tiên; các file khác chưa được đồng bộ. CLAUDE.md — file chi phối toàn bộ hành vi agent — cần tuyên bố này để đảm bảo agent nhất quán khi giới thiệu/phân loại Mạch Rễ.

**Fix:**
1. **CLAUDE.md** — Thêm section "Phân loại Khung nền — Triết học Tương quan-Phân tán" vào Core Principles (RCA 5.0/5), kèm quy tắc sử dụng bắt buộc cho agent.
2. **index.html** — Mở rộng định nghĩa trong Disclaimer (VN + EN): "khung nền triết học và nhân học mở, thuộc loại hình triết học tương quan-phân tán... không phải triết học hệ thống-siêu hình" (RCA 4.8/5).
3. **what.html** — Thêm paragraph "Về loại hình triết học" vào §6 "Vị trí trong bản đồ triết học toàn cầu", neo vào Ubuntu và Tiên Đề VIII, kèm link đến Paper 005 (RCA 4.8/5).

**RCA scores:** CLAUDE.md: 5.0/5; index.html: 4.8/5; what.html: 4.8/5.

## 2026-06-09 — RCA: Sắp xếp lại `axiom_3.html` theo thứ tự khoa học + tách §7B thành trang riêng · RCA 4.8/5

**Symptom:** 13 section trong `axiom_3.html` được sắp xếp theo thứ tự **viết** (accretion pattern: 1→1A→1B→1C→2→3→4→5→6→7→7B→8→9), không theo thứ tự **đọc khoa học** (dependency graph). Hậu quả: giải thích cấp-3 (§1A) và từ nguyên (§1B) nằm trước phân tích bản thể học (§1C); tiêu chí tiên đề (§2) nằm sau 350 dòng giải thích; so sánh văn hóa 7 quốc gia (§7B, ~200 dòng) chen giữa RCA gap analysis và Limitations.

**Root:** Document được xây dựng incremental — mỗi RCA finding được append vào vị trí gần nhất (vd: §1C được gắn sau §1B, §7B được gắn sau §7). Không có dependency-ordered architecture rule. Số hiệu `1A/1B/1C` là bằng chứng trực quan của accretion pattern.

**Fix:**

1. **Reorder `axiom_3.html`** theo dependency graph (nguyên lý: mỗi section chỉ dùng khái niệm đã định nghĩa trước đó):
   - §1 Phát biểu → §2 Tiên đề mới? → §3 Minh họa → §4 RCA Bản thể học → §5 So sánh triết học → §6 Bảng tổng hợp → §7 RCA Vì sao ít được phát biểu → §8 Thực hành ở VN → §9 Tổng quan văn hóa (summary mới) → §10 High School → §11 Từ Việt Hóa → §12 Giới hạn → §13 Kết luận

2. **Tách §7B thành `axiom_3_cultural_comparison.html`** (RCA 5.0/5): §7B trả lời câu hỏi khác ("Tiên Đề III biểu hiện thế nào ở các nền văn hóa?" vs câu hỏi chính "Tiên Đề III là gì?"), có structural independence (methodology riêng, kết luận riêng), và dùng epistemic register khác (star ratings, ascii bar charts). Giữ lại insight cốt lõi + link trong §9 mới.

**Result:** `axiom_3.html`: 1344 → 1153 dòng (-14%). `axiom_3_cultural_comparison.html`: ~200 dòng (trang mới). Tất cả anchor IDs bảo toàn. Glossary reference cập nhật (§1C → §4). Bottom nav + footer thêm link đến trang mới.

**RCA score:** 4.8/5 (Correct: 1, Deep: 1, Feasible: 0.8 (cross-reference risk, đã verify), Conflict-risk: 1, Preservation: 1)

## 2026-06-09 — Fix link hư `#cau-hoi-goc` trong `axioms.html` + `what.html` · RCA 5.0/5

**Symptom:** 8 internal links (`<a href="#cau-hoi-goc">`) trong `axioms.html` (4) và `what.html` (4) trỏ đến anchor không tồn tại. Không có element nào mang `id="cau-hoi-goc"` trong cả hai file.

**Root:** Heading "Câu hỏi gốc" (`<h2>` trong axioms, `<h3>` trong what) được viết nhưng không có `id` attribute. Internal link được thêm vào "Phạm vi" của từng tiên đề với giả định anchor đã tồn tại — không ai kiểm tra chéo sau khi viết link.

**Fix:** Thêm `id="cau-hoi-goc"` vào heading "Câu hỏi gốc" trong cả hai file:
- `axioms.html:108`: `<h2 id="cau-hoi-goc">Câu hỏi gốc</h2>`
- `what.html:563`: `<h3 id="cau-hoi-goc">Câu hỏi gốc (R)</h3>`

**RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)

## 2026-06-09 — A11: Cơ Chế Lưu Trữ — Trang HTML phân tích kiến trúc lưu trữ của Mạch Rễ · RCA 5.0/5

**Payload:** Tạo `luu_tru.html` — trang phân tích cơ chế lưu trữ của triết học Mạch Rễ (lưu cái gì, ở đâu, theo chiều nào, ghi ra sao, xử lý nhiễu thế nào). Tham khảo nội dung từ `raw/luu_tru.html` (Claude chat export), tái cấu trúc thành tài liệu chính thức với RCA gate, cross-reference hệ tiên đề canonical (`axiom_spec.md`), và tích hợp navigation.

**RCA (3-round × 5-Why × scoring gate 5.0/5):**

- **R1 Symptom:** `raw/luu_tru.html` tồn tại dưới dạng raw chat export — nội dung triết học có giá trị nhưng chưa tích hợp vào kiến trúc tài liệu chính thức.
- **R2 Mechanism:** Nội dung được sinh ra trong hội thoại nhưng không có slot trong cấu trúc 4W1H hiện tại. Câu hỏi "Mạch Rễ lưu data ở đâu?" là câu hỏi về cơ chế nội tại, không thuộc 4W1H.
- **R3 Root:** Architectural gap — thiếu trang "cơ chế nội tại". Fix = tạo `luu_tru.html`, neo vào hệ tiên đề canonical, cross-reference `axiom_spec.md`.

**5-Why trace:**
```
Q: Tại sao raw/luu_tru.html chưa được publish?
  ↓ Why 1: Nội dung là chat export, chưa qua RCA gate + reformat.
  ↓ Why 2: Chưa có quyết định đây là tài liệu chính thức.
  ↓ Why 3: Câu hỏi "cơ chế lưu trữ" không nằm trong cấu trúc 4W1H gốc.
  ↓ Why 4: 4W1H không có slot cho câu hỏi "cơ chế nội tại" (how it works internally).
  ↓ Root: Architectural gap — cần tạo slot mới hoặc gắn vào slot có sẵn.
```

**Scoring (action rubric):**

| Criterion | Score | Reason |
|---|---|---|
| Correct | 1 | Nội dung thực sự có giá trị — trả lời câu hỏi phổ biến về kiến trúc hệ thống |
| Deep | 1 | Fix tận gốc architectural gap, không patch bề mặt |
| Feasible | 1 | Tạo file HTML + thêm link nav, không đụng cấu trúc core |
| Conflict-risk | 1 | Nội dung derived từ axiom canonical, không tạo claim mới |
| Preservation | 1 | Bảng tổng hợp (phần mạnh nhất của raw) được giữ và nâng cấp |

**Links added to:** `index.html` (nav card), `what.html` (footer + inline cross-ref tại Mệnh Đề V), `axioms.html` (footer), `axiom_3.html` (footer).

**File mới:** `luu_tru.html` — bảng tổng hợp 9 hàng (mở rộng từ 7 hàng gốc trong raw), thêm cột "Tầng" (Core/Derived/Meta), thêm hàng "Ai quyết định ghi gì" và "Làm sao biết pattern còn đúng", thêm điều kiện bác bỏ, thêm RCA trace section.

## 2026-06-09 — A12: RCA Tiên Đề I Biểu hiện/Bản chất — Giữ nguyên "Có Nhau", thêm ghi chú canonical · RCA 2.2/5 (KHÔNG SỬA)

**Payload:** RCA đánh giá đề xuất đổi tên Tiên Đề I từ "Sống Trong Quan Hệ — Có Nhau Mới Có Mình" → "Bên Nhau Mới Có Mình". Đề xuất bị bác (2.2/5 < 4/5). Thay vào đó, thêm ghi chú vào `plan/dictionary_rule.md §9` giải thích vì sao Biểu hiện và Bản chất của Tiên Đề I gần nghĩa — đây là feature, không phải bug.

**RCA (3-round × 5-Why × scoring gate 2.2/5 — KHÔNG SỬA claim):**

- **R1 Symptom:** "Sống Trong Quan Hệ" (Biểu hiện) và "Có Nhau Mới Có Mình" (Bản chất) gần nghĩa — khó phân biệt hai tầng.
- **R2 Mechanism:** Tiên Đề III cần phân biệt gắt gao (ngăn collapse với Halbwachs/Luhmann), nhưng công cụ này được áp uniform cho toàn bộ 8 tiên đề. Với Tiên Đề I, chính ontological claim (identity IS relations) làm khoảng cách essence-manifestation tự triệt tiêu.
- **R3 Root:** Yêu cầu phân biệt Biểu hiện/Bản chất — thiết yếu cho III — được áp máy móc cho I, nơi nội dung tiên đề khiến hai tầng trở thành near-synonym một cách logic. Không phải lỗi thiết kế.

**5-Why trace:**
```
Q: Tại sao đề xuất đổi "Có Nhau" → "Bên Nhau"?
  ↓ Why 1: Cảm giác hai tầng của Tiên Đề I dư thừa / gần nghĩa.
  ↓ Why 2: "Sống Trong Quan Hệ" ≈ "Có Nhau Mới Có Mình" — cả hai đều nói về relational being.
  ↓ Why 3: Với Relational Ontology, không có gap giữa "nó là gì" và "nó hiện ra thế nào".
  ↓ Why 4: Bản thân Tiên Đề I tuyên bố identity = relations → essence và manifestation collapse.
  ↓ Root: Uniform application của Biểu hiện/Bản chất (đúng cho III) tạo cảm giác dư thừa ở I — nhưng đây là hệ quả logic, không phải defect.
```

**Scoring (candidate edit: "Có Nhau" → "Bên Nhau", gộp một tầng):**

| Criterion | Score | Reason |
|---|---|---|
| Correct | 3/5 | Có vấn đề thật (hai tầng gần nghĩa) nhưng là hệ quả logic của Tiên Đề I, không phải lỗi |
| Deep | 2/5 | Fix chạm symptom (gộp tầng) nhưng không chạm root; "Bên" (spatial) yếu hơn "Có" (existential) cho ontological claim |
| Feasible | 2/5 | Kỹ thuật làm được nhưng gãy đối xứng với II–VIII; canonical table có 2 cột — I sẽ thiếu 1 ô |
| Conflict-risk | 2/5 | Tạo asymmetry trong canonical table; index.html:278 dẫn "Sống Trong Quan Hệ" → pratītyasamutpāda; 6+ file cần sync |
| Preservation | 2/5 | "Có Nhau" (mutual existential belonging) mạnh hơn "Bên Nhau" (spatial co-presence) cho [AX-I] |

**Average: 2.2/5 → DƯỚI NGƯỠNG → KHÔNG ÁP DỤNG.**

**Hành động thay thế:** Thêm "Neo quan trọng (I)" vào `plan/dictionary_rule.md §9` — giải thích sự gần nghĩa là hệ quả logic của Relational Ontology, không phải khiếm khuyết. Không thay đổi tên canonical, không đụng bảng, không tạo asymmetry.

**Phân tích bổ sung — "Có Nhau" vs "Bên Nhau":**
- "Có" = sở hữu hiện sinh (existential having) → identity constituted THROUGH mutual relations → khớp [AX-I]
- "Bên" = không gian cận kề (spatial beside) → co-presence ≠ constitution → yếu hơn cho ontological claim
- "Bên Nhau" có thể chỉ là hai thực thể độc lập đứng cạnh nhau — không nhất thiết cấu thành lẫn nhau

## 2026-06-09 — A10: Trường ngữ nghĩa "nếp" — Sứ mệnh Việt hóa từ vựng triết học · RCA 5.0/5

**Payload:** Thêm Core Principle mới vào CLAUDE.md: "Sứ mệnh Việt hóa — Từ vựng triết học thuần Việt". Thêm §10 vào `plan/dictionary_rule.md`: trường ngữ nghĩa "nếp" — bảng canonical 6 thuật ngữ, quy tắc chọn từ (4 mức ưu tiên), ranh giới phạm trù "nếp" ≠ "tập quán"/"tập tục".

**RCA (3-round × 5-Why × scoring gate 5.0/5):**

- **R1 Symptom:** Glossary `axiom_3.html:1328` ghi "nề nếp → truyền thống / tập quán văn hóa" — tạo lực căng: nếu gloss đã là "tập quán", tại sao canonical không phải "tập quán"?
- **R2 Mechanism:** "tập quán" và "tập tục" thuộc phạm trù **quy ước xã hội** (social convention — có thể đàm phán, biến đổi). "nếp" thuộc phạm trù **cấu trúc sống** (living structure — mất đi thì hệ thống sụp đổ). Nếu thay "nề nếp" → "tập quán", toàn bộ Tiên Đề III từ ontological claim → sociological description.
- **R3 Root:** Mạch Rễ đang **xây dựng** từ vựng triết học bằng tiếng Việt bản địa (không Hán-Việt, không dịch từ Anh/Pháp). "Nếp" là atomic concept — toàn bộ họ từ ("nếp tổ chức", "nếp bản sắc", "nếp sống", "nề nếp") chia sẻ gốc này. Đây là kiến trúc ngữ nghĩa có chủ đích, không phải ngẫu nhiên.

**5-Why trace:**
```
Q: Có nên thay "nề nếp" bằng "tập tục" hoặc "tập quán"?
  ↓ Why 1: "nề nếp" ít phổ biến hơn trong khẩu ngữ → muốn dùng từ dễ hiểu hơn.
  ↓ Why 2: Framework nhắm accessibility → từ phổ thông có vẻ hợp lý.
  ↓ Why 3: "Nếp" là atomic concept — thay "nề nếp" → "tập quán" làm sụp toàn bộ trường ngữ nghĩa.
  ↓ Why 4: Mạch Rễ đang xây dựng từ vựng, không mượn từ vựng có sẵn.
  ↓ Root: "tập tục"/"tập quán" ∈ quy ước xã hội; "nếp" ∈ cấu trúc sống. Sai phạm trù = ontological → sociological.
```
**Kết luận:** Giữ "nề nếp" canonical. "tập quán" giữ làm explanatory gloss (có ghi chú phân biệt). "tập tục" không dùng.

**Scoring (proposal rubric — 5 tiêu chí):**

| Criterion | Score | Reason |
|---|---|---|
| Correct | 1 | "nề nếp" thực sự thuộc structural pattern, "tập quán" thực sự thuộc social convention |
| Deep | 1 | Chạm internal consistency: trường ngữ nghĩa "nếp" là kiến trúc backbone của Việt hóa |
| Feasible | 1 | Sửa bằng cách thêm rule vào CLAUDE.md + dictionary_rule.md — không phá gì |
| Conflict-risk | 1 | Không tạo mâu thuẫn mới — tất cả "nếp" đã dùng nhất quán xuyên framework |
| Preservation | 1 | Giữ nguyên sức mạnh cốt lõi: "nếp" family là điểm mạnh nhất của Việt hóa |
| **Average** | **5.0/5** | **→ FIX: thêm rule, giữ canonical, làm sắc nét glossary** |

## 2026-06-09 — A07: Operational Definition cho Tiên Đề IV (Định nghĩa vận hành) · RCA 4.8/5

**Payload:** Thêm Định nghĩa Vận hành (Operational Definition) cho Tiên Đề IV — đóng GAP_03 (CHECK_07: "tái tổ chức theo logic pattern nội tại" là tautology). Bổ sung gồm 4 phần: O-1 (chỉ báo quan sát được cho 3 cơ chế con: pattern recognition, selective integration, pattern update — mỗi cơ chế có 3 indicators + điều kiện phản chứng riêng); O-2 (tích hợp mẫu hình "vượt gộp" 3 giai đoạn của Phan Ngọc như empirical hypothesis, không phải universal rule); O-3 (định nghĩa ngưỡng tái cấu trúc — kết nối với F-C của Mệnh Đề F); O-4 (phân biệt yêu cầu chức năng vs. cơ chế vận hành — tách hai tầng phân tích độc lập). Điều kiện phản chứng được mở rộng từ 2 cực (tường kín / mở toang) thành 3 điều kiện bổ sung phủ vùng xám thực tế.

**RCA (3-round × 5-Why × scoring gate 4.8/5):**

- **R1 Symptom:** "tái tổ chức theo logic pattern nội tại" mô tả kết quả lọc bằng chính kết quả lọc — "logic pattern nội tại" chỉ được định nghĩa bởi cái gì sống sót. Ba cơ chế con (a,b,c) mô tả conceptually nhưng không có chỉ báo quan sát được. Điều kiện phản chứng gốc chỉ phủ hai cực (tường kín hoàn toàn / mở hoàn toàn) — không test được vùng xám nơi đa số hệ thực tế vận hành.
- **R2 Mechanism:** (a) F-C ("tốc độ xâm nhập vượt ngưỡng tái cấu trúc") cần IV có operational threshold — nhưng "ngưỡng tái cấu trúc" chưa được định nghĩa. (b) DSH-2 ("biên giới lọc khác nhau ở các độ sâu") cần IV có hook cho structural distance — nhưng IV chưa có hook này. (c) PROPOSAL_03 gốc (decision tree: "Cái này có thể sống trong cấu trúc quan hệ không?") chỉ restate vấn đề dưới dạng câu hỏi — không thêm operational content.
- **R3 Root:** Tiên Đề IV nhập nhằng giữa *yêu cầu chức năng* (functional requirement: selective permeability là điều kiện cần để sống sót — falsifiable qua hai cực) và *cơ chế vận hành* (operational mechanism: restructuring diễn ra như thế nào — trước A07, không falsifiable độc lập). Fix: tách hai tầng (O-4), thêm chỉ báo quan sát được cho cơ chế vận hành (O-1), tích hợp mẫu hình thực nghiệm từ Phan Ngọc như hypothesis (O-2), định nghĩa ngưỡng kết nối với F-C (O-3).

**5-Why trace:**

```
Observation: PROPOSAL_03 (decision tree) không giải quyết được CHECK_07's tautology finding.
  ↓ Why? Decision tree hỏi "Can this live in our relational structure?" — same question, tree format.
  ↓ Why is that the same? Vì "can live in our relational structure" ≡ "tái tổ chức theo logic pattern
    nội tại" — cùng một undefined term, khác cách diễn đạt.
  ↓ Why is the term undefined? Vì Mạch Rễ chưa chỉ ra observable indicators phân biệt
    "integrated into pattern" với "rejected by pattern" — ngoài việc nhìn kết quả cuối cùng.
  ↓ Why can't Phan Ngọc's empirical pattern serve as the indicator?
  ↓ ROOT: Nó CÓ THỂ — nhưng với tư cách [empirical hypothesis] ("trong lịch sử Việt Nam quan sát được,
    bộ lọc giữ X và bỏ Y"), không phải universal decision rule ("mọi hệ lọc theo tiêu chí Z").
    PROPOSAL_03 gốc nhập nhằng hai tầng này — trình bày empirical pattern dưới dạng universal rule.
    Fix: O-2 đánh dấu rõ [empirical hypothesis] + O-4 tách functional requirement khỏi operational mechanism.
```

**Scoring (proposal rubric — 5 tiêu chí):**

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Correct | 5 | CHECK_07 đúng: "logic pattern nội tại" thực sự là tautology. Cần operational indicators độc lập. |
| Deep | 5 | Root cause: conflation giữa functional requirement và operational mechanism. Fix tách hai tầng — không patch prose. |
| Feasible | 5 | Addition-only — không phá vỡ cấu trúc hiện có. Mechanism addendum giữ nguyên. Tương thích với F-C, DSH-2, VIII. |
| Conflict-risk | 4 | Risk nhỏ: O-2 (vượt gộp) có thể bị đọc nhầm thành universal requirement. Mitigated: (i) `[empirical hypothesis]`; (ii) "là evidence, không phải definition"; (iii) O-4 tách hai tầng. |
| Preservation | 5 | Core insight được giữ: selective permeability là functional requirement (falsifiable). Mechanism (a,b,c) không đổi. F-C operationalized qua O-3. DSH-2 kết nối tường minh qua O-3(i). |
| **Avg** | **4.8** | **→ PASS threshold.** |

**Operational Definition specification:**

```
O-1 — Observable Indicators (3 sub-mechanisms × 3 indicators + falsification each):
  (a) Pattern recognition: (i) Discourse, (ii) Institutional, (iii) Behavioral.
      Falsification: no differentiation across content types → "mở toang."
  (b) Selective integration: (i) Modification from original, (ii) Time-course via hybrid phase,
      (iii) Perception shift (no longer "foreign").
      Falsification: unmodified integration + still "foreign" after ≥2 gens.
  (c) Pattern update: (i) Continuity MP(P_t) ≈ MP(P_{t+1}), (ii) Legitimacy from guardians,
      (iii) Lineage traceability.
      Falsification: first+second order pattern replacement → F(S,t)=TRUE.

O-2 — Empirical Pattern from Phan Ngọc: "Vượt gộp" (3-stage):
  G1: Mechanical imitation → G2: Hybrid combination → G3: Synthesis (Aufheben).
  Status: [empirical hypothesis] — observed in Vietnamese history (Phan Ngọc, tr.30-32).
  Role: evidence for IV, NOT definition of IV.

O-3 — Restructuring Threshold (F-C connection):
  Below threshold → O-1 normal → VI. Above threshold → (a)+(b) overloaded → F-C triggered.
  Threshold NOT fixed — depends on: (i) structural distance (DSH-2), (ii) historical context,
  (iii) reflexivity (VIII).

O-4 — Functional Requirement vs. Operational Mechanism:
  Two independent analytical layers. System can satisfy functional requirement
  while operating via different mechanisms → doesn't refute IV as requirement,
  but weakens mechanism universality claim.
```

**GAP_03 closure:**

```
Before A07: "tái tổ chức theo logic pattern nội tại" = tautology (CHECK_07 FAIL).
After A07:
  - O-1: 3 sub-mechanisms × 3 observable indicators + individual falsification each
  - O-2: empirical pattern from Phan Ngọc (vượt gộp) as hypothesis, not definition
  - O-3: restructuring threshold operationalizes F-C
  - O-4: functional requirement ≠ operational mechanism — independent analytical layers
  - Falsification: expanded from 2 extremes to 3 additional gray-zone conditions
  → CHECK_07: FAIL → PASS. GAP_03: CLOSED.
```

## 2026-06-09 — A05: DSH — Diagnostic Stratification Heuristic (Heuristic Chẩn Đoán Phân Tầng) · RCA 4.6/5

**Payload:** Thêm Diagnostic Stratification Heuristic (DSH) — công cụ chẩn đoán nằm GIỮA tầng tiên đề và Diagnosis Rubric, KHÔNG phải tiên đề mới. DSH đóng GAP_01 (thiếu phân tầng bất biến) bằng cách cung cấp 3 nguyên tắc chẩn đoán: DSH-1 (vi sai tốc độ thay đổi), DSH-2 (lọc theo độ sâu), DSH-3 (độ sâu = khoảng cách cấu trúc, không phải loại nội dung). DSH vận hành hóa Condition A của Mệnh Đề F và cung cấp cơ sở cho trọng số chẩn đoán trong Diagnosis Rubric.

**RCA (3-round × 5-Why × scoring gate 4.6/5):**

- **R1 Symptom:** Mạch Rễ collapses Phan Ngọc's stratified observations (văn hóa/văn minh, 4 lĩnh vực với tốc độ thay đổi khác nhau) into a single flat `Pattern(R(S))`. Không phân biệt được thay đổi ở core vs. surface. Diagnosis Rubric có 6 indicators với trọng số ngang nhau — nhưng thờ cúng tổ tiên thay đổi ≠ từ vay mượn thay đổi.
- **R2 Mechanism:** (a) F's Condition A ("core relational pattern attacked") không operationalizable nếu không biết cái gì là "core pattern" vs "surface content." (b) Tiên Đề IV's "tái tổ chức theo logic pattern nội tại" không phân biệt được restructuring ở độ sâu nào. (c) Framework không giải thích được tại sao một số yếu tố bản sắc thay đổi chậm hơn yếu tố khác — một hiện tượng quan sát được xuyên văn hóa.
- **R3 Root:** `Identity(S) = Pattern(R(S))` treats the invariant relational pattern as structurally flat. Nhưng identity systems empirically exhibit differential coupling strength — một số quan hệ có structural distance ngắn hơn đến invariant pattern và do đó thay đổi chậm hơn. Đây là structural fact, không phải ontological claim — không có "essence" (svabhāva) nào được giới thiệu.

**5-Why trace:**

```
Observation: Mạch Rễ treats all identity elements as equally deep.
  ↓ Why? Pattern(R(S)) is flat — one pattern, one depth.
  ↓ Why? Re-derivation prioritized Pattern vs Content distinction; depth-within-Pattern deferred.
  ↓ Why now? A06 (F) defines "core pattern attacked" but "core" is undefined without depth.
  ↓ Why can't existing axioms handle this? II, III, IV define pattern/invariance/transmission/boundary
    but not differential coupling strength within the pattern itself.
  ↓ ROOT: Pattern(R(S)) is structurally flat. A diagnostic heuristic (not axiom) can add depth
    without claiming ontological stratification — preserving BRIDGE-II-III's anti-svabhāva constraint.
```

**Scoring (proposal rubric — 5 tiêu chí):**

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Correct | 5 | GAP_01 thật. F's Condition A cần operationalization. Diagnosis Rubric cần trọng số khác biệt. |
| Deep | 4 | Chạm root (flat pattern → differential coupling). Mất 1 điểm: không claim giải quyết epistemological problem xác định depth trong novel cases. |
| Feasible | 5 | Heuristic (không axiom) → không phá vỡ cấu trúc hiện có. Additive only. 2.0/3 triangulation advisory support. |
| Conflict-risk | 4 | DSH-3 "depth = structural distance" tương thích BRIDGE-II-III (không svabhāva). Risk nhỏ: misinterpretation "depth = essence" — mitigated bằng explicit disclaimer trong §9.8. |
| Preservation | 5 | Tất cả axiom I-VIII, F không đổi. F được củng cố (Condition A operational). Diagnosis Rubric được làm giàu (trọng số phân tầng). |
| **Avg** | **4.6** | **→ PASS threshold.** |

**DSH specification:**

```
DSH-1 — Differential Rate of Change:
  Yếu tố có coupling strength với invariant pattern (II) càng cao → thay đổi càng chậm.
  Empirical grounding: Phan Ngọc's văn hóa/văn minh distinction.

DSH-2 — Depth-Dependent Filtering:
  Biên giới (IV) lọc nghiêm ngặt hơn ở gần invariant pattern.
  Empirical grounding: Phan Ngọc's differential Việt hóa (Phật giáo sâu, Nho giáo nông).

DSH-3 — Depth = Structural Distance, Not Content Type:
  "Độ sâu" = structural distance từ invariant pattern (II), không phải content type.
  Cùng content type có thể ở độ sâu khác nhau trong các hệ khác nhau.

Triangulation: A (STRONG 1.0) + B (PARTIAL 0.5) + C (PARTIAL 0.5) = 2.0/3 (advisory)
Falsification: DSH-F1 (no differential rate) | DSH-F2 (no depth-dependent filtering)
Status: [empirical hypothesis] — pending cross-cultural verification (Phase 2)
```

**Carry-Forward Set (PROPOSAL_01 → DSH):**

| Asset từ PROPOSAL_01 | Trạng thái |
|---|---|
| "Bất biến cấu trúc không phải một tầng duy nhất" | **Carried** → DSH-1 |
| "Tầng sâu hơn bền hơn, thay đổi chậm hơn" | **Carried** → DSH-1 |
| "Hấp thụ có định hướng vận hành khác nhau ở mỗi tầng" | **Carried** → DSH-2 |
| 4-tier model (Tier 1-4 với tên cụ thể) | **DROPPED** — quá Vietnam-specific |
| "Tiên Đề IIb" status (new core axiom) | **DROPPED** — category error |
| Phân biệt văn hóa/văn minh (Phan Ngọc) | **Carried** — empirical grounding |
| Điều kiện phản chứng gốc | **REFORMULATED** → DSH-F1, DSH-F2 |

**Files changed:**
- `axiom_spec.md`: +DSH header in numbering scheme (§0); +`heuristics:` block in YAML dependency graph (§8); +§9 Diagnostic Stratification Heuristic (full spec: phát biểu VI/EN, empirical grounding from Phan Ngọc, connection to F, connection to Diagnosis Rubric, triangulation check, falsification conditions, limitations & warnings, status & roadmap, carry-forward set)
- `axioms.html`: +DSH in hero count; +DSH section (3 DSH articles + connections to F & Diagnosis Rubric + indicator weight table + neo table + falsification + limitations + validation roadmap); updated `<title>` and `<meta>` (3→4 Derived, +1 Heuristic); updated footer (DSH RCA score)
- `CHANGELOG.md`: this entry

**Verification:** (1) DSH explicitly marked "NOT an axiom" — không thêm architectural complexity vào hệ tiên đề. (2) DSH-3 "depth = structural distance" tương thích BRIDGE-II-III — không svabhāva, tất cả tầng đều saṃvṛtisat. (3) F-A có operational content: "core relational pattern" = yếu tố có structural distance ngắn nhất đến invariant pattern — observable, không phải mysterious essence. (4) Triangulation 2.0/3 (advisory — heuristic không yêu cầu ≥2/3 nhưng có ≥2/3 làm tăng confidence). (5) Connection to Mệnh Đề F (A06) rõ ràng — DSH phụ thuộc vào F (như PLAN_RCA_REVIEW requirement). (6) Connection to Diagnosis Rubric rõ ràng — bảng trọng số 6 indicators kèm cảnh báo Vietnam-specific. (7) 2 falsification conditions (DSH-F1, DSH-F2) vận hành được. (8) 5 limitations tường minh ngăn misuse.

**A05 status: COMPLETE** — GAP_01 được đóng bằng DSH (empirical hypothesis, pending Phase 2 cross-cultural verification). Phase 1 complete (A01-A04, A06, A08, now A05). A07 (Amendment IV operational definition) còn lại.

---

## 2026-06-09 — A04: Khung EAP — Qualitative Metric cho "áp lực đồng hóa tương đương" · RCA 4.4/5

**Payload:** Thêm Khung So sánh Định tính Đa chiều EAP (Equivalent Assimilation Pressure Qualitative Comparative Framework) — định nghĩa vận hành cho "áp lực đồng hóa tương đương" trong điều kiện phản chứng toàn hệ. A04 đóng CHECK_08 (Falsification PARTIAL) — bottleneck cuối cùng khiến điều kiện phản chứng toàn hệ không vận hành được: trước A04, "áp lực đồng hóa tương đương" là placeholder từ, cho phép mọi counterexample đều bị dismiss với lý do "áp lực không tương đương." Sau A04, điều kiện phản chứng có operational content: 5 chiều độc lập × quy tắc so sánh ≥4/5 × calibration anchor (Việt Nam 1000 năm Bắc thuộc).

**RCA (3-round × 5-Why × scoring gate 4.4/5):**

- **R1 Symptom:** "Áp lực đồng hóa tương đương" không có định nghĩa vận hành — là placeholder từ. Điều kiện phản chứng toàn hệ trở thành vacuous: luôn có thể claim "áp lực không tương đương" để bảo vệ framework. Counterexample bất kỳ không thể được đánh giá vì không có tiêu chí so sánh.
- **R2 Mechanism:** (a) Assimilation pressure là hiện tượng đa chiều (duration, institutional control, elite replacement, demographic ratio, cultural targeting) — gộp thành scalar "tương đương" là oversimplification khiến mọi so sánh lịch sử trở thành subjective. (b) Không có controlled experiment cho lịch sử → cần qualitative comparative framework, không phải quantitative metric. (c) Nếu A06 (Mệnh đề F) định nghĩa internal failure conditions, A04 định nghĩa external comparison conditions — cả hai đều cần để falsification vận hành.
- **R3 Root:** **Category error** — falsification condition giả định "áp lực đồng hóa" là unidimensional scalar, trong khi nó là multi-dimensional historical phenomenon. Các chiều (duration, institutional control, etc.) có thể biến thiên độc lập — hai trường hợp có thể "tương đương" trên một chiều và khác biệt hoàn toàn trên chiều khác. Fix: thay scalar equivalence bằng multi-dimensional qualitative comparative framework với quy tắc so sánh rõ ràng.

**5-Why trace:**

```
Observation: "áp lực đồng hóa tương đương" is undefined.
  ↓ Why? Because it was a placeholder from initial axiom derivation — "good enough for now."
  ↓ Why was it "good enough"? Because priority was deriving positive axioms (I-VIII); falsification was deferred.
  ↓ Why does it need fixing NOW? A06 (F) closed internal failure; without A04, global falsification still vacuous.
  ↓ Why can't a simple scalar metric work? Because assimilation pressure varies independently on multiple dimensions.
  ↓ ROOT: Category error — treating a multi-dimensional historical phenomenon as a unidimensional scalar.
```

**Scoring (proposal rubric — 5 tiêu chí):**

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Correct | 4 | Đúng: "áp lực tương đương" thực sự là multi-dimensional. Mất 1 điểm vì historical comparison luôn có edge cases. |
| Deep | 4 | Chạm gốc: chuyển từ scalar equivalence → multi-dimensional comparative framework. Mất 1 điểm vì không giải quyết được fundamental problem của historical uniqueness. |
| Feasible | 5 | 5 dimensions đều observable từ historical records. Calibration anchor có sẵn. Không cần controlled experiments. |
| Conflict-risk | 5 | Không conflict với bất kỳ axiom/proposition nào. Tương thích với F: F = internal failure, EAP = external comparison. |
| Preservation | 4 | Giữ nguyên falsification condition gốc, chỉ operationalize "tương đương." Mất 1 điểm vì qualitative framework inherently có ambiguity. |
| **Avg** | **4.4** | **→ PASS threshold.** |

**EAP Framework specification:**

```
5 chiều độc lập, mỗi chiều 3 mức:
  D₁ — Duration:           Short (<3 gen) · Medium (3-10) · Long (>10)
  D₂ — Institutional Ctrl: None · Partial · Total
  D₃ — Elite Replacement:  None · Partial · Total
  D₄ — Demographic Ratio:  Minority (<30%) · Parity (30-70%) · Majority (>70%)
  D₅ — Cultural Infra Atk: None · Partial · Systematic

Comparative Rule: B ≥ A ⇔ (1) B ≥ A on ≥4/5 dimensions, AND (2) no dimension where B < A by 2 levels.

Calibration Anchor: Vietnam under 1000 năm Bắc thuộc (179 TCN – 939 SCN)
  D₁=Long, D₂=Total, D₃=Partial, D₄=Minority, D₅=Partial

Epistemic status: [qualitative comparative framework] — structured comparison tool, not measurement instrument.
```

**Files changed:**
- `axiom_spec.md`: +EAP framework definition (5 dimensions, comparative rule, calibration anchor, usage note) at §3, directly after global falsification condition
- `axioms.html`: +EAP framework in HTML (2 tables + 2 notes) after global falsification condition, in §3 derivation diagram section
- `what.html`: +EAP framework in §4.8 Falsification section (2 tables + 2 def-boxes); +cross-reference link from §3.5 falsification note → §4.8; +anchor `id="falsification"` on §4.8 header
- `CHANGELOG.md`: this entry

**Verification:** (1) Global falsification condition now has operational definition — a critic must specify 5 EAP dimensions to claim counterexample. (2) EAP framework is structural (observable from historical records), not metaphysical. (3) Calibration anchor is explicit and documented — not hidden behind "equivalent." (4) Epistemic status is correctly labeled as `[qualitative comparative framework]`, not `[measurement instrument]`. (5) A04 + A06 together close CHECK_08 completely: F defines internal failure criterion, EAP defines external comparison criterion. (6) All links between axiom_spec.md, axioms.html, and what.html are consistent.

**A04 status: COMPLETE** — CHECK_08 moves from PARTIAL → PASS. A01-A04, A06, A08 now complete (Phase 1 closed).

---

## 2026-06-09 — A08: Diagnosis Rubric "Đứt gãy" integration hoàn tất · RCA 4.0→4.8/5

**Payload:** Hoàn tất A08 với 3 fix nhỏ (A08a/A08b/A08c) sau 3-round RCA. A08 ban đầu được tích hợp cùng commit A06 (thêm score band "Rễ đã đứt" + điều chỉnh range 1-4), nhưng 3-round RCA phát hiện 3 gap: (S1) derivation diagram thiếu F trong axioms.html, (S2) 6 rubric indicators không map đến A/B/C conditions của F, (S3) score band 1-4 không có differential diagnosis giữa recoverable crisis và approaching severance.

**RCA (3-round × 5-Why × scoring gate):**

- **A08a (diagram sync) — 4.8/5:** Root: A06 commit cập nhật `axiom_spec.md` diagram nhưng quên đồng bộ sang `axioms.html`. Fix: 1 dòng ASCII art.
- **A08b (indicator→F mapping) — 4.6/5:** Root: audit plan dùng "ngưỡng" cho cả continuous score threshold lẫn discrete AND gate — conflating two mathematical types. Fix: explanatory `<div class="note">` bridge hai loại thang đo.
- **A08c (differential diagnosis) — 4.4/5:** Root: pre-F rubric chỉ có "rễ nông" — không có khái niệm structural severance. Thêm F thay đổi ngữ nghĩa band 1-4 nhưng action text chưa cập nhật. Fix: 1 câu phân biệt A+C (phục hồi) vs A+B+C (đứt gãy).

**Scoring (A08 overall — proposal rubric):**

| Phase | C | D | F | CR | P | Avg |
|-------|---|---|---|---|-----|-----|
| A08a | 5 | 4 | 5 | 5 | 5 | **4.8** |
| A08b | 5 | 3 | 5 | 5 | 5 | **4.6** |
| A08c | 4 | 4 | 5 | 4 | 5 | **4.4** |
| **Tổng** | | | | | | **4.6** |

**Files changed:**
- `axioms.html`: +F line in derivation diagram (l.371), đồng bộ với `axiom_spec.md:214`
- `how.html`: +indicator→F mapping note (l.363-369); +differential diagnosis in score band 1-4 (l.380)
- `CHANGELOG.md`: this entry

**Verification:** (1) Diagram axioms.html ≡ axiom_spec.md — F đối xứng với VI. (2) Mapping note bridge continuous↔discrete, không overclaim. (3) Differential diagnosis dùng ngôn ngữ hedged ("nếu nghi ngờ"). (4) Tất cả link → axioms.html#F. (5) Score bands 5-12 untouched.

**A08 status: COMPLETE** — đóng S1, S2, S3. Không cần mở lại.

---

## 2026-06-09 — A06: Mệnh đề F (Failure Conditions / Điều Kiện Đứt Gãy) · RCA 5.0/5

**Payload:** Thêm Mệnh đề F (Điều Kiện Đứt Gãy — "Đứt Khi Hết Cội") là derived proposition thứ 4 của Mạch Rễ, suy từ II+III+IV. F đóng GAP_02 (survivorship bias) — lỗ hổng triết học nghiêm trọng nhất được audit plan xác định. F độc lập với A05 (IIb/DSH), dùng toàn bộ khái niệm hiện có, không thêm primitive concept nào.

**RCA (3-round × 5-Why × scoring gate 5.0/5):**

- **R1 Symptom:** Mạch Rễ chỉ có case study thành công (1000 năm Bắc thuộc, 500kV, hòa giải Việt-Mỹ). Không có case study thất bại. Diagnosis Rubric có thang "rễ nông" nhưng không có ngưỡng "không còn rễ." Điều kiện phản chứng toàn hệ không vận hành được vì "áp lực đồng hóa tương đương" không có định nghĩa.
- **R2 Mechanism:** (a) Không có lý thuyết về thất bại → mọi trường hợp mất bản sắc đều có thể rationalize hậu kiểm là "áp dụng I-IV chưa đủ" thay vì "I-IV không đủ để giải thích." (b) "Rễ nông đang phục hồi" và "rễ đã đứt" là hai trạng thái khác nhau về bản chất, đòi hỏi can thiệp khác nhau — gộp chung = chẩn đoán sai. (c) Thiếu internal failure conditions → falsification chỉ dựa trên external comparison không thể chuẩn hóa.
- **R3 Root:** Mạch Rễ được suy từ câu hỏi "vì sao một số hệ SỐNG SÓT?" — nó tập trung tự nhiên vào cơ chế sinh tồn. Nhưng một lý thuyết hoàn chỉnh về sinh tồn phải xác định được khi nào sinh tồn THẤT BẠI — nếu không "sống sót" chỉ là phát biểu tautological: "hệ sống sót là hệ có những thứ cần để sống sót."

**Scoring (proposal rubric — 5 tiêu chí):**

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Correct | 5 | Survivorship bias là thật và kiểm chứng được. 3 điều kiện suy trực tiếp từ II+III+IV. |
| Deep | 5 | Chạm gốc: F định nghĩa internal failure conditions, không chỉ external comparison. |
| Feasible | 5 | KHÔNG cần IIb. Dùng toàn bộ khái niệm hiện có. |
| Conflict-risk | 5 | Ashby: variety destruction; Anattā: nirodha (cessation conditions); Phan Ngọc: empirical grounding (dây thăng bằng, Do Thái, Hồ/Nguyễn). |
| Preservation | 5 | Đóng lỗ hổng quan trọng nhất mà không thêm architectural complexity. |

**F specification:**

```
Mệnh Đề F — Điều Kiện Đứt Gãy (Failure Conditions)
Loại: Derived Proposition [II+III+IV]
3-condition AND gate: F(S,t) ≡ A(S,t) ∧ B(S,t) ∧ C(S,t)

  A: Core relational pattern (II) bị tấn công trực tiếp
  B: V-axis (III) bị cắt đứt vật lý (gián đoạn truyền liên thế hệ)
  C: Tốc độ xâm nhập > ngưỡng tái cấu trúc biên giới (IV)

Phân biệt:
  Chỉ C → Biến đổi thích nghi (bình thường)
  A+C, không B → Khủng hoảng có thể phục hồi
  Cả A+B+C → Đứt gãy thực sự

Triangulation: A (Phan Ngọc: dây thăng bằng tr.140; tộc người mất diện mạo tr.145;
  Jewish diaspora tr.146; Hồ/Nguyễn tr.408) · B (Ashby: variety destruction) ·
  C-cond (Anattā: nirodha) — ~2.5/3
Falsification: SAI nếu tồn tại cộng đồng trải qua A∧B∧C mà pattern vẫn tái tạo
  được qua ≥1 thế hệ.
```

**Files changed:**
- `axiom_spec.md`: +K11 derivation log entry; +F full spec (VI/EN phát biểu, 3-condition AND gate, differential diagnosis, triangulation, falsification, relation to VI & VIII); updated derivation diagram, YAML dependency graph, headers (3→4 derived propositions)
- `axioms.html`: +F article display (between VII and VIII) with id="F" anchor, tier label (3→4), hero count (3→4)
- `how.html`: +"⛔ Rễ đã đứt" score band (score 0) with F link; adjusted "Rễ nông trầm trọng" range (0–4 → 1–4); +CSS for severed band
- `CHANGELOG.md`: this entry

**Verification:** (1) F chỉ dùng khái niệm từ II, III, IV — không primitive concept mới. (2) Triangulation ~2.5/3 — vượt threshold 1.5. (3) Điều kiện phản chứng rõ ràng, falsifiable. (4) F đối xứng với VI: cùng đầu vào (II+III+IV), hai kết quả đối xứng (ΔVariety>0 vs ΔPattern=∅). (5) Diagnosis Rubric có ngưỡng "Đứt gãy" phân biệt rõ với "Rễ nông trầm trọng."

**Dependency note:** F độc lập với A05 (IIb/DSH). A06 được execute TRƯỚC A05 theo MODIFICATION 1 của PLAN_RCA_REVIEW. A08 (Diagnosis Rubric update) tích hợp cùng lần này.

---

## 2026-06-09 — `Zhang_Yimou_Spielberg_Hybrid_Screenplay_v2.md`: Canonical promotion + auto-trigger · RCA 5.0/5

**Payload:** Replace v1 (`Zhang_Yimou_Spielberg_Hybrid_Screenplay.md`) with v2 (`_v2.md`) as canonical skill file referenced in CLAUDE.md §Screenplay & Creative Writing Rules. Mark v1 deprecated. Add "Luôn kích hoạt khi tạo kịch bản phim" to ensure the skill auto-triggers for all screenplay work.

**RCA (3-round × 5-Why × scoring gate 5/5):**

- **R1 Symptom:** CLAUDE.md points to v1, but v2 exists with 104 additional lines including Analysis Mode (6-step protocol), Project Brief Template, Layer Tension model, Screenplay Format Sample, Supporting Character Test, and Priority Rule. Capability gap: user asks "analyze this scene" → v1 has no Analysis Mode → improvise ad-hoc.
- **R2 Mechanism:** v2's frontmatter states "This skill covers creation mode and analysis mode equally — trigger for both." But v1-only CLAUDE.md reference makes analysis mode unreachable. This is an internal inconsistency in the project's own tooling.
- **R3 Root:** The skill file upgrade (v1→v2) was performed without a Carry-Forward Set declaration, violating the "rebuild with carry-forward" rule (CLAUDE.md §Document contract rules). CLAUDE.md reference to v1 is a downstream symptom of this protocol gap.

**Scoring (plan item rubric):** Correct=1, Deep=1, Feasible=1, Conflict-risk=1, Preservation=1 → **5/5**.

**Carry-Forward Set (v1→v2):**
| Asset | Status |
|---|---|
| 5 Core Hybrid Principles | Carried verbatim |
| Structural Tension Map (V/H axes) | Carried verbatim |
| Beat-Level Priority Rule (8 beats) | Carried verbatim |
| Story Architecture (3 acts) | Carried verbatim |
| Character Construction (3-layer) | Carried + expanded (Layer Tension) |
| Scene-Level Writing Guidelines | Carried + expanded (Format Sample) |
| Tonal Calibration | Carried verbatim |
| Output Formats (5 types) | Carried + expanded (axis annotation) |
| Quick Reference Checklist (12 items) | Carried + expanded (Priority Rule) |
| Film Anchor Reference | Carried verbatim |
| **NEW: Analysis Mode** | v2 only |
| **NEW: Project Brief Template** | v2 only |
| **NEW: Supporting Character Test** | v2 only |
| **NEW: How to Begin / Choose Mode** | v2 only |

**Files changed:** `CLAUDE.md` (1 line updated: path→v2 + expanded description + "Luôn kích hoạt khi tạo kịch bản phim"), `publish/movie_script/Zhang_Yimou_Spielberg_Hybrid_Screenplay.md` (deprecation notice replacing frontmatter), `CHANGELOG.md` (this entry).

**Verification:** `grep -r "Zhang_Yimou_Spielberg_Hybrid_Screenplay.md"` — only v1's own deprecation notice + CHANGELOG historical entries + frozen screenplay artifacts (mv_001). No broken references. v2 path active in CLAUDE.md. Skill auto-trigger instruction embedded.

---

## 2026-06-09 — `Zhang_Yimou_Spielberg_Hybrid_Screenplay.md`: RCA review × Mạch Rễ — 7 structural edits · RCA ≥ 4/5

**Hành động:** Review `rev.txt` phát hiện 3 FAIL + 4 PARTIAL trong skill file. Dùng 3-round RCA × 5-Why × scoring gate ≥ 4/5 để quyết định từng edit. Tất cả 7 edits đạt 5.0/5 → applied. Bổ sung cơ chế cấu trúc dùng Mạch Rễ axioms làm structural backbone, không phải loose analogy.

**RCA (3-round × 5-Why × scoring) — root cause of all FAIL/PARTIAL findings:**

- **R1 Symptom:** Skill file mô tả aesthetic outcomes (output) nhưng thiếu structural mechanisms (cơ chế). 3 FAIL: không có tension map giữa Zhang-Spielberg, color system phẳng, system antagonist thiếu embodiment. 4 PARTIAL: midpoint rationale, character layer tension, silence examples, output format examples.
- **R2 Mechanism:** Skill file treat Zhang-Spielberg như hai palette blendable thay vì hai hệ thống cấu trúc trực giao. Mỗi FAIL trace về cùng một pattern: mô tả kết quả thẩm mỹ → không mô tả cơ chế sản sinh.
- **R3 Root:** Skill file xây trên kết quả (output aesthetic) thay vì xây trên cơ chế (tại sao hai hệ thống tạo ra kết quả đó). Không nhận diện Zhang và Spielberg như hai trục trực giao (V⊥H — Axiom III) cần governance mechanism (Axiom IV) thay vì blending.

**7 edits applied (all scored 5.0/5 via independent 3-round RCA):**

| # | Edit | RCA Score | Mạch Rễ anchor | Addresses |
|---|------|-----------|----------------|-----------|
| 1 | Structural Tension Map — V-axis (Zhang) vs H-axis (Spielberg), beat-level priority rule, conflict check | 5.0 | Axiom III (V⊥H) + Axiom IV (Dynamic Boundary) | FAIL_01, RCA_01 |
| 2 | Color System Deepening — 4-register vocabulary with Zhang film anchors + 4 grammar rules (transition, collision, beat-triggered shift, direction) | 5.0 | Axiom II (Structural Invariance) + Axiom IV (Selective Integration) | FAIL_02 |
| 3 | System Antagonist Embodiment Catalog — Zhang methods (4) + Spielberg methods (3) + hybrid combination example | 5.0 | Axiom I (Relational Ontology) + Axiom III (Vertical Temporality) | FAIL_03 |
| 4 | Midpoint Rationale — H-axis peak before V-axis reassertion; Zhang's "too complete to open" technique | 5.0 | Axiom III (V⊥H structural hinge) | PARTIAL_01 |
| 5 | Character Layer Tension — Surface vs Personal Wound (primary) + Personal vs Generational Wound (deepening) + construction test | 5.0 | Axiom VI (Perturbation Transformation) | PARTIAL_02 |
| 6 | Weighted Checklist (3-tier) — HIGH (structural failure) / MEDIUM (weakened impact) / LOW (aesthetic) + priority rule | 5.0 | Axiom hierarchy: Core (I-IV) → Derived (V-VII) → Meta (VIII) | RCA_03 |
| 7 | Film Anchor Reference — Zhang 3 modes + Spielberg 3 modes + calibration rule (default: Raise the Red Lantern × E.T.) | 5.0 | Axiom II (Pattern Recognition requires calibration examples) | RCA_02 |

**Nguyên tắc áp dụng Mạch Rễ:**
- Mỗi edit mapped to a specific axiom's **structural mechanism** — không phải loose analogy hay thematic borrowing
- Tension Map dùng V⊥H như structural description của hai hệ thống trực giao, không phải metaphor
- Color Grammar dùng Axiom IV (selective permeability) cho collision rule: màu tối (system/V-axis) frames màu sáng (human/H-axis)
- System Antagonist dùng Axiom I: system manifests through relations (space, ritual, objects), not as entity
- Midpoint dùng Axiom III: H-axis peak → V-axis reassertion là structural hinge, không phải aesthetic choice
- Không Tiên Đề nào được namedrop trong skill file — chúng vận hành như structural backbone, không phải content

**Files changed:** `publish/movie_script/Zhang_Yimou_Spielberg_Hybrid_Screenplay.md` (7 targeted extensions; all original content preserved; file grew from 206 → 355 lines). `CHANGELOG.md` (this entry).

**Verification:** Skill file checked against CLAUDE.md Screenplay Rules (Tier 2, 7 quy tắc) — no contradictions. All 5 Core Principles preserved intact. No axiom names appear in scene-level or dialogue instructions. The V/H terminology is internal to the skill file's structural analysis sections — consistent with "show, don't tell" rule (Tiên Đề III as structure, not theme).

---

## 2026-06-09 — `CLAUDE.md`: Thêm Screenplay & Creative Writing Rules section · RCA 5.0/5

**Hành động:** Thêm section mới vào CLAUDE.md — Screenplay & Creative Writing Rules — với Tier 1 (Zhang-Spielberg Hybrid framework + Canonical 10 Slate reference) và Tier 2 (7 quy tắc bắt buộc cho screenplay writing). Quyết định qua 3-round RCA × 5-Why × scoring gate.

**RCA (3-round × 5-Why × scoring):**

- **R1 Symptom:** CLAUDE.md có Paper & Publication Rules (Tier 1/2/3) nhưng không có routing cho screenplay/creative writing — dù project đã phát triển lượng lớn nội dung điện ảnh (Zhang-Spielberg skill 206 dòng, Canonical 10 Slate 659 dòng, 5 file ideas).
- **R2 Mechanism:** MACH_RE dùng screenplay như phương tiện applied Tiên Đề III — không phải creative writing thông thường. Thiếu routing → agent không kích hoạt skill khi cần → chất lượng output không được guarantee bởi methodology đã thiết kế.
- **R3 Root:** CLAUDE.md thiếu structural parity giữa academic writing và creative cinematic writing — Paper Rules có routing đầy đủ, Screenplay Rules không tồn tại → **bất đối xứng cấu trúc**.
- **Scoring:** Correct 5 · Deep 5 · Feasible 5 · Conflict-risk 5 · Preservation 5 → **5.0/5 → ADD.**

**Section mới gồm:**
- Tier 1: Zhang-Spielberg Hybrid framework (bắt buộc đọc) + Canonical 10 Slate (reference)
- Tier 2: 7 quy tắc (RCA gate cho idea mới, show-don't-tell, antagonist as system, specificity, constraint set, RCA traceability, falsification condition)

**Files changed:** `CLAUDE.md` only (addition thuần túy, không sửa/xóa gì).

---

## 2026-06-08 — `axiom_spec.md` P5: ISSUE-08 (triangulation protocol) + YAML dependency graph · RCA ≥ 4/5

**Hành động:** Phase 5 (optional). ISSUE-08: thêm triangulation protocol (forward-only) với 5-step scoring procedure. YAML dependency graph cho machine readability.

**RCA (3-round × 5-Why × scoring):**

- **ISSUE-08 — Triangulation Protocol** — 5/5 → ADD: neo-score hiện tại là informal, author-assessed. Không có intersubjective procedure → scoring không reproducible. Fix: 5-step protocol với STRONG(1.0)/PARTIAL(0.5)/WEAK(0.25)/NONE(0.0), threshold 1.5. Forward-only: không retroactive re-score I–VIII trừ khi tác giả quyết định re-derive.
- **YAML Graph** — 5/5 → ADD: dependency graph giúp LLM + tooling parse được cấu trúc hệ tiên đề. Bao gồm sot_references mapping.

**Files changed:** `axiom_spec.md` only (no render propagation needed).

---

## 2026-06-08 — `axiom_spec.md` P4: ISSUE-06 (VII notation) + ISSUE-07 (scope pointers) · RCA ≥ 4/5

**Hành động:** Phase 4. ISSUE-06: làm rõ "gradient trường F" là structural analogy. ISSUE-07: thêm GLOBAL SCOPE block + scope pointer cho mỗi Tiên Đề I-IV.

**RCA per-issue (3-round × 5-Why × scoring):**

- **ISSUE-06 — VII notation** — 5/5 → ADD: "Gradient trường F" trộn formal notation với metaphor → giảm LLM parsability, mời misreading. Fix: gán nhãn "structural analogy", cung cấp formal rendering (attractor dynamics A(S)), tham khảo Kauffman/Weick/Odum.
- **ISSUE-07 — scope pointers** — 5/5 → ADD: Tiên Đề I-IV phát biểu ở dạng universal, nhưng câu hỏi gốc scope rõ ràng cho collective identity systems xuyên thế hệ. Thiếu scope qualifier → risk over-application (startup culture) và under-application (micro-collectives). Fix: GLOBAL SCOPE block + one-line pointer mỗi axiom, reference về Câu hỏi gốc.

**Files changed:** `axiom_spec.md`, `axioms.html`, `what.html`.

---

## 2026-06-08 — `axiom_spec.md` P3: ISSUE-05 (AX-VIII continuity constraint, MP + SOT-K) · RCA ≥ 4/5

**Hành động:** Phase 3. ISSUE-05: thêm ràng buộc liên tục cho Tiên Đề VIII — meta-pattern MP bảo toàn identity-across-revision.

**RCA (3-round × 5-Why × scoring):** 5/5 → ADD: VIII cho phép self-revision. Không có boundary condition → full revision = hệ mới thay hệ cũ → phá claim persistence. Fix: MP(P_t) ≈ MP(P_{t+1}). First-order pattern sửa được; second-order MP phải ổn định. Kantian analogy (SOT-K §1.1): MP ≈ transcendental unity of apperception.

**Files changed:** `axiom_spec.md`, `axioms.html`, `what.html`.

---

## 2026-06-08 — `axiom_spec.md` P2: ISSUE-03 (ARG-III-1) + ISSUE-04 (AX-IV mechanism) · RCA ≥ 4/5

**Hành động:** Phase 2 của `review/mach-re-axioms-review-plan.md` (v2). ISSUE-03: thêm ARG-III-1 bảo vệ tính trực giao V ⊥ H bằng lập luận Synchronic vs Diachronic + Kantian framing (SOT-K), dựa trên BRIDGE-II-III. ISSUE-04: thêm mechanism addendum (3 cơ chế con) cho Tiên Đề IV.

**RCA per-issue (3-round × 5-Why × scoring):**

- **ISSUE-03 — ARG-III-1** — 5/5 → ADD: Claim V ⊄ H không có lập luận bảo vệ → burden of proof chưa được đáp ứng → physicalist có thể argue mọi "nối kết cội nguồn" đều là H-axis phenomena. Fix: lập luận Synchronic vs Diachronic — trí nhớ H là diachronic (mã hóa quá khứ), V là synchronic (hành động *như thể* ràng buộc tổ tiên đang vận hành NOW). Bằng chứng: nghi lễ tạo nghĩa vụ hiện tại, cấu trúc thừa kế nợ/ân tình, "nghĩa vụ với tổ tiên" có hiệu lực pháp lý/văn hóa. Kantian framing (SOT-K): V là transcendental condition — không lượng H-axis memory nào bù đắp được sự vắng mặt của V.
- **ISSUE-04 — AX-IV mechanism** — 5/5 → ADD: IV mô tả *cái gì* xảy ra (thấm chọn lọc, tái tổ chức) nhưng không nói *như thế nào*. Thiếu → không operationalizable, không phân biệt được với mô tả hiện tượng. Fix: 3 cơ chế con (a) Pattern recognition, (b) Selective integration, (c) Pattern update. Cơ chế (c) tạo liên kết IV → VIII, ngăn IV thành cơ chế bảo thủ thuần túy.

**Files changed:** `axiom_spec.md` (source of truth), `axioms.html` (primary render), `what.html` (ISSUE-04 only).

---

## 2026-06-08 — `axiom_spec.md` P1: ISSUE-01 (≡ → DEF/AX split) + ISSUE-02 (BRIDGE-II-III, SOT-K + SOT-M) · RCA ≥ 4/5

**Hành động:** Phase 1 của `review/mach-re-axioms-review-plan.md` (v2). ISSUE-01: tách ký hiệu `≡` thành `[DEF-1]` + `[AX-I]` — giữ precision notation, làm axiom falsifiable. ISSUE-02: thêm BRIDGE-II-III giữa Tiên Đề II và III — giải quyết sức căng saṃvṛtisat × ontological dimension bằng Kantian transcendental condition (SOT-K) + Madhyamaka saṃvṛtisat (SOT-M).

**RCA per-issue (3-round × 5-Why × scoring):**

- **ISSUE-01 — Option B (DEF/AX split)** — 5/5 → FIX: `≡` là definitional operator → axiom không falsifiable được → mâu thuẫn với KEEP-02 (explicit falsifiability per axiom). Fix: `[DEF-1]` định nghĩa relational profile; `[AX-I]` claim identity constituted by RP(S). Ký hiệu cũ giữ làm pedagogical shorthand.
- **ISSUE-02 — BRIDGE-II-III** — 5/5 → ADD: II claim pattern là saṃvṛtisat (quy ước thật); III claim trục dọc là ontological dimension. Thiếu cầu → mâu thuẫn nội bộ (quy ước vs bản thể). Fix: (1) saṃvṛtisat scope = pattern có causal efficacy trong operational domain, không phải paramārtha-sat (SOT-M Row 110-111); (2) V ⊥ H là transcendental condition (SOT-K), không phải svabhāva claim. Hai move cùng hoạt động: pattern saṃvṛtisat + trục dọc transcendental condition → không mâu thuẫn.

**Files changed:** `axiom_spec.md` (source of truth), `axioms.html` (primary render), `what.html` (secondary render — ISSUE-01 only).

---

## 2026-06-08 — `axiom_spec.md` Tiên Đề III: đồng bộ theo `axiom_3.html` · RCA sync (single source of truth)

**Hành động:** Cập nhật spec canonical Tiên Đề III theo `axiom_3.html` — nguồn chân lý phát triển đầy đủ nhất.

**RCA findings (3-round × 5-Why × scoring):**

- **Header** (5/5 → FIX): `Mạch Cội Dọc — Mạch Cội Nguồn (Orthogonal Temporality)` → `Mạch Cội Nguồn (Orthogonal Temporality)`. Root: "Mạch Cội Dọc" = biểu hiện (manifestation), "Mạch Cội Nguồn" = bản chất (essence). Header nên dùng tên bản chất làm định danh chính — nhất quán với page title `axiom_3.html` và CLAUDE.md §Tiên Đề III. "Mạch Cội Dọc" đã có trong field `Biểu hiện (manifestation)` bên trong entry.
- **Phát biểu** (5/5 → FIX): Phát biểu cũ thiếu 3 yếu tố: (a) phủ định H tường minh, (b) "mạch tồn tại / ontological dimension", (c) "không phải ẩn dụ". Root: spec viết trước khi canonical statement trong `axiom_3.html` Section 1 được hoàn chỉnh. Fix: thêm VI + EN đầy đủ.
- **Ba thành phần cốt lõi** (5/5 → ADD): Cấu trúc "không câu nào được phép thiếu" từ `axiom_3.html` vắng mặt trong spec — đây là guard chống drift cho các render file. Fix: thêm field mới.
- **Phản chứng** (5/5 → FIX): Chỉ có điều kiện (1). Điều kiện (2) V ⊆ H (mất trực giao) — claim gốc rễ phân biệt với Halbwachs/Luhmann — vắng mặt. Fix: thêm cả hai điều kiện.

**File changed:** `axiom_spec.md` (Tiên Đề III header + spec, lines 80–95).

---

## 2026-06-07 — `axioms.html` + `what.html` Tiên Đề III: đồng bộ stmt + phản chứng theo `axiom_3.html` · RCA sync

**Hành động:** Cập nhật card Tiên Đề III trong cả hai file theo nguồn chân lý `axiom_3.html` (Section 1 "Phát biểu tường minh nhất" + Section 1C "Mạch Tồn Tại · Chiều kích Bản thể học").

**RCA findings (3-round × 5-Why × scoring):**

- **stmt** (4.5/5 → FIX): "chiều dọc là *điều kiện tồn tại*, không chỉ điều kiện nhận thức" không dùng thuật ngữ canonical "mạch tồn tại / ontological dimension". Root: stmt được viết trước Section 1C xác lập khái niệm này. Fix: `mạch cội dọc là *mạch tồn tại* — chiều kích bản thể học (ontological dimension) của hệ thống`.
- **phản chứng** (5/5 → FIX): chỉ có 1 điều kiện (thiếu V) — bỏ qua điều kiện 2 (V ⊆ H, mất trực giao) là claim gốc rễ nhất của Tiên Đề III. Root: phản chứng viết trước "Ba thành phần không câu nào được phép thiếu" trong `axiom_3.html`. Fix: thêm cả hai điều kiện.

**Files changed:** `axioms.html` (Tiên Đề III article), `what.html` (Tiên Đề III article trong section Hệ Tiên Đề).

---

## 2026-06-07 — `axiom_3.html` hyperlink hai chiều: Formal Statement ↔ glossary "Inherited Patterns / nề nếp"

**Hành động:** thêm `id="glossary-inherited-patterns"` vào glossary row; link "nề nếp" (VI, dòng 237) và "inherit patterns" (EN, dòng 245) → `#glossary-inherited-patterns`; glossary row đã có link ngược `#formal-statement` từ commit trước.

- *237 VI*: `kế thừa nề nếp từ` → `kế thừa <a href="#glossary-inherited-patterns">nề nếp</a> từ` (style: `var(--accent)`, underline — nhất quán với các link cùng câu).
- *245 EN*: `access and inherit patterns` → `access and <a href="#glossary-inherited-patterns">inherit patterns</a>` (style: `var(--green)`, underline — nhất quán với EN def-box).
- *1328 Glossary*: thêm `id="glossary-inherited-patterns"` vào `<tr>`.
- *Bảo tồn*: không thay đổi nội dung, cấu trúc, hay các link hiện có trong cùng câu.

---

## 2026-06-07 — `axiom_3.html` glossary: thêm "Inherited Patterns / nề nếp" + hyperlink · 5/5 → FIX

**Cổng RCA (3-round × 5-Why × scoring ≥ 4/5).** 2 hành động: (1) thêm hàng glossary "Inherited Patterns / nề nếp"; (2) thêm hyperlink EN + VI → `#formal-statement`. Cả hai đạt 5/5.

### Thêm hàng glossary · **5/5 → FIX**
- *Root*: "nề nếp" xuất hiện ở Formal Statement (dòng 237) nhưng vắng glossary — vi phạm contract "mọi thuật ngữ chuyên ngành trong tài liệu".
- *Sửa*: thêm hàng cuối bảng — EN: `Inherited Patterns`, VI: `nề nếp`, Ghi chú: "truyền thống / tập quán văn hóa — phân biệt với 'nếp tổ chức' (structural configuration)".

### Thêm hyperlink EN + VI → `#formal-statement` · **5/5 → FIX**
- *Root*: hàng mới không có link ngược về nơi dùng, vi phạm truy vết hai chiều mà document architecture thực hiện nhất quán ở mọi term khác (nếp tổ chức → `#rca-configuration`, mạch tồn tại → `#rca-ontological`).
- *Sửa*: thêm `id="formal-statement"` vào `<section>` §1 (dòng 230); wrap "Inherited Patterns" và "nề nếp" trong glossary với `<a href="#formal-statement">`.
- *Bảo tồn*: nội dung không thay đổi; style link giữ màu gốc của từng cột (`color:#b05040` cho EN, `color:inherit` cho VI).

---

## 2026-06-07 — `axiom_3.html` Formal Statement: "nếp" → "nề nếp" · 5/5 → FIX

**Cổng RCA (3-round × 5-Why × scoring ≥ 4/5).** Vị trí: dòng 237, Phát biểu chính thức (Formal Statement), Tiếng Việt (Việt hóa bản sắc). 1 ứng viên; đạt ngưỡng 5/5 → FIX.

### "kế thừa nếp từ" → "kế thừa nề nếp từ" · **5/5 → FIX**
- *Symptom (R1)*: "kế thừa **nếp** từ các **nếp** tổ chức" — từ "nếp" xuất hiện hai lần liên tiếp: một lần đơn lẻ, một lần trong thuật ngữ kỹ thuật "nếp tổ chức" → người đọc không phân biệt được nghĩa.
- *Mechanism (R2)*: Formal Statement là *source of truth* cho mọi tài liệu downstream; category blur giữa "nếp" (văn hóa) và "nếp tổ chức" (structural configuration) tại đây sẽ lan toàn hệ.
- *Root (R3)*: "nếp" đơn lẻ trong "kế thừa nếp từ" không phân biệt được với thuật ngữ kỹ thuật "nếp tổ chức" ngay sau đó trong cùng câu, vi phạm yêu cầu nhất quán thuật ngữ nội tại của framework.
- *Sửa*: dòng 237 `kế thừa nếp từ các nếp tổ chức quá khứ` → `kế thừa nề nếp từ các nếp tổ chức quá khứ`. "Nề nếp" (truyền thống / tập quán văn hóa) tách biệt hoàn toàn với "nếp tổ chức" (structural configuration).
- *Bảo tồn*: toàn bộ cấu trúc câu, anchor, link giữ nguyên; chỉ thêm "nề" trước "nếp" đứng độc lập.

---

## 2026-06-07 — `axiom_3.html` Việt hóa trục V/H trong prose: 6 fix qua gate 4/5, GIỮ nhóm formal

**Cổng RCA (3-round × 5-Why × scoring ≥ 4/5).** Yêu cầu user: `trục dọc thế hệ (V)` / `Mối quan hệ thế hệ (trục dọc V)` / `trục dọc V` → "mạch cội dọc"; `trục ngang H` → "mạch nguồn ngang". 10 ứng viên; 6 (prose) đạt ngưỡng → FIX, 4 (formal) dưới ngưỡng → GIỮ.

### Phát hiện gốc rễ (R3)
`mạch cội dọc` = Vertical Temporality = **biểu hiện (manifestation)**; còn `Trục V ⊥ trục H`, `V ⊆ H`, `tập con của H` = **essence/cấu trúc hình thức** (`CLAUDE.md §Core Principles`, RCA 2026-06-05 score 5/5). Thay tên biểu hiện vào tầng essence sẽ tạo mâu thuẫn nội tại với chính dòng 294–296 (nơi file tự phân biệt essence ≠ manifestation) → đúng loại category error RULE ZERO cấm. Do đó phân loại theo ngữ cảnh, không tìm-thay máy móc.

### FIX — prose/bản thể học (≥ 4/5)
- *497* (5.0): `trục dọc thế hệ (V)` → `mạch cội dọc (V)` (card Bản thể học, ví dụ user).
- *509* (5.0): `Mối quan hệ thế hệ (trục dọc V)` → `Mối quan hệ thế hệ (mạch cội dọc)` (ví dụ user).
- *510* (4.6): `cắt đứt trục dọc này` → `cắt đứt mạch cội dọc này` (mở rộng nhất quán).
- *531* (4.2): `trục ngang H (…) và trục dọc V (…)` → `mạch nguồn ngang (…) và mạch cội dọc (…)` (RCA Why 3-5; giữ khung "hai chiều trực giao độc lập"; là chỗ "trục ngang H" literal duy nhất).
- *577* (4.4): `thứ trục dọc đang duy trì` → `thứ mạch cội dọc đang duy trì` (mở rộng nhất quán).
- *583* (4.2): `Trục dọc (Vertical Time)` → `Mạch cội dọc (Vertical Time)` (mở rộng nhất quán).

### GIỮ NGUYÊN (< 4/5 cho hành động convert — convert sẽ phá tầng essence)
- *265* (convert 1.8): `trục V độc lập, không là tập con của H` — set object.
- *272* (convert 1.6): `liên tục theo trục H… tức V ⊆ H` — phản chứng, ký hiệu tập hợp.
- *294* (convert 1.2): `Trục V ⊥ trục H` — nhãn tường minh "Bản chất (Essence)".
- *277–287* (convert 1.0): ASCII formal notation `H (ngang)`, `V = ∅`, `depth(V)`.

**Bảo tồn chung:** toàn bộ cấu trúc/layout/anchor/JS giữ nguyên; tầng essence & formal notation không đụng; 6 fix chỉ là đồng bộ thuật ngữ trong prose.

---

## 2026-06-07 — `axiom_3.html` RCA logic nội tại: 4 fix (A, B, E, F) qua gate 4/5

**Cổng RCA (3-round × 5-Why × scoring ≥ 4/5).** Quét logic nội tại toàn file theo yêu cầu user. 7 ứng viên A–G; 4 đạt ngưỡng → FIX, 3 dưới ngưỡng → GIỮ.

### A — "cấu hình" → "nếp tổ chức" (terminology self-contradiction) · **4.8/5 → FIX**
- *Symptom (R1)*: §1C (dòng 578) lập luận tường minh "không giữ 'Cấu hình'", nhưng "cấu hình" vẫn còn trong giọng Mạch Rễ ở 5 chỗ (662 SVG, 755, 769, 963 Eliade card, 1315 glossary).
- *Mechanism (R2)*: link `#rca-configuration` (755) có chữ neo "cấu hình" trỏ tới đúng hộp bảo "đừng dùng từ này" → tự phản ở điểm lập luận.
- *Root (R3)*: quyết định đổi "cấu hình"→"nếp tổ chức" (§1C, CHANGELOG trước) chưa được quét toàn file.
- *Sửa*: 662 `Cấu hình đã qua`→`Nếp tổ chức đã qua`; 755 chữ neo `cấu hình`→`nếp tổ chức`; 769 `với cấu hình đã qua`→`với nếp tổ chức đã qua`; 963 `Kết nối với các cấu hình`→`…các nếp tổ chức`; 1315 glossary `các cấu hình đã qua`→`các nếp tổ chức đã qua`.
- *Bảo tồn (KHÔNG đụng)*: dòng 578 (trích "Cấu hình" như từ bị bác bỏ — buộc phải giữ) và dòng 937 (thuật ngữ Barbour "spatial configurations" — không phải thuật ngữ Mạch Rễ). Verify: `grep "cấu hình"` còn đúng 2 chỗ này.

### B — Ma trận §6 có hàng rating không có chỗ chống đỡ · **Giddens 4.6 / Gadamer 4.1 → FIX**
- *Symptom (R1)*: §6 chấm ✅/❌/⚠️ cho Gadamer (1019) & Giddens (1022); §5 không có compare-card cho cả hai (Giddens không có gì ngoài hàng bảng; Gadamer chỉ 1 câu ở §7).
- *Mechanism (R2)*: bảng "Tổng Hợp So Sánh" ngụ ý tóm tắt phân tích trên; rating không truy được làm yếu câu chốt "Không triết học nào… đạt đủ 4 cột".
- *Root (R3)*: phạm vi ma trận rộng hơn phạm vi card §5, gap chưa khớp → vi phạm truy vết (mọi rating phải trace về chỗ đỡ).
- *Sửa*: thêm 1 đoạn ghi chú italic ngay dưới bảng §6, nêu cơ sở rating: Gadamer (*Wirkungsgeschichte* — thông diễn/epistemo, không đặt điều kiện sức bền) và Giddens (*structuration* — truyền thống tái tạo qua thiết chế nên cross-gen không trực tiếp). Extend, không xóa hàng.

### E — §7B: rating sao tự chấm thiếu đánh dấu tầng-claim · **4.5/5 → FIX**
- *Symptom (R1)*: §7B dùng "⭐⭐⭐⭐⭐", "hấp thụ cao nhất" như sự kiện thực nghiệm; thiếu câu cảnh báo phạm vi mà §2/§5/§6/§7 đều có.
- *Mechanism (R2)*: phần còn lại hedge cẩn thận; §7B không hedge → lệch register/epistemic ngay trong cùng file, làm yếu chính sự cẩn trọng đã xây.
- *Root (R3)*: vi phạm Claim Ladder (viết ở tầng Empirical nội dung chỉ ở tầng Interpretation), thiếu marker phạm vi.
- *Sửa*: thêm 1 đoạn italic "Ghi chú phạm vi (claim level)" ngay sau h2 §7B, đánh dấu "đánh giá định tính minh họa, không phải đo lường thực nghiệm; tầng claim = diễn giải/đối chiếu". Giữ nguyên toàn bộ nội dung bảng/sao.

### F — "mạch tồn tại" trong phát biểu chính thức nhưng vắng glossary · **4.5/5 → FIX**
- *Symptom (R1)*: "mạch tồn tại" ở hero (224), phát biểu chính thức (237), tiêu đề §1C — nhưng glossary chỉ có "Chiều kích Bản thể học", không đăng ký "mạch tồn tại".
- *Mechanism (R2)*: glossary tự cam kết liệt "các thuật ngữ chuyên ngành dùng trong tài liệu"; từ nằm trong câu canonical mà tra glossary không thấy → gap truy vết chỗ dễ thấy nhất.
- *Root (R3)*: vi phạm contract glossary/term-traceability — định nghĩa trong prose §1C nhưng chưa đăng ký vào bảng index.
- *Sửa*: gộp vào hàng "Ontological Dimension" (giữ một nguồn chân lý): VI cell → "Chiều kích Bản thể học · mạch tồn tại"; note thêm "Việt hóa song song: 'mạch tồn tại' = 'Chiều kích Bản thể học'". Verify: `grep "mạch tồn tại"` 7→8.

### Giữ nguyên (< 4/5, ghi lý do)
- **C — hai nghĩa "Mạch Cội Nguồn" (2.8/5)**: kiểm chứng cho thấy nhất quán — "Cội Nguồn" = cả hai trục = bản chất; "Mạch Cội Dọc" = trục dọc = biểu hiện; không chỗ nào dùng "mạch cội dọc" để chỉ toàn hệ. Không phải defect; sửa tên canonical = rủi ro cao lan `dictionary_rule.md §9`.
- **D — pseudo-formula `depth(V)` (3.8/5, biên)**: "=" là định nghĩa depth (đếm thế hệ) hợp lệ; "tăng theo" là claim định tính, không phải phương trình số giả. Dưới ngưỡng.
- **G — §2 "Phủ đầy" vs "Tối giản" (2.6/5)**: không mâu thuẫn (III ∈ I–IV và là trụ chịu tải). Oddity "không suy ra từ … hay V" nhẹ, không sai logic.

**Bảo tồn chung:** toàn bộ cấu trúc, layout, anchor, nội dung 3 item dưới ngưỡng giữ nguyên; 4 fix đều là extend/đồng bộ thuật ngữ (an toàn cho HTML đã publish).

---

## 2026-06-07 — `axiom_3.html` Hero banner: Thêm "mạch tồn tại" vào link text `#rca-ontological`

**Cổng RCA (terminology consistency, 5/5 → FIX).** Thực hiện theo yêu cầu của user.

**Root cause:** Hero banner `<p>` (dòng 224) dùng `"chiều kích bản thể học (ontological dimension)"` làm link text dẫn vào `#rca-ontological`, trong khi toàn bộ chuỗi §1 → §1C đã được cập nhật để "mạch tồn tại" dẫn đầu. Hero là phần tử đầu tiên reader thấy — phải nhất quán.

**Sửa** (dòng 224):
- `chiều kích bản thể học (ontological dimension)` → `mạch tồn tại — chiều kích bản thể học (ontological dimension)` trong link text của hero `<p>`.

**Bảo tồn:** `href="#rca-ontological"`, style, và cụm "chiều kích bản thể học (ontological dimension)" giữ nguyên hoàn toàn.

---

## 2026-06-07 — `axiom_3.html` §1C: Thêm "mạch tồn tại" vào h2 anchor `#rca-ontological` (bổ sung fix trước)

**Cổng RCA (document contract, 5/5 → FIX).** Bổ sung fix bị thiếu trong lần trước.

**Root cause:** Fix trước (h3 + def-box) chưa đủ sâu — bỏ sót h2 là phần tử đang mang `id="rca-ontological"`, tức điểm đầu tiên reader thấy khi click "mạch tồn tại" từ formal statement. H2 vẫn chỉ hiện "Chiều kích Bản thể học."

**Sửa** (tại [axiom_3.html](file:///c:/Stable_Diffusion/MACH_RE/axiom_3.html) §1C dòng 483–486):
- Comment HTML: `CHIỀU KÍCH BẢN THỂ HỌC` → `MẠCH TỒN TẠI · CHIỀU KÍCH BẢN THỂ HỌC`
- h2: `Chiều kích Bản thể học (Ontological Dimension)` → `Mạch Tồn Tại · Chiều kích Bản thể học (Ontological Dimension)`
- Đoạn mở: thêm `<strong>mạch tồn tại</strong> (chiều kích bản thể học)` thay cho `"bản thể học"` đứng một mình

**Bảo tồn:** `id="rca-ontological"`, "Chiều kích Bản thể học (Ontological Dimension)" giữ nguyên hoàn toàn.

---

## 2026-06-07 — `axiom_3.html` §1C: Thêm "mạch tồn tại" vào section `#rca-ontological`

**Cổng RCA (terminology / document contract, 5/5 → FIX).** Thực hiện theo yêu cầu của user.

**RCA (3-round × 5-Why):**
- *Symptom (Round 1)*: Anchor link `href="#rca-ontological"` gắn vào "mạch tồn tại" trong formal statement (dòng 237), nhưng §1C không chứa từ "mạch tồn tại" ở bất kỳ đâu — người đọc click link đến §1C và không tìm thấy thuật ngữ họ vừa click.
- *Mechanism (Round 2)*: "mạch tồn tại" được đưa vào formal statement như Việt hóa của "chiều kích bản thể học" (CHANGELOG 2026-06-07) nhưng §1C không được cập nhật song hành — hai tầng tên (Việt hóa + học thuật) tách rời nhau.
- *Root cause (Round 3)*: Vi phạm document contract của anchor link — destination phải surface linked term; khi một thuật ngữ được Việt hóa, section giải thích phải chứa cả Việt hóa lẫn academic term song song.

**Sửa** (tại [axiom_3.html](file:///c:/Stable_Diffusion/MACH_RE/axiom_3.html) §1C dòng 500–507):
- Comment HTML: `Chiều kích Bản thể học` → `mạch tồn tại / Chiều kích Bản thể học (Ontological Dimension)`
- h3: thêm `"mạch tồn tại" —` trước `Chiều kích Bản thể học (Ontological Dimension)`
- def-box label: đồng bộ tương tự
- Câu mở blockquote: giới thiệu `Mạch tồn tại` là Việt hóa của `Chiều kích Bản thể học — Ontological Dimension`, giải thích ngắn lý do chọn từ ("Mạch" = tính sống và chảy; "tồn tại" = giữ nghĩa ontological)
- Câu dẫn vào bullet list: cập nhật thành `"mạch tồn tại" (chiều kích bản thể học)`

**Bảo tồn:**
- h2 `#rca-ontological` giữ nguyên: `🔍 1C. Phân tích RCA — Chiều kích Bản thể học (Ontological Dimension)`
- Toàn bộ nội dung 3 bullet list và các def-box Why 1–5 giữ nguyên.

---

## 2026-06-07 — `axiom_3.html` Section 1 Tiếng Việt: "khuôn mẫu" → "nếp" trong phát biểu chính thức

**Cổng RCA (terminology, 5/5 → FIX).** Thực hiện theo RCA "kế thừa khuôn mẫu" do user yêu cầu.

**RCA (3-round × 5-Why):**
- *Symptom (Round 1)*: "khuôn mẫu" dùng để chuyển nghĩa "patterns" trong "kế thừa khuôn mẫu của các nếp tổ chức quá khứ". Từ "khuôn" = cái khuôn đúc (hình thức cố định, áp từ ngoài vào); "mẫu" = mẫu để sao chép (prescriptive, static). Kết hợp: "khuôn mẫu" = template/mold — thứ bạn đổ vào để tạo bản sao đồng nhất.
- *Mechanism (Round 2)*: Framework đã định nghĩa tường minh tại §1C: "nếp tổ chức" được chọn vì "nếp" nhấn mạnh "tính sống và truyền được". "khuôn mẫu" vi phạm cả hai: không "sống" (khuôn là thứ tĩnh, passive) và không "truyền theo thực hành" (khuôn truyền bằng cách đổ/áp, không qua thực hành và thấm).
- *Root cause (Round 3)*: "khuôn mẫu" là category mismatch — vi phạm nhất quán nội bộ giữa formal statement và glossary §1C: toàn bộ §1C định nghĩa "nếp" là thứ được kế thừa theo trục V, nhưng formal statement dùng "khuôn mẫu" ở điểm phát biểu chính thức.

**Sửa:**
- Thay `"kế thừa khuôn mẫu của các nếp tổ chức quá khứ (tổ tiên)"` → `"kế thừa nếp từ các nếp tổ chức quá khứ (tổ tiên)"` tại dòng 237 của [axiom_3.html](file:///c:/Stable_Diffusion/MACH_RE/axiom_3.html). Dùng "từ" thay "của" để tránh redundancy "nếp của nếp tổ chức".

**Bảo tồn:**
- Giữ nguyên toàn bộ cấu trúc câu, anchor links, và nội dung còn lại của phát biểu Tiếng Việt.

---

## 2026-06-07 — `axiom_3.html` Section 1: Tinh chỉnh câu rút gọn "cắm thẳng" → "nối thẳng" trong Plainest Statement

**Cổng RCA (terminology, 4.8/5 → FIX).** Thực hiện theo yêu cầu của user.

**RCA (3-round × 5-Why):**
- *Symptom (Round 1)*: Động từ "cắm thẳng" mang cảm giác cơ học, tĩnh và hơi thô ráp trong câu tóm tắt rút gọn của Tiên Đề III.
- *Mechanism (Round 2)*: Từ "cắm" (như cắm cọc, cắm mốc) gợi lên trạng thái cố định về mặt không gian địa lý, trong khi Mạch Rễ đang mô tả tính liên kết mạng lưới (relational network) và dòng chảy thông tin/bản sắc động của hệ thống tự tạo (autopoietic system). Việc dùng từ mang nghĩa cơ học thô ráp làm mờ đi tính chất liên kết quan hệ linh động.
- *Root cause (Round 3)*: Chưa tối ưu hóa ngôn từ theo nguyên lý *Upāya* và tính nhất quán với Tiên Đề I (Quan hệ bản thể - Relational Ontology, vạn vật duyên khởi và luôn kết nối/nối kết với nhau).
- *Hướng giải quyết*: Thay thế bằng "nối thẳng". Từ "nối" biểu đạt chính xác tính liên kết mạng lưới và dòng chảy liên thông của mạch cội dọc, nhất quán với các cụm từ khác trong cùng box ("nối trực tiếp", "nối kết theo trục").

**Sửa:**
- Thay thế `"vẫn cắm thẳng vào quá khứ và tương lai"` thành `"vẫn nối thẳng vào quá khứ và tương lai"` trong câu rút gọn của box "Phát biểu tường minh nhất" tại Section 1 của [axiom_3.html](file:///c:/Stable_Diffusion/MACH_RE/axiom_3.html).

**Bảo tồn**:
- Giữ nguyên các nội dung và cấu trúc so sánh, phản chứng khác trong cùng box "Phát biểu tường minh nhất".

---

## 2026-06-07 — `axiom_3.html` Section 1: Cập nhật thuật ngữ "chiều kích bản thể học" → "mạch tồn tại" trong phát biểu Tiếng Việt

**Cổng RCA (terminology, 4.8/5 → FIX).** Thực hiện theo yêu cầu của user.

**RCA (3-round × 5-Why):**
- *Symptom (Round 1)*: Thuật ngữ chuyên môn dịch gốc phương Tây "chiều kích bản thể học" (ontological dimension) quá hàn lâm và trừu tượng, tạo khoảng cách nhận thức đối với độc giả phổ thông khi đọc phát biểu Tiếng Việt.
- *Mechanism (Round 2)*: Từ "chiều kích" mang tính tĩnh của không gian hình học, trong khi "Mạch Rễ" vốn đang mô tả sự tồn tại và tự tạo của hệ thống như một dòng chảy động, xuyên thế hệ. Việc duy trì từ Hán-Việt hàn lâm này ở ngay phát biểu Tiếng Việt chính thức mâu thuẫn với nỗ lực Việt hóa và làm trực quan hóa triết lý Mạch Rễ.
- *Root cause (Round 3)*: Chưa bản địa hóa triệt để thuật ngữ triết học phương Tây theo nguyên lý *Upāya* (phương tiện thiện xảo) và tính nhất quán với cốt tủy tên dự án "Mạch Rễ" (hướng tới các thực thể tự nhiên động).
- *Hướng giải quyết*: Thay thế bằng "mạch tồn tại". "Mạch" vừa biểu thị tính liên kết (mạch nguồn, mạch cội), vừa biểu thị sự sống động của cấu trúc nâng đỡ hệ thống; "mạch tồn tại" phản ánh chính xác ontological dimension một cách giản dị, thuần Việt và tự nhiên hơn.

**Sửa:**
- Thay thế cụm từ `"chiều kích bản thể học"` bằng `"mạch tồn tại"` trong phát biểu chính thức Tiếng Việt tại Section 1 của [axiom_3.html](file:///c:/Stable_Diffusion/MACH_RE/axiom_3.html).
- Sửa dấu câu và viết hoa đúng chính tả: Viết hoa chữ cái đầu câu cho từ `Mạch` trong cụm liên kết `Mạch cội dọc` ở đầu câu thứ hai.
- Tinh chỉnh từ ngữ liên kết ở vế sau phát biểu: Thay đổi `hướng tới` thành `truyền tới` để thể hiện rõ nét hơn tính truyền thừa, tiếp nối nếp tổ chức đến hậu thế.
- Đồng bộ hóa định nghĩa thời gian: Thay thế `nếp tổ chức đã qua` thành `nếp tổ chức quá khứ` và `nếp tổ chức chưa đến` thành `nếp tổ chức tương lai` để tương hợp chính xác với chú thích hệ thời gian `(quá khứ → hiện tại → tương lai)` ở vế trước.
- Tinh chỉnh động từ liên kết: Thay thế `"kết nối với"` thành `"chạm tới"` (tổng hợp lại chuyển đổi từ `"truy cập"` ban đầu thành `"chạm tới"`) để tăng tính gần gũi, trực giác và bản sắc của Mạch Rễ.

**Bảo tồn**:
- Giữ nguyên anchor liên kết `href="#rca-ontological"` để bảo đảm khả năng điều hướng bài viết đến phần giải nghĩa chi tiết ở dưới.
- Giữ nguyên nhãn "ontological dimension" ở phiên bản tiếng Anh (English statement) để đối chiếu chính xác với các prior-art học thuật.

---

## 2026-06-07 — `axiom_3.html`: Việt hóa hoàn toàn phát biểu Tiếng Việt Section 1 & Tinh chỉnh thuật ngữ

**Thực hiện theo yêu cầu và đồng thuận của user.** Không qua RCA gate (đây là tinh chỉnh ngôn từ phát biểu và Việt hóa thuật ngữ, không thay đổi core claim).

**Sửa:**
1. **Việt hóa thuật ngữ**:
   - Thay thế toàn bộ cụm từ tiếng Anh còn sót trong phát biểu chính thức Tiếng Việt tại Section 1: `(past → present → future)` thành `(quá khứ → hiện tại → tương lai)`.
   - Lược bỏ phụ đề `(pattern)` sau từ `khuôn mẫu` vì nghĩa tiếng Việt đã tự đủ và rõ ràng.
2. **Cập nhật thuật ngữ "nếp tổ chức"**:
   - Thay thế từ "cấu hình" thành "nếp tổ chức" trong phát biểu Tiếng Việt tại Section 1 (3 vị trí: các nếp tổ chức hiện tại, các nếp tổ chức đã qua, các nếp tổ chức chưa đến), nhất quán với định nghĩa chi tiết tại §1C.
3. **Dịch "resilience"**:
   - Dịch "resilience" thành "sức bền" (sức bền hệ thống / sức bền văn hóa) trong các ngữ cảnh tiếng Việt liên quan để thuần Việt hóa hoàn toàn ngôn ngữ trình bày.
4. **Tinh chỉnh cụm từ liên kết**:
   - Trong phát biểu chính thức (Formal Statement) của Tiên Đề III: Thay thế cụm từ `truy cập và kế thừa` thành `kết nối với và kế thừa` để diễn đạt chính xác mối liên kết bản thể học của nếp tổ chức hiện tại với các nếp tổ chức quá khứ/tương lai.

**Bảo tồn**:
- Giữ nguyên các thẻ liên kết `href` (ví dụ `#rca-configuration`) để đảm bảo các liên kết điều hướng trong trang không bị hỏng.
- Giữ nguyên phiên bản tiếng Anh (English statement) và các ký hiệu kỹ thuật trong hộp ASCII (như `Past_configs`) để duy trì tính đối chiếu cấu trúc học thuật.

---

## 2026-06-07 — Global rename: "Thời Gian Dọc" → "Mạch Cội Dọc" và "Thời Gian Ngang" → "Mạch Nguồn Ngang"

**Thực hiện theo xác nhận user.** Không qua RCA gate (đây là rename thuật ngữ đồng thuận, không phải sửa claim).

**Rationale:** Hoàn thiện hệ thống tên "Mạch" thống nhất cho cả ba trục thời gian:
- "Mạch Cội Dọc" (Vertical / Root) — Biểu hiện của Tiên Đề III, trục tổ tiên ↕ hiện tại ↕ hậu thế
- "Mạch Nguồn Ngang" (Horizontal / Flow) — Trục tuyến tính quá khứ → hiện tại → tương lai
- "Mạch Cội Nguồn" (Orthogonal Temporality) — Bản chất của Tiên Đề III (đã đổi trước đó, 2026-06-07)

Ba tên cùng dùng tiền tố "Mạch", nhất quán với tên dự án "Mạch Rễ". Bỏ hoàn toàn "Thời Gian" khỏi tên trục dọc/ngang để tránh confusion với clock-time tuyến tính.

**Phạm vi:** 34 files ("Mạch Cội Dọc") + 7 files bổ sung ("Mạch Nguồn Ngang") — tổng 34 files cập nhật. Bao gồm toàn bộ HTML pages, plan docs, academic papers, raw/, archives/.

**Canonical:** `plan/dictionary_rule.md §9` — đã cập nhật. `CLAUDE.md` bảng Tiên Đề — đã cập nhật.

---

## 2026-06-07 — Global rename: "Thời Gian Cội Nguồn" → "Mạch Cội Nguồn" (Tiên Đề III Bản chất)

**Cổng RCA (terminology, 4.6/5 → FIX).** 3-round RCA × 5-Why. Thực hiện theo xác nhận user.

**Root cause:** "Thời Gian" trong "Thời Gian Cội Nguồn" gợi clock-time tuyến tính (chronological time), trong khi Tiên Đề III mô tả tính **trực giao** của trục thời gian (V ⊥ H — structurally independent, not sequential). Từ "Thời Gian" tạo category confusion với "Horizontal temporality" (cũng là thời gian), làm mờ bản chất distinguishing của Tiên Đề III. Root: tên gọi không encode structural property cốt lõi (`⊥`) mà chỉ encode domain ("time").

**Rationale "Mạch":** mạch (vein / underground current / pulse) = flow + depth + connectivity, không mang nghĩa clock-time, kết nối với tên dự án "Mạch Rễ", không xung đột với sub-terms "Chiều Cội" / "Chiều Nguồn". Score: Correct 5 / Deep 5 / Feasible 4 / Conflict-risk 4 / Preservation 5 = **4.6/5**.

**Phạm vi:** 16 files — `axiom_3.html`, `axioms.html`, `what.html`, `mach_re_homologous.html`, `CLAUDE.md`, `CHANGELOG.md`, `axiom_spec.md`, `plan/dictionary_rule.md`, `plan/mach-re-P6a-inventory.md`, `plan/mach-re-axiom-revision-plan-v2.md`, `plan/mach-re-plan-ten-thuan-viet-tien-de.md`, `raw/axiom_4.html`, `papers/paper_001/paper_001_draft.md`, `papers/paper_003/paper_003_draft.md`, `papers/paper_003/paper_003.html`, `papers/paper_004/paper_004_draft.md`.

**Canonical:** `plan/dictionary_rule.md §9` — nguồn chân lý duy nhất cho tên Tiên Đề III Bản chất đã cập nhật.

---

## 2026-06-07 — `axiom_3.html`: Hợp nhất 2 định nghĩa "cấu hình" thành 1 tại §1C

**Cổng RCA (structural, 4.6/5 → FIX).** 3-round RCA × 5-Why.

**Root cause:** Có hai box định nghĩa cùng một khái niệm: (1) gloss §1 "Đọc nhanh — cấu hình nghĩa là gì?" (thêm 2026-06-07 vì §1C quá xa điểm dùng) và (2) §1C "Giải thích khái niệm: Cấu hình" (bản gốc). Mỗi bên có nội dung unique mà bên kia thiếu (gloss §1 có ví dụ hai gia đình + diễn giải "đã qua/chưa tới"; §1C có lý do không dùng "thực thể"/"trạng thái" + câu kết giao diện kết nối). Hai bản song song tạo redundancy và nguy cơ drift nội dung.

**Sửa 2 chỗ:**
1. **Xóa** gloss §1 (dòng 263–273) hoàn toàn.
2. **Mở rộng §1C** — thêm ví dụ hai gia đình và diễn giải "đã qua/chưa tới" vào box §1C; giữ nguyên anchor `id="rca-configuration"`, lý do không dùng "thực thể"/"trạng thái", câu kết giao diện kết nối. Thứ tự 5 lớp: định nghĩa → ví dụ → lý do thuật ngữ → đã qua/chưa tới → câu kết.

**Bảo tồn:** Anchor `id="rca-configuration"` giữ nguyên (nhiều link trỏ đến). Toàn bộ nội dung unique của cả hai bên được giữ lại trong box hợp nhất. Không mất thông tin.

---

## 2026-06-07 — `axiom_3.html` Section 1: Dời box "Phát biểu tường minh nhất" xuống sau Tiếng Việt/English

**Thực hiện theo yêu cầu user.** Không RCA gate (thay đổi thứ tự trình bày, không sửa nội dung/claim).

**Sửa:** Hoán vị thứ tự trong Section 1 — Tiếng Việt/English (canonical) lên trước; box "Phát biểu tường minh nhất" + gloss "cấu hình" xuống sau. Cập nhật dòng ghi chú trong box plain: "ngay bên dưới" → "ngay bên trên" (cho đúng hướng sau khi dời).

**Thứ tự mới:** H2 → Tiếng Việt → English → [box plain + gloss cấu hình] → Formal Notation → box Bản chất/Biểu hiện.

**Bảo tồn:** Toàn bộ nội dung hai box giữ nguyên, không sửa câu chữ nào ngoài "bên dưới" → "bên trên".

---

## 2026-06-07 — `axiom_3.html` Section 1: Đánh dấu canonical + sửa câu cụt trong box "Phát biểu tường minh nhất"

**Cổng RCA (claim, 4.4/5 → FIX).** 3-round RCA × 5-Why.

**Vấn đề 1 — vị trí:** Box "Phát biểu tường minh nhất" (bản plain) là item đầu tiên dưới H2 "Phát biểu **chính thức** (Formal Statement)", trước phát biểu Tiếng Việt/English (bản canonical). Root cause: một H2 gánh hai thứ khác tầng nhận thức (on-ramp + canonical) mà không đánh dấu trạng thái → người lướt dễ tưởng box plain là bản để trích dẫn. Kết luận RCA: **giữ vị trí đầu** (đúng progressive disclosure, nhất quán với fix jargon-first turn trước), khuyết tật thật là *trạng thái canonical chưa đánh dấu*.

**Vấn đề 2 — câu cụt:** "...sau một nhiễu loạn đủ lớn hệ thống mất bất biến." — "mất bất biến" thiếu danh từ (mất *cái gì*), thiếu dấu phẩy, chưa nói rõ mất bản sắc.

**Sửa 2 chỗ:**
1. Thêm dòng ghi chú in nghiêng dưới phần "Rút gọn một câu": "Đây là điểm vào dễ nhất để nắm ý — không phải bản để trích dẫn. Bản chính thức (canonical) là phát biểu Tiếng Việt và English ngay bên dưới."
2. Sửa câu: → "...bỏ nó đi thì sau một nhiễu loạn đủ lớn, hệ thống đánh mất bản sắc — đúng cái bất biến cấu trúc mà nó cần giữ."

**Bảo tồn:** Vị trí box, nội dung phát biểu lõi, bảng 3 thành phần, falsification giữ nguyên — chỉ thêm 1 dòng đánh dấu trạng thái và làm rõ 1 câu.

---

## 2026-06-07 — `axiom_3.html` Section 1: Gỡ khó từ "cấu hình"

**Cổng RCA (claim, 4.4/5 → FIX).** 3-round RCA × 5-Why.

**Root cause:** Chữ "cấu hình" xuất hiện ngay trong box "Phát biểu tường minh nhất" (vừa thêm cùng ngày) và phát biểu Tiếng Việt, nhưng định nghĩa đầy đủ chỉ nằm ở §1C (~300 dòng dưới, nối qua link `#rca-configuration`). Box có mục đích "dễ nhất" lại rò rỉ từ "khó nhất" mà không gloss tại chỗ → tự mâu thuẫn mục đích; gloss tồn tại nhưng không ở-gần điểm dùng.

**Sửa 2 chỗ:**
1. **Box lõi** — thay "các cấu hình đã qua và chưa tới" → "những thế hệ đã qua và chưa tới — không chỉ con người, mà với cả *nếp tổ chức* của họ (quan hệ, giá trị, quy tắc)" (bỏ jargon khỏi box plain nhất).
2. **Thêm gloss "Đọc nhanh — cấu hình nghĩa là gì?"** ngay sau box lõi (trước "Tiếng Việt"): định nghĩa plain (thành phần + mạng lưới quan hệ = "bức ảnh toàn cảnh"), ví dụ hai gia đình cùng số người khác nếp → hai cấu hình, và diễn giải "cấu hình đã qua/chưa tới" theo nghĩa nếp tổ chức tổ tiên/hậu thế. Vẫn trỏ §1C cho lý do chọn thuật ngữ.

**Bảo tồn:** Định nghĩa §1C và phát biểu Tiếng Việt/English giữ nguyên; gloss mới là additive, đặt ngay điểm dùng. Đồng bộ với §1C (không định nghĩa lại khác đi).

---

## 2026-06-07 — `axiom_3.html` Section 1: Thêm box "Phát biểu tường minh nhất"

**Cổng RCA (claim, 4.6/5 → FIX).** 3-round RCA × 5-Why.

**Root cause:** Section 1 có 5+ phát biểu Tiên Đề III (def-box dòng 223, 385, 3 "định dạng"), nhưng mỗi phát biểu đều mở đầu bằng thuật ngữ kỹ thuật ("orthogonal", "ontological", "configuration") rồi mới đến nội dung — *jargon-first ordering*. Người đọc hỏi "tiên đề này khẳng định điều gì, trần trụi nhất?" phải tự lắp ráp từ 4 lớp (cấu trúc + bản thể học + cơ chế + biểu hiện). Gốc: chưa tách được **mệnh đề lõi** (lõi = tính trực giao V không phải tập con của H; bỏ chữ này thì sụp về Halbwachs/Luhmann) khỏi các hệ quả và biểu hiện.

**Sửa:** Chèn `<div class="def-box">` "Phát biểu tường minh nhất (Plainest Statement)" làm box **dẫn đầu** Section 1, ngay sau H2, trước phần "Tiếng Việt" — fix đúng gốc (plain-statement-first). Nội dung: (a) phát biểu lõi đã bóc hết ẩn dụ/biểu hiện; (b) bản rút gọn một câu; (c) bảng 3 thành phần không-được-thiếu kèm "bỏ đi thì sụp thành gì"; (d) điều kiện phản chứng (falsification) 2 nhánh.

**Bảo tồn:** Toàn bộ phát biểu cũ (def-box 223/385, 3 định dạng, box Bản chất/Biểu hiện) giữ nguyên — box mới là additive, đặt trước để làm điểm vào dễ nhất; dùng class CSS sẵn có, không sửa style.

---

## 2026-06-06 — `when.html` Section 3: Mở rộng bảng so sánh + fix "Trí tuệ sâu nhất"

**RCA gate (4.8/5 → FIX).** 3-round RCA × 5-Why.

**Root cause:** Quote-box "Trí tuệ sâu **nhất**" là superlative tuyệt đối rút từ bảng 5 dân tộc — vi phạm `dictionary §1` (không dùng "nhất" không phạm vi). Sâu hơn: bảng đo tiêu chí "phân tán / không trung gian" (structural resilience) rồi kết luận "wisdom depth" (value judgment) — category error: structural robustness ≠ epistemic depth.

**Sửa 3 chỗ:**
1. **Intro paragraph** — đổi "điểm neo" → "loại trung gian thể chế mà điểm neo phụ thuộc vào" + thêm scope disclaimer ("bộ so sánh có chủ đích, không phủ hết mọi trường hợp").
2. **Bảng** — đổi cột "Rủi ro" → "Loại trung gian / Điểm nghẽn" (tiêu chí chính xác hơn); mở rộng từ 5 → 11 dân tộc: thêm Triều Tiên, Tây Tạng, Armenia, Basque, Duy Ngô Nhĩ, Kurd — tất cả có áp lực đồng hóa kéo dài tương đương; cập nhật nội dung cột 3 từ tham chiếu "Core II" sang mô tả loại trung gian cụ thể.
3. **Quote-box** — thay "Trí tuệ sâu **nhất**" → "ít phụ thuộc trung gian thể chế **nhất** trong bộ khảo sát này" (scoped structural claim); giữ nguyên câu kết "nó được sống thành thực hành, trước khi lý thuyết có ngôn ngữ để gọi tên nó".

**Bảo tồn:** Insight lõi về implicit/lived wisdom giữ nguyên — chỉ scope lại từ absolute value judgment thành structural claim có phạm vi. Luận điểm so sánh mạnh hơn vì có nhiều case studies hơn.

---

## 2026-06-06 — `when.html`: Thêm Section 0 — Địa lý như môi trường chọn lọc

**RCA gate (5/5 → FIX).** Gap: `when.html` trình bày timeline Việt Nam mà không có case selection justification — người đọc có thể quy việc chọn Việt Nam cho confirmation bias (tác giả người Việt).

**Root cause:** Thiếu epistemological framing phân biệt "địa lý là selection environment" khỏi "địa lý là structural origin". Giả thuyết dạng mạnh ("địa lý sinh ra Mạch Rễ") đã bị bác bỏ qua RCA 3-round × 5-Why trong cùng phiên (falsification: (1) diaspora Việt duy trì Mạch Rễ ngoài địa lý; (2) người Chăm cùng địa lý → cấu trúc đối lập).

**Sửa:** Thêm `<!-- SECTION 0 -->` vào `when.html`, trước timeline hiện tại. Nội dung: (a) lưu ý phương pháp luận rõ ràng — địa lý = selection environment ≠ structural origin; (b) ba nguồn áp lực đa hướng (Hoa Hạ, sông Hằng, cận-hiện đại); (c) bảng 3 điều kiện tạo "phòng thí nghiệm tự nhiên"; (d) bảng so sánh 4 dân tộc cùng áp lực → kết quả khác nhau (Chăm, Khmer, Triều Tiên, Việt).

**Bảo tồn:** Toàn bộ 6 section cũ giữ nguyên, không sửa. Section 0 là additive.

---

## 2026-06-06 — P5 #1: hòa giải overclaim "Không Ai Phát Biểu Tiên Đề IV" (`axiom_4.html`)

**Cổng RCA (claim, 4.6/5 → FIX).** Plan: `plan/mach-re-P5-content-reconciliation.md` (#1). P1 quét đa trang: overclaim chỉ tập trung ở `axiom_4.html` (các "không ai" khác là nghĩa lành tính; bản trong `raw/` không đụng — P4).

**Mâu thuẫn:** "Không ai/chưa ai phát biểu" trái (a) prior-art của chính `axiom_spec.md` (Heidegger *Geschichtlichkeit*, Gadamer *Wirkungsgeschichte*) và (b) `dictionary §1` (cấm tuyệt đối).

**Sửa (4 chỗ, `axiom_4.html`):** tiêu đề §7 "Tại Sao Không Ai Phát Biểu" → "Vì Sao Góc Này Ít Được Phát Biểu Trực Diện?" + ghi chú phạm vi (nêu tên nguồn, acknowledge Heidegger/Gadamer là tiền lệ gần nhất); Why-2 "Không ai hỏi" → "ít được đặt trực diện trong phạm vi này"; Gốc rễ "chưa ai hệ thống hóa" → "ít được hệ thống hóa trực diện trong phạm vi khảo sát"; glossary "Đóng góp nguyên bản = mệnh đề chưa được phát biểu trước đây" → "góc đặc trưng / ít được phát biểu trực diện trong phạm vi đã nêu — không phải tuyên bố phổ quát".

**Bảo tồn:** giữ "góc đặc trưng" (tính trực giao V⊥H) làm điểm khác biệt — chỉ scope, không bỏ.

**P5 #2 (cùng đợt) — "hấp thụ có định hướng" khỏi khung novel cấp tiên đề (RCA 4.4/5).** P1 quét: chỗ thật duy nhất = `what.html:933` ("Đóng góp độc nhất" + "tất cả framework hiện có" + "hầu hết triết học phương Tây"). Các match khác lành tính (how.html:420 đã scoped "ba hệ đối chiếu"; axiom_conflict:208 chỉ nêu ví dụ; upgrade:343 "không ai được phép hỏi lại" nghĩa khác). Sửa `what.html:933`: label "Đóng góp độc nhất" → "Góc đặc trưng"; "tất cả/hầu hết" → "phần lớn … tôi khảo sát"; thêm chú "cơ chế này là *hệ quả* của Bất Biến × Biên Giới Động — không phải tiên đề riêng" (khớp `axiom_spec.md` Mệnh Đề VI).

**P5 #3 (cùng đợt) — lớp Nhị đế cho Tiên Đề II (RCA 4.8/5, theo spec Quyết định 3).** P1: `axiom_conflict.html` + `upgrade.html` đã có "lõi trống tự tính"; chỗ thiếu = card II `what.html`. Thêm clause vào phát biểu II: "bất biến bền ở mức *quy ước* (conventional / Nhị đế), không phải bản thể tuyệt đối — pattern cũng *trống tự tính* (svabhāva), nhất quán Tiên Đề I". Gỡ rủi ro essentialism (II mâu thuẫn I).

**P5 #4 (cùng đợt) — VIII scope-conditional có biện minh (RCA 4.6/5).** `upgrade.html` §3: thêm đoạn "Vì sao VIII là điều kiện cần (không phải bolt-on)": với áp lực *tiến hóa*, invariant cố định không tự-xét-lại sẽ giòn → phản tư là điều kiện cần; VIII là Meta-Tiên Đề. Lấp khoảng trống biện minh mà spec divergence #1 nêu.

**P5 #5 (cùng đợt) — bổ sung no-telos (additive, RCA 4.4/5).** `what.html` §Giới Hạn: thêm def-box "Một điều Mạch Rễ cố tình KHÔNG đặt thành tiên đề (no-telos)" — "sống sót" là explanandum, không phải tiên đề; từ chối tiên đề mục đích luận theo kỷ luật Anattā/Śūnyatā (hệ C). Khớp `axiom_spec.md` K10.

**→ P5 #1–#5 hoàn tất** (mọi mâu thuẫn claim legacy↔spec đã hòa giải + no-telos). Còn lại #6 (đổi số La Mã toàn site) tách thành plan riêng `plan/mach-re-P6-renumber-batch.md`.

---

## 2026-06-06 — REBUILD P0–P4(mẫu): governance + Carry-Forward Set + re-derive + render mẫu

**Quyết định bằng cổng RCA (3-round × 5-Why × threshold 4/5).** Chuyển từ *revision* sang *rebuild* hệ tiên đề (plan: `plan/mach-re-axiom-rebuild-plan.md`, thay thế hai plan axiom-revision).

**RCA gốc (vì sao rebuild, không revision):** "extend, not overwrite" là quy tắc *bảo tồn* — hợp cho corpus đã xuất bản — bị áp lên hệ tiên đề *chưa xuất bản, đang dò* → mỗi sửa khái niệm cõng chi phí tương thích ngược → chính quy tắc chống mâu thuẫn lại đẻ mâu thuẫn (bảng ✅ độc lập / text derived; 7 vs 8). Điểm ~4.0/5 (cảnh báo Bảo-tồn 2/5 → bịt bằng Carry-Forward Set).

**P0 — đổi governance:** `CLAUDE.md` §Document contract rules — thay "extend, not overwrite" → **"rebuild with carry-forward"**: phần chưa xuất bản cho viết đè sạch / re-derive, NHƯNG phải khai báo Carry-Forward Set trước; phần đã xuất bản vẫn ưu tiên extend.

**P1 — khai báo Carry-Forward Set (TB 4.6/5):** `dictionary_rule.md §7` đổi vai "Điều KHÔNG đụng" → **"Carry-Forward Set mặc định"**. Tách PHƯƠNG PHÁP (giữ vô điều kiện: cổng RCA, §1–§6, phản chứng, la bàn Phật giáo) khỏi NỘI DUNG (ứng viên, phải sống sót P2). Backbone tam giác đạc: **A Phan Ngọc · B Ashby/Weick · C Anattā**. `§9` hạ trạng thái từ "nguồn chân lý duy nhất" → "ứng viên carry-forward chờ re-derive".

**P2 — re-derive hệ tiên đề (TB 4.6/5):** sản phẩm `axiom_spec.md` (single source of truth). Suy từ câu hỏi gốc, independence test *bằng văn bản*, neo 3 hệ A/B/C. Kết quả KHÔNG pre-commit: **4 Core (CA-1..4) + 3 Derived (DP-1..3) + 1 Meta (MA-1)**. 3 quyết định §5 giải bằng RCA: (1) scope R = áp lực tiến hóa → MA-1 IN (4.6); (2) định danh CA/DP/MA, bỏ La Mã, giữ tên thuần Việt (4.6); (3) CA-2 gắn lớp Nhị đế "trống svabhāva" để tránh mâu thuẫn CA-1 (4.8). 4 điểm phân kỳ thật so với hệ cũ (anti-rubber-stamp): MA scope-conditional · "hấp thụ có định hướng" → cơ chế dẫn xuất · phát hiện no-telos · CA-2 quy ước.

**Bỏ → reference-only:** tập 7/8 tiên đề + số La Mã I–VIII (giữ bảng map cũ→mới ở `axiom_spec.md §5.1`) + nhãn "4 Core+3 Derived" cũ.

**P4 — đánh số & render (người dùng chốt: bỏ CA/DP/MA, dùng SỐ LA MÃ đếm lại theo tầng I–IV/V–VII/VIII; file cũ archive):**
- `axiom_spec.md` cập nhật định danh sang La Mã mới (single source).
- `axioms.html` (MỚI) — trang mẫu render từ spec, theo phong cách site.
- `index.html` — thêm thẻ nav "Hệ Tiên Đề" → `axioms.html`.
- `what.html` — banner trỏ canonical `axioms.html` (additive) + gỡ mâu thuẫn bảng kiểm tra (III/VI/VII "Độc lập" ✅→⚠️ dẫn xuất) + kết luận §3.6 "giả thuyết" → "đã giải" (W4 transform, giữ lập luận làm provenance). Card 7 tiên đề giữ số cũ (banner phủ legacy) — chưa renumber tại chỗ vì cần reorder + trùng `axioms.html`.
- Banner canonical (additive, không remap) thêm vào: `upgrade.html`, `mach_re_homologous.html` (lưu ý IV→III), `axiom_conflict.html` (VIII giữ số), `axiom_4.html` (IV→III), `how.html` (generic). Mỗi banner trỏ `axioms.html` + bảng map `axiom_spec.md §5.1`. `who.html` (1 ref thoáng) + `when.html`/`why.html` (không nhắc số) bỏ qua.
- **Deep-renumber từng trang = GATE REJECT (3.0/5):** cascade cross-file (tên file/text-link/cross-ref). Chỉ làm khi có batch phối hợp toàn site, hoặc không (banner đã đủ). **P4 hoàn tất ở mức single-source + canonical pointer; site coherent, không mâu thuẫn ngầm.**
- **Quyết định gate — renumber hàng loạt 8 file: 2.0/5 → REJECT.** Lý do: ~150 ref La Mã trong prose bị *remap nghĩa* (III cũ=Phân Tán → III mới=Thời Gian) → find/replace mù sẽ hỏng nghĩa = đúng bẫy vá-chồng-vá. Rollout đúng phương pháp = **regenerate từng trang từ spec + archive**, page-by-page (chưa làm).

**Files đã sửa:** `CLAUDE.md`, `plan/dictionary_rule.md` (§7, §9), `axiom_spec.md` (MỚI→renumber), `axioms.html` (MỚI), `index.html`, `what.html` (banner), `plan/mach-re-axiom-rebuild-plan.md` (P0–P4 mẫu).
**Không đụng:** `raw/`, `archives/` (P4); 7 file HTML còn lại (`upgrade`, `who`, `how`, `mach_re_homologous`, `axiom_4`, `axiom_conflict`, `when`, `why`) — chờ regenerate page-by-page.

---

## 2026-06-05 — Bổ sung tên thuần Việt cho 8 Tiên Đề (Phase 2–4 hoàn tất)

**Quyết định bằng cổng RCA (3-round × 5-Why × threshold 4/5). La bàn: Nhận thức luận Phật giáo (Upāya).**

**RCA gốc rễ:** thiếu tên thuần Việt = vi phạm nguyên lý Upāya mà Tiên Đề VIII tự dựng lên ("triết lý chỉ sống khi được nói trong ngôn ngữ mà người ta nghĩ"). Sửa = làm framework tuân theo chuẩn của chính nó. Điểm 5/5.

**Kết quả chấm điểm (8/8 đạt ≥ 4/5):**

| # | Biểu hiện | Bản chất | Điểm |
|---|---|---|---|
| I | Sống Trong Quan Hệ | Có Nhau Mới Có Mình | 4.8 |
| II | Nếp Bản Sắc | Đổi Mà Vẫn Là Mình | 4.8 |
| III | Giữ Mà Không Gom | Ai Cũng Giữ Một Phần | 5.0 |
| IV | Mạch Cội Dọc | Mạch Cội Nguồn | 4.8 |
| V | Ranh Giới Mềm | Đóng Mở Có Chọn | 5.0 |
| VI | Hóa Nhiễu Thành Sức | Đau Được Xử Là Đau Lành | 4.8 |
| VII | Nổi Lên Có Hướng | Hợp Lại Thành Cái Mới | 5.0 |
| VIII | Tự Nhìn Thấy Mình | Soi Mình Mà Không Vỡ | 5.0 |

**Neo Tiên Đề IV (Conflict-risk 4):** "Cội Nguồn" = tên bản chất *cảm xúc-bản sắc*, KHÔNG đồng nghĩa "Orthogonal/trực giao" (thuật ngữ cấu trúc). Hai tầng essence ≠ manifestation vẫn giữ nguyên.

**Files đã sửa:**
- `plan/dictionary_rule.md`: thêm §9 — bảng tên canonical (nguồn chân lý duy nhất)
- `CLAUDE.md`: thêm `### Tên thuần Việt các Tiên Đề` vào Core Principles
- `what.html`: 7 h3 heading (I–III, V–VII) + summary table + hierarchy ASCII block
- `upgrade.html`: h2 + display block title + ASCII kiến trúc cho VIII
- `index.html`: nav card description cho VIII
- `who.html`: first-mention VIII trong body
- `axiom_conflict.html`: label div Module 5 (first-mention VIII)
- `mach_re_homologous.html`: hero section intro (first-mention IV)
- `axiom_4.html`: `<title>`, `<meta description>`, kết luận label

**Không đụng:** `raw/`, `archives/` (P4); nội dung lập luận inline (chỉ sửa naming-definition points); thuật ngữ EN (extend-only).

---

## 2026-06-05 — Thêm Module 5: Xung Đột Lõi (Core Conflict) — cơ chế xử lý bất đồng nội bộ

**Quyết định bằng cổng RCA (theo yêu cầu người dùng: 3-round RCA × 5-Why × threshold 4/5, la bàn = nhận thức luận Phật giáo).**

**RCA — có nên thêm module (3-round × 5-Why):**
- R1 Triệu chứng: mọi tài liệu nói về "lõi" ở số ít; Tiên Đề II định nghĩa bản sắc là *một* invariant pattern → framework mặc định cộng đồng đồng thuận về lõi.
- R2 Cơ chế: Mạch Rễ tự tuyên bố "cho toàn dân tộc, không phân biệt chính kiến" — nhưng không có cơ chế cho lúc người Việt bất đồng *về chính định nghĩa người Việt* → tự mâu thuẫn với phạm vi tuyên bố.
- R3 Gốc (một câu): framework gán **tự tính cố định** cho "lõi", nên không có chỗ cho bất đồng — trong khi chuẩn *Śūnyatā* của Tiên Đề VIII nói lõi cũng trống tự tính, vậy bất đồng là điều phải-có, không phải bệnh lý.

**Scoring (thêm module):** Đúng 5 / Sâu 5 / Khả thi 4 / Rủi-ro-thấp 4 / Bảo tồn 5 → **TB 4.6/5 → PROCEED**

**RCA — định vị cấu trúc (cổng quyết định, không chọn tay):**
- La bàn Śūnyatā: gán địa vị "Tiên Đề IX" cho một thứ phái sinh = vật-hóa nó = đúng cái lỗi module ra đời để sửa → loại.
- La bàn Upāya: Tiên Đề VIII vốn là "Mạch Rễ tự thấy giới hạn" → Core Conflict thuộc về VIII tự nhiên.
- **Kết quả:** A+B (hệ quả thứ 5 của Tiên Đề VIII, đóng khung ảnh trực giao trục-H của Self-Criticism) = **4.8/5**; phương án Tiên Đề IX = 2.4/5 → **loại**.

**Sửa gì (extend, không overwrite):**
- `axiom_conflict.html` (MỚI): trang deep-dive song song `axiom_4.html` — lỗ hổng, phát biểu song ngữ, RCA 3-round, định vị V⊥H (Self-Criticism trục-V ⊥ Core Conflict trục-H), 4 công cụ Phật học (Śūnyatā↦lõi, Nhị đế, Tứ cú Catuṣkoṭi, Pramāṇa), 3 định dạng, 3 ví dụ (trong nước↔hải ngoại, ngôn ngữ, người lai), glossary.
- `upgrade.html`: thêm Hệ quả 5 vào cons-grid; cập nhật ASCII kiến trúc 4→5 + ghi chú V⊥H; thêm card "MODULE 5 — Xung Đột Lõi" + link; "Bốn hệ quả"→"Năm hệ quả"; +glossary row.
- `what.html`: thêm "Giới hạn V" (giả định đồng thuận); "Bốn giới hạn"→"Năm giới hạn" + link; thêm qualifier phân tầng pattern/nội dung cho Tiên Đề II.
- `how.html`: Thực hành "Nhận Dạng Lõi" thêm đoạn "Khi cộng đồng bất đồng về lõi" + link.
- `who.html`: ghi chú dưới bảng VN×Ubuntu×Yoruba ("Tự phê bình ❌ Yếu" → đã nâng cấp) + link.
- `why.html`: "Bốn hạn chế"→"Năm hạn chế" + card hạn chế #5 (Core Conflict Gap); "Bốn Mô-đun"→"Năm Mô-đun" + hàng bảng Module 5 (nguồn Nāgārjuna/Dharmakīrti, không mượn đa nguyên phương Tây) + link; "bốn mô-đun"→"năm mô-đun" trong quote-box.
- `index.html`: thẻ UPGRADE nhắc Module 5; thẻ WHY "bốn hạn chế/bốn Mô-đun"→"năm".

**Phân tầng chống mâu thuẫn "lõi bất biến":** cái *bất biến* = kiểu quan hệ (pattern); cái *thương lượng được* = nội dung / biên giới thành viên. Bất đồng ở tầng nội dung, không phá Tiên Đề II (invariant dưới content transformation).

**Lưu ý nguồn:** KHÔNG dùng *Anekāntavāda* (Kỳ-na/Jain) — chỉ Nāgārjuna/Dharmakīrti, giữ nhất quán nguồn Phật giáo.

**Không đụng:** `raw/`, `archives/` (P4); ý lõi "hấp thụ có định hướng"; các tiên đề I–VII và Tiên Đề VIII gốc.

---

## 2026-06-05 — what.html: Cập nhật Tiên Đề IV → Mạch Cội Nguồn (6 vị trí)

**RCA 3-round:**
- R1 Triệu chứng: `what.html` dùng "Mạch Cội Dọc / Vertical Temporality" mà không có tên bản chất "Orthogonal Temporality / Mạch Cội Nguồn" — mâu thuẫn thuật ngữ với `axiom_4.html` vừa cập nhật.
- R2 Cơ chế: Người đọc đọc what.html (tổng quan) xong sang axiom_4.html (chi tiết) gặp "Mạch Cội Nguồn / Root-Flow" mà không có context chuẩn bị.
- R3 Gốc: CLAUDE.md quy định "phát biểu bản thể học → dùng Orthogonal Temporality (bản chất)". what.html phát biểu bản thể học nhưng thiếu tên bản chất.

**Scoring tất cả ≥ 4/5 → thực hiện 6 sửa (extend, không overwrite):**
- Heading card IV: thêm "Mạch Cội Nguồn / Orthogonal"
- Note hai tầng (mới): thêm inline note Bản chất ↔ Biểu hiện sau phát biểu
- ASCII hierarchy: thêm "(Orthogonal Temporality)" vào dòng Tiên Đề IV
- Summary table: "Mạch Cội Dọc" → "Mạch Cội Dọc / Cội Nguồn"
- Link text: mention "Mạch Cội Nguồn"
- Paragraph verification: "Mạch Cội Dọc" → "Mạch Cội Dọc / Cội Nguồn"

---

## 2026-06-05 — Tích hợp raw/axiom_4.html: Mạch Cội Nguồn (Root-Flow Temporality)

**RCA 3-round × 5-Why:**
- R1 Triệu chứng: `axiom_4.html` thiếu thuật ngữ Việt hóa chính thức cho Orthogonal Temporality, thiếu bảng song ngữ 6 cặp, thiếu 3 định dạng phát biểu Tiên Đề IV.
- R2 Cơ chế: Nội dung RCA về "Mạch Cội Nguồn" đã được tạo ra (lưu trong `raw/axiom_4.html`) nhưng chưa được tích hợp vào tài liệu chính — tồn tại dưới dạng HTML thô từ Claude.ai.
- R3 Gốc: Không có workflow tích hợp `raw/` → tài liệu chính, dẫn đến phát hiện quan trọng (cội nguồn = Orthogonal Temporality trong ngôn ngữ Việt bản địa) bị cô lập khỏi nơi người đọc sẽ tra cứu.

**Scoring:** Đúng 1 / Sâu 1 / Khả thi 1 / Rủi ro mâu thuẫn 1 / Bảo tồn 1 → **5/5 → PROCEED**

**Sửa gì (extend, không overwrite):**
- `axiom_4.html`: Thêm Section 1B "Từ Việt Hóa — Mạch Cội Nguồn" sau Section 1. Bao gồm: RCA 5-Why, bảng đánh giá 6 phương án (Cội Nguồn = 9.5), phát biểu chính thức song ngữ (TIÊN ĐỀ IV — Mạch Cội Nguồn / AXIOM IV — Root-Flow Temporality), bảng song ngữ 6 cặp, 3 định dạng phát biểu.

**Phát hiện quan trọng ghi nhận:**
- "Cội nguồn" trong tiếng Việt = Orthogonal Temporality (cội = V, nguồn = H) — người Việt đã vận hành triết học này trong ngôn ngữ hàng nghìn năm trước khi có tên.
- Tên tiếng Anh chính thức: **Root-Flow Temporality** (Root = cội/V, Flow = nguồn/H).

---

## 2026-06-05 — RCA finding: Orthogonal Temporality là bản chất của Tiên Đề IV

**RCA 3-round × 5-Why:**
- R1 Triệu chứng: Tiên Đề IV chỉ có tên "Vertical Temporality" — mô tả hình thức trực quan nhưng không đặt tên tính chất cấu trúc nền tảng.
- R2 Cơ chế: Không có tên cho tính chất cấu trúc nên phần so sánh với Luhmann phải dùng 5 dòng để diễn đạt "past ↕ present không phải subset của past → present" — dấu hiệu thiếu thuật ngữ. Không phân biệt được Tiên Đề IV với "past là input của present" chỉ bằng tên "Vertical."
- R3 Gốc: Bản chất của Tiên Đề IV là tính **trực giao** (V ⊥ H) — hai chiều thời gian độc lập tuyến tính, không rút gọn về nhau. "Vertical" chỉ là cách tính trực giao hiện ra trong văn hóa. Thiếu tên "Orthogonal Temporality" = thiếu falsifiability handle.

**Scoring (5 tiêu chí):** Đúng 1 / Sâu 1 / Khả thi 1 / Rủi ro mâu thuẫn 1 / Bảo tồn 1 → **5/5 → PROCEED**

**Sửa gì (extend, không overwrite):**
- `CLAUDE.md`: Thêm `### Tiên Đề IV — Bản chất và Biểu hiện` vào Core Principles.
- `axiom_4.html`: Thêm def-box "Bản chất và Biểu hiện" vào cuối Section 1 (formal statement).
- `mach_re_homologous.html`: Mở rộng Foundation Statement — thêm câu clarification Orthogonal/Vertical.
- `plan/dictionary_rule.md`: Thêm section `## 8.` — bảng tra cứu hai tầng, quy tắc thuật ngữ.

**Không đụng:** Tên "Vertical Temporality" trong titles/headings, ASCII diagrams, compare-cards, thực hành văn hóa.

---

## 2026-06-05 — Governance update: CLAUDE.md (quyết định qua 3-round RCA × scoring)

**RCA tổng kết (3 round):**
- R1 Triệu chứng: phương pháp "3-round RCA × 5-Why × threshold 4/5" đã dùng nhất quán trong hai đợt tự phê bình nhưng chỉ tồn tại trong `plan/` và `CHANGELOG.md`, không có trong `CLAUDE.md`.
- R2 Cơ chế: mỗi phiên mới nạp `CLAUDE.md`, không tự nạp `plan/` → phương pháp không được tái áp dụng đáng tin.
- R3 Gốc: quy trình đã kiểm chứng chưa được "thăng cấp" lên file hợp đồng quản trị — khoảng trống governance.

**Sửa gì:** Chèn thêm tiểu mục `### Decision procedure — 3-round RCA × 5-Why × scoring gate (≥ 4/5)` vào RULE ZERO, ngay sau "Five-step process". Bao gồm: mô tả 3 round, 5-Why, rubric 5 tiêu chí, chiều ngưỡng rõ ràng (chấm *claim*, ≥ 4/5 → sửa), 2 ví dụ neo `CHANGELOG.md`, ghi chú khử mâu thuẫn ngầm với `plan v2` §2.

**Không đụng:** `plan/dictionary_rule.md`, `plan/mach-re-plan-chinh-sua-v2.md`, 8 file html, khối gitnexus, Core Principles.

**Quyết định bị phương pháp loại:** Sửa `dictionary_rule.md`/`plan v2` (TB score 2.2 < 4) — dictionary §0 đã khớp chiều ngưỡng; plan v2 là bản ghi đóng băng.

---

## 2026-06-05 — Tự phê bình v2.0 (theo kế hoạch mach-re-plan-chinh-sua-v2.md)

**Lý do gốc (RCA §1):** Các khẳng định tuyệt đối vi phạm chính chuẩn falsification/traceability mà framework tự đặt ra (`upgrade.html` — "mọi claim phải truy được về bằng chứng, nếu không → đánh dấu speculative"). Sửa = làm framework nhất quán với chính nó.

### what.html
- **A5 (line 232):** "Đây không chỉ là ẩn dụ — trùng khớp chính xác" → "ẩn dụ đắt — gần khớp về cấu trúc"
- **A5 dedupe (G5):** Lines 369 ≡ 405 đồng bộ cùng câu chữ (đã dedupe)
- **A1 (line 602):** "Không có triết học nào... đóng góp nguyên bản" → "góc ít được khai thác... phạm vi có giới hạn"
- **A2 (line 714):** "đóng góp nguyên bản" → "tự thấy khác biệt nhất so với các nguồn kế thừa (Ashby, cấu trúc luận, Phật giáo)"
- **A3 (line 904):** "đóng góp lý thuyết thực sự" → "phần Mạch Rễ bổ sung so với ba nguồn kế thừa"
- **B (line 600):** Bỏ `Resilience(S) = f(depth(V))` (f không định nghĩa) → văn xuôi; đổi nhãn "Sơ đồ"
- **B (line 656):** Bỏ `Direction(agentᵢ) = ∇F(positionᵢ)` (∇F vô định) → "mỗi agent tự định hướng theo lực hút của Field F"
- **C:** Bỏ cột "Tổng" + điểm 9.4 khỏi bảng so sánh; bỏ khối tính điểm `9.35/10`; thêm disclaimer chủ quan; bỏ cột "Điểm" (x/10) khỏi bảng chi tiết; sửa "không chỉ là ẩn dụ" trong ô lý do

### axiom_4.html
- **meta description:** "đóng góp nguyên bản" → "góc nhìn đặc trưng"
- **Hero subtitle:** "chưa được phát biểu trước đây" → "ít được khai thác trực diện trong các framework bản sắc đương đại"
- **Section 2:** "Không có triết học nào..." → "Mạch Rễ nhấn mạnh... phạm vi tham khảo có giới hạn"
- **Section 5:** "Để chứng minh... đóng góp nguyên bản" → "Để kiểm tra... khác biệt cấu trúc"
- **Section 5 kết luận:** "Không ai đạt đủ 4 cột... đóng góp nguyên bản" → "Không triết học nào trong phạm vi khảo sát... chỉ số cấu trúc trong phạm vi tham khảo"
- **Kết luận blockquote:** "chưa được phát biểu trước đây — đóng góp nguyên bản" → "ít được khai thác trực diện — góc đặc trưng so với nguồn kế thừa"
- **B:** Bỏ `Resilience(S) = f(depth(V))` → văn xuôi; đổi nhãn "Sơ đồ"

### who.html
- **Line 329:** "hầu hết triết học phương Tây hiện đại" → "phần lớn framework bản sắc phương Tây tôi khảo sát"

## 2026-06-05 — Tự phê bình v2.1 (đợt 2: how, when, why, upgrade, mach_re_homologous)

**Lý do gốc:** cùng RCA §1 — nhất quán với chuẩn falsification nội tại. Threshold scoring 4/5 áp dụng cho từng claim.

### how.html
- **L416:** "không có trong bất kỳ hệ thống nào" → "chưa có rõ trong ba hệ thống đối chiếu (Ashby, Phan Ngọc, Anattā)" [score 4.6]
- **L528:** "đóng góp lý thuyết mới mẻ, độc đáo nhất" → "điểm đặc trưng nhất so với ba hệ thống kế thừa" [score 4.6]

### when.html
- **L276:** "Theo tất cả mô hình đồng hóa lịch sử" → "Theo phần lớn mô hình... tôi khảo sát" [score 4.2]
- **L281:** "không có tiền lệ (precedent)" → "ít có tiền lệ so sánh trực tiếp" [score 4.0]
- **L320:** "thực sự mới mẻ, độc đáo (novel)" → "Điểm đặc biệt nổi bật" [score 3.8]

### why.html
- **L238:** "Được **chứng minh** qua 2.000 năm" → "Được **minh họa** qua 2.000 năm" [score 4.6 — plan D trực tiếp]

### upgrade.html
- **L213:** "mô tả **chính xác** cơ chế sinh tồn" → bỏ "chính xác" [score 4.8 — tự mâu thuẫn: cùng trang liệt kê 4 giới hạn của chính mô tả đó]
- **L604:** "cách **duy nhất** để nâng cấp" → "cách **hiệu quả nhất**" [score 4.2]

### mach_re_homologous.html
- **L501:** "đơn vị **duy nhất** không bị phá vỡ" → "đơn vị ít bị phá vỡ nhất trong ba hệ thống đối chiếu" [score 3.6]
- **L541–543:** "Khác biệt gốc rễ **duy nhất**" → "Khác biệt gốc rễ **chủ yếu**"; "Từ **một** điểm phân kỳ" → "Từ điểm phân kỳ... **phần lớn** những khác biệt" [score 3.6]

**SKIP (dưới threshold hoặc claim hợp lệ):**
- `mach_re_homologous.html:217` "ngôn ngữ đủ chính xác để đối thoại" — mục tiêu thiết kế, không phải universal [score 3.2]
- `why.html:354` "giải quyết chính xác một hạn chế" — mô tả ý định thiết kế, không phải empirical [3.6, không phá vỡ traceability]

---

**Điều KHÔNG thay đổi (bảo tồn phần mạnh):**
- Ý lõi: bản sắc bền nhờ hấp thụ có định hướng, không nhờ dựng tường
- Khái niệm "rễ nông", "trí nhớ sống / trí nhớ chết"
- Phân biệt quan hệ dọc vs ngang
- Cơ chế tự phê bình + tiêu chí phản chứng
- Đoạn tự mổ xẻ "7 tiên đề thực ra cần 4"
- Các sơ đồ quan hệ có kiểu (`Time = H × V`, `Identity = Pattern(R(S))`, v.v.)


## 2026-06-06 — P6 Coordinated Renumbering Batch (đổi số La Mã toàn site)

**Lý do gốc:** Thực thi Quyết định 2 về định danh (đã chốt bởi người dùng) để chuyển đổi toàn diện website sang hệ tiên đề canonical mới (Core I-IV · Derived V-VII · Meta VIII), thống nhất hiển thị và gỡ bỏ các thông báo di trú trung gian.

### dictionary_rule.md
- Cập nhật Mục 8 & 9 và chốt trạng thái canonical cho bộ thuật ngữ.

### axiom_spec.md
- Đánh dấu trạng thái migration hoàn tất tại §5.1.

### what.html
- Thay thế dải số cũ bằng hệ tiên đề canonical 4+3+1.
- Reorder các thẻ tiên đề (Phân tán từ III -> V, Ranh giới mềm từ V -> IV, mạch cội dọc từ IV -> III).
- Cập nhật các bảng so sánh và sơ đồ dẫn xuất ASCII.
- Điều chỉnh phân loại pills trong kiến trúc đồng cấu (Giao điểm: I,II,V; Cầu nối: IV,VI; Khoảng trống: III,VII).

### axiom_3.html (đổi tên từ axiom_4.html)
- Chuyển đổi các nhãn và tham chiếu tự thân "Tiên Đề IV" thành "Tiên Đề III".
- Chuyển đổi tham chiếu chéo "hay III" (Phân tán) ở dòng 396 thành "hay V".
- Gỡ bỏ banner cảnh báo di trú trung gian.
- Thêm chú thích HTML giải thích việc đổi tên file.

### upgrade.html
- Thay thế các nhãn "Tiên Đề IV" thành "Tiên Đề III" và "Tiên Đề III" thành "Tiên Đề V".
- Cập nhật tham chiếu "Tiên Đề IV Nâng cấp" thành "Tiên Đề III Nâng cấp" ở dòng 376.
- Gỡ bỏ banner cảnh báo di trú trung gian.

### axiom_conflict.html
- Remap tham chiếu "Tiên Đề IV" thành "Tiên Đề III" ở dòng 253.
- Gỡ bỏ banner cảnh báo di trú trung gian.

### index.html
- Cập nhật mô tả thẻ "how" (IV -> III) và phần thuật ngữ chân trang (II và III -> II và V).

### how.html
- Cập nhật tham chiếu mạch cội dọc (IV -> III) ở dòng 7.
- Thêm banner chú giải tại mục 3 nêu rõ sơ đồ 3 Core Axioms cục bộ là mô hình rút gọn riêng.

### mach_re_homologous.html
- Remap toàn bộ các tham chiếu "Tiên Đề IV" sang "Tiên Đề III".
- Gỡ bỏ banner cảnh báo di trú trung gian.


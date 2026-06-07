# Changelog — Mạch Rễ

## 2026-06-07 — `papers/paper_003/paper_003_draft.md`: Thêm Bảng Giải Thích Thuật Ngữ Cấp Học Sinh (Glossary)

**Cổng RCA (claim, 5/5 → FIX).**

**Root cause:** Bài viết sử dụng nhiều thuật ngữ chuyên môn phức tạp (Bản thể học liên chủ thể, Thời gian cội nguồn, Bất biến cấu trúc, Ranh giới thấm hút...) nhưng chưa có định nghĩa đơn giản hóa, làm hạn chế khả năng tiếp cận đối với đối tượng độc giả phổ thông (học sinh trung học phổ thông - high school level) và dễ dẫn đến hiểu nhầm hoặc lạm dụng thuật ngữ.

**Sửa:**
1. Thêm mục `## Bảng giải thích thuật ngữ (Glossary)` vào cuối bài viết, trước phần tài liệu tham khảo.
2. Giải thích 9 khái niệm then chốt bằng ngôn ngữ phổ thông giản dị kết hợp với các ẩn dụ trực quan (ví dụ: viên bi, ngôi nhà, sợi chỉ) và các ví dụ điện ảnh Việt Nam quen thuộc (*Bố Già*, *Nhà Bà Nữ*, *Mai*, *Móng Vuốt*).
3. Cập nhật đồng bộ các khái niệm ở phần kết luận khớp với từ điển thuật ngữ mới.

**Bảo tồn:** Giữ nguyên các lập luận học thuật và bố cục nguyên bản của bài viết.

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
| IV | Thời Gian Dọc | Thời Gian Cội Nguồn | 4.8 |
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

## 2026-06-05 — what.html: Cập nhật Tiên Đề IV → Thời Gian Cội Nguồn (6 vị trí)

**RCA 3-round:**
- R1 Triệu chứng: `what.html` dùng "Thời Gian Dọc / Vertical Temporality" mà không có tên bản chất "Orthogonal Temporality / Thời Gian Cội Nguồn" — mâu thuẫn thuật ngữ với `axiom_4.html` vừa cập nhật.
- R2 Cơ chế: Người đọc đọc what.html (tổng quan) xong sang axiom_4.html (chi tiết) gặp "Thời Gian Cội Nguồn / Root-Flow" mà không có context chuẩn bị.
- R3 Gốc: CLAUDE.md quy định "phát biểu bản thể học → dùng Orthogonal Temporality (bản chất)". what.html phát biểu bản thể học nhưng thiếu tên bản chất.

**Scoring tất cả ≥ 4/5 → thực hiện 6 sửa (extend, không overwrite):**
- Heading card IV: thêm "Thời Gian Cội Nguồn / Orthogonal"
- Note hai tầng (mới): thêm inline note Bản chất ↔ Biểu hiện sau phát biểu
- ASCII hierarchy: thêm "(Orthogonal Temporality)" vào dòng Tiên Đề IV
- Summary table: "Thời Gian Dọc" → "Thời Gian Dọc / Cội Nguồn"
- Link text: mention "Thời Gian Cội Nguồn"
- Paragraph verification: "Thời Gian Dọc" → "Thời Gian Dọc / Cội Nguồn"

---

## 2026-06-05 — Tích hợp raw/axiom_4.html: Thời Gian Cội Nguồn (Root-Flow Temporality)

**RCA 3-round × 5-Why:**
- R1 Triệu chứng: `axiom_4.html` thiếu thuật ngữ Việt hóa chính thức cho Orthogonal Temporality, thiếu bảng song ngữ 6 cặp, thiếu 3 định dạng phát biểu Tiên Đề IV.
- R2 Cơ chế: Nội dung RCA về "Thời Gian Cội Nguồn" đã được tạo ra (lưu trong `raw/axiom_4.html`) nhưng chưa được tích hợp vào tài liệu chính — tồn tại dưới dạng HTML thô từ Claude.ai.
- R3 Gốc: Không có workflow tích hợp `raw/` → tài liệu chính, dẫn đến phát hiện quan trọng (cội nguồn = Orthogonal Temporality trong ngôn ngữ Việt bản địa) bị cô lập khỏi nơi người đọc sẽ tra cứu.

**Scoring:** Đúng 1 / Sâu 1 / Khả thi 1 / Rủi ro mâu thuẫn 1 / Bảo tồn 1 → **5/5 → PROCEED**

**Sửa gì (extend, không overwrite):**
- `axiom_4.html`: Thêm Section 1B "Từ Việt Hóa — Thời Gian Cội Nguồn" sau Section 1. Bao gồm: RCA 5-Why, bảng đánh giá 6 phương án (Cội Nguồn = 9.5), phát biểu chính thức song ngữ (TIÊN ĐỀ IV — Thời Gian Cội Nguồn / AXIOM IV — Root-Flow Temporality), bảng song ngữ 6 cặp, 3 định dạng phát biểu.

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
- Reorder các thẻ tiên đề (Phân tán từ III -> V, Ranh giới mềm từ V -> IV, Thời gian dọc từ IV -> III).
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
- Cập nhật tham chiếu thời gian dọc (IV -> III) ở dòng 7.
- Thêm banner chú giải tại mục 3 nêu rõ sơ đồ 3 Core Axioms cục bộ là mô hình rút gọn riêng.

### mach_re_homologous.html
- Remap toàn bộ các tham chiếu "Tiên Đề IV" sang "Tiên Đề III".
- Gỡ bỏ banner cảnh báo di trú trung gian.

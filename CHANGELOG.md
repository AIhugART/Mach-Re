# Changelog — Mạch Rễ

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

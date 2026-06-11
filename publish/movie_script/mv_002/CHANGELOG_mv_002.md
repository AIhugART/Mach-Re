# CHANGELOG — mv_002 (Ba Vòng Vo)

> **Phạm vi:** Mọi thay đổi cho file trong `publish/movie_script/mv_002/` **phải và chỉ được** ghi vào file này.
> **Quy tắc:** Theo rule "CHANGELOG phân tầng" trong `CLAUDE.md §Document contract rules` (RCA 2026-06-11, score 4.8/5). Naming: `CHANGELOG_<tên-folder>.md`; vị trí: trong chính folder đó; routing: tầng gần nhất.
> **Liên kết:** Lịch sử toàn dự án (axiom, HTML, audit, infrastructure) → [`CHANGELOG.md`](../../../CHANGELOG.md) tại root.

---

## 2026-06-11 — Bổ sung mục *Silence* vào Scene Construction blocks (Cảnh 1 & Cảnh 2) · RCA 4.6/5

**File:** `Ba_Vong_Vo.md`

### Phát hiện (3-round RCA)

- **Round 1 — Symptom:** Câu hỏi V-axis bắt buộc của Phase 3 (Construction Protocol v3) —
  *"Where does the scene's silence live — what cannot be said and therefore must be held in image?"* —
  không được trả lời trong khối "Scene Construction Questions" của Cảnh 1 và Cảnh 2.
  Chỉ Cảnh 3 có mục *Silence* tường minh.
- **Round 2 — Mechanism:** Silence là phần tử dễ bị mất nhất khi tài liệu được revise về sau —
  bản năng của người sửa là lấp khoảng lặng bằng nhạc hoặc thoại giải thích ("Explained Silence",
  failure mode 5.4 của framework). Không có mục đánh dấu trong construction block nghĩa là
  không có gì bảo vệ khoảng lặng đó ở tầng tài liệu; một framework tự nhận tuân thủ protocol
  bị tổn thương nhiều hơn khi chính artifact của nó bỏ sót câu hỏi của protocol.
- **Round 3 — Root:** Khối construction của từng cảnh được sinh từ *field-set của Template A/B/C*
  thay vì từ *bộ câu hỏi chuẩn của Phase 3*. Template B có field "THE SILENCE" riêng (nên Cảnh 3 có),
  Template A và C không có field này (nên Cảnh 1, 2 bị rơi). Đây là vi phạm chuẩn tự thân —
  Axiom VIII (Tự Nhìn Thấy Mình): artifact phải tuân thủ protocol mà nó tuyên bố áp dụng.

### 5-Why (câu root một dòng)

Khối construction được dựng từ template field-set thay vì từ Phase 3 question protocol,
nên câu hỏi nào Phase 3 có mà template không có thì bị rơi.

### Scoring gate (ngưỡng ≥ 4/5)

| Tiêu chí | Điểm | Ghi chú |
|---|---|---|
| Correct | 4 | Thiếu sót thật trong block đã publish; nhưng silence đã được *thực thi* trong văn bản cảnh |
| Deep | 4 | Fix chạm root (hoàn chỉnh bộ câu hỏi Phase 3), không phải sửa tone |
| Feasible | 5 | Hai entry tài liệu, không chạm prose kịch bản |
| Conflict-risk | 5 | Không tạo mâu thuẫn với checklist hay frontmatter |
| Preservation | 5 | Toàn bộ cấu trúc và sức mạnh kịch bản giữ nguyên |
| **Trung bình** | **4.6/5** | **≥ 4 → fix** |

### La bàn Buddhist epistemology (compass cho cách fix)

Tri thức về khoảng lặng thuộc tầng "direct perception" (vô phân biệt — nonconceptual);
chuyển nó thành mệnh đề giải nghĩa là đánh mất bản chất của nó. Ràng buộc rút ra cho fix:
mục *Silence* chỉ được **định vị** im lặng (ngón tay chỉ trăng — trả lời "im lặng nằm ở đâu"
và "điều gì không nói được"), **không được giải nghĩa** im lặng ("im lặng có nghĩa là gì").
Ràng buộc này trùng khớp với quy tắc nội tại của framework v3: *"explanation converts
V-axis content into H-axis content."* Hai entry được viết và kiểm theo đúng ràng buộc đó.

### Thay đổi

1. **Cảnh 1 (Template A), khối V-axis** — thêm mục *Silence*: định vị im lặng ở việc bà
   không trả lời câu "Bao nhiêu vòng ạ?" (câu hỏi trả lại bằng câu hỏi, rồi bằng động tác);
   điều không nói được giữ trong hình ảnh "Camera giữ ở đôi tay. Không zoom. Không nhạc."
2. **Cảnh 2 (Template C), khối V-axis** — thêm mục *Silence*: định vị im lặng ở nhịp
   "Im lặng." trước lời thú nhận của mẹ và ở điều không ai gọi tên sau đó; điều không
   nói được giữ trong bố cục ba người — ba khoảng không — không chạm nhau.

### Verify (root đã bị loại, không chỉ symptom)

- Cả 3 cảnh giờ trả lời đủ bộ câu hỏi V-axis của Phase 3 (V-anchor, Silence, Color/Light) —
  block không còn phụ thuộc field-set của template để quyết định câu hỏi nào được trả lời.
- Prose kịch bản không đổi một ký tự; checklist 10 mục và Axiom VIII check giữ nguyên hiệu lực.
- Hai entry mới qua kiểm "định vị, không giải nghĩa": không câu nào phát biểu *nghĩa* của im lặng.

### Giữ nguyên (dưới ngưỡng, kèm điểm)

- **Mục "suspense" thiếu ở Cảnh 2–3 — 3.8/5, keep.** Template C không có slot suspense;
  Template B ghi "if applicable". Độ vênh nằm ở framework v3 (Phase 3 generic vs template
  field-set), không nằm ở kịch bản; ép thêm suspense vào cảnh synthesis có rủi ro méo cấu trúc.
- **Ba câu hỏi invariant Phase 1 (Q1, Q3) không ghi lại — ~3/5, keep.** Framework chỉ yêu cầu
  output là một câu invariant; checklist v3 chỉ yêu cầu "stated in one sentence" — cả hai thỏa.

---

*Tài liệu này không có trích dẫn nghiên cứu từ bên ngoài.*

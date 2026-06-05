# Kế hoạch chỉnh sửa — Mạch Rễ (v2 · sau review RCA)

> **Bản này thay thế tinh thần của** `mach-re-plan-chinh-sua.md` (v1) sau khi review bằng **3-round RCA × 5-Why × scoring threshold 4/5**.
> Bản v1 được giữ nguyên làm tham chiếu lịch sử. Mọi mục v1 vẫn đúng về *hướng*; v2 sửa lại *lý do gốc*, *phạm vi*, *thứ tự thực thi* và bịt các lỗ hổng khiến v1 có thể tạo mâu thuẫn mới.

---

## 0. Tóm tắt quyết định (TL;DR)

| Mục v1 | Verdict RCA | Lý do một dòng |
|--------|-------------|----------------|
| A. Hạ giọng khẳng định tuyệt đối | **MODIFY** (3.6/5 → 4.6 sau sửa) | Đúng, nhưng thiếu quét **đa trang** + lý do gốc sai tầng |
| B. Bỏ công thức toán | **MODIFY MẠNH** (2.8/5) | "Bỏ" quá thô — công thức nằm trong *thân* 7 tiên đề; phải **phân tầng**, không xóa sạch |
| C. Bỏ bảng tự chấm điểm | **KEEP** (4.4/5) | Đúng và khả thi; giữ lập luận định tính, bỏ điểm |
| D. Giảm chất tuyên ngôn | **KEEP** (4.0/5) | Đúng; chỉ cần neo vào chuẩn truy xuất nguồn |
| **(mới) G1–G7** | **ADD** | Các lỗ hổng v1 bỏ sót: đa trang, lý do gốc, trình tự, song ngữ, dedupe |

**Quyết định tổng:** Plan v1 **được chấp nhận có điều kiện**. Không thực thi v1 nguyên trạng — thực thi theo v2 vì v1 thiếu cơ chế chống mâu thuẫn (xóa trên 1 trang, để sót bản sao trên 5 trang → tệ hơn không sửa).

---

## 1. RCA — 5-Why trên vấn đề trung tâm

**Triệu chứng:** Tài liệu dùng "không có triết học nào / hoàn hảo / chính xác / duy nhất / 9.4/10".

1. *Tại sao cần sửa?* → Vì khẳng định tuyệt đối chỉ cần một phản ví dụ là sập (Heidegger, Bergson, Nho giáo dòng tộc…).
2. *Tại sao một phản ví dụ làm sập cả ý?* → Vì ở văn phong học thuật, một phổ quát (universal) sai làm người đọc suy rộng lỗi ra toàn framework.
3. *Tại sao người đọc suy rộng?* → Vì framework **tự dựng chuẩn nghiêm** (tiên đề, công thức, RCA, falsification) → mời gọi soi xét nghiêm → một phổ quát ẩu đọc như tác giả **không đạt chuẩn của chính mình**.
4. *Tại sao framework đặt chuẩn đó?* → Vì nó **tự tuyên bố** chuẩn truy xuất nguồn: `upgrade.html:519` — "mọi claim phải truy được về bằng chứng lịch sử 4.000 năm, nếu không → đánh dấu *speculative*".
5. **GỐC:** Các khẳng định tuyệt đối **vi phạm chuẩn nhận thức luận nội tại của chính Mạch Rễ**. Lỗi **không phải "giọng văn"** mà là **mâu thuẫn nội bộ** giữa *phương pháp tuyên bố* (khả phản chứng, truy nguồn, tự phê bình) và *thực hành tu từ* (phổ quát bất khả chứng, tự chấm điểm mình).

> **Đây là cải tiến quan trọng nhất so với v1.** Lý do của v1 ("càng khiêm tốn càng tin") là *thuyết phục/tu từ*. Gốc RCA là *nhất quán logic*. Khác biệt thực dụng: gốc RCA vừa cho biết **phải sửa gì**, vừa cho **điều kiện dừng khách quan** (mỗi claim hoặc truy được nguồn, hoặc bị đánh dấu *speculative*) — không phụ thuộc khẩu vị "khiêm tốn".

### 3-round RCA (3 tầng đào)
- **Round 1 — Triệu chứng:** từ ngữ tuyệt đối + điểm số + ký hiệu toán làm bề mặt thiếu tin cậy. *(v1 dừng ở đây.)*
- **Round 2 — Cơ chế:** framework tự mời soi xét nghiêm → bề mặt ẩu phản tác dụng mạnh hơn ở văn bản "ra vẻ chặt".
- **Round 3 — Gốc:** vi phạm chuẩn falsification/traceability **do chính framework đặt ra** (`upgrade.html:519`, `how.html:519`). → Sửa = **làm framework tuân thủ chính nó**, đồng thời biến việc sửa thành **bằng chứng sống** cho cơ chế tự phê bình (vốn là điểm mạnh nhất cần giữ).

---

## 2. Scoring (threshold 4/5) — giữ/sửa/bỏ từng mục

Thang 5 điểm/tiêu chí. Trung bình **≥ 4/5 → giữ nguyên**; **< 4 → sửa**. Tiêu chí: **Đúng** (nhận đúng lỗi thật) · **Sâu** (chạm gốc) · **Khả thi** · **Rủi-ro-mâu-thuẫn** (điểm cao = ít tạo mâu thuẫn mới) · **Bảo tồn** (giữ điểm mạnh).

| Mục | Đúng | Sâu | Khả thi | Rủi ro MT | Bảo tồn | TB | Verdict |
|-----|:--:|:--:|:--:|:--:|:--:|:--:|:--|
| **A** Hạ giọng tuyệt đối | 5 | 3 | 3 | 2 | 5 | **3.6** | MODIFY → +G1,G2,G5,G7 ⇒ 4.6 |
| **B** Bỏ công thức | 4 | 3 | 2 | 2 | 3 | **2.8** | MODIFY MẠNH → phân tầng |
| **C** Bỏ bảng điểm | 5 | 4 | 5 | 4 | 4 | **4.4** | KEEP |
| **D** Giảm tuyên ngôn | 4 | 4 | 4 | 4 | 4 | **4.0** | KEEP |

---

## 3. Mục A (đã sửa) — Hạ giọng + truy nguồn, quét ĐA TRANG

Nguyên tắc giữ nguyên: tránh **"không ai / tất cả / duy nhất / chính xác / hoàn hảo"** → **"ít thấy / phần lớn tôi khảo sát / một trong những / gần khớp"**.
**Bổ sung v2:** mỗi khẳng định mạnh phải **(a)** nêu phạm vi đã đối chiếu *hoặc* **(b)** tự gắn nhãn *speculative* — đúng theo `upgrade.html:519`.

| # | Vị trí (đã xác minh) | Hiện tại | Sửa |
|---|---|---|---|
| A1 | `what.html:602` thẻ Tiên Đề IV **và** `what.html:714` ghi chú bảng | "Không có triết học nào… / đóng góp nguyên bản" | "…góc **ít được khai thác trực diện** trong các framework bản sắc tôi khảo sát (liệt kê phạm vi)." Sửa **cả hai chỗ** cùng câu chữ. |
| A2 | `what.html:714` | "…đóng góp nguyên bản vào triết học" | "…hai điểm Mạch Rễ **tự thấy khác biệt nhất** so với các nguồn nó kế thừa (Ashby, cấu trúc luận, Phật giáo)." |
| A3 | `what.html:904` (Isomorphism) | "A5 và A7 là đóng góp lý thuyết thực sự" | "…phần Mạch Rễ **bổ sung mà ba hệ thống kia chưa nói rõ**." |
| A4 | Hộp "Đóng góp độc nhất" (bản đồ triết học) | "hầu hết / tất cả các khung nền" | Bỏ "hầu hết/tất cả" → "**phần lớn framework tôi khảo sát**" + nêu rõ phạm vi (Ubuntu, Wabi-sabi, Tikkun Olam, Ahimsa, Ikigai). |
| A5 | `what.html:232`, **369 và 405** (câu lặp 2 lần) | "Không chỉ là ẩn dụ — cơ chế sinh học trùng khớp **chính xác/hoàn hảo**" | "Hình ảnh mạch dẫn trong rễ là một **ẩn dụ đắt — gần khớp về cấu trúc**, dù không cùng cơ chế vật lý." Dedupe 369/405 (xem G5). |
| **A6 (mới)** | `axiom_4.html`, `how.html`, `mach_re_homologous.html`, `upgrade.html` | Bản sao của A1–A5 | **Bắt buộc** sửa đồng bộ — xem **G1**. |

---

## 4. Mục B (sửa mạnh) — PHÂN TẦNG công thức, không xóa sạch

**Phát hiện then chốt v1 bỏ sót:** các ô ASCII **nằm trong thân phát biểu chính thức của 7 tiên đề** (`what.html:546–601`: `∀x: Being(x) ≡ …`, `Identity(S) = Pattern(R(S))`, `Time(S) = H × V`…) và lặp lại ở `how.html`. "Bỏ" thô = viết lại xương sống framework + làm hỏng mục tự mổ xẻ "7 tiên đề thực ra cần 4" (vốn tham chiếu chúng). → **Quy tắc quyết định 3 tầng:**

- **GIỮ (đổi nhãn "sơ đồ quan hệ"):** biểu thức là **quan hệ/ràng buộc có kiểu** giúp hình dung — `Time = H × V`, các *corollary* phân tán↔fragility (`what.html:580–586`). Gọi là *sơ đồ*, **không** gọi *công thức/formula*.
- **BỎ:** biểu thức **giả-định-lượng** ngụ ý tính toán không tồn tại — `Resilience(S) = f(depth(V))` (f không định nghĩa), `Direction(agentᵢ) = ∇F(positionᵢ)` (gradient của F vô định). Diễn đạt lại bằng câu: *"Sức bền tăng theo chiều sâu trục thời gian dọc."*
- **NHÃN:** tuyệt đối không trình bày bất kỳ ô nào là "công thức/formula"; tối đa **1–2 sơ đồ/tiên đề**.

**Tiêu chí một dòng:** giữ nếu là *quan hệ có kiểu*; cắt nếu là *phương trình/đạo hàm giả* với toán tử vô định.

---

## 5. Mục C (giữ) — Bỏ điểm, giữ lập luận định tính

- **(Khuyên dùng)** Giữ *lập luận định tính* (vì sao "Mạch Rễ" hợp hơn tên khác) nhưng **bỏ điểm số**; trình bày dạng ưu/nhược.
- Áp dụng: bảng chọn tên `what.html:414–419` (9/10, 10/10…) + dòng tổng **9.4** `what.html:344` + bảng "mỗi tiên đề có phải axiom thật".
- Nếu giữ điểm: **ghi rõ** "đánh giá chủ quan của tác giả, tiêu chí + trọng số do tác giả đặt, không phải đo lường khách quan".

---

## 6. Mục D (giữ) — Tách *minh họa* khỏi *bằng chứng*

- Cụm "Được sống 4.000 năm… đặt tên 2026": **cho phép ở hero/mở đầu** (`index.html:255`) như câu khơi gợi; **không lặp** trong thân học thuật.
- Case study (1.000 năm Bắc thuộc, 500kV, hòa giải Việt–Mỹ — `index.html:341–355`, `when.html`): gắn nguồn/dữ kiện; **phân biệt rõ "minh họa" vs "chứng minh"** — chính là vận dụng chuẩn `upgrade.html:519`.

---

## 7. Các mục MỚI (G1–G7) — bịt lỗ hổng v1

| # | Mức | Nội dung | Vì sao bắt buộc |
|---|---|---|---|
| **G1** | **CAO** | **Ma trận nhất quán đa trang.** Lập bảng: mỗi claim/công thức → liệt kê **mọi trang** chứa nó (`what.html, how.html, upgrade.html, axiom_4.html, mach_re_homologous.html, raw/*`) → sửa **theo lô cùng lúc**. | v1 chỉ nhắm what.html. Sửa 1 trang, sót bản sao 5 trang → **mâu thuẫn = tệ hơn không sửa**. |
| **G2** | **CAO** | **Đổi lý do gốc** của toàn plan: từ "khiêm tốn → tin" sang **"nhất quán với chính tiên đề falsification của Mạch Rễ"** (gốc RCA §1). | Cho điều kiện dừng khách quan + biến việc sửa thành *bằng chứng* cho cơ chế tự phê bình. |
| **G3** | TB | **Trình tự thực thi** giảm rework: ① chốt lý do (G2) → ② **kiểm kê** claim/công thức đa trang (G1) → ③ sửa lô tuyệt đối (A) → ④ phân tầng công thức (B) → ⑤ bỏ điểm (C) → ⑥ tone (D). **Kiểm kê trước khi sửa.** | v1 có ưu tiên nhưng không có thứ tự — dễ sửa đi sửa lại. |
| **G4** | TB | **Cổng nghiệm thu nhị phân/claim** thay checklist mơ hồ: *"Claim này truy được về bằng chứng? Không → đánh dấu speculative hoặc hạ giọng."* | Vận hành hóa D + chuẩn nội tại; đo được, không cãi khẩu vị. |
| **G5** | THẤP | **Dedupe câu lặp:** `what.html:369` ≡ `405`; claim "đóng góp nguyên bản" ở `602` & `714`. Gộp/đồng bộ khi sửa. | Tránh sửa một chỗ quên chỗ kia. |
| **G6** | THẤP | **Changelog tự phê bình:** ghi lại đã hạ giọng gì & vì sao, ngay trong repo. | Biến chỉnh sửa thành minh chứng framework **tự áp dụng phương pháp của mình** (điểm mạnh nhất). |
| **G7** | **TB→CAO** | **Đối xứng song ngữ VN/EN.** Commit gần đây là "line-by-line bilingual VN/EN pass". Mỗi câu hạ giọng phải sửa **cả VN lẫn EN** cùng lúc, nếu không hai bản phân kỳ. | Bề mặt sửa **nhân đôi**; v1 hoàn toàn im lặng về việc này. |

---

## 8. Trade-off (nêu rõ để chọn có ý thức)

| Đánh đổi | Rủi ro nếu làm thô | Cách v2 giải |
|---|---|---|
| Bỏ công thức ↔ mất vẻ "chặt chẽ" | Người đọc thích hình thức thấy framework nhạt đi | **Phân tầng** (giữ sơ đồ có kiểu, cắt phương trình giả) thay vì xóa sạch |
| Hạ giọng ↔ mất sức nhớ/khẩu khí | Văn mất "punch", khó lan truyền | **Manifesto chỉ ở hero/mở đầu**; thân phân tích giữ nghiêm. Giữ **1 câu mạnh/khái niệm** |
| Quét đa trang ↔ tốn công gấp nhiều lần | Vượt phạm vi "chỉ what.html" của v1 | Bắt buộc, vì bỏ qua tạo mâu thuẫn; **gom theo loại claim** để làm lô |
| Song ngữ ↔ gấp đôi bề mặt | EN/VN lệch nghĩa | Sửa **cặp** trong cùng một lần đụng file |

---

## 9. Độ phức tạp · Sổ rủi ro

**Độ phức tạp tổng: TRUNG BÌNH.** Không có logic code; thuần chỉnh sửa nội dung — **nhưng** trải trên **6+ file HTML**, có **câu trùng lặp** và **cặp song ngữ VN/EN**, nên mỗi sửa đổi nhân đôi và phải đồng bộ chéo.

| ID | Rủi ro | Khả năng | Giảm thiểu |
|---|---|---|---|
| R1 | Mâu thuẫn chéo trang | **Cao** (nếu bỏ G1) | Ma trận nhất quán G1 trước khi sửa |
| R2 | Lệch song ngữ VN/EN | **Cao** | Sửa cặp G7 |
| R3 | Cắt công thức quá tay làm mất "rigor" | TB | Phân tầng B (giữ sơ đồ có kiểu) |
| R4 | Mất giọng/khả năng nhớ | Thấp–TB | Manifesto chỉ ở mở đầu; giữ 1 câu mạnh/khái niệm |
| R5 | Phình phạm vi/thời gian | TB | Trình tự G3 + làm lô theo loại claim |

---

## 10. Checklist nghiệm thu (thay v1 — neo vào chuẩn falsification)

- [ ] **G1:** Đã lập ma trận claim/công thức × trang, và mọi bản sao được sửa đồng bộ?
- [ ] **G7:** Mỗi câu sửa đã áp dụng cho **cả VN lẫn EN**?
- [ ] **A:** Hết "không ai/tất cả/duy nhất/chính xác/hoàn hảo" → từ có giới hạn phạm vi?
- [ ] **A/D-G4:** Mỗi claim mạnh **truy được nguồn** *hoặc* đã gắn nhãn *speculative*?
- [ ] **A2:** Mỗi chỗ "nguyên bản/đóng góp" đã nêu kế thừa từ ai (Ashby, cấu trúc luận, Phật giáo)?
- [ ] **B:** Đã cắt phương trình giả (`f(depth(V))`, `∇F`)? Sơ đồ giữ lại đã đổi nhãn "sơ đồ", ≤2/tiên đề?
- [ ] **C:** Điểm số (9.4/10…) đã bỏ *hoặc* ghi rõ là đánh giá chủ quan?
- [ ] **D:** Mỗi case study đã phân biệt "minh họa" vs "bằng chứng"?
- [ ] **G5:** Câu lặp 369/405 và claim 602/714 đã dedupe?
- [ ] **G6:** Đã ghi changelog "đã hạ giọng gì & vì sao"?

---

## 11. Điểm GIỮ NGUYÊN (không đụng — phần mạnh nhất)

- Ý lõi: **bản sắc bền nhờ hấp thụ có định hướng, không nhờ dựng tường.**
- Khái niệm **"rễ nông"**, **"trí nhớ sống / trí nhớ chết"**.
- Phân biệt **quan hệ dọc** (tổ tiên–hậu thế) vs **ngang** (Ubuntu).
- **Cơ chế tự phê bình + tiêu chí phản chứng** (`upgrade.html:519`) — *chính là chuẩn để soi mọi sửa đổi ở trên*.
- Đoạn **tự mổ xẻ "7 tiên đề thực ra cần 4"** — trung thực trí tuệ, điểm cộng lớn.

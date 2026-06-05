# Từ điển Quy tắc Phát biểu — Mạch Rễ

> Chắt lọc từ hai đợt tự phê bình (xem `CHANGELOG.md`) và kế hoạch `mach-re-plan-chinh-sua-v2.md`.
> **Mục đích:** một bảng tra cứu để mọi câu khẳng định trong bộ tài liệu nhất quán với chuẩn nhận thức luận **nội tại** của chính Mạch Rễ (falsifiability + traceability, `upgrade.html`).
> **Quy tắc vàng (gốc RCA):** *Mỗi khẳng định mạnh hoặc (a) nêu rõ phạm vi đã đối chiếu, hoặc (b) tự gắn nhãn speculative. Một phổ quát không phạm vi = một mâu thuẫn nội bộ chờ sập.*

---

## 0. Cổng quyết định (áp dụng trước khi sửa BẤT KỲ câu nào)

Mỗi câu nghi vấn chấm trên 5 tiêu chí (mỗi tiêu chí 1 điểm). **Sửa nếu trung bình ≥ 4/5.**

| Tiêu chí | Hỏi |
|---|---|
| Đúng | Đây có thật là khẳng định quá mức / bất khả chứng không? |
| Sâu | Sửa có chạm gốc (nhất quán nội tại) hay chỉ đổi giọng? |
| Khả thi | Sửa được mà không phá cấu trúc/ý lõi? |
| Rủi ro mâu thuẫn | Sửa có tạo mâu thuẫn với trang khác? (→ phải quét đa trang) |
| Bảo tồn | Có giữ được sức mạnh/ý lõi sau khi sửa? |

**Dưới 4/5 → GIỮ NGUYÊN.** Ví dụ đã giữ: "ngôn ngữ đủ chính xác để đối thoại" (mục tiêu thiết kế, 3.2); "giải quyết chính xác một hạn chế" (mô tả ý định, 3.6).

---

## 1. Từ điển thay thế — Tuyệt đối → Có phạm vi

| ❌ Cấm (phổ quát không phạm vi) | ✅ Thay bằng | Ghi chú |
|---|---|---|
| không có triết học nào / không ai | góc ít được khai thác trực diện trong [phạm vi khảo sát] | luôn liệt kê phạm vi |
| đóng góp nguyên bản / original contribution | góc đặc trưng / tự thấy khác biệt nhất so với [nguồn kế thừa] | nêu nguồn: Ashby, cấu trúc luận, Phật giáo |
| đóng góp lý thuyết thực sự / mới mẻ, độc đáo nhất | phần bổ sung so với [N hệ thống đối chiếu] | |
| chưa được phát biểu trước đây | ít được khai thác trực diện trong [phạm vi] | |
| không có trong bất kỳ hệ thống nào | chưa có rõ trong [N hệ thống đối chiếu được nêu tên] | |
| tất cả / mọi mô hình | phần lớn ... tôi khảo sát | |
| hầu hết triết học phương Tây | phần lớn framework bản sắc phương Tây tôi khảo sát | |
| duy nhất | chủ yếu / hiệu quả nhất / ít ... nhất trong [phạm vi] | |
| không có tiền lệ | ít có tiền lệ so sánh trực tiếp | |
| chính xác (khi mô tả thực nghiệm) | (bỏ) — hoặc "gần khớp" | xem §4 |
| hoàn hảo / trùng khớp hoàn hảo | gần khớp về cấu trúc | |

---

## 2. Ẩn dụ ≠ Sự thật (quy tắc mạch dẫn–rễ)

| ❌ Cấm | ✅ Thay bằng |
|---|---|
| Đây không chỉ là ẩn dụ — đây là cơ chế sinh học trùng khớp chính xác | Hình ảnh ... là một **ẩn dụ đắt — gần khớp về cấu trúc**, dù không cùng cơ chế vật lý |
| Đây không phải ẩn dụ — đây là sự thật sinh học trùng khớp hoàn hảo | một ẩn dụ đắt, gần khớp về cấu trúc với triết lý, dù không cùng cơ chế vật lý |

**Nguyên tắc:** không tuyên bố một ẩn dụ là "cơ chế/sự thật". Gọi đúng tên: ẩn dụ mạnh, gần khớp *cấu trúc*.

---

## 3. Minh họa ≠ Bằng chứng (quy tắc case study)

| ❌ Cấm | ✅ Thay bằng |
|---|---|
| Được **chứng minh** qua 2.000 năm lịch sử | Được **minh họa** qua 2.000 năm lịch sử |
| [case study] chứng minh framework | [case study] minh họa / nhất quán với framework |

**Nguyên tắc:** lịch sử *minh họa* (illustrate), không *chứng minh* (prove). Dành "chứng minh" cho suy luận logic, không cho dữ kiện lịch sử đơn lẻ.

---

## 4. Công thức giả → Sơ đồ / Văn xuôi (quy tắc phân tầng)

**Tiêu chí một dòng:** GIỮ nếu là *quan hệ/ràng buộc có kiểu*; CẮT nếu là *phương trình/đạo hàm giả* với toán tử vô định.

| Loại | Xử lý | Ví dụ |
|---|---|---|
| Quan hệ có kiểu | GIỮ, đổi nhãn "**Sơ đồ**" (không gọi "công thức/formula") | `Time = H × V`; `Identity = Pattern(R(S))`; corollary phân tán↔fragility |
| Phương trình giả-định-lượng | CẮT → diễn đạt văn xuôi | `Resilience(S) = f(depth(V))` (f vô định) → "Sức bền tăng theo chiều sâu của V" |
| Đạo hàm/gradient vô định | CẮT → văn xuôi | `Direction(agentᵢ) = ∇F(positionᵢ)` → "mỗi agent tự định hướng theo lực hút của Field F" |

Tối đa **1–2 sơ đồ/tiên đề**. Không bao giờ trình bày ô ASCII dưới nhãn "công thức/formula".

---

## 5. Điểm số tự chấm → Lập luận định tính (quy tắc bảng điểm)

- **Bỏ** cột "Tổng" và mọi con số tổng hợp kiểu `9.4/10`, khối tính điểm `935 ÷ 100`.
- **Giữ** lập luận định tính (vì sao đáp ứng tiêu chí) + trọng số, **kèm disclaimer**:
  > *Tiêu chí, trọng số, và điểm số đều do tác giả tự đặt — đánh giá chủ quan, không phải đo lường khách quan.*
- Không dùng bảng điểm để "chứng minh" bằng số.

---

## 6. Quy tắc quy trình (bắt buộc khi sửa)

| # | Quy tắc | Vì sao |
|---|---|---|
| P1 | **Quét đa trang trước khi sửa.** Một claim thường lặp ở nhiều file (what, how, axiom_4, upgrade, who, mach_re_homologous). Sửa đồng bộ theo lô. | Sửa 1 trang, sót bản sao → mâu thuẫn = tệ hơn không sửa |
| P2 | **Đối xứng song ngữ VN/EN.** Mỗi câu sửa phải áp dụng cả hai ngôn ngữ nếu có cặp. | Tránh EN/VN phân kỳ |
| P3 | **Dedupe.** Câu lặp nguyên văn (vd what.html 369≡405) phải đồng bộ cùng lúc. | |
| P4 | **Không đụng `raw/`.** Đó là archive cuộc trò chuyện gốc, không phải tài liệu xuất bản. | |
| P5 | **Ghi CHANGELOG.** Mỗi đợt sửa ghi lại *sửa gì & vì sao* — bằng chứng framework tự áp dụng cơ chế tự phê bình. | |

---

## 8. Tiên Đề IV — Hai tầng khái niệm (bản chất vs biểu hiện)

> RCA finding 2026-06-05 — Điểm 5/5. Bắt buộc áp dụng trong mọi phát biểu và so sánh liên quan đến Tiên Đề IV.

| Tầng | Thuật ngữ | Dùng khi nào |
|---|---|---|
| **Bản chất** (Essence) | **Orthogonal Temporality** — Thời gian trực giao | Phát biểu nguyên lý bản thể học; phân biệt Tiên Đề IV với Halbwachs/Luhmann |
| **Biểu hiện** (Manifestation) | **Vertical Temporality** — Thời gian dọc | Mô tả thực hành văn hóa; sơ đồ trực quan; so sánh ba nền văn hóa |

**Quy tắc:** Hai thuật ngữ **không** thay thế nhau — chúng khác tầng (essence ≠ manifestation).
- ❌ Cấm: "Orthogonal Temporality tức là Vertical Temporality"
- ✅ Đúng: "Tiên Đề IV có bản chất là Orthogonal Temporality, biểu hiện trong đời sống qua cấu trúc Vertical Temporality"

**Gốc rễ của quy tắc:** Nếu chỉ dùng "Vertical Temporality," không thể phân biệt Tiên Đề IV với "past là input của present operations" (Luhmann) — vì cả hai đều có hướng "dọc" về quá khứ. Chỉ tính **trực giao** (V không rút gọn về H) mới là ranh giới falsifiable.

---

## 7. Điều KHÔNG đụng (bảo tồn — đừng "hạ giọng" nhầm)

- Ý lõi: **bản sắc bền nhờ hấp thụ có định hướng, không nhờ dựng tường.**
- "rễ nông", "trí nhớ sống / trí nhớ chết", phân biệt quan hệ dọc vs ngang.
- Cơ chế tự phê bình + tiêu chí phản chứng — *chính là chuẩn để soi mọi quy tắc trên.*
- Đoạn tự mổ xẻ "7 tiên đề thực ra cần 4".
- Câu manifesto ở **hero/mở đầu** (vd "Được sống... đặt tên 2026") — cho phép ở mở đầu, không lặp trong thân học thuật.
- Mô tả *ý định thiết kế* ("đủ chính xác để đối thoại", "giải quyết một hạn chế") — không phải empirical claim, không cần hạ giọng.

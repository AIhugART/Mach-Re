# Mạch Rễ — P5: Hòa Giải Nội Dung (Content Reconciliation)

> **Loại:** Plan tiếp nối, xác định bằng cổng RCA (3-round × 5-Why × ≥4/5).
> **Vị trí:** P5 — sau P4 (render + canonical pointer) của `plan/mach-re-axiom-rebuild-plan.md`.
> **Quyết định người dùng:** xác định + lưu plan kế tiếp (2026-06-06).
> **Một câu:** đưa CLAIM của tài liệu legacy về khớp `axiom_spec.md`; đổi số La Mã chỉ là subtask phụ.

---

## 0. TÓM TẮT (TL;DR)

| Ứng viên plan | TB RCA | Verdict |
|---|:--:|---|
| A. Đổi số La Mã toàn site | **2.8** | ❌ cosmetic + cascade cross-file |
| **B. Hòa giải nội dung legacy ↔ spec** | **4.6** | ✅ **PLAN NÀY** |
| C. QA/phản chứng độc lập spec | 4.4 | ✅ phase con / sau B |

**Gốc:** rebuild không chỉ đổi *số* — nó đổi *claim* (xem §1). Banner mới *trỏ tới* canonical nhưng tài liệu legacy chưa *hòa giải về* nó → người đọc trang legacy vẫn tiêu thụ claim đã bị spec bác = **mâu thuẫn nội dung thật**, nặng hơn lệch số.

---

## 1. RCA — VÌ SAO HÒA GIẢI NỘI DUNG, KHÔNG PHẢI ĐỔI SỐ

**Round 1 — Triệu chứng:** bước "hiển nhiên" kế tiếp trông như đổi nốt số La Mã trên trang legacy.

**Round 2 — Cơ chế:** `axiom_spec.md` (P2) đã *sửa claim*, không chỉ số:
- "hấp thụ có định hướng" hạ từ *đóng góp novel* → cơ chế dẫn xuất (chữ ký II×IV);
- thêm phát hiện *no-telos*;
- Tiên Đề II gắn lớp *Nhị đế* (invariant trống "svabhāva");
- VIII thành *scope-conditional có biện minh* (không bolt-on);
- prior-art III = Heidegger/Gadamer/Burke/Pratītyasamutpāda.
Trang legacy vẫn khẳng định claim CŨ — rõ nhất `axiom_4.html` §"Tại Sao Không Ai Phát Biểu Tiên Đề IV?".

**Round 3 — Gốc (một câu):** rebuild tạo nguồn chân lý mới với claim đã sửa, nhưng legacy mới chỉ được *trỏ tới* (banner), chưa *hòa giải về* — nên banner tạo *trấn an giả*. → Fix gốc = hòa giải claim, không phải cosmetic số.

**Chấm điểm plan B (hành động):** Đúng 5 · Sâu 5 · Khả thi 4 · Rủi-ro 4 · Bảo-tồn 5 → **4.6/5 → PROCEED**.

---

## 2. HÀNG ĐỢI ƯU TIÊN (theo mức độ mâu thuẫn)

> Mỗi claim: quét đa trang (P1) → chấm RCA ≥4/5 → sửa → CHANGELOG (P5). Bảng thay thế tuyệt đối→có-phạm-vi: `dictionary §1`.

### 🔴 #1 — Overclaim "Không Ai Phát Biểu Tiên Đề IV" (NẶNG NHẤT) — ✅ XONG 2026-06-06
> Đã sửa 4 chỗ trong `axiom_4.html` (RCA 4.6/5; CHANGELOG). Quét đa trang xác nhận overclaim chỉ ở file này (published). Còn lại #2–#6.
- **Vị trí:** `axiom_4.html` §RCA ([:712](../axiom_4.html#L712) tiêu đề "Tại Sao Không Ai Phát Biểu…", [:731](../axiom_4.html#L731) "chưa ai hệ thống hóa cho đến khi Mạch Rễ").
- **Mâu thuẫn:** (a) trái prior-art của chính spec (Heidegger/Gadamer/Burke); (b) vi phạm `dictionary §1` (cấm "không ai / chưa ai").
- **Sửa:** → "góc ít được khai thác trực diện trong [phạm vi khảo sát đã nêu tên]"; đổi tiêu đề §RCA sang "Vì sao góc này ít được khai thác trực diện?".
- **Quét đa trang:** kiểm `mach_re_homologous`, `what` (đã sửa thành "tự thấy khác biệt nhất" — OK), `upgrade`.

### 🟡 #2 — "Hấp thụ có định hướng" như đóng góp novel cấp tiên đề — ✅ XONG 2026-06-06
> Sửa `what.html:933` (RCA 4.4/5): "Đóng góp độc nhất/tất cả/hầu hết" → "Góc đặc trưng/phần lớn… tôi khảo sát" + chú "hệ quả II×IV, không phải tiên đề". P1: chỗ thật duy nhất; how.html:420 đã scoped sẵn. Còn lại #3–#6.
- **Mâu thuẫn:** spec hạ nó thành *cơ chế dẫn xuất* (chữ ký II×IV trong Mệnh Đề VI), không phải tiên đề/novel.
- **Sửa:** mọi nơi gọi nó "đóng góp nguyên bản/novel" → "cơ chế đặc trưng, là hệ quả của Bất Biến × Biên Giới Động".
- **Vị trí cần quét:** `what`, `axiom_4`, `upgrade`, `who`.

### 🟡 #3 — Tiên Đề II trình bày bất biến tuyệt đối (essentialism) — ✅ XONG 2026-06-06
> Thêm clause Nhị đế vào card II `what.html` (RCA 4.8/5). P1: `axiom_conflict`/`upgrade` đã có sẵn "trống tự tính". Còn lại #4–#6.
- **Mâu thuẫn:** thiếu lớp Nhị đế → II đọc thành essentialism → trái Tiên Đề I + hệ C.
- **Sửa:** thêm một mệnh đề ngắn "invariant bền ở mức *quy ước* (conventional), trống svabhāva" vào phát biểu II.
- **Vị trí:** `what.html` (card II), `axiom_conflict.html` (định nghĩa invariant).

### 🟢 #4 — VIII trình bày như "thêm meta-axiom" — ✅ XONG 2026-06-06
> `upgrade.html` §3: thêm đoạn biện minh scope-conditional (RCA 4.6/5). Còn lại #5 (tùy chọn), #6 (phụ).
- **Sửa:** ghi rõ *scope-conditional có biện minh* (cần ⇔ áp lực tiến hóa) thay vì bolt-on.
- **Vị trí:** `upgrade.html`, `axiom_conflict.html`.

### 🟢 #5 — Bổ sung phát hiện "no-telos" (tùy chọn) — ✅ XONG 2026-06-06
> `what.html` §Giới Hạn: thêm def-box no-telos (RCA 4.4/5). **P5 #1–#5 hoàn tất.** #6 → plan riêng `mach-re-P6-renumber-batch.md`.
- Thêm như một self-limit/ghi chú: hệ C (Anattā) chủ động chặn tiên đề mục đích luận.

### ⚪ #6 — Đổi số La Mã (subtask phụ)
- **Chỉ** gộp vào khi đã mở từng trang sửa claim, **và** chỉ nếu làm batch phối hợp toàn site (đổi tên file + text-link + nội dung). Nếu không → giữ banner. KHÔNG find/replace mù (gate 2.0, xem rebuild §8).

---

## 3. QUY TẮC QUY TRÌNH (`dictionary §6`)
P1 quét đa trang trước khi sửa · P2 đối xứng song ngữ VN/EN · P3 dedupe câu lặp · P4 không đụng `raw/`,`archives/` · P5 ghi CHANGELOG mỗi lô.

## 4. RISK REGISTER
| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Sửa claim 1 trang, sót bản sao trang khác | 🟡 | P1 quét đa trang theo lô claim |
| Hạ giọng nhầm vào ý lõi mạnh | 🟢 | `dictionary §7` carry-forward; chỉ sửa claim mâu thuẫn spec |
| Lẫn đổi-claim với đổi-số | 🟡 | Tách rõ: #1–#5 = claim; #6 = số (phụ, có điều kiện) |
| EN/VN phân kỳ | 🟢 | P2 song ngữ |

## 5. THỨ TỰ THỰC THI
`#1 (axiom_4 overclaim) → #2 (directed absorption) → #3 (Nhị đế II) → #4 (VIII scope) → #5 (no-telos, optional) → #6 (số, chỉ nếu batch phối hợp)` · ghi CHANGELOG sau mỗi mục.

## 6. LIÊN HỆ TÀI LIỆU
- Nguồn chân lý đối chiếu: `axiom_spec.md` (đặc biệt prior-art mỗi tiên đề + §4 "phân kỳ thật").
- Các overclaim này từng được nêu trong `plan/mach-re-axiom-revision-plan.md` (v1) — nay **cấp thiết hơn** vì spec mới đã chủ động bác chúng.
- Carry-forward / điều không hạ giọng nhầm: `plan/dictionary_rule.md §7`.

---

> **Metadata cho LLM:** P5 sau P4 · trọng tâm = claim reconciliation (không phải số) · cổng RCA ≥4/5/claim · đối chiếu `axiom_spec.md` · thứ tự #1→#6 · QA độc lập (ứng viên C) có thể chạy sau như P6.

# Mạch Rễ — P6: Batch Đổi Số La Mã Toàn Site (Coordinated Renumber)

> **Loại:** Plan riêng cho việc lớn (tách khỏi P5). Xác định bằng cổng RCA.
> **Vị trí:** P6 — sau P5 (content reconciliation đã xong #1–#5).
> **Mục tiêu:** mọi trang hiển thị **trực tiếp** số La Mã mới (Core I–IV · Derived V–VII · Meta VIII), gỡ banner trung gian.
> **Quyết định người dùng:** lập kế hoạch (2026-06-06).

---

## 0. CẢNH BÁO RCA TRƯỚC TIÊN (đọc kỹ trước khi quyết thực thi)

| Cách làm | Điểm RCA | Verdict |
|---|---|---|
| Piecemeal / find-replace mù | **2.0** | ❌ đã loại (rebuild §8) |
| **Coordinated batch (plan này)** | **~3.4** | ⚠️ **DƯỚI 4 — polish tùy chọn, KHÔNG bắt buộc** |

> **Trung thực:** ngay cả làm phối hợp, batch này vẫn **dưới ngưỡng 4/5** vì: giá trị là *cosmetic* (banner đã cho coherence), khối lượng lớn (~150 ref remap nghĩa), rủi-ro vốn có. **Chỉ thực thi nếu "hiển thị số mới trực tiếp" là yêu cầu cứng.** Nếu không → giữ banner (trạng thái hiện tại đã nhất quán).
> Plan này tồn tại để: *nếu* chọn làm, có phương pháp an toàn tránh bẫy 2.0.

---

## 1. BẢNG REMAP (nguồn: `axiom_spec.md §5.1`)

| Số cũ | Axiom | → Số mới | Tầng mới |
|---|---|---|---|
| I | Quan Hệ Bản Thể | **I** | Core |
| II | Bất Biến Cấu Trúc | **II** | Core |
| III | Phân Tán Bản Thể | **V** | Derived |
| IV | Mạch Cội Dọc | **III** | Core |
| V | Biên Giới Động | **IV** | Core |
| VI | Chuyển Hóa Nhiễu | **VI** | Derived |
| VII | Nổi Lên Có Hướng | **VII** | Derived |
| VIII | Tự Nhìn Thấy Mình | **VIII** | Meta |

**Điểm chết người:** số bị *hoán đổi nghĩa* — "Tiên Đề III" cũ (Phân Tán) → V; "Tiên Đề IV" cũ (Thời Gian) → III; "Tiên Đề V" cũ (Biên Giới) → IV. **Mỗi ref phải remap theo NỘI DUNG nó trỏ tới, không theo con số.** → cấm tuyệt đối find/replace `"Tiên Đề IV"→"Tiên Đề III"`.

---

## 2. GỐC RỄ RỦI RO (vì sao piecemeal = 2.0) & cách batch hóa giải

| Rủi ro (cascade) | Mitigation trong batch phối hợp |
|---|---|
| Số remap nghĩa → sót 1 ref = "III" hai nghĩa | **Inventory-first (P6a):** liệt kê + phân loại MỌI ref trước khi sửa |
| Sửa 1 trang lệch trang khác (transient mismatch) | **All-at-once:** sửa trọn site trong một lô, không để nửa vời |
| `axiom_4.html` (tên file = "4") nội dung "III" | **Quyết định filename (P6b)** — xem §3 |
| Text link vào ("Đọc: Tiên Đề IV…") lệch | **Cập nhật link-text site-wide (P6d)** |
| Card legacy thứ tự cũ (I,II,Phân Tán,Thời Gian,Biên Giới…) → số nhảy cóc | **Reorder hoặc replace-by-render (P6c)** |

---

## 3. PHA THỰC THI

### P6a — Inventory (bắt buộc làm trước, không sửa gì) — ✅ XONG 2026-06-06 → `plan/mach-re-P6a-inventory.md`
- Grep mỗi file: `Tiên Đề [num]`, `AXIOM [num]`, `[từ I+II]`-kiểu cross-ref, `✅ ← novel/synthesis`, link-text "Tiên Đề [num]".
- Lập bảng: `file · dòng · số cũ · axiom nó trỏ · số mới`. ~150 dòng.
- File ảnh hưởng: `what`, `upgrade`, `mach_re_homologous`, `axiom_4`, `axiom_conflict`, `how` (sơ đồ 3-Core cục bộ — xử lý riêng), `index`, `who`.

### P6b — Quyết định filename `axiom_4.html`
| Phương án | Ưu | Nhược |
|---|---|---|
| **A. Giữ tên `axiom_4.html`** (khuyến nghị) | không vỡ 4 inbound link + bookmark ngoài | tên file ≠ nội dung ("4" mà là III) — thêm chú giải |
| B. Đổi tên `axiom_3.html` | tên khớp nội dung | phải sửa mọi href + bookmark ngoài vỡ |
> Khuyến nghị **A** + thêm chú `<!-- file axiom_4.html = Tiên Đề III (Mạch Cội Dọc) -->` và một dòng hiển thị nhỏ.

### P6c — Render lại vùng tiên đề (per-page, content-aware)
- `what.html`: reorder 7 card về thứ tự mới (I,II,III=Thời Gian,IV=Biên Giới,V=Phân Tán,VI,VII) + đổi nhãn loại + sửa bảng tóm tắt/kiểm tra/sơ đồ dẫn xuất + cross-ref `[từ …]`. *(Hoặc thay cả vùng bằng render giống `axioms.html` để dedupe — cân nhắc single-source.)*
- `axiom_4.html`: title/meta/hero/breadcrumb/nội dung "IV"→"III"; cross-ref line ~396 "I, II, hay III(Phân Tán)" → "I, II, hay V".
- `mach_re_homologous.html`: "Tiên Đề IV"→"III" (toàn trang về Mạch Cội Dọc).
- `upgrade.html`: "7 Tiên Đề gốc" + ascii giới hạn theo số — remap; VIII giữ.
- `axiom_conflict.html`: VIII/II giữ số; các ref khác remap.
- `how.html`: sơ đồ "3 Core Axioms" CỤC BỘ — KHÔNG cùng tập; chỉ cập nhật câu "Tiên Đề IV vs triết học" (→III) + ghi rõ đây là sơ đồ rút gọn riêng.
- `index.html`: card "how" mô tả "Tiên Đề IV"→"III"; glossary "tiên đề II và III"(Phân Tán)→"II và V".

### P6d — Cập nhật link-text site-wide
- Mọi `<a>` có chữ "Tiên Đề [num]" trong text (vd `what.html:603`, `index.html:317/325`) → remap theo nội dung đích.

### P6e — Verify & retire
- Grep toàn site: không còn số mang nghĩa cũ; không còn "III=Phân Tán" lẫn "III=Thời Gian".
- **Gỡ banner** "đã tái dựng… số cũ" ở 6 trang (vì số đã trực tiếp đúng).
- Cập nhật `dictionary §9` + `axiom_spec.md §5.1` (đánh dấu migration hoàn tất).
- Ghi `CHANGELOG` (P5/G6).

---

## 4. THỨ TỰ & QUY TẮC
`P6a inventory → P6b filename → P6c render (theo file, all-at-once) → P6d link-text → P6e verify+gỡ banner+CHANGELOG`.
Quy tắc `dictionary §6`: P1 đa trang · P2 song ngữ · P3 dedupe · P4 không đụng `raw/`,`archives/` · P5 CHANGELOG.

## 5. RISK REGISTER
| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Sót ref → "III" hai nghĩa | 🔴 | P6a inventory đầy đủ + P6e grep verify |
| Vỡ inbound link/bookmark | 🟡 | P6b giữ filename (phương án A) |
| Reorder card phá nội dung kề | 🟡 | hoặc replace-by-render từ `axioms.html` (dedupe) |
| Công lớn, dở dang → trạng thái nửa vời tệ hơn | 🟡 | all-at-once; nếu không đủ thời lượng → KHÔNG bắt đầu, giữ banner |

## 6. KHUYẾN NGHỊ
- **Mặc định: HOÃN.** Banner hiện tại đã cho site coherence; batch này chỉ là cosmetic (RCA 3.4 < 4).
- **Chỉ làm khi:** cần bản xuất bản/publish hiển thị số mới trực tiếp, và có đủ thời lượng cho all-at-once.
- Nếu làm: **bắt buộc P6a (inventory) trước**, cân nhắc P6c bằng *replace-by-render từ `axioms.html`* để vừa renumber vừa dedupe (single-source).

---

> **Metadata cho LLM:** P6 = renumber batch · RCA 3.4 (polish, dưới ngưỡng) · remap nghĩa (III↔V, IV→III, V→IV) cấm find/replace · inventory-first + all-at-once · filename `axiom_4` giữ (khuyến nghị) · gỡ banner sau khi xong · nguồn: `axiom_spec.md §5.1`.

# P6a — Inventory Tham Chiếu Số Tiên Đề (foundation cho P6c)

> **Trạng thái:** read-only inventory (KHÔNG sửa gì ở pha này). Nguồn an toàn cho P6c renumber.
> **Ngày:** 2026-06-06. Loại `raw/` + `archives/` (P4). Map gốc: `axiom_spec.md §5.1`.
> **Quy ước:** chỉ liệt kê ref **CẦN ĐỔI** (III/IV/V mang nghĩa Phân Tán/Thời Gian/Biên Giới) + ranges/derivations + link-text. Ref tới I, II, VI, VII, VIII **GIỮ NGUYÊN** (không liệt kê trừ khi nằm trong range/derivation cần diễn giải lại).

---

## 0. BẢNG REMAP NGHĨA (3 số hoán đổi)
| Cũ | Axiom | → Mới |
|---|---|---|
| III | Phân Tán Bản Thể | **V** |
| IV | Mạch Cội Dọc | **III** |
| V | Biên Giới Động | **IV** |
> I, II, VI, VII, VIII giữ số. **Cấm find/replace** — "III"/"IV"/"V" mỗi chỗ phải đọc nghĩa.

---

## 1. NHÓM ĐỔI III (Phân Tán) → V
| File:dòng | Ngữ cảnh | Hành động |
|---|---|---|
| what.html:569 | `<!-- AXIOM III -->` + card Phân Tán | đổi nhãn III→V, **reorder** xuống nhóm Derived |
| what.html:652 | `[từ Tiên Đề III]` (Distributed, trong derivation VII) | III→V |
| what.html:672 | hierarchy "Tiên Đề III — Giữ Mà Không Gom" | III→V |
| what.html:690-691 | summary table row III | III→V (reorder) |
| what.html:706 | check-table row III (đã ⚠️) | III→V |
| what.html:734 | ascii "III — Phân tán ⚠️ có thể từ I+II" | III→V |
| what.html:764 | ascii "III — Phân tán bản thể [từ I+II]" | III→V |
| what.html:851 | self-limit "Tiên Đề III có thể bị hiểu chống mọi tập trung" | III→V |
| upgrade.html:288 | "UPGRADE III — Tiên Đề III" (nhãn axiom) | "Tiên Đề III"→"Tiên Đề V" (giữ "UPGRADE III" = số thứ tự upgrade) |
| upgrade.html:290 | "Tiên Đề III hiện tại: …phân tán phi tập trung" | III→V |
| upgrade.html:301 | (omitted) nội dung UPGRADE III | kiểm + III→V |
| axiom_4.html:396 | "Không suy ra từ Tiên Đề I, II, hay III" (Phân Tán) | **III→V** (chú ý: ngược chiều phần còn lại của trang!) |
| index.html:448 | glossary "thượng là tiên đề II và III" (Phân Tán) | III→V |

---

## 2. NHÓM ĐỔI IV (Mạch Cội Dọc) → III  *(lớn nhất)*
| File:dòng | Ngữ cảnh | Hành động |
|---|---|---|
| **axiom_4.html** | **toàn trang đơn-chủ-đề** Mạch Cội Dọc | title:6, meta:7, breadcrumb:204, hero tag:208, label:222/975, AXIOM IV:338, body: 438,461,469,488,492,502,508,522,546,554,571,579,594,601,605,617,635,643,658,663,732,739,740,924,928,948,958,973 — **TẤT CẢ IV→III** (trừ 396 ở §1, và VIII:961 giữ) |
| **mach_re_homologous.html** | **toàn trang** về Mạch Cội Dọc | 206,220,221,226,243,368,370,376,379,386,398,400,408,412,414,415,416,425,455,477,493,505,506,507,508,552 — **TẤT CẢ IV→III** |
| what.html:585 | `<!-- AXIOM IV -->` card Thời Gian | IV→III (Core, giữ vị trí 3) |
| what.html:653 | `[từ Tiên Đề IV]` (Vertical time) | IV→III |
| what.html:675 | hierarchy "Tiên Đề IV — Mạch Cội Dọc" | IV→III |
| what.html:692 | summary table row IV | IV→III |
| what.html:707 | check-table row IV "✅ ← novel" | IV→III |
| what.html:713 | "Tiên Đề IV (Mạch Cội Dọc) và VII…" | IV→III |
| what.html:731 | ascii "IV — mạch cội dọc ✅" | IV→III |
| what.html:855 | self-limit "Tiên Đề IV chỉ mô tả đối thoại với quá khứ" | IV→III |
| upgrade.html:308 | "UPGRADE IV — Tiên Đề IV" (nhãn axiom) | "Tiên Đề IV"→"Tiên Đề III" |
| upgrade.html:310 | "Tiên Đề IV hiện tại: …giao diện tổ tiên" | IV→III |
| upgrade.html:321 | (omitted) nội dung UPGRADE IV | kiểm + IV→III |
| upgrade.html:380 | "tự nhiên từ Tiên Đề IV Nâng cấp" | IV→III |
| axiom_conflict.html:253 | "trực giao V⊥H của Tiên Đề IV" | IV→III |
| index.html:325 | how card "Tiên Đề IV vs triết học thế giới" | IV→III |

---

## 3. NHÓM ĐỔI V (Biên Giới Động) → IV
| File:dòng | Ngữ cảnh | Hành động |
|---|---|---|
| what.html:607 | `<!-- AXIOM V -->` card Biên Giới | V→IV (Core, lên vị trí 4) |
| what.html:678 | hierarchy "Tiên Đề V — Ranh Giới Mềm" | V→IV |
| what.html:693 | summary table row V | V→IV |
| what.html:708 | check-table row V | V→IV |
| what.html:735 | ascii "V — Biên giới động ⚠️ có thể từ I+II+III" | V→IV (và "I+II+III" nội dung → diễn giải lại) |

---

## 4. LINK-TEXT cần đổi (P6d)
| File:dòng | Text hiện tại | → |
|---|---|---|
| what.html:603 | "Đọc chi tiết: Tiên Đề IV — Mạch Cội Nguồn" | "Tiên Đề III" |
| what.html:975 | footer `<a href="axiom_4.html">Tiên Đề IV</a>` | "Tiên Đề III" |
| mach_re_homologous.html:198,560,566 | `Tiên Đề IV` (link axiom_4) | "Tiên Đề III" |
| axiom_conflict.html:410 | footer `Tiên Đề IV` | "Tiên Đề III" |
| axiom_4.html:204 | breadcrumb `Tiên Đề IV` | "Tiên Đề III" |
> Lưu ý: filename `axiom_4.html` **GIỮ** (P6b phương án A) — chỉ đổi *text*, không đổi href.

---

## 5. RANGES / DERIVATIONS cần DIỄN GIẢI LẠI (không phải đổi số đơn)
| File:dòng | Cũ | Mới (theo spec) |
|---|---|---|
| what.html:682 | "Tiên Đề VII … [từ I–VI]" | VII [từ I+II+III+IV] (4 Core) |
| what.html:737 | "VII … ⚠️ có thể từ I–VI" | VII [từ I+II+III+IV] |
| what.html:740-766 | khối "Thử với 4 axioms / Đề xuất 4 cốt lõi" dùng I+II+IV+V, [từ IV+V], [từ I+II+IV+V] | remap nội dung: 4 Core = I,II,III,IV mới; VI[II+III+IV], VII[I+II+III+IV], V(Phân Tán)[I+II] |
| what.html:809 | "bốn Tiên Đề I–IV" (falsification) | **GIỮ "I–IV"** — số mới I–IV = 4 Core (nghĩa khớp) |
| axiom_4.html:398 | "Từ I–IV có thể suy ra toàn bộ" | GIỮ "I–IV" (nghĩa = 4 core, khớp) |
| upgrade.html:405 | "VIII không thay thế I-VII" | GIỮ "I–VII" (toàn hệ object-level + derived) |

---

## 6. TRƯỜNG HỢP ĐẶC BIỆT — KHÔNG remap theo bộ chính
| File | Vấn đề |
|---|---|
| **how.html** | Dùng sơ đồ **"3 Core Axioms" CỤC BỘ** (Core Axiom I/II/III — lines 389,400,411,414,426-431) — KHÁC bộ 8. KHÔNG remap như bộ chính. Chỉ: (a) câu "Tiên Đề IV vs triết học" (nếu có) → III; (b) giữ/ghi rõ đây là sơ đồ rút gọn riêng. **Cần quyết riêng** có hợp nhất vào bộ 8 hay không. |
| **index.html:293** | Nav card "axioms" ĐÃ là số mới (canonical) — GIỮ. |
| **axiom_4.html filename** | Tên `axiom_4` ≠ nội dung "III" — P6b giữ tên + chú giải. |

---

## 7. THỐNG KÊ & ĐÁNH GIÁ
- **Đổi III→V:** ~13 chỗ (rải 5 file). **Đổi IV→III:** ~70+ chỗ (chủ yếu axiom_4 + mach_re_homologous monothematic). **Đổi V→IV:** ~5 chỗ (what.html). **Link-text:** ~8. **Ranges diễn giải:** ~6. **Đặc biệt:** how.html (sơ đồ riêng).
- **Trang nặng nhất:** `what.html` (reorder card + bảng + ascii — phức tạp nhất, cân nhắc *replace-by-render từ axioms.html*). `axiom_4` + `mach_re_homologous` nhiều nhưng **near-uniform IV→III** (an toàn hơn, trừ axiom_4:396).
- **Bẫy nguy hiểm nhất:** `axiom_4.html:396` ("hay III" = Phân Tán → **V**) đi NGƯỢC chiều phần còn lại của trang (IV→III). Dễ sửa nhầm thành III.

---

## 8. KHUYẾN NGHỊ THỨ TỰ P6c (giảm rủi ro)
1. **mach_re_homologous.html** — monothematic, near-uniform IV→III, không cross-ref ngược → **an toàn nhất, làm trước để hiệu chỉnh quy trình.**
2. **axiom_4.html** — monothematic IV→III, NHƯNG nhớ 396 (→V) + filename giữ.
3. **upgrade.html** — vài chỗ III→V, IV→III; VIII giữ.
4. **axiom_conflict.html** — chỉ 253 (IV→III); còn lại II/VIII giữ.
5. **index.html** — 325 (IV→III), 448 (III→V); 293 giữ.
6. **what.html** — NẶNG NHẤT, làm cuối; cân nhắc replace-by-render từ `axioms.html` (vừa renumber vừa dedupe single-source).
7. **how.html** — quyết riêng (sơ đồ cục bộ).
8. **P6d link-text + P6e verify + gỡ banner + CHANGELOG.**

> **Verify cuối (P6e):** grep `Tiên Đề (III|IV|V)` toàn site → mỗi hit phải khớp nghĩa MỚI (III=Thời Gian, IV=Biên Giới, V=Phân Tán). Không còn nghĩa cũ lẫn lộn.

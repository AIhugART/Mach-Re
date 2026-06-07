# Mạch Rễ — Kế Hoạch Chỉnh Sửa Hệ Tiên Đề (v2.0 · sau review RCA)

> **Bản này thay thế tinh thần của** `mach-re-axiom-revision-plan.md` (v1). v1 giữ nguyên làm tham chiếu lịch sử.
> **Quyết định hướng đi (người dùng chốt 2026-06-06):** thực thi **đại phẫu thật** — biến III/VI/VII từ "Tiên Đề" thành "Mệnh Đề Dẫn Xuất" trên toàn framework.
> **Vai trò của v2:** v1 đúng về *ý tưởng kiến trúc*, nhưng bị **lệch thời điểm** (viết cho 7 tiên đề, trong khi hệ đã thành 8 + Module 5 + canonical naming). v2 **không hủy** v1 — v2 *nâng cấp* v1 để đại phẫu được thực thi mà **không phá** ba quyết định canonical ra đời sau nó.
> **Định dạng:** LLM-friendly Markdown — mỗi section độc lập.

---

## 0. TÓM TẮT QUYẾT ĐỊNH (TL;DR)

| Workstream | Verdict RCA | Điểm TB | Một dòng |
|---|---|---|---|
| **W1** — Đại phẫu 7→"4 Core + 3 Derived" | **PROCEED (có điều kiện)** | 2.4 → **4.2** sau khi bịt 3 lỗ hổng | Chỉ an toàn khi kèm W2+W3+W4 |
| **W2** — Migration canonical naming (`dictionary §9` SSOT) | **ADD (bắt buộc)** | 4.6 | Không có W2, đại phẫu = ghi đè SSOT → mâu thuẫn |
| **W3** — Định vị lại VIII (Meta-Axiom) + Module 5 trong sơ đồ mới | **ADD (bắt buộc)** | 4.6 | VIII không thuộc 4+3; phải đặt thành tầng phản tư riêng |
| **W4** — Chuyển hóa (KHÔNG xóa) đoạn "tự mổ xẻ 4-vs-7" | **ADD (bắt buộc)** | 4.8 | Bảo tồn điểm mạnh §7; đổi từ "giả thuyết mở" → "provenance của quyết định" |
| **W5** — Bổ sung prior-art mỗi tiên đề | **KEEP từ v1** | 4.6 | Thuần extend, không đụng cấu trúc |
| **W6** — Sửa mâu thuẫn bảng "Kiểm Tra Axiom" | **KEEP từ v1** | 4.6 | Lỗi thật, vẫn đang sống ([what.html:701-707](../what.html#L701-L707)) |
| ~~Overclaim IV~~, ~~disclaimer notation~~, ~~falsification per axiom~~ | **DONE (lỗi thời)** | — | Đã làm xong nơi khác — §9 |

**Quyết định tổng:** Đại phẫu **được chấp nhận** vì người dùng chủ động chọn, **nhưng chỉ thực thi theo trình tự W2→W3→W4→W1→W5→W6** để không tạo mâu thuẫn mới. Đại phẫu đơn lẻ (chỉ W1) bị từ chối ở mức 2.4/5.

---

## 1. RCA GỐC RỄ — VÌ SAO v1 CẦN NÂNG CẤP THÀNH v2

### 1.1 Triệu chứng
v1 đề xuất đổi tên III/VI/VII → "Mệnh Đề Dẫn Xuất" trên "10 file HTML" của Mạch Rễ v2.0.

### 1.2 3-round RCA × 5-Why

**Round 1 — Triệu chứng:** Nếu thực thi v1 *nguyên trạng*, nó sẽ đụng vào những thứ v1 chưa biết tồn tại.

**Round 2 — Cơ chế:** v1 viết khi hệ còn **7 tiên đề**. Sau đó (cùng ngày 2026-06-05 → 06-06) hệ thêm:
- Tiên Đề **VIII** "Tự Nhìn Thấy Mình" (Meta-Axiom, Reflexive Cognition) — `CHANGELOG.md`, `dictionary §9`.
- **Module 5 "Xung Đột Lõi"** = hệ quả của VIII (`axiom_conflict.html`).
- **Bảng tên canonical** `dictionary §9` — tự tuyên bố là *"nguồn chân lý duy nhất"*, chốt **cả 8 đều gọi là "Tiên Đề"**, điểm ≥4/5.

→ v1 nếu chạy nguyên trạng sẽ **ghi đè** ba quyết định ra đời *sau* nó.

**Round 3 — Gốc (một câu):** v1 vi phạm chính chuẩn nội tại của framework — hợp đồng *"extend, not overwrite"* (CLAUDE.md) và `dictionary §7` ("đoạn tự mổ xẻ '7 tiên đề thực ra cần 4'" nằm trong danh sách **cấm đụng**). **Fix = không hủy v1, mà bọc nó trong các workstream bảo toàn canonical (W2/W3/W4) trước khi đại phẫu (W1).**

### 1.3 Vì sao đại phẫu vẫn hợp lệ sau khi bịt lỗ hổng
Người dùng — tác giả framework — có thẩm quyền *nâng cấp* canonical. `dictionary §9` là SSOT *có thể sửa bằng cổng RCA*, không phải bất biến. Mâu thuẫn duy nhất là khi sửa **một phần** (đổi tên ở HTML mà quên SSOT). W2 loại bỏ đúng rủi ro đó: **sửa SSOT trước, đồng bộ HTML sau.**

---

## 2. KIẾN TRÚC MỤC TIÊU (sau đại phẫu)

### 2.1 Ba tầng

```
TẦNG PHẢN TƯ (Reflexive / Meta) — đứng NGOÀI và TRÊN hệ đối tượng
└── Meta-Axiom VIII — Tự Nhìn Thấy Mình (Reflexive Cognition)
       │  (tiên đề, nhưng ở tầng meta — quan sát chính hệ thống bên dưới)
       └── Hệ quả: Module 5 — Xung Đột Lõi (Core Conflict)
              = ảnh trực giao trục-H của Tự phê bình

TẦNG ĐỐI TƯỢNG (Object-level) — hệ tiên đề về bản sắc
├── 4 Core Axioms (độc lập thật)
│   ├── A1 — Quan Hệ Bản Thể     (Relational Ontology)
│   ├── A2 — Bất Biến Cấu Trúc   (Structural Invariance)
│   ├── A4 — Mạch Cội Dọc       (Vertical / Orthogonal Temporality)
│   └── A5 — Biên Giới Động      (Dynamic Boundary)
└── 3 Derived Propositions (suy ra, không phải tiên đề)
    ├── P3 — Phân Tán Bản Thể     [từ A1 + A2]
    ├── P6 — Chuyển Hóa Nhiễu Loạn [từ A4 + A5]
    └── P7 — Nổi Lên Có Hướng     [từ A1 + A2 + A4 + A5]
```

### 2.2 Quyết định kiến trúc then chốt (khác v1)

| # | Câu hỏi v1 bỏ ngỏ | Quyết định v2 | Lý do |
|---|---|---|---|
| Q1 | VIII đặt ở đâu trong 4+3? | **Tầng Meta riêng — KHÔNG tính vào "4 Core"** | VIII là *reflexive* (hệ tự quan sát), không cùng loại với A1–A5 (object-level). Gộp vào 4 Core là category error mới. |
| Q2 | Module 5 đi đâu? | **Hệ quả của VIII**, theo đúng `axiom_conflict.html` | Không gắn vào A2; giữ nguyên định vị đã chốt. |
| Q3 | V (Biên Giới Động) là Core hay Derived? | **Core (A5)** — chốt cứng | [what.html:732](../what.html#L732) gợi ý "V có thể từ I+II+III" → **mâu thuẫn cần sửa**: nếu V derived thì mất cơ chế tương tác môi trường → P6/P7 không dẫn xuất được. V phải là Core. Sửa dòng 732. |
| Q4 | Đếm tổng thế nào cho người đọc? | **"4 Tiên Đề Cốt Lõi + 3 Mệnh Đề Dẫn Xuất + 1 Meta-Tiên Đề"** | Trung thực với cả ba tầng; không ép về một con số. |

### 2.3 Sơ đồ dẫn xuất (object-level)

```
A1 ──┬──→ A2 ──────────────→ P3 (Phân Tán)   [A1+A2]
     │      │
     │     A4 (Mạch Cội Dọc)
     │      │
     │     A5 (Biên Giới Động) ──→ P6 (Chuyển Hóa) [A4+A5]
     │      │
     └──────┴────────────────────→ P7 (Nổi Lên Có Hướng) [A1+A2+A4+A5]
```

---

## 3. CỔNG RCA TỪNG WORKSTREAM (scoring, threshold 4/5)

Thang 5 điểm/tiêu chí. Đối tượng chấm = *hành động đề xuất*; ≥4/5 = hành động đáng làm.

| Workstream | Đúng | Sâu | Khả thi | Rủi ro MT⁺ | Bảo tồn | TB | Verdict |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--|
| W1 đại phẫu **đơn lẻ** | 3 | 4 | 2 | 1 | 2 | **2.4** | REJECT nếu đứng một mình |
| W1 đại phẫu **+ W2+W3+W4** | 4 | 5 | 4 | 4 | 4 | **4.2** | **PROCEED** |
| W2 migration SSOT | 5 | 5 | 4 | 4 | 5 | **4.6** | ADD |
| W3 định vị VIII + Module 5 | 5 | 5 | 4 | 4 | 5 | **4.6** | ADD |
| W4 chuyển hóa đoạn tự-mổ-xẻ | 5 | 5 | 5 | 4 | 5 | **4.8** | ADD |
| W5 prior-art | 4 | 4 | 5 | 5 | 5 | **4.6** | KEEP |
| W6 sửa bảng kiểm tra | 4 | 5 | 5 | 4 | 5 | **4.6** | KEEP |

⁺ *Rủi ro MT = rủi ro mâu thuẫn; điểm cao = ít tạo mâu thuẫn mới.*

> **Đòn bẩy của v2:** W1 nhảy từ 2.4 → 4.2 **chỉ nhờ** đi kèm W2/W3/W4. Đó là toàn bộ giá trị review này: không phải "có làm hay không" mà "làm theo trình tự nào để hợp lệ".

---

## 4. W2 — MIGRATION CANONICAL NAMING (làm TRƯỚC tiên)

**Mục tiêu:** SSOT (`dictionary §9`) phải phản ánh đại phẫu *trước khi* đụng bất kỳ file HTML nào (đảo trình tự của v1).

### 4.1 Sửa `dictionary_rule.md §9`
Thêm cột **"Loại"** vào bảng canonical, không xóa tên thuần Việt:

| # | Biểu hiện | Bản chất | EN | **Loại (mới)** |
|---|---|---|---|---|
| I | Sống Trong Quan Hệ | Có Nhau Mới Có Mình | Relational Ontology | **Core Axiom A1** |
| II | Nếp Bản Sắc | Đổi Mà Vẫn Là Mình | Structural Invariant | **Core Axiom A2** |
| III | Giữ Mà Không Gom | Ai Cũng Giữ Một Phần | Distributed Storage | **Derived P3** [A1+A2] |
| IV | Mạch Cội Dọc | Mạch Cội Nguồn | Vertical/Orthogonal Temporality | **Core Axiom A4** |
| V | Ranh Giới Mềm | Đóng Mở Có Chọn | Dynamic Boundaries | **Core Axiom A5** |
| VI | Hóa Nhiễu Thành Sức | Đau Được Xử Là Đau Lành | Perturbation Transformation | **Derived P6** [A4+A5] |
| VII | Nổi Lên Có Hướng | Hợp Lại Thành Cái Mới | Directed Emergence | **Derived P7** [A1+A2+A4+A5] |
| VIII | Tự Nhìn Thấy Mình | Soi Mình Mà Không Vỡ | Reflexive Cognition | **Meta-Axiom** |

### 4.2 Quy tắc đặt tên mới (thêm vào §9)
- **Số La Mã I–VIII GIỮ NGUYÊN** làm định danh ổn định (stable ID) cho người đọc — tránh phá mọi liên kết chéo và trí nhớ người dùng.
- Nhãn loại (`Core Axiom` / `Derived Proposition` / `Meta-Axiom`) là **thuộc tính bổ sung**, không thay số.
- Tên hiển thị đầy đủ mới: `Tiên Đề III — Giữ Mà Không Gom (Mệnh Đề Dẫn Xuất P3, từ A1+A2)`.
- ❗ **Không bỏ chữ "Tiên Đề" khỏi III/VI/VII trong điều hướng/breadcrumb** — chỉ thêm chú "(dẫn xuất)". Lý do: bỏ hẳn sẽ phá UX và mọi anchor `#tien-de-iii`. Đại phẫu là về *phân loại*, không về *xóa định danh*.

### 4.3 Ghi `CHANGELOG.md`
Một entry mới: "Đại phẫu kiến trúc 4 Core + 3 Derived + Meta VIII", kèm bảng điểm RCA của plan này (P5, `dictionary §6`).

---

## 5. W3 — ĐỊNH VỊ LẠI VIII + MODULE 5

- **VIII** chuyển nhãn → **Meta-Axiom** (tầng phản tư). Trong mọi sơ đồ ASCII kiến trúc (`what.html`, `upgrade.html`), vẽ VIII **tách khỏi** khối 4+3, có mũi tên "quan sát" trỏ xuống.
- **Module 5 (Xung Đột Lõi)** giữ nguyên định vị "hệ quả của VIII" — chỉ cập nhật nếu sơ đồ tổng có nhắc.
- Kiểm tra chéo: 4 self-limits ở [what.html:840-856](../what.html#L840-L856) — limit #2 (cần self-criticism) và limit #5 (core conflict) **đã được VIII + Module 5 giải quyết**; cập nhật wording để trỏ tới VIII thay vì để treo.

---

## 6. W4 — CHUYỂN HÓA ĐOẠN "TỰ MỔ XẺ 4-VS-7" (không xóa)

Section [what.html:718-795](../what.html#L718-L795) là **điểm mạnh được `dictionary §7` bảo vệ**. Đại phẫu *không* xóa nó — mà **đổi vai**:

| Trước (giả thuyết mở) | Sau (provenance của quyết định) |
|---|---|
| "Kiến trúc tối ưu: 4+3. **Nhưng đây vẫn là giả thuyết** — cần người khác phá vỡ." | "Mạch Rễ **đã chọn** kiến trúc 4 Core + 3 Derived. Dưới đây là đường suy luận dẫn tới quyết định đó — giữ lại làm bằng chứng cơ chế tự phê bình (Tiên Đề VIII)." |

→ Giữ 100% lập luận, chỉ đổi câu kết từ "ngỏ" → "đã quyết". Bảo tồn strength **và** loại mâu thuẫn "tự nói là giả thuyết nhưng đã thực thi".

---

## 7. W1 — CHỈNH SỬA TỪNG TIÊN ĐỀ (lõi đại phẫu)

Giữ nguyên nội dung chi tiết của v1 §3 (derivation cho P3/P6/P7, prior-art). Bổ sung/đính chính:

- **A1, A2, A4, A5** → giữ "Tiên Đề" + thêm nhãn "Core Axiom". Prior-art theo v1 §3.1/3.2/3.4/3.5.
- **III/VI/VII** → thêm nhãn "Mệnh Đề Dẫn Xuất" + block derivation (v1 §3.3/3.6/3.7), GIỮ tên thuần Việt + số La Mã.
- **Sửa [what.html:732](../what.html#L732):** bỏ dòng "V có thể từ I+II+III" (sai — V là Core, xem Q3 §2.2). Đây là edit độc lập quan trọng để bảng độc-lập-test khớp kiến trúc mới.
- **Falsification statement** [what.html:806](../what.html#L806) hiện viết "bốn Tiên Đề I–IV" → đổi thành "bốn Core Axiom (I, II, IV, V)" cho khớp tập core mới. ⚠️ Đây là điểm dễ sót.

---

## 8. W6 — SỬA MÂU THUẪN BẢNG "KIỂM TRA AXIOM" (lỗi thật, đang sống)

[what.html:701-707](../what.html#L701-L707) đánh **III, VI, VII = ✅ "Độc lập"** — mâu thuẫn trực tiếp với §3.6 (chúng là derived). Sau đại phẫu:

```
III | Độc lập: ✅ → ⚠️ derived (P3)
VI  | Độc lập: ✅ → ⚠️ derived (P6)
VII | Độc lập: ✅ → ⚠️ derived (P7)
```

Đồng bộ song ngữ + mọi bản sao bảng này nếu lặp ở file khác (quét P1).

---

## 9. CÁC MỤC v1 ĐÃ LỖI THỜI (đánh dấu DONE — đừng làm lại)

| Mục v1 | Trạng thái | Bằng chứng |
|---|---|---|
| Xóa overclaim IV "không có triết học nào…" | ✅ DONE | [what.html:710](../what.html#L710) đã là "tự thấy khác biệt nhất" |
| Thêm disclaimer notation / phân tầng công thức | ✅ DONE | `dictionary §4` |
| Falsification per axiom | ✅ DONE | [what.html:806](../what.html#L806) |
| Tái viết claim "đóng góp nguyên bản" | ◐ PARTIAL | ngôn ngữ "tự thấy khác biệt nhất" đã vào; phần phân loại 3-mức (Synthesis/Extension/Novel) còn optional |

---

## 10. RISK REGISTER & TRÌNH TỰ THỰC THI

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Sửa HTML mà quên SSOT → mâu thuẫn | 🔴 CAO | **W2 trước W1** (đảo trình tự v1) |
| Sót bản sao claim trên nhiều file | 🔴 CAO | **P1 quét đa trang** trước mỗi lô; grep "Tiên Đề III/VI/VII" toàn repo |
| EN/VN phân kỳ | 🟡 TB | **P2 đối xứng song ngữ** mỗi câu |
| VIII bị gộp nhầm vào "4 Core" | 🟡 TB | W3 vẽ tách tầng meta rõ ràng |
| Phá anchor `#tien-de-iii` / liên kết chéo | 🟡 TB | Giữ số La Mã làm stable ID (§4.2) |
| Mất điểm mạnh "tự phê bình" | 🟢 THẤP | W4 chuyển hóa thay vì xóa |

**Trình tự bắt buộc:** `W2 (SSOT) → W3 (VIII/Module5) → W4 (provenance) → W1 (đại phẫu HTML) → W5 (prior-art) → W6 (bảng) → ghi CHANGELOG`.

**Quy tắc quy trình (`dictionary §6`):** P1 quét đa trang · P2 song ngữ · P3 dedupe · P4 không đụng `raw/` · P5 ghi CHANGELOG sau mỗi lô.

---

## 11. CHECKLIST TRIỂN KHAI

### Lô 1 — SSOT & định vị (làm trước, không đụng HTML nội dung)
- [ ] W2: thêm cột "Loại" + quy tắc §4.2 vào `dictionary_rule.md §9`
- [ ] W2: cập nhật CLAUDE.md §"Tên thuần Việt" — thêm nhãn loại
- [ ] W3: quyết định VIII = Meta-Axiom tách tầng (ghi vào dictionary)

### Lô 2 — HTML cấu trúc (theo P1 quét đa trang)
- [ ] W1: thêm nhãn Core/Derived vào 7 h3 heading trong `what.html`
- [ ] W6: sửa 3 ô "Độc lập" bảng kiểm tra → ⚠️ derived
- [ ] W1: sửa [what.html:732](../what.html#L732) (V là Core, bỏ "V từ I+II+III")
- [ ] W1: sửa [what.html:806](../what.html#L806) falsification → "Core Axiom I, II, IV, V"
- [ ] W4: chuyển câu kết section 3.6 từ "giả thuyết" → "đã quyết + provenance"
- [ ] W3: vẽ lại ASCII kiến trúc tách tầng Meta VIII (`what.html`, `upgrade.html`)

### Lô 3 — Extend (an toàn, làm sau)
- [ ] W5: prior-art A1 (Whitehead, Buttimer, Anattā), A2 (Phan Ngọc, Lévi-Strauss), A4 (Heidegger, Gadamer, Burke), A5 (Ashby)
- [ ] W3: cập nhật 4 self-limits trỏ tới VIII/Module 5
- [ ] (optional) phân loại đóng góp 3 mức Synthesis/Extension/Novel

### Lô 4 — Chốt
- [ ] P1: grep toàn repo "Tiên Đề (III|VI|VII)" xác nhận đồng bộ
- [ ] P5: ghi `CHANGELOG.md` đợt đại phẫu + bảng điểm RCA

---

## 12. NHỮNG GÌ KHÔNG ĐỤNG (bảo tồn — `dictionary §7`)

| Phần | Lý do giữ |
|---|---|
| Tên thuần Việt 8 tiên đề (`§9`) | Canonical, điểm ≥4/5 — đại phẫu chỉ *thêm nhãn loại*, không đổi tên |
| Số định danh La Mã I–VIII | Stable ID — đổi sẽ phá anchor + trí nhớ người đọc |
| Hai tầng IV (Orthogonal vs Vertical) | RCA 5/5 — đại phẫu không đụng essence/manifestation |
| Đoạn tự-mổ-xẻ (chuyển hóa, không xóa) | Điểm mạnh nhất — W4 giữ lập luận |
| `raw/`, `archives/` | P4 — archive gốc |
| 5 khái niệm nền tảng, isomorphism 3 hệ, falsification conditions | `dictionary §7` |

---

*Tài liệu này là plan đã review (v2.0), chưa phải bản thực thi. Đại phẫu được người dùng chốt hướng 2026-06-06; mọi edit thực tế ghi CHANGELOG theo P5.*

> **Metadata cho LLM:**
> - Thay thế tinh thần: `mach-re-axiom-revision-plan.md` (v1)
> - Phụ thuộc đọc: `dictionary_rule.md §6/§7/§9`, `what.html §3.5–3.6`, `axiom_conflict.html`, `CHANGELOG.md`
> - Cổng quyết định: 3-round RCA × 5-Why × ≥4/5 (CLAUDE.md RULE ZERO)
> - Trình tự bất biến: W2 → W3 → W4 → W1 → W5 → W6

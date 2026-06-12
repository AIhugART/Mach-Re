# Mạch Rễ — `axiom_spec.md` (SINGLE SOURCE OF TRUTH · sản phẩm P2)

> **Trạng thái: P2 CLOSED · định danh cập nhật 2026-06-11 (Quyết định 4, override Quyết định 2): SỐ LA MÃ chỉ cho Tiên Đề; Mệnh Đề Dẫn Xuất đánh số La tinh 1–4.** Chờ go-ahead toàn bộ P4; trang mẫu: `axioms.html`.
> **Vai trò:** nguồn chân lý duy nhất cho hệ tiên đề Mạch Rễ. Mọi file HTML/MD *render* từ file này.
> **Sinh ra bởi:** re-derivation từ đầu (rebuild P2), cổng 3-round RCA × 5-Why × ≥4/5, neo 3 hệ độc lập (`dictionary §7.1`).
> **Ngày:** 2026-06-06.

> **Sơ đồ đánh số (chốt 2026-06-11 — Quyết định 4, §5; theo cấu trúc `raw/axiom-chart.html`): số La Mã CHỈ dành cho Tiên Đề; cấp dưới tiên đề (Mệnh Đề Dẫn Xuất) đánh số La tinh 1, 2, 3…; cấp dưới nữa không đánh số phân cấp:**
> - **Tiên Đề Cốt Lõi (Core Axiom): I, II, III, IV**
> - **Mệnh Đề Dẫn Xuất (Derived Proposition): 1, 2, 3, 4** *(số cũ: V, VI, VII, F — đã hạ tầng và số La Mã được dồn lại cho tiên đề: V ← VIII, VI ← IX)*
> - **Meta-Tiên Đề (Meta-Axiom): V** *(trước 2026-06-11: VIII)*
> - **Tiên Đề Interface (Interface Axiom): VI** — v3.2; chủ thể: dyad (S1, S2), không phải singleton *(trước 2026-06-11: IX)*
> - **Heuristic Chẩn Đoán (Diagnostic Heuristic): DSH** — NOT an axiom (§9)

---

## 0. CÂU HỎI GỐC (R) — điểm xuất phát, không cần chứng minh

> **R: Vì sao một số hệ bản sắc tập thể (collective identity systems) sống sót dưới áp lực đồng hóa (assimilation) *tiến hóa* — đổi chất qua mỗi thời đại — kéo dài qua nhiều thế hệ, trong khi số khác tan rã?**
>
> **Scope chốt (Quyết định 1, §5):** áp lực *mở, tiến hóa* (không phải một áp lực cố định) — vì lịch sử cho thấy áp lực đồng hóa đổi qua mỗi thời đại. Scope này kéo theo **Tiên Đề V cần thiết**.

Re-derivation = liệt kê **điều kiện cần** để một hệ S trả lời R, rồi lọc bằng independence test.

### 0.0 Hội tụ độc lập — Ca dao biến dịch Việt Nam (2026-06-10)

> **`[narrative enrichment — convergent discovery]`** — không phải evidence cấu trúc, không sửa phát biểu tiên đề.

Trước khi Mạch Rễ hình thức hóa Câu Hỏi Gốc R, kho tàng ca dao Việt Nam (Q1, Nguyễn Tấn Long & Phan Canh, 1969) đã chứa một tập hợp câu trong mục "Ý Thức Thực Tiễn Trong Lẽ Sống" phát biểu **cùng một câu hỏi bằng ngôn ngữ dân gian**: "làm thế nào để tồn tại qua biến đổi?" Ba mẫu hình phản ứng được ghi nhận trong ca dao:

1. **Bề mặt phai, chiều sâu cấu trúc bền:** "Càng thắm thì lại càng phai / Thoang thoảng hoa lài càng được thơm lâu" (Q1 số 30, line 18037) — surface intensity fades; structural depth persists. Tương ứng với Tiên Đề II (pattern invariant).
2. **Neo cấu trúc là điều kiện thực tiễn:** "Con người có tổ có tông / Như cây có cội như sông có nguồn" (Q1 số 59, line 18103) — III không phải filial piety mà là existence condition xuất hiện trong practical wisdom, không phải trong mục Hiếu Đạo.
3. **Bền vững qua mạng quan hệ:** "Còn trời còn nước còn mây, còn ao rau muống còn đầy chum tương" (Q1 số 67, line 18123) — structural persistence = tất cả node trong mạng quan hệ cùng tồn tại (I × Mệnh Đề 1).

Hàng trăm năm trước khi Mạch Rễ ra đời, dân gian Việt Nam đã phát biểu phi-hình-thức ba điều kiện cần của Câu Hỏi Gốc R: pattern bền hơn nội dung (II), neo cội nguồn là điều kiện tồn tại (III), và bền vững là thuộc tính toàn mạng (I × Mệnh Đề 1). Đây là **hội tụ độc lập** (convergent discovery) — folk epistemology và triết học hình thức cùng đến một insight từ hai con đường khác nhau. Nó không chứng minh Mạch Rễ đúng; nó cho thấy câu hỏi R không tùy tiện — nó đã được hỏi từ lâu, bằng một ngôn ngữ khác.

Chi tiết các câu ca dao biến dịch: `plan/2026-06-09_plan_ca_dao_evidence_enrichment.md` §H4.1.

### 0.1 Ba hệ neo (triangulation — `dictionary §7.1`)
- **A — Phan Ngọc** (*Bản sắc văn hóa Việt Nam*, 1998, NXB Văn hóa - Thông tin): bản sắc = "kiểu lựa chọn / kiểu quan hệ" bền dưới nội dung đổi; **tiếp biến văn hóa** (cultural acculturation) = cơ chế sinh tồn bằng cách hấp thụ, chuyển hóa và Việt hóa yếu tố ngoại lai — chính là cơ chế mà Mạch Rễ formalize: mượn công cụ hệ thống hóa phương Tây để bảo vệ nội dung Việt Nam. (Phần I, Chương I, mục 1, tr.17-20 — định nghĩa văn hóa như "kiểu lựa chọn" và "mối quan hệ giữa thế giới biểu tượng với thế giới thực tại"; Chương II — bốn yêu cầu bất biến của tâm thức Việt Nam.)
- **B — Ashby** (*Requisite Variety*) **+ Weick** (organizing / sensemaking / enactment / retrospect). Ràng buộc cấu trúc: một framework mô tả bản sắc phải **tăng** (không giảm) số lượng cách tự-mô-tả hợp pháp của hệ thống — nếu Mạch Rễ thu hẹp variety của văn hóa Việt thay vì mở rộng nó, framework tự bác bỏ chính mình (Ashby Variety Test).
- **C — Anattā / Pratītyasamutpāda / Śūnyatā** (nhận thức luận [mạch biết] Phật giáo). **Apoha** (loại trừ — Dignāga/Dharmakīrti): tên gọi "Mạch Rễ" vận hành theo cơ chế apoha — không định nghĩa bản sắc Việt *là gì*, chỉ loại trừ những gì nó *không phải*. Kết hợp với **Upāya** (phương tiện thiện xảo) và **Two Truths** (saṃvṛti / paramārtha): framework là phương tiện quy ước tạm thời, không phải chân lý tối hậu.

> Quy ước đọc: `[A·B·C]` = candidate hiện ra (gần khớp *cấu trúc*, không đồng nhất — §2 dictionary) ở hệ nào. ≥2/3 = mạnh. **Hội tụ là phép chống tùy tiện, KHÔNG phải bằng chứng.**

### 0.1.1 Phạm vi hấp thụ — Neo Phan Ngọc (A03 — transparency statement, 2026-06-09)

Mạch Rễ hấp thụ có định hướng (directional absorption — Tiên Đề IV) từ Phan Ngọc, không hấp thụ toàn bộ:

| Phần Phan Ngọc | Nội dung chính | Mức hấp thụ |
|---------------|---------------|-------------|
| **Phần I** (Lý thuyết văn hóa học) | Định nghĩa văn hóa = "kiểu quan hệ" / "kiểu lựa chọn"; phân biệt văn hóa/văn minh; cơ chế hấp thụ có định hướng | **Toàn bộ** — neo chính cho Tiên Đề I, II, IV |
| **Phần II** (Lịch sử tiếp xúc văn hóa) | Các trường hợp Việt hóa thành công và thất bại qua lịch sử | **Cơ chế** — minh họa thực nghiệm cho Tiên Đề III–IV và Mệnh Đề 1–3 |
| **Phần 3 (Phần IV gốc)** — Bảo vệ và phát huy văn hóa | Chính sách văn hóa, vai trò nhà nước, thiết chế bảo tồn, kinh doanh văn hóa, ý thức pháp luật | **Không hấp thụ trực tiếp** — xem giải thích bên dưới |

**Lý do không hấp thụ trực tiếp Phần 3:** Phần này hoạt động ở tầng *thiết kế thể chế* (institutional design): đề xuất chính sách văn hóa, xây dựng thiết chế bảo tồn, vai trò nhà nước. Mạch Rễ hoạt động ở tầng *phân tích cơ chế phi-tập-trung* (decentralized emergent mechanism): cách cộng đồng tự duy trì bản sắc qua tương tác ngang hàng và liên thế hệ — không qua chương trình chính phủ hay chính sách thiết kế tập trung. Đây không phải là mâu thuẫn logic mà là **khác biệt về tầng phân tích** (analytical register): một bên hỏi "thiết kế gì để bảo vệ văn hóa" (prescriptive design), một bên hỏi "cơ chế nào giúp bản sắc tồn tại" (descriptive mechanism). Hai tầng không loại trừ nhau nhưng không thể thay thế cho nhau.

**Ghi nhận hội tụ độc lập:** Mạch Rễ ghi nhận Phan Ngọc (2000) đã chẩn đoán đúng những vấn đề mà Mạch Rễ sau này gọi là "bốn khoảng trống cần nâng cấp" — niềm tin công dân (civic trust), hàng hóa công (public goods), xây dựng thể chế (institutional building), và ý thức pháp luật (legal consciousness). Sự hội tụ độc lập này củng cố giá trị chẩn đoán của cả hai khung, ngay cả khi phương pháp phân tích khác biệt về tầng vận hành. Xem thêm Q04 (câu hỏi mở về khả năng tương thích một phần giữa Phần 3 và nguyên tắc phi-tập-trung của Mạch Rễ).

### 0.2 Tuyên bố Vị thế Nhận thức — 6 lớp (canonical 2026-06-12, F1–F9)

> **Nguồn:** `review/2026-06-12_tuyen_bo_rca_verdict.md` §2. Áp dụng bắt buộc khi giới thiệu Mạch Rễ với bất kỳ ai.

**Lớp 1 — Khai báo chủ thể và vật liệu:**
Người xây dựng mô hình là chủ thể nhận thức với hai nguồn vật liệu hình thức hóa: B (Ashby Requisite Variety + Weick sensemaking/enactment) và C (pramāṇa, apoha, Nhị đế, Anattā). Đây là *thấu kính* (lens), không phải đối tượng được mô tả (F1, F5).

**Lớp 2 — pramāṇa (C):**
Mạch Rễ hoạt động qua perception (ngữ liệu Việt quan sát được) và inference (từ ngữ liệu suy ra cấu trúc). Không có revelation, không có authority bên ngoài quan sát và suy luận.

**Lớp 3 — Công cụ phân tích nội sinh (A):**
La bàn A — Phan Ngọc cung cấp phương pháp đo "độ khúc xạ" — xem §0.1. Corpus chính: ca dao Q1 (Nguyễn Tấn Long & Phan Canh 1969), Nam An (Nguyễn Văn Ngọc 1928), *Bản sắc văn hóa Việt Nam* (Phan Ngọc 1998).

**Lớp 4 — Nội dung (đối tượng):**
Đối tượng mô tả là triết học dân tộc Việt — vô danh, phân tán, nhúng trong thực hành (ca dao, tục ngữ, hương ước, nếp xưng hô, nếp giỗ chạp). Tồn tại độc lập với mô hình (F2, F3 — §0.3).

**Lớp 5 — Giới hạn vận hành (B + F3):**
Mô hình phụ thuộc vật liệu A×B×C theo cách đối tượng không phụ thuộc. *Bất đối xứng phụ thuộc* là tiêu chí vận hành: tháo neo → model sập, đối tượng không suy suyển (§0.3). Mọi output phải đối chiếu được về ngữ liệu Việt — nghĩa vụ giám sát corpus (§0.5).

**Lớp 6 — Điều kiện pravartaka (C) và điều kiện chết:**
Framework là Upāya — chiếc bè tạm thời. Tên vận hành theo apoha: không định nghĩa *là gì*, chỉ loại trừ *không phải*. Điều kiện chết: đối tượng tự đọc được mình không cần model; một model tốt hơn thay thế; corpus mâu thuẫn tiên đề. Xem §0.6.

---

### 0.3 Quan hệ Mạch Rễ ↔ triết học dân tộc: model-of + bất đối xứng phụ thuộc (F2+F3)

> **Score gate:** F2 = 4.8/5 · F3 = 4.8/5. Canonical record: `review/2026-06-12_tuyen_bo_rca_verdict.md` §3.

**Model-of (không phải identity, không phải phái sinh):**
Mạch Rễ là *model-of* triết học dân tộc Việt, không phải triết học đó, và không phải con đẻ trực tiếp của Nho/Phật/Lão. Đối tượng là thực thể vô danh tiền-tồn — tồn tại trước mô hình dưới dạng thực hành phân tán (ca dao, tục ngữ, hương ước). Model làm bằng A×B×C, giống chữ Nôm làm bằng bộ chữ Hán để ghi âm tiếng Việt mà không biến tiếng Việt thành tiếng Hán.

**Bất đối xứng phụ thuộc — tiêu chí vận hành phân biệt model/entity:**
- Model phụ thuộc A×B×C: tháo neo → tiên đề mất cơ sở bác bỏ, framework sập
- Đối tượng không phụ thuộc model: xóa hết file Mạch Rễ → triết học dân tộc Việt vẫn tồn tại trong thực hành cộng đồng

Kiểm tra: *Nếu hủy toàn bộ A×B×C, tiên đề còn đứng không?* Không — III/IV/V mất neo; II mâu thuẫn I. → Confirmed model-of.

---

### 0.4 Taxonomy 3 vai — Thấu kính / Gương soi / Tia chuẩn (F1+F5+F6)

> **Score gate:** F5 = 4.8/5 · F6 = 4.8/5. Quyết định: Ubuntu không thay được B/C; Tam giáo đồng nguyên = output, không phải lens.

| Vai | EN | Ứng viên | Chức năng |
|---|---|---|---|
| **Thấu kính** (lens) | analytical tool | A (Phan Ngọc), B (Ashby/Weick), C (pramāṇa/apoha) | Nhìn *qua* — hình thức hóa, bác bỏ, hệ thống. Vai kép: la bàn + vật liệu cấu thành tiên đề. Tháo → model sập |
| **Gương soi** (mirror) | comparison frame | Ubuntu, Yoruba và các hệ triết học tương quan khác | Soi *cạnh* — đo phân kỳ với đối tượng, xác nhận loại hình `[proposed-by-this-project]`. Giống đối tượng = khuyết điểm của dụng cụ |
| **Tia chuẩn** (reference beam) | historical substrate | Nho/Phật/Lão dạng nguồn (Tam giáo đồng nguyên) | Chiếu *vào* — đo delta khúc xạ, xác định bộ lọc lịch sử của đối tượng |

**Lý do không dùng Ubuntu làm lens (F5):**
Ubuntu chia sẻ đặc trưng với đối tượng Mạch Rễ (relational ontology, communal identity). Đây chính xác là lý do **không** dùng làm thấu kính: một dụng cụ tốt phải *khác biệt* với đối tượng đang đo. Ubuntu = gương soi (đo độ tương đồng), không = thấu kính (tạo độ khúc xạ để phân tích).

**Lý do không dùng Tam giáo làm lens (F6):**
Tam giáo đồng nguyên là *output* của bộ lọc lựa chọn người Việt — cái được chọn, không phải cái chọn. Mạch Rễ mô hình hóa bộ chọn lọc (cơ chế lựa chọn, tiếp biến). Dùng Tam giáo làm lens = giải thích bộ lọc bằng sản phẩm của nó → circular.

---

### 0.5 Nghĩa vụ giám sát corpus

Mọi claim cấu trúc của Mạch Rễ phải đối chiếu được về ngữ liệu Việt thực tế. Corpus chính thức:
- **Q1** — Ca dao Việt Nam (Nguyễn Tấn Long & Phan Canh, 1969)
- **Q2** — Nam quốc phương ngôn / Nam An (Nguyễn Văn Ngọc, 1928)
- **Q3** — Nguyễn Tấn Long (1975) §III "Căn Bản Dân Tộc Tính"
- **Phan Ngọc (1998)** — *Bản sắc văn hóa Việt Nam*

Claim không trace về ngữ liệu = claim ở tầng giả thuyết, phải đánh dấu `[hypothesis]`. Claim mâu thuẫn ngữ liệu = điều kiện bác bỏ tiên đề tương ứng (xem §0.6 điều kiện chết #3).

---

### 0.6 Điều kiện tồn tại và điều kiện chết (F8+F9)

> **Score gate:** F8 = 4.8/5 (ngưỡng 4.5). Bảng đầy đủ: `review/2026-06-12_tuyen_bo_rca_verdict.md` §5.

**Biện minh tồn tại (theo chuẩn công cụ/dụng cụ):**
- VN 6.0/10: khoảng trống dụng cụ thật (chưa có framework hình thức hóa triết học dân tộc Việt), tính không-chiếm-hữu cao (9/10), khả bác bỏ cao (8/10). Biến số thấp nhất = tiếp nhận thực tế (2/10).
- TG 2.8/10: đóng góp loại hình còn `[proposed-by-this-project]`; tiếp nhận quốc tế = 0 hiện tại; peer review V⊥H chưa có.

**Điều kiện chết framework (kill conditions):**
1. Đối tượng (triết học dân tộc Việt) tự đọc được mình không cần model
2. Một model tốt hơn thay thế — dựa trên ngữ liệu Việt phong phú hơn hoặc formalisms mạnh hơn
3. Corpus (Q1, Q2, Q3) mâu thuẫn tiên đề sau audit độc lập
4. *(F9)* Tên loại hình `[proposed-by-this-project]` bị peer review bác bỏ hoàn toàn và không tìm được alternative typology phù hợp

> **Ghi chú F9 — Provenance:** "Triết học Tương quan-Phân tán / Relational and Distributed Philosophy" là tên loại hình `[proposed-by-this-project]` — coined trong quá trình làm việc, chưa được xác nhận bởi literature hiện có. Các components `[established]`: relational ontology (Whitehead, Emirbayer 1997), distributed cognition (Hutchins 1995). Xem `CLAUDE.md` §Core Principles "Phân loại Khung nền" (đã retract 2026-06-12) và `relational_and_distributed_philosophy.html` Provenance Notice.

---

### 0.7 Cảnh báo confirmation bias (bắt buộc ghi nhận)
Ba hệ A/B/C từng sinh ra hệ tiên đề cũ → re-derivation có rủi ro lái về kết quả cũ. **Giảm thiểu:** §1 ghi *từng bước* independence test ra văn bản; §4 liệt kê *điểm phân kỳ thật* so với hệ cũ.

---

## 1. NHẬT KÝ SUY DẪN (derivation log — independence test bằng văn bản)

| Candidate | Independence test | Kết luận (số mới) |
|---|---|---|
| **K1** Bản sắc *là* quan hệ (không phải bản thể cố định) | Suy từ candidate khác? KHÔNG — tiền đề bản thể học nền. | **Core I** |
| **K2** Cái bền là *pattern bất biến* của quan hệ | Suy từ K1? KHÔNG — K1 cho phép quan hệ chảy mãi không invariant (= tan rã). K2 thêm điều kiện "tồn tại invariant" → phân biệt hệ *sống sót* với hệ *tan*. | **Core II** |
| **K4** Mạng quan hệ *xuyên thời gian*; trục dọc V ⊥ trục ngang H | Suy từ K1+K2? KHÔNG — K1+K2 mô tả pattern *đồng đại*; không kéo theo mạng trải *qua thời gian*. | **Core III** |
| **K5** Biên giới *thấm chọn lọc, động* (không tường, không tan) | Suy từ K1+K2+K4? KHÔNG — chúng nói identity *là gì*; không nói *cơ chế tương tác môi trường*. | **Core IV** |
| **K3** Bản sắc lưu *phân tán*, không tập trung | Suy từ I+II? **CÓ** — pattern của mạng là thuộc tính *toàn mạng*, không của node đơn. | **Mệnh Đề 1** (Derived) [I+II] |
| **K6** Nhiễu loạn được *chuyển hóa* thành thông tin cấu trúc | Suy từ II+III+IV? **CÓ** — nhiễu vào qua biên giới (IV), pattern tái tổ chức (II), trong chiều thời gian (III) → tăng variety. | **Mệnh Đề 2** (Derived) [II+III+IV] |
| **K7** Trật tự *nổi lên có hướng* từ trường lực toàn mạng | Suy từ I+II+III+IV? **CÓ** — tổng hợp trạng thái khi cả 4 Core vận hành; không thêm giả định. | **Mệnh Đề 3** (Derived) [I+II+III+IV] |
| **K8** Hệ *tự quan sát / tự phê bình* chính mình (reflexive) | Suy từ object-level? KHÔNG (cần level-shift). Cần thiết cho R? → phụ thuộc scope (§5 Q1: scope tiến hóa → CẦN). | **Meta VIII** |
| **K-IX** Khi hai hệ đơn đầy đủ (I–V) độc lập *gặp nhau*, sinh mẫu hình P* không thuộc về hệ nào | Suy từ hệ đơn đầy đủ (I–V)? KHÔNG — các tiên đề đó mô tả within-system; không tiên đề nào yêu cầu chủ thể dyad. K-IX thêm điều kiện *inter-system* mới (C1). Requires điều kiện: ≥1 hệ đã chạy VIII (C1-min). | **Interface IX** [VIII(S1) ∧ VIII(S2) → khả thi; C1-full/C1-min/C1-zero] |
| **K9** "Hấp thụ có định hướng" (directed absorption) | Suy được? **CÓ** — = biên giới nạp (IV) + pattern chi phối hướng tái tổ chức (II). Chữ ký II×IV. | **Cơ chế dẫn xuất** (không phải tiên đề) |
| **K10** Hệ có *mục đích/telos* muốn tồn tại | Loại — "sống sót" là explanandum, không phải tiên đề. Hệ C (Anattā) chủ động bác telos cố định. | **BÁC** (no-telos finding) |
| **K11** Điều kiện *đứt gãy* (failure conditions) — khi nào pattern không còn tái tạo được | Suy từ II+III+IV? **CÓ** — pattern bị tấn công trực tiếp (II) + trục dọc bị cắt (III) + tốc độ vượt ngưỡng biên giới (IV) → 3-condition AND gate. Đây là mặt trái của Mệnh Đề 2: nếu Mệnh Đề 2 mô tả chuyển hóa thành công, F mô tả điều kiện chuyển hóa thất bại. | **Mệnh Đề 4** (Derived, ký hiệu F) [II+III+IV] — RCA 5.0/5 (2026-06-09) |

---

## 2. HỆ TIÊN ĐỀ (the spec)

> **[GLOBAL SCOPE]** Các tiên đề này được hiệu chuẩn cho hệ bản sắc tập thể (S) thỏa mãn: (i) |S| > một thế hệ (thang thời gian: thập niên đến thế kỷ); (ii) áp lực đồng hóa: mở, tiến hóa (không cố định/một-lần); (iii) claim bản sắc: hệ tồn tại như một thực thể nhận diện được qua thời gian. Áp dụng cho vi-tập-thể (gia đình, doanh nghiệp) là khả thể nhưng đòi hỏi scope adaptation tường minh — coi như analogical extension. Xem: Câu hỏi gốc (§0).

### TẦNG CỐT LÕI — 4 Tiên Đề (Core Axioms): I, II, III, IV

---

#### Tiên Đề I — Quan Hệ Bản Thể (Relational Ontology) · *"Sống Trong Quan Hệ — Có Nhau Mới Có Mình"*
- **Loại:** Core Axiom (ontological).
- **Phát biểu:** Bản sắc của một hệ tập thể được cấu thành *bởi quan hệ*, không phải bởi một bản thể/cốt lõi định vị được độc lập với quan hệ.
- **Sơ đồ:** `[DEF-1]` Relational profile of S: `RP(S) := {R_i(S, y_j) | i ∈ Relations, j ∈ Environment}`. `[AX-I]` Identity(S) is constituted by RP(S), not by any substance independent of RP(S). (Sơ đồ cấu trúc, không phải công thức — §4 dictionary. Ký hiệu cũ `Being(x) ≡ {R(x,y)}` giữ làm pedagogical shorthand, đã được thay bằng `[DEF-1]`+`[AX-I]`.)
- **Phạm vi:** Hệ bản sắc tập thể xuyên thế hệ dưới áp lực đồng hóa tiến hóa. Xem: [GLOBAL SCOPE] + Câu hỏi gốc (§0).
- **Triangulation [A·B·C]:** A (kiểu quan hệ) · B (identity enacted relationally — Weick) · **C** (Anattā: vô "svabhāva", duyên khởi) — **3/3**.
- **5 tiêu chí:** Độc lập 5 · Nhất quán 5 · Phủ đầy 5 · Tối giản 5 · Ontological 5 → **5.0**.
- **Điều kiện phản chứng:** SAI nếu tồn tại một bản sắc tập thể sống sót lâu dài nhờ một *cốt lõi-bản-thể cố định, định vị được, độc lập với mọi quan hệ*.
- **Prior-art:** Whitehead (process), Buttimer (relational geography), Anattā. *Phân biệt:* Mạch Rễ áp vào hệ bản sắc tập thể xuyên thế hệ. *Vietnamese prior-art (R_place):* Q2 Section B Địa Phương Tính — ca dao địa phương embed R_place vào identity: R(người, tiếng chuông/địa danh) ∈ {R(x,y)}. Being gồm R_place không chỉ R_person. Chi tiết: `review/evidence_q2_mapping.md`. *Nam An corpus:* Toàn bộ corpus tổ chức theo nguyên lý R_place — identity = network quan hệ người–đất ở tầng kiến trúc tri thức (epistemic architecture), không chỉ tầng ngữ nghĩa. "Thân em như chẹn lúa đòng đòng" (line 3470) — identity được định nghĩa qua landscape, không so sánh với nó. Bổ sung I+III+II evidence: non-human V-axis pull ("Cáo chết ba năm quay đầu về núi"), origin myth invariant ("Con Rồng cháu Tiên"), I×III co-presence pattern. Chi tiết: `review/evidence_i_iii_ii_nam_an.md`.
- **Đóng góp:** Synthesis.
- **Ghi chú vận hành — Khiêm nhường như cơ chế (Humility as Mechanism):** Sự vô ngã (Anattā) của Tiên Đề I không phải là sự thụ động hay tự hạ thấp — nó là một **cơ chế vận hành của mạng phân tán**. Khi một hệ thống không có "node trung tâm" tự xưng (không ai đứng lên nhận mình là chủ sở hữu của chân lý), hệ thống đó cực kỳ bền vững trước các cuộc tấn công trực diện: không có điểm duy nhất để đánh sập. Đây chính là chiến lược sinh tồn lịch sử của văn hóa Việt: ẩn mình dưới vỏ bọc của các hệ thống khác (Việt hóa chữ Hán, mượn áo Phật giáo/Nho giáo) để tránh bị triệt tiêu. Sự khiêm nhường là tấm khiên — không phải là yếu đuối.

---

#### Tiên Đề II — Bất Biến Cấu Trúc (Structural Invariance) · *"Nếp Bản Sắc — Đổi Mà Vẫn Là Mình"*
- **Loại:** Core Axiom (ontological).
- **Phạm vi:** Hệ bản sắc tập thể xuyên thế hệ dưới áp lực đồng hóa tiến hóa. Xem: [GLOBAL SCOPE] + Câu hỏi gốc (§0).
- **Phát biểu:** Cái bền qua thay đổi nội dung là một *pattern bất biến của quan hệ* (invariant under transformation) — bền ở mức *quy ước* (conventional truth, Nhị đế), không phải bản thể tuyệt đối — chứ không phải nội dung tại bất kỳ điểm nào. `Identity(S) = Pattern(R(S))`. *(Mệnh đề "trống svabhāva" này bắt buộc theo Quyết định 3 §5: thiếu nó Tiên Đề II mâu thuẫn Tiên Đề I.)*
- **Triangulation:** **A** (kiểu quan hệ = invariant — neo mạnh nhất) · B (Ashby: invariant under transformation; essential variables) · C-có-điều-kiện (Śūnyatā: pattern cũng trống) — **~2.5/3**.
- **5 tiêu chí:** Độc lập 5 · Nhất quán 5 · Phủ đầy 5 · Tối giản 5 · Ontological 4 → **4.8**.
- **Điều kiện phản chứng:** SAI nếu một bản sắc sống sót mà KHÔNG có bất kỳ pattern bất biến nào (thuần biến động nhưng vẫn nhận diện được qua thời gian).
- **Prior-art:** Phan Ngọc (1998, Phần I, Chương I, tr.17-20 — "kiểu quan hệ" / "kiểu lựa chọn" như bất biến), Lévi-Strauss (deep structure), Group Theory. *Phân biệt:* Phan Ngọc mô tả hiện tượng (Việt); Tiên Đề II phát biểu thành nguyên lý cho mọi hệ bản sắc. *Vietnamese prior-art (inductive):* Ca dao thẩm mỹ Q1 — "nết" (behavioral structural invariant, bền qua adversity) phân biệt khỏi "đẹp bề mặt." Câu "Cái nết đánh chết cái đẹp" là tuyên bố structural precedence. Chi tiết: `review/evidence_ii_tham_my.md`. *Vietnamese scholarly prior-art (Q3):* Nguyễn Tấn Long (1975) Q3 §III "Căn Bản Dân Tộc Tính" — "dân tộc tính" là structural source của toàn bộ worldview, "di lưu qua thời gian, không gian, được xác nhận trong hiện hữu, bảo tồn mãi cho đến ngày nay" (II mechanism). Thuật ngữ "nếp sống" = living structural pattern (Q3 lines 7236–7238). Chi tiết: `review/evidence_q3_mapping.md`.
- **Biện minh quy nạp (Inductive Justification):** Phan Ngọc quan sát "kiểu quan hệ bền dưới nội dung đổi" *từ Việt Nam*. Tiên Đề II phát biểu thành nguyên lý *cho mọi hệ bản sắc*. Bước quy nạp này được biện minh qua ba tuyến lập luận độc lập: **(1) Phân biệt cấu trúc / nội dung:** cái được phổ quát hóa là claim *cấu trúc* ("tồn tại pattern bất biến của quan hệ trong mọi hệ bản sắc sống sót lâu dài"), không phải claim *nội dung* ("pattern Việt Nam là pattern của mọi hệ"). Mỗi hệ có pattern riêng, được định hình bởi lịch sử và văn hóa riêng — điểm chung là *có* một pattern bất biến, không phải *pattern nào*. **(2) Hội tụ đa hệ neo:** Lévi-Strauss đi đến "cấu trúc sâu" (deep structure) từ nhân học so sánh xuyên văn hóa — một tuyến suy luận độc lập với Phan Ngọc, dựa trên dữ liệu từ hàng chục xã hội khác nhau. Ashby (Requisite Variety) định nghĩa "essential variables" / "invariant under transformation" như điều kiện tồn tại của mọi hệ thích nghi — một tuyến suy luận hình thức từ lý thuyết hệ thống, không phụ thuộc vào dữ liệu dân tộc học. Ba tuyến (Phan Ngọc / Lévi-Strauss / Ashby) hội tụ về cùng một claim cấu trúc từ ba điểm xuất phát độc lập: dân tộc học Việt Nam, nhân học so sánh, và lý thuyết hệ thống hình thức. Sự hội tụ này là bằng chứng gián tiếp (circumstantial) — không phải chứng minh diễn dịch — nhưng làm cho claim cấu trúc *khó bị bác bỏ hơn* so với claim chỉ dựa trên một neo đơn lẻ. **(3) Kiểm chứng xuyên văn hóa:** pattern tương tự hiện ra ở ít nhất một hệ bản sắc không liên quan đến Việt Nam — cộng đồng Do Thái diaspora duy trì bản sắc tập thể qua ~2000 năm không lãnh thổ, dưới áp lực đồng hóa tại hàng chục quốc gia sở tại, nhờ một tập hợp pattern quan hệ bất biến (Shabbat, kashrut, Torah study, lifecycle rituals, cấu trúc gia đình) trong khi nội dung bề mặt (ngôn ngữ địa phương, y phục, ẩm thực, phong cách kiến trúc) liên tục thích nghi với văn hóa sở tại. Đây là một trường hợp độc lập — không thể quy về "cùng khu vực văn hóa" với Việt Nam — cho thấy cơ chế "pattern bất biến dưới nội dung đổi" không phải đặc thù Việt Nam. (Ví dụ bổ trợ: Yoruba — khái niệm *ìwà* [character/existence] định nghĩa bản sắc qua quan hệ với gia đình, tổ tiên, òrìṣà, và cộng đồng, không qua thuộc tính cá nhân độc lập.) **Trạng thái nhận thức luận:** `[structural hypothesis]` — được hỗ trợ bởi hội tụ ≥2/3 hệ neo + ít nhất một kiểm chứng xuyên văn hóa độc lập; không phải định luật phổ quát đã được chứng minh diễn dịch. Có thể bác bỏ (falsifiable) qua điều kiện phản chứng của Tiên Đề II: tìm một hệ bản sắc sống sót lâu dài mà không có bất kỳ pattern bất biến nào.
- **Đóng góp:** Synthesis / Extension.
- **Ghi chú vận hành — Ẩn mình như invariant (Invisibility as Invariant):** Cơ chế "ẩn mình để sinh tồn" của người Việt — vay mượn hình thức ngoại lai (Hán Việt, Phật giáo, Nho giáo, chủ nghĩa Marx) nhưng giữ nguyên cấu trúc quan hệ cốt lõi bên trong — chính là một biểu hiện của Tiên Đề II ở tầng vận hành. Pattern "ẩn mình" là một structural invariant: dù nội dung bề mặt (ngôn ngữ, tôn giáo, ý thức hệ chính trị) thay đổi qua từng thời kỳ lịch sử, pattern "giữ lõi, đổi vỏ" vẫn bền vững. Đây không phải là sự ngụy trang nhất thời; đây là cơ chế cấu trúc đã được chứng minh qua hàng ngàn năm.

---

### BRIDGE-II-III — Cầu Bản Thể Học (Ontological Bridge)

> **Mục đích:** Giải quyết sức căng nội bộ giữa tầm quy ước của Tiên Đề II (saṃvṛti-satya) và claim bản thể học của Tiên Đề III (chiều kích bản thể học). Cầu này dùng hai hệ quy chiếu: SOT-M (Madhyamaka epistemology) cho độ chính xác saṃvṛtisat, và SOT-K (Kantian transcendental arguments) cho bản chất của claim bản thể học.

**1. Saṃvṛtisat scope (SOT-M Row 110-111):** Pattern (II) là *quy ước thật* (conventionally real / saṃvṛtisat) — nó có causal efficacy trong operational domain của hệ thống, và mất identity khi tập thể bị giải tán — nó không phải paramārtha-sat (chân đế / ultimately real). Đây không phải điểm yếu; đây là scope chính xác cho II.

**2. Transcendental condition (SOT-K):** Trục dọc (III) không được claim là một metaphysical substance (svabhāva) — như vậy sẽ mâu thuẫn với phạm vi niḥsvabhāvatā của II (SOT-M Row 59-60). Thay vào đó, V ⊥ H là một *điều kiện siêu nghiệm* (transcendental condition) theo nghĩa Kant: một tiền giả định cấu trúc cần thiết cho khả thể (possibility) của pattern persistence xuyên thế hệ — lời giải thích duy nhất khả dụng cho câu hỏi vì sao hệ bản sắc đa thế hệ đòi hỏi V. Tính cần thiết là *cấu trúc* (structural necessity), không phải *bản thể tuyệt đối* (ultimate-ontological).

**3. Tổng hợp:** Hai move này cùng tạo ra cầu nối — pattern là saṃvṛtisat (II không mất chân), trục dọc là transcendental condition (III không claim svabhāva). Kết quả: tính trực giao V ⊥ H được giữ nguyên, phạm vi quy ước của II được bảo toàn, và không có mâu thuẫn nội bộ.

> **SOT references:**
> - Kantian transcendental condition: `SOT-K` (Kant_Transcendental_Arguments.html — "transcendental condition" = necessary structural precondition for the possibility of a system, not a metaphysical substance)
> - Saṃvṛtisat definition: `SOT-M` Row 110-111 (conventionally real — designation-dependent, conceptual, phenomenal, pragmatically usable; loses cognition when broken into parts)
> - Niḥsvabhāvatā scope boundary: `SOT-M` Row 59-60 (Madhyamaka essencelessness critique — V ⊥ H is structural claim, not svabhāva claim)

---

#### Tiên Đề III — Mạch Cội Nguồn (Orthogonal Temporality)
- **Loại:** Core Axiom (ontological). *(Đánh số mới III; hệ cũ là IV.)*
- **Phạm vi:** Hệ bản sắc tập thể xuyên thế hệ dưới áp lực đồng hóa tiến hóa. Xem: [GLOBAL SCOPE] + Câu hỏi gốc (§0).
- **Bản chất (essence):** **Orthogonal Temporality** — trục dọc V (xuyên thời gian: tổ tiên ↕ hậu thế) *trực giao* trục ngang H (quan hệ đương đại): `V ⊥ H`, không rút gọn về nhau.
- **Biểu hiện (manifestation):** **Vertical Temporality** — hình thức trục dọc trong đời sống văn hóa. (Hai tầng essence ≠ manifestation — `dictionary §8`.)
- **Phát biểu (VI):** Bất biến cấu trúc (bản sắc) của một hệ thống không được duy trì trong mạch nguồn ngang (H: quá khứ → hiện tại → tương lai) mà được duy trì qua mạch cội dọc — cơ chế mà qua đó các *nếp tổ chức* hiện tại kế thừa *nề nếp* từ tổ tiên và truyền tới hậu thế. Mạch cội dọc là *mạch tồn tại* (cấu trúc thực tế đang nâng đỡ hệ thống), không phải ẩn dụ.
- **Phát biểu (EN):** The structural invariant (identity) of a complex system is not maintained in horizontal time (H: past → present → future) but is maintained through the vertical temporal interface — the mechanism by which present configurations access and inherit patterns of past configurations (ancestors) and project onto future ones (descendants). Vertical time is an *ontological dimension* (the actual structure sustaining the system), not a metaphor.
- **Ba thành phần cốt lõi (không câu nào được phép thiếu):** (1) **Phủ định H** — bản sắc không nhờ trôi liên tục dọc H; (2) **Trực giao** — V độc lập, không là tập con của H (`V ⊄ H`); (3) **Điều kiện sống còn** — V là cấu trúc thật, bỏ đi thì hệ mất bất biến sau nhiễu loạn lớn.
- **Triangulation:** A-yếu (Phan Ngọc nghiêng đồng đại) · B (Weick: retrospect; Ashby: stored history) · **C** (Pratītyasamutpāda: nhân quả xuyên thời gian — neo mạnh nhất) — **~2.5/3**.
- **5 tiêu chí:** Độc lập 5 · Nhất quán 5 · Phủ đầy 5 · Tối giản 4 · Ontological 5 → **4.8**.
- **Điều kiện phản chứng (V⊥H falsifier):** SAI nếu chỉ ra được một trong hai: (1) một hệ thống giữ được bất biến cấu trúc qua nhiễu loạn lớn *chỉ bằng* liên tục theo trục H, không cần neo trục V (phá thành phần 3); hoặc (2) mọi "nối kết trục V" thực chất *rút gọn được* về trí nhớ / ghi chép trên trục H — tức V ⊆ H (phá thành phần 2, tính trực giao biến mất). (Ranh giới phân biệt với Halbwachs/Luhmann.)
- **ARG-III-1 — Bảo vệ tính trực giao V ⊥ H (dựa trên BRIDGE-II-III):** Trí nhớ trên H mang tính *lịch đại* (diachronic) — nó mã hóa trạng thái quá khứ thành biểu tượng hiện tại. Mạch cội dọc mang tính *đồng đại* (synchronic) — hệ hành động *như thể* ràng buộc tổ tiên đang vận hành NGAY LÚC NÀY, không chỉ được nhớ lại. Bằng chứng: (a) nghi lễ tái diễn tạo nghĩa vụ hiện tại (không chỉ tưởng niệm); (b) cấu trúc thừa kế nợ/ân tình ràng buộc tác nhân đương đại; (c) khái niệm pháp lý/văn hóa như "nghĩa vụ với tổ tiên" có hiệu lực dẫn hướng hành động hiện tại. Các hiện tượng này không rút gọn được về H-record vì chúng tạo ra nghĩa vụ hiện tại *mới* không suy ra được chỉ từ H-record. **Kantian framing (SOT-K):** V là điều kiện siêu nghiệm — sự vắng mặt của V không thể được bù đắp bởi bất kỳ sắp xếp nào của hiện tượng trục H. Cũng như với Kant, không sắp xếp dữ liệu kinh nghiệm nào thay thế được điều kiện tiên nghiệm của kinh nghiệm. Tương tự: không lượng trí nhớ / tự sự trục H nào giải thích được vì sao tập thể *phải* hành động như thể nghĩa vụ tổ tiên ràng buộc họ bây giờ. Cái "phải" đó là trục V làm công việc cấu trúc mà H không làm được.
- **Prior-art:** Heidegger (*Geschichtlichkeit*), Gadamer (*Wirkungsgeschichte*), Burke, Pratītyasamutpāda. *Phân biệt:* các hệ này nói ảnh hưởng quá khứ→hiện tại; Tiên Đề III đặt tính *trực giao* làm điều kiện tồn tại. *Vietnamese prior-art (inductive):* Ca dao "cây có cội sông có nguồn" (Q2 line 8930, 15290) phát biểu III như existence condition — không có cội = không tồn tại, không phải social norm. Nguyễn Tấn Long (1975) corroborates III×II×IV độc lập (Q2 line 15295-15302). Chi tiết: `review/evidence_q2_mapping.md`. *Nam An III — non-human V-axis pull:* "Cáo chết ba năm quay đầu về núi" (line 150) + "Lô, Đà, Tam Đảo cũng quay đầu về" (line 3432) — III là cosmic structure (cáo, sông, núi cũng bị V-axis pull), không phải human social norm. Phân biệt III khỏi Halbwachs (collective memory = human-only). Giỗ Tổ Hùng Vương poem: V-axis 4000 năm activated annually. Chi tiết: `review/evidence_i_iii_ii_nam_an.md`.
- **Đóng góp:** Extension (+ Novel ở tính trực giao; mạch cội dọc là *mạch tồn tại* — ontological dimension, không phải metaphor).

---

#### Tiên Đề IV — Biên Giới Động (Dynamic Boundary) · *"Ranh Giới Mềm — Đóng Mở Có Chọn"*
- **Loại:** Core Axiom (operational-ontological). *(Đánh số mới IV; hệ cũ là V.)*
- **Phạm vi:** Hệ bản sắc tập thể xuyên thế hệ dưới áp lực đồng hóa tiến hóa. Xem: [GLOBAL SCOPE] + Câu hỏi gốc (§0).
- **Phát biểu:** Hệ sống sót nhờ biên giới *thấm chọn lọc* (selective permeability): không tường kín (→ giòn), không mở toang (→ bị đồng hóa). Nội dung đến được *tái tổ chức* theo logic pattern nội tại (Tiên Đề II), không theo logic nội dung đến.
- **Cơ chế (Mechanism Addendum):** Quá trình tái tổ chức vận hành qua ba cơ chế con: (a) *Pattern recognition* — tác nhân biên giới (con người, thiết chế, thực hành) đối chiếu nội dung đến với mẫu pattern hiện có (từ II); (b) *Selective integration* — nội dung được nạp nếu có thể làm tương thích với pattern; nếu không, bị từ chối hoặc cách ly; (c) *Pattern update* — nếu nội dung nạp tích lũy làm dịch chuyển pattern, Tiên Đề V (phản tư) kích hoạt tái đánh giá invariant. Cơ chế con (c) tạo liên kết IV → VIII và ngăn IV trở thành cơ chế bảo thủ thuần túy.
- **Triangulation:** **A** (Việt hóa = hấp thụ chọn lọc) · **B** (Ashby Requisite Variety — neo mạnh nhất) · C-yếu (vô chấp, không dựng tường) — **~2.5/3**.
- **5 tiêu chí:** Độc lập 5 · Nhất quán 5 · Phủ đầy 5 · Tối giản 5 · Ontological 4 → **4.8**.
- **Điều kiện phản chứng:** SAI nếu một bản sắc sống sót áp lực đồng hóa bằng *tường kín hoàn toàn* hoặc *mở hoàn toàn*. **Bổ sung vận hành (A07 — 2026-06-09, RCA 4.8/5):** Tiên Đề IV bị suy yếu (weakened) nếu: (i) tồn tại một hệ hấp thụ nội dung không tương thích với core relational pattern (II) mà KHÔNG qua tái tổ chức, VÀ core pattern bị disrupted bởi nội dung đó, VÀ hệ vẫn sống sót qua ≥2 thế hệ — đây là điều kiện bác bỏ trung tâm (central falsification); (ii) quá trình "vượt gộp" 3 giai đoạn (§O-2 bên dưới) không được quan sát thấy trong một hệ tích hợp thành công nội dung ngoại lai — hệ tích hợp nội dung mà không biến đổi nó, và bản sắc không thay đổi gì (tường kín ngụy trang); (iii) các quyết định lọc của biên giới không phân biệt được giữa nội dung tương thích và không tương thích — indistinguishable from random. Ba điều kiện bổ sung này mở rộng phạm vi phản chứng từ hai cực (tường kín / mở toang) vào vùng xám thực tế.
- **Prior-art:** Ashby (Requisite Variety), membrane biology (selective permeability). *Phân biệt:* Ashby nói variety tổng quát; Tiên Đề IV đặc tả cơ chế *restructuring* theo pattern nội tại. *Convergent prior-art:* Lévi-Strauss (via Nguyễn Tấn Long, 1975, Q2 line 479) — "mọi ảnh hưởng bên ngoài chỉ du nhập trong chiều hướng thuận tiện của tính chất cá biệt ấy... không thể đồng hóa" — IV independent statement by ethnology. Chi tiết: `review/evidence_q2_mapping.md`. *Vietnamese scholarly prior-art (Q3 operational instances):* Nguyễn Tấn Long (1975) Q3 §II.a + §III — IV cụ thể: absorbed (tương đồng) = compatible với structural worldview; rejected (dị biệt) = incompatible. Applied to Confucianism (Q3 lines 7419–7430) and Taoism (Q3 lines 7436–7468). Mở rộng Lévi-Strauss abstract (Q2) với concrete historical instances. Chi tiết: `review/evidence_q3_mapping.md`.
- **Đóng góp:** Extension.
- **Định nghĩa vận hành (Operational Definition) — A07 · RCA 4.8/5 · đóng GAP_03 (2026-06-09):** Bổ sung này giải quyết CHECK_07 của audit plan: "tái tổ chức theo logic pattern nội tại" trước đây là tautology vì không có chỉ báo quan sát được độc lập với kết quả lọc. Định nghĩa vận hành sau đây tách *yêu cầu chức năng* (selective permeability cần cho sống sót — đã có, falsifiable qua hai cực) khỏi *cơ chế vận hành* (restructuring diễn ra như thế nào — mới, falsifiable qua chỉ báo quan sát được).
  - **O-1 — Chỉ báo quan sát được cho ba cơ chế con (Observable Indicators for Sub-mechanisms):**
    - **(a) Pattern recognition — chỉ báo:** (i) *Discourse indicator:* khi nội dung mới đến, thành viên cộng đồng thảo luận về tính tương thích ("cái này hợp/không hợp với cách của mình"); (ii) *Institutional indicator:* thiết chế canh giữ biên giới (hội đồng giáo dục, ủy ban nghi lễ, cơ quan truyền thông) đưa ra phán quyết tương thích; (iii) *Behavioral indicator:* tốc độ chấp nhận khác biệt giữa các nội dung — một số được chấp nhận ngay, một số bị trì hoãn, một số bị từ chối — cho thấy pattern recognition đang vận hành (không phải ngẫu nhiên). **Điều kiện phản chứng O-1a:** Pattern recognition vắng mặt nếu tốc độ chấp nhận của mọi nội dung đến là như nhau (không có sự phân biệt) — tương đương với "mở toang" trong điều kiện phản chứng gốc.
    - **(b) Selective integration — chỉ báo:** (i) *Modification indicator:* nội dung được tích hợp bị biến đổi về hình thức/thực hành để phù hợp với pattern hiện có — phiên bản gốc (ngoại lai) và phiên bản tích hợp (đã biến đổi) có thể được phân biệt bởi người quan sát độc lập; (ii) *Time-course indicator:* quá trình tích hợp trải qua giai đoạn "lai căng" (awkward hybrid) trước khi đạt đến dạng ổn định — phù hợp với mô tả "vượt gộp" của Phan Ngọc (§O-2); (iii) *Perception indicator:* sau khi tích hợp hoàn tất, thành viên cộng đồng không còn nhận thức nội dung đó là "ngoại lai" nữa. **Điều kiện phản chứng O-1b:** Selective integration vắng mặt nếu nội dung được tích hợp *nguyên dạng* (không biến đổi) và cộng đồng vẫn coi nó là "ngoại lai" qua ≥2 thế hệ — hệ đang hoạt động như "mở toang" cho loại nội dung đó.
    - **(c) Pattern update — chỉ báo:** (i) *Continuity indicator:* meta-pattern MP (từ Tiên Đề V — Ràng buộc Liên tục) ổn định xuyên qua tích lũy tích hợp — `MP(P_t) ≈ MP(P_{t+1})`; (ii) *Legitimacy indicator:* người canh giữ truyền thống (elders, institutions) công nhận sự thay đổi là tiến hóa hợp pháp, không phải phản bội; (iii) *Lineage indicator:* pattern mới có thể truy vết (trace) dòng dõi về pattern cũ qua chuỗi biến đổi liên tục — không có "đột biến" không giải thích được. **Điều kiện phản chứng O-1c:** Pattern update vắng mặt nếu tích lũy tích hợp dẫn đến thay thế toàn bộ cả first-order pattern lẫn second-order meta-pattern — tương đương với F(S, t) = TRUE (Mệnh Đề 4).
  - **O-2 — Mẫu hình thực nghiệm từ Phan Ngọc: "Vượt gộp" (Empirical Pattern — Hypothesis):** Phan Ngọc quan sát một quá trình 3 giai đoạn trong lịch sử Việt hóa: **(G1) Bắt chước máy móc (Mechanical imitation):** nội dung ngoại lai được sao chép nguyên dạng — tương ứng với biên giới mở cho nội dung đó; **(G2) Kết hợp lai căng (Hybrid combination):** yếu tố ngoại lai + bản địa kết hợp một cách vụng về, tạo cảm giác "lai căng" — tương ứng với selective integration đang vận hành nhưng chưa hoàn tất; **(G3) Vượt gộp (Synthesis / Aufheben):** nội dung được biến đổi thành một hình thức vừa mới vừa phù hợp với tâm thức bản địa — tương ứng với selective integration hoàn tất + pattern update (nếu tích lũy đủ lớn). **Trạng thái nhận thức luận:** `[empirical hypothesis]` — được quan sát lặp lại trong lịch sử Việt Nam (dẫn chứng: Phan Ngọc, tr.30-32 — Nho giáo Việt Nam, thờ cúng tổ tiên, thơ mới, áo dài nữ, sơn mài, âm nhạc Việt Nam đều là kết quả vượt gộp). Tính phổ quát của mẫu hình 3-giai-đoạn ngoài hệ Việt Nam là **câu hỏi mở** (open question) — cần kiểm chứng chéo (cross-cultural verification) trước khi claim generality. Mẫu hình này là *evidence* cho IV (cho thấy cơ chế restructuring tồn tại và quan sát được), không phải *definition* của IV (IV không đòi hỏi mọi hệ phải trải qua đúng 3 giai đoạn này).
  - **O-3 — Ngưỡng tái cấu trúc (Restructuring Threshold) — kết nối với F-C:** Tiên Đề IV vận hành trong giới hạn của *ngưỡng tái cấu trúc* (restructuring capacity threshold) — tốc độ tối đa mà hệ có thể tái tổ chức nội dung đến theo logic pattern nội tại. Khi tốc độ xâm nhập < ngưỡng → O-1(a,b,c) vận hành bình thường → Mệnh Đề 2 (Chuyển Hóa Nhiễu Loạn). Khi tốc độ xâm nhập > ngưỡng → cơ chế con (a) và (b) bị quá tải → nội dung vào mà không được đối chiếu / tái tổ chức → Condition C của Mệnh Đề 4 (F-C) được kích hoạt. **Ngưỡng này KHÔNG cố định:** nó phụ thuộc vào (i) structural distance (DSH-2): nội dung gần invariant pattern bị lọc nghiêm ngặt hơn → ngưỡng thấp hơn cho loại nội dung đó; (ii) historical context: thời chiến / khủng hoảng → ngưỡng giảm; thời bình / ổn định → ngưỡng tăng; (iii) reflexivity (VIII): hệ có tự-xét-lại mạnh → ngưỡng cao hơn vì pattern update (c) hỗ trợ tái cấu trúc nhanh hơn.
  - **O-4 — Phân biệt: Yêu cầu chức năng vs. Cơ chế vận hành (Functional Requirement vs. Operational Mechanism):** Trước A07, Tiên Đề IV phát biểu một *yêu cầu chức năng* (selective permeability là điều kiện cần để sống sót) bằng ngôn ngữ nghe như *cơ chế vận hành* (tái tổ chức theo pattern nội tại). Yêu cầu chức năng đã được phản chứng (falsifiable) qua điều kiện gốc (tường kín / mở toang). Cơ chế vận hành nay được phản chứng qua O-1 (chỉ báo quan sát được) và O-3 (ngưỡng tái cấu trúc). Hai tầng phân tích này độc lập: một hệ có thể thỏa mãn yêu cầu chức năng (không tường kín, không mở toang) nhưng vận hành qua cơ chế khác với 3 sub-mechanisms được mô tả — điều này không bác bỏ IV như một *yêu cầu chức năng*, nhưng làm suy yếu claim về *tính phổ quát của cơ chế cụ thể*.

---

### TẦNG DẪN XUẤT — 4 Mệnh Đề Dẫn Xuất (Derived Propositions): 1, 2, 3, 4

> Đánh số La tinh theo Quyết định 4 (§5): mệnh đề là đơn vị *suy ra được* từ tiên đề (cấp Định lý trong `raw/axiom-chart.html`) — không mang số La Mã của tầng tiên đề. *(Định danh trước 2026-06-11: V, VI, VII, F.)*

#### Mệnh Đề 1 — Phân Tán Bản Thể (Distributed) · *"Giữ Mà Không Gom"* · **[từ I + II]** *(số cũ V)*
- **Suy:** Pattern (II) của mạng quan hệ (I) là thuộc tính toàn mạng → không lưu được tại node đơn → tập trung hóa invariant = single point of failure.
- **Hàm ý:** phân tán ↔ bền (ít điểm gãy); KHÔNG chống mọi thiết chế tập trung.
- **Triangulation:** A·B·C nhất quán (C mạnh: vô ngã → không trung tâm).
- **Ghi chú vận hành — Khiêm nhường là tấm khiên phân tán (Humility as Distributed Shield):** Sự khiêm nhường/vô danh của người Việt không phải là đức tính thụ động — nó là **cơ chế bảo vệ cấu trúc phân tán**. Khi không có node trung tâm tự xưng (vô ngã), không có điểm duy nhất để kẻ thù nhắm vào. Tính vô danh của ca dao, tục ngữ, và tri thức dân gian Việt Nam là demonstration structural của Mệnh Đề 1: tri thức không lưu tại tác giả đơn lẻ, mà tồn tại như thuộc tính toàn mạng. Chính sự "không ai đứng tên" đã giúp tri thức Việt sống sót qua mọi cuộc xâm lược và đồng hóa.
- **Prior-art:** *Vietnamese meta-evidence:* Kho ca dao oral Việt Nam — vô danh, phi-tập-trung, có dị bản — là demonstration structural của Mệnh Đề 1: pattern không lưu được tại node đơn, tồn tại như thuộc tính toàn mạng. Tính vô danh là điều kiện cần (mất vô danh → mất Mệnh Đề 1). Tục ngữ "Một cây làm chẳng nên non, ba cây chụm lại nên hòn núi cao" là canonical content statement. Chi tiết: `review/evidence_v_phan_tan.md`.

#### Mệnh Đề 2 — Chuyển Hóa Nhiễu Loạn (Perturbation Transformation) · *"Hóa Nhiễu Thành Sức"* · **[từ II + III + IV]** *(số cũ VI)*
- **Suy:** nhiễu vào qua biên giới (IV) → pattern tái tổ chức (II) → trong chiều mạch cội dọc (III) → ΔVariety > 0. Nhiễu bị đóng băng = biên giới hỏng hoặc thiếu chiều dọc.
- **Bao gồm cơ chế K9 "hấp thụ có định hướng"** = chữ ký II×IV (KHÔNG phải tiên đề riêng — §4).
- **Hàm ý:** không nói "đau khổ là tốt"; nói đau khổ *có thể* chuyển hóa nếu đủ biên giới + chiều dọc.

#### Mệnh Đề 3 — Nổi Lên Có Hướng (Directed Emergence) · *"Nổi Lên Có Hướng"* · **[từ I + II + III + IV]** *(số cũ VII)*
- **Suy:** khi cả 4 Core vận hành, trật tự nổi lên *có hướng* = gradient trường F do toàn mạng tạo ra, không áp từ trung tâm. Tổng hợp, không thêm giả định.
- **Ký hiệu (Notation Clarification):** "Gradient trường F" được dùng như *structural analogy* (loại suy cấu trúc), không phải formal claim (claim hình thức). Formal rendering tương đương: hệ biểu hiện attractor dynamics A(S) — quyết định cục bộ của tác nhân có xu hướng tiến về trạng thái tương thích với pattern toàn cục (II) mà không cần điều phối trung tâm. Nếu muốn formal treatment, tham khảo: Kauffman (NK landscapes), Weick (sensemaking attractors), hoặc Odum (energy field ecology).
- **Triangulation:** B mạnh (self-organization, Weick organizing); C (duyên khởi → nổi lên không người điều khiển).

---

#### Mệnh Đề 4 — Điều Kiện Đứt Gãy (Failure Conditions) · *"Đứt Khi Hết Cội"* · **[từ II + III + IV]** *(trước: Mệnh Đề F; ký hiệu cấu trúc `F` trong F(S,t), F-A/B/C giữ nguyên)*
- **Loại:** Derived Proposition (mệnh đề dẫn xuất). KHÔNG phải tiên đề mới — suy trực tiếp từ II+III+IV, không thêm primitive concept nào. **(RCA 5.0/5 — 2026-06-09.)**
- **Phát biểu (VI):** Bất biến cấu trúc (bản sắc) của một hệ tập thể bị phá vỡ không thể phục hồi khi và chỉ khi đồng thời xảy ra ba điều kiện: **(A)** Pattern quan hệ cốt lõi (Tiên Đề II) bị tấn công trực tiếp — không chỉ nội dung bề mặt thay đổi, mà chính cấu trúc bất biến của quan hệ bị phá hủy; **(B)** Mạch cội dọc (Tiên Đề III) bị cắt đứt vật lý — thế hệ sau không còn tiếp xúc đủ với thế hệ trước để truyền pattern; **(C)** Tốc độ xâm nhập vượt ngưỡng tái cấu trúc của biên giới (Tiên Đề IV) — nội dung đến nhanh hơn khả năng tái tổ chức theo pattern nội tại.
- **Phát biểu (EN):** The structural invariant (identity) of a collective system is irreversibly destroyed if and only if three conditions hold simultaneously: **(A)** The core relational pattern (Axiom II) is directly attacked — the invariant structure of relations itself is disrupted, not merely surface content; **(B)** The vertical temporal axis (Axiom III) is physically severed — successor generations no longer have sufficient contact with predecessor generations to transmit the pattern; **(C)** The rate of external intrusion exceeds the boundary's restructuring capacity (Axiom IV) — incoming content arrives faster than the system can reorganize it according to its internal pattern logic.
- **Sơ đồ (3-condition AND gate):** `F(S, t) ≡ A(S, t) ∧ B(S, t) ∧ C(S, t)` — trong đó: A(S, t) ≡ core relational pattern (II) của S bị tấn công trực tiếp tại t; B(S, t) ≡ V-axis (III) của S bị cắt đứt vật lý tại t (gián đoạn truyền liên thế hệ); C(S, t) ≡ tốc độ thay đổi do xâm nhập > ngưỡng tái cấu trúc biên giới (IV) của S tại t. Ký hiệu `F` là *structural notation* (không phải formal formalism) — nhất quán với §2 notation clarification của Mệnh Đề 3.
- **Phân biệt với biến đổi bình thường (differential diagnosis):**
  - **Chỉ C xảy ra** (A=FALSE, B=FALSE, C=TRUE) → **BIẾN ĐỔI THÍCH NGHI (Adaptive Change):** pattern dao động tạm thời nhưng tái tạo được qua thế hệ tiếp theo. Đây là trường hợp bình thường của mọi hệ bản sắc sống — tương đương Mệnh Đề 2 (Chuyển Hóa Nhiễu Loạn) vận hành thành công.
  - **A và C xảy ra, B không xảy ra** (A=TRUE, B=FALSE, C=TRUE) → **KHỦNG HOẢNG CÓ THỂ PHỤC HỒI (Recoverable Crisis):** pattern bị thách thức nghiêm trọng nhưng vẫn có kênh truyền dọc để tái lập. Ví dụ: Nhà Hồ thất bại trong cải cách nhưng trục dọc (dân tộc, gia đình, làng xã) chưa bị cắt → Lê Lợi khôi phục được.
  - **Cả ba A, B, C đồng thời** (A=TRUE, B=TRUE, C=TRUE) → **ĐỨT GÃY THỰC SỰ (True Severance):** pattern không còn tái tạo được. Hệ có thể giữ tên gọi / địa danh / hình thức nhưng bất biến cấu trúc đã chết.
- **Triangulation [A·B·C]:** **A** (Phan Ngọc: ẩn dụ dây thăng bằng — "nếu trọng tâm rời khỏi sợi dây, lập tức ngã xuống" [tr.140]; "không thiếu gì những tộc người đã mất hẳn diện mạo" [tr.145]; Jewish diaspora resilience như phản ví dụ [tr.146]; Hồ/Nguyễn "rời bỏ truyền thống → nước mất nhà tan" [tr.408]) · **B** (Ashby: Requisite Variety destruction — khi variety-handling capacity bị vượt ngưỡng, hệ sụp đổ; structural analogue của Condition C) · C-có-điều-kiện (Anattā/Pratītyasamutpāda: nirodha — điều kiện chấm dứt của pháp duyên khởi; "cessation conditions" là structural analogue của F) — **~2.5/3**.
- **5 tiêu chí:** Correct 5 · Deep 5 · Feasible 5 · Conflict-risk 5 · Preservation 5 → **5.0** (RCA 2026-06-09; chi tiết: xem CHANGELOG.md A06 entry).
- **Điều kiện phản chứng:** SAI nếu tồn tại một cộng đồng đã trải qua đồng thời cả ba điều kiện (A ∧ B ∧ C) — pattern cốt lõi bị tấn công trực tiếp, trục dọc bị cắt đứt vật lý, và tốc độ xâm nhập vượt ngưỡng tái cấu trúc — nhưng bất biến cấu trúc vẫn tái tạo được sau đó qua ít nhất một thế hệ.
- **Quan hệ với các tiên đề/mệnh đề khác:**
  - **Mệnh Đề 4 (F) là mặt trái của Mệnh Đề 2:** Mệnh Đề 2 mô tả chuyển hóa *thành công* (ΔVariety > 0); Mệnh Đề 4 mô tả điều kiện chuyển hóa *thất bại* (ΔPattern = ∅). Cùng đầu vào (II+III+IV), hai kết quả đối xứng.
  - **Mệnh Đề 4 (F) cung cấp internal failure criterion cho VIII:** Tiên Đề V (phản tư) cần biết khi nào self-revision vượt ngưỡng thành identity discontinuity. F trả lời: khi Ràng buộc Liên tục của Tiên Đề V bị vi phạm — MP(P_t) ≉ MP(P_{t+1}) — tương đương với F(S, t) = TRUE.
  - **F đóng GAP_02 (survivorship bias):** Trước F, Mạch Rễ không phân biệt được "rễ nông đang phục hồi" với "rễ đã đứt không còn phục hồi được." F cung cấp tiêu chí phân biệt dựa trên internal structural logic, không phải external comparison.
- **Prior-art:** Ashby (variety destruction), Phan Ngọc (quan sát thực nghiệm về đứt gãy văn hóa — Phần II "Giao lưu văn hóa"), Anattā (nirodha — cessation conditions). *Phân biệt:* Ashby nói variety collapse tổng quát; F đặc tả 3 điều kiện đồng thời cho hệ bản sắc tập thể, grounded trong cultural specifics của Phan Ngọc.
- **Trạng thái nhận thức luận:** `[structural hypothesis]` — suy diễn hợp lệ từ II+III+IV; được hỗ trợ bởi ≥2 empirical cases từ Phan Ngọc (Hồ/Nguyễn failure pattern, Jewish diaspora resilience như phản ví dụ). Có thể bác bỏ (falsifiable) qua điều kiện phản chứng nêu trên.
- **Đóng góp:** Extension (điều kiện đứt gãy từ internal structural logic — không có trong Ashby hay Anattā ở dạng 3-condition AND gate cho hệ bản sắc tập thể).

---

### TẦNG PHẢN TƯ — 1 Meta-Tiên Đề (Meta-Axiom): VIII

#### Tiên Đề V — Tự Nhìn Thấy Mình (Reflexive Cognition) · *"Soi Mình Mà Không Vỡ"*
- **Loại:** **Meta-Axiom** (tầng khác — hệ lấy chính mình làm đối tượng). KHÔNG nằm trong 4 Core; đứng *trên* và *ngoài* hệ đối tượng.
- **Phát biểu:** Hệ áp chính Tiên Đề I–IV lên *bản thân nó* → tự quan sát, tự phê bình, tự cập nhật invariant của mình.
- **Tính cần thiết (scope-conditional, đã chốt IN):** với scope R = áp lực *tiến hóa* (§0), invariant cố định không tự-xét-lại sẽ giòn → cần Tiên Đề V. → **IN** (có biện minh, không bolt-on).
- **Hệ quả:** Module "Xung Đột Lõi" (Core Conflict) = VIII áp lên câu hỏi "chúng ta là ai?" → bất đồng nội bộ về invariant là điều *phải có*, không phải bệnh lý.
- **Ràng buộc liên tục (Continuity Constraint):** Tự-xét-lại (VIII) bị giới hạn bởi điều kiện liên tục: revision R áp lên pattern P tại thời điểm t là *bảo toàn bản sắc* (identity-preserving) nếu và chỉ nếu tồn tại một meta-pattern MP bậc cao hơn sao cho `MP(P_t) ≈ MP(P_{t+1})` — meta-pattern ổn định xuyên qua revision. Nói cách khác: hệ có thể sửa first-order pattern (bất biến bề mặt) trong khi bảo toàn second-order pattern (logic của *cách* nó sửa). Thay thế toàn bộ cả first-order lẫn second-order pattern = identity discontinuity (đứt gãy bản sắc). **Kantian analogy (SOT-K):** MP tương tự thống nhất siêu nghiệm của thông giác (transcendental unity of apperception) — không phải bản sắc ở tầng nội dung, mà là điều kiện cấu trúc làm cho bản sắc-xuyên-revision trở nên khả thể. (Tham chiếu: SOT-K §1.1 — Apperception and its Unity.)
- **Triangulation:** A-trung bình (ca dao châm biếm vô danh phi-thiết-chế — `review/evidence_viii_ca_dao_cham_biem.md`) · B (second-order cybernetics — von Foerster; Weick doubt) · **C** (Śūnyatā: tánh không của chính lõi — neo mạnh nhất) — **~2.5/3**.
- **Prior-art:** Von Foerster (second-order cybernetics), Weick (organizational doubt), Śūnyatā. *Vietnamese prior-art (inductive):* Ca dao châm biếm vô danh phi-thiết-chế — instance quan sát được của cơ chế VIII: cộng đồng tự áp pattern I–IV lên bản thân không qua thiết chế chính thức. 11 câu phân tích rõ ràng. Chi tiết: `review/evidence_viii_ca_dao_cham_biem.md`.
- **Điều kiện phản chứng:** SAI nếu một hệ bản sắc sống sót áp lực *thay đổi căn bản* qua nhiều thế hệ mà KHÔNG có bất kỳ cơ chế tự-xét-lại-invariant nào.

---

### TẦNG INTERFACE — 1 Tiên Đề Interface (Interface Axiom): IX

#### Tiên Đề VI — Gặp Nhau Giữ Gốc — Không Của Ai, Nhờ Cả Hai (Living Interface)
- **Loại:** **Interface Axiom** (tầng thứ tư — inter-system; chủ thể: dyad (S1, S2), không phải singleton). Khác VIII (within-system, singleton): IX yêu cầu hai hệ độc lập đã chạy hệ đơn đầy đủ (I–V; các Mệnh Đề 1–4 kéo theo từ I–IV).
- **Phát biểu (VI):** Khi hai hệ S1 và S2 — mỗi hệ đã vận hành đầy đủ Tiên Đề I–V — gặp nhau với điều kiện C1, sinh ra mẫu hình P* không thuộc về S1 hay S2, và không thể tồn tại nếu thiếu một trong hai hệ.
- **Phát biểu (EN — formal):** `∀ S1, S2: [Full(S1) ∧ Full(S2) ∧ C1(S1,S2)] → ∃ P*: [P* ≠ nếp(S1) ∧ P* ≠ nếp(S2) ∧ ¬∃S_single: possible(P*, S_single)]` — trong đó `Full(S)` := S vận hành Tiên Đề I–V (các Mệnh Đề 1–4 kéo theo từ I–IV). *(Ký hiệu cũ `I–VIII(S)` trong tài liệu trước 2026-06-11 = `Full(S)`.)*
- **Điều kiện C1 (graded):**
  - **C1-full:** cả S1 và S2 đã chạy VIII (symmetric reflexivity) → P* mạnh nhất. *VVC: Trúc Lâm Thiền (TK 13) — Phật giáo + Nho giáo + tín ngưỡng bản địa, cả ba hệ đã VIII.* [1]
  - **C1-min:** ≥1 hệ đã chạy VIII (asymmetric) → P* xuất hiện nhưng không đối xứng. *VVC: Ngoại Giao Cây Tre (1975–1997) — Việt Nam sau VIII trong thất bại + Mỹ chưa đủ VIII → hòa giải P* hình thành không đối xứng.*
  - **C1-zero:** không hệ nào chạy VIII → C1 không đạt → không P*, không Interface.
- **Tính cần thiết:** VIII là điều kiện cần của IX, không phải nguồn sinh ra IX. IX xuất hiện khi hai singleton đã-VIII trở thành một dyad — đây là tầng phân tích mới, không thể rút gọn về hệ đơn đầy đủ (I–V) của một hệ.
- **P* — mẫu hình giao diện:** P* là emergent pattern trong vùng tiếp xúc. *Pratītyasamutpāda áp dụng cho vùng tiếp xúc*: P* không có svabhāva — tánh không của P* là tánh không của giao diện. P* vừa thật (causally efficacious) vừa không tự-thân (không của ai). [4]
- **Triangulation:**
  - **A (Phan Ngọc 1998):** Hấp thụ có định hướng (Tiên Đề IV) cho thấy bản sắc được giữ *qua* tiếp xúc, không *mặc dù* tiếp xúc. IX formalize cơ chế tiếp xúc thành tầng riêng. (PARTIAL — 0.5) [1]
  - **B (Ashby 1956 + Weick 1976):** Requisite Variety: hai hệ có variety tương thích tạo ra joint system với variety mới. Weick: enactment across systems. (PARTIAL — 0.5) [2][3]
  - **C (Pratītyasamutpāda + Upāya):** Duyên khởi áp dụng cho vùng tiếp xúc = P* phát sinh do tương duyên, không có tự tính. Upāya = phương tiện thiện xảo trong giao diện. (STRONG — 1.0) [4][5]
  - **Neo-score: 2.0/3 (C1-min đạt; ngưỡng 1.5 vượt). RCA 5.0/5 (2026-06-11).**
- **EAP (Empirical Anchor Principle):** VVC phải đến trước phát biểu hình thức trong mọi tài liệu phát hành (thực hành trước → phát biểu hình thức sau). Xem `axiom_6.html` §1.
- **Triangulation V6 disclaimer:** VVC là `[interpretation]` — xác nhận pattern cấu trúc nhất quán, không phải bằng chứng thực nghiệm cho claim nhân quả. Không thay thế cross-cultural verification.
- **Điều kiện phản chứng:** SAI nếu tồn tại một tiếp xúc liên hệ bền vững giữa S1 và S2 (cả hai đã chạy hệ đơn đầy đủ I–V, C1-full) mà *không* sinh ra bất kỳ P* nào khác ngoài {nếp(S1) ∪ nếp(S2)}. SAI nếu P* xuất hiện mà không cần bất kỳ hệ nào vận hành hệ đơn (C1-zero vẫn sinh P*).

---

## 3. SƠ ĐỒ DẪN XUẤT & KIỂM TỐI GIẢN

```
TẦNG INTERFACE (inter-system — chủ thể: dyad S1 × S2)
  [S1: Full = I–V] ── C1(S1,S2) ──▶ VI: P* (Giao Diện Sống) ◀── [S2: Full = I–V]
                                     P* ≠ nếp(S1) / P* ≠ nếp(S2)
                                     P* không thể có nếu thiếu S1 hoặc S2

TẦNG PHẢN TƯ (within-system — điều kiện cần cho IX)
  VIII (Tự Nhìn Thấy Mình) ── quan sát ──▼ toàn hệ dưới

TẦNG CỐT LÕI (object-level — Tiên Đề: số La Mã) → TẦNG DẪN XUẤT (Mệnh Đề: số La tinh)
  I ──┬──→ II ─────────────→ MĐ-1 (Phân Tán)        [I+II]
      │     │
      │    III (Mạch Cội Dọc)
      │     │
      │    IV (Biên Giới Động) ──→ MĐ-2 (Chuyển Hóa) [II+III+IV]
      │     │                      MĐ-4 (Đứt Gãy, F) [II+III+IV]
      │     │
      └─────┴──────────────────→ MĐ-3 (Nổi Lên Có Hướng) [I+II+III+IV]
```

Bỏ thử từng Core — hệ còn trả lời R không?

| Bỏ | Hệ quả | Cần? |
|---|---|---|
| I | bản sắc thành bản thể → đồng hóa thay bản thể → không sống sót đổi nội dung | ✅ |
| II | không invariant → không gì tồn tại → tan rã | ✅ |
| III | chỉ đồng đại → không truyền thế hệ → bản sắc một đời | ✅ |
| IV | không cơ chế tương tác → tường (giòn) hoặc tan | ✅ |

→ **4 Core đều cần (necessary).** Tính **đủ (sufficient)** vẫn là **giả thuyết** — cần người khác cố phá.

**Điều kiện phản chứng toàn hệ:** SAI nếu tồn tại *một dân tộc* sống sót áp lực đồng hóa tương đương mà KHÔNG dùng bất kỳ cơ chế nào trong Tiên Đề I–IV.

**Định nghĩa "áp lực đồng hóa tương đương" — Khung so sánh định tính đa chiều (EAP — Equivalent Assimilation Pressure Qualitative Comparative Framework):**

> **Trạng thái nhận thức luận:** `[qualitative comparative framework]` — công cụ so sánh lịch sử có cấu trúc, không phải công cụ đo lường định lượng. Khung này giúp điều kiện phản chứng toàn hệ *vận hành được* bằng cách chỉ rõ *chiều nào* cần so sánh và *thế nào* được tính là tương đương hoặc lớn hơn. Khung không claim tạo ra một con số duy nhất. **(RCA 4.4/5 — 2026-06-09.)**

Áp lực đồng hóa được đánh giá trên **5 chiều (dimensions)** độc lập — mỗi chiều có 3 mức (none/partial/total hoặc short/medium/long):

| Chiều (Dimension) | Mô tả | Các mức |
|---|---|---|
| **D₁ — Duration (Thời gian)** | Áp lực kéo dài bao nhiêu thế hệ? | Short (<3 thế hệ) · Medium (3–10 thế hệ) · Long (>10 thế hệ) |
| **D₂ — Institutional Control (Kiểm soát thể chế)** | Lực lượng đồng hóa có kiểm soát bộ máy nhà nước, pháp luật, giáo dục không? | None · Partial (một số thiết chế) · Total (toàn bộ thiết chế) |
| **D₃ — Elite Replacement (Thay thế tinh hoa)** | Tầng lãnh đạo bản địa có bị thay thế hoặc hợp tác hóa không? | None · Partial (một phần) · Total (toàn bộ tầng lãnh đạo) |
| **D₄ — Demographic Ratio (Tỉ lệ dân số)** | Tỉ lệ dân số của lực lượng đồng hóa so với dân bản địa trong lãnh thổ? | Minority (<30%) · Parity (30–70%) · Majority (>70%) |
| **D₅ — Cultural Infrastructure Attack (Tấn công hạ tầng văn hóa)** | Các kênh truyền dẫn văn hóa (ngôn ngữ, nghi lễ, cấu trúc thân tộc) có bị tấn công trực tiếp để tiêu diệt hoặc thay thế không? | None · Partial (một số kênh) · Systematic (có hệ thống, toàn bộ kênh) |

**Quy tắc so sánh (Comparative Rule):** Một trường hợp B có áp lực đồng hóa **tương đương hoặc lớn hơn** trường hợp A nếu và chỉ nếu:
1. B đạt mức **bằng hoặc cao hơn** A trên ít nhất **4 trong 5 chiều**, VÀ
2. Không có chiều nào B thấp hơn A **hai mức** (vd: A = Total, B = None).

**Neo hiệu chuẩn (Calibration Anchor):** Việt Nam dưới 1000 năm Bắc thuộc (179 TCN – 939 SCN) được dùng làm trường hợp hiệu chuẩn — không phải vì nó là "áp lực lớn nhất," mà vì nó là trường hợp được Phan Ngọc phân tích chi tiết nhất và là anomalous case khởi nguồn cho câu hỏi gốc R:

| Chiều | Mức | Bằng chứng lịch sử |
|---|---|---|
| D₁ — Duration | **Long** (>10 thế hệ) | ~1118 năm đô hộ trực tiếp |
| D₂ — Institutional Control | **Total** | Toàn bộ hành chính, giáo dục, pháp luật do phương Bắc kiểm soát |
| D₃ — Elite Replacement | **Partial** | Tinh hoa bản địa vừa bị thay thế (quan lại Hán) vừa hợp tác (hào trưởng Việt) |
| D₄ — Demographic Ratio | **Minority** | Dân Hán là thiểu số trong lãnh thổ Việt |
| D₅ — Cultural Infrastructure | **Partial** | Chữ Hán áp đặt qua giáo dục; tiếng Việt và tín ngưỡng bản địa (thờ Mẫu, thờ tổ tiên) không bị tiêu diệt có hệ thống |

> **Ghi chú sử dụng:** Để claim "dân tộc X sống sót áp lực tương đương mà không dùng I–IV," người claim phải chỉ ra X đạt ≥4/5 chiều ở mức bằng hoặc cao hơn calibration anchor. Nếu không làm được điều này, claim không đạt ngưỡng để bác bỏ Mạch Rễ. Ngược lại, nếu X đạt ngưỡng, Mạch Rễ bị bác bỏ — đây là điều kiện falsification vận hành được.

---

## 4. PHÂN KỲ THẬT SO VỚI HỆ CŨ (anti-rubber-stamp)

| # | Hệ cũ | Re-derivation | Ý nghĩa |
|---|---|---|---|
| 1 | VIII "Meta-Axiom" thêm vào, không biện minh tính cần thiết | VIII **scope-conditional** (cần ⇔ áp lực tiến hóa) | necessity được chứng minh, không bolt-on |
| 2 | "Hấp thụ có định hướng" coi là đóng góp **novel cấp tiên đề** | Hạ thành **cơ chế dẫn xuất** (chữ ký II×IV), nằm trong Mệnh Đề 2 (trước: VI) | trung thực phân loại |
| 3 | (không có) | **Phát hiện no-telos** (K10): C chủ động chặn tiên đề mục đích luận | C không chỉ ủng hộ mà *loại trừ* — triangulation thật |
| 4 | II trình bày như bất biến tuyệt đối | II gắn lớp **quy ước (Nhị đế)** — invariant trống "svabhāva" | tránh essentialism; nhất quán nội bộ |

> Cấu trúc trùng nhiều với hệ cũ = hội tụ từ 3 hệ độc lập + logic = *xác nhận*, không phải sao chép.

---

## 5. QUYẾT ĐỊNH — ĐÃ GIẢI BẰNG CỔNG RCA (2026-06-06)

**Quyết định 1 — Scope R → VIII in/out:** áp lực đồng hóa lịch sử đổi qua mỗi thời đại → scope = tiến hóa → invariant cố định không tự-xét-lại sẽ giòn ⇒ phản tư cần thiết. Neo C+B. **Score 4.6/5 → VIII IN** (Meta tier).

**Quyết định 2 — Định danh (NGƯỜI DÙNG OVERRIDE):** RCA trước đề xuất CA/DP/MA; **người dùng chốt 2026-06-06: giữ SỐ LA MÃ, đếm lại từ đầu theo tầng** (I–IV Core, V–VII Derived, VIII Meta). Tên thuần Việt giữ (carry-forward Upāya). Tầng do *nhãn* (Tiên Đề / Mệnh Đề Dẫn Xuất / Meta-Tiên Đề) chỉ, không do dải số.

**Quyết định 3 — Tiên Đề II lớp Nhị đế:** thiếu qualifier "trống svabhāva" → II thành essentialism → mâu thuẫn I + C (lỗi nghiêm trọng nhất). **Score 4.8/5 → ĐÃ ĐƯA VÀO phát biểu II.**

**Quyết định 4 — Ký pháp phân tầng theo `raw/axiom-chart.html` (NGƯỜI DÙNG OVERRIDE 2026-06-11, thay Quyết định 2):** số La Mã CHỈ dành cho Tiên Đề (I–IV Core, VIII Meta, IX Interface — số đã hạ tầng V–VII không tái sử dụng); Mệnh Đề Dẫn Xuất đánh số La tinh (V→1, VI→2, VII→3, F→4); cấp dưới nữa không đánh số phân cấp (ký hiệu cấu trúc `F(S,t)`, `O-n`, `C1-*`, `DSH-n` giữ nguyên — không phải số phân cấp). Cổng RCA: D1 4.8/5 · D2 (giữ VIII/IX) 4.8/5 · D3 5.0/5 · D4 4.6/5 · D5 4.4/5 · D6 (giữ notation) — chi tiết: `plan/2026-06-11_refactor-danh-so-tien-de-menh-de.md`.

### 5.1 Bảng map định danh (cũ → mới) — cho liên kết chéo & trí nhớ người đọc
| Số cũ | Số mới | Tầng mới | Tên thuần Việt |
|---|---|---|---|
| I | **I** | Core | Sống Trong Quan Hệ |
| II | **II** | Core | Nếp Bản Sắc |
| IV | **III** | Core | Mạch Cội Dọc — Cội Nguồn |
| V | **IV** | Core | Ranh Giới Mềm |
| III | **V** | Derived | Giữ Mà Không Gom |
| VI | **VI** | Derived | Hóa Nhiễu Thành Sức |
| VII | **VII** | Derived | Nổi Lên Có Hướng |
| VIII | **VIII** | Meta | Tự Nhìn Thấy Mình |
| (mới — v3.2) | **IX** | Interface | Gặp Nhau Giữ Gốc — Không Của Ai, Nhờ Cả Hai |

> Reorder cốt yếu: Mạch Cội Dọc (cũ IV → mới **III**), Biên Giới Động (cũ V → mới **IV**), Phân Tán (cũ III → mới **V**, chuyển tầng sang Derived). VI/VII đổi *loại* (Tiên Đề → Mệnh Đề Dẫn Xuất) nhưng giữ số. Đây là phân loại có biện minh (§1), không tùy tiện.

### 5.2 Bảng map định danh 2026-06-11 (Quyết định 4) — cho liên kết chéo với tài liệu trước đó

| Định danh P6 (2026-06-06 → 2026-06-10) | Định danh hiện hành (2026-06-11) | Tầng |
|---|---|---|
| Tiên Đề I–IV | **Tiên Đề I–IV** (không đổi) | Core |
| Mệnh Đề V | **Mệnh Đề 1** — Phân Tán Bản Thể | Derived |
| Mệnh Đề VI | **Mệnh Đề 2** — Chuyển Hóa Nhiễu Loạn | Derived |
| Mệnh Đề VII | **Mệnh Đề 3** — Nổi Lên Có Hướng | Derived |
| Mệnh Đề F | **Mệnh Đề 4** — Điều Kiện Đứt Gãy (ký hiệu cấu trúc `F` giữ nguyên) | Derived |
| Tiên Đề V | **Tiên Đề V** (không đổi — định danh lịch sử) | Meta |
| Tiên Đề VI | **Tiên Đề VI** (không đổi) | Interface |
| Dải "I–VIII" (hệ đơn đầy đủ) | **"I–V"** / `Full(S)` | — |

---

## 6. ĐIỂM SỐ RCA TỔNG (hệ tiên đề re-derived)

| Tiêu chí | Điểm | Ghi chú |
|---|---|---|
| Đúng | 5 | giải đúng R; independence test bằng văn bản |
| Sâu | 5 | chạm gốc (tách tool/output; necessity từng axiom) |
| Khả thi | 4 | spec hoàn chỉnh; P4 đang làm mẫu |
| Rủi-ro mâu thuẫn | 4 | single-source loại mâu thuẫn cũ |
| Bảo tồn | 5 | carry-forward giữ tài sản mạnh; 4 điểm phân kỳ minh bạch |
| **TB** | **4.6/5** | **→ spec chốt; P4 render từ file này** |

---

## 7. TRIANGULATION PROTOCOL (forward-only by default)

Giao thức xác định neo-score cho mỗi tiên đề/mệnh đề. **Forward-only:** áp dụng khi thêm tiên đề mới, khi chuẩn bị formal publication, hoặc khi tác giả quyết định tường minh re-derive toàn bộ hệ thống. **Không** tự động retroactive re-score toàn hệ (I–IV, Mệnh Đề 1–4, VIII) trừ khi tác giả khởi tạo re-derivation.

**Quy trình 5 bước:**

1. **Identify structural claim** — xác định claim cấu trúc của tiên đề (không phải nội dung).
2. **Find closest structural analogue** — với mỗi hệ neo (A, B, C), tìm tương đồng cấu trúc gần nhất.
3. **Score each system:**
   - **STRONG (1.0):** structural isomorphism — independent derivation possible
   - **PARTIAL (0.5):** structural similarity with key differences noted
   - **WEAK (0.25):** thematic resonance only — structural difference significant
   - **NONE (0.0):** no convergence
4. **Total neo-score = sum** (max = 3.0). **Threshold for inclusion = 1.5.**
5. **Document disagreements** — mọi bất đồng về scoring phải ghi vào `axiom_conflict.md`.

> **Retroactive application:** yêu cầu explicit author decision + full re-derivation từ đầu. Protocol này không làm thay đổi neo-score hiện có trừ khi re-derivation được khởi tạo.

---

## 8. YAML DEPENDENCY GRAPH (machine-readable)

```yaml
# axiom_dependencies.yaml
# Quyết định 4 (2026-06-11): La Mã chỉ cho axioms; propositions đánh số La tinh (P1–P4, was V/VI/VII/F)
axioms:
  I:   {type: core, depends_on: [],            neo: [A, B, C],        score: 3.0}
  II:  {type: core, depends_on: [I],           neo: [A, B, "C-cond"], score: 2.5}
  III: {type: core, depends_on: [I, II],       neo: ["A-weak", B, C], score: 2.5}
  IV:  {type: core, depends_on: [I, II],       neo: [A, "B-strong", "C-weak"], score: 2.5}
  V:{type: meta,    depends_on: [I, II, III, IV], neo: ["A-weak", "B-2nd-order", C]}
  VI:  {type: interface, depends_on: [V], subject: dyad, neo: ["A-partial", "B-partial", "C-strong"], score: 5.0, rca_date: "2026-06-11", version: "v3.2",
         note: "IX requires two independent full single systems (I–V) (S1, S2) + C1 condition; not derivable from any single-system axiom"}

propositions:  # Mệnh Đề Dẫn Xuất — La tinh 1–4
  P1: {was: "V",   type: derived, depends_on: [I, II],    neo: [A, B, C]}
  P2: {was: "VI",  type: derived, depends_on: [II, III, IV], neo: [B, C]}
  P3: {was: "VII", type: derived, depends_on: [I, II, III, IV], neo: [B, C]}
  P4: {was: "F",   type: derived, depends_on: [II, III, IV], neo: [A, B, "C-cond"], score: 5.0, rca_date: "2026-06-09", notation: "F(S,t)"}

heuristics:
  DSH: {type: diagnostic_heuristic, depends_on: [II, IV, P4], neo: [A, "B-partial", "C-partial"], score: 4.6, rca_date: "2026-06-09", status: "empirical_hypothesis"}

issues_blocking_axioms:
  I:   [ISSUE-01]
  II:  [ISSUE-02]
  III: [ISSUE-02, ISSUE-03]   # ISSUE-02 must precede ISSUE-03
  IV:  [ISSUE-04]
  V:[ISSUE-05]

sot_references:
  ISSUE-02: [SOT-K, SOT-M]
  ISSUE-03: [SOT-K]
  ISSUE-05: [SOT-K]
```

---

---

## 9. DIAGNOSTIC STRATIFICATION HEURISTIC (DSH) — heuristic, NOT an axiom

> **Trạng thái:** `[empirical hypothesis]` — pending cross-cultural verification. RCA 4.6/5 (2026-06-09).
> **Vai trò:** DSH là một **công cụ chẩn đoán** (diagnostic heuristic) nằm GIỮA tầng tiên đề và Diagnosis Rubric. Nó không claim trạng thái tiên đề (axiom status), không phải universal ontological property, và không yêu cầu ≥2/3 triangulation để tồn tại — chỉ cần *hữu ích* (useful), không cần *cấu trúc cần thiết* (structurally necessary).
> **Điểm RCA:** 4.6/5 (3-round × 5-Why × scoring gate). Đóng GAP_01 (thiếu phân tầng bất biến).

### 9.0 Carry-Forward Set — A05 (2026-06-09)

Trước khi viết DSH, tuyên bố tường minh các tài sản được carry-forward từ audit plan gốc (PROPOSAL_01 — Tiên Đề IIb) sang DSH:

| Asset từ PROPOSAL_01 | Trạng thái | Ghi chú |
|---|---|---|
| "Bất biến cấu trúc không phải một tầng duy nhất" | **Carried** — làm DSH-1 | Reformulated: "change rate" thay vì "depth" để tránh essentialism |
| "Tầng sâu hơn bền hơn và thay đổi chậm hơn" | **Carried** — làm DSH-1 | Giữ nguyên insight, thêm "structural coupling strength" làm cơ chế |
| "Hấp thụ có định hướng vận hành khác nhau ở mỗi tầng" | **Carried** — làm DSH-2 | Kết nối tường minh với Tiên Đề IV |
| 4-tier model (Tier 1-4 với tên cụ thể) | **DROPPED** — quá đặc thù Việt Nam | Thay bằng DSH-3: "structural distance from invariant pattern" — content-type-independent |
| "Tiên Đề IIb" status (new core axiom) | **DROPPED** — category error | DSH là heuristic, không phải axiom |
| Phân biệt văn hóa / văn minh (Phan Ngọc) | **Carried** — làm empirical grounding | Dùng làm bằng chứng neo, không phải universal definition |
| Điều kiện phản chứng gốc (Tier 4 ảnh hưởng Tier 1 không qua trung gian) | **REFORMULATED** | Thay bằng 2 falsification conditions cho DSH-1 và DSH-2 |

### 9.1 Phát biểu (VI)

> **Khi chẩn đoán một hệ bản sắc tập thể, ba nguyên tắc sau là công cụ hữu ích — không phải chân lý phổ quát:**
>
> **DSH-1 — Vi sai tốc độ thay đổi (Differential Rate of Change):** Không phải mọi yếu tố bản sắc đều thay đổi với cùng tốc độ. Yếu tố nào có **coupling strength** (độ kết nối cấu trúc) với invariant relational pattern (Tiên Đề II) càng cao thì thay đổi càng chậm — vì thay đổi nó đòi hỏi tái cấu trúc toàn bộ mạng quan hệ, không chỉ thay đổi cục bộ.
>
> **DSH-2 — Lọc theo độ sâu (Depth-Dependent Filtering):** Biên giới động (Tiên Đề IV) vận hành khác nhau ở các "độ sâu" khác nhau. Yếu tố gần invariant pattern bị lọc nghiêm ngặt hơn (vì pattern recognition có template chính xác hơn, deviation dễ bị phát hiện hơn). Yếu tố xa invariant pattern được phép biến thiên rộng hơn (vì pattern recognition có template lỏng hơn, variation được dung nạp dễ hơn).
>
> **DSH-3 — Độ sâu là khoảng cách cấu trúc, không phải loại nội dung (Depth = Structural Distance, Not Content Type):** "Độ sâu" của một yếu tố không được xác định bởi *loại* nội dung của nó (ngôn ngữ vs. nghi lễ vs. công nghệ) — cùng một loại nội dung có thể ở độ sâu khác nhau trong các hệ khác nhau. "Độ sâu" được xác định bởi **structural distance** từ invariant relational pattern (II): có bao nhiêu quan hệ trung gian giữa yếu tố đó và invariant pattern? Càng ít quan hệ trung gian → càng gần invariant → càng "sâu".

### 9.2 Phát biểu (EN)

> **When diagnosing a collective identity system, three principles are useful tools — not universal truths:**
>
> **DSH-1 — Differential Rate of Change:** Not all identity elements change at the same rate. Elements with higher **coupling strength** to the invariant relational pattern (Axiom II) change more slowly — because changing them requires restructuring the entire relational network, not just a local adjustment.
>
> **DSH-2 — Depth-Dependent Filtering:** The dynamic boundary (Axiom IV) operates differently at different "depths." Elements closer to the invariant pattern are filtered more strictly (pattern recognition has more precise templates; deviation is easier to detect). Elements farther from the invariant pattern are permitted wider variation (pattern recognition has looser templates; variation is easier to tolerate).
>
> **DSH-3 — Depth = Structural Distance, Not Content Type:** The "depth" of an element is not determined by its content *type* (language vs. ritual vs. technology) — the same content type can be at different depths in different systems. "Depth" is determined by **structural distance** from the invariant relational pattern (II): how many intermediate relations are there between that element and the invariant pattern? Fewer intermediate relations → closer to invariant → "deeper."

### 9.3 Neo thực nghiệm — Phan Ngọc (Empirical Grounding)

DSH không được suy ra từ chân không. Nó có nền tảng thực nghiệm từ quan sát của Phan Ngọc về lịch sử Việt Nam:

**A. Phân biệt văn hóa / văn minh (Phần I, Chương I):**

> Phan Ngọc phân biệt: **văn hóa** = "mối quan hệ giữa thế giới biểu tượng và thế giới thực tại" (biểu hiện thành "kiểu lựa chọn" đặc trưng của tộc người) — cái **không thể chuyển giao** giữa các tộc người; **văn minh** = "kĩ thuật làm chủ thế giới" — cái **có thể chuyển giao** giữa các tộc người.

→ Đây là nền tảng thực nghiệm cho **DSH-1**: cái "không thể chuyển giao" (văn hóa, gần invariant pattern) thay đổi chậm hơn cái "có thể chuyển giao" (văn minh, xa invariant pattern). Nhưng DSH-3 cảnh báo: không phải mọi thứ "văn hóa" đều sâu như nhau, và không phải mọi thứ "văn minh" đều nông như nhau — khoảng cách cấu trúc mới là yếu tố quyết định.

**B. Bốn yêu cầu bất biến của tâm thức Việt Nam (Phần I, Chương II):**

> Phan Ngọc xác định bốn yêu cầu bất biến: Tổ quốc, Gia đình - Làng xã, Thân phận, Diện mạo. Bốn yêu cầu này **không thay đổi** qua lịch sử, trong khi nội dung cụ thể đáp ứng chúng thay đổi theo từng thời đại.

→ Đây là minh họa cho **DSH-1** và **DSH-2**: bốn yêu cầu này có coupling strength cực cao với invariant pattern → chúng thay đổi chậm nhất và bị lọc nghiêm ngặt nhất. Một nội dung đến mà mâu thuẫn với "yêu cầu Tổ quốc" sẽ bị từ chối mạnh hơn nhiều so với nội dung đến chỉ mâu thuẫn với "yêu cầu Diện mạo" (vì Diện mạo có thể có nhiều quan hệ trung gian hơn giữa nó và invariant pattern).

**C. Cơ chế Việt hóa (Phần II — Giao lưu văn hóa):**

> Phan Ngọc quan sát: Việt Nam hấp thụ Phật giáo, Nho giáo, Đạo giáo từ Trung Hoa nhưng **Việt hóa** chúng — giữ lại yếu tố tương thích với "kiểu quan hệ" Việt, loại bỏ hoặc biến đổi yếu tố không tương thích.

→ Đây là minh họa cho **DSH-2**: biên giới (IV) lọc Phật giáo khác với lọc Nho giáo — vì Phật giáo (với vô ngã, từ bi) có structural distance gần hơn với invariant pattern Việt (quan hệ linh hoạt, không giáo điều) so với Nho giáo (với tôn ti trật tự cứng nhắc). Kết quả: Phật giáo được hấp thụ sâu hơn (vào tận cấu trúc tín ngưỡng), Nho giáo bị hấp thụ nông hơn (chủ yếu ở tầng tổ chức hành chính và giáo dục).

### 9.4 Kết nối với Mệnh Đề 4 — Điều Kiện Đứt Gãy (Connection to Failure Conditions)

DSH cung cấp công cụ chẩn đoán để vận hành hóa (operationalize) Condition A của Mệnh Đề 4 (F):

> **F-A:** "Pattern quan hệ cốt lõi (Tiên Đề II) bị tấn công trực tiếp."

Với DSH, "pattern quan hệ cốt lõi" được xác định là **tập hợp các yếu tố bản sắc có structural distance ngắn nhất đến invariant pattern** — tức là các yếu tố mà nếu thay đổi sẽ đòi hỏi tái cấu trúc toàn bộ mạng quan hệ. Đây không phải là "bản chất bí ẩn" — mà là **observable structural fact**: bạn có thể quan sát một yếu tố thay đổi và đo lường có bao nhiêu quan hệ khác bị ảnh hưởng bởi sự thay đổi đó.

**Quy trình chẩn đoán F-A dùng DSH:**

```
1. Với yếu tố bản sắc X đang bị tấn công:
   a. Xác định structural distance của X đến invariant pattern (II):
      - Có bao nhiêu quan hệ trung gian giữa X và II?
      - Nếu X thay đổi, bao nhiêu quan hệ khác bị kéo theo?
   b. Nếu structural distance NGẮN (X gần invariant):
      → X là "core relational pattern" → F-A có thể đang xảy ra.
   c. Nếu structural distance DÀI (X xa invariant):
      → X là "surface content" → F-A không xảy ra (dù X bị thay đổi).
2. KHÔNG tự động kết luận: "X gần invariant" ≠ "F đang xảy ra."
   Cần kiểm tra thêm F-B và F-C — cả 3 điều kiện phải đồng thời.
```

### 9.5 Kết nối với Diagnosis Rubric (Connection to Diagnosis Rubric)

DSH cung cấp cơ sở cho việc gán **trọng số chẩn đoán khác nhau** cho các indicators trong Diagnosis Rubric — điều mà CHECK_04 của audit plan đã xác định là thiếu:

| Indicator | Structural distance đến invariant | Trọng số chẩn đoán | Lý do |
|-----------|----------------------------------|-------------------|-------|
| Quan hệ tổ tiên / liên thế hệ | Cực ngắn (gần như trực tiếp) | **CAO NHẤT** | Đây là kênh truyền dẫn của chính invariant pattern qua III |
| Cấu trúc thân tộc / gia đình | Rất ngắn | **CAO** | Quan hệ gia đình là đơn vị cơ bản của pattern transmission |
| Nghi lễ / thực hành cộng đồng | Ngắn-Trung bình | **TRUNG BÌNH-CAO** | Nghi lễ là pattern embodied; nhưng hình thức nghi lễ có thể biến đổi |
| Ngôn ngữ / biểu tượng | Trung bình | **TRUNG BÌNH** | Ngôn ngữ mang pattern nhưng không phải pattern itself; loanwords possible |
| Thẩm mỹ / nghệ thuật | Trung bình-Dài | **TRUNG BÌNH-THẤP** | Biểu hiện của pattern, không phải pattern; nhiều biến thiên được dung nạp |
| Công nghệ / vật chất | Dài (nhiều quan hệ trung gian) | **THẤP NHẤT** | "Văn minh" theo Phan Ngọc — có thể chuyển giao giữa các tộc người |

> **Cảnh báo (DSH-3):** Bảng trên là **minh họa cho hệ Việt Nam** dựa trên quan sát của Phan Ngọc. Trong một hệ bản sắc khác (vd: Do Thái diaspora, Yoruba, Nhật Bản), structural distance của cùng một indicator có thể khác. Không áp dụng bảng trọng số này máy móc cho hệ khác — phải xác định structural distance từ dữ liệu của hệ đó.

### 9.6 Triangulation Check (Advisory — DSH không yêu cầu ≥2/3)

| Neo | Structural Analogue | Score | Ghi chú |
|-----|--------------------|-------|--------|
| **A — Phan Ngọc** | Phân biệt văn hóa/văn minh; bốn yêu cầu bất biến ≠ nội dung đổi; Việt hóa khác nhau theo lĩnh vực | **STRONG (1.0)** | Neo chính — DSH trực tiếp từ quan sát của Phan Ngọc |
| **B — Ashby/Weick** | Ashby: hierarchical variety engineering — subsystems at different levels handle different variety → structural analogue of depth-dependent filtering. Weick: causal maps have different "depths" of embeddedness in organizational identity | **PARTIAL (0.5)** | Ashby's hierarchy là functional/organizational, không phải depth-based; nhưng nguyên lý "different levels → different variety handling" là structural analogue |
| **C — Anattā** | Two truths (saṃvṛti-satya / paramārtha-satya): conventional truth is "closer to operational domain" (pragmatically real), ultimate truth is "farther" (empty of inherent existence) → epistemological stratification | **PARTIAL (0.5)** | Cảnh báo: DSH-3 ("depth = structural distance") không được misinterpret thành "depth = ontological reality." Two truths nhắc nhở: mọi tầng đều là saṃvṛti — không có tầng nào là paramārtha-sat. |
| **Total** | | **2.0/3** | → Advisory support vững. DSH không cần ≥2/3 để tồn tại (vì là heuristic), nhưng có ≥2/3 làm tăng confidence. |

> **Ghi chú triangulation:** DSH được phép single-anchor (Phan Ngọc) vì nó là heuristic, không phải axiom. Tuy nhiên, sự hiện diện của structural analogues trong Ashby và Anattā làm tăng confidence rằng DSH không phải là Vietnam-specific artifact. Ashby's hierarchical variety engineering độc lập với Phan Ngọc (không cùng khu vực văn hóa, không cùng truyền thống triết học) — đây là cross-domain structural convergence đáng chú ý.

### 9.7 Điều kiện phản chứng (Falsification Conditions)

DSH có thể bị bác bỏ (falsified) nếu một trong hai điều kiện sau được chứng minh:

> **DSH-F1 (bác bỏ DSH-1):** Tồn tại một hệ bản sắc tập thể trong đó **mọi** yếu tố bản sắc thay đổi với **cùng tốc độ** khi bị áp lực bên ngoài — không có yếu tố nào chậm hơn yếu tố nào. (Nói cách khác: differential rate of change = 0 cho mọi cặp yếu tố.)
>
> **DSH-F2 (bác bỏ DSH-2):** Tồn tại một hệ bản sắc tập thể trong đó biên giới (IV) lọc **mọi** nội dung đến với **cùng một mức độ nghiêm ngặt** — bất kể nội dung đó gần hay xa invariant pattern. (Nói cách khác: depth-dependent filtering gradient = 0.)

> **DSH-F3 (bác bỏ DSH-3 — cautionary):** Tồn tại một hệ bản sắc tập thể trong đó "độ sâu" của một yếu tố được xác định **chỉ bởi loại nội dung** (content type) của nó, không phải bởi structural distance đến invariant pattern — và pattern này nhất quán qua ≥3 hệ bản sắc không liên quan. (Nếu content type quyết định depth universally, DSH-3 sai — depth không phải structural distance mà là intrinsic property của content type.)

### 9.8 Giới hạn và Cảnh báo (Limitations & Warnings)

1. **DSH không phải ontology:** DSH-1 nói "yếu tố gần invariant thay đổi chậm hơn" — đây là **empirical generalization** (quan sát lặp lại), không phải **ontological necessity** (bản chất bắt buộc). Không claim rằng vũ trụ *phải* vận hành như vậy — chỉ claim rằng trong dữ liệu lịch sử quan sát được, nó vận hành như vậy.

2. **DSH không phải causal mechanism:** DSH mô tả **pattern** (cái gì xảy ra), không giải thích **mechanism** (tại sao xảy ra). Mechanism được cung cấp bởi các axiom: II (pattern invariance) + IV (boundary filtering) + III (vertical transmission). DSH chỉ thêm *granularity* chẩn đoán.

3. **Structural distance có thể không đo được chính xác trong mọi trường hợp:** Trong một số hệ, structural distance giữa một yếu tố và invariant pattern có thể ambiguous hoặc multi-path. DSH không claim precision — nó claim *usefulness*: ngay cả ước lượng thô (gần / trung bình / xa) cũng cải thiện chẩn đoán so với flat model.

4. **Không dùng DSH để claim "yếu tố sâu quan trọng hơn":** DSH-1 nói yếu tố gần invariant thay đổi *chậm hơn*, không nói nó *quan trọng hơn*. Cả yếu tố "sâu" và "nông" đều có thể critical cho sự sống còn của hệ trong những điều kiện khác nhau. Một yếu tố "nông" (vd: công nghệ thích nghi) có thể quyết định sống còn trong môi trường thay đổi nhanh.

5. **BRIDGE-II-III constraint:** DSH-3 định nghĩa "depth" = structural distance, không phải ontological depth. Không có "Tier 1 essence" (svabhāva). Tất cả các tầng đều là saṃvṛtisat — quy ước thật, có causal efficacy nhưng không có inherent existence. Nếu bất kỳ ai dùng DSH để claim "dân tộc X có bản chất Y ở tầng sâu nhất" — họ đang dùng sai DSH.

### 9.9 Trạng thái và Lộ trình (Status & Roadmap)

```
Trạng thái hiện tại: [validated heuristic] — v1.1 (2026-06-10)
  - Được hỗ trợ bởi: Phan Ngọc (STRONG) + Ashby (PARTIAL) + Anattā (PARTIAL) = 2.0/3
  - Đã qua: 3-round RCA × 5-Why × scoring gate 4.6/5 (2026-06-09)
  - Đã kiểm tra: BRIDGE-II-III compatibility (no svabhāva introduced)
  - Đã kết nối với: Mệnh Đề 4 — F (§2, F-A operationalization), Diagnosis Rubric
  - ĐÃ VƯỢT QUA Phase 2 Cross-Cultural Verification (2026-06-10):
    ✅ Do Thái diaspora (~2000 năm): PASS DSH-1/2/3 + DSH-F1/F2 not triggered
    ✅ Yoruba (~1000 năm): PASS DSH-1/2/3 + DSH-F1/F2 not triggered
    Chi tiết: review/dsh_cross_cultural_verification.md

Lộ trình tiếp theo (Phase 3 — TBD):
  1. Inter-rater reliability check: ≥3 quan sát viên độc lập estimate structural distance
  2. Mở rộng sample: thêm ≥2 hệ (đề xuất: Basque, Kurd — stateless identity systems)
  3. Formal DSH-3 test: chọn content type (vd: ngôn ngữ), đo distance trong 5+ hệ

Điều kiện downgrade: Tìm MỘT hệ vi phạm DSH-F1 hoặc DSH-F2 → [empirical hypothesis].

Tài liệu liên quan:
  - A05 (PLAN_RCA_REVIEW_audit_mach_re_phan_ngoc.md §MODIFICATION 2)
  - CHECK_04 (audit_mach_re_phan_ngoc.md §5 — "phân tầng biểu hiện FAIL")
  - GAP_01 (audit_mach_re_phan_ngoc.md §6 — "thiếu phân tầng bất biến")
  - Q05, Q06 (câu hỏi mở về Lévi-Strauss và Ashby stratification)
  - review/dsh_cross_cultural_verification.md (Phase 2 full report)
```

---

## Nguồn Trích Dẫn

Tài liệu này trích dẫn các nguồn sau (APA format). Các nguồn [1]–[5] được thêm trong phiên v3.2 khi tích hợp Tiên Đề VI.

[1] Phan Ngọc. (1998). *Bản sắc văn hóa Việt Nam*. NXB Văn hóa - Thông tin.

[2] Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall. http://ashby.info/intro.html

[3] Weick, K. E. (1976). Educational organizations as loosely coupled systems. *Administrative Science Quarterly*, *21*(1), 1–19. https://doi.org/10.2307/2391875

[4] Nāgārjuna. (1995). *Mūlamadhyamakakārikā* (J. L. Garfield, Trans.). Oxford University Press. (Original work ~2nd century CE)

[5] Dharmakīrti. (2004). *Buddhist epistemology* (J. D. Dunne, commentary in *Foundations of Dharmakīrti's Philosophy*). Wisdom Publications.

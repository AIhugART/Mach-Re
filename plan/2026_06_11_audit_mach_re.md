# PLAN — RCA AUDIT: Epistemic Enclosure vs. Cultural Humility in Mạch Rễ Naming
<!-- 3-round RCA × 5-Why × scoring gate ≥ 4/5 — cultural-consistency audit -->
<!-- Date: 2026-06-11 | Method: RCA-driven single-lens deep audit | Status: DRAFT — awaiting approval -->

## METADATA

```yaml
document_type     : plan_audit_rca
subject           : Mạch Rễ Framework (axioms, landing pages, and specifications)
audit_lens        : Epistemic Enclosure (Appropriation of the Commons) vs. Cultural Humility (Anattā & Distributed Non-Ownership)
lens_type         : INTERNAL & CULTURAL CONSISTENCY
                    Does the framework's act of naming and systematizing violate the 
                    very principles of "non-ownership", "anattā", and "distributed identity" 
                    that it claims to protect?
primary_source    : analysis_results.md (RCA Naming Paradox, 2026-06-11)
fallback_source   :
  - axiom_spec.md (Single Source of Truth for Axioms)
  - review/audit_index_html_buddhist_pramana_phase1.md (Apoha semantics findings)
method            : 3-round RCA × 5-Why × scoring gate ≥ 4/5
references        :
  - index.html
  - what.html (specifically Section 4: RCA Naming)
  - why.html (specifically Section: Why Naming Now)
  - when.html
  - axioms.html & axiom_spec.md
status            : DRAFT — awaiting user approval before execution
```

---

## EXECUTIVE SUMMARY

**Quyết định phê bình cốt lõi: Mạch Rễ đang mắc phải một nghịch lý cấu trúc sâu sắc (constitutive paradox). Framework tuyên xưng bản sắc Việt Nam là phi bản thể (Tiên Đề I) và phân tán vô danh (Mệnh Đề V), nhưng chính hành vi "đặt tên và đóng gói" của framework lại mang tính chiếm hữu nhận thức (epistemic enclosure) — biến của chung khuyết danh thành sản phẩm hữu danh có nhãn hiệu.**

Cáo buộc của nhà nghiên cứu văn hóa: *"Văn hóa VN thực ra nó đề cao sự khiêm nhường, kể cả có nghĩ ra cũng không ai muốn đứng lên trên cả dân tộc mà đặt tên"* là hoàn toàn chính xác trên phương diện đạo đức học nhận thức. Tagline hiện tại `"Được sống: từ khi có dân tộc Việt. Được đặt tên: 2026."` là bằng chứng rõ nhất của sự ngạo mạn nhận thức (epistemic hubris).

Mục tiêu của cuộc audit này là:
1.  **Nhận diện và cô lập** mọi phát biểu, thuật ngữ, hoặc tuyên ngôn trong codebase mang tính chất "chiếm hữu chủ quyền nhận thức" đối với di sản chung của dân tộc.
2.  **Thiết kế giải pháp giải thực (de-enclosure)**: chuyển đổi định vị của Mạch Rễ từ "tên gọi của triết lý dân tộc" thành "tên gọi của mô hình phân tích", xóa bỏ mốc thời gian độc quyền, và thiết lập cơ chế mã nguồn mở nhận thức (CC0) để tự hủy tính chiếm hữu.

---

## 1. AUDIT TARGETS & CLAIMS INVENTORY

Cuộc rà soát này sẽ quét qua toàn bộ các tài liệu chính của dự án để phát hiện các biểu hiện của sự "chiếm hữu nhận thức".

| File | Vùng rà soát | Claim / Phần bị ảnh hưởng | Mức độ rủi ro |
| :--- | :--- | :--- | :--- |
| **index.html** | Hero Section (L417) | Tagline: `"Được sống: từ khi có dân tộc Việt. Được đặt tên: 2026."` | **CRITICAL** (Tuyên ngôn chiếm hữu lớn nhất) |
| **index.html** | What-box (L426-431) | Định nghĩa: `"Mạch Rễ là khung nền... được xây dựng để đặt tên và hệ thống hóa... triết lý sinh tồn... chưa từng được hệ thống hóa"` | **HIGH** (Thiếu định vị "mô hình phân tích") |
| **what.html** | Hero Section (L233) | Tagline và định nghĩa tương tự index.html | **HIGH** |
| **what.html** | Section 4 (L276-481) | RCA Tên gọi: Giải thích vì sao chọn tên Mạch Rễ nhưng thiếu việc ghi nhận "áp đặt biểu tượng tạm thời" | **HIGH** (Cần bổ sung tuyên bố tự phản tư) |
| **why.html** | Section RCA (L244) | *"Tại sao phải đặt tên ngay bây giờ"* — Lập luận có xu hướng "xảo ngôn biện hộ" nếu không làm rõ tính công cụ quy ước (Upāya) | **MEDIUM** |
| **when.html** | Timeline (L353-356) | Mốc thời gian `2026` với mô tả: `"Mạch Rễ được đặt tên"` | **HIGH** (Cố định hóa mốc đặt tên lịch sử) |
| **axiom_spec.md** | Section 2 (L92, 108, 142) | Cách diễn dịch các Tiên đề I, II, III. Đặc biệt cần làm rõ sự khiêm nhường là một thuộc tính vận hành (invariant) | **MEDIUM** |
| **LICENSE** | Toàn bộ | Giấy phép hiện tại (CC BY 4.0) bắt buộc ghi danh, cản trở tính chất "tài sản chung mở rộng" | **HIGH** (Cản trở de-enclosure pháp lý) |

---

## 2. KEY DIAGNOSTIC LENSES

Chúng ta sẽ dùng 3 lăng kính con của Đạo đức học tri thức để rà soát:

```
                  ┌────────────────────────────────────────┐
                  │          LĂNG KÍNH AUDIT               │
                  └───────────────────┬────────────────────┘
                                      │
         ┌────────────────────────────┼────────────────────────────┐
         ▼                            ▼                            ▼
┌──────────────────┐         ┌──────────────────┐         ┌──────────────────┐
│ L1: Định vị      │         │ L2: Tự phủ định  │         │ L3: Giải thực    │
│ Mô hình hóa vs   │         │ Tính công cụ     │         │ Bản quyền        │
│ Đặt tên Thực thể │         │ (Upāya / Tục đế) │         │ (CC0 Open Source)│
└──────────────────┘         └──────────────────┘         └──────────────────┘
```

*   **L1: Định vị Mô hình hóa vs. Đặt tên Thực thể (Model vs. Entity):**  
    Rà soát xem văn bản có đồng nhất "Mạch Rễ" với bản thân "triết lý dân tộc" hay không. Framework phải tự định vị là *mô hình mô tả* (như Thuyết vạn vật hấp dẫn), để ngỏ thực thể gốc vẫn khuyết danh và tự do.
*   **L2: Tự phủ định và Tính công cụ (Epistemic Humility & Upāya):**  
    Rà soát xem ngôn từ có mang tính giáo điều, tuyệt đối hóa hay không. Phải làm rõ Mạch Rễ chỉ là một *Upāya* (phương tiện thiện xảo) mang tính quy ước (*saṃvṛti-sat*), một chiếc bè tạm thời, không phải là chân lý tối hậu của dân tộc.
*   **L3: Giải thực Bản quyền (Licensing De-enclosure):**  
    Đánh giá cơ chế cấp phép. Một triết lý dân tộc không thể bị ràng buộc bởi điều khoản "ghi công tác giả" (CC BY 4.0). Nó phải được chuyển giao hoàn toàn thành tài sản chung không sở hữu (CC0 / Public Domain).

---

## 3. CHECKLIST KIỂM ĐỊNH CHI TIẾT (Audit Checklist)

### 🩺 Nhóm 1: Rà soát Tagline & Tuyên ngôn Lịch sử
- [ ] **Check 1.1 (index.html, what.html, when.html):** Có tồn tại cụm từ `"Được đặt tên: 2026"` hoặc `"Mạch Rễ được đặt tên"` không?  
  *Yêu cầu:* Xóa bỏ hoặc đổi thành `"Mô hình được xây dựng: 2026."` hoặc `"Tạm mô hình hóa: 2026."`
- [ ] **Check 1.2 (index.html, what.html):** Định nghĩa Mạch Rễ có dùng các từ mang tính áp đặt như "đặt tên cho triết lý dân tộc" không?  
  *Yêu cầu:* Sửa thành "đặt tên cho mô hình cấu trúc mô tả triết lý sinh tồn".

### 🩺 Nhóm 2: Rà soát RCA Tên gọi & Biện hộ (what.html, why.html)
- [ ] **Check 2.1 (what.html §4):** RCA tên gọi có giải thích rõ rằng việc đặt tên là một hành vi "áp đặt biểu tượng tạm thời" (temporary symbolic enclosure) và tự phản tư về hành vi này không?  
  *Yêu cầu:* Bổ sung ghi chú phản tư thừa nhận nghịch lý đặt tên ngay trong mục RCA.
- [ ] **Check 2.2 (why.html):** Phần *"Tại sao phải đặt tên"* có thừa nhận tính chất công cụ quy ước (Upāya) để đối phó với đứt gãy thông tin thế hệ, thay vì tuyên xưng một quyền lực định nghĩa tối hậu không?  
  *Yêu cầu:* Điều chỉnh tông giọng từ "định đoạt" sang "công cụ hỗ trợ sinh tồn".

### 🩺 Nhóm 3: Rà soát Hệ tiên đề (axiom_spec.md)
- [ ] **Check 3.1 (axiom_spec.md §0.1):** Ba hệ neo (Phan Ngọc, Ashby, Phật giáo) có làm nổi bật tính vô ngã và khiêm nhường không?  
  *Yêu cầu:* Làm rõ Tiên Đề I (Quan hệ bản thể) là sự phủ định cái tôi trung tâm (vô ngã).
- [ ] **Check 3.2 (axiom_spec.md §2):** Có ghi nhận "Sự khiêm nhường/Ẩn mình" như một invariant vận hành của Tiên Đề II và Mệnh Đề V không?  
  *Yêu cầu:* Bổ sung diễn dịch về cơ chế "ẩn mình để sinh tồn" của người Việt.

### 🩺 Nhóm 4: Rà soát Pháp lý & Bản quyền (LICENSE)
- [ ] **Check 4.1 (LICENSE, index.html):** Giấy phép có đang là `CC BY 4.0` không?  
  *Yêu cầu:* Đề xuất đổi sang `CC0 1.0 Universal` (Public Domain Dedication) để xóa bỏ hoàn toàn quyền sở hữu biểu tượng.

---

## 4. MA TRẬN PHÂN BỔ CÔNG VIỆC (Fix Matrix)

| ID | Điểm phát hiện (Dự kiến) | File ảnh hưởng | Mức độ ưu tiên | Hành động khắc phục |
| :--- | :--- | :--- | :--- | :--- |
| **FIX-01** | Tagline `"Được đặt tên: 2026"` ở Hero | `index.html`<br>`what.html` | **CRITICAL** | Sửa thành: `"Được sống: từ khi có dân tộc Việt. Mô hình hóa: 2026."` |
| **FIX-02** | Mốc timeline `"Mạch Rễ được đặt tên"` | `when.html`<br>`index.html` | **HIGH** | Sửa thành: `"Mô hình Mạch Rễ được hệ thống hóa (v3.2)"` |
| **FIX-03** | Thiếu tuyên bố tự phản tư trong RCA Naming | `what.html` | **HIGH** | Chèn thêm một khối blockquote tự nhận lỗi nhận thức (epistemic enclosure) |
| **FIX-04** | Giấy phép CC BY 4.0 đòi hỏi ghi công | `index.html`<br>`LICENSE` | **HIGH** | Thay đổi toàn bộ khai báo bản quyền sang `CC0 (Public Domain)` |
| **FIX-05** | Đồng nhất "Mạch Rễ" với bản sắc thực | `axiom_spec.md`<br>`what.html` | **MEDIUM** | Hiệu chỉnh định nghĩa: Mạch Rễ là *framework mô tả*, không phải bản thân thực thể văn hóa. |

---

## 5. RISK & DEPENDENCY CHAIN

```
                  ┌────────────────────────────────────────┐
                  │      BẮT ĐẦU: DUYỆT PLAN AUDIT         │
                  └───────────────────┬────────────────────┘
                                      │
                                      ▼
                        ┌──────────────────────────┐
                        │ Phase 1: Rà soát & Sửa   │
                        │ các file HTML chính      │
                        │ (index, what, when, why) │
                        └─────────────┬────────────┘
                                      │
                                      ▼
                        ┌──────────────────────────┐
                        │ Phase 2: Cập nhật        │
                        │ Spec gốc (axiom_spec.md) │
                        └─────────────┬────────────┘
                                      │
                                      ▼
                        ┌──────────────────────────┐
                        │ Phase 3: Thay đổi pháp lý│
                        │ (CC BY 4.0 → CC0)        │
                        └──────────────────────────┘
```

*   **Rủi ro 1: Phản ứng ngược từ các cộng tác viên cũ.** Một số người tham gia xây dựng phiên bản trước có thể không muốn chuyển từ CC BY 4.0 sang CC0 vì muốn giữ quyền ghi danh.  
    *Biện pháp:* Giải thích rõ rằng việc giữ CC BY 4.0 mâu thuẫn trực tiếp với Tiên Đề I (Vô ngã) và Mệnh Đề V (Phân tán) của chính framework.
*   **Rủi ro 2: Làm giảm tính nhận diện thương hiệu của dự án.** Khi tự nhận mình chỉ là "mô hình phân tích tạm thời", dự án có thể giảm đi sức hút truyền thông.  
    *Biện pháp:* Chấp nhận rủi ro này. Sự chính trực về mặt triết học và văn hóa quan trọng hơn sự lan truyền thương hiệu ngắn hạn.

---

## 6. TIÊU CHÍ XÁC NHẬN HOÀN THÀNH (Definition of Done)

Kế hoạch audit này được coi là hoàn thành khi và chỉ khi:
1.  [ ] Không còn bất kỳ câu tagline nào dạng "Được đặt tên: 2026" tồn tại trên website.
2.  [ ] Định nghĩa Mạch Rễ trong tất cả các tài liệu được chuyển đổi nhất quán thành "Mô hình cấu trúc mô tả" (analytical model), không tự nhận là "tên gọi của triết lý dân tộc".
3.  [ ] Tuyên bố phản tư về "Nghịch lý đặt tên" được tích hợp công khai vào tài liệu giới thiệu chính thức ở `what.html`.
4.  [ ] Toàn bộ dự án được xác lập giấy phép CC0 công khai.

---

**PLAN STATUS: DRAFT — AWAITING USER APPROVAL**

> **Phản hồi của bạn:**
> - **"yes" / "execute"** — để tôi bắt đầu tiến hành kiểm định và sửa đổi trực tiếp theo kế hoạch này.
> - **"modify: [chi tiết chỉnh sửa]"** — nếu bạn muốn điều chỉnh bất kỳ mục tiêu hay giải pháp nào trong kế hoạch.

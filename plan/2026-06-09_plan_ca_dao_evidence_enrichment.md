# PLAN — Khai Thác Ca Dao Tục Ngữ Làm Bằng Chứng Cho Mạch Rễ

> **Ngày:** 2026-06-09  
> **Nguồn gốc:** [RCA Ca Dao Tục Ngữ Coverage](file:///C:/Users/PC/.gemini/antigravity-ide/brain/2d7cc985-3474-4277-8e16-b61033391131/rca_ca_dao_tuc_ngu_coverage.md) (cùng ngày)  
> **Nguyên tắc:** KHÔNG mở rộng hệ tiên đề — chỉ làm giàu bằng chứng thực nghiệm (evidence enrichment).  
> **Trạng thái:** CHƯA DUYỆT — chờ go-ahead từ người dùng.

---

## Tổng quan 5 hạng mục (sắp theo ưu tiên)

| # | Hạng mục | Ưu tiên | Loại | Ước lượng |
|---|---|---|---|---|
| **H1** | Ca dao châm biếm → minh họa Tiên Đề VIII (Phản Tư) | 🔴 Cao | Evidence enrichment | 1–2 phiên |
| **H2** | Ca dao thẩm mỹ → evidence bổ trợ Tiên Đề II (Bất Biến Cấu Trúc) | 🟡 Trung bình | Evidence enrichment | 1 phiên |
| **H3** | Kiểm tra ánh xạ Quyển 2 (Gia Đình Quan) + Quyển 3 (Xã Hội Quan) | 🟡 Trung bình | Future RCA | 2–3 phiên |
| **H4** | Ca dao biến dịch → narrative Câu Hỏi Gốc R (convergent discovery) | 🟢 Thấp | Narrative enrichment | 0.5 phiên |
| **H5** | Quyết định: Không mở rộng hệ tiên đề cho nội dung tâm lý cá nhân | — | Ghi nhận | 0 — chỉ ghi nhận |

---

## H1 — Ca Dao Châm Biếm Minh Họa Tiên Đề VIII 🔴 CAO

### Lý do ưu tiên cao
- Tiên Đề VIII (Phản Tư) hiện có triangulation yếu nhất (~2/3), neo A-yếu.
- Ca dao châm biếm Việt Nam là **bằng chứng thực nghiệm mạnh** cho cơ chế phản tư phi-thiết-chế: dân gian tự phê bình qua tiếng cười, không cần cơ quan giám sát.
- Bổ sung vào sẽ **nâng neo A** từ yếu lên trung bình cho VIII.

### Đầu vào
- Thi Ca Bình Dân Q1, phần "CHÂM BIẾM VÀ HÀI HƯỚC" (mục 9 trong Nhân Sinh Quan)
- Tập ca dao châm biếm sưu tập trong kho `documents/public_documents/ca_dao_tuc_ngu_Viet_Nam/`

### Các bước

- [ ] **H1.1** Trích xuất 10–15 câu ca dao châm biếm tiêu biểu từ Q1, phân loại theo đối tượng phê bình:
  - (a) Phê bình giới cầm quyền / quan lại
  - (b) Phê bình nội bộ cộng đồng (lười biếng, dối trá, tham lam)
  - (c) Tự trào (self-deprecation)
- [ ] **H1.2** Phân tích cấu trúc: mỗi câu ca dao châm biếm vận hành Tiên Đề VIII như thế nào?
  - VIII = "Hệ áp chính Tiên Đề I–IV lên bản thân nó"
  - Ca dao châm biếm = hệ tự phát hiện vi phạm pattern (II) và tự phát tín hiệu sửa
- [ ] **H1.3** Viết đoạn phân tích ~500 từ, định dạng phù hợp để bổ sung vào:
  - `axiom_spec.md` → phần Tiên Đề VIII, mục Prior-art hoặc Biện minh quy nạp
  - Hoặc tạo file evidence riêng: `review/evidence_viii_ca_dao_cham_biem.md`
- [ ] **H1.4** Cập nhật triangulation score của VIII nếu evidence đủ mạnh (A-yếu → A-trung bình?)

### Tiêu chí hoàn thành
- Có ≥10 câu ca dao châm biếm được ánh xạ rõ ràng lên cơ chế VIII
- Có đoạn phân tích viết xong, đặt đúng vị trí trong hệ tài liệu
- Triangulation score được đánh giá lại (nâng hoặc giữ nguyên, có lý do)

### Ràng buộc
- KHÔNG thêm tiên đề mới
- KHÔNG sửa phát biểu VIII — chỉ bổ sung evidence/prior-art

---

## H2 — Ca Dao Thẩm Mỹ Bổ Trợ Tiên Đề II 🟡 TRUNG BÌNH

### Lý do ưu tiên trung bình
- Tiên Đề II đã mạnh (4.8/5, triangulation ~2.5/3), evidence hiện tại đã dùng "Bầu ơi thương lấy bí cùng" (paper_005).
- Ca dao thẩm mỹ bổ sung một **chiều evidence mới** (thẩm mỹ vs. đạo đức) nhưng không thay đổi strength rating.

### Đầu vào
- Thi Ca Bình Dân Q1, phần "Ý THỨC VỀ CÁI ĐẸP, CÁI XẤU" (mục 8)

### Các bước

- [ ] **H2.1** Trích xuất 5–8 câu ca dao thẩm mỹ tiêu biểu, phân loại:
  - (a) Đẹp ngoại hình vs. đẹp nội tâm ("cái nết đánh chết cái đẹp")
  - (b) Đẹp tự nhiên vs. đẹp nhân tạo
  - (c) Đẹp cộng đồng vs. đẹp cá nhân
- [ ] **H2.2** Phân tích: quan niệm thẩm mỹ dân gian có phải là **pattern bất biến** (II) hay biến đổi theo thời đại?
  - Nếu bất biến → evidence trực tiếp cho II
  - Nếu biến đổi nội dung nhưng giữ cấu trúc (vd: luôn ưu tiên nội tâm > ngoại hình, dù tiêu chuẩn ngoại hình đổi) → evidence mạnh hơn: chính là minh họa "đổi mà vẫn là mình"
- [ ] **H2.3** Viết đoạn ~300 từ, bổ sung vào:
  - `review/rca_phan_ngoc_trong_mach_re.md` → mục PN_P2_07 (ca dao tục ngữ như carrier)
  - Hoặc paper_005 nếu có bản cập nhật

### Tiêu chí hoàn thành
- Có ≥5 câu ca dao thẩm mỹ phân tích qua lăng kính Tiên Đề II
- Kết luận rõ: pattern thẩm mỹ dân gian là invariant hay không

### Ràng buộc
- Giữ nguyên score II (4.8/5) — chỉ thêm evidence, không sửa phát biểu

---

## H3 — Kiểm Tra Ánh Xạ Quyển 2 & Quyển 3 🟡 TRUNG BÌNH

### Lý do ưu tiên trung bình
- RCA hiện tại chỉ kiểm Q1 (Nhân Sinh Quan). Bộ sách có 3 quyển:
  - Q1: Nhân Sinh Quan (đã kiểm ✅)
  - Q2: Gia Đình Quan (gia đình, hôn nhân, hiếu đạo)
  - Q3: Xã Hội Quan (xã hội, đạo đức, chính trị)
- Q2 có thể chứa evidence mạnh cho Tiên Đề III (Mạch Cội Dọc — trục dọc gia đình)
- Q3 có thể chứa evidence cho Tiên Đề IV (Biên Giới Động — phản ứng xã hội với ngoại lai)

### Đầu vào
- Kiểm tra xem Q2, Q3 có trong thư mục `documents/public_documents/ca_dao_tuc_ngu_Viet_Nam/` không
- Nếu chưa có → tìm nguồn hoặc đánh dấu "pending source"

### Các bước

- [ ] **H3.1** Kiểm tra sự tồn tại của file Q2 và Q3 trong kho tài liệu
- [ ] **H3.2** Nếu có: đọc mục lục, lập bảng ánh xạ chủ đề → tiên đề (giống §3 trong RCA)
- [ ] **H3.3** Nếu chưa có: ghi nhận "pending source" và đề xuất nguồn tìm kiếm
- [ ] **H3.4** Viết RCA bổ sung nếu tìm được vùng mới đáng khai thác

### Tiêu chí hoàn thành
- Biết rõ Q2/Q3 có trong kho hay không
- Nếu có: bảng ánh xạ hoàn chỉnh
- Nếu không: ghi nhận rõ ràng, không block các hạng mục khác

### Ràng buộc
- Đây là RCA tiếp nối, không phải sửa hệ tiên đề

---

## H4 — Ca Dao Biến Dịch Trong Câu Hỏi Gốc R 🟢 THẤP

### Lý do ưu tiên thấp
- Đây là enrichment thuần narrative — không thay đổi logic hay strength của hệ tiên đề
- Giá trị chính: cho thấy dân gian Việt Nam đã "phát hiện" câu hỏi gốc R một cách phi hình thức, hàng trăm năm trước Mạch Rễ

### Đầu vào
- Thi Ca Bình Dân Q1, phần "Ý THỨC THỰC TIỄN TRONG LẼ SỐNG" (mục 13)
- Ca dao biến dịch nổi tiếng: "sông có khúc, người có lúc", "nước chảy đá mòn", "có bột mới gột nên hồ"

### Các bước

- [ ] **H4.1** Trích 5–7 câu ca dao biến dịch, phân loại:
  - (a) Biến dịch tự nhiên (nước chảy, mùa đổi)
  - (b) Biến dịch xã hội (thời thế, vận mệnh)
  - (c) Phản ứng trước biến dịch (nhẫn nại, thích ứng)
- [ ] **H4.2** Viết đoạn ~200 từ, vị trí đề xuất:
  - `axiom_spec.md` → §0 Câu Hỏi Gốc R, ghi chú footnote "convergent discovery"
  - Hoặc `why.html` → phần mở đầu

### Tiêu chí hoàn thành
- Có ≥5 câu ca dao biến dịch với phân tích ngắn
- Gắn được vào narrative mà không làm nặng hệ spec

### Ràng buộc
- Ghi rõ trạng thái `[narrative enrichment]` — KHÔNG phải evidence cấu trúc

---

## H5 — Ghi Nhận: Không Mở Rộng Hệ Tiên Đề Cho Nội Dung Cá Nhân

### Nội dung quyết định
3 chủ đề ca dao thuộc tâm lý cá nhân (hờn dỗi, si mê, biến thái tình yêu) **nằm ngoài** `[GLOBAL SCOPE]` của Mạch Rễ:

> *"hệ bản sắc tập thể (S) thỏa mãn: (i) |S| > một thế hệ; (ii) áp lực đồng hóa: mở, tiến hóa"*

### Ghi nhận

- [x] **H5.1** Xác nhận: tâm lý cá nhân ∉ scope Mạch Rễ → KHÔNG tạo tiên đề mới
- [x] **H5.2** Lý do: khác biệt tầng phân tích (cơ chế tập thể vs. tâm lý cá nhân), tương tự cách Mạch Rễ không hấp thụ Phần 3 Phan Ngọc (thiết kế thể chế vs. cơ chế phi tập trung)
- [x] **H5.3** Ghi nhận trong RCA gốc: đã ghi ✅

### Trạng thái: ĐÃ ĐÓNG — không cần hành động thêm.

---

## Lộ trình đề xuất

```
Tuần 1:  H1 (Cao)  ──→  H5 đã đóng
Tuần 2:  H2 (T.bình) + H4 (Thấp, nhỏ, làm cùng lúc)
Tuần 3+: H3 (T.bình, phụ thuộc nguồn Q2/Q3)
```

---

## Appendix: Liên kết tài liệu

| Tài liệu | Đường dẫn |
|---|---|
| Hệ tiên đề (source of truth) | [axiom_spec.md](file:///c:/Stable_Diffusion/MACH_RE/axiom_spec.md) |
| Thi Ca Bình Dân Q1 | [Thi-CA-Binh-Dan...Q1.txt](file:///c:/Stable_Diffusion/MACH_RE/documents/public_documents/ca_dao_tuc_ngu_Viet_Nam/Thi-CA-Binh-Dan-Việt-Nam-Quyển-1-Nguyễn-Tấn-Long-Phan-Canh.txt) |
| RCA gốc | [rca_ca_dao_tuc_ngu_coverage.md](file:///C:/Users/PC/.gemini/antigravity-ide/brain/2d7cc985-3474-4277-8e16-b61033391131/rca_ca_dao_tuc_ngu_coverage.md) |
| Review Phan Ngọc | [rca_phan_ngoc_trong_mach_re.md](file:///c:/Stable_Diffusion/MACH_RE/review/rca_phan_ngoc_trong_mach_re.md) |
| Paper 005 | [paper_005.md](file:///c:/Stable_Diffusion/MACH_RE/papers/paper_005/paper_005.md) |

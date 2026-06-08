# AUDIT PLAN: Mạch Rễ Framework — Triết Học by Phan Ngọc
<!-- RCA-driven. LLM-friendly. Pure doc. No decoration. -->

## METADATA

```
document_type     : audit_plan
audit_subject     : Mạch Rễ Framework (v2.0, 2026)
audit_lens        : Phan Ngọc "Bản sắc văn hóa Việt Nam" (2000)
audit_scope       : Tầng triết học — không bao gồm thực nghiệm lịch sử, chính sách
rca_method        : 5 Whys + gap analysis + falsification check
author_note       : Xuất từ phiên RCA ngày 2026-06-08
llm_note          : Tài liệu này được cấu trúc để LLM có thể đọc, trích dẫn, và
                    tiếp tục phân tích theo từng section độc lập.
```

---

## MỤC LỤC

1. Mục tiêu audit
2. Phạm vi và giới hạn
3. Nguồn tham chiếu
4. Ma trận audit — Tiên đề vs Phan Ngọc
5. Audit chi tiết — 8 điểm kiểm tra
6. Gap analysis — 3 lỗ hổng triết học
7. Đề xuất bổ sung — 3 tiên đề / mệnh đề mới
8. Điều kiện đóng audit
9. Câu hỏi mở cho vòng audit tiếp theo

---

## 1. MỤC TIÊU AUDIT

```
primary_goal   : Xác định chính xác Mạch Rễ kế thừa gì từ Phan Ngọc,
                 thiếu gì từ Phan Ngọc, và cần bổ sung gì — ở tầng triết học.

secondary_goal : Tạo tài liệu LLM-friendly để các vòng phân tích tiếp theo
                 có thể trích dẫn và mở rộng mà không cần đọc lại toàn bộ
                 tài liệu gốc.

out_of_scope   : Bằng chứng lịch sử thực nghiệm.
                 Chính sách văn hóa.
                 So sánh với Ubuntu, Yoruba, hay các framework bản sắc khác.
                 Đánh giá tính đúng sai của Phan Ngọc.
```

---

## 2. PHẠM VI VÀ GIỚI HẠN

### 2.1 Trong phạm vi audit này

- Hệ 8 tiên đề của Mạch Rễ (I–VII + VIII meta-axiom)
- Ba khái niệm nền tảng Mạch Rễ kế thừa từ Phan Ngọc: kiểu quan hệ, bất biến cấu trúc, hấp thụ có định hướng
- Ba phần của "Bản sắc văn hóa Việt Nam" (Phan Ngọc 2000) theo vai trò triết học

### 2.2 Giới hạn tường minh

```
LIMIT_01 : Audit này không phán xét Phan Ngọc đúng hay sai.
           Nó chỉ hỏi: Mạch Rễ đã hấp thụ đủ chưa?

LIMIT_02 : Mạch Rễ tự xác định là framework triết học mở (CC BY 4.0).
           Audit này tuân theo cùng tinh thần — không phải tấn công,
           mà là peer review có cấu trúc.

LIMIT_03 : Các đề xuất bổ sung ở Section 7 là hypothesis,
           không phải kết luận. Cần vòng kiểm chứng độc lập.
```

---

## 3. NGUỒN THAM CHIẾU

### 3.1 Tài liệu Mạch Rễ (đã đọc trực tiếp)

```
SOURCE_MR_01 : https://aihugart.github.io/Mach-Re/ (index)
SOURCE_MR_02 : https://aihugart.github.io/Mach-Re/what.html
SOURCE_MR_03 : https://aihugart.github.io/Mach-Re/why.html
SOURCE_MR_04 : https://aihugart.github.io/Mach-Re/how.html
SOURCE_MR_05 : https://aihugart.github.io/Mach-Re/who.html
SOURCE_MR_06 : https://aihugart.github.io/Mach-Re/when.html
SOURCE_MR_07 : https://aihugart.github.io/Mach-Re/axioms.html
SOURCE_MR_08 : https://aihugart.github.io/Mach-Re/upgrade.html
SOURCE_MR_09 : https://aihugart.github.io/Mach-Re/papers/paper_005/paper_005.html
```

### 3.2 Tài liệu Phan Ngọc (tham chiếu gián tiếp qua Mạch Rễ + Paper 005)

```
SOURCE_PN_01 : Phan Ngọc (2000). Bản sắc văn hóa Việt Nam. NXB Văn học, Hà Nội.
               Phần 1 — Những khái niệm mở đầu
               Phần 2 — Giao lưu văn hóa
               Phần 3 — Bảo vệ và phát huy văn hóa

NOTE : Audit này đọc Phan Ngọc qua trích dẫn trong Mạch Rễ và Paper 005.
       Vòng audit 2 cần đọc trực tiếp văn bản gốc Phan Ngọc.
```

### 3.3 Khái niệm Phan Ngọc được Mạch Rễ trích dẫn (toàn bộ)

```
CONCEPT_PN_01 : "kiểu quan hệ" — bản sắc = cách tổ chức quan hệ, không phải nội dung
CONCEPT_PN_02 : "kiểu lựa chọn" — mỗi dân tộc có kiểu chọn lọc đặc trưng
CONCEPT_PN_03 : "kiểu cấu trúc hóa thực tại" — cấu trúc bền dưới nội dung đổi
CONCEPT_PN_04 : Quan sát lịch sử: Việt hóa Phật giáo, Nho giáo (dùng làm case study)

NOTE : Bốn khái niệm trên đều từ Phần 1 của Phan Ngọc.
       Phần 2 được dùng làm bằng chứng lịch sử (không phải nguồn lý thuyết).
       Phần 3 VẮNG MẶT HOÀN TOÀN — không một trích dẫn nào.
```

---

## 4. MA TRẬN AUDIT — TIÊN ĐỀ VS PHAN NGỌC

<!-- Đọc cột VERDICT theo scale: PASS / PARTIAL / FAIL / N/A -->
<!-- PASS = Mạch Rễ hấp thụ đủ và đúng từ Phan Ngọc -->
<!-- PARTIAL = Hấp thụ một phần, còn thiếu -->
<!-- FAIL = Không hấp thụ hoặc hấp thụ sai -->
<!-- N/A = Tiên đề không liên quan đến Phan Ngọc -->

| Tiên đề | Tên | Nguồn Phan Ngọc | Verdict | Ghi chú |
|---------|-----|-----------------|---------|---------|
| I | Quan Hệ Bản Thể | CONCEPT_PN_01 (gián tiếp) | PARTIAL | Phan Ngọc quan sát quan hệ trong cộng đồng cụ thể. Mạch Rễ nâng thành bản thể học phổ quát — bước nâng chưa được biện minh đủ. |
| II | Bất Biến Cấu Trúc | CONCEPT_PN_01, PN_02, PN_03 | PARTIAL | Hấp thụ đúng nhân hạt. Bỏ qua phân tầng bất biến theo lĩnh vực mà Phan Ngọc quan sát. |
| III | Mạch Cội Dọc | SOURCE_PN_01 (không có) | N/A | Tự nhận là đóng góp mới của Mạch Rễ. Phan Ngọc không có khái niệm tương đương. Nhưng Phan Ngọc quan sát *bằng chứng* của cơ chế này mà không đặt tên. |
| IV | Biên Giới Động | CONCEPT_PN_02, PN_03 | PARTIAL | Hấp thụ cơ chế chọn lọc từ Phần 2 (Việt hóa). Không hấp thụ tiêu chí phán đoán của Phan Ngọc. |
| V | Phân Tán Bản Thể | SOURCE_PN_01 (không có) | N/A | Đến từ Ashby/Anattā. Phan Ngọc quan sát hiện tượng (1000 năm Bắc thuộc không cần nhà nước) nhưng không lý thuyết hóa. |
| VI | Chuyển Hóa Nhiễu Loạn | CONCEPT_PN_04 (gián tiếp) | PARTIAL | Phan Ngọc có quan sát về hòa giải và hấp thụ. Mạch Rễ formalize nhưng không trích dẫn nguồn Phần 2. |
| VII | Nổi Lên Có Hướng | SOURCE_PN_01 (không có) | N/A | Đến từ Weick/Ashby. |
| VIII | Tự Nhìn Thấy Mình | SOURCE_PN_01 (không có) | N/A | Đến từ Phật giáo. Nhưng Phan Ngọc Phần 3 có nội dung tương tự về tự phê bình văn hóa — không được trích dẫn. |

---

## 5. AUDIT CHI TIẾT — 8 ĐIỂM KIỂM TRA

### CHECK_01 — Traceability: Mạch Rễ có thể truy nguồn mọi claim về Phan Ngọc không?

```
status   : FAIL
evidence : Mạch Rễ trích Phan Ngọc bằng một câu duy nhất trong axioms.html:
           "bản sắc = kiểu quan hệ bền dưới nội dung đổi."
           Không có trang, không có chương, không có đoạn văn cụ thể.
           Paper 005 có thêm: "Phan Ngọc (2000). Bản sắc văn hóa Việt Nam."
           Nhưng không có page reference cho bất kỳ khái niệm cụ thể nào.
problem  : Mạch Rễ tự đặt ra yêu cầu traceability nhưng vi phạm nó với
           chính nguồn neo quan trọng nhất của mình.
action   : Bổ sung page reference cho mọi khái niệm Phan Ngọc được dùng.
```

### CHECK_02 — Formalization step: Bước từ "quan sát mô tả" sang "tiên đề hình thức" có được biện minh không?

```
status   : PARTIAL
evidence : Mạch Rễ tự nhận: "nâng mô tả (Việt) thành nguyên lý cho mọi hệ"
           nhưng không có bước trung gian nào giải thích tại sao quan sát
           của Phan Ngọc (về một dân tộc cụ thể) có thể nâng thành
           nguyên lý phổ quát (áp cho mọi dân tộc).
gap      : Đây là inductive leap — cần ít nhất: (a) kiểm tra với 2-3 dân tộc
           khác, hoặc (b) biện minh triết học tại sao cấu trúc này là
           universal chứ không phải đặc thù Việt Nam.
action   : Thêm mục "Biện minh formalization" vào axioms.html trước khi
           tuyên bố Tiên Đề II là universal.
```

### CHECK_03 — Phần 1 Phan Ngọc: phân biệt văn hóa / văn minh có được hấp thụ không?

```
status   : FAIL
evidence : Không tìm thấy bất kỳ dấu vết nào của phân biệt
           văn hóa (cách tổ chức quan hệ) vs văn minh (thành tựu có thể
           chuyển giao) trong toàn bộ tài liệu Mạch Rễ.
           Đây là nền lý thuyết của Tiên Đề IV (Biên Giới Động)
           nhưng hoàn toàn vắng mặt.
consequence : Tiên Đề IV không có tiêu chí phân biệt cái gì được hấp thụ
              vào lõi vs cái gì chỉ được hấp thụ vào lớp vỏ.
action   : Xem Section 7, Đề xuất 1 (Tiên Đề IIb).
```

### CHECK_04 — Phần 1 Phan Ngọc: phân tầng biểu hiện theo lĩnh vực có được hấp thụ không?

```
status   : FAIL
evidence : Phan Ngọc quan sát kiểu quan hệ biểu hiện khác nhau trong:
           ngôn ngữ, nghệ thuật, tín ngưỡng, tổ chức xã hội, ứng xử.
           Mạch Rễ gộp tất cả thành Identity(S) = Pattern(R(S)) —
           một tầng duy nhất.
consequence : Mạch Rễ không thể phân biệt pattern nào bền hơn pattern nào.
              Diagnosis Rubric (how.html) có 6 chỉ báo nhưng không có
              trọng số phân tầng — mọi chỉ báo đều có giá trị ngang nhau.
action   : Xem Section 7, Đề xuất 1 (Tiên Đề IIb — Phân Tầng Bất Biến).
```

### CHECK_05 — Phần 2 Phan Ngọc: điều kiện đứt gãy có được hấp thụ không?

```
status   : FAIL
evidence : Mạch Rễ chỉ phân tích case study thành công (1000 năm Bắc thuộc,
           500kV, hòa giải Việt-Mỹ). Không có một case study thất bại nào.
           Phần 2 Phan Ngọc có phân tích các trường hợp đứt gãy —
           hoàn toàn không được trích dẫn trong Mạch Rễ.
consequence : Survivorship bias ở tầng lý thuyết.
              Mạch Rễ không thể phân biệt "rễ nông" và "không còn rễ"
              vì không có lý thuyết về điều kiện đứt gãy.
action   : Xem Section 7, Đề xuất 2 (Mệnh đề Điều kiện Đứt gãy).
```

### CHECK_06 — Phần 3 Phan Ngọc: hoàn toàn vắng mặt — có lý do triết học không?

```
status   : UNRESOLVED
evidence : Phần 3 Phan Ngọc bàn về: chính sách văn hóa, vai trò nhà nước,
           xây dựng thiết chế bảo tồn — tức là nội dung quy chuẩn (normative).
           Mạch Rễ có nguyên tắc: "không top-down, không chương trình chính phủ."
possible_reason : Phần 3 mâu thuẫn với nguyên tắc phi tập trung của Mạch Rễ
                  → chủ động loại bỏ.
problem  : Nếu đây là lý do, Mạch Rễ cần nói thẳng. Không nói gì về Phần 3
           trong khi tuyên bố traceability đầy đủ là transparency gap.
           Mỉa mai: đây sẽ là minh họa tốt nhất cho Tiên Đề IV
           (Mạch Rễ hấp thụ có định hướng từ chính Phan Ngọc).
action   : Thêm một đoạn tường minh trong axioms.html hoặc how.html:
           "Chúng tôi không hấp thụ Phần 3 Phan Ngọc vì lý do X."
```

### CHECK_07 — Tiên Đề IV: có tiêu chí phán đoán vận hành không?

```
status   : FAIL
evidence : Tiên Đề IV phát biểu: "nội dung đến được tái tổ chức theo
           logic pattern nội tại."
           Không có tiêu chí nào xác định "logic pattern nội tại" là gì
           trong một tình huống cụ thể.
           Ba câu hỏi thực hành (how.html) — "giữ gì, biến đổi gì, từ chối gì"
           — là hướng dẫn thực hành, không phải tiêu chí triết học.
consequence : Tiên Đề IV là tautology ở dạng hiện tại:
              "biên giới lọc theo pattern" không khác với "biên giới lọc."
action   : Xem Section 7, Đề xuất 3 (Cơ chế Phán đoán cho Tiên Đề IV).
```

### CHECK_08 — Falsification: Mạch Rễ có điều kiện phản chứng đủ mạnh không?

```
status   : PARTIAL
evidence : Mạch Rễ có điều kiện phản chứng toàn hệ (axioms.html):
           "SAI nếu tồn tại một dân tộc sống sót áp lực đồng hóa tương đương
           mà không dùng bất kỳ cơ chế nào trong Tiên Đề I–IV."
           Đây là điều kiện đúng về hình thức.
problem  : "Áp lực đồng hóa tương đương" chưa được định nghĩa đo lường được.
           Ai quyết định áp lực của dân tộc A "tương đương" với áp lực
           mà Việt Nam đã chịu?
           Thiếu metric → điều kiện phản chứng không thể vận hành thực tế.
action   : Bổ sung định nghĩa đo lường được cho "áp lực đồng hóa tương đương."
           Ví dụ: thời gian đô hộ trực tiếp, tỉ lệ dân số bị đồng hóa,
           số thế hệ bị gián đoạn truyền dẫn văn hóa.
```

---

## 6. GAP ANALYSIS — 3 LỖ HỔNG TRIẾT HỌC

<!-- Mỗi gap được định nghĩa bằng: vị trí trong hệ tiên đề, nguồn trong
     Phan Ngọc có thể lấp, và hệ quả nếu không lấp. -->

### GAP_01 — Thiếu phân tầng bất biến

```
location    : Tiên Đề II (Bất Biến Cấu Trúc)
phan_ngoc   : Phần 1 — phân biệt văn hóa / văn minh;
               phân tầng biểu hiện theo lĩnh vực
current_state : Identity(S) = Pattern(R(S)) — một tầng duy nhất
consequence : (a) Không phân biệt được pattern nào là lõi thực sự.
              (b) Diagnosis Rubric không có trọng số phân tầng.
              (c) Tiên Đề IV không có tiêu chí quyết định cái gì
                  được hấp thụ vào tầng nào.
severity    : HIGH — ảnh hưởng đến Tiên Đề II, IV, và Diagnosis Rubric
```

### GAP_02 — Thiếu lý thuyết về điều kiện đứt gãy

```
location    : Giữa Tiên Đề II và Tiên Đề IV (không có mệnh đề nào xử lý)
phan_ngoc   : Phần 2 — các trường hợp Việt hóa thất bại, đứt gãy văn hóa
current_state : Mạch Rễ chỉ có lý thuyết về thành công.
               Diagnosis Rubric có thang điểm "rễ nông" nhưng không có
               ngưỡng "không còn rễ" và không có lý thuyết tại sao
               vượt ngưỡng đó thì đứt gãy xảy ra.
consequence : (a) Survivorship bias baked into framework.
              (b) Không thể phân biệt "rễ nông đang phục hồi" với
                  "rễ đã đứt không còn phục hồi được."
              (c) Điều kiện phản chứng toàn hệ không thể vận hành.
severity    : HIGH — ảnh hưởng đến tính falsifiable của toàn framework
```

### GAP_03 — Tiên Đề IV thiếu cơ chế phán đoán vận hành

```
location    : Tiên Đề IV (Biên Giới Động)
phan_ngoc   : Phần 1 + 2 — tiêu chí thực tiễn: "nuôi được quan hệ cộng
               đồng không?" là bộ lọc quan sát được trong lịch sử Việt Nam
current_state : "tái tổ chức theo logic pattern nội tại" —
               mô tả kết quả, không mô tả tiêu chí quyết định.
consequence : (a) Tiên Đề IV là tautology.
              (b) Ba câu hỏi thực hành (giữ, biến đổi, từ chối) không có
                  căn cứ triết học để trả lời.
              (c) Không thể áp dụng Mạch Rễ vào tình huống mới mà không
                  có hướng dẫn cụ thể hơn.
severity    : MEDIUM — ảnh hưởng đến khả năng áp dụng thực tế
```

---

## 7. ĐỀ XUẤT BỔ SUNG — 3 TIÊN ĐỀ / MỆNH ĐỀ MỚI

<!-- Status: HYPOTHESIS. Cần vòng kiểm chứng độc lập. -->
<!-- Mỗi đề xuất: phát biểu chính thức + sơ đồ + điều kiện phản chứng -->

### PROPOSAL_01 — Tiên Đề IIb: Phân Tầng Bất Biến (Stratified Invariance)

```
closes_gap   : GAP_01
source       : Phan Ngọc Phần 1 — phân biệt văn hóa/văn minh +
               phân tầng biểu hiện theo lĩnh vực
```

**Phát biểu:**

> Bất biến cấu trúc không phải một tầng duy nhất mà có độ sâu.
> Tầng sâu hơn bền hơn và thay đổi chậm hơn.
> Hấp thụ có định hướng (Tiên Đề IV) vận hành khác nhau ở mỗi tầng —
> cái được phép thay đổi ở tầng nông có thể không được phép thay đổi
> ở tầng sâu.

**Cấu trúc phân tầng:**

```
TẦNG 1 — LÕI KIỂU QUAN HỆ
  Định nghĩa : Cách tổ chức quan hệ người↔người, người↔tổ tiên
  Bền vững   : Cực cao — thay đổi chậm nhất
  Nguồn      : Phan Ngọc, "văn hóa" theo nghĩa hẹp
  Ví dụ      : Quan hệ trực tiếp người sống↔người đã khuất (thờ cúng tổ tiên)

TẦNG 2 — CẤU TRÚC XÃ HỘI
  Định nghĩa : Hình thức tổ chức cụ thể của Tầng 1
  Bền vững   : Cao — thay đổi theo thế kỷ
  Nguồn      : Phan Ngọc, tổ chức làng xã
  Ví dụ      : Hội đồng làng, dòng họ, gia đình ba thế hệ

TẦNG 3 — BIỂU HIỆN LĨNH VỰC
  Định nghĩa : Cách Tầng 1 biểu hiện trong từng lĩnh vực cụ thể
  Bền vững   : Trung bình — thay đổi theo thập kỷ
  Nguồn      : Phan Ngọc, phân tích lĩnh vực
  Ví dụ      : Ngôn ngữ, nghi lễ, thẩm mỹ, ứng xử đạo đức

TẦNG 4 — NỘI DUNG CỤ THỂ
  Định nghĩa : Thành tựu vật chất và kỹ thuật có thể chuyển giao
  Bền vững   : Thấp — thay đổi tự do nhất
  Nguồn      : Phan Ngọc, "văn minh" theo nghĩa hẹp
  Ví dụ      : Từ vay mượn, công nghệ, phong tục sinh hoạt
```

**Hệ quả cho Tiên Đề IV:**

```
Nội dung đến → Xác định tầng tác động → Áp dụng bộ lọc tương ứng
                     │
           ┌─────────┼─────────┐
        Tầng 1    Tầng 2-3   Tầng 4
        Lọc rất    Lọc        Hấp thụ
        nghiêm     vừa        tự do
```

**Điều kiện phản chứng:**

```
SAI nếu: tồn tại dân tộc trong đó Tầng 4 (nội dung) thay đổi
          ảnh hưởng trực tiếp đến Tầng 1 (lõi kiểu quan hệ)
          mà không qua Tầng 2-3 làm trung gian.
```

---

### PROPOSAL_02 — Mệnh đề F: Điều Kiện Đứt Gãy (Failure Conditions)

```
closes_gap   : GAP_02
source       : Phan Ngọc Phần 2 — các trường hợp đứt gãy văn hóa
derived_from : Tiên Đề II (Bất Biến) + Tiên Đề III (Mạch Cội Dọc)
               + Tiên Đề IV (Biên Giới Động)
type         : Derived proposition — không phải tiên đề độc lập
```

**Phát biểu:**

> Bất biến cấu trúc bị phá vỡ khi đồng thời xảy ra ba điều kiện:
> (A) Tầng 1 (lõi kiểu quan hệ) bị tấn công trực tiếp, không phải chỉ tầng nội dung;
> (B) Mạch cội dọc (Tiên Đề III) bị cắt đứt vật lý — thế hệ không còn
>     tiếp xúc với thế hệ trước đủ để truyền pattern;
> (C) Tốc độ thay đổi vượt qua ngưỡng tái cấu trúc của biên giới (Tiên Đề IV).

**Sơ đồ:**

```
ĐỨT GÃY xảy ra khi:

Điều kiện A        Điều kiện B        Điều kiện C
Tầng 1 bị tấn  AND Trục V bị cắt AND Tốc độ > ngưỡng
công trực tiếp      (thế hệ đứt)       tái cấu trúc
      │                  │                   │
      └──────────────────┴───────────────────┘
                         │
              [tất cả 3 điều kiện cùng lúc]
                         │
              Bất biến không còn tái tạo được
                         │
                   ĐỨT GÃY THỰC SỰ
                   (≠ biến đổi bình thường)

BIẾN ĐỔI BÌNH THƯỜNG xảy ra khi:
  Chỉ Điều kiện C xảy ra (tốc độ cao)
  nhưng A và B không xảy ra → hệ tái tạo được pattern.
```

**Hệ quả cho Diagnosis Rubric:**

```
Thêm ngưỡng "Đứt gãy" vào Diagnosis Rubric (how.html):

  0 điểm    : RỄ ĐÃ ĐỨT — cả 3 điều kiện F đều đã xảy ra
               → không còn khả năng tự phục hồi nội tại
  1-4 điểm  : RỄ NÔNG TRẦM TRỌNG — nguy cơ đứt gãy
  5-8 điểm  : RỄ ĐANG NÔNG (giữ nguyên theo Mạch Rễ hiện tại)
  9-10 điểm : RỄ ĐANG PHÁT TRIỂN (giữ nguyên)
  11-12 điểm: RỄ SÂU (giữ nguyên)
```

**Điều kiện phản chứng:**

```
SAI nếu: tồn tại cộng đồng đã trải qua cả 3 điều kiện A+B+C
          nhưng bất biến cấu trúc vẫn tái tạo được sau đó.
```

---

### PROPOSAL_03 — Bổ sung vào Tiên Đề IV: Cơ Chế Phán Đoán (Judgment Mechanism)

```
closes_gap   : GAP_03
source       : Phan Ngọc Phần 1+2 — tiêu chí thực tiễn quan sát được
               trong lịch sử Việt hóa: "nuôi được quan hệ cộng đồng không?"
type         : Amendment to existing axiom — không phải tiên đề mới
```

**Phát biểu bổ sung vào Tiên Đề IV:**

> Biên giới động vận hành qua một tiêu chí phán đoán thực tiễn có thể
> quan sát được: nội dung đến được hấp thụ nếu và chỉ nếu nó có thể
> được tích hợp vào cấu trúc quan hệ hiện có (Tầng 1-2 theo IIb)
> mà không phá vỡ lõi kiểu quan hệ.
> Tiêu chí này không phải quyết định ý thức của cá nhân —
> mà là bộ lọc vận hành ở tầng cộng đồng qua thời gian dài.

**Sơ đồ cơ chế phán đoán:**

```
Nội dung đến
      │
      ▼
[Câu hỏi thực tiễn]
"Cái này có thể sống trong
cấu trúc quan hệ của chúng ta
mà không phá vỡ Tầng 1 không?"
      │
 ┌────┴────┐
 CÓ       KHÔNG
 │         │
 ▼         ▼
Hấp thụ  Loại bỏ hoặc
+ tái    trung lập hóa
cấu      (không đưa vào lõi)
trúc
theo IIb
```

**Mối quan hệ với ba câu hỏi thực hành hiện tại của Mạch Rễ:**

```
Câu hỏi hiện tại (how.html)    Nền triết học được bổ sung
"Giữ lại gì?"               → Cái tích hợp được vào Tầng 1-2
"Biến đổi thành gì?"        → Cái tích hợp được vào Tầng 3-4 sau tái cấu trúc
"Từ chối gì?"               → Cái không tích hợp được vào bất kỳ tầng nào
                               mà không phá vỡ Tầng 1
```

**Điều kiện phản chứng:**

```
SAI nếu: tồn tại trường hợp hấp thụ thành công trong đó
          nội dung tích hợp vào lõi (Tầng 1) và phá vỡ cấu trúc
          quan hệ cũ mà bản sắc vẫn sống sót.
```

---

## 8. ĐIỀU KIỆN ĐÓNG AUDIT

<!-- Audit này được coi là "đóng" khi Mạch Rễ team xử lý các action items.
     Mỗi action item có priority và dependency. -->

| ID | Action Item | Priority | Depends on | Closes |
|----|-------------|----------|------------|--------|
| A01 | Thêm page reference cho mọi trích dẫn Phan Ngọc | HIGH | — | CHECK_01 |
| A02 | Thêm mục "Biện minh formalization" cho Tiên Đề II | HIGH | — | CHECK_02 |
| A03 | Tường minh hóa lý do không hấp thụ Phần 3 Phan Ngọc | MEDIUM | — | CHECK_06 |
| A04 | Bổ sung metric cho "áp lực đồng hóa tương đương" | HIGH | — | CHECK_08 |
| A05 | Draft Tiên Đề IIb (Stratified Invariance) | HIGH | A01, A02 | GAP_01 |
| A06 | Draft Mệnh đề F (Failure Conditions) | HIGH | A05 | GAP_02 |
| A07 | Draft Amendment cho Tiên Đề IV (Judgment Mechanism) | MEDIUM | A05 | GAP_03 |
| A08 | Cập nhật Diagnosis Rubric với ngưỡng "Đứt gãy" | MEDIUM | A06 | GAP_02 |
| A09 | Peer review độc lập cho A05, A06, A07 | HIGH | A05-A07 | toàn bộ |

**Audit được coi là đóng khi:** A01–A04 hoàn thành (minimum) + A09 có ít nhất
một reviewer độc lập không thuộc nhóm tác giả Mạch Rễ.

---

## 9. CÂU HỎI MỞ CHO VÒNG AUDIT TIẾP THEO

<!-- Những câu hỏi này không có câu trả lời trong vòng audit hiện tại.
     LLM hoặc researcher đọc tài liệu này nên dùng chúng làm điểm vào. -->

```
Q01 : Phan Ngọc định nghĩa "văn hóa" và "văn minh" chính xác như thế nào
      trong văn bản gốc? Audit hiện tại đọc qua trích dẫn gián tiếp.
      Cần đọc Phần 1 trực tiếp để xác nhận.

Q02 : Phan Ngọc có ví dụ nào về đứt gãy văn hóa thất bại không?
      Hay Phần 2 chỉ phân tích thành công? Câu hỏi này quyết định
      độ tin cậy của PROPOSAL_02.

Q03 : Tiêu chí phán đoán "nuôi được quan hệ cộng đồng không?" —
      đây là diễn giải của audit này từ quan sát Phan Ngọc,
      hay Phan Ngọc phát biểu tường minh tiêu chí này?
      Cần kiểm tra văn bản gốc.

Q04 : Phần 3 Phan Ngọc đề xuất gì cụ thể? Có mâu thuẫn thực sự với
      nguyên tắc phi tập trung của Mạch Rễ không, hay chỉ là bề mặt?
      Câu hỏi này quyết định xem CHECK_06 có verdict FAIL hay PASS.

Q05 : Lévi-Strauss — được Mạch Rễ liệt kê cùng Phan Ngọc trong prior-art
      của Tiên Đề II — có phân tầng bất biến tương tự PROPOSAL_01 không?
      Nếu có, PROPOSAL_01 không phải đề xuất mới mà là kế thừa bỏ sót.

Q06 : Tiên Đề IIb (Stratified Invariance) có xuất hiện dưới dạng khác
      trong Ashby's Requisite Variety không? Nếu có, neo triangulation
      của nó mạnh hơn nhiều.
```

---

## APPENDIX — SƠ ĐỒ TỔNG HỢP

```
PHAN NGỌC "Bản sắc văn hóa Việt Nam" (2000)
│
├── PHẦN 1 — Lý thuyết
│   ├── Khái niệm văn hóa / văn minh ──────────────── FAIL (A03) → PROPOSAL_01
│   ├── Kiểu quan hệ / kiểu lựa chọn ──────────────── PARTIAL → Tiên Đề II (thiếu tầng)
│   └── Phân tầng biểu hiện theo lĩnh vực ──────────── FAIL → PROPOSAL_01
│
├── PHẦN 2 — Giao lưu văn hóa
│   ├── Việt hóa thành công (case studies) ─────────── PARTIAL (dùng làm bằng chứng)
│   ├── Điều kiện đứt gãy ───────────────────────────── FAIL → PROPOSAL_02
│   └── Tiêu chí phán đoán thực tiễn ───────────────── FAIL → PROPOSAL_03
│
└── PHẦN 3 — Bảo vệ và phát huy
    └── Toàn bộ ─────────────────────────────────────── UNRESOLVED → Q04

MẠCH RỄ (2026)
│
├── Tiên Đề I-IV (Core) — PARTIAL from Phần 1+2
├── Tiên Đề V-VII (Derived) — N/A (Ashby/Anattā)
├── Tiên Đề VIII (Meta) — N/A (Phật giáo)
│
├── GAP_01 (thiếu phân tầng) → PROPOSAL_01 (Tiên Đề IIb)
├── GAP_02 (thiếu điều kiện đứt gãy) → PROPOSAL_02 (Mệnh đề F)
└── GAP_03 (thiếu tiêu chí phán đoán) → PROPOSAL_03 (Amendment IV)
```

---

*Tài liệu này là hypothesis, không phải kết luận.*
*Mọi đề xuất cần vòng kiểm chứng độc lập (A09) trước khi tích hợp vào Mạch Rễ.*
*Phiên bản: 1.0 — 2026-06-08*
*Phương pháp: RCA 5 Whys + gap analysis + falsification check*
*Scope: Tầng triết học — không bao gồm thực nghiệm lịch sử, chính sách*

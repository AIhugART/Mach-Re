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

## 8. Tiên Đề III — Hai tầng khái niệm (bản chất vs biểu hiện)

> RCA finding 2026-06-05 — Điểm 5/5. Bắt buộc áp dụng trong mọi phát biểu và so sánh liên quan đến Tiên Đề III.

| Tầng | Thuật ngữ | Dùng khi nào |
|---|---|---|
| **Bản chất** (Essence) | **Orthogonal Temporality** — Thời gian trực giao | Phát biểu nguyên lý bản thể học; phân biệt Tiên Đề III với Halbwachs/Luhmann |
| **Biểu hiện** (Manifestation) | **Vertical Temporality** — mạch cội dọc | Mô tả thực hành văn hóa; sơ đồ trực quan; so sánh ba nền văn hóa |

**Quy tắc:** Hai thuật ngữ **không** thay thế nhau — chúng khác tầng (essence ≠ manifestation).
- ❌ Cấm: "Orthogonal Temporality tức là Vertical Temporality"
- ✅ Đúng: "Tiên Đề III có bản chất là Orthogonal Temporality, biểu hiện trong đời sống qua cấu trúc Vertical Temporality"

**Gốc rễ của quy tắc:** Nếu chỉ dùng "Vertical Temporality," không thể phân biệt Tiên Đề III với "past là input của present operations" (Luhmann) — vì cả hai đều có hướng "dọc" về quá khứ. Chỉ tính **trực giao** (V không rút gọn về H) mới là ranh giới falsifiable.

---

## 9. Bảng Tên Canonical — Tên Thuần Việt Các Tiên Đề & Mệnh Đề

> **[CHỐT CANONICAL 2026-06-11 · Quyết định 4 — ký pháp phân tầng theo `raw/axiom-chart.html`]** (thay chốt 2026-06-06 "La Mã đếm liên tục theo tầng"). Đã đồng bộ với `axiom_spec.md` §5.2. Quy tắc: **số La Mã CHỈ dành cho Tiên Đề** (đơn vị độc lập, không suy ra được); **Mệnh Đề Dẫn Xuất đánh số La tinh 1–4**; cấp dưới nữa không đánh số phân cấp. **Dãy tiên đề I–VI liên tục:** I–IV (Core) → V = Meta (trước: VIII) → VI = Interface (trước: IX). Số La Mã cũ của Mệnh Đề (V/VI/VII) **đã được dồn lại** — đây là upāya tốt hơn cho người mới tiếp cận.
> Quy tắc dùng: format đầy đủ = `Tiên Đề [La Mã] — [Biểu hiện] — [Bản chất] ("EN")` · `Mệnh Đề [1–4] — [Biểu hiện] — [Bản chất] ("EN")`.
> Khi không gian hạn chế (menu, breadcrumb) → chỉ dùng `Tiên Đề [số] — [Biểu hiện]` / `Mệnh Đề [số] — [Biểu hiện]`.

**Tiên Đề (Axioms — số La Mã):**

| # | Biểu hiện (thuần Việt) | Bản chất (thuần Việt) | Thuật ngữ kỹ thuật (EN) | Điểm | Tầng |
|---|---|---|---|---|---|
| I | Sống Trong Quan Hệ | Có Nhau Mới Có Mình | Relational Ontology | 4.8 | Core |
| II | Nếp Bản Sắc | Đổi Mà Vẫn Là Mình | Structural Invariant | 4.8 | Core |
| III | Mạch Cội Dọc | Mạch Cội Nguồn | Vertical / Orthogonal Temporality | 4.8 | Core |
| IV | Ranh Giới Mềm | Đóng Mở Có Chọn | Dynamic Boundaries | 5.0 | Core |
| V | Tự Nhìn Thấy Mình | Soi Mình Mà Không Vỡ | Reflexive Cognition (Meta-Axiom) | 5.0 | Meta |
| VI | Gặp Nhau Giữ Gốc | Không Của Ai, Nhờ Cả Hai | Living Interface | 4.8 | Interface |

**Mệnh Đề Dẫn Xuất (Derived Propositions — số La tinh; suy ra từ các Tiên Đề Core):**

| # | (trước 2026-06-11) | Biểu hiện (thuần Việt) | Bản chất (thuần Việt) | Thuật ngữ kỹ thuật (EN) | Điểm | Suy từ |
|---|---|---|---|---|---|---|
| 1 | Mệnh Đề V | Giữ Mà Không Gom | Ai Cũng Giữ Một Phần | Distributed Storage | 5.0 | I+II |
| 2 | Mệnh Đề VI | Hóa Nhiễu Thành Sức | Đau Được Xử Là Đau Lành | Perturbation Transformation | 4.8 | II+III+IV |
| 3 | Mệnh Đề VII | Nổi Lên Có Hướng | Hợp Lại Thành Cái Mới | Directed Emergence | 5.0 | I+II+III+IV |
| 4 | Mệnh Đề F | Đứt Khi Hết Cội | — (ký hiệu cấu trúc `F` giữ nguyên) | Failure Conditions | 5.0 | II+III+IV |

**Neo quan trọng (I):** Với Tiên Đề I, Biểu hiện ("Sống Trong Quan Hệ") và Bản chất ("Có Nhau Mới Có Mình") gần nghĩa một cách có chủ đích — không phải lỗi thiết kế. Bản thân nội dung ontological của Tiên Đề I (identity IS relations) làm collapse khoảng cách essence-manifestation: nếu bản sắc được cấu thành bởi quan hệ, thì "sống trong quan hệ" (cách nó hiện ra trong đời sống) và "có nhau mới có mình" (cấu trúc nền) là hai mặt của cùng một thực tại. Phân biệt gắt gao Biểu hiện/Bản chất là thiết yếu cho Tiên Đề III (ngăn category collapse với Halbwachs/Luhmann), nhưng với Tiên Đề I, sự gần nghĩa là hệ quả logic của chính nội dung tiên đề, không phải khiếm khuyết cần sửa. RCA 2026-06-09 — xem CHANGELOG.md A12.

**Neo quan trọng (III):** "Cội Nguồn" = tên thuần Việt cho bản chất *cảm xúc-bản sắc* của Tiên Đề III.
KHÔNG đồng nghĩa với "Orthogonal/trực giao" (thuật ngữ cấu trúc). Hai tầng khác nhau: essence ≠ manifestation.
Xem chi tiết: §8 của file này và CLAUDE.md §Core Principles.

**Neo quan trọng (IX):** Biểu hiện "Gặp Nhau Giữ Gốc" = tầng saṃvṛti (quy ước): cái thấy được khi IX vận hành — hai hệ tiếp xúc, mỗi hệ giữ nguyên gốc rễ hệ đơn đầy đủ I–V (điều kiện C1). Bản chất "Không Của Ai, Nhờ Cả Hai" = tầng paramārtha (chân lý tối hậu): cấu trúc P* — đồng sinh (pratītyasamutpāda) từ cả hai, không quy thuộc về ai (anattā của P*). Tương phản có chủ đích với Mệnh Đề 1: "Ai Cũng Giữ Một Phần" (phân tán quyền sở hữu *trong* hệ) ↔ "Không Của Ai" (không quyền sở hữu P* *giữa* hai hệ). Tầng "Interface" = tầng thứ tư mới — đòi hỏi hai hệ hoàn chỉnh (I–V) mỗi bên. Cặp tiếng Anh gợi hình (rule P2 — bilingual symmetry): Manifestation "Mine, Yours, and the Space Between"; Essence "Owned by Neither, Born of Both". Phase 1b · RCA 4.8/5 · La bàn C (Phật giáo nhận thức luận) · 2026-06-11.

---

## 7. Carry-Forward Set mặc định (rebuild governance)

> **Vai trò mới (2026-06-06 · P1 của `mach-re-axiom-rebuild-plan.md`).** Thay cho "Điều KHÔNG đụng".
> Theo quy tắc CLAUDE.md "rebuild with carry-forward": đây là danh sách tài sản *được phép mang sang* khi re-derive hệ tiên đề. Mục **PHƯƠNG PHÁP** giữ vô điều kiện (là công cụ suy). Mục **NỘI DUNG** là *ứng viên* phải sống sót cổng RCA (≥4/5) trong P2; ngoài danh sách → bỏ (reference-only).
> Cổng quyết định P1: 3-round RCA × 5-Why × ≥4/5 → TB **4.6/5 → PROCEED**.

### 7.1 Ba hệ quy chiếu neo (triangulation backbone cho P2)
> Re-derivation suy trên ba hệ **độc lập**. Một candidate axiom **mạnh hơn** nếu nó hiện ra (gần khớp *cấu trúc* theo §2 — ẩn dụ đắt, KHÔNG phải đồng nhất) trong ≥2/3 hệ. Đây là phép chống tùy tiện, KHÔNG phải bằng chứng.

| Hệ | Nguồn | Neo cấu trúc cho |
|---|---|---|
| **A** | Phan Ngọc — *Bản sắc văn hóa Việt Nam*: bản sắc = "kiểu lựa chọn / kiểu quan hệ" bền dưới nội dung đổi | bất biến cấu trúc; quan hệ làm nền |
| **B** | Ashby (*Requisite Variety*) + Weick (*organizing / sensemaking / enactment / retrospect*) | biên giới động & xử lý nhiễu; bản sắc duy trì qua vận hành; chiều hồi cố |
| **C** | Anattā / Pratītyasamutpāda / Śūnyatā (nhận thức luận Phật giáo) | vô ngã = quan hệ bản thể (không "svabhāva"); phân tán không trung tâm; phản tư / tánh không của lõi |

⚠️ **Confirmation bias (P2.3):** ba hệ này từng sinh ra hệ tiên đề cũ → dễ vô thức lái re-derivation về kết quả cũ. Bắt buộc chạy independence test *bằng văn bản*.

### 7.2 PHƯƠNG PHÁP — giữ vô điều kiện
- Cổng RCA: 3-round × 5-Why × ≥4/5.
- §1–§6 của file này (chống tuyệt đối · ẩn dụ≠sự thật · minh họa≠chứng minh · công thức giả→sơ đồ · bỏ tự-chấm-điểm · quy trình P1–P5).
- **Cơ chế tự phê bình + tiêu chí phản chứng** — chuẩn để soi chính các tiên đề mới.
- La bàn nhận thức luận Phật giáo (Upāya, Śūnyatā, Nhị đế, Tứ cú, Pramāṇa) — dùng để suy, không phải kết luận.

### 7.3 NỘI DUNG — ứng viên, phải sống sót re-derivation (P2)
| Ứng viên | Điều kiện sống sót |
|---|---|
| Câu hỏi gốc: *vì sao một số hệ bản sắc tập thể sống sót đồng hóa, số khác không?* | Giữ làm điểm xuất phát (không cần chứng minh) |
| Ý lõi: **bản sắc bền nhờ hấp thụ có định hướng, không nhờ dựng tường** | Re-test: tiên đề, hệ quả, hay minh họa? |
| Từ vựng: "rễ nông", "trí nhớ sống / trí nhớ chết", quan hệ dọc vs ngang | Giữ nếu khái niệm tương ứng tái xuất hiện |
| Hai tầng IV: essence (Orthogonal) vs manifestation (Vertical) | Chỉ giữ nếu "thời gian" tái xuất hiện như tiên đề độc lập |
| "Hấp thụ có định hướng" như cơ chế thứ ba (giữa assimilation ↔ isolation) | Re-test phân loại đóng góp (Synthesis/Extension/Novel) |
| Prior-art catalog (Whitehead, Heidegger, Gadamer, Lévi-Strauss…) | Gắn vào tiên đề mới ở P3 (bổ sung ngoài 3 hệ neo) |

### 7.4 BỎ → reference-only (KHÔNG carry-forward)
- Tập 7/8 tiên đề + **số La Mã I–V** như định danh ràng buộc.
- Nhãn "4 Core + 3 Derived" + đoạn tự-mổ-xẻ "7 thực ra cần 4" (chỉ còn là provenance lịch sử).
- Bảng tên canonical §9 như *ràng buộc* (xem trạng thái mới ở §9).

### 7.5 Tầng trình bày — theo vế "đã xuất bản vẫn extend"
- Câu manifesto ở **hero/mở đầu** (vd "Được sống... đặt tên 2026") và mô tả *ý định thiết kế* ("đủ chính xác để đối thoại", "giải quyết một hạn chế") — KHÔNG bị rebuild đụng; đây là tầng trình bày đã công bố, không phải nội dung tiên đề.

---

## 10. Trường ngữ nghĩa "nếp" — Từ vựng triết học thuần Việt (RCA 2026-06-09)

> RCA finding: 3-round × 5-Why × scoring gate → **5.0/5.** Đây là proof-of-concept cho sứ mệnh Việt hóa của Mạch Rễ: xây dựng từ vựng triết học bằng tiếng Việt bản địa, không Hán-Việt, không dịch từ Anh/Pháp.

### 10.1 Sứ mệnh

Khung nền triết học Mạch Rễ cố gắng xây dựng một bộ từ vựng triết học **bằng tiếng Việt bản địa**. Đây là yêu cầu cấu trúc, không phải thẩm mỹ: nếu dùng từ Hán-Việt hoặc từ dịch, framework sẽ mượn luôn hệ quy chiếu triết học của ngôn ngữ nguồn và mất đi tính nguyên bản của góc nhìn.

### 10.2 "Nếp" — khái niệm nguyên tử (atomic concept)

**"Nếp"** là đơn vị cấu trúc sống cơ bản của toàn bộ Việt hóa Mạch Rễ. Nó thuộc phạm trù **cấu trúc sống** (living structure), phân biệt với phạm trù **quy ước xã hội** (social convention).

| Phạm trù | Định nghĩa | Ví dụ | Mất đi thì |
|---|---|---|---|
| **Cấu trúc sống** (nếp) | Điều kiện cần cho tồn tại của hệ thống — structural necessity | nếp thờ tổ tiên, nếp vai vế trên-dưới | Hệ thống **sụp đổ** (mất bản sắc) |
| **Quy ước xã hội** (tập quán, tập tục) | Thói quen tập thể có thể đàm phán, biến đổi — social convention | tập quán ăn trầu, tập tục cúng đình | Hệ thống thay đổi hình thức, không sụp |

### 10.3 Bảng trường ngữ nghĩa "nếp" (canonical)

| # | Thuật ngữ thuần Việt | EN mapping | Vị trí trong framework | Ghi chú |
|---|---|---|---|---|
| 1 | **nếp** (gốc) | living pattern (atomic) | Khái niệm nguyên tử | Không đứng một mình trong phát biểu — luôn đi với từ ghép |
| 2 | **nếp tổ chức** | Configuration | Tiên Đề III — đơn vị được truyền qua mạch cội dọc | Thay cho "cấu hình" (quá kỹ thuật) và "thực thể" (quá vật lý) |
| 3 | **nếp bản sắc** | Structural Invariant | Tiên Đề II — nếp không đổi xuyên thời gian | "Bản sắc" = cái riêng không thể trộn lẫn |
| 4 | **nếp sống** | Living pattern | Mô tả thực hành hằng ngày | Biểu hiện quan sát được của nếp tổ chức |
| 5 | **nề nếp** | Inherited Patterns | Tiên Đề III — nếp được kế thừa qua V | "Nề" = nếp đã thành khuôn phép, ổn định |
| 6 | **Mạch Cội Nguồn** | Orthogonal Temporality | Tiên Đề III — bản chất | "Cội" (dọc) ⊥ "Nguồn" (ngang) — hai chiều trực giao |

### 10.4 Quy tắc chọn từ canonical (thứ tự ưu tiên)

| Ưu tiên | Loại từ | Hành động | Ví dụ |
|---|---|---|---|
| **1** | Thuần Việt có sẵn, đúng phạm trù | Chọn làm canonical | "nếp" cho structural pattern |
| **2** | Thuần Việt chưa có, ghép được | Ghép từ gốc thuần Việt | "nếp tổ chức" = nếp + tổ chức |
| **3** | Không có thuần Việt tương đương | Giữ EN, ghi rõ "chưa Việt hóa" | "autopoiesis" (tạm thời) |
| **4** | Hán-Việt đã thành khẩu ngữ | Dùng kèm thuần Việt gloss | "bản thể học" — luôn kèm "mạch tồn tại" |

**Canonical glosses đã xác lập (Rule 4):**
| Hán-Việt | Thuần Việt gloss | Trạng thái |
|---|---|---|
| bản thể học | mạch tồn tại | ✅ canonical (CLAUDE.md) |
| nhận thức luận | mạch biết | ✅ canonical (Phase 8c naming RCA 2026-06-11, la bàn Phan Ngọc, 4.8/5) |
| ngữ pháp siêu việt | nếp coi là chung | ✅ canonical (Phase 8c naming RCA 2026-06-11, la bàn Phan Ngọc, 4.8/5) |

### 10.5 Ranh giới phạm trù: "nếp" ≠ "tập quán" / "tập tục"

Đây là kết quả RCA của câu hỏi: *có nên thay "nề nếp" bằng "tập tục" hoặc "tập quán" trong phát biểu chính thức Tiếng Việt không?*

**Kết luận: KHÔNG. Điểm: 0.0/5 (scoring gate — giữ nguyên "nề nếp").**

| ❌ Đề xuất bị bác | Lý do bác | Hệ quả nếu làm |
|---|---|---|
| "nề nếp" → "tập quán" | "tập quán" ∈ social convention, không phải structural pattern | Tiên Đề III từ ontological → sociological |
| "nề nếp" → "tập tục" | "tập tục" còn hẹp hơn "tập quán" (nghiêng về lễ nghi cổ truyền) | Không phủ được "inherited patterns" (gồm cả nếp sống hằng ngày không mang tính nghi lễ) |
| Giữ "nề nếp" nhưng xóa gloss | Gloss "tập quán" giúp người đọc định vị — không phải synonym | Giữ nguyên hiện trạng: canonical = "nề nếp", gloss = "tập quán văn hóa" (có ghi chú phân biệt) |

**5-Why gốc rễ (tóm tắt):**

1. Tại sao muốn thay? → "nề nếp" ít phổ biến hơn "tập quán" trong khẩu ngữ.
2. Tại sao đó là vấn đề? → Framework nhắm đến accessibility (Việt hóa bản sắc).
3. Tại sao không nên thay? → "Nếp" là atomic concept — "nếp tổ chức", "nếp bản sắc", "nếp sống", "nề nếp" cùng họ. Thay "nề nếp" → "tập quán" làm sụp toàn bộ trường ngữ nghĩa.
4. Tại sao giữ trường ngữ nghĩa quan trọng hơn dùng từ phổ thông? → Vì Mạch Rễ đang **xây dựng** từ vựng triết học, không phải **mượn** từ vựng có sẵn. Nếu chỉ dùng từ phổ thông, framework không có gì mới về mặt khái niệm.
5. **Root (1 câu):** "tập tục"/"tập quán" ∈ quy ước xã hội (có thể đàm phán); "nếp" ∈ cấu trúc sống (mất → sụp). Dùng sai phạm trù = kéo ontological claim xuống sociological description.

### 10.6 Liên kết với các phần khác

- **CLAUDE.md §Core Principles → Sứ mệnh Việt hóa:** quy tắc chọn từ canonical + bảng trường ngữ nghĩa "nếp" (bản rút gọn).
- **`axiom_3.html` dòng 237:** canonical term "nề nếp" trong phát biểu chính thức Tiếng Việt.
- **`axiom_3.html` dòng 1328:** glossary — "tập quán văn hóa" là explanatory gloss, không phải synonym. **Cần làm sắc nét ghi chú** (TODO: thêm câu phân biệt gloss ≠ canonical term).
- **`axiom_spec.md`:** định nghĩa formal của "Inherited Patterns" — canonical EN term, mapping sang "nề nếp".

---

## 11. Quan hệ model-of, taxonomy 3 vai, phát hiện về đối tượng, provenance rules (RCA findings 2026-06-12, F2–F9)

> **Score gate:** F2 = 4.8/5 · F3 = 4.8/5 · F5 = 4.8/5 · F6 = 4.8/5 · F9 = 4.8/5. Canonical record: `review/2026-06-12_tuyen_bo_rca_verdict.md`. Áp dụng bắt buộc khi viết về vị trí của Mạch Rễ trong triết học, khi so sánh với các hệ khác, và khi phát biểu tên loại hình.

### 11.1 Quan hệ model-of + bất đối xứng phụ thuộc (F2+F3)

**Quy tắc:** Mạch Rễ là *model-of* triết học dân tộc Việt — không phải triết học đó, không phải phái sinh của nó, không phải definition của nó.

| Cách diễn đạt | Trạng thái | Lý do |
|---|---|---|
| "Mạch Rễ mô tả triết học dân tộc Việt" | ✅ | model-of — đúng quan hệ |
| "Mạch Rễ là triết học dân tộc Việt" | ❌ | identity claim — sai quan hệ |
| "Mạch Rễ phái sinh từ Nho/Phật/Lão" | ❌ | sai tầng — A×B×C là vật liệu, không phải nội dung |
| "Mạch Rễ được xây từ triết học dân tộc Việt" | ❌ ambiguous | dùng "làm mô hình về" thay vì "xây từ" |

**Tiêu chí vận hành — bất đối xứng phụ thuộc (F3):**
Kiểm tra: *Nếu hủy toàn bộ Mạch Rễ, đối tượng có tồn tại không?*
- Đúng: CÓ — triết học dân tộc Việt tồn tại trong thực hành cộng đồng độc lập với model.
- Nếu KHÔNG → framework đang tuyên bố identity → overclaim → phải sửa.

**Analogy chuẩn (F2):** Chữ Nôm làm bằng bộ chữ Hán để ghi âm tiếng Việt mà không biến tiếng Việt thành tiếng Hán. Mạch Rễ làm bằng A×B×C để mô hình hóa triết học dân tộc Việt mà không biến triết học đó thành triết học phương Tây hay Phật giáo Ấn Độ.

### 11.2 Taxonomy 3 vai — Thấu kính / Gương soi / Tia chuẩn (F5+F6)

**Quy tắc:** Ba vai này không thể hoán đổi. Trước khi so sánh Mạch Rễ với bất kỳ hệ triết học nào, xác định vai của hệ đó trước.

| Vai | EN | Ứng viên | Chức năng | Lý do không hoán đổi |
|---|---|---|---|---|
| **Thấu kính** (lens) | analytical tool | A, B, C | Nhìn *qua* — hình thức hóa, bác bỏ | Tháo → model sập. Giống đối tượng = khuyết điểm |
| **Gương soi** (mirror) | comparison frame | Ubuntu, Yoruba | Soi *cạnh* — đo phân kỳ | Không cấu thành tiên đề |
| **Tia chuẩn** (reference beam) | historical substrate | Nho/Phật/Lão nguồn | Chiếu *vào* — đo delta khúc xạ | Output của bộ lọc → không thể là thấu kính |

**Quy tắc chẩn đoán vai:**
1. Hệ đó giúp *phân tích cấu trúc* hay *được phân tích*? → Phân tích = thấu kính; được phân tích = tia chuẩn
2. Hệ đó *giống đối tượng* hay *khác*? → Giống = gương soi; khác + có formalisms = thấu kính
3. Hệ đó là *cơ chế* hay *sản phẩm của cơ chế*? → Sản phẩm = tia chuẩn

### 11.3 Cái-chọn ≠ Cái-được-chọn (F6 — phân biệt canonical)

**Tam giáo đồng nguyên** = cái *được chọn* — output của bộ lọc văn hóa Việt qua nhiều thế hệ.
**Mạch Rễ** = mô hình hóa cơ chế *chọn lọc* — bộ lọc, không phải sản phẩm.

Dùng Tam giáo để giải thích Mạch Rễ = dùng sản phẩm để giải thích bộ chọn → vòng tròn nhận thức luận. Không cho phép trong phát biểu chính thức.

### 11.4 Phát hiện về đối tượng: "Bản thể luận Dị-Tương-Thuộc" (F4)

**Trạng thái:** Finding *về đối tượng* (triết học dân tộc Việt) — không phải tiên đề của Mạch Rễ, không vào canonical terminology của framework.

**Nội dung:** Đối tượng được mô hình hóa có thể thuộc loại hình "Dị-Tương-Thuộc" — nơi các thực thể *khác biệt* (Dị) cùng tồn tại trong mối quan hệ *tương hỗ* (Tương) mà không tan chảy vào nhau (Thuộc = tương thuộc, không hòa tan). Đây là *mô tả của model về đối tượng*, chưa phải tuyên bố cấu trúc đã kiểm chứng.

**Quy tắc sử dụng:**
- Phát biểu nội bộ: có thể dùng như hypothesis về đặc trưng của đối tượng
- Phát biểu formal/paper: phải đánh `[hypothesis]` và trace về ngữ liệu Việt cụ thể
- Không đưa vào tên tiên đề, không dùng như nhãn canonical

### 11.5 Provenance tag rules (F9)

**Quy tắc:** Mọi tên loại hình / taxonomy / lịch sử so sánh mới phát biểu trong Mạch Rễ phải mang một trong hai tag:
- `[established]` + source APA: claim có nguồn học thuật xác định
- `[proposed-by-this-project]`: tên/taxonomy coined trong quá trình phát triển Mạch Rễ

**Bảng tên loại hình (canonical provenance table):**

| Tên | Provenance tag | Source |
|---|---|---|
| "Triết học Tương quan-Phân tán / Relational and Distributed Philosophy" | `[proposed-by-this-project]` | Coined trong dự án Mạch Rễ, 2026 |
| relational ontology | `[established]` | Whitehead, Emirbayer (1997), Dewey & Bentley |
| distributed cognition / epistemology | `[established]` | Hutchins (1995) *Cognition in the Wild* |
| Orthogonal Temporality (V ⊥ H) | `[proposed-by-this-project]` | Tiên Đề III Mạch Rễ — chưa peer review |

**Kill condition:** Nếu literature review tìm thấy tên compound "Relational and Distributed Philosophy" đã tồn tại trước trong học thuật → tag thay đổi về `[established]` và kill condition #4 (axiom_spec.md §0.6) bị xóa.

---

## 12. Phản biện canonical: "Triết học Việt Nam như rễ chùm vay mượn" (F7, RCA 2026-06-12)

> **Score gate:** Claim phản biện bị bác = 1.6/5 (dưới ngưỡng). Counter-argument = 4.6/5 (trên ngưỡng). Giữ counter.

**Nhận định bị bác:** *"Triết học Việt Nam giống rễ chùm — vay mượn nhiều hướng, không sâu như rễ cọc, mục tiêu chỉ để bám đất mà sống chứ không vươn lên lớn mạnh."*

**Phân tích F7 — 3-round RCA:**
- **Round 1:** Nhận định này dùng rễ cọc như chuẩn ngầm — triết học "thật" = phải như rễ cọc (sâu, thẳng, tập trung). Triết học Việt = rễ chùm = thấp hơn.
- **Round 2:** Lỗi phạm trù thứ hai: rễ cọc và rễ chùm là hai *kiến trúc khác nhau với chức năng khác nhau*, không phải cùng loại ở mức độ phát triển khác nhau.
- **Round 3 — Root:** Ẩn dụ gán giá trị (cọc tốt hơn chùm) vào đặc trưng cấu trúc khác nhau. Rễ chùm không phải rễ cọc thất bại — nó là kiến trúc tối ưu cho môi trường khác.

**Counter-argument (4.6/5):**
Rễ chùm là kiến trúc tối ưu cho *môi trường áp lực cao, đa hướng* — chính xác là môi trường lịch sử Việt Nam. Rễ cọc thất bại khi bị tấn công trực diện vào trung tâm. Rễ chùm không thất bại khi bị cắt một nhánh — mạng lưới còn lại tiếp tục giữ. Đây là Mệnh Đề 1 (lưu trữ phân tán) hoạt động ở tầng sinh học.

**Câu chốt canonical:** *"Số 0 của dụng cụ rễ cọc không có nghĩa là đối tượng không tồn tại — chỉ có nghĩa là dụng cụ sai."*

**Quy tắc sử dụng:**
- Khi gặp nhận định "rễ chùm vay mượn": phân tích morphology error trước khi đáp lại về nội dung
- Không nói "rễ chùm kém hơn" hay "tốt hơn" rễ cọc — hai kiến trúc cho hai môi trường

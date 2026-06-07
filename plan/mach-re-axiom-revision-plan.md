# Mạch Rễ — Kế Hoạch Chỉnh Sửa Học Thuật: Hệ Tiên Đề

> **Mục đích tài liệu:** Đề xuất chỉnh sửa có căn cứ cho kiến trúc tiên đề của Mạch Rễ v2.0, nhằm tăng tính chặt chẽ học thuật mà không làm mất giá trị thực hành.
> **Phiên bản gốc:** what.html — Mạch Rễ v2.0
> **Định dạng:** LLM-friendly Markdown (tiêu đề phân cấp rõ, mỗi section độc lập, không phụ thuộc context trước đó)

---

## MỤC LỤC

1. [Chẩn Đoán Vấn Đề](#1-chẩn-đoán-vấn-đề)
2. [Kiến Trúc Đề Xuất: 4 Tiên Đề + 3 Mệnh Đề Dẫn Xuất](#2-kiến-trúc-đề-xuất)
3. [Chỉnh Sửa Từng Tiên Đề](#3-chỉnh-sửa-từng-tiên-đề)
4. [Xử Lý Claim "Đóng Góp Nguyên Bản"](#4-xử-lý-claim-đóng-góp-nguyên-bản)
5. [Chỉnh Sửa Công Thức Ký Hiệu](#5-chỉnh-sửa-công-thức-ký-hiệu)
6. [Bảng Đối Chiếu Trước / Sau](#6-bảng-đối-chiếu-trước--sau)
7. [Checklist Triển Khai](#7-checklist-triển-khai)
8. [Những Gì KHÔNG Nên Thay Đổi](#8-những-gì-không-nên-thay-đổi)

---

## 1. CHẨN ĐOÁN VẤN ĐỀ

### 1.1 Danh Sách Lỗi Theo Mức Độ Nghiêm Trọng

| Mức | Loại Lỗi | Vị Trí | Mô Tả |
|-----|----------|--------|-------|
| 🔴 CRITICAL | Mâu thuẫn nội bộ | Bảng 7 tiên đề + Phần "Quan Hệ 3 và 7" | Tài liệu tự kết luận III, VI, VII là hệ quả nhưng vẫn gọi chúng là "tiên đề" |
| 🔴 CRITICAL | Vi phạm định nghĩa | Bảng kiểm tra "Axiom thật sự" | III được đánh ✅ "Độc lập" nhưng ngay sau đó thừa nhận có thể suy ra từ I+II |
| 🟡 MAJOR | Overclaim | Tiên Đề IV | "Không có triết học nào trước đây phát biểu mạch cội dọc như chiều kích bản thể học" — cần bằng chứng so sánh |
| 🟡 MAJOR | Nhầm lẫn thể loại | Công thức toán học | Notation triết học được trình bày như toán học hình thức, không có định lý kiểm chứng được |
| 🟢 MINOR | Thiếu trích dẫn | Tiên Đề I | Relational Ontology đã có trong Whitehead, Buttimer — cần acknowledge |
| 🟢 MINOR | Thiếu trích dẫn | Tiên Đề II | Structural invariant gần với Phan Ngọc + Group Theory — cần link rõ hơn |

### 1.2 Nguyên Nhân Gốc Rễ (RCA)

**Why 1:** Tại sao có mâu thuẫn nội bộ?
→ Tài liệu ưu tiên "7" vì dễ đọc và đầy đủ hơn cho người dùng thông thường.

**Why 2:** Tại sao điều đó tạo ra vấn đề?
→ Vì tài liệu đồng thời claim tính học thuật nghiêm túc ("hệ tiên đề thỏa mãn 5 tiêu chí").

**Why 3:** Tại sao không tách hai mục đích?
→ Chưa có cấu trúc hai tầng rõ ràng: tầng học thuật và tầng thực hành.

**Gốc rễ:** Mạch Rễ chưa phân biệt rõ **Axiom System** (cho học giả) và **Expanded Framework** (cho người dùng thông thường). Giải pháp không phải chọn một — mà là tách rõ cả hai.

---

## 2. KIẾN TRÚC ĐỀ XUẤT

### 2.1 Cấu Trúc Hai Tầng

```
TẦNG HỌC THUẬT (Academic Layer)
├── 4 Core Axioms (tiên đề thực sự độc lập)
│   ├── A1: Relational Ontology
│   ├── A2: Structural Invariance
│   ├── A4: Vertical Temporality
│   └── A5: Dynamic Boundary
└── 3 Derived Propositions (mệnh đề dẫn xuất, không phải tiên đề)
    ├── P3: Distributed Ontology [từ A1 + A2]
    ├── P6: Perturbation Transformation [từ A4 + A5]
    └── P7: Directed Emergence [từ A1 + A2 + A4 + A5]

TẦNG THỰC HÀNH (Practitioner Layer)
└── 7 Nguyên Lý Mạch Rễ (không gọi là "tiên đề")
    = 4 Core Axioms + 3 Derived Propositions
    = đúng nội dung, đúng thứ tự, sai tên gọi → sửa tên gọi
```

### 2.2 Tại Sao 4, Không Phải 3 Hay 5?

**Thử với 3 (I, II, IV):**
- Thiếu cơ chế tương tác với môi trường bên ngoài
- Không suy ra được cách hệ thống hấp thụ nhiễu loạn
- → Chưa đủ

**Thử với 4 (I, II, IV, V — thêm Biên Giới Động):**
- I + II: định nghĩa *cái gì* là bản sắc
- IV: định nghĩa *chiều thời gian* của bản sắc
- V: định nghĩa *cơ chế tương tác* với môi trường
- → Đủ để dẫn xuất III, VI, VII
- → **Đây là minimum viable axiom set**

**Thử với 5 (thêm III):**
- III có thể suy ra từ I+II (distributed storage là hệ quả của relational ontology + structural invariance)
- → Dư một cái, không tối giản

**Kết luận: 4 là số axiom tối ưu.**

### 2.3 Sơ Đồ Dẫn Xuất

```
A1 (Quan Hệ Bản Thể)
    │
    ├──→ A2 (Bất Biến Cấu Trúc) ──→ P3 (Phân Tán Bản Thể)
    │         │                              │
    │         │                              │
    │    A4 (Mạch Cội Dọc)                  │
    │         │                              │
    │    A5 (Biên Giới Động) ───────────→ P6 (Chuyển Hóa Nhiễu Loạn)
    │         │                              │
    └─────────┴──────────────────────────→ P7 (Nổi Lên Có Hướng)
```

---

## 3. CHỈNH SỬA TỪNG TIÊN ĐỀ

### 3.1 Tiên Đề I — Quan Hệ Bản Thể (GIỮ NGUYÊN, thêm context)

**Trạng thái:** ✅ Giữ làm Core Axiom A1

**Thay đổi cần thiết:**

❌ **Bỏ dòng này** (hoặc điều chỉnh):
> "Phân biệt: Descartes — Ngã có trước, quan hệ sau"

✅ **Thêm vào** — acknowledge prior art:
```markdown
**Vị trí trong triết học hiện có:**
- Whitehead (Process Philosophy): thực thể là "occasions of experience" trong quan hệ
- Buttimer (Relational Geography): nơi chốn được định nghĩa qua quan hệ
- Anattā (Phật giáo): vô ngã — không có thực thể độc lập với quan hệ

**Đóng góp của Mạch Rễ tại A1:**
Không phải phát minh Relational Ontology, mà là **ứng dụng vào hệ thống bản sắc tập thể xuyên thế hệ** — phạm vi chưa được các framework trên đề cập đầy đủ.
```

---

### 3.2 Tiên Đề II — Bất Biến Cấu Trúc (GIỮ NGUYÊN, thêm context)

**Trạng thái:** ✅ Giữ làm Core Axiom A2

**Thay đổi cần thiết:**

✅ **Thêm vào** — acknowledge và phân biệt:
```markdown
**Liên quan đến:**
- Phan Ngọc: "kiểu quan hệ" là cái bền vững trong văn hóa Việt
- Group Theory: invariant dưới phép biến đổi
- Structural Anthropology (Lévi-Strauss): deep structure vs surface content

**Đóng góp của Mạch Rễ tại A2:**
Phan Ngọc mô tả hiện tượng. A2 phát biểu nó thành nguyên lý có thể áp dụng cho bất kỳ hệ thống bản sắc nào — không riêng Việt Nam.
```

---

### 3.3 Tiên Đề III — Phân Tán Bản Thể (CHUYỂN THÀNH MỆNH ĐỀ DẪN XUẤT)

**Trạng thái:** ⚠️ Chuyển từ Axiom → Derived Proposition P3

**Lý do:**
P3 có thể được dẫn xuất từ A1 + A2:
- A1: bản sắc tồn tại *trong* mạng quan hệ, không phải *tại* một node
- A2: invariant là *pattern* của quan hệ, không phải nội dung tại một điểm
- → Nếu invariant là pattern phân tán, không thể lưu tập trung → P3

**Phiên bản chỉnh sửa:**
```markdown
### P3 — Mệnh Đề Phân Tán (Derived Proposition, từ A1 + A2)

> **Hệ quả trực tiếp của A1 và A2:** Nếu bản sắc là pattern của mạng quan hệ (A1 + A2),
> thì nó không thể được lưu giữ tại bất kỳ node đơn lẻ nào. Tập trung hóa invariant
> là điều kiện đủ để tạo single point of failure.

*Đây không phải tiên đề độc lập — đây là hệ quả logic của A1 và A2.*
```

---

### 3.4 Tiên Đề IV — Mạch Cội Dọc (GIỮ, điều chỉnh claim)

**Trạng thái:** ✅ Giữ làm Core Axiom A4 — nhưng **phải sửa claim**

**Thay đổi bắt buộc:**

❌ **Xóa dòng này:**
> "Không có triết học nào trước đây phát biểu mạch cội dọc như một chiều kích bản thể học."

✅ **Thay bằng:**
```markdown
**Prior art cần acknowledge:**
- Heidegger (*Geschichtlichkeit*): tồn tại là tồn tại-trong-lịch-sử, quá khứ hiện diện
  cấu thành hiện tại
- Gadamer (*Wirkungsgeschichte*): lịch sử tác động — ta không thể đứng ngoài truyền thống
  để hiểu nó
- Burke: "partnership between the dead, the living, and the unborn"
- Pratītyasamutpāda: tương thuộc nhân quả xuyên thời gian

**Đóng góp thực sự của A4 (cần diễn đạt lại):**
Các triết học trên nói đến ảnh hưởng của quá khứ lên hiện tại.
A4 phát biểu mạch cội dọc như **điều kiện tồn tại của bản sắc hệ thống** —
không chỉ điều kiện nhận thức. Cụ thể hơn: *chiều sâu của V (vertical time)
tỉ lệ thuận với khả năng phục hồi của hệ thống sau nhiễu loạn.*

Đây là đóng góp ứng dụng, không phải phát minh ontological từ đầu.
```

---

### 3.5 Tiên Đề V — Biên Giới Động (GIỮ NGUYÊN)

**Trạng thái:** ✅ Giữ làm Core Axiom A5

**Thay đổi nhỏ — thêm:**
```markdown
**Liên quan đến:**
- Ashby's Law of Requisite Variety: hệ thống cần đủ variety để xử lý variety của môi trường
- Membrane biology: selective permeability — không phải ẩn dụ, là cơ chế tương đồng

**Phân biệt với Ashby:**
Ashby nói về variety tổng quát. A5 đặc tả cơ chế *restructuring* — nội dung đến được
tái tổ chức theo logic của pattern nội tại, không phải logic của nội dung đến.
```

---

### 3.6 Tiên Đề VI — Chuyển Hóa Nhiễu Loạn (CHUYỂN THÀNH MỆNH ĐỀ DẪN XUẤT)

**Trạng thái:** ⚠️ Chuyển từ Axiom → Derived Proposition P6

**Lý do:**
P6 = A4 (vertical time depth cho ngữ cảnh) + A5 (dynamic boundary cho cơ chế xử lý):
- Perturbation đến qua boundary A5
- Được xử lý trong ngữ cảnh mạch cội dọc A4
- → ΔVariety > 0 nếu boundary hoạt động đúng

**Phiên bản chỉnh sửa:**
```markdown
### P6 — Mệnh Đề Chuyển Hóa (Derived Proposition, từ A4 + A5)

> **Hệ quả của A4 và A5:** Perturbation đi qua biên giới động (A5) và được xử lý
> trong ngữ cảnh mạch cội dọc (A4) → trở thành thông tin cấu trúc làm tăng variety.
> Perturbation bị đóng băng = biên giới thất bại (κ→0) hoặc thiếu chiều sâu dọc (V=∅).

**Hàm ý thực hành (quan trọng):**
P6 không nói "đau khổ là tốt." P6 nói: đau khổ *có thể* được chuyển hóa nếu
có đủ biên giới (A5) và chiều sâu dọc (A4). Hòa giải là nhu cầu cấu trúc,
không phải lựa chọn đạo đức.
```

---

### 3.7 Tiên Đề VII — Nổi Lên Có Hướng (CHUYỂN THÀNH MỆNH ĐỀ DẪN XUẤT)

**Trạng thái:** ⚠️ Chuyển từ Axiom → Derived Proposition P7

**Lý do:**
P7 là synthesis của toàn bộ A1–A5 (qua P3, P6). Nó không thêm giả định mới — nó mô tả trạng thái nổi lên khi cả 4 axiom hoạt động đầy đủ.

**Phiên bản chỉnh sửa:**
```markdown
### P7 — Mệnh Đề Nổi Lên (Derived Proposition, từ A1 + A2 + A4 + A5)

> **Synthesis:** Khi A1–A5 đồng thời hoạt động, trật tự nổi lên theo hướng —
> không ngẫu nhiên, không từ trung tâm. Field F được tạo ra bởi toàn bộ
> mạng quan hệ, hướng nổi lên là gradient của Field đó.

**Liên quan đến:**
- Complexity Theory: self-organization, emergence
- Attractor basins (Dynamical Systems): hệ thống "biết đường về" sau perturbation

**Đây là mệnh đề tổng hợp quan trọng nhất của Mạch Rễ** — nhưng nó là
kết luận, không phải tiên đề. Gọi nó là tiên đề làm yếu, không làm mạnh,
vì tiên đề không cần chứng minh còn mệnh đề này *được chứng minh* từ A1–A5.
```

---

## 4. XỬ LÝ CLAIM "ĐÓNG GÓP NGUYÊN BẢN"

### 4.1 Phân Loại Lại Đóng Góp

Thay vì claim tất cả đều "nguyên bản," phân loại rõ 3 mức:

```markdown
## Phân Loại Đóng Góp của Mạch Rễ

### Mức 1 — Synthesis (Tổng hợp từ các nguồn hiện có)
- A1 (Relational Ontology): synthesis từ Whitehead + Anattā + Phan Ngọc
- A2 (Structural Invariance): synthesis từ Phan Ngọc + Group Theory

**Giá trị:** Đặt tên chung, tạo ngôn ngữ thống nhất, áp dụng vào domain mới

### Mức 2 — Extension (Mở rộng có hướng)
- A4 (Vertical Temporality): extend Heidegger/Gadamer vào hệ thống bản sắc tập thể
- A5 (Dynamic Boundary): extend Ashby vào cơ chế identity preservation cụ thể

**Giá trị:** Lấp khoảng trống giữa các lý thuyết hiện có, tạo cầu nối

### Mức 3 — Novel (Thực sự mới)
- Formalization của "hấp thụ có định hướng" như cơ chế identity preservation
  (phân biệt với cả assimilation lẫn isolation — không có framework nào trước đây
  phát biểu cơ chế này như một nguyên lý riêng)
- Kết hợp vertical time + dynamic boundary thành một hệ thống coherent giải thích
  tại sao một số dân tộc survive đồng hóa còn các dân tộc khác không

**Giá trị:** Đây là đóng góp học thuật thực sự — cần làm nổi bật hơn
```

### 4.2 Tái Viết Claim Chính

❌ **Phiên bản gốc:**
> "Tiên Đề IV (Mạch Cội Dọc) và VII (Nổi Lên Có Hướng) là hai điểm Mạch Rễ đóng góp nguyên bản vào triết học."

✅ **Phiên bản đề xuất:**
```markdown
**Đóng góp học thuật của Mạch Rễ:**

1. **Formalization:** Chuyển các pattern sinh tồn quan sát được trong lịch sử Việt
   thành hệ nguyên lý có thể áp dụng và kiểm tra với các dân tộc khác.

2. **Tích hợp:** Kết nối Relational Ontology + Structural Invariance + Vertical
   Temporality + Dynamic Boundary thành một hệ thống coherent — các framework
   trước đây chỉ có từng phần riêng lẻ.

3. **Nguyên bản (Novel):** Nguyên lý "hấp thụ có định hướng" (Directed Absorption)
   như cơ chế thứ ba giữa assimilation và isolation — chưa được phát biểu như
   một nguyên lý độc lập trong bất kỳ framework bản sắc nào hiện có.
```

---

## 5. CHỈNH SỬA CÔNG THỨC KÝ HIỆU

### 5.1 Vấn Đề Hiện Tại

Công thức như `∀x: Being(x) ≡ {R(x,y) | y ∈ Universe}` gây nhầm lẫn vì:
- Trông như First-Order Logic nhưng không có axiom schema đầy đủ
- Trông như Set Theory nhưng không có ZFC foundation
- Không có định lý nào được *chứng minh* từ các công thức này

### 5.2 Đề Xuất: Phân Loại Rõ Notation

Thêm disclaimer vào đầu phần công thức:

```markdown
> **Ghi chú về ký hiệu:** Các công thức dưới đây là *structural notation* —
> ngôn ngữ ký hiệu triết học để tư duy rõ hơn, không phải toán học hình thức
> (formal mathematics) với đầy đủ axiom schema và proof calculus.
> Mạch Rễ không claim tính toán học — claim tính triết học có cấu trúc.
```

### 5.3 Công Thức Nên Giữ vs Nên Điều Chỉnh

| Công thức | Đánh giá | Hành động |
|-----------|----------|-----------|
| `∀x: Being(x) ≡ {R(x,y) \| y ∈ Universe}` | Ổn nếu có disclaimer | Giữ + thêm disclaimer |
| `Identity(S) = Pattern(R(S))` | Rất rõ, đẹp | Giữ nguyên |
| `Resilience(S) = f(depth(V))` | Ổn — functional relationship | Giữ, note f chưa defined |
| `Direction(agent_i) = ∇F(position_i)` | Overclaim — gradient của gì? | Thay bằng: "agent định hướng theo field F do toàn mạng tạo ra" |

---

## 6. BẢNG ĐỐI CHIẾU TRƯỚC / SAU

| # | Tên gốc | Loại gốc | Loại đề xuất | Thay đổi |
|---|---------|----------|--------------|----------|
| I | Quan Hệ Bản Thể | Axiom | **Core Axiom A1** | Thêm prior art (Whitehead, Anattā) |
| II | Bất Biến Cấu Trúc | Axiom | **Core Axiom A2** | Thêm prior art (Phan Ngọc, Lévi-Strauss) |
| III | Phân Tán Bản Thể | Axiom | **Derived Proposition P3** | Chuyển loại, thêm derivation từ A1+A2 |
| IV | Mạch Cội Dọc | Axiom | **Core Axiom A4** | Xóa overclaim, thêm prior art, phát biểu lại đóng góp thực |
| V | Biên Giới Động | Axiom | **Core Axiom A5** | Thêm link với Ashby, phân biệt rõ hơn |
| VI | Chuyển Hóa Nhiễu Loạn | Axiom | **Derived Proposition P6** | Chuyển loại, thêm derivation từ A4+A5 |
| VII | Nổi Lên Có Hướng | Axiom | **Derived Proposition P7** | Chuyển loại, thêm derivation từ A1+A2+A4+A5 |

### Phát biểu lại tiêu đề chính

❌ **Phiên bản gốc:**
> "Bảy Tiên Đề (Axioms) Của Mạch Rễ — mỗi tiên đề thỏa mãn 5 tiêu chí: Độc lập, Nhất quán, Phủ đầy, Tối giản, Thuộc bản thể học"

✅ **Phiên bản đề xuất:**
> "Hệ Nguyên Lý Mạch Rễ: 4 Tiên Đề Cốt Lõi và 3 Mệnh Đề Dẫn Xuất
> — 4 Core Axioms đáp ứng đầy đủ tiêu chí Độc lập, Nhất quán, Tối giản, và Thuộc bản thể học.
> — 3 Derived Propositions được suy ra logic từ các tiên đề cốt lõi, phát biểu rõ ràng vì tầm quan trọng thực hành."

---

## 7. CHECKLIST TRIỂN KHAI

### Ưu Tiên Cao (làm trước)

- [ ] **Đổi tiêu đề** phần 7 tiên đề → "4 Core Axioms + 3 Derived Propositions"
- [ ] **Sửa bảng kiểm tra "Axiom thật sự"** — III, VI, VII không được ✅ "Độc lập"
- [ ] **Xóa dòng overclaim** về Tiên Đề IV ("không có triết học nào trước đây...")
- [ ] **Thêm disclaimer** vào đầu phần công thức ký hiệu

### Ưu Tiên Trung Bình (làm sau)

- [ ] **Thêm prior art** cho A1 (Whitehead, Buttimer) và A2 (Phan Ngọc, Lévi-Strauss)
- [ ] **Viết lại section "Đóng Góp Nguyên Bản"** theo 3 mức: Synthesis / Extension / Novel
- [ ] **Thêm derivation proof** cho P3, P6, P7 (ngắn gọn, vài dòng logic)
- [ ] **Điều chỉnh công thức** `∇F` → ngôn ngữ mô tả

### Ưu Tiên Thấp (tùy chọn)

- [ ] Thêm mục "Falsification per Axiom" — mỗi core axiom bị bác bỏ bởi điều kiện gì cụ thể
- [ ] Thêm bảng so sánh với Ubuntu, Yoruba, Baltic (đã có trong who.html) — link cross-reference
- [ ] Xem xét thêm Tiên Đề VIII (từ upgrade.html) vào kiến trúc chính thức

---

## 8. NHỮNG GÌ KHÔNG NÊN THAY ĐỔI

Phần này quan trọng không kém phần chỉnh sửa.

| Phần | Lý do giữ nguyên |
|------|-----------------|
| **RCA tên gọi (5 Whys cho "Mạch Rễ")** | Logic chặt, đây là phần tốt nhất tài liệu |
| **5 khái niệm nền tảng** (Lõi, Rễ, Hấp thụ có định hướng, Rễ nông, Trí nhớ sống) | Thực dụng, rõ ràng, không claim gì sai |
| **Falsification conditions** | Hiếm có trong framework dân tộc, cần giữ và làm nổi bật hơn |
| **Isomorphism 3 hệ thống** (Phan Ngọc + Ashby + Anattā) | Ý tưởng tốt, chỉ cần đào sâu hơn |
| **Giới Hạn Tự Nhận (4 limits)** | Đây là dấu hiệu tư duy trưởng thành — không thay đổi |
| **Cấu trúc tên "Mạch Rễ"** | Phân tích âm thanh và ý nghĩa hoàn toàn đúng |
| **Bảng đối chiếu triết lý toàn cầu** | Đặt vị trí đúng, câu hỏi cốt lõi chính xác |

---

## PHỤ LỤC — TEMPLATE PHÁT BIỂU LẠI TIÊN ĐỀ

Template LLM-friendly để phát biểu lại từng axiom theo chuẩn học thuật:

```markdown
### [A/P][số] — [Tên] ([Core Axiom / Derived Proposition])

**Loại:** Core Axiom | Derived Proposition
**Nguồn gốc (nếu là Derived):** Từ [A? + A?]

**Phát biểu:**
> [Nội dung tiên đề hoặc mệnh đề]

**Prior Art (acknowledge):**
- [Tên tác giả/trường phái]: [điểm tương đồng]
- [Tên tác giả/trường phái]: [điểm tương đồng]

**Phân biệt với Prior Art:**
[Mạch Rễ khác ở điểm nào — cụ thể, không chung chung]

**Hàm ý thực hành:**
[1-2 câu về ứng dụng thực tế]

**Điều kiện bác bỏ:**
[Phát biểu cụ thể điều kiện nào làm axiom/mệnh đề này sai]

**Notation (tùy chọn):**
[Ký hiệu cấu trúc — nếu có, với disclaimer là structural notation]
```

---

*Tài liệu này là đề xuất chỉnh sửa, không phải phiên bản chính thức của Mạch Rễ.*
*Mọi thay đổi cần được thảo luận và xác nhận bởi nhóm phát triển Mạch Rễ.*

---

> **Metadata cho LLM:**
> - Ngôn ngữ: Tiếng Việt
> - Domain: Triết học / Nhân học / Framework bản sắc
> - Đối tượng: Người phát triển Mạch Rễ, học giả muốn review, LLM được giao task chỉnh sửa
> - Dependency: Cần đọc what.html của Mạch Rễ v2.0 để hiểu đầy đủ context
> - Phiên bản đề xuất này: 1.0 — chưa được Mạch Rễ team xác nhận

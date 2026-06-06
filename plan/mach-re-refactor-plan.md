# Mạch Rễ — Refactor Plan (Triết học)

## Goal

Refactor Mạch Rễ từ "framework vừa triết học vừa thực hành" thành **lý thuyết triết học nghiêm túc**: 4 axiom thực sự độc lập, điều kiện phản chứng rõ ràng, tách bạch hoàn toàn tầng descriptive khỏi tầng normative.

---

## RCA Diagnosis (đầu vào)

| Lỗi | Mô tả ngắn | Mức độ |
|-----|-----------|--------|
| Is-Ought Fallacy | Axiom descriptive → dùng làm normative | CRITICAL |
| Confirmation Bias | Case study minh họa, không kiểm chứng | HIGH |
| Ethnic Monolith | "Dân tộc Việt Nam" = người Kinh ngầm định | HIGH |
| Axiom không độc lập | III, VI, VII suy ra được từ I, II, IV, V | MEDIUM |
| Nhầm tầng | Framework + Theory cùng lúc | ROOT CAUSE |

---

## Tasks

- [ ] **T1: Phân tách hai văn bản** → Tạo `theory.md` (triết học thuần) và `practice.md` (công cụ thực hành). Hai file hoàn toàn độc lập. Verify: đọc `theory.md` không cần đọc `practice.md` để hiểu logic.

- [ ] **T2: Thu gọn về 4 Axiom thực sự** → Giữ I (Quan hệ bản thể), II (Bất biến cấu trúc), IV (Thời gian dọc), V (Biên giới động). Chuyển III, VI, VII thành **Derived Propositions** có chứng minh tường minh. Verify: mỗi axiom còn lại không suy ra được từ 3 cái kia.

- [ ] **T3: Vá Is-Ought Gap** → Thêm một mục `Normative Bridge` giải thích rõ: từ "hệ thống tồn tại theo cơ chế X" → "cộng đồng nên thực hành X" cần thêm tiền đề chuẩn mực nào (ví dụ: "nếu mục tiêu là sinh tồn văn hóa lâu dài, thì..."). Verify: không có câu nào dùng "do đó ta nên" mà thiếu tiền đề chuẩn mực tường minh.

- [ ] **T4: Xây điều kiện phản chứng nghiêm túc** → Bổ sung mục `Falsification Conditions` với ít nhất 2 điều kiện cụ thể, đo được, và thêm mục `Failure Cases` khảo sát ít nhất 1 giai đoạn lịch sử mà cơ chế Mạch Rễ *không* hoạt động (ví dụ: nam tiến và đồng hóa người Chăm). Verify: đọc xong có thể hình dung thí nghiệm để bác bỏ lý thuyết.

- [ ] **T5: Giải quyết Ethnic Monolith** → Thêm mục `Scope Boundary` tuyên bố rõ phạm vi: lý thuyết áp dụng cho nhóm văn hóa nào, với điều kiện lịch sử nào. Thừa nhận rằng 53 tộc thiểu số có thể có cơ chế khác hoặc đối kháng. Verify: không còn câu nào ngầm đồng nhất "dân tộc Việt Nam" với một thực thể văn hóa thuần nhất.

- [ ] **T6: Chuẩn hóa ký hiệu logic** → Kiểm tra toàn bộ ký hiệu toán học (∀, ≡, →). Mỗi ký hiệu phải được định nghĩa trước lần dùng đầu tiên. Mỗi công thức phải có diễn giải ngôn ngữ tự nhiên đi kèm. Verify: LLM có thể parse và diễn giải lại từng công thức không cần context bên ngoài.

- [ ] **T7: Viết `index.md` LLM-friendly** → File entry point với YAML frontmatter đầy đủ, tóm tắt lý thuyết trong ≤200 từ, bảng điều hướng đến từng file, và `quick-load context block` cho LLM (mục đích, phạm vi, không áp dụng khi nào). Verify: LLM đọc `index.md` đủ để trả lời câu hỏi cơ bản về lý thuyết mà không cần đọc file khác.

- [ ] **T8: Kiểm tra nhất quán xuyên file** → Đảm bảo mọi thuật ngữ có định nghĩa duy nhất, không có thuật ngữ được dùng với 2 nghĩa khác nhau ở 2 file. Verify: bảng glossary trong `index.md` khớp 100% với cách dùng trong `theory.md`.

---

## Cấu trúc file sau refactor

```
mach-re/
├── index.md              ← Entry point, LLM context block, điều hướng
├── theory.md             ← 4 Axiom + 3 Derived Propositions + Falsification
├── practice.md           ← 5 khái niệm + Rubric + 3 thực hành (độc lập với theory)
├── scope.md              ← Phạm vi áp dụng, giới hạn, Ethnic Monolith fix
├── bridge.md             ← Normative Bridge: từ descriptive → prescriptive
└── glossary.md           ← Định nghĩa chuẩn tất cả thuật ngữ
```

---

## LLM-Friendly Conventions (áp dụng cho toàn bộ file)

```
- YAML frontmatter: title, version, depends_on, scope, last_updated
- Heading hierarchy: H1 = file title, H2 = section, H3 = subsection
- Mỗi axiom/proposition: block quote cho phát biểu chính thức
- Công thức logic: code block với ngôn ngữ `logic`, diễn giải bằng prose ngay bên dưới
- Cross-reference: [[file#section]] format
- Không dùng emoji trong theory.md và glossary.md
- Tất cả ví dụ lịch sử: chú thích nguồn tham khảo
```

---

## Done When

- [ ] `theory.md` đọc độc lập, không chứa câu normative nào thiếu tiền đề chuẩn mực
- [ ] 4 axiom vượt được independence test (bỏ từng cái, 3 cái còn lại không suy ra được cái bị bỏ)
- [ ] `practice.md` hoạt động hoàn toàn không cần đọc `theory.md`
- [ ] Có ít nhất 1 failure case lịch sử được phân tích trong `scope.md`
- [ ] LLM đọc `index.md` → có thể trả lời: "lý thuyết này nói gì, áp dụng khi nào, không áp dụng khi nào, bác bỏ bằng gì"

---

## Notes

**Thứ tự ưu tiên:** T2 (axiom) và T3 (is-ought) phải làm trước T1 (tách file) — vì cần biết nội dung đúng trước khi phân chia cấu trúc.

**Rủi ro chính:** T4 (failure cases) đòi hỏi nghiên cứu lịch sử thực chất — không thể chỉ nói "cơ chế có thể thất bại" mà phải chỉ ra *khi nào* và *vì sao*.

**Không làm:** Không xóa phần thực hành (Rubric, 3 câu hỏi hấp thụ) — chúng có giá trị độc lập. Chỉ tách ra và để tự đứng trong `practice.md`.

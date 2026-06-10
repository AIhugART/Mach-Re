# Plan: Tự phân loại Mạch Rễ trong Paper 005

> **Date:** 2026-06-10
> **RCA score:** 5.0/5 (Correct: 1, Deep: 1, Feasible: 1, Conflict-risk: 1, Preservation: 1)
> **Decision:** THÊM (proceed)

## 1. Vấn đề

Paper 005 dùng Mạch Rễ để chẩn đoán "lỗi phạm trù" (đánh giá triết học tương quan-phân tán bằng thước đo hệ thống-siêu hình) nhưng không tự tuyên bố Mạch Rễ thuộc loại hình triết học nào. Paper phân loại *đối tượng được phân tích* (triết học Việt Nam) nhưng không tự phân loại *công cụ phân tích* (Mạch Rễ).

## 2. RCA — 3-round × 5-Why

### Round 1 — Symptom
Paper 005 thiếu tuyên bố về loại hình triết học của chính Mạch Rễ, dù dùng Mạch Rễ làm công cụ phân loại cho hệ khác.

### Round 2 — Mechanism
1. Paper 005's core contribution is Tiên Đề VIII (Reflexive Cognition): "hệ áp chính Tiên Đề I–IV lên bản thân nó"
2. Nếu Mạch Rễ không tự phân loại, nó vi phạm chính meta-axiom mà nó đề xuất
3. Tạo asymmetry: "bạn nói triết học Việt là tương quan-phân tán — thế framework của BẠN là loại gì?"
4. Mạch Rễ appears to claim a privileged external vantage point — điều Tiên Đề I (Relational Ontology) cấm
5. **Root (one sentence):** Paper áp dụng phân loại phản tư lên đối tượng nghiên cứu nhưng không lên chính nó — vi phạm Tiên Đề VIII.

### Round 3 — Root
Framework phải tuân theo chính tiêu chuẩn nó áp đặt lên đối tượng khác. Self-classification là hệ quả trực tiếp của Tiên Đề VIII.

## 3. Scoring gate (≥ 4/5 → fix)

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Correct | 1 | Genuine reflexivity gap — Tiên Đề VIII demands self-application |
| Deep | 1 | Fix touches root: internal consistency, not cosmetic wording |
| Feasible | 1 | Adding statements is structurally safe |
| Conflict-risk | 1 | Aligns with all existing axioms; no contradiction with any page |
| Preservation | 1 | Core argument strengthened — framework reflexivity becomes evidence |
| **TOTAL** | **5.0** | |

## 4. Implementation

### Vị trí chèn

| # | File | Vị trí | Nội dung |
|---|------|--------|----------|
| 1 | `paper_005.html` | Abstract (sau dòng 213, trước `<hr />`) | Compact self-classification (1 đoạn) |
| 2 | `paper_005.html` | §2.1 (sau dòng 334, trước bảng) | Fuller self-classification with Tiên Đề I grounding |
| 3 | `paper_005.md` | Abstract (sau dòng 13) | Đồng bộ với #1 |
| 4 | `paper_005.md` | §2.1 (sau dòng 63) | Đồng bộ với #2 |
| 5 | `paper_005_for_pdf.md` | Abstract (sau dòng 66) | Đồng bộ với #1 (LaTeX) |
| 6 | `paper_005_for_pdf.md` | §2.1 (sau dòng 116) | Đồng bộ với #2 (LaTeX) |

### Nội dung tuyên bố (bản compact — Abstract)

> **Phân loại khung nền (Framework Classification).** Mạch Rễ (Root-Circuit) tự phân loại là một **khung nền triết học thuần túy** (pure philosophical framework) thuộc loại hình **triết học tương quan-phân tán** (Relational and Distributed Philosophy). Nó không phải là triết học hệ thống-siêu hình (Systematic Metaphysics): các tiên đề của nó là mô tả cấu trúc của động lực quan hệ (structural descriptions of relational dynamics), không phải tuyên bố về bản chất tối hậu của thực tại (ultimate reality). Việc tự phân loại này là hệ quả trực tiếp của Tiên Đề VIII — Tự Nhìn Thấy Mình: framework phải áp dụng chính thước đo phân loại của mình lên bản thân nó (`[project interpretation]`).

### Nội dung tuyên bố (bản đầy đủ — §2.1)

> **Tự phân loại của Mạch Rễ.** Mạch Rễ (Root-Circuit) — khung nền được sử dụng trong bài viết này — tự phân loại thuộc cột phải của bảng trên: nó là một **khung nền triết học thuần túy thuộc loại hình Tương quan-Phân tán** (a pure philosophical framework of the Relational and Distributed type). Các tiên đề của Mạch Rễ không phải là mệnh đề siêu hình về bản chất tối hậu; chúng là mô tả cấu trúc (structural descriptions) về cách hệ thống tồn tại, bền vững, và tự nhận thức thông qua các mẫu hình quan hệ (relational patterns) phân tán trong mạng. Tiên Đề I (Sống Trong Quan Hệ — Relational Ontology) là tuyên bố nền tảng xác lập điều này: `Being(x) ≡ {R(x,y)}` — bản sắc được cấu thành bởi quan hệ, không phải bởi bản thể độc lập. Việc framework tự phân loại chính mình là yêu cầu của Tiên Đề VIII (Tự Nhìn Thấy Mình): một khung nền dùng thước đo "tương quan-phân tán vs. hệ thống-siêu hình" để phân tích đối tượng khác phải áp dụng được chính thước đo đó lên bản thân nó (`[project interpretation]`).

## 5. Verification checklist

- [x] Statement uses `[project interpretation]` tag per paper convention
- [x] No banned absolute terms from `dictionary_rule.md §1`
- [x] Aligns with Tiên Đề I (Relational Ontology — `Being(x) ≡ {R(x,y)}`)
- [x] Aligns with Tiên Đề VIII (Reflexive Cognition — self-application)
- [x] Does not contradict any existing page
- [x] CHANGELOG entry recorded

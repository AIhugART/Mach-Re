# Changelog — Papers (Mạch Rễ)

> **Phạm vi:** Nơi **duy nhất** ghi nhận thay đổi cho các file trong `papers/`. Không ghi paper changes vào `CHANGELOG.md` gốc.
> **Liên kết:** Lịch sử toàn bộ dự án (axiom, HTML nodes, audit, evidence) → xem [`CHANGELOG.md`](../CHANGELOG.md) tại thư mục gốc.
> **Quy tắc:** Mỗi entry phải qua 3-round RCA × 5-Why × scoring gate ≥ 4/5 (theo `CLAUDE.md` §RULE ZERO).

---

## 2026-06-10 — paper_005.md + paper_005.html — Sync codebase mới + Bảng Nguồn Trích Dẫn [1]–[15] · RCA 4.8/5

**Symptom:** Paper 005 thiếu ba evidence mới từ codebase (Yoruba *ìwà* [13], ca dao biến dịch [14], Mệnh Đề F [12]), chưa có inline `[N]` citation markers, và TÀI LIỆU THAM KHẢO chưa có bảng Nguồn Trích Dẫn đánh số APA.

**Root:** Paper viết trước khi Yoruba evidence, ca dao convergent discovery, Mệnh Đề F, và Rule #12 (Citation Table) được thêm vào codebase.

**Fix — 5 nhóm:**
1. §4.1 — Yoruba *ìwà* [13] + Ubuntu [15]
2. §4.2 — Ca dao biến dịch [14] + Phan Ngọc [3]
3. §4.3 — Mệnh Đề F structural explanation [12]
4. 12 inline `[N]` citation markers toàn bài
5. Bảng Nguồn Trích Dẫn [1]–[15] APA + HTML hyperlink anchors

**Files:** `papers/paper_005/paper_005.md`, `papers/paper_005/paper_005.html`
**RCA:** 4.8/5 (Correct 5 · Deep 5 · Feasible 4 · Conflict-risk 5 · Preservation 5)

---

## 2026-06-10 — paper_005 — Thêm tự phân loại Mạch Rễ (Framework Classification) · RCA 5.0/5

**Symptom:** Paper 005 dùng Mạch Rễ để chẩn đoán "lỗi phạm trù" (đánh giá triết học tương quan-phân tán bằng thước đo hệ thống-siêu hình) nhưng không tự tuyên bố Mạch Rễ thuộc loại hình nào. Vi phạm Tiên Đề VIII.

**Fix:** Thêm Framework Classification vào Abstract và §2.1 — Mạch Rễ là triết học tương quan-phân tán, không phải hệ thống-siêu hình. Neo vào Tiên Đề I + VIII.

**Files:** `papers/paper_005/paper_005.html`, `papers/paper_005/paper_005.md`, `papers/paper_005/paper_005_for_pdf.md`
**RCA:** 5.0/5 · Plan: `plan/paper_005_self_classification_plan.md`

---

## 2026-06-08 — paper_005 — Sync Tiên Đề III theo `axiom_spec.md` · RCA 5/5

**Symptom:** Paper 005 dùng tên Tiên Đề III cũ, chưa nhất quán với nguồn chân lý `axiom_spec.md`.

**Fix:**
- Abstract: "Mạch Cội Dọc" → "Mạch Cội Nguồn" (bản chất)
- §4.3 header + phát biểu: cập nhật canonical name + thêm claim "mạch tồn tại / ontological dimension"

**Files:** `papers/paper_005/paper_005.md`, `papers/paper_005/paper_005.html`
**RCA:** 5/5

---

## 2026-06-07 — paper_003 — Thêm Bảng Giải Thích Thuật Ngữ (Glossary) · RCA 5/5

**Symptom:** Paper 003 dùng nhiều thuật ngữ chuyên môn (Bản thể học liên chủ thể, Mạch cội nguồn, Bất biến cấu trúc…) nhưng chưa có định nghĩa đơn giản hóa cho độc giả phổ thông.

**Fix:** Thêm bảng glossary cuối bài, trước tài liệu tham khảo. Mỗi thuật ngữ kèm giải thích ở trình độ học sinh cấp 3.

**Files:** `papers/paper_003/paper_003_draft.md`
**RCA:** 5/5

---

## 2026-06-07 — paper_005 — Bổ sung bảng giải thích nhãn phân loại học thuật (RCA) · RCA 5/5

**Symptom:** Paper 005 dùng các nhãn `[established scholarship]`, `[contested scholarship]`, `[project interpretation]`, `[analogy]`, `[hypothesis]` nhưng chưa có bảng giải thích ý nghĩa cho người đọc.

**Fix:** Thêm chương "Ý NGHĨA CÁC NHÃN PHÂN LOẠI HỌC THUẬT (RCA)" cuối paper, kèm bảng 5 nhãn với giải thích học thuật + trực quan (trình độ học sinh cấp 3) + ví dụ cụ thể trong bài.

**Files:** `papers/paper_005/paper_005.md`, `papers/paper_005/paper_005.html`, `papers/paper_005/paper_005.pdf`
**RCA:** 5/5

---

> **Ghi chú:** Toàn bộ paper entries đã được di chuyển từ [`CHANGELOG.md`](../CHANGELOG.md) sang đây (2026-06-10). Từ nay, mọi thay đổi cho `papers/` **chỉ** ghi vào file này — không ghi song song vào `CHANGELOG.md` gốc.

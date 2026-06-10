# Changelog — Papers (Mạch Rễ)

> **Phạm vi:** Nơi **duy nhất** ghi nhận thay đổi cho các file trong `papers/`. Không ghi paper changes vào `CHANGELOG.md` gốc.
> **Liên kết:** Lịch sử toàn bộ dự án (axiom, HTML nodes, audit, evidence) → xem [`CHANGELOG.md`](../CHANGELOG.md) tại thư mục gốc.
> **Quy tắc:** Mỗi entry phải qua 3-round RCA × 5-Why × scoring gate ≥ 4/5 (theo `CLAUDE.md` §RULE ZERO).

---

## 2026-06-10 — TỔNG KẾT: Đại tu paper_005 + Hạ tầng papers/ · RCA 4.9/5 (session)

**Phạm vi:** 6 commits, 10 files changed.

### A. paper_005 — Sync codebase mới (3 evidence + citation system)

| # | Thay đổi | § | RCA |
|---|----------|---|-----|
| A1 | Yoruba *ìwà* [13] + Ubuntu [15] — hội tụ độc lập relational ontology | §4.1 | 5.0 |
| A2 | Ca dao biến dịch [14] + Phan Ngọc [3] — convergent evidence "Càng thắm thì lại càng phai" | §4.2 | 4.8 |
| A3 | Mệnh Đề F [12] — giải thích cấu trúc vì sao bản sắc Việt không tan rã (A∧B∧C chưa đồng thời) | §4.3 | 4.8 |
| A4 | 12 inline `[N]` citation markers toàn bài — [1]–[15] | all | 4.8 |
| A5 | Bảng Nguồn Trích Dẫn APA [1]–[15] thay TÀI LIỆU THAM KHẢO | footer | 5.0 |
| A6 | HTML: `<a href="#nguon-N">[N]</a>` hyperlinks + `id="nguon-N"` anchors | all | 5.0 |
| A7 | Fix nguồn văn bản: Wikipedia → "tổng hợp anonymous" | footer | 5.0 |

### B. Hạ tầng papers/

| # | Thay đổi | RCA |
|---|----------|-----|
| B1 | Tạo `CHANGELOG_papers.md` — changelog riêng cho papers | 4.8 |
| B2 | Di chuyển 5 paper entries từ `CHANGELOG.md` → `CHANGELOG_papers.md` (exclusive) | 5.0 |
| B3 | Cập nhật `CLAUDE.md` Document Contract Rules: paper changes → chỉ `CHANGELOG_papers.md` | 5.0 |
| B4 | Link `CHANGELOG_papers.md` từ `papers/index.html` footer | — |
| B5 | Xóa `papers/CLAUDE_REF.md` — file CLAUDE.md của dự án VVV-QMRF (không liên quan) | 5.0 |
| B6 | Fix `deploy-pages.yml` — thêm `papers/**` vào paths trigger | 5.0 |

### Citation table [1]–[15] (final)

| # | Nguồn | Mới? |
|---|-------|------|
| [1] | Cadière (1958) | |
| [2] | Đào Duy Anh (1938) | |
| [3] | Phan Ngọc (2000) | |
| [4] | Ashby (1956) | |
| [5] | Weick (1995) | |
| [6]–[9] | Hountondji, Wiredu, Matilal, Oruka | |
| [10]–[11] | Trần Văn Giàu, Nguyễn Tài Thư | |
| [12] | Mạch Rễ `axiom_spec.md` | |
| [13] | Peel (2000) — Yoruba | ✅ |
| [14] | Nguyễn Tấn Long & Phan Canh (1969) — Ca dao | ✅ |
| [15] | Udah et al. (2025) — Ubuntu | ✅ |

### Files changed (10)

`papers/paper_005/paper_005.md`, `papers/paper_005/paper_005.html`, `papers/CHANGELOG_papers.md`, `papers/index.html`, `CHANGELOG.md`, `CLAUDE.md`, `.github/workflows/deploy-pages.yml` (+ `papers/CLAUDE_REF.md` deleted)

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

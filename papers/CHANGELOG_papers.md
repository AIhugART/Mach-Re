# Changelog — Papers (Mạch Rễ)

> **Phạm vi:** Nơi **duy nhất** ghi nhận thay đổi cho các file trong `papers/` (ngoại trừ `papers/paper_005/` — đã có [`CHANGELOG_paper_005.md`](paper_005/CHANGELOG_paper_005.md) riêng). Không ghi paper changes vào `CHANGELOG.md` gốc.
> **Liên kết:** Lịch sử toàn bộ dự án (axiom, HTML nodes, audit, evidence) → xem [`CHANGELOG.md`](../CHANGELOG.md) tại thư mục gốc.
> **Quy tắc:** Mỗi entry phải qua 3-round RCA × 5-Why × scoring gate ≥ 4/5 (theo `CLAUDE.md` §RULE ZERO).

## 2026-06-11 — Phase 7 completion: paper_009 title V4 fix · RCA 4.4/5

**Triple compass:** A (Phan Ngọc) — title is the paper's public face; "Giao Diện Sống" imports computer-interface frame, failing Việt hóa rule 1. B (Ashby) — Requisite Variety: body already uses canonical names, title was the single stale artifact. C (Buddhist epistemology) — Pramāṇa: a title that doesn't match the framework's own naming standard is deceptive at the point of first contact.

**RCA R3 (root):** Title was set before Phase 1b naming RCA completed (2026-06-11). Body text (written after Phase 1b) already uses "Gặp Nhau Giữ Gốc — Không Của Ai, Nhờ Cả Hai" in §3.2 — title was the lone stale artifact.

**Scoring: 4.4/5** → fix (Correct 4, Deep 4, Feasible 5, Conflict-risk 4 [papers/index.html sync], Preservation 5).

**Files sửa:**
- `papers/paper_009/paper_009_draft.md` line 5: `"Giao Diện Sống"` → `"Gặp Nhau Giữ Gốc (Living Interface)"`
- `papers/index.html` line 267: same title fix (tiered routing exception — this is a papers-scope change affecting the papers index, recorded here)

**Phase 7 deliverable status:** paper_009_draft.md is fully v3.2-compliant — ESP Layer E ✓, Boundary Statement ✓, graded C1 ✓, canonical names in body ✓, epistemic marks ✓, falsification conditions ✓, APA citation table ✓, author metadata ✓. No further Phase 7 work required.

---


## 2026-06-11 — Phase 8c: paper_009 thuần-Việt gloss "nhận thức luận (mạch biết)" · RCA 4.8/5

Part of naming RCA (la bàn Phan Ngọc): "nhận thức luận" → thuần-Việt gloss "mạch biết" (4.8/5).
- `paper_009_draft.md` line 94: "nhận thức luận (mạch biết)"

> Cross-ref tầng root: dictionary_rule.md §4 canonical gloss table + axiom_9.html + axiom_spec.md → logged in [`CHANGELOG.md`](../CHANGELOG.md).

---

## 2026-06-11 — Phase 8a: paper_009 V4 name fix "Gặp Nhân" → "Gặp Nhau" · RCA 5.0/5

**Symptom:** `paper_009_draft.md` dùng "Gặp Nhân Giữ Gốc" (Phase 7 viết theo session summary lỗi) thay vì canonical "Gặp Nhau Giữ Gốc" từ `dictionary_rule.md §9`. Gloss đi kèm cũng sai: "gặp người khác" → phải là "gặp nhau, reciprocal".

**RCA R3 (root):** V4 rule không được kiểm tra tại Phase 7. "Nhau" = hai hệ gặp lẫn nhau (inter-system reciprocal) — đúng ngữ nghĩa IX; "Nhân" = người — sai phạm trù.

**Scoring: 5.0/5** → fix.

**Files sửa:**
- `papers/paper_009/paper_009_draft.md` line 78: `"Gặp Nhân Giữ Gốc"` → `"Gặp Nhau Giữ Gốc"` + gloss "gặp người khác" → "gặp nhau, reciprocal"
- `papers/paper_009/paper_009_draft.md` line 200: `Gặp Nhân Giữ Gốc` → `Gặp Nhau Giữ Gốc`

> Cross-ref tầng root: `axiom_spec.md` + `index.html` + CHANGELOG entry → logged in [`CHANGELOG.md`](../CHANGELOG.md) (Phase 8a).

---

## 2026-06-11 — paper_009 (TẠO MỚI): "Ngoại Giao Cây Tre như Giao Diện Sống" · ESP E 4.8/5 + RCA 4.8/5

**ESP Layer E (bắt buộc trước prose — Tier 3 Rule #1):**
- L1–L4 RCA Stack: Bamboo Diplomacy thiếu formal structural account → Việt Nam-VIII + US-chưa-VIII → C1-min → P* = identity-preserving inter-system encounter. IX formalize gap này.
- Claim Ladder: **Interpretive Mapping [interpretation]** — an toàn, rõ ràng definitions.
- Boundary Statement in §2: NOT-claim / CLAIM list explicit.
- Score E: 4.8/5 → proceed to prose.

**Files tạo:**
- `papers/paper_009/paper_009_draft.md` — full prose paper (bilingual VI/EN)
- `papers/index.html` — Paper 009 card added (purple #5a3070)

**Routing tiered changelog:** ONLY `papers/CHANGELOG_papers.md`. Root `CHANGELOG.md` không nhận entry này.

**RCA score: 4.8/5.** Phase 7 → COMPLETE.

---

## 2026-06-10 — TỔNG KẾT: Đại tu paper_005 + Hạ tầng papers/ · RCA 4.9/5 (session)

**Phạm vi:** 6 commits, 10 files changed. **Paper_005 portion** (A1–A7) → [`CHANGELOG_paper_005.md`](paper_005/CHANGELOG_paper_005.md); **papers/ infrastructure portion** (B1–B6) logged here.

### B. Hạ tầng papers/

| # | Thay đổi | RCA |
|---|----------|-----|
| B1 | Tạo `CHANGELOG_papers.md` — changelog riêng cho papers | 4.8 |
| B2 | Di chuyển 5 paper entries từ `CHANGELOG.md` → `CHANGELOG_papers.md` (exclusive) | 5.0 |
| B3 | Cập nhật `CLAUDE.md` Document Contract Rules: paper changes → chỉ `CHANGELOG_papers.md` | 5.0 |
| B4 | Link `CHANGELOG_papers.md` từ `papers/index.html` footer | — |
| B5 | Xóa `papers/CLAUDE_REF.md` — file CLAUDE.md của dự án VVV-QMRF (không liên quan) | 5.0 |
| B6 | Fix `deploy-pages.yml` — thêm `papers/**` vào paths trigger | 5.0 |

### Files changed (3 — infrastructure only)

`papers/CHANGELOG_papers.md`, `CLAUDE.md`, `.github/workflows/deploy-pages.yml` (+ `papers/CLAUDE_REF.md` deleted)

> Cross-ref: Paper_005 portion (A1–A7, 7 paper files, citation table [1]–[15]) → [`CHANGELOG_paper_005.md`](paper_005/CHANGELOG_paper_005.md).

---

## 2026-06-07 — paper_003 — Thêm Bảng Giải Thích Thuật Ngữ (Glossary) · RCA 5/5

**Symptom:** Paper 003 dùng nhiều thuật ngữ chuyên môn (Bản thể học liên chủ thể, Mạch cội nguồn, Bất biến cấu trúc…) nhưng chưa có định nghĩa đơn giản hóa cho độc giả phổ thông.

**Fix:** Thêm bảng glossary cuối bài, trước tài liệu tham khảo. Mỗi thuật ngữ kèm giải thích ở trình độ học sinh cấp 3.

**Files:** `papers/paper_003/paper_003_draft.md`
**RCA:** 5/5

---

> **Ghi chú:** Toàn bộ paper entries đã được di chuyển từ [`CHANGELOG.md`](../CHANGELOG.md) sang đây (2026-06-10). Từ nay, mọi thay đổi cho `papers/` **chỉ** ghi vào file này — không ghi song song vào `CHANGELOG.md` gốc.
>
> **Cập nhật 2026-06-11:** Toàn bộ entry cho `papers/paper_005/` đã được di chuyển sang [`CHANGELOG_paper_005.md`](paper_005/CHANGELOG_paper_005.md). Từ nay, mọi thay đổi cho file trong `papers/paper_005/` **chỉ** ghi vào changelog đó — không ghi vào đây.

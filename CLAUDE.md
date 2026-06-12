# CLAUDE.md

## RULE ZERO — Root Cause Analysis (RCA)

**This is the highest mandatory rule, applied to every activity: research planning, literature review, conceptual mapping, documentation, critique, revision, and publication preparation.**

Never treat a symptom, ambiguity, or attractive analogy as the conclusion. Always trace the observed issue, claim, or mismatch back to its root cause before acting.

### Five-step process

1. **Define** — Describe the observed issue precisely. Separate the *symptom* (what appears in the text, argument, mapping, citation, or structure) from the *cause* (the assumption, source gap, conceptual mismatch, or methodological error that produced it).
2. **Trace** — Follow the causal chain backward by asking: "What made this issue appear?" Repeat at least three times using the "5 Whys" method.
3. **Isolate** — Identify the starting point of the failure: an unsupported claim, weak citation, ambiguous term, broken mapping, category error, outdated source, missing definition, or structural inconsistency. If it is not isolated, do not revise yet.
4. **Fix the cause, not the symptom** — Correct the root cause directly. Do not patch prose, soften wording, add a vague caveat, or create a workaround unless it is explicitly marked as `TODO(HOTFIX)`.
5. **Verify** — Show that the root cause has been removed, not merely that the visible symptom disappeared. When possible, verify against the source text, the active mapping files, the published node/edge definitions, and the research objective.

### Decision procedure — 3-round RCA × 5-Why × scoring gate (≥ 4/5)

This operationalizes steps 2–4 above. It is the procedure already proven in
`CHANGELOG.md` (each edited claim carries its score) and tabulated in
`plan/dictionary_rule.md`.

**3-round RCA (three depths of digging).** Step 2 "Trace" must reach the third
round; stopping earlier treats a symptom.
- Round 1 — Symptom: name the surface defect (absolute wording, self-scored
  number, pseudo-formula).
- Round 2 — Mechanism: why the surface defect backfires *here specifically* — a
  framework that invites strict scrutiny is hurt more by a sloppy surface.
- Round 3 — Root: which internal standard it violates (the framework's own
  falsifiability / traceability rule). The fix makes the framework obey itself.

**5-Why.** Inside each round, ask "what made this appear?" until the chain
bottoms out in one sentence (the root). If the root needs more than one
sentence, the trace is incomplete — return to Round 1.

**Scoring gate (≥ 4/5).** Before changing ANY claim, score that claim on five
criteria, 1 point each. The scored unit is *the candidate claim*; a high score
means a strong case to edit.

| Criterion | Question | High score means |
|---|---|---|
| Correct | Is this genuinely an overclaim / unfalsifiable statement? | real defect |
| Deep | Does the fix touch the root (internal consistency), not just tone? | reaches root |
| Feasible | Can it be fixed without breaking core structure/meaning? | safe to do |
| Conflict-risk | Will the fix avoid creating contradictions on other pages? | low new risk |
| Preservation | Is the core strength kept after the fix? | strength kept |
| **Provenance** | **Does every typology/history/comparison claim carry `[established]+source` or `[proposed-by-this-project]`?** | **no untagged claim** |

> **Tiêu chí Provenance — bắt buộc (RCA finding 2026-06-12, F9, score 4.8/5):** Gate này được thêm vào sau khi kiểm chứng ngoài (con người) xác nhận tên phạm trù "Triết học Tương quan-Phân tán / Relational and Distributed Philosophy" là AI coinage trình bày sai tư cách `[established]` — đã tồn tại qua nhiều vòng RCA nội bộ vì không tiêu chí nào kiểm xuất xứ ngoài repo. Bước **Verify** (bước 5 RULE ZERO) được mở rộng: ngoài nguồn nội bộ, phải kiểm tra mọi claim loại hình/lịch sử có tồn tại trong văn liệu học thuật ngoài repo. Claim không có tag provenance = claim chưa hoàn chỉnh.

**Threshold: average ≥ 4/5 → fix; below 4/5 → keep as-is.** Anchors from
`CHANGELOG.md`: `upgrade.html:213` "describes *precisely*" scored 4.8 (the same
page lists four limits of that very description → self-contradiction) → fixed;
`mach_re_homologous.html:217` "language precise enough for dialogue" scored 3.2
(a design goal, not a universal claim) → kept.

> Second use of the same rubric: `plan/mach-re-plan-chinh-sua-v2.md` §2 scores
> *plan items* (not claims), where ≥ 4/5 means "the proposed action is sound,
> keep it". Same five criteria, different scored object and orientation — always
> state which one you are scoring.

**After any fixing pass, record it in `CHANGELOG.md`** (what was lowered/changed
and why), per `plan/dictionary_rule.md` (P5/G6). The canonical lookup table for
absolute→scoped substitutions lives in `plan/dictionary_rule.md`; consult it
before editing prose and do not duplicate it here.

### Activity-specific application

| Activity | RCA requirement |
|----------|-----------------|
| **Research planning** | Ask "Why is this research question necessary?" before "How should it be written?" Identify the real problem behind the requested document or section. |
| **Literature review** | Trace every major claim to a source, and distinguish established scholarship from interpretation, analogy, or hypothesis. |
| **Conceptual mapping** | Understand why each concept exists in its original system before mapping it across systems. Treat cross-domain links as analogies unless equivalence is explicitly justified. |
| **Documentation** | Find what caused confusion before rewriting. Fix the structure, terminology, missing definition, or broken reference, not only the sentence that looks unclear. |
| **Review** | Classify every finding as either symptom or root cause. A blocking issue must identify the root cause; a surface-level wording issue is only a documentation bug. |
| **Revision** | Identify what is truly causing complexity or inconsistency before simplifying, reorganizing, or abstracting. Do not create structure around a symptom. |

### Example

```text
Symptom: A section claims Buddhist Epistemology "solves" Quantum Measurement.
  → Why? The wording treats a philosophical mapping as a physical explanation.
    → Why? The document does not separate analogy, interpretation, and prediction.
      → Why? The claim lacks a formal boundary between ontology and physics.
        → Root cause: Category error between epistemological interpretation and empirical physical theory.
          → Fix: Reframe the section as an interpretive mapping unless formal proof, peer review, physical predictions, and experimental tests are supplied.
```

### Warnings

- If the revision only changes the sentence where the symptom appears, it is **not enough**; return to step 2.
- If the root cause cannot be explained in one sentence, understanding is **not complete**; return to step 1.
- If the fix only adds a vague caveat, fallback phrase, or defensive wording, it is **treating the symptom**; return to step 4.

## Core Principles

### Phân loại Khung nền — Tuyên bố Vị thế `[proposed-by-this-project]` (RCA finding 2026-06-10; RETRACTED & REVISED 2026-06-12 — F9)

> **⚠️ RETRACTION 2026-06-12 (F9, score 4.8/5):** Điểm RCA 5.0/5 cũ bị rút — chấm bằng rubric mù provenance (5 tiêu chí nội bộ, không có tiêu chí Provenance). Kiểm chứng ngoài (con người) xác nhận tên phạm trù "Triết học Tương quan-Phân tán / Relational and Distributed Philosophy" là AI coinage, không tồn tại trong văn liệu học thuật độc lập. Điểm chấm lại theo rubric 6 tiêu chí: **3.8/6** (Provenance = 0 → kéo xuống). Đây là retraction đầu tiên của dự án, do kiểm chứng ngoài. Root cause: gate thiếu tiêu chí Provenance — đã fix ở RULE ZERO ở trên.
>
> Áp dụng bắt buộc khi giới thiệu, định nghĩa, hoặc so sánh Mạch Rễ với bất kỳ hệ triết học nào khác.

**Mạch Rễ (Root-Circuit) tự phân loại là một khung nền triết học thuần túy (pure philosophical framework) đề xuất loại hình `[proposed-by-this-project]` là triết học tương quan-phân tán.** Nó không phải là Triết học Hệ thống-Siêu hình (Systematic Metaphysics).

**Phân biệt tư cách (Provenance breakdown):**
- `[established]` — **Relational ontology**: Whitehead (process philosophy), Emirbayer (relational sociology, 1997), Ramose / Ubuntu scholarship (Anattā, pratītyasamutpāda)
- `[established]` — **Distributed cognition/memory**: Hutchins (1995), Weick (sensemaking)
- `[proposed-by-this-project]` — **Tổ hợp hai thành phần trên thành một loại hình có tên "Tương quan-Phân tán" với tư cách thành viên**: đây là coinage của dự án, chưa được kiểm chứng ngoài. Đề xuất taxonomy mới là hành vi triết học hợp lệ — nhưng phải mang đúng tag.

**Bản chất (Essence):** Các tiên đề của Mạch Rễ là mô tả cấu trúc (structural descriptions) của động lực quan hệ — cách hệ thống tồn tại, bền vững, và tự nhận thức thông qua các mẫu hình quan hệ (relational patterns) phân tán trong mạng. Chúng không phải là mệnh đề siêu hình về bản chất tối hậu của thực tại (ultimate reality).

**Quy tắc sử dụng (cập nhật sau F9):**
- Khi giới thiệu Mạch Rễ với người mới → nêu rõ: "Đây là framework đề xuất loại hình tương quan-phân tán `[proposed-by-this-project]`, không phải siêu hình học, chưa qua thẩm định học giới"
- Khi so sánh với hệ triết học khác → đặt nó vào cột đề xuất, kèm tag status
- Khi viết paper → Boundary Statement phải phân biệt `[established]` vs `[proposed-by-this-project]` cho từng thành phần
- Việc tự phân loại là hệ quả của Tiên Đề V — Soi Mình Mà Không Vỡ: framework phải áp dụng chính thước đo của mình lên bản thân nó — bao gồm cả thước đo provenance

### Quan hệ model-of — Bất đối xứng phụ thuộc (RCA findings F2+F3, 2026-06-12)

> Điểm RCA: F2 = 4.8/5 · F3 = 4.8/5. Áp dụng bắt buộc khi mô tả quan hệ giữa Mạch Rễ và triết học dân tộc Việt; khi so sánh với Ubuntu, Tam giáo, hoặc bất kỳ hệ nào khác.

**Quan hệ Mạch Rễ ↔ triết học dân tộc Việt là quan hệ model-of, không phải identity, không phải phái sinh.** Đối tượng là thực thể vô danh tiền-tồn — tồn tại trước model dưới dạng thực hành phân tán (ca dao, tục ngữ, hương ước). Model làm bằng A×B×C, như chữ Nôm làm bằng bộ chữ Hán để ghi âm tiếng Việt mà không biến tiếng Việt thành tiếng Hán.

**Tiêu chí vận hành — bất đối xứng phụ thuộc (F3):**
Để phân biệt model/entity: *Nếu hủy toàn bộ Mạch Rễ, đối tượng có tồn tại không?*
- CÓ → quan hệ là model-of (đúng)
- KHÔNG → framework đang tuyên bố identity → overclaim → phải sửa bằng 3-round RCA

**Quy tắc sử dụng:**
- Dùng "Mạch Rễ mô tả / làm mô hình về triết học dân tộc Việt" — ✅
- Không dùng "Mạch Rễ là triết học dân tộc Việt" hay "Mạch Rễ phái sinh từ Nho/Phật/Lão" — ❌
- Chi tiết: `axiom_spec.md §0.3` · `plan/dictionary_rule.md §11.1`

### Taxonomy 3 vai: Thấu kính / Gương soi / Tia chuẩn (RCA findings F5+F6, 2026-06-12)

> Điểm RCA: F5 = 4.8/5 · F6 = 4.8/5. Áp dụng bắt buộc trước khi so sánh Mạch Rễ với bất kỳ hệ triết học nào, hoặc trả lời câu hỏi "tại sao không dùng X làm nền tảng?"

**Ba vai không thể hoán đổi:**

| Vai | Ứng viên | Chức năng | Điều kiện |
|---|---|---|---|
| **Thấu kính** (lens) | A (Phan Ngọc), B (Ashby/Weick), C (pramāṇa/apoha) | Nhìn *qua* — hình thức hóa, bác bỏ | Tháo → model sập. Giống đối tượng = khuyết điểm |
| **Gương soi** (mirror) | Ubuntu, Yoruba | Soi *cạnh* — đo phân kỳ, xác nhận loại hình | Không cấu thành tiên đề — có thể thay |
| **Tia chuẩn** (reference beam) | Nho/Phật/Lão dạng nguồn | Chiếu *vào* — đo delta khúc xạ của đối tượng | Output của bộ lọc → không thể là thấu kính |

**Quy tắc:**
- Ubuntu chia sẻ đặc trưng với đối tượng → đây là lý do *không* dùng làm thấu kính (F5): giống đối tượng = khuyết điểm của dụng cụ
- Tam giáo đồng nguyên = cái-được-chọn, không phải cái-chọn → không thể dùng làm lens (F6): giải thích bộ lọc bằng sản phẩm của bộ lọc = vòng tròn
- Chi tiết: `axiom_spec.md §0.4` · `plan/dictionary_rule.md §11.2–11.3`

### Tiên Đề III — Bản chất và Biểu hiện (RCA finding 2026-06-05)

> Phân tích gốc rễ (không phải hotfix). Điểm RCA: 5/5. Áp dụng bắt buộc trong mọi tài liệu, phát biểu, và so sánh triết học liên quan đến Tiên Đề III.

**Bản chất (Essence) — Mạch Cội Nguồn (Orthogonal Temporality):** Trục V và trục H là hai chiều kích thời gian **trực giao** (mathematically independent, irreducible to each other): `V ⊥ H`. Tính trực giao này là tính chất cấu trúc (structural property) nền tảng của Tiên Đề III — lý do duy nhất để phân biệt Tiên Đề III với "ký ức là một phần của hiện tại" (Halbwachs, Luhmann). Tên canonical tiếng Việt: **Mạch Cội Nguồn** — "Cội" (dọc/V) ⊥ "Nguồn" (ngang/H), hai chiều trực giao không rút gọn về nhau.

**Biểu hiện (Manifestation) — Mạch Cội Dọc (Vertical Temporality):** Hình thức mà tính trực giao hiện ra trong đời sống văn hóa xã hội: trục quan hệ tổ tiên ↕ hiện tại ↕ hậu thế. "Dọc" là cách đặt tên trực quan cho chiều trực giao đó, không phải định nghĩa cấu trúc. Tên canonical tiếng Việt: **Mạch Cội Dọc**.

**Quy tắc sử dụng thuật ngữ:**
- Khi phát biểu nguyên lý bản thể học → dùng **Orthogonal Temporality** / **Mạch Cội Nguồn** (bản chất)
- Khi mô tả thực hành văn hóa / sơ đồ trực quan / so sánh đa văn hóa → dùng **Vertical Temporality** / **Mạch Cội Dọc** (biểu hiện)
- Hai thuật ngữ **không** thay thế nhau: chúng khác tầng (essence ≠ manifestation), không phải đồng nghĩa
- **Mạch Cội Nguồn** ≠ **Mạch Cội Dọc**: "Cội Nguồn" = cả hai trục (V ⊥ H) = bản chất; "Cội Dọc" = trục dọc (V) = biểu hiện

### Tên thuần Việt các Tiên Đề & Mệnh Đề (RCA finding 2026-06-05; ký pháp cập nhật 2026-06-11)

> Điểm RCA: 8/8 đơn vị đạt ≥ 4/5. Bảng canonical (nguồn chân lý duy nhất) tại `plan/dictionary_rule.md §9`.
> **Quy tắc ký pháp phân tầng (Quyết định 4, 2026-06-11 — theo `raw/axiom-chart.html`):** số La Mã CHỈ dành cho **Tiên Đề** (đơn vị độc lập, không suy ra được); **Mệnh Đề Dẫn Xuất** đánh số La tinh 1–4 (trước: V, VI, VII, F); cấp dưới nữa không đánh số phân cấp. Số La Mã đã hạ tầng (V–VII) không tái sử dụng — dãy tiên đề I–IV, VIII, IX có khoảng trống chủ đích.
> Format đầy đủ: `Tiên Đề [La Mã] — [Biểu hiện thuần Việt] — [Bản chất thuần Việt] ("EN")` · `Mệnh Đề [1–4] — [Biểu hiện] — [Bản chất] ("EN")`.

| # | Tầng | Biểu hiện | Bản chất |
|---|---|---|---|
| Tiên Đề I | Core | Sống Trong Quan Hệ | Có Nhau Mới Có Mình |
| Tiên Đề II | Core | Nếp Bản Sắc | Đổi Mà Vẫn Là Mình |
| Tiên Đề III | Core | Mạch Cội Dọc | Mạch Cội Nguồn |
| Tiên Đề IV | Core | Ranh Giới Mềm | Đóng Mở Có Chọn |
| Mệnh Đề 1 *(trước: V)* | Derived | Giữ Mà Không Gom | Ai Cũng Giữ Một Phần |
| Mệnh Đề 2 *(trước: VI)* | Derived | Hóa Nhiễu Thành Sức | Đau Được Xử Là Đau Lành |
| Mệnh Đề 3 *(trước: VII)* | Derived | Nổi Lên Có Hướng | Hợp Lại Thành Cái Mới |
| Mệnh Đề 4 *(trước: F)* | Derived | Đứt Khi Hết Cội | — (ký hiệu cấu trúc `F` giữ nguyên) |
| Tiên Đề V | Meta | Tự Nhìn Thấy Mình | Soi Mình Mà Không Vỡ |
| Tiên Đề VI | Interface | Gặp Nhau Giữ Gốc | Không Của Ai, Nhờ Cả Hai |

### Sứ mệnh Việt hóa — Từ vựng triết học thuần Việt (RCA finding 2026-06-09)

> Điểm RCA: 5.0/5 (3-round × 5-Why × scoring gate). Áp dụng bắt buộc khi chọn thuật ngữ canonical, viết phát biểu chính thức Tiếng Việt, hoặc quyết định giữa từ thuần Việt và từ Hán-Việt/dịch.

**Sứ mệnh:** Khung nền triết học Mạch Rễ cố gắng xây dựng một bộ từ vựng triết học **bằng tiếng Việt bản địa** — không phải Hán-Việt, không phải dịch từ Anh/Pháp. Đây không phải là lựa chọn thẩm mỹ; đây là yêu cầu cấu trúc: nếu dùng từ Hán-Việt hoặc từ dịch, framework sẽ mượn luôn hệ quy chiếu triết học của ngôn ngữ nguồn và mất đi tính nguyên bản của góc nhìn.

**Trường ngữ nghĩa "nếp" — ví dụ canonical (proof-of-concept):**

> "Nếp" là khái niệm nguyên tử (atomic concept) của toàn bộ Việt hóa Mạch Rễ. Nó thuộc phạm trù **cấu trúc sống** (living structure — mất đi thì hệ thống sụp đổ), phân biệt với phạm trù **quy ước xã hội** (social convention — có thể thay đổi, đàm phán).

| Thuật ngữ | EN mapping | Vai trò trong framework |
|---|---|---|
| **nếp** | living pattern (atomic) | Đơn vị cấu trúc sống cơ bản — không phải thói quen, không phải phong tục |
| **nếp tổ chức** | Configuration | Cách một hệ thống tự tổ chức thành chỉnh thể tại một thời điểm |
| **nếp bản sắc** | Structural Invariant (Tiên Đề II) | Nếp không đổi xuyên thời gian dù nội dung biểu hiện thay đổi |
| **nếp sống** | Living pattern / way of living | Nếp đang được thực hành hằng ngày — biểu hiện của nếp tổ chức |
| **nề nếp** | Inherited Patterns | Nếp được kế thừa qua mạch cội dọc từ nếp tổ chức quá khứ |
| **Mạch Cội Nguồn** | Orthogonal Temporality (Tiên Đề III) | Bản chất: hai chiều thời gian trực giao — Cội (dọc/V) ⊥ Nguồn (ngang/H) |

**Quy tắc chọn từ canonical (thứ tự ưu tiên):**

1. **Thuần Việt có sẵn, đúng phạm trù** → chọn (vd: "nếp" cho structural pattern, "Mạch Cội Nguồn" cho Orthogonal Temporality).
2. **Thuần Việt chưa có, ghép được từ các từ thuần Việt có sẵn** → ghép (vd: "nếp tổ chức" = nếp + tổ chức, "nếp bản sắc" = nếp + bản sắc).
3. **Không có thuần Việt tương đương** → giữ English technical term và ghi rõ "đây là thuật ngữ kỹ thuật chưa Việt hóa."
4. **Hán-Việt** → chỉ dùng khi từ đó đã thành khẩu ngữ Việt không thể thay thế (vd: "bản thể học" cho ontology — nhưng luôn kèm thuần Việt "mạch tồn tại" ở lần đầu xuất hiện).

**Quy tắc phân biệt phạm trù (category boundary):**

| ❌ Nhầm phạm trù | ✅ Đúng phạm trù | Lý do |
|---|---|---|
| "nếp" = "tập quán" (social convention) | "nếp" = cấu trúc sống (living structure) | Tập quán có thể mất mà hệ thống vẫn tồn tại; mất "nếp" → hệ thống sụp đổ |
| "nề nếp" = "tập tục" (traditional custom) | "nề nếp" = nếp được kế thừa (inherited structural patterns) | Tập tục là biểu hiện bề mặt; nề nếp là kiến trúc nền |
| Dùng "tập quán văn hóa" làm canonical term | Dùng "tập quán" làm explanatory gloss (từ phổ thông giúp định vị), canonical vẫn là "nề nếp" | Gloss ≠ synonym; gloss giúp người đọc tiếp cận, canonical giữ chính xác phạm trù |

> **Neo quan trọng:** "tập tục" và "tập quán" thuộc phạm trù **quy ước xã hội** (có thể đàm phán, biến đổi, thích nghi); "nếp" thuộc phạm trù **cấu trúc sống** (mất đi thì hệ thống sụp đổ — điều kiện cần cho tồn tại). Dùng từ sai phạm trù sẽ kéo toàn bộ Tiên Đề III từ ontological claim xuống sociological description. Chi tiết RCA tại `plan/dictionary_rule.md §10`.

### Document contract rules

- **Bảng Nguồn Trích Dẫn bắt buộc** (RCA finding 2026-06-10, score 4.8/5) — Mọi tài liệu có ≥ 1 trích dẫn nghiên cứu bên ngoài phải kết thúc bằng bảng "Nguồn Trích Dẫn" APA-formatted (xem Paper & Publication Rules Tier 3 Rule #12). Áp dụng cho tất cả file loại: `.html`, `.md`, paper manuscript, plan doc. Format ví dụ:
  > Udah, H., Tusasiirwe, S., Mugumbate, R., & Gatwiri, K. (2025). Ubuntu philosophy, values, and principles: An opportunity to do social work differently. *Journal of Social Work*, pp. 1–19. https://doi.org/10.1177/14680173241312749
- **Liên kết trích dẫn theo định dạng tài liệu (citation linking by format)** (RCA finding 2026-06-10, score 4.8/5):
  - **HTML:** mỗi trích dẫn inline phải là hyperlink `<a href="#nguon-N">[N]</a>` trỏ đến entry tương ứng trong bảng "Nguồn Trích Dẫn". Entry trong bảng phải có `id="nguon-N"` (N = số thứ tự nguồn). Không có hyperlink = tài liệu HTML chưa hoàn chỉnh.
  - **Mọi định dạng khác** (`.md`, `.tex`, manuscript, plan doc): dùng số thứ tự `[N]` inline trong văn bản; N tương ứng với thứ tự entry trong bảng "Nguồn Trích Dẫn".
- **CHANGELOG phân tầng — tiered changelogs** (RCA finding 2026-06-11, score 4.8/5; kế thừa papers/ instance từ RCA 2026-06-10, score 5.0/5):
  - **Quy tắc đặt tên:** `CHANGELOG_<tên-folder-chứa>.md` — ví dụ folder `mv_002` → `CHANGELOG_mv_002.md`; folder `papers` → `CHANGELOG_papers.md`; folder `paper_005` → `CHANGELOG_paper_005.md`. Ngoại lệ duy nhất: tầng root dùng `CHANGELOG.md` (không hậu tố).
  - **Vị trí:** file changelog nằm **trong chính folder đó**, không nằm nơi khác.
  - **Routing "phải và chỉ được":** mỗi thay đổi ghi vào changelog của **tầng gần nhất chứa file bị sửa** (nearest ancestor folder có file changelog), và **chỉ** vào đó — không ghi trùng lên tầng cha, không ghi vào root nếu đã thuộc tầng con nào. Root `CHANGELOG.md` là fallback cho mọi file không thuộc tầng con (axiom system, HTML nodes, audit plans, review documents, evidence enrichment, và infrastructure).
  - **Tạo tầng mới:** khi một folder cần lịch sử riêng, tạo file theo quy tắc đặt tên trên; header phải khai phạm vi + liên kết về `CHANGELOG.md` gốc (theo mẫu của `papers/CHANGELOG_papers.md`).
  - **Mỗi entry vẫn phải qua** 3-round RCA × 5-Why × scoring gate ≥ 4/5 (không đổi).
  - **Tầng hiện có (instances):** root → `CHANGELOG.md`; `papers/` → `papers/CHANGELOG_papers.md`; `papers/paper_005/` → `papers/paper_005/CHANGELOG_paper_005.md`; `publish/movie_script/mv_002/` → `publish/movie_script/mv_002/CHANGELOG_mv_002.md`.
- Use bilingual English/Vietnamese where appropriate across project documents; keep technical terminology, formal claims, and publication-facing text in technically precise English; communicate with the user in Vietnamese, keep English technical terms inside quotation marks, and explain concepts at a high-school level.
- Apply the mandatory principle "rebuild with carry-forward" (replaces the former "extend, not overwrite" rule; RCA finding 2026-06-06, score ≥ 4/5). For **unpublished / still-being-derived** content (the axiom system, internal mappings), clean overwrite and from-scratch re-derivation are **permitted** — preserving the old structure is not required. Binding condition: **before deleting or overwriting, declare an explicit "Carry-Forward Set"** — a named list of the assets (claims, definitions, falsification conditions, methodological compass) eligible to be carried over. Every item in the set is a *candidate that must survive re-validation through the RCA gate*, not an automatic keep; anything not in the set defaults to dropped (reference-only). For **published / externally-depended-upon** content, still prefer extend, and overwrite only when the user explicitly requests it. The default Carry-Forward Set lives in `plan/dictionary_rule.md §7`.

### Paper & Publication Rules

> Áp dụng khi viết, sửa, hoặc review bất kỳ paper nào trong `papers/`.

**Tier 1 — Project-specific frameworks (đọc trước khi viết):**

| Framework | File | Khi nào |
|---|---|---|
| **ESP Framework** | `papers/ESP_Framework_Scientific_Paper.md` | **Bắt buộc đọc.** Quy trình 3 lớp E→S→P (Epistemic→Structural→Presentational) cho mọi paper. Chứa RCA Stack, Claim Ladder, Sub-Question Architecture, Red Flag Audit, LLM Prompt Library. |
| **Einstein Writing** | `papers/einstein_writing_framework.md` | 6 nguyên tắc từ Einstein 1905: epistemic honesty, open with contradiction, intuition before formalism, structured sub-questions, minimal citation, bold reasoning + careful conclusions. |
| **RCA Scientific Paper** | `papers/SKILL_RCA_scientific_paper.md` | 5-layer RCA stack chuyên cho scientific paper. Claim Ladder (Analogy → Empirical). RCA Output Template. Red Flags list. |
| **Scientific Paper Writing** | `papers/SKILL_scientific_paper_writing.md` | Framing rules: never self-label, anchor→gap→extend, steel-man first, scope conservatively. Verb & hedge calibration table. 5-sentence abstract formula. |

**Tier 2 — Installed agent skills (routing theo giai đoạn):**

| Giai đoạn | Skill | Khi nào |
|---|---|---|
| Research & outline | `scientific-writing` | IMRAD structure, section drafting, reporting guidelines (CONSORT/STROBE/PRISMA), venue-specific style, LaTeX `scientific_report.sty` |
| Citations | `citation-management` | DOI → BibTeX, PubMed/Scholar search, metadata extraction, validation, dedup |
| Format conversion | `latex-paper-conversion` | Chuyển LaTeX giữa template journals (Springer → MDPI → IEEE…) |
| Literature lookup | `literature-search-arxiv`, `literature-search-europepmc`, `literature-search-openalex` | Tìm paper theo keyword, DOI, author |
| Deep research | `deep-research` | Autonomous research tasks: plan → search → read → synthesize |

**Tier 3 — Quy tắc bắt buộc:**

1. **ESP trước khi viết** — mọi paper phải qua Layer E (RCA Stack + Claim Ladder + Boundary Statement) TRƯỚC KHI viết prose. Không skip.
2. **RCA trước khi sửa claim** — mọi claim trong paper phải qua 3-round RCA × 5-Why × scoring gate ≥ 4/5 (cùng rubric §RULE ZERO ở trên).
3. **Phản chứng** — mỗi tiên đề / claim core phải kèm điều kiện bác bỏ (falsification condition) rõ ràng.
4. **Claim Ladder** — locate claim level (Analogy → Interpretive Mapping → Ontological Framework → Physical Model → Empirical Solution). Không viết trên mức evidence hỗ trợ.
5. **Boundary Statement** — mỗi paper phải có: "This paper does not claim…" + "This paper claims…" trong Introduction.
6. **Prose, không bullet** — bản nộp (manuscript) phải viết prose đầy đủ; bullet chỉ cho outline nội bộ (Stage 1 → Stage 2 workflow).
7. **Citation traceability** — mọi claim phải trace về nguồn; mark rõ `[established]` / `[contested]` / `[interpretation]` / `[analogy]` / `[hypothesis]`. Không bịa citation.
8. **Conservative form** — dùng "proposes", "may clarify", "one interpretation consistent with". KHÔNG dùng "revolutionary", "groundbreaking", "overturns", "proves" (trừ khi có formal proof).
9. **Bilingual** — thuật ngữ kỹ thuật giữ English; giải thích bằng Vietnamese khi cần. Formal claims bằng English.
10. **Avoid negatively evaluative wording** — không dùng "logical fallacy", "mistake", "wrong" khi nói về hệ khác. Dùng "scope boundary", "category boundary", "not implied by this framework".
11. **Author metadata** — file trong `papers/` (không nằm trong `public_documents/`) thêm dòng đầu: `Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/`
12. **Citation table — Bảng Nguồn Trích Dẫn** (RCA finding 2026-06-10, score 4.8/5) — Mọi tài liệu (paper, plan doc, HTML node, mapping doc) có ≥ 1 trích dẫn nghiên cứu bên ngoài **PHẢI** kết thúc bằng một bảng "Nguồn Trích Dẫn" ở cuối tài liệu. Không có bảng nguồn = tài liệu chưa hoàn chỉnh (không publish, không merge). Format canonical APA + DOI:
    > **Nguồn:** Tác giả, A., & Tác giả, B. (năm). Tên bài báo. *Tên tạp chí*, vol(issue), pp. x–y. https://doi.org/xxxxx
    - Áp dụng cho tài liệu **mới tạo hoặc được sửa** (không retroactive với tài liệu cũ chưa chỉnh).
    - Nếu tài liệu không có trích dẫn ngoài → ghi rõ "Tài liệu này không có trích dẫn nghiên cứu từ bên ngoài."
    - Phân biệt với Rule #7 (citation traceability = semantic level — mark `[established]`/`[hypothesis]`/…); Rule #12 là *output format* — bảng hiện diện ở cuối trang.

### Screenplay & Creative Writing Rules (RCA finding 2026-06-09)

> Điểm RCA: 5.0/5 (3-round × 5-Why × scoring gate). Áp dụng khi viết, sửa, hoặc review bất kỳ screenplay, story beat, character breakdown, hoặc opening image brief nào trong `publish/movie_script/`.

**Tier 1 — Project-specific frameworks (đọc trước khi viết):**

| Framework | File | Khi nào |
|---|---|---|
| **Zhang-Spielberg Hybrid v3** | `publish/movie_script/Zhang_Yimou_Spielberg_Hybrid_Screenplay_v3.md` | **Bắt buộc đọc. Luôn kích hoạt khi tạo kịch bản phim.** H×V unified framework grounded in Mach Re epistemology. Core: 4 Mach Re axioms in practice (Relational Ontology, Structural Invariance, Vertical Temporality, Dynamic Boundary). 5-phase Construction Protocol (Invariant Discovery → Character Architecture → Scene Construction → Dialogue Discipline → Ritual Architecture). 3 scene templates (A: H-axis primary, B: V-axis primary, C: Synthesis H meets V). Synthesis law: depth of V-axis wound = f(strength of H-axis bond). Color & Light Lexicon (6 registers). Music & Silence Protocol (Williams Trap + Silence Rule). 10-item Structural Invariant Checklist. Embedded reference files: hz-analysis (Spielberg 7 techniques vs Zhang 6 techniques, 9-dimension comparison), mach-re-axioms (all 8 axioms → screenplay application, Axiom V reflexive meta-check), scene-examples (annotated real-film scenes by template type — Schindler's List, Red Sorghum, Raise the Red Lantern, E.T., Saving Private Ryan). RCA finding 2026-06-11, score 5/5. |
| **Canonical 10 Slate v1** | `publish/movie_script/ideas/canonical_10_slate_v1.md` | 10 kịch bản đã RCA-gated (tất cả 5.0/5) — D1–D5, D9–D13: acute fractures. |
| **Canonical 10 Slate v2** | `publish/movie_script/ideas/canonical_10_slate_v2.md` | 10 kịch bản bổ sung (tất cả 5.0/5) — D6–D8, D14–D20: filling taxonomy gaps. |
| **Canonical 5 Erosion Slate** | `publish/movie_script/ideas/canonical_5_erosion_slate_v1.md` | 5 kịch bản V hao mòn (tất cả 5.0/5) — E1–E5: chronic erosion (không phải acute fracture). **Trục V vô danh bắt buộc.** Xem khi cần ý tưởng về sự biến mất chậm, không được để ý của V-axis. |

**Tier 2 — Quy tắc bắt buộc:**

1. **RCA trước khi viết idea mới** — mọi screenplay idea phải qua 3-round RCA × 5-Why × scoring gate ≥ 4/5, dùng rubric 5 tiêu chí: (C1) Axiom 3 core, (C2) Cinematic specificity, (C3) Everyday problem, (C4) Vietnamese rootedness, (C5) Originality gap.
2. **Show, don't tell** — Tiên Đề III không bao giờ được giải thích trong lời thoại. Nó là cấu trúc sinh drama, không phải theme/message.
3. **Antagonist as system** — kẻ phản diện là lực lượng kinh tế / xã hội / lịch sử / tập quán, không phải cá nhân ác.
4. **Specificity over universality** — không "truyền thống vs. hiện đại", mà là "cái bát sứ cụ thể này mà bà ngoại dùng để chia cháo."
5. **Constraint set** — Không chính trị · Không tôn giáo · UK/US cinematic language · Bối cảnh Việt Nam · Tiên Đề III là cấu trúc (không phải chủ đề).
6. **RCA traceability** — mọi screenplay entry phải ghi rõ 3-round RCA trace và điểm scoring, theo format chuẩn trong canonical slate.
7. **Falsification condition** — mỗi idea phải có điều kiện bác bỏ rõ ràng (khi nào idea fail).

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **Mach-Re** (3886 symbols, 3683 relationships, 0 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> If any GitNexus tool warns the index is stale, run `npx gitnexus analyze` in terminal first.

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `gitnexus_impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `gitnexus_detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `gitnexus_query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `gitnexus_context({name: "symbolName"})`.

## Never Do

- NEVER edit a function, class, or method without first running `gitnexus_impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `gitnexus_rename` which understands the call graph.
- NEVER commit changes without running `gitnexus_detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/Mach-Re/context` | Codebase overview, check index freshness |
| `gitnexus://repo/Mach-Re/clusters` | All functional areas |
| `gitnexus://repo/Mach-Re/processes` | All execution flows |
| `gitnexus://repo/Mach-Re/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->

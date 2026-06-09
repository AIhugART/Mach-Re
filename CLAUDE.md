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

### Tiên Đề III — Bản chất và Biểu hiện (RCA finding 2026-06-05)

> Phân tích gốc rễ (không phải hotfix). Điểm RCA: 5/5. Áp dụng bắt buộc trong mọi tài liệu, phát biểu, và so sánh triết học liên quan đến Tiên Đề III.

**Bản chất (Essence):** Thời gian trực giao (Orthogonal Temporality) — trục V và trục H là hai chiều kích thời gian **trực giao** (mathematically independent, irreducible to each other): `V ⊥ H`. Tính trực giao này là tính chất cấu trúc (structural property) nền tảng của Tiên Đề III — lý do duy nhất để phân biệt Tiên Đề III với "ký ức là một phần của hiện tại" (Halbwachs, Luhmann).

**Biểu hiện (Manifestation):** mạch cội dọc (Vertical Temporality) — hình thức mà tính trực giao hiện ra trong đời sống văn hóa xã hội: trục quan hệ tổ tiên ↕ hiện tại ↕ hậu thế. "Dọc" là cách đặt tên trực quan cho chiều trực giao đó, không phải định nghĩa cấu trúc.

**Quy tắc sử dụng thuật ngữ:**
- Khi phát biểu nguyên lý bản thể học → dùng **Orthogonal Temporality** (bản chất)
- Khi mô tả thực hành văn hóa / sơ đồ trực quan / so sánh đa văn hóa → dùng **Vertical Temporality** (biểu hiện)
- Hai thuật ngữ **không** thay thế nhau: chúng khác tầng (essence ≠ manifestation), không phải đồng nghĩa

### Tên thuần Việt các Tiên Đề (RCA finding 2026-06-05)

> Điểm RCA: 8/8 tiên đề đạt ≥ 4/5. Bảng canonical (nguồn chân lý duy nhất) tại `plan/dictionary_rule.md §9`.
> Format đầy đủ: `Tiên Đề [số] — [Biểu hiện thuần Việt] — [Bản chất thuần Việt] ("EN")`.

| # | Tầng | Biểu hiện | Bản chất |
|---|---|---|---|
| I | Core | Sống Trong Quan Hệ | Có Nhau Mới Có Mình |
| II | Core | Nếp Bản Sắc | Đổi Mà Vẫn Là Mình |
| III | Core | Mạch Cội Dọc | Mạch Cội Nguồn |
| IV | Core | Ranh Giới Mềm | Đóng Mở Có Chọn |
| V | Derived | Giữ Mà Không Gom | Ai Cũng Giữ Một Phần |
| VI | Derived | Hóa Nhiễu Thành Sức | Đau Được Xử Là Đau Lành |
| VII | Derived | Nổi Lên Có Hướng | Hợp Lại Thành Cái Mới |
| VIII | Meta | Tự Nhìn Thấy Mình | Soi Mình Mà Không Vỡ |

### Paper & Publication Rules (sourced from `papers/CLAUDE_REF.md`)

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

**Tier 3 — Quy tắc bắt buộc (carry-forward từ `papers/CLAUDE_REF.md`):**

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

### Screenplay & Creative Writing Rules (RCA finding 2026-06-09)

> Điểm RCA: 5.0/5 (3-round × 5-Why × scoring gate). Áp dụng khi viết, sửa, hoặc review bất kỳ screenplay, story beat, character breakdown, hoặc opening image brief nào trong `publish/movie_script/`.

**Tier 1 — Project-specific frameworks (đọc trước khi viết):**

| Framework | File | Khi nào |
|---|---|---|
| **Zhang-Spielberg Hybrid** | `publish/movie_script/Zhang_Yimou_Spielberg_Hybrid_Screenplay.md` | **Bắt buộc đọc.** 5 core principles (beauty as argument, silence over dialogue, individual small / weight enormous, loss without villain, acceptance as bravery), story architecture (3-act structure with precise emotional markers), character construction (3-layer: surface → personal wound → generational wound), scene-level guidelines (dialogue 3-pass reduction, silence as content, color as emotional score, objects as emotional proxies), tonal calibration, 5 output formats, 12-item checklist. |
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

### Document contract rules

- Use bilingual English/Vietnamese where appropriate across project documents; keep technical terminology, formal claims, and publication-facing text in technically precise English; communicate with the user in Vietnamese, keep English technical terms inside quotation marks, and explain concepts at a high-school level.
- Apply the mandatory principle "rebuild with carry-forward" (replaces the former "extend, not overwrite" rule; RCA finding 2026-06-06, score ≥ 4/5). For **unpublished / still-being-derived** content (the axiom system, internal mappings), clean overwrite and from-scratch re-derivation are **permitted** — preserving the old structure is not required. Binding condition: **before deleting or overwriting, declare an explicit "Carry-Forward Set"** — a named list of the assets (claims, definitions, falsification conditions, methodological compass) eligible to be carried over. Every item in the set is a *candidate that must survive re-validation through the RCA gate*, not an automatic keep; anything not in the set defaults to dropped (reference-only). For **published / externally-depended-upon** content, still prefer extend, and overwrite only when the user explicitly requests it. The default Carry-Forward Set lives in `plan/dictionary_rule.md §7`.

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **MACH_RE** (1794 symbols, 1987 relationships, 44 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

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
| `gitnexus://repo/MACH_RE/context` | Codebase overview, check index freshness |
| `gitnexus://repo/MACH_RE/clusters` | All functional areas |
| `gitnexus://repo/MACH_RE/processes` | All execution flows |
| `gitnexus://repo/MACH_RE/process/{name}` | Step-by-step execution trace |

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

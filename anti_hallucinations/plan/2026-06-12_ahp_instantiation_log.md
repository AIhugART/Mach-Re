Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# AHP Instantiation Log — MACH-RE
## Calibration Decision Record

**Plan reference:** `plan/2026-06-12_plan_ahp_installation.md`
**Template:** AHP v3.1 Template v1.0 (2026-06-12)
**Date started:** 2026-06-12
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5

---

## Decision Log

| # | Phase | File | Decision | Placeholder → Value | RCA score | Date |
|---|-------|------|----------|---------------------|-----------|------|
| 1 | P1 | README.md | Project name | `{{PROJECT_NAME}}` → `MACH-RE` | 5.0/5 | 2026-06-12 |
| 2 | P1 | index.md | Project scope | `{{PROJECT_SCOPE}}` → multi-system mapping scope | 5.0/5 | 2026-06-12 |
| 3 | P1 | index.md | Compass | `{{COMPASS}}` → Buddhist Epistemology (C of MACH RE) | 5.0/5 | 2026-06-12 |
| 4 | P1 | index.md | Systems mapped | → PN, AW, BE, MR | 5.0/5 | 2026-06-12 |
| 5 | P1 | All files | labels.md integration | Added as canonical confirmation SOT | 4.8/5 | 2026-06-12 |
| 6 | P1 | label_system.md | `[AH-NAJ]` label | Added 3rd confirmation label from labels.md #3 | 4.8/5 | 2026-06-12 |

---

## RCA Traces for Key Decisions

### Decision 5 — labels.md as canonical confirmation SOT

```
R1 (Symptom): AHP template has 2 confirmation labels (HCNF, AIHL) — binary.
  W1: Why only 2? Template assumes binary true/false judgment.
  W2: Why is binary problematic? F9 showed internally-consistent claims can be
      externally false — system needs "cannot judge" as valid state.
  W3: Why does labels.md already have this? labels.md #3 "No authority to judge"
      was created precisely to prevent false binaries.
  W4: Why not replace labels.md? labels.md is simpler (3 labels), already in use,
      and is the human-facing verdict layer. AHP adds middle layer feeding INTO it.
  W5 (Root): labels.md = verdict SOT; AHP = pipeline producing scored candidates.
      Category confusion between pipeline (how) and verdict (what).

R2 (Mechanism): Does declaring labels.md canonical create contradictions?
  No — AHP labels ([AH-HCNF], [AH-AIHL], [AH-NAJ]) are 1:1 encodings of
  labels.md #1, #2, #3. labels.md takes precedence in any discrepancy.

R3 (Root): Which internal standard requires this?
  Tiên Đề V: audit system must apply own standards to itself. Preserving
  labels.md (vs replacing) = framework obeying "extend, not overwrite"
  at the meta-audit level.

Score: 4.8/5 — Correct 1, Deep 1, Feasible 1, Conflict-risk 1, Preservation 1,
Provenance 0.8 ([proposed-by-this-project] integration pattern).
```

### Decision 6 — `[AH-NAJ]` label addition

```
R1 (Symptom): AHP template has no "cannot judge" label.
  W1: Why needed? Binary confirmation forces true/false on claims outside
      epistemic jurisdiction.
  W2: Why MACH RE specifically? F9: claim passed RCA 5.0/5 but externally false.
      Label #3 would have caught it pre-external-review.
  W3: Why does labels.md #3 solve this? "No authority to judge" = structural
      admission of epistemic limitation — ternary, not binary.
  W4: Why add to AHP vs keep only in labels.md? AHP decision tree must apply
      ternary logic systematically, not ad-hoc.
  W5 (Root): AHP binary model assumes authority to judge all claims. MACH RE's
      Tiên Đề V requires recognizing when it does not.

R2 (Mechanism): Does [AH-NAJ] create contradictions?
  No — confirmation label tier, same as HCNF/AIHL. Can coexist with any
  Primary label (e.g., AH-WARN + AH-NAJ = "risky but cannot judge").

R3 (Root): Internal standard?
  axiom_spec.md §0.6 kill condition #1 + Tiên Đề V applied to audit layer.

Score: 4.8/5 — Same pattern as Decision 5.
```

---

## Phase Completion Log

| Phase | Files created | RCA gate | Date |
|-------|--------------|----------|------|
| P1 — Bootstrap | README.md, index.md, instantiation_log.md | ✅ 3/3 | 2026-06-12 |
| P2 — System Registry | system_registry.md, mapping_registry.md | ✅ 2/2 | 2026-06-12 |
| P3 — Calibration | 05_scoring.md, vyapti_registry.md, stakes_assessment.md | ✅ 3/3 | 2026-06-12 |
| P4 — Pipeline | 01, 02, 03, 04, label_system, 06 | ✅ 6/6 | 2026-06-12 |
| P5 — Integration | integration_spec.md | ✅ 1/1 | 2026-06-12 |
| P6 — Finalize | CHANGELOG.md, CLAUDE.md | ✅ 2/2 | 2026-06-12 |

---

*Instantiation Log v1.0 — 2026-06-12. Records every calibration decision with RCA trace.*

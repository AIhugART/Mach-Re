Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# 02 — Component Detection & Inventory
## MACH-RE — 4-Group Origin Classification

**Role:** Classify every component by origin and assign initial ES tag + confirmation field referencing `labels.md`.
**Input:** Trigger from `01_early_warning.md` + component list.
**Output:** Inventory table with Group, ES tag, confirmation field.

---

## 1. 4-Group Origin Classification

| Group | Description | MACH RE Examples | Default ES Tag | Risk |
|-------|-------------|-----------------|---------------|------|
| **A (Standard)** | Pre-existing SOT concepts with direct source anchors | Axiom I–IV core claims; N_PN_00001–00030; N_AW_ASH_00001–00100; N_BE_00001–00030; labels.md #1-#3 | `[ES-PRATY]` | LOW |
| **B (Pre-existing, New Scope)** | Concepts existed before AHP, now under first systematic audit | Mệnh Đề 1–4; DSH-1/2/3; TRITHUC-1 through 10; BRIDGE-II-III | `[ES-ANUMA]` | MEDIUM |
| **C (New, Anchored)** | New concepts with SOT traceability at creation | AHP calibration anchors; Vyāpti Registry entries; NAC table entries; `[AH-NAJ]` entries | `[ES-ANUMA]` | MEDIUM |
| **D (New, Unanchored)** | New concepts without SOT trace — HIGHEST RISK | New axiom candidate without triangulation check; working-document claims | `[ES-VIKALP]` | **HIGH** |

---

## 2. Initial Component Inventory

| # | Comp ID | Name | System | Group | SOT Link | ES Tag | H Score | Confirmation (labels.md) |
|---|---------|------|--------|-------|----------|--------|---------|--------------------------|
| 1 | `AX_I` | Relational Ontology | MR | A | SOT-1 §I | `[ES-PRATY]` | 0 | `[AH-HCNF]` (#1) |
| 2 | `AX_II` | Structural Invariance | MR | A | SOT-1 §II | `[ES-ANUMA]` | 3 | `[AH-HCNF]` (#1) |
| 3 | `AX_III` | Orthogonal Temporality | MR | A | SOT-1 §III | `[ES-ANUMA]` | 4 | — |
| 4 | `AX_IV` | Dynamic Boundary | MR | A | SOT-1 §IV | `[ES-ANUMA]` | 3 | `[AH-HCNF]` (#1) |
| 5 | `AX_P1` | Distributed Identity | MR | B | SOT-1 §MĐ 1 | `[ES-ANUMA]` | 3 | — |
| 6 | `AX_P2` | Perturbation Transformation | MR | B | SOT-1 §MĐ 2 | `[ES-ANUMA]` | 3 | — |
| 7 | `AX_P3` | Directed Emergence | MR | B | SOT-1 §MĐ 3 | `[ES-ANUMA]` | 3 | — |
| 8 | `AX_P4` | Failure Conditions (F) | MR | B | SOT-1 §MĐ 4 | `[ES-ANUMA]` | 4 | — |
| 9 | `AX_V` | Reflexive Cognition | MR | A | SOT-1 §V | `[ES-ANUMA]` | 4 | — |
| 10 | `AX_VI` | Living Interface | MR | A | SOT-1 §VI | `[ES-ANUMA]` | 4 | — |
| 11 | `AX_DSH` | Diagnostic Heuristic | MR | B | SOT-1 §9 | `[ES-ANUMA]` | 5 | — |
| 12 | TRITHUC-1 | V ⊥ H Orthogonality | Gap | B | SOT-3 | `[ES-VIKALP]` | 6 | `[AH-NAJ]` (#3) |
| 13 | NAC_002 | Yogipratyakṣa | BE/C | C | SOT-8 N_BE_00012 | `[ES-PRATY]` (home) | 2 | — |
| 14 | NAC_003 | Design-as-Selection | AW/B | C | SOT-7 N_AW_ASH_00091 | `[ES-PRATY]` (home) | 2 | — |

> Confirmation field references `labels.md` label numbers. Blank = unjudged.

---

## 3. Detection Workflow

```
New/modified claim
  → 01_early_warning scan → signal match?
      YES → classify Group A/B/C/D → assign ES tag → add to inventory → route to 03
      NO  → document as Group A (pre-existing, verified)
```

---

*02_detection.md v1.0 — 14 initial components, 4-group classification. Instantiated from AHP Template v1.0 (2026-06-12).*

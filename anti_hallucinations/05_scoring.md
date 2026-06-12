Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# 05 — Hallucination Scoring Rubric
## MACH-RE Anti-Hallucination Pipeline

**Role:** 0-10 rubric for hallucination risk. Domain-calibrated for MACH RE multi-system mapping.
**Input:** Component + RCA from `04_analysis.md`.
**Output:** H score 0-10 + band classification.
**Complementarity:** AHP score (0-10) = hallucination RISK. RCA gate (≥ 4/5) = change DECISION. Both apply.

---

## 1. Scoring Rubric — 5 Bands

### Band 1 — Green (0-2): Verified / Standard

| Score | Criteria | MACH RE Calibration Anchor |
|-------|----------|--------------------------|
| **0** | Frozen axiom, direct SOT anchor ≥ 3 published sources | `AX_I`: "Identity = relations" — 3.0/3 triangulation A·B·C, `[established]` |
| **1** | Direct SOT trace ≥ 2 STRONG anchors, no new assumption | `N_PN_00010` (Relation vs. object) — source line verified |
| **2** | Pre-existing concept, fully documented lineage | `N_AW_ASH_00077` (Requisite Variety) — textbook, published 1956 |

### Band 2 — Blue (3-4): Low Risk / Framework-Grounded

| Score | Criteria | MACH RE Calibration Anchor |
|-------|----------|--------------------------|
| **3** | Framework-grounded extension, documented derivation chain | `AX_P2` — derived from II+III+IV, 3.0/3 triangulation |
| **4** | Valid inference from Pratyakṣa claims, ≥ 2 SOT anchors | `AX_P3` — derived from I+II+III+IV, all core axioms grounded |

### Band 3 — Yellow (5-6): Speculative but Flagged

| Score | Criteria | MACH RE Calibration Anchor |
|-------|----------|--------------------------|
| **5** | Speculative with explicit falsification conditions | `AX_DSH` (DSH-2) — `[empirical hypothesis]`, Phase 2 passed, DSH-F1/F2 stated |
| **6** | Weak anchor (1 SOT) OR single-compass triangulation | TRITHUC-5 (V as Ontological) — BRIDGE-II-III required, weak direct support |

### Band 4 — Orange (7-8): High Risk

| Score | Criteria | MACH RE Calibration Anchor |
|-------|----------|--------------------------|
| **7** | Trace ≤ 1/N, WEAK anchor, or category ambiguity | DSH-3 applied to non-Vietnamese system without recalibration |
| **8** | Near-orphaned: trace 0-1, no STRONG anchor, internal argument only | New axiom candidate without triangulation check in working document |

### Band 5 — Red (9-10): Critical / Fabricated

| Score | Criteria | MACH RE Calibration Anchor |
|-------|----------|--------------------------|
| **9** | Orphaned: trace=0, contradicts SOT, S18 violation | Claim `[established]` but actually `[proposed-by-this-project]` — F9 pattern |
| **10** | Confirmed AI-fabricated: `[AH-AIHL]` (labels.md #2) | "MACH RE solves Quantum Measurement" — category error, contradicts scope |

---

## 2. Scoring Formula

```
H = Base Score + Adjustment (clamped [0, 10])

Base Score:
  Trace score = 0          → Base 8
  Trace score = 1          → Base 6
  Trace score = 2-3        → Base 4
  Trace score = 4-5        → Base 2
  Trace score ≥ 6          → Base 0

Adjustments (cumulative):
  +1  if [ES-VIKALP]
  +1  if Signal R1-R5 fired (RED)
  +0  if Signal O1-O5 fired (ORANGE)
  -1  if [ES-PRATY] + ≥ 2 STRONG anchors
  -1  if triangulation ≥ 2.5/3
  -1  if [AH-HCNF] (labels.md #1)
  +2  if S20 fired (TIP violation) → auto ≥ 7
```

## 3. Example

```
Component: AX_I (Relational Ontology)
  Trace: 8/8 | ES: [ES-PRATY] | Triangulation: 3.0/3 | Signals: none | Confirmation: [AH-HCNF]
  Base: 0 (trace ≥ 6)
  Adjustments: -1 (ES-PRATY) -1 (triangulation ≥ 2.5) -1 (HCNF) = -3
  H = 0 → Band Green
```

---

## 4. Calibration Verification

**Before declaring any score:** verify against ≥ 2 calibration anchors in same band.
**Anchor recency:** Bands 1-2: annual | Band 3: 6-month | Bands 4-5: quarterly.

---

*05_scoring.md v1.0 — 5-band, 10-anchor MACH RE calibration. Instantiated from AHP Template v1.0 (2026-06-12).*

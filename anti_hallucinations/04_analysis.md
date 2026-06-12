Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# 04 — Root Cause Analysis (5-Whys + FSR)
## MACH-RE — 6 Root Cause Types + Falsifier Strength Rubric

**Role:** Trace hallucination symptoms to root cause using structured 5-Whys + FSR verification.
**Input:** Component + trace score from `03_sot_traceability.md`.
**Output:** Root cause (1 sentence, Type 1-6) + FSR score (≥ 9/12 = confirmed).

---

## 1. MACH RE Root Cause Types

| Type | Name | MACH RE Example | Typical Signal |
|------|------|----------------|---------------|
| **Type 1** | Category Error | "MACH RE solves Quantum Measurement" — epistemology ≠ physics | R1 |
| **Type 2** | Provenance Failure | `[proposed-by-this-project]` presented as `[established]` — F9 pattern | R5, S18 |
| **Type 3** | Triangulation Overstatement | "V ⊥ H strongly supported by all compasses" — actual 1.5/3 | O1 |
| **Type 4** | Temporal Decay | Ashby (1956) treated as "current consensus" without TTL re-verify | O4 |
| **Type 5** | Mapping Overreach | ANALOGY promoted to STRUCTURAL without new formal justification | R4, O3 |
| **Type 6** | Scope Violation | DSH-3 applied to Yoruba without re-measurement; institutional design conflated with emergent mechanism | Y2 |

---

## 2. 5-Whys Template

```
Component: [ID] | Signal: [R1-R5/O1-O5/Y1-Y5/S16-S20]

W1: Why does [symptom] appear? → [immediate cause]
W2: Why in this specific context?    → [mechanism]
W3: Why wasn't it caught?           → [gap in process/infrastructure]
W4: Why does it matter structurally? → [structural weakness]
W5 (Root — 1 sentence):             → [Type 1-6]

RCA Score: [X.X/5] (Correct, Deep, Feasible, Conflict-risk, Preservation, Provenance)
```

---

## 3. Worked Example — F9 Retraction

```
Component: "Triết học Tương quan-Phân tán" as [established]
Signal: R5 (Untagged Provenance) + S18 (Vikalpa as Pratyakṣa)

W1: Why trigger R5? → Term presented as established category without provenance tag.
W2: Why presented as established? → Internal RCA scored 5.0/5 on 5 criteria;
     no Provenance criterion existed → claim appeared internally consistent.
W3: Why wasn't it caught? → RULE ZERO criteria are internal consistency checks.
     None asks "does this exist in external literature?"
W4: Why structurally? → Without Provenance criterion, internally-consistent but
     externally-false claims pass every check. Systematic blind spot, not one-off.
W5 (Root): RULE ZERO's scoring gate lacked a Provenance criterion, allowing
     AI coinage to pass as [established] scholarship.
     → Type 2 (Provenance Failure)

RCA Score: 4.8/5 — Correct 1, Deep 1, Feasible 1, Conflict-risk 1, Preservation 1,
Provenance 0.8 (the analysis itself is [proposed-by-this-project])
```

---

## 4. FSR — Falsifier Strength Rubric (≥ 9/12 = Confirmed Hallucination)

| # | Criterion | Score (0-2) |
|---|-----------|------------|
| 1 | Falsification condition clearly stated | |
| 2 | Falsification condition is empirically testable | |
| 3 | Claim scope is explicitly bounded | |
| 4 | Alternative explanations listed and addressed | |
| 5 | Counter-evidence would be recognizable if present | |
| 6 | Claim does not rely on unfalsifiable assumptions | |
| **Total** | **(≥ 9/12 → confirmed)** | |

**Scoring:** 0 = absent, 1 = partial, 2 = fully satisfied.

---

## 5. RCA-to-Solution Routing

| Root Cause Type | Default Solution | Priority |
|----------------|-----------------|----------|
| Type 1 (Category Error) | Type 2 (SCOPE BOUNDARY) or Type 4 (REMOVE) | P0/P1 |
| Type 2 (Provenance Failure) | Type 1 (SOT ANCHOR) — add provenance tag | P0 |
| Type 3 (Triangulation Overstatement) | Type 3 (DOCUMENT) — downgrade language | P2 |
| Type 4 (Temporal Decay) | Type 1 (SOT ANCHOR) — TTL re-verify | P2 |
| Type 5 (Mapping Overreach) | Type 3 (DOCUMENT) — downgrade mapping_type | P1 |
| Type 6 (Scope Violation) | Type 2 (SCOPE BOUNDARY) or Type 5 (DEFER) | P2/P-DEFER |

---

*04_analysis.md v1.0 — 6 types, 5-Whys template, FSR rubric, worked F9 example. Instantiated from AHP Template v1.0 (2026-06-12).*

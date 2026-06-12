Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# Stakes Assessment — MACH-RE Claim Routing

**Role:** Stakes-based routing — determines pipeline depth BEFORE entering `01_early_warning`.
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5

---

## 1. Stakes Levels

| Level | Definition | MACH RE Examples | AHP Routing |
|-------|-----------|-----------------|-------------|
| **CRITICAL** | Affects classification, public claim, or framework integrity | Revising `AX_I` statement; retracting `[proposed-by-this-project]` claim; F9-class provenance failure | Full pipeline + **mandatory TIP-1** |
| **HIGH** | Affects top-risk ranking, structural framework, or gap registry | Adding axiom evidence; TRITHUC status change; mapping confidence change; `[AH-NAJ]` deferral | Full pipeline (01→06) |
| **MEDIUM** | Affects interpretive layer or mapping documentation | New mapping link; new NAC entry; DSH recalibration; VYR update | `03` + `05` minimum |
| **LOW** | Documentation, terminology, version metadata | Doc/terminology fix; version bump; README update | `01` scan only (R1-R5) |

---

## 2. MACH RE Claim Type → Stakes Default

| Claim Type | Default Stakes | Override |
|-----------|----------------|---------|
| Core axiom (I–IV) — statement revision | **CRITICAL** | Mandatory TIP-1 |
| Core axiom — evidence row addition | **HIGH** | → CRITICAL if contradicts triangulation |
| Derived proposition (1–4) — derivation revision | **CRITICAL** | Affects dependency chain |
| Meta/Interface axiom (V, VI) — revision | **CRITICAL** | Affects whole-system reflexivity |
| DSH — statement revision | **HIGH** | → CRITICAL if falsification triggered |
| DSH — recalibration (new sample) | **MEDIUM** | → HIGH if anchor changes |
| TRITHUC gap — status change (Open→Resolved) | **HIGH** | → CRITICAL if resolution changes axiom |
| TRITHUC gap — new gap identified | **MEDIUM** | — |
| Cross-system mapping link — new | **MEDIUM** | → HIGH if NAC reclassified |
| Mapping link — confidence change | **HIGH** | Affects triangulation scores |
| NAC entry — new | **MEDIUM** | → HIGH if previously force-mapped |
| **`[AH-NAJ]` (labels.md #3)** | **HIGH** | **DEFER — not BLOCKING** |
| Vyāpti Registry — new VYR | **MEDIUM** | — |
| Documentation / terminology fix | **LOW** | → MEDIUM if affects formal claim |
| AHP pipeline — version update | **LOW** | → MEDIUM if scoring formula changes |

---

## 3. Routing Rules

### CRITICAL — Full + TIP-1
`01→02→03→04→05→label→06 → [MANDATORY: Human TIP-1 → labels.md verdict] → 00 update`

### HIGH — Full Pipeline
As CRITICAL; TIP-1 recommended, not mandatory. `[AH-NAJ]` adds deferral step.

### MEDIUM — Minimum
`03→05 → IF score ≥ 7 escalate to HIGH → IF < 7 label + document`

### LOW — Scan Only
`01 (R1-R5 RED only) → IF RED escalate to MEDIUM → IF no RED proceed`

---

## 4. Override Conditions

| Override | Effect |
|----------|--------|
| R1-R5 RED fired | → **CRITICAL** |
| S20 fired (TIP violation) | → **CRITICAL** + mandatory TIP-1 |
| `[AH-CRIT]` / `[AH-AIHL]` (labels.md #2) | → **CRITICAL** + BLOCKING |
| `[AH-HIGH]` | → **HIGH** minimum |
| `[AH-NAJ]` (labels.md #3) | → **HIGH** with deferral — do NOT escalate |
| Top-risk record component | → **HIGH** minimum |

---

## 5. `[AH-NAJ]` Special Routing (labels.md #3)

1. Route as **HIGH** (full pipeline for documentation)
2. Solution: **DEFER** (Type 5) with explicit unlock condition
3. Priority: **P-DEFER** — tracked separately
4. Log in: `06_solution.md` P-DEFER + `00_top_risk_record.md` (TTL=Current)
5. Re-evaluate: unlock condition met OR quarterly

**This is NOT failure.** `[AH-NAJ]` = system recognizing its own limits per Tiên Đề V.

---

*Stakes Assessment v1.0 — 4 levels, 15 MACH RE claim types, [AH-NAJ] routing. Instantiated from AHP Template v1.0 (2026-06-12).*

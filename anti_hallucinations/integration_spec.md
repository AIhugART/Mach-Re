Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# Epistemic Integration Specification — MACH-RE AHP
## AHP ↔ MACH RE RCA Pipeline + labels.md

**Role:** How AHP maps into MACH RE RCA pipeline and labels.md.
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5

---

## 1. 3-Layer Architecture

```
Layer 1 — PROCESS:   RULE ZERO (CLAUDE.md)
                      5-step: Define→Trace→Isolate→Fix→Verify
                      3-round × 5-Why × scoring gate ≥ 4/5

Layer 2 — PIPELINE:  AHP (anti_hallucinations/)
                      01→02→03→04→05→label→06
                      Detection → ES tags → Trace → RCA → Scoring → Labels → Solutions

Layer 3 — VERDICT:   labels.md (project root)
                      [1] Human confirmed ← [AH-HCNF]
                      [2] AI hallucination ← [AH-AIHL]
                      [3] No authority to judge ← [AH-NAJ]
```

---

## 2. Layer Mapping

| AHP Component | MACH RE RCA | Relationship |
|---------------|------------|-------------|
| `01_early_warning` | Step 1 (Define) | Signals flag symptoms before RCA |
| `02_detection` (ES tag) | Step 2 (Trace) + Triangulation §7 | ES = epistemic provenance classification |
| `03_sot_traceability` | Step 3 (Isolate) | Trace score = anchor strength quantification |
| `04_analysis` (5-Whys) | Step 2–3 + 5-Why method | Standardized RCA recording |
| `05_scoring` (0-10) | Scoring gate (≥ 4/5) | **Complementary:** RCA = change decision; AHP = risk tracking |
| `label_system` — ES | Provenance tags | ES = epistemic layer; provenance = sociological layer |
| `label_system` — Confirmation | **labels.md** (SOT) | AHP labels = encoding; labels.md = canonical |
| `06_solution` (P0-P4) | Step 4 (Fix) + CHANGELOG | Standardized resolution tracking |
| `00_top_risk_record` | Step 5 (Verify) ongoing | Temporal tracking + re-audit cadence |

---

## 3. Critical Integration Rules

### Rule 1 — Dual Scoring
```
RCA gate (≥ 4/5):  "Should this claim be changed?"
AHP score (0-10):  "How risky is this claim right now?"

F9 pattern: RCA ≥ 4/5 + AHP ≥ 7 + labels.md unjudged → flag provenance review
```

### Rule 2 — labels.md Canonical
```
Confirmation: labels.md is SOT. Discrepancy → labels.md wins.
[AH-HCNF] = #1 | [AH-AIHL] = #2 | [AH-NAJ] = #3 (MACH RE addition)
```

### Rule 3 — Dual Tagging
```
Every claim: Provenance tag ([established]/[proposed-by-this-project]/[interpretation])
            + ES tag ([ES-PRATY]/[ES-ANUMA]/[ES-SMRTI]/[ES-VIKALP])
```

### Rule 4 — F9 Prevention
```
IF RCA ≥ 4/5 AND AHP ≥ 7 AND labels.md = unjudged
THEN → HIGH priority + mandatory TIP-1 BEFORE claiming [established]
```

---

## 4. TIP Protocol

| Level | Mechanism | Trigger |
|-------|-----------|---------|
| **TIP-1** | Independent human RCA | Every claim `[AH-WARN]`+ |
| **TIP-2** | SOT cross-reference | Every component |
| **TIP-3** | S20 detection | `[ES-ANUMA]`/`[ES-VIKALP]` claims |

**Independence:** AI cannot self-verify. Must have (a) human RCA or (b) independent SOT anchor.

---

## 5. TTL Mapping

| TTL_CLASS | MACH RE Application | Re-verify |
|-----------|--------------------|-----------|
| **Atemporal** | AX_I core; NAC home-system | Architecture revision |
| **Geological** | AX_II–IV, AX_P1–P4 | Compass revision |
| **Historical** | DSH, mapping links, folk evidence | New data |
| **Current** | TRITHUC gaps, `[proposed-by-this-project]` | Quarterly |

**Smṛti acceleration:** `[ES-SMRTI]` → TTL shifts 1 class faster.

---

## 6. RCA Design Verification

| Round | Score | Finding |
|-------|-------|---------|
| R1 — Independence | 4.8/5 | TIP + S20/S18 catch Vikalpa-as-Pratyakṣa. labels.md #3 = ternary escape. |
| R2 — Applicability | 5.0/5 | All mechanisms map to MACH RE. Compass C already integrated. |
| R3 — Root cause | 4.8/5 | Middle layer filled: detection→classification→scoring between process and verdict. |
| **Aggregate** | **4.87/5** | **PASS** (≥ 4/5) |

---

*Integration Spec v1.0 — 3 layers, 4 rules, TIP, TTL. Instantiated from AHP Template v1.0 (2026-06-12).*

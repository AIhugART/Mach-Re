Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# Stakes Assessment — {{PROJECT_NAME}} Claim Routing

**Role:** Stakes-based routing for {{PROJECT_NAME}} claims — determines pipeline depth before entering 01_early_warning.
**Usage:** Apply BEFORE pipeline (before 01_early_warning) to determine routing depth.
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5

---

## 1. Stakes Levels `[GENERIC structure — CALIBRATE examples for {{PROJECT_NAME}}]`

| Level | Definition | Examples in {{PROJECT_NAME}} `[CALIBRATE]` | AHP Routing |
|-------|-----------|------------------------------------------|-------------|
| **CRITICAL** | Change affects classification status, public claim, or framework integrity | `{{CRITICAL_EXAMPLE_1}}` | Full pipeline (01→06) + **mandatory human TIP-1** + AHP-SYNC if top-risk record changes |
| **HIGH** | Change may affect top-risk ranking or structural framework | `{{HIGH_EXAMPLE_1}}` | Full pipeline (01→06) |
| **MEDIUM** | Change in interpretive layer or postulate/mapping documentation | `{{MEDIUM_EXAMPLE_1}}` | 03_sot_traceability + 05_scoring minimum |
| **LOW** | Documentation, terminology, or version metadata change | `{{LOW_EXAMPLE_1}}` | 01_early_warning scan only (R1-R5 RED signals) |

---

## 2. Claim Routing Rules `[GENERIC]`

### 2.1 CRITICAL — Full Pipeline + TIP-1

```
[CRITICAL claim]
  → 01_early_warning (all 20 signals)
  → 02_detection (full inventory)
  → 03_sot_traceability (all SOTs)
  → 04_analysis (5-Whys + FSR)
  → 05_scoring
  → label_system
  → 06_solution
  → [MANDATORY: Human TIP-1 review]
  → 00_top_risk_record update + AHP-SYNC
```

### 2.2 HIGH — Full Pipeline (TIP-1 recommended, not mandatory)

### 2.3 MEDIUM — Minimum Path

```
[MEDIUM claim]
  → 03_sot_traceability → 05_scoring
  → IF score ≥ 7 → escalate to HIGH
  → IF score < 7 → label + document
```

### 2.4 LOW — Scan Only

```
[LOW claim]
  → 01_early_warning (R1-R5 RED signals only)
  → IF RED → escalate to MEDIUM
  → IF no RED → proceed
```

---

## 3. Stakes Classification Guide

### 3.1 How to determine Stakes Level `[GENERIC]`

Ask 3 questions in order:
1. Does this change affect classification status or any public-facing claim? → YES → **CRITICAL**
2. Does this affect top-risk scores, structural framework, or system-level architecture? → YES → **HIGH**
3. Does this affect interpretive mapping, postulate text, or core documentation? → YES → **MEDIUM**
4. Otherwise → **LOW**

### 3.2 Override Conditions `[GENERIC]`

| Override condition | Effect |
|--------------------|--------|
| Signal R1-R5 fired (RED) | Escalate to CRITICAL |
| Signal S20 fired (TIP violation) | Escalate to CRITICAL + mandatory TIP-1 |
| `[AH-CRIT]` label assigned | Escalate to CRITICAL + BLOCKING |
| `[AH-HIGH]` label assigned | Escalate to HIGH minimum |
| Top-risk record component involved | Escalate to HIGH minimum |

---

## 4. {{PROJECT_NAME}} Claim Type → Stakes Default `[CALIBRATE]`

| Claim Type | Default Stakes | Override |
|-----------|----------------|---------|
| `{{CLAIM_TYPE_CRITICAL_1}}` | CRITICAL | — |
| `{{CLAIM_TYPE_CRITICAL_2}}` | CRITICAL | — |
| `{{CLAIM_TYPE_HIGH_1}}` | HIGH | Escalate to CRITICAL if affects public claim |
| `{{CLAIM_TYPE_HIGH_2}}` | HIGH | — |
| `{{CLAIM_TYPE_MEDIUM_1}}` | MEDIUM | Escalate to HIGH if core anchor changes |
| Cross-system mapping link (new or revised) | MEDIUM | Escalate to HIGH if NAC classification affected |
| Documentation / terminology fix | LOW | Escalate if affects formal claim text |
| Version bump (semantic only) | LOW | — |

---

*Stakes Assessment — 4 levels, routing rules, override conditions. Exported from AHP v3.1 bds_stakes_assessment.md (4.33/5 PASS). Calibrate §1 and §4 for {{PROJECT_NAME}}.*

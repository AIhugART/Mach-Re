Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# Anti-Hallucination System — {{PROJECT_NAME}}

**System name:** {{PROJECT_NAME}} Anti-Hallucination Pipeline (AHP)
**Version:** v1.0 (YYYY-MM-DD)
**Scope:** {{PROJECT_SCOPE}} <!-- [CALIBRATE] e.g., "All layers of system {{SYS_A}} mapped to system {{SYS_B}}" -->
**Systems mapped:** {{SYS_A}}, {{SYS_B}} <!-- [CALIBRATE] list all N system codes -->
**Compass:** {{COMPASS}} <!-- [CALIBRATE] Default: Buddhist Epistemology (Pratyakṣa/Anumāna/Smṛti/Vikalpa) -->
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5
**BDS Integration:** Tier 1 FULL (CCL S16-S20, FSR rubric, ES tags) + Tier 2 SELECTIVE (TTL_CLASS, Vyāpti Registry, Stakes Assessment)
**Status:** INSTANTIATING <!-- Change to ACTIVE after self-audit (TEMPLATE_README.md §3) passes -->

> **Purpose:** Detect, analyze, score, and remove hallucination across all of {{PROJECT_NAME}}. This system standardizes the RCA process into an auditable pipeline.

---

## 1. Pipeline Overview `[GENERIC — do not modify structure]`

```
                      +-----------------------------------+
                      | 00_top_risk_record                |  <- Highest priority
                      | Risk Score = H x W x (1+A)        |     Re-audit weekly
                      | + TTL_CLASS tracking              |
                      +-----------------------------------+
                                        |
[BDS] stakes_assessment <- Routing depth (CRITICAL/HIGH/MEDIUM/LOW)
               |
               v
| 01_early_warning  |  20 signals (R1-R5, O1-O5, Y1-Y5, S16-S20)
               | TRIGGER
               v
| 02_detection      |  Component inventory + ES tag
               v
| 03_sot_traceability | SOT cross-reference + trace score  [BDS Vyāpti]
               v
| 04_analysis       |  5-Whys + FSR rubric ≥9/12          [BDS FSR]
               v
| 05_scoring        |  0-10 hallucination rubric
               v
| label_system      |  24 labels (Primary + Risk + ES + Confirmation + Secondary)
               v
| 06_solution       |  P0-P4 priority + resolution tracking

BDS v4.0 support: integration_spec.md | vyapti_registry.md | stakes_assessment.md
Multi-system:     system_registry.md  | mapping_registry.md
```

---

## 2. File Map `[CALIBRATE — update when files are added]`

### 2A. Pipeline Core (8 files)

| File | Role | When to use | Input | Output |
|------|------|-------------|-------|--------|
| `00_top_risk_record.md` | Top-N risk ranking, Risk Score H×W×(1+A), TTL_CLASS | Weekly re-audit + new component | All components | Risk ranking |
| `01_early_warning.md` | 20 early-warning signals | New claim/term/mapping | Claim text | Signal match + severity |
| `02_detection.md` | Component inventory + 4-group origin classification | On trigger from 01 | Component list | Inventory table |
| `03_sot_traceability.md` | SOT cross-reference matrix, trace score 0-N | After inventory | Component ID | Trace score + anchor strength |
| `04_analysis.md` | 5-Whys RCA, 6 root cause types, FSR rubric | Suspicious components | Component + trace score | Root cause (1 sentence) |
| `05_scoring.md` | 0-10 rubric, 5 bands, aggregate formula | Every component | Component + RCA | Score 0-10 |
| `label_system.md` | 24-label taxonomy + decision tree | After scoring | H + Risk Score + trace | Label(s) |
| `06_solution.md` | P0-P4 matrix, 5 solution types, resolution tracking | Score ≥ 5 | Score + root cause | Solution type + action |

### 2B. BDS v4.0 Support (3 files)

| File | Role | When to use |
|------|------|-------------|
| `integration_spec.md` | Layer mapping, TIP protocol, TTL definitions | Understanding integration |
| `vyapti_registry.md` | Claim type taxonomy + reliability priors | Checking claim reliability prior |
| `stakes_assessment.md` | Routing rules by stakes level | Routing new claims |

### 2C. Multi-System Files (2 files) `[CALIBRATE]`

| File | Role | When to use |
|------|------|-------------|
| `system_registry.md` | N systems × node/edge tables | Node/edge code lookup |
| `mapping_registry.md` | Cross-system links + NAC table | Recording/auditing mapping claims |

### 2D. Plan & Session Files `[CALIBRATE — add as created]`

| File | Role |
|------|------|
| `plan/` | Planning documents |

### 2E. External SOT Files `[CALIBRATE]`

| File (full path from repo root) | Role |
|----------------------------------|------|
| `{{SOT_PATH_1}}` | `{{SOT_1_DESCRIPTION}}` |
| `{{SOT_PATH_2}}` | `{{SOT_2_DESCRIPTION}}` |

---

## 3. Quick Reference `[GENERIC]`

| Situation | Start from |
|-----------|-----------|
| "Top-N highest-risk components?" | `00_top_risk_record.md` |
| "Claim seems ungrounded" | `01_early_warning.md` → signal registry |
| "Audit a whole file" | `02_detection.md` → component inventory |
| "What SOT anchors this component?" | `03_sot_traceability.md` |
| "Why is this claim wrong?" | `04_analysis.md` → 5-Whys |
| "Hallucination score?" | `05_scoring.md` → rubric |
| "What does label [AH-WARN] mean?" | `label_system.md` → taxonomy |
| "How to fix this?" | `06_solution.md` → priority matrix |
| "Node code for X?" | `system_registry.md` → node table for `{{SYS_X}}` |
| "Is this cross-system link justified?" | `mapping_registry.md` → mapping registry |

---

## 4. Design Principles `[GENERIC — 3-Round RCA Verified]`

| Principle | Rationale |
|-----------|-----------|
| **Extend, not overwrite** | Inherit Rule Zero; do not replace valid structure |
| **SOT-first** | Every claim must trace to ≥ 1 SOT |
| **Score before solve** | Score before proposing solutions |
| **Proportionality** | Simple → detection + scoring; complex → full pipeline |
| **Track resolution** | Every issue tracked to RESOLVED |
| **Compass, not cargo** | Epistemic framework guides RCA; do not import its structure as domain data |
| **Namespace integrity** | Each system's node/edge codes are independent — never merge |
| **Mapping = auditable claim** | Every cross-system link: mapping_type + justification + label |
| **NAC = valid result** | No-analogue means no forced mapping — record as NAC |

---

## 5. Version History `[CALIBRATE]`

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | YYYY-MM-DD | Initial instantiation from AHP Template v1.0 — {{PROJECT_NAME}} |

---

*{{PROJECT_NAME}} AHP — Compass: {{COMPASS}}. Instantiated from AHP Template v1.0 (2026-06-12).*

Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# Anti-Hallucination System — MACH-RE

**System name:** MACH-RE Anti-Hallucination Pipeline (AHP)
**Version:** v1.0 (2026-06-12)
**Scope:** All layers of system A·B·C mapped to MACH RE axioms; 10 TRITHUC gaps tracked; provenance audit across 3 compass systems; confirmation verdicts anchored to labels.md
**Systems mapped:** PN (Phan Ngọc), AW (Ashby/Weick), BE (Buddhist Epistemology), MR (MACH RE Axioms)
**Compass:** Buddhist Epistemology (Pratyakṣa / Anumāna / Smṛti / Vikalpa) — compass C of MACH RE
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5
**labels.md:** Canonical SOT for confirmation verdicts — `[AH-HCNF]` (#1), `[AH-AIHL]` (#2), `[AH-NAJ]` (#3)
**Status:** ACTIVE — self-audit passed (2026-06-12)

> **Purpose:** Middle layer connecting RULE ZERO (process) → labels.md (verdict). Standardized infrastructure for detecting, classifying, scoring, and tracking hallucination risk.

---

## Architecture: 3-Layer Model

```
RULE ZERO (process — CLAUDE.md)
       │
       ▼
╔══════════════════════════════════════════╗
║         AHP MIDDLE LAYER                 ║
║  01_early_warning ──→ phát hiện symptom  ║
║  02_detection      ──→ phân loại ES tag  ║
║  03_sot_traceability ──→ đo anchor strength║
║  04_analysis       ──→ truy vết root cause║
║  05_scoring        ──→ định lượng rủi ro  ║
║  00_top_risk_record ──→ theo dõi TTL      ║
║  label_system      ──→ gán nhãn chuẩn hóa ║
║  06_solution       ──→ theo dõi resolution║
╚══════════════════════════════════════════╝
       │
       ▼
labels.md (verdict — canonical SOT)
  [1] Human confirmed        ←── [AH-HCNF]
  [2] AI hallucination       ←── [AH-AIHL]
  [3] No authority to judge  ←── [AH-NAJ]
```

---

## 1. Pipeline Flow

```
                      +-----------------------------------+
                      | 00_top_risk_record                |  <- Highest priority
                      | Risk Score = H x W x (1+A)        |     Re-audit weekly
                      +-----------------------------------+
                                        |
[BDS] stakes_assessment ← Routing (CRITICAL/HIGH/MEDIUM/LOW)
               |
               v
| 01_early_warning  |  20 signals (R1-R5, O1-O5, Y1-Y5, S16-S20)
               | TRIGGER
               v
| 02_detection      |  Component inventory + ES tag + confirmation field
               v
| 03_sot_traceability | SOT cross-reference + trace score
               v
| 04_analysis       |  5-Whys + FSR rubric ≥9/12
               v
| 05_scoring        |  0-10 hallucination rubric
               v
| label_system      |  25 labels (Primary + Risk + ES + Confirmation + Secondary)
               v
| 06_solution       |  P0-P4 + P-DEFER priority + resolution tracking
```

---

## 2. File Map

### 2A. Pipeline Core (8 files)

| File | Role | When to use |
|------|------|-------------|
| `00_top_risk_record.md` | Risk ranking, Risk Score H×W×(1+A), TTL_CLASS | Weekly re-audit |
| `01_early_warning.md` | 20 early-warning signals | New claim/term/mapping |
| `02_detection.md` | Component inventory + 4-group classification | On trigger from 01 |
| `03_sot_traceability.md` | SOT cross-reference (N=8 internal) | After inventory |
| `04_analysis.md` | 5-Whys RCA, 6 root cause types, FSR rubric | Suspicious components |
| `05_scoring.md` | 0-10 rubric, 5 bands | Every component |
| `label_system.md` | 25-label taxonomy + decision tree | After scoring |
| `06_solution.md` | P0-P4 + P-DEFER, resolution tracking | Score ≥ 5 |

### 2B. BDS Support (3 files)

| File | Role |
|------|------|
| `integration_spec.md` | AHP ↔ MACH RE RCA Pipeline + labels.md |
| `vyapti_registry.md` | 9 VYR entries |
| `stakes_assessment.md` | Routing by stakes level |

### 2C. Multi-System (2 files)

| File | Role |
|------|------|
| `system_registry.md` | 4 systems (PN, AW, BE, MR) |
| `mapping_registry.md` | Cross-system links + NAC (5 entries) |

### 2D. Meta (4 files)

| File | Role |
|------|------|
| `README.md` | Instantiation guide + quick reference |
| `index.md` | This file |
| `plan/2026-06-12_ahp_instantiation_log.md` | Calibration decision log |
| `../plan/2026-06-12_plan_ahp_installation.md` | Authorizing plan (ARCHIVED) |

### 2E. External SOTs

| File | Role |
|------|------|
| `axiom_spec.md` | Framework core SOT |
| `labels.md` | Canonical confirmation verdict SOT |
| `documents/mapping/a_b_c_system_mapping.md` | A·B·C → axiom mapping SOT |
| `documents/gap/TRITHUC_index.md` | Gap registry SOT |
| `CLAUDE.md` | Rule system SOT |
| `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` | Compass A SOT |
| `documents/B_SYSTEM_Ashby_Weick/b_system_ashby_weick.md` | Compass B SOT |
| `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md` | Compass C SOT |

---

## 3. Quick Reference

| Situation | Start from |
|-----------|-----------|
| "Top-N highest-risk components?" | `00_top_risk_record.md` |
| "Claim seems ungrounded" | `01_early_warning.md` |
| "Audit a whole file" | `02_detection.md` |
| "What SOT anchors this?" | `03_sot_traceability.md` |
| "Why is this claim wrong?" | `04_analysis.md` |
| "Hallucination score?" | `05_scoring.md` |
| "What does label [AH-WARN] mean?" | `label_system.md` |
| "How to fix this?" | `06_solution.md` |
| "Node code for X?" | `system_registry.md` |
| "Is this cross-system link justified?" | `mapping_registry.md` |
| "Is this claim human-confirmed?" | `labels.md` (canonical SOT) |

---

## 4. Design Principles

| Principle | Rationale |
|-----------|-----------|
| **Extend, not overwrite** | Inherit Rule Zero; do not replace valid structure |
| **SOT-first** | Every claim must trace to ≥ 1 SOT |
| **Score before solve** | Score before proposing solutions |
| **Proportionality** | Simple → detection + scoring; complex → full pipeline |
| **Track resolution** | Every issue tracked to RESOLVED |
| **Compass, not cargo** | Epistemic framework guides RCA; do not import as domain data |
| **Namespace integrity** | Each system's node/edge codes are independent |
| **Mapping = auditable claim** | Every cross-system link: mapping_type + justification + label |
| **NAC = valid result** | No-analogue means no forced mapping |
| **labels.md = canonical** | Confirmation verdicts anchored to labels.md |

---

## 5. Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-06-12 | Initial instantiation from AHP Template v1.0 — MACH-RE. labels.md integrated as canonical confirmation SOT. `[AH-NAJ]` added. RCA 4.83/5. |
| v1.1 | 2026-06-13 | Correction per audit AF-1 (`plan/2026-06-13_plan_ahp_audit.md`): self-audit 2026-06-12 khai PASS sai ở check #1 (file count). `00_top_risk_record.md` bị bỏ sót khỏi phân rã phase — tạo ngày 2026-06-13. Văn bản v1.0 giữ nguyên; entry này là correction note. |

---

*MACH-RE AHP — Compass: Buddhist Epistemology. Instantiated from AHP Template v1.0 (2026-06-12). labels.md = canonical confirmation SOT.*

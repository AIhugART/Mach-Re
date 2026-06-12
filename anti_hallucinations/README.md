Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# AHP — Anti-Hallucination Pipeline for MACH RE
## Multi-System Mapping Audit Infrastructure

**Exported from:** AHP v3.1 (2026-06-12)
**Instantiated version:** v1.0 (2026-06-12)
**Language:** English-first, bilingual annotations in Vietnamese
**Compass:** Buddhist Epistemology (Pratyakṣa / Anumāna / Smṛti / Vikalpa) — compass C of MACH RE
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5
**Authorizing plan:** `plan/2026-06-12_plan_ahp_installation.md`

> **Purpose:** AHP là tầng giữa (middle layer) kết nối RULE ZERO (process) → labels.md (verdict). Cung cấp infrastructure chuẩn hóa để detect, classify, score, và track hallucination risk cho MACH RE: A (Phan Ngọc) · B (Ashby/Weick) · C (Buddhist Epistemology) → MACH RE Axioms (I–IV, 1–4, V, VI, DSH).
>
> **labels.md integration:** `labels.md` (project root) là canonical SOT cho confirmation verdicts. AHP thêm `[AH-NAJ]` (No Authority to Judge) derived từ labels.md label #3.

---

## Quick Reference

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

## File Inventory (17 files)

### Pipeline Core (8)

| # | File | Role |
|---|------|------|
| 1 | `00_top_risk_record.md` | Risk ranking, Risk Score H×W×(1+A), TTL_CLASS |
| 2 | `01_early_warning.md` | 20 signals (R1-R5, O1-O5, Y1-Y5, S16-S20) |
| 3 | `02_detection.md` | Component inventory + 4-group classification |
| 4 | `03_sot_traceability.md` | SOT cross-reference (N=8 internal SOTs) |
| 5 | `04_analysis.md` | 5-Whys RCA + 6 root cause types + FSR rubric |
| 6 | `05_scoring.md` | 0-10 rubric, 5-band calibration |
| 7 | `label_system.md` | 25-label taxonomy + decision tree |
| 8 | `06_solution.md` | P0-P4 + P-DEFER, 5 solution types |

### BDS Support (3)

| # | File | Role |
|---|------|------|
| 9 | `integration_spec.md` | AHP ↔ MACH RE RCA Pipeline + labels.md |
| 10 | `vyapti_registry.md` | 9 VYR entries |
| 11 | `stakes_assessment.md` | Routing by stakes level |

### Multi-System (2)

| # | File | Role |
|---|------|------|
| 12 | `system_registry.md` | 4 systems (PN, AW, BE, MR) |
| 13 | `mapping_registry.md` | Cross-system links + NAC (5 entries) |

### Meta (4)

| # | File | Role |
|---|------|------|
| 14 | `README.md` | This file |
| 15 | `index.md` | Master index |
| 16 | `plan/2026-06-12_ahp_instantiation_log.md` | Calibration decision log |
| 17 | `../plan/2026-06-12_plan_ahp_installation.md` | Authorizing plan |

### External SOTs

| File | Role |
|------|------|
| `axiom_spec.md` | Framework core SOT |
| `labels.md` | Canonical confirmation verdict SOT (3 labels) |
| `documents/mapping/a_b_c_system_mapping.md` | A·B·C → axiom mapping SOT |
| `documents/gap/TRITHUC_index.md` | Gap registry SOT |
| `CLAUDE.md` | Rule system SOT |
| `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` | Compass A SOT |
| `documents/B_SYSTEM_Ashby_Weick/b_system_ashby_weick.md` | Compass B SOT |
| `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md` | Compass C SOT |

---

## Self-Audit Checklist

| # | Check | Status |
|---|-------|--------|
| 1 | File count (17 total) | ☐ |
| 2 | Provenance stamp on all files | ☐ |
| 3 | Author metadata on all files | ☐ |
| 4 | No foreign calibration data | ☐ |
| 5 | System Registry (4 systems) | ☐ |
| 6 | SOT list (8 internal + 3 external) | ☐ |
| 7 | Scoring calibration (≥ 2 anchors/band) | ☐ |
| 8 | Vyāpti Registry (≥ 3 VYR) | ☐ |
| 9 | Mapping Registry + NAC table (5 entries) | ☐ |
| 10 | labels.md integration (4 cross-references) | ☐ |
| 11 | File Map complete | ☐ |

---

*AHP v3.1 — Instantiated for MACH-RE. Compass: Buddhist Epistemology. Multi-system: PN + AW + BE + MR. Authorized by plan/2026-06-12_plan_ahp_installation.md (RCA 4.83/5).*

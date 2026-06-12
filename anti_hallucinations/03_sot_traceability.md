Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# 03 — SOT Traceability Matrix
## MACH-RE — Single Source of Truth Cross-Reference (N=8)

**Role:** Measures how many SOTs anchor a component. Trace score = count of anchoring internal SOTs.
**Input:** Component ID from `02_detection.md`.
**Output:** Trace score 0-8 + anchor strength (STRONG/MODERATE/WEAK/ORPHANED).

---

## A. SOT Registry

### A.1 Internal SOTs (N = 8)

| SOT ID | Name | Path | Type |
|--------|------|------|------|
| **SOT-1** | Axiom Spec | `axiom_spec.md` | Framework core |
| **SOT-2** | A·B·C System Mapping | `documents/mapping/a_b_c_system_mapping.md` | Mapping SOT |
| **SOT-3** | TRITHUC Gap Index | `documents/gap/TRITHUC_index.md` | Gap registry |
| **SOT-4** | CLAUDE.md | `CLAUDE.md` | Rule system |
| **SOT-5** | **labels.md** | `labels.md` | **Confirmation verdict SOT** |
| **SOT-6** | A — Phan Ngọc | `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` | Compass A (68N/124E) |
| **SOT-7** | B — Ashby/Weick | `documents/B_SYSTEM_Ashby_Weick/b_system_ashby_weick.md` | Compass B (180N) |
| **SOT-8** | C — Buddhist Epistemology | `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md` | Compass C (255N) |

### A.2 External SOTs (bonus: +0.5 each)

| SOT ID | Reference | Type |
|--------|-----------|------|
| EXT-1 | Phan Ngọc (1998). *Bản sắc văn hóa Việt Nam*. NXB Văn hóa - Thông tin. | Published monograph |
| EXT-2 | Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall. | Published textbook |
| EXT-3 | Orton, J. D., & Weick, K. E. (1990). Loosely coupled systems: A reconceptualization. *AMR*, 15(2), 203–223. | Peer-reviewed paper |

---

## B. Anchor Strength Classification

| Classification | Trace Score | Meaning |
|---------------|------------|---------|
| **STRONG** | ≥ 4/8 | Multi-SOT; ≥ 2 different SOT types |
| **MODERATE** | 2-3/8 | Adequate; may be single-SOT-type |
| **WEAK** | 1/8 | Single anchor; conceptual only |
| **ORPHANED** | 0/8 | `[AH-ORPHAN]` + `[ES-VIKALP]` |

---

## C. Cross-Reference Examples

### AX_I (Relational Ontology)

| SOT-1 | SOT-2 | SOT-3 | SOT-4 | SOT-5 | SOT-6 | SOT-7 | SOT-8 | Trace | Anchor |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|
| ✅ §I | ✅ MAP_I | — | ✅ RULE ZERO | — | ✅ N_PN_00010 | ✅ N_AW_WEI_00001 | ✅ N_BE_00066 | **6/8** | **STRONG** |

### TRITHUC-1 (V ⊥ H Orthogonality)

| SOT-1 | SOT-2 | SOT-3 | SOT-4 | SOT-5 | SOT-6 | SOT-7 | SOT-8 | Trace | Anchor |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|
| ✅ §III | ✅ MAP_III | ✅ TRITHUC-1 | — | — | ⚠️ N_PN_00041 (manifestation) | ⚠️ N_AW_ASH_00071 (analogue) | ⚠️ N_BE_00026 (analogue) | **3/8** | **MODERATE** |

> ⚠️ = conceptual analogue, not direct anchor.

---

## D. Expected Trace by Component Type

| Component Type | Expected | Minimum | Action if Below |
|---------------|----------|---------|-----------------|
| Core axiom | ≥ 4/8 | 2/8 | Provenance review |
| Derived proposition | ≥ 3/8 | 2/8 | Check derivation chain |
| Heuristic (DSH) | ≥ 2/8 | 1/8 | Acceptable — single anchor permitted |
| TRITHUC gap | ≥ 1/8 | 0/8 | Low trace by definition |
| Mapping link | ≥ 2/8 | 1/8 | Home system + target SOT |
| NAC entry | ≥ 1/8 (home) | 1/8 | No analogue in others |
| `[proposed-by-this-project]` | ≥ 1/8 (framework) | 1/8 | axiom_spec.md minimum |

---

*03_sot_traceability.md v1.0 — N=8 internal SOTs + 3 external. Instantiated from AHP Template v1.0 (2026-06-12).*

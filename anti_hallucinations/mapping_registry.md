Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# Mapping Registry — MACH-RE Cross-System Links + NAC

**Role:** Central registry of all cross-system mapping links and No-Analogue Concepts (NAC). Every link is an auditable claim.

**SOT reference:** `documents/mapping/a_b_c_system_mapping.md` Part II.
**Cross-reference:** `system_registry.md` for node/edge codes; `03_sot_traceability.md` for SOT anchoring.

---

## 1. Mapping Type Definitions `[GENERIC]`

| mapping_type | Definition | When to use |
|-------------|------------|-------------|
| **ANALOGY** | Functional/structure similarity on different substrates | Default for cross-system mappings |
| **STRUCTURAL** | Formal correspondence demonstrated; relations preserved under transformation | Requires explicit formal mapping |
| **EQUIVALENCE-JUSTIFIED** | Identity via formal proof or published equivalence | Rare — not applicable in MACH RE domain |

**Default rule:** All cross-system mappings default to **ANALOGY** unless formal correspondence is demonstrated.

---

## 2. Mapping Links — A·B·C → MACH RE Axioms

> Source: `documents/mapping/a_b_c_system_mapping.md` Part II.

### 2.1 Core Axiom Mappings

| Map ID | Source Node | Target | mapping_type | justification | ground | AHP label | Status |
|--------|------------|--------|-------------|---------------|--------|-----------|--------|
| MAP_I_001 | `N_PN_00010` (Relation vs. object) | `AX_I` | **STRUCTURAL** | "Văn hóa không phải là một vật mà là một hệ thống những quan hệ" — direct relational ontology statement | PN | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_I_002 | `N_AW_WEI_00001` (Loose coupling) | `AX_I` | **STRUCTURAL** | "Elements responsive while retaining separateness and identity" — identity = relational | AW | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_I_003 | `N_BE_00066` (Anātmavāda) | `AX_I` | **STRUCTURAL** | "Non-self and non-substantialism" — no fixed self; identity is relational | BE | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_I_004 | `N_AW_ASH_00054` (Emergent property) | `AX_I` (humility) | **ANALOGY** | "Property of whole absent from parts" ≈ decentralized identity | AW | `[AH-LOW][ES-ANUMA]` | VERIFIED |
| MAP_II_001 | `N_PN_00003` (Cultural identity) | `AX_II` | **STRUCTURAL** | "Cái mặt bất biến của văn hóa... hệ thống quan hệ ổn định" — direct invariant pattern | PN | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_II_002 | `N_AW_ASH_00038` (Invariant) | `AX_II` | **STRUCTURAL** | "Property unchanged through series of changes" — formal invariant definition | AW | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_II_003 | `N_BE_00026` (Dvisatya) | `AX_II` (scope) | **ANALOGY** | Saṃvṛtisat ≈ pattern at conventional level. Structural analogue. | BE | `[AH-LOW][ES-ANUMA]` | VERIFIED |
| MAP_III_001 | `N_PN_00041` (Ancestor worship) | `AX_III` (manifestation) | **ANALOGY** | Thờ cúng tổ tiên = V-axis cultural manifestation. A provides practice evidence, not V ⊥ H formalization. | PN | `[AH-LOW][ES-ANUMA]` | VERIFIED |
| MAP_III_002 | `N_BE_00069` (Pratītyasamutpāda) | `AX_III` | **STRUCTURAL** | "Conditioned arising" — causal continuity across time; strongest neo for III | BE | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_III_003 | `N_AW_ASH_00071` (Survival as stability) | `AX_III` (V-as-ontological) | **ANALOGY** | Survival = pattern transmission across time. Structural analogue only. | AW | `[AH-LOW][ES-ANUMA]` | VERIFIED |
| MAP_IV_001 | `N_PN_00050` + `N_PN_00021` | `AX_IV` | **STRUCTURAL** | "Chủ động tiếp thu" + "Vượt gộp 3 giai đoạn" — direct selective permeability mechanism | PN | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_IV_002 | `N_AW_ASH_00077` (Requisite Variety) | `AX_IV` | **STRUCTURAL** | V_O ≥ V_D / V_R — formalizes selective permeability as variety management | AW | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_IV_003 | `N_BE_00015` (Apoha) | `AX_IV` | **ANALOGY** | Meaning through exclusion ≈ selective boundary. Semantic-level, not system-level. | BE | `[AH-LOW][ES-ANUMA]` | VERIFIED |

### 2.2 Derived Proposition Mappings (key excerpts)

| Map ID | Source Node | Target | mapping_type | justification | ground | AHP label | Status |
|--------|------------|--------|-------------|---------------|--------|-----------|--------|
| MAP_P1_001 | `N_PN_00029` + `N_PN_00057` | `AX_P1` | **STRUCTURAL** | Folk culture = vô danh, phi-tập-trung. Multi-dim org = distributed storage. | PN | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_P1_002 | `N_BE_00066` (Anātmavāda) | `AX_P1` | **STRUCTURAL** | No permanent unified self → distributed ontology | BE | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_P2_001 | `N_PN_00021` + `N_PN_00018` | `AX_P2` | **STRUCTURAL** | Vượt gộp + Độ khúc xạ = perturbation → growth mechanism | PN | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_P2_002 | `N_AW_ASH_00077` + `N_AW_ASH_00086` | `AX_P2` | **STRUCTURAL** | Requisite Variety + Ultrastability = perturbation handling | AW | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_P3_001 | `N_AW_ASH_00054` (Emergent property) | `AX_P3` | **STRUCTURAL** | "Property of whole absent from parts" — order without central control | AW | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_P3_002 | `N_BE_00069` (Pratītyasamutpāda) | `AX_P3` | **STRUCTURAL** | "Conditioned arising" — order from conditions, no controller | BE | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_P4_001 | `N_AW_ASH_00047` (Part-whole equilibrium) | `AX_P4` (F-AND-gate) | **STRUCTURAL** | "Each part has veto power" — multi-condition stability logic | AW | `[AH-LOW][ES-ANUMA]` | VERIFIED |
| MAP_P4_002 | `N_BE_00018` (Trairūpya) | `AX_P4` (F-AND-gate) | **ANALOGY** | Triple-condition validation. AND-gate = `[proposed-by-this-project]` | BE | `[AH-LOW][ES-ANUMA]` | VERIFIED |
| MAP_V_001 | `N_BE_00011` (Svasaṃvedana) | `AX_V` | **STRUCTURAL** | Self-cognition — strongest neo for V | BE | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_V_002 | `N_AW_ASH_00086` (Ultrastability) | `AX_V` | **ANALOGY** | Two-level feedback = self-observation mechanism | AW | `[AH-LOW][ES-ANUMA]` | VERIFIED |
| MAP_VI_001 | `N_BE_00069` (Pratītyasamutpāda) | `AX_VI` | **STRUCTURAL** | Duyên khởi in contact zone — strongest neo for VI | BE | `[AH-OK][ES-PRATY]` | VERIFIED |
| MAP_VI_002 | `N_PN_00037` (Đạo Nho Việt Nam) | `AX_VI` (P*) | **ANALOGY** | Confucianism → refraction → new product. Empirical case for P*. | PN | `[AH-LOW][ES-ANUMA]` | VERIFIED |
| MAP_VI_003 | `N_AW_ASH_00015` (Coupling) | `AX_VI` (P*) | **ANALOGY** | Coupling produces new system — formal analogue, not interface equivalence | AW | `[AH-LOW][ES-ANUMA]` | VERIFIED |

---

## 3. NAC Table — No-Analogue Concepts

> **Rule:** NAC = valid result. Never force-map a NAC — that is Vikalpa hallucination (Signal O3).

| NAC ID | Node | Home | Concept | Why no analogue | TRITHUC | Status |
|--------|------|------|---------|----------------|---------|--------|
| NAC_001 | — | AW/B | Formal Structural Boundary | C: non-attachment is ethical, not structural. PN: rich operational, not formalized. | TRITHUC-3 | DOCUMENTED |
| NAC_002 | `N_BE_00012` | BE/C | Yogipratyakṣa | PN + AW: no transcendental perception faculty. C-unique. | TRITHUC-7 | DOCUMENTED |
| NAC_003 | `N_AW_ASH_00091`–`00100` | AW/B | Design-as-Selection | PN + BE: no formal design-as-variety-reduction. B-unique (Ashby Ch.12-13). | TRITHUC-8 | DOCUMENTED |
| NAC_004 | `N_BE_00253` | BE/C | Anupalabdhi | PN + AW: no absence-as-evidence category. C-unique. | TRITHUC-9 | DOCUMENTED |
| NAC_005 | `N_PN_00029` + `N_PN_00030` | PN/A | Folk Epistemology | AW + BE: formal/scholastic, not folk. A-unique. | TRITHUC-10 | DOCUMENTED |

---

## 4. Mapping Statistics

| Metric | Value |
|--------|-------|
| Total mapping links | 26 |
| ANALOGY | 13 |
| STRUCTURAL | 13 |
| EQUIVALENCE-JUSTIFIED | 0 |
| NAC entries | 5 |
| TRITHUC gaps covered by NAC | 5/10 |

---

## 5. Critical Mapping Risks

| Risk | Map IDs | Issue | Re-audit |
|------|---------|-------|----------|
| III-orthogonality (V ⊥ H) | MAP_III_001–003 | `[proposed-by-this-project]` — no compass formalizes V ⊥ H | Quarterly |
| VI-C1 conditions | MAP_VI_001–003 | C1-graded reflexivity has no direct compass equivalent | When case studies added |
| F-AND-gate | MAP_P4_001–002 | `[proposed-by-this-project]` — AND-gate for identity failure | When historical cases analyzed |
| IV-C gap | MAP_IV_003, NAC_001 | Category boundary between epistemology (C) and cybernetics (B) | Acknowledged |

---

## 6. Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-06-12 | Initial instantiation. 26 mapping links imported from `a_b_c_system_mapping.md`. 5 NAC from TRITHUC gaps. |

---

*Mapping Registry v1.0 — 26 mapping links, 5 NAC entries, 4 critical risks. Instantiated from AHP Template v1.0 (2026-06-12).*

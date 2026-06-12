Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# System Registry — MACH-RE Multi-System Namespace

**Role:** Central registry of all 4 knowledge systems in MACH-RE. Defines namespace rules, node/edge code formats, and SOT references.

**Cross-reference:** `mapping_registry.md` for cross-system links; `03_sot_traceability.md` for SOT anchoring.

---

## 1. System Registration Table

| System ID | System Name | Short Name | SOT File Path | Namespace Prefix | Node Code Format | Edge Code Format | Status |
|-----------|------------|------------|---------------|------------------|-----------------|-----------------|--------|
| SYS-1 | Phan Ngọc — Bản Sắc Văn Hóa Việt Nam (1998) | PN | `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` | `N_PN_` | `N_PN_00001` | `ED_PN_00001` | ACTIVE |
| SYS-2 | Ashby/Weick — Cybernetics (1956) & Loose Coupling (1990) | AW | `documents/B_SYSTEM_Ashby_Weick/b_system_ashby_weick.md` | `N_AW_ASH_` / `N_AW_WEI_` | `N_AW_ASH_00001` | `ED_AW_ASH_00001` | ACTIVE |
| SYS-3 | Buddhist Epistemology — Pramāṇavāda (Dignāga/Dharmakīrti) | BE | `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md` | `N_BE_` | `N_BE_00001` | `ED_BE_00001` | ACTIVE |
| SYS-4 | MACH RE Axioms | MR | `axiom_spec.md` | `AX_` | `AX_I` | — | ACTIVE |

> **AW note:** SYS-2 has two sub-namespaces (Ashby + Weick). Both share SYS-2 registration.
> **MR note:** SYS-4 uses `AX_` prefix for axiom references. MR axioms are propositional, not graph-based.

---

## 2. Namespace Rule `[GENERIC]`

```
Every node/edge code across ALL systems MUST have a globally unique prefix.

N_PN_XXXXX ≠ N_AW_ASH_XXXXX ≠ N_AW_WEI_XXXXX ≠ N_BE_XXXXX
ED_PN_XXXXX ≠ ED_AW_ASH_XXXXX ≠ ED_AW_WEI_XXXXX ≠ ED_BE_XXXXX

Prefix encodes the home system. No global renumbering needed.
```

---

## 3. Node Definition Tables

### 3.1 SYS-1 — PN (Phan Ngọc): Top-20 Canonical

Source: `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` (68 nodes)

| Code | Name (EN) | Name (VI) | Definition | Source | Pre-existing? |
|------|-----------|-----------|------------|--------|---------------|
| `N_PN_00001` | Culture (operational) | Văn hóa (định nghĩa thao tác luận) | Relation between symbolic world and reality; manifests as mode of selection | TRANG 19, L281 | Y |
| `N_PN_00002` | Mode of selection | Kiểu lựa chọn | Distinct way individuals/peoples respond to common needs | TRANG 18, L261–L270 | Y |
| `N_PN_00003` | Cultural identity | Bản sắc văn hóa | Invariant face of culture through history; stable system of relations | TRANG 34, L453 | Y |
| `N_PN_00004` | Mentality | Tâm thức | Synthesis of 4 invariant needs: Nation, Family-Village, Status, Face | TRANG 7, L79–L95 | Y |
| `N_PN_00005` | Invariant needs | Nhu cầu bất biến | Inner needs that do not change; form stable relational system | TRANG 7, L67–L70 | Y |
| `N_PN_00010` | Relation (vs. object) | Quan hệ (vs. vật) | Culture = system of relations, not a thing | TRANG 6–7, L61–L67 | Y |
| `N_PN_00014` | Nation-centeredness | Tổ quốc luận | Nation as reference point for all moral judgment | TRANG 36–44, L470–L563 | Y |
| `N_PN_00015` | Family–Village | Gia đình–Làng xã | Family as protector; village as autonomous community | TRANG 71–72, L884–L898 | Y |
| `N_PN_00018` | Refraction index | Độ khúc xạ | Degree of change when thought/religion passes through another culture | TRANG 20–21, L292–L299 | Y |
| `N_PN_00019` | Cultural contact | Tiếp xúc văn hóa | Encounter between two cultures → blending of selection modes | TRANG 28, L371–L372 | Y |
| `N_PN_00021` | Aufheben/Dépassement | Vượt gộp | Absorb the new and renew it on basis of the old already renovated | TRANG 31, L399–L411 | Y |
| `N_PN_00024` | Personhood culture | Nhân cách luận | Person defined by position & duty in relations | TRANG 99–100, L1169–L1177 | Y |
| `N_PN_00028` | Self-governing commune | Công xã tự quản | Village self-governance: covenant, elected reps, land division | TRANG 65–66, L789–L797 | Y |
| `N_PN_00029` | Folk culture | Văn hóa dân gian | Rural commune culture: proverbs, folk songs, chèo, tuồng | TRANG 64, L779–L781 | Y |
| `N_PN_00041` | Ancestor worship | Thờ cúng tổ tiên | Foundational belief; all religions entering Vietnam take it as base | TRANG 104–106, L1230–L1253 | Y |
| `N_PN_00049` | Self-restraint | Tự kiềm chế | Limiting selfish ambitions; identity maintenance in contact | TRANG 26, L328 | Y |
| `N_PN_00050` | Active reception | Chủ động tiếp thu | Actively absorb what fits one's mentality | TRANG 47, L582 | Y |
| `N_PN_00057` | Multi-dim. village org. | Tổ chức làng xã đa chiều | Person belongs to multiple independent organizations simultaneously | TRANG 83–84, L995–L1002 | Y |
| `N_PN_00065` | Anti-assimilation strategy | Tiếp thu VH để chống đồng hóa | Absorb foreign culture to protect national sovereignty | TRANG 44–45, L550–L565 | Y |
| `N_PN_00068` | Multi-dim. relations | Quan hệ nhiều chiều | Expand relations with many nations; avoid one-sided dependence | TRANG 47, L585 | Y |

### 3.2 SYS-2a — AW (Ashby 1956): Top-15

Source: `documents/B_SYSTEM_Ashby_Weick/b_system_ashby_weick.md` Part A

| Code | Name (EN) | Definition | Source | Pre-existing? |
|------|-----------|------------|--------|---------------|
| `N_AW_ASH_00001` | Cybernetics | Science of control and communication; information-tight systems | Ashby L180–L183 | Y |
| `N_AW_ASH_00002` | Behaviouristic method | "What does it do?" — indifferent to material substrate | Ashby L192–L199 | Y |
| `N_AW_ASH_00009` | Transformation | Set of transitions defined by what happens, not why | Ashby L404–L420 | Y |
| `N_AW_ASH_00010` | Closure | Transform stays within operand set; no new element | Ashby L424–L432 | Y |
| `N_AW_ASH_00012` | State (of a machine) | Complete description at one moment; vector of variable values | Ashby L910–L930 | Y |
| `N_AW_ASH_00013` | Variety | Number of distinct elements; fundamental diversity measure | Ashby L3228–L3284 | Y |
| `N_AW_ASH_00014` | Constraint | Variety present < maximum; variables not independent | Ashby L3284–L3316 | Y |
| `N_AW_ASH_00015` | Coupling (of systems) | Output of one machine = input to another | Ashby L1379–L1455 | Y |
| `N_AW_ASH_00038` | Invariant | Property unchanged through series of changes | Ashby L1962–L1979 | Y |
| `N_AW_ASH_00042` | Disturbance | Transformation displacing system from current state | Ashby L2089–L2129 | Y |
| `N_AW_ASH_00043` | Stability (under disturbance) | System returns to equilibrium: lim TⁿD(a) = a | Ashby L2089–L2129 | Y |
| `N_AW_ASH_00054` | Emergent property | Property of whole absent from parts separately | Ashby L2920–L2976 | Y |
| `N_AW_ASH_00072` | Essential variables | Variables to keep within limits for survival | Ashby L4998–L5033 | Y |
| `N_AW_ASH_00077` | Law of Requisite Variety | V_O ≥ V_D / V_R; only variety destroys variety | Ashby L5200–L5260 | Y |
| `N_AW_ASH_00086` | Ultrastability | Two-level feedback: behavior loop + parameter-changing loop | Ashby L6060–L6102 | Y |

### 3.3 SYS-2b — AW (Weick 1990): Top-15

| Code | Name (EN) | Definition | Source | Pre-existing? |
|------|-----------|------------|--------|---------------|
| `N_AW_WEI_00001` | Loose coupling | Responsive yet separate; both determinacy and indeterminacy | Weick L66–L68 | Y |
| `N_AW_WEI_00002` | Dialectical interpretation | Simultaneously open/closed, indeterminate/rational | Weick L122–L159 | Y |
| `N_AW_WEI_00009` | Eight types of loose coupling | Individuals, subunits, organizations, levels, environments, ideas, activities, intentions-actions | Weick L276–L282 | Y |
| `N_AW_WEI_00010` | Preliminary model | Five-construct causal model | Weick L693–L803 | Y |
| `N_AW_WEI_00016` | Tightly coupled system | Responsiveness without distinctiveness | Weick L152–L153 | Y |
| `N_AW_WEI_00017` | Decoupled system | Distinctiveness without responsiveness | Weick L154–L155 | Y |
| `N_AW_WEI_00018` | Loosely coupled system | Both distinctiveness AND responsiveness simultaneously | Weick L155–L159 | Y |
| `N_AW_WEI_00021` | Causal indeterminacy | Unclear means-ends from bounded rationality, uncertainty | Weick L194–L213 | Y |
| `N_AW_WEI_00022` | Bounded rationality | Limited info-processing, obscured memory → idiosyncratic worlds | Weick L202–L213 | Y |
| `N_AW_WEI_00027` | Fragmented external environment | Dispersed stimuli or incompatible expectations | Weick L226–L262 | Y |
| `N_AW_WEI_00030` | Fragmented internal environment | Few participants involved in all operations | Weick L263–L262 | Y |
| `N_AW_WEI_00040` | Modularity | Low coupling = well-designed system | Weick L401–L420 | Y |
| `N_AW_WEI_00041` | Requisite variety (effect) | Capacity to register environmental inputs | Weick L384–L393 | Y |
| `N_AW_WEI_00052` | Persistence (organizational) | Long-term survival as outcome of loose coupling | Weick L527–L572 | Y |
| `N_AW_WEI_00065` | Five-construct model | Integrated causal model linking five voices | Weick L693–L803 | Y |

### 3.4 SYS-3 — BE (Buddhist Epistemology): Top-30 Core

Source: `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md`

| Code | Name (Skt.) | Name (EN) | Definition | Source | Pre-existing? |
|------|-------------|-----------|------------|--------|---------------|
| `N_BE_00001` | Pramāṇa | Valid cognition | Reliable knowledge source; four components | L17, L67–L71 | Y |
| `N_BE_00002` | Pratyakṣa | Direct perception | Immediate cognition, free from conceptual construction | L17, L159–L163 | Y |
| `N_BE_00003` | Anumāna | Inference | Indirect knowledge via logical sign (liṅga) | L17, L189–L207 | Y |
| `N_BE_00005` | Prameya | Object of cognition | Dual: svalakṣaṇa for perception, sāmānyalakṣaṇa for inference | L17, L141–L143 | Y |
| `N_BE_00006` | Bhrānti | Erroneous cognition | Mistaken apprehension; mirage as water | L151, L307–L311 | Y |
| `N_BE_00008` | Kalpanā/Vikalpa | Conceptual construction | Categorizing cognition; five word-types superimposed | L149–L151 | Y |
| `N_BE_00009` | Nirvikalpaka | Non-conceptual perception | Pure perception free from conceptual elaboration | L159–L161 | Y |
| `N_BE_00011` | Svasaṃvedana | Self-awareness | Reflexive self-cognition | L45 | Y |
| `N_BE_00013` | Svalakṣaṇa | Particular/Unique mark | Unique, causally efficacious, non-denotable | L141–L143 | Y |
| `N_BE_00014` | Sāmānyalakṣaṇa | Universal/General mark | Shared characteristic; no causal efficacy | L141–L143 | Y |
| `N_BE_00015` | Apoha | Exclusion | Meaning via exclusion: not-non-cow → cow | L27, L177–L181 | Y |
| `N_BE_00016` | Liṅga/Hetu | Sign/Logical reason | Inferential mark; evidence for probandum | L105, L191–L207 | Y |
| `N_BE_00018` | Trairūpya | Triple-condition syllogism | Three criteria for valid reason | L107, L209–L215 | Y |
| `N_BE_00019` | Vyāpti | Pervasion | Invariant relation between probans and probandum | L27, L177–L179 | Y |
| `N_BE_00021` | Svabhāvapratibandha | Essential relation | Tadutpatti (causality) + tādātmya (identity) | L27, L207 | Y |
| `N_BE_00022` | Arthakriyā | Causal efficacy | Ontological reality criterion + epistemological success | L73, L171–L173 | Y |
| `N_BE_00023` | Avidyā | Ignorance | Fundamental ignorance constructing phenomenal world | L23, L259–L263 | Y |
| `N_BE_00025` | Śūnyatā | Emptiness | Absence of inherent essence; Madhyamaka critique | L27 | Y |
| `N_BE_00026` | Dvisatya | Two truths | Conventional (saṃvṛti) vs. ultimate (paramārtha) | L67–L69 | Y |
| `N_BE_00029` | Kṣaṇabhaṅgavāda | Momentariness | Moment disappears as soon as it appears | L27, L147–L149 | Y |
| `N_BE_00066` | Anātmavāda | Non-self | Doctrine of non-self and non-substantialism | L19–L23 | Y |
| `N_BE_00069` | Pratītyasamutpāda | Dependent arising | Universal dynamic principle of conditioned arising | L23, L75, L295 | Y |
| `N_BE_00070` | — | Dependent arising (alt) | Conditioned arising — Buddha's fundamental insight | L23, L75, L295 | Y |
| `N_BE_00234` | Aviṣaṃvāditva | Reliability | Non-deceptiveness of cognition | L267–L271 | Y |
| `N_BE_00247` | — | Dharmakīrti's momentariness | Commitment to Sautrāntika momentariness | L303–L305 | Y |
| `N_BE_00250` | Tadutpatti | Causal production | Causal production — essential connection type | L303–L305 | Y |
| `N_BE_00251` | Tādātmya | Identity relation | Identity relation — essential connection type | L303–L305 | Y |
| `N_BE_00253` | Anupalabdhi | Non-perception | Non-perception replacing realist absence theory | L303–L305 | Y |
| `N_BE_00007` | Saṃśaya | Doubt | Doubt motivating pursuit of certainty | L81–L83 | Y |
| `N_BE_00012` | Alaukika | Transcendental perception | Meditational perception without external objects | L71 | Y |

### 3.5 SYS-4 — MR (MACH RE Axioms)

Source: `axiom_spec.md`

| Code | Name (EN) | Name (VI) | Type | Tier | Depends On | Triangulation |
|------|-----------|-----------|------|------|-----------|---------------|
| `AX_I` | Relational Ontology | Sống Trong Quan Hệ | Core Axiom | Object | — | 3.0/3 |
| `AX_II` | Structural Invariance | Nếp Bản Sắc | Core Axiom | Object | I | ~2.5/3 |
| `AX_III` | Orthogonal Temporality | Mạch Cội Nguồn | Core Axiom | Object | I, II | ~2.5/3 |
| `AX_IV` | Dynamic Boundary | Ranh Giới Mềm | Core Axiom | Object | I, II | ~2.5/3 |
| `AX_P1` | Distributed Identity | Giữ Mà Không Gom | Derived Prop. | Object | I, II | 3.0/3 |
| `AX_P2` | Perturbation Transformation | Hóa Nhiễu Thành Sức | Derived Prop. | Object | II, III, IV | 3.0/3 |
| `AX_P3` | Directed Emergence | Nổi Lên Có Hướng | Derived Prop. | Object | I, II, III, IV | 3.0/3 |
| `AX_P4` | Failure Conditions (F) | Đứt Khi Hết Cội | Derived Prop. | Object | II, III, IV | ~2.5/3 |
| `AX_V` | Reflexive Cognition | Soi Mình Mà Không Vỡ | Meta-Axiom | Meta | I, II, III, IV | ~2.5/3 |
| `AX_VI` | Living Interface | Gặp Nhau Giữ Gốc | Interface Axiom | Interface | V (both S1, S2) | 2.0/3 |
| `AX_DSH` | Diagnostic Heuristic | — | Heuristic | Diagnostic | II, IV, P4 | 2.0/3 |

---

## 4. System Statistics

| System | Short Name | Total Nodes | Total Edges | In Registry | Status |
|--------|-----------|------------|-------------|-------------|--------|
| Phan Ngọc (1998) | PN | 68 | 124 | 20 | ACTIVE |
| Ashby (1956) | AW-ASH | 100 | 108 | 15 | ACTIVE |
| Weick (1990) | AW-WEI | 80 | 80+ | 15 | ACTIVE |
| Buddhist Epistemology | BE | 30+225 | 39 | 30 | ACTIVE |
| MACH RE Axioms | MR | 11 | N/A | 11 | ACTIVE |

---

*System Registry v1.0 — 4 systems. Instantiated from AHP Template v1.0 (2026-06-12).*

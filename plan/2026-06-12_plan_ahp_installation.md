Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Kế Hoạch Cài Đặt AHP vào Mạch Rễ
## AHP Installation Plan for MACH RE

**Plan type:** installation
**Date:** 2026-06-12
**Status:** EXECUTED 2026-06-12 (commit efc919a) — AUDITED 2026-06-13, 4 findings (AF-1 CRITICAL, AF-2 HIGH, AF-3 HIGH, AF-4 MEDIUM), see `plan/2026-06-13_plan_ahp_audit.md`
**Target folder:** `anti_hallucinations/`
**Template source:** `anti_hallucinations/template/` (AHP Template v1.0, exported from AHP v3.1)
**Compass:** C — Buddhist Epistemology (Pratyakṣa / Anumāna / Smṛti / Vikalpa)
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5

**Reference files (READ-ONLY — not modified by this plan):**
- `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` — 68 nodes, 124 edges
- `documents/B_SYSTEM_Ashby_Weick/b_system_ashby_weick.md` — 100 Ashby nodes + 80 Weick nodes
- `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md` — 30 core + ~225 RCA nodes
- `documents/mapping/a_b_c_system_mapping.md` — A·B·C → MACH RE axioms (SOT mapping)
- `documents/gap/TRITHUC_index.md` — 10 triangulation gaps
- `axiom_spec.md` — Single Source of Truth for axiom system
- **`labels.md`** — **MACH RE canonical 3-label confirmation system (SOT for human verdict layer)**

**Related plans (reference only):**
- `plan/2026-06-12_plan_a_b_c_mapping.md` — A·B·C system mapping plan
- `plan/dictionary_rule.md` — canonical lookup table

---

# PART 0 — RCA DECISION: SHOULD AHP BE INSTALLED?

## 0.1 Decision Statement

**Question:** Should the Anti-Hallucination Pipeline (AHP v3.1 template) be instantiated and installed into the MACH RE project (`anti_hallucinations/`)?

**Candidate answer:** YES — instantiate all 15 template files + create 1 plan file + 1 instantiation log, integrating with the existing `labels.md` 3-label confirmation system as canonical anchor.

## 0.2 3-Round RCA

### Round 1 — Symptom: Why does MACH RE need AHP when it already has RULE ZERO + labels.md?

**Observed issue:** MACH RE already has a rigorous RCA pipeline (RULE ZERO: 5-step process, 3-round RCA × 5-Why × scoring gate ≥ 4/5, provenance tags) AND a canonical 3-label confirmation system (`labels.md`: Human confirmed / AI hallucination / No authority to judge). Adding a 24-label AHP taxonomy could be redundant.

**W1:** Why might MACH RE need AHP despite having both RULE ZERO and labels.md?
→ RULE ZERO is a **process** (method); `labels.md` is a **verdict layer** (3 confirmation states). AHP fills the gap between them: **detection → classification → scoring → verdict**. Currently MACH RE has the endpoints (process + verdict) but lacks the middle infrastructure (standardized signal detection, ES provenance classification, risk scoring, TTL tracking).

**W2:** Why is the missing middle a problem?
→ The TRITHUC index identifies 10 gaps with varying RCA levels, gap types, and resolution statuses. Without standardized tracking (TTL_CLASS, Risk Score, ES tags), each gap's status degrades — "🔓 Open" tells you nothing about *when* last checked, *what* would close it, or *how risky* it is. The 3-label system can only say "AI hallucination" or "Human confirmed" AFTER investigation — it cannot prioritize WHICH claims to investigate first.

**W3:** Why does temporal degradation matter even with labels.md?
→ The F9 retraction (2026-06-12) showed a claim scored 5.0/5 internally survived multiple RCA rounds because the scoring gate lacked a Provenance criterion. The gap wasn't detected by the process — it was found by external human check. AHP's Vyāpti Registry and TTL_CLASS tracking would have flagged `[ES-VIKALP]` risk on unverified provenance claims *before* external review. The 3-label system is a verdict, not a risk predictor — it's applied after the fact, not before.

**W4:** Why wasn't this gap caught by labels.md?
→ `labels.md` label #3 "No authority to judge" is the closest — but it's a human judgment call applied manually, not an automated signal triggered by structural patterns (like "claim has zero SOT trace"). For F9, the claim looked internally consistent (RCA 5.0/5 on 5 criteria) so no human would apply "No authority to judge" — the failure was in the criteria themselves (missing Provenance). AHP's S18 signal (Vikalpa passed as Pratyakṣa) would have caught it automatically.

**W5:** What is the root cause?
→ **Root cause (1 sentence):** RULE ZERO is a reasoning protocol, labels.md is a verdict layer — MACH RE lacks the **middle infrastructure** (detection signals, provenance classification, risk scoring) that connects process to verdict, leaving a gap where internally-consistent but externally-false claims pass through undetected.

### Round 2 — Mechanism: Why would AHP specifically address this root cause?

**W1:** Why AHP (vs. building custom)?
→ AHP is designed for multi-system mapping projects — exactly MACH RE's structure. It exports `[GENERIC]` sections as-is and has `[CALIBRATE]` sections to fill. Building custom would re-derive what exists.

**W2:** Why does the Buddhist Epistemology compass fit?
→ C is already compass C of MACH RE. ES tags (Pratyakṣa/Anumāna/Smṛti/Vikalpa) map to N_BE_00002, N_BE_00003, N_BE_00008. Not foreign — same epistemic framework.

**W3:** Why does AHP's confirmation layer need to integrate with labels.md?
→ `labels.md` has 3 canonical labels already in use. AHP's confirmation labels (`[AH-HCNF]`, `[AH-AIHL]`) map to labels #1 and #2. But label #3 "No authority to judge" has NO AHP equivalent — it's a MACH RE innovation. The plan must: (a) preserve labels.md as SOT, (b) map AHP confirmation labels to labels 1-2, (c) add `[AH-NAJ]` (No Authority to Judge) as a new AHP confirmation label derived from label #3, (d) make labels.md the canonical anchor for all confirmation-state verdicts.

**W4:** Why does NAC tracking matter specifically for MACH RE?
→ TRITHUC already identifies C-unique concepts (TRITHUC-7, 9) and B-unique concepts (TRITHUC-8). Currently in prose. AHP's NAC table makes them machine-trackable: "exists in X, absent in Y/Z, do not force-map."

**W5:** What mechanism does AHP add that the existing process→verdict pipeline alone cannot provide?
→ **Root cause (1 sentence):** AHP adds the missing middle layer — temporal persistence (TTL_CLASS), provenance classification (ES tags), cross-system gap documentation (NAC table), and risk-scored prioritization (Risk Score) — connecting RULE ZERO's reasoning protocol to labels.md's verdict layer through a standardized, auditable pipeline.

### Round 3 — Root: Which internal standard does MACH RE violate by NOT installing AHP?

**W1:** Which internal standard is at stake?
→ `axiom_spec.md §0.6` kill condition #4: "Tên loại hình `[proposed-by-this-project]` bị peer review bác bỏ." F9 showed internally-consistent claims can be externally false.

**W2:** Why a structural obligation?
→ Tiên Đề V (Soi Mình Mà Không Vỡ): framework must apply its own standards to itself. Identifying a gap (provenance tracking) + having access to a tool (AHP) + choosing NOT to install it = V-violation.

**W3:** Why root cause, not preference?
→ TRITHUC index: 10 gaps, all 🔓 Open, zero resolution dates. Gaps identified but never scheduled for re-audit. Tracking infrastructure failure, not knowledge failure.

**W4:** What if AHP is NOT installed?
→ Gaps remain 🔓 Open indefinitely. TTL_CLASS decay untracked. ES-VIKALP claims scored without provenance check. Next F9-type failure is a matter of *when*, not *if*.

**W5:** Deepest structural reason?
→ **Root cause (1 sentence):** Tiên Đề V (self-observation) + TRITHUC index (10 documented but untracked gaps) + labels.md (verdict layer without middle infrastructure) = structural requirement for AHP's detection→classification→scoring→verdict pipeline — refusing it without building an alternative violates the framework's own reflexivity standard.

## 0.3 Scoring Gate (≥ 4/5 required to proceed)

| Criterion | Question | Score | Reasoning |
|---|---|---|---|
| **Correct** | Is the need for AHP a genuine infrastructure gap? | **1/1** | Yes — TRITHUC: 10 gaps 🔓 Open, zero resolution dates. labels.md: 3 verdict labels with no detection/prioritization layer. RULE ZERO: process without tracking infrastructure. F9 retraction proves the gap is real. |
| **Deep** | Does the fix touch the root (middle layer), not just tone? | **1/1** | Yes — AHP adds TTL_CLASS, ES tags, NAC table, Vyāpti Registry, and Risk Score. Fills the process→verdict gap structurally. Preserves labels.md as canonical anchor. |
| **Feasible** | Can AHP be installed without breaking core structure? | **1/1** | Yes — template designed for instantiation. Reference files READ-ONLY. AHP sits in `anti_hallucinations/` as parallel audit layer. labels.md preserved as SOT for confirmation verdicts. |
| **Conflict-risk** | Will installation avoid creating contradictions? | **1/1** | Yes — AHP's compass (C/BE) is already MACH RE compass. ES tags map to N_BE_ nodes. labels.md label #3 ("No authority to judge") is added to AHP as `[AH-NAJ]` — no deletion, only extension. |
| **Preservation** | Is core strength (RULE ZERO + triangulation + labels.md) kept? | **1/1** | Yes — RULE ZERO remains highest rule. labels.md remains SOT for confirmation verdicts. AHP adds middle layer connecting them — does not replace either. |
| **Provenance** | Does every claim carry `[established]`+source or `[proposed-by-this-project]`? | **0.8/1** | The claim "AHP addresses MACH RE's middle-layer gap" is `[proposed-by-this-project]`. Evidence (TRITHUC gaps, F9, labels.md structure) is `[established]` within project. Slight deduction for self-referential meta-claim. |
| **TOTAL** | | **5.8/6** → **4.83/5** (normalized) | **≥ 4/5 → PROCEED.** |

---

# PART 1 — INSTALLATION OVERVIEW

## 1.1 Existing Assets (preserved, not replaced)

| Asset | Role | Fate in this plan |
|-------|------|-------------------|
| **RULE ZERO** (`CLAUDE.md`) | Highest mandatory RCA process | **Untouched.** AHP reads RCA outputs; does not replace the process. |
| **`labels.md`** | Canonical 3-label confirmation system (Human confirmed / AI hallucination / No authority to judge) | **Preserved as SOT.** AHP adds `[AH-NAJ]` derived from label #3. All AHP confirmation labels reference labels.md as canonical anchor. |
| **Triangulation Protocol** (`axiom_spec.md §7`) | 3-system neo-scoring | **Untouched.** AHP scoring is parallel (hallucination risk), not replacement (structural convergence). |
| **Provenance tags** (`[established]`, `[proposed-by-this-project]`, `[interpretation]`) | Claim provenance classification | **Preserved.** AHP ES tags add epistemic layer (how the claim was derived); provenance tags add sociological layer (where the claim sits in literature). Both apply. |
| **TRITHUC index** | 10 triangulation gaps | **Preserved.** AHP adds TTL_CLASS + Risk Score tracking per gap; NAC table cross-references gaps. |

## 1.2 The New Middle Layer

```
[TRƯỚC KHI CÀI AHP]
  RULE ZERO (process) ──────────────────────────→ labels.md (verdict)
                              ↑
                         KHOẢNG TRỐNG:
                   Không có detection signals
                   Không có provenance classification
                   Không có risk prioritization
                   Không có TTL tracking

[SAU KHI CÀI AHP]
  RULE ZERO (process)
       │
       ▼
  AHP MIDDLE LAYER:
   01_early_warning (20 signals) ──→ phát hiện symptom
   02_detection (ES tag)          ──→ phân loại provenance
   03_sot_traceability            ──→ đo anchor strength
   04_analysis (5-Whys + FSR)     ──→ truy vết root cause
   05_scoring (0-10 rubric)       ──→ định lượng rủi ro
   00_top_risk_record (TTL)       ──→ theo dõi temporal decay
       │
       ▼
  labels.md (verdict)
   [1] Human confirmed        ←── [AH-HCNF]
   [2] AI hallucination       ←── [AH-AIHL]
   [3] No authority to judge  ←── [AH-NAJ] (new — AHP derived)
```

## 1.3 What Gets Created

| # | New file | Instantiated from | Status after install |
|---|----------|-------------------|---------------------|
| 1 | `anti_hallucinations/index.md` | `template/template_index.md` | ACTIVE |
| 2 | `anti_hallucinations/00_top_risk_record.md` | `template/template_00_top_risk_record.md` | ACTIVE |
| 3 | `anti_hallucinations/01_early_warning.md` | `template/template_01_early_warning.md` | ACTIVE |
| 4 | `anti_hallucinations/02_detection.md` | `template/template_02_detection.md` | ACTIVE |
| 5 | `anti_hallucinations/03_sot_traceability.md` | `template/template_03_sot_traceability.md` | ACTIVE |
| 6 | `anti_hallucinations/04_analysis.md` | `template/template_04_analysis.md` | ACTIVE |
| 7 | `anti_hallucinations/05_scoring.md` | `template/template_05_scoring.md` | ACTIVE |
| 8 | `anti_hallucinations/06_solution.md` | `template/template_06_solution.md` | ACTIVE |
| 9 | `anti_hallucinations/label_system.md` | `template/template_label_system.md` | ACTIVE — **integrated with labels.md** |
| 10 | `anti_hallucinations/stakes_assessment.md` | `template/template_stakes_assessment.md` | ACTIVE |
| 11 | `anti_hallucinations/vyapti_registry.md` | `template/template_vyapti_registry.md` | ACTIVE |
| 12 | `anti_hallucinations/integration_spec.md` | `template/template_integration_spec.md` | ACTIVE |
| 13 | `anti_hallucinations/system_registry.md` | `template/template_system_registry.md` | ACTIVE |
| 14 | `anti_hallucinations/mapping_registry.md` | `template/template_mapping_registry.md` | ACTIVE |
| 15 | `anti_hallucinations/README.md` | `template/TEMPLATE_README.md` | ACTIVE |
| 16 | `anti_hallucinations/plan/2026-06-12_ahp_instantiation_log.md` | (new) | ACTIVE |
| 17 | `plan/2026-06-12_plan_ahp_installation.md` | (this file) | ARCHIVED after approval |

## 1.4 What Gets Modified

| File | Change | RCA |
|------|--------|-----|
| `CHANGELOG.md` | Add entry: AHP installation + integration with labels.md | Root-level changelog |
| `CLAUDE.md` | Add §Anti-Hallucination Pipeline — pointer to `anti_hallucinations/index.md` | Routing reference |

## 1.5 What Remains READ-ONLY

All 7 reference files (§header). AHP is a parallel audit layer reading from them, never writing.

---

# PART 2 — labels.md INTEGRATION (cross-cutting — affects all phases)

## 2.1 The Canonical 3-Label System

`labels.md` is the **Single Source of Truth** for confirmation verdicts in MACH RE:

| # | Tên | Meaning | AHP mapping |
|---|-----|---------|-------------|
| **1** | Human confirmed | Human reviewer explicitly confirmed; TIP-1 PASS documented | `[AH-HCNF]` — Human Confirmed |
| **2** | AI hallucination | Confirmed AI-fabricated: trace=0 + contradicts SOT + S20 + human verdict | `[AH-AIHL]` — AI Hallucination Confirmed |
| **3** | No authority to judge | System recognizes it lacks epistemic authority to judge this claim | **`[AH-NAJ]` — NEW AHP label** (derived from labels.md #3) |

## 2.2 AHP Label System Integration Rules

**Rule 1 — labels.md is canonical for confirmation verdicts:**
AHP's `label_system.md` §1.5 (Confirmation State Labels) SHALL declare `labels.md` as its canonical anchor. The AHP confirmation labels `[AH-HCNF]`, `[AH-AIHL]`, `[AH-NAJ]` are the AHP encoding of labels.md labels #1, #2, #3.

**Rule 2 — `[AH-NAJ]` is added to AHP:**
The AHP template has only 2 confirmation labels (`[AH-HCNF]`, `[AH-AIHL]`). A third label `[AH-NAJ]` (No Authority to Judge) is added during instantiation, derived from `labels.md` label #3. Trigger: human reviewer determines the system lacks the epistemic framework to evaluate this claim. Action: **DEFER** with unlock condition documented. Supersedes `[AH-WARN]` but does not block — the claim may be valid, the system simply cannot judge it.

**Rule 3 — Confirmation decision tree respects labels.md:**
```
After H score + ES tag + secondary labels:
  → Can a human reviewer judge this claim?
      YES → judge → [AH-HCNF] (label #1) or [AH-AIHL] (label #2)
      NO  → [AH-NAJ] (label #3) + defer with unlock condition
```

**Rule 4 — labels.md is referenced in every AHP file that emits confirmation labels:**
- `label_system.md` §1.5: Declares `labels.md` as canonical SOT for confirmation verdicts
- `06_solution.md`: `[AH-NAJ]` → Solution Type 5 (DEFER)
- `00_top_risk_record.md`: Confirmation column references labels.md label numbers
- `integration_spec.md`: Maps AHP confirmation labels → labels.md labels

## 2.3 Why labels.md Matters for AHP Design

| Design decision | Without labels.md | With labels.md |
|----------------|-------------------|----------------|
| Confirmation labels | 2 (HCNF, AIHL) — binary true/false | 3 (HCNF, AIHL, NAJ) — ternary with epistemic humility |
| Authority model | System claims authority to judge all claims | System explicitly marks claims it cannot judge |
| F9 prevention | Binary: claim is either hallucination or confirmed | Ternary: claim can be "outside our epistemic jurisdiction" — catching the exact class of errors where the system lacks the categories to detect its own mistakes |
| Epistemic humility | Implicit in RULE ZERO | **Structurally enforced** — label #3 is a permanent reminder that some claims require external authority |

> **RCA note:** Label #3 "No authority to judge" is a direct implementation of `axiom_spec.md §0.6` kill condition #1 ("Đối tượng tự đọc được mình không cần model") applied to the auditing layer itself: the audit system must know when it cannot audit something. This is Tiên Đề V (Soi Mình Mà Không Vỡ) at the meta-audit level.

---

# PART 3 — PHASE-BY-PHASE INSTALLATION PLAN

## Phase 1 — Project Identity & Bootstrap (files 1, 15, 16)

**Goal:** Set project identity, establish master index, create instantiation log.

### Step 1.1 — Create `anti_hallucinations/README.md`

Instantiate from `template/TEMPLATE_README.md`:
- `{{PROJECT_NAME}}` → `MACH-RE`
- Scope → `Multi-system mapping: A (Phan Ngọc) · B (Ashby/Weick) · C (Buddhist Epistemology) → MACH RE Axioms (I–IV, 1–4, V, VI, DSH)`
- Add to §2 File Inventory: reference to `labels.md` as canonical confirmation SOT
- Record AHP v3.1 instantiation; reference this plan

### Step 1.2 — Create `anti_hallucinations/index.md`

Instantiate from `template/template_index.md`:
- `{{PROJECT_NAME}}` → `MACH-RE`
- `{{PROJECT_SCOPE}}` → `All layers of system A·B·C mapped to MACH RE axioms; 10 TRITHUC gaps tracked; provenance audit across 3 compass systems; confirmation verdicts anchored to labels.md`
- `{{COMPASS}}` → `Buddhist Epistemology (Pratyakṣa / Anumāna / Smṛti / Vikalpa) — compass C of MACH RE`
- Systems mapped: `PN, AW, BE, MR`
- Add to §2E External SOT: `labels.md` — MACH RE canonical confirmation labels
- Status: `ACTIVE` after self-audit

### Step 1.3 — Create `anti_hallucinations/plan/2026-06-12_ahp_instantiation_log.md`

New file — records every calibration decision with RCA trace.

**RCA gate for Phase 1:** All 3 files with correct project identity, labels.md reference, provenance stamps → PASS.

---

## Phase 2 — System Registry (files 13, 14)

**Goal:** Register all 4 systems with node/edge tables and cross-system mapping links.

### Step 2.1 — Create `anti_hallucinations/system_registry.md`

4 systems:

| System ID | System Name | Short Name | SOT File | Namespace Prefix |
|-----------|------------|------------|----------|-----------------|
| SYS-1 | Phan Ngọc — Bản Sắc Văn Hóa Việt Nam | PN | `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` | `N_PN_` |
| SYS-2 | Ashby/Weick — Cybernetics & Loose Coupling | AW | `documents/B_SYSTEM_Ashby_Weick/b_system_ashby_weick.md` | `N_AW_ASH_` / `N_AW_WEI_` |
| SYS-3 | Buddhist Epistemology — Pramāṇavāda | BE | `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md` | `N_BE_` |
| SYS-4 | MACH RE Axioms | MR | `axiom_spec.md` | `AX_` |

Node tables: reuse top-20 per system from `a_b_c_system_mapping.md` Part I.

### Step 2.2 — Create `anti_hallucinations/mapping_registry.md`

**Mapping links:** Import all Part II mapping rows from `a_b_c_system_mapping.md`. Each row:
- `mapping_type`: `ANALOGY` (default) / `STRUCTURAL` (formal correspondence) / `EQUIVALENCE-JUSTIFIED` (rare)
- `justification`: one sentence
- `ground_system`: which compass provides reference frame
- `AHP label`: `[ES-ANUMA]` + boundary note

**NAC table (No-Analogue Concept) — 5 entries from TRITHUC:**

| NAC ID | Node | Home System | Why no analogue | TRITHUC ref |
|--------|------|-------------|-----------------|-------------|
| NAC_PN_AW_001 | Formal Structural Boundary (IV) | AW/B | C has non-attachment (ethical), not structural boundary | TRITHUC-3 |
| NAC_AW_PN_001 | Yogipratyakṣa | BE/C | A and B have no transcendental perception faculty | TRITHUC-7 |
| NAC_PN_BE_001 | Design-as-Selection | AW/B | A and C have no formal design-as-variety-reduction framework | TRITHUC-8 |
| NAC_AW_PN_002 | Anupalabdhi (Absence Cognition) | BE/C | A and B have no absence-as-evidence category | TRITHUC-9 |
| NAC_AW_BE_001 | Folk Epistemology | PN/A | B and C are formal/scholastic, not folk | TRITHUC-10 |

**RCA gate for Phase 2:** 4 systems registered; NAC table (5 entries); all mapping links have 4-column entry → PASS.

---

## Phase 3 — Calibration Anchors (files 7, 10, 11)

**Goal:** Domain-specific calibration anchors for MACH RE.

### Step 3.1 — Create `anti_hallucinations/05_scoring.md`

**5-band calibration anchors:**

| Band | Score | MACH RE Anchor Example | Rationale |
|------|-------|----------------------|-----------|
| **Band 1 (Green)** | 0-2 | Axiom I core — "Identity = relations" triangulated 3.0/3 across A·B·C with `[established]` sources | Direct SOT anchor, no new assumption |
| **Band 2 (Blue)** | 3-4 | Mệnh Đề 2 — "Perturbation → growth" derived from II+III+IV with strong triangulation | Framework-grounded extension, documented lineage |
| **Band 3 (Yellow)** | 5-6 | DSH-2 (Depth-Dependent Filtering) — `[empirical hypothesis]`, Phase 2 passed, Phase 3 pending | Speculative but flagged, falsification conditions stated |
| **Band 4 (Orange)** | 7-8 | TRITHUC-5 (V as Ontological Dimension) — requires BRIDGE-II-III transcendental argument; no direct compass support | Weak foundation, sustained by philosophical argument only |
| **Band 5 (Red)** | 9-10 | "MACH RE solves Quantum Measurement" — category error between epistemology and physics | Orphaned — no SOT anchor, contradicts scope boundary |

### Step 3.2 — Create `anti_hallucinations/vyapti_registry.md`

**9 VYR entries for MACH RE claim types:**

| VYR | Claim Type | Detection Pattern | ES Tag | Reliability Prior | TTL_CLASS |
|-----|-----------|-------------------|--------|-------------------|-----------|
| VYR-1 | Core axiom with 3.0/3 triangulation | triangulation score 3.0, `[established]` sources ≥ 3 | `[ES-PRATY]` | HIGH | Atemporal |
| VYR-2 | Core axiom with 1.5-2.5/3 triangulation | triangulation score 1.5-2.5, mixed provenance | `[ES-ANUMA]` | HIGH | Geological |
| VYR-3 | Derived proposition | "derived from", "suy từ", depends_on chain | `[ES-ANUMA]` | HIGH | Geological |
| VYR-4 | Heuristic (DSH) | "heuristic", "empirical hypothesis", "useful tool" | `[ES-ANUMA]` | MEDIUM | Historical |
| VYR-5 | TRITHUC gap (unresolved) | "🔓 Open", "proposed-by-this-project" | `[ES-VIKALP]` | LOW | Current |
| VYR-6 | Cross-system mapping link | "↔", "mapping_type", "ANALOGY" | `[ES-ANUMA]` + boundary | MEDIUM | Historical |
| VYR-7 | NAC entry | "no analogue", "NAC_", "do not force-map" | `[ES-PRATY]` (home system) | HIGH | Atemporal |
| VYR-8 | `[proposed-by-this-project]` claim | "proposed-by-this-project", novel contribution | `[ES-ANUMA]` | LOW | Current |
| VYR-9 | Vietnamese cultural manifestation | "ca dao", "tục ngữ", "thờ cúng tổ tiên" | `[ES-SMRTI]` | MEDIUM | Historical |

### Step 3.3 — Create `anti_hallucinations/stakes_assessment.md`

**MACH RE claim type → stakes mapping (incorporates labels.md label #3):**

| Claim Type | Default Stakes | Override |
|-----------|----------------|---------|
| Core axiom (I–IV) — revision to statement | CRITICAL | Mandatory TIP-1 |
| Core axiom — adding evidence row | HIGH | — |
| Derived proposition (1–4) — revision to derivation | CRITICAL | Affects logical dependency chain |
| Meta/Interface axiom (V, VI) — revision | CRITICAL | Affects whole-system reflexivity |
| DSH — revision | HIGH | Affects diagnostic operationalization |
| TRITHUC gap — status change (Open → Resolved) | HIGH | Affects gap registry integrity |
| Cross-system mapping link — new | MEDIUM | Escalate to HIGH if NAC reclassified |
| Cross-system mapping link — confidence change | HIGH | Affects triangulation scores |
| NAC entry — new | MEDIUM | Escalate to HIGH if previously force-mapped |
| Claim triggering `[AH-NAJ]` (labels.md #3) | HIGH | **DEFER — not BLOCKING.** Document unlock condition. |
| Documentation / terminology fix | LOW | Escalate if affects formal claim text |

**RCA gate for Phase 3:** 5 bands with ≥ 2 anchors; 9 VYR entries; stakes table includes `[AH-NAJ]` routing → PASS.

---

## Phase 4 — Pipeline Files (files 3, 4, 5, 6, 8, 9)

**Goal:** Fill pipeline files with MACH RE content, labels.md reference throughout.

### Step 4.1 — Create `anti_hallucinations/01_early_warning.md`

**20 signals with MACH RE examples:**

**RED (R1-R5) — Hallucination:**
- R1 (Category error): "MACH RE solves Quantum Measurement" → epistemology ≠ physics
- R2 (Absolute claim): "proves", "revolutionary", "overturns" → violates conservative form rule
- R3 (Self-scored number without rubric): "RCA score 5.0/5" without 5-criterion breakdown
- R4 (Equivalence without justification): PN concept = AW concept without mapping_type
- R5 (Untagged provenance): Typology/history claim without `[established]`/`[proposed-by-this-project]` → F9-class

**ORANGE (O1-O5) — Warning:**
- O1 (Triangulation < 1.5/3 used as Strong)
- O2 (TRITHUC gap cited as resolved without date)
- O3 (Forced mapping — NAC concept mapped without justification)
- O4 (TTL decay ignored — pre-2000 source treated as Current)
- O5 (ES tag mismatch — `[ES-VIKALP]` presented with `[ES-PRATY]` language)

**YELLOW (Y1-Y5) — Caution:**
- Y1 (Single-anchor overclaim)
- Y2 (DSH applied outside scope)
- Y3 (Mệnh Đề used as Tiên Đề)
- Y4 (Vận hành ghi chú treated as formal claim)
- Y5 (Bilingual term used as formal without English equivalent)

**CCL (S16-S20):**
- S16 (New assertion without SOT trace)
- S17 (Model self-evaluates — AI RCA without TIP-1)
- S18 (Vikalpa passed as Pratyakṣa — **primary hallucination mechanism**)
- S19 (Bootstrapping — claim A → claim B, same AI session)
- S20 (TIP violation — AI-generated as authority for AI-generated)

### Step 4.2 — Create `anti_hallucinations/02_detection.md`

**4-group origin classification:**

| Group | MACH RE Examples | ES tag default |
|-------|-----------------|---------------|
| **A (Standard)** | Axiom I–IV core; N_PN_00001–00030; N_AW_ASH_00001–00100; N_BE_00001–00030 | `[ES-PRATY]` |
| **B (Pre-existing, new scope)** | Mệnh Đề 1–4; DSH-1/2/3; TRITHUC-1–10 | `[ES-ANUMA]` |
| **C (New, anchored)** | AHP calibration anchors; VYR entries; NAC table; `[AH-NAJ]` entries | `[ES-ANUMA]` |
| **D (New, unanchored)** | Any new axiom element without triangulation check | `[ES-VIKALP]` |

**Confirmation column:** Every component gets a confirmation field referencing `labels.md` label # (1/2/3) or blank if unjudged.

### Step 4.3 — Create `anti_hallucinations/03_sot_traceability.md`

**Internal SOTs (8):**

| SOT ID | Name | Path | Type |
|--------|------|------|------|
| SOT-1 | Axiom Spec | `axiom_spec.md` | Framework core |
| SOT-2 | A·B·C System Mapping | `documents/mapping/a_b_c_system_mapping.md` | Mapping SOT |
| SOT-3 | TRITHUC Gap Index | `documents/gap/TRITHUC_index.md` | Gap registry |
| SOT-4 | CLAUDE.md | `CLAUDE.md` | Rule system |
| SOT-5 | **labels.md** | `labels.md` | **Confirmation verdict SOT** |
| SOT-6 | A — Phan Ngọc | `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` | Compass A |
| SOT-7 | B — Ashby/Weick | `documents/B_SYSTEM_Ashby_Weick/b_system_ashby_weick.md` | Compass B |
| SOT-8 | C — Buddhist Epistemology | `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md` | Compass C |

**External SOTs (3):** Phan Ngọc (1998), Ashby (1956), Orton & Weick (1990).

**Trace score denominator:** N = 8 (internal). External = bonus.

### Step 4.4 — Create `anti_hallucinations/04_analysis.md`

**6 root cause types:**

| Type | Name | MACH RE Example |
|------|------|----------------|
| Type 1 | Category Error | "MACH RE solves Quantum Measurement" |
| Type 2 | Provenance Failure | Claim `[established]` but actually `[proposed-by-this-project]` (F9) |
| Type 3 | Triangulation Overstatement | 1.5/3 triangulation called "strongly supported" |
| Type 4 | Temporal Decay | Pre-2000 literature without TTL re-verification |
| Type 5 | Mapping Overreach | ANALOGY → STRUCTURAL without new formal justification |
| Type 6 | Scope Violation | DSH outside calibration; institutional design conflation |

**FSR rubric (≥ 9/12 = hallucination confirmed):** Standard 12-point, MACH RE examples.

### Step 4.5 — Create `anti_hallucinations/label_system.md`

**CRITICAL: This file is where AHP meets labels.md.**

**§1.5 — Confirmation State Labels (modified from template):**

> **Canonical SOT:** `labels.md` (project root). The three confirmation labels below are the AHP encodings of labels.md labels #1, #2, #3. labels.md is the single source of truth for confirmation verdict semantics. In case of any discrepancy, labels.md takes precedence.

| Label | labels.md # | Trigger | Meaning | Action |
|-------|------------|---------|---------|--------|
| `[AH-HCNF]` | **#1** | Human reviewer explicitly confirmed; TIP-1 PASS documented | Human Confirmed — claim verified by independent human RCA | Log reviewer + date in registry |
| `[AH-AIHL]` | **#2** | Confirmed AI-fabricated: trace=0 + contradicts SOT + S20 + human verdict | AI Hallucination Confirmed — claim is fabricated | **BLOCKING.** Supersedes `[AH-CRIT]`. Remove or replace. |
| `[AH-NAJ]` | **#3** | Human reviewer determines system lacks epistemic framework to evaluate this claim | No Authority to Judge — system cannot judge; claim may be valid but outside our epistemic jurisdiction | **DEFER.** Document unlock condition. Re-evaluate when condition met. Does NOT block. |

> **`[AH-NAJ]` — Design rationale:** This label implements `axiom_spec.md §0.6` kill condition #1 at the audit level: the audit system must recognize when it cannot audit something. Without this, the system would be forced to classify every claim as either "confirmed" or "hallucinated" — a false binary that violates Tiên Đề V (the framework must apply its own standards to itself, including the standard of epistemic humility). Label #3 is MACH RE's structural implementation of: "I don't know" is a valid epistemic state.

**ES tag defaults calibrated for MACH RE:**

| Claim type in MACH RE | Default ES tag | Rationale |
|-----------------------|---------------|-----------|
| Core axiom with 3.0/3 triangulation | `[ES-PRATY]` | Direct anchor to ≥ 3 compass systems, published sources |
| Core axiom with 1.5-2.5/3 triangulation | `[ES-ANUMA]` | Derived by valid structural inference |
| Derived proposition (Mệnh Đề 1–4) | `[ES-ANUMA]` | Logically entailed; derivation chain explicit |
| Heuristic (DSH) | `[ES-ANUMA]` + TTL=Historical | Empirical generalization, stated falsification conditions |
| Cross-system mapping link | `[ES-ANUMA]` + boundary: "Interpretive — not equivalence" | Structural analogy, not identity |
| TRITHUC gap (unresolved) | `[ES-VIKALP]` pending resolution | Currently unanchored |
| Ca dao / folk evidence | `[ES-SMRTI]` | Oral tradition, not formal scholarship |
| Vận hành ghi chú (operational note) | `[ES-ANUMA]` | Derived from axiom mechanism |
| New unverified claim | `[ES-VIKALP]` pending trace | Default until trace ≥ 2/N |

**Updated decision tree (Step 5 modified):**
```
New component
  → Step 1: H score → Primary Label
  → Step 2: Risk Score → RS Label
  → Step 3: ES source type → ES Label
  → Step 4: Secondary conditions → Secondary Labels
  → Step 5: Human confirmation
      Can a human reviewer judge this claim?
        YES → judge → [AH-HCNF] (labels.md #1) or [AH-AIHL] (labels.md #2)
        NO  → [AH-NAJ] (labels.md #3) + defer with unlock condition
  → Register in Component Registry (§3)
```

### Step 4.6 — Create `anti_hallucinations/06_solution.md`

**5 solution types:**

| Type | Name | MACH RE Example |
|------|------|----------------|
| Type 1 | SOT ANCHOR | Link claim to node code + source line |
| Type 2 | SCOPE BOUNDARY | Add "This claim does not apply to..." |
| Type 3 | DOCUMENT | Fix wording — "isomorphic" → "analogous" |
| Type 4 | REMOVE | Delete hallucinated claim |
| Type 5 | DEFER | `[AH-NAJ]` — defer with unlock condition; log in labels.md #3 registry |

**Priority matrix (P0-P4):**
- P0 (BLOCKING): `[AH-CRIT]` / `[AH-AIHL]` + Risk Score ≥ 20
- P1 (URGENT): `[AH-HIGH]` + Risk Score 15-19.9
- P2 (STANDARD): `[AH-WARN]` + Risk Score 10-14.9
- P3 (LOW): `[AH-LOW]` + Risk Score < 10
- P4 (OBSERVE): `[AH-OK]`
- **P-DEFER**: `[AH-NAJ]` — tracked separately; not prioritized until unlock condition met

**RCA gate for Phase 4:** All pipeline files have MACH RE content; labels.md referenced throughout; `[AH-NAJ]` added; decision tree updated → PASS.

---

## Phase 5 — Integration & Self-Audit (files 12, cross-cutting)

**Goal:** Wire AHP into MACH RE RCA pipeline; verify completeness.

### Step 5.1 — Create `anti_hallucinations/integration_spec.md`

**Layer mapping: AHP ↔ MACH RE RCA Pipeline + labels.md:**

| AHP Component | MACH RE Equivalent | Integration |
|---------------|-------------------|-------------|
| `01_early_warning` (20 signals) | RULE ZERO Step 1 (Define) | Signals flag symptoms before RCA |
| `02_detection` (inventory + ES tag) | RULE ZERO Step 2 (Trace) + Triangulation §7 | ES tag = epistemic provenance classification |
| `03_sot_traceability` | RULE ZERO Step 3 (Isolate) | Trace score identifies anchor strength |
| `04_analysis` (5-Whys + FSR) | RULE ZERO Step 2–3 + 5-Why method | Standardized RCA form |
| `05_scoring` (0-10) | RULE ZERO scoring gate (≥ 4/5) | AHP score = risk; RCA gate = change decision. Complementary. |
| `label_system` — ES tags | Provenance tags (`[established]`, etc.) | ES = epistemic; provenance = sociological |
| `label_system` — Confirmation | **`labels.md`** (canonical SOT) | AHP labels = encoding; labels.md = SOT |
| `06_solution` (P0-P4 + P-DEFER) | RULE ZERO Step 4 (Fix) + CHANGELOG | Standardized resolution tracking |
| `00_top_risk_record` (Risk Score + TTL) | RULE ZERO Step 5 (Verify) — ongoing | Temporal tracking |

**Critical integration rule (unchanged):**
- RCA gate (≥ 4/5) → "Should this claim be changed?"
- AHP score (0-10) → "How risky is this claim right now?"
- labels.md verdict → "What is the human judgment on this claim?"
- F9 pattern: RCA ≥ 4/5 + AHP ≥ 7 + labels.md = unjudged → **flag for provenance review.**

### Step 5.2 — Create `anti_hallucinations/plan/2026-06-12_ahp_instantiation_log.md`

Record every calibration decision with RCA trace.

### Step 5.3 — Self-Audit Checklist

| # | Check | Expected Result |
|---|-------|----------------|
| 1 | File count | 15 instantiated + 2 new = 17 |
| 2 | Provenance stamp | Every file: `Instantiated from: AHP Template v1.0 (2026-06-12)` |
| 3 | Author metadata | Every file has author metadata |
| 4 | No foreign calibration data | Zero false matches |
| 5 | System Registry | 4 systems (PN, AW, BE, MR) |
| 6 | SOT list | 8 internal (incl. labels.md) + 3 external = 11 |
| 7 | Scoring calibration | ≥ 2 anchors per band |
| 8 | Vyāpti Registry | 9 VYR entries (≥ 3) |
| 9 | Mapping Registry | All Part II rows; NAC table (5 entries) |
| 10 | **labels.md integration** | `[AH-NAJ]` label added; labels.md referenced in label_system.md §1.5, 06_solution.md, integration_spec.md, 03_sot_traceability.md |
| 11 | File Map | Complete listing in index.md §2 |

**RCA gate for Phase 5:** All 11 checks PASS → declare ACTIVE → update index.md header.

---

## Phase 6 — Finalize (files: CHANGELOG.md, CLAUDE.md)

### Step 6.1 — Update `CHANGELOG.md`

```
## 2026-06-12 — AHP Installation

- **AHP v3.1 installed** into `anti_hallucinations/` — Anti-Hallucination Pipeline for multi-system mapping audit.
  - RCA decision: 3-round × 5-Why × scoring gate 5.8/6 (4.83/5) → PROCEED.
  - 15 files instantiated from template; 2 new files (instantiation log + this plan).
  - Systems: PN (68N/124E), AW (180N), BE (255N), MR (6 axioms + 4 propositions + DSH).
  - NAC table: 5 entries from TRITHUC gaps (3, 7, 8, 9, 10).
  - Vyāpti Registry: 9 VYR entries.
  - **labels.md integration:** `[AH-NAJ]` added (derived from labels.md #3); labels.md = canonical SOT for confirmation verdicts.
  - Integration: AHP = middle layer connecting RULE ZERO (process) → labels.md (verdict).
  - Plan: `plan/2026-06-12_plan_ahp_installation.md`.
```

### Step 6.2 — Update `CLAUDE.md`

Add after "Always Do" section:
```
### Anti-Hallucination Pipeline (AHP)

MACH RE uses an Anti-Hallucination Pipeline (AHP v3.1) at `anti_hallucinations/`. Entry point: `anti_hallucinations/index.md`.

- **Before writing a new cross-system mapping claim:** check `anti_hallucinations/mapping_registry.md`.
- **Before claiming a TRITHUC gap is resolved:** verify against `anti_hallucinations/vyapti_registry.md`.
- **When scoring a claim via RULE ZERO:** assign ES tag per `anti_hallucinations/label_system.md` §1.4.
- **Confirmation verdicts:** `labels.md` is the canonical SOT. Use `[AH-HCNF]` (#1), `[AH-AIHL]` (#2), or `[AH-NAJ]` (#3).
```

---

# PART 4 — DEPENDENCY GRAPH

```
Phase 1 (Bootstrap)
  └─→ Phase 2 (System Registry + Mapping Registry)
        └─→ Phase 3 (Calibration Anchors)
              └─→ Phase 4 (Pipeline Files — labels.md referenced throughout)
                    └─→ Phase 5 (Integration + Self-Audit incl. labels.md check)
                          └─→ Phase 6 (Finalize — CHANGELOG + CLAUDE.md)
```

**Parallelizable within phases:**
- Phase 2: `system_registry.md` ∥ `mapping_registry.md`
- Phase 3: `05_scoring.md` ∥ `vyapti_registry.md` ∥ `stakes_assessment.md`
- Phase 4: All 6 pipeline files (share reference data, independently fillable)

---

# PART 5 — RISK ASSESSMENT

| Risk | Severity | Mitigation |
|------|----------|-----------|
| **AHP scoring drifts from RCA gate** | MEDIUM | Integration spec: RCA gate = change decision; AHP score = risk. Rule: RCA ≥ 4/5 AND AHP ≥ 7 → provenance review. |
| **Template calibration incomplete** | MEDIUM | Self-audit checklist catches placeholders. Mandatory PASS before ACTIVE. |
| **AHP adds overhead without improving outcomes** | LOW | Proportionality: CRITICAL → full pipeline; LOW → scan-only. Stakes assessment gates depth. |
| **Namespace collision** | LOW | AHP namespace (`AH-`, `RS-`, `ES-`, `VYR-`, `NAC_`, `MAP_`) — no overlap with N_PN_, N_AW_, N_BE_. |
| **labels.md divergence** — AHP label semantics drift from labels.md SOT | MEDIUM | labels.md declared as canonical SOT in label_system.md §1.5. Integration spec rule: any discrepancy → labels.md takes precedence. Self-audit check #10 verifies cross-references. |
| **`[AH-NAJ]` overuse** — too many claims deferred | LOW | `[AH-NAJ]` requires explicit unlock condition + human reviewer sign-off. Not a default. Tracked in 00_top_risk_record for quarterly review. |

---

# PART 6 — FILE OUTPUT SUMMARY

```
anti_hallucinations/
├── README.md                          # (from TEMPLATE_README.md)
├── index.md                           # (from template_index.md)
├── 00_top_risk_record.md              # (from template_00_top_risk_record.md)
├── 01_early_warning.md                # (from template_01_early_warning.md)
├── 02_detection.md                    # (from template_02_detection.md)
├── 03_sot_traceability.md             # (from template_03_sot_traceability.md) — SOT-5 = labels.md
├── 04_analysis.md                     # (from template_04_analysis.md)
├── 05_scoring.md                      # (from template_05_scoring.md)
├── 06_solution.md                     # (from template_06_solution.md) — P-DEFER for [AH-NAJ]
├── label_system.md                    # (from template_label_system.md) — §1.5 anchors to labels.md
├── stakes_assessment.md               # (from template_stakes_assessment.md)
├── vyapti_registry.md                 # (from template_vyapti_registry.md)
├── integration_spec.md                # (from template_integration_spec.md)
├── system_registry.md                 # (from template_system_registry.md)
├── mapping_registry.md                # (from template_mapping_registry.md)
├── template/                          # (unchanged)
│   └── ...
└── plan/
    └── 2026-06-12_ahp_instantiation_log.md  # (new)

labels.md                              # (PRESERVED — canonical confirmation SOT)
```

---

# PART 7 — BOUNDARY STATEMENT

1. **This installation does NOT modify any axiom, proposition, or heuristic.** `axiom_spec.md` is READ-ONLY.
2. **This installation does NOT replace RULE ZERO.** AHP is the middle layer recording RCA outputs.
3. **This installation does NOT replace labels.md.** labels.md is preserved as canonical SOT for confirmation verdicts. AHP adds `[AH-NAJ]` derived from label #3 — no deletion, only extension.
4. **This installation does NOT change triangulation scores.**
5. **This installation does NOT resolve TRITHUC gaps.** AHP provides tracking infrastructure; closing gaps requires separate RCA.
6. **This installation does NOT claim to eliminate hallucination.** Reduces probability of undetected hallucination; cannot guarantee zero.
7. **This installation is `[proposed-by-this-project]`** — AHP template v3.1 was developed for this domain. Application to MACH RE not externally validated.
8. **`[AH-NAJ]` is `[proposed-by-this-project]`** — derived from labels.md label #3 "No authority to judge." The AHP template (v3.1) does not have this label; it is a MACH RE addition.

---

# PART 8 — APPROVAL CHECKLIST

| # | Check | Status |
|---|-------|--------|
| 1 | RCA decision complete (≥ 4/5) | ☑ PASS — 5.8/6 (4.83/5) |
| 2 | labels.md integrated as canonical confirmation SOT | ☑ PASS |
| 3 | `[AH-NAJ]` label design reviewed | ☑ PASS |
| 4 | Phase plan reviewed | ☑ PASS |
| 5 | Dependency graph validated | ☑ PASS |
| 6 | Risk assessment reviewed | ☑ PASS |
| 7 | Boundary statement accepted | ☑ PASS |
| 8 | User approval "yes" / "proceed" | ☑ APPROVED — user (2026-06-13): "yes ,(Buddhist epistemology as compass) dùng 3-round RCA (× 5-Why × scoring threshold 4/5) để quyết định" |

---

**WAITING FOR CONFIRMATION:** Proceed with this AHP installation plan? (yes / no / modify)

---

*Plan v2.0 — 2026-06-12. RCA decision: 5.8/6 (4.83/5) → PROCEED. 6 phases, 17 output files, 2 modified files, 7 reference files (incl. labels.md). Key addition from v1.0: labels.md integration with `[AH-NAJ]` label + canonical SOT status.*

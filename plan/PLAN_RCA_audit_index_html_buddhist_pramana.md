# PLAN — RCA AUDIT: `index.html` × Buddhist Pramāṇa Epistemology
<!-- 3-round RCA × 5-Why × scoring gate ≥ 4/5 — internal-consistency audit -->
<!-- Date: 2026-06-09 | Method: RCA-driven single-lens deep audit | Status: DRAFT — awaiting approval -->

## METADATA

```
document_type     : plan_audit_rca
subject           : index.html (Mạch Rễ landing page, v2.1 — post triple-lens audit)
audit_lens        : Buddhist Pramāṇa-Epistemology, Logic, and Language
                    (Hari Shankar Prasad, with reference to Vasubandhu, Diṅnāga, Dharmakīrti)
lens_type         : INTERNAL CONSISTENCY — Mạch Rễ explicitly anchors in Buddhist epistemology
                    as one of 3 independent systems (C6: "neo 3 hệ độc lập")
primary_source    : The_Buddhist_Pramana_Epistemology_Logic_and_Language_RCA_Table.md
                    (233 concepts, line-evidenced)
fallback_source   : The_Buddhist_Pramana_-Epistemology_Logic_and_Langu_ol.md
                    (full article, ~317 source lines)
method            : 3-round RCA × 5-Why × scoring gate ≥ 4/5
                    single-lens deep: fewer passes, greater depth per pass
                    internal-consistency rule: the framework is audited against ITS OWN anchor
references        :
  - index.html (audit target, post triple-lens audit at commit 5c35ba3)
  - CLAUDE.md (RULE ZERO — RCA procedure)
  - plan/dictionary_rule.md (canonical lookup table)
  - axiom_spec.md (canonical axiom definitions)
  - review/audit_index_html_triple_lens_phase1.md (prior Kant findings — cross-reference)
  - review/audit_index_html_triple_lens_phase2.md (prior Ashby/Weick findings — cross-reference)
status            : DRAFT — awaiting user approval before execution
```

---

## EXECUTIVE SUMMARY

**Verdict: This audit fills a gap the triple-lens audit left open. The Kant lens (L1) audited epistemological STATUS — whether claims are over-scoped. This audit checks epistemological METHOD — whether the framework actually follows the Buddhist epistemology it claims as an anchor.**

The triple-lens audit (Kant × Ashby × Weick/Orton, commit `5c35ba3`) audited `index.html` through three EXTERNAL lenses. It found 14 defects (all fixed) and confirmed 4 strengths. But it left one question unasked: **does Mạch Rễ obey the rules of its own anchor system?**

Mạch Rễ claims "neo 3 hệ độc lập" — Buddhist epistemology, cybernetics (Ashby), and organizational theory (Weick/Orton). The Ashby and Weick/Orton anchors were thoroughly applied in the triple-lens audit. The Buddhist anchor was NOT — it was treated as a historical/cultural reference point, not as an active epistemological standard.

This is a gap because:
1. Mạch Rễ's central epistemic move (deriving axioms from a root question) is structurally parallel to Buddhist pramāṇa methodology — both start from an existential predicament and derive conceptual tools to overcome it
2. Mạch Rễ uses terms ("nhận dạng", "thực hành", "trí tuệ", "vô minh") that have precise technical meanings in Buddhist epistemology
3. The framework's disclaimer uses negation ("phi chính trị, phi tôn giáo") that maps to Buddhist logical operators (prasajya-pratiṣedha vs paryudāsa-pratiṣedha)
4. If Mạch Rễ violates Buddhist epistemological standards while claiming Buddhism as an anchor, it undermines the triangulation method itself

**This is an INTERNAL CONSISTENCY audit, not an external critique.** The question is not "does Mạch Rễ satisfy Buddhist epistemology?" but rather "given that Mạch Rễ CLAIMS Buddhist epistemology as an anchor, does it follow the standards that anchor imposes?"

### Key diagnostic axes

| Axis | Buddhist concept | Applied to | Diagnostic question |
|------|-----------------|------------|---------------------|
| **Pramāṇa structure** | Pramāṇa/Prameya/Pramāphala (#22-25) | C1, C5, C6 | Does the framework specify what it knows, how it knows, and what results from knowing? |
| **Two Truths** | Saṃvṛti-sat / Paramārtha-sat (#99-100) | C1, C3, C7 | Does the framework locate itself at the conventional level? Does it claim ultimate truth? |
| **Particular vs Universal** | Svalakṣaṇa / Sāmānyalakṣaṇa (#138-139) | C5, C15 | Does the framework claim to capture unique particulars (causally efficient, inexpressible) or general characteristics (conceptual, expressible)? |
| **Apoha semantics** | Apoha / Double negation (#5, #74) | C1, C2, C14 | Does Mạch Rễ's naming ("đặt tên") work through exclusion, or does it claim positive reference to real universals? |
| **Valid reason** | Trairūpya-hetu (#128, #180-183) | C6, C7 | Does the derivation satisfy the three criteria of a valid inferential sign? |
| **Gold-testing** | Buddha's testing method (#106) | C1, C12 | Does index.html INVITE testing, or does it demand acceptance? |
| **Negation type** | Prasajya / Paryudāsa (#72-73) | C12 (disclaimer) | Is "phi chính trị" mere negation or implicative negation? |
| **Dependent arising** | Pratītyasamutpāda (#39-40) | C1, C5, Tiên Đề I | Is the mapping between Tiên Đề I and dependent arising explicit? |
| **Avidyā → Prajñā** | Ignorance → Wisdom (#42, #54) | C5, C6 | Does the framework's diagnosis rubric map to the Buddhist path? |
| **Arthakriyā** | Causal efficacy (#105, #167-168) | C1, C4 | Does the framework claim successful activity? Is this demonstrated or asserted? |
| **Scepticism** | Methodological doubt (#12, #107) | C1, C5 | Does the framework embody the Buddha's "sailing against the current"? |
| **Restricted scope** | Diṅnāga's deliberate restriction (#81) | C4, C6 | Does the framework delimit its scope, or claim unbounded applicability? |

---

## 1. AUDIT SCOPE

### 1.1 Relationship to prior triple-lens audit

This audit is **complementary, not redundant**, to the triple-lens audit (commit `5c35ba3`).

| Aspect | Triple-lens audit (done) | This audit (new) |
|--------|--------------------------|-------------------|
| **Lenses** | Kant (L1), Ashby (L2), Weick/Orton (L3) | Buddhist Pramāṇa only |
| **Approach** | External critique — does the framework overclaim? | Internal consistency — does the framework obey its own anchor? |
| **Depth** | 3 lenses × 16 claims = 48 potential passes (24 executed) | 1 lens × 16 claims = 16 deep passes |
| **Key finding** | Epistemological underspecification (RC1) | Buddhist epistemological conformance |
| **What it didn't ask** | Does Mạch Rễ actually follow Buddhist pramāṇa methodology? | (This audit's core question) |

### 1.2 Target: `index.html` claim inventory (same 16 claims)

The 16-claim catalog from the triple-lens audit plan (§1.2) is reused. The claims have been partially modified by the triple-lens fixes (applied at commit `5c35ba3`). This audit checks the MODIFIED claims.

| ID | Claim (current wording, post triple-lens fixes) | Zone |
|----|------------------------------------------------|------|
| **C1** | "Mạch Rễ là khung nền (framework) nhận dạng và thực hành bản sắc sinh tồn — được xây dựng để đặt tên và hệ thống hóa — làm hiển lộ (make explicit) cấu trúc vốn đã tồn tại trong thực hành, không phải áp đặt từ bên ngoài" | Z2 |
| **C2** | "triết lý sinh tồn được dân tộc Việt Nam thể hiện qua hành vi tập thể trong lịch sử" | Z2 |
| **C3** | "được sống và liên tục thích nghi qua 4.000 năm nhưng chưa từng được hệ thống hóa thành một khung nền (framework) hoàn chỉnh" | Z2 |
| **C4** | "Có thể áp dụng cho cá nhân, cộng đồng, và tổ chức đang đối mặt với áp lực đồng hóa trong thời đại biến động" | Z2 |
| **C5** | "Làm sao giữ được mình khi mọi thứ xung quanh muốn thay đổi mình?" + boundary note (Requisite Variety, tight/loose, growth) | Z2 |
| **C6** | "Bản tái dựng (rebuild 2026) suy từ câu hỏi gốc (derivation — theo nghĩa điều kiện cần: lời giải thích khả dĩ duy nhất) và kiểm chứng chéo qua 3 hệ độc lập (triangulation)" | Z3 |
| **C7** | "4 Tiên Đề Cốt Lõi (I–IV) + 4 Mệnh Đề Dẫn Xuất (V–VII, F) + 1 Meta-Tiên Đề (VIII)" | Z3 |
| **C8–C11** | Timeline: 179 TCN, TK 13, 1994, 1997 (title fixed: "Hành trình của triết lý sinh tồn mà Mạch Rễ đặt tên") | Z4 |
| **C12** | "Mạch Rễ tồn tại trước mọi nhà nước Việt Nam hiện đại và thuộc về toàn thể dân tộc" + "Phi chính trị · Phi tôn giáo" | Z1/Z5 |
| **C13** | Glossary: Framework = "Hệ thống công cụ nhận dạng và thực hành bản sắc sinh tồn" (with process note) | Z5 |
| **C14** | Glossary: Homomorphism (was Isomorphism) | Z5 |
| **C15** | Glossary: Invariant = "Thuộc tính hay quan hệ vẫn giữ nguyên qua một chuỗi biến đổi" | Z5 |
| **C16** | Glossary: Attractor basin = "Vùng mà hệ thống luôn tự động quay về sau các biến động trong phạm vi (basin) của nó" | Z5 |

### 1.3 What is NOT audited

- CSS/styling, visual design — same as prior audit
- Linked pages — same as prior audit
- The Buddhist RCA table's accuracy — assumed valid for this audit; defects in the RCA table would be a separate task
- Comparison with Kant findings — noted where relevant but not re-audited

---

## 2. TWO-TIER REFERENCE ARCHITECTURE

### 2.1 Architecture

```
┌─────────────────────────────────────────────────────────┐
│              BUDDHIST PRAMĀṆA AUDIT                       │
│                                                         │
│  For each claim Cᵢ:                                      │
│                                                         │
│  ┌──────────────────┐                                   │
│  │ TIER 1 (primary) │ ←── Always start here             │
│  │   RCA Table       │     233 concepts                 │
│  │   15 selected     │     Line-evidenced definitions   │
│  └────────┬─────────┘                                   │
│           │                                             │
│           │ Is the RCA table definition sufficient?     │
│           │                                             │
│     ┌─────┴─────┐                                       │
│     │ YES       │ NO — escalate                         │
│     ▼           ▼                                       │
│  Proceed    ┌──────────────────────┐                    │
│  with       │ TIER 2 (verification)│                    │
│  diagnosis  │   Full article       │                    │
│             │   ~317 source lines  │                    │
│             │   Line-evidenced     │                    │
│             └──────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

### 2.2 Tier 1 — RCA Concept Table (primary)

**Source:** `The_Buddhist_Pramana_Epistemology_Logic_and_Language_RCA_Table.md`
**Size:** 233 concepts across epistemology, logic, language, ontology, soteriology, methodology
**Selected:** 15 diagnostic concepts (see §3)

### 2.3 Tier 2 — Full Source Document (fallback)

**Source:** `The_Buddhist_Pramana_-Epistemology_Logic_and_Langu_ol.md`
**Size:** ~317 source lines (article body, excluding metadata)
**Content:** Full article by Hari Shankar Prasad — Buddhist pramāṇa-epistemology with reference to Vasubandhu, Diṅnāga, and Dharmakīrti

**Four escalation paths (same protocol as prior audit):**

| Path | Trigger | Action |
|------|---------|--------|
| **P-VERIFY** | RCA table definition seems incomplete for the nuance needed | Read surrounding paragraphs in full source to confirm or correct |
| **P-MINE** | The 15 selected concepts don't cover a defect that clearly exists | Search full source for the missing concept |
| **P-DISPUTE** | A finding contradicts the prior audit's Kant-based findings | Verify both interpretations against their respective sources |
| **P-RECALIBRATE** | Recalibration checkpoint reveals a gap in the 15 selected concepts | Mine full source for additional concepts |

### 2.4 Tier 2 quick-reference map

For efficient surgical reads during audit execution:

| Concept area | Approximate section in full source | Key thinkers |
|-------------|-----------------------------------|--------------|
| Pramāṇa formulation (4 components) | §1 (L17-L25), §4 (L67-L105) | Diṅnāga |
| Two Truths (saṃvṛti / paramārtha) | §4 (L91-L105) | Vasubandhu |
| Svalakṣaṇa / Sāmānyalakṣaṇa | §4 (L141-L169) | Diṅnāga, Dharmakīrti |
| Apoha / double negation | §1 (L11), §4 (L233-L255) | Diṅnāga |
| Trairūpya (three criteria) | §4 (L107-L215) | Diṅnāga |
| Gold-testing method | §4 (L77-L85) | Buddha, Diṅnāga |
| Scepticism & methodological doubt | §2 (L37-L45) | Buddha |
| Diṅnāga's restricted scope | §2 (L39-L41), §3 (L49-L61) | Diṅnāga |
| Dependent arising | §1 (L23-L33) | Buddha |
| Avidyā → Prajñā path | §1 (L23-L33) | Buddha |
| Arthakriyā (causal efficacy) | §4 (L73-L77, L167-L173) | Dharmakīrti |
| Prasajya / Paryudāsa negation | §1 (L27) | (listed only) |
| Pramāṇabhūta (Buddha as authority) | §4 (L75-L81) | Diṅnāga |
| Dharmakīrti's pragmatism | §4 (L303-L315) | Dharmakīrti |

---

## 3. DIAGNOSTIC CONCEPT SELECTION — 15 of 233 Concepts

Selected for maximum diagnostic leverage against `index.html` claims. Each concept exposes a *falsifiable* risk in at least one claim.

### 3.1 Epistemology cluster (5 concepts)

| B# | Concept | RCA # | Diagnostic question |
|----|---------|-------|---------------------|
| **B1** | Pramāṇa 4-fold structure (pramāṇa/prameya/pramā/phala) | #22-25, #97 | Does `index.html` specify: (a) what Mạch Rễ knows (prameya = bản sắc sinh tồn?), (b) how it knows (pramāṇa = derivation from question + triangulation?), (c) what valid cognition results (pramā = diagnosis?), (d) what the result yields (phala = practice?) |
| **B2** | Pratyakṣa vs Anumāna (perception vs inference) | #27-28 | Does Mạch Rễ claim direct perception of identity-survival patterns, or inference from observed behavior? "Nhận dạng" implies perception — but the Black Box method (confirmed strength, prior audit) implies inference |
| **B3** | Svalakṣaṇa vs Sāmānyalakṣaṇa (particular vs universal) | #138-139 | Does the framework claim to capture unique particulars (causally efficient, inexpressible) or general characteristics (conceptual, expressible)? "Bản sắc sinh tồn" — which is it? |
| **B4** | Pramāṇādhīna vs Prameyādhīna (means-first vs object-first) | #134-135 | Diṅnāga's dictum: knowledge of object depends on means of knowledge. Does Mạch Rễ's "suy từ câu hỏi gốc" follow this? Or does it assume the object (bản sắc) determines the means? |
| **B5** | Non-distinction of means and result | #140 | Diṅnāga rejects the realist distinction between means and result of cognition. Does the framework separate "nhận dạng" (means) from "thực hành" (result), or does it preserve their non-distinction? |

### 3.2 Two Truths cluster (2 concepts)

| B# | Concept | RCA # | Diagnostic question |
|----|---------|-------|---------------------|
| **B6** | Saṃvṛti-sat (conventional truth) | #99, #110 | Does `index.html` locate Mạch Rễ at the conventional level (useful designation, conceptual, pragmatically usable)? Or does it drift toward claiming ultimate truth? |
| **B7** | Paramārtha-sat (ultimate truth) | #100, #109 | Does the framework claim to describe "ultimate ontological reality" (non-conceptual, irreducible, infallible)? A framework with 8 axioms and a diagnosis rubric is conceptual by nature — it CANNOT be paramārtha-sat |

### 3.3 Semantics cluster (3 concepts)

| B# | Concept | RCA # | Diagnostic question |
|----|---------|-------|---------------------|
| **B8** | Apoha / Double negation (exclusion-based meaning) | #5, #74, #189 | "Đặt tên" (naming) in Buddhist semantics works through apoha: "bản sắc sinh tồn" means "that which is EXCLUDED from non-survival, non-identity." Does Mạch Rễ's definitional method follow apoha, or does it claim positive reference to a real universal? |
| **B9** | Prasajya-pratiṣedha vs Paryudāsa-pratiṣedha (non-implicative vs implicative negation) | #72-73 | "Phi chính trị · Phi tôn giáo" — is this prasajya (mere negation: "not political, not religious — period") or paryudāsa (implicative: "not political, not religious — THEREFORE something else")? The disclaimer's legal function suggests prasajya; the framework's positioning suggests paryudāsa |
| **B10** | Anyāpoha (exclusion of others) | #189, #192 | Does the glossary's "Homomorphism" definition (C14) actually follow anyāpoha logic — defining by excluding what it is NOT — rather than by positive description? |

### 3.4 Logic & Method cluster (3 concepts)

| B# | Concept | RCA # | Diagnostic question |
|----|---------|-------|---------------------|
| **B11** | Trairūpya-hetu (three criteria of valid reason) | #128, #180-183 | C6 claims the axioms are "derived." A valid inference in Buddhist logic requires: (1) reason is property of subject, (2) reason occurs in similar cases, (3) reason does not occur in dissimilar cases. Does the derivation satisfy these? |
| **B12** | Gold-testing method | #106, #96 | The Buddha: "accept my statement only by testing its validity, not out of reverence." Does `index.html` INVITE testing? Is there a falsification condition visible on the landing page? |
| **B13** | Scepticism as methodological tool | #12, #107 | Buddhist epistemology begins with doubt (saṃśaya) and desire to know (jijñāsā). Does `index.html` present Mạch Rễ as ARISING FROM doubt, or as a SETTLED DOCTRINE? |

### 3.5 Ontology & Soteriology cluster (2 concepts)

| B# | Concept | RCA # | Diagnostic question |
|----|---------|-------|---------------------|
| **B14** | Dependent arising (pratītyasamutpāda) | #39-40 | Tiên Đề I ("Có Nhau Mới Có Mình") is structurally identical to dependent arising. Does `index.html` acknowledge this mapping, or is the Buddhist anchor left implicit? |
| **B15** | Avidyā → Prajñā (ignorance → wisdom) | #42, #54 | The Buddhist path moves from avidyā (ignorance constructing suffering) to prajñā (wisdom seeing reality-as-it-is). Mạch Rễ's diagnosis rubric moves from "rễ nông" to "rễ sâu." Is this mapping acknowledged? Does the framework claim to ELIMINATE ignorance (nirvāṇa-claim) or to DIAGNOSE it (conventional tool)? |

---

## 4. CLAIM-TO-CONCEPT MAPPING (Audit Matrix)

| Claim | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 | B11 | B12 | B13 | B14 | B15 | Count | Priority |
|-------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|-------|----------|
| **C1** | ● | ● | ● |   | ● | ● | ● | ● |   |     |     | ●   | ●   | ●   |     | 10 | **CRITICAL** |
| **C5** | ● | ● | ● | ● |   | ● |   |   |   |     |     | ●   | ●   |     | ●   | 8 | **CRITICAL** |
| **C6** | ● |   |   | ● |   |   |   |   |   |     | ●   |     |     |     |     | 3 | **HIGH** |
| **C2** |   |   |   |   |   | ● | ● | ● |   |     |     |     |     |     |     | 3 | **HIGH** |
| **C12** |   |   |   |   |   |   |   |   | ● |     |     | ●   |     |     |     | 2 | **HIGH** |
| **C3** |   |   |   |   |   | ● | ● |   |   |     |     |     | ●   |     |     | 3 | MEDIUM |
| **C7** | ● |   |   |   |   | ● |   |   |   |     |     |     |     |     |     | 2 | MEDIUM |
| **C14** |   |   |   |   |   |   |   | ● |   | ●   |     |     |     |     |     | 2 | MEDIUM |
| **C15** |   |   | ● |   |   |   |   |   |   |     |     |     |     |     |     | 1 | MEDIUM |
| **C4** |   |   |   |   |   |   |   |   |   |     |     |     |     |     | ●   | 1 | MEDIUM |
| **C13** |   |   |   |   |   | ● |   |   |   |     |     |     |     |     |     | 1 | LOW |
| **C16** |   |   |   |   |   |   |   |   |   |     |     |     |     |     |     | 0 | LOW |
| **C8–11** |   |   |   |   |   |   |   |   |   |     |     |     |     |     |     | 0 | INFO |

**Priority legend:**
- **CRITICAL** (2 claims, C1 + C5): ≥8 concept coverage — audit first, deepest
- **HIGH** (3 claims, C2 + C6 + C12): structural/epistemological claims with 2–3 concepts
- **MEDIUM** (5 claims): definitional claims with 1–3 concepts
- **LOW** (2 claims): 0–1 concept coverage; audit if findings cascade
- **INFO** (4 claims, C8–C11): timeline claims — out of scope for Buddhist epistemology lens; note as such

---

## 5. AUDIT METHODOLOGY

### 5.1 Procedure (per claim)

```
FOR each CRITICAL → HIGH → MEDIUM claim Cᵢ:
  FOR each applicable concept Bⱼ:
    1. MATCH (Tier 1) — identify the Buddhist concept's definition from RCA table
       → If insufficient → escalate to Tier 2 via P-VERIFY
    2. DIAGNOSE — apply 5-Why to the mismatch between claim and Buddhist standard
    3. SCORE — 5-criterion scoring gate (Correct/Deep/Feasible/Conflict-risk/Preservation)
    4. RECOMMEND — propose fix or mark "keep as-is"
    5. CROSS-CHECK — if finding contradicts prior triple-lens audit finding, flag for resolution
```

### 5.2 Three-round depth structure

| Round | Depth | Question | Buddhist lens role |
|-------|-------|----------|-------------------|
| **R1 — Symptom** | Surface defect | "What does the Buddhist lens SEE that the prior audit missed?" | Buddhist concept provides precise technical vocabulary to name the gap |
| **R2 — Mechanism** | Why it backfires | "Why does violating THIS Buddhist standard matter for a framework that claims Buddhism as anchor?" | Buddhist epistemology provides the THEORETICAL REASON the gap is consequential |
| **R3 — Root** | Internal standard violated | "What Buddhist epistemological rule does Mạch Rễ set for itself (by claiming Buddhist anchor) that this claim breaks?" | The framework's own triangulation claim makes Buddhist conformance an internal standard |

### 5.3 Scoring gate (same rubric)

| Criterion | Question | High score means |
|-----------|----------|-----------------|
| Correct | Is this genuinely a defect against Buddhist epistemological standards? | Real defect |
| Deep | Does the finding touch the root (internal consistency of triangulation claim)? | Reaches root |
| Feasible | Can it be fixed without breaking core structure/meaning? | Safe to fix |
| Conflict-risk | Will the fix avoid contradicting the prior triple-lens fixes? | Low new risk |
| Preservation | Is the core strength kept after the fix? | Strength preserved |

**Threshold: average ≥ 4/5 → recommend fix; < 4/5 → keep as-is, document why.**

### 5.4 Expected finding types

Based on structural analysis before audit execution:

| Type | Description | Likelihood |
|------|-------------|------------|
| **Underspecification** | The framework uses a Buddhist-compatible method but doesn't label it → missed opportunity for internal consistency | HIGH |
| **Category tension** | The framework claims something (perception, ultimate truth) that Buddhist epistemology would locate differently | MEDIUM |
| **Terminology gap** | A Buddhist technical term would be more precise than the current wording | MEDIUM |
| **Confirmed Buddhist alignment** | The framework's method is already consistent with Buddhist epistemology — document as strength | HIGH |
| **Negation ambiguity** | The disclaimer's negation type is underspecified | LOW |

---

## 6. EXECUTION PLAN — 2 PHASES, 4 DELIVERABLES

### Phase 1: CRITICAL + HIGH claims (estimated: 1 session, 5 claims × 1–10 concepts = 26 diagnostic passes)

| Step | Action | Tier 2 expected? | Output |
|------|--------|------------------|--------|
| P1.1 | Audit **C1** (framework definition) through B1–B5, B6–B7, B8, B12–B14 (10 passes) | **Yes** — B1 (pramāṇa structure) and B8 (apoha) likely need full-source nuance | Diagnostic table for C1 |
| P1.2 | Audit **C5** (central question) through B1–B4, B6, B12–B13, B15 (8 passes) | **Yes** — B15 (avidyā → prajñā) needs full-source §1 for the path structure | Diagnostic table for C5 |
| P1.3 | Audit **C6** (derivation method) through B1, B4, B11 (3 passes) | **Yes** — B11 (trairūpya) needs full-source §4 for the three criteria formulation | Diagnostic table for C6 |
| P1.4 | Audit **C2** (systematization claim) through B6–B8 (3 passes) | Possible — B8 (apoha) for "đặt tên" semantics | Diagnostic table for C2 |
| P1.5 | Audit **C12** (disclaimer) through B9, B12 (2 passes) | Possible — B9 (negation type) is "listed only" in RCA table; P-MINE may be needed | Diagnostic table for C12 |
| P1.6 | **Recalibration checkpoint** — assess concept sufficiency, Tier 2 escalation rate, cross-check with prior audit findings | N/A | Recalibration report |

**Deliverable D1**: `review/audit_index_html_buddhist_pramana_phase1.md` — per-claim diagnostic tables with scores

### Phase 2: MEDIUM + LOW claims + synthesis

| Step | Action | Tier 2 expected? | Output |
|------|--------|------------------|--------|
| P2.1 | Audit C3, C7, C14, C15, C4 (5 claims, 8 passes) | Unlikely for most; possible for C14×B10 | Diagnostic tables |
| P2.2 | Cross-reference with prior audit findings — identify where Buddhist lens confirms, qualifies, or contradicts triple-lens findings | N/A | Cross-audit consistency table |
| P2.3 | Synthesize root cause map — which Buddhist epistemological standards are most consistently underspecified? | N/A | Root cause map |

**Deliverable D2**: `review/audit_index_html_buddhist_pramana_phase2.md` — remaining claims + cross-audit synthesis

**Deliverable D3**: `review/audit_index_html_buddhist_pramana_fix_proposals.md` — prioritized fix proposals with dependency chain

**Deliverable D4**: `CHANGELOG.md` entries for any modified claims

### Phase 1 recalibration checkpoint

After auditing C1, C5, and C6 (first 3 claims, 21 passes), pause and assess:

| Checkpoint question | Action if "no" |
|---------------------|----------------|
| Are the 15 selected concepts sufficient? | P-MINE the full source for additional concepts |
| Have RCA table definitions been accurate? | Document corrections; flag RCA table for revision (separate) |
| Tier 2 escalation rate? | If >40%, expand concept selection or adjust Tier 1 definitions |
| Do findings contradict prior triple-lens findings? | Flag for P2.2 cross-audit resolution |
| Is the Buddhist lens finding defects the Kant lens missed? | If 0 new findings, the Buddhist anchor is well-satisfied → document as meta-strength |

---

## 7. SELF-AUDIT — 3-ROUND RCA ON THIS PLAN

### Round 1 — Symptom

| # | Surface concern |
|---|----------------|
| S1 | Single-lens audit may miss defects visible only through multiple perspectives |
| S2 | 15 selected concepts from 233 — selection bias risk |
| S3 | The audit uses Buddhist epistemology as a STANDARD — but Buddhist epistemology itself has internal debates (Sautrāntika vs Yogācāra, Diṅnāga vs Dharmakīrti) |
| S4 | Claims C8–C11 and C16 score 0 concept coverage — are they genuinely out of scope? |
| S5 | The prior audit already fixed 14 defects — this audit may find only minor residual issues (low ROI) |

### Round 2 — Mechanism

**S1**: The single-lens design is intentional. The triple-lens audit already covered external perspectives. This audit fills a specific gap: internal consistency with the Buddhist anchor. Adding more lenses would dilute depth. The cross-reference with prior audit findings (P2.2) provides a form of multi-perspective verification.

**S2**: The 15 concepts were selected by relevance to claim TYPES (definitional, epistemological, methodological, soteriological), not by random sampling. The selection criterion is documented (§3). The recalibration checkpoint explicitly tests sufficiency. Tier 2 P-MINE provides a safety net.

**S3**: This is the deepest risk. The RCA table and full source document the debates (e.g., Sautrāntika realism vs Yogācāra idealism, Diṅnāga's vyāpti lapse vs Dharmakīrti's svabhāvapratibandha correction). The audit should use Diṅnāga/Dharmakīrti's MATURE positions (not the positions they criticized) as the standard, since Mạch Rễ claims them as anchors. Where the Buddhist tradition itself is divided, the audit should note the division and flag which interpretation Mạch Rễ aligns with.

**S4**: C8–C11 (timeline) and C16 (attractor basin) are genuinely out of scope for Buddhist epistemology. C16 maps to cybernetics (Ashby), not pramāṇa. C8–C11 are historical claims — Buddhism has historical claims too, but pramāṇa epistemology doesn't provide tools for auditing historical factuality. This is correctly documented as a lens limitation.

**S5**: This is a legitimate concern but not a defect. If the audit finds 0 new defects, that's a STRENGTH FINDING: the Buddhist anchor is well-satisfied, and the prior audit's fixes were sufficient. The audit's value is in the verification, not just the defects found. Documenting "the framework conforms to Buddhist epistemological standards in N ways" is a positive outcome.

### Round 3 — Root

| Symptom | Root cause (one sentence) | Score |
|---------|--------------------------|-------|
| S1 | Single-lens design is a feature (depth over breadth), not a bug — the triple-lens audit already covered breadth; this audit fills the Buddhist gap | **5/5** |
| S2 | Concept selection is heuristic but documented, transparent, and backed by P-MINE fallback | **4/5** |
| S3 | Intra-Buddhist debate risk is real but manageable — the audit standard should be Diṅnāga/Dharmakīrti's mature positions; divisions should be noted, not resolved | **4/5** |
| S4 | Scope limitation is correctly identified — C8–C11 and C16 are genuinely outside Buddhist epistemology's diagnostic range | **5/5** |
| S5 | Zero-finding outcome is a valid (and valuable) result — the audit verifies internal consistency, and "consistent" is a finding, not a failure | **4/5** |

**Average: 4.4/5 — plan is sound. The Buddhist lens addresses a genuine gap in the prior audit.**

---

## 8. RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Buddhist lens finds nothing new (all findings duplicate prior audit) | MEDIUM | LOW | Document as confirmation strength — the prior audit's fixes already addressed Buddhist-conformance issues |
| Intra-Buddhist doctrinal division makes "the Buddhist standard" ambiguous | MEDIUM | MEDIUM | Use Diṅnāga/Dharmakīrti mature synthesis as standard; note divisions where relevant |
| RCA table extraction errors propagate into findings | LOW | MEDIUM | P-VERIFY escalation path; the RCA table has 233 line-evidenced rows — extraction quality appears high |
| Findings require modifying the prior audit's carefully calibrated fixes | LOW | MEDIUM | Cross-audit consistency check (P2.2); flag any contradiction for user decision |
| Audit scope creeps into auditing the Buddhist RCA table itself | MEDIUM | LOW | Strict scope boundary: the RCA table is a TOOL, not a target |
| Tier 2 full source reading balloons | LOW | LOW | The full source is ~317 lines (manageable), unlike Ashby's 7035 lines in prior audit |

---

## 9. DEPENDENCY CHAIN

```
Phase 1 (CRITICAL + HIGH claims)
  ├── P1.1 (C1 — 10 passes) ──┐
  ├── P1.2 (C5 — 8 passes)  ──┤── Independent — can run in parallel
  ├── P1.3 (C6 — 3 passes)  ──┤     Tier 2 escalations are claim-local
  ├── P1.4 (C2 — 3 passes)  ──┤
  ├── P1.5 (C12 — 2 passes) ──┘
  └── P1.6 (Recalibration) ←── Depends on P1.1–P1.3 completion

RECALIBRATION CHECKPOINT
  ├── Assess concept sufficiency
  ├── Assess Tier 2 usage
  ├── Cross-check with prior audit findings
  └── Decide: expand concept set? adjust Phase 2 scope?

Phase 2 (MEDIUM + LOW + synthesis)
  ├── P2.1 (C3, C7, C14, C15, C4) ←── Independent
  ├── P2.2 (Cross-audit consistency) ←── Depends on Phase 1 + Phase 2 findings
  └── P2.3 (Root cause synthesis)    ←── Depends on ALL findings

Deliverables
  ├── D1 (Phase 1 report)
  ├── D2 (Phase 2 report)
  ├── D3 (Fix proposals) ←── Depends on D1 + D2
  └── D4 (CHANGELOG)     ←── Depends on applied fixes
```

---

## 10. EXPECTED OUTCOMES (Hypotheses)

Based on structural analysis before audit execution:

| # | Hypothesis | Concept | Prior probability | If confirmed |
|---|-----------|---------|-------------------|--------------|
| **H1** | Mạch Rễ does not specify its pramāṇa structure — what is the prameya (object), pramāṇa (means), pramā (cognition), and phala (result)? The fourfold structure is implicit but unstated | B1 | HIGH | Add a sentence mapping the framework to pramāṇa structure: "Về mặt nhận thức luận: đối tượng (prameya) = bản sắc sinh tồn; phương tiện (pramāṇa) = suy từ câu hỏi gốc + kiểm chứng chéo; nhận thức đúng (pramā) = chẩn đoán; kết quả (phala) = thực hành." |
| **H2** | "Nhận dạng" (recognition) is ambiguous between pratyakṣa (direct perception) and anumāna (inference). The Black Box method (confirmed strength) implies anumāna — but this is not stated | B2 | HIGH | Clarify: "Nhận dạng ở đây là suy luận (anumāna) từ hành vi quan sát được — không phải trực giác (pratyakṣa) về bản chất." |
| **H3** | The framework does not locate itself on the Two Truths spectrum. As a conceptual framework (8 axioms + glossary + diagnosis rubric), it is saṃvṛti-sat (conventional) — but the tone sometimes suggests paramārtha-sat ambition | B6, B7 | MEDIUM | Add a Two Truths boundary: "Mạch Rễ là công cụ ở tầng chân lý quy ước (saṃvṛti-sat) — hữu ích, có thể kiểm chứng, nhưng không phải chân lý tối hậu (paramārtha-sat)." |
| **H4** | "Đặt tên" (naming) does not follow apoha (exclusion-based) semantics — definitions are positive ("X là Y") rather than exclusionary ("X là cái không-phải-không-X") | B8 | MEDIUM | The glossary already uses some exclusion framing — document where apoha is implicit |
| **H5** | The disclaimer's "Phi chính trị · Phi tôn giáo" uses prasajya-pratiṣedha (mere negation) in legal function, but the framework's positioning implies paryudāsa-pratiṣedha (negation implying "therefore it IS a philosophical framework") — the duality is unexamined | B9 | LOW | Document the dual function; no fix required unless it creates legal ambiguity |
| **H6** | Tiên Đề I ("Có Nhau Mới Có Mình") is structurally identical to pratītyasamutpāda but this mapping is not acknowledged on the landing page — missing opportunity to strengthen the Buddhist anchor | B14 | MEDIUM | Add a note: "Tiên Đề I tương đương cấu trúc với Duyên Khởi (pratītyasamutpāda) trong Phật giáo." |
| **H7** | The Diagnosis Rubric (rễ sâu → rễ nông) maps to avidyā → prajñā but doesn't claim to ELIMINATE ignorance (nirvāṇa) — this is correctly scoped. The landing page should make the mapping explicit to strengthen internal consistency | B15 | MEDIUM | Add: "Chẩn đoán là công cụ quy ước (không phải giải thoát) — song song với lộ trình từ vô minh (avidyā) đến trí tuệ (prajñā) trong Phật giáo." |

---

## 11. CONFIRMATION CHECKLIST

Before execution begins, confirm:

- [ ] User approves this plan (yes / modify / no)
- [ ] The 15 selected concepts are agreed as sufficient starting set
- [ ] The priority classification (CRITICAL → HIGH → MEDIUM → LOW → INFO) is accepted
- [ ] Cross-reference with prior triple-lens audit findings is desired (P2.2)
- [ ] Output directory: `review/` (matching prior audit convention)
- [ ] Token budget: Phase 1 estimated at ~26 diagnostic passes; each pass ~500-1500 tokens; total Phase 1 ~15K-40K tokens

---

## APPENDIX A — Selected Concepts Quick Reference (Tier 1 → Tier 2)

| This plan | RCA # | Concept | Tier 2 fallback (full source lines) |
|-----------|-------|---------|-------------------------------------|
| B1 | #22-25, #97 | Pramāṇa 4-fold | L65-L105 (§4 opening) |
| B2 | #27-28 | Pratyakṣa / Anumāna | L141-L163, L189-L207 |
| B3 | #138-139 | Svalakṣaṇa / Sāmānyalakṣaṇa | L141-L169 |
| B4 | #134-135 | Pramāṇādhīna / Prameyādhīna | L137 |
| B5 | #140 | Non-distinction of means/result | L141-L143 |
| B6 | #99, #110 | Saṃvṛti-sat | L67-L69, L85-L93 |
| B7 | #100, #109 | Paramārtha-sat | L67-L69, L85-L93 |
| B8 | #5, #74, #189 | Apoha / Double negation | L233-L255 |
| B9 | #72-73 | Prasajya / Paryudāsa | L27 (listed only — may need P-MINE) |
| B10 | #189, #192 | Anyāpoha | L233-L255 |
| B11 | #128, #180-183 | Trairūpya-hetu | L107-L215 |
| B12 | #106, #96 | Gold-testing / Buddha's authority | L77-L87 |
| B13 | #12, #107 | Scepticism (saṃśaya) | L37-L45, L81-L83 |
| B14 | #39-40 | Dependent arising | L23-L33 (§1 doctrinal principles) |
| B15 | #42, #54 | Avidyā → Prajñā | L23-L33, L259-L263 |

---

## APPENDIX B — Cross-Reference with Prior Triple-Lens Findings

Where Buddhist lens findings may interact with prior audit results:

| Prior finding | Buddhist lens | Potential interaction |
|---------------|---------------|----------------------|
| RC1 — Epistemological underspecification (Kant) | B1 (Pramāṇa structure) | Buddhist pramāṇa provides the VOCABULARY to specify what Kant said was underspecified |
| C5×L2a — Essential variables (Ashby, KEEP as future work) | B3 (Svalakṣaṇa) | Buddhist epistemology accepts that unique particulars are INEXPRESSIBLE — this provides philosophical justification for why essential variables cannot be fully specified |
| C14 — Isomorphism→Homomorphism (Ashby) | B8, B10 (Apoha) | Apoha semantics provides an alternative framework for understanding conceptual mapping — not as positive correspondence but as exclusion-based |
| C1×L3d — Static vs dynamic (Weick, FIXED) | B6 (Saṃvṛti-sat) | The processual framing ("diễn ra khi") already maps to conventional truth as dynamic designation — strengthen by adding Two Truths vocabulary |
| C3×L1c — "Chưa bao giờ" (Kant, FIXED) | B13 (Scepticism) | Buddhist methodological doubt (saṃśaya) provides a positive framing for why the framework STARTS from a question, not a declaration |

---

**PLAN STATUS: DRAFT — AWAITING USER APPROVAL**

> Respond with:
> - **"yes" / "proceed" / "execute"** — begin Phase 1 audit execution
> - **"modify: [specific changes]"** — adjust scope, concepts, priorities, or deliverables
> - **"specific claim: [C#]"** — audit only one claim as a trial run
> - **"phase 1 only"** — execute Phase 1 and pause before Phase 2

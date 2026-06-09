# PLAN — RCA AUDIT: `index.html` (Mạch Rễ Landing Page) × Triple Lens
<!-- 3-round RCA × 5-Why × scoring gate ≥ 4/5 — applied to the audit plan itself -->
<!-- Date: 2026-06-09 | Method: RCA-driven audit planning | Status: DRAFT — awaiting approval -->
<!-- Revision: v2 — added full-source fallback tier per user directive -->

## METADATA

```
document_type     : plan_audit_rca
subject           : index.html (Mạch Rễ landing page, v2.0, 486 lines)
audit_lenses      :
  L1 — Kant_Transcendental_Arguments_RCA.md         (62 concepts, epistemology)
       └─ full source: Kant_Transcendental_Arguments.html  (SEP article, HTML)
  L2 — 945973-An-Introduction-to-Cybernetics-Ashby_RCA_Ashby_Cybernetics.md (100 concepts)
       └─ full source: 945973-An-Introduction-to-Cybernetics-Ashby.txt  (Ashby 1956, 7035 lines)
  L3 — 672922816-Loosely-Coupled-Systems-A-Reconceptualization-1_RCA_Table.md (80 concepts)
       └─ full source: 672922816-Loosely-Coupled-Systems-A-Reconceptualization-1.txt  (Orton & Weick 1990)
reference_tier    : TWO-TIER
  Tier 1 (primary)   — RCA concept tables (pre-extracted, line-evidenced, 242 concepts total)
  Tier 2 (fallback)  — full source documents (line-evidenced verification, concept mining, dispute resolution)
method            : 3-round RCA × 5-Why × scoring gate ≥ 4/5
                    triangulation rule: claim strength ∝ ≥2/3 lens convergence
                    deep reference protocol: escalate to Tier 2 when Tier 1 is insufficient
references        :
  - index.html (audit target)
  - CLAUDE.md (RULE ZERO — RCA procedure)
  - plan/dictionary_rule.md (canonical lookup table)
  - axiom_spec.md (canonical axiom definitions)
  - review/PLAN_RCA_REVIEW_audit_mach_re_phan_ngoc.md (structural template)
status            : DRAFT — awaiting user approval before execution
```

---

## EXECUTIVE SUMMARY

**Verdict: Audit is worth executing. The plan identifies 16 auditable claims in `index.html`, selects 18 diagnostic concepts from 242 available across 3 lenses, and proposes a 2-phase execution with 5 deliverables. A two-tier reference architecture (RCA Table → Full Source) ensures that no diagnostic dead-end blocks the audit.**

`index.html` is the public-facing root of Mạch Rễ — the first thing any visitor reads. It makes claims about what the framework IS, what PROBLEM it solves, HOW it was derived, WHO it applies to, and what its HISTORICAL ANCHORS are. Every claim on this page sets expectations that downstream pages must fulfill. If a claim on `index.html` is over-scoped, unfalsifiable, or category-confused, the entire framework inherits that defect.

The three audit lenses provide complementary diagnostics:
- **Kant (L1)**: Epistemological status of claims — are they presented as necessary conditions, modest interpretations, or something in between? Does the framework claim existence or only belief?
- **Ashby (L2)**: System formalization — are "survival," "stability," "identity," and "regulation" defined with operational precision? Does the framework account for variety?
- **Weick/Orton (L3)**: Dialectical integrity — does the framework preserve simultaneous openness/closedness, or does it drift toward unidimensional description?

**Each lens has two reference tiers:**
- **Tier 1 (RCA Table)**: Pre-extracted concept tables with line-evidenced definitions — used for fast diagnostic matching. 242 concepts across 3 tables.
- **Tier 2 (Full Source)**: Complete original texts — used when (a) the RCA table's definition is insufficient for the nuance needed, (b) a concept exists in the source but was not extracted into the table, (c) a dispute about interpretation arises, or (d) the recalibration checkpoint reveals a gap in the 18 selected concepts.

**The plan itself scores 4.4/5 through the RCA gate** (see §7), confirming its feasibility, low conflict risk, and strong method alignment. The two-tier architecture eliminates the single-point-of-failure risk (RCA table extraction error) that was present in v1.

---

## 1. AUDIT SCOPE

### 1.1 Target: `index.html` claim inventory

The page makes 16 claims distributed across 5 zones:

| Zone | Claims | Description |
|------|--------|-------------|
| **Z1 — Hero** (L244–259) | C1, C12 | Branding, scope badges, historical existence claim |
| **Z2 — What is Mạch Rễ** (L262–275) | C2, C3, C4, C5 | Framework definition, systematization, applicability, central question |
| **Z3 — Navigation Grid** (L278–348) | C6, C7 | Derivation method, axiom architecture |
| **Z4 — Timeline Strip** (L351–379) | C8, C9, C10, C11 | Historical anchor claims |
| **Z5 — Glossary** (L452–477) | C13, C14, C15, C16 | Technical term definitions |

### 1.2 Full claim catalog

| ID | Claim text (paraphrased) | Claim type | Zone |
|----|--------------------------|------------|------|
| **C1** | "Mạch Rễ là khung nền (framework) nhận dạng và thực hành bản sắc sinh tồn" | Definitional | Z1 |
| **C2** | "đặt tên và hệ thống hóa triết lý sinh tồn của dân tộc Việt Nam" | Method/product | Z2 |
| **C3** | "được sống qua 4.000 năm nhưng chưa bao giờ được viết thành lý thuyết" | Historical existence | Z2 |
| **C4** | "Áp dụng cho cá nhân, cộng đồng, và tổ chức đang đối mặt với áp lực đồng hóa" | Applicability scope | Z2 |
| **C5** | "Làm sao giữ được mình khi tất cả muốn thay đổi mình?" | Core problem (transcendental question) | Z2 |
| **C6** | "Bản tái dựng (rebuild 2026) suy từ câu hỏi gốc, neo 3 hệ độc lập" | Derivation method | Z3 |
| **C7** | "4 Tiên Đề Cốt Lõi (I–IV) + 4 Mệnh Đề Dẫn Xuất (V–VII, F) + 1 Meta-Tiên Đề (VIII)" | Architecture | Z3 |
| **C8** | "~179 TCN — Bắt đầu 1.000 năm Bắc thuộc — tiếng Việt không mất" | Historical anchor | Z4 |
| **C9** | "TK 13 — Trúc Lâm Thiền — Mạch Rễ mặc áo Phật giáo nhập thế" | Historical anchor | Z4 |
| **C10** | "1994 — Đường dây 500kV — Mạch Rễ trong hành động hiện đại" | Historical anchor | Z4 |
| **C11** | "1997 — Bình thường hóa Việt–Mỹ — hòa giải không quên" | Historical anchor | Z4 |
| **C12** | "Mạch Rễ tồn tại trước mọi nhà nước Việt Nam hiện đại và thuộc về toàn thể dân tộc" | Pre-political existence | Z1 (disclaimer) |
| **C13** | Glossary: "Framework = Hệ thống công cụ nhận dạng và thực hành bản sắc sinh tồn" | Definitional | Z5 |
| **C14** | Glossary: "Isomorphism = Hai cấu trúc khác nhau về nội dung nhưng giống nhau về kiểu quan hệ" | Definitional | Z5 |
| **C15** | Glossary: "Invariant = Yếu tố không thay đổi khi mọi thứ khác thay đổi — cốt lõi bản sắc" | Definitional | Z5 |
| **C16** | Glossary: "Attractor basin = Vùng mà hệ thống luôn tự động quay về sau mọi biến động" | Definitional | Z5 |

### 1.3 What is NOT audited

- CSS/styling, visual design, typography (presentational, not doctrinal)
- Navigation structure (unless it materially misrepresents content)
- Footer text (duplicates disclaimer — audited once under Z5)
- Linked pages (`what.html`, `axioms.html`, etc.) — out of scope for this audit; each would require its own audit plan

---

## 2. TWO-TIER REFERENCE ARCHITECTURE

### 2.1 Architecture diagram

```
┌─────────────────────────────────────────────────────────┐
│                    AUDIT EXECUTION                       │
│                                                         │
│  For each claim Cᵢ × lens Lⱼ:                           │
│                                                         │
│  ┌──────────────────┐                                   │
│  │ TIER 1 (primary) │ ←── Always start here             │
│  │   RCA Table      │     Fast concept lookup           │
│  │   242 concepts   │     Line-evidenced definitions    │
│  │   18 selected    │     Pre-verified against source   │
│  └────────┬─────────┘                                   │
│           │                                             │
│           │ Is the RCA table definition sufficient?     │
│           │                                             │
│     ┌─────┴─────┐                                       │
│     │ YES       │ NO — escalate                         │
│     ▼           ▼                                       │
│  Proceed    ┌──────────────────────┐                    │
│  with       │ TIER 2 (verification)│                    │
│  diagnosis  │   Full Source        │                    │
│             │   Original text      │                    │
│             │   Line-evidenced     │                    │
│             │   4 escalation paths │                    │
│             └──────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

### 2.2 Tier 1 — RCA Concept Tables (primary)

| Lens | File | Size | Concepts | Selected |
|------|------|------|----------|----------|
| L1 — Kant | `Kant_Transcendental_Arguments_RCA.md` | 77 lines | 62 concepts | 6 |
| L2 — Ashby | `945973-An-Introduction-to-Cybernetics-Ashby_RCA_Ashby_Cybernetics.md` | 121 lines | 100 concepts | 6 |
| L3 — Weick/Orton | `672922816-Loosely-Coupled-Systems-A-Reconceptualization-1_RCA_Table.md` | 97 lines | 80 concepts | 6 |
| **Total** | | | **242 concepts** | **18 selected** |

**Use Tier 1 when:**
- The diagnostic concept is among the 18 selected (see §3)
- The RCA table definition is sufficient for naming the defect
- The line evidence cited in the RCA table is adequate

### 2.3 Tier 2 — Full Source Documents (verification & fallback)

| Lens | File | Size | Format | Content |
|------|------|------|--------|---------|
| L1 | `Kant_Transcendental_Arguments.html` | SEP article | HTML | Full Stanford Encyclopedia entry on Kant's Transcendental Arguments |
| L2 | `945973-An-Introduction-to-Cybernetics-Ashby.txt` | 7,035 lines | Plain text | Ashby's complete 1956 book *An Introduction to Cybernetics* |
| L3 | `672922816-Loosely-Coupled-Systems-A-Reconceptualization-1.txt` | Full paper | Plain text | Orton & Weick (1990) *Academy of Management Review*, 15(2), 203–223 |

**Four escalation paths from Tier 1 → Tier 2:**

| Path | Trigger | Action |
|------|---------|--------|
| **P-VERIFY** | An RCA table definition seems incomplete or potentially inaccurate for the nuance needed | Read the surrounding paragraphs in the full source to confirm or correct the definition |
| **P-MINE** | The 18 selected concepts don't cover a defect that clearly exists — the concept is in the source but wasn't extracted into the RCA table | Search the full source for the missing concept; if found, add it to the diagnostic set for this claim |
| **P-DISPUTE** | Two lenses produce contradictory diagnoses and the conflict may stem from an RCA table interpretation error | Verify both interpretations against their full sources; resolve the conflict at the source level |
| **P-RECALIBRATE** | The recalibration checkpoint (§6) reveals that the 18 selected concepts miss a pattern visible across multiple claims | Mine all three full sources for concepts relevant to the newly discovered pattern |

### 2.4 Tier 2 usage protocol

1. **Always start at Tier 1** — use the RCA table concept first
2. **Escalate explicitly** — document which path triggered the escalation and what was found
3. **Cite line numbers from the full source** — maintain the same line-evidenced standard as the RCA tables
4. **If Tier 2 also fails** — mark the finding as `TENTATIVE (source-limited)` and flag for future investigation
5. **Do not re-extract the entire source** — only read the relevant sections; the RCA tables already did the heavy extraction work

---

## 3. AUDIT LENSES — DIAGNOSTIC CONCEPT SELECTION (Tier 1)

From 242 total concepts across 3 lenses, 18 diagnostic concepts are selected for relevance to `index.html` claims. Selection criterion: the concept must expose a *falsifiable* risk in at least one audited claim. If a selected concept proves insufficient during execution, escalate to Tier 2 via P-MINE.

### 3.1 L1 — Kant's Transcendental Arguments (6 of 62 concepts selected)

| L1# | Concept | RCA # | Applied to claim(s) | Diagnostic question |
|-----|---------|-------|---------------------|---------------------|
| L1a | Transcendental argument form | #2 | C5, C6 | Does C5 function as a transcendental argument premise? Is C6's "suy từ câu hỏi gốc" structurally equivalent to transcendental derivation? |
| L1b | Necessary condition (weaker than logical) | #3 | C5, C7 | Are the axioms presented as *logically* necessary or as the "only possible explanation" (weaker, Kantian sense)? |
| L1c | Stroud's challenge (1968) | #57 | C2, C3 | Does Mạch Rễ claim to establish *existence* of the framework in Vietnamese history, or only a *belief* about it? |
| L1d | Modest transcendental argument | #58 | C5, C6 | Should Mạch Rễ explicitly adopt "modest" scope — reasoning to conceptual commitment, not ontological existence? |
| L1e | Objective validity | #11 | C1, C7 | What would it mean for a Tiên Đề to have "objective validity"? Is this claimed? |
| L1f | Universality and necessity (criterion) | #35 | C4, C7 | Does C4's applicability claim ("cá nhân, cộng đồng, tổ chức") assert universality? If so, is necessity established? |

### 3.2 L2 — Ashby's Cybernetics (6 of 100 concepts selected)

| L2# | Concept | RCA # | Applied to claim(s) | Diagnostic question |
|-----|---------|-------|---------------------|---------------------|
| L2a | Essential variables | #72 | C1, C5 | What are Mạch Rễ's essential variables? Are they operationally defined, or does "bản sắc sinh tồn" function as a placeholder? |
| L2b | Survival as stability | #71 | C1, C3 | Is "sinh tồn" (survival) formalized as a set of states M₁…Mₖ stable under a transformation? |
| L2c | Variety + Law of Requisite Variety | #53, #77 | C4, C5 | Does the framework account for the *variety* of assimilation pressures it claims to regulate? Is V_R ≥ V_D? |
| L2d | Constraint | #55 | C6 | Is "neo 3 hệ độc lập" (anchoring in 3 independent systems) a constraint-detection method? Does it reduce variety correctly? |
| L2e | Isomorphism vs. Homomorphism | #50, #51 | C14 | Does the glossary correctly define isomorphism (one-one state correspondence), or is the actual relationship homomorphism (many-one, simplified)? |
| L2f | Black Box | #47 | C1, C3 | Is Vietnamese cultural history treated as a Black Box (internal structure inferred from I/O behavior), or is internal structure assumed? |

### 3.3 L3 — Loosely Coupled Systems (6 of 80 concepts selected)

| L3# | Concept | RCA # | Applied to claim(s) | Diagnostic question |
|-----|---------|-------|---------------------|---------------------|
| L3a | Loose coupling (dialectical) | #2, #6 | C1, C5 | Does the framework present identity as simultaneously responsive AND distinctive (dialectical), or does it drift toward one pole? |
| L3b | Drift hazard: imprecise generalization | #72 | C1, C2, C4 | Does `index.html` chain from "loose coupling claim" to "performance conclusion" without specifying which elements, domains, and characteristics? |
| L3c | Drift hazard: presence of connectedness | #74 | C3, C5 | Does the framework ignore the *connectedness* that actually exists in Vietnamese culture (focusing only on what persists), dissolving the dialectic? |
| L3d | Static vs. dynamic description | #71 | C1, C13, C15 | Is `index.html` using noun-based labeling ("this IS a framework") or verb-based framing ("identity survival occurs when…")? |
| L3e | Simultaneous loose-tight coupling | #64 | C5, C7 | Does the framework acknowledge that some elements must be *tightly* coupled for identity to persist? Does "đổi mà vẫn là mình" (Tiên Đề II) map to this? |
| L3f | Five voices framework | #14 | C1–C7 (structural) | Does `index.html` present only ONE voice (causation? direct effects?), or does it preserve the multi-voice dialectic? |

---

## 4. CLAIM-TO-LENS MAPPING (Audit Matrix)

Each claim receives ≥2 lens diagnostics where applicable. **Triangulation rule**: a finding is stronger if it emerges from ≥2/3 independent lenses.

| Claim | L1 (Kant) | L2 (Ashby) | L3 (Weick/Orton) | Lens count | Priority |
|-------|-----------|------------|-------------------|------------|----------|
| C1 | L1e | L2a, L2b, L2f | L3a, L3b, L3d | 3 | **HIGH** |
| C2 | L1c | — | L3b | 2 | **HIGH** |
| C3 | L1c | L2b, L2f | L3c | 3 | **HIGH** |
| C4 | L1f | L2c | L3b | 3 | MEDIUM |
| C5 | L1a, L1b, L1d | L2a, L2c | L3a, L3c, L3e | 3 | **HIGH** |
| C6 | L1a, L1d | L2d | — | 2 | **HIGH** |
| C7 | L1b, L1e, L1f | — | L3e | 2 | MEDIUM |
| C8 | — | — | L3c | 1 | LOW |
| C9 | — | — | L3c | 1 | LOW |
| C10 | — | — | — | 0 | LOW |
| C11 | — | — | — | 0 | INFO |
| C12 | L1c | — | — | 1 | MEDIUM |
| C13 | — | — | L3d | 1 | MEDIUM |
| C14 | — | L2e | — | 1 | MEDIUM |
| C15 | — | — | L3d | 1 | MEDIUM |
| C16 | — | L2b | — | 1 | MEDIUM |

**Priority legend:**
- **HIGH** (6 claims): ≥3 lenses OR ≥2 lenses with high structural weight — audit first
- **MEDIUM** (8 claims): 1–2 lenses, definitional/historical — audit second
- **LOW** (1 claim): single lens, historical anchor — audit if time permits
- **INFO** (1 claim): zero lens coverage — note as out-of-scope for current lens set; consider Tier 2 mining (P-MINE) if the claim becomes relevant during execution

---

## 5. AUDIT METHODOLOGY — 3-ROUND RCA PER CLAIM

### 5.1 Procedure (per claim, per lens)

```
FOR each HIGH-priority claim Cᵢ:
  FOR each applicable lens Lⱼ:
    1. MATCH (Tier 1) — identify which lens concept(s) apply from the selected 18
       → If concept definition is insufficient → escalate to Tier 2 via P-VERIFY
       → If no selected concept covers the defect → escalate to Tier 2 via P-MINE
    2. DIAGNOSE — apply 5-Why to the mismatch
       → If 5-Why chain needs source-level nuance → escalate to Tier 2 via P-VERIFY
    3. SCORE — 5-criterion scoring gate (Correct/Deep/Feasible/Conflict-risk/Preservation)
    4. TRIANGULATE — if ≥2 lenses flag the same root cause, finding is CONFIRMED
       → If lenses contradict → escalate to Tier 2 via P-DISPUTE
    5. RECOMMEND — propose fix or mark as "keep as-is"
```

### 5.2 Three-round depth structure

| Round | Depth | Question | Lens role | Tier used |
|-------|-------|----------|-----------|-----------|
| **R1 — Symptom** | Surface defect in claim wording | "What is wrong on the page?" | Lens concept provides the *vocabulary* to name the defect precisely | Tier 1 (concept definition) |
| **R2 — Mechanism** | Why the defect backfires *here specifically* | "Why does this defect matter for Mạch Rễ?" | Lens provides the *theoretical reason* the defect is consequential | Tier 1 → Tier 2 if nuance needed |
| **R3 — Root** | Which internal standard does it violate? | "What rule does Mạch Rễ set for itself that this claim breaks?" | Lens provides the *external benchmark* against which internal consistency is measured | Tier 1 → Tier 2 if source verification needed |

### 5.3 Scoring gate (per claim-lens finding)

Same 5-criterion rubric from CLAUDE.md RULE ZERO:

| Criterion | Question | High score means |
|-----------|----------|-----------------|
| Correct | Is this genuinely a defect (overclaim, category error, missing definition)? | Real defect found |
| Deep | Does the finding touch the root (internal consistency), not just surface wording? | Reaches root |
| Feasible | Can it be fixed without breaking core structure/meaning? | Safe to fix |
| Conflict-risk | Will the fix avoid creating contradictions elsewhere? | Low new risk |
| Preservation | Is the core strength kept after the fix? | Strength preserved |

**Threshold: average ≥ 4/5 → recommend fix; < 4/5 → keep as-is, document why.**

### 5.4 Triangulation rule

A finding is:
- **CONFIRMED** if ≥2/3 lenses independently identify the same root cause
- **PROBABLE** if 1 lens identifies it and ≥1 other lens is consistent (does not contradict)
- **TENTATIVE** if only 1 lens identifies it and other lenses are silent or inapplicable
- **TENTATIVE (source-limited)** if neither Tier 1 nor Tier 2 provides sufficient diagnostic vocabulary — flag for future investigation
- **DISCARDED** if ≥2 lenses produce contradictory diagnoses *after Tier 2 verification* (escalate via P-DISPUTE first)

---

## 6. EXECUTION PLAN — 2 PHASES, 5 DELIVERABLES

### Phase 1: HIGH-priority claims (estimated: 1 session, 6 claims × 2–3 lenses each = 12–18 diagnostic passes)

| Step | Action | Tier 2 escalation expected? | Output |
|------|--------|---------------------------|--------|
| P1.1 | Audit C5 (central question) through L1a, L1b, L1d + L2a, L2c + L3a, L3c, L3e | **Yes** — C5 is the deepest claim; L1a (transcendental argument form) likely needs full-source verification of Kant's original formulation | 8 diagnostic findings |
| P1.2 | Audit C1 (framework definition) through L1e + L2a, L2b, L2f + L3a, L3b, L3d | **Yes** — L2a (essential variables) likely needs Ashby §10/4–10/6 in full source for precise operational definition | 7 diagnostic findings |
| P1.3 | Audit C3 (historical existence) through L1c + L2b, L2f + L3c | **Possible** — L1c (Stroud's challenge) may need the full SEP article's §4 for exact formulation | 4 diagnostic findings |
| P1.4 | Audit C2 (systematization) through L1c + L3b | Unlikely — both concepts have clear RCA table definitions | 2 diagnostic findings |
| P1.5 | Audit C6 (derivation method) through L1a, L1d + L2d | **Possible** — L2d (constraint) may need Ashby §7 for the formal definition of constraint-as-variety-reduction | 3 diagnostic findings |
| P1.6 | Triangulation synthesis — cross-reference Phase 1 findings, identify root patterns | N/A | Synthesis table |

**Deliverable D1**: `review/audit_index_html_triple_lens_phase1.md` — per-claim diagnostic table with scores, Tier 2 escalations documented

### Phase 2: MEDIUM + LOW priority claims + integration

| Step | Action | Tier 2 escalation expected? | Output |
|------|--------|---------------------------|--------|
| P2.1 | Audit C4, C7 (applicability, architecture) through remaining lenses | Possible for L2c (Law of Requisite Variety — Ashby §11) | 5 diagnostic findings |
| P2.2 | Audit C12–C16 (glossary + disclaimer) through applicable lenses | **Yes** — L2e (isomorphism vs homomorphism) strongly needs Ashby §6/12–6/14 in full source; the distinction is subtle and the RCA table summary may not capture it fully | 5 diagnostic findings |
| P2.3 | Audit C8–C11 (timeline) through applicable lenses | Unlikely — historical claims; if L3c diagnosis is thin, may P-MINE the Orton & Weick full text for additional drift-hazard concepts | 3 diagnostic findings |
| P2.4 | Cross-reference with `axiom_spec.md` — verify index.html claims match canonical definitions | N/A (canonical reference, not a lens source) | Consistency report |

**Deliverable D2**: `review/audit_index_html_triple_lens_phase2.md` — remaining claims + consistency check

**Deliverable D3**: `review/audit_index_html_triple_lens_root_causes.md` — synthesized root cause map (which root causes recur across multiple claims), with Tier 2 verification status

**Deliverable D4**: `review/audit_index_html_triple_lens_fix_proposals.md` — prioritized fix proposals with dependency chain, effort estimate, and risk assessment

**Deliverable D5**: `CHANGELOG.md` entries for any claim that is modified

### Phase 1 recalibration checkpoint

After auditing C5, C1, and C3 (first 3 HIGH-priority claims), pause and assess:

| Checkpoint question | Action if "no" |
|---------------------|----------------|
| Are the 18 selected Tier 1 concepts sufficient? | P-MINE the full sources for additional concepts; expand the diagnostic set |
| Have any RCA table definitions been found inaccurate or incomplete? | Document the corrections; flag the RCA table for future revision (separate task) |
| How many Tier 2 escalations occurred? | If >50% of passes needed Tier 2, the 18-concept selection may be too narrow — expand |
| What is the average token/pass? | Re-estimate Phase 1 and Phase 2 completion; reduce scope to HIGH-only if needed |
| Are the three full sources actually needed, or are the RCA tables sufficient? | If 0 Tier 2 escalations, the RCA tables are well-extracted — proceed with confidence |

---

## 7. SELF-AUDIT — 3-ROUND RCA ON THIS PLAN (v2)

### Round 1 — Symptom

| # | Surface concern | New in v2? |
|---|----------------|------------|
| S1 | The plan selects 18/242 concepts — how do we know these are the RIGHT 18? | v1 |
| S2 | C10 and C11 score 0 lens coverage — should we add a lens or exclude the claims? | v1 |
| S3 | The plan audits `index.html` but not its linked pages — findings may be incomplete if root causes live downstream | v1 |
| S4 | Phase 1 estimates 12–18 diagnostic passes but doesn't estimate tokens/time per pass | v1 |
| **S5** | **The RCA tables are themselves extractions — what if an extraction error propagates into the audit?** | **v2** |
| **S6** | **Tier 2 full sources are large (Ashby = 7035 lines) — how do we avoid scope-creep into re-reading entire books?** | **v2** |

### Round 2 — Mechanism

**S1**: The 18 concepts were selected by *relevance to auditable claim types* (definitional, epistemological, systemic, dialectical), not by random sampling. The two-tier architecture now provides a safety net: if a selected concept misses a defect, P-MINE opens the full source for additional concept discovery. The recalibration checkpoint explicitly tests sufficiency after 3 claims.

**S2**: C10 and C11 are *factual historical claims* — the three lenses are not designed to audit historical facts. This is a lens limitation, not a plan defect. However, P-MINE is available: if, during execution, a historical claim reveals a structural/epistemological dimension, the full sources can be mined for relevant concepts not in the RCA tables. Example: Ashby's "repetitive disturbance" (#89) or "Grand Disturbance" (#88) might apply to C11's "hòa giải không quên" if reframed as regulatory learning.

**S3**: Legitimate scope boundary. Cross-reference with `axiom_spec.md` in P2.4 prevents false positives where `index.html`'s summary is imprecise but the canonical definition is precise.

**S4**: Estimation gap mitigated by the recalibration checkpoint (now with explicit token/pass metric).

**S5** (NEW): This is the critical risk that v2 addresses. The RCA tables were created by human extraction — they may contain interpretation errors, omissions, or over-compression. The two-tier architecture eliminates this single point of failure: every RCA table concept can be verified against its full source. The escalation paths P-VERIFY and P-DISPUTE are specifically designed to catch extraction errors. Additionally, if a pattern of extraction errors is found, the RCA tables themselves become candidates for revision (separate task, flagged in D4).

**S6** (NEW): The Tier 2 usage protocol (§2.4) enforces surgical reading: "Do not re-extract the entire source — only read the relevant sections." The RCA tables already provide line-number citations, so Tier 2 reads are targeted: find the cited line, read ±20 lines of context. The Ashby RCA table already cites specific sections (S.x/y notation), making targeted lookup efficient. For the Kant HTML, the RCA table cites specific line numbers from the stripped plain-text version. The protocol's rule 5 ("Do not re-extract") is enforced by the audit executor's discipline, not by tooling — the recalibration checkpoint monitors Tier 2 usage to catch scope creep.

### Round 3 — Root

| Symptom | Root cause (one sentence) | Score |
|---------|--------------------------|-------|
| S1 | Concept selection is heuristic — but documented, transparent, and now backed by P-MINE fallback to full sources | **4.5/5** (↑ from 4/5 in v1) |
| S2 | Lens scope limitation (historical claims are factual, not structural) — correctly identified; P-MINE provides a theoretical escape hatch if needed | **5/5** |
| S3 | Scope boundary between `index.html` (summary) and `axiom_spec.md` (canonical) is explicit — P2.4 cross-reference enforces it | **4/5** |
| S4 | Estimation uncertainty is inherent in diagnostic work — recalibration checkpoint now includes explicit token/pass and Tier-2-usage metrics | **4/5** |
| S5 | RCA table extraction error risk is real but fully mitigated by two-tier architecture with explicit P-VERIFY and P-DISPUTE paths | **5/5** (new) |
| S6 | Full-source scope creep is a discipline risk, not an architectural risk — Tier 2 usage protocol (§2.4) with its 5 rules and checkpoint monitoring provides sufficient guardrails | **4/5** (new) |

**Average: 4.42/5 (↑ from 4.25/5 in v1) — plan is sound; two-tier architecture eliminates the primary structural risk.**

---

## 8. RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation | New in v2? |
|------|-----------|--------|------------|------------|
| Selected lens concepts miss a critical defect | MEDIUM | HIGH | Recalibration checkpoint + P-MINE escalation to full sources | ↑ strengthened |
| RCA table extraction error propagates into audit finding | MEDIUM | **HIGH** | P-VERIFY path: verify any suspicious or load-bearing definition against the full source before finalizing the finding | **YES** |
| Tier 2 full-source reading balloons into re-reading entire books | MEDIUM | MEDIUM | §2.4 protocol rule 5 ("Do not re-extract"); targeted ±20 line reads from cited line numbers; recalibration checkpoint monitors Tier 2 usage | **YES** |
| Findings are all "keep as-is" (audit is too conservative) | LOW | MEDIUM | The 3-lens method + Tier 2 depth makes false negatives unlikely |
| Findings are all "fix" (audit is too aggressive, overfitting to lenses) | MEDIUM | MEDIUM | Triangulation rule (≥2/3 lenses) + Tier 2 source verification prevents single-lens overfitting |
| `index.html` claims are imprecise summaries of precise canonical definitions — audit produces false positives | MEDIUM | HIGH | Phase 2 cross-reference with `axiom_spec.md` before finalizing any fix proposal |
| Audit scope creep — findings pull in linked pages | HIGH | LOW | Strict scope boundary enforced; flag cross-page issues as "out of scope" |
| Token budget exceeded in Phase 1 | MEDIUM | MEDIUM | Recalibration checkpoint; explicit token/pass tracking; reduce to HIGH-only if needed |
| Full source files are too large to read in one pass | LOW | MEDIUM | The Ashby .txt (7035 lines) is the only large file; RCA table line citations enable targeted reads; Read tool supports offset+limit for surgical access |

---

## 9. DEPENDENCY CHAIN

```
Phase 1 (HIGH claims)
  ├── P1.1 (C5) ──┐
  ├── P1.2 (C1) ──┤── Independent — can run in parallel
  ├── P1.3 (C3) ──┤     Tier 2 escalations are claim-local (no cross-claim dependency)
  ├── P1.4 (C2) ──┘
  ├── P1.5 (C6) ←── Benefits from P1.1–P1.4 findings (C6's "neo 3 hệ" claim connects to C1–C5)
  └── P1.6 (Synthesis) ←── Depends on ALL Phase 1 findings

RECALIBRATION CHECKPOINT ←── After P1.1–P1.3
  ├── Assess Tier 2 usage rate
  ├── Assess RCA table accuracy
  ├── Re-estimate tokens/pass
  └── Decide: expand concept set? reduce scope?

Phase 2 (MEDIUM + LOW claims)
  ├── P2.1 (C4, C7) ←── Benefits from Phase 1 synthesis
  ├── P2.2 (C12–C16) ←── Independent; P2.2's L2e strongly needs Tier 2 (Ashby §6/12–6/14)
  ├── P2.3 (C8–C11) ←── Independent (historical claims)
  └── P2.4 (axiom_spec.md cross-ref) ←── Depends on ALL findings

Phase 3 (Deliverables)
  ├── D3 (Root cause map) ←── Depends on Phase 1 + Phase 2
  ├── D4 (Fix proposals) ←── Depends on D3
  └── D5 (CHANGELOG) ←── Depends on D4
```

---

## 10. EXPECTED OUTCOMES (Hypotheses)

Based on structural analysis of `index.html` before audit execution, the most likely findings are:

| Hypothesis | Lens | Prior probability | Tier 2 needed? | If confirmed |
|------------|------|-------------------|----------------|--------------|
| **H1**: C5 is framed as a transcendental question but is not explicitly labeled as such — the epistemological status of the central question is ambiguous | L1 | HIGH | **Yes** — Kant's original formulation of "transcendental argument" (SEP §1) should be cited directly | Add a boundary statement clarifying that C5 is the *premise* of a transcendental-style argument, not an empirical question |
| **H2**: "Bản sắc sinh tồn" (C1) has no Ashby-style operational definition — essential variables are not specified | L2 | HIGH | **Yes** — Ashby §10/4–10/6 (survival as stability) and §10/5 (essential variables) should be read directly | Define the essential variables that must be kept within limits for "survival" to hold |
| **H3**: C3's "4.000 năm…chưa bao giờ được viết thành lý thuyết" may be an overclaim — fragments of theory exist in Vietnamese scholarship | L1 (Stroud) | MEDIUM | Possible — Stroud 1968 formulation in SEP §4 | Scope the claim: "chưa được hệ thống hóa thành framework" rather than "chưa bao giờ được viết" |
| **H4**: The glossary definition of "Isomorphism" (C14) may actually describe "Homomorphism" in Ashby's sense (many-one, not one-one) | L2 | MEDIUM | **Yes** — Ashby §6/12 (isomorphism) and §6/14 (homomorphism) are distinct and the distinction is load-bearing | Correct the glossary or justify the stronger claim with one-one correspondence evidence |
| **H5**: `index.html` uses predominantly static/noun-based framing ("Mạch Rễ LÀ…") — missing verb-based process description | L3 | MEDIUM | Possible — Orton & Weick § "Static vs. dynamic description" (p. 846–874 in source) | Add dynamic framing: "Mạch Rễ occurs when…" or "Loose coupling in Vietnamese identity appears when…" |
| **H6**: The timeline (C8–C11) treats historical events as *manifestations* of Mạch Rễ without stating the inference direction — is this forward projection or backward pattern-matching? | L1 (necessary condition) | LOW | Unlikely | Add an explicit note: "These are interpretive anchors, not deductive proofs" |

---

## 11. CONFIRMATION CHECKLIST

Before execution begins, confirm:

- [ ] User approves this plan (yes / modify / no)
- [ ] `axiom_spec.md` is up-to-date and can serve as canonical reference for cross-validation
- [ ] The three RCA concept tables (Tier 1) are finalized — no pending edits
- [ ] The three full source documents (Tier 2) are accessible and correctly formatted
- [ ] Token budget for Phase 1 is agreed, including anticipated Tier 2 reads
- [ ] Output directory is confirmed: `review/` (matching existing `review/audit_mach_re_phan_ngoc.md` convention)

---

## APPENDIX A — Lens Concept Cross-Reference (Tier 1)

Full mapping of 18 selected concepts to their source RCA tables and full-source locations for Tier 2 verification:

| This plan | RCA Table doc | Row # | Concept name | Tier 2 fallback location |
|-----------|--------------|-------|-------------|--------------------------|
| L1a | Kant_RCA | #2 | Transcendental argument | `Kant_Transcendental_Arguments.html` L2–L9 (SEP §1 opening) |
| L1b | Kant_RCA | #3 | Necessary condition (transcendental) | `Kant_Transcendental_Arguments.html` L10–L13 |
| L1c | Kant_RCA | #57 | Stroud's challenge (1968) | `Kant_Transcendental_Arguments.html` L672–L685 (SEP §4) |
| L1d | Kant_RCA | #58 | Modest transcendental argument | `Kant_Transcendental_Arguments.html` L690–L703 |
| L1e | Kant_RCA | #11 | Objective validity | `Kant_Transcendental_Arguments.html` L78–L81 |
| L1f | Kant_RCA | #35 | Universality and necessity | `Kant_Transcendental_Arguments.html` L362–L380 (SEP §18–19) |
| L2a | Ashby_RCA | #72 | Essential variables | `Ashby.txt` L4998–L5033 (S.10/5–10/6) |
| L2b | Ashby_RCA | #71 | Survival as stability | `Ashby.txt` L4938–L5000 (S.10/3–10/4) |
| L2c | Ashby_RCA | #53, #77 | Variety + Law of Requisite Variety | `Ashby.txt` L3228–L3284 (S.7/6–7/7), L5200–L5260 (S.11/6–11/7) |
| L2d | Ashby_RCA | #55 | Constraint | `Ashby.txt` L3284–L3316 (S.7/10) |
| L2e | Ashby_RCA | #50, #51 | Isomorphism vs. Homomorphism | `Ashby.txt` L2686–L2835 (S.6/12–6/14) |
| L2f | Ashby_RCA | #47 | Black Box | `Ashby.txt` L2288–L2350 (S.6/1–6/3) |
| L3a | Weick_RCA | #2, #6 | Loose coupling (dialectical) | `Orton_Weick.txt` L66–L68, L122–L159 |
| L3b | Weick_RCA | #72 | Drift hazard: imprecise generalization | `Orton_Weick.txt` L894–L898 |
| L3c | Weick_RCA | #74 | Drift hazard: presence of connectedness | `Orton_Weick.txt` L875–L893 |
| L3d | Weick_RCA | #71 | Static vs. dynamic description | `Orton_Weick.txt` L846–L874 |
| L3e | Weick_RCA | #64 | Simultaneous loose-tight coupling | `Orton_Weick.txt` L666–L680 |
| L3f | Weick_RCA | #14 | Five voices framework | `Orton_Weick.txt` L101–L108 |

---

## APPENDIX B — Tier 2 Quick-Reference Map

For efficient surgical reads during audit execution:

### L1 — Kant (SEP HTML)
| Concept area | Line range in stripped text | SEP section |
|-------------|---------------------------|-------------|
| Transcendental argument definition | L2–L28 | §1 Introduction |
| Transcendental Deduction (A & B) | L44–L178 | §2 Transcendental Deduction |
| Apperception & unity | L189–L270 | §2 (continued) |
| Single-Substantive-Premise debate | L280–L315 | §2 (interpretive) |
| Objective validity & universality | L330–L470 | §2 (continued) |
| B-Deduction second step | L478–L525 | §2 (continued) |
| Refutation of Idealism | L530–L632 | §3 Refutation of Idealism |
| Strawson & Stroud (contemporary) | L645–L760 | §4 Contemporary Arguments |

### L2 — Ashby (plain text, 7035 lines)
| Concept area | Line range | Ashby section |
|-------------|-----------|---------------|
| Change, transformation, machines | L334–L838 | Ch.2–3 |
| Coupling, feedback, independence | L1244–L1598 | S.4/1–4/14 |
| Stability, equilibrium, cycles | L1962–L2283 | S.5/2–5/14 |
| Black Box | L2288–L2469 | S.6/1–6/6 |
| Isomorphism, homomorphism, emergence | L2686–L2976 | S.6/12–6/18 |
| Variety, constraint, information | L3109–L4110 | Ch.7–9 |
| Regulation, Requisite Variety | L4938–L5260 | Ch.10–11 |
| Error-controlled & Markovian regulation | L5535–L5883 | S.12/2–12/15 |
| Ultrastability, amplification | L6060–L6800 | S.12/22–14/6 |

### L3 — Orton & Weick (plain text)
| Concept area | Approximate line range | Article section |
|-------------|----------------------|-----------------|
| Definitions & dialectical interpretation | L63–L170 | Introduction |
| Five voices framework | L101–L108 (overview) | Introduction |
| Voice of causation | L179–L262 | §Causation |
| Voice of typology | L259–L373 | §Typology |
| Voice of direct effects | L374–L462 | §Direct Effects |
| Voice of compensations | L422–L548 | §Compensations |
| Voice of organizational outcomes | L527–L692 | §Organizational Outcomes |
| Preliminary causal model | L693–L803 | §Model |
| Puzzles & methodological recommendations | L728–L898 | §Discussion |

---

## APPENDIX C — Method Compliance Checklist

Per CLAUDE.md RULE ZERO:

| RCA Step | Applied to | Status |
|----------|-----------|--------|
| 1. Define | Audit plan design | ✅ Claims catalogued (§1.2), lenses selected (§3), mapping created (§4), two-tier architecture defined (§2) |
| 2. Trace (3-round) | Plan self-audit | ✅ 3-round RCA on plan itself (§7), including 2 new v2 concerns (S5, S6) |
| 3. Isolate | Plan risks | ✅ Root causes identified for each plan concern (§7 Round 3); new v2 risks added to risk table (§8) |
| 4. Fix cause | Plan adjustments | ✅ Two-tier architecture added to eliminate RCA-table-extraction-error single point of failure; Tier 2 usage protocol with 5 rules; recalibration checkpoint expanded |
| 5. Verify | Plan scoring | ✅ Self-audit score 4.42/5 ≥ 4/5 threshold (↑ from 4.25 in v1) |

Per CLAUDE.md Tiên Đề III Essence/Manifestation rule:
- Glossary definitions are checked for essence/manifestation conflation (C15 "Invariant")

Per CLAUDE.md Paper & Publication Rules:
- RCA before claim modification: ✅ Plan self-audit (§7) applies the same rubric
- Claim Ladder: ✅ Each hypothesis (§10) states its epistemic level
- Boundary Statement: ✅ §1.3 defines what is NOT audited

---

**PLAN STATUS: DRAFT v2 — AWAITING USER APPROVAL**

> Respond with:
> - **"yes" / "proceed" / "execute"** — begin Phase 1 audit execution
> - **"modify: [specific changes]"** — adjust scope, lenses, priorities, or deliverables
> - **"phase 2 only"** — skip Phase 1, audit only MEDIUM/LOW claims
> - **"specific claim: [C#]"** — audit only one claim as a trial run

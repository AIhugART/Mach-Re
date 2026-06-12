Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# 04 — RCA Analysis: 5-Whys + Root Cause Taxonomy
## {{PROJECT_NAME}}

**Role:** Layer 4 of pipeline — from symptom + trace score, apply 5-Whys RCA to trace back to root cause. Inherits directly from project governance Rule Zero (5-step process).

**Input:** Component inventory (from `02_detection.md`) + trace score (from `03_sot_traceability.md`).
**Output:** Root cause (1 sentence) + verdict + documentation quality audit.
**Next:** `05_scoring.md` — 10-Point Hallucination Scale.

---

## 1. 5-Whys Standardized Template `[GENERIC]`

Apply to every component showing suspicion signs (trace score ≤ 2 or ORANGE+ signal):

```markdown
### W1: Why did [SYMPTOM] appear?
**Answer:** [Direct cause]

### W2: Why did [W1 CAUSE] happen?
**Answer:** [Cause 1 level deeper]

### W3: Why did [W2 CAUSE] happen?
**Answer:** [Cause 2 levels deeper]

### W4: Why did [W3 CAUSE] happen?
**Answer:** [Cause 3 levels deeper]

### W5: Is [COMPONENT] a fabrication?
**Answer:** YES / NO. [1-sentence explanation]

### Root Cause (1 sentence):
[Isolated root cause — the starting point of the failure]
```

### 1.1 Calibrated Example `[CALIBRATE — replace with {{PROJECT_NAME}} example]`

```
Symptom: {{SYMPTOM_DESCRIPTION}}
  W1: Why does {{SYMPTOM_SHORT}} appear?
    → {{W1_ANSWER}}
  W2: Why {{W2_QUESTION}}?
    → {{W2_ANSWER}}
  W3: Why {{W3_QUESTION}}?
    → {{W3_ANSWER}}
  W4: Why {{W4_QUESTION}}?
    → {{W4_ANSWER}}
  W5: Is {{COMPONENT}} a fabrication?
    → NO. {{W5_EXPLANATION}}

Root Cause: {{ROOT_CAUSE_1_SENTENCE}}
```

---

## 2. Root Cause Taxonomy (6 Types) `[GENERIC — calibrate examples for {{PROJECT_NAME}}]`

### Type 1 — Category Error

| Attribute | Description |
|-----------|-------------|
| **Definition** | Epistemology claim mistaken as physics claim (or vice versa); mapping treated as causal explanation |
| **Symptom** | Claim asserts "X solves/explains/predicts Y" without formal proof |
| **Example in {{PROJECT_NAME}}** | `{{CATEGORY_ERROR_EXAMPLE}}` |
| **Signal match** | R1 (category error), R4 (equivalence without justification) |
| **Solution type** | Reframe claim as interpretive mapping UNLESS formal proof + experimental test supplied |
| **Prevention** | Always place boundary statement: "this is an interpretive mapping, not a physical explanation" |

### Type 2 — Missing Definition

| Attribute | Description |
|-----------|-------------|
| **Definition** | Term used without formal definition |
| **Symptom** | Term appears ≥ 3 times without definition block |
| **Example in {{PROJECT_NAME}}** | `{{MISSING_DEF_EXAMPLE}}` |
| **Signal match** | O1 (undefined term) |
| **Solution type** | DOCUMENT — add definition block + link to SOT |
| **Prevention** | Rule: every new term must have a definition block before use |

### Type 3 — Broken Trace

| Attribute | Description |
|-----------|-------------|
| **Definition** | Claim cannot be traced to any SOT |
| **Symptom** | Trace score = 0 |
| **Example in {{PROJECT_NAME}}** | `{{BROKEN_TRACE_EXAMPLE}}` |
| **Signal match** | O2 (broken trace) |
| **Solution type** | ANCHOR (add SOT reference) or REMOVE (if cannot anchor) |
| **Prevention** | Every claim must carry SOT reference at creation time |

### Type 4 — Assumption Masquerading

| Attribute | Description |
|-----------|-------------|
| **Definition** | Claim presented as fact but actually an assumption |
| **Symptom** | No assumption flag, no trace, no "assumption" label |
| **Example in {{PROJECT_NAME}}** | `{{ASSUMPTION_MASQ_EXAMPLE}}` |
| **Signal match** | O3 (assumption not flagged) |
| **Solution type** | DOCUMENT — flag assumption clearly + add anchor |
| **Prevention** | Every new assumption → flag + trace + anchor strength |

### Type 5 — Structural Gap

| Attribute | Description |
|-----------|-------------|
| **Definition** | Framework lacks machinery to support the claim |
| **Symptom** | Claim requires theorem/mechanism not yet formalized |
| **Example in {{PROJECT_NAME}}** | `{{STRUCTURAL_GAP_EXAMPLE}}` |
| **Signal match** | O4 (weak anchor) |
| **Solution type** | DERIVE (build theorem) or DEFER (if research needed) |
| **Prevention** | Do not claim anything beyond the currently verified layer |

### Type 6 — Citation Hallucination

| Attribute | Description |
|-----------|-------------|
| **Definition** | Invented source, wrong author, wrong year, wrong content |
| **Symptom** | Cannot find source in primary literature |
| **Example in {{PROJECT_NAME}}** | `{{CITATION_HALLUCINATION_EXAMPLE}}` |
| **Signal match** | R2 (invented source) |
| **Solution type** | REMOVE (delete claim) or ANCHOR (find real source) |
| **Prevention** | Every citation must be verified before use |

---

## 3. FSR — Falsifier Strength Rubric (BDS v4.0) `[GENERIC]`

> Before accepting a counterargument as valid in the 5-Whys process, check its quality. A weak counterargument can invalidate a valid claim, or a fabricated counterargument can block a correct claim. FSR formalizes the quality threshold.

**When to apply FSR:** After W3-W5 answers that contain a counterargument, BEFORE accepting it as "root cause confirmed" or "claim invalid."

```
FSR — FALSIFIER Strength Rubric

Criterion 1: SPECIFICITY (1-3)
  3 = cites specific facts, dates, quantities, named entities, experimental results
  2 = references specific category/type without named instance
  1 = vague, general objection ("this seems wrong", "may not hold")

Criterion 2: SOURCE_QUALITY (1-3)
  3 = peer-reviewed literature, core axiom file (SOT-3), primary SOT, published experimental data
  2 = reputable secondary source, RCA report with 3-Round verification, internal derived theorem
  1 = AI-generated text (same session), unverified claim, circular reference, anonymous assertion

Criterion 3: DIRECTNESS (1-3)
  3 = directly contradicts the specific claim being evaluated
  2 = contradicts an assumption of the claim (indirect but relevant)
  1 = tangentially related, does not target the claim or its assumptions

Criterion 4: RECENCY (1-3)
  3 = within relevant TTL_CLASS window for this claim type (see integration_spec)
  2 = older but within accepted reference window for the claim type
  1 = outdated relative to claim's temporal context (Smṛti drift)
  N/A = Atemporal claim (frozen axioms) → score as 3 automatically

THRESHOLD: Total ≥ 9/12 to accept counterargument as valid

FSR_NULL: Total < 9 → [FSR_NULL | WEAK_COUNTERARGUMENT]
  → Treat as: NO_CONTRADICTION (claim not invalidated by this counterargument)
  → Do NOT accept as root cause confirmation
  → Continue 5-Whys to next Why level

FSR_PASS: Total ≥ 9 → Counterargument accepted as valid
  → Can be used to confirm root cause or flag claim
```

> **Note:** FSR evaluates the QUALITY of the counterargument's form, not its truth. An FSR_PASS counterargument can still be factually wrong — always verify content against SOT after FSR check.

---

## 4. Isolation Checklist `[GENERIC]`

Before concluding root cause, verify 7 questions:

- [ ] Can root cause be explained in 1 sentence?
- [ ] Where is the root cause: assumption, source gap, category error, or structural gap?
- [ ] Is the symptom merely the "visible surface" of a deeper issue?
- [ ] If this root cause is fixed, will the symptom disappear permanently?
- [ ] Is there any cascade effect from this root cause to other components?
- [ ] Is this root cause located in a SOT? (if yes, which SOT?)
- [ ] Can this root cause be verified independently (not just from symptom)?

---

## 5. Documentation Quality Audit `[GENERIC]`

After identifying root cause, audit component documentation quality:

| Criterion | Scale 1-5 | Check Question |
|-----------|-----------|---------------|
| **Assumption transparency** | ?/5 | Are all assumptions flagged + traced? |
| **Traceability** | ?/5 | Does every term have source traced (SOT, axiom, or external standard)? |
| **Self-awareness of limitation** | ?/5 | Does file self-identify as POSTULATE/THEOREM/MAPPING? Has boundary statement? |
| **Boundary honesty** | ?/5 | Are new terms flagged "NEW" — not disguised as established standard? |
| **System lineage documentation** | ?/5 | Does every system-specific concept have node/edge reference? |

**Audit score:** Total / 25. Threshold: ≥ 20/25 = PASS.

---

## 6. Verdict Template `[GENERIC]`

After completing RCA + audit, fill verdict template:

```markdown
### Verdict — [Component/Document Name]

**Date:** YYYY-MM-DD
**RCA Method:** 5-Whys × scoring threshold 4/5
**Root cause type:** [1-6]
**Root cause (1 sentence):** [...]

**Overall Assessment:**

| Metric | Value |
|--------|-------|
| Total components investigated | N |
| Pre-existing components | N (XX%) |
| New-in-scope components | N (XX%) |
| Flagged-assumption components | N (XX%) |
| DERIVED components | N (XX%) |
| ORPHANED components | N (XX%) |
| Average hallucination score | X.XX/10 |
| Hallucination components (7-10) | N |

**Conclusion:**

> [Component] [IS / IS NOT] hallucination. [...]
>
> [If not:] It is a [postulate / theorem / conceptual extension] systematically built from:
> - XX% components inherited from [...]
> - XX% components from [...]
> - XX% new components flagged as assumptions
>
> [If hallucination:] Weaknesses: [...]
> Strengths: [...]
```

---

## 7. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | 5-Whys template — matches governance Rule Zero? | ?/5 | `[CALIBRATE]` |
| R2 | Root cause taxonomy — are 6 types exhaustive? | ?/5 | `[CALIBRATE]` |
| R3 | Audit criteria — do 5 criteria match project standards? | ?/5 | `[CALIBRATE]` |
| **Aggregate** | | **?/5** `[PASS/FAIL]` (threshold ≥ 4/5) | |

---

*RCA Analysis Framework — 6 root cause types, 5-Whys template, 5 audit criteria + FSR (4 criteria, threshold ≥9/12). Exported from AHP v3.1 04_analysis.md. Calibrate examples and §1.1 for {{PROJECT_NAME}}.*

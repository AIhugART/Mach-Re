Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# 05 — Scoring: 10-Point Hallucination Scale
## {{PROJECT_NAME}}

**Role:** Heart of the system — defines the standardized 10-point scale, scoring rubric, and aggregate formula. Every component receives a single number: "how many hallucination points does this component have?"

**Input:** Component + trace score (from `03_sot_traceability.md`) + RCA result (from `04_analysis.md`).
**Output:** Hallucination score 0-10 + band classification + aggregate summary.
**Next:** `06_solution.md` — Prioritized Solution Framework (if score ≥ 5).

---

## 1. 10-Point Rubric — 5 Bands

### Band 1: GREEN — 0-2 points (Fully real, verifiable)

| Score | Label | Criteria | Example in {{PROJECT_NAME}} `[CALIBRATE]` |
|-------|-------|----------|------------------------------------------|
| **0** | Established textbook standard | In every standard reference for this domain, experimentally verified > 50 years | `{{GREEN_0_EXAMPLE}}` |
| **1** | Standard-derived necessity | Mathematical consequence of established standard (e.g., normalization) | `{{GREEN_1_EXAMPLE}}` |
| **2** | Pre-existing axiom — verified | Has formal definition in core axioms + system lineage + SOT trace ≥ 3 | `{{GREEN_2_EXAMPLE}}` |

**Rule:**
- Component found in standard textbooks → auto 0-1
- Component in core frozen axioms + SOT verified → auto 1-2
- No new assumptions added

### Band 2: BLUE — 3-4 points (Grounded, conceptual extension)

| Score | Label | Criteria | Example in {{PROJECT_NAME}} `[CALIBRATE]` |
|-------|-------|----------|------------------------------------------|
| **3** | System-grounded extension | Clear system lineage + framework anchor + no new assumption | `{{BLUE_3_EXAMPLE}}` |
| **4** | Framework extension — derived | SOT trace ≥ 3 + derived from pre-existing axioms + conceptual refinement | `{{BLUE_4_EXAMPLE}}` |

**Rule:**
- Component is a "conceptual extension" from pre-existing framework
- No new assumption created, but extends how existing concepts are used
- System lineage strongly documented

### Band 3: YELLOW — 5-6 points (Speculative but flagged)

| Score | Label | Criteria | Example in {{PROJECT_NAME}} `[CALIBRATE]` |
|-------|-------|----------|------------------------------------------|
| **5** | Speculative — well-anchored | New assumption + clearly flagged + anchor MODERATE+ + trace score ≥ 2 | `{{YELLOW_5_EXAMPLE}}` |
| **6** | Speculative — weakly-anchored | New assumption + flagged but anchor WEAK + trace score = 1 | `{{YELLOW_6_EXAMPLE}}` |

**Rule:**
- This is the "acceptable speculation" zone — assumption transparently declared
- Not hallucination, but needs tracking for future strengthening
- If stuck at 5-6 for > 2 weeks → escalate to `06_solution.md` priority MEDIUM

### Band 4: ORANGE — 7-8 points (Suspicious, weak basis)

| Score | Label | Criteria | Example in {{PROJECT_NAME}} `[CALIBRATE]` |
|-------|-------|----------|------------------------------------------|
| **7** | Weak foundation | Missing anchor (trace score ≤ 1) + assumption not fully flagged | `{{ORANGE_7_EXAMPLE}}` |
| **8** | Near-orphaned | Only 1 WEAK anchor + no formal definition + no system lineage | `{{ORANGE_8_EXAMPLE}}` |

**Rule:**
- This is the "warning" zone — component may be hallucination
- Full RCA analysis (`04_analysis.md`) required before concluding
- Priority HIGH in `06_solution.md`

### Band 5: RED — 9-10 points (Clear hallucination)

| Score | Label | Criteria | Example in {{PROJECT_NAME}} `[CALIBRATE]` |
|-------|-------|----------|------------------------------------------|
| **9** | Fabrication | Orphaned (trace score = 0) + no SOT anchor + no assumption flag | `{{RED_9_EXAMPLE}}` |
| **10** | Blatant hallucination | Orphaned + contradicts known fact + cannot trace to anything | `{{RED_10_EXAMPLE}}` |

**Rule:**
- This is BLOCKING — component must be REMOVED or ANCHORED immediately
- Cannot merge/release with Red components
- Priority P0 (BLOCKING) in `06_solution.md`

---

## 2. Scoring Protocol `[GENERIC]`

### 2.1 Who scores?

- **Primary scorer:** AI assistant — applies rubric
- **Reviewer:** Human researcher — verifies + calibrates
- **Independent review:** (optional) Different AI assistant or human reviewer

### 2.2 When to score?

| Trigger | Scope |
|---------|-------|
| New component/claim created | Score that component |
| Structural change in core axioms or system SOT | Re-score all affected components |
| Assumption DERIVED (assumption → theorem) | Re-score that component (typically -1 to -3 points) |
| Periodic (weekly) | Re-score all active components |

### 2.3 When to re-score?

| Change | Action |
|--------|--------|
| SOT changes (e.g., core axiom file update) | Re-score components anchored to that SOT |
| New anchor added | Re-score — typically reduces score |
| Assumption derived (assumption → theorem) | Re-score — reduce 1-3 points |
| Old anchor found to be wrong | Re-score — typically increases score |

### 2.4 Borderline Rule

When score falls between two bands (e.g., 4.5, 6.5):

| Situation | Rule |
|-----------|------|
| Score = X.5 + anchor STRONG | Round DOWN (e.g., 4.5 → 4) |
| Score = X.5 + anchor WEAK or no anchor | Round UP (e.g., 4.5 → 5) |
| Score = X.5 + currently being derived | Temporarily round UP, re-score after derivation |

---

## 3. Aggregate Scoring Formula `[GENERIC]`

### 3.1 Average Score

```
Avg = SUM(score_i) / N_components

Where:
  score_i = hallucination score of component i (0-10)
  N_components = total components scored
```

### 3.2 Score Distribution

```
% Green Band (0-2) = N_green / N_components × 100%
% Blue Band (3-4)  = N_blue / N_components × 100%
% Yellow Band (5-6) = N_yellow / N_components × 100%
% Orange Band (7-8) = N_orange / N_components × 100%
% Red Band (9-10)   = N_red / N_components × 100%
```

### 3.3 Analysis by Origin

| Origin | Component Count | Avg Score |
|--------|----------------|-----------|
| From established standard | N_A | TB_A |
| From {{PROJECT_NAME}} pre-existing | N_B | TB_B |
| From current scope — flagged assumption | N_C | TB_C |
| From current scope — DERIVED | N_C' | TB_C' |
| From current scope — ORPHANED | N_D | TB_D |

---

## 4. Score Evolution Tracking `[GENERIC]`

| Stage | Component 1 | Component 2 | ... | System Avg | Assumption Count | Notes |
|-------|-------------|-------------|-----|-----------|------------------|-------|
| Baseline | X/10 | Y/10 | ... | Z.ZZ/10 | N | Initial scoring |
| After fix A | X'/10 | Y'/10 | ... | Z'.ZZ/10 | N' | Fix description |
| After fix B | ... | ... | ... | ... | ... | ... |

---

## 5. Scoring Quick Reference `[GENERIC]`

| Question | Answer |
|----------|--------|
| Is this component in the established standard? | YES → 0-2 (Green) |
| Is this component in pre-existing core axioms? | YES → 1-4 (Green/Blue) |
| Does this component have a new assumption? | YES + flagged → 5-6 (Yellow) |
| Does this component have an assumption but NOT flagged? | YES → 7-8 (Orange) + escalate |
| Can this component NOT be traced to any SOT? | YES → 9-10 (Red) + BLOCKING |
| Was this component JUST derived from an assumption? | YES → reduce 1-3 points from previous |

---

## 6. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Rubric calibration — do 5 bands match known component scores? | ?/5 | `[CALIBRATE]` |
| R2 | Borderline rule — is the round-up/down rule consistent? | ?/5 | `[CALIBRATE]` |
| R3 | Aggregate formula — does it match component distribution? | ?/5 | `[CALIBRATE]` |
| **Aggregate** | | **?/5** `[PASS/FAIL]` (threshold ≥ 4/5) | |

---

*Hallucination Scale — 10-point rubric, 5 bands, 3-tier aggregate. Exported from AHP v3.1 05_scoring.md. Calibrate example columns for {{PROJECT_NAME}}.*

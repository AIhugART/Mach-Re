Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# 06 — Solution: Prioritized Solution Framework
## {{PROJECT_NAME}}

**Role:** Final layer of pipeline — from scoring + RCA results, propose solutions classified by priority and tracked to RESOLVED.

**Input:** Hallucination score (from `05_scoring.md`) + root cause (from `04_analysis.md`).
**Output:** Solution type + priority level + action plan + resolution tracking entry.
**Next:** Return to `01_early_warning.md` to re-scan after fix.

---

## 1. Priority Matrix `[GENERIC]`

| Priority | Score Range | Label | Action | Deadline | SLA |
|----------|-------------|-------|--------|----------|-----|
| **P0** | 9-10 (Red) | BLOCKING | Fix immediately — block merge/release | Before next commit | 1 session |
| **P1** | 7-8 (Orange) | HIGH | Fix in current working session | Within the day | 1-2 sessions |
| **P2** | 5-6 (Yellow) | MEDIUM | Strengthen anchor / add documentation | Within the week | 1 week |
| **P3** | 3-4 (Blue) | LOW | Additional documentation, lineage elaboration | When time permits | 1 month |
| **P4** | 0-2 (Green) | ONGOING | Maintain practices: flag assumptions, trace terms | Continuously | No limit |

---

## 2. Solution Categories (5 Types) `[GENERIC — calibrate examples for {{PROJECT_NAME}}]`

### Type 1 — DERIVE

| Attribute | Description |
|-----------|-------------|
| **Purpose** | Convert assumption → theorem. Build structural proof to eliminate assumption. |
| **When to apply** | Assumption can be proved from core axioms + system SOT (no new postulate needed) |
| **Example in {{PROJECT_NAME}}** | `{{DERIVE_EXAMPLE}}` |
| **Effort** | HIGH (1-3 sessions + 3-round RCA verification) |
| **Impact** | Reduces hallucination score 1-3 points + assumption count -1 |
| **RCA Round** | Round 1: correctness, Round 2: consistency, Round 3: impact |

### Type 2 — ANCHOR

| Attribute | Description |
|-----------|-------------|
| **Purpose** | Add SOT reference, external anchor, or system lineage to increase trace score |
| **When to apply** | Component has low trace score (0-2) but anchor can be found |
| **Example in {{PROJECT_NAME}}** | `{{ANCHOR_EXAMPLE}}` |
| **Effort** | MEDIUM (1 session research + documentation) |
| **Impact** | Increases trace score +1-3, may reduce hallucination score 1-2 points |
| **RCA Round** | 1-2 rounds (verify anchor validity) |

### Type 3 — DOCUMENT

| Attribute | Description |
|-----------|-------------|
| **Purpose** | Flag assumptions more clearly, add trace, add boundary statement |
| **When to apply** | Component already has anchor but documentation is incomplete |
| **Example in {{PROJECT_NAME}}** | `{{DOCUMENT_EXAMPLE}}` |
| **Effort** | LOW (usually < 1 session) |
| **Impact** | Increases documentation quality score, no effect on hallucination score |
| **RCA Round** | Not needed — pure documentation fix |

### Type 4 — REMOVE

| Attribute | Description |
|-----------|-------------|
| **Purpose** | Delete unsalvageable component (orphaned, fabricated, contradicted) |
| **When to apply** | Component trace score = 0 + cannot anchor + contradicts known fact |
| **Example in {{PROJECT_NAME}}** | `{{REMOVE_EXAMPLE}}` |
| **Effort** | LOW (delete + document reason) |
| **Impact** | Component count -1, may require re-design of dependent components |
| **RCA Round** | Round 1: confirm orphaned status, Round 2: assess cascade impact |

### Type 5 — DEFER

| Attribute | Description |
|-----------|-------------|
| **Purpose** | Record that assumption is necessary but not yet resolvable |
| **When to apply** | Component needs further research, experimental data, or theorem not yet built |
| **Example in {{PROJECT_NAME}}** | `{{DEFER_EXAMPLE}}` |
| **Effort** | LOW (document DEFERRED status + unlock condition) |
| **Impact** | No effect on score, but must track to avoid forgetting |
| **RCA Round** | Round 1: confirm deferral warranted, Round 2: set unlock condition |

---

## 3. Resolution Tracking Table `[CALIBRATE]`

| # | Issue | Component | Score | Priority | Root Cause Type | Solution Type | Status | Assignee | Open Date | Resolve Date | Commit |
|---|-------|-----------|-------|----------|-----------------|---------------|--------|----------|-----------|-------------|--------|
| 1 | `{{ISSUE_1}}` | `{{COMP_1}}` | ?/10 | P? | 1-6 | 1-5 | OPEN | `{{ASSIGNEE}}` | YYYY-MM-DD | — | — |

### 3.1 Status Options

| Status | Meaning |
|--------|---------|
| **OPEN** | Identified, not started |
| **IN PROGRESS** | Currently working |
| **RESOLVED** | Fixed + verified |
| **DEFERRED** | Postponed — has unlock condition |
| **WONT_FIX** | Accepted risk — has reason |

---

## 4. Implementation Record Template `[GENERIC]`

When a solution is implemented, record using this template:

```markdown
### [Solution Name] — Implementation Record

**Date:** YYYY-MM-DD
**Target:** [Component / Issue #]
**Solution type:** [1-5]
**RCA score before:** X.X/10
**RCA score after:** Y.Y/10

#### What was built

[Brief description of what was done]

#### RCA Verification

| Round | Focus | Score |
|-------|-------|-------|
| Round 1 | [Focus] | X.X/5 |
| Round 2 | [Focus] | X.X/5 |
| Round 3 | [Focus] | X.X/5 |
| **Aggregate** | | **X.XX/5** [PASS/FAIL] |

#### Files modified

| File | Change |
|------|--------|
| `path/to/file` | [Description] |

#### Net impact

| Metric | Before | After |
|--------|--------|-------|
| [Metric 1] | X | Y |
| [Metric 2] | X | Y |
```

---

## 5. Decision Matrix — Which Solution Type? `[GENERIC]`

| Situation | Solution Type | Example |
|-----------|---------------|---------|
| Assumption can be proved from core axioms | **DERIVE** | `[CALIBRATE]` |
| Assumption needs further research (experiment, theorem) | **DEFER** | `[CALIBRATE]` |
| Component trace score = 0, unsalvageable | **REMOVE** | Orphaned component |
| Component trace score low but anchor found | **ANCHOR** | `[CALIBRATE]` |
| Component has anchor but documentation missing | **DOCUMENT** | Add system lineage |
| Component < 5 points + stable | **ONGOING** | Core axioms |

---

## 6. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Solution type coverage — do 5 types cover all fix patterns? | ?/5 | `[CALIBRATE]` |
| R2 | Priority matrix calibration — do P0-P4 thresholds match scoring bands? | ?/5 | `[CALIBRATE]` |
| R3 | Tracking usability — can resolution tracking catch stale issues? | ?/5 | `[CALIBRATE]` |
| **Aggregate** | | **?/5** `[PASS/FAIL]` (threshold ≥ 4/5) | |

---

*Solution Framework — 5 priority levels, 5 solution types, full tracking. Exported from AHP v3.1 06_solution.md. Calibrate examples and resolution tracking for {{PROJECT_NAME}}.*

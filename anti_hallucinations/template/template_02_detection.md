Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# 02 — Detection: Component Inventory & Tracing Protocol
## {{PROJECT_NAME}}

**Role:** Layer 2 of pipeline — when triggered by `01_early_warning.md`, provides protocol to inventory and trace each component of a claim or document.
**Input:** Trigger signal(s) + claim/document to investigate.
**Output:** Component Inventory Table + 4-group origin classification + preliminary hallucination score.
**Next:** `03_sot_traceability.md`

---

## 1. Component Inventory Template `[GENERIC schema — CALIBRATE Group B/C/D labels]`

| # | ID | Name & Meaning | Origin | Pre-existing? | SOT link | Reference standard | Location in standard | H score |
|---|-----|---------------|--------|--------------|----------|--------------------|----------------------|---------|
| 1 | `{{COMP_001}}` | `{{NAME}} — {{1-sentence function}}` | `{{SYS_A / SYS_B / Mapping / New}}` | Y/N | `{{SOT file or external ref}}` | `{{equivalent concept}}` | `{{location}}` | ?/10 |

### 1.1 Column Definitions `[GENERIC]`

| Column | How to fill |
|--------|-------------|
| **#** | Sequential number |
| **ID** | Component code: `N_{{SYS}}_00001`, `MAP_001`, etc. |
| **Name & Meaning** | Name + 1-sentence function |
| **Origin** | `{{SYS_A}}`, `{{SYS_B}}`, `Mapping`, `New` |
| **Pre-existing?** | Y = existed before current scope; N = new |
| **SOT link** | File path + line number or external reference |
| **Reference standard** | Equivalent in reference standard, or "No equivalent in {{SYS_B}}" |
| **Location in standard** | Exact location (§, page, line) |
| **H score** | Preliminary, to be verified in `05_scoring.md` |

---

## 2. Four-Group Origin Classification `[GENERIC — calibrate B/C group examples for {{PROJECT_NAME}}]`

### Group A — From Established Standard (verified)

| Criterion | Notes |
|-----------|-------|
| In every standard definition of `{{SYS_A}}` or `{{SYS_B}}` | `{{EXAMPLE_GROUP_A}}` |
| Verified in primary literature / reference | — |
| **Trace score:** 1 SOT sufficient | **Band: 0-2 (Green)** |

### Group B — From {{PROJECT_NAME}} Pre-Existing Definitions

| Criterion | Notes |
|-----------|-------|
| Existed before current analysis scope | `{{EXAMPLE_GROUP_B}}` |
| Has formal definition in `system_registry.md` | — |
| Has documented system lineage (`N_{{SYS}}_XXXXX`) | — |
| **Trace score:** ≥ 2/N | **Band: 0-4 (Green/Blue)** |

### Group C — New — Flagged Assumption + Has Anchor

| Criterion | Notes |
|-----------|-------|
| Created within current scope | `{{EXAMPLE_GROUP_C}}` |
| Explicitly flagged as assumption or working definition | — |
| Has ≥ 1 anchor (system SOT or external reference) | — |
| **Trace score:** ≥ 1/N | **Band: 5-6 (Yellow)** |

### Group D — New — ORPHANED ← RED FLAG

| Criterion | Notes |
|-----------|-------|
| Created in current scope | — |
| NOT flagged as assumption | — |
| CANNOT trace to any SOT | — |
| **Trace score:** 0/N | **Band: 7-10 (Orange/Red) → BLOCKING** |

---

## 3. Detection Workflow `[GENERIC]`

```
Trigger from 01_early_warning.md
  → Step 1: DECOMPOSE — break claim into components; fill Inventory Table
  → Step 2: TRACE — trace origin of each component via SOTs and system_registry.md
  → Step 3: CLASSIFY — assign to Group A/B/C/D
      Group D → RED FLAG → escalate immediately
  → Step 4: PRE-SCORE — preliminary score (Group D → auto ≥ 7/10)
  → Step 5: ESCALATE — Group D present? → RED; Group C score ≥ 6? → prioritize
```

---

## 4. ES Tag Assignment (BDS v4.0) `[GENERIC]`

| Group | Default ES tag |
|-------|---------------|
| A | `[ES-PRATY]` |
| B (formal derivation) | `[ES-ANUMA]` |
| B (literature) | `[ES-SMRTI]` |
| C (derivation chain) | `[ES-ANUMA]` |
| C (literature anchor only) | `[ES-SMRTI]` |
| D | `[ES-VIKALP]` — BLOCKING |

---

## 5. Orphaned Component Report Template `[GENERIC]`

```markdown
### Orphaned Component Report — [Component Name]

Date: YYYY-MM-DD
File: [path]
Description: [1 sentence]

Trace attempts:
- SOT for {{SYS_A}}: [not found / found at ...]
- SOT for {{SYS_B}}: [not found / found at ...]
- External reference: [not found / found at ...]

Trace score: 0/N
Preliminary H: [7-10]
Urgency: RED — BLOCKING
Action: 06_solution.md — Remove or Anchor
```

---

## 6. Quick Checklist `[GENERIC]`

- [ ] Every term defined? (O1)
- [ ] Every claim traces to SOT? (O2)
- [ ] Every assumption flagged? (O3)
- [ ] No stale/invalidated references? (O5)
- [ ] No cross-system equivalence without justification? (R4)
- [ ] No contradiction with core axioms? (R5)
- [ ] Consistent terminology? (Y3)
- [ ] File has version/date metadata? (Y4)
- [ ] All cross-system links in Mapping Registry? (Y5)

---

*Detection — Component Inventory, 4-group classification, 5-step workflow. Exported from AHP v3.1 02_detection.md. Calibrate Group B/C examples for {{PROJECT_NAME}}.*

Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# 03 — SOT Traceability: Cross-Reference Matrix
## {{PROJECT_NAME}}

**Role:** Backbone of verification. Defines all SOTs (Sources of Truth) and provides cross-reference matrix: every component → which SOT anchors it → verification status.

**Input:** Component ID (from `02_detection.md` inventory).
**Output:** Trace score (anchored SOT count / total relevant SOTs) + SOT links + anchor strength.
**Next:** `04_analysis.md` — RCA Analysis Framework.

---

## Part A: SOT Registry

### A.1 Internal SOTs (within {{PROJECT_NAME}} repository) `[CALIBRATE — replace placeholder rows]`

| SOT ID | SOT Name | File Path | Role | Last Verified | Version |
|--------|----------|-----------|------|---------------|---------|
| **SOT-1** | `{{SYS_A}}` Full System | `{{PATH_TO_SYS_A_SOT}}` | Single source of truth for {{SYS_A}} node/edge definitions | YYYY-MM-DD | v1.0 |
| **SOT-2** | `{{SYS_B}}` Full System | `{{PATH_TO_SYS_B_SOT}}` | Single source of truth for {{SYS_B}} node/edge definitions | YYYY-MM-DD | v1.0 |
| **SOT-3** | {{PROJECT_NAME}} Core Axioms | `{{PATH_TO_CORE_AXIOM_FILE}}` | Structural axioms / frozen definitions | YYYY-MM-DD | v1.0 |
| **SOT-4** | {{PROJECT_NAME}} Governance | `{{PATH_TO_GOVERNANCE_FILE}}` | Project rules, terminology, CLAUDE.md or equivalent | YYYY-MM-DD | — |

> **Note:** Add more SOT rows as needed for systems beyond 2. Each additional system (`{{SYS_C}}`, `{{SYS_D}}`, ...) should have its own SOT row if it has a node/edge definition file.

### A.2 External SOTs (outside repository) `[CALIBRATE]`

| SOT ID | SOT Name | Reference | Role | Verification method |
|--------|----------|-----------|------|---------------------|
| **SOT-5** | `{{EXTERNAL_STANDARD_1}}` | `{{TEXTBOOK_OR_PRIMARY_REFERENCE}}` | `{{DESCRIPTION}}` | Cross-check with primary source |
| **SOT-6** | `{{EXTERNAL_DATA_SOURCE}}` | `{{PUBLICATION_OR_DATASET}}` | `{{DESCRIPTION}}` | Cross-check with published data |

### A.3 Compass (intelligence only — no structure import) `[CALIBRATE if applicable]`

| ID | Name | File Path | Role |
|----|------|-----------|------|
| **COMPASS-1** | `{{COMPASS_NAME}}` | `{{COMPASS_PATH}}` | External intelligence about nodes, gaps, stress points. **Compass only — do not import structure into core.** |

---

## Part B: Cross-Reference Matrix `[CALIBRATE — replace all placeholder rows]`

Each row = 1 component. Each column = 1 SOT. `+` = anchor verified. `−` = no anchor. `?` = unverified.

### B.1 System {{SYS_A}} Core Nodes `[CALIBRATE example]`

| Component | SOT-1 ({{SYS_A}}) | SOT-2 ({{SYS_B}}) | SOT-3 (Core) | SOT-4 (Gov) | SOT-5 (Ext) | SOT-6 (Data) | Trace Score | Anchor Strength |
|-----------|-------------------|-------------------|-------------|------------|------------|-------------|-------------|-----------------|
| `N_{{SYS_A}}_00001` — `{{NAME}}` | + | - | + | + | + | - | 4/6 | STRONG |
| `N_{{SYS_A}}_00002` — `{{NAME}}` | + | - | + | + | - | - | 3/6 | STRONG |

### B.2 System {{SYS_B}} Core Nodes `[CALIBRATE example]`

| Component | SOT-1 ({{SYS_A}}) | SOT-2 ({{SYS_B}}) | SOT-3 (Core) | SOT-4 (Gov) | SOT-5 (Ext) | SOT-6 (Data) | Trace Score | Anchor Strength |
|-----------|-------------------|-------------------|-------------|------------|------------|-------------|-------------|-----------------|
| `N_{{SYS_B}}_00001` — `{{NAME}}` | - | + | + | + | + | - | 4/6 | STRONG |

### B.3 Cross-System Mapping Links `[CALIBRATE example]`

| Component | SOT-1 ({{SYS_A}}) | SOT-2 ({{SYS_B}}) | SOT-3 (Core) | SOT-4 (Gov) | SOT-5 (Ext) | SOT-6 (Data) | Trace Score | Anchor Strength |
|-----------|-------------------|-------------------|-------------|------------|------------|-------------|-------------|-----------------|
| `{{MAP_001}}` — `N_{{SYS_A}}_XXXXX` ↔ `N_{{SYS_B}}_XXXXX` | + | + | + | + | - | - | 4/6 | STRONG |
| `{{MAP_002}}` — `N_{{SYS_A}}_XXXXX` ↔ `N_{{SYS_B}}_YYYYY` | + | + | - | + | - | - | 3/6 | MODERATE |

### B.4 Assumptions (flagged) `[CALIBRATE example]`

| Component | SOT-1 ({{SYS_A}}) | SOT-2 ({{SYS_B}}) | SOT-3 (Core) | SOT-4 (Gov) | SOT-5 (Ext) | SOT-6 (Data) | Trace Score | Anchor Strength |
|-----------|-------------------|-------------------|-------------|------------|------------|-------------|-------------|-----------------|
| `{{A-01}}` — `{{ASSUMPTION_NAME}}` | - | + | + | + | - | - | 3/6 | MODERATE |

> **Note on denominator:** The denominator (total SOTs) should be adjusted per component — SOT-5 only counts if the component claims external-standard relevance; SOT-6 only counts if the component claims experimental/data relevance. For {{SYS_A}}-only components, denominator may be 4 (internal SOTs).
>
> **Minimum denominator rule:** If N systems are registered, every component must be traceable to at least its home system SOT (trace score ≥ 1/N_systems_internal).

---

## Part C: Verification Protocol `[GENERIC]`

### C.1 How to verify a trace link

```
1. Read SOT file at claimed line/location
2. Confirm: does SOT actually define/support this claim?
3. YES → mark "+" + note verification date
4. PARTIAL → mark "~" + note what's missing
5. NO → mark "−" → this is a GAP to fill
```

### C.2 Trace Score Calculation

```
Trace Score = number of SOTs with anchor (+) / total relevant SOTs

Where:
  Numerator = count of SOTs with verified anchor ("+")
  Denominator = total SOTs relevant to this component
  
  SOT-5 (External Standard) only counts if component makes a claim about that standard
  SOT-6 (Data Source) only counts if component claims experimental/data fit
  → For system-internal-only components: denominator = count of internal SOTs
```

### C.3 Anchor Strength Calibration

| Strength | Criteria | Trace Score Range |
|----------|----------|-------------------|
| **STRONG** | ≥ 3 SOT anchors, verified within 1 week | ≥ 3/6 |
| **MODERATE** | 1-2 SOT anchors, or not re-verified > 1 week | 1-2/6 |
| **WEAK** | 1 SOT anchor, conceptual link only (no line reference) | 1/6 |
| **ORPHANED** | 0 SOT anchors — CANNOT TRACE | 0/6 → RED FLAG |

### C.4 Periodic Re-verification `[CALIBRATE triggers for {{PROJECT_NAME}}]`

| Trigger | Action |
|---------|--------|
| Structural change in {{SYS_A}} or {{SYS_B}} SOT | Re-verify all SOT links for that system |
| Core axiom update | Re-verify SOT-3 links |
| Governance file update | Re-verify SOT-4 links |
| New component added | Add row to matrix + verify all relevant SOTs |
| New system registered | Add new SOT row(s) + re-denominate existing trace scores |

---

## Part D: Trace Score Summary `[CALIBRATE]`

| Group | Component Count | Avg Trace Score | Avg Anchor Strength |
|-------|----------------|-----------------|---------------------|
| Group A (from established standards) | ? | ?/N | ? |
| Group B (pre-existing in {{PROJECT_NAME}}) | ? | ?/N | ? |
| Group C (new — flagged assumption) | ? | ?/N | ? |
| Group C' (new — derived) | ? | ?/N | ? |
| Group D (orphaned) | 0 | — | — |
| **TOTAL** | **?** | **?/N** | **?** |

> **Conclusion:** `[CALIBRATE: summarize trace health. Flag weakest components.]`

---

## 5. Multi-System Denominator Rule `[GENERIC — applies to N-system projects]`

For a project with N registered systems (`{{SYS_A}}`, `{{SYS_B}}`, ... `{{SYS_N}}`):

```
Internal SOT count = 1 per system + 1 core + 1 governance = N + 2 minimum
External SOT count = as many as relevant (textbooks, data sources, compasses)

Base denominator per component:
  = N_systems_home (always ≥ 1, the component's origin system)
  + N_core (if claim touches core framework)
  + N_governance (always 1, terminology/governance)
  + N_external (if claim touches external standard)
  + N_data (if claim touches experimental data)
```

---

## 6. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | SOT selection — are all SOTs necessary and sufficient? | ?/5 | `[CALIBRATE]` |
| R2 | Matrix accuracy — do trace links match detection results? | ?/5 | `[CALIBRATE]` |
| R3 | Protocol usability — can a new reviewer verify a trace link? | ?/5 | `[CALIBRATE]` |
| **Aggregate** | | **?/5** `[PASS/FAIL]` (threshold ≥ 4/5) | |

---

*SOT Traceability Matrix — N-system SOT Registry, Cross-Reference Matrix, Trace Score formula, Anchor Strength calibration. Exported from AHP v3.1 03_sot_traceability.md. Calibrate all SOT entries, matrix rows, and summary for {{PROJECT_NAME}}.*

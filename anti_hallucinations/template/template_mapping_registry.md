Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# Mapping Registry — {{PROJECT_NAME}} Cross-System Links
## {{PROJECT_NAME}}

**Role:** Central registry of all cross-system mapping links in {{PROJECT_NAME}}. Every mapping link is an **auditable claim** — it must carry justification, type, ground system, and AHP label.

**Key principle:** Mapping is NOT equivalence. A cross-system link is an interpretive claim that requires the same rigor as any other claim in the pipeline.

**Input:** Proposed cross-system mapping link.
**Output:** Registered mapping entry with 4-column mandatory schema + AHP label + verification status.
**Cross-reference:** `system_registry.md` for node codes; `03_sot_traceability.md` for SOT anchors.

---

## 1. Mapping Link Schema — 4 Mandatory Columns `[GENERIC]`

Every cross-system mapping link MUST carry these 4 columns. A link missing any column is a **Signal R4** (equivalence without justification) and is BLOCKING:

| Column | Type | Meaning | Example |
|--------|------|---------|---------|
| **mapping_type** | ENUM | ANALOGY / STRUCTURAL / EQUIVALENCE-JUSTIFIED | ANALOGY |
| **justification** | TEXT | 1-3 sentences explaining WHY this link exists | "Both concepts share the structural property of..." |
| **ground_system** | SYS-ID | Which system serves as the primary reference frame for this link | `{{SYS_A}}` |
| **AHP label** | LABEL | Pipeline label from `label_system.md` | `[AH-LOW][ES-ANUMA]` |

### 1.1 Mapping Type Definitions

| mapping_type | Meaning | When to use | Confidence level |
|-------------|---------|-------------|-----------------|
| **ANALOGY** | Concepts share a structural pattern, but no claim of equivalence | Default for most cross-system links | LOW — interpretive |
| **STRUCTURAL** | Formal structural correspondence demonstrated (preserves relations) | When formal mapping conditions are proven | MEDIUM — formal but domain-bounded |
| **EQUIVALENCE-JUSTIFIED** | Concepts are formally equivalent under explicit conditions | ONLY when formal proof + peer review + experimental test supplied | HIGH — rarely justified |

> **Critical rule:** ANALOGY is the DEFAULT mapping type for any new cross-system link. Upgrading to STRUCTURAL requires formal proof. Upgrading to EQUIVALENCE-JUSTIFIED requires formal proof + peer review + experimental test. Signal R4 fires when ANALOGY is promoted without new justification.

---

## 2. Mapping Registry Table `[CALIBRATE]`

| Map ID | Source Node | Target Node | mapping_type | justification | ground_system | AHP label | Status | Last Verified |
|--------|------------|-------------|-------------|---------------|---------------|-----------|--------|---------------|
| `{{MAP_001}}` | `N_{{SYS_A}}_00001` | `N_{{SYS_B}}_00005` | ANALOGY | `{{JUSTIFICATION_TEXT}}` | `{{SYS_A}}` | `[AH-LOW][ES-ANUMA]` | OPEN | YYYY-MM-DD |
| `{{MAP_002}}` | `N_{{SYS_A}}_00003` | `N_{{SYS_B}}_00007` | STRUCTURAL | `{{JUSTIFICATION_TEXT}}` | `{{SYS_A}}` | `[AH-LOW][ES-ANUMA]` | VERIFIED | YYYY-MM-DD |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

### 2.1 Column Definitions

| Column | How to fill |
|--------|-------------|
| **Map ID** | `MAP_001` through `MAP_NNN` — sequential, project-wide unique |
| **Source Node** | Full node code with system prefix from `system_registry.md` |
| **Target Node** | Full node code with system prefix from `system_registry.md` |
| **mapping_type** | ANALOGY (default) / STRUCTURAL / EQUIVALENCE-JUSTIFIED |
| **justification** | 1-3 sentences: what structural property is shared? What is the evidence? |
| **ground_system** | The system that serves as the primary reference frame |
| **AHP label** | From `label_system.md` — at minimum `[ES-ANUMA]` (mapping is inferential) |
| **Status** | OPEN / VERIFIED / DISPUTED / RETIRED |
| **Last Verified** | Date of last SOT cross-check |

---

## 3. NAC — No-Analogue Concept Table `[CALIBRATE]`

A NAC is a node in one system that has **no structural equivalent** in another system. This is a **valid result** — not a gap to be filled. Forcing a NAC into a mapping is a Vikalpa error (Signal R4).

| NAC ID | Node | Home System | Why no analogue in `{{OTHER_SYS}}` | Status |
|--------|------|-------------|-------------------------------------|--------|
| `{{NAC_001}}` | `N_{{SYS_A}}_00007` | `{{SYS_A}}` | `{{NAC_RATIONALE}}` | DOCUMENTED |
| `{{NAC_002}}` | `N_{{SYS_B}}_00012` | `{{SYS_B}}` | `{{NAC_RATIONALE}}` | DOCUMENTED |
| ... | ... | ... | ... | ... |

### 3.1 NAC Rules `[GENERIC]`

1. **NAC is a valid result** — not every concept has an analogue in every other system.
2. **Do NOT force-map NACs** — creating a mapping for a NAC is Vikalpa (pattern-construction without anchor).
3. **NAC must be documented** — silence about a NAC reads as "this concept maps to nothing" which is ambiguous. Explicitly state: "X has no analogue in Y because [reason]."
4. **NAC can become a mapping later** — if new scholarship reveals a structural correspondence, a NAC can be converted to a mapping entry (with full justification).

---

## 4. Lookup Command Patterns `[GENERIC]`

Cross-system queries use these patterns (adapt to {{PROJECT_NAME}} terminology):

```
# Find all mappings where {{SYS_A}} is the ground system
grep "N_{{SYS_A}}_" mapping_registry.md

# Find all nodes in {{SYS_A}} that map to {{SYS_B}}
grep "N_{{SYS_B}}_" mapping_registry.md | grep "N_{{SYS_A}}_"

# Find all NACs for {{SYS_A}}
grep "{{SYS_A}}" mapping_registry.md | grep "NAC"

# Find all STRUCTURAL (non-ANALOGY) mappings
grep "STRUCTURAL" mapping_registry.md

# Check if a specific node has an existing mapping
grep "N_{{SYS_A}}_00007" mapping_registry.md
```

---

## 5. Mapping Verification Protocol `[GENERIC]`

```
1. Source node: verified in system_registry.md? → YES
2. Target node: verified in system_registry.md? → YES
3. mapping_type: ANALOGY (default) / STRUCTURAL / EQUIVALENCE-JUSTIFIED? → CHECK justification matches type
4. justification: ≥ 1 sentence with structural reasoning? → YES
5. ground_system: explicitly stated? → YES
6. AHP label: assigned via label_system.md? → minimum [ES-ANUMA]
7. SOT cross-check: both nodes traceable to their home SOTs? → YES
8. No circular dependency? Source ≠ Target? → YES
9. NAC check: is either node a NAC in the other system? → If YES, flag as potential Vikalpa error
```

---

## 6. Quick Checklist `[GENERIC]`

- [ ] Every mapping link has all 4 mandatory columns?
- [ ] mapping_type = ANALOGY is the default for new links?
- [ ] No ANALOGY promoted to STRUCTURAL without new formal proof?
- [ ] No ANALOGY promoted to EQUIVALENCE-JUSTIFIED without peer review + experiment?
- [ ] Every NAC is explicitly documented (not silent)?
- [ ] No NAC has been force-mapped?
- [ ] All node codes match `system_registry.md`?
- [ ] No duplicate mapping (same source + same target)?
- [ ] ground_system is consistent across related mappings?

---

## 7. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Schema completeness — do 4 columns capture all mapping audit needs? | ?/5 | `[CALIBRATE]` |
| R2 | NAC guard — does NAC table prevent Vikalpa force-mapping? | ?/5 | `[CALIBRATE]` |
| R3 | Traceability — can every mapping be traced to both system SOTs? | ?/5 | `[CALIBRATE]` |
| **Aggregate** | | **?/5** `[PASS/FAIL]` (threshold ≥ 4/5) | |

---

*Mapping Registry — 4-column mandatory schema, NAC table, lookup patterns, verification protocol. Exported from AHP Template v1.0 (no direct AHP v3.1 source — new file for multi-system support). Calibrate all entries for {{PROJECT_NAME}}.*

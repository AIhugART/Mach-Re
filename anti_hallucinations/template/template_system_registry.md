Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# System Registry — {{PROJECT_NAME}} Multi-System Namespace
## {{PROJECT_NAME}}

**Role:** Central registry of all knowledge systems in {{PROJECT_NAME}}. Defines namespace rules, node/edge code formats, and the single source of truth for each system's definitions.

**Key principle:** N systems is **data**, not structure. The registry pattern supports 2 systems, 3 systems, or N systems without structural change — only the number of rows changes.

**Input:** System registration request.
**Output:** Registered system entry + namespace allocation + node/edge code schema.
**Cross-reference:** `mapping_registry.md` for cross-system links; `03_sot_traceability.md` for SOT anchoring.

---

## 1. System Registration Table `[CALIBRATE — replace placeholders]`

| System ID | System Name | Short Name | SOT File Path | Namespace Prefix | Node Code Format | Edge Code Format | Status |
|-----------|------------|------------|---------------|------------------|-----------------|-----------------|--------|
| SYS-1 | `{{SYS_A_FULL_NAME}}` | `{{SYS_A}}` | `{{PATH_TO_SYS_A_SOT}}` | `N_{{SYS_A}}_` | `N_{{SYS_A}}_00001` | `ED_{{SYS_A}}_00001` | ACTIVE |
| SYS-2 | `{{SYS_B_FULL_NAME}}` | `{{SYS_B}}` | `{{PATH_TO_SYS_B_SOT}}` | `N_{{SYS_B}}_` | `N_{{SYS_B}}_00001` | `ED_{{SYS_B}}_00001` | ACTIVE |
| ... | ... | ... | ... | ... | ... | ... | ... |

> **Add rows for SYS-3, SYS-4, ... SYS-N as needed.** The registry is N-row, not 2-row. N is data.

### 1.1 Column Definitions `[GENERIC]`

| Column | Meaning |
|--------|---------|
| **System ID** | Short internal reference: SYS-1, SYS-2, ... |
| **System Name** | Full name of the knowledge system |
| **Short Name** | Abbreviation for use in code format and namespace (e.g., "BE") |
| **SOT File Path** | Path to the single source of truth for this system's node/edge definitions |
| **Namespace Prefix** | Prefix that all nodes from this system share — ensures unique ID across systems |
| **Node Code Format** | Template for node codes: `N_{{SYS}}_XXXXX` (5-digit zero-padded) |
| **Edge Code Format** | Template for edge codes: `ED_{{SYS}}_XXXXX` (5-digit zero-padded) |
| **Status** | ACTIVE / FROZEN / DEPRECATED |

---

## 2. Namespace Rule `[GENERIC]`

### 2.1 Prefix-Unique Constraint

```
Every node/edge code across ALL systems MUST have a globally unique prefix.

Rule: N_{{SYS_A}}_XXXXX ≠ N_{{SYS_B}}_XXXXX
       ED_{{SYS_A}}_XXXXX ≠ ED_{{SYS_B}}_XXXXX

Example: N_BE_00001 and N_QM_00001 are different nodes in different systems.
         No ambiguity — the prefix encodes the home system.
```

### 2.2 Cross-System Code Reference

When a node from `{{SYS_A}}` is referenced in a mapping context:
```
N_{{SYS_A}}_00001 (Pramāṇa) ↔ N_{{SYS_B}}_00005 (Measurement)
```

The prefix `N_{{SYS_A}}_` always identifies the home system. No global renumbering is needed when a new system is added.

---

## 3. Node Definition Table — `{{SYS_A}}` `[CALIBRATE]`

| Code | Name (EN) | Name (VI) | Definition | SOT Reference | Pre-existing? |
|------|-----------|-----------|------------|---------------|---------------|
| `N_{{SYS_A}}_00001` | `{{NODE_01_NAME_EN}}` | `{{NODE_01_NAME_VI}}` | `{{1-sentence function}}` | `{{SOT file + line}}` | Y |
| `N_{{SYS_A}}_00002` | `{{NODE_02_NAME_EN}}` | `{{NODE_02_NAME_VI}}` | `{{1-sentence function}}` | `{{SOT file + line}}` | Y |
| ... | ... | ... | ... | ... | ... |

### 3.1 Node Definition Column Guide `[GENERIC]`

| Column | How to fill |
|--------|-------------|
| **Code** | `N_{{SYS}}_XXXXX` — 5-digit sequential, globally unique via prefix |
| **Name (EN)** | Primary English name — use established terminology from the source system |
| **Name (VI)** | Vietnamese equivalent (if bilingual project); can be omitted for English-only |
| **Definition** | One sentence describing the node's function within its home system |
| **SOT Reference** | File path + line number or section in the system SOT |
| **Pre-existing?** | Y = existed before {{PROJECT_NAME}}; N = created within {{PROJECT_NAME}} |

---

## 4. Edge Definition Table — `{{SYS_A}}` `[CALIBRATE]`

| Code | Name | From Node | To Node | Direction | Definition | SOT Reference |
|------|------|-----------|---------|-----------|------------|---------------|
| `ED_{{SYS_A}}_00001` | `{{EDGE_01_NAME}}` | `N_{{SYS_A}}_00001` | `N_{{SYS_A}}_00002` | → | `{{1-sentence}}` | `{{SOT file + line}}` |
| ... | ... | ... | ... | ... | ... | ... |

### 4.1 Edge Direction Convention `[GENERIC]`

| Symbol | Meaning |
|--------|---------|
| `→` | Directed: From Node → To Node (From depends on / implies / supports To) |
| `↔` | Bidirectional: mutual relationship |
| `—` | Undirected: relationship without direction |

---

## 5. Node/Edge Code Numbering Convention `[GENERIC]`

```
Node codes:  N_{{SYS}}_00001 through N_{{SYS}}_99999
Edge codes: ED_{{SYS}}_00001 through ED_{{SYS}}_99999

Gap policy: Numbers do NOT need to be contiguous.
            Deleted codes are NOT reused.
            New nodes take the next available number.
```

---

## 6. System Status Lifecycle `[GENERIC]`

| Status | Meaning | Allowed Actions |
|--------|---------|-----------------|
| **ACTIVE** | System is actively referenced and may grow | Add/edit nodes, edges, mappings |
| **FROZEN** | System definitions are locked | Read-only; no structural changes |
| **DEPRECATED** | System is retired | Keep for historical reference; flag all mappings |

---

## 7. Quick Checklist `[GENERIC]`

- [ ] Every system has a unique namespace prefix?
- [ ] Every node code is globally unique (prefix + number)?
- [ ] Every node has a 1-sentence definition + SOT reference?
- [ ] Every edge specifies direction (→, ↔, —)?
- [ ] Pre-existing vs. new nodes are distinguished?
- [ ] SOT file path points to an existing file?

---

## 8. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Namespace uniqueness — does prefix rule prevent collisions? | ?/5 | `[CALIBRATE]` |
| R2 | Schema completeness — do node/edge tables capture all needed fields? | ?/5 | `[CALIBRATE]` |
| R3 | N-scalability — does registry support adding a 3rd/4th/Nth system? | ?/5 | `[CALIBRATE]` |
| **Aggregate** | | **?/5** `[PASS/FAIL]` (threshold ≥ 4/5) | |

---

*System Registry — N-system namespace management, node/edge code schemas, prefix-unique constraint. Exported from AHP Template v1.0 (no direct AHP v3.1 source — new file for multi-system support). Calibrate all entries for {{PROJECT_NAME}}.*

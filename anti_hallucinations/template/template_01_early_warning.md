Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# 01 — Early Warning: Hallucination Signal Registry
## {{PROJECT_NAME}}

**Role:** Layer 1 of pipeline — defines early-warning signals. When a claim, term, or mapping matches a signal → trigger anti-hallucination process.
**Input:** Claim text, component description, or file under review.
**Output:** Signal match (Y/N) + severity (RED/ORANGE/YELLOW) + link to `02_detection.md`.
**Next:** `02_detection.md`

---

## 1. Signal Registry `[GENERIC signal names + trigger conditions — CALIBRATE "Example" column for {{PROJECT_NAME}}]`

### 1.1 RED — Category Error / Fabrication

| ID | Signal name | Symptom pattern | Trigger condition | Example from {{PROJECT_NAME}} `[CALIBRATE]` |
|----|------------|-----------------|-------------------|---------------------------------------------|
| R1 | Category error (domain A → domain B) | Claim treats a mapping as a causal explanation | Asserts "X solves/explains/predicts Y" without formal proof or experimental test | `{{DOMAIN_EXAMPLE_R1}}` |
| R2 | Invented source / citation hallucination | Citation does not exist; wrong author/year | Cannot find source in primary literature | `{{DOMAIN_EXAMPLE_R2}}` |
| R3 | Contradiction with known fact | Claim contradicts a verified result or frozen axiom | Asserts result contradicted by published data | `{{DOMAIN_EXAMPLE_R3}}` |
| R4 | **Equivalence without justification** *(most critical for mapping projects)* | Cross-system link treated as equivalence, not analogy | Uses "=" or "<=>" between nodes of different systems without justification | `{{DOMAIN_EXAMPLE_R4}}` |
| R5 | Structural contradiction with core axioms | Claim violates frozen axioms of `{{SYS_A}}` or `{{SYS_B}}` | Requires condition not met by system definition | `{{DOMAIN_EXAMPLE_R5}}` |

### 1.2 ORANGE — Missing / Weak Foundation

| ID | Signal name | Symptom pattern | Trigger condition | Example `[CALIBRATE]` |
|----|------------|-----------------|-------------------|-----------------------|
| O1 | Undefined term | Term used without formal definition | Term appears ≥ 3 times without definition block | `{{DOMAIN_EXAMPLE_O1}}` |
| O2 | Broken trace — source gap | Claim cannot be traced to any SOT | Trace score = 0 | `{{DOMAIN_EXAMPLE_O2}}` |
| O3 | Assumption not flagged | Claim presented as fact, but is assumption | No assumption flag, no boundary note | `{{DOMAIN_EXAMPLE_O3}}` |
| O4 | Weak anchor — single source only | 1 anchor, WEAK strength | Trace score = 1, anchor = WEAK | `{{DOMAIN_EXAMPLE_O4}}` |
| O5 | Stale reference — superseded data | Uses data that has been invalidated | Reference to file/version marked INVALIDATED | `{{DOMAIN_EXAMPLE_O5}}` |

### 1.3 YELLOW — Documentation / Presentation

| ID | Signal name | Symptom pattern | Trigger condition | Example `[CALIBRATE]` |
|----|------------|-----------------|-------------------|-----------------------|
| Y1 | Ambiguous boundary language | Unclear scope of interpretation vs. analogy vs. mapping | Uses "suggests", "implies" without explicit scope | `{{DOMAIN_EXAMPLE_Y1}}` |
| Y2 | Missing disclaimer / boundary statement | Claim exceeds system scope, no boundary note | File lacks scope boundary | `{{DOMAIN_EXAMPLE_Y2}}` |
| Y3 | Inconsistent terminology | Same concept, multiple names | ≥ 2 term variants for same concept in same file | `{{DOMAIN_EXAMPLE_Y3}}` |
| Y4 | Missing version / date metadata | No version, date, or status in file | Markdown file without header metadata | `{{DOMAIN_EXAMPLE_Y4}}` |
| Y5 | System lineage not documented | Cross-system mapping exists but not in Mapping Registry | Node with known analogue but no registry entry | `{{DOMAIN_EXAMPLE_Y5}}` |

### 1.4 CCL — Confidence Calibration Signals (BDS v4.0) `[GENERIC]`

> CCL detects linguistic overconfidence — high-confidence language for low-reliability claims.

| ID | Signal | Pattern markers | Trigger | Example `[CALIBRATE]` |
|----|--------|----------------|---------|----------------------|
| S16 | Confident marker + LOW-reliability claim | "it is proven", "clearly establishes", "obviously" | Pattern in unverified/LOW-VYR claim | `{{DOMAIN_EXAMPLE_S16}}` |
| S17 | Precision overclaim | "exactly", "precisely", "definitively" | Numeric value without uncertainty bounds | `{{DOMAIN_EXAMPLE_S17}}` |
| S18 | Universal quantifier without boundary | "always", "never", "all", "every" | Universal claim without scope statement | `{{DOMAIN_EXAMPLE_S18}}` |
| S19 | Temporal currency implied for Smṛti | "currently", "now", "at present" | Time-indexed claim in TTL_CLASS=Current without citation date | `{{DOMAIN_EXAMPLE_S19}}` |
| S20 | Self-referential verification — TIP violation | AI claim A cited as evidence for AI claim B | Circular: A→B→A; same session generates + evaluates | `{{DOMAIN_EXAMPLE_S20}}` |

**Severity:** S16-S19 → ORANGE; S20 → RED (block + mandatory TIP-1).

---

## 2. Severity Escalation Protocol `[GENERIC]`

| Severity | Meaning | Action | Deadline |
|----------|---------|--------|----------|
| **RED** | Category error or fabrication | Block merge + full pipeline | Before next commit |
| **ORANGE** | Missing foundation | Investigate 02→03→04 | Within current session |
| **YELLOW** | Documentation gap | Review + fix | Within the week |

---

## 3. Trigger Workflow `[GENERIC]`

```
New claim / component
  → Scan Signal Registry (§1)
  → Match RED? → Stakes CRITICAL → Full pipeline + TIP-1
  → Match ORANGE? → Stakes HIGH/MEDIUM → Full or minimum pipeline
  → Match YELLOW? → Documentation review
  → No match? → Document as [AH-OK] (pending full scoring)
```

---

## 4. Quick Scan Checklist `[GENERIC]`

- [ ] Every term has a formal definition? (O1)
- [ ] Every claim traces to a SOT? (O2)
- [ ] Every assumption is flagged? (O3)
- [ ] No stale/invalidated references? (O5)
- [ ] No cross-system equivalence without justification? (R4)
- [ ] No contradiction with core axioms? (R5)
- [ ] No overconfident language for low-reliability claims? (S16)
- [ ] No circular AI self-citation? (S20)
- [ ] All mapping links registered in Mapping Registry? (Y5)
- [ ] File has version/date metadata? (Y4)

---

*Early Warning — 20 signals: R1-R5 (RED), O1-O5 (ORANGE), Y1-Y5 (YELLOW), S16-S20 (CCL). Generic; calibrate "Example" column for {{PROJECT_NAME}}. Exported from AHP v3.1.*

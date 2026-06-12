Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# Vyāpti Registry — {{PROJECT_NAME}} Claim Type Taxonomy

**Version:** v1.0 (YYYY-MM-DD)
**Role:** {{PROJECT_NAME}} claim type taxonomy with reliability priors — Vyāpti (pervasion) check: does the claim type's reliability prior warrant its confidence level?
**Usage:** Look up BEFORE a claim is accepted into the pipeline. Match claim → VYR entry → check reliability prior + TTL_CLASS.
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5

---

## 1. Vyāpti Principle `[GENERIC]`

**Vyāpti** (Sanskrit: pervasion/invariable concomitance): "A implies B" is only valid when A and B have invariable co-occurrence — no case where A holds but B does not.

In the anti-hallucination pipeline: "Claim type implies reliability prior." You can only trust a confidence level when the claim type's historical reliability warrants it.

**{{PROJECT_NAME}} adaptation:** Each claim type has a reliability prior calibrated from {{PROJECT_NAME}} audit history. When assessing confidence level of a claim, first check: "Does this claim type have reliability high enough to warrant this confidence level?"

---

## 2. VYR Registry — Core Entries `[CALIBRATE ALL — every entry must be re-derived for {{PROJECT_NAME}}]`

### 2A. Structural Framework Claims

| VYR-ID | Claim Type | Detection Pattern | ES Tag | Reliability Prior | TTL_CLASS | Re-verify Trigger |
|--------|-----------|-------------------|--------|------------------|-----------|------------------|
| **VYR-001** | `{{CORE_AXIOM_TYPE}}` | `{{DETECTION_PATTERN}}` | `[ES-PRATY]` | **HIGH** — `{{RELIABILITY_RATIONALE}}` | Atemporal | `{{REVERIFY_TRIGGER}}` |
| **VYR-002** | `{{THEOREM_TYPE}}` | `{{DETECTION_PATTERN}}` | `[ES-ANUMA]` | **HIGH** — `{{RELIABILITY_RATIONALE}}` | Geological | `{{REVERIFY_TRIGGER}}` |
| **VYR-003** | `{{THEOREM_DEFERRED_TYPE}}` | `{{DETECTION_PATTERN}}` | `[ES-ANUMA]` | **MEDIUM** — `{{RELIABILITY_RATIONALE}}` | Geological | `{{REVERIFY_TRIGGER}}` |

### 2B. Empirical Claims

| VYR-ID | Claim Type | Detection Pattern | ES Tag | Reliability Prior | TTL_CLASS | Re-verify Trigger |
|--------|-----------|-------------------|--------|------------------|-----------|------------------|
| **VYR-004** | `{{EMPIRICAL_CLAIM_TYPE}}` | `{{DETECTION_PATTERN}}` | `[ES-ANUMA]`+`[ES-SMRTI]` | **LOW** — `{{RELIABILITY_RATIONALE}}` | Current | `{{REVERIFY_TRIGGER}}` |
| **VYR-005** | `{{DATA_ANALYSIS_TYPE}}` | `{{DETECTION_PATTERN}}` | `[ES-SMRTI]` | **MEDIUM** — `{{RELIABILITY_RATIONALE}}` | Current | `{{REVERIFY_TRIGGER}}` |

### 2C. Postulate & Mapping Claims

| VYR-ID | Claim Type | Detection Pattern | ES Tag | Reliability Prior | TTL_CLASS | Re-verify Trigger |
|--------|-----------|-------------------|--------|------------------|-----------|------------------|
| **VYR-006** | `{{POSTULATE_TYPE}}` | `{{DETECTION_PATTERN}}` | `[ES-ANUMA]` | **MEDIUM** — `{{RELIABILITY_RATIONALE}}` | Historical | `{{REVERIFY_TRIGGER}}` |
| **VYR-007** | Cross-system mapping claim | `N_{{SYS_A}}_`, `maps to`, `↔`, `N_{{SYS_B}}_` | `[ES-ANUMA]` | **MEDIUM** — system SOTs strong; MAPPING = interpretive boundary | Historical | SOT change in either system |
| **VYR-008** | `{{CLASSIFICATION_TYPE}}` | `{{DETECTION_PATTERN}}` | `[ES-ANUMA]` | **HIGH** — `{{RELIABILITY_RATIONALE}}` | Geological | `{{REVERIFY_TRIGGER}}` |

### 2D. Implementation & Technical Claims

| VYR-ID | Claim Type | Detection Pattern | ES Tag | Reliability Prior | TTL_CLASS | Re-verify Trigger |
|--------|-----------|-------------------|--------|------------------|-----------|------------------|
| **VYR-009** | `{{IMPLEMENTATION_TYPE}}` | `{{DETECTION_PATTERN}}` | `[ES-ANUMA]` | **LOW** — `{{RELIABILITY_RATIONALE}}` | Current | `{{REVERIFY_TRIGGER}}` |
| **VYR-010** | Score/rank claim in top risk record | "Rank", "Risk Score", "H=", "W=", "RS-HIGH", "RS-CRIT" | `[ES-PRATY]` | **HIGH** — explicitly computed + RCA-verified per changelog | Geological | Re-audit trigger |

> **Calibration note:** The above entries are PLACEHOLDER templates. Every VYR entry MUST be re-derived from {{PROJECT_NAME}}'s actual claim types, audit history, and system architecture. Do NOT copy VYR entries from any other project — each project's reliability priors are domain-specific.

---

## 3. Reliability Prior Definitions `[GENERIC]`

| Level | Meaning | {{PROJECT_NAME}} threshold `[CALIBRATE]` |
|-------|---------|----------------------------------------|
| **HIGH** | Claim type has strong invariable relationship between assertion and ground truth | Trace score ≥ 4/N + multiple verification rounds |
| **MEDIUM** | Claim type has moderate reliability; some risk of error | Trace score 2-3/N; at least 1 verification round |
| **LOW** | Claim type frequently has confidence exceeding evidence | Trace score ≤ 1/N; limited verification; exploratory claim |

**Vyāpti check rule:** When claim type = LOW reliability prior, MUST NOT express as HIGH confidence ("it is proven", "clearly establishes", "beyond doubt"). If this pattern is detected → Signal S16 (CCL, `01_early_warning.md` §1.4).

---

## 4. How to Use This Registry `[GENERIC]`

1. **Identify claim type:** Match claim text against Detection Pattern column.
2. **Look up VYR entry:** Get reliability prior + TTL_CLASS + ES tag.
3. **Apply Vyāpti check:** Is the claim's expressed confidence consistent with reliability prior?
4. **Check TTL_CLASS:** Is this claim's verification state still within TTL window?
5. **Flag if mismatch:** LOW reliability + HIGH confidence language → S16 (CCL overconfidence signal).

### Example Application `[CALIBRATE]`

```
Claim: "{{EXAMPLE_CLAIM_TEXT}}"

Step 1: Match pattern → {{MATCHED_VYR_ID}}
Step 2: {{VYR_ID}}: Reliability Prior = {{LEVEL}}; TTL_CLASS = {{TTL}}; ES Tag = {{ES_TAG}}
Step 3: Vyāpti check: "{{CONFIDENCE_LANGUAGE}}" = {{CONFIDENCE_LEVEL}} confidence vs {{LEVEL}} reliability → {{MATCH/MISMATCH}}
Step 4: TTL: {{TTL}} → {{WITHIN_WINDOW/EXPIRED}}
Step 5: {{IF_MISMATCH}} Flag: Signal S16 (linguistic overconfidence for LOW-reliability claim type)
  → Reframe to: "{{REFramed_CLAIM}}"
```

---

## 5. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Coverage — do VYR entries cover all known claim types? | ?/5 | `[CALIBRATE]` |
| R2 | Reliability calibration — do priors match actual audit history? | ?/5 | `[CALIBRATE]` |
| R3 | Usability — can reviewer match a claim to VYR quickly? | ?/5 | `[CALIBRATE]` |
| **Aggregate** | | **?/5** `[PASS/FAIL]` (threshold ≥ 4/5) | |

---

*Vyāpti Registry — claim type taxonomy with reliability priors. Exported from AHP v3.1 bds_vyapti_registry.md. ALL VYR entries are placeholders — MUST be re-derived for {{PROJECT_NAME}}. 3-Round RCA verification required after calibration.*

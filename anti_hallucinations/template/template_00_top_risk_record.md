Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# 00 — Top Risk Record
## {{PROJECT_NAME}} — Highest-Risk Components

**Version:** v1.0 (YYYY-MM-DD)
**Scope:** {{PROJECT_SCOPE}}
**Re-audit cadence:** [RS-CRIT] weekly | [RS-HIGH] every 2 weeks | [RS-MED] monthly | [RS-LOW] quarterly
**Risk Score formula:** H × W × (1+A)
  - H = Hallucination score (0-10)
  - W = Weighting factor (1-3: 1=documentation, 2=framework, 3=public claim)
  - A = Amplifier (0-1: 0=none, 0.5=active research, 1.0=blocking/public)
**TTL_CLASS:** Atemporal | Geological (years) | Historical (months) | Current (weeks)

---

## Table 1 — {{PROJECT_NAME}} Core Components `[CALIBRATE — replace placeholder rows]`

| Rank | Component ID | Name | System | H | W | A | Risk Score | TTL_CLASS | Label | Notes |
|------|-------------|------|--------|---|---|---|-----------|-----------|-------|-------|
| 1 | `{{COMP_001}}` | `{{COMP_001_NAME}}` | `{{SYS_A}}` | ? | ? | ? | — | `{{TTL}}` | `[AH-?][RS-?][ES-?]` | `{{NOTES_1}}` |
| 2 | `{{COMP_002}}` | `{{COMP_002_NAME}}` | `{{SYS_B}}` | ? | ? | ? | — | `{{TTL}}` | `[AH-?][RS-?][ES-?]` | `{{NOTES_2}}` |

> **Mapping risk note:** Cross-system mapping links (mapping_type = ANALOGY promoted to STRUCTURAL without new justification) are often the highest-risk components in multi-system projects. Signal R4 (equivalence without justification) applies. Track in Table 2.

---

## Table 2 — Cross-System Mapping Components `[CALIBRATE]`

| Rank | Mapping ID | Source Node | Target Node | mapping_type | H | Risk Score | Label | Justification |
|------|-----------|------------|------------|--------------|---|-----------|-------|--------------|
| 1 | `{{MAP_001}}` | `N_{{SYS_A}}_XXXXX` | `N_{{SYS_B}}_XXXXX` | ANALOGY | ? | — | `[AH-?][ES-ANUMA]` | ☐ Documented |

---

## Risk Score Formula `[GENERIC]`

```
Risk Score = H × W × (1 + A)

Example: H=7, W=2, A=0.5 → 7 × 2 × 1.5 = 21.0 → [RS-CRIT]

W calibration for {{PROJECT_NAME}} [CALIBRATE]:
  1 = documentation component
  2 = framework / mapping component
  3 = public claim or system-level definition

A calibration:
  0.0 = stable, not actively developed
  0.5 = under active development
  1.0 = blocking gate or public-facing claim
```

---

## TTL_CLASS Definitions `[GENERIC]`

| TTL_CLASS | Meaning | Re-verify trigger |
|-----------|---------|------------------|
| Atemporal | Frozen structural axiom | Architecture revision only |
| Geological | Stable years — theorem, proof | Architecture revision |
| Historical | Stable months — literature claim | Relevant literature update |
| Current | Valid weeks–months — empirical result | New experimental data |

---

## Shared Component Rule `[GENERIC]`

A component appearing in both Table 1 and Table 2 must be tracked in BOTH with consistent scores. If scores diverge, use the higher score.

---

## Version History `[CALIBRATE]`

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | YYYY-MM-DD | Initial instantiation — {{PROJECT_NAME}} |

---

*Top Risk Record v1.0 — Risk Score H×W×(1+A), Dual-Table, TTL_CLASS. Exported from AHP v3.1. Calibrate all entries for {{PROJECT_NAME}}.*

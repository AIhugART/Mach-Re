Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# 06 — Solution Matrix & Resolution Tracking
## MACH-RE — P0-P4 + P-DEFER Priority

**Role:** Standardized resolution tracking for every issue scored ≥ 5.
**Input:** H score + root cause (`04_analysis.md`) + confirmation (`labels.md`).
**Output:** Solution type + priority + action + tracking entry.

---

## 1. Solution Types

| Type | Name | MACH RE Example |
|------|------|----------------|
| **Type 1** | SOT ANCHOR | Link claim to node code + source line + add citation |
| **Type 2** | SCOPE BOUNDARY | Add "This claim does not apply to..." boundary statement |
| **Type 3** | DOCUMENT | Fix wording: "isomorphic" → "structurally analogous"; "proves" → "is consistent with" |
| **Type 4** | REMOVE | Delete hallucinated claim — no salvage possible |
| **Type 5** | DEFER | `[AH-NAJ]` claims; claims requiring unavailable external expertise |

---

## 2. Priority Matrix

| Priority | Trigger | Response Time | Blocking? |
|----------|---------|--------------|-----------|
| **P0** | `[AH-CRIT]` / `[AH-AIHL]` (#2) / Risk ≥ 20 / S20 | Before any merge | **YES** |
| **P1** | `[AH-HIGH]` / Risk 15–19.9 / R1-R4 | Within current sprint | **YES** (release) |
| **P2** | `[AH-WARN]` / Risk 10–14.9 / O1-O5 | Next audit cycle | No |
| **P3** | `[AH-LOW]` / Risk < 10 | Document + monitor | No |
| **P4** | `[AH-OK]` | No action | No |
| **P-DEFER** | `[AH-NAJ]` (#3) | Unlock condition OR quarterly | No |

---

## 3. Resolution Tracking

| # | Issue | Component | H | Root Cause | Priority | Solution | Action | Status |
|---|-------|-----------|---|------------|----------|----------|--------|--------|
| 1 | "Isomorphic" overstates MAP_001 | MAP_001 wording | 5 | Type 5 | P2 | Type 3 | "isomorphic" → "structurally analogous" | OPEN |
| 2 | V ⊥ H no compass formalization | TRITHUC-1 | 6 | Type 3 | P-DEFER | Type 5 | Unlock: cross-cultural verification ≥ 1 non-VN system | OPEN |

---

## 4. P-DEFER Registry (`[AH-NAJ]` — labels.md #3)

| # | Claim | Unlock Condition | Defer Date | Re-evaluate By |
|---|-------|-----------------|-----------|---------------|
| 1 | TRITHUC-1: V ⊥ H | Cross-cultural verification ≥ 1 non-Vietnamese system | 2026-06-12 | 2026-09-12 |
| 2 | TRITHUC-2: C1-graded reflexivity | Formalization across ≥ 1 dyadic case study | 2026-06-12 | 2026-09-12 |

---

## 5. Resolution Workflow

```
Issue scored ≥ 5
  → Assign Solution Type (1-5) + Priority (P0-P4/P-DEFER)
  → IF [AH-NAJ] → P-DEFER, document unlock condition
  → IF P0/P1 → CHANGELOG entry + notify
  → IF P2 → schedule next audit cycle
  → Track to RESOLVED or DEFERRED
```

---

*06_solution.md v1.0 — 5 types, P0-P4+P-DEFER, resolution tracking, P-DEFER registry. Instantiated from AHP Template v1.0 (2026-06-12).*

Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# Label System — MACH-RE Warning Tag Taxonomy
## 25 Labels: 5 Primary + 9 Secondary + 4 RS + 4 ES + 3 Confirmation

**Role:** Standardized label mechanism. Anchored to `labels.md` for confirmation verdicts.
**Input:** H score (`05_scoring.md`) + Risk Score + trace score + anchor strength.
**Output:** Primary + RS + ES + Confirmation + Secondary labels.

---

## 1. Label Taxonomy

### 1.1 Primary Labels — by H Score

| Label | Band | H Score | Meaning | Action |
|-------|------|---------|---------|--------|
| `[AH-OK]` | 🟢 | 0-2 | SOT-verified | No action |
| `[AH-LOW]` | 🔵 | 3-4 | Low risk — documented lineage | Add docs if needed |
| `[AH-WARN]` | 🟡 | 5-6 | Warning — speculative | Investigate. Weekly re-audit. |
| `[AH-HIGH]` | 🟠 | 7-8 | High risk — weak basis | Full RCA. No merge unresolved. |
| `[AH-CRIT]` | 🔴 | 9-10 | Critical — hallucination | BLOCKING. Fix immediately. |

### 1.2 Secondary Labels

| Label | Trigger | Meaning |
|-------|---------|---------|
| `[AH-ORPHAN]` | Trace = 0 | No SOT anchor |
| `[AH-WEAK]` | WEAK anchor (1 SOT) | Weak anchor |
| `[AH-DERIVED]` | Assumption → proven | Derived |
| `[AH-ELIM]` | Fully removed | Eliminated |
| `[AH-DEFER]` | Deferred + unlock condition | Deferred |
| `[AH-LOCK]` | Decision-locked | Locked |
| `[AH-DIVERGE]` | ≥ 2 interpretations | Divergent |
| `[AH-NOISE]` | Alternative not ruled out | Noise risk |
| `[AH-EX]` | External compass flagged | Compass-flagged |

### 1.3 Risk Score Labels

| Label | Risk Score | Re-audit |
|-------|-----------|----------|
| `[RS-CRIT]` | ≥ 20 | Weekly |
| `[RS-HIGH]` | 15–19.9 | Every 2 weeks |
| `[RS-MED]` | 10–14.9 | Monthly |
| `[RS-LOW]` | < 10 | Quarterly |

### 1.4 Epistemic Source Labels

| Label | Definition | Trace Threshold | MACH RE Default For |
|-------|-----------|----------------|---------------------|
| `[ES-PRATY]` | Direct external anchor: published data, frozen axioms | ≥ 4/8; ≥ 1 STRONG | Core axioms 3.0/3 (VYR-1); NAC home-system (VYR-7) |
| `[ES-ANUMA]` | Derived by valid inference; explicit derivation chain | 2-3/8 | Core axioms 1.5-2.5/3 (VYR-2); derived props (VYR-3); heuristics (VYR-4); mapping links (VYR-6); `[proposed-by-this-project]` (VYR-8) |
| `[ES-SMRTI]` | Literature-derived; needs TTL check | 1-2/8 | Folk evidence (VYR-9); ca dao, tục ngữ |
| `[ES-VIKALP]` | Pattern-constructed without anchor | 0/8 | TRITHUC gaps (VYR-5); new unverified claims |

**Critical:** `[ES-VIKALP]` MUST NOT be presented as `[ES-PRATY]`. Detection: S16+S20 → `[AH-CRIT]`.

### 1.5 Confirmation State Labels — Anchored to `labels.md`

> **Canonical SOT:** `labels.md`. In case of discrepancy, labels.md takes precedence.

| Label | labels.md # | Trigger | Meaning | Action |
|-------|------------|---------|---------|--------|
| `[AH-HCNF]` | **#1** | TIP-1 PASS | Human Confirmed | Log reviewer + date |
| `[AH-AIHL]` | **#2** | trace=0 + contradicts SOT + S20 + human verdict | AI Hallucination | **BLOCKING.** Remove/replace. |
| `[AH-NAJ]` | **#3** | Cannot judge — outside epistemic jurisdiction | No Authority to Judge | **DEFER.** Unlock condition. Does NOT block. |

> **`[AH-NAJ]` rationale:** Implements `axiom_spec.md §0.6` kill condition #1 at audit level. "I don't know" is a valid epistemic state — Tiên Đề V.

**Label order:** `[AH-WARN] [RS-HIGH] [ES-ANUMA] [AH-HCNF] [AH-EX]`

---

## 2. Decision Tree

```
New component
  → Step 1: H score → Primary Label
  → Step 2: Risk Score → RS Label
  → Step 3: ES source type → ES Label
  → Step 4: Secondary conditions → Secondary Labels
  → Step 5: Human confirmation
      Can judge? → YES → [AH-HCNF] (#1) or [AH-AIHL] (#2)
                   NO  → [AH-NAJ] (#3) + defer with unlock condition
  → Register in Component Registry
```

---

## 3. MACH RE ES Tag Defaults

| Claim type | Default ES Tag | Rationale |
|-----------|---------------|-----------|
| Core axiom, 3.0/3 triangulation | `[ES-PRATY]` | ≥ 3 compass systems, published sources |
| Core axiom, 1.5–2.5/3 | `[ES-ANUMA]` | Valid structural inference |
| Derived proposition | `[ES-ANUMA]` | Logically entailed |
| Heuristic (DSH) | `[ES-ANUMA]` + TTL=Historical | Empirical generalization |
| Cross-system mapping link | `[ES-ANUMA]` + boundary: "Interpretive — not equivalence" | Structural analogy |
| TRITHUC gap (unresolved) | `[ES-VIKALP]` pending | Currently unanchored |
| Ca dao / folk evidence | `[ES-SMRTI]` | Oral tradition |
| New unverified claim | `[ES-VIKALP]` pending | Default until trace ≥ 2/8 |

---

*Label System v1.0 — 25 labels. labels.md = canonical confirmation SOT. Instantiated from AHP Template v1.0 (2026-06-12).*

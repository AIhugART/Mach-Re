Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# Label System — Warning Tag Taxonomy
## {{PROJECT_NAME}} Anti-Hallucination Pipeline

**Role:** Standardized warning label mechanism for every component/concept/claim in {{PROJECT_NAME}}.
**Input:** Hallucination score H (from `05_scoring.md`) + Risk Score (from `00_top_risk_record.md`) + trace score + anchor strength.
**Output:** Primary label + secondary label(s) + registry entry.

---

## 1. Label Taxonomy `[GENERIC — all 24 labels export as-is]`

### 1.1 Primary Labels — by Hallucination Score (H)

| Label | Band | H Score | Color | Meaning | Action |
|-------|------|---------|-------|---------|--------|
| `[AH-OK]` | Green | 0-2 | 🟢 | Verified — SOT-verified, no new assumption | No action. |
| `[AH-LOW]` | Blue | 3-4 | 🔵 | Low risk — conceptual extension, documented lineage | Add documentation if needed. |
| `[AH-WARN]` | Yellow | 5-6 | 🟡 | Warning — speculative, flagged assumption | Investigate. Re-audit weekly. |
| `[AH-HIGH]` | Orange | 7-8 | 🟠 | High risk — suspicious, weak basis | Full RCA. Do not merge unresolved. |
| `[AH-CRIT]` | Red | 9-10 | 🔴 | Critical — clear hallucination / orphaned | BLOCKING. Fix immediately. |

### 1.2 Secondary Labels — by Status / Characteristic

| Label | Trigger | Meaning |
|-------|---------|---------|
| `[AH-ORPHAN]` | Trace score = 0 | Orphaned — no SOT anchor |
| `[AH-WEAK]` | Anchor strength = WEAK (1 SOT, conceptual only) | Weak anchor |
| `[AH-DERIVED]` | Was assumption → now proven | Derived |
| `[AH-ELIM]` | Assumption fully removed | Eliminated |
| `[AH-DEFER]` | Deferred with unlock condition | Deferred |
| `[AH-LOCK]` | Locked by decision | Decision-locked |
| `[AH-DIVERGE]` | ≥ 2 implementations/interpretations | Divergent |
| `[AH-NOISE]` | Alternative explanation not ruled out | Noise risk |
| `[AH-EX]` | Flagged by external compass | Compass-flagged |

### 1.3 Risk Score Labels — by Risk Score H×W×(1+A)

| Label | Risk Score | Re-audit cadence |
|-------|-----------|-----------------|
| `[RS-CRIT]` | ≥ 20 | Weekly |
| `[RS-HIGH]` | 15–19.9 | Every 2 weeks |
| `[RS-MED]` | 10–14.9 | Monthly |
| `[RS-LOW]` | < 10 | Quarterly |

### 1.4 Epistemic Source Labels `[GENERIC — calibrate defaults below for {{PROJECT_NAME}}]`

| Label | BDS Equivalent | Definition | Trace Threshold |
|-------|----------------|------------|-----------------|
| `[ES-PRATY]` | Pratyakṣa | Direct external anchor: frozen axioms, published data, peer-reviewed result | Trace ≥ 4/N; ≥ 1 STRONG anchor |
| `[ES-ANUMA]` | Anumāna | Derived by valid inference — formal proof, bridge theorem | Trace 2-3/N; derivation chain explicit |
| `[ES-SMRTI]` | Smṛti | Literature-derived; secondary source; needs TTL check | Trace 1-2/N |
| `[ES-VIKALP]` | Vikalpa | Pattern-constructed without anchor; AI-generated without SOT | Trace 0/N |

**Critical rule:** `[ES-VIKALP]` MUST NOT be presented as `[ES-PRATY]`. Detection: S16 + S20 → `[AH-CRIT]`.

**Default ES tag by claim type `[CALIBRATE]`:**

| Claim type in {{PROJECT_NAME}} | Default ES tag | Rationale |
|-------------------------------|---------------|-----------|
| `{{CLAIM_TYPE_1}}` | `[ES-PRATY]` | `{{RATIONALE_1}}` |
| `{{CLAIM_TYPE_2}}` | `[ES-ANUMA]` | `{{RATIONALE_2}}` |
| Cross-system mapping links | `[ES-ANUMA]` + boundary note | Interpretive — not equivalence unless formally justified |
| New unverified claims | `[ES-VIKALP]` pending trace | Default until trace ≥ 2/N |

**Label order:**
```
[AH-WARN] [RS-HIGH] [ES-ANUMA] [AH-HCNF] [AH-EX]
  ^         ^          ^          ^          ^
  Primary   Risk       ES Source  Confirm   Secondary
```

### 1.5 Confirmation State Labels `[GENERIC]`

> `[AH-HCNF]` ≡ Pratyakṣa (direct perception by reliable expert); `[AH-AIHL]` ≡ Vikalpa confirmed ungrounded.

| Label | Trigger | Meaning | Action |
|-------|---------|---------|--------|
| `[AH-HCNF]` | Human reviewer explicitly confirmed; TIP-1 PASS documented | Human Confirmed | Log reviewer + date in registry |
| `[AH-AIHL]` | Confirmed AI-fabricated: trace=0 + contradicts SOT + S20 + human verdict | AI Hallucination Confirmed | **BLOCKING**. Supersedes `[AH-CRIT]`. Remove or replace. |

---

## 2. Decision Tree `[GENERIC]`

```
New component
  → Step 1: H score → Primary Label
  → Step 2: Risk Score H×W×(1+A) → RS Label
  → Step 3: ES source type → ES Label
      direct anchor → [ES-PRATY]
      formal derivation → [ES-ANUMA]
      literature only → [ES-SMRTI]
      new + unanchored → [ES-VIKALP]
  → Step 4: Secondary conditions → Secondary Labels
  → Step 5: Human confirmation → [AH-HCNF] / [AH-AIHL]
  → Register in Component Registry (§3)
```

---

## 3. Component Registry `[CALIBRATE]`

| Component ID | Name | Primary | RS | ES | Confirm | Secondary | Last audit |
|-------------|------|---------|----|----|---------|-----------|-----------|
| `{{COMP_001}}` | `{{COMP_001_NAME}}` | `[AH-?]` | `[RS-?]` | `[ES-?]` | — | — | YYYY-MM-DD |

---

## 4. Dashboard `[CALIBRATE — update after each audit]`

### 4.1 Primary Distribution

| Label | Count | % |
|-------|-------|---|
| `[AH-OK]` | 0 | — |
| `[AH-LOW]` | 0 | — |
| `[AH-WARN]` | 0 | — |
| `[AH-HIGH]` | 0 | — |
| `[AH-CRIT]` | 0 | — |
| **Total** | **0** | — |

### 4.2 ES Source Distribution

| Label | Count |
|-------|-------|
| `[ES-PRATY]` | 0 |
| `[ES-ANUMA]` | 0 |
| `[ES-SMRTI]` | 0 |
| `[ES-VIKALP]` | 0 |

### 4.3 Confirmation State

| Label | Count |
|-------|-------|
| `[AH-HCNF]` | 0 |
| `[AH-AIHL]` | 0 |

---

*Label System — 24 labels: 5 Primary + 9 Secondary + 4 RS + 4 ES + 2 Confirmation. Exported from AHP v3.1 label_system.md. Calibrate §1.4 ES tag defaults for {{PROJECT_NAME}}.*

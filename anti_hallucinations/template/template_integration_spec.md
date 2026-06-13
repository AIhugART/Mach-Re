Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: {{PROJECT_NAME}} | Date: YYYY-MM-DD -->

# Epistemic Integration Specification — {{PROJECT_NAME}} AHP

**Version:** v1.0 (YYYY-MM-DD)
**Role:** Specification for how the Epistemic Framework maps into the {{PROJECT_NAME}} Anti-Hallucination Pipeline.
**Target:** AHP pipeline (files 01–06 + label_system + 00_top_risk).
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5

---

## 1. Layer Mapping: AHP ↔ Epistemic Framework `[CALIBRATE]`

| AHP Component | Epistemic Layer | Mechanism | Integration Status | Notes |
|---------------|----------------|-----------|-------------------|-------|
| `01_early_warning.md` (signals) | `{{DHARMA_EQUIVALENT}}` | Structural Validation + Confidence Calibration | **ACTIVE** | CCL signals S16-S20 (§1.4) |
| `02_detection.md` (inventory) | `{{CITTA_EQUIVALENT}}` | Component classification + Epistemic tag emission | **ACTIVE** | ES tag per component via `label_system.md` §1.4 |
| `03_sot_traceability.md` (SOT cross-ref) | `{{DHARMA_EQUIVALENT}}` | Vyāpti check + Anchor verification | **ACTIVE** | Vyāpti Registry cross-check |
| `04_analysis.md` (5-Whys RCA) | `{{SANGHA_EQUIVALENT}}` | FSR (Falsifier Strength Rubric) | **ACTIVE** | FSR section — threshold ≥9/12 |
| `05_scoring.md` (0-10 rubric) | `{{SANGHA_EQUIVALENT}}` | Calibrator (score calibration) | **ACTIVE** | Two-tier calibration via Stakes Assessment |
| `label_system.md` | Output Schema | Epistemic labels + TTL_CLASS | **ACTIVE** | ES labels §1.4; TTL_CLASS referenced |
| `06_solution.md` (P0-P4) | Pipeline routing | Routing rules | **ACTIVE** | Stakes-based routing |
| `00_top_risk_record.md` | Monitoring Layer | TTL tracking + temporal decay | **ACTIVE** | TTL_CLASS column |

---

## 2. Epistemic Source Tag Definitions `[GENERIC — calibrate domain examples]`

Four epistemic types applicable to any multi-system mapping project:

| Tag | Epistemic Type | Definition | Verification Requirement |
|-----|---------------|------------|--------------------------|
| `[ES-PRATY]` | Direct external anchor | Claim directly verified against: (a) established textbook/paper, (b) published experimental data, (c) frozen core axioms, or (d) peer-reviewed result | Trace score ≥ 4/N; at least 1 STRONG anchor |
| `[ES-ANUMA]` | Derived by valid inference | Claim is result of derivation, proof, or formal implication from Pratyakṣa-grounded claims | Trace score 2-3/N; explicit derivation chain; bridge theorem or formal deduction present |
| `[ES-SMRTI]` | Literature-derived | Claim supported by secondary literature, analogy, or historical precedent — no direct anchor to project-specific SOT | Trace score 1-2/N; TTL_CLASS check required (literature ages); re-verify periodically |
| `[ES-VIKALP]` | Pattern-constructed only | Claim arises from linguistic pattern, analogy-completion, or AI generation without external anchor | Trace score 0/N; `[AH-ORPHAN]` likely; **BLOCKING** if presented as Pratyakṣa |

### 2.1 Critical Rule (Anti-Hallucination Core)

> **`[ES-VIKALP]` MUST NOT be presented as `[ES-PRATY]`.**
>
> This is the primary hallucination mechanism: AI-generated text carries the linguistic confidence of Pratyakṣa (direct) but has the epistemic foundation of Vikalpa (pattern-constructed). When this pattern is detected: Signal S20 (TIP violation) + `[AH-CRIT]` priority.

### 2.2 Calibration Table — {{PROJECT_NAME}} Claim Types `[CALIBRATE]`

| Claim Type | Default ES Tag | Rationale |
|-----------|---------------|-----------|
| `{{CLAIM_TYPE_1}}` | `[ES-PRATY]` | `{{RATIONALE_1}}` |
| `{{CLAIM_TYPE_2}}` | `[ES-ANUMA]` | `{{RATIONALE_2}}` |
| `{{CLAIM_TYPE_3}}` | `[ES-ANUMA]` + `[ES-SMRTI]` | `{{RATIONALE_3}}` |
| Cross-system mapping links | `[ES-ANUMA]` + boundary note | Interpretive, not equivalence |
| New claims (unverified) | `[ES-VIKALP]` pending trace | Default until trace ≥ 2/N established |

---

## 3. TIP — Tagger Independence Protocol `[GENERIC]`

### 3.1 TIP Definition

A Tagger model MUST NOT share epistemic foundation with the Generator model. The same entity that produced a claim cannot reliably evaluate its own hallucination risk — this is the bootstrapping paradox.

### 3.2 Implementation Levels

| TIP Level | Mechanism | Trigger |
|-----------|-----------|---------|
| **TIP-1:** Independent human RCA | Human reviewer runs independent RCA round when AI generates a claim | Every new claim `[AH-WARN]` or above |
| **TIP-2:** SOT cross-reference | Claim must trace to SOT independent of AI generation context | Every component in pipeline |
| **TIP-3:** Signal S20 detection | Flag when AI-generated claim is cited as evidence for another AI-generated claim | Every claim in `[ES-ANUMA]` or `[ES-VIKALP]` band |

**Independence guarantee:** AI cannot "self-verify" a claim it just generated — must have (a) human RCA round or (b) SOT anchor independent of generation context.

### 3.3 TIP Warning

> "If the tagger is the same model as the generator, its evaluations are conditioned on the same distributional priors. It will be systematically overconfident in claims that match its training distribution — exactly the class of confident-but-wrong claims we need to catch."
>
> **{{PROJECT_NAME}} implication:** Every claim with `[ES-VIKALP]` risk must be human-reviewed (TIP-1) BEFORE being accepted into the framework.

---

## 4. TTL Classes — {{PROJECT_NAME}} Mapping `[GENERIC — calibrate examples]`

Verification state is time-limited (Kṣaṇika principle: momentariness).

| TTL_CLASS | Definition | {{PROJECT_NAME}} Application `[CALIBRATE]` | Re-verify Trigger |
|-----------|-----------|------------------------------------------|------------------|
| **Atemporal** | Mathematical truths; no expiration | `{{ATEMPORAL_EXAMPLE}}` | Only if axiom revised |
| **Geological** | Stable for years; slow-changing | `{{GEOLOGICAL_EXAMPLE}}` | Major architecture revision |
| **Historical** | Stable for months-years; changes with field consensus | `{{HISTORICAL_EXAMPLE}}` | SOT change, new scholarship |
| **Current** | Weeks-months; experimental or implementation state | `{{CURRENT_EXAMPLE}}` | New experimental data |
| **Live** | Hours-days; real-time state | (typically N/A for research projects) | N/A |

**Smṛti acceleration rule:** Literature-based claims with `[ES-SMRTI]` tag → TTL shifts 1 class faster than structural equivalent. Example: experimental result from paper → `Current` (not `Historical`).

---

## 5. Tier Applicability Summary `[GENERIC]`

| Mechanism | Tier | {{PROJECT_NAME}} Applicability | Implementation |
|-----------|------|------------------------------|----------------|
| CCL (Confidence Calibration) | 1 | FULL | S16-S20 in `01_early_warning.md` §1.4 |
| FSR (Falsifier Strength Rubric) | 1 | FULL | FSR section in `04_analysis.md` |
| ES Tags (Epistemic Source) | 1 | FULL | `label_system.md` §1.4 + per-component |
| TTL_CLASS | 2 | SELECTIVE | Column in `00_top_risk_record.md` + new claim fields |
| Vyāpti Registry | 2 | SELECTIVE | `vyapti_registry.md` |
| Stakes Assessment | 2 | SELECTIVE | `stakes_assessment.md` |
| TIP (Tagger Independence) | 1→2 | ADAPTED | §3 of this file (human-enforced) |

---

## 6. Integrated Pipeline Flow `[GENERIC]`

```
New claim / component
        |
        v
[ES Tag assignment] ← §2 of this file
        |
        v
[Stakes Assessment] ← stakes_assessment.md
        |
        +--> CRITICAL/HIGH → Full pipeline (01→06) + human TIP-1
        +--> MEDIUM → 03 + 05 minimum
        +--> LOW → 01 scan only
        |
        v
01_early_warning (all signals + S16-S20 CCL)
        |
        v
02_detection → ES tag confirmed
        |
        v
03_sot_traceability → Vyāpti Registry cross-check
        |
        v
04_analysis (5-Whys + FSR rubric for counterarguments)
        |
        v
05_scoring → H score
        |
        v
label_system → [AH-XXX] [RS-XXX] [ES-XXX] labels
        |
        v
06_solution → resolution
        |
        v
00_top_risk_record → TTL_CLASS tracking
```

---

## 7. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Root cause — does pipeline lack epistemic independence? | ?/5 | `[CALIBRATE]` |
| R2 | Feasibility — are all mechanisms applicable? | ?/5 | `[CALIBRATE]` |
| R3 | Verification — do changes address root cause? | ?/5 | `[CALIBRATE]` |
| **Aggregate** | | **?/5** `[PASS/FAIL]` (threshold ≥ 4/5) | |

---

---

## §6 — Post-Installation Verification Checklist `[GENERIC — run as measurements, not declarations]`

> These checks must be run as **filesystem measurements** before declaring AHP ACTIVE. Added to template 2026-06-13 per MACH-RE audit findings AF-1/AF-3/AF-4.

| # | Check | Method | Pass condition |
|---|-------|--------|----------------|
| 12 | File count matches inventory | `ls <ahp_folder>/*.md \| wc -l` | Count = expected (record output) |
| 13 | All internal SOTs are git-tracked | `git ls-files --error-unmatch <SOT-path>` for each SOT | Exit 0 for all SOTs — no `??` status |
| 14 | Authorizing plan closed | Read plan header `**Status:**` field | Must read "EXECUTED…" not "AWAITING" |
| 15 | No lingering working-tree SOT changes | `git diff --name-only` + `git status --short` for SOT paths | No unstaged SOT modifications |

**Rule:** Only after all 4 checks PASS by measurement (with recorded output) → declare ACTIVE in `index.md`.

---

*Epistemic Integration Spec — Layer mapping, ES Tags, TIP, TTL_CLASS, Pipeline Flow. §6 Post-Installation Verification added 2026-06-13. Exported from AHP v3.1. Calibrate all claim types, TTL examples, and layer names for {{PROJECT_NAME}}.*

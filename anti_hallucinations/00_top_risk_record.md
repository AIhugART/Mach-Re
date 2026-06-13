Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-13 -->
<!-- Correction note: File was missing from 2026-06-12 installation (AF-1, audit 2026-06-13). Created 2026-06-13. -->

# 00 — Top Risk Record
## MACH-RE — Highest-Risk Components

**Version:** v1.0 (2026-06-13)
**Scope:** All layers of system A·B·C mapped to MACH RE axioms; 10 TRITHUC gaps tracked; 4 audit findings (AF-1→AF-4) from 2026-06-13 audit
**Compass:** Buddhist Epistemology (Pratyakṣa / Anumāna / Smṛti / Vikalpa)
**Re-audit cadence:** [RS-CRIT] weekly | [RS-HIGH] every 2 weeks | [RS-MED] monthly | [RS-LOW] quarterly
**Risk Score formula:** H × W × (1+A)
  - H = Hallucination score (0-10, per `05_scoring.md`)
  - W = Weighting factor (1=documentation, 2=framework/mapping, 3=public claim/system-level definition)
  - A = Amplifier (0.0=stable, 0.5=active development, 1.0=blocking/public-facing)
**TTL_CLASS:** Atemporal | Geological (years) | Historical (months) | Current (weeks)
**Confirmation SOT:** `labels.md` — #1 Human confirmed · #2 AI hallucination · #3 No authority to judge

---

## Table 1 — Audit Findings & TRITHUC Gaps (ranked by Risk Score)

| Rank | Component ID | Name | System | H | W | A | Risk Score | TTL_CLASS | Primary Label | Confirmation | Notes |
|------|-------------|------|--------|---|---|---|-----------|-----------|--------------|--------------|-------|
| 1 | `AF-1` | Self-certified ACTIVE status (00_top_risk_record.md missing) | AHP/meta | 9 | 3 | 1.0 | **54.0** [RS-CRIT] | Current | `[AH-CRIT][RS-CRIT][ES-VIKALP]` | `[AH-AIHL]` labels.md #2 | Self-audit declared PASS without filesystem measurement. File #2 dropped from phase decomposition. S17+S18. Fixed: 2026-06-13 Phase A. |
| 2 | `AF-2` | §AHP deleted from CLAUDE.md working tree (accident) | CLAUDE.md | 7 | 3 | 0.5 | **31.5** [RS-CRIT] | Current | `[AH-HIGH][RS-CRIT][ES-VIKALP]` | `[AH-HCNF]` labels.md #1 | 28 dòng xóa chưa commit; pipeline silently inert. Human confirmed accident (Q1, 2026-06-13). Fixed: Phase C. |
| 3 | `AF-3` | SOT-8 (Compass C) untracked in git | SOT/git | 7 | 3 | 0.5 | **31.5** [RS-CRIT] | Current | `[AH-HIGH][RS-CRIT][ES-VIKALP]` | — | `documents/C_SYSTEM_Buddhist_Epistemology/` untracked. TTL tracking meaningless without VCS. Fixed: Phase D. |
| 4 | `TRITHUC-1` | V ⊥ H Orthogonal Temporality | MR/III | 3 | 3 | 0.5 | **13.5** [RS-MED] | Current | `[AH-WARN][RS-MED][ES-ANUMA]` | — | Strong RCA. `[proposed-by-this-project]` + `[corroborated: Japan/Nakane 1970 + Ubuntu/Mbiti 1969]`. Strong partial-close 2026-06-13: 3 convergent cases (Vietnam+Japan+Ubuntu), Mbiti sasa/zamani ontological, C-system negative evidence. `TRITHUC-1_ubuntu_verification.md`. Re-audit: monthly. |
| 5 | `TRITHUC-2` | C1-Graded Reflexivity (full/min/zero) | MR/VI | 6 | 3 | 0.5 | **27.0** [RS-CRIT] | Current | `[AH-WARN][RS-CRIT][ES-VIKALP]` | — | Strong RCA. `[proposed-by-this-project]`. Requires dyadic case study formalization. |
| 6 | `TRITHUC-5` | V as Ontological Dimension | MR/III | 6 | 3 | 0.5 | **27.0** [RS-CRIT] | Current | `[AH-WARN][RS-CRIT][ES-VIKALP]` | — | Medium RCA. BRIDGE-II-III required (SOT-K). A=Gap, B=Weak. |
| 7 | `TRITHUC-4` | F-AND-Gate (3-condition identity failure) | MR/Mệnh Đề 4 | 5 | 2 | 0.5 | **15.0** [RS-HIGH] | Current | `[AH-WARN][RS-HIGH][ES-VIKALP]` | — | Medium RCA. Derived from II+III+IV; validation requires historical identity failure cases. |
| 8 | `AF-4` | Plan 2026-06-12 still "AWAITING APPROVAL" post-execution | Records | 4 | 2 | 0.0 | **8.0** [RS-MED] | Current | `[AH-LOW][RS-MED][ES-VIKALP]` | — | Trace integrity gap. Approval not ghi nhận trong repo. Fixed: Phase B. |
| 9 | `TRITHUC-3` | Formal Structural Boundary (B vs C category gap) | MR/IV | 4 | 2 | 0.0 | **8.0** [RS-MED] | Historical | `[AH-LOW][RS-MED][ES-ANUMA]` | — | Medium RCA. Category boundary acknowledged (NAC_001). C's non-attachment ≠ IV structural boundary. No force-map needed. |
| 10 | `TRITHUC-8` | Design-as-Selection (Ashby Ch.12–13) | B/unique | 3 | 2 | 0.0 | **6.0** [RS-MED] | Geological | `[AH-OK][RS-MED][ES-PRATY]` | — | Weak RCA. B-unique (NAC_003). Analogue for IV + V. Do not force-map. |
| 11 | `TRITHUC-7` | Yogipratyakṣa (Limit-Case Faculty) | C/unique | 3 | 1 | 0.0 | **3.0** [RS-LOW] | Geological | `[AH-OK][RS-LOW][ES-PRATY]` | — | Weak RCA. C-unique (NAC_002). A/B sufficient without. No force-map. |
| 12 | `TRITHUC-9` | Anupalabdhi (Absence Cognition) | C/unique | 3 | 1 | 0.0 | **3.0** [RS-LOW] | Geological | `[AH-OK][RS-LOW][ES-PRATY]` | — | Weak RCA. C-unique (NAC_004). Potential enrichment for IV-A07 diagnostic. |
| 13 | `TRITHUC-10` | Folk Epistemology as Convergent Discovery | A/unique | 3 | 1 | 0.0 | **3.0** [RS-LOW] | Historical | `[AH-OK][RS-LOW][ES-SMRTI]` | — | Weak RCA. A-unique (NAC_005). Convergent discovery per `axiom_spec.md §0.0`. |
| 14 | `TRITHUC-6` | Institutional Design Layer (Phan Ngọc Phần 3) | Register | 2 | 1 | 0.0 | **2.0** [RS-LOW] | Historical | `[AH-OK][RS-LOW][ES-ANUMA]` | — | Weak RCA. Scope excluded per `axiom_spec.md §0.1.1`. Register mismatch, not gap to fill. |

> **Mapping risk note:** Cross-system mapping links with `mapping_type = ANALOGY` promoted toward `STRUCTURAL` without new justification are the highest latent risk in MACH RE. Signal R4 (equivalence without justification). NAC entries (5) guard against forced mapping — see Table 2.

---

## Table 2 — Cross-System Mapping Components (highest-risk MAP_ links)

Tracked separately per Shared Component Rule. Full registry: `mapping_registry.md`.

| Rank | Mapping ID | Source Node | Target Node | mapping_type | H | Risk Score | Label | Justification status |
|------|-----------|------------|------------|--------------|---|-----------|-------|---------------------|
| 1 | `MAP_IV_003` | IV-boundary (AW/B) | vô chấp ethical (BE/C) | ANALOGY | 6 | 18.0 [RS-HIGH] | `[AH-WARN][ES-ANUMA]` | NAC_001 — category boundary acknowledged; TRITHUC-3 |
| 2 | `MAP_III_001` | Thờ cúng tổ tiên (PN/A) | Kṣaṇabhaṅgavāda (BE/C) | ANALOGY | 5 | 15.0 [RS-HIGH] | `[AH-WARN][ES-ANUMA]` | TRITHUC-1 open — full justification needed |
| 3 | `MAP_V_001` | Svasaṃvedana (BE/C) | Meta-loop Mạch Rễ (MR) | ANALOGY | 5 | 12.5 [RS-MED] | `[AH-WARN][ES-ANUMA]` | Tiên Đề V structural claim — Anumāna chain needed |

> **Note:** Remaining 23 MAP_ links assessed at H ≤ 4. Full audit of all 26 links = RCA summary §7 next-step P2 (hạn 2026-06-26).

---

## Risk Score Formula (MACH RE calibration)

```
Risk Score = H × W × (1 + A)

W calibration for MACH-RE:
  1 = documentation / operational note
  2 = framework component / mapping link
  3 = public claim / system-level definition / SOT-level

A calibration:
  0.0 = stable, not actively developed
  0.5 = under active development or open TRITHUC gap
  1.0 = blocking gate or pipeline integrity issue

RS bands:
  [RS-CRIT] >= 20  → weekly re-audit
  [RS-HIGH] 15-19.9 → bi-weekly re-audit
  [RS-MED]  8-14.9  → monthly re-audit
  [RS-LOW]  < 8    → quarterly re-audit
```

---

## TTL_CLASS (MACH RE calibration)

| TTL_CLASS | MACH RE meaning | Re-verify trigger |
|-----------|----------------|------------------|
| Atemporal | Frozen axiom: AX_I–AX_IV core, triangulation 3.0/3 `[established]` | Architecture revision only |
| Geological | Stable literature claim: N_PN_, N_AW_, N_BE_ core nodes | Annual (relevant literature update) |
| Historical | Derived proposition / heuristic / mapping link | 6-month cycle or new compass evidence |
| Current | TRITHUC gap / audit finding / `[proposed-by-this-project]` open item | Weekly–monthly (new research cycle) |

---

## Shared Component Rule

A component appearing in both Table 1 and Table 2 must be tracked in BOTH with consistent scores. If scores diverge, use the **higher** score. Example: `MAP_IV_003` / `TRITHUC-3` — Table 1 H=4 RS=8, Table 2 H=6 RS=18 → use 18 [RS-HIGH].

---

## Re-audit Schedule

| Next re-audit | Scope | Trigger |
|--------------|-------|---------|
| 2026-06-20 | AF-1→AF-4 — verify fixes applied (Phase A–E complete) | Weekly [RS-CRIT] |
| 2026-06-26 | All 26 MAP_ links — audit mapping_type (RCA summary §7 P2) | Scheduled |
| 2026-07-13 | TRITHUC-1 — monthly [RS-MED] strong partial-close; Path B progress (formal derivation I+II→V⊥H) | Monthly [RS-MED] |
| 2026-07-13 | TRITHUC-2, TRITHUC-5 — open CRIT gaps | Bi-weekly [RS-CRIT] |
| 2026-09-13 | Full TRITHUC quarterly re-audit (all 10 gaps) | Quarterly |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-06-13 | Initial instantiation — MACH-RE. File missing from 2026-06-12 installation (AF-1, audit plan `plan/2026-06-13_plan_ahp_audit.md`). 14 entries: 4 audit findings + 10 TRITHUC gaps. labels.md = canonical confirmation SOT. |
| v1.1 | 2026-06-13 | TRITHUC-1 partial-close: Japan/Nakane 1970 cross-cultural verification. H 6→4, RS 27.0→18.0 [RS-CRIT→RS-HIGH], ES-VIKALP→ES-ANUMA. Operational V⊥H confirmed both directions. See `documents/gap/TRITHUC-1_japan_verification.md`. Re-audit: weekly → bi-weekly. |
| v1.2 | 2026-06-13 | TRITHUC-1 strong partial-close: Ubuntu/Mbiti 1969 + ABC triangulation (3-round RCA × scoring gate 6/6=5.0/5). H 4→3, RS 18.0→13.5 [RS-HIGH→RS-MED]. 3 convergent cases (Vietnam+Japan+Ubuntu). Mbiti sasa/zamani = ontological-level claim; C-system negative evidence. Path A substantially met. See `documents/gap/TRITHUC-1_ubuntu_verification.md`. Re-audit: bi-weekly → monthly. |

---

*Top Risk Record v1.0 — MACH-RE. Risk Score H×W×(1+A). 14 entries ranked. Compass: Buddhist Epistemology. Instantiated from AHP Template v1.0 (2026-06-13, per audit AF-1). `labels.md` = canonical confirmation SOT.*

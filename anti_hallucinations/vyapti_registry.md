Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# Vyāpti Registry — MACH-RE Claim Type Reliability

**Role:** Pre-computed reliability priors for each claim type in MACH RE. Used by `03_sot_traceability.md` for Vyāpti cross-check and `label_system.md` for default ES tag.

**Vyāpti (pervasion):** Invariant relation between claim type and epistemic reliability — just as smoke pervades fire in Buddhist logic, certain claim structures pervade certain reliability levels.

---

## VYR Summary

| VYR | Claim Type | ES Tag | Reliability | TTL_CLASS | Re-verify |
|-----|-----------|--------|-------------|-----------|-----------|
| VYR-1 | Core axiom, 3.0/3 triangulation | `[ES-PRATY]` | HIGH | Atemporal | Architecture revision |
| VYR-2 | Core axiom, 1.5–2.5/3 triangulation | `[ES-ANUMA]` | HIGH | Geological | Compass revision |
| VYR-3 | Derived proposition | `[ES-ANUMA]` | HIGH | Geological | Dependency axiom change |
| VYR-4 | Heuristic (DSH) | `[ES-ANUMA]` | MEDIUM | Historical | New cross-cultural data |
| VYR-5 | TRITHUC gap (unresolved) | `[ES-VIKALP]` | LOW | Current | Quarterly |
| VYR-6 | Cross-system mapping link | `[ES-ANUMA]` + boundary | MEDIUM | Historical | System revision |
| VYR-7 | NAC entry | `[ES-PRATY]` (home) | HIGH | Atemporal | New analogue found |
| VYR-8 | `[proposed-by-this-project]` | `[ES-ANUMA]` | LOW | Current | External validation |
| VYR-9 | Vietnamese folk evidence | `[ES-SMRTI]` | MEDIUM | Historical | Scholarly reinterpretation |

---

## Detailed VYR Entries

### VYR-1 — Core Axiom with 3.0/3 Triangulation

- **Detection:** Keywords "identity is constituted", "relational pattern", triangulation 3.0/3
- **Node pattern:** `AX_I` (only I has 3.0/3)
- **ES tag:** `[ES-PRATY]` — direct anchor ≥ 3 compass systems, published sources
- **Reliability:** HIGH | **TTL:** Atemporal
- **Example:** `AX_I`: "Identity of a collective system is constituted by relations"
- **RCA:** 5.0/5 — verified against N_PN_00010, N_AW_WEI_00001, N_BE_00066

### VYR-2 — Core Axiom with 1.5–2.5/3 Triangulation

- **Detection:** Keywords "invariant", "structural pattern", triangulation ~2.5/3, "A-weak" or "C-cond"
- **Node pattern:** `AX_II`, `AX_III`, `AX_IV`
- **ES tag:** `[ES-ANUMA]` — valid structural inference from Pratyakṣa-grounded claims
- **Reliability:** HIGH | **TTL:** Geological
- **Example:** `AX_II`: "What persists through content change is an invariant pattern of relations"
- **RCA:** 4.8/5 — C-evidence conditional (pattern = saṃvṛtisat)

### VYR-3 — Derived Proposition

- **Detection:** Keywords "derived from", "suy từ", explicit depends_on chain
- **Node pattern:** `AX_P1`–`AX_P4`
- **ES tag:** `[ES-ANUMA]` — logically entailed; derivation chain explicit in `axiom_spec.md` §1
- **Reliability:** HIGH | **TTL:** Geological
- **Example:** `AX_P2`: "Perturbation → growth" derived from II+III+IV
- **RCA:** 4.8/5 — valid derivation; dependent on stability of II, III, IV

### VYR-4 — Heuristic (DSH)

- **Detection:** Keywords "heuristic", "empirical hypothesis", "useful tool", "not universal truth"
- **Node pattern:** `AX_DSH`
- **ES tag:** `[ES-ANUMA]` + TTL=Historical
- **Reliability:** MEDIUM | **TTL:** Historical
- **Example:** `DSH-2`: "Elements closer to invariant pattern are filtered more strictly"
- **RCA:** 4.6/5 — advisory triangulation 2.0/3; single-anchor permitted for heuristic

### VYR-5 — TRITHUC Gap (Unresolved)

- **Detection:** Keywords "🔓 Open", "gap type:", "proposed-by-this-project", "TRITHUC-"
- **Node pattern:** TRITHUC-1 through TRITHUC-10
- **ES tag:** `[ES-VIKALP]` pending resolution — unanchored by definition
- **Reliability:** LOW | **TTL:** Current (quarterly re-verify)
- **Example:** TRITHUC-1: V ⊥ H orthogonality — `[proposed-by-this-project]`

### VYR-6 — Cross-System Mapping Link

- **Detection:** Keywords "↔", "mapping_type", "ANALOGY", "STRUCTURAL", cross-system node codes
- **Node pattern:** `MAP_*` in `mapping_registry.md`
- **ES tag:** `[ES-ANUMA]` + boundary: "Interpretive — not equivalence"
- **Reliability:** MEDIUM | **TTL:** Historical
- **Example:** MAP_III_001: N_PN_00041 ↔ AX_III — ANALOGY
- **RCA:** 4.6/5 — all mapping rows RCA-gated; registry is derivative

### VYR-7 — NAC Entry

- **Detection:** Keywords "no analogue", "NAC_", "do not force-map", "C-unique", "B-unique"
- **Node pattern:** `NAC_*` in `mapping_registry.md`
- **ES tag:** `[ES-PRATY]` for concept IN HOME SYSTEM; NAC classification = `[interpretation]`
- **Reliability:** HIGH (home) | **TTL:** Atemporal
- **Example:** NAC_003: Design-as-Selection — B-unique (Ashby Ch.12-13)
- **RCA:** 4.8/5 — classification correct; falsifiable if new analogue found

### VYR-8 — `[proposed-by-this-project]` Claim

- **Detection:** Keywords "proposed-by-this-project", "MACH RE coinage", "novel contribution"
- **Node pattern:** Elements tagged `[proposed-by-this-project]` in mapping
- **ES tag:** `[ES-ANUMA]` — derived within framework, not externally verified
- **Reliability:** LOW | **TTL:** Current
- **Example:** III-orthogonality (V ⊥ H): partially supported by all three, fully captured by none
- **RCA:** 4.8/5 — correctly tagged; claim not scored here, only classification accuracy

### VYR-9 — Vietnamese Folk Evidence

- **Detection:** Keywords "ca dao", "tục ngữ", "thờ cúng tổ tiên", "dân gian", "vô danh"
- **Node pattern:** Evidence rows referencing Q1, Q2, Q3 corpus
- **ES tag:** `[ES-SMRTI]` — folk epistemology, oral tradition, not formal scholarship
- **Reliability:** MEDIUM | **TTL:** Historical (Smṛti acceleration rule applies)
- **Example:** Ca dao "Cây có cội sông có nguồn" — Q2 line 8930
- **RCA:** 4.6/5 — valid inductive support, not formal proof

---

## Vyāpti Cross-Check Protocol

When `03_sot_traceability.md` flags a component:
1. Identify claim type → map to VYR entry
2. Compare actual ES tag vs VYR default → mismatch = O5 signal
3. Check TTL_CLASS → expired = O4 signal
4. If reliability = LOW and presented as HIGH-confidence → S18 signal

---

*Vyāpti Registry v1.0 — 9 VYR entries. Instantiated from AHP Template v1.0 (2026-06-12).*

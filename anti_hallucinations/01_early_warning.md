Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

<!-- Instantiated from: AHP Template v1.0 (2026-06-12) | Project: MACH-RE | Date: 2026-06-12 -->

# 01 — Early Warning Signal Registry
## MACH-RE — 20 Signals (R1-R5, O1-O5, Y1-Y5, S16-S20)

**Role:** First line of hallucination detection. 20 standardized signals flag suspicious claims before RCA.
**Input:** Any new claim, term, or cross-system mapping.
**Output:** Signal match (RED/ORANGE/YELLOW) + severity → trigger `02_detection.md`.

---

## RED (R1-R5) — Hallucination Indicators

| Signal | Name | Trigger | MACH RE Example | Severity |
|--------|------|---------|----------------|----------|
| **R1** | Category Error | Epistemology as physics, metaphor as mechanism, model as object | "MACH RE solves Quantum Measurement" — epistemology ≠ physics | 🔴 CRITICAL |
| **R2** | Absolute Claim | "proves", "revolutionary", "overturns" without formal proof | "MACH RE proves Vietnamese culture is relational" — violates conservative form | 🔴 CRITICAL |
| **R3** | Self-Scored Without Rubric | "RCA score X.X/5" without 5-criterion breakdown | Score stated without criterion table — violates scoring gate transparency | 🔴 CRITICAL |
| **R4** | Equivalence Without Justification | Cross-system identity claim without mapping_type | "Phan Ngọc's kiểu lựa chọn IS Ashby's invariant" — should be ANALOGY | 🔴 CRITICAL |
| **R5** | Untagged Provenance | Typology/history claim without `[established]`/`[proposed-by-this-project]` | "Triết học Tương quan-Phân tán is established" — F9 pattern: AI coinage as established | 🔴 CRITICAL |

## ORANGE (O1-O5) — Warning Indicators

| Signal | Name | Trigger | MACH RE Example | Severity |
|--------|------|---------|----------------|----------|
| **O1** | Triangulation < 1.5/3 as Strong | "Well-supported" when triangulation below threshold | "V ⊥ H strongly supported by all compasses" — actual: 1.5/3 for orthogonality | 🟠 HIGH |
| **O2** | Gap Cited as Resolved | TRITHUC "🔓 Open" treated as settled in prose | "The boundary problem is addressed" — TRITHUC-3 still Open, no resolution date | 🟠 HIGH |
| **O3** | Forced Mapping (NAC) | NAC concept mapped cross-system without justification | "Anupalabdhi ≈ Black Box inaccessible states" — NAC_004 exists | 🟠 HIGH |
| **O4** | TTL Decay Ignored | Pre-2000 source treated as Current | Ashby (1956) as "current consensus" without noting 70-year age | 🟠 HIGH |
| **O5** | ES Tag Mismatch | `[ES-VIKALP]` with `[ES-PRATY]` language confidence | "Directly established" for Vikalpa-tagged claim | 🟠 HIGH |

## YELLOW (Y1-Y5) — Caution

| Signal | Name | Trigger | MACH RE Example | Severity |
|--------|------|---------|----------------|----------|
| **Y1** | Single-Anchor Overclaim | One-compass support called "convergent" | Only Phan Ngọc supports pattern but called "cross-system convergence" | 🟡 MEDIUM |
| **Y2** | DSH Outside Scope | DSH-3 weights applied to non-Vietnamese system | Yoruba structural distance estimated without re-measurement | 🟡 MEDIUM |
| **Y3** | Mệnh Đề as Tiên Đề | Derived proposition as independent axiom | "Distributed Identity is foundational" — derived from I+II | 🟡 MEDIUM |
| **Y4** | Ghi Chú as Formal Claim | Operational note quoted as axiom statement | "Khiêm nhường như cơ chế" note quoted as Tiên Đề I | 🟡 MEDIUM |
| **Y5** | Bilingual Term as Formal | Thuần Việt in English formal claim without EN | "Nếp bản sắc is the invariant" without EN equivalent | 🟡 MEDIUM |

## CCL (S16-S20) — Confidence Calibration

| Signal | Name | Trigger | MACH RE Example | Severity |
|--------|------|---------|----------------|----------|
| **S16** | No SOT Trace | Claim without citation table in new document | New paper section without Bảng Nguồn Trích Dẫn | 🔴 CRITICAL |
| **S17** | Model Self-Evaluates | AI RCA score without TIP-1 | AI: "RCA 5.0/5" in same session as claim generation | 🔴 CRITICAL |
| **S18** | Vikalpa as Pratyakṣa | AI text with linguistic confidence, zero SOT | "It is well-established that..." for `[proposed-by-this-project]` claim | 🔴 CRITICAL |
| **S19** | Bootstrapping | Claim A → Claim B, same AI session | "X supported by Y" where both generated this session | 🔴 CRITICAL |
| **S20** | TIP Violation | AI-generated as authority for AI-generated | Circular self-certification, no human TIP-1 | 🔴 CRITICAL |

## Signal Response

| Level | Response |
|-------|----------|
| 🔴 RED (R1-R5, S16-S20) | Full pipeline + mandatory TIP-1. BLOCKING if R1/R2/S18/S20. |
| 🟠 ORANGE (O1-O5) | Full pipeline. Re-audit within 2 weeks. |
| 🟡 YELLOW (Y1-Y5) | Flag. Re-audit monthly. |

---

*01_early_warning.md v1.0 — 20 signals (5+5+5+5). Instantiated from AHP Template v1.0 (2026-06-12).*

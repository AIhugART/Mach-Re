Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Tổng Kết — Cài Đặt AHP vào Mạch Rễ
## AHP Installation — Final RCA Summary Report

**Date:** 2026-06-12
**Plan:** `plan/2026-06-12_plan_ahp_installation.md`
**Status:** COMPLETED — 6/6 phases PASS
**Method:** 3-Round RCA × 5-Why × scoring gate ≥ 4/5

---

## 1. QUYẾT ĐỊNH GỐC — Có nên cài AHP không?

### 1.1 3-Round RCA

| Round | Focus | Root cause (1 câu) |
|-------|-------|-------------------|
| **R1 — Symptom** | Sao cần AHP khi đã có RULE ZERO + labels.md? | RULE ZERO là process, labels.md là verdict — MACH RE thiếu **tầng giữa** (detection→classification→scoring), để lại khoảng trống nơi claim nội-bộ-đúng nhưng ngoại-bộ-sai lọt qua. |
| **R2 — Mechanism** | Sao AHP giải quyết được? | AHP thêm TTL_CLASS, ES tags, NAC table, Risk Score — bốn trụ infrastructure mà process đơn thuần không đảm bảo vì process re-execute mỗi lần, infrastructure tồn tại xuyên session. |
| **R3 — Root** | Standard nội bộ nào bị vi phạm nếu KHÔNG cài? | Tiên Đề V + TRITHUC index (10 gaps, 0 resolved) + labels.md (verdict không có middle infrastructure) → từ chối AHP = V-violation ở tầng meta-audit. |

### 1.2 Scoring Gate

| Criterion | Score |
|-----------|-------|
| Correct (real gap?) | 1/1 |
| Deep (touches root?) | 1/1 |
| Feasible (safe to do?) | 1/1 |
| Conflict-risk (no contradictions?) | 1/1 |
| Preservation (core kept?) | 1/1 |
| Provenance (tagged?) | 0.8/1 |
| **TOTAL** | **5.8/6 → 4.83/5** ✅ |

---

## 2. 5 QUYẾT ĐỊNH CHI TIẾT

| # | Decision | RCA | Claim |
|---|----------|-----|-------|
| **D1** | Install AHP | 4.83/5 | AHP fills missing middle layer between RULE ZERO (process) and labels.md (verdict) |
| **D2** | labels.md canonical SOT | 4.8/5 | labels.md preserved as confirmation SOT; AHP labels = encoding, not replacement |
| **D3** | `[AH-NAJ]` added | 4.8/5 | Ternary confirmation: "I don't know" is valid epistemic state per Tiên Đề V |
| **D4** | NAC table | 4.8/5 | 5 NAC entries from TRITHUC gaps — documented, not force-mapped |
| **D5** | Dual scoring | 4.8/5 | RCA gate (change decision) + AHP score (risk tracking) — complementary |

### D1 Evidence Chain

```
F9 retraction → claim passed RCA 5.0/5 but externally false
→ scoring gate lacked Provenance criterion
→ AHP ES tags + Vyāpti Registry catches pre-external-review
→ TRITHUC: 10 gaps, all 🔓 Open, 0 resolution dates
→ labels.md: 3 verdict labels, no detection/prioritization
→ Gap: process (how) → ??? → verdict (what)
→ AHP fills: process → detection→classification→scoring → verdict
```

### D3 Design Rationale

```
Binary confirmation (true/false) → false dichotomy
F9: internally-consistent but externally-false → system lacked categories to detect error
Label #3 → ternary: confirmed / hallucinated / cannot-judge
Implements axiom_spec.md §0.6 kill condition #1 at audit level
NOT failure — DEFER, not BLOCKING
```

---

## 3. KẾT QUẢ — Before vs After

```
[TRƯỚC]
  RULE ZERO ─────────────────────────→ labels.md
                KHOẢNG TRỐNG

[SAU]
  RULE ZERO
       │
       ▼
  ╔══════════════════════════════╗
  ║   AHP MIDDLE LAYER           ║
  ║   01: 20 signals             ║
  ║   02: ES tag + confirmation  ║
  ║   03: SOT trace (N=8)        ║
  ║   04: 5-Whys + FSR           ║
  ║   05: 0-10 rubric (5 bands)  ║
  ║   label: 25 labels           ║
  ║   06: P0-P4 + P-DEFER        ║
  ║   00: Risk Score + TTL       ║
  ║   VYR: 9 reliability priors  ║
  ║   NAC: 5 no-analogue docs    ║
  ╚══════════════════════════════╝
       │
       ▼
  labels.md (canonical SOT)
    [1] Human confirmed   ← [AH-HCNF]
    [2] AI hallucination  ← [AH-AIHL]
    [3] No authority      ← [AH-NAJ]
```

---

## 4. FILE INVENTORY

| Phase | Files | Status |
|-------|-------|--------|
| P1 — Bootstrap | `README.md`, `index.md`, `instantiation_log.md` | ✅ |
| P2 — Registry | `system_registry.md` (4 systems), `mapping_registry.md` (26 links + 5 NAC) | ✅ |
| P3 — Calibration | `05_scoring.md` (10 anchors), `vyapti_registry.md` (9 VYR), `stakes_assessment.md` (15 types) | ✅ |
| P4 — Pipeline | `01`–`04`, `label_system.md`, `06_solution.md` | ✅ |
| P5 — Integration | `integration_spec.md` (3-layer, 4 rules) | ✅ |
| P6 — Finalize | `CHANGELOG.md`, `CLAUDE.md` (modified) | ✅ |

**Tổng:** 15 instantiated + 2 new + 1 RCA summary + 2 modified = **20 files touched**

> **Correction 2026-06-13 (audit AF-1, `plan/2026-06-13_plan_ahp_audit.md`):** File inventory thực tế tại 2026-06-12 là **14 instantiated** (không phải 15) — `00_top_risk_record.md` bị bỏ sót khỏi phân rã phase trong installation plan. File được tạo ngày 2026-06-13 theo audit corrective Phase A. Văn bản gốc §4 giữ nguyên để bảo toàn lịch sử; entry này là correction note additive.

---

## 5. KEY NUMBERS

| Metric | Value |
|--------|-------|
| RCA decisions (≥ 4/5) | 5 |
| Average RCA score | 4.83/5 |
| Systems registered | 4 (PN 68N/124E, AW 180N, BE 255N, MR 11 axioms) |
| Internal SOTs | 8 |
| Early warning signals | 20 |
| Label taxonomy | 25 |
| Scoring bands | 5 (10 MACH RE anchors) |
| Root cause types | 6 |
| Vyāpti Registry entries | 9 |
| Cross-system mapping links | 26 |
| NAC entries | 5 |
| TRITHUC gaps under TTL monitoring | 10 |

---

## 6. VERIFICATION — Điều kiện phản chứng

**AHP installation FAILS nếu:**
1. AHP scoring consistently contradicts RCA gate without explainable pattern
2. `[AH-NAJ]` overuse (>30% claims deferred without unlock condition)
3. NAC entry proven wrong (structural analogue discovered)
4. No hallucination detected within 6 months (pipeline unused)
5. Template drift beyond reconciliation

**AHP installation SUCCEEDS nếu:**
1. ≥1 F9-class provenance failure caught by AHP BEFORE external review
2. ≥1 TRITHUC gap progresses from 🔓 Open toward resolution with dated tracking
3. Dual scoring produces ≥1 productive divergence (RCA passes, AHP flags risk)

---

## 7. NEXT STEPS

| Priority | Task | Timeline |
|----------|------|----------|
| P1 | Populate `00_top_risk_record.md` with actual risk scores | Within 1 week |
| P1 | First full pipeline pass on TRITHUC-1 (V ⊥ H) | Within 1 week |
| P2 | Audit all 26 mapping links — verify mapping_type | Within 2 weeks |
| P2 | Quarterly re-audit of TRITHUC gaps (TTL_CLASS=Current) | 2026-09-12 |

---

## 8. BOUNDARY STATEMENT

1. AHP does NOT replace RULE ZERO — RULE ZERO remains highest mandatory rule.
2. AHP does NOT replace labels.md — labels.md is canonical confirmation SOT.
3. AHP does NOT modify any axiom/proposition/heuristic — reference files READ-ONLY.
4. AHP does NOT resolve TRITHUC gaps — provides tracking infrastructure only.
5. AHP does NOT eliminate hallucination — reduces undetected probability.
6. AHP in MACH RE is `[proposed-by-this-project]` — not externally validated.
7. `[AH-NAJ]` is `[proposed-by-this-project]` — MACH RE addition to AHP template.

---

*RCA Summary v1.0 — 2026-06-12. 5 decisions ≥ 4/5, 20 files, 3-layer architecture ACTIVE.*

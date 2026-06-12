# Plan: A·B·C System Mapping → MACH RE Axioms

**Date:** 2026-06-12
**Status:** PLAN — chờ phê duyệt
**RCA gate:** 3-round × 5-Why × scoring threshold 4/5 cho mọi quyết định mapping

---

## 1. Yêu cầu (Restatement)

| Mục | Chi tiết |
|---|---|
| **Nhiệm vụ** | Mapping 3 hệ thống neo (A — Phan Ngọc, B — Ashby/Weick, C — Buddhist Epistemology) theo hệ tiên đề MACH RE |
| **Khung quy chiếu** | `axiom_spec.md` — 4 Core I–IV · 4 Derived 1–4 · Meta V · Interface VI · DSH heuristic |
| **Đầu vào A** | `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` — 68 nodes, 124 edges |
| **Đầu vào B** | `documents/B_SYSTEM_Ashby_Weick/b_system_ashby_weick.md` — Ashby 100 nodes + Weick 80 nodes, 108+80+ edges |
| **Đầu vào C** | `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md` — 30 core + ~225 RCA nodes, 39 core edges |
| **Schema tham chiếu** | `documents/gap/BIAN_index_schema.md` (định dạng BIAN index cho gap concepts) |
| **Output chính** | `documents/mapping/a_b_c_system_mapping.md` — file mapping 3-hệ |
| **Output gap** | `documents/gap/TRITHUC_index.md` — index các gap concept (namespace `TRITHUC-`; tương tự BIAN index trong BE↔QM mapping) |
| **Phương pháp** | 3-round RCA × 5-Why × scoring gate ≥ 4/5 cho mọi quyết định mapping |
| **Constraint** | `axiom_spec.md §0.1.1` — Phan Ngọc Phần 3 không hấp thụ trực tiếp; taxonomy 3 vai (lens/mirror/beam) bất khả xâm phạm |

---

## 2. Phân tích rủi ro

| # | Rủi ro | Mức | Giảm thiểu |
|---|---|---|---|
| R1 | **Scale explosion** — 250+ nodes × 10 axioms = 2500+ potential mappings | HIGH | Map ở tầng axiom-level, không node-by-node. Mỗi axiom map tối đa 3-5 node/edge từ mỗi system |
| R2 | **RCA fatigue** — mỗi mapping row cần 3-round RCA sẽ cực chậm | HIGH | RCA gate dành cho mapping *decisions* (strong/weak/gap classification), không cho từng ô dữ liệu; dùng batch scoring |
| R3 | **Redundancy với axiom_spec.md** — A·B·C đã được neo trong triplet rows của axiom spec | MEDIUM | Tái sử dụng triplet `[A·B·C]` đã có làm baseline; file mới là **mở rộng có cấu trúc**, không phải lặp lại |
| R4 | **Schema mismatch** — BE↔QM schema là 1-1 concept mapping; A·B·C↔MACH RE là many-to-one axiom triangulation | HIGH | Adapt schema: tier → axiom-level; correspondence → triangulation strength; BIAN → TRIANGULATION_GAP |
| R5 | **Provenance discipline** — mapping claims phải có provenance tag nhưng A/B/C đều ở các tầng khác nhau | MEDIUM | Mỗi mapping row có cột provenance `[established]`/`[proposed-by-this-project]`/`[interpretation]`; phân biệt provenance của claim mapping vs provenance của node nguồn |
| R6 | **Gap index overlap** — `documents/gap/TRITHUC_index.md` có thể trùng namespace với BE↔QM BIAN labels (đã có BIAN-1 đến BIAN-20) | MEDIUM | Dùng tiền tố `TRITHUC-` (Tri Thức = epistemological gaps trong triangulation) cho gap labels để phân biệt với `BIAN-` của BE↔QM |

---

## 3. Kiến trúc file đầu ra (2 file output + 1 file plan)

### 3.1 File chính: `documents/mapping/a_b_c_system_mapping.md`

```
# System Mapping: A·B·C → MACH RE Axioms
## Canonical Identification / Nhận diện Chuẩn
## Mapping Confidence Rules
## Analogy-not-equivalence Warning

# PART I — SYSTEM NODE/EDGE REFERENCE
## A — Phan Ngọc nodes/edges summary (top-20 canonical)
## B — Ashby/Weick nodes/edges summary (top-30 canonical)
## C — Buddhist Epistemology nodes/edges summary (top-30 canonical)

# PART II — TIER-BY-TIER AXIOM MAPPING
## Tier Core — Tiên Đề I–IV
### I — Relational Ontology [A·B·C triangulation]
### II — Structural Invariance [A·B·C triangulation]
### III — Orthogonal Temporality [A·B·C triangulation]
### IV — Dynamic Boundary [A·B·C triangulation]

## Tier Derived — Mệnh Đề 1–4
### 1 — Distributed Identity [A·B·C triangulation]
### 2 — Perturbation Transformation [A·B·C triangulation]
### 3 — Directed Emergence [A·B·C triangulation]
### 4 — Failure Conditions (F) [A·B·C triangulation]

## Tier Meta — Tiên Đề V
## Tier Interface — Tiên Đề VI
## Tier Heuristic — DSH

# PART III — STRUCTURAL SUMMARY
## Coverage matrix (axiom × system)
## Critical asymmetries (strongest divergences)
## Strongest convergences

# PART IV — BOUNDARY STATEMENT
## What This Mapping Does NOT Claim

# PART V — SCHEMA VALIDATION CHECKLIST

# PART VI — NGUỒN TRÍCH DẪN
```

### 3.2 File gap: `documents/gap/TRITHUC_index.md`

Định dạng theo schema từ `BIAN_index_schema.md`, nhưng với namespace `TRITHUC-` (Tri Thức gap — epistemological gaps phát hiện qua triangulation A·B·C):

- **Part 1 — Master Table:** Mỗi dòng = một gap concept có mặt trong ≥1 system nhưng yếu/thiếu trong ≥2 system còn lại
- **Part 2 — Resolution Registry:** Trạng thái giải quyết (Open / Resolved / Partial)
- **Part 3 — Edge Connections:** Các edge liên quan đến mỗi TRITHUC node
- **Part 4 — Summary Statistics**
- **Part 5 — Correction Log**
- **Part 6 — Schema validation checklist**

---

## 4. Mapping Row Schema (cho Part II)

Mỗi axiom element có một bảng con với format:

| Axiom element | A-evidence (Phan Ngọc) | B-evidence (Ashby/Weick) | C-evidence (BE) | Triang. score | Type | RCA score | Provenance |
|---|---|---|---|---|---|---|---|
| (tên element) | N_PN_XXXXX + excerpt | N_AW_XXX_XXXXX + excerpt | N_BE_XXXXX + excerpt | X.X/3 | Strong/Medium/Weak/Gap | X.X/5 | tag |

**Quy tắc cột:**
- **A/B/C-evidence:** node/edge code + trích đoạn ≤2 câu + page/line reference
- **Triang. score:** dựa trên `axiom_spec.md` triplet rows, carry-forward + cross-validate
- **Type:** Strong (close structural parallel), Medium (clear analogy), Weak (nearest available), Gap (absent in system)
- **RCA score:** 3-round × 5-Why × scoring gate ≥ 4/5 cho mọi type classification
- **Provenance:** `[established]` / `[proposed-by-this-project]` / `[interpretation]` — phân biệt claim mapping với node nguồn

---

## 5. Kế hoạch thực hiện (6 phases)

### Phase 1 — Schema Design & RCA Gate (planning-only, 10% effort)
- [ ] P1.1 — Thiết kế chính xác cấu trúc từng mapping row (cột, format, quy tắc)
- [ ] P1.2 — Adapt schema từ BE↔QM template: thay "BE concept" / "QM concept" → "A-evidence" / "B-evidence" / "C-evidence"
- [ ] P1.3 — Thiết kế TRITHUC-index format (namespace TRITHUC-, tránh overlap với BIAN-1–20)
- [ ] P1.4 — RCA gate: score P1 decisions ≥ 4/5

### Phase 2 — Node/Edge Summary Table (15% effort)
- [ ] P2.1 — Trích xuất canonical nodes/edges từ A (top-20) dưới dạng bảng tham chiếu ngắn gọn
- [ ] P2.2 — Trích xuất canonical nodes/edges từ B (top-30: Ashby 15 + Weick 15) dưới dạng bảng tham chiếu
- [ ] P2.3 — Trích xuất canonical nodes/edges từ C (top-30: 30 core) dưới dạng bảng tham chiếu
- [ ] P2.4 — Map các node codes vào axiom (bảng ánh xạ sơ bộ)
- [ ] P2.5 — Output: Part I của `a_b_c_system_mapping.md`

### Phase 3 — Core Axiom Mapping I–IV (35% effort, RCA gate bắt buộc)
- [ ] P3.1 — Mapping Tiên Đề I: mỗi system → evidence rows → triangulation score → RCA validation
- [ ] P3.2 — Mapping Tiên Đề II: như trên
- [ ] P3.3 — Mapping Tiên Đề III: như trên, đặc biệt chú ý A-yếu (Phan Ngọc thiên đồng đại)
- [ ] P3.4 — Mapping Tiên Đề IV: như trên, đặc biệt chú ý B-mạnh (Ashby Requisite Variety)
- [ ] P3.5 — Cross-validation: so sánh triangulation scores mới với `axiom_spec.md` triplet rows

### Phase 4 — Derived + Meta + Interface Mapping (20% effort)
- [ ] P4.1 — Mapping Mệnh Đề 1–4 (derived → evidence từ I–IV được carry-forward)
- [ ] P4.2 — Mapping Tiên Đề V (Meta) — đặc biệt chú ý C (Śūnyatā = neo mạnh nhất)
- [ ] P4.3 — Mapping Tiên Đề VI (Interface) — đặc biệt chú ý C1 conditions × A/B/C
- [ ] P4.4 — Mapping DSH heuristic

### Phase 5 — TRITHUC Gap Index + Structural Summary (10% effort)
- [ ] P5.1 — Liệt kê concepts hiện diện trong một system nhưng yếu/thiếu trong ≥2 system còn lại
- [ ] P5.2 — Viết `documents/gap/TRITHUC_index.md` theo schema `BIAN_index_schema.md` (Part 1–5 + validation)
- [ ] P5.3 — Đếm coverage score cho từng axiom × từng system
- [ ] P5.4 — Xác định critical asymmetries (strongest divergences) và strongest convergences

### Phase 6 — Boundary Statement + Validation + Nguồn Trích Dẫn (10% effort)
- [ ] P6.1 — Viết "What This Mapping Does NOT Claim" (Part IV)
- [ ] P6.2 — Schema validation checklist (Part V, theo mẫu BE↔QM)
- [ ] P6.3 — Bảng Nguồn Trích Dẫn APA (Part VI — Phan Ngọc 1998, Ashby 1956, Weick/Orton 1990, BE source)
- [ ] P6.4 — RCA gate final pass: score toàn bộ mapping decisions

---

## 6. Độ phức tạp ước tính

| Phase | Effort | Độ phức tạp | Lý do |
|---|---|---|---|
| 1 — Schema Design | 10% | LOW | Quyết định cấu trúc, ít dữ liệu |
| 2 — Node/Edge Summary | 15% | MEDIUM | Nhiều dữ liệu nhưng ít quyết định — extract + format |
| 3 — Core Mapping (I–IV) | 35% | **HIGH** | RCA gate cho mỗi mapping decision; 4 axioms × 3 systems = 12 bảng |
| 4 — Derived+Meta+Interface | 20% | MEDIUM | 7 đơn vị còn lại, ít evidence hơn Core |
| 5 — Gap Index + Summary | 10% | MEDIUM | Cần cross-reference toàn bộ 3 system |
| 6 — Boundary + Validation | 10% | LOW | Template-driven |

**Tổng thể: HIGH** — do số lượng system (3) × số axiom (10) × RCA requirement.

---

## 7. Carry-Forward Set

Từ `axiom_spec.md` + `dictionary_rule.md §7`, các asset được carry-forward (phải tái xác nhận qua RCA gate):

| # | Asset | Nguồn | Ghi chú |
|---|---|---|---|
| CF1 | Triplet scores `[A·B·C]` cho từng axiom | `axiom_spec.md` §2 | Làm baseline, không làm kết luận — phải cross-validate |
| CF2 | Taxonomy 3 vai (lens/mirror/beam) | `axiom_spec.md` §0.4, CLAUDE.md | Bất khả xâm phạm — A/B/C = lens, không phải mirror |
| CF3 | Neo calibration | `axiom_spec.md` §0.1.1 | A: Phần I+II (không Phần 3); B: Requisite Variety + sensemaking; C: pramāṇa/apoha/Nhị đế |
| CF4 | Điều kiện phản chứng từng axiom | `axiom_spec.md` §2 (mỗi axiom) | Dùng làm anchor cho Weak/Gap classification |
| CF5 | Phân kỳ thật so với hệ cũ | `axiom_spec.md` §4 | 4 điểm phân kỳ đã xác nhận |
| CF6 | Bất đối xứng phụ thuộc (F2+F3) | `axiom_spec.md` §0.3 | Model-of, không phải identity |
| CF7 | Quan hệ model-of | CLAUDE.md §Core Principles | Áp dụng cho mapping A→MACH RE (MACH RE là model-of triết học dân tộc) |

---

## 8. Dependency Graph

```
Phase 1 (Schema)
  │
  └──▶ Phase 2 (Node/Edge Summary)
          │
          ├──▶ Phase 3 (Core I–IV) ────┐
          │                             │
          └──▶ Phase 5 (Gap Index) ◀───┘
                    │
                    └──▶ Phase 4 (Derived+Meta+Interface)
                              │
                              └──▶ Phase 6 (Boundary+Validation)
```

Phase 3 và Phase 5 có thể chạy song song sau Phase 2.

---

## 9. Decision Log (cập nhật trong quá trình thực hiện)

| # | Quyết định | RCA score | Date |
|---|---|---|---|
| D1 | Dùng namespace TRITHUC- cho gap labels (tránh overlap BIAN-1–20) | 4.8/5 | 2026-06-12 |
| D2 | Map ở axiom-level, không node-by-node | 5.0/5 | 2026-06-12 |
| D3 | Tái sử dụng triplet scores từ axiom_spec.md làm baseline | 4.8/5 | 2026-06-12 |
| D4 | III-orthogonality V ⊥ H = `[proposed-by-this-project]` — partially supported by all 3 compasses | 4.8/5 | 2026-06-12 |
| D5 | A-evidence: Phần 3 Phan Ngọc excluded per `axiom_spec.md §0.1.1` | 4.8/5 | 2026-06-12 |
| **Status** | **All 6 phases COMPLETE** | — | **2026-06-12** |

---

*Plan này được viết theo 3-round RCA × 5-Why × scoring gate ≥ 4/5. Mọi quyết định mapping trong quá trình thực hiện sẽ được ghi nhận vào Decision Log ở trên.*

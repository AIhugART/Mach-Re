Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# AHP Template — Instantiation Guide
## Anti-Hallucination Pipeline for Multi-System Mapping Projects

**Exported from:** AHP v3.1 (2026-06-12) — *snapshot, không tự đồng bộ; kiểm tra AHP live tại `anti_hallucinations/` trước khi instantiate.*
**Template version:** v1.0
**Language:** English-first, bilingual annotations in Vietnamese
**Compass:** Buddhist Epistemology (Pratyakṣa / Anumāna / Smṛti / Vikalpa)
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5

> **Purpose (Mục đích):** Template này cho phép triển khai Anti-Hallucination Pipeline (AHP) cho bất kỳ **multi-system mapping project** nào — dự án map 2, 3, hoặc N hệ thống khái niệm với nhau, mỗi hệ thống có bảng node/edge code, và các cross-system link là auditable claims.
>
> Template tách hai lớp:
> - `[GENERIC]` — epistemic structure, pipeline flow, label taxonomy: **giữ nguyên**
> - `[CALIBRATE]` — SOT list, scoring anchors, signal examples, system registries: **phải re-derive cho domain của bạn**

---

## Quick Start

1. Copy toàn bộ file từ folder `template/` vào anti-hallucination folder của project mới.
2. Làm theo 9-step instantiation checklist bên dưới.
3. Chạy self-audit checklist (§3) trước khi tuyên bố pipeline ACTIVE.

---

## File Inventory (15 files + demo)

| # | File | Exported from | What to fill |
|---|------|--------------|--------------|
| 1 | `TEMPLATE_README.md` | (file này) | Read only |
| 2 | `template_index.md` | `index.md` | `{{PROJECT_NAME}}`, Scope, Compass, SOT references, system list |
| 3 | `template_00_top_risk_record.md` | `00_top_10_hallucinations_record.md` | All risk entries |
| 4 | `template_01_early_warning.md` | `01_early_warning.md` | Example column |
| 5 | `template_02_detection.md` | `02_detection.md` | Example inventory, Group B/C/D labels |
| 6 | `template_03_sot_traceability.md` | `03_sot_traceability.md` | `{{SOT_LIST}}` (≥ 3 SOTs), cross-reference matrix |
| 7 | `template_04_analysis.md` | `04_analysis.md` | Example RCA |
| 8 | `template_05_scoring.md` | `05_scoring.md` | Calibration anchors (≥ 2 per band) |
| 9 | `template_06_solution.md` | `06_solution.md` | Example tracking entries |
| 10 | `template_label_system.md` | `label_system.md` | ES tag defaults for your claim types |
| 11 | `template_stakes_assessment.md` | `bds_stakes_assessment.md` | Stakes criteria for your domain |
| 12 | `template_vyapti_registry.md` | `bds_vyapti_registry.md` | All VYR entries (must re-derive) |
| 13 | `template_integration_spec.md` | `bds_integration_spec.md` | Epistemic framework mapping |
| 14 | `template_system_registry.md` | (new — multi-system) | All system entries + node/edge tables |
| 15 | `template_mapping_registry.md` | (new — multi-system) | All mapping links + NAC table |
| — | `demo_instantiation/` | Synthetic 2-system example | Reference only |

---

## 9-Step Instantiation Checklist

### Step 1 — Set project identity
*[CALIBRATE]*

In every file, replace:
- `{{PROJECT_NAME}}` → your project name (e.g., `PROJ-XYZ`)
- `{{PROJECT_SCOPE}}` → one sentence describing what is being mapped to what
- `{{COMPASS}}` → your epistemic compass (default: Buddhist Epistemology; may keep as-is)

Add to each file header:
```
Instantiated from: AHP Template v1.0 (2026-06-12)
Project: {{PROJECT_NAME}}
Date instantiated: YYYY-MM-DD
```

---

### Step 2 — Register N systems in `template_system_registry.md`
*[CALIBRATE — core multi-system data structure]*

For each system `SYS_X`:
1. Add one entry to the **System Registry Table** (§1).
2. Fill the **Node Table**: code `N_{{SYS}}_XXXXX`, name, definition, source.
3. Fill the **Edge Table**: code `ED_{{SYS}}_XXXXX`, from-node, to-node, relation type, directed.

**Namespace rule** `[GENERIC]`: Every node/edge code carries its system prefix. `N_A_00001` and `N_B_00001` are different nodes even if conceptually related. Never merge namespaces.

Minimum: ≥ 2 systems.

---

### Step 3 — Declare SOT list in `template_03_sot_traceability.md` §A
*[CALIBRATE — Vyāpti phải được thiết lập lại cho domain mới]*

Each system registered in Step 2 automatically becomes one internal SOT (its canonical definition file). Add at minimum:
- Internal SOTs: one per system
- External SOTs: ≥ 1 published reference per domain (textbook, paper, standard)

Update SOT Registry table (§A.1, §A.2) and set trace score denominator (§C.2).

---

### Step 4 — Choose compass
*[GENERIC for structure; CALIBRATE for domain application]*

The Buddhist Epistemology compass (Pratyakṣa/Anumāna/Smṛti/Vikalpa) is domain-general and exports as-is. What you must calibrate:
- Default ES tag per claim type in `template_label_system.md` §1.4
- TTL_CLASS assignments in `template_vyapti_registry.md`

---

### Step 5 — Fill calibration anchors in `template_05_scoring.md`
*[CALIBRATE — REQUIRED before ACTIVE declaration]*

For each of the 5 scoring bands, provide ≥ 2 example components from your domain:
- Band 1 (0-2): verified, standard components
- Band 2 (3-4): framework-grounded extensions
- Band 3 (5-6): speculative but flagged assumptions
- Band 4 (7-8): weak-foundation components
- Band 5 (9-10): orphaned / fabricated components

Without calibration anchors, scores drift. **Pipeline must NOT be declared ACTIVE without this step.**

---

### Step 6 — Fill signal examples in `template_01_early_warning.md`
*[CALIBRATE — signal names + trigger conditions are GENERIC; only the "Example" column must be filled]*

For each of the 20 signals (R1-R5, O1-O5, Y1-Y5, S16-S20), provide ≥ 1 example from your domain. Priority: fill R1-R5 first, then S16-S20, then O1-O5.

---

### Step 7 — Re-derive Vyāpti Registry in `template_vyapti_registry.md`
*[CALIBRATE — VYR entries CANNOT be inherited from another domain]*

Delete all `{{VYR_EXAMPLE_*}}` placeholder rows and re-derive from scratch for your domain. For each claim type:
1. Detection pattern (keywords, codes)
2. ES tag (Pratyakṣa/Anumāna/Smṛti/Vikalpa)
3. Reliability prior (HIGH/MEDIUM/LOW)
4. TTL_CLASS (Atemporal / Geological / Historical / Current)
5. Re-verify trigger

Minimum: ≥ 3 VYR entries before ACTIVE.

---

### Step 8 — Populate Mapping Registry in `template_mapping_registry.md`
*[CALIBRATE — mapping links are the highest-risk claim type]*

For every cross-system link, fill 4 mandatory columns:
1. `mapping_type`: `ANALOGY` / `STRUCTURAL` / `EQUIVALENCE-JUSTIFIED`
2. `justification`: one sentence
3. `ground_system`: reference frame for this direction
4. `AHP label`: default `[ES-ANUMA]` + boundary note

For nodes with **no analogue** in another system: add to **NAC Table** (No-Analogue Concept). Never force-map a NAC — that is Vikalpa hallucination.

---

### Step 9 — Run self-audit before ACTIVE declaration

See §3 Self-Audit Checklist below. All 10 PASS → declare pipeline ACTIVE.

---

## §3 — Self-Audit Checklist

| # | Check | PASS condition | Status |
|---|-------|---------------|--------|
| 1 | File count | All 15 template files present in folder | ☐ |
| 2 | Provenance stamp | Every file has `Instantiated from: AHP Template v1.0` header | ☐ |
| 3 | Author metadata | Every file has author metadata (if outside `public_documents/`) | ☐ |
| 4 | No foreign calibration data | grep for source project terms — all matches inside `<!-- ... -->` illustration comments | ☐ |
| 5 | System Registry | ≥ 2 systems registered; each has node table + edge table | ☐ |
| 6 | SOT list | ≥ 3 SOTs declared in `template_03_sot_traceability.md` §A | ☐ |
| 7 | Scoring calibration | ≥ 2 anchor examples per band in `template_05_scoring.md` | ☐ |
| 8 | Vyāpti Registry | ≥ 3 VYR entries (domain-specific) | ☐ |
| 9 | Mapping Registry | All cross-system links have 4-column entries; NAC table exists | ☐ |
| 10 | File Map | `template_index.md` §2 lists all files including any additions | ☐ |

**All 10 PASS → declare pipeline ACTIVE in `template_index.md` header.**

---

## §4 — Placeholder Reference

| Placeholder | Replace with | Used in |
|-------------|-------------|---------|
| `{{PROJECT_NAME}}` | Your project name | All files |
| `{{PROJECT_SCOPE}}` | One-sentence scope | `template_index.md` |
| `{{COMPASS}}` | Epistemic compass name | `template_index.md`, `template_integration_spec.md` |
| `{{SYS_A}}`, `{{SYS_B}}`, `{{SYS_N}}` | System codes (e.g., `BE`, `QM`, `LOG`) | `template_system_registry.md`, `template_mapping_registry.md` |
| `{{SOT_LIST}}` | Bulleted list of SOTs | `template_03_sot_traceability.md` |
| `{{CALIBRATION_ANCHOR_BAND_N}}` | Domain component example for band N | `template_05_scoring.md` |
| `{{DOMAIN_EXAMPLE_*}}` | Any domain-specific example | `template_01_early_warning.md`, `template_04_analysis.md` |
| `{{VYR_EXAMPLE_*}}` | Domain claim type VYR entry | `template_vyapti_registry.md` |

---

## §5 — Design Principles `[GENERIC — do not modify]`

| Principle | Rationale |
|-----------|-----------|
| **Extend, not overwrite** | Preserve valid structure; add, refine, qualify — do not replace |
| **SOT-first** | Every claim must trace to ≥ 1 SOT |
| **Score before solve** | Score before proposing solutions |
| **Proportionality** | Simple → detection + scoring; complex → full pipeline |
| **Track resolution** | Every issue tracked to RESOLVED |
| **Compass, not cargo** | Epistemic framework guides RCA; do not import its structure as domain data |
| **Namespace integrity** | Each system's node/edge codes are independent |
| **Mapping = auditable claim** | Every cross-system link: mapping_type + justification + AHP label |
| **NAC = valid result** | No-analogue means no forced mapping — record as NAC |

---

*AHP Template v1.0 — Exported from AHP v3.1 (2026-06-12). Compass: Buddhist Epistemology (Pramāṇa structure exportable; Vyāpti re-derivable per domain). Multi-system: System Registry + Mapping Registry (N systems). 3-Round RCA design: 4.64/5 PASS.*

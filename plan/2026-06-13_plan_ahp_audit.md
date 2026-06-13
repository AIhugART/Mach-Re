Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Kế Hoạch Audit Cài Đặt AHP — Mạch Rễ
## AHP Installation Audit Plan for MACH RE

**Plan type:** audit (post-installation verification)
**Date:** 2026-06-13
**Version:** v1.1 — Q1/Q2 đã được người dùng trả lời (2026-06-13); xem Part 6
**Status:** AWAITING APPROVAL — chỉ lưu plan, chưa sửa bất kỳ file nào; chờ "yes/proceed" để thực thi Phases A–E
**Audit target:** `anti_hallucinations/` (cài đặt tại commit `efc919a`, 2026-06-12)
**Authorizing plan being audited:** `plan/2026-06-12_plan_ahp_installation.md`
**Compass:** C — Buddhist Epistemology (Pratyakṣa / Anumāna / Smṛti / Vikalpa)
**Method:** 3-Round RCA × 5-Why × scoring gate ≥ 4/5 (rubric 6 tiêu chí, có Provenance)

**Reference files (READ-ONLY trong audit này):**
- `documents/A_SYSTEM_Phan_Ngoc_BanSacVanHoaVietNam/a_system_phan_ngoc.md` — Compass A (git-tracked ✅)
- `documents/B_SYSTEM_Ashby_Weick/b_system_ashby_weick.md` — Compass B (git-tracked ✅)
- `documents/C_SYSTEM_Buddhist_Epistemology/c_system_buddhist_epistemology.md` — Compass C (**UNTRACKED ⚠** — xem AF-3)
- `documents/mapping/a_b_c_system_mapping.md` — Mapping SOT (git-tracked ✅)
- `documents/gap/TRITHUC_index.md` — Gap registry (git-tracked ✅)
- `labels.md` — Confirmation verdict SOT (git-tracked ✅)

**Nguyên tắc bằng chứng (evidence rule):** Mọi kết luận PASS/FAIL trong audit này đều đo trực tiếp trên filesystem hoặc git history — không lấy lại số liệu tự khai trong `index.md` / `2026-06-12_ahp_rca_summary.md`. Đây là khác biệt cốt lõi so với self-audit gốc (xem AF-1 Round 3).

---

# PART 1 — MA TRẬN XÁC MINH (re-run self-audit checklist, đo độc lập)

Self-audit gốc (installation plan Phase 5.3) gồm 11 check, tất cả khai PASS. Kết quả đo lại:

| # | Check | Khai báo gốc | Kết quả đo 2026-06-13 | Verdict |
|---|-------|--------------|----------------------|---------|
| 1 | File count: 15 instantiated + 2 new = 17 | PASS | **14 instantiated** + 2 new + 1 RCA summary. `00_top_risk_record.md` KHÔNG tồn tại (xác nhận bằng Glob + danh sách 35 file của commit `efc919a` — chỉ có `template/template_00_top_risk_record.md`) | **FAIL → AF-1** |
| 2 | Provenance stamp mọi file | PASS | 14/14 file hiện hữu có stamp `Instantiated from: AHP Template v1.0 (2026-06-12)` (grep count = 14 ngoài `template/`) | PASS |
| 3 | Author metadata mọi file | PASS | Spot-check `index.md`, `mapping_registry.md`, `05_scoring.md`: có. Full check 14 file → Phase E | PASS (spot-check) |
| 4 | No foreign calibration data / placeholder | PASS | Grep `\{\{[A-Z_]+\}\}` ngoài `template/`: 0 match. Placeholder chỉ còn trong `template/` (đúng thiết kế) | PASS |
| 5 | System Registry: 4 systems | PASS | `system_registry.md` có SYS PN, AW, BE, MR | PASS |
| 6 | SOT list: 8 internal (incl. labels.md) + 3 external | PASS | `03_sot_traceability.md:24` — SOT-5 = labels.md, N=8. **Nhưng SOT-8 (compass C) untracked trong git** | PASS có điều kiện → AF-3 |
| 7 | Scoring: ≥ 2 anchors/band | PASS | `05_scoring.md`: 5 bands × 2 anchors = 10 anchors MACH RE | PASS |
| 8 | Vyāpti Registry ≥ 3 entries | PASS | 9 dòng `VYR-` (grep count = 9) | PASS |
| 9 | Mapping Registry: all Part II rows + NAC 5 | PASS | 26 dòng `MAP_` + 5 NAC entries (NAC_001–005, dòng 74–78) | PASS |
| 10 | labels.md integration: `[AH-NAJ]` + cross-refs | PASS | `[AH-NAJ]` hiện diện trong 9 file (label_system, 06_solution, integration_spec, stakes_assessment, index, 02_detection, README, 2 plan files). **Nhưng** "Confirmation column trong 00_top_risk_record" không kiểm được vì file không tồn tại | PARTIAL → phụ thuộc AF-1 |
| 11 | File Map complete trong index.md §2 | PASS | `index.md` §2A liệt kê `00_top_risk_record.md` như file đang hoạt động ("Re-audit weekly") — **liệt kê file không tồn tại** | **FAIL → AF-1** |

**Các kiểm tra bổ sung ngoài checklist gốc:**

| # | Check bổ sung | Kết quả | Verdict |
|---|---------------|---------|---------|
| 12 | CHANGELOG.md có entry AHP | Có — "2026-06-12 — AHP Installation" | PASS |
| 13 | CLAUDE.md có §Anti-Hallucination Pipeline | **HEAD có (29 dòng); working tree ĐÃ XÓA (diff: 1 insertion, 28 deletions, chưa commit).** CHANGELOG vẫn khai "Modified: CLAUDE.md — added §Anti-Hallucination Pipeline" | **FAIL → AF-2** |
| 14 | SOT files trong version control | 6/7 tracked. `documents/C_SYSTEM_Buddhist_Epistemology/` untracked (cả folder `??` trong git status) | **FAIL → AF-3** |
| 15 | Plan gốc cập nhật trạng thái sau khi thực thi | `plan/2026-06-12_plan_ahp_installation.md:8` vẫn ghi "Status: AWAITING APPROVAL"; Part 8 checklist toàn "☐ Pending" — dù đã thực thi và commit | **FAIL → AF-4** |

**Tổng kết:** 9/15 PASS · 1 PARTIAL · 4 FAIL → 4 findings (AF-1 → AF-4).

---

# PART 2 — FINDINGS (mỗi finding: 3-Round RCA × 5-Why × scoring gate)

## AF-1 — `00_top_risk_record.md` không tồn tại nhưng self-audit khai PASS và hệ thống khai ACTIVE

**Severity: CRITICAL** (finding nặng nhất — cùng lớp lỗi với F9)

### 3-Round RCA

**Round 1 — Symptom:** `index.md:14` khai "Status: ACTIVE — self-audit passed (2026-06-12)"; RCA summary §4 khai "15 instantiated"; nhưng filesystem và commit `efc919a` chỉ có 14 file — `00_top_risk_record.md` chưa bao giờ được tạo. Check #1 (đếm file) không thể PASS nếu thực sự đếm.

**Round 2 — Mechanism (vì sao lỗi này backfire ở đây đặc biệt nặng):** AHP là tầng chống ảo giác — bản ghi kích hoạt đầu tiên của nó lại chứa một self-certified false claim. Theo chính taxonomy của AHP, đây là tín hiệu **S17** (model self-evaluates không qua TIP-1) và **S18** (Vikalpa trình bày như Pratyakṣa — "passed" được *viết ra* chứ không được *đo*). Tệ hơn: file bị thiếu chính là tầng TTL_CLASS / Risk Score — đúng năng lực được viện dẫn ở Round 1 W3 của quyết định cài đặt ("TTL_CLASS tracking would have flagged F9 before external review"). Thành phần biện minh cho việc cài đặt là thành phần duy nhất không được cài.

**Round 3 — Root (chuẩn nội bộ nào bị vi phạm):** RULE ZERO bước 5 (Verify: "Show that the root cause has been removed, not merely that the visible symptom disappeared") và Tiên Đề V (Soi Mình Mà Không Vỡ). Self-audit được thực thi như một **tuyên bố sinh ra** (generated declaration) thay vì một **phép đo** (measurement against filesystem) — cùng root class với F9: claim nội-bộ-nhất-quán nhưng ngoại-bộ-sai, lọt qua vì gate không có bước kiểm độc lập.

### 5-Why

- **W1:** Vì sao `00_top_risk_record.md` thiếu? → Không có phase step nào tạo nó.
- **W2:** Vì sao không có phase step? → Phân rã phase của installation plan (Part 3) bỏ sót file #2: Phase 1 = files 1, 15, 16 · Phase 2 = 13, 14 · Phase 3 = 7, 10, 11 · Phase 4 = 3, 4, 5, 6, 8, 9 · Phase 5 = 12. Hợp lại: 1, 3–16. **File #2 không thuộc phase nào.** (Kiểm chứng được trực tiếp trên plan gốc.)
- **W3:** Vì sao self-audit check #1 vẫn PASS? → Self-audit đối chiếu với **con số kỳ vọng trong plan** ("15 + 2 = 17") thay vì đếm file thật trên đĩa.
- **W4:** Vì sao đối chiếu kỳ vọng thay vì đo? → Self-audit do chính session AI thực thi cài đặt tự chấm, không có bước verification độc lập (TIP-1) — đúng định nghĩa tín hiệu S17 của chính AHP.
- **W5 → Root (1 câu):** Self-audit thiếu bước đo độc lập (đếm filesystem so với inventory), nên một lỗ hổng coverage trong phân rã phase của plan lan truyền không bị chặn thành tuyên bố ACTIVE — cùng root class với F9 (tự chấm điểm không kiểm chứng ngoài).

### Scoring gate (chấm CLAIM "self-audit passed / 15 files / ACTIVE" — orientation: ≥ 4/5 → sửa)

| Criterion | Score | Reasoning |
|---|---|---|
| Correct | 1/1 | File vắng mặt chứng minh được bằng Glob + commit `efc919a` (35 files, không có root `00_*`) |
| Deep | 1/1 | Fix chạm root: tạo file + đổi cách self-audit từ tuyên-bố sang phép-đo + đính chính hồ sơ |
| Feasible | 1/1 | `template_00_top_risk_record.md` có sẵn; không phá cấu trúc nào |
| Conflict-risk | 1/1 | Tạo file thực hiện đúng ý định đã ghi; đính chính là additive |
| Preservation | 1/1 | 14 file đã cài đúng được giữ nguyên |
| Provenance | 1/1 | Mọi bằng chứng trace được: `index.md:14`, `index.md:82`, RCA summary §4/§7, `git show efc919a --stat` |
| **TOTAL** | **6/6 = 5.0/5** | **→ FIX (Phase A + B)** |

---

## AF-2 — Working tree CLAUDE.md đã xóa §Anti-Hallucination Pipeline trong khi CHANGELOG khai "added"

**Severity: HIGH** — **Q1 ĐÃ TRẢ LỜI (2026-06-13): TAI NẠN → Option A**

### 3-Round RCA

**Round 1 — Symptom:** `git diff CLAUDE.md` = 28 dòng bị xóa (toàn bộ §AHP), chưa commit. CHANGELOG.md (đã commit) khai "Modified: CLAUDE.md — added §Anti-Hallucination Pipeline". Hai SOT mâu thuẫn nhau.

**Round 2 — Mechanism:** CLAUDE.md là rule-routing SOT được nạp vào mỗi session. Không có §AHP, các session tương lai không định tuyến claim mới qua pipeline → AHP trơ về mặt vận hành (silently inert). Điều này kích hoạt sớm chính điều kiện FAIL #4 của RCA summary §6: "No hallucination detected within 6 months (pipeline unused)". Việc xóa section đẩy nhanh kill condition của chính pipeline.

**Round 3 — Root:** Divergence chưa commit giữa hai SOT mà không có changelog entry cho việc xóa — vi phạm quy tắc traceability. Câu hỏi về ý định ban đầu được xếp DEFER theo labels.md #3 (No authority to judge). **Unlock condition ĐÃ ĐẠT (2026-06-13): người dùng xác nhận việc xóa là TAI NẠN** (human verdict — labels.md #2 áp cho thay đổi working-tree: thay đổi không chủ ý, không có thẩm quyền). → Phase C chốt **Option A: khôi phục section**, không còn nhánh chờ.

### 5-Why (rút gọn — root đã được human xác nhận)

- **W1:** Vì sao CLAUDE.md mất §AHP? → Một edit chưa commit xóa 28 dòng.
- **W2:** Vì sao edit này không có dấu vết? → Chưa commit, không CHANGELOG entry, không plan nào khai báo việc xóa.
- **W3 → Root (1 câu):** Một thay đổi working-tree **không chủ ý** (human-confirmed 2026-06-13) đè mất section trong lúc nhiều file đang modified chưa commit — root vận hành: thay đổi SOT không được commit/ghi nhận ngay sau khi tạo, để working tree tồn đọng lâu thành môi trường dễ đè nhau.

### Scoring gate (chấm PLAN ITEM "khôi phục §AHP vào CLAUDE.md — Option A" — orientation: ≥ 4/5 → giữ action)

| Criterion | Score | Reasoning |
|---|---|---|
| Correct | 1/1 | Divergence có thật (`git diff` 1+/28−); ý định đã xác nhận |
| Deep | 1/1 | Khôi phục đúng nội dung đã commit + root vận hành xử lý ở Phase E (đóng working tree sớm) |
| Feasible | 1/1 | Chèn lại section thủ công — một bước |
| Conflict-risk | 1/1 | Người dùng đã xác nhận tai nạn (Q1) → không còn rủi ro ngược ý |
| Preservation | 1/1 | Các sửa khác trong CLAUDE.md working tree được giữ nguyên |
| Provenance | 1/1 | `git diff CLAUDE.md`, CHANGELOG.md:36, user verdict 2026-06-13 |
| **TOTAL** | **6/6 = 5.0/5** | **→ GIỮ ACTION (Phase C — Option A, hết gate chờ)** |

---

## AF-3 — SOT-8 (Compass C — file hệ thống Buddhist Epistemology) không nằm trong version control

**Severity: HIGH** — **Q2 ĐÃ TRẢ LỜI (2026-06-13): TRACK TẤT CẢ**

### 3-Round RCA

**Round 1 — Symptom:** `documents/C_SYSTEM_Buddhist_Epistemology/` là folder untracked (`??` trong git status; `git ls-files` xác nhận không match). AHP đã commit (`efc919a`) khai file này là SOT-8 và là **compass** của toàn pipeline.

**Round 2 — Mechanism:** Trace score của AHP dùng N=8 internal SOTs làm mẫu số. Một SOT không có version history có thể thay đổi hoặc biến mất mà không để lại dấu vết → mọi trace score từng tính dựa trên nó trở nên không kiểm chứng lại được (unfalsifiable retroactively). Nghịch lý nặng nhất: compass C là hệ quy chiếu epistemic của pipeline — thành phần chịu tải lớn nhất lại có lớp bảo vệ phiên bản yếu nhất. Cùng tình trạng (mức độ nhẹ hơn): `documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md`, `documents/gap/BIAN_index_schema.md`, `documents/archives/` đều untracked.

**Round 3 — Root:** Vi phạm nguyên tắc SOT-first của chính AHP (`index.md` §4): một Single Source of Truth không nằm trong version control thì không audit được theo thời gian — TTL tracking với nó là vô nghĩa. Root: phạm vi commit `efc919a` chỉ gồm `anti_hallucinations/` + plan, bỏ sót SOT mới tạo trong cùng luồng công việc.

### 5-Why

- **W1:** Vì sao SOT-8 untracked? → Commit `efc919a` không add folder C_SYSTEM.
- **W2:** Vì sao không add? → Phạm vi commit giới hạn vào sản phẩm AHP; file C-system được tạo trong luồng việc khác (commit message `4da24f9` nhắc "3 compass" nhưng file C không vào index git).
- **W3:** Vì sao không ai phát hiện? → Self-audit chỉ kiểm tồn tại file trên đĩa, không kiểm trạng thái git của SOT.
- **W4:** Vì sao self-audit không có check git? → Checklist gốc (11 mục) không có tiêu chí version-control coverage cho SOT.
- **W5 → Root (1 câu):** Self-audit checklist thiếu tiêu chí "SOT phải nằm trong version control", nên một compass SOT chỉ tồn tại trên working tree lọt qua mọi vòng kiểm.

### Scoring gate (chấm PLAN ITEM "đưa SOT-8 và toàn bộ tài liệu untracked liên quan vào git" — orientation: ≥ 4/5 → giữ action)

| Criterion | Score | Reasoning |
|---|---|---|
| Correct | 1/1 | Untracked xác nhận bằng `git ls-files --error-unmatch` (exit 1) |
| Deep | 1/1 | Fix root (đưa vào VCS + thêm check #14 vĩnh viễn vào checklist), không chỉ add một file |
| Feasible | 1/1 | `git add` — không đổi nội dung file nào |
| Conflict-risk | 1/1 | Additive; phạm vi đã được người dùng chốt "tất cả" (Q2) |
| Preservation | 1/1 | Không sửa nội dung SOT |
| Provenance | 1/1 | git status + ls-files output + user verdict Q2 (2026-06-13) |
| **TOTAL** | **6/6 = 5.0/5** | **→ GIỮ ACTION (Phase D — hết gate chờ)** |

---

## AF-4 — Plan gốc vẫn ghi "AWAITING APPROVAL" dù đã thực thi và commit

**Severity: MEDIUM** (hồ sơ, nhưng chạm trace integrity)

**3-Round rút gọn:** (R1) `plan/2026-06-12_plan_ahp_installation.md:8` = "AWAITING APPROVAL", Part 8 toàn "☐ Pending", trong khi commit `efc919a` chứa toàn bộ sản phẩm và chính plan đó khai file #17 sẽ "ARCHIVED after approval". (R2) Hồ sơ phê duyệt là mắt xích trace giữa quyết định người dùng và hành động AI — để trống nghĩa là về mặt hồ sơ, việc thực thi không có approval được ghi nhận (gần lớp tín hiệu S20: sản phẩm AI tự cấp thẩm quyền). (R3 — Root, 1 câu): Quy trình thực thi không có bước "đóng plan" (cập nhật status + checklist sau khi user approve), nên approval chỉ tồn tại trong hội thoại session — ngoài repo, không trace được.

**Scoring gate (chấm PLAN ITEM "cập nhật status plan gốc thành EXECUTED/ARCHIVED kèm ngày approve"):** Correct 1 · Deep 0.8 (fix hồ sơ là đúng nhưng root đầy đủ là thêm bước "đóng plan" vào quy trình — đưa vào Phase E) · Feasible 1 · Conflict-risk 1 · Preservation 1 · Provenance 1 → **5.8/6 = 4.83/5 → GIỮ ACTION (Phase B).**

---

## Những hạng mục XÁC NHẬN ĐÚNG (không phải finding)

Để công bằng với cài đặt gốc — các phần sau được đo lại và đạt:

1. 14 file đã cài có đầy đủ provenance stamp, không sót placeholder `{{...}}`.
2. Tích hợp labels.md đúng thiết kế: SOT-5 = labels.md, `[AH-NAJ]` hiện diện và route đúng (DEFER, không BLOCKING) trong label_system / 06_solution / stakes_assessment / integration_spec.
3. Số liệu khai trong RCA summary khớp thực tế ở các mục: 9 VYR ✅ · 26 MAP links ✅ · 5 NAC ✅ · 4 systems ✅ · 5 bands × 2 anchors ✅ · 20 signals (per 01_early_warning).
4. CHANGELOG.md có entry root-level đúng quy tắc routing phân tầng.
5. NAC table dùng đúng node codes (N_BE_00012, N_AW_ASH_00091–00100, N_BE_00253, N_PN_00029/30) khớp TRITHUC refs.

---

# PART 3 — KẾ HOẠCH SỬA (corrective actions — CHƯA THỰC THI, chờ duyệt; Q1/Q2 đã chốt → không còn nhánh chờ trong nội dung)

> Orientation scoring ở phần này: chấm *plan item* (≥ 4/5 = action hợp lệ, giữ) — theo `plan/mach-re-plan-chinh-sua-v2.md` §2.

## Phase A — Tạo `anti_hallucinations/00_top_risk_record.md` (sửa AF-1, phần thiếu hụt)

1. Instantiate từ `template/template_00_top_risk_record.md` với provenance stamp + author metadata.
2. Populate các entry đầu tiên:
   - 10 TRITHUC gaps (TTL_CLASS = Current, theo VYR-5, ES tag `[ES-VIKALP]`).
   - **4 audit findings AF-1→AF-4 của chính audit này làm risk record đầu tiên** — Tiên Đề V ở tầng meta-audit: pipeline mở sổ rủi ro bằng chính rủi ro của nó.
   - Confirmation column tham chiếu labels.md (#1/#2/#3) theo Rule 4 của installation plan.
3. Hoàn thành luôn next-step P1 của RCA summary §7 ("Populate 00_top_risk_record.md — within 1 week", hạn 2026-06-19).

## Phase B — Đính chính hồ sơ (sửa AF-1 phần khai sai + AF-4)

> Nguyên tắc: **đính chính bằng correction note, không viết lại lịch sử âm thầm** (silent rewrite = xóa dấu vết lỗi = vi phạm traceability).

1. `anti_hallucinations/index.md`: thêm Version History v1.1 — "Correction 2026-06-13: self-audit 2026-06-12 khai PASS sai ở check #1; 00_top_risk_record.md được tạo ngày 2026-06-13 theo audit plan."
2. `anti_hallucinations/plan/2026-06-12_ahp_rca_summary.md`: thêm mục "Correction 2026-06-13" — file inventory thực tế 14 (không phải 15) tại thời điểm 2026-06-12; giữ nguyên văn bản gốc.
3. `anti_hallucinations/plan/2026-06-12_ahp_instantiation_log.md`: log entry cho Phase A + B.
4. `plan/2026-06-12_plan_ahp_installation.md`: cập nhật Status → "EXECUTED 2026-06-12 (commit efc919a) — AUDITED 2026-06-13, 4 findings"; tick Part 8 checklist kèm ngày.

## Phase C — Khôi phục §AHP vào CLAUDE.md (sửa AF-2 — **Q1 đã chốt: TAI NẠN → Option A**)

1. Chèn lại section §Anti-Hallucination Pipeline (nội dung lấy từ `git show HEAD:CLAUDE.md`, 28 dòng) vào CLAUDE.md working tree — **chèn thủ công, KHÔNG dùng `git checkout HEAD -- CLAUDE.md`** (sẽ mất các sửa khác đang có trong working tree).
2. Ghi nhận sự cố trong CHANGELOG.md (gộp với entry Phase E): "AHP section accidentally removed from working-tree CLAUDE.md, restored 2026-06-13 per audit AF-2 (user-confirmed accident)."
3. Verify sau khi chèn: grep "Anti-Hallucination Pipeline" trong CLAUDE.md phải match, và `git diff CLAUDE.md` không còn dòng `-## Anti-Hallucination Pipeline`.

## Phase D — Git hygiene cho SOT (sửa AF-3 — **Q2 đã chốt: TRACK TẤT CẢ**)

1. `git add` theo đường dẫn cụ thể, đủ 4 hạng mục:
   - `documents/C_SYSTEM_Buddhist_Epistemology/` (SOT-8 — bắt buộc)
   - `documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md`
   - `documents/gap/BIAN_index_schema.md`
   - `documents/archives/`
2. Ghi chú: `review/2026-06-12-Tuyen_bo.html` cũng đang untracked (thấy trong git status) nhưng KHÔNG thuộc phạm vi Q2 (không phải SOT/tài liệu AHP) — không add trong phase này; nêu lại cho người dùng ở lần commit sau.
3. Commit riêng, message rõ phạm vi (không gộp với Phase A/B/C).

## Phase E — Re-run self-audit như PHÉP ĐO + vá quy trình (sửa root của AF-1, AF-2, AF-3, AF-4)

1. Chạy lại 11 check gốc + 4 check bổ sung (Part 1), mỗi check kèm **lệnh đo + output** (Glob/grep/git), không chấp nhận khai báo suông.
2. Thêm vĩnh viễn vào self-audit checklist (sửa cả `template/` để dự án sau thừa hưởng):
   - Check #12: "File count đo bằng lệnh đếm trên filesystem, ghi kèm output."
   - Check #13: "Mọi internal SOT phải `git ls-files` match."
   - Check #14: "Plan gốc phải được đóng (status + approval checklist) trước khi declare ACTIVE."
   - Check #15: "Thay đổi SOT phải được commit hoặc khai báo trong cùng phiên làm việc — không để working tree tồn đọng" (root vận hành của AF-2).
3. Chỉ sau khi 15/15 PASS bằng phép đo → ghi CHANGELOG.md (root) entry "AHP Audit 2026-06-13 — 4 findings fixed" theo quy tắc P5/G6.

**Scoring gate cho toàn bộ corrective plan (Phases A–E, v1.1):** Correct 1 · Deep 1 (Phase E vá root quy trình, không chỉ vá 4 symptom) · Feasible 1 · Conflict-risk 1 (Q1/Q2 đã chốt — không còn nhánh mơ hồ) · Preservation 1 · Provenance 1 → **6/6 = 5.0/5 → plan hợp lệ.**

---

# PART 4 — DEPENDENCY & RISK

```
Phase A (tạo 00_top_risk_record) ──→ Phase B (đính chính hồ sơ)
                                          │
Phase C (khôi phục CLAUDE.md — Q1 ✅) ────┤
Phase D (git add SOT — Q2 ✅) ────────────┤
                                          ▼
                                  Phase E (re-audit đo + CHANGELOG)
```

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Đính chính bị hiểu là "viết lại lịch sử" | MEDIUM | Correction note ghi kèm ngày, giữ nguyên văn gốc — không xóa dòng nào của hồ sơ 2026-06-12 |
| Phase C chèn section đè lên sửa đổi khác trong CLAUDE.md | LOW | Chèn thủ công đúng vị trí cũ (sau phần GitNexus theo HEAD); verify bằng `git diff` sau chèn |
| Audit này cũng là AI tự chấm (S17 đệ quy) | MEDIUM | Mọi verdict Part 1 kèm phép đo tái lập được (lệnh + vị trí dòng); Q1/Q2 do người dùng trả lời = human verdict (TIP-1) cho hai finding chờ; người dùng duyệt plan này là TIP-1 cho phần còn lại |
| Commit Phase D kéo theo file ngoài ý muốn | LOW | `git add` theo 4 đường dẫn cụ thể (liệt kê ở Phase D.1), không `git add -A`; `review/2026-06-12-Tuyen_bo.html` chủ động loại trừ |

---

# PART 5 — BOUNDARY STATEMENT

1. **Audit này KHÔNG phủ nhận quyết định cài AHP.** Quyết định gốc (4.83/5) vẫn đứng vững; 4 findings là lỗi *thực thi và hồ sơ*, không phải lỗi *thiết kế*.
2. **Audit này KHÔNG sửa file nào** — chỉ lưu plan này và dừng. Mọi fix nằm ở Phases A–E, chờ duyệt cuối.
3. **Verdict về ý định AF-2 là của người dùng (Q1, 2026-06-13), không phải của AI** — audit chỉ ghi nhận; trước khi có Q1, finding này được xếp DEFER theo labels.md #3.
4. **Audit này KHÔNG kiểm nội dung học thuật** của 26 mapping links hay 9 VYR (đó là next-step P2 của RCA summary §7, "Audit all 26 mapping links — within 2 weeks", hạn 2026-06-26) — chỉ kiểm tính toàn vẹn cấu trúc của cài đặt.
5. **Findings và corrective actions là `[proposed-by-this-project]`** — dựa hoàn toàn trên bằng chứng nội bộ repo (filesystem, git history) + hai verdict người dùng (Q1/Q2); chưa qua kiểm chứng ngoài.

---

# PART 6 — QUYẾT ĐỊNH ĐÃ CHỐT & APPROVAL CHECKLIST

**Q1 — ĐÃ TRẢ LỜI (2026-06-13):** Việc xóa §Anti-Hallucination Pipeline khỏi CLAUDE.md là **TAI NẠN** → Phase C thực thi **Option A: khôi phục section**, kèm CHANGELOG note.

**Q2 — ĐÃ TRẢ LỜI (2026-06-13):** Track **TẤT CẢ**: `documents/C_SYSTEM_Buddhist_Epistemology/` + `documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md` + `documents/gap/BIAN_index_schema.md` + `documents/archives/`.

| # | Check | Status |
|---|-------|--------|
| 1 | Ma trận xác minh Part 1 (15 checks, có bằng chứng đo) | ☑ **15/15 PASS** (Phase E, 2026-06-13) |
| 2 | 4 findings AF-1→AF-4 (RCA trace + scoring ≥ 4/5) | ☑ **Đã fix** (Phases A–D, 2026-06-13) |
| 3 | Corrective plan Phases A–E (5.0/5, v1.1) | ☑ **EXECUTED** (2026-06-13) |
| 4 | Q1 — quyết định CLAUDE.md | ☑ **TAI NẠN → Option A** (user, 2026-06-13) |
| 5 | Q2 — phạm vi git add | ☑ **TẤT CẢ** (user, 2026-06-13) |
| 6 | User approval "yes" / "proceed" để thực thi Phases A–E | ☑ **"yes ,(Buddhist epistemology as compass) dùng 3-round RCA…"** (user, 2026-06-13) |

**AUDIT STATUS: COMPLETE — 4 findings fixed, 15/15 PASS, CHANGELOG.md updated, Phases A–E executed.**

---

**Nguồn Trích Dẫn:** Tài liệu này không có trích dẫn nghiên cứu từ bên ngoài. (Toàn bộ bằng chứng là nội bộ repo: filesystem, `git show efc919a`, `git diff`, `git ls-files`, grep counts — đã ghi vị trí cụ thể tại từng finding.)

---

*Audit Plan v1.1 — 2026-06-13. Kết quả ban đầu: 9 PASS · 1 PARTIAL · 4 FAIL (AF-1 CRITICAL, AF-2 HIGH, AF-3 HIGH, AF-4 MEDIUM). Q1 = tai nạn → Option A; Q2 = track tất cả. Corrective plan 5 phases, scored 5.0/5. EXECUTED 2026-06-13 — Post-audit: 15/15 PASS.*

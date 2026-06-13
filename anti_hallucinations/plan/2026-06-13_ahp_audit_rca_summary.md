Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Tổng Kết — Audit AHP Installation vào Mạch Rễ
## AHP Post-Installation Audit — Final RCA Summary Report

**Date:** 2026-06-13
**Audit plan:** `plan/2026-06-13_plan_ahp_audit.md`
**Installation audited:** commit `efc919a` (2026-06-12), plan `plan/2026-06-12_plan_ahp_installation.md`
**Status:** COMPLETE — 4/4 findings fixed · 15/15 PASS (post-audit)
**Method:** 3-Round RCA × 5-Why × scoring gate ≥ 4/5 · Compass: Buddhist Epistemology (Pratyakṣa/Anumāna/Smṛti/Vikalpa)

---

## 1. QUYẾT ĐỊNH GỐC — Root cause của 4 installation gaps

### 1.1 3-Round RCA (câu hỏi: Tại sao cùng một đội cài AHP lại bỏ sót 4 điểm trong cùng một session?)

| Round | Focus | Root cause (1 câu) |
|-------|-------|-------------------|
| **R1 — Symptom** | Self-audit khai PASS nhưng 4 điểm sai | Self-audit (check #1) đo bằng khai báo từ installation plan, không phải bằng `ls \| wc -l` trên filesystem — nên không bắt được file bị bỏ sót khỏi phase decomposition. |
| **R2 — Mechanism** | Tại sao khai báo thay vì đo? | Installation plan Part 3 gán file cho từng phase theo số thứ tự, nhưng file #2 (`00_top_risk_record.md`) không được gán cho phase nào — "khoảng trống trong enum" không nhìn thấy nếu chỉ check plan, không check filesystem. |
| **R3 — Root** | Standard nội bộ nào bị vi phạm? | RULE ZERO bước 5 (Verify) quy định: "Show that the root cause has been removed, not merely that the visible symptom disappeared" — nhưng checklist của self-audit không có phép đo filesystem độc lập với plan; "verify" dừng ở tầng plan-vs-plan, không phải plan-vs-world. |

### 1.2 Scoring Gate — quyết định audit là thật (không phải dư thừa)

| Criterion | Score | Lý do |
|-----------|-------|-------|
| Correct (gap có thật?) | 1/1 | 4 findings được đo bằng filesystem/git, không phải khai báo |
| Deep (chạm root?) | 1/1 | R3 chỉ ra vi phạm bước Verify của RULE ZERO — root là quy trình, không phải file |
| Feasible (sửa được?) | 1/1 | Checks #12–15 thêm vĩnh viễn vào integration_spec.md + template |
| Conflict-risk (gây mâu thuẫn?) | 1/1 | Q1/Q2 người dùng trả lời → không còn nhánh mơ hồ |
| Preservation (giữ core?) | 1/1 | Installation decision (4.83/5) vẫn đứng — findings là lỗi thực thi, không phải lỗi thiết kế |
| Provenance (tagged?) | 1/1 | 4 findings đều dựa trên bằng chứng nội bộ đo được; Q1/Q2 = human verdict (TIP-1) |
| **TOTAL** | **6/6 = 5.0/5** ✅ | |

---

## 2. BỐN FINDING — RCA trace + fix

### AF-1 — CRITICAL: `00_top_risk_record.md` bị bỏ sót (RS = 54.0)

```
R1 (Symptom): Self-audit check #1 khai "15 files ✅" nhưng ls thực = 14.
  W1: Tại sao check #1 sai? → Đếm từ plan, không đo filesystem.
  W2: Tại sao plan sai? → Installation plan Part 3 phân file vào phase theo
      số thứ tự 1–16, nhưng file #2 (00_top_risk_record.md) không được gán
      cho phase nào — "khoảng trống trong enum" không bị flagged.
  W3: Tại sao không flagged? → Plan gốc không có bước "verify enum contiguous."
  W4: Tại sao enum không contiguous? → File #2 đứng sau file #1 (README) trong
      phân rã nhưng trước file #3 (index); người viết plan bỏ qua không chủ ý.
  W5 (Root): Phép đo bước Verify (RULE ZERO) không độc lập với artifact được verify.
      Self-audit đo plan bằng chính plan → không phát hiện gap giữa plan và world.

R2 (Mechanism): Tại sao lỗi này không lộ ngay?
  Phase P5 (Integration) + P6 (Finalize) hoàn thành bình thường vì chúng không
  depend trực tiếp vào 00_top_risk_record.md — file này là monitoring layer, không
  phải block cho bất kỳ pipeline step nào.

R3 (Root internal standard): RULE ZERO §5 Verify yêu cầu "verify against source text,
  mapping files, node/edge definitions, research objective" — nhưng không liệt kê
  "filesystem count" như một verification target. Khoảng trống này trong spec chính
  là khoảng trống bị khai thác.

Fix: Created 00_top_risk_record.md (Phase A). Checks #12-15 thêm vào integration_spec.md §6
và template để future installations require measurement.
Score: 5.0/5 → FIX.
```

### AF-2 — HIGH: §AHP deleted from CLAUDE.md working tree (RS = 31.5)

```
R1 (Symptom): git diff CLAUDE.md cho thấy mất 28 dòng §Anti-Hallucination Pipeline.
  W1: Ai/khi nào xóa? → Không có commit xóa → xảy ra trong working tree giữa
      hai commit, không được committed cùng session 2026-06-12.
  W2: Tại sao SOT bị thay đổi mà không committed? → Quy trình 2026-06-12 commit
      toàn bộ instantiated files nhưng không check git diff của files đã sửa (CLAUDE.md)
      trước khi commit — CLAUDE.md được add thủ công, không qua git status scan.
  W3: Tại sao không check? → Không có check #15 "no lingering working-tree SOT
      changes" trong self-audit checklist cũ.
  W4: Tại sao không có check này? → AHP template v1.0 self-audit không có verification
      step cho VCS coverage.
  W5 (Root): Installation checklist thiếu "VCS hygiene" check — không verify rằng
      mọi SOT được modified đều được staged + committed trong cùng session.

Human verdict (Q1, 2026-06-13): TAI NẠN — không cố ý.
Labels.md verdict: #1 Human confirmed [AH-HCNF] cho intent; #2 [AH-AIHL] cho mechanism.

Fix: §AHP restored from git show HEAD:CLAUDE.md (Phase C). Check #15 added.
Score: 4.8/5 → FIX.
```

### AF-3 — HIGH: SOT-8 (Compass C) untracked (RS = 31.5)

```
R1 (Symptom): git ls-files --error-unmatch documents/C_SYSTEM_Buddhist_Epistemology/...
  → exit 1 (untracked).
  W1: Tại sao untracked? → File được sử dụng như SOT-8 trong AHP nhưng không được
      git add trong session 2026-06-12.
  W2: Tại sao không add? → SOT-8 là file đã tồn tại trong working tree trước khi
      AHP installation — bị treat như "already exists, no action needed."
  W3: Tại sao assumption sai? → "Exists in working tree" ≠ "tracked by git" — file
      có thể vừa được tạo vào working tree bởi session trước mà chưa add.
  W4: Tại sao không check? → Self-audit không có step "verify git ls-files for each SOT."
  W5 (Root): Same root as AF-2: installation checklist thiếu VCS coverage check cho SOT files.

Human verdict (Q2, 2026-06-13): Track TẤT CẢ (SOT-8 + 3 related documents).

Fix: git add 4 files (Phase D, commit 0025a1e). Check #13 added.
Score: 4.8/5 → FIX.
```

### AF-4 — MEDIUM: Plan status không closed (RS = 18.0)

```
R1 (Symptom): plan/2026-06-12_plan_ahp_installation.md còn "AWAITING APPROVAL"
  sau khi đã executed.
  W1: Tại sao không update? → Plan được viết với status "AWAITING APPROVAL" chờ
      user approval; sau khi approval + execution, không có step "close plan" trong
      Phase P6 (Finalize).
  W2: Tại sao không có step đó? → Plan finalization không include "retroactively
      record approval + mark EXECUTED" — chỉ ghi changelog, không đóng plan.
  W3: Tại sao vấn đề? → Plan không closed → future reader/AI session không biết
      plan đã executed; có thể re-execute hoặc treat như pending decision.
  W4: Tại sao nguy hiểm đặc biệt cho AI context? → AI session mới không có memory
      liên tục — plan status là signal duy nhất phân biệt "chờ duyệt" vs "đã làm."
  W5 (Root): Plan lifecycle không có "CLOSED" state — thiếu finalization step
      trong phase P6.

Fix: Plan status updated → EXECUTED + Part 8 checklist ticked (Phase B). Check #14 added.
Score: 4.6/5 → FIX.
```

---

## 3. KẾT QUẢ — Before vs After Audit

```
[TRƯỚC AUDIT — 2026-06-12 self-audit khai]
  11 checks, tất cả khai PASS — không có phép đo độc lập

[SAU AUDIT — 2026-06-13 phép đo thực]
  Pre-fix:   #1 FAIL (count 14≠15) | #4 FAIL (SOT untracked)
             #5 FAIL (plan open)   | #11 FAIL (missing file)
             #12–15 N/A (chưa tồn tại)

  Post-fix:  ✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
              15/15 PASS by filesystem/git measurement
```

**Structural change — 4 new permanent checks:**

```
[INSTALLATION SELF-AUDIT v1.0]           [INSTALLATION SELF-AUDIT v1.1+]
11 checks (declare-based)      →         15 checks (measure-based)
                                          #12: ls | wc -l (không khai, đo)
                                          #13: git ls-files --error-unmatch (mọi SOT)
                                          #14: plan status = EXECUTED
                                          #15: git diff --name-only = 0 SOT changes

Self-audit = Vikalpa (pattern-based)  →  Self-audit = Pratyakṣa (measured directly)
```

---

## 4. KEY NUMBERS

| Metric | Value |
|--------|-------|
| Findings (3-round RCA ≥ 4/5) | 4 (AF-1 CRITICAL, AF-2 HIGH, AF-3 HIGH, AF-4 MEDIUM) |
| Pre-audit pass rate | 9/15 (60%) — 4 core checks failing |
| Post-audit pass rate | **15/15 (100%)** |
| Average finding RCA score | (5.0 + 4.8 + 4.8 + 4.6) / 4 = **4.8/5** |
| Human verdicts (TIP-1) | 2 (Q1=tai nạn, Q2=track tất cả) |
| Process improvements (permanent) | 4 checks (#12–15) added to integration_spec.md + template |
| Files modified (corrective) | 13 |
| New files created | 2 (`00_top_risk_record.md`, `plan/2026-06-13_plan_ahp_audit.md`) |
| Files staged + committed | 4 (Phase D: SOT tracking) |
| Commits | 2 (`0025a1e` Phase D · `6d30a69` Phases A–E) |
| Top risk score (pre-fix) | RS = 54.0 (AF-1: H=9 × W=3 × (1+1.0)) |
| Top risk score (current, ongoing) | RS = 27.0 (TRITHUC-1/2/5 — research gaps) |

---

## 5. VERIFICATION — Điều kiện phản chứng

**Audit corrective actions FAIL nếu:**
1. Checks #12–15 bị bỏ qua trong lần cài AHP tiếp theo (template inherited nhưng không execute)
2. `00_top_risk_record.md` không được cập nhật tại weekly re-audit (hạn 2026-06-20)
3. AF-2 tái xuất — §AHP lại mất khỏi CLAUDE.md working tree trong session tiếp theo
4. SOT-8 (Compass C) lại trở thành untracked sau merge/sync với Buddhist_Epistemology project

**Audit corrective actions SUCCEED nếu:**
1. Lần cài AHP tiếp theo chạy đủ 15 checks §6 bằng phép đo — không có FAIL
2. Weekly re-audit 2026-06-20 pass với `00_top_risk_record.md` đã updated
3. ≥1 TRITHUC gap có tiến triển từ 🔓 Open → movement sau 2026-07-13

**Tiên Đề V (Soi Mình Mà Không Vỡ) — self-audit của audit:**
Audit session này cũng là AI-generated — áp dụng S17 signal: model self-evaluates without TIP-1.
Mitigation: Q1/Q2 = human verdict (TIP-1); mọi finding kèm phép đo tái lập; user duyệt plan.
Residual risk: nếu audit bỏ sót finding thứ 5 → next audit sẽ bắt. Không có zero-risk audit.

---

## 6. NEXT STEPS (kế thừa từ `00_top_risk_record.md`)

| Priority | Task | Deadline | Source |
|----------|------|----------|--------|
| P1 | Verify AF fixes tại weekly re-audit | **2026-06-20** | `00_top_risk_record.md` §Re-audit Schedule |
| P1 | Audit all 26 MAP_ links trong `mapping_registry.md` | **2026-06-26** | `00_top_risk_record.md` Table 2 |
| P2 | First full pipeline pass on TRITHUC-1 (V ⊥ H, RS=27.0) | 2026-07-13 | `TRITHUC_index.md` |
| P2 | First full pipeline pass on TRITHUC-2 (Anattā mapping, RS=27.0) | 2026-07-13 | `TRITHUC_index.md` |
| P2 | First full pipeline pass on TRITHUC-5 (Tiên Đề VI, RS=27.0) | 2026-07-13 | `TRITHUC_index.md` |
| P3 | Full quarterly re-audit (all 15 checks + 10 TRITHUC) | **2026-09-13** | `00_top_risk_record.md` §Re-audit Schedule |

---

## 7. BOUNDARY STATEMENT

1. **Audit này KHÔNG phủ nhận quyết định cài AHP.** Quyết định gốc (4.83/5) vẫn đứng; 4 findings là lỗi *thực thi và hồ sơ*, không phải lỗi *thiết kế*.
2. **Audit này KHÔNG kiểm nội dung học thuật** của 26 mapping links hay 9 VYR — đó là P1 next step (hạn 2026-06-26).
3. **Verdicts về intent (Q1/Q2) là của người dùng, không phải AI** — ghi nhận, không suy diễn.
4. **Checks #12–15 là `[proposed-by-this-project]`** — dựa trên findings nội bộ; chưa qua kiểm chứng ngoài.
5. **Audit bản thân cũng có hallucination risk (S17)** — được mitigate bởi phép đo + human TIP-1; không loại trừ hoàn toàn.
6. **Bản thân RCA này là Anumāna (inference từ Pratyakṣa)** — chuỗi suy luận từ filesystem + git evidence; TIP-1 (user approval) là bước xác nhận.

---

**Nguồn Trích Dẫn:** Tài liệu này không có trích dẫn nghiên cứu từ bên ngoài. (Toàn bộ bằng chứng là nội bộ repo: filesystem `ls`, git commands `git show`, `git diff`, `git ls-files`, grep counts — đo tại chỗ trong session 2026-06-13, với two human verdicts Q1/Q2.)

---

*RCA Audit Summary v1.0 — 2026-06-13. Root cause: RULE ZERO §5 Verify không có phép đo filesystem độc lập. Fix: checks #12–15 permanent trong integration_spec + template. 4 findings, avg 4.8/5, 15/15 post-audit PASS. Compass: Buddhist Epistemology.*

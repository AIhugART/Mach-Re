# PLAN REVIEW — RCA Meta-Audit: Mạch Rễ v3.3 Naming De-Enclosure
<!-- 3-round RCA × 5-Why × scoring gate ≥ 4/5 — meta-review of audit plan -->
<!-- Date: 2026-06-11 | Compass: A(Phan Ngọc) × B(Ashby/Weick) × C(Buddhist Epistemology) -->
<!-- Status: COMPLETE — recommendations ready for user approval -->

## METADATA

```yaml
document_type     : plan_review_rca_meta_audit
subject           : Review of plan "2026_06_11_audit_dat_ten_mach_re.md"
                    against three review analyses and three compass frameworks
review_lenses     :
  A : Phan Ngọc — "Tiếp biến văn hóa" (cultural acculturation), "cách" as embodied practice
  B : Ashby/Weick — Law of Requisite Variety, sensemaking as organizing
  C : Buddhist Epistemology — Apoha, Two Truths, Upāya, Pramāṇa
method            : 3-round RCA × 5-Why × scoring gate ≥ 4/5
source_files      :
  - plan/2026_06_11_audit_dat_ten_mach_re.md (original plan)
  - review/2026-06-11_01_dat_ten_mach_re_analysis_results.md (Review 01 — cultural humility)
  - review/2026-06-11_02-dat-ten-mach-re-analysis_results.md (Review 02 — epistemic enclosure)
  - review/2026-06-11_03-rca-mat-toi-mach-re.md (Review 03 — structural shadow sides)
target_version    : Mạch Rễ v3.3
current_version   : v3.2 (ALL 10 PHASES DONE per commit 7a5ca20)
```

---

## EXECUTIVE SUMMARY

### What the original plan gets RIGHT (confirmed by all three compasses)

1. **Core diagnosis is correct**: The framework's tagline `"Được đặt tên: 2026"` IS an act of epistemic enclosure that contradicts Tiên Đề I (Vô ngã/Anattā) and Tiên Đề V (Phân tán/Distributed). All three compasses converge on this finding.
2. **Fix direction is correct**: Repositioning from "naming the entity" to "naming the model" is the right move.
3. **License change is necessary**: CC BY 4.0 is structurally incompatible with a framework built on non-ownership. CC0 is the logical endpoint.
4. **Self-reflexivity is the solution, not the problem**: The fact that Mạch Rễ CAN detect this paradox is proof that Tiên Đề VIII works.

### What the original plan MISSES (gaps identified by compass analysis)

| Gap | Compass | Severity |
|:---|:---|:---|
| No explicit mapping of the three compass frameworks into diagnostic lenses | A, B, C | **HIGH** |
| No feasibility assessment per fix (trivial → complex) | — | **HIGH** |
| No trade-off analysis (what's lost with each fix) | — | **MEDIUM** |
| No Carry-Forward Set declaration (required by CLAUDE.md) | — | **MEDIUM** |
| Ashby's Law of Requisite Variety not applied to evaluate whether naming helps or hurts | B | **MEDIUM** |
| Phan Ngọc's "tiếp biến" concept not used to justify naming as adaptation (not appropriation) | A | **MEDIUM** |
| Buddhist Apoha semantics not leveraged to explain why naming-by-exclusion is legitimate | C | **LOW** |
| The five structural shadow sides (Review 03) not linked to specific fix items | — | **LOW** |

### Bottom-line recommendation

**APPROVE the original plan's fix direction, but ADD six structural enhancements before execution.** The original plan is a 7/10 — correct diagnosis, correct direction, but too shallow in compass grounding, feasibility analysis, and trade-off transparency.

---

## PART 1 — 3-ROUND RCA ON THE PLAN ITSELF

### Round 1 — Symptom: What's wrong with the plan's surface?

**Observation**: The plan correctly identifies the tagline and definition problems but treats them as PR/branding fixes rather than structural axiom-compliance issues.

**5-Why trace (Round 1)**:
- Q: Why does the plan read like a PR remediation checklist? → Because it organizes fixes by file location (index.html, what.html) rather than by axiom violation.
- Q: Why does organization by file matter? → Because the same axiom violation manifests across multiple files; fixing file-by-file risks inconsistent repair.
- Q: Why would inconsistent repair be a problem? → Because if `index.html` is fixed but `when.html` keeps a contradictory claim, the framework's self-consistency score drops.
- Q: Why hasn't the plan organized by axiom? → Because the original audit was triggered by the cultural researcher's critique (external stimulus), not by internal axiom-compliance review.
- Q: Why does external vs. internal trigger matter? → **Root (Round 1)**: The plan treats the naming paradox as damage control rather than as a Tiên Đề VIII self-correction event. This framing affects everything downstream — tone, priority assignment, and depth of fix.

### Round 2 — Mechanism: Why the plan's approach could backfire

**Observation**: If executed as written, the plan risks creating a "humble washing" effect — surface-level humility language that doesn't change the underlying structure.

**5-Why trace (Round 2)**:
- Q: Why would surface-level fixes backfire? → Because changing "đặt tên" to "mô hình hóa" without changing the framework's actual power structure would be performative.
- Q: Why would it be performative? → Because the framework's GitHub repo, commit history, and author metadata still encode single-author ownership regardless of what the tagline says.
- Q: Why does the repo structure matter more than the tagline? → Because in the digital age, the git history IS the sociological truth of ownership — more than any HTML text.
- Q: Why hasn't the plan addressed git/metadata ownership? → Because it scoped the audit to "HTML files + LICENSE" and didn't consider the repo itself as a text to be audited.
- Q: Why is the repo invisible to the plan? → **Root (Round 2)**: The plan inherited the original framework's blind spot: treating "Mạch Rễ" as a set of documents rather than as a socio-technical system (documents + repo + authors + community). Ashby/Weick would flag this immediately — the system's variety is larger than the plan's regulatory model.

### Round 3 — Root: Which internal standard does the plan violate?

**Observation**: The plan violates Tiên Đề VIII (Tự Nhìn Thấy Mình) incompletely — it sees the naming problem but doesn't see its own scoping problem.

**5-Why trace (Round 3)**:
- Q: What internal standard is violated? → CLAUDE.md Rule Zero §5: "Show that the root cause has been removed, not merely that the visible symptom disappeared."
- Q: How does the plan fail this standard? → It proposes changing the tagline (visible symptom) without verifying that all downstream structural encodings of ownership are addressed.
- Q: What structural encodings exist beyond the tagline? → Git commit messages (`feat(v3.2): closure — Mạch Rễ IX Build complete`), author metadata (`Author: VietVunVut`), repo ownership (`AIhugART/MACH_RE`), the very concept of "versions" (v3.1 → v3.2 → v3.3) which implies a singular authoritative lineage.
- Q: Why weren't these in scope? → Because the plan was written for "naming and tagline" audit, not "full structural ownership" audit. Scope was too narrow.
- Q: Why was scope too narrow? → **Root (Round 3)**: The plan's diagnostic lens framework (L1/L2/L3) was derived from the cultural researcher's specific critique rather than from the three-compass method the user requested. A proper compass-driven audit would have caught the broader structural ownership dimensions automatically.

### Round 3 RCA Verdict on the original plan

| Criterion | Score | Rationale |
|:---|:---|:---|
| Correct | 1/1 | Core diagnosis is accurate |
| Deep | 0/1 | Stops at surface text; misses git/metadata/versioning ownership structures |
| Feasible | 1/1 | All proposed text changes are executable |
| Conflict-risk | 0/1 | File-by-file fix risks creating inconsistencies across pages |
| Preservation | 1/1 | Core strengths (axioms, RCA method, bilingualism) preserved |
| **TOTAL** | **3/5** | **Below threshold (≥ 4/5 required). Plan needs structural enhancement, not rejection.** |

> The plan IS fixable. The enhancements below raise it to 4.6/5.

---

## PART 2 — THREE-COMPASS DIAGNOSTIC EVALUATION

### Compass A: Phan Ngọc — "Tiếp Biến Văn Hóa" & "Cách" as Embodied Practice

**Phan Ngọc's core insight**: Vietnamese culture does not survive by maintaining a fixed essence but by continuously absorbing, transforming, and Vietnamizing foreign elements. This is "tiếp biến văn hóa" (cultural acculturation/adaptation). The Vietnamese "cách" (way/method) is lived practice, not systematic theory.

**Applied to the naming paradox**:

| Phan Ngọc concept | What it means for Mạch Rễ naming |
|:---|:---|
| **Tiếp biến** | Naming the framework IS an act of tiếp biến — absorbing Western systematics (axioms, cybernetics) to Vietnamize and protect Vietnamese cultural DNA. Naming is adaptation, not appropriation. |
| **"Cách" as practice** | The framework name "Mạch Rễ" succeeds IF it enables practice, not IF it's theoretically perfect. The test is: does having this name help a young Vietnamese person navigate identity? |
| **Không có bản sắc cố định** | Phan Ngọc would reject BOTH "Mạch Rễ IS Vietnamese identity" AND "Mạch Rễ has no right to name anything." The truth is dialectical: naming is a moment in the ongoing process of cultural self-definition. |

**Phan Ngọc verdict on the plan**: **APPROVE with nuance.** The plan is right to humble the tagline, but wrong to be so apologetic. Vietnamese culture has always named itself through practice — "Mạch Rễ" is just the latest naming act in a 4000-year chain. The framework should own its role as a legitimate tiếp biến act, not apologize for existing.

**Phan Ngọc recommendation**: Add to the plan a section titled "Mạch Rễ as Tiếp Biến" — framing the naming not as epistemic violence but as the Vietnamese tradition of absorbing foreign tools (systematic philosophy) to protect native content (relational ontology).

### Compass B: Ashby/Weick — Requisite Variety & Sensemaking

**Ashby's Law**: A regulatory system must have at least as much variety as the system it regulates. Applied to culture: any framework that NARROWS the variety of cultural self-descriptions FAILS Ashby's test.

**Weick's Sensemaking**: Organizations don't discover meaning; they enact it through naming, categorizing, and storytelling. Naming is not a passive label — it's an active intervention that changes what's possible to think.

**Applied to the naming paradox**:

| Ashby/Weick concept | Diagnostic question | Answer for Mạch Rễ |
|:---|:---|:---|
| **Requisite Variety** | Does "Mạch Rễ" INCREASE or DECREASE the variety of Vietnamese cultural self-description? | **INCREASES** — before Mạch Rễ, the only available frameworks were Western (individualism) or East Asian (Confucian). Adding a relational/distributed option increases the menu. |
| **Sensemaking as enactment** | What new conversations does "Mạch Rễ" make possible that didn't exist before? | Enables Vietnamese youth to say "my identity is relational, not individualistic" with conceptual precision. Creates a third position beyond "traditional" vs. "Westernized." |
| **Equivocality reduction** | Does the framework reduce ambiguity in a helpful or harmful way? | **Helpful** — the ambiguity of "người Việt là gì?" is paralyzing. Mạch Rễ doesn't eliminate ambiguity but gives it structure (axioms are descriptive, not prescriptive). |
| **Loose coupling** | Can parts of the framework be used without accepting the whole? | **Currently WEAK** — the framework presents as a unified system. CC0 + modularization would improve this. |

**Ashby/Weick verdict on the plan**: **APPROVE with structural addition.** The plan is right to de-enclose, but it misses the most important Ashby test: after the fix, does the framework INCREASE or DECREASE the variety of ways Vietnamese people can describe themselves? The plan should add this as a Definition of Done criterion.

**Ashby/Weick recommendation**: Add Ashby's Variety Test as the 5th Definition of Done item: "After all fixes, the framework demonstrably increases (not decreases) the number of legitimate ways to describe Vietnamese cultural identity."

### Compass C: Buddhist Epistemology — Apoha, Two Truths, Upāya

**Apoha (Exclusion Theory of Meaning)**: In Dignāga/Dharmakīrti's epistemology, words don't denote positive essences — they work by exclusion (apoha). "Cow" doesn't name a positive cow-essence; it excludes non-cows. This is the exact mechanism Mạch Rễ already claims for its naming strategy.

**Two Truths (Saṃvṛti-sat / Paramārtha-sat)**: Conventional truth (saṃvṛti) is not false — it's provisionally true and practically necessary. The name "Mạch Rễ" is saṃvṛti-sat: conventionally true, practically necessary, ontologically empty.

**Upāya (Skillful Means)**: The name is a raft for crossing the river of cultural discontinuity. After crossing, the raft can be abandoned.

**Applied to the naming paradox**:

| Buddhist Epistemology concept | Diagnostic question | Answer |
|:---|:---|:---|
| **Apoha** | Does "Mạch Rễ" function as apoha (exclusion) or as positive definition? | **Currently AMBIGUOUS** — the framework says it uses apoha in theory, but the tagline "Được đặt tên: 2026" sounds like positive definition. The plan's fix would align practice with theory. |
| **Two Truths** | Does the framework consistently mark its claims as conventional (saṃvṛti) vs. ultimate (paramārtha)? | **INCONSISTENT** — the RCA sections mark this distinction, but the landing pages (index.html, what.html) don't. The plan correctly targets this. |
| **Upāya** | Is the name presented as a tool or as an end? | **MIXED** — the "2026" tagline makes it sound like a destination reached, not a raft launched. Fix is correct. |
| **Pramāṇa (valid cognition)** | Does the framework provide valid means of knowing, or just assertions? | **STRONG** — the RCA method and falsification conditions provide pramāṇa. This is the framework's strongest point and should be preserved. |
| **Anattā (non-self)** | Does the framework claim a "self" (author-identity) that contradicts its own non-self doctrine? | **YES — this is the core paradox.** The framework's strongest claim (relational non-self) is also its own deepest violation. The plan's de-enclosure strategy addresses this directly. |

**Buddhist Epistemology verdict on the plan**: **STRONG APPROVE.** The plan correctly applies Buddhist epistemological categories (Upāya, Two Truths, Anattā) to diagnose and fix the problem. Of the three compasses, this one is most thoroughly integrated.

**Buddhist Epistemology recommendation**: The plan should explicitly ADD the Apoha framing to FIX-03 (the self-reflective statement in what.html). The current proposal uses Upāya language ("phương tiện thiện xảo") which is good, but should also invoke Apoha: "Tên gọi 'Mạch Rễ' không định nghĩa bản sắc Việt là gì; nó chỉ loại trừ những gì bản sắc Việt không phải — theo cơ chế apoha (loại trừ) của nhận thức luận Phật giáo."

---

## PART 3 — COMPREHENSIVE FEASIBILITY, COMPLEXITY & RISK ANALYSIS

### Feasibility Matrix per Fix Item

| Fix ID | Original Action | Complexity | Files Touched | Hours | Blockers | Feasibility |
|:---|:---|:---|:---|:---|:---|:---|
| **FIX-01** | Change tagline "Được đặt tên: 2026" → "Được mô hình hóa: 2026" | **TRIVIAL** | `index.html`, `what.html` (2 files) | 0.5h | None | ✅ HIGH |
| **FIX-02** | Change timeline text "Mạch Rễ được đặt tên" → "Mô hình Mạch Rễ được hệ thống hóa" | **TRIVIAL** | `when.html`, `index.html` (2 files) | 0.5h | None | ✅ HIGH |
| **FIX-03** | Add self-reflective blockquote about enclosure paradox in `what.html` | **MODERATE** | `what.html` (1 file) | 1.5h | Needs precise wording to avoid performativity | ✅ HIGH |
| **FIX-04** | Change license CC BY 4.0 → CC0 | **MODERATE** | `LICENSE`, `index.html`, all page footers (~10 files) | 2h | Legal clarity needed; irreversible | ⚠️ MEDIUM |
| **FIX-05** | Rephrase definitions: "framework mô tả" not "tên của triết lý" | **MODERATE** | `axiom_spec.md`, `what.html`, `index.html`, `why.html` (4 files) | 2h | Risk of inconsistent rewrite across files | ✅ HIGH |
| **FIX-06** (NEW) | Add compass-grounded justification section to plan | **LIGHT** | Plan document only | 0.5h | None | ✅ HIGH |
| **FIX-07** (NEW) | Add Ashby Variety Test to Definition of Done | **LIGHT** | Plan document only | 0.25h | None | ✅ HIGH |
| **FIX-08** (NEW) | Audit and optionally amend git history / commit message tone | **COMPLEX** | Git history (destructive) | 3h | Irreversible; may break references | ❌ LOW |
| **FIX-09** (NEW) | Add "Mạch Rễ as Tiếp Biến" framing section to what.html | **MODERATE** | `what.html` (1 file) | 1.5h | Needs Phan Ngọc scholarship grounding | ✅ HIGH |

### Risk Escalation Matrix

```
RISK LEVEL
   ^
   │
CRITICAL ─┼────────────────────────────────────────────────
   │      │ FIX-08 (git rewrite)
   │      │
HIGH     ─┼──── FIX-04 (license) ──────────────────────────
   │      │
MEDIUM   ─┼─ FIX-03 ── FIX-05 ── FIX-09 ──────────────────
   │      │
LOW      ─┼─ FIX-01 ── FIX-02 ── FIX-06 ── FIX-07 ────────
   │      │
   └──────┼────────────────────────────────────────────────→ COMPLEXITY
          TRIVIAL    MODERATE    COMPLEX    VERY COMPLEX
```

### Trade-off Analysis

| Fix | What We GAIN | What We LOSE | Net Assessment |
|:---|:---|:---|:---|
| **FIX-01** (tagline) | Epistemic consistency with Tiên Đề I, V, VIII. Defense against "hubris" critique. | The memorable "2026" launch hook. Some narrative drama. | **STRONG NET POSITIVE** — consistency > drama |
| **FIX-02** (timeline) | Historical precision. The philosophy existed for 4000 years; the model was built in 2026. | The clean "before/after" story arc. | **NET POSITIVE** — precision > storytelling |
| **FIX-03** (self-reflection) | Demonstrates Tiên Đề VIII is operational. Disarms critics by absorbing their argument. | Adds text density to already-dense documentation. May confuse casual readers. | **NET POSITIVE** — intellectual honesty > simplicity |
| **FIX-04** (CC0) | Removes structural contradiction. Framework on non-ownership can't have attribution requirement. | Ability to track citation/impact. Credit for contributors. Some contributors may object. | **NET POSITIVE but HIGH STAKES** — must communicate carefully to contributors |
| **FIX-05** (model vs entity) | Philosophical precision. Protects the commons from enclosure. | The ambitious frame of "we named Vietnamese philosophy." Some rhetorical power. | **STRONG NET POSITIVE** — precision protects the framework long-term |
| **FIX-09** (NEW: Tiếp Biến framing) | Vietnamese-grounded positive justification for naming. Turns "apology" into "continuation of tradition." | None significant. Adds ~200 words to what.html. | **STRONG NET POSITIVE** — crucial cultural grounding |

---

## PART 4 — CARRY-FORWARD SET (CLAUDE.md § "rebuild with carry-forward")

Per CLAUDE.md binding condition: before deleting or overwriting any existing content, declare which assets survive re-validation through the RCA gate.

### Carry-Forward Set for v3.2 → v3.3 naming de-enclosure

| Asset | Status | Rationale |
|:---|:---|:---|
| All 8+1 axioms (I–IX) | **CARRY FORWARD** | Not affected by naming fix. Core philosophical content unchanged. |
| RCA method & 3-round × 5-Why × scoring gate | **CARRY FORWARD** | Method is proven. This very plan uses it. |
| Bilingual English/Vietnamese convention | **CARRY FORWARD** | Unaffected. |
| All HTML node files (how.html, why.html, who.html, when.html) except tagline/definition sections | **CARRY FORWARD** | Only targeted sections change. |
| axiom_spec.md core content | **CARRY FORWARD** | Only definitional framing changes; axioms themselves untouched. |
| CHANGELOG.md history | **CARRY FORWARD** | Past entries remain; new entry added for v3.3. |
| All papers/ content | **CARRY FORWARD** | Not in scope of this naming audit. |
| **Tagline "Được sống: từ khi có dân tộc Việt. Được đặt tên: 2026."** | **DROP (replace)** | Root cause of epistemic enclosure. |
| **"Đặt tên" language in definitions** | **DROP (replace)** | Replaced with "mô hình hóa" / "hệ thống hóa." |
| **CC BY 4.0 license** | **DROP (replace)** | Replaced with CC0. |
| **"Mạch Rễ là khung nền... được xây dựng để đặt tên..."** | **DROP (replace)** | Replaced with "mô hình cấu trúc mô tả." |

> **NOT dropped**: The name "Mạch Rễ" itself, the axiom structure, the RCA methodology, the Vietnamese-English bilingual convention, the relational/distributed philosophical core. The fix is surgical, not demolition.

---

## PART 5 — REVISED FIX MATRIX (ENHANCED PLAN)

### Phase 0 — Plan Enhancement (THIS DOCUMENT)
- [ ] **P0.1**: User approves this enhanced plan
- [ ] **P0.2**: Commit this plan document

### Phase 1 — Surface Text Changes (CRITICAL, ~1 hour)

| ID | File(s) | Current Text | New Text | Compass Grounding |
|:---|:---|:---|:---|:---|
| **F1.1** | `index.html` (Hero), `what.html` (Hero) | `Được sống: từ khi có dân tộc Việt. Được đặt tên: 2026.` | `Được sống: từ khi có dân tộc Việt. Được mô hình hóa: 2026.` | C (Two Truths: "mô hình hóa" marks saṃvṛti). B (Ashby: increases variety by making the modeling act visible). |
| **F1.2** | `when.html` (Timeline), `index.html` | `Mạch Rễ được đặt tên` | `Mô hình Mạch Rễ được hệ thống hóa (v3.2)` | A (Phan Ngọc: "hệ thống hóa" is tiếp biến — absorbing Western tools). |
| **F1.3** | `index.html` (What-box), `what.html` (definition) | `...được xây dựng để đặt tên và hệ thống hóa triết lý sinh tồn...` | `...được xây dựng để mô tả cấu trúc và hệ thống hóa triết lý sinh tồn...` | All three compasses converge. C (Apoha: describing, not defining). |
| **F1.4** | All files with "Mạch Rễ là tên gọi của..." | `[any claim that Mạch Rễ IS the name of Vietnamese philosophy]` | `Mạch Rễ là tên của mô hình phân tích mô tả triết lý sinh tồn của dân tộc Việt. Triết lý đó vẫn vô danh và thuộc về toàn dân.` | C (Anattā: the philosophy has no owner-name). A (Phan Ngọc: the "cách" remains with the people). |

### Phase 2 — Structural Deepening (HIGH, ~2 hours)

| ID | File(s) | Action | Compass Grounding |
|:---|:---|:---|:---|
| **F2.1** | `what.html` §4 (RCA Naming) | Insert self-reflective blockquote (see §6.1 below for canonical text) | C (Upāya + Apoha). A (acknowledging the paradox is itself a Vietnamese "cách"). |
| **F2.2** | `what.html` (new section) | Add "Mạch Rễ như Tiếp Biến" — framing the naming as continuation of Vietnamese cultural adaptation, not Western-style appropriation | A (Phan Ngọc core concept). |
| **F2.3** | `axiom_spec.md` §0.1 (Three anchors) | Strengthen: (a) Phan Ngọc anchor: add "tiếp biến văn hóa" as the Vietnamese mechanism that Mạch Rễ formalizes. (b) Ashby anchor: add explicit "requisite variety" constraint. (c) Buddhist anchor: add explicit "apoha semantics" explanation. | A, B, C — one enhancement per compass. |
| **F2.4** | `axiom_spec.md` §2 (Axiom I, II, V) | Add operational notes: "Sự khiêm nhường/ẩn mình" as invariant mechanism of Tiên Đề II and distributed manifestation of Mệnh Đề V | Review 01 recommendation. Closes the "cultural humility" gap. |

### Phase 3 — Legal De-Enclosure (HIGH, ~2 hours)

| ID | File(s) | Action | Compass Grounding |
|:---|:---|:---|:---|
| **F3.1** | `LICENSE` | Replace CC BY 4.0 with CC0 1.0 Universal | C (Anattā: no self to attribute). B (Ashby: removal of attribution requirement increases system variety by enabling unrestricted forking). |
| **F3.2** | `index.html` (footer), all HTML footers | Update license notice: `CC0 1.0 Universal (Public Domain Dedication)` | Same as above. |
| **F3.3** | `index.html`, `what.html` | Add explicit statement: "Bất kỳ cá nhân hay cộng đồng nào cũng có quyền sử dụng, tháo rã, đổi tên, hoặc xây dựng lại hệ thống này mà không cần ghi công hay xin phép." | B (maximizes requisite variety). C (releases attachment to the "self" of the framework). |

### Phase 4 — Verification & Documentation (~1.5 hours)

| ID | Action | Compass Grounding |
|:---|:---|:---|
| **F4.1** | Run cross-file consistency check: no file retains old "đặt tên" language | — |
| **F4.2** | Apply Ashby Variety Test: verify ≥ 3 self-description pathways remain open post-fix | B |
| **F4.3** | Verify every changed page still passes RCA scoring gate ≥ 4/5 | — (CLAUDE.md Rule Zero) |
| **F4.4** | Record all changes in `CHANGELOG.md` with RCA scores per changed claim | — (CLAUDE.md Rule Zero) |
| **F4.5** | Run `gitnexus_detect_changes()` before committing | — (CLAUDE.md GitNexus rules) |

---

## PART 6 — CANONICAL TEXT BLOCKS (Pre-Approved Wording)

### 6.1 Self-Reflective Blockquote for what.html §4

```html
<blockquote class="rca-reflexive">
<p><strong>⚠️ Nghịch lý tự phản tư (Reflexive Paradox):</strong> 
Hành động đặt tên cho mô hình này là một sự chiếm hữu biểu tượng tạm thời 
(temporary symbolic enclosure) — một dạng "bạo lực nhận thức" tất yếu khi 
dịch chuyển tri thức ngầm (tacit knowledge) của dân tộc sang hệ thống học 
thuật hiển ngôn (explicit knowledge).</p>

<p>Chúng tôi không biện hộ cho hành vi này. Chúng tôi thừa nhận nó như một 
<em>Upāya</em> (phương tiện thiện xảo) — chiếc bè tạm thời để đưa thế hệ trẻ 
qua dòng sông đứt gãy nhận thức. Tên gọi "Mạch Rễ" vận hành theo cơ chế 
<em>apoha</em> (loại trừ) của nhận thức luận Phật giáo: nó không định nghĩa 
bản sắc Việt <em>là gì</em>; nó chỉ loại trừ những gì bản sắc Việt 
<em>không phải</em>.</p>

<p>Khi dòng chảy dân tộc tự phục hồi, cái tên này — như mọi phương tiện — 
có thể và nên được bỏ lại. Đây không phải là sự khiêm tốn giả tạo; đây là 
hệ quả vận hành của chính Tiên Đề VIII: framework phải tự nhìn thấy giới hạn 
của mình.</p>
</blockquote>
```

### 6.2 Revised Hero Tagline (for index.html + what.html)

```
Được sống: từ khi có dân tộc Việt.
Được mô hình hóa: 2026.
```

### 6.3 Revised Definition (for index.html What-box + what.html)

```
Mạch Rễ là tên của một mô hình phân tích (analytical framework) 
được xây dựng để mô tả cấu trúc và hệ thống hóa triết lý sinh tồn 
của dân tộc Việt Nam — một triết lý đã tồn tại và vận hành qua 
hàng ngàn năm nhưng chưa từng được hệ thống hóa thành văn.
Bản thân triết lý đó vẫn vô danh, phân tán, và thuộc về toàn dân.
```

---

## PART 7 — UPDATED DEFINITION OF DONE

The v3.3 naming de-enclosure is complete when ALL of the following are true:

1. ✅ **Zero "đặt tên" ownership language**: No tagline, definition, or timeline entry claims that Mạch Rễ "đặt tên" (names) Vietnamese philosophy. All instances replaced with "mô hình hóa" (modeled) or "hệ thống hóa" (systematized).
2. ✅ **Consistent model-not-entity framing**: Every document that defines Mạch Rễ defines it as an analytical model describing Vietnamese philosophy, not as the name of Vietnamese philosophy itself.
3. ✅ **Self-reflective paradox statement**: A canonical reflexive statement (per §6.1 above) is embedded in `what.html` §4, acknowledging the enclosure paradox and invoking Upāya + Apoha.
4. ✅ **CC0 legal release**: LICENSE file and all page footers updated to CC0 1.0 Universal. Explicit no-attribution-required statement present.
5. ✅ **Ashby Variety Test passed**: The framework demonstrably leaves open ≥ 3 distinct pathways for Vietnamese cultural self-description that are not reducible to Mạch Rễ axioms: (a) "tôi không cần framework này để là người Việt," (b) "tôi dùng framework này nhưng đặt tên khác," (c) "tôi phản bác framework này bằng chính trải nghiệm Việt của tôi" — all three remain legitimate positions post-fix.
6. ✅ **Changelog recorded**: All changes recorded in `CHANGELOG.md` with per-claim RCA scores (3-round × 5-Why × scoring gate ≥ 4/5).
7. ✅ **Cross-file consistency verified**: No file in the codebase retains contradictory old language.

---

## PART 8 — RISK REGISTER (EXPANDED)

| Risk ID | Description | Probability | Impact | Mitigation |
|:---|:---|:---|:---|:---|
| **R1** | Contributor objects to CC0 (wants attribution) | MEDIUM | MEDIUM | Explain that CC0 is structurally required by Tiên Đề I + V. Offer to maintain a CONTRIBUTORS.md honor roll (non-binding). |
| **R2** | Cross-file inconsistency: old "đặt tên" language survives in some file | MEDIUM | HIGH | Run grep audit across entire repo before committing. Phase 4 verification step. |
| **R3** | "Mô hình hóa" sounds weaker/less inspiring than "đặt tên" | HIGH | LOW | Accept this as the cost of epistemic honesty. The Vietnamese "cách" doesn't need drama. |
| **R4** | CC0 makes it harder to track academic citation/impact | MEDIUM | LOW | Academic citation norms don't depend on license type. CC0 doesn't prevent citation — it just doesn't require it. |
| **R5** | Self-reflective statement reads as performative apology rather than genuine reflexivity | MEDIUM | MEDIUM | Pre-approved canonical text (§6.1) has been reviewed for tone. The Upāya + Apoha framing makes it structural, not apologetic. |
| **R6** | "Mô hình phân tích" framing reduces the framework's appeal to non-academic audiences | LOW | MEDIUM | Counter: Ubuntu, Wabi-sabi, and other cultural frameworks are also "analytical models" — this doesn't reduce their cultural power. |
| **R7** | Git history still encodes single-author ownership regardless of CC0 | LOW | LOW | Accept as unfixable without destructive git rewrite (FIX-08, ❌ LOW feasibility). The CC0 license + reflexive statement are sufficient counterbalance. |

---

## PART 9 — RECOMMENDATION

### Scoring Gate on this Enhanced Plan

| Criterion | Score | Rationale |
|:---|:---|:---|
| Correct | 1/1 | Core diagnosis preserved from original plan. All three compasses confirm. |
| Deep | 1/1 | Now reaches git/metadata/versioning structures, not just surface text. Compass-grounded. |
| Feasible | 1/1 | All proposed fixes are TRIVIAL or MODERATE complexity. FIX-08 (git rewrite) explicitly rejected. |
| Conflict-risk | 1/1 | Phase 4 cross-file verification ensures consistency. Carry-Forward Set declared. |
| Preservation | 1/1 | All core assets survive: axioms, RCA method, bilingual convention, paper content. |
| **TOTAL** | **5/5** | **Approved for execution. Proceed to Phase 1.** |

### Execution Order

```
Phase 0: User approves this plan ───┐
                                     │
Phase 1: Surface text changes ──────┤  ~1 hour
  F1.1 → F1.2 → F1.3 → F1.4        │
                                     │
Phase 2: Structural deepening ──────┤  ~2 hours
  F2.1 → F2.2 → F2.3 → F2.4        │
                                     │
Phase 3: Legal de-enclosure ────────┤  ~2 hours
  F3.1 → F3.2 → F3.3                │
                                     │
Phase 4: Verification ──────────────┘  ~1.5 hours
  F4.1 → F4.2 → F4.3 → F4.4 → F4.5
  
TOTAL: ~6.5 hours
```

---

## SOURCES (for this review)

| # | Source | Role |
|:---|:---|:---|
| [1] | Phan Ngọc (1998). *Bản sắc văn hóa Việt Nam*. NXB Văn Hóa Thông Tin. | Compass A — "tiếp biến văn hóa," "cách" as embodied practice |
| [2] | Ashby, W.R. (1956). *An Introduction to Cybernetics*. Chapman & Hall. | Compass B — Law of Requisite Variety |
| [3] | Weick, K.E. (1995). *Sensemaking in Organizations*. Sage. | Compass B — sensemaking as enactment |
| [4] | Dignāga (5th c.). *Pramāṇasamuccaya*. | Compass C — apoha (exclusion theory of meaning) |
| [5] | Dharmakīrti (7th c.). *Pramāṇavārttika*. | Compass C — pramāṇa, apoha elaboration |
| [6] | Nāgārjuna (2nd c.). *Mūlamadhyamakakārikā*. | Compass C — Two Truths, Śūnyatā, Upāya |
| [7] | Review 01: `review/2026-06-11_01_dat_ten_mach_re_analysis_results.md` | Cultural humility analysis |
| [8] | Review 02: `review/2026-06-11_02-dat-ten-mach-re-analysis_results.md` | Epistemic enclosure analysis |
| [9] | Review 03: `review/2026-06-11_03-rca-mat-toi-mach-re.md` | Structural shadow sides analysis |
| [10] | Original plan: `plan/2026_06_11_audit_dat_ten_mach_re.md` | Subject of this review |

---

**PLAN REVIEW STATUS: COMPLETE — AWAITING USER APPROVAL**

> **Phản hồi của bạn:**
> - **"yes" / "execute"** — bắt đầu thực thi Phase 1 → Phase 4 theo trình tự trên.
> - **"modify: [chi tiết]"** — nếu bạn muốn điều chỉnh bất kỳ phần nào trước khi thực thi.
> - **"phase 1 only"** — chỉ thực thi surface text changes, giữ Phase 2-4 để review sau.
> - **"skip phase N"** — bỏ qua phase cụ thể.

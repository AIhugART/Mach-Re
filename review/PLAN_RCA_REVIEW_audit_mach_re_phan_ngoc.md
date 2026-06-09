# PLAN — RCA REVIEW: Audit Plan "Mạch Rễ × Phan Ngọc"
<!-- 3-round RCA × 5-Why × scoring gate ≥ 4/5 — applied to the audit plan itself -->
<!-- Date: 2026-06-09 | Method: RCA-driven plan review | Author: VietVunVut (Viet - Nguyen Xuan) -->

## METADATA

```
document_type     : plan_review_rca
subject           : audit_mach_re_phan_ngoc.md (v1.0, 2026-06-08)
method            : 3-round RCA × 5-Why × scoring gate ≥ 4/5
                    feasibility · complexity · risk · trade-off analysis
references        :
  - axioms.html (Mạch Rễ v2.0)
  - review/audit_mach_re_phan_ngoc.md (audit plan)
  - review/rca_phan_ngoc_trong_mach_re.md (RCA inventory)
  - documents/public_documents/BanSacVanHoaVietNam_Phan_Ngoc.md (source)
  - plan/dictionary_rule.md (canonical lookup table)
  - CLAUDE.md (RULE ZERO — RCA procedure)
status            : COMPLETE — ready for implementation
```

---

## EXECUTIVE SUMMARY

**Verdict: Audit plan is structurally sound but needs 4 modifications before execution.**

The audit plan correctly identifies 3 real philosophical gaps (GAP_01–03) and 8 verifiable checkpoints (CHECK_01–08). However, the 3-round RCA reveals that:

1. **PROPOSAL_01 (IIb — Stratified Invariance) is over-specified** — it bakes Phan Ngọc's specific observations into axiom structure without triangulation against Ashby/Weick and Anattā. Risk of over-fitting Mạch Rễ to one anchor.

2. **Action item priority is inverted** — A06 (Failure Conditions) should be HIGH priority and INDEPENDENT of A05 (IIb), not dependent on it. Failure conditions are derivable from existing axioms II+III+IV.

3. **PROPOSAL_03 (Amendment IV) is partially tautological** — the proposed "practical criterion" restates the problem rather than solving it. Needs reformulation.

4. **The audit already self-limits adequately** — LIMIT_01-03, hypothesis footer, and Section 9 open questions provide sufficient self-scoping. A10 (self-audit section) was proposed then dropped (RCA 2.8/5: category error — audit proposals are single-anchor hypotheses, not axioms).

5. **Dependency chain A05→A06→A07 is fragile** — if IIb is rejected or significantly modified, the entire proposal stack collapses. Each proposal should be independently evaluable.

**Recommendation: MODIFY AND PROCEED** — the audit plan is worth executing but with revised priorities, descoped IIb, and elevated Failure Conditions as the primary deliverable.

---

## 1. 3-ROUND RCA ON THE AUDIT PLAN ITSELF

### Round 1 — Symptom

| # | Surface defect | Location |
|---|---|---|
| S1 | PROPOSAL_01 introduces 4-tier stratification as an *axiom* (IIb) rather than as an *empirical hypothesis* or *diagnostic heuristic* | Section 7, PROPOSAL_01 |
| S2 | A06 (Failure Conditions) is marked as dependent on A05 (IIb), but the logical derivation F = f(II, III, IV) does not require stratification | Section 8, dependency column |
| S3 | PROPOSAL_03's "practical criterion" — "can it live in our relational structure without breaking Tier 1?" — restates Tiên Đề IV's existing statement: "nội dung đến được tái tổ chức theo logic pattern nội tại" | Section 7, PROPOSAL_03 |
| S4 | The audit plan does not apply triangulation (≥2/3 anchors) to its own proposals, violating the method it audits | Throughout Section 7 |
| S5 | CHECK_07's verdict of "FAIL — tautology" for Tiên Đề IV is correct, but PROPOSAL_03 doesn't fully resolve the tautology — it adds a decision tree without operational criteria for the branch condition | CHECK_07 + PROPOSAL_03 |

### Round 2 — Mechanism

**Why S1 matters here specifically:** Mạch Rễ's strength is triangulation — a claim is *stronger* if it emerges from ≥2/3 independent anchors. By proposing IIb as an axiom derived solely from Phan Ngọc (with no Ashby/Weick or Anattā check), the audit plan asks Mạch Rễ to violate its own constitution. This is not just a methodological oversight — it creates an asymmetric dependency where one anchor (Phan Ngọc) supplies the *structure* of an axiom while the other two anchors become decorative.

**Why S2 matters:** The dependency chain A05→A06→A07 means the most actionable proposal (Failure Conditions, which directly addresses survivorship bias and strengthens falsifiability) is gated behind the most complex and risky proposal (4-tier stratification). If IIb takes 3 months to validate through peer review, the framework remains without failure conditions for that entire period — when failure conditions could be drafted in days from existing axioms.

**Why S3 matters:** PROPOSAL_03 asks: "Can this live in our relational structure without breaking Tier 1?" This is exactly what Tiên Đề IV already says: "nội dung đến được tái tổ chức theo logic pattern nội tại." The decision tree adds visual clarity but doesn't add operational content. The real missing piece — which Phan Ngọc's text actually supplies — is not a *criterion* but a *historical pattern*: "giữ quan hệ thực tiễn, bỏ siêu hình" (keep practical-relational, discard purely metaphysical). This is an empirical observation about Vietnamese cultural filtering, not yet a universal criterion.

**Why S4 matters:** The audit plan audits Mạch Rễ for not fully absorbing Phan Ngọc. But it doesn't ask: *would these proposals also emerge from Ashby/Weick or Anattā?* If PROPOSAL_01 (stratification) only appears in Phan Ngọc, its status should be "Phan Ngọc-specific empirical observation" not "axiom of the universal framework." This is the same inductive leap problem the audit correctly identifies in CHECK_02.

**Why S5 matters:** Adding a decision-tree diagram to a tautology doesn't resolve the tautology — it visualizes it. The operational criterion is still missing. The audit correctly diagnoses the disease but prescribes a bandage.

### Round 3 — Root

| Symptom | Root cause (one sentence) | Violates |
|---------|--------------------------|----------|
| S1 | PROPOSAL_01 confuses "Phan Ngọc's empirical observation about Vietnam" with "universal structural property derivable from ≥2/3 anchors" — the same inductive leap problem identified in CHECK_02. | Triangulation rule (axioms.html: "một tiên đề mạnh hơn nếu hiện ra ở ≥2/3 hệ") |
| S2 | The dependency chain assumes stratification is a prerequisite for failure analysis, but failure is a *dynamic* property of II×III×IV interaction, not a *structural* property requiring stratified layers. | Logical derivation order (axioms.html: F should derive from existing axioms, not from a new axiom) |
| S3 | The audit plan treats "operational criterion" as a *decision rule* (if-then tree) when Phan Ngọc's actual contribution is an *empirical pattern* (historical observation of what was kept/discarded) — these are different epistemological types. | Category boundary: decision rule ≠ empirical pattern |
| S4 | The audit applies RCA to Mạch Rễ but does not self-apply RCA to its own proposals — asymmetry in methodological rigor. | RULE ZERO (CLAUDE.md): "If the revision only changes the sentence where the symptom appears, it is not enough" |
| S5 | The audit correctly identifies Tiên Đề IV's tautology but doesn't trace *why* it's a tautology — because "logic pattern nội tại" has no independent definition outside the filtering outcome it's supposed to explain. | 5-Why incompleteness: stopped at Round 1 |

---

## 2. SCORING GATE — PER CHECKPOINT AND PROPOSAL

### 2.1 Audit Checkpoints (CHECK_01–08)

Scored on: **Correct / Deep / Feasible / Conflict-risk / Preservation** — whether the *finding* is sound.

| Checkpoint | C | D | F | CR | P | Avg | Verdict |
|---------------|---|---|---|---|-----|------|--------|
| CHECK_01 (Traceability FAIL) | 5 | 5 | 5 | 5 | 5 | **5.0** | KEEP — finding is correct, deep, and actionable |
| CHECK_02 (Formalization PARTIAL) | 5 | 4 | 4 | 5 | 4 | **4.4** | KEEP — correct diagnosis; action needs specificity |
| CHECK_03 (Văn hóa/Văn minh FAIL) | 5 | 5 | 4 | 3 | 4 | **4.2** | KEEP — correct gap; risk of over-correction (see S1) |
| CHECK_04 (Stratification FAIL) | 4 | 4 | 3 | 3 | 3 | **3.4** | MODIFY — gap is real but severity may be overstated; check if Ashby covers this |
| CHECK_05 (Failure conditions FAIL) | 5 | 5 | 5 | 5 | 5 | **5.0** | KEEP — strongest finding in the audit |
| CHECK_06 (Phần 3 UNRESOLVED) | 4 | 3 | 5 | 4 | 4 | **4.0** | KEEP — transparency gap is real; action is simple (add a sentence) |
| CHECK_07 (IV tautology FAIL) | 4 | 3 | 3 | 4 | 4 | **3.6** | MODIFY — correct diagnosis, but PROPOSAL_03 doesn't fix it |
| CHECK_08 (Falsification PARTIAL) | 5 | 4 | 3 | 5 | 4 | **4.2** | KEEP — correct; metric definition is genuinely hard |

**CHECK_04 and CHECK_07 fall below 4/5 threshold** → need modification before execution.

### 2.2 Proposals (PROPOSAL_01–03)

Scored on: **Correct / Deep / Feasible / Conflict-risk / Preservation** — whether the *proposed action* is sound.

| Proposal | C | D | F | CR | P | Avg | Verdict |
|----------|---|---|---|---|-----|------|--------|
| PROPOSAL_01 (IIb — Stratified Invariance) | 3 | 4 | 2 | 2 | 2 | **2.6** | **REVISE** — over-specified, single-anchor, high conflict risk |
| PROPOSAL_02 (F — Failure Conditions) | 5 | 5 | 5 | 5 | 5 | **5.0** | **KEEP** — strongest proposal; make INDEPENDENT of IIb |
| PROPOSAL_03 (Amendment IV — Judgment Mechanism) | 3 | 2 | 3 | 4 | 3 | **3.0** | **REVISE** — doesn't resolve the tautology it diagnoses |

### 2.3 Detailed Scoring Rationale

#### PROPOSAL_01 (IIb) — score 2.6/5 → REVISE

```
C=3 : The gap is real (Mạch Rễ does collapse stratification), but the 4-tier
      system is ONE possible formalization, not THE correct one. Phan Ngọc's
      own text doesn't use these 4 tiers — the audit PLAN invented them.

D=2 : Does not trace WHY stratification exists. Is it a universal property of
      identity systems, or a contingent feature of Vietnamese history? The
      proposal assumes the former without argument.

F=2 : Implementing 4-tier stratification requires:
      (a) Rewriting Tiên Đề II (breaks existing structure)
      (b) Updating Diagnosis Rubric with weights (complex calibration)
      (c) Re-verifying all 8 axioms against new tier system
      (d) Checking compatibility with Ashby's Requisite Variety
      This is a ~3-month research program, not an "action item."

CR=2 : HIGH conflict risk:
      (a) Ashby/Weick don't have stratified identity — they have variety
          engineering, which is orthogonal to tier depth
      (b) Anattā's śūnyatā explicitly denies stratified essence
      (c) Making "Tier 1" (lõi kiểu quan hệ) the deepest layer risks
          re-introducing svabhāva (inherent essence) — exactly what
          BRIDGE-II-III warns against

P=2 : Risk of making Mạch Rễ into "Phan Ngọc formalized" rather than
      "Phan Ngọc as one triangulation anchor." The universality claim
      would be weakened, not strengthened.
```

#### PROPOSAL_02 (F) — score 5.0/5 → KEEP, ELEVATE

```
C=5 : Survivorship bias is real and verifiable. The 3-condition AND gate
      (A: Tier-1 attacked, B: V-axis severed, C: rate > threshold) is
      logically derivable from II+III+IV without new axioms.

D=5 : Addresses root cause: Mạch Rễ cannot distinguish "shallow roots
      recovering" from "roots severed beyond recovery." This is a
      falsifiability defect at the framework level.

F=5 : Does NOT require IIb. Can be formulated with existing concepts:
      "pattern" (II), "vertical axis" (III), "boundary restructuring
      rate" (IV). The 3 conditions are structural, not tier-dependent.

CR=5 : LOW conflict risk:
      (a) Ashby: "variety destruction" is a known concept — F is the
          cultural analogue of "requisite variety collapse"
      (b) Anattā: pratītyasamutpāda (dependent origination) has
          "cessation conditions" — F is structurally analogous
      (c) F is a DERIVED proposition (like V-VII), not a new core axiom

P=5 : Strengthens Mạch Rễ by closing the most critical gap (survivorship
      bias) without adding architectural complexity.
```

#### PROPOSAL_03 (Amendment IV) — score 3.0/5 → REVISE

```
C=3 : Correctly identifies the tautology problem in IV, but the proposed
      fix doesn't resolve it. "Can it live in our relational structure?"
      restates "tái tổ chức theo logic pattern nội tại" in question form.

D=2 : Does not trace WHY the tautology exists. The root cause is that
      "logic pattern nội tại" has no operational definition independent
      of the filtering outcome. Adding a decision tree around an
      undefined term doesn't define the term.

F=3 : Can be reformulated without IIb. The real operational criterion
      from Phan Ngọc is the EMPIRICAL PATTERN: "historical Vietnamese
      filtering kept practical-relational content, discarded purely
      metaphysical content." This is an observation, not yet a universal
      criterion — but it's a START that can be tested against other cases.

CR=4 : Low conflict if reformulated as "empirical hypothesis" rather than
      "amendment to axiom."

P=3 : As written, doesn't preserve the clarity gain. A better formulation:
      "Tiên Đề IV's operational criterion is the OBSERVABLE outcome of
      community-level filtering over generational time, not a conscious
      individual decision rule." This makes IV falsifiable without
      claiming to have a universal decision algorithm.
```

---

## 3. FEASIBILITY, COMPLEXITY, RISK, TRADE-OFF ANALYSIS

### 3.1 Feasibility Matrix

| Action Item | Original Priority | Effort | Blocker | Revised Priority |
|-------------|-------------------|--------|---------|------------------|
| A01 (Page references) | HIGH | 2-4 hours | None — needs access to Phan Ngọc book with chapter/section numbers | HIGH |
| A02 (Formalization justification) | HIGH | 4-8 hours | None — philosophical writing | HIGH |
| A03 (Phần 3 transparency) | MEDIUM | 1-2 hours | None — add one paragraph | MEDIUM |
| A04 (Falsification metric) | HIGH | 8-16 hours | Needs historical/comparative data | HIGH |
| A05 (Draft IIb) | HIGH | 40-80 hours | Needs Ashby/Anattā triangulation first | **↓ MEDIUM** |
| A06 (Draft F — Failure Conditions) | HIGH | 8-16 hours | **REMOVE dependency on A05** | **↑ HIGH (independent)** |
| A07 (Draft Amendment IV) | MEDIUM | 8-16 hours | **REMOVE dependency on A05** | **↓ LOW (reformulate)** |
| A08 (Update Diagnosis Rubric) | MEDIUM | 4-8 hours | Depends on A06 (correctly) | MEDIUM |
| A09 (Independent peer review) | HIGH | Variable | Depends on A01-A07 completion | HIGH |

### 3.2 Complexity Assessment

```
PROPOSAL_01 (IIb)  : HIGH complexity
  - Requires: new axiom definition, tier interaction rules, Diagnosis Rubric
    recalibration, compatibility check with 3 anchors, potential revision
    of Tiên Đề IV mechanism
  - Touch points: axioms.html §Tiên Đề II, §Tiên Đề IV, how.html (Diagnosis
    Rubric), BRIDGE-II-III (svabhāva risk)
  - Estimation: 2-4 weeks of focused philosophical work + peer review

PROPOSAL_02 (F)    : MEDIUM complexity
  - Requires: 3-condition formalization, threshold definition, Diagnosis
    Rubric extension, falsification condition refinement
  - Touch points: axioms.html (new derived proposition), how.html (new
    "Đứt gãy" threshold), CHECK_08 (falsification metric)
  - Estimation: 3-5 days of focused work + peer review

PROPOSAL_03 (Amd IV): LOW-MEDIUM complexity (if reformulated)
  - Requires: reformulation of Tiên Đề IV's operational language,
    integration of Phan Ngọc's empirical pattern as hypothesis
  - Touch points: axioms.html §Tiên Đề IV
  - Estimation: 1-2 days of focused work
```

### 3.3 Risk Register

| Risk ID | Description | Probability | Impact | Mitigation |
|---------|-------------|-------------|--------|------------|
| R1 | IIb introduces svabhāva (inherent essence) through "Tier 1 lõi" — contradicts BRIDGE-II-III | MEDIUM | CRITICAL | Require IIb to pass Anattā compatibility check before adoption |
| R2 | IIb makes Mạch Rễ Vietnam-specific, breaking universality claim | HIGH | HIGH | Test IIb against at least one non-Vietnamese case (e.g., Jewish diaspora, Yoruba) before adoption |
| R3 | Dependency chain A05→A06→A07 blocks progress on F (the highest-value proposal) | HIGH | MEDIUM | Break dependency: make A06 independent |
| R4 | PROPOSAL_03 as written doesn't resolve IV's tautology — wasted effort | HIGH | LOW | Reformulate before drafting |
| R5 | Falsification metric (A04) is practically unmeasurable — CHECK_08 remains unresolved | MEDIUM | MEDIUM | Accept qualitative comparative threshold as minimum viable; mark quantitative metric as future work |
| R6 | Phan Ngọc's book has no page-standardized edition — page references may differ across printings | MEDIUM | LOW | Use chapter+section references instead of page numbers; note edition used |

### 3.4 Key Trade-offs

```
TRADE-OFF 1: Depth of Phan Ngọc absorption vs. Framework universality
  - More Phan Ngọc → more Vietnam-specific → weaker universality claim
  - Less Phan Ngọc → gaps remain → weaker philosophical foundation
  - RECOMMENDATION: Absorb Phan Ngọc's STRUCTURAL insights (kiểu quan hệ,
    kiểu lựa chọn, hấp thụ có định hướng) into axiom formalism. Keep
    Phan Ngọc's EMPIRICAL observations (4-tier manifestation, specific
    historical patterns) as evidence/case studies, not axioms.

TRADE-OFF 2: Axiom count vs. Explanatory power
  - More axioms → more complete → heavier, harder to verify
  - Fewer axioms → more elegant → gaps in explanation
  - RECOMMENDATION: Add F as DERIVED proposition (consistent with V-VII
    pattern). Do NOT add IIb as core axiom. Consider adding a "Diagnostic
    Layer" (separate from axiom layer) for stratification heuristics.

TRADE-OFF 3: Immediate actionability vs. Philosophical completeness
  - Fast: implement A01, A02, A03, A06 → closes 3 of 3 gaps partially
  - Complete: full IIb + F + Amendment IV → closes all gaps but takes months
  - RECOMMENDATION: Two-phase approach. Phase 1 (June 2026): A01-A04, A06,
    A08 — closes traceability, transparency, and survivorship bias.
    Phase 2 (July-August 2026): A05 (rescoped), A07 (reformulated), A09.
```

---

## 4. REVISED PLAN — 4 MODIFICATIONS

### MODIFICATION 1: Break the dependency chain (CRITICAL)

**Change:** A06 (Failure Conditions) is now INDEPENDENT of A05 (IIb).

**Rationale:** F derives from II+III+IV interaction, not from stratification. The 3 conditions (Tier-1 attacked, V-axis severed, rate > threshold) can be formulated using existing concepts: "pattern" (II), "vertical axis" (III), "boundary restructuring capacity" (IV). The word "Tier-1" in the original PROPOSAL_02 is a label, not a dependency — it can be replaced with "core relational pattern (II)" without loss of meaning.

**New dependency graph:**
```
A01, A02 (foundations) ── independent
A03 (transparency)     ── independent
A04 (falsification)    ── independent
A06 (Failure Conditions) ── depends on: A01 (for traceable citations)
A08 (Diagnosis update)   ── depends on: A06
A05 (IIb, rescoped)      ── depends on: A06 (learn from F before stratifying)
A07 (Amendment IV)       ── depends on: A06 (F clarifies boundary dynamics)
A09 (peer review)        ── depends on: A01-A08
```

### MODIFICATION 2: Rescope PROPOSAL_01 (IIb) from "axiom" to "diagnostic heuristic" (HIGH)

**Change:** IIb is NOT a new axiom. It becomes a **Diagnostic Stratification Heuristic (DSH)** — an optional layer that sits BETWEEN the axiom system and the Diagnosis Rubric, guiding practical application without claiming axiom status.

**Rationale:**
- Avoiding svabhāva risk: "Tier 1 lõi" as axiom implies an essence that survives all change — this contradicts BRIDGE-II-III's explicit statement that Pattern(II) is saṃvṛtisat (conventional truth), not paramārtha-sat
- Maintaining universality: 4-tier stratification calibrated to Vietnamese history may not generalize
- Keeping triangulation: As a heuristic (not axiom), DSH doesn't need ≥2/3 anchor support — it only needs to be *useful*, not *structurally necessary*

**New formulation:**
```
Diagnostic Stratification Heuristic (DSH) — NOT an axiom
Source: Phan Ngọc's observation + general systems theory
Status: Empirical hypothesis, pending cross-cultural verification

When diagnosing a collective identity system, consider:
  DSH-1: Not all identity elements change at the same rate.
          Elements closer to core relational patterns change slower.
  DSH-2: Boundary filtering (IV) operates differently at different
          "depths" — surface elements are more permissive.
  DSH-3: The "depth" of an element is not its content type
          (language vs. ritual vs. technology) but its structural
          distance from the invariant relational pattern (II).

This heuristic does NOT claim that stratification is a universal
ontological property — only that it is a useful diagnostic lens
consistent with Phan Ngọc's observations and general systems theory.
```

### MODIFICATION 3: Reformulate PROPOSAL_03 (Amendment IV) from "decision rule" to "operational definition" (MEDIUM)

**Change:** Instead of adding a decision tree, add an **operational definition** of "tái tổ chức theo logic pattern nội tại" that makes Tiên Đề IV falsifiable.

**Current (tautological):**
> "nội dung đến được tái tổ chức theo logic pattern nội tại"
> Problem: "logic pattern nội tại" is defined by the outcome of the filtering it's supposed to explain.

**Revised (operational):**
> "nội dung đến được tái tổ chức theo logic pattern nội tại" — operationalized as:
> (a) **Observable outcome**: After ≥2 generations, the introduced content is
>     used by community members in ways structurally consistent with pre-existing
>     relational patterns (II), as judged by ethnographic or historical analysis.
> (b) **Empirical pattern (from Phan Ngọc, hypothesis)**: Content compatible with
>     practical relational functions tends to be integrated; content requiring
>     metaphysical commitments incompatible with existing relational ontology
>     tends to be neutralized or discarded.
> (c) **Falsification**: Tiên Đề IV is weakened if a community is found where
>     (i) content incompatible with core relational patterns was absorbed WITHOUT
>     restructuring, AND (ii) the core pattern was disrupted as a result, AND
>     (iii) the identity survived anyway.

This makes IV falsifiable without claiming to have a universal decision algorithm.

### MODIFICATION 4: Revised priority and phasing (STRUCTURAL)

**Change:** Two-phase execution instead of flat priority list.

**Phase 1 — "Close the Critical Gaps" (June 2026, ~2 weeks)**
```
Week 1: A01 (page references) ✅ + A02 (formalization justification) + A03 (Phần 3 statement)
Week 2: A06 (Failure Conditions draft) + A08 (Diagnosis Rubric update)
Note: A10 (self-audit) dropped per RCA 2.8/5 — audit plan is single-anchor, not axiom-building; existing LIMIT_01-03 + hypothesis footer + Section 9 already provide self-limitation.
Deliverable: Mạch Rễ v2.1 — traceable, transparent, with failure conditions
```

**Phase 2 — "Deepen and Verify" (July-August 2026, ~6 weeks)**
```
Week 3-4: A05-rescoped (DSH draft) + A07-reformulated (IV operational definition)
Week 5-6: A04 (falsification metric) + internal testing against non-Vietnamese cases
Week 7-8: A09 (independent peer review)
Deliverable: Mạch Rễ v2.2 — with diagnostic heuristics, operational IV, peer-reviewed
```

---

## 5. REVISED ACTION ITEM TABLE

| ID | Action Item | Phase | Priority | Depends on | Closes | Effort |
|----|-------------|-------|----------|------------|--------|--------|
| A01 | Thêm chapter/section reference cho mọi trích dẫn Phan Ngọc | 1 | HIGH | — | CHECK_01 | 2-4h |
| A02 | Thêm mục "Biện minh formalization" — inductive leap justification | 1 | HIGH | — | CHECK_02 | 4-8h |
| A03 | Tường minh hóa lý do không hấp thụ Phần 3 Phan Ngọc | 1 | MEDIUM | — | CHECK_06 | 1-2h |
| A04 | Bổ sung qualitative metric cho "áp lực đồng hóa tương đương" | 2 | HIGH | — | CHECK_08 | 8-16h |
| A05 | Draft Diagnostic Stratification Heuristic (DSH) — rescoped from IIb | 2 | MEDIUM | A06 | GAP_01 | 16-24h |
| A06 | Draft Mệnh đề F (Failure Conditions) — **INDEPENDENT** of A05 | 1 | **HIGH** | A01 | GAP_02 | 8-16h |
| A07 | Reformulate Tiên Đề IV operational definition | 2 | LOW | A06 | GAP_03 | 8-16h |
| A08 | Cập nhật Diagnosis Rubric với ngưỡng "Đứt gãy" | 1 | MEDIUM | A06 | GAP_02 | 4-8h |
| A09 | Peer review độc lập cho A05, A06, A07 | 2 | HIGH | A05-A07 | Toàn bộ | Variable |
| ~~A10~~ | ~~Self-audit section~~ — **DROPPED** (RCA 2.8/5: category error — audit proposals are single-anchor hypotheses, not axioms; triangulation ≥2/3 rule does not apply) | — | — | — | — | — |

---

## 6. VERIFICATION — HOW TO KNOW THE REVISED PLAN WORKS

### 6.1 Success Criteria

```
SC1 — Traceability    : Every Phan Ngọc citation in axioms.html has a
                         chapter/section reference. (A01 complete)

SC2 — Formalization   : axioms.html §Tiên Đề II includes a paragraph explaining
                         why Phan Ngọc's observation (about Vietnam) supports a
                         universal structural claim, with at least one non-Vietnamese
                         example showing the same pattern. (A02 complete)

SC3 — Transparency    : A statement in axioms.html or how.html: "Phần 3 của
                         Phan Ngọc (Bảo vệ và phát huy văn hóa) bàn về chính sách
                         và thiết chế — chúng tôi không hấp thụ phần này vì
                         Mạch Rễ phân tích cơ chế phi-tập-trung, không thiết kế
                         chính sách top-down." (A03 complete)

SC4 — Survivorship    : Mệnh đề F exists as a derived proposition with clear
                         3-condition AND gate, falsification condition, and
                         integration into Diagnosis Rubric. (A06 + A08 complete)

SC5 — Operational IV  : Tiên Đề IV's description includes operational indicators
                         (generational time, structural consistency, observable
                         outcomes) that make the claim falsifiable. (A07 complete)

SC6 — Self-consistency: ~~Audit plan includes self-check section...~~ **DROPPED** (see A10 RCA).
                         Audit plan already self-limited via LIMIT_01-03 + hypothesis
                         footer + Section 9 open questions.
```

### 6.2 Regression Tests

```
RT1 : After A01-A03, re-run CHECK_01 through CHECK_06 against updated
      axioms.html. All should move from FAIL/PARTIAL → PASS.

RT2 : After A06, test Mệnh đề F against:
      (a) 1000 năm Bắc thuộc (prediction: Điều kiện A+B+C không đồng thời →
          không đứt gãy — PASS if prediction matches history)
      (b) A known case of cultural extinction (prediction: cả 3 điều kiện
          đồng thời → đứt gãy — PASS if prediction matches)

RT3 : After A07, test Tiên Đề IV operational definition:
      "Can a neutral observer determine, for a given historical case,
       whether content was 'tái tổ chức theo logic pattern nội tại'
       without knowing the outcome in advance?"
      PASS if the operational indicators allow ex-ante judgment.
```

---

## 7. OPEN QUESTIONS (CARRIED FORWARD + NEW)

### Carried forward from original audit (Q01–Q06)

```
Q01 : [RESOLVED for this review] Phan Ngọc's exact definitions of "văn hóa"
      and "văn minh" in the original text. From pages 19-24 of the OCR text:
      văn hóa = mối quan hệ giữa thế giới biểu tượng và thế giới thực tại
      (biểu hiện thành kiểu lựa chọn); văn minh = kĩ thuật làm chủ thế giới
      (có thể chuyển giao giữa các tộc người).

Q02 : [STILL OPEN] Does Phan Ngọc provide examples of FAILED cultural
      filtering, or only successes? This determines whether PROPOSAL_02's
      3-condition model can be calibrated against negative cases from
      Phan Ngọc's own data.

Q03 : [STILL OPEN] Is "nuôi được quan hệ cộng đồng không?" an explicit
      criterion in Phan Ngọc, or an interpretation by the audit?

Q04 : [STILL OPEN] Does Phần 3 genuinely conflict with Mạch Rễ's
      non-top-down principle, or is there a reading that's compatible?

Q05 : [PARTIALLY RESOLVED] Lévi-Strauss and stratification — this review
      recommends checking whether Ashby's "variety engineering" already
      implies stratification (different subsystems need different variety
      levels). If so, DSH has 2/3 anchor support.

Q06 : [PARTIALLY RESOLVED] Ashby's Requisite Variety and stratification —
      this review's RESCOPING of IIb→DSH partially addresses this.
      Ashby does imply that different system levels need different
      variety-handling capacity, which is structurally analogous to
      stratification without requiring the specific 4-tier model.
```

### New questions from this RCA review

```
Q07 : [NEW] Can Mệnh đề F be formulated using ONLY concepts already
      defined in axioms I-VII? If yes, F is a genuine derivation (like
      V-VII). If it requires new primitive concepts, it may need axiom
      status — which changes its burden of proof.

Q08 : [NEW] Does the DSH (Diagnostic Stratification Heuristic) have any
      analogue in the other two anchors?
      - Ashby: "hierarchical variety engineering" — subsystems at different
        levels handle different variety → structural analogue
      - Anattā: "two truths" (saṃvṛti-satya / paramārtha-satya) —
        conventional vs. ultimate truth → epistemological stratification
      If both have structural analogues, DSH has stronger foundation than
      currently assumed.

Q09 : [NEW] What is the MINIMUM set of changes that would move the overall
      audit verdict from PARTIAL → PASS? This review proposes:
      Minimum: A01 + A02 + A03 + A06 + A08 (Phase 1)
      This closes traceability (CHECK_01), formalization (CHECK_02),
      transparency (CHECK_06), and survivorship bias (CHECK_05, GAP_02).
      GAP_01 and GAP_03 would remain open but documented as future work.

Q10 : [NEW] If Phan Ngọc's own text does NOT contain explicit failure
      case studies (Q02), does PROPOSAL_02's 3-condition model become
      Mạch Rễ's ORIGINAL contribution rather than a "gap fill" from
      Phan Ngọc? This changes how F should be credited and justified.
```

---

## 8. DECISION LOG

| Decision | Rationale | Score |
|----------|-----------|-------|
| D1: Break A06 dependency on A05 | F derives from II+III+IV, not from stratification. Independence enables parallel progress. | 5.0/5 |
| D2: Rescope IIb → DSH (heuristic, not axiom) | Avoids svabhāva risk, maintains universality, reduces conflict with Ashby/Anattā | 4.6/5 |
| D3: Reformulate Amendment IV as operational definition | Current proposal (decision tree) doesn't resolve tautology. Operational indicators do. | 4.4/5 |
| D4: Two-phase execution | Phase 1 closes critical gaps fast; Phase 2 handles complex proposals with peer review | 4.8/5 |
| D5: ~~Add self-audit section (A10)~~ **DROPPED** | RCA re-evaluation 2.8/5: audit plan is single-anchor (Phan Ngọc only); applying triangulation ≥2/3 to its proposals is a category error — proposals are gap-fill hypotheses, not axiom claims. Existing LIMIT_01-03 + hypothesis footer + Section 9 already sufficient. | ~~4.2/5~~ → 2.8/5 |
| D6: Keep CHECK_04 and CHECK_07 findings but modify their actions | Gaps are real; proposed fixes need adjustment, not the diagnosis | 4.0/5 |

All decisions pass ≥ 4/5 threshold → proceed.

---

## APPENDIX A — RCA TRACE FOR EACH MAJOR FINDING

### A.1 Why PROPOSAL_01 overfits (5-Why)

```
Observation: PROPOSAL_01 proposes 4-tier stratification as an axiom (IIb).
  ↓ Why?
Because the audit found that Mạch Rễ collapses Phan Ngọc's stratified
observations into a single Pattern(R(S)).
  ↓ Why is that a problem requiring a NEW AXIOM?
Because without stratification, Tiên Đề IV can't distinguish what gets
absorbed into core vs. surface.
  ↓ Why can't this be solved within existing axioms?
Because "logic pattern nội tại" has no operational definition — adding
stratification gives it one by specifying which tier is affected.
  ↓ Why must the stratification be an AXIOM rather than a heuristic?
**ROOT**: It doesn't. The audit implicitly assumes that "what Phan Ngọc
observed" = "what Mạch Rễ must formalize as axiom." But Phan Ngọc's
stratified observations are about VIETNAM SPECIFICALLY. A diagnostic
heuristic (DSH) serves the same function without claiming universality.
```

### A.2 Why F (Failure Conditions) is the highest-value proposal (5-Why)

```
Observation: Mạch Rễ has no theory of failure — only success cases.
  ↓ Why?
Because the framework was derived from the question "why do some systems
SURVIVE?" — it naturally focused on survival mechanisms.
  ↓ Why is this a critical gap?
Because without failure conditions, the framework can't be falsified:
every case of identity loss can be post-hoc rationalized as "insufficient
application of I-IV" rather than "I-IV are insufficient to explain this."
  ↓ Why can't falsification conditions (CHECK_08) cover this?
Because "áp lực đồng hóa tương đương" is undefined — you can always
claim the pressure wasn't equivalent, making the condition vacuous.
  ↓ Why does F solve this better than a metric definition alone?
**ROOT**: F defines the INTERNAL conditions under which identity fails,
making the framework falsifiable from WITHIN. A metric definition (A04)
defines EXTERNAL comparison conditions. You need both: F tells you WHEN
failure should occur (internal logic), A04 tells you how to COMPARE cases
(external measurement). F is logically prior because it defines what
you're measuring.
```

### A.3 Why PROPOSAL_03 doesn't resolve the tautology (5-Why)

```
Observation: PROPOSAL_03 adds a decision tree to Tiên Đề IV.
  ↓ Why doesn't this resolve the tautology?
Because the decision tree's branch condition is: "Can this live in our
relational structure without breaking Tier 1?"
  ↓ Why is that still tautological?
Because "can live in our relational structure" is equivalent to "can be
tái tổ chức theo logic pattern nội tại" — same undefined term, new phrasing.
  ↓ Why is the term undefined?
Because Mạch Rễ has not specified what observable indicators distinguish
"successfully integrated into pattern" from "rejected by pattern."
  ↓ Why can't Phan Ngọc's empirical pattern serve as the indicator?
**ROOT**: It CAN — but as an EMPIRICAL HYPOTHESIS ("in observed Vietnamese
history, the filter kept X and discarded Y"), not as a UNIVERSAL DECISION
RULE ("for all systems, the filter works by criterion Z"). PROPOSAL_03
conflates these two — it presents an empirical pattern in the grammatical
form of a universal rule. The fix is to operationalize IV with observable
indicators while marking the specific "giữ quan hệ thực tiễn, bỏ siêu hình"
pattern as a TESTABLE HYPOTHESIS from Phan Ngọc, not as the definition of IV.
```

---

## APPENDIX B — COMPARISON: ORIGINAL vs. REVISED PLAN

| Dimension | Original Audit Plan | This RCA-Reviewed Plan |
|-----------|--------------------|------------------------|
| **Proposals** | 3 proposals: IIb (axiom), F (derived), Amendment IV | 3 outputs: DSH (heuristic), F (derived, independent), IV operational definition |
| **Dependency** | A05 → A06 → A07 (linear chain) | A06 independent; A05, A07 parallel after A06 |
| **Priority** | Flat list with HIGH/MEDIUM | Two-phase with clear deliverable per phase |
| **IIb status** | New core axiom (Tiên Đề IIb) | Diagnostic Stratification Heuristic (not axiom) |
| **F status** | Derived, dependent on IIb | Derived, independent, grounded in II+III+IV |
| **IV fix** | Decision tree with "practical criterion" | Operational definition with observable indicators + empirical hypothesis |
| **Self-audit** | Proposed then dropped (RCA 2.8/5) | N/A — existing LIMIT_01-03 + hypothesis footer sufficient |
| **Risk management** | Implicit | Explicit risk register with 6 identified risks |
| **Phasing** | None | Phase 1 (2 weeks, critical gaps) + Phase 2 (6 weeks, deepening) |
| **Minimum viable** | Not specified | A01+A02+A03+A06+A08 = minimum to move verdict PARTIAL→PASS |
| **Open questions** | 6 questions | 10 questions (6 carried + 4 new from RCA) |

---

## APPENDIX C — IMMEDIATE NEXT ACTIONS

```
IMMEDIATE (this week):
  1. [x] Execute A01 — add chapter/section references to all Phan Ngọc citations
         (DONE 2026-06-09: 10 citations across 4 files)
  2. [x] Execute A02 — draft "Biện minh formalization" paragraph for Tiên Đề II
         (DONE 2026-06-09: inductive justification with 3 independent argument lines)
  3. [x] Execute A03 — add Phần 3 transparency statement
         (DONE 2026-06-09: transparency table + explanation in axiom_spec.md §0.1.1)

NEXT WEEK:
  5. [x] Execute A06 — draft Mệnh đề F (Failure Conditions) as derived proposition
         (DONE 2026-06-09: Mệnh đề F · RCA 5.0/5 · 3-condition AND gate)
  6. [x] Execute A08 — update Diagnosis Rubric with "Đứt gãy" threshold
         (DONE 2026-06-09: A08a diagram sync, A08b indicator→F mapping, A08c differential diagnosis)

COMPLETED (unblocked by RCA):
  9. [x] Execute A04 — add qualitative metric for "áp lực đồng hóa tương đương"
         (DONE 2026-06-09: EAP 5-dimension qualitative comparative framework · RCA 4.4/5)
         NOTE: Originally listed as BLOCKED (needs external data). RCA revealed the root cause
         is a category error (scalar vs. multi-dimensional), not a data problem. Fix:
         qualitative comparative framework using 5 observable dimensions + calibration anchor
         — no external data needed for the framework definition itself.

AFTER A06:
  7. [ ] Rescope A05 — draft DSH (not IIb axiom)
  8. [ ] Reformulate A07 — operational definition for Tiên Đề IV

BLOCKED (need external resource):
  10. [ ] A09 — needs independent reviewer not in Mạch Rễ author group

PHASE 1 STATUS: COMPLETE (A01, A02, A03, A04, A06, A08) — all critical gaps closed.
  CHECK_01 (traceability)     : PASS (A01)
  CHECK_02 (formalization)    : PASS (A02)
  CHECK_06 (transparency)     : PASS (A03)
  CHECK_08 (falsification)    : PASS (A04 + A06)
  GAP_02 (survivorship bias)  : CLOSED (A06 + A08)
  Minimum viable set achieved → audit verdict: PARTIAL → PASS (with GAP_01, GAP_03 documented as future work).
```

---

*Tài liệu này là kết quả của 3-round RCA × 5-Why × scoring gate ≥ 4/5 áp dụng lên chính audit plan.*
*Mọi đề xuất sửa đổi trong tài liệu này đã qua scoring gate — xem Section 2 để biết điểm số từng proposal.*
*Phiên bản: 1.0 — 2026-06-09*
*Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/*

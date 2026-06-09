# RCA AUDIT — Phase 1: Buddhist Pramāṇa Lens (`index.html` CRITICAL + HIGH Claims)
<!-- 3-round RCA × 5-Why × scoring gate ≥ 4/5 — executed 2026-06-09 -->
<!-- Internal-consistency audit: Mạch Rễ audited against its own Buddhist anchor -->
<!-- Tier 2 escalations documented inline -->

## METADATA

```
document_type     : audit_report_phase1
plan              : plan/PLAN_RCA_audit_index_html_buddhist_pramana.md
audit_target      : index.html (post triple-lens audit, commit 5c35ba3)
claims_audited    : C1, C5, C6, C2, C12 (2 CRITICAL + 3 HIGH)
lens_passes       : 26 diagnostic passes
tier2_escalations : 4 (B1, B8, B11, B15 — all confirmed RCA table accuracy)
fixes_recommended : 7 (1 P0-critical, 3 P1-important, 3 P2-minor)
strengths_confirmed: 7
status            : COMPLETE
```

---

## CLAIM C1 — "Mạch Rễ là khung nền (framework) nhận dạng và thực hành bản sắc sinh tồn"

**Source:** `index.html` L265-276
**Context:** The opening definitional paragraph. Post triple-lens audit, L275 now includes verb-based framing ("diễn ra khi"), Requisite Variety limit, tight/loose distinction, and growth dimension.

---

### C1 × B1 — Pramāṇa 4-Fold Structure (RCA #22-25, #97)

**Tier 2 verified** against full source L67-L105 (§4 opening).

Buddhist pramāṇa-epistemology structures knowledge in four integrated components: (i) pramāṇa (means of knowing), (ii) pramā (valid cognition), (iii) prameya (object known), (iv) pramāṇaphala (resultant cognition). Every school that uses pramāṇa-theory must specify these four.

Mạch Rễ's fourfold structure is IMPLICIT in `index.html`:
- **Prameya (object)**: "bản sắc sinh tồn" — the survival identity
- **Pramāṇa (means)**: "đặt tên và hệ thống hóa" + "suy từ câu hỏi gốc" + "kiểm chứng chéo qua 3 hệ độc lập"
- **Pramā (valid cognition)**: "nhận dạng" (recognition) — but criteria of validity are unstated
- **Phala (result)**: "thực hành" (practice) — but what practice PRODUCES is unstated

The fourfold structure IS there. But it is never named, never mapped to Buddhist terminology, and the criteria that distinguish VALID cognition (pramā) from INVALID cognition (apramā) are nowhere on the landing page.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | The pramāṇa structure is implicit but unnamed. "Nhận dạng" has no stated validity criterion |
| **R2 — Mechanism** | Mạch Rễ claims Buddhism as 1 of 3 anchors. Buddhist epistemology's signature contribution IS the pramāṇa formulation. If the framework uses pramāṇa structure without acknowledging it, the anchor is invisible to readers — weakening the triangulation claim |
| **R3 — Root** | The framework's method IS pramāṇa-compatible, but the Buddhist epistemological VOCABULARY is absent. Root cause: **the Buddhist anchor is structurally present but verbally invisible on the landing page** |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 5 | 5 | 5 | **4.8** | **FIX** — Make pramāṇa structure explicit |

**Recommended fix:** Add one sentence after C1's definition: "Về mặt nhận thức luận Phật giáo (pramāṇa): đối tượng nhận thức (prameya) = bản sắc sinh tồn; phương tiện nhận thức (pramāṇa) = suy từ câu hỏi gốc + kiểm chứng chéo; nhận thức đúng (pramā) = chẩn đoán phân biệt rễ sâu / rễ nông; kết quả (phala) = thực hành giữ bản sắc." N.B.: a one-sentence mapping is sufficient for a landing page; full elaboration belongs in `what.html`.

---

### C1 × B2 — Pratyakṣa vs Anumāna (Perception vs Inference) (RCA #27-28)

"Nhận dạng" (recognition) in Vietnamese can mean either direct recognition (pratyakṣa — perception without conceptual construction) or inferential recognition (anumāna — indirect knowledge based on signs). The Black Box methodology (confirmed strength, prior audit L2f: 4.8/5) makes clear that Mạch Rễ INFERS structure from observed behavior — it does not claim direct perception of identity-survival patterns.

But "nhận dạng" is the word used. In Diṅnāga's strict epistemology, pratyakṣa is "free from conceptual construction" (kalpanāpoḍha). Mạch Rễ IS conceptual (8 axioms, glossary, diagnosis rubric). Therefore "nhận dạng" in Mạch Rễ MUST be anumāna, not pratyakṣa — but this is never stated.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Nhận dạng" is ambiguous between direct perception and inference |
| **R2 — Mechanism** | A reader familiar with Buddhist epistemology may read "nhận dạng" as pratyakṣa and object that Mạch Rễ claims direct intuitive access to identity — which it does not. The framework's actual method (inference from observed behavior) is epistemically MORE modest and MORE defensible |
| **R3 — Root** | The word "nhận dạng" carries perceptual connotations in Vietnamese that are stronger than the framework's actual epistemological method. Root cause: **terminological imprecision in the flagship verb of the framework** |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 4 | 5 | 5 | 5 | **4.6** | **FIX** — Clarify "nhận dạng" as inferential |

**Recommended fix:** Add a parenthetical after the first occurrence of "nhận dạng": "nhận dạng (qua suy luận — anumāna — từ hành vi quan sát được, không phải trực giác — pratyakṣa — về bản chất)". Short, precise, and maps to Buddhist technical terms.

---

### C1 × B3 — Svalakṣaṇa vs Sāmānyalakṣaṇa (Particular vs Universal) (RCA #138-139)

**Tier 2 verified** against full source L141-L169.

Diṅnāga's strict dualism: svalakṣaṇa (self-defined particular) is causally efficient, inexpressible, unique — the object of perception. Sāmānyalakṣaṇa (general characteristic) is conceptual, expressible, common to many — the object of inference.

"Bản sắc sinh tồn" (survival identity) — which is it? The framework treats it as a PATTERN that can be recognized across individuals, communities, and organizations. This is sāmānyalakṣaṇa — a general characteristic, object of inference. The framework does NOT claim to capture each person's unique, inexpressible particular identity (svalakṣaṇa).

This is correctly scoped — but implicit. The Buddhist distinction provides vocabulary to explain WHY the framework works at the general level and WHY it cannot capture individual uniqueness. This maps directly to the prior audit's C5×L2a finding (essential variables as future work): svalakṣaṇa is INEXPRESSIBLE by definition in Buddhist epistemology, so the framework's inability to fully operationalize "bản sắc" is philosophically justified, not a defect.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Bản sắc sinh tồn" is not located on the svalakṣaṇa/sāmānyalakṣaṇa spectrum |
| **R2 — Mechanism** | The framework's scope (general patterns, not individual uniqueness) is ALREADY correct — but without the Buddhist vocabulary, it cannot DEFEND this scope boundary against demands for more specificity |
| **R3 — Root** | The svalakṣaṇa/sāmānyalakṣaṇa distinction provides the Buddhist anchor's OWN justification for why a framework of identity must operate at the general (sāmānyalakṣaṇa) level — this justification is missing |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 5 | 5 | 5 | **4.8** | **FIX** — This finding STRENGTHENS the framework by providing Buddhist justification for its scope boundary |

**Recommended fix:** Add to the boundary note (L275) or glossary (C15 — Invariant): "Bản sắc sinh tồn được nhận dạng ở tầng đặc tính chung (sāmānyalakṣaṇa) — đối tượng của suy luận — không phải ở tầng cá biệt (svalakṣaṇa) vốn bất khả diễn đạt. Đây là giới hạn nhận thức luận, không phải khiếm khuyết."

**Cross-reference:** This finding provides the PHILOSOPHICAL JUSTIFICATION for the prior audit's C5×L2a (essential variables, scored 3.6, marked "future work"). Buddhist epistemology ACCEPTS that unique particulars cannot be fully specified in language — the framework's inability to operationalize every essential variable is not a defect but a category boundary. The prior audit's "future work" finding can now be closed with a philosophical justification instead of an operational one.

---

### C1 × B5 — Non-Distinction of Means and Result (RCA #140)

Diṅnāga rejects the realist distinction between means (pramāṇa) and result (pramāṇaphala) of cognition. C1 defines Mạch Rễ as "nhận dạng VÀ thực hành" — recognition AND practice. These are presented as TWO activities (nhận dạng → thực hành), which suggests a means-result DISTINCTION.

But Diṅnāga's radical position is that the means IS the result — cognition and its object arise together. Does Mạch Rễ's "nhận dạng" (recognition) and "thực hành" (practice) maintain non-distinction?

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Nhận dạng và thực hành" presents them as two separable activities — implying means/result distinction |
| **R2 — Mechanism** | The prior audit's L3a finding (C1×L3a: 4.8, "dialectical definition") confirmed that the pair preserves distinctiveness + responsiveness. But Diṅnāga's non-distinction thesis is STRONGER than Weick's dialectic — it claims the two are non-separable, not just complementary |
| **R3 — Root** | The framework's "nhận dạng + thực hành" dyad is closer to Sautrāntika realism (means and result are distinct but related through resemblance, sārūpya) than to Diṅnāga's radical non-distinction. The Buddhist anchor is Diṅnāga/Dharmakīrti — this warrants acknowledgment of which Buddhist sub-tradition the framework aligns with |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 3 | 3 | 4 | 4 | 5 | **3.8** | **KEEP** — Nuance-level finding. "Và" (and) is correct for a landing page. Flag for `what.html` deep dive |

---

### C1 × B6 — Saṃvṛti-sat (Conventional Truth) (RCA #99, #110)

**Tier 2 verified** against full source L91-L105 (Vasubandhu's Two Truths).

Vasubandhu: conventional truth (saṃvṛti-sat) = that which loses its cognition when broken into parts or mentally abstracted from properties. "But conventional designations are applied to those very things, so one who says on the authority of convention that there is a water-jug...is speaking the truth rather than a falsehood."

Mạch Rễ is a saṃvṛti-sat entity: it is a conceptual designation (8 axioms + glossary + diagnosis rubric) that is USEFUL and TRUE at the conventional level, but would dissolve under ultimate analysis. The framework does not claim paramārtha-sat (ultimate truth — non-conceptual, irreducible, infallible).

The prior audit's C1×L3d fix ("Nói cách khác: Mạch Rễ không phải là một vật cố định...nó là một quá trình") already captures the dynamic, conventional nature. But the Two Truths vocabulary would make this EXPLICIT.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | The framework's conventional-truth status is implicit but not labeled |
| **R2 — Mechanism** | Without the Two Truths vocabulary, a reader might mistake Mạch Rễ's confidence ("đặt tên và hệ thống hóa") for a claim to ultimate truth. The Buddhist anchor provides the vocabulary to say: "this is conventional truth — useful, testable, but not ultimate" |
| **R3 — Root** | Same root as B1 — the Buddhist vocabulary is absent from the surface, making the anchor invisible |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 4 | 5 | 5 | 5 | **4.6** | **FIX** — Add Two Truths location |

**Recommended fix:** Add to the boundary note (L275): "Mạch Rễ hoạt động ở tầng chân lý quy ước (saṃvṛti-sat) — hữu ích, có thể kiểm chứng, nhưng không phải chân lý tối hậu (paramārtha-sat)."

---

### C1 × B7 — Paramārtha-sat (Ultimate Truth) (RCA #100, #109)

The diagnostic question: does the framework claim to describe "ultimate ontological reality" (non-conceptual, irreducible, infallible)?

C1's current wording (post triple-lens fixes) does NOT claim paramārtha-sat. "Làm hiển lộ cấu trúc vốn đã tồn tại" (make explicit a structure that already existed) sounds ambitious but is still conventional: it claims to REVEAL a pattern, not to access non-conceptual ultimate reality. The framework's 8-axiom structure is inherently conceptual — it cannot be paramārtha-sat.

The prior audit's fixes (C5×L2c Requisite Variety limit, C3×L1c scoping "chưa bao giờ") have already eliminated any paramārtha-sat drift. This is a confirmed strength.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 5 | 5 | 5 | **5.0** | **KEEP** — Confirmed Buddhist alignment. No paramārtha-sat drift detected |

---

### C1 × B8 — Apoha / Double Negation (Exclusion-Based Meaning) (RCA #5, #74, #189)

**Tier 2 verified** against full source L233-L261 (Chapter V — Anyāpoha).

Apoha: meaning is established through exclusion (anyāpoha = "exclusion of others"). "Cow" means "not non-cow." Buddhist semantics REJECTS positive reference to real universals (sāmānya) — universals are conceptual constructions.

C1 says Mạch Rễ "đặt tên và hệ thống hóa" (names and systematizes). "Đặt tên" (naming) in Buddhist semantics should work through apoha. But the glossary definitions in `index.html` (C13–C16) use POSITIVE description: "Framework = Hệ thống công cụ nhận dạng và thực hành bản sắc sinh tồn" — this is positive predication, not exclusion-based.

However, the framework's METHOD is structurally apoha-compatible: "bản sắc sinh tồn" is defined by what it EXCLUDES (non-survival, non-identity), and the triangulation method ("neo 3 hệ độc lập") works by excluding patterns that don't appear across all 3 systems.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | Glossary definitions use positive predication ("X là Y"), not exclusion-based apoha ("X là cái không-phải-không-X") |
| **R2 — Mechanism** | Positive predication implies reference to real universals — the very thing Buddhist semantics (apoha) rejects. If Mạch Rễ claims Buddhist semantic anchor, its definitional method should at minimum ACKNOWLEDGE that its concepts work through exclusion |
| **R3 — Root** | The framework's METHOD is apoha-compatible (triangulation excludes non-convergent patterns; naming carves out conceptual space by exclusion), but its PRESENTATION uses positive predication. The gap is presentational, not methodological |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 4 | 4 | 5 | **4.4** | **FIX** — Add apoha acknowledgment |

**Recommended fix:** Add to the "What is" paragraph or glossary preamble: "Việc đặt tên trong Mạch Rễ vận hành theo cơ chế apoha (tính loại trừ — exclusion): mỗi khái niệm được xác định bằng cách loại trừ những gì nó không phải, thay vì tham chiếu đến một bản chất cố định (universal)."

---

### C1 × B12 — Gold-Testing Method (RCA #106, #96)

**Tier 2 verified** against full source L77-L87.

Buddha's gold-testing verse (Tattvasamgraha kārikā 3587): "The wise one should agree with my statement only by testing its validity, not out of reverence, just as a goldsmith accepts the purity of gold only by testing it in fire, cutting it, and carefully testing it on a touchstone."

Does `index.html` INVITE testing? The page currently has:
- "CC BY 4.0" (open license — invites use and adaptation)
- "Đang phát triển" (under development — acknowledges incompleteness)
- The Requisite Variety limit (acknowledges scope boundary)
- But: no explicit invitation to TEST or FALSIFY

The `axioms.html` page has "Mệnh đề F (Failure Conditions)" — but this is NOT on the landing page. A reader of `index.html` has no indication that the framework has built-in failure conditions.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | `index.html` lacks an explicit invitation to test. Mệnh đề F exists but is invisible from the landing page |
| **R2 — Mechanism** | The Buddha's gold-testing method is the Buddhist anchor's CORE epistemic virtue: test before accepting. If the landing page doesn't embody this, the framework appears to demand acceptance rather than invite testing — violating its own anchor's primary methodological rule |
| **R3 — Root** | Mệnh đề F exists in `axiom_spec.md` and `axioms.html`, but the landing page doesn't signal its existence. The framework HAS the falsification conditions — it just doesn't advertise them at the entry point |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 4 | 4 | 5 | 5 | **4.4** | **FIX (minor)** — Signal Mệnh đề F on landing page |

**Recommended fix:** Add to the boundary note (L275) or as a short sentence after C5: "Mỗi tiên đề đều có điều kiện bác bỏ (falsification condition — Mệnh đề F) — xem chi tiết tại Hệ Tiên Đề."

---

### C1 × B13 — Scepticism as Methodological Tool (RCA #12, #107)

Buddhist epistemology begins with doubt (saṃśaya) and desire to know (jijñāsā). The Buddha's "sailing against the current" (paṭisotagāmī) is sceptical toward unsupported views.

C5 IS the doubt: "Làm sao giữ được mình...?" The framework STARTS from a question. This is structurally Buddhist — the central question IS saṃśaya (doubt) motivating jijñāsā (desire to know). The prior audit's C6×L1d ("tái dựng" = 5.0 confirmed strength) already recognized the epistemic modesty.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 5 | 5 | 5 | **5.0** | **KEEP** — Confirmed Buddhist alignment. The question-first structure IS Buddhist scepticism in practice |

---

### C1 × B14 — Dependent Arising (Pratītyasamutpāda) (RCA #39-40)

Tiên Đề I ("Có Nhau Mới Có Mình" / "Sống Trong Quan Hệ") is structurally identical to pratītyasamutpāda (dependent arising) — the Buddha's fundamental dynamic insight that every empirical formation arises through conditioned conditions.

But `index.html` never mentions this mapping. The axioms are listed in C7 (L298) as "4 Tiên Đề Cốt Lõi (I–IV)" — their names are not stated on the landing page. The Buddhist anchor for Tiên Đề I is invisible.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | Tiên Đề I's structural identity with pratītyasamutpāda is not acknowledged |
| **R2 — Mechanism** | The Buddhist anchor is one of 3 independent systems. If the most fundamental Buddhist doctrine (dependent arising) is structurally identical to the framework's FIRST axiom, and this is invisible, the anchor claim is weakened — it looks like Buddhism is a decorative reference rather than a structural foundation |
| **R3 — Root** | The axiom names are not stated on `index.html` — the landing page only gives the count (4+4+1). Tiên Đề I's name ("Sống Trong Quan Hệ") is in `axiom_spec.md` and `axioms.html` but not on the entry page. The mapping to pratītyasamutpāda is in neither |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 4 | 4 | 5 | **4.6** | **FIX** — Acknowledge Tiên Đề I = pratītyasamutpāda |

**Recommended fix:** Add to the C6/C7 area (L298): "Tiên Đề I ('Sống Trong Quan Hệ' — Có Nhau Mới Có Mình) tương đương cấu trúc với Duyên Khởi (pratītyasamutpāda) — nền tảng của tiến trình nhận thức luận Phật giáo."

---

### C1 — VERDICT SUMMARY

| Lens | Score | Verdict |
|------|-------|---------|
| B1 — Pramāṇa structure | **4.8** | **FIX** |
| B2 — Pratyakṣa vs Anumāna | **4.6** | **FIX** |
| B3 — Svalakṣaṇa/Sāmānyalakṣaṇa | **4.8** | **FIX** (strengthens scope boundary) |
| B5 — Non-distinction means/result | **3.8** | KEEP |
| B6 — Saṃvṛti-sat | **4.6** | **FIX** |
| B7 — Paramārtha-sat | **5.0** | KEEP (confirmed strength) |
| B8 — Apoha semantics | **4.4** | **FIX** |
| B12 — Gold-testing | **4.4** | **FIX (minor)** |
| B13 — Scepticism | **5.0** | KEEP (confirmed strength) |
| B14 — Dependent arising | **4.6** | **FIX** |

**Triangulation:** 7/10 passes recommend fix (all above threshold). The root cause is consistent across B1, B2, B3, B6, B8, B14: **the Buddhist epistemological vocabulary is absent from the surface of the landing page, making the Buddhist anchor structurally present but verbally invisible.** 3/10 passes confirm Buddhist alignment (B7, B13, B5).

**Root cause (one sentence):** `index.html`'s method IS consistent with Buddhist pramāṇa-epistemology (pramāṇa structure implicit, Two Truths correctly scoped, scepticism embodied, dependent arising structurally encoded), but the Buddhist TECHNICAL VOCABULARY is absent — making the anchor invisible and missing opportunities to strengthen the framework's epistemic modesty with its own anchor's justifications.

---

## CLAIM C5 — "Làm sao giữ được mình khi mọi thứ xung quanh muốn thay đổi mình?"

**Source:** `index.html` L271-276
**Context:** The central question, post triple-lens fixes. L275 now adds Requisite Variety limit, tight/loose distinction, process framing, and growth dimension.

---

### C5 × B1 — Pramāṇa Structure (RCA #22-25)

C5 is the PREMISE of the pramāṇa process. In Buddhist terms: C5 poses the existential predicament (duḥkha — the suffering of identity under assimilation pressure). The pramāṇa inquiry then asks: what valid cognition (pramā) can address this? What means (pramāṇa) produce it? What object (prameya) is known? What result (phala) is achieved?

C5 as a question IS the starting point of pramāṇa inquiry. This is structurally correct. The question "làm sao...?" maps to the Buddhist starting point: doubt (saṃśaya) motivating the desire to know (jijñāsā). Same root cause as C1×B1 — the mapping is structurally present but verbally invisible.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 4 | 5 | 5 | 5 | **4.6** | **FIX** — Resolved by C1×B1 fix (single pramāṇa mapping sentence covers both) |

---

### C5 × B2 — Pratyakṣa vs Anumāna (RCA #27-28)

C5 is a question about EXPERIENCE ("muốn thay đổi mình" — want to change you). This is the experienced disturbance (D in Ashby's terms). The question arises from direct experience of assimilation pressure. But the ANSWER (axioms, diagnosis) operates through inference.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 3 | 5 | 5 | 5 | **4.4** | **FIX** — Resolved by C1×B2 fix (anumāna clarification covers C5's answer) |

---

### C5 × B3 — Svalakṣaṇa vs Sāmānyalakṣaṇa (RCA #138-139)

"Giữ được mình" (keep oneself) — "mình" (self) here could be read as svalakṣaṇa (unique, inexpressible particular self) or sāmānyalakṣaṇa (general characteristics of identity). The framework's answer operates at sāmānyalakṣaṇa level — it identifies general patterns, not individual uniqueness.

But C5's "mình" is singular, personal, intimate. This creates a productive TENSION: the question is personal (svalakṣaṇa-flavored), but the answer is general (sāmānyalakṣaṇa). This tension is not a defect — it's the engine of the framework. But the Buddhist vocabulary would help readers understand WHY the framework answers at the general level.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 3 | 3 | 5 | 5 | 5 | **4.2** | **KEEP (minor)** — The tension is productive. Resolved by C1×B3 fix |

---

### C5 × B4 — Pramāṇādhīna vs Prameyādhīna (RCA #134-135)

Diṅnāga's radical dictum: pramāṇādhīnaḥ prameyādhigamaḥ — "acquisition of knowledge of an object depends on the means of knowledge." Opposing non-Buddhist view: prameyādhīnaḥ pramāṇasiddhiḥ — "the object determines the means."

C5's "suy từ câu hỏi gốc" (derive from root question) — which direction does it follow? The question IS the means-determining-the-object path: start with the experienced predicament (the need to know), design the means (derivation + triangulation), and the object (bản sắc sinh tồn) emerges THROUGH the means.

This is Diṅnāga's pramāṇādhīna direction. Mạch Rễ does NOT start with "bản sắc sinh tồn" as a pre-given object and then design means to know it. It starts with the QUESTION and derives the object through the means. This is correct Buddhist epistemology.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 5 | 5 | 5 | **5.0** | **KEEP** — Confirmed Buddhist alignment. The question-first method IS pramāṇādhīna |

---

### C5 × B6 — Saṃvṛti-sat (Conventional Truth) (RCA #99, #110)

C5 asks about "giữ được mình" (keeping oneself). Is "mình" (self) in the conventional or ultimate sense? In Buddhist terms: the conventional self (saṃvṛti-sat — a useful designation) or the ultimate self (paramārtha-sat — which Buddhism denies exists as ātman)?

The framework's answer (Tiên Đề II: "đổi mà vẫn là mình") operates at the CONVENTIONAL level: identity is a useful designation that persists through change. This aligns with anātmavāda (non-self): there is no permanent self to "keep" — only patterns that persist. The framework's "mình" is saṃvṛti-sat identity, not ātman.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 5 | 5 | 5 | **4.8** | **KEEP** — Confirmed Buddhist alignment. The framework's "mình" is conventional self, consistent with anātmavāda |

---

### C5 × B12 — Gold-Testing Method (RCA #106)

Does C5 invite testing? C5 IS a question — questions invite answers, and answers can be tested. The structure of C5 ("Làm sao...?") is inherently invitational. But the TESTING criterion (how do you know the answer is right?) is downstream in `axioms.html` (Mệnh đề F).

Same root as C1×B12 — Mệnh đề F should be signaled on the landing page.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 3 | 3 | 5 | 5 | 5 | **4.2** | **KEEP (minor)** — Resolved by C1×B12 fix |

---

### C5 × B13 — Scepticism as Methodological Tool (RCA #12, #107)

C5 IS the doubt. "Làm sao giữ được mình...?" = saṃśaya (doubt) + jijñāsā (desire to know). The framework does not start from a declaration — it starts from a question. This is the Buddhist methodological virtue embodied.

The prior audit's C6×L1d ("tái dựng" = 5.0) and C5×L3a (dialectical framing, 3.8, KEEP) both touched this. The Buddhist lens confirms: the question-first architecture IS Buddhist scepticism.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 5 | 5 | 5 | **5.0** | **KEEP** — Confirmed strength across 2 lenses (Buddhist + Kant) |

---

### C5 × B15 — Avidyā → Prajñā (Ignorance → Wisdom) (RCA #42, #54)

**Tier 2 verified** against full source L23-L33, L259-L263.

The Buddhist path: avidyā (ignorance) constructs suffering (duḥkha) → prajñā (wisdom) sees reality as it is (yathābhūtañāṇadassana) → nirvāṇa (liberation).

Mạch Rễ's diagnosis rubric: "rễ nông" (shallow roots = identity at risk) → "rễ sâu" (deep roots = identity resilient). This is structurally parallel to avidyā → prajñā. But there is a crucial DIFFERENCE: Mạch Rễ does NOT claim nirvāṇa (ultimate liberation from assimilation pressure). The prior audit's C5×L2c fix (Requisite Variety limit) already scoped this: "Khung nền không đảm bảo giữ được bản sắc trong mọi điều kiện."

The framework correctly stops at DIAGNOSIS (conventional tool) rather than claiming LIBERATION (soteriological goal). This is epistemically honest. But the mapping to avidyā → prajñā is never acknowledged.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | The Diagnosis Rubric's mapping to avidyā → prajñā is implicit |
| **R2 — Mechanism** | Acknowledging the mapping would STRENGTHEN the Buddhist anchor AND clarify the scope boundary: Mạch Rễ is prajñā (diagnostic wisdom), not nirvāṇa (liberation) |
| **R3 — Root** | Same root as B1, B14 — the Buddhist vocabulary is absent, making structural parallels invisible |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 5 | 5 | 5 | **5.0** | **FIX** — This is the strongest finding: the diagnosis rubric IS the avidyā→prajñā path, correctly scoped. Acknowledging it costs one sentence and gains enormous internal consistency |

**Recommended fix:** Add to the boundary note (L275): "Chẩn đoán 'rễ sâu / rễ nông' là công cụ quy ước — song song với lộ trình từ vô minh (avidyā) đến trí tuệ (prajñā) trong nhận thức luận Phật giáo, nhưng không tuyên bố giải thoát (nirvāṇa)."

---

### C5 — VERDICT SUMMARY

| Lens | Score | Verdict |
|------|-------|---------|
| B1 — Pramāṇa structure | **4.6** | FIX (resolved by C1×B1) |
| B2 — Pratyakṣa/Anumāna | **4.4** | FIX (resolved by C1×B2) |
| B3 — Svalakṣaṇa/Sāmānyalakṣaṇa | **4.2** | KEEP (resolved by C1×B3) |
| B4 — Pramāṇādhīna | **5.0** | KEEP (confirmed strength) |
| B6 — Saṃvṛti-sat (self) | **4.8** | KEEP (confirmed strength) |
| B12 — Gold-testing | **4.2** | KEEP (resolved by C1×B12) |
| B13 — Scepticism | **5.0** | KEEP (confirmed strength) |
| B15 — Avidyā → Prajñā | **5.0** | **FIX** (strongest finding) |

C5 is the most Buddhist-aligned claim on the page. 3 confirmed strengths (B4, B6, B13). The question-first structure, conventional-self framing, and pramāṇādhīna direction are all correct. The only fix is B15: acknowledging the avidyā→prajñā mapping.

---

## CLAIM C6 — "Bản tái dựng (rebuild 2026) suy từ câu hỏi gốc...và kiểm chứng chéo qua 3 hệ độc lập (triangulation)"

**Source:** `index.html` L298
**Context:** Post triple-lens fix: "suy từ câu hỏi gốc (derivation — theo nghĩa điều kiện cần: lời giải thích khả dĩ duy nhất) và kiểm chứng chéo qua 3 hệ độc lập (triangulation)"

---

### C6 × B1 — Pramāṇa Structure (RCA #22-25)

C6 specifies the PRAMĀṆA (means of knowing): derivation from root question + triangulation across 3 independent systems. This is two pramāṇas working together — a composite means.

In Buddhist epistemology, Diṅnāga recognizes exactly TWO pramāṇas: pratyakṣa (perception) and anumāna (inference). C6's composite method maps to anumāna (inference) — specifically svārthānumāna (inference for oneself — the derivation) and parārthānumāna (inference for others — the communication of the framework).

The prior audit's C6 fix (separating derivation from triangulation) already improved clarity. The Buddhist lens confirms the method is structurally sound.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 3 | 5 | 5 | 5 | **4.4** | **FIX (minor)** — Resolved by C1×B1 fix (pramāṇa mapping sentence) |

---

### C6 × B4 — Pramāṇādhīna (Means-First) (RCA #134-135)

C6's "suy từ câu hỏi gốc" (derived from root question) IS pramāṇādhīna: the means (question → derivation → axioms) determines the object (bản sắc sinh tồn), not vice versa. Same finding as C5×B4 — confirmed alignment.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 5 | 5 | 5 | **5.0** | **KEEP** — Confirmed Buddhist alignment |

---

### C6 × B11 — Trairūpya-Hetu (Three Criteria of Valid Reason) (RCA #128, #180-183)

**Tier 2 verified** against full source L233-L261.

A valid inference in Buddhist logic requires the three-criteria sign (trairūpya-liṅga):
1. **Pakṣadharmatva**: the reason must be a property of the subject
2. **Sapakṣe sattvam** (anvaya): the reason must occur in similar cases
3. **Vipakṣe asattvam** (vyatireka): the reason must NOT occur in dissimilar cases

C6 claims the axioms are "derived" (anumāna). Does this derivation satisfy trairūpya?

- **Pakṣa (subject)**: Vietnamese identity-survival behavior
- **Hetu (reason)**: the pattern appears across 3 independent systems (Buddhist epistemology, cybernetics, organizational theory)
- **Sādhya (what is to be proved)**: the 8 axioms capture the structural conditions of identity survival

**Criterion 1 (pakṣadharmatva)**: Is the reason (triangulation across 3 systems) a property of the subject (Vietnamese identity)? PARTIALLY — the triangulation is a METHODOLOGICAL property, not a property of Vietnamese identity itself. The method belongs to the FRAMEWORK, not to the subject.

**Criterion 2 (sapakṣe sattvam)**: Does triangulation across 3 independent systems occur in similar cases (other cultures' identity-survival patterns)? NOT YET DEMONSTRATED — the framework has not been tested on non-Vietnamese cases.

**Criterion 3 (vipakṣe asattvam)**: Does triangulation fail in dissimilar cases (cases where identity does NOT survive)? NOT YET TESTED — Mệnh đề F provides falsification conditions but empirical testing has not been done.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | C6 presents the derivation as COMPLETE ("Bản tái dựng...suy từ..."), but trairūpya criteria 2 and 3 are not yet satisfied by published evidence |
| **R2 — Mechanism** | The prior audit's C6×L2d (triangulation = constraint detection, 5.0) confirmed the method is sound IN PRINCIPLE. But trairūpya asks: has it been DEMONSTRATED? The answer is: in principle yes, in published practice no. The gap between principled validity and demonstrated validity is unmarked |
| **R3 — Root** | The framework's derivation is logically sound (condition 1 satisfied) but empirically incomplete (conditions 2 and 3 untested). The landing page presents it as complete. Root cause: **the epistemological status of the derivation (principled vs demonstrated) is unstated** |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 3 | 3 | 4 | **4.0** | **KEEP** — The finding is real but fixing it on the landing page is premature. This is a research-program-level finding, not a wording fix |

**Finding:** C6's derivation satisfies trairūpya criterion 1 (logical structure) but criteria 2 and 3 (empirical demonstration) are future work. The prior audit's C5×L2a (essential variables, future work) and the plan's H3 (empirical testing) already flag this. Document as: "Trairūpya status: criterion 1 ✓, criteria 2–3 = future empirical work."

---

### C6 — VERDICT SUMMARY

| Lens | Score | Verdict |
|------|-------|---------|
| B1 — Pramāṇa structure | **4.4** | FIX (resolved by C1×B1) |
| B4 — Pramāṇādhīna | **5.0** | KEEP (confirmed strength) |
| B11 — Trairūpya | **4.0** | KEEP (future work — principled validity confirmed, empirical demonstration pending) |

C6's derivation method is logically sound (B4, B11 criterion 1) and structurally pramāṇa-compatible (B1). The gap is empirical, not logical — and the framework already acknowledges this through Mệnh đề F and "Đang phát triển" badge.

---

## CLAIM C2 — "triết lý sinh tồn được dân tộc Việt Nam thể hiện qua hành vi tập thể trong lịch sử"

**Source:** `index.html` L267
**Context:** Post triple-lens fix: "được dân tộc Việt Nam thể hiện qua hành vi tập thể" (was the prior audit's C2 fix: shifted from "của" to "được thể hiện qua").

---

### C2 × B6 — Saṃvṛti-sat (Conventional Truth) (RCA #99, #110)

C2 claims the philosophy "được thể hiện qua hành vi tập thể" (is manifested through collective behavior). This IS the saṃvṛti-sat framing: the philosophy exists as conventional patterns observable in behavior, not as an ultimate essence. The post-fix wording ("được thể hiện qua" rather than "của") already embodies this.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 5 | 5 | 5 | **4.8** | **KEEP** — Confirmed Buddhist alignment. The observational framing is saṃvṛti-sat |

---

### C2 × B7 — Paramārtha-sat (Ultimate Truth) (RCA #100, #109)

C2 does NOT claim the philosophy is an ultimate essence of Vietnamese people. The post-fix wording ("thể hiện qua hành vi tập thể" — manifested through collective behavior) is observational, not essentialist.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 5 | 5 | 5 | **5.0** | **KEEP** — Confirmed strength |

---

### C2 × B8 — Apoha Semantics (RCA #5, #74)

"Triết lý sinh tồn" (survival philosophy) — how is this concept formed? In apoha semantics, a concept is formed by excluding what it is NOT. "Survival philosophy" means: the set of practices and beliefs that are NOT non-survival, NOT random, NOT externally imposed.

The prior audit's C2 fix ("theo cách đọc của tác giả, không phải tiếng nói duy nhất") already embodies apoha logic: it defines the framework's claim by EXCLUDING totalizing ownership. This is apoha-compatible framing.

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 3 | 3 | 5 | 5 | 5 | **4.2** | **KEEP** — Apoha logic is already implicit in the post-fix wording. Resolved by C1×B8 fix |

---

### C2 — VERDICT SUMMARY

| Lens | Score | Verdict |
|------|-------|---------|
| B6 — Saṃvṛti-sat | **4.8** | KEEP (confirmed strength) |
| B7 — Paramārtha-sat | **5.0** | KEEP (confirmed strength) |
| B8 — Apoha | **4.2** | KEEP (resolved by C1×B8) |

All 3 passes confirm Buddhist alignment. The prior audit's C2 fixes (observational framing + authorial modesty) pre-emptively addressed Buddhist epistemological concerns.

---

## CLAIM C12 — "Mạch Rễ tồn tại trước mọi nhà nước Việt Nam hiện đại và thuộc về toàn thể dân tộc" + "Phi chính trị · Phi tôn giáo"

**Source:** `index.html` L400-403 (disclaimer), L253 (badge), L484 (footer)
**Context:** The political/religious disclaimer and scope badges.

---

### C12 × B9 — Prasajya vs Paryudāsa Negation (RCA #72-73)

In Buddhist logic:
- **Prasajya-pratiṣedha** (non-implicative negation): "X is not Y" — mere negation, no positive implication
- **Paryudāsa-pratiṣedha** (implicative negation): "X is not Y" — implying "X is therefore Z"

"Phi chính trị · Phi tôn giáo" (non-political · non-religious) — which negation type?

The **legal disclaimer function** requires prasajya: "This document is not political. Period. It is not religious. Period." Adding "therefore it IS a philosophical framework" (paryudāsa) could create legal ambiguity — "not political BUT philosophical" in some jurisdictions doesn't preclude political interpretation.

The **framework positioning** suggests paryudāsa: "Not political, not religious — therefore it IS a philosophical and anthropological framework." The badges ("Phi chính trị · Phi tôn giáo") appear next to "CC BY 4.0" and "Đang phát triển" — they position the framework in academic/scholarly space.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Phi chính trị · Phi tôn giáo" functions as prasajya in legal context and paryudāsa in positioning context — the duality is unexamined |
| **R2 — Mechanism** | In Buddhist debate logic, choosing the wrong negation type produces category errors. If the disclaimer is read as paryudāsa ("therefore philosophical"), a critic could argue that philosophy IS political in some traditions — undermining the disclaimer. If read as prasajya, the framework loses the positive positioning |
| **R3 — Root** | The disclaimer serves two masters (legal protection + framework positioning) with one phrase. The Buddhist distinction between negation types reveals the tension but does not generate a fix — the dual function is inherent to the disclaimer genre |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 3 | 2 | 2 | 4 | **3.0** | **KEEP** — Below threshold. Interesting Buddhist-logic insight but no feasible fix without legal review. The disclaimer's dual function is inherent, not a defect |

---

### C12 × B12 — Gold-Testing Method (RCA #106)

The disclaimer says "Tài liệu này được soạn thảo và chia sẻ với tinh thần học thuật mở" (this document is authored and shared in the spirit of open scholarship). "Open scholarship" implies openness to testing and critique. But the gold-testing method requires ACTIVE invitation: "test this, don't accept on faith."

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 3 | 3 | 4 | 5 | 5 | **4.0** | **KEEP** — Same as C1×B12. Resolved by C1×B12 fix (signal Mệnh đề F) |

---

### C12 — VERDICT SUMMARY

| Lens | Score | Verdict |
|------|-------|---------|
| B9 — Negation type | **3.0** | KEEP (below threshold) |
| B12 — Gold-testing | **4.0** | KEEP (resolved by C1×B12) |

---

## PHASE 1 — TRIANGULATION SYNTHESIS

### Cross-claim root cause map

26 diagnostic passes across 5 claims reveal 1 recurring root cause:

| Root Cause | Claims affected | Concepts converging | Severity |
|------------|-----------------|---------------------|----------|
| **RC-B1 — Buddhist vocabulary absent**: The framework's method IS compatible with Buddhist pramāṇa-epistemology (pramāṇa structure implicit, Two Truths correctly scoped, pramāṇādhīna direction followed, scepticism embodied, dependent arising structurally encoded, avidyā→prajñā mapped), but the Buddhist TECHNICAL VOCABULARY is missing from the surface — making the Buddhist anchor structurally present but verbally invisible | C1, C5, C6, C2 | B1, B2, B3, B6, B8, B14, B15 | **MEDIUM** — Presentational, not doctrinal. All fixes are vocabulary additions, not structural changes |

### Confirmed Buddhist alignments (strengths)

| Strength | Claims | Concepts | Score |
|----------|--------|----------|-------|
| **Pramāṇādhīna direction** — framework starts from question (means), not from pre-given object | C5, C6 | B4 | 5.0, 5.0 |
| **No paramārtha-sat drift** — framework correctly stays at conventional truth level | C1, C2 | B7 | 5.0, 5.0 |
| **Scepticism embodied** — question-first architecture IS Buddhist methodological doubt | C1, C5 | B13 | 5.0, 5.0 |
| **Saṃvṛti-sat self** — "mình" is conventional self, consistent with anātmavāda | C5 | B6 | 4.8 |
| **Saṃvṛti-sat method** — observational framing ("được thể hiện qua") | C2 | B6 | 4.8 |
| **Apoha-compatible** — post-fix wording uses exclusion-based framing | C2, C1 | B8 | 4.2-4.4 |
| **Trairūpya criterion 1** — derivation has sound logical structure | C6 | B11 | 4.0 |

### Fix priority

| Priority | Claim | Fix | Effort | Depends on |
|----------|-------|-----|--------|------------|
| **P0** | C1 | Add single pramāṇa-structure mapping sentence (resolves B1, B2, B3, B6, B14, B15 for ALL claims) | 1 sentence | None |
| **P1** | C1 | Clarify "nhận dạng" as anumāna (B2) | 1 parenthetical | None |
| **P1** | C1 | Add svalakṣaṇa/sāmānyalakṣaṇa scope justification (B3) | 1 sentence | None |
| **P1** | C5 | Acknowledge avidyā→prajñā mapping for diagnosis rubric (B15) | 1 sentence | None |
| **P2** | C1 | Add apoha acknowledgment (B8) | 1 sentence | None |
| **P2** | C1 | Signal Mệnh đề F on landing page (B12) | 1 short sentence | None |
| **P2** | C1 | Acknowledge Tiên Đề I = pratītyasamutpāda (B14) | 1 sentence near C6/C7 | None |

### Findings deferred or cross-referenced

| Finding | Why |
|---------|-----|
| B5 — Non-distinction means/result (3.8) | Nuance-level; flag for `what.html` |
| B9 — Negation type (3.0) | Below threshold; no feasible fix without legal review |
| B11 — Trairūpya criteria 2-3 (4.0) | Future empirical work; already flagged by prior audit |
| B3 — Closes prior audit C5×L2a (essential variables) | Buddhist epistemology provides philosophical justification for inexpressibility of particulars |

---

## RECALIBRATION CHECKPOINT

| Question | Assessment |
|----------|------------|
| Are the 15 selected concepts sufficient? | **Yes** — All 5 claims received ≥2 concept passes. No claim lacked Buddhist-epistemological coverage |
| RCA table accuracy? | **No issues found** — All 4 Tier 2 escalations (B1, B8, B11, B15) confirmed the RCA table definitions |
| Tier 2 escalation rate? | **4/26 = 15%** — Low. RCA table definitions were sufficient for most passes |
| Do findings contradict prior triple-lens findings? | **No contradictions** — Buddhist lens CONFIRMS 5 prior strengths (Black Box = anumāna, dialectical definition, triangulation, "tái dựng", process framing) and PROVIDES VOCABULARY for the prior audit's RC1 (epistemological underspecification) |
| Is the Buddhist lens finding defects the Kant lens missed? | **Yes — 1 genuinely new finding**: the Buddhist vocabulary is absent (RC-B1). The Kant lens found epistemological UNDERSECIFICATION; the Buddhist lens finds VOCABULARY ABSENCE. The methods are compatible; the labels are missing |
| Expand concept set for Phase 2? | **No** — Current 15 concepts are sufficient. Phase 2 claims have fewer concept overlaps |
| Most significant finding? | **B15 (avidyā→prajñā, 5.0/5)**: the diagnosis rubric IS the Buddhist path, correctly scoped (no nirvāṇa claim), but the mapping is invisible. Acknowledging it costs one sentence and gains maximum internal consistency |
| Meta-finding? | **The Buddhist anchor is REAL but INVISIBLE.** 7 confirmed Buddhist alignments vs 0 Buddhist vocabulary terms on the landing page. The framework IS Buddhist-epistemologically sound, but it doesn't SAY so. This is a presentational gap, not a doctrinal one |

---

*Phase 1 complete. 5 claims audited (2 CRITICAL + 3 HIGH). 26 diagnostic passes. 4 Tier 2 escalations. 7 fixes recommended (1 P0, 3 P1, 3 P2). 7 Buddhist alignments confirmed. 1 root cause (RC-B1: vocabulary absent). 0 contradictions with prior triple-lens audit.*

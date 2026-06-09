# RCA AUDIT — Phase 1: HIGH-Priority Claims (`index.html` × Triple Lens)
<!-- 3-round RCA × 5-Why × scoring gate ≥ 4/5 — executed 2026-06-09 -->
<!-- Tier 2 escalations documented inline -->

## METADATA

```
document_type     : audit_report_phase1
plan              : plan/PLAN_RCA_audit_index_html_triple_lens.md (v2)
audit_target      : index.html (L244–348 — Zones Z1–Z3)
claims_audited    : C5, C1, C3, C2, C6 (5 HIGH-priority claims; C12 deferred to Phase 2 as MEDIUM)
lens_passes       : 24 diagnostic passes (8 + 7 + 4 + 2 + 3)
tier2_escalations : 5 (L1a, L1b, L2a, L2c, L3d — all confirmed RCA table accuracy)
fixes_recommended : 10 (2 P0-critical, 4 P1-important, 4 P2-nice-to-have)
strengths_confirmed: 4
status            : COMPLETE
```

---

## CLAIM C5 — "Làm sao giữ được mình khi tất cả muốn thay đổi mình?"

**Source:** `index.html` L271–273, `<div class="central-question">`
**Context:** Presented as THE central question of Mạch Rễ, immediately after the framework definition. Styled as a highlighted quote box — the most visually prominent claim on the page.

### C5 × L1a — Transcendental Argument Form (Kant RCA #2)

**Tier 2 verified** against `Kant_Transcendental_Arguments.html` L7–L20.

C5 states a premise about experience ("everything wants to change you") from which axioms are derived (C6: "suy từ câu hỏi gốc"). This is structurally a transcendental argument: compelling premise → substantive, unobvious necessary condition. But `index.html` does not label the inference type. "Suy" (derive) could mean transcendental deduction, abductive inference, or heuristic derivation.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Suy từ câu hỏi gốc" does not specify the logical force of the derivation |
| **R2 — Mechanism** | A transcendental argument requires the premise to establish *necessary conditions*; if the derivation is merely heuristic, the axioms don't inherit necessity — but the architecture (4 core + 4 derived + 1 meta) *looks* like a necessary-condition structure |
| **R3 — Root** | The framework uses a transcendental-style argument structure without adopting the epistemological vocabulary to specify the inference type. Root cause: **the derivation method is structurally Kantian but verbally underspecified** |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 5 | 5 | 5 | **4.8** | **FIX** — Add inference-type label |

**Recommended fix:** After "suy từ câu hỏi gốc," add: "theo nghĩa: các tiên đề là điều kiện cần (necessary conditions) để câu hỏi có câu trả lời khả dĩ — không phải suy diễn logic, mà là lời giải thích khả dĩ duy nhất (the only possible explanation, Kantian sense)."

---

### C5 × L1b — Necessary Condition (Weaker Than Logical) (Kant RCA #3)

**Tier 2 verified** against `Kant_Transcendental_Arguments.html` L16–L20.

Kant's own transcendental arguments use a *weaker* necessity: "the only possible explanation" rather than logical necessity. C5's derivation doesn't claim logical necessity — this is good. But it also doesn't claim the weaker Kantian sense — it claims nothing about necessity at all.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | The necessity status of the axiom→question relationship is unstated |
| **R2 — Mechanism** | Readers may assume logical necessity (too strong → overclaim) or mere heuristic (too weak → why 8 axioms specifically?) |
| **R3 — Root** | Same root as L1a — the framework hasn't formalized its inference type. The fix from L1a (adding "điều kiện cần theo nghĩa Kant") resolves this simultaneously |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 4 | 5 | 4 | 5 | **4.4** | **FIX** — Resolved by L1a fix |

---

### C5 × L1d — Modest Transcendental Argument (Kant RCA #58)

Stroud's challenge (1968): transcendental arguments can only establish *beliefs* or *conceptual commitments*, not mind-independent existence. Should Mạch Rễ adopt modest scope?

The framework already operates in modest territory — it systematizes a "triết lý sinh tồn" that was *lived* (conceptual commitment of a culture), not a mind-independent ontological fact. But C5's wording "tất cả muốn thay đổi mình" could be read as universal ("all possible entities face assimilation") rather than contextual ("the forces acting on Vietnamese identity").

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Tất cả" (everything) is ambiguous between universal and contextual scope |
| **R2 — Mechanism** | Vietnamese is a high-context language — "tất cả" in context means "everything around you" not "all logically possible entities." But in English translation, the universal reading is more natural |
| **R3 — Root** | The claim's scope is contextually clear to a Vietnamese reader but ambiguous in translation — a localization issue, not a logical defect |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 3 | 3 | 5 | 5 | 5 | **4.2** | **FIX (minor)** — Add contextual scoping for translation resilience |

**Recommended fix:** Change "khi tất cả muốn thay đổi mình" → "khi mọi thứ xung quanh muốn thay đổi mình" (narrows "tất cả" to contextual "mọi thứ xung quanh").

---

### C5 × L2a — Essential Variables (Ashby RCA #72)

**Tier 2 verified** against `Ashby.txt` L4938–L5037 (S.10/3–10/6).

Ashby: survival = essential variables E kept within acceptable limits η. C5 asks "làm sao giữ được mình" — this IS the essential-variable question. But Mạch Rễ does not specify what the essential variables ARE. "Bản sắc sinh tồn" (survival identity) is the placeholder, not the operationalization.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Bản sắc sinh tồn" is a unitary concept — no decomposition into measurable variables |
| **R2 — Mechanism** | Without specifying E, the regulator F (axioms + practices) cannot be evaluated. The Diagnosis Rubric needs criteria for "rễ sâu" vs "rễ nông" |
| **R3 — Root** | The framework is at the *philosophical* level (making identity intelligible), not the *engineering* level (measuring identity). Operationalizing "bản sắc" into variables is a research program, not a definitional fix |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 3 | 3 | 4 | 4 | **3.6** | **KEEP** — Document as known limitation / future work |

**Finding:** Gap is real but feasibility is low. The Ashby lens asks for a level of formalization the framework doesn't currently claim. Flag as: "Future work: operationalize 'bản sắc sinh tồn' into essential variables with specified acceptable limits η."

---

### C5 × L2c — Variety + Law of Requisite Variety (Ashby RCA #53, #77)

**Tier 2 verified** against `Ashby.txt` L5200–L5260 (S.11/6–11/7).

Ashby: V_O ≥ V_D − V_R. Only variety in the regulator can reduce variety in the essential variables. C5's "tất cả muốn thay đổi mình" = disturbances D with variety V_D. The framework (regulator R) must have sufficient variety. But `index.html` never acknowledges a *limit* — it doesn't say "within the scope that the framework can regulate."

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Giữ được mình" is presented without a scope boundary — implicit promise of unbounded regulation |
| **R2 — Mechanism** | If V_D > V_R (assimilation pressures exceed framework's regulatory capacity), the framework cannot guarantee survival. Not stating this creates an implicit over-promise |
| **R3 — Root** | The framework makes a regulatory promise in natural language that, if formalized, is bounded by Requisite Variety — the bound is never stated |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 4 | 5 | 5 | 4 | **4.4** | **FIX** — Add scope limitation |

**Recommended fix:** Add to the "What is" paragraph: "Khung nền không đảm bảo giữ được bản sắc trong mọi điều kiện — nó cung cấp công cụ nhận dạng và thực hành, và hiệu quả phụ thuộc vào mức độ đa dạng của áp lực đồng hóa mà nó có thể điều tiết."

---

### C5 × L3a — Loose Coupling — Dialectical Interpretation (Weick RCA #2, #6)

Weick/Orton: loose coupling = simultaneous responsiveness AND distinctiveness. C5 asks about distinctiveness ("giữ được mình") under responsiveness pressure ("muốn thay đổi mình"). The question IS the dialectic — it asks how both can coexist. But the framing tilts: "giữ" (keep/defend) frames change as *threat* rather than *resource*.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | C5 frames change purely as threat — missing the possibility that change can strengthen identity |
| **R2 — Mechanism** | The framework's downstream answer (Tiên Đề II: "đổi mà vẫn là mình") restores the dialectic, but a reader who only reads `index.html` gets a unidimensional first impression |
| **R3 — Root** | The question is a *provocation* — its rhetorical purpose IS to sharpen the threat. The tilt is intentional, not accidental |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 3 | 3 | 4 | 5 | 4 | **3.8** | **KEEP** — Rhetorical purpose justifies the framing |

---

### C5 × L3c — Drift Hazard: Presence of Connectedness (Weick RCA #74)

Weick/Orton warn: researchers who enter expecting decoupling are surprised to find connectedness. C5 foregrounds the threat to distinctiveness. But Vietnamese identity is ALSO sustained by intense connectedness (family, lineage, village). The question, taken alone, could give the impression that identity is purely defensive.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | C5 is a survival question ("giữ được mình") — not a flourishing question ("giữ được mình VÀ tiếp tục lớn lên") |
| **R2 — Mechanism** | Vietnamese cultural survival involved proactive synthesis (Buddhism, alphabet, cuisine) — not just defense. The question's purely defensive framing underrepresents this |
| **R3 — Root** | The question starts from what's AT RISK (problem-driven framing). The axioms correct this downstream (Tiên Đề VI: "Hóa Nhiễu Thành Sức"), but the correction isn't visible from the landing page |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 3 | 5 | 5 | 4 | **4.2** | **FIX (minor)** — Add growth dimension |

**Recommended fix:** Consider adding a complementary sentence below the question: "Câu hỏi không chỉ là phòng thủ — mà còn là: giữ gì, đổi gì, và lớn lên từ đâu."

---

### C5 × L3e — Simultaneous Loose-Tight Coupling (Weick RCA #64)

Peters & Waterman: tight cultural coupling + loose structural coupling = adaptive identity. C5 treats "mình" (self) as unitary. But identity persistence requires SOME elements to be tightly held (language, relational structure) and others loosely held (tools, aesthetic forms). The framework's axiom hierarchy (core I–IV = tight, derived V–VII = looser) implicitly encodes this, but it's invisible from `index.html`.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Giữ được mình" doesn't distinguish WHAT must be tightly vs loosely coupled |
| **R2 — Mechanism** | Without the tight/loose distinction, "giữ được mình" could justify cultural rigidity (keep everything) rather than strategic preservation (keep the right things) |
| **R3 — Root** | The axiom hierarchy already encodes tight/loose (core = tight, derived = looser), but this architectural feature is downstream of the landing page |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 3 | 4 | 4 | 5 | 5 | **4.2** | **FIX (minor)** — Surface tight/loose on landing page |

**Recommended fix:** Add to the "What is" paragraph: "Một số yếu tố phải giữ chặt (ngôn ngữ, cấu trúc quan hệ), số khác có thể lỏng (hình thức, công cụ) — cốt lõi của khung nền là phân biệt được đâu là gốc rễ, đâu là cành lá."

---

### C5 — VERDICT SUMMARY

| Lens | Score | Verdict |
|------|-------|---------|
| L1a — Transcendental argument form | **4.8** | FIX |
| L1b — Necessary condition | **4.4** | FIX (resolved by L1a) |
| L1d — Modest scope | **4.2** | FIX (minor) |
| L2a — Essential variables | **3.6** | KEEP (future work) |
| L2c — Requisite Variety | **4.4** | FIX |
| L3a — Dialectical framing | **3.8** | KEEP (rhetorical intent) |
| L3c — Connectedness drift | **4.2** | FIX (minor) |
| L3e — Tight/loose coupling | **4.2** | FIX (minor) |

**Triangulation:** L1a + L1b + L2c converge on a single root cause → **CONFIRMED**: the epistemological status of C5 and its relationship to the axioms is underspecified. 5/8 passes recommend fix (all above threshold). The fix is a boundary/clarification statement, not a substantive change.

**Root cause (one sentence):** `index.html` deploys a transcendental-style argument structure (premise→derivation→axioms) without specifying the inference type, necessity strength, or scope boundary, leaving the framework's epistemic ambition ambiguous to readers.

---

## CLAIM C1 — "Mạch Rễ là khung nền (framework) nhận dạng và thực hành bản sắc sinh tồn"

**Source:** `index.html` L265–269
**Context:** The opening definitional paragraph. This is THE definition of Mạch Rễ — everything else hangs on it.

### C1 × L1e — Objective Validity (Kant RCA #11)

Kant: objective validity = "the property of a concept or representation whereby it correctly applies to, or represents, objects of experience." What would it mean for a Tiên Đề to have "objective validity"? Is this claimed?

C1 defines Mạch Rễ as a "khung nền nhận dạng và thực hành" (framework for recognition and practice). "Nhận dạng" (recognition) is epistemological — it claims to correctly IDENTIFY something real. "Thực hành" (practice) is pragmatic — it claims to provide usable tools. The framework claims both: it correctly DESCRIBES identity survival AND provides tools to PRACTICE it. But objective validity (in Kant's sense) requires that the description correctly applies to objects of experience — a claim `index.html` does not explicitly make or defend.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | C1 claims descriptive accuracy ("nhận dạng") without stating the standard of correctness |
| **R2 — Mechanism** | "Nhận dạng" implies the framework can correctly identify identity-survival patterns. But by what criterion is a "nhận dạng" correct? The framework doesn't specify |
| **R3 — Root** | The framework conflates two claims: (a) "this framework provides a vocabulary for describing identity survival" (modest, interpretive) and (b) "this framework correctly identifies real patterns" (stronger, validity-claiming). The landing page wording leans toward (b) without supporting it |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 3 | 4 | 4 | 4 | **3.8** | **KEEP** — The ambiguity is more about word choice than structural defect; "nhận dạng" is reasonably read as "provides recognition tools" |

---

### C1 × L2a — Essential Variables (Ashby RCA #72)

Same lens as C5×L2a, applied to the definitional claim. "Bản sắc sinh tồn" (survival identity) is the concept the framework claims to help "nhận dạng" (recognize). But what is being recognized? In Ashby's terms: what are the essential variables E, and what is the acceptable set η?

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Bản sắc sinh tồn" is not decomposed into measurable components |
| **R2 — Mechanism** | Without specifying E, the framework cannot distinguish "nhận dạng đúng" (correct recognition) from "nhận dạng sai" (incorrect recognition) |
| **R3 — Root** | Same root as C5×L2a — the framework is philosophical, not operational. The gap is real but the fix is a research program |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 3 | 3 | 2 | 4 | 4 | **3.2** | **KEEP** — Below threshold; future work |

---

### C1 × L2b — Survival as Stability (Ashby RCA #71)

Ashby formalizes "survival" as: a set of states M₁…Mₖ is stable under operation C if C maps every living state to another living state. "Sinh tồn" (survival) in C1 is used as a descriptive label, not a formal concept. The framework does not define what counts as "survival" vs "non-survival."

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Sinh tồn" is used colloquially, not operationally |
| **R2 — Mechanism** | Without a survival criterion, the framework cannot distinguish "bản sắc đang sinh tồn" from "bản sắc đang biến mất" except by post-hoc historical judgment |
| **R3 — Root** | The framework derives its concept of survival from Vietnamese history (4000 years of persistence = survival), which is a post-hoc criterion — it identifies survival after the fact but cannot predict it |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 2 | 4 | 3 | **3.6** | **KEEP** — Important finding, but fixing requires redefining "survival" predictively, which is a major structural change |

---

### C1 × L2f — Black Box (Ashby RCA #47)

Ashby: Black Box = system whose internal structure is unknown; only I/O behavior observable. Is Vietnamese cultural history treated as a Black Box (inferring structure from observed I/O), or is internal structure assumed?

C1 claims the framework "đặt tên và hệ thống hóa" (names and systematizes) a philosophy that was "được sống" (lived) but never "được viết" (written). This IS a Black Box approach: the philosophy existed in behavior (output), and the framework infers its structure. This is methodologically sound and honest. The framework does NOT claim to know the internal structure a priori.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | None — the Black Box approach is correctly implicit |
| **R2 — Mechanism** | The "được sống…chưa được viết" framing is exactly the Black Box premise: behavior exists, structure must be inferred |
| **R3 — Root** | No defect — this is a strength. The framework's epistemic modesty (we infer from observed behavior) is consistent with Ashby's methodology |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 5 | 5 | 5 | **4.8** | **KEEP** — This is a confirmed strength, not a defect |

---

### C1 × L3a — Loose Coupling — Dialectical (Weick RCA #2, #6)

Weick/Orton: loose coupling = simultaneous responsiveness AND distinctiveness. C1 defines Mạch Rễ as "nhận dạng và thực hành bản sắc sinh tồn" — "nhận dạng" (recognition = understanding distinctiveness) AND "thực hành" (practice = responsive action). The definition itself IS dialectical: it binds understanding (closed, reflective) with practice (open, responsive).

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | None — the definition is structurally dialectical |
| **R2 — Mechanism** | "Nhận dạng" + "thực hành" mirrors Weick/Orton's "distinctiveness + responsiveness" |
| **R3 — Root** | Confirmed strength — the framework's definition preserves the dialectic from the first sentence |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 5 | 5 | 5 | **4.8** | **KEEP** — Confirmed strength |

---

### C1 × L3b — Drift Hazard: Imprecise Generalization (Weick RCA #72)

**Tier 2 verified** against `Orton_Weick.txt` L854–L874 (static vs dynamic description) and L894–L898 (drift hazard).

Weick/Orton: researchers drift by chaining from "loose coupling claim" → "performance conclusion" without specifying elements, domains, characteristics. C1 defines Mạch Rễ as applying to "cá nhân, cộng đồng, và tổ chức" — three very different levels of analysis. Does the framework specify HOW the same axioms apply differently at each level?

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | C1 chains from "framework for identity survival" → "applies to individuals, communities, AND organizations" without level-specific operationalization |
| **R2 — Mechanism** | Ashby's essential variables for an individual (psychological identity), a community (shared practices), and an organization (institutional continuity) are DIFFERENT variables. Claiming the same framework works for all three invites imprecise generalization |
| **R3 — Root** | The framework's isomorphism claim (3 systems share the same relational structure) is the theoretical justification for cross-level applicability. But if the isomorphism is actually homomorphism (many-one, lossy — see C14), the cross-level claim is weaker than stated |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 4 | 4 | 3 | 4 | **3.8** | **KEEP** — Depends on C14 (isomorphism vs homomorphism) resolution in Phase 2 |

---

### C1 × L3d — Static vs. Dynamic Description (Weick RCA #71)

**Tier 2 verified** against `Orton_Weick.txt` L846–L858.

Weick/Orton: "researchers who see systems as static objects to be labeled ('this is a loosely coupled system') are less likely to capture loose coupling than are researchers who see systems as an arena for complex, ongoing processes ('loose coupling in this system occurs when…')."

C1 says: "Mạch Rễ **là** khung nền…" — noun-based, static labeling. The entire "What is" section uses "là" (is) repeatedly. This is the "flat, static description" that Weick/Orton warn against.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | `index.html` uses predominantly static/noun-based framing: "Mạch Rễ LÀ…", "Đây LÀ…" |
| **R2 — Mechanism** | Noun-based labeling reifies the framework as a fixed object rather than a dynamic process. A visitor's first impression is of a product, not a practice |
| **R3 — Root** | The landing page's rhetorical purpose (introducing WHAT something is) naturally pulls toward static description. But the framework's content is dynamic (practices, diagnosis, adaptation). The landing page's genre convention (definitional introduction) is in tension with the framework's processual nature |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 5 | 5 | 4 | **4.6** | **FIX** — Add at least one verb-based sentence |

**Recommended fix:** After the static definition, add: "Nói cách khác: Mạch Rễ không phải là một vật cố định để dán nhãn — nó là một quá trình: bản sắc sinh tồn **diễn ra khi** một cộng đồng vừa giữ được cấu trúc quan hệ cốt lõi, vừa thích nghi được với áp lực bên ngoài."

---

### C1 — VERDICT SUMMARY

| Lens | Score | Verdict |
|------|-------|---------|
| L1e — Objective validity | **3.8** | KEEP |
| L2a — Essential variables | **3.2** | KEEP (future work) |
| L2b — Survival as stability | **3.6** | KEEP (future work) |
| L2f — Black Box | **4.8** | KEEP (confirmed strength) |
| L3a — Dialectical definition | **4.8** | KEEP (confirmed strength) |
| L3b — Imprecise generalization | **3.8** | KEEP (depends on C14) |
| L3d — Static vs dynamic | **4.6** | **FIX** |

**Triangulation:** L2f + L3a converge on CONFIRMED STRENGTH (Black Box methodology + dialectical definition). L3d is the only above-threshold fix — static/noun-based framing. C1 is structurally sound; the main improvement is adding processual language.

---

## CLAIM C3 — "được sống qua 4.000 năm nhưng chưa bao giờ được viết thành lý thuyết"

**Source:** `index.html` L267–268
**Context:** The historical existence claim — the philosophy existed in practice for 4000 years but was never formalized as theory.

### C3 × L1c — Stroud's Challenge (Kant RCA #57)

Stroud (1968): transcendental arguments can only establish a *belief* about existence, not existence itself. C3 claims: (a) the philosophy EXISTED in practice for 4000 years, and (b) it was never THEORIZED. Claim (a) is an existence claim. Claim (b) is an absence claim.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Chưa bao giờ được viết thành lý thuyết" (never written as theory) is a strong universal negative — it claims NO prior theorization exists |
| **R2 — Mechanism** | Vietnamese scholarship HAS produced theoretical fragments: Phan Ngọc's "Bản sắc Văn hóa Việt Nam," Trần Đình Hượu's work on Vietnamese cultural patterns, etc. These aren't FULL frameworks, but they are theoretical fragments. The claim "chưa bao giờ" is falsified by their existence |
| **R3 — Root** | The claim conflates "chưa được hệ thống hóa thành framework hoàn chỉnh" (never systematized into a complete framework) with "chưa bao giờ được viết thành lý thuyết" (never written as theory at all). The former is defensible; the latter is not |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 5 | 5 | 5 | **4.8** | **FIX** — Scope the claim |

**Recommended fix:** Change "chưa bao giờ được *viết* thành lý thuyết" → "chưa từng được *hệ thống hóa* thành một khung nền (framework) hoàn chỉnh." This preserves the core claim (Mạch Rễ is the first complete framework) while avoiding the falsifiable universal negative.

---

### C3 × L2b — Survival as Stability (Ashby RCA #71)

Ashby formalizes survival as stability of a set of states under transformation. C3's "4.000 năm" is precisely what Ashby would call a stability claim: the identity-system has persisted (remained in acceptable states η) across 4000 years of disturbances. But the framework doesn't formalize WHAT persisted — it gestures at "triết lý sinh tồn" without specifying the transformation or the stable set.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "4.000 năm" is used as an existence proof without defining what was stable across that period |
| **R2 — Mechanism** | Without specifying the stable set, "4.000 năm" can be pattern-matched to any narrative of continuity. Was it language? Family structure? Rice agriculture? All of the above? Different answers → different frameworks |
| **R3 — Root** | The 4000-year claim functions as a rhetorical anchor ("this is deep") rather than as a formal stability claim ("these specific variables remained within these specific limits") |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 4 | 3 | 4 | 4 | **3.8** | **KEEP** — Important nuance, but 4000 years as rhetorical anchor is acceptable for a landing page |

---

### C3 × L2f — Black Box (Ashby RCA #47)

Same lens as C1×L2f. C3's "được sống…chưa được viết" is the Black Box premise applied historically: the system's behavior was observable (survival outcomes), but its internal structure was not documented.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | None — consistent with C1×L2f finding |
| **R2 — Mechanism** | The historical claim is methodologically honest: we observe survival, we infer structure |
| **R3 — Root** | Confirmed strength — the Black Box framing is consistent across C1 and C3 |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 5 | 5 | 5 | **4.8** | **KEEP** — Confirmed strength |

---

### C3 × L3c — Drift Hazard: Presence of Connectedness (Weick RCA #74)

**Tier 2 verified** against `Orton_Weick.txt` L875–L879.

Weick/Orton: researchers who expect decoupling are surprised by connectedness. C3 focuses on WHAT PERSISTED (the invariant). But Vietnamese history is also characterized by intense CONNECTEDNESS with external forces: Chinese cultural import, French colonial influence, American engagement, global capitalism. The framework could drift toward a "pure persistence" narrative that ignores how MUCH external connection shaped Vietnamese identity.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | C3 emphasizes continuity ("được sống qua 4.000 năm") without acknowledging that survival occurred THROUGH connection, not despite it |
| **R2 — Mechanism** | The timeline (C8–C11) actually DOES show connection events (Buddhism, 500kV modernization, US reconciliation) — but C3's wording frames these as "things that happened TO a persistent identity" rather than "interactions that SHAPED identity" |
| **R3 — Root** | The rhetorical structure of C3 (survival despite everything) creates a subtle drift: identity as something that ENDURED external forces, rather than something that ABSORBED and TRANSFORMED through them |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 3 | 5 | 4 | 4 | **4.0** | **FIX (minor)** — Add absorption dimension |

**Recommended fix:** Change "được *sống* qua 4.000 năm" → "được *sống* và *liên tục thích nghi* qua 4.000 năm" — adds the absorption/adaptation dimension.

---

### C3 — VERDICT SUMMARY

| Lens | Score | Verdict |
|------|-------|---------|
| L1c — Stroud's challenge | **4.8** | **FIX** |
| L2b — Survival as stability | **3.8** | KEEP |
| L2f — Black Box | **4.8** | KEEP (confirmed strength) |
| L3c — Connectedness drift | **4.0** | **FIX (minor)** |

**Triangulation:** L1c is the only strong fix — an overclaim ("chưa bao giờ") that needs scoping. L3c adds nuance. Two confirmed strengths (L2f, L3c-partial). The claim is structurally sound with one significant wording fix needed.

---

## CLAIM C2 — "đặt tên và hệ thống hóa triết lý sinh tồn của dân tộc Việt Nam"

**Source:** `index.html` L266–267
**Context:** The methodological claim — Mạch Rễ NAMES and SYSTEMATIZES. This is the product claim: this is what the framework DOES.

### C2 × L1c — Stroud's Challenge (Kant RCA #57)

C2 claims to "đặt tên và hệ thống hóa" — name and systematize. "Hệ thống hóa" (systematize) is an epistemic act: it claims to ORGANIZE existing knowledge into a coherent structure. But Stroud's challenge applies: does the framework DISCOVER a structure that was already there, or IMPOSE a structure that makes sense of the data?

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Hệ thống hóa" could mean either "discover the latent system" or "impose a useful system" |
| **R2 — Mechanism** | If the framework discovers a latent system, it claims objective validity (Kant). If it imposes a useful system, it claims interpretive utility (modest). The word "hệ thống hóa" doesn't distinguish |
| **R3 — Root** | Same root as C5×L1a — the epistemological status of the framework's relationship to its subject matter is underspecified |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 4 | 5 | 5 | 4 | **4.4** | **FIX** — Clarify discover vs impose |

**Recommended fix:** After "hệ thống hóa," add: "— không phải áp đặt một hệ thống từ bên ngoài, mà là làm hiển lộ (make explicit) cấu trúc vốn đã tồn tại trong thực hành."

---

### C2 × L3b — Drift Hazard: Imprecise Generalization (Weick RCA #72)

C2 claims the framework systematizes "triết lý sinh tồn của dân tộc Việt Nam" — the survival philosophy of the VIETNAMESE PEOPLE. This is a collective subject: "dân tộc Việt Nam" is ~100 million people across multiple generations, regions, classes, and diasporas. Does the framework specify WHICH Vietnamese people's philosophy it systematizes? Or does it implicitly claim to represent ALL Vietnamese?

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Của dân tộc Việt Nam" is a totalizing claim — it implies the framework represents the philosophy of the entire people |
| **R2 — Mechanism** | Any framework that claims to represent "the Vietnamese people's survival philosophy" faces an insurmountable diversity problem: urban vs rural, northern vs southern, domestic vs diaspora, elite vs popular, historical vs contemporary |
| **R3 — Root** | The framework needs a scope boundary: it systematizes ONE interpretation (the author's) of patterns observed across Vietnamese history, not THE philosophy of the Vietnamese people as a monolithic entity |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 4 | 4 | 4 | 3 | **4.0** | **FIX** — Add representational modesty |

**Recommended fix:** Change "triết lý sinh tồn của dân tộc Việt Nam" → "triết lý sinh tồn đã được dân tộc Việt Nam thể hiện qua hành vi tập thể trong lịch sử" — shifts from ownership claim ("của") to observational claim ("được thể hiện qua"). OR add a caveat: "— theo cách đọc (reading) của tác giả, không phải tiếng nói duy nhất."

---

### C2 — VERDICT SUMMARY

| Lens | Score | Verdict |
|------|-------|---------|
| L1c — Stroud (discover vs impose) | **4.4** | **FIX** |
| L3b — Imprecise generalization | **4.0** | **FIX** |

Both passes recommend fix. The core issue: C2 claims too much epistemic authority for what it actually delivers.

---

## CLAIM C6 — "Bản tái dựng (rebuild 2026) suy từ câu hỏi gốc, neo 3 hệ độc lập"

**Source:** `index.html` L295 (axioms.html nav card description)
**Context:** The derivation method claim — how the axioms were produced.

### C6 × L1a — Transcendental Argument Form (Kant RCA #2)

C6 uses "suy từ câu hỏi gốc" (derived from the root question) — this is the same verb "suy" as in C5. The claim is that the 8 axioms are DERIVED from the central question. But "suy" is ambiguous: deduction? abduction? heuristic derivation?

Additionally, C6 says "neo 3 hệ độc lập" (anchored in 3 independent systems) — this is the TRIANGULATION method. The axioms are not ONLY derived from the question; they're also CONSTRAINED by three independent systems. This is methodologically sophisticated: it prevents single-anchor overfitting.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | "Suy từ câu hỏi gốc" inherits C5's ambiguity about inference type |
| **R2 — Mechanism** | The triangulation method ("neo 3 hệ") partially compensates: even if the derivation is heuristic, the 3-anchor constraint provides independent validation. But the relationship between "suy" (derivation) and "neo" (anchoring) is unclear — are they sequential (derive, then validate) or simultaneous (co-constrain)? |
| **R3 — Root** | The framework has TWO epistemic foundations (derivation from question + triangulation across 3 systems) but `index.html` presents them in one sentence without specifying their logical relationship |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 4 | 4 | 5 | 5 | 5 | **4.6** | **FIX** — Clarify the relationship between derivation and triangulation |

**Recommended fix:** "Bản tái dựng (rebuild 2026) **suy từ** câu hỏi gốc (derivation) và **kiểm chứng chéo qua** 3 hệ độc lập (triangulation): Phật giáo, Điều khiển học (Ashby), và Lý thuyết Tổ chức (Weick/Orton)." This separates the two methods and makes their relationship explicit.

---

### C6 × L1d — Modest Transcendental Argument (Kant RCA #58)

C6 says the axioms are a "tái dựng" (rebuild) — this word is epistemically modest. A "rebuild" is a CONSTRUCTION, not a discovery. It acknowledges the active role of the framework builder. This aligns with the modest transcendental argument: the framework builds a conceptual structure, it doesn't claim to discover mind-independent truths.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | None — "tái dựng" (rebuild) is the right word |
| **R2 — Mechanism** | "Tái dựng" implies: (a) something existed before (the lived philosophy), (b) it's being reconstructed (not created ex nihilo), (c) the reconstruction may differ from the original. All three implications are epistemically honest |
| **R3 — Root** | Confirmed strength — the word choice is precise and modest |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 5 | 5 | 5 | **5.0** | **KEEP** — Confirmed strength |

---

### C6 × L2d — Constraint (Ashby RCA #55)

Ashby: constraint = condition where variety actually present < maximum possible; whenever two variables are not independent, a constraint holds. C6's "neo 3 hệ độc lập" IS a constraint-detection method: it looks for patterns that appear ACROSS independent systems, which is exactly what Ashby means by detecting constraints. If a pattern appears in Buddhist epistemology AND cybernetics AND organizational theory, the variety of possible interpretations is REDUCED — that's a constraint.

| Round | Finding |
|-------|---------|
| **R1 — Symptom** | None — "neo 3 hệ độc lập" is methodologically sound |
| **R2 — Mechanism** | Triangulation across independent systems is a rigorous constraint-detection method. If ≥2/3 systems show the same structural pattern, the pattern is not an artifact of any single system's assumptions |
| **R3 — Root** | Confirmed strength — the triangulation method has a formal justification in Ashby's constraint theory |

| C | D | F | CR | P | Avg | Verdict |
|---|-----|---|---|-----|------|--------|
| 5 | 5 | 5 | 5 | 5 | **5.0** | **KEEP** — Confirmed strength |

**Note:** A finding from Phase 2 (C14 — isomorphism vs homomorphism) may qualify this. If the mapping between the 3 systems is homomorphic (many-one, lossy) rather than isomorphic (one-one, structure-preserving), the constraint is weaker than implied. Flag for Phase 2 integration.

---

### C6 — VERDICT SUMMARY

| Lens | Score | Verdict |
|------|-------|---------|
| L1a — Transcendental argument form | **4.6** | **FIX** |
| L1d — Modest scope ("tái dựng") | **5.0** | KEEP (confirmed strength) |
| L2d — Constraint (triangulation) | **5.0** | KEEP (confirmed strength) |

C6 is the strongest claim on the page — two 5.0/5 confirmed strengths. The only fix is clarifying the derivation/triangulation relationship.

---

## PHASE 1 — TRIANGULATION SYNTHESIS

### Cross-claim root cause map

24 diagnostic passes across 5 claims reveal 3 recurring root causes:

| Root Cause | Claims affected | Lenses converging | Severity |
|------------|-----------------|-------------------|----------|
| **RC1 — Epistemological underspecification**: The framework's inference type, necessity strength, and scope boundary are not stated. "Suy từ câu hỏi gốc" is ambiguous between transcendental derivation, abduction, and heuristic | C5, C2, C6 | L1a, L1b, L1d, L1c | **HIGH** — Affects the framework's core epistemic claim |
| **RC2 — Static/noun-based framing**: The landing page uses predominantly "là" (is) statements, reifying the framework as a fixed object rather than a dynamic process | C1, (C5 partial) | L3d | **MEDIUM** — Presentational, not doctrinal; affects first impressions |
| **RC3 — Totalizing language**: Claims about "dân tộc Việt Nam" and "chưa bao giờ" use universal/collective quantifiers that are falsifiable or over-scoped | C2, C3 | L1c, L3b, L3c | **MEDIUM** — Scoping fixes are straightforward |

### Confirmed strengths

| Strength | Claims | Evidence |
|----------|--------|----------|
| **Black Box methodology** — framework infers structure from observed behavior | C1, C3 | L2f: 4.8, 4.8 |
| **Dialectical definition** — "nhận dạng + thực hành" preserves distinctiveness + responsiveness | C1 | L3a: 4.8 |
| **Triangulation method** — "neo 3 hệ độc lập" as constraint detection | C6 | L2d: 5.0 |
| **Epistemic modesty of "tái dựng"** — acknowledges construction, not discovery | C6 | L1d: 5.0 |

### Fix priority

| Priority | Claim | Fix | Effort | Depends on |
|----------|-------|-----|--------|------------|
| **P0** | C3 | Scope "chưa bao giờ được viết" → "chưa từng được hệ thống hóa thành framework hoàn chỉnh" | 1 word change | None |
| **P0** | C5 | Add inference-type label to "suy từ câu hỏi gốc" (Kantian necessary-condition) | 1 sentence | None |
| **P1** | C2 | Add epistemic modesty: "theo cách đọc của tác giả" + clarify discover vs impose | 1-2 sentences | None |
| **P1** | C6 | Separate derivation from triangulation: "suy từ…và kiểm chứng chéo qua…" | 1 phrase | None |
| **P1** | C5 | Add Requisite Variety scope limitation | 1 sentence | None |
| **P2** | C1 | Add verb-based process framing alongside static definition | 1 sentence | None |
| **P2** | C5 | Contextual scoping for "tất cả" (translation resilience) | 2 words | None |
| **P2** | C5 | Add growth/flourishing dimension | 1 sentence | None |
| **P2** | C5 | Surface tight/loose distinction | 1 sentence | None |
| **P2** | C3 | Add absorption/adaptation dimension ("được sống và liên tục thích nghi") | 3 words | None |

### Findings deferred to Phase 2

| Finding | Why deferred |
|---------|-------------|
| C14 — Isomorphism vs Homomorphism (L2e) | MEDIUM priority; may qualify C6's triangulation strength |
| C1×L3b — Cross-level applicability (depends on C14 resolution) | MEDIUM priority |
| C5×L2a — Essential variables operationalization | KEEP as future work; below fix threshold (3.6/5) |
| C1×L2b — Survival formalization | KEEP as future work; below fix threshold (3.6/5) |

---

## RECALIBRATION CHECKPOINT

| Question | Assessment |
|----------|------------|
| Are the 18 selected Tier 1 concepts sufficient? | **Yes** — No claim had zero lens coverage. All 5 claims received ≥2 lens passes |
| RCA table accuracy? | **No issues found** — All 5 Tier 2 escalations confirmed (not corrected) the RCA table definitions |
| Tier 2 escalation rate? | **5/24 = 21%** — Acceptable. Tier 2 was used for nuance, not for correcting errors |
| Expand concept set for Phase 2? | **No** — Current 18 concepts are sufficient |
| Reduce Phase 2 scope? | **No** — Proceed with full Phase 2 as planned |

---

*Phase 1 complete. 5 HIGH-priority claims audited (C12 deferred to Phase 2 — MEDIUM priority, located in disclaimer zone Z1). 10 fixes recommended (2 P0-critical, 4 P1-important, 4 P2-nice-to-have), 4 strengths confirmed, 4 findings documented as future work.*

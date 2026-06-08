# REVIEW PLAN — Hệ Tiên Đề Mạch Rễ
<!-- source: https://aihugart.github.io/Mach-Re/axioms.html -->
<!-- version: v2 — 2026-06-08 -->
<!-- changes from v1: RCA meta-analysis applied; 5 modifications scored ≥ 4/5; 2 SOTs added (Kant + Madhyamaka) -->
<!-- format: LLM-friendly Markdown — pure doc, no HTML, no emoji clusters -->
<!-- encoding: UTF-8 -->

---

## META

```
document_type   : review_plan
subject         : axiom_spec — Mach Re (Mạch Rễ)
version_reviewed: rendered from axiom_spec.md (as of 2026-06-08)
review_scope    : architecture · internal_consistency · falsifiability
                  operationalizability · agency · cross-tradition tension
output_intent   : human + LLM consumption; structured for diff/patch workflow
plan_version    : v2
rca_applied_to  : review plan itself (meta-level) — 5 modifications, all ≥ 4/5
```

---

## 0. RCA META-REVIEW (new in v2)

This section records the RCA analysis applied to the v1 review plan itself.
All 8 original issues are confirmed valid against `axioms.html` and `what.html`.
Five modifications to the plan were scored; all reached threshold ≥ 4/5.

| MOD | Description | Score | Decision |
|-----|-------------|-------|----------|
| A | Add Implementation Workflow section (file mapping per issue) | 5/5 | ADDED — Section 2.5 |
| B | Add dependency chain annotations (ISSUE-02 blocks ISSUE-03) | 5/5 | ADDED — in each ISSUE entry |
| C | Classify Open Questions by research type | 5/5 | ADDED — Section 6 |
| D | Revise ISSUE-07 fix: reference pointer, not full text repetition | 5/5 | REVISED — ISSUE-07 |
| E | Scope ISSUE-08 Triangulation Protocol as forward-only by default | 5/5 | ADDED — ISSUE-08 |

---

## 0.5 SOURCES OF TRUTH (SOT) — New in v2

Two external SOTs added. These ground the philosophical terminology in ISSUE-02,
ISSUE-03, and ISSUE-05 with citable, locally-available sources.

```
SOT-K  Kant's Transcendental Arguments
       File  : ../documents/public_documents/Kant_Transcendental_Arguments.html
       Use   : ISSUE-02 (BRIDGE-II-III), ISSUE-05 (meta-pattern analogy)
       Key   : "transcendental condition" = necessary structural precondition for
               the possibility of a system — not a metaphysical substance (svabhāva),
               not an empirical generalization. Kant: argument begins with a premise
               about experience and reasons to its necessary presupposition.

SOT-M  Buddhist Pramāṇa-Epistemology, Logic, and Language — RCA Concept Table
       File  : ../documents/public_documents/The_Buddhist_Pramana_Epistemology_Logic_and_Language_RCA_Table.md
       Use   : ISSUE-02 (saṃvṛti-sat precision), ISSUE-03 (Madhyamaka context)
       Key rows:
         Row 99/110 — Saṃvṛtisat: "conventional truth: designation-dependent,
                      conceptual, phenomenal, and pragmatically usable."
         Row 111    — Conventionally real: "that which loses its cognition when
                      broken into parts or mentally abstracted from properties."
                      → Pattern(R(S)) satisfies this: dissolve the collective,
                      the pattern disappears. Pattern is saṃvṛti-sat, not
                      paramārtha-sat.
         Row 112    — Rigorously real (paramārtha-sat): "that which still gives
                      rise to perception after division or abstraction." Pattern
                      does NOT satisfy this → confirms II's scope is conventional.
         Row 59/60  — Madhyamaka / Niḥsvabhāvatā: essencelessness critique of
                      realism. V ⊥ H is a structural claim, not an svabhāva claim.
```

**How SOTs resolve the II × III tension (ISSUE-02):**
- Axiom II's "conventional truth" is precisely saṃvṛtisat (SOT-M Row 110-111):
  the pattern has causal efficacy within the conventional domain without being
  ultimately real (paramārtha-sat).
- Axiom III's "ontological dimension" is a transcendental condition in the
  Kantian sense (SOT-K): V ⊥ H is a necessary structural precondition for
  pattern persistence — not an svabhāva entity (which would contradict II),
  but a condition without which the system cannot operate.
- These two moves together produce BRIDGE-II-III (see ISSUE-02) without
  asserting any ultimate ontological substance.

---

## 1. STRUCTURE MAP (as-is)

```
LAYER_0  meta-axiom
  VIII  Reflexive Cognition       [scope-conditional, observes I–IV]

LAYER_1  core axioms (object-level)
  I     Relational Ontology       [neo: A·B·C — 3/3]
  II    Structural Invariance     [neo: A·B·C-cond — ~2.5/3]
  III   Vertical Temporality      [neo: A-weak·B·C — ~2.5/3]
  IV    Dynamic Boundary          [neo: A·B-strong·C-weak — ~2.5/3]

LAYER_2  derived propositions
  V     Distributed Ontology      [from: I + II]
  VI    Perturbation Transform    [from: II + III + IV]
  VII   Directed Emergence        [from: I + II + III + IV]
```

---

## 2. ISSUE REGISTRY

Each issue has:
- `id`         : unique reference for tracking
- `severity`   : CRITICAL / MAJOR / MINOR / SUGGESTION
- `target`     : axiom(s) affected
- `type`       : logic | ontology | notation | operationalization | agency | scope
- `blocks`     : issues that cannot be resolved until this issue is resolved
- `files`      : files requiring changes if this issue is fixed
- `description`: what the problem is
- `proposed_fix`: concrete revision or addition (with SOT citations where applicable)

---

### ISSUE-01

```
id       : ISSUE-01
severity : CRITICAL
target   : Axiom I
type     : notation + logic
blocks   : none
files    : axiom_spec.md → axioms.html → what.html (axiom I card)
```

**Problem**

The schema `Being(x) ≡ {R(x,y)}` uses `≡` (logical equivalence / definitional
identity). This is stronger than an axiom — it is a *definition*. Definitions
cannot be falsified; axioms can. The document simultaneously claims falsifiability
(SAI nếu...) and uses definitional notation. This is a contradiction.

Additionally, `{R(x,y)}` is underspecified: R is a single binary relation
placeholder, but identity presumably involves a structured *set* of heterogeneous
relations across different domains and timescales.

**Proposed fix**

Option A — Weaken notation to claim, not definition:
```
Being(x) ~= f({R_i(x, y_j)})   where f extracts structural pattern
```
Replace `≡` with `~=` (approximate or structural correspondence) and annotate:
"claim, not definition — falsifiable via falsification condition F1."

Option B — Separate definition from claim:
```
[DEF-1]  Relational profile of x  =def  RP(x) := {R_i(x, y_j) | i ∈ Relations, j ∈ Environment}
[AX-I]   Identity(x) is constituted by RP(x), not by a substance S independent of RP(x).
```
This keeps the notation precise and the axiom falsifiable.

---

### ISSUE-02

```
id       : ISSUE-02
severity : CRITICAL
target   : Axiom II × Axiom III
type     : ontology — internal tension
blocks   : ISSUE-03 (the V ⊥ H non-reducibility argument rests on the
           ontological status of V established by this bridge; resolving
           ISSUE-03 before ISSUE-02 creates a self-undermining argument)
files    : axiom_spec.md → axioms.html (axiom II + III cards) → what.html
```

**Problem**

Axiom II qualifies the invariant pattern as existing at "conventional truth
level" (saṃvṛti-satya / Nhị đế — quy ước). This implies the pattern has no
ultimate ontological grounding (no svabhāva) — confirmed by SOT-M Row 110-111:
saṃvṛtisat is "designation-dependent, conceptual, phenomenal, and pragmatically
usable"; and "that which loses its cognition when broken into parts."

Axiom III claims that vertical temporality is an "ontological dimension"
(chiều kích bản thể học) of the system — i.e., it has genuine ontological
weight, not merely conventional status.

These two claims are in tension: if patterns are only conventional (II), on
what basis does the vertical axis claim ontological status (III)? The system
borrows Madhyamaka epistemology in II but makes a realist move in III without
bridging the gap.

**Proposed fix (with SOT citations)**

Add a bridging note — "Ontological Bridge" — between II and III.
The bridge uses two moves:
1. Saṃvṛtisat (SOT-M Row 110-111): Pattern is conventionally real — it has
   causal efficacy within the system's operational domain even without being
   paramārtha-sat. This is not a weakness; it is the correct scope for II.
2. Transcendental condition (SOT-K): V ⊥ H is not claimed to be a metaphysical
   substance (which would contradict II's saṃvṛtisat scope), but a necessary
   structural precondition — in Kant's sense, the only possible explanation for
   how pattern persistence operates across time. Necessity is structural, not
   ultimate-ontological.

```
[BRIDGE-II-III]
The pattern (II) is conventionally real (saṃvṛti-satya) in the sense defined
by SOT-M Row 110-111: it has causal efficacy within the system's operational
domain, and loses its identity when the collective is dissolved — it is not
paramārtha-sat.

The vertical axis (III) is an ontological dimension not in the sense of
svabhāva (which would violate II's niḥsvabhāvatā scope, SOT-M Row 60), but
in the sense of a transcendental condition (SOT-K): a necessary structural
precondition for pattern persistence — the only available explanation for why
multi-generational identity systems require V at all. This is Kantian
transcendental necessity (structural, not empirical, not metaphysical-substance),
not Madhyamaka paramārtha-sat.

This avoids asserting ultimate ontological status while preserving
the non-reducibility claim (V ⊥ H) and keeping II's conventional scope intact.

SOT references:
  - Kantian transcendental condition: SOT-K (Kant_Transcendental_Arguments.html)
  - Saṃvṛtisat definition: SOT-M Row 110-111
  - Niḥsvabhāvatā scope boundary: SOT-M Row 59-60
```

---

### ISSUE-03

```
id       : ISSUE-03
severity : MAJOR
target   : Axiom III
type     : logic — burden of proof
prerequisite: ISSUE-02 must be resolved first (see ISSUE-02 `blocks` field)
files    : axiom_spec.md → axioms.html (axiom III card)
```

**Problem**

The central claim of Axiom III is that V (vertical axis) is *not reducible*
to H (horizontal axis): `V ⊄ H`. The falsification condition (F2) acknowledges
this: "SAI nếu V ⊆ H."

However, the document provides no positive argument *why* V is non-reducible.
A cognitive scientist or physicalist can argue: all "connection to origin" is
encoded memory, narrative, embodied practice — all of which are H-axis phenomena.
The burden of proof sits with the author and is currently unmet.

Note: Once BRIDGE-II-III (ISSUE-02) is in place, ARG-III-1 below has a
cleaner foundation — it argues from the Kantian transcendental necessity of V,
not from an unsupported ontological claim.

**Proposed fix**

Add a sub-section "Defense of V ⊥ H" with at least one structural argument:

```
[ARG-III-1]  Synchronic vs Diachronic
Memory on H is diachronic — it encodes past states as present representations.
Vertical temporality is synchronic — the system acts *as if* ancestral
constraints are operative NOW, not merely recalled. This is evidenced by:
  - ritual re-enactment that creates present obligation (not just remembrance)
  - inheritance of debt / gratitude structures that bind current agents
  - legal/cultural concepts like "obligation to ancestors" that are
    action-guiding now

These are not reducible to stored H-representations because they generate
novel present obligations not derivable from the H-record alone.

Kantian framing (SOT-K): V is a transcendental condition in the sense that
its absence cannot be compensated by any arrangement of H-axis phenomena —
just as for Kant, no arrangement of empirical data can substitute for the
a priori conditions of experience. The parallel: no amount of H-axis memory
or narrative explains why a collective *must* act as if ancestral obligations
bind them now. That "must" is the V-axis doing structural work H cannot do.
```

Even if debatable, this elevates the claim from assertion to argued position.

---

### ISSUE-04

```
id       : ISSUE-04
severity : MAJOR
target   : Axiom IV · Proposition VI
type     : agency — unspecified mechanism
blocks   : none
files    : axiom_spec.md → axioms.html (axiom IV card, mệnh đề VI card)
```

**Problem**

Axiom IV states that incoming content is "restructured according to internal
pattern logic (Axiom II)." Proposition VI describes perturbation being
"absorbed with direction." But neither specifies:

1. What agent or sub-process performs restructuring?
2. What is the decision procedure for accept / reject / transform at the boundary?
3. How does the system "know" its own pattern well enough to apply it to novel inputs?

Without this, IV and VI describe *what happens* but not *how* — they are
descriptive, not mechanistic.

**Proposed fix**

Add a mechanism clause to Axiom IV:

```
[AX-IV — mechanism addendum]
The restructuring process operates via three sub-mechanisms:
  (a) Pattern recognition — boundary agents (persons, institutions, practices)
      match incoming content against existing pattern templates (from II).
  (b) Selective integration — content is admitted if it can be rendered
      compatible with pattern; otherwise it is rejected or quarantined.
  (c) Pattern update — if accumulated admitted content shifts the pattern,
      Axiom VIII (reflexive cognition) triggers re-evaluation of invariant.

Note: Sub-mechanism (c) creates the link IV → VIII and prevents IV
from being a pure conservation mechanism.
```

---

### ISSUE-05

```
id       : ISSUE-05
severity : MAJOR
target   : Axiom I × Axiom VIII
type     : logic — revision boundary condition
blocks   : none
files    : axiom_spec.md → axioms.html (axiom VIII card)
```

**Problem**

Axiom I says identity IS the relational pattern. Axiom VIII says the system
can revise its invariant through self-observation. If self-revision can change
the pattern entirely, what remains of "identity"? The system needs a boundary
condition on how much revision is compatible with continuity.

Without this, VIII can trivially falsify the persistence claim: a system that
revises itself completely is simply a new system — the original did not survive,
it was replaced.

**Proposed fix (with SOT analogy)**

Add a continuity constraint to Axiom VIII.

Kantian analogy (SOT-K): The "necessary unity of apperception" in Kant describes
a structural identity-condition that persists through changes in the content of
experience. The meta-pattern (MP below) plays the analogous role for collective
identity — it is the structural condition under which first-order revision is
identity-preserving. Reference: SOT-K §1.1 (Apperception and its Unity).

```
[AX-VIII — continuity constraint]
Self-revision (VIII) is bounded by a continuity condition:
  Revision R applied to pattern P at time t is identity-preserving iff
  there exists a higher-order meta-pattern MP such that:
    MP(P_t) ≈ MP(P_{t+1})  [meta-pattern is stable across the revision]

This means the system can revise first-order patterns (surface invariants)
while preserving second-order patterns (the logic of how it revises).
Full replacement of both first- and second-order patterns = identity discontinuity.

Kantian analogy (SOT-K): MP is analogous to the transcendental unity of
apperception — not a content-level identity, but the structural condition
that makes identity-across-revision possible.
```

This creates a two-level pattern hierarchy: P (first-order) and MP (meta-pattern),
which also connects to second-order cybernetics (Axiom VIII's neo: B).

---

### ISSUE-06

```
id       : ISSUE-06
severity : MINOR
target   : Proposition VII
type     : notation — metaphor vs formalism
blocks   : none
files    : axiom_spec.md → axioms.html (mệnh đề VII card)
```

**Problem**

"Gradient trường F do toàn mạng tạo ra" (gradient of field F generated by
the whole network) uses physical field metaphor. It is unclear whether this is:
- A formal mathematical claim (in which case F must be defined)
- An illustrative analogy (in which case it should be labeled as such)

Mixing formal notation with metaphor reduces LLM parsability and invites misreading.

**Proposed fix**

Clarify register explicitly:

```
[PROP-VII — notation clarification]
"Gradient field F" is used as structural analogy, not formal claim.
Formal rendering: the system exhibits attractor dynamics A(S) such that
local decisions by agents tend toward states compatible with the global
pattern (II) without central coordination.
If formal treatment is desired, refer to: Kauffman (NK landscapes),
Weick (sensemaking attractors), or Odum (energy field ecology).
```

---

### ISSUE-07

```
id       : ISSUE-07
severity : MINOR
target   : Scope (global)
type     : scope — universality vs domain specificity
blocks   : none
files    : axiom_spec.md → axioms.html (each axiom card header)
```

**Problem**

The founding question is explicitly scoped to: *collective identity systems
under assimilation pressure, across generations, evolving.* However, Axioms I–IV
are stated in universal form without scope qualifiers. This creates risk of
over-application (a startup's "culture") and under-application (micro-collectives).

**Proposed fix (revised in v2 — lighter touch)**

v1 proposed adding full scope text to each axiom. v2 revises this: the global
scope already exists in the "Câu hỏi gốc" section. Adding full scope text to
each axiom card creates bloat and redundancy. The lighter and correct fix is:

Add a one-line scope reference pointer in each axiom card:

```
[SCOPE POINTER — add to each axiom I–IV card]
"Scope: multi-generational collective identity systems under evolving
assimilation pressure. See: Câu hỏi gốc [link to scope section]."
```

Additionally, add a global scope block at top of axiom_spec.md:

```
[GLOBAL SCOPE — add once at top of axiom_spec.md]
These axioms are calibrated for collective identity systems (S) satisfying:
  - |S| > single generation (temporal scale: decades to centuries)
  - Assimilation pressure: open-ended, evolving (not fixed/one-time)
  - Identity claim: system persists as recognizably same entity
Applicability to micro-collectives (families, firms) is possible but
requires explicit scope adaptation — treat as analogical extension.
```

---

### ISSUE-08

```
id       : ISSUE-08
severity : SUGGESTION
target   : Triangulation method (global)
type     : methodology
blocks   : none
files    : axiom_spec.md (new section)
scope    : FORWARD-ONLY by default — applies to new axioms and formal paper
           submissions; does not trigger automatic retroactive re-scoring of
           I–VIII unless author explicitly decides to re-derive
```

**Problem / Observation**

The triangulation method is the strongest methodological feature of the system.
However, the scoring "neo: A · B · C — 3/3" is informal and author-assessed.
There is no intersubjective procedure for how neo-convergence is determined.

**Scope note (new in v2):** A retroactive formal re-scoring of all axioms could
change neo-scores and potentially destabilize the current system (e.g., downgrade
"C-có-điều-kiện" of Axiom II). This protocol is therefore forward-only by default:
apply when adding new axioms, when preparing formal publication, or when the
author explicitly decides to re-derive the full system from scratch.

**Proposed enhancement**

Add a triangulation protocol:

```
[TRIANGULATION PROTOCOL — forward-only by default]
For each axiom, neo-score is determined by:
  1. Identify the structural claim in the axiom (not its content).
  2. For each reference system (A, B, C), find the closest structural analogue.
  3. Score as:
       STRONG (1.0)  — structural isomorphism, independent derivation possible
       PARTIAL (0.5) — structural similarity with key differences noted
       WEAK   (0.25) — thematic resonance only, structural difference significant
       NONE   (0.0)  — no convergence
  4. Total neo-score = sum; max = 3.0; threshold for inclusion = 1.5
  5. Disagreements must be documented in axiom_conflict.md

Retroactive application: requires explicit author decision + full re-derivation.
This protocol does not alter existing neo-scores unless re-derivation is initiated.
```

---

## 2.5 IMPLEMENTATION WORKFLOW (new in v2)

**Source-of-truth hierarchy:**
1. `axiom_spec.md` — single source of truth; edit here first, always
2. `axioms.html` — primary rendered output; propagate changes from axiom_spec.md
3. `what.html` — secondary render (contains canonical axiom card copies);
   propagate if axiom statement, sơ đồ, phản chứng, or prior-art changes

**Per-issue file sequence:**

| Issue | Edit in axiom_spec.md | Propagate to axioms.html | Propagate to what.html |
|-------|----------------------|--------------------------|------------------------|
| ISSUE-01 | Axiom I sơ đồ field | Axiom I `<code>` tag | Axiom I `<code>` tag |
| ISSUE-02 | Add BRIDGE-II-III section between II and III | Add bridge note between II and III cards | Same |
| ISSUE-03 | Add ARG-III-1 to Axiom III body | Axiom III card phản chứng / body | Same |
| ISSUE-04 | Add mechanism addendum to Axiom IV | Axiom IV card | Axiom IV card |
| ISSUE-05 | Add continuity constraint to Axiom VIII | Axiom VIII card | Axiom VIII card |
| ISSUE-06 | Annotate VII "gradient trường F" | Mệnh đề VII card | Mệnh đề VII card |
| ISSUE-07 | Add GLOBAL SCOPE block at top | Add scope pointer to each axiom I–IV card | Same |
| ISSUE-08 | Add TRIANGULATION PROTOCOL section | No render change needed | No render change needed |

**Commit sequence (recommended):**
```
P1: fix ISSUE-01 → fix ISSUE-02
P2: fix ISSUE-03 (after ISSUE-02 committed) → fix ISSUE-04
P3: fix ISSUE-05
P4: fix ISSUE-06 → fix ISSUE-07
P5: fix ISSUE-08 (optional, forward-only)
```

---

## 3. REVISION PRIORITY MATRIX

```
Priority   Issues              Action                                     Blocks      Files
---------  ------------------  -----------------------------------------  ----------  --------------------------------
P1 (now)   ISSUE-01            Fix notation contradiction                  —           axiom_spec.md; axioms.html; what.html
P1 (now)   ISSUE-02            Bridge II–III (Kant SOT-K + Madhyamaka SOT-M) ISSUE-03 axiom_spec.md; axioms.html; what.html
P2 (soon)  ISSUE-03            Argue V ⊥ H (after ISSUE-02 committed)     —           axiom_spec.md; axioms.html
P2 (soon)  ISSUE-04            Add IV mechanism clause                     —           axiom_spec.md; axioms.html; what.html
P3 (next)  ISSUE-05            Add VIII continuity constraint (Kant SOT-K) —           axiom_spec.md; axioms.html; what.html
P4 (later) ISSUE-06            Clarify VII notation                        —           axiom_spec.md; axioms.html; what.html
P4 (later) ISSUE-07            Add scope pointer (lighter fix)             —           axiom_spec.md; axioms.html; what.html
P5 (opt)   ISSUE-08            Formalize triangulation protocol (fwd-only) —           axiom_spec.md only
```

---

## 4. WHAT TO KEEP (do not change)

```
KEEP-01  Three-layer architecture (core / derived / meta) — correctly separates
         axioms from propositions from meta-level claims.

KEEP-02  Explicit falsifiability conditions per axiom — rare and valuable;
         do not soften or remove even if they are hard to test empirically.

KEEP-03  "Sufficient = hypothesis" disclaimer — epistemic honesty; retain.

KEEP-04  Axiom VIII as separate meta-layer — structurally sound; merging it
         into core would create self-reference loops in the object layer.

KEEP-05  Triangulation as anti-arbitrariness device — the principle is correct;
         only the protocol needs formalization (ISSUE-08, forward-only).

KEEP-06  The cấp-3 explanations — pedagogically effective; keep as non-normative
         appendices, not part of the formal spec.
```

---

## 5. SUGGESTED ADDITION — DEPENDENCY GRAPH (machine-readable)

For LLM / tooling consumption, add the following block to axiom_spec.md.
Note: neo-scores below reflect current informal scoring; formal protocol
(ISSUE-08) applies only when explicitly initiated.

```yaml
# axiom_dependencies.yaml
axioms:
  I:   {type: core, depends_on: [],            neo: [A, B, C],        score: 3.0}
  II:  {type: core, depends_on: [I],           neo: [A, B, "C-cond"], score: 2.5}
  III: {type: core, depends_on: [I, II],       neo: ["A-weak", B, C], score: 2.5}
  IV:  {type: core, depends_on: [I, II],       neo: [A, "B-strong", "C-weak"], score: 2.5}
  V:   {type: derived, depends_on: [I, II],    neo: [A, B, C]}
  VI:  {type: derived, depends_on: [II, III, IV], neo: [B, C]}
  VII: {type: derived, depends_on: [I, II, III, IV], neo: [B, C]}
  VIII:{type: meta,    depends_on: [I, II, III, IV], neo: ["A-weak", "B-2nd-order", C]}

issues_blocking_axioms:
  I:   [ISSUE-01]
  II:  [ISSUE-02]
  III: [ISSUE-02, ISSUE-03]   # ISSUE-02 must precede ISSUE-03
  IV:  [ISSUE-04]
  VIII:[ISSUE-05]

sot_references:
  ISSUE-02: [SOT-K, SOT-M]
  ISSUE-03: [SOT-K]
  ISSUE-05: [SOT-K]
```

---

## 6. OPEN QUESTIONS — Classified by research type (updated in v2)

Open questions are now classified by research type to make them actionable.
Type A = conceptual (author can resolve with framework analysis alone).
Type B = hybrid (partial conceptual, partial empirical).
Type C = empirical (requires data, methodology, collaboration).

```
OQ-1  [Type A — Conceptual]
      What is the minimum viable pattern size?
      How much of Pattern(R(S)) must be preserved for Identity(S) to hold?
      Axiom II is silent on quantitative threshold.
      → Can be addressed by formal analysis within II's definition + Axiom VIII
        continuity constraint (ISSUE-05 fix).

OQ-2  [Type A — Conceptual]
      Can two distinct collective identities share the same Pattern(R(S))?
      If yes, identity is not unique — what individuates?
      → Directly addressable from Axiom I (relational profile includes context,
        not just pattern type).

OQ-3  [Type B — Hybrid]
      What happens at identity failure?
      The system explains persistence; does it also generate a theory of collapse?
      Proposition VI (perturbation transform) implies a threshold — but what
      determines when perturbation overwhelms rather than strengthens?
      → Conceptual: threshold can be formalized from IV's selective permeability.
      → Empirical: threshold calibration requires historical case study data.

OQ-4  [Type B — Hybrid]
      Cross-system interaction:
      Two identity systems with different patterns meeting — which pattern
      governs the boundary? Is there a meta-pattern for inter-system contact?
      → Conceptual: Axiom IV + VIII provide partial answer (boundary is managed
        by both systems' pattern logic; VIII governs reflexive adjustment).
      → Empirical: contact zone dynamics require ethnographic or historical data.

OQ-5  [Type C — Empirical]
      Measurement protocol:
      For empirical testing of the falsifiability conditions, what data
      sources and methods would be needed?
      (ethnography, historical analysis, computational social science, or
      combination?)
      → Requires methodological collaboration; outside scope of solo conceptual work.
      → Candidate framework: computational social science + longitudinal ethnography.
```

---

## 7. CROSS-REFERENCE: EXTERNAL TRADITIONS TO ENGAGE

```
Tradition / Author            Relevance                           Tension with Mach Re
--------------------------    ----------------------------------  -----------------------
Luhmann — autopoiesis         AX-IV boundary; self-reproduction   Luhmann: no environment
                                                                   input restructuring —
                                                                   system generates own meaning
Maturana / Varela             AX-I relational; AX-IV boundary     Structural coupling vs
                                                                   selective permeability
Mesoudi — cultural evolution  AX-II pattern persistence           Mach Re: no replication
                                                                   mechanism specified
Rawls — reflective equilibrium AX-VIII reflexive cognition        Rawls: individual; Mach Re:
                                                                   collective — who reflects?
Ernest Gellner — nationalism  Falsification candidate             Nations as invented, not
                                                                   pattern-persistent — direct
                                                                   challenge to AX-II + AX-III
Kant — Transcendental Args    AX-III (V ⊥ H as transcendental    Kant: individual cognition;
(SOT-K)                       condition); AX-VIII (unity of       Mach Re: collective — bridge
                              apperception → meta-pattern)        requires collective analogue
Madhyamaka / Diṅnāga          AX-II (saṃvṛtisat precision);      Madhyamaka: essencelessness;
(SOT-M)                       AX-III (niḥsvabhāvatā boundary)    Mach Re must ensure V ⊥ H
                                                                   claim stays below svabhāva
```

---

## 8. REVIEW COMPLETION CHECKLIST

```
[ ] ISSUE-01 resolved — notation fixed in axiom_spec.md; propagated to axioms.html, what.html
[ ] ISSUE-02 resolved — BRIDGE-II-III added (with SOT-K and SOT-M citations)
[ ] ISSUE-03 resolved — ARG-III-1 or equivalent added (after ISSUE-02 committed)
[ ] ISSUE-04 resolved — mechanism clause added to AX-IV
[ ] ISSUE-05 resolved — continuity constraint added to AX-VIII (with SOT-K analogy)
[ ] ISSUE-06 resolved — VII notation clarified
[ ] ISSUE-07 resolved — scope pointer added to each axiom I–IV card (lighter fix)
[ ] ISSUE-08 addressed — triangulation protocol drafted (forward-only scope declared)
[ ] YAML dependency graph added to axiom_spec.md (with sot_references field)
[ ] Open questions OQ-1 and OQ-2 addressed (Type A — author can resolve)
[ ] Open questions OQ-3 and OQ-4 partially addressed (Type B — conceptual part)
[ ] Open question OQ-5 assigned to research agenda (Type C — empirical)
[ ] Cross-reference table reviewed; Luhmann + Gellner + Kant (SOT-K) + Madhyamaka (SOT-M) engaged
[ ] axiom_conflict.md updated to reflect ISSUE-02 (II × III tension)
[ ] Version tag bumped in axiom_spec.md after each P1/P2 fix
[ ] SOT-K and SOT-M cited in axiom_spec.md wherever BRIDGE-II-III is referenced
```

---

*Review plan v2 — updated 2026-06-08.*
*Changes from v1: RCA meta-analysis applied to plan itself; 5 modifications (MOD-A–E) all scored ≥ 4/5 and incorporated. Two SOTs added: Kant_Transcendental_Arguments.html (SOT-K) and The_Buddhist_Pramana_Epistemology_Logic_and_Language_RCA_Table.md (SOT-M). ISSUE-02 proposed fix now grounded in SOT-K (transcendental condition) and SOT-M (saṃvṛtisat / niḥsvabhāvatā). ISSUE-03 ARG-III-1 now uses Kantian framing from SOT-K. ISSUE-05 continuity constraint cites SOT-K §1.1. ISSUE-07 fix revised to lighter touch (reference pointer). ISSUE-08 scoped as forward-only. Implementation workflow (Section 2.5) added. OQs classified by research type (A/B/C). Kant + Madhyamaka added to cross-reference table.*
*This document is a patch-proposal, not a replacement. Retain axiom_spec.md as source of truth.*

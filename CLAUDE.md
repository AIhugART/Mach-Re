# CLAUDE.md

## RULE ZERO — Root Cause Analysis (RCA)

**This is the highest mandatory rule, applied to every activity: research planning, literature review, conceptual mapping, documentation, critique, revision, and publication preparation.**

Never treat a symptom, ambiguity, or attractive analogy as the conclusion. Always trace the observed issue, claim, or mismatch back to its root cause before acting.

### Five-step process

1. **Define** — Describe the observed issue precisely. Separate the *symptom* (what appears in the text, argument, mapping, citation, or structure) from the *cause* (the assumption, source gap, conceptual mismatch, or methodological error that produced it).
2. **Trace** — Follow the causal chain backward by asking: "What made this issue appear?" Repeat at least three times using the "5 Whys" method.
3. **Isolate** — Identify the starting point of the failure: an unsupported claim, weak citation, ambiguous term, broken mapping, category error, outdated source, missing definition, or structural inconsistency. If it is not isolated, do not revise yet.
4. **Fix the cause, not the symptom** — Correct the root cause directly. Do not patch prose, soften wording, add a vague caveat, or create a workaround unless it is explicitly marked as `TODO(HOTFIX)`.
5. **Verify** — Show that the root cause has been removed, not merely that the visible symptom disappeared. When possible, verify against the source text, the active mapping files, the published node/edge definitions, and the research objective.

### Decision procedure — 3-round RCA × 5-Why × scoring gate (≥ 4/5)

This operationalizes steps 2–4 above. It is the procedure already proven in
`CHANGELOG.md` (each edited claim carries its score) and tabulated in
`plan/dictionary_rule.md`.

**3-round RCA (three depths of digging).** Step 2 "Trace" must reach the third
round; stopping earlier treats a symptom.
- Round 1 — Symptom: name the surface defect (absolute wording, self-scored
  number, pseudo-formula).
- Round 2 — Mechanism: why the surface defect backfires *here specifically* — a
  framework that invites strict scrutiny is hurt more by a sloppy surface.
- Round 3 — Root: which internal standard it violates (the framework's own
  falsifiability / traceability rule). The fix makes the framework obey itself.

**5-Why.** Inside each round, ask "what made this appear?" until the chain
bottoms out in one sentence (the root). If the root needs more than one
sentence, the trace is incomplete — return to Round 1.

**Scoring gate (≥ 4/5).** Before changing ANY claim, score that claim on five
criteria, 1 point each. The scored unit is *the candidate claim*; a high score
means a strong case to edit.

| Criterion | Question | High score means |
|---|---|---|
| Correct | Is this genuinely an overclaim / unfalsifiable statement? | real defect |
| Deep | Does the fix touch the root (internal consistency), not just tone? | reaches root |
| Feasible | Can it be fixed without breaking core structure/meaning? | safe to do |
| Conflict-risk | Will the fix avoid creating contradictions on other pages? | low new risk |
| Preservation | Is the core strength kept after the fix? | strength kept |

**Threshold: average ≥ 4/5 → fix; below 4/5 → keep as-is.** Anchors from
`CHANGELOG.md`: `upgrade.html:213` "describes *precisely*" scored 4.8 (the same
page lists four limits of that very description → self-contradiction) → fixed;
`mach_re_homologous.html:217` "language precise enough for dialogue" scored 3.2
(a design goal, not a universal claim) → kept.

> Second use of the same rubric: `plan/mach-re-plan-chinh-sua-v2.md` §2 scores
> *plan items* (not claims), where ≥ 4/5 means "the proposed action is sound,
> keep it". Same five criteria, different scored object and orientation — always
> state which one you are scoring.

**After any fixing pass, record it in `CHANGELOG.md`** (what was lowered/changed
and why), per `plan/dictionary_rule.md` (P5/G6). The canonical lookup table for
absolute→scoped substitutions lives in `plan/dictionary_rule.md`; consult it
before editing prose and do not duplicate it here.

### Activity-specific application

| Activity | RCA requirement |
|----------|-----------------|
| **Research planning** | Ask "Why is this research question necessary?" before "How should it be written?" Identify the real problem behind the requested document or section. |
| **Literature review** | Trace every major claim to a source, and distinguish established scholarship from interpretation, analogy, or hypothesis. |
| **Conceptual mapping** | Understand why each concept exists in its original system before mapping it across systems. Treat cross-domain links as analogies unless equivalence is explicitly justified. |
| **Documentation** | Find what caused confusion before rewriting. Fix the structure, terminology, missing definition, or broken reference, not only the sentence that looks unclear. |
| **Review** | Classify every finding as either symptom or root cause. A blocking issue must identify the root cause; a surface-level wording issue is only a documentation bug. |
| **Revision** | Identify what is truly causing complexity or inconsistency before simplifying, reorganizing, or abstracting. Do not create structure around a symptom. |

### Example

```text
Symptom: A section claims Buddhist Epistemology "solves" Quantum Measurement.
  → Why? The wording treats a philosophical mapping as a physical explanation.
    → Why? The document does not separate analogy, interpretation, and prediction.
      → Why? The claim lacks a formal boundary between ontology and physics.
        → Root cause: Category error between epistemological interpretation and empirical physical theory.
          → Fix: Reframe the section as an interpretive mapping unless formal proof, peer review, physical predictions, and experimental tests are supplied.
```

### Warnings

- If the revision only changes the sentence where the symptom appears, it is **not enough**; return to step 2.
- If the root cause cannot be explained in one sentence, understanding is **not complete**; return to step 1.
- If the fix only adds a vague caveat, fallback phrase, or defensive wording, it is **treating the symptom**; return to step 4.

## Core Principles

### Document contract rules

- Use bilingual English/Vietnamese where appropriate across project documents; keep technical terminology, formal claims, and publication-facing text in technically precise English; communicate with the user in Vietnamese, keep English technical terms inside quotation marks, and explain concepts at a high-school level.
- Apply the mandatory principle "extend, not overwrite": when revising project documents, preserve existing valid structure, claims, terminology, citations, mappings, and author intent unless the user explicitly requests replacement; add, refine, or qualify content by extending the existing document contract rather than overwriting it.

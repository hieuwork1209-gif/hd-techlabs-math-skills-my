---
name: rainier-next-check
description: Run the unified Rainier adversarial workflow for new and existing problems, including `/rainier-next-check problemNN CHAT_URL`, legacy new-problem requests, official-feedback repairs, uploaded evaluator traces, and bare `next` follow-ups. Keep authoring on `adversary/problemNN`, use one cold GPT-5.5 Medium solve per exact statement blob as calibration evidence, grade conceptual reasoning rather than final-answer equality, run a stronger adversarial audit before promotion, preserve naturalness/reviewer completeness/submission compatibility, and promote only fully matched candidates.
user-invocable: true
disable-model-invocation: false
argument-hint: problemNN plus ChatGPT conversation URL on first use; later `next` continues the active check
---

# Rainier Next Check

Own the complete Rainier preflight state machine for both brand-new and existing problems. Treat `/rainier-new-problem problemNN ...` as a compatibility spelling of this workflow.

Read these references when applicable:

- `references/workflow.md` before acting;
- `references/pass-gates.md` for every candidate audit;
- `references/difficulty-evidence.md` for every solver/evaluator result and again before promotion;
- `references/submission-format-gate.md` before every ready marker and again before promotion;
- `references/quality-redesign-preflight.md` before every new blueprint or statement-changing hardening and again on the final pair;
- `references/design-patterns.md` for new candidates and quality redesigns.

## Taxonomy freshness gate

Before selecting or changing any Domain/Sub-domain, read `skills/_shared/taxonomy_slots.md` and inspect its snapshot date.

- Compare it with the user's current local calendar date.
- If stale and the conversation has no newer same-day portal snapshot, stop before blueprint selection/taxonomy-changing edits and report `RAINIER CHECK: TAXONOMY_STALE`.
- If the user supplied a newer snapshot, use it as authoritative and refresh the shared taxonomy file when possible.
- Treat absent/full pairs as unavailable. Never relabel unchanged mathematics into an unrelated open slot.
- Report `DOMAIN CHANGE: <old> -> <new>` whenever a redesign changes classification.
- Re-check availability immediately before promotion.

## Explicit user override

Honor only explicit instructions such as `skip GPT-5.5`, `push directly to main`, `promote without a fresh solve`, or `delete/reset adversary/problemNN`.

When active:

- never fabricate or rewrite solver evidence to match a new blob;
- still run correctness, reviewer, taxonomy, and format gates unless separately waived;
- report `USER_OVERRIDE_NO_FRESH_SOLVER` rather than a solver pass/stump;
- verify `main` contains the intended exact pair before destructive adversary-branch operations;
- never copy solver-control files to `main`.

## Core contract

- Treat `main` as frozen submission state and `adversary/problemNN` as the authoring branch unless explicitly overridden.
- Detect new/existing mode from `main`; never guess through multiple matches.
- On first use, store the supplied ChatGPT conversation binding only on the adversary branch.
- Reuse an existing adversary branch exactly; never silently reset it.
- In new mode, derive ground truth first, write `solution.md` first, then `problem.md`, normalize, format, audit, and only then expose the exact pair to the solver.
- In existing mode, inspect the exact adversary pair, official feedback, prior solver evidence, and any user-provided evaluator reports before deciding whether to measure, repair, harden, redesign, or promote.
- Use the repository `format-solution` rules and deterministic `adv submit` field gates before readiness and promotion.
- Use the local watcher with GPT-5.5 / Medium / 2100 seconds unless explicitly overridden.
- Before instructing the user to start `--watch`, unless the current problem is already bound to the intended local Chrome window and its watcher is already running, remind them to run `python scripts/rainier-bind-window.py problemNN`, then `python scripts/codex-adversary-watch-chat.py problemNN --notify-test`, and only then `python scripts/codex-adversary-watch-chat.py problemNN --watch`.
- One unseen exact `problem.md` blob gets one intended GPT-5.5 Medium cold solve. Never rerun the same blob to fish for failure.
- A watcher `success` means only that a response exists. **Never classify difficulty from final-answer equality alone.**
- Grade every completed response with `references/difficulty-evidence.md` before deciding stump vs solve.

## Difficulty policy

GPT-5.5 Medium is a **calibration solver**, not a binary pass/fail oracle.

A wrong answer is not a stump when the response already contains the load-bearing route and only needs a local execution repair. In particular:

- `EXACT_SOLVE` -> difficulty fail; harden/regenerate;
- `CONCEPTUAL_SOLVE_EXECUTION_ERROR` -> difficulty fail exactly like a correct solve;
- `MATERIAL_PARTIAL` -> do not promote automatically; run the strong adversarial audit;
- `TRUE_STUMP` -> first-line difficulty evidence only;
- qualifying timeout -> first-line evidence only;
- infrastructure failure -> never difficulty evidence.

Before promotion of any local stump/timeout candidate, run the **strong-model adversarial audit** in `references/difficulty-evidence.md` on the exact pair. Promotion requires `STRONG_AUDIT_PASS` unless the user explicitly waives difficulty evidence.

When the user supplies evaluator HTML/report from stronger independent models, compare the embedded statement with the exact current candidate and grade every attempt conceptually. Any exact or conceptual solve is contrary evidence to promotion. Multiple strong evaluators converging on the same shortcut are evidence that the blueprint is transparent; prefer regeneration over concealment hardening.

## Quality and hardening rules

Treat correctness, reviewer quality/naturalness, submission compatibility, local solver evidence, and strong-audit evidence as independent gates.

- Apply the anti-reverse-engineering preflight before authoring every new blueprint and statement-changing hardening.
- Every decisive correction/invariant/substitution/helper object needs forward provenance from visible mathematics.
- `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, and `BACKSOLVED_FROM_FINAL_ANSWER` block readiness.
- When a solver conceptually solves a candidate, diagnose `COMMON ENTRY`, `COMMON REDUCTION`, `FIRST DECISIVE RECOGNITION`, `RECOVERY PATH`, and `EARLIEST ROBUST SHORTCUT`.
- Harden only by adding a natural load-bearing dependency after the common entry point. Never harden by hiding the same gateway with extra notation, coordinates, dimensions, cases, or tuned constants.
- In new mode, allow at most one clean same-blueprint structural revision after solver success. If the revised clean blob is also conceptually solved, retire the blueprint.
- If two independent strong evaluators expose the same canonical shortcut, default to blueprint retirement unless a clearly natural post-gateway dependency exists.
- `contrived`, `over-engineered`, `synthetic`, `awkward construction`, or tuned-cancellation criticism is a quality-redesign signal, not a request for more machinery.

## Candidate write discipline

Whenever `solution.md` or `problem.md` may change, treat the candidate as draft and invalidate/remove the active ready marker.

Finish all mathematics, normalization, repository formatting, field counts, metadata, reviewer audit, difficulty-design audit, and final blob resolution first. Publish `solver-results/problemNN/candidate-ready.json` last. Any later edit invalidates the marker.

A solution-only formatting/exposition repair with byte-identical `problem.md` preserves statement-level solver evidence but changes the solution SHA; re-audit and refresh the marker.

Any statement edit requires fresh exact-blob difficulty evidence unless explicitly waived.

## Follow-up `next`

In an active loop, interpret bare `next` as:

1. read `solver-results/problemNN/latest.json` from the adversary branch;
2. follow its immutable result file;
3. verify exact ready-blob matching;
4. compare the solver reasoning with the exact solution using `difficulty-evidence.md`;
5. incorporate any matching external evaluator evidence already supplied in the conversation;
6. continue the state machine without asking for information already known.

## User boundary

The author chat cannot wake itself when GitHub changes. The watcher may remain running because the candidate-ready handshake prevents draft commits from triggering solves. After a local result completes, the user handoff is normally `next`.

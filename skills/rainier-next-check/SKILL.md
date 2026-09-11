---
name: rainier-next-check
description: Run the unified Rainier adversarial workflow for both brand-new and existing problems. Use for `/rainier-next-check problemNN CHAT_URL`, new-problem requests that would previously use `/rainier-new-problem`, requests to create or resume `adversary/problemNN`, official-feedback repairs, and bare `next` follow-ups in an active Rainier loop. Keep all authoring/hardening off `main`, finish and audit the exact solution/problem pair before exposing it to the watcher, then allow exactly one cold GPT-5.5 Medium solve per ready statement blob. Preserve naturalness, reviewer completeness, exact solver evidence, submission-format compatibility, and promote only a fully matched candidate.
user-invocable: true
disable-model-invocation: false
argument-hint: problemNN plus ChatGPT conversation URL on first use; later `next` continues the active check
---

# Rainier Next Check

Own the complete Rainier preflight state machine for **both new and existing problems**. Do not maintain a separate creation state machine. Treat `/rainier-new-problem problemNN ...` as a compatibility spelling of this workflow when encountered.

Read `references/workflow.md` before acting. Read `references/pass-gates.md` for every candidate audit. Read `references/submission-format-gate.md` before every `candidate-ready.json` and again before promotion. Before selecting any new blueprint or proposing any statement-changing hardening, read `references/quality-redesign-preflight.md`; run that preflight again on the final normalized pair before `candidate-ready.json`. For a brand-new candidate or a quality redesign, also read `references/design-patterns.md`.

## Core contract

- Treat `main` as frozen submission state and `adversary/problemNN` as the only authoring/design branch.
- Detect mode from `main`: exactly one `workspace/rainier-problem/problemNN-*/problem.md` means **existing mode**; none means **new mode**; multiple matches are an error to resolve rather than guessing.
- On first use, accept the user-supplied ChatGPT conversation URL and upsert `solver-results/problemNN/chat-binding.json` on the adversary branch only. Never invent a conversation ID and never copy the binding to `main`.
- Reuse an existing `adversary/problemNN` branch exactly; never silently reset it. If absent, create it from current `main`.
- In new mode, derive ground truth first, write/repair `solution.md` first, write `problem.md` second, normalize, re-read the exact pair, and pass reviewer/quality/submission gates before making the candidate solver-eligible.
- In existing mode, preserve the current `/rainier-next-check` semantics: inspect the exact adversary pair, official feedback, and prior solver evidence before deciding whether to measure, harden, redesign, repair, or promote.
- Treat repository submission formatting as a hard dependency, not an optional cleanup. Before every `candidate-ready.json`, apply the rules in `skills/format-solution/SKILL.md` to the exact Rainier `solution.md` path, using `workspace/rainier-problem/problemNN-*` as an explicit path override, and apply both `references/submission-format-gate.md` and `skills/_shared/hard_gates.md`. Mirror the current field constants in `scripts/adv` rather than trusting stale limits.
- Run the same submission-format gate again immediately before promotion. Never report `MAIN_READY_FOR_RAINIER` while `./scripts/adv submit problemNN` would still reject a deterministic field-shape issue such as Answer length, prompt length, concept count/length, missing sections, answer aliases defined only in the solution, or a mismatched boxed answer.
- The Answer gate is dual: the exact mapped Answer field must satisfy the current raw `ANSWER_MAX` in `scripts/adv` (currently 102 characters), and after stripping `$` plus whitespace it must be under 100 characters. If the answer cannot honestly fit without changing the statement or Answer Type, block before Codex/promotion and redesign; never truncate or hide content behind solution-only aliases.
- Use `python scripts/codex-adversary-watch-chat.py problemNN --watch` as the independent local solver harness. Default settings are GPT-5.5, Medium reasoning, 2100 seconds.
- Before reporting any `*_WAIT_CODEX` status, ensure the repository copy of `scripts/codex-adversary-watch-chat.py` implements the bundled candidate-ready gate; if it is older, sync the bundled wrapper first. The running watcher process must be restarted after a runner-script update because Python does not hot-reload it.
- The watcher must obey the **candidate-ready handshake** in `references/workflow.md`. A new or changed `problem.md` by itself is never permission to solve.
- One ready unseen `problem.md` blob gets exactly one GPT-5.5 Medium cold solve. Never rerun a blob to fish for failure.
- A watcher `success` means only that text was returned. Compare it mathematically against the exact candidate `solution.md` before classifying difficulty.
- Treat correctness, reviewer quality/naturalness, submission compatibility, and solver difficulty as independent gates. A local stump never excuses a bad problem, incomplete solution, or invalid portal field.
- Apply the anti-reverse-engineering preflight **before authoring** any new blueprint or statement-changing hardening. Every decisive correction, invariant, substitution, or helper object must have forward provenance from visible mathematics; `GUESSED_TO_CANCEL`, `FIT_TO_TARGET`, `COEFFICIENT_TUNED`, and `BACKSOLVED_FROM_FINAL_ANSWER` are automatic rejections before Codex.
- When GPT-5.5 solves correctly, diagnose the earliest robust shortcut. Harden only through a genuinely load-bearing mathematical dependency that deepens reasoning after the common entry point. Never harden by making a standard structure harder to recognize. In new mode, allow at most one same-blueprint structural revision before regenerating. Never stack tuned constants, cancellation devices, extra indices, giant computations, custom relation layers, or notation merely to stump the solver.
- Official feedback such as `contrived`, `over-engineered`, `synthetic`, `awkward construction`, or `customized to force cancellation` is a **QUALITY_REDESIGN** signal, not a request for more machinery.
- If the solver is wrong/materially incomplete or a valid 2100-second timeout is recorded, stop local hardening, run every promotion gate, including the repository submission-format gate, and promote the exact matching pair to `main` only if all gates are green.
- A solution-only formatting repair with byte-identical `problem.md` does not require another cold solve, but it invalidates the solution SHA in `candidate-ready.json`; re-audit and refresh the marker. Any statement edit requires fresh solver evidence for the new problem blob.
- Never promote on `SOLVER_ERROR`, stale solver evidence, a mismatched ready marker, infrastructure failure, or a deterministic `adv submit` field failure.
- PowerShell notifications must open the exact bound ChatGPT conversation. Never use a GitHub result URL as a click fallback.

## Candidate write discipline

Whenever `solution.md` or `problem.md` may change, treat the candidate as **draft**. Ensure the ready marker is absent/stale while editing. Finish all mathematical work, normalization, repository `format-solution` rules, exact portal-field counts, metadata, and reviewer audit first. Resolve the final problem and solution blob SHAs and upsert `solver-results/problemNN/candidate-ready.json` **last**. Any later change to either file invalidates that marker and requires a new final audit plus a new marker.

## Follow-up `next`

In a conversation already using this workflow, interpret a bare `next` as: read `solver-results/problemNN/latest.json` on `adversary/problemNN`, follow its `result_file`, verify the result belongs to the exact ready candidate, compare it with the matching solution, and continue the unified state machine without asking the user to restate the problem or chat URL.

## User boundary

The web chat cannot wake itself when GitHub changes. After a solver attempt completes, the only user handoff is `next`. The watcher may remain running continuously because the candidate-ready handshake prevents draft/intermediate commits from triggering Codex.

---
name: rainier-next-check
description: Run the unified Rainier adversarial workflow for both brand-new and existing problems. Use for `/rainier-next-check problemNN CHAT_URL`, new-problem requests that would previously use `/rainier-new-problem`, requests to create or resume `adversary/problemNN`, official-feedback repairs, and bare `next` follow-ups in an active Rainier loop. Keep all authoring/hardening off `main`, finish and audit the exact solution/problem pair before exposing it to the watcher, then allow exactly one cold GPT-5.5 Medium solve per ready statement blob. Preserve naturalness, reviewer completeness, exact solver evidence, and promote only a fully matched candidate.
user-invocable: true
disable-model-invocation: false
argument-hint: problemNN plus ChatGPT conversation URL on first use; later `next` continues the active check
---

# Rainier Next Check

Own the complete Rainier preflight state machine for **both new and existing problems**. Do not maintain a separate creation state machine. Treat `/rainier-new-problem problemNN ...` as a compatibility spelling of this workflow when encountered.

Read `references/workflow.md` before acting. Read `references/pass-gates.md` for every candidate audit. For a brand-new candidate or a quality redesign, also read `references/design-patterns.md`.

## Core contract

- Treat `main` as frozen submission state and `adversary/problemNN` as the only authoring/design branch.
- Detect mode from `main`: exactly one `workspace/rainier-problem/problemNN-*/problem.md` means **existing mode**; none means **new mode**; multiple matches are an error to resolve rather than guessing.
- On first use, accept the user-supplied ChatGPT conversation URL and upsert `solver-results/problemNN/chat-binding.json` on the adversary branch only. Never invent a conversation ID and never copy the binding to `main`.
- Reuse an existing `adversary/problemNN` branch exactly; never silently reset it. If absent, create it from current `main`.
- In new mode, derive ground truth first, write/repair `solution.md` first, write `problem.md` second, normalize, re-read the exact pair, and pass reviewer/quality gates before making the candidate solver-eligible.
- In existing mode, preserve the current `/rainier-next-check` semantics: inspect the exact adversary pair, official feedback, and prior solver evidence before deciding whether to measure, harden, redesign, repair, or promote.
- Use `python scripts/codex-adversary-watch-chat.py problemNN --watch` as the independent local solver harness. Default settings are GPT-5.5, Medium reasoning, 2100 seconds.
- Before reporting any `*_WAIT_CODEX` status, ensure the repository copy of `scripts/codex-adversary-watch-chat.py` implements the bundled candidate-ready gate; if it is older, sync the bundled wrapper first. The running watcher process must be restarted after a runner-script update because Python does not hot-reload it.
- The watcher must obey the **candidate-ready handshake** in `references/workflow.md`. A new or changed `problem.md` by itself is never permission to solve.
- One ready unseen `problem.md` blob gets exactly one GPT-5.5 Medium cold solve. Never rerun a blob to fish for failure.
- A watcher `success` means only that text was returned. Compare it mathematically against the exact candidate `solution.md` before classifying difficulty.
- Treat correctness, reviewer quality/naturalness, and solver difficulty as independent gates. A local stump never excuses a bad problem or incomplete solution.
- When GPT-5.5 solves correctly, diagnose the earliest robust shortcut. Harden only through a genuinely load-bearing mathematical dependency. In new mode, allow at most one same-blueprint structural revision before regenerating. Never stack tuned constants, cancellation devices, extra indices, giant computations, or notation merely to stump the solver.
- Official feedback such as `contrived`, `over-engineered`, `synthetic`, `awkward construction`, or `customized to force cancellation` is a **QUALITY_REDESIGN** signal, not a request for more machinery.
- If the solver is wrong/materially incomplete or a valid 2100-second timeout is recorded, stop local hardening, run every promotion gate, and promote the exact matching pair to `main` only if all gates are green.
- Never promote on `SOLVER_ERROR`, stale solver evidence, a mismatched ready marker, or infrastructure failure.
- PowerShell notifications must open the exact bound ChatGPT conversation. Never use a GitHub result URL as a click fallback.

## Candidate write discipline

Whenever `solution.md` or `problem.md` may change, treat the candidate as **draft**. Ensure the ready marker is absent/stale while editing. Finish all mathematical work, normalization, metadata, and reviewer audit first. Resolve the final problem and solution blob SHAs and upsert `solver-results/problemNN/candidate-ready.json` **last**. Any later change to either file invalidates that marker and requires a new final audit plus a new marker.

## Follow-up `next`

In a conversation already using this workflow, interpret a bare `next` as: read `solver-results/problemNN/latest.json` on `adversary/problemNN`, follow its `result_file`, verify the result belongs to the exact ready candidate, compare it with the matching solution, and continue the unified state machine without asking the user to restate the problem or chat URL.

## User boundary

The web chat cannot wake itself when GitHub changes. After a solver attempt completes, the only user handoff is `next`. The watcher may remain running continuously because the candidate-ready handshake prevents draft/intermediate commits from triggering Codex.

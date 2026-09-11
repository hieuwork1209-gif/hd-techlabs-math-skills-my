# Repository Submission-Format Gate

Run this gate twice: immediately before publishing `candidate-ready.json`, and again immediately before promotion to `main` / `MAIN_READY_FOR_RAINIER`.

## Repository formatter bridge

When the GitHub repository is available, fetch and apply the current repository rules in:

- `skills/format-solution/SKILL.md`
- `skills/_shared/hard_gates.md`
- the current field-limit constants in `scripts/adv`

The Rainier adversarial workspace is `workspace/rainier-problem/problemNN-*`. Apply `format-solution` to the exact candidate `solution.md` using that path explicitly even if the repository formatter's default examples mention another workspace.

## Exact field gates

Use the current `scripts/adv` constants as source of truth. Known values at the time of this skill update are:

- prompt: at most 2000 raw characters;
- answer: at most 102 raw characters;
- each Solution Concept: at most 100 raw characters;
- Solution Concepts: 1-5 items.

For the Answer, also apply the stricter formatter safety gate: after stripping every `$` and whitespace character, fewer than 100 characters may remain.

The Answer must be exactly one mathematical object, contain no `\boxed`, and use only notation introduced in the problem prompt except dummy indices bound locally inside the answer expression. Do not use solution-only aliases merely to shorten the field. The answer object must match the content inside the final `Final Answer: $\boxed{...}$` exactly.

The `## Steps` payload must be under 10,000 characters as written. Compression may not hide a load-bearing derivation.

## Failure handling

If a mathematically equivalent compact answer can be written using prompt-defined notation, treat that as a solution-only format repair. A solution-only formatting edit does not require a new cold solve when `problem.md` is byte-identical, but it changes the solution blob SHA and therefore requires a refreshed ready marker after re-audit.

If satisfying the Answer gate requires editing `problem.md` or changing the Answer Type, treat it as a statement change. Do not expose/promote that candidate on stale solver evidence; obtain fresh solver evidence for the new problem blob.

Never report `MAIN_READY_FOR_RAINIER` while the exact pair would still fail deterministic checks mirrored by `./scripts/adv submit problemNN`.

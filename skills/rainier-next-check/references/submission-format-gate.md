# Repository Submission-Format Gate

Run this gate twice: immediately before publishing `candidate-ready.json`, and again immediately before promotion to `main` / `MAIN_READY_FOR_RAINIER`.

## Mandatory formatter execution

Treat repository formatting as an **actual file transformation/checkpoint**, not a mental checklist.

1. Read the current repository `skills/format-solution/SKILL.md` and apply it to the exact `workspace/rainier-problem/problemNN-*/solution.md` path.
2. If local repo execution is available and the formatter flow can be completed in the current turn, run `./scripts/adv format problemNN`; otherwise perform the same rewrite directly from `skills/format-solution/SKILL.md`.
3. Re-read the resulting `solution.md`. Do not continue merely because the mathematical content was already correct.
4. A formatter pass is incomplete unless the physical file contains, in order, `## Steps`, `## Answer`, `## Classification`, and `## Solution Concepts`.
5. The final step must end with the literal shape `Final Answer: $\boxed{...}$`. The object inside `\boxed{}` must be character-for-character identical to the object in `## Answer`, while the `## Answer` field itself must not contain `\boxed`.
6. Reject stale pre-formatter layouts such as a file that ends with an unboxed `Final Answer:` after `## Solution Concepts`, or a file with no `## Answer` section. These exact failures surface in `adv submit` as `Answer is empty` and `The last step must end with 'Final Answer: $\boxed{...}$'`.
7. Apply all other formatter rules, including no `\tag{...}`, consecutive `Step N:` labels, allowed math delimiters, concept formatting, classification fields, the zero-blackbox requirement, and the solution-length gate.

A solution-only formatter edit with byte-identical `problem.md` does not require a new cold solve. It does change the solution blob SHA, so re-audit and refresh `candidate-ready.json` after formatting.

## Exact repository field gates

Read `skills/_shared/hard_gates.md` and the current constants in `scripts/adv`; current script values outrank cached values in this file. Known values at the time of this update are:

- prompt: at most 2000 raw characters;
- answer: at most 102 raw characters;
- each Solution Concept: at most 100 raw characters;
- Solution Concepts: 1-5 items.

At minimum verify:

- the mapped Math Problem field is nonempty and within the current raw prompt limit;
- the mapped Answer field is nonempty, is exactly one mathematical object, contains no `\boxed`, and uses only prompt-defined notation except locally bound dummy indices;
- the mapped Answer field is within the current raw `ANSWER_MAX`, and after stripping `$` plus whitespace it is under 100 characters;
- the boxed final answer and `## Answer` object match exactly;
- `## Steps` is under 10,000 characters as written;
- Solution Concepts number 1-5 and each is within the current concept-length limit;
- Problem Type and Answer Type agree between `problem.md` and `solution.md`;
- no stale metadata remains.

If satisfying the Answer gate requires editing `problem.md` or changing Answer Type, treat it as a statement change and require fresh solver evidence. Never truncate or hide content behind solution-only aliases.

## Promotion-side verification

After copying the pair to `main`, re-fetch the exact `main` files and run this same structural/field check on the promoted copy before writing `terminal.json` or reporting `MAIN_READY_FOR_RAINIER`.

Never report `MAIN_READY_FOR_RAINIER` while the exact promoted pair would still fail deterministic checks mirrored by `./scripts/adv submit problemNN`.

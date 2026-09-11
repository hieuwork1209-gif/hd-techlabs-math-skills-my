# Rainier Submission Hard Gates

Use this file as the repository source of truth for submission-shape validation. Before declaring a candidate ready for Rainier, map the exact portal fields and apply these gates to the exact text that would be submitted.

## Live portal caps

Mirror the constants in `scripts/adv` before relying on cached values. At the time of this file's creation, `adv submit` enforces:

- `PROMPT_MAX = 2000` raw characters for Math Problem (Prompt).
- `ANSWER_MAX = 102` raw characters for Answer.
- `CONCEPT_MAX = 100` raw characters per Solution Concept.
- `CONCEPT_LIMIT = 5`, with at least one concept required.

If `scripts/adv` changes, its current constants outrank the historical numbers above. Never report `MAIN_READY_FOR_RAINIER` from stale caps.

## Answer Length Gate

Run both checks:

1. **Portal gate:** the exact `## Answer` field, including its `$...$` delimiters and any whitespace that will be pasted, must be at most 102 raw characters.
2. **Formatter safety gate:** after stripping every `$` and every whitespace character, the answer must be under 100 characters.

The answer must also:

- contain exactly one mathematical object;
- contain no `\boxed`;
- use only notation introduced in the problem prompt, except bound dummy indices introduced locally inside the answer expression;
- match character-for-character the content inside `Final Answer: $\boxed{...}$` after removing the outer `$` and `\boxed{}` wrappers.

Do not shorten an answer by using aliases defined only in `solution.md`. Prefer an equivalent compact expression built from prompt-defined notation. If the requested object cannot honestly fit the caps without changing the problem or Answer Type, stop before solver exposure/promotion and route to a statement/Answer-Type redesign. Never truncate mathematical content.

## Prompt Length Gate

The exact mapped Math Problem (Prompt) must be nonempty and at most 2000 raw characters, using the current `PROMPT_MAX` from `scripts/adv` when it differs.

## Solution Length Gate

Count the `## Steps` payload exactly as written, including prose, LaTeX, and whitespace. It must be under 10,000 characters. Compression must remain zero-blackbox: do not hide a load-bearing derivation behind phrases such as "one checks" or "it follows" merely to fit the cap.

## Solution Concepts Gate

Require 1-5 concepts. Each exact mapped concept must satisfy the current `CONCEPT_MAX` in `scripts/adv` and the repository's plain-text concept rules.

## Structural Gate

Require all of the following before submit-ready status:

- `problem.md` contains normalized prompt, Domain/Sub-domain, Problem Type, Answer Type, and Domain Explanation.
- `solution.md` contains consecutive `Step N:` blocks, `## Answer`, `## Classification`, and `## Solution Concepts`.
- The final step ends with the exact required `Final Answer: $\boxed{...}$` line.
- Problem Type and Answer Type agree between `problem.md` and `solution.md`.
- The standalone answer is self-contained relative to the prompt.

## Workflow rule

These gates are mandatory twice in adversarial Rainier workflows:

1. after normalization/`format-solution`, before `candidate-ready.json` is published;
2. again immediately before promotion to `main` / `MAIN_READY_FOR_RAINIER`.

A solution-only formatting repair does not require a new cold solve when `problem.md` is byte-identical, but it invalidates the old solution SHA in `candidate-ready.json`; refresh the marker after re-auditing the exact pair. Any `problem.md` edit requires fresh solver evidence for the new problem blob.

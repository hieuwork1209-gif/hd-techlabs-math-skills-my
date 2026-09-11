# Quality-Redesign Preflight

Run this preflight **before authoring** every new blueprint and every statement-changing hardening proposal. Run it again on the exact normalized `solution.md` / `problem.md` pair before publishing `candidate-ready.json`.

The purpose is to prevent official feedback such as `contrived`, `over-engineered`, `synthetic`, `hidden structure introduced after the fact`, `customized to force cancellation`, or `reverse-engineered solution`.

## Governing rule

Difficulty may hide the **answer**, but it must not hide the **reason the decisive mathematics should be searched for**.

A representation, invariant, substitution, correction term, auxiliary object, or normal form may be absent from the statement. However, the solution must derive why it is natural from visible data before using it. Verification that a guessed object happens to work is not enough.

## Stage 1 — Statement-construction audit

Reject the blueprint/proposal before writing it if any of these are true:

- the statement expands a standard object into many custom generators, relations, coordinates, or coefficients mainly so the solver must reconstruct the standard object;
- several displayed coefficients or relations are present only because they make a later cancellation or factorization work;
- a natural standard formulation would remove most of the statement and also remove most of the difficulty;
- the problem is interesting mainly because the author knows a hidden encoding, not because the visible object has independent mathematical interest;
- the proposed hardening is accurately summarized as “make the same key structure harder to recognize.”

### Compression test

Mentally rewrite the problem using the decisive structure revealed by the solution. If this makes the statement dramatically shorter and the remaining mathematics becomes routine, the original difficulty was concealment. Reject it.

A hidden representation is acceptable only when discovering it is forced by an intrinsic obstruction and **at least two load-bearing reasoning nodes remain after the representation is found**.

## Stage 2 — Forward-provenance audit

For every non-obvious object introduced in the solution, record internally:

1. **Trigger** — Which visible equation, obstruction, symmetry, extremal condition, or closure requirement tells the solver to look for this object?
2. **Derivation** — How is the object obtained: solving an explicit condition, applying a canonical construction, optimizing an intrinsic quantity, taking a universal/normal form, or deriving a recursion?
3. **Canonicity** — Why this choice, rather than infinitely many tuned alternatives?
4. **Load-bearing role** — Which later reasoning step genuinely requires it?

Classify the provenance as one of:

- `CANONICAL`;
- `FORCED_BY_EQUATIONS`;
- `INTRINSIC_EXTREMAL_OR_UNIVERSAL`;
- `STANDARD_NATURAL_REPRESENTATION`;
- `GUESSED_TO_CANCEL`;
- `FIT_TO_TARGET`;
- `COEFFICIENT_TUNED`;
- `BACKSOLVED_FROM_FINAL_ANSWER`.

The last four classifications are automatic rejection signals. Do not publish a ready marker and do not spend a Codex solve on that candidate.

### Solution-writing requirement

The first appearance of each decisive non-obvious object must be preceded by its forward derivation. The pattern

> “Define $A,B,C$ by these special combinations. Direct calculation shows all unwanted terms cancel.”

is reviewer-unsafe unless the combinations were already derived from a canonical system of equations or an intrinsic construction.

Likewise, a correction such as $X-\alpha$ is acceptable only when the solution first writes the condition that the correction must satisfy and derives $\alpha$ from that condition.

## Stage 3 — Harden-by-depth, never harden-by-concealment

When GPT-5.5 Medium solves a candidate correctly, prefer a new natural dependency that deepens reasoning **after** the common entry point. Good hardening moves include:

- inverse reconstruction plus uniqueness;
- local-to-global compatibility or an obstruction;
- a sharp equality/extremal certificate;
- interaction of two intrinsic invariants;
- a genuine parameter-regime transition;
- classification/exhaustiveness after a candidate has been found;
- a canonical normal form whose existence and uniqueness both require proof.

Reject hardening that mainly:

- adds another algebraic layer, generator family, index, or custom relation;
- conjugates/recoordinates a standard object solely to hide it;
- inserts coefficients chosen to cancel terms already seen in the solver trace;
- replaces a natural formulation by a verbose presentation of the same object;
- increases dimension/degree/number of cases without a new dependency;
- makes the gateway harder to recognize while leaving the post-gateway solution nearly automatic.

Before editing the statement, complete this sentence:

> “The solver's original shortcut fails because the revised problem introduces the natural dependency ___, which arises from ___ and forces the additional reasoning step ___.”

If the sentence cannot be completed without mentioning extra notation, tuned coefficients, hidden encodings, or cancellation, reject the hardening proposal and choose a different blueprint.

## Stage 4 — Reviewer-quote simulation

Before `candidate-ready.json`, inspect the exact normalized pair and ask whether a strict reviewer could reasonably write any of the following:

- “The specific correction terms were chosen exactly to remove the unwanted action.”
- “The invariants are introduced in precisely the combinations that make all brackets/terms cancel.”
- “The hidden structure is uncovered only after the fact rather than motivated forward.”
- “The statement appears engineered from the intended solution.”
- “Difficulty comes from discovering a reverse-engineered encoding rather than genuine reasoning.”
- “Once the hidden representation is recognized, the rest is routine.”

For every plausible quote, either show the exact earlier forward derivation that defeats it or reject/redesign the candidate immediately. A bare statement that the construction is “natural” does not count.

## Stage 5 — Final quality verdict

A candidate is quality-safe only if all are true:

- the visible mathematical object has independent interest;
- every special ingredient has intrinsic provenance;
- no decisive object is merely guessed and verified by cancellation;
- the main difficulty survives a cleaner/natural formulation;
- at least two meaningful reasoning nodes remain after the main representation/invariant is discovered;
- the proposed hardening adds depth, not camouflage;
- the reviewer-quote simulation has no unanswered red flag.

Any failure is a pre-Codex rejection. Redesign now, not after portal feedback.

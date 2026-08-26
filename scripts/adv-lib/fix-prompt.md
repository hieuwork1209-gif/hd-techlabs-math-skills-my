Begin your reply with the `=== PROBLEM: ... ===` line above, copied exactly.

A human reviewer rejected this submission. Their feedback is at the end of this
message. Fix every defect they list, then resend both files.

Read these first from GitHub repo vohavinhtan/hd-skill-problem, branch main —
skip any you already read in this conversation:

  skills/math-check/SKILL.md
  skills/format-solution/SKILL.md
  skills/_shared/frontier_authoring_guide.md
  skills/_shared/style_guide.md
  skills/_shared/blocked_words.md
  skills/_shared/edit_scope_discipline.md
  skills/_shared/taxonomy_slots.md

`math-check` carries the Answer Falsification Audit and the Conclusion Checklist —
run both against your corrected draft before replying, since the reviewer's
objections are exactly what those gates exist to catch. `format-solution` governs
how the solution is written; `edit_scope_discipline` governs how much you are
allowed to touch.

Those files reference `skills/_shared/hard_gates.md`,
`skills/_shared/passed_exemplars.md` and `skills/_shared/breaker_playbook.md`,
which are NOT in the repo. Do not look for them; the limits they hold are listed
at the end of this message.

Ground rules:

- Address each numbered item. Do not argue with the reviewer, do not explain why
  a point is unfair, and do not fix only the easy ones. If you believe an item is
  mistaken, still change the text so the objection cannot be raised again.
- Do not change the problem's mathematics or its final answer unless an item
  requires it. This is a justification and metadata pass.
- "Unsupported claim" means an identity, bound, or comparison is used but never
  derived. Derive it inline, in the step that uses it. Stating it again more
  firmly does not fix it.
- "Reverse-engineered" means an auxiliary object is produced by decree and then
  verified. Rewrite so the object is *derived*: say what forces its shape, why the
  normalising constant is what it is, and what a solver would compute to find it.
  A verification appended to a guess is not a derivation.
- If a named formula is used more than once (conductor of a numerical semigroup,
  a degree bound, a residue rule), state it once explicitly with its hypotheses
  before its first use.

If any item concerns the Domain Explanation, rewrite that field to the portal's
required five-part structure, in this order and naming real alternatives:

  This problem involves <key mathematical elements>,
  which are part of <chosen domain and sub-domain>.
  The problem also involves <additional elements>,
  which are part of <the next best domain and sub-domain>.
  However, <why those are not core to the problem, or are less advanced>.

If any item concerns Problem Type or Answer Type, pick the option that actually
describes the task and update the classification table in BOTH files so they
match. The portal's Problem Type options are: Exact computation, Symbolic
derivation, Numerical approximation, Solve for unknowns, Construction under
constraints, Optimization, Exhaustive enumeration, Canonicalization or
normalization, Transformation between representations, Parameter identification,
Other.

Keep the hard limits: the problem statement under 2000 characters; the boxed
answer under 100 characters with `$` and whitespace stripped; each solution
concept under 100 characters, one to five of them; `## Steps` under 10,000
characters with no black-boxing to fit the cap.

Reply with exactly this and nothing else:

=== VERDICT: FIXED ===
=== FILE: problem.md ===
```markdown
<the full corrected problem.md>
```
=== FILE: solution.md ===
```markdown
<the full corrected solution.md>
```

The file payloads MUST sit inside the ```markdown fences. Write math as `$...$`
and `$$...$$`, never `\(...\)` or `\[...\]`, and never begin a line with `=`,
`-`, or `#` inside display math — a lone `=` on its own line becomes a heading
underline and destroys the formula above it when copied.

--- REVIEWER FEEDBACK ---

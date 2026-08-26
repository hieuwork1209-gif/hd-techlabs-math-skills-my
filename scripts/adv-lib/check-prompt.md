Begin your reply with the `=== PROBLEM: ... ===` line above, copied exactly.

This is the problem you authored in this conversation. Use the statement and the
ground truth you already hold here — nothing needs to be re-read.

The solver model was given that problem and produced the attempt at the end of
this message. Check its final answer against your ground truth.

The verdict describes the PROBLEM, not the solver. Use one of these three strings
exactly — `PASS`, `TOO_EASY`, `STALE`. Do not invent others such as `FAIL`,
`CORRECT`, or `REJECT`: anything else is discarded and the round is lost.

  solver was WRONG   → the problem held    → PASS
  solver was RIGHT   → the problem is weak → TOO_EASY

CASE A — the solver's final answer is WRONG.
The problem holds. Reply with exactly:

=== VERDICT: PASS ===

then one short paragraph naming the step it failed at.

CASE B — the solver's final answer is CORRECT (mathematically equivalent to the
ground truth, even if written differently).
The problem is too easy. Before hardening, read these from GitHub repo
vohavinhtan/hd-skill-problem, branch main — once is enough for this whole
conversation:

  skills/math-harder/SKILL.md
  skills/_shared/harden_loop.md
  skills/_shared/triviality_probe.md
  skills/_shared/taxonomy_slots.md
  skills/_shared/frontier_authoring_guide.md
  skills/format-solution/SKILL.md
  skills/_shared/style_guide.md
  skills/_shared/blocked_words.md

Those files reference `skills/_shared/hard_gates.md`,
`skills/_shared/passed_exemplars.md` and `skills/_shared/breaker_playbook.md`,
which are NOT in the repo. Do not look for them. In place of hard_gates, apply
its two rules directly: the boxed answer, with `$` and whitespace stripped,
under 100 characters; the `## Steps` section under 10,000 characters, with no
black-boxing to fit the cap.

Then diagnose the decisive shortcut the solver used and harden the problem to
close that route, per math-harder. Deepen the mathematical structure — do not add
difficulty through verbosity, extra variables, or extra requested outputs.
Re-derive the ground truth, and write solution.md to the format-solution
standard.

Reply with exactly this and nothing else:

=== VERDICT: TOO_EASY ===
=== FILE: problem.md ===
```markdown
<the full hardened problem.md>
```
=== FILE: solution.md ===
```markdown
<the full re-derived solution.md>
```

CASE C — the attempt answers a DIFFERENT version of the problem than the one you
hold. This applies in either direction: the statement may have been revised
outside this conversation, or you may have revised it here without that revision
reaching the repo. Either way the verdict would be meaningless, so do not judge
it — and do not call it PASS merely because the answer does not match.

Reply with exactly:

=== VERDICT: STALE ===
=== FILE: problem.md ===
```markdown
<the full current problem.md as you hold it>
```
=== FILE: solution.md ===
```markdown
<the full current solution.md as you hold it>
```

If you do not hold this problem at all, reply with `=== VERDICT: STALE ===` and
one line saying so, with no file blocks.

---

File payloads MUST sit inside the ```markdown fences shown above. Copying an
unfenced reply mangles LaTeX, and that mangled text is what gets written to
disk. Inside a fenced block the text is copied verbatim.

Write math as `$...$` and `$$...$$`, never `\(...\)` or `\[...\]`.

Never begin a line with `=`, `-`, or `#` inside display math. Keep each relation
on one line, or put the operator at the END of the previous line — a lone `=` on
its own line is read as a markdown heading underline, and copying the reply
replaces the formula above it with a row of `=`.

`solution.md` must keep the repo's section structure, in this order: `## Steps`,
`## Answer`, `## Classification`, `## Solution Concepts`. A reply carrying only
`## Steps` is incomplete — the submission gates read `## Answer` and
`## Classification`, and they must match the taxonomy table in problem.md. Keep
the `## Steps` section under 10,000 characters.

--- SOLVER ATTEMPT ---

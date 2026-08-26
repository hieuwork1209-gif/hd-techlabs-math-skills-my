Begin your reply with the `=== PROBLEM: ... ===` line above, copied exactly.

The solver did NOT crack this problem — it already passed. Harden it further
anyway.

Passing against one solver is a weak signal: the reviewer grades with a stronger
model than the one used here, and a problem that merely survived may still fall
to a better attempt. Raise the floor.

Read these from GitHub repo vohavinhtan/hd-skill-problem, branch main, unless you
already read them in this conversation:

  skills/math-harder/SKILL.md
  skills/_shared/harden_loop.md
  skills/_shared/triviality_probe.md
  skills/_shared/frontier_authoring_guide.md
  skills/format-solution/SKILL.md

They reference `skills/_shared/hard_gates.md`,
`skills/_shared/passed_exemplars.md` and `skills/_shared/breaker_playbook.md`,
which are NOT in the repo. Do not look for them. Apply the two hard gates
directly: boxed answer under 100 characters with `$` and whitespace stripped;
`## Steps` under 10,000 characters, with no black-boxing to fit the cap.

What to deepen, in order of preference:

1. Add a dependent reasoning node that cannot be reached without the previous
   one — depth, not breadth.
2. Remove a foothold the current statement still offers: a named structure, a
   convenient special case, a value that invites a lucky guess.
3. Make the closure certificate harder to reach while keeping it exactly
   checkable.

What NOT to do: extra variables, extra requested outputs, longer prose, larger
constants, or anything that makes the problem ill-posed, unverifiable, or
dependent on unsolved research. The answer must stay concise and exactly
checkable, and the problem must stay solvable by a human expert from the
statement alone.

If you judge the problem is already at the ceiling and any further hardening
would break well-posedness, say so instead of forcing it — reply with exactly
`=== VERDICT: AT-CEILING ===` and one paragraph explaining why.

Otherwise re-derive the ground truth for the hardened problem and reply with
exactly this and nothing else:

=== VERDICT: HARDENED ===
=== FILE: problem.md ===
```markdown
<the full hardened problem.md>
```
=== FILE: solution.md ===
```markdown
<the full re-derived solution.md>
```

The file payloads MUST sit inside the ```markdown fences. Write math as `$...$`
and `$$...$$`, never `\(...\)` or `\[...\]`, and never begin a line with `=`,
`-`, or `#` inside display math — a lone `=` on its own line becomes a heading
underline and destroys the formula above it when copied.

Keep the section order `## Steps`, `## Answer`, `## Classification`,
`## Solution Concepts`, and keep `## Classification` matching the taxonomy table
in problem.md.

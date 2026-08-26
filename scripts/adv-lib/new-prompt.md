Begin your reply with the `=== PROBLEM: ... ===` line above, copied exactly.

Author a NEW original frontier math problem for the Rainier project, and its
ground-truth solution.

Read these first from GitHub repo vohavinhtan/hd-skill-problem, branch main:

  skills/math-clone/SKILL.md
  skills/_shared/taxonomy_slots.md
  skills/_shared/frontier_authoring_guide.md
  skills/_shared/triviality_probe.md
  skills/_shared/originality_audit.md
  skills/format-solution/SKILL.md
  skills/_shared/style_guide.md
  skills/_shared/blocked_words.md

They reference `skills/_shared/hard_gates.md`,
`skills/_shared/passed_exemplars.md`, `skills/_shared/breaker_playbook.md` and
`skills/_shared/accepted_topic_history.md`, none of which are in the repo. Do
not look for them. In place of hard_gates apply its two rules directly: the
boxed answer, with `$` and all whitespace stripped, under 100 characters; the
`## Steps` section under 10,000 characters, with no black-boxing to fit the cap.

Pick the Domain / Sub-domain from `taxonomy_slots.md`. Among honest fits prefer
the open slot with the smallest positive remaining capacity. State which slot you
chose and why in one line before the file blocks.

The problem must be solvable by a human expert from the statement alone, have a
concise exactly-checkable answer, and target a model-breaking difficulty: a
GPT-5-class thinking model should be likely to fail unless it reconstructs the
whole hidden structure. Build difficulty from dependent structure, not from
verbosity, extra variables, extra requested outputs, or large constants.

This conversation is the home of this problem from now on: keep the statement and
the ground truth, because every later round of checking and hardening happens
here.

Reply with exactly this and nothing else after the one-line slot note:

=== VERDICT: NEW ===
=== FILE: problem.md ===
```markdown
<the full problem.md, including the Domain Classification table>
```
=== FILE: solution.md ===
```markdown
<the full solution.md>
```

The file payloads MUST sit inside the ```markdown fences. Write math as `$...$`
and `$$...$$`, never `\(...\)` or `\[...\]`, and never begin a line with `=`,
`-`, or `#` inside display math — a lone `=` on its own line becomes a heading
underline and destroys the formula above it when copied.

`problem.md` must carry a `## Domain Classification` table with **Domain**,
**Sub-domain**, **Problem Type**, **Answer Type**. `solution.md` must use the
section order `## Steps`, `## Answer`, `## Classification`, `## Solution
Concepts`, and its `## Classification` must match that table.

Begin your reply with the `=== PROBLEM: ... ===` line above, copied exactly.

Reformat the `solution.md` you produced for this problem so it meets the repo's
submission standard.

First read these from GitHub repo vohavinhtan/hd-skill-problem, branch main:

  skills/format-solution/SKILL.md
  skills/_shared/style_guide.md
  skills/_shared/blocked_words.md
  skills/_shared/edit_scope_discipline.md

Those files reference `skills/_shared/hard_gates.md`, which is not in the repo.
Do not look for it. Apply its two rules directly instead:

- the boxed final answer, with `$` and all whitespace stripped, must be under
  100 characters
- the `## Steps` section, counted as written, must be under 10,000 characters

Compression must stay zero-blackbox: never hide a derivation behind "one checks"
or "it follows" to fit the cap. If an honest write-up cannot fit, say so instead
of faking it.

Do not change the mathematics, the final answer, or the problem. This is a
formatting and presentation pass only — same result, same reasoning, restructured
and cleaned to the standard.

Reply with exactly this and nothing else:

=== VERDICT: REFORMAT ===
=== FILE: solution.md ===
```markdown
<the full reformatted solution.md>
```

The file payload MUST sit inside the ```markdown fence. Write math as `$...$`
and `$$...$$`, never `\(...\)` or `\[...\]`, and never begin a line with `=`,
`-`, or `#` inside display math — a lone `=` on its own line becomes a markdown
heading underline and destroys the formula above it when copied.

Keep the section order `## Steps`, `## Answer`, `## Classification`,
`## Solution Concepts`, and keep `## Classification` matching the taxonomy table
in problem.md.

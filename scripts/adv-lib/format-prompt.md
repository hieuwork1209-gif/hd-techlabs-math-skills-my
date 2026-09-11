Begin your reply with the `=== PROBLEM: ... ===` line above, copied exactly.

Reformat the `solution.md` you produced for this problem so it meets the repo's
submission standard.

First read these from GitHub repo hieuwork1209-gif/hd-techlabs-math-skills-my,
branch main:

  skills/format-solution/SKILL.md
  skills/_shared/hard_gates.md
  skills/_shared/style_guide.md
  skills/_shared/blocked_words.md
  skills/_shared/edit_scope_discipline.md

Treat `skills/_shared/hard_gates.md` as the submission source of truth and also
mirror the current field constants in `scripts/adv`. In particular, run both
Answer gates on the exact `## Answer` field:

- raw portal length must be at most the current `ANSWER_MAX` in `scripts/adv`
  (currently 102 characters)
- after stripping `$` and all whitespace, the answer must be under 100 characters

Also require the answer to use only prompt-defined notation except bound dummy
indices introduced locally inside the answer expression. Do not use aliases that
exist only in the solution just to fit the cap. Prefer a mathematically equivalent
compact expression in prompt-defined notation. Never truncate the requested
mathematical object.

The `## Steps` section, counted as written, must be under 10,000 characters.
Compression must stay zero-blackbox: never hide a derivation behind "one checks"
or "it follows" to fit the cap.

Do not change the mathematics, the final result, or the problem. This is a
formatting and presentation pass only: same result and same reasoning, rewritten
to the repository standard. If the exact answer cannot honestly meet the hard
gates without changing the problem or Answer Type, do not invent a proxy; keep
the mathematical result intact so the upstream workflow can route the problem to
a statement/Answer-Type redesign instead of falsely marking it submit-ready.

Reply with exactly this and nothing else:

=== VERDICT: REFORMAT ===
=== FILE: solution.md ===
```markdown
<the full reformatted solution.md>
```

The file payload MUST sit inside the ```markdown fence. Write math as `$...$`
and `$$...$$`, never `\(...\)` or `\[...\]`, and never begin a line with `=`,
`-`, or `#` inside display math: a lone `=` on its own line becomes a Markdown
heading underline and destroys the formula above it when copied.

Keep the section order `## Steps`, `## Answer`, `## Classification`,
`## Solution Concepts`, and keep `## Classification` matching the taxonomy table
in problem.md.

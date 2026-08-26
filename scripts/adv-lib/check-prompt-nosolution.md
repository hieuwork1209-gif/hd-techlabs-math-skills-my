Begin your reply with the `=== PROBLEM: ... ===` line above, copied exactly.

**This problem has no `solution.md` in the repo yet.** Use the ground truth you
derived for it earlier in this conversation as the reference answer. If you no
longer hold it, say so plainly instead of guessing — do not invent an answer.

The current problem statement is pasted at the end of this message; treat it as
authoritative. Follow skills/math-harder/SKILL.md when hardening.

The solver model was given that problem and produced the attempt at the end of
this message. Check its final answer against your ground truth.

CASE A — the solver's final answer is WRONG.
The problem holds. Reply with exactly:

=== VERDICT: PASS ===
=== FILE: solution.md ===
```markdown
<the full ground-truth solution.md for the current problem>
```

then one short paragraph naming the step the solver failed at. Write the
solution file properly — it is missing from the repo and this reply is what
fills it in.

CASE B — the solver's final answer is CORRECT (mathematically equivalent to your
ground truth, even if written differently).
The problem is too easy. Diagnose the decisive shortcut the solver used, then
harden the problem to close that route. Deepen the mathematical structure — do
not add difficulty through verbosity, extra variables, or extra requested
outputs. Re-derive the ground truth for the hardened problem.

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

File payloads MUST sit inside the ```markdown fences shown above. Copying an
unfenced reply mangles LaTeX — display math loses its backslashes and rows of
`=` become markdown headings — and that mangled text is what gets written to
disk. Inside a fenced block the text is copied verbatim.

Write math as `$...$` and `$$...$$`, never `\(...\)` or `\[...\]`.

Never begin a line with `=`, `-`, or `#` inside display math. Keep each relation
on one line, or put the operator at the END of the previous line:

    $$
    H(t) = \frac{1 - 2t^{p+2}}{(1-t)^2}
    $$

not

    $$
    H(t)
    =
    \frac{1 - 2t^{p+2}}{(1-t)^2}
    $$

A lone `=` on its own line is read as a markdown heading underline, and copying
the reply turns the line above it into `============`, destroying the formula.

`solution.md` must keep the repo's section structure, in this order:

```
## Steps

Step 1: <short title>
<derivation>

Step 2: ...

---

## Answer

<the final answer alone, in LaTeX, nothing else>

---

## Classification

**Problem Type:** <type>

**Answer Type:** <type>

---

## Solution Concepts

- <concept>
- <concept>
```

A reply carrying only `## Steps` is incomplete — the downstream submission gates
read `## Answer` and `## Classification`, and they must match the taxonomy table
in problem.md. Keep the `## Steps` section under 10,000 characters.

--- CURRENT problem.md ---

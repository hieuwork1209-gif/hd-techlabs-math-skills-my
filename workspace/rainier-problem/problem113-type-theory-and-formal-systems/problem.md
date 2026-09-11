# Normalized Math Problem

## LaTeX (Normalized)

Consider the following formal term-rewriting system. Terms are generated from a constant $z$, a unary constructor $a$, and unary constructors $d_q$ for $2\leq q\leq n$. Write $a^r(t)$ for the $r$-fold iterate of $a$, with $a^0(t)=t$.

The only reduction rules are, for every term $t$,
$$
d_q(a(t))\longrightarrow a^2(d_q(t)),
\qquad 2\leq q\leq n,
$$
and
$$
d_q(d_p(t))\longrightarrow a(d_p(d_q(t))),
\qquad 2\leq p<q\leq n.
$$
A reduction may be applied to any matching subterm, and each rule application counts as one step.

For $n\geq2$, define
$$
M_n=d_n(d_{n-1}(\cdots d_2(z)\cdots)).
$$
A complete reduction is a reduction sequence from $M_n$ to a term with no applicable rule. Different choices of redex can give different sequence lengths. Let $L_n$ be the minimum number of steps in a complete reduction of $M_n$.

Determine $L_n$ exactly as a closed-form expression in $n$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Logic, Set Theory, and Foundations |
| **Sub-domain** | Type theory and formal systems |
| **Problem Type** | Optimization |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem asks for an exact shortest normalization in a formal term-rewriting system. Each interchange creates one new $a$, while an $a$ created deeper in the unary word is repeatedly duplicated as it moves outward. The reduction order therefore induces a genuinely weighted adjacent-swap optimization on the constructor permutation, rather than a fixed inversion count alone.

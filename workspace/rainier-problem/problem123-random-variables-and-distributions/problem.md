# Normalized Math Problem

## LaTeX (Normalized)

Let $a>0$ and $t>0$. Consider all real random variables $X$ taking values in $[0,1]$ and satisfying
$$
EX=\frac12,
$$
$$
EX^2=\frac{a+1}{2(2a+1)},
\qquad
EX^3=\frac{a+2}{4(2a+1)}.
$$
Define
$$
\Delta_a(t)
=
\sup E\frac1{1+tX}
-
\inf E\frac1{1+tX},
$$
where both extrema are taken over all such $X$.

Determine $\Delta_a(t)$ exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Random variables and distributions |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The problem asks for the exact range of an expectation as the law of a bounded random variable varies under prescribed moment constraints. The primary object is therefore the family of admissible probability distributions of a random variable; polynomial moment duality is the tool used to identify the extremal laws.

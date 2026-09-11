# Normalized Math Problem

## LaTeX (Normalized)

Let $n\ge2$, and let $U_1,\dots,U_n$ be independent random variables, each uniformly distributed on $(0,1)$. Write their order statistics as
$$
U_{(1)}<\cdots<U_{(n)}.
$$
Fix integers $1\le r<s\le n$. Define
$$
\rho_{r,s}^{(n)}
=\sup E\bigl[f(U_{(r)})g(U_{(s)})\bigr],
$$
where the supremum is over all real Borel functions $f,g$ satisfying
$$
Ef(U_{(r)})=Eg(U_{(s)})=0,
\qquad
E f(U_{(r)})^2=E g(U_{(s)})^2=1.
$$
Determine $\rho_{r,s}^{(n)}$ exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Joint distributions and dependence |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The problem asks for the strongest possible nonlinear correlation between two dependent order statistics. Its primary object is therefore dependence structure in a joint distribution; conditional laws and orthogonal-polynomial operator methods are used to determine that dependence coefficient exactly.

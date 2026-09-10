# Normalized Math Problem

## LaTeX (Normalized)

For a permutation $\pi\in S_6$, let
$$
\operatorname{inv}(\pi)=\#\{(i,j):1\le i<j\le6,\ \pi(i)>\pi(j)\}
$$
be its inversion number. Index the rows and columns of a $720\times720$ matrix $A$ by the elements of $S_6$, and define
$$
A_{\sigma,\tau}=2^{\operatorname{inv}(\sigma^{-1}\tau)}
\qquad(\sigma,\tau\in S_6).
$$
Determine $\det A$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Determinants |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The entries form the exponential kernel of Kendall-tau distance on permutations, since $\operatorname{inv}(\sigma^{-1}\tau)$ is the adjacent-transposition distance between $\sigma$ and $\tau$. The determinant is governed by a noncentral factorization in the regular representation of $S_6$, so Linear Algebra -> Determinants is the primary classification.

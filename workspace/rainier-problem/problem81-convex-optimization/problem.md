# Normalized Math Problem

## LaTeX (Normalized)

Let $\varepsilon=(\varepsilon_1,\ldots,\varepsilon_6)\in\{-1,1\}^6$. Let $\mathcal F_\varepsilon$ be the set of real symmetric positive semidefinite matrices $G=(g_{ij})_{1\le i,j\le6}$ satisfying
$$
g_{ii}=1\quad(1\le i\le6),
$$
and, with cyclic indices,
$$
g_{i,i+1}=\frac{\varepsilon_i}{2}\quad(1\le i\le6).
$$
Define
$$
D(\varepsilon)=\max_{G\in\mathcal F_\varepsilon}\det G.
$$
For $\sigma\in\{-1,1\}$, let $D_\sigma$ denote the common value of $D(\varepsilon)$ among sign patterns satisfying $\prod_{i=1}^6\varepsilon_i=\sigma$, provided that this common value is well-defined.

Prove that $D_+$ and $D_-$ are well-defined and determine the ordered pair $(D_+,D_-)$ exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Convex optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem asks for maximum determinants of positive-semidefinite matrix completions under signed affine correlation constraints. The sign pattern has a switching invariant around the cycle, and the optimizer must be characterized through strict concavity, first-order optimality, and the resulting sparse precision matrix before the two determinant values can be evaluated. Thus Optimization and Numerical Mathematics -> Convex optimization is the direct classification.

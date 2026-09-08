# Normalized Math Problem

## LaTeX (Normalized)

Let $\operatorname{Sym}_3^+(\mathbb R)$ be the cone of positive-semidefinite real symmetric $3\times3$ matrices, with Lebesgue measure on the six independent entries. For $A\in\operatorname{Sym}_3^+(\mathbb R)$, put
$$
e_2(A)=\frac12\left((\operatorname{tr}A)^2-\operatorname{tr}(A^2)\right).
$$
For $n\ge1$, define
$$
I_n=\int_{\operatorname{Sym}_3^+(\mathbb R)}
\exp\left(-n\left(e_2(A)^2+(\operatorname{tr}A)^8\right)\right)\,dA.
$$
Also let
$$
\gamma=\lim_{m\to\infty}\left(\sum_{k=1}^m\frac1k-\log m\right)
$$
be Euler's constant. Evaluate
$$
\lim_{n\to\infty}
\left(
\frac{64n^{3/2}}{\pi^{5/2}}I_n-\log n
\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of integration |
| **Problem Type** | Exact computation |
| **Answer Type** | Real number |

---

## Domain Explanation

The invariant $e_2(A)$ is the second elementary symmetric polynomial of the eigenvalues and vanishes on the rank-one boundary of the positive-semidefinite cone. The regular interior scale and the rank-one boundary scale occur at the same critical order, producing a logarithmic resonance whose finite part determines the limit. This is a natural degenerate asymptotic-integration problem in Calculus -> Applications of integration.

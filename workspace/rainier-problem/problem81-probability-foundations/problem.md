# Normalized Math Problem

## LaTeX (Normalized)

Consider a two-type Galton-Watson process with types $A$ and $B$.

A type $A$ individual has offspring
$$
\varnothing
$$
with probability $\frac{1}{2}$,
$$
(A,A)
$$
with probability $\frac{3}{8}$, and
$$
(B,B)
$$
with probability $\frac{1}{8}$.

A type $B$ individual has offspring
$$
\varnothing
$$
with probability $\frac{1}{2}$,
$$
(A)
$$
with probability $\frac{1}{4}$, and
$$
(B,B,B)
$$
with probability $\frac{1}{4}$.

Let $T$ be the total number of individuals ever born, including the initial ancestor, and define
$$
G_A(z)=\mathbb E_A[z^T],
\qquad
G_B(z)=\mathbb E_B[z^T].
$$

There are unique constants $\kappa,\alpha,\beta$ such that, as $z\uparrow1$,
$$
1-G_A(z)
=
\kappa(1-z)^{1/2}
+
O(1-z)
$$
and
$$
G_A(z)-G_B(z)
=
-\alpha(1-z)
+
\beta(1-z)^{\frac{3}{2}}
+
o((1-z)^{\frac{3}{2}}).
$$

Determine $(\kappa,\alpha,\beta)$ exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Probability foundations |
| **Problem Type** | Parameter identification |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem asks for singular coefficients of total-progeny probability generating functions in a critical irreducible multitype Galton-Watson process. The critical Perron mode creates the square-root singularity, while the stable type-difference mode controls the next asymmetric term. Thus Probability and Statistics -> Probability foundations is primary.

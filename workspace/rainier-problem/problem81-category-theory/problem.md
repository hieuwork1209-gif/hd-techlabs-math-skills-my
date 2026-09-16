# Normalized Math Problem

## LaTeX (Normalized)

Let $\mathcal V$ be the category of finite-dimensional vector spaces over $\mathbb F_2$ and linear maps, and let $T:\mathcal V\to\mathcal V$ be the tensor-cube functor
$$
T(V)=V^{\otimes3},
\qquad
T(f)=f^{\otimes3}.
$$
A natural endomorphism $E:T\Rightarrow T$ is called idempotent if $E_V^2=E_V$ for every $V$.

For each integer $n\ge2$, let $R_n$ be the largest possible rank of
$$
E_{\mathbb F_2^n}:(\mathbb F_2^n)^{\otimes3}\to(\mathbb F_2^n)^{\otimes3}
$$
among all natural idempotents $E$ other than $0$ and the identity transformation. Let $N_n$ be the number of natural idempotents attaining this maximum.

Determine the ordered pair $(R_n,N_n)$ exactly for every $n\ge2$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Logic, Set Theory, and Foundations |
| **Sub-domain** | Category theory |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem asks for an extremal property of direct-summand natural transformations of a tensor-power functor. Solving it requires first recovering the natural endomorphism algebra from naturality, then understanding how its idempotents act functorially on tensor cubes of varying dimension. Thus Logic, Set Theory, and Foundations -> Category theory is the primary classification.

# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
\operatorname{Alt}_6(2)=\{A\in M_6(\mathbb F_2):A^T=A,\ \operatorname{diag}(A)=0\}.
$$
Call a $3$-dimensional subspace $W\le \operatorname{Alt}_6(2)$ nonsingular if every nonzero matrix in $W$ is invertible.

A $3$-dimensional subspace $U\le \mathbb F_2^6$ is a common Lagrangian for $W$ if
$$
u^TAv=0
$$
for all $u,v\in U$ and all $A\in W$.

The group $GL_6(2)$ acts on such subspaces by simultaneous congruence,
$$
g\cdot W=\{g^TAg:A\in W\}.
$$
Determine the exact number of $GL_6(2)$-orbits of nonsingular $3$-dimensional subspaces $W\le \operatorname{Alt}_6(2)$ that admit at least one common Lagrangian.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Matrix decompositions and canonical forms |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for a simultaneous-congruence classification of structured spaces of alternating matrices. The common-Lagrangian condition allows the matrices to be reduced to field-valued cross blocks and then to two canonical linearized-polynomial normal forms, so the central task is a matrix canonical-form classification rather than determinant evaluation or finite enumeration.

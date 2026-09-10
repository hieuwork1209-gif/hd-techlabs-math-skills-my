# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
\operatorname{Alt}_6(2)=\{A\in M_6(\mathbb F_2):A^T=A,\ \operatorname{diag}(A)=0\}
$$
be the $15$-dimensional space of alternating $6\times6$ matrices over $\mathbb F_2$.

Call a $3$-dimensional subspace $W\le \operatorname{Alt}_6(2)$ nonsingular if every nonzero matrix in $W$ is invertible.

The group $GL_6(2)$ acts on such subspaces by simultaneous congruence,
$$
g\cdot W=\{g^TAg:A\in W\}.
$$
Determine the exact number of $GL_6(2)$-orbits of nonsingular $3$-dimensional subspaces of $\operatorname{Alt}_6(2)$.

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

The central task is to classify $3$-dimensional spaces of alternating matrices up to simultaneous congruence. Nonsingularity is only the structural constraint defining the family; the requested output is the number of canonical congruence classes. This makes Matrix decompositions and canonical forms a better fit than Determinants or Matrices and matrix operations, which would describe local computations rather than the orbit-classification problem itself.

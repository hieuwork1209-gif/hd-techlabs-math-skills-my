# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
\operatorname{Alt}_{24}(3)=\{A\in M_{24}(\mathbb F_3):A^T=-A\}.
$$
A $2$-dimensional subspace $W\le \operatorname{Alt}_{24}(3)$ is called regular semisimple of type $(4,4,4)$ if, for some ordered basis $(A,B)$ of $W$, the matrix $A$ is invertible and
$$
T=A^{-1}B
$$
has squarefree minimal polynomial
$$
m_T=p_1p_2p_3,
$$
where $p_1,p_2,p_3\in\mathbb F_3[x]$ are distinct monic irreducible polynomials of degree $4$.

The group $GL_{24}(3)$ acts on such pencils by simultaneous congruence,
$$
g\cdot W=\{g^TAg:A\in W\}.
$$
Determine the exact number of $GL_{24}(3)$-orbits of regular semisimple pencils of type $(4,4,4)$.

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

The problem is a canonical-form classification of regular semisimple alternating matrix pencils. The self-adjoint operator $A^{-1}B$ decomposes into three irreducible quartic primary symplectic blocks, while changing the basis of the pencil acts simultaneously on the three primary factors through $PGL_2(3)$. The central issue is therefore primary decomposition and simultaneous matrix-pencil equivalence.
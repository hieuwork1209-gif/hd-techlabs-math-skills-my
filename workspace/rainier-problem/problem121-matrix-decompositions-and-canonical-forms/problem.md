# Normalized Math Problem

## LaTeX (Normalized)

Let $n\geq6$ be even and let $m=\binom{n}{2}$. Let $B_n\in M_{n\times m}(\mathbb Z)$ have columns indexed by the unordered pairs $\{i,j\}\subset\{1,\ldots,n\}$, with the column indexed by $\{i,j\}$ equal to $e_i+e_j$. Let $J_n$ be the $n\times n$ all-ones matrix, and define
$$
L_n=
\begin{pmatrix}
(2n-1)I_n-J_n&-B_n\\
-B_n^T&2nI_m-B_n^TB_n
\end{pmatrix}.
$$
Determine the Smith normal form of $L_n$ over $\mathbb Z$, with the diagonal invariant factors written in divisibility order.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Matrix decompositions and canonical forms |
| **Problem Type** | Canonicalization or normalization |
| **Answer Type** | Canonical form |

---

## Domain Explanation

The problem asks for the Smith normal form of an explicit structured integer block matrix. In the even-$n$ regime, the main obstruction is the 2-primary part: the incidence matrix loses one rank modulo $2$, and distinguishing the resulting order-$4$ correction requires a genuinely 2-adic lifting argument rather than only rational spectral data. This makes Linear Algebra -> Matrix decompositions and canonical forms the fundamental classification.

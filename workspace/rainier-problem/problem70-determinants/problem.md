# Normalized Math Problem

## LaTeX (Normalized)

Index the rows and columns of a $1024\times1024$ matrix $A$ by the subsets of $[10]=\{1,\dots,10\}$. For subsets $S,T\subseteq[10]$, define
$$
A_{S,T}=
\begin{cases}
11+|S|(10-|S|),&S=T,\\
-1,&|S\triangle T|=1,\\
0,&\text{otherwise},
\end{cases}
$$
where $S\triangle T$ denotes symmetric difference. Determine $\det A$.

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

The matrix is $I+L+V$ on the $10$-dimensional hypercube, where $L$ is the graph Laplacian and $V(S)=|S|(10-|S|)$ is the radial potential equal to the edge-boundary size of the subset $S$. Its exact determinant is obtained by decomposing the Boolean lattice into symmetric chains and evaluating the resulting tridiagonal blocks, so Linear Algebra -> Determinants is the primary classification.

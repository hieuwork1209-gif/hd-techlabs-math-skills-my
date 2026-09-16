# Normalized Math Problem

## LaTeX (Normalized)

Let $(e_1,\dots,e_5)$ and $(f_1,\dots,f_5)$ be orthonormal bases of $\mathbb R^5$. Suppose there are positive real numbers $a,b$ such that
$$
|\langle e_i,f_i\rangle|=a\qquad(i=1,\dots,5)
$$
and
$$
|\langle e_i,f_j\rangle|=b\qquad(i\ne j).
$$
Determine $a$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Linear Algebra |
| **Sub-domain** | Inner product spaces |
| **Problem Type** | Exact determination |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem is primarily Linear Algebra and Inner product spaces: the pairwise inner products between two orthonormal bases form an orthogonal transition matrix whose matched and unmatched coefficients have two common magnitudes. Orthogonality couples the signs of these coefficients globally, and determining the diagonal magnitude requires resolving that sign compatibility rather than only using row norms.

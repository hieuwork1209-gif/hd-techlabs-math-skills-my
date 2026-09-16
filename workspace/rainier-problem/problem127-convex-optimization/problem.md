# Normalized Math Problem

## LaTeX (Normalized)

Let $n\ge4$, and let $r,s\in\mathbb R$ satisfy
$$
|r|<1,
\qquad
|s-r^2|<1-r^2.
$$
Among all real symmetric positive definite Toeplitz matrices
$$
T=(c_{|i-j|})_{i,j=0}^{n-1}
$$
with
$$
c_0=1,
\qquad
c_1=r,
\qquad
c_2=s,
$$
determine the largest possible value of $\det T$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Convex optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

This problem is primarily Optimization and Numerical Mathematics and Convex optimization: it maximizes the determinant over an affine family of positive definite Toeplitz matrices. The key issue is to parameterize successive positive-definite completions so that the global log-determinant objective separates into sharp one-step losses.

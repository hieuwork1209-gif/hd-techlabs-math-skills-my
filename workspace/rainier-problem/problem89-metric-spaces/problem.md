# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
C=\mathbb{Z}/10\mathbb{Z}
$$
with the cycle metric
$$
d_C(i,j)=\min\{|i-j|,10-|i-j|\}.
$$

Let $P$ be the Petersen graph with vertices
$$
\{u_i,v_i:i\in\mathbb{Z}/5\mathbb{Z}\}
$$
and edges
$$
u_i u_{i+1},\qquad u_i v_i,\qquad v_i v_{i+2},
$$
with indices taken modulo $5$. Give $P$ its shortest-path metric $d_P$.

For a bijection $f:C\to P$, define
$$
\operatorname{dist}(f)
=
\left(\max_{i\neq j}\frac{d_P(f(i),f(j))}{d_C(i,j)}\right)
\left(\max_{i\neq j}\frac{d_C(i,j)}{d_P(f(i),f(j))}\right).
$$

Determine
$$
\min_{f:C\to P\text{ bijective}}\operatorname{dist}(f).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Metric spaces |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for the least bi-Lipschitz distortion between two explicit finite metric spaces, so Analysis / Metric spaces is the natural primary classification. The proof reduces the metric distortion to a circular-bandwidth obstruction for the Petersen graph and then constructs an optimal cyclic ordering.

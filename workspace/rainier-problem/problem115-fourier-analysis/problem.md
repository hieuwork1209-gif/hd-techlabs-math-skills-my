# Normalized Math Problem

## LaTeX (Normalized)

Let $E=\mathbb F_2^8$ with the standard dot product. For every $M\in\operatorname{GL}(8,2)$ and every Boolean polynomial $g:E\to\mathbb F_2$ of algebraic degree at most $2$ with $g(0)=0$ and
$$
\left|\sum_{y\in E}(-1)^{g(y)+a\cdot y}\right|=16
\qquad\text{for every }a\in E,
$$
$$
\sum_{y\in E}(-1)^{g(y)}=16,
$$
define
$$
f_{M,g}(x,y)=(-1)^{x\cdot My+g(y)},
\qquad (x,y)\in E\times E.
$$
For $h:E\times E\to\mathbb C$, define the normalized Walsh--Fourier transform
$$
(\mathcal Fh)(u,v)=2^{-8}\sum_{x,y\in E}h(x,y)(-1)^{x\cdot v+y\cdot u}.
$$
How many distinct functions $f_{M,g}$ satisfy
$$
\mathcal Ff_{M,g}=f_{M,g}?
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Fourier analysis |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for the exact number of self-dual functions in the positive-Walsh quadratic Maiorana--McFarland class. Walsh self-duality forces a linear involution, while the positive bent sign selects one Arf type of nondegenerate quadratic forms, so the count is governed by the interaction of Fourier duality with orthogonal geometry over $\mathbb F_2$.

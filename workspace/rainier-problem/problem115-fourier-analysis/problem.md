# Normalized Math Problem

## LaTeX (Normalized)

Let $E=\mathbb F_2^8$ with the standard dot product, and fix
$$
e=(1,0,0,0,0,0,0,0)\in E.
$$
For every $M\in\operatorname{GL}(8,2)$ and every Boolean polynomial $g:E\to\mathbb F_2$ of algebraic degree at most $2$ with $g(0)=0$ and
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
How many distinct functions $f_{M,g}$ satisfy all three conditions
$$
\mathcal Ff_{M,g}=f_{M,g},\qquad Me=e,\qquad g(e)=0?
$$
Express the exact count in prime-factorized form.

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

The problem asks for the exact number of marked self-dual functions in a quadratic Walsh--Fourier class. Fourier self-duality first forces a linear involution preserving a positive-sign quadratic bent form, while the marked conditions require a second incidence count between those involutions and singular fixed vectors; the orthogonal geometry enters as the finite-dimensional structure controlling that Fourier fixed-point problem.

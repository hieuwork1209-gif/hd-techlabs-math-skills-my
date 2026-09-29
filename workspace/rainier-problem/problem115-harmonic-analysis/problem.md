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
For $h:E\times E\to\mathbb C$, define
$
(\mathcal Fh)(u,v)=2^{-8}\sum_{x,y\in E}h(x,y)(-1)^{x\cdot v+y\cdot u}.
$
Over all distinct functions $f_{M,g}$ satisfying $\mathcal Ff_{M,g}=f_{M,g}$, compute
$
\sum_f\sum_{0\ne b\in E}2^{-8}\sum_{x\in E}
f(x,0)\overline{f(x,b)}(-1)^{b\cdot x}.
$
Express the exact value in prime-factorized form.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Harmonic analysis |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The requested quantity is a diagonal Walsh-correlation sum over Fourier-invariant quadratic phases. The decisive harmonic-analysis steps are character orthogonality and Fourier self-duality; finite orthogonal geometry then parametrizes the symmetries needed to evaluate the resulting fixed-vector sum.

# Normalized Math Problem

## LaTeX (Normalized)

Let $E=\mathbb F_2^8$ with the standard dot product. For every affine permutation
$$
\pi(y)=My+c,
\qquad M\in\operatorname{GL}(8,2),\ c\in E,
$$
and every Boolean polynomial $g:E\to\mathbb F_2$ of algebraic degree at most $2$ with $g(0)=0$, define
$$
f_{\pi,g}(x,y)=(-1)^{x\cdot\pi(y)+g(y)},
\qquad (x,y)\in E\times E.
$$
For $h:E\times E\to\mathbb C$, define the normalized Walsh--Fourier transform
$$
(\mathcal Fh)(u,v)=2^{-8}\sum_{x,y\in E}h(x,y)(-1)^{x\cdot v+y\cdot u}.
$$
How many distinct functions $f_{\pi,g}$ satisfy
$$
\mathcal Ff_{\pi,g}=f_{\pi,g}?
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

The problem asks for the exact number of self-dual quadratic functions in the affine Maiorana--McFarland class under the normalized Walsh--Fourier transform. Fourier self-duality becomes an affine-involution condition, while the quadratic restriction on $g$ forces an invariant-polynomial calculation for those involutions, so Fourier analysis is the organizing subject.

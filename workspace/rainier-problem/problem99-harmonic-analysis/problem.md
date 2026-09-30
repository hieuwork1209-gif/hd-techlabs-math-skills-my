# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
p(\theta)=1+2\operatorname{Re}\left(c_1e^{i\theta}+c_2e^{2i\theta}+c_3e^{3i\theta}+c_4e^{4i\theta}\right)
$$
be a trigonometric polynomial satisfying $p(\theta)\geq0$ for every real $\theta$. Suppose that $c_2=0$.

Determine the largest possible value of $|c_1|$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Harmonic analysis |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for a sharp extremal bound on a Fourier coefficient of a nonnegative trigonometric polynomial under a vanishing Fourier-coefficient constraint. Its decisive structure is spectral factorization of positive trigonometric polynomials together with Fourier-coefficient optimization, which is part of Analysis / Harmonic analysis. Finite-dimensional Hermitian quadratic forms enter after factorization as the optimization certificate, so Linear Algebra is secondary.

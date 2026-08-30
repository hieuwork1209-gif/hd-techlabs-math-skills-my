# Normalized Math Problem

## LaTeX (Normalized)

For a $2\pi$-periodic trigonometric polynomial $g$, define its periodic Hilbert transform by
$$
\widehat{Hg}(k)=-i\,\operatorname{sgn}(k)\widehat g(k),
\qquad
\widehat g(k)=\frac1{2\pi}\int_0^{2\pi}g(x)e^{-ikx}\,dx,
$$
with $\operatorname{sgn}(0)=0$.

Let $f$ be a real trigonometric polynomial of degree at most $4$ such that
$$
\widehat f(0)=0,
\qquad
\frac1{2\pi}\int_0^{2\pi}f(x)^2\,dx=1,
$$
$$
f(0)=\frac8{\sqrt{981}},
\qquad
f\!\left(\frac\pi2\right)=-\frac{36}{\sqrt{981}}.
$$
Assume that, for every real $x$,
$$
981\bigl(H(f^2)(x)-f(x)Hf(x)\bigr)
=-1250\sin x+331\sin(2x)-30\sin(3x).
$$
Determine $f$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Fourier analysis |
| **Problem Type** | Construction under constraints |
| **Answer Type** | Function or mapping |

---

## Domain Explanation

The decisive structure comes from the periodic Hilbert transform as a Fourier multiplier. The nonlinear identity determines the modulus of the positive-frequency part of $f$, after which one must perform a finite spectral factorization of a reciprocal polynomial and use the point constraints to select the correct factor. This is fundamentally a Fourier-analysis problem rather than an algebraic factorization problem, because the spectral factorization arises only after the Hilbert-transform frequency decomposition.

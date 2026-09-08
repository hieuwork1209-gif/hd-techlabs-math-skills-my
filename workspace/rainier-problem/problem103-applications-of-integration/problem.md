# Normalized Math Problem

## LaTeX (Normalized)

For $n\ge1$, define
$$
I_n=\iint_{\mathbb R^2}
\exp\left(-n(x^2-y^3)^2-y^2\right)\,dx\,dy.
$$
Also let
$$
\Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\,dt
\qquad(s>0),
$$
and put
$$
C_0=
\frac{(3+\sqrt3)\Gamma(5/12)\Gamma(1/6)\Gamma(1/3)}{12\sqrt\pi}.
$$
Evaluate
$$
\lim_{n\to\infty}n^{1/2}
\left(
I_n-\frac{C_0}{n^{5/12}}
\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of integration |
| **Problem Type** | Exact computation |
| **Answer Type** | Real number |

---

## Domain Explanation

The curve $x^2=y^3$ is the semicubical discriminant cusp and, up to a constant factor, is the discriminant-zero locus of the depressed cubic $t^3-3yt+2x$. The leading Laplace term is created by the singular cusp, while the requested correction comes from the two regular discriminant branches. The Gaussian factor in $y$ makes the global integral finite without altering this local geometry, so this is a natural degenerate asymptotic-integration problem in Calculus -> Applications of integration.

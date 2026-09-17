# Normalized Math Problem

## LaTeX (Normalized)

For real numbers $a,b,c$, define the analytic trigonometric polynomial
$$
f_{a,b,c}(\theta)
=
a(1+e^{6i\theta})
+b(e^{i\theta}+e^{5i\theta})
+c(e^{2i\theta}+e^{4i\theta}).
$$
Assume the $L^2$ normalization
$$
\frac1{2\pi}\int_0^{2\pi}|f_{a,b,c}(\theta)|^2\,d\theta=1.
$$

Determine exactly
$$
M_*
=
\max_{a,b,c\in\mathbb R}
\frac1{2\pi}\int_0^{2\pi}|f_{a,b,c}(\theta)|^6\,d\theta,
$$
and determine all real triples $(a,b,c)$ attaining the maximum.

It is acceptable to specify algebraic constants as the unique real solution of an explicit polynomial system together with isolating inequalities.

Return the exact pair
$$
\bigl(M_*,\mathcal E_*\bigr),
$$
where $\mathcal E_*$ is the complete set of maximizing triples.

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Analysis |
| Sub-domain | Harmonic analysis |
| Problem Type | Optimization |
| Answer Type | Tuple or ordered list |

---

## Domain Explanation

The problem is an exact higher Fourier-moment extremal problem for a finite analytic trigonometric family. The essential structure comes from writing the $L^6$ norm as the $L^2$ norm of the triple convolution of the Fourier coefficients, then proving a global two-variable algebraic optimization and classifying all equality cases. Thus Analysis -> Harmonic analysis is primary, with elimination and root isolation serving as subordinate algebraic tools.

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
\frac1{2\pi}\int_0^{2\pi}|f_{a,b,c}(\theta)|^4\,d\theta,
$$
and determine all real triples $(a,b,c)$ attaining the maximum.

It is acceptable to specify an algebraic constant as the unique real root of an explicit polynomial together with an isolating interval.

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

The problem is an exact Fourier-norm extremal problem for a finite analytic trigonometric family. The essential structure comes from expressing the $L^4$ norm through the autocorrelation Fourier coefficients of $|f|^2$, then optimizing the resulting additive-energy functional under the $L^2$ normalization. Thus Analysis -> Harmonic analysis is primary, with algebraic optimization serving as the subordinate tool.

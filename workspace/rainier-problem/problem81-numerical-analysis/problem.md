# Normalized Math Problem

## LaTeX (Normalized)

Consider the one-parameter family of degree-$4$ stability polynomials
$$
R_a(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+az^4,
\qquad a\in\mathbb R.
$$
These are precisely the degree-$4$ polynomials satisfying the classical order-$3$ conditions at the origin.

For each $a$, define its negative-real-axis stability radius by
$$
L(a)
=
\sup\left\{L\ge0:
|R_a(x)|\le1
\text{ for every }x\in[-L,0]
\right\}.
$$
Let
$$
L_*=\sup_{a\in\mathbb R}L(a).
$$

Determine exactly the unique coefficient $a_*$ attaining $L_*$ and the exact value of $L_*$. Also determine the unique interior contact point $m_*>0$ for which
$$
R_{a_*}(-m_*)=-1,
\qquad
R_{a_*}'(-m_*)=0.
$$

It is acceptable to specify algebraic numbers as unique real roots of explicit polynomial equations together with isolating inequalities.

Return the exact tuple
$$
(a_*,L_*,m_*).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Optimization and Numerical Mathematics |
| Sub-domain | Numerical analysis |
| Problem Type | Optimization |
| Answer Type | Tuple or ordered list |

---

## Domain Explanation

The problem asks for the stability polynomial in a fixed order family that maximizes the interval of absolute stability on the negative real axis. The essential work is an exact stability-region optimization, including a sharp envelope argument, active stability contacts, and uniqueness of the maximizing coefficient. Thus Optimization and Numerical Mathematics -> Numerical analysis is primary.

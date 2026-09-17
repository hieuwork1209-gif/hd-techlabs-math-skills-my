# Normalized Math Problem

## LaTeX (Normalized)

Consider the two-parameter family of degree-$5$ stability polynomials
$$
R_{a,b}(z)
=1+z+\frac{z^2}{2}+\frac{z^3}{6}+az^4+bz^5,
\qquad a,b\in\mathbb R.
$$
These are precisely the degree-$5$ polynomials satisfying the classical order-$3$ conditions at the origin.

For each pair $(a,b)$, define its negative-real-axis stability radius by
$$
L(a,b)
=
\sup\left\{L\ge0:
|R_{a,b}(x)|\le1
\text{ for every }x\in[-L,0]
\right\}.
$$
Let
$$
L_*=\sup_{a,b\in\mathbb R}L(a,b).
$$

Determine exactly the unique optimizing pair
$$
(a_*,b_*),
$$
the exact maximal radius $L_*$, and the two unique interior contact points
$$
0<m_*<n_*<L_*
$$
for which
$$
R_{a_*,b_*}(-m_*)=-1,
\qquad
R_{a_*,b_*}'(-m_*)=0,
$$
$$
R_{a_*,b_*}(-n_*)=1,
\qquad
R_{a_*,b_*}'(-n_*)=0.
$$
Also verify that
$$
R_{a_*,b_*}(-L_*)=-1.
$$

It is acceptable to specify algebraic numbers as the unique real solution of an explicit polynomial system together with isolating inequalities.

Return the exact tuple
$$
(a_*,b_*,L_*,m_*,n_*).
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

The problem asks for the exact degree-$5$, order-$3$ stability polynomial maximizing the interval of absolute stability on the negative real axis. The essential work is a two-parameter semi-infinite stability optimization: one must convert the uniform constraint to an affine envelope problem, identify the active supporting contacts, and prove global optimality and uniqueness from the contact geometry. Thus Optimization and Numerical Mathematics -> Numerical analysis is primary.

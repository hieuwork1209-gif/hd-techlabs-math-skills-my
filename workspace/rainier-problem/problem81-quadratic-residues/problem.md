# Normalized Math Problem

## LaTeX (Normalized)

Let $p\equiv1\pmod8$ be a prime, and let
$$
\chi(x)=\left(\frac{x}{p}\right)
$$
be the Legendre symbol modulo $p$, extended by $\chi(0)=0$. Put
$$
\delta=\chi(3)=\left(\frac3p\right).
$$
By Fermat's two-square theorem, write
$$
p=u^2+v^2,
$$
where $u$ is odd, $v>0$ is even, and the sign of $u$ is chosen by
$$
u\equiv1\pmod4.
$$

Define $A(p)$ to be the number of $x\in\mathbb F_p$ for which
$$
\chi(x),\quad
\chi(x-1),\quad
\chi(x-3),\quad
\chi(x+3)
$$
are all equal to $+1$ or are all equal to $-1$.

Define $B(p)$ to be the number of $x\in\mathbb F_p$ for which, among these same four Legendre symbols, exactly two are $+1$ and exactly two are $-1$.

Determine exactly
$$
\bigl(A(p),B(p)\bigr)
$$
in terms of $p$, $\delta$, and the signed integer $u$ above.

Your derivation must evaluate, with the correct sign and twist,
$$
Q_p
=
\sum_{x\in\mathbb F_p}
\chi\bigl(x(x-1)(x-3)(x+3)\bigr).
$$
A derivation by transforming the genus-one quartic
$$
y^2=x(x-1)(x-3)(x+3)
$$
to an explicit quadratic twist of
$$
y^2=x^3-x
$$
is acceptable. Merely invoking a Hasse bound or quoting the absolute value of the trace is not sufficient.

Your count must also account explicitly for the four branch points
$$
x=0,1,3,-3.
$$

Return the exact pair
$$
\bigl(A(p),B(p)\bigr).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| Domain | Number Theory |
| Sub-domain | Quadratic residues and reciprocity |
| Problem Type | Exact computation |
| Answer Type | Tuple or ordered list |

---

## Domain Explanation

The problem asks for exact counts of simultaneous quadratic-residue sign patterns at four fixed shifts. The decisive step is a signed quartic quadratic-character sum whose genus-one curve has harmonic cross-ratio and is a quadratic twist of the CM curve $y^2=x^3-x$; after evaluating that trace, one must perform exact branch-point corrections. Thus Number Theory -> Quadratic residues and reciprocity is primary.

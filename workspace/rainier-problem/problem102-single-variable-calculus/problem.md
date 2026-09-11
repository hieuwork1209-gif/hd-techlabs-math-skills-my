# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. Let
$$
f:(1,\infty)\to[0,\infty),
$$
and define
$$
g(s)=f(e^s),\qquad s>0.
$$
Assume that $g\in C^1(0,\infty)$,
$$
g(1)=0,
$$
$$
g'(s)<0\quad(0<s<1),
\qquad
g'(s)>0\quad(s>1),
$$
and
$$
\lim_{s\to0^+}g(s)=\lim_{s\to\infty}g(s)=\infty.
$$
Suppose also that
$$
g(s)=g(1/s)
$$
for every $s>0$. For each $E>0$, let $a(E)\in(0,1)$ and $b(E)>1$ be the unique points satisfying
$$
g(a(E))=g(b(E))=E.
$$
Assume that, for every $E>0$,
$$
\int_{a(E)}^{b(E)}\frac{ds}{\sqrt{E-g(s)}}=\pi.
$$
Determine $f(x)$ for all $x>1$. For grading, write the final answer as $f(x)=\cdots$, use $\log x$, and keep the reciprocal of $\log x$ inside the squared parentheses.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Single-variable calculus |
| **Problem Type** | Solve for unknowns |
| **Answer Type** | Function or mapping |

---

## Domain Explanation

The logarithmic profile is an inversion-symmetric one-dimensional potential well with an energy-independent turning-point travel integral. Splitting the integral across the two monotone branches produces an Abel relation for the separation of the turning points. A second integration recovers that separation, while inversion symmetry determines the two branches individually. The problem uses one-variable integration, inverse functions, improper endpoint behavior, and symmetry.

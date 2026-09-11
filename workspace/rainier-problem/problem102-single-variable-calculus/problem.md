# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. Let
$$
f:(1,\infty)\to(0,1),
$$
and define
$$
g(s)=f(e^s),\qquad s>0.
$$
Assume that $g\in C^2(0,\infty)$, that $g'(s)<0$ for every $s>0$, and that
$$
\lim_{s\to0^+}g(s)=1,
\qquad
\lim_{s\to\infty}g(s)=0,
\qquad
g(1)=\frac14.
$$
Suppose there exists a constant $c>0$ such that, for every $s>0$,
$$
s^2g''(s)+(1+c)s g'(s)+g(s)(1-g(s))=0.
$$
Assume moreover that the finite positive limits
$$
\alpha=-\lim_{s\to0^+}\frac{s g'(s)}{1-g(s)},
\qquad
\beta=-\lim_{s\to\infty}\frac{s g'(s)}{g(s)}
$$
exist and satisfy
$$
\beta=2\alpha.
$$
Determine $f(x)$ for all $x>1$. For grading, write the final answer as $f(x)=\cdots$, use $\log x$, and leave the exponent $1/\sqrt6$ unchanged.

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

After logarithmic time $t=\log s$, the profile becomes a monotone Fisher-KPP traveling wave with an unknown speed. The two endpoint logarithmic rates satisfy the characteristic equations at the two equilibria, and their prescribed ratio selects the speed. At that speed the nonlinear wave equation admits a load-bearing first-order factorization; the value at $s=1$ fixes the remaining translation. The problem uses one-variable differential equations, asymptotic rates, phase-plane structure, and nonlinear factorization.

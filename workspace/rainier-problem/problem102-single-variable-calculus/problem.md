# Normalized Math Problem

## LaTeX (Normalized)

All logarithms are natural. Let $f:(1,\infty)\to\mathbb R$, and assume that all improper integrals below converge for every $x>1$. Suppose that the function $s\mapsto f(e^s)$ is concave on $(0,\infty)$. Define
$$
A(x)=\frac{1}{\log x}\int_1^x\frac{f(t)}{t}\,dt,
$$
$$
B(x)=\frac{2}{(\log x)^2}\int_1^x\log\!\left(\frac{x}{t}\right)\frac{f(t)}{t}\,dt,
$$
and
$$
C(x)=\frac{3}{(\log x)^3}\int_1^x\log^2\!\left(\frac{x}{t}\right)\frac{f(t)}{t}\,dt.
$$
Assume that
$$
\bigl(C(e)-2\bigr)^2=\frac14,
$$
$$
\lim_{x\to\infty}(\log x)^2\bigl(2-C(x)\bigr)^2=1,
$$
and, for every $x>1$,
$$
\bigl(2-3B(x)+2C(x)\bigr)^2
=
\bigl(2-C(x)\bigr)\bigl(2-3A(x)+3B(x)-C(x)\bigr).
$$
Determine $f(x)$ for all $x>1$. For grading, write the final answer as $f(x)=\cdots$ in unexpanded fraction notation: use $\frac{1}{(\cdots)^4}$ rather than a negative fourth power, write the logarithm as $\log x$, and do not expand or rearrange the denominator.

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

After the logarithmic change of variables, the three weighted means form a differential hierarchy. The global algebraic condition becomes a rank-one relation among three consecutive transformed quantities, which yields a nonlinear differential equation for their hidden ratio. The value at $e$ and the asymptotic condition determine the scale, while concavity selects the admissible sign. The problem is therefore governed by one-variable differentiation, integration, asymptotics, continuity, and concavity.

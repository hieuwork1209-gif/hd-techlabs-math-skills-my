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
and that, for every $x>1$,
$$
\bigl(2-3B(x)+2C(x)\bigr)^2=\bigl(2-C(x)\bigr)^4,
$$
$$
\bigl(2-3A(x)+3B(x)-C(x)\bigr)^2=\bigl(2-C(x)\bigr)^6.
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

After the logarithmic change of variables, the three weighted means form a differential hierarchy in one real variable. The nonlinear constraints determine algebraic sign branches of that hierarchy; a continuation argument rules out the singular branches, and concavity eliminates the remaining convex branch. The solution combines differentiation, integration, first-order differential relations, continuity, and concavity in one variable, so Single-variable calculus is the best-fit sub-domain.

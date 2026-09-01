# Normalized Math Problem

## LaTeX (Normalized)

For each integer $n\geq1$ and real $\lambda$, define
$$
I_n(\lambda)=\int_0^1 (2x-1)\exp\!\left(-n x^2(1-x)^2+\lambda(2x-1)\right)
\left(1+(2x-1)\exp\!\left(-\frac1{x(1-x)}\right)\right)\,dx,
$$
where the factor $\exp(-1/(x(1-x)))$ is interpreted as $0$ at $x=0,1$.
For each $n$, let $\lambda_n$ be the unique real number satisfying
$$
I_n(\lambda_n)=0.
$$
Determine the constants $c>0$ and $L\neq0$ such that
$$
\lim_{n\to\infty} e^{c n^{1/3}}\lambda_n=L.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Calculus |
| **Sub-domain** | Applications of integration |
| **Problem Type** | Exact computation |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem asks for the exponentially small displacement of an implicitly defined root of a definite integral. The symmetric endpoint contributions cancel to every algebraic order, so the decisive contribution comes from a flat perturbation whose dominant region moves toward the endpoints on a different scale. Determining that scale and evaluating the resulting saddle asymptotics are applications of integration and asymptotic evaluation of definite integrals, so Calculus -> Applications of integration is the best fit.

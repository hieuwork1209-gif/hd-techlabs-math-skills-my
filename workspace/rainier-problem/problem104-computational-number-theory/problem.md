# Normalized Math Problem

## LaTeX (Normalized)

Fix an integer $n\geq3$ and let
$$
R_n=\mathbb Z/55^n\mathbb Z.
$$
Define a sequence in $R_n$ by
$$
x_0=3,\qquad x_{k+1}=x_k^2-2\quad(k\geq0).
$$

Let $(\mu_n,\lambda_n)$ be the lexicographically least pair of integers with $\mu_n\geq0$ and $\lambda_n\geq1$ such that
$$
x_{k+\lambda_n}=x_k
$$
in $R_n$ for every $k\geq\mu_n$. Let $s_n$ be the unique integer satisfying
$$
0\leq s_n<55^n
$$
and
$$
s_n\equiv\sum_{j=0}^{\lambda_n-1}x_{\mu_n+j}\pmod{55^n}.
$$

Determine $(\mu_n,\lambda_n,s_n)$ in closed form.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Number Theory |
| **Sub-domain** | Computational number theory |
| **Problem Type** | Symbolic derivation |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem asks for the exact preperiod, period, and cycle sum of a quadratic recurrence modulo two prime powers. Its decisive work is the analysis of a ramified quadratic unit at $5$, a split quadratic unit at $11$, local order lifting, and Chinese remainder reconstruction, so Computational number theory is the primary sub-domain.

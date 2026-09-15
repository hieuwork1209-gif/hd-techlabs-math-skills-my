# Normalized Math Problem

## LaTeX (Normalized)

Let $X$ be a real-valued random variable supported on $[-1,1]$ such that its moments through degree $8$ agree with those of the uniform distribution on $[-1,1]$:
$$
\mathbb E[X^k]=\frac12\int_{-1}^1 t^k\,dt
\qquad(0\leq k\leq8).
$$
Determine exactly
$$
\max \mathbb P\left(X=\frac13\right),
$$
where the maximum is over all probability distributions satisfying these conditions. A complete proof must also classify all distributions attaining the maximum.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Random variables and distributions |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem is an extremal question about probability distributions determined by finitely many moments and a compact support constraint. The main work uses the moment identities together with positivity on $[-1,1]$ to construct a sharp polynomial certificate for an off-center atom, then reconstructs and proves uniqueness of the extremal discrete distribution through quadrature identities, so the primary classification is Probability and Statistics and Random variables and distributions. Polynomial norm minimization and interpolation are subordinate tools used to analyze the distributional moment problem.

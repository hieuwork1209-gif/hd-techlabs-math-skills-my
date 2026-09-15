# Normalized Math Problem

## LaTeX (Normalized)

Let $X$ be a real-valued random variable supported on $[-1,1]$ such that its moments through degree $8$ agree with those of the uniform distribution on $[-1,1]$:
$$
\mathbb E[X^k]=\frac12\int_{-1}^1 t^k\,dt
\qquad(0\leq k\leq8).
$$
Determine exactly
$$
\max \mathbb P(X=0),
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

The problem is an extremal question about probability distributions determined by finitely many moments. The main work uses the prescribed moments to construct a sharp polynomial bound for an atom, then reconstructs and verifies the unique extremal discrete distribution, so the primary classification is Probability and Statistics and Random variables and distributions. Real-analysis tools enter only through a finite-dimensional polynomial norm minimization and are subordinate to the distributional moment problem.

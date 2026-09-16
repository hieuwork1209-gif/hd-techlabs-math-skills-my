# Normalized Math Problem

## LaTeX (Normalized)

Let $(X_n)_{n\geq1}$ be an infinite exchangeable sequence of $\{0,1\}$-valued random variables satisfying
$$
\mathbb P(X_1=1)=\frac12,
$$
$$
\mathbb P(X_1=X_2=1)=\frac13,
$$
$$
\mathbb P(X_1=X_2=X_3=1)=\frac14.
$$
Determine exactly
$$
\max \mathbb P(X_1+X_2+X_3+X_4+X_5+X_6=2).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Probability foundations |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem is fundamentally about infinite exchangeability and its de Finetti mixing representation for Bernoulli sequences. The given joint probabilities become constraints on the first three moments of the latent mixing variable, and the target event becomes a degree-six Bernstein polynomial whose expectation must be optimized over all admissible mixing laws. The truncated moment optimization is the secondary mechanism used after the probabilistic representation is established.

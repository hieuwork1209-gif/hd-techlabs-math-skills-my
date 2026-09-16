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
Let
$$
E=\max \mathbb P\left(X_7=1\mid X_1+X_2+X_3+X_4+X_5+X_6=2\right),
$$
where the maximum ranges over all such exchangeable sequences. Determine the primitive irreducible polynomial $P(T)\in\mathbb Z[T]$ with positive leading coefficient such that
$$
P(E)=0.
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Probability foundations |
| **Problem Type** | Optimization |
| **Answer Type** | Polynomial or rational function |

---

## Domain Explanation

This problem is fundamentally about infinite exchangeability and de Finetti's mixing representation for Bernoulli sequences. The given joint probabilities fix the first three moments of the latent mixing variable, while the posterior predictive probability becomes a linear-fractional functional of its law. Proving the exact optimum requires a matching moment measure and polynomial dual certificate; algebraic elimination is secondary to the probabilistic extremal structure.

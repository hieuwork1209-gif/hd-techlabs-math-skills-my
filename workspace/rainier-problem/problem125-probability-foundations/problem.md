# Normalized Math Problem

## LaTeX (Normalized)

Let $X_1,\ldots,X_8$ be $\{0,1\}$-valued random variables with
$$
\mathbb P(X_i=1)=\frac12\qquad(1\le i\le8).
$$
Assume that for every $J\subseteq\{1,\ldots,8\}$ with $|J|\leq6$, the family $(X_j)_{j\in J}$ is mutually independent.

Determine exactly
$$
\max \mathbb P(X_1=X_2=\cdots=X_8=0),
$$
where the maximum is over all joint distributions satisfying these conditions. A complete proof must also classify all joint distributions attaining the maximum.

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

The problem asks for a sharp extremal atom probability under finite $6$-wise-independence constraints and for a classification of the extremal joint law. The decisive work converts independence into exact low-order sign-moment identities, uses positivity of point probabilities to obtain a sharp certificate, and reconstructs the unique maximizing law, so the primary classification is Probability and Statistics and Probability foundations. A secondary ingredient is Linear Algebra and Systems of linear equations, used only to solve the remaining moment constraints after the probabilistic reduction, so it is subordinate to the probability content.

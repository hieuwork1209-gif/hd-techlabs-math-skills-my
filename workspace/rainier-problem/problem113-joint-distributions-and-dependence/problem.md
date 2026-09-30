# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
X_1,\ldots,X_{10}\in\{0,1\}
$$
be exchangeable random variables such that
$$
\mathbb P(X_i=1)=\frac12
$$
for every $i$, and every subfamily of at most five coordinates is independent. Put
$$
S=X_1+\cdots+X_{10},
\qquad
p_s=\mathbb P(S=s)
\quad(0\leq s\leq10).
$$

Among all such joint laws, determine the distribution vector
$$
(p_0,p_1,\ldots,p_{10})
$$
of $S$ for which
$$
\mathbb P(S\in\{0,10\})
$$
is maximal.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Joint distributions and dependence |
| **Problem Type** | Optimization |
| **Answer Type** | Vector |

---

## Domain Explanation

This problem asks for an extremal exchangeable joint distribution under a limited-independence constraint. The main reasoning converts five-wise independence into moment constraints on the exchangeable sum, uses those constraints to certify the sharp probability bound, and reconstructs the unique maximizing dependence structure. Therefore Probability and Statistics / Joint distributions and dependence is the primary classification. Probability foundations is a close secondary fit, but the requested object is specifically an extremal joint law governed by dependence restrictions.

# Normalized Math Problem

## LaTeX (Normalized)

Let $Q=(Q_1,Q_2,Q_3)$ be a random probability vector, so $Q_i\geq0$ and $Q_1+Q_2+Q_3=1$. Conditional on $Q$, let $X_1,X_2,\ldots$ be independent random variables taking values in $\{1,2,3\}$ with
$$
\mathbb P(X_n=i\mid Q)=Q_i.
$$

Suppose
$$
\mathbb P(X_1=X_2)=\frac{1}{2}
$$
and
$$
\mathbb P(X_1=X_2=X_3)=\frac{11}{36}.
$$

Determine the exact interval of all possible values of
$$
\mathbb P(X_1=X_2=X_3=X_4=X_5).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Probability foundations |
| **Problem Type** | Optimization |
| **Answer Type** | Interval or region description |

---

## Domain Explanation

The problem asks for the sharp feasible range of a collision probability in a latent categorical mixture under lower-order collision constraints. The solution converts those probabilities to symmetric power sums of the latent probability vector and then solves a constrained extremal moment problem with sharp attainable certificates. Thus Probability and Statistics -> Probability foundations is primary.

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

Let
$$
K=|\{i:Q_i>0\}|.
$$
Determine the exact interval $I$ of all possible values of
$$
\mathbb P(X_1=X_2=X_3=X_4=X_5).
$$
Also determine the support-size law forced at each endpoint. Report the result as
$$
(I,k_-,(p_1,p_2,p_3)),
$$
where $k_-$ is the almost-sure value of $K$ for any law attaining the lower endpoint, and $p_k=\mathbb P(K=k)$ for any law attaining the upper endpoint.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Probability foundations |
| **Problem Type** | Optimization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem asks for a sharp feasible range of a collision probability in a latent categorical mixture and for the equality structure of the endpoint laws. The solution converts collision probabilities to symmetric power sums, proves sharp attainable extremal certificates, and then classifies the equality cases to recover the latent support-size profiles. Thus Probability and Statistics -> Probability foundations is primary.

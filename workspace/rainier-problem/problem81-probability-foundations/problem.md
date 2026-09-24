# Normalized Math Problem

## LaTeX (Normalized)

Let $Y_1,Y_2,\ldots$ be independent positive-integer-valued random variables with
$$
\mathbb P(Y_1=k)=\frac{1}{k(k+1)},
\qquad
k\geq1.
$$
Define the renewal times
$$
\tau_0=0,
\qquad
\tau_m=Y_1+\cdots+Y_m.
$$
For each $n$ with $n\in\{\tau_m:m\geq0\}$, let $K_n$ be the unique index such that $\tau_{K_n}=n$.

Let
$$
m_n=\mathbb E[K_n\mid n\in\{\tau_m:m\geq0\}],
$$
$$
v_n=\operatorname{Var}(K_n\mid n\in\{\tau_m:m\geq0\}),
$$
and let $\gamma$ denote Euler's constant.

Determine exactly
$$
\left(
\lim_{n\to\infty}
\log n
\left(
\frac{\log n}{n}m_n-1
\right),
\;
\lim_{n\to\infty}
\frac{(\log n)^3}{n^2}v_n
\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Probability foundations |
| **Problem Type** | Exact computation |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem concerns a renewal process with infinite mean inter-renewal time at the logarithmic boundary. The requested quantities require second-order conditional renewal asymptotics: the mean needs the first logarithmic correction, while the variance is determined only after cancellation of the leading conditional second-moment terms. Thus Probability and Statistics -> Probability foundations is primary.

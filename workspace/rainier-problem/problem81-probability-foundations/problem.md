# Normalized Math Problem

## LaTeX (Normalized)

A generalized Polya urn starts with $4$ red, $4$ green, and $4$ blue balls. At each step, one ball is chosen uniformly at random, returned to the urn, and additional balls are added according to the color drawn:

$$
\begin{array}{c|ccc}
\text{drawn color}&\text{red added}&\text{green added}&\text{blue added}\\
\hline
\text{red}&9&3&0\\
\text{green}&1&7&4\\
\text{blue}&2&2&8
\end{array}
$$

Let $(R_n,G_n,B_n)$ be the urn composition after $n$ draws.

Determine exactly
$$
\lim_{n\to\infty}
\mathbb P\left(
R_n>G_n
\text{ and }
R_n+G_n>2B_n
\right).
$$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Probability and Statistics |
| **Sub-domain** | Probability foundations |
| **Problem Type** | Exact computation |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for a limiting joint-sign probability in a critical balanced generalized Polya urn. The defective half-Perron Jordan block creates two coupled fluctuation scales, and the target probability depends on their joint Gaussian limit rather than on covariance magnitudes alone. Thus Probability and Statistics -> Probability foundations is primary.

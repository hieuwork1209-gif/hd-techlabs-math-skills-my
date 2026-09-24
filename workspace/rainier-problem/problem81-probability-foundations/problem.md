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

Let
$$
X_n=(R_n,G_n,B_n)
$$
be the urn composition after $n$ draws, and let $\Sigma_n$ be the covariance matrix of $X_n$. Since the total number of balls is deterministic, $\Sigma_n$ has one zero eigenvalue. Let
$$
0<\lambda_n^-\leq\lambda_n^+
$$
be its other two eigenvalues.

Determine exactly
$$
\left(
\lim_{n\to\infty}\frac{\lambda_n^-}{n\log n},
\;
\lim_{n\to\infty}\frac{\lambda_n^+}{n(\log n)^3}
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

The problem asks for critical covariance asymptotics of a balanced generalized Polya urn. The replacement matrix has a nontrivial Jordan chain at half the Perron eigenvalue, which creates nested logarithmic fluctuation scales and a nontrivial interaction between the two covariance modes. Thus Probability and Statistics -> Probability foundations is primary.

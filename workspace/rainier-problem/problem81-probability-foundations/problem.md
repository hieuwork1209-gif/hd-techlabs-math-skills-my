# Normalized Math Problem

## LaTeX (Normalized)

Let $U$ be the uniform probability measure on $\{-1,1\}^{12}$. For $x=(x_1,\ldots,x_{12})$, define
$$
S(x)=\sum_{i=1}^{12}x_i,
\qquad
R(x)=\prod_{i=1}^{12}x_i.
$$
Let $\mu$ range over all laws of random variables $X_1,\ldots,X_{12}\in\{-1,1\}$ that are unbiased and $8$-wise independent. Let $\bar\mu$ denote the permutation symmetrization of $\mu$, obtained by averaging $\mu$ over all permutations of the twelve coordinates.

Determine the ordered pair consisting of:

1. the largest possible value of $\mu(S=0)$;
2. the Radon-Nikodym density $d\bar\mu/dU$ shared by the permutation symmetrizations of all maximizing laws.

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

The problem asks for a sharp extremal probability under finite-wise independence constraints and then for the equality-case structure after permutation symmetrization. The proof must combine low-order moment constraints with an extremal construction, a sharp polynomial certificate, and uniqueness of the exchangeable optimizer. Thus Probability and Statistics -> Probability foundations is the direct classification.

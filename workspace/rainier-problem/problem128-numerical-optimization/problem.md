# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
H=
\begin{pmatrix}
2&1&0\\
1&2&1\\
0&1&2
\end{pmatrix},
\qquad
f(x)=\frac{1}{2}x^THx.
$$
At the start of one epoch, choose a permutation
$$
\pi=(\pi_1,\pi_2,\pi_3)
$$
of $\{1,2,3\}$ according to an arbitrary probability distribution $\nu$ on the six permutations. Then perform exact coordinate minimization in the order $\pi_1,\pi_2,\pi_3$:
$$
x^+=x-\frac{e_i^THx}{H_{ii}}e_i
$$
when coordinate $i$ is selected.

Define the worst-case expected one-epoch energy ratio
$$
\rho(\nu)=
\sup_{x_0\neq0}
\frac{\mathbb E_\nu[f(x_3)]}{f(x_0)}.
$$
Determine
$$
\inf_\nu \rho(\nu)
$$
exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

The problem asks for the best probability law for random reshuffling in exact coordinate descent on a quadratic objective, measured by the worst-case expected energy reduction over one full epoch. The main task is to optimize a randomized coordinate-update strategy for an iterative optimization method, so the primary sub-domain is Numerical optimization.

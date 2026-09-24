# Normalized Math Problem

## LaTeX (Normalized)

For $n\geq3$, let $W_n$ be the wheel graph with rim cycle
$$
v_0v_1\cdots v_{n-1}v_0
$$
and hub $h$ adjacent to every rim vertex.

Let $Q_n$ be the reduced Laplacian obtained by deleting the row and column of $h$ from the Laplacian of $W_n$. The critical group of $W_n$ is
$$
K(W_n)=\mathbb Z^n/Q_n\mathbb Z^n.
$$

Let the Fibonacci and Lucas sequences be defined by
$$
F_0=0,\quad F_1=1,\quad F_{j+1}=F_j+F_{j-1},
$$
$$
L_0=2,\quad L_1=1,\quad L_{j+1}=L_j+L_{j-1}.
$$

Determine the non-unit invariant factors of the Smith normal form of $Q_n$, listed in divisibility order as an ordered tuple.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Discrete Mathematics and Combinatorics |
| **Sub-domain** | Graph theory |
| **Problem Type** | Canonicalization or normalization |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The requested object is the non-unit Smith invariant factors of the reduced Laplacian of a wheel graph, equivalently the canonical decomposition of its critical group. The solution must compress the cyclic integer presentation and determine its invariant factors through a Fibonacci transfer recurrence.

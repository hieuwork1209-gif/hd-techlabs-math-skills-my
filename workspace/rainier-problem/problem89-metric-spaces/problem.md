# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
X=\operatorname{Sym}_3(\mathbb F_3)
$$
be the set of symmetric $3\times3$ matrices over $\mathbb F_3$. Let $G$ be the graph on $X$ in which distinct matrices $A,B$ are adjacent exactly when
$$
\operatorname{rank}(A-B)=1.
$$
Let $d$ be the shortest-path metric on $G$.

For $p>0$, say that $(X,d)$ has $p$-negative type if every real family $(c_A)_{A\in X}$ with $\sum_Ac_A=0$ satisfies
$$
\sum_{A,B\in X}c_Ac_B\,d(A,B)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(X,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^X:\sum_Ac_A=0,\ \sum_{A,B}c_Ac_B\,d(A,B)^{\wp}=0\right\}.
$$
Determine the ordered pair $(\wp,\dim E)$.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Analysis |
| **Sub-domain** | Metric spaces |
| **Problem Type** | Exact computation |
| **Answer Type** | Tuple or ordered list |

---

## Domain Explanation

The problem asks for the maximal negative-type exponent of a natural finite metric induced by rank-one moves on symmetric matrices, together with the dimension of the boundary equality space.

# Normalized Math Problem

## LaTeX (Normalized)

Let $m\ge3$, and let $P_m=[2]\times[m]$ be the product poset, so
$$
(r,i)\le(s,j)
$$
exactly when $r\le s$ and $i\le j$.

Let $\mathcal L_m$ be the graph whose vertices are the linear extensions of $P_m$, with two vertices adjacent exactly when one is obtained from the other by swapping two consecutive incomparable elements. Let $d$ be the shortest-path metric on $\mathcal L_m$.

For $p>0$, say that $(\mathcal L_m,d)$ has $p$-negative type if every real family $(c_L)$ with $\sum_Lc_L=0$ satisfies
$$
\sum_{L,L'}c_Lc_{L'}\,d(L,L')^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(\mathcal L_m,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^{\mathcal L_m}:\sum_Lc_L=0,\ \sum_{L,L'}c_Lc_{L'}\,d(L,L')^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of a natural linear-extension graph metric and the dimension of its boundary equality space. The key structure is a hidden Hamming representation by the relative orders of incomparable pairs, together with the Catalan enumeration of the extensions of the $2\times m$ grid poset.

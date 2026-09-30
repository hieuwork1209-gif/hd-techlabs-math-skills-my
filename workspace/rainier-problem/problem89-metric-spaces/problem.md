# Normalized Math Problem

## LaTeX (Normalized)

Let $[7]=\{1,2,3,4,5,6,7\}$ and
$$
X=\binom{[7]}{2}.
$$
Give $X$ the shortest-path metric $d$ of the Kneser graph $KG(7,2)$: two distinct vertices $A,B\in X$ are adjacent exactly when $A\cap B=\varnothing$.

For $p>0$, say that $(X,d)$ has $p$-negative type if every real family $(c_A)_{A\in X}$ with $\sum_A c_A=0$ satisfies
$$
\sum_{A,B\in X}c_Ac_B d(A,B)^p\leq0.
$$
Let
$$
\wp=\sup\{p>0:(X,d)\text{ has }p\text{-negative type}\},
$$
and define
$$
E=\left\{c\in\mathbb R^X:\sum_A c_A=0,\ \sum_{A,B}c_Ac_B d(A,B)^{\wp}=0\right\}.
$$

For $L\leq E$, write
$$
\operatorname{supp}(L)=\{A\in X:\text{some }c\in L\text{ has }c_A\neq0\}.
$$
For $1\leq r\leq\dim E$, define
$$
d_r=\min_{\substack{L\leq E\\ \dim L=r}}|\operatorname{supp}(L)|.
$$
Determine
$$
\left(\wp,\dim E,(d_1,\ldots,d_{\dim E})\right).
$$

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

The primary object is a finite shortest-path metric, and the problem asks for its supremal negative type and the support profile of the equality space at the critical exponent, so Analysis / Metric spaces is the natural primary classification. Spectral graph methods and finite-dimensional linear algebra are secondary tools; an extremal graph argument determines the support profile.

# Normalized Math Problem

## LaTeX (Normalized)

Let $X$ be the set of complete flags
$$
0<V_1<V_2<V_3<\mathbb{F}_2^4,
\qquad \dim V_i=i.
$$
Form a graph $G$ on $X$ by joining two flags exactly when they differ in one of the three subspaces $V_1,V_2,V_3$. Let $d$ be the shortest-path metric on $G$.

For $p>0$, say that $(X,d)$ has $p$-negative type if every real family $(c_F)_{F\in X}$ with $\sum_Fc_F=0$ satisfies
$$
\sum_{F,H\in X}c_Fc_H\,d(F,H)^p\leq0.
$$
Let
$$
\wp=\sup\{p>0:(X,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb{R}^X:\sum_Fc_F=0,\ \sum_{F,H}c_Fc_H\,d(F,H)^{\wp}=0\right\}.
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

This problem involves the supremal negative type and boundary equality space of a finite graph metric, which are part of Analysis and Metric spaces. The problem also involves complete flags and finite building incidence, which are part of abstract algebra and finite geometry. However, those structures are used to analyze the metric kernel, while the requested quantity is a metric-space invariant.

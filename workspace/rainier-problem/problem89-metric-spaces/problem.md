# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
H=\mathbb F_3^3
$$
with group law
$$
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+xy').
$$
Put
$$
a=(1,0,0),\qquad b=(0,1,0),\qquad c=(0,0,1),
$$
and let $G$ be the Cayley graph of $H$ with generating set
$$
\{a^{\pm1},b^{\pm1},c^{\pm1}\}.
$$
Let $d$ be the shortest-path metric on $G$.

For $p>0$, say that $(H,d)$ has $p$-negative type if every real family $(c_g)_{g\in H}$ with $\sum_gc_g=0$ satisfies
$$
\sum_{g,h\in H}c_gc_h\,d(g,h)^p\le0.
$$
Let
$$
\wp=\sup\{p>0:(H,d)\text{ has }p\text{-negative type}\}.
$$
At $p=\wp$, define the equality space
$$
E=\left\{c\in\mathbb R^H:\sum_gc_g=0,\ \sum_{g,h}c_gc_h\,d(g,h)^{\wp}=0\right\}.
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

The problem asks for the maximal negative-type exponent of a natural finite word metric on the Heisenberg group over $\mathbb F_3$, together with the dimension of its boundary equality space.

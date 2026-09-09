## Steps

Step 1: Express the average contraction as a discrete polynomial norm
Let
$$
A=\operatorname{diag}(1,2,3,4,5,6,7).
$$
After three gradient steps,
$$
x_3=p(A)x_0,
\qquad
p(\lambda)=\prod_{k=0}^2(1-\alpha_k\lambda),
$$
so $p$ has degree at most $3$ and satisfies $p(0)=1$.

If $x_0$ is uniform on the unit sphere in $\mathbb R^7$, symmetry gives
$$
\mathbb E[x_{0,j}^2]=\frac17,
\qquad j=1,\dots,7,
$$
because the seven expectations are equal and $\sum_jx_{0,j}^2=1$. Therefore
$$
\mathbb E\|x_3\|_2^2
=\frac17\sum_{j=1}^7p(j)^2.
$$
Thus it is enough to minimize this discrete squared norm over cubic polynomials with $p(0)=1$, provided the minimizing cubic has positive roots.

Step 2: Prove the sharp lower bound by a discrete evaluation certificate
Set
$$
(w_1,\dots,w_7)
=\frac17(16,-4,-8,-3,4,6,-4).
$$
Directly,
$$
\sum_{j=1}^7w_j=1,
\qquad
\sum_{j=1}^7j^mw_j=0
\quad(m=1,2,3).
$$
Hence every polynomial $q$ of degree at most $3$ satisfies
$$
q(0)=\sum_{j=1}^7w_jq(j).
$$
For any admissible residual polynomial $q$ with $q(0)=1$, Cauchy--Schwarz gives
$$
1
\le
\left(\sum_{j=1}^7w_j^2\right)
\left(\sum_{j=1}^7q(j)^2\right).
$$
Since
$$
\sum_{j=1}^7w_j^2
=\frac{59}{7},
$$
we obtain
$$
\frac17\sum_{j=1}^7q(j)^2\ge\frac1{59}.
$$
Therefore $R_*\ge1/59$.

Step 3: Attain the bound with a realizable three-step residual
Consider
$$
p_*(\lambda)
=\frac{354-341\lambda+90\lambda^2-7\lambda^3}{354}.
$$
Its values at the seven eigenvalues are
$$
\bigl(p_*(1),\dots,p_*(7)\bigr)
=\frac1{59}(16,-4,-8,-3,4,6,-4).
$$
Hence
$$
\frac17\sum_{j=1}^7p_*(j)^2
=\frac1{59},
$$
so the lower bound is attained at the polynomial level.

It remains to check that $p_*$ comes from three positive gradient step sizes. The displayed values give
$$
p_*(1)>0>p_*(2),
$$
$$
p_*(4)<0<p_*(5),
$$
$$
p_*(6)>0>p_*(7).
$$
Thus $p_*$ has one root in each of $(1,2)$, $(4,5)$, and $(6,7)$. Since it is cubic, these are exactly its three roots, all positive. Writing them as $r_1,r_2,r_3>0$ gives
$$
p_*(\lambda)=\prod_{i=1}^3\left(1-\frac{\lambda}{r_i}\right),
$$
so choosing the three step sizes $\alpha_i=1/r_i$ realizes $p_*$. Consequently the minimum average squared contraction is $1/59$.

Final Answer: $\boxed{\frac1{59}}$

---

## Answer

$\frac1{59}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Number

---

## Solution Concepts

- average-case gradient descent tuning
- discrete polynomial norm
- Cauchy--Schwarz evaluation certificate

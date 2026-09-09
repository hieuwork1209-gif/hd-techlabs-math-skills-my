## Steps

Step 1: Reduce the three steps to a residual polynomial
Let
$$
p(\lambda)=\prod_{k=0}^2(1-\alpha_k\lambda).
$$
For a symmetric positive-definite matrix $A$ with spectrum in $[1,9]$,
$$
x_3=p(A)x_0,
$$
so the worst-case Euclidean contraction is
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\max_{1\le\lambda\le9}|p(\lambda)|.
$$
The per-step nonexpansiveness restriction is
$$
0<\alpha_k\le\frac29.
$$

Step 2: Obtain a sharp lower bound from the stability constraint
Set
$$
z_k=1-9\alpha_k,
$$
so $-1\le z_k<1$. Then
$$
p(1)=\prod_{k=0}^2\frac{8+z_k}{9},
\qquad
p(9)=\prod_{k=0}^2z_k.
$$
Put $x_k=|z_k|\in[0,1]$ and
$$
u=x_0x_1x_2.
$$
Since $8+z_k\ge8-x_k$,
$$
p(1)\ge\frac{\prod_{k=0}^2(8-x_k)}{9^3}.
$$
For $x,y\in[0,1]$,
$$
(8-x)(8-y)-7(8-xy)=8(1-x)(1-y)\ge0.
$$
Applying this inequality twice gives
$$
\prod_{k=0}^2(8-x_k)\ge49(8-u).
$$
Therefore every admissible schedule satisfies
$$
R\ge\max\left\{\frac{49(8-u)}{729},u\right\}.
$$
The first quantity decreases in $u$ and the second increases, so their maximum is minimized when they are equal:
$$
\frac{49(8-u)}{729}=u.
$$
Hence
$$
u=\frac{196}{389},
$$
and consequently
$$
R\ge\frac{196}{389}.
$$

Step 3: Construct an admissible schedule attaining the bound
Take the ordered step sizes
$$
\alpha_0=\frac{65}{389},
\qquad
\alpha_1=\alpha_2=\frac29.
$$
They satisfy
$$
0<\alpha_0\le\alpha_1\le\alpha_2\le\frac29.
$$
The residual is
$$
p_*(\lambda)
=\left(1-\frac{65}{389}\lambda\right)
\left(1-\frac{2}{9}\lambda\right)^2.
$$
At the endpoints,
$$
p_*(1)=\frac{196}{389},
\qquad
p_*(9)=-\frac{196}{389}.
$$
On $[1,9/2]$, both factors are nonnegative and
$$
p_*'(\lambda)
=-\left(1-\frac{2\lambda}{9}\right)
\frac{2141-390\lambda}{3501}\le0,
$$
so $p_*$ decreases from $196/389$ to $0$.
On $[9/2,6]$,
$$
\left|1-\frac{2\lambda}{9}\right|\le\frac13,
\qquad
\left|1-\frac{65\lambda}{389}\right|<\frac14,
$$
so
$$
|p_*(\lambda)|<\frac1{36}<\frac{196}{389}.
$$
Finally, on $[6,9]$ both factors give $p_*(\lambda)\le0$, and the derivative formula above shows $p_*'(\lambda)<0$, so $p_*$ decreases to $-196/389$. Thus
$$
\max_{1\le\lambda\le9}|p_*(\lambda)|=\frac{196}{389}.
$$
Therefore the lower bound is attained.

Final Answer: $\boxed{\left(\frac{196}{389},\left(\frac{65}{389},\frac29,\frac29\right)\right)}$

---

## Answer

$\left(\frac{196}{389},\left(\frac{65}{389},\frac29,\frac29\right)\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- nonstationary gradient descent
- per-step spectral stability
- constrained residual polynomial

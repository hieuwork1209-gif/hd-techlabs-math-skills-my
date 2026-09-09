## Steps

Step 1: Reduce the average contraction to three residual values
Let
$$
p(\lambda)=\prod_{k=0}^2(1-\alpha_k\lambda).
$$
Since
$$
A=\operatorname{diag}(1,2,4),
$$
after three gradient steps we have
$$
x_3=p(A)x_0.
$$
For $x_0$ uniform on the unit sphere in $\mathbb R^3$, symmetry gives
$$
\mathbb E[x_{0,j}^2]=\frac13,
\qquad j=1,2,3.
$$
Therefore
$$
R(\alpha_0,\alpha_1,\alpha_2)
=\frac13\bigl(p(1)^2+p(2)^2+p(4)^2\bigr).
$$

Step 2: Use the stability restriction to obtain a sharp lower bound
Set
$$
q(s)=p(2-s).
$$
For each step,
$$
1-\alpha_k(2-s)=(1-2\alpha_k)+\alpha_k s.
$$
Because $0<\alpha_k\le1/2$, both coefficients are nonnegative. Hence
$$
q(s)=c_0+c_1s+c_2s^2+c_3s^3
$$
with
$$
c_0,c_1,c_2,c_3\ge0.
$$
Also
$$
q(2)=p(0)=1.
$$
The three spectral points $1,2,4$ correspond to $s=1,0,-2$, so
$$
3R=q(1)^2+q(0)^2+q(-2)^2.
$$

Expanding in the nonnegative coefficients gives the identity
$$
16q(1)-q(-2)-3q(2)=12(c_0+c_1)\ge0.
$$
Since $q(2)=1$,
$$
16q(1)-q(-2)\ge3.
$$
By Cauchy--Schwarz,
$$
\bigl(16q(1)-q(-2)\bigr)^2
\le(16^2+1)\bigl(q(1)^2+q(-2)^2\bigr)
\le257\cdot3R.
$$
Thus
$$
9\le771R,
$$
so every admissible schedule satisfies
$$
R\ge\frac3{257}.
$$

Step 3: Construct a schedule attaining the bound
Take, in any order,
$$
\alpha_0=\frac12,
\qquad
\alpha_1=\frac12,
\qquad
\alpha_2=\frac{65}{257}.
$$
All three step sizes obey the stability restriction. The residual polynomial is
$$
p_*(\lambda)
=\left(1-\frac\lambda2\right)^2
\left(1-\frac{65}{257}\lambda\right).
$$
Equivalently,
$$
q_*(s)=p_*(2-s)
=\frac{s^2(127+65s)}{1028}.
$$
Hence
$$
q_*(1)=\frac{48}{257},
\qquad
q_*(0)=0,
\qquad
q_*(-2)=-\frac3{257}.
$$
Therefore
$$
R
=\frac13\left[
\left(\frac{48}{257}\right)^2
+\left(\frac3{257}\right)^2
\right]
=\frac3{257}.
$$
This attains the lower bound from Step 2.

Final Answer: $\boxed{\frac3{257}}$

---

## Answer

$\frac3{257}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Number

---

## Solution Concepts

- stable nonstationary gradient descent
- residual polynomial with nonnegative shifted coefficients
- Cauchy--Schwarz contraction certificate

## Steps

Step 1: Convert the nonnegative trigonometric polynomial into a finite quadratic problem
Write
$$
T(\theta)=1+2a\cos\theta+2\sum_{k=3}^{6}a_k\cos(k\theta).
$$
The Fejer-Riesz factorization theorem in the needed form says that every real trigonometric polynomial of degree at most $6$ that is nonnegative for every real $\theta$ can be written as
$$
T(\theta)=|P(e^{i\theta})|^2,
\qquad
P(z)=\sum_{j=0}^{6}c_jz^j
$$
for some complex coefficients $c_0,\ldots,c_6$.

Expanding $|P(e^{i\theta})|^2$, its nonnegative Fourier coefficients are
$$
t_k=\sum_{j=0}^{6-k}c_{j+k}\overline{c_j}\qquad(0\leq k\leq6).
$$
Because $T$ is real and even, these coefficients are real. Hence
$$
\sum_{j=0}^{6}|c_j|^2=t_0=1,
$$
$$
\operatorname{Re}\sum_{j=0}^{5}c_{j+1}\overline{c_j}=t_1=a,
$$
and the missing second Fourier coefficient gives
$$
\operatorname{Re}\sum_{j=0}^{4}c_{j+2}\overline{c_j}=t_2=0.
$$
Let $A,B$ be the real symmetric $7\times7$ matrices with
$$
A_{j,j+1}=A_{j+1,j}=\frac12,
\qquad
B_{j,j+2}=B_{j+2,j}=\frac12,
$$
and all other entries zero. For the column vector $c=(c_0,\ldots,c_6)^T$, the problem is therefore
$$
c^*c=1,\qquad c^*Bc=0,\qquad a=c^*Ac.
$$

Step 2: Use reversal symmetry to derive a sharp candidate
The Lagrange-stationarity matrices for the quadratic problem in Step 1 have the form $A-uB$. Both $A$ and $B$ commute with coordinate reversal, so the natural invariant sectors of every such stationarity matrix are the reversal-even and reversal-odd subspaces. To generate a candidate, examine the odd sector
$$
c=(x,y,z,0,-z,-y,-x)^T.
$$
There the missing-frequency constraint becomes
$$
c^*Bc=2xz-z^2=z(2x-z).
$$
If $z=0$, then $2x^2+2y^2=1$ and $c^*Ac=2xy\leq1/2$. The nonzero branch is $z=2x$. On that branch,
$$
c^*c=10x^2+2y^2,
\qquad
c^*Ac=6xy.
$$
Put $X=\sqrt{10}x$ and $Y=\sqrt2y$. Then $X^2+Y^2=1$ and
$$
6xy=\frac{6}{\sqrt{20}}XY\leq\frac{3}{\sqrt{20}}.
$$
Equality occurs when $X=Y>0$, which gives
$$
x=\frac1{\sqrt{20}},\qquad y=\frac12,\qquad z=\frac1{\sqrt5}.
$$
Thus the normalized candidate is
$$
c_*=\frac1{\sqrt{20}}(1,\sqrt5,2,0,-2,-\sqrt5,-1)^T
$$
and it attains
$$
c_*^*Ac_*=\frac{3}{\sqrt{20}}.
$$

Step 3: Derive and verify a global positive-semidefinite certificate
Set
$$
m=\frac{3}{\sqrt{20}}=\frac{3}{2\sqrt5}.
$$
A Lagrange-dual certificate for the upper bound $a\leq m$ has the form
$$
M=mI-A+uB,
$$
because $M\succeq0$ would imply $m-a=c^*Mc$ for every feasible $c$. To make such a certificate sharp at the candidate from Step 2, require $Mc_*=0$. Using the unnormalized vector
$$
v=(1,\sqrt5,2,0,-2,-\sqrt5,-1)^T,
$$
the first two coordinates of $(mI-A+uB)v=0$ are
$$
m-\frac{\sqrt5}{2}+u=0,
\qquad
m\sqrt5-\frac32=0.
$$
The second identity holds for the displayed $m$, and the first forces
$$
u=\frac1{\sqrt5}.
$$
So it remains only to verify that
$$
D:=2\sqrt5M=3I-2\sqrt5A+2B
$$
is positive semidefinite. For every $q=(q_0,\ldots,q_6)^T\in\mathbb{C}^7$, expanding the right-hand side gives the exact identity
$$
\begin{aligned}
q^*Dq={}&3\left|q_0-\frac{\sqrt5}{3}q_1+\frac13q_2\right|^2
+\frac43\left|q_1-\frac{\sqrt5}{2}q_2+\frac34q_3\right|^2\\
&+\left|q_2-\frac{\sqrt5}{2}q_3+q_4\right|^2
+\left|q_3-\frac{\sqrt5}{2}q_4+q_5\right|^2\\
&+\frac34\left|q_4-\frac{2\sqrt5}{3}q_5+\frac43q_6\right|^2
+\frac13\left|q_5-\sqrt5q_6\right|^2.
\end{aligned}
$$
Thus $D\succeq0$, hence $M\succeq0$. For every feasible factor vector $c$ from Step 1,
$$
m-a=c^*(mI-A+uB)c=c^*Mc\geq0.
$$
Therefore
$$
a\leq\frac{3}{\sqrt{20}}.
$$

Step 4: Realize equality by an explicit spectral factor
Take
$$
P_*(z)=\frac{1+\sqrt5z+2z^2-2z^4-\sqrt5z^5-z^6}{\sqrt{20}}
$$
and set
$$
T_*(\theta)=|P_*(e^{i\theta})|^2.
$$
This is a real nonnegative trigonometric polynomial of degree at most $6$. Its constant Fourier coefficient is $c_*^*c_*=1$, its second Fourier coefficient is $c_*^*Bc_*=0$, and its first Fourier coefficient is
$$
c_*^*Ac_*=\frac{3}{\sqrt{20}}.
$$
Hence the upper bound from Step 3 is attained.

Final Answer: $\boxed{\frac{3}{\sqrt{20}}}$

---

## Answer

$\frac{3}{\sqrt{20}}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- Fejer-Riesz factorization
- Fourier coefficients
- quadratic-form dual certificate
- positive semidefinite matrices
- equality case analysis

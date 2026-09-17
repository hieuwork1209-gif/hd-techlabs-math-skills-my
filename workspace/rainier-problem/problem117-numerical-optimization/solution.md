## Steps

Step 1: A self-contained uniqueness criterion for this trust-region family
For a symmetric matrix $A$ with simple eigenvalues $\lambda_1<\cdots<\lambda_n$ and an orthonormal eigenbasis $u_i$, write $c_i=u_i^Tb$. Assume $\lambda_1<0$. If $c_1\ne0$, then
$$
h(\mu)=\sum_{i=1}^n\frac{c_i^2}{(\lambda_i+\mu)^2},\qquad \mu> -\lambda_1,
$$
is strictly decreasing, tends to $+\infty$ as $\mu\downarrow-\lambda_1$, and tends to $0$ as $\mu\to\infty$. Hence there is a unique $\mu> -\lambda_1$ with $h(\mu)=1$. Define
$$
x=-\sum_{i=1}^n\frac{c_i}{\lambda_i+\mu}u_i.
$$
Then $\|x\|=1$, $(A+\mu I)x=-b$, and $A+\mu I\succ0$. For every $y$ with $\|y\|\le1$,
$$
q(y)-q(x)
=\frac12(y-x)^T(A+\mu I)(y-x)
+\frac\mu2(1-\|y\|^2)\ge0. \tag{1}
$$
Both terms can vanish only at $y=x$, so the global minimizer is unique.

For our matrix $A_\tau$, every eigenspace is one-dimensional: once the first component of an eigenvector is fixed, the tridiagonal recurrence with nonzero off-diagonal entries determines all later components, while first component $0$ forces the zero vector. Since $A_\tau$ is symmetric, all eigenvalues are simple. Also
$$
\lambda_1(A_\tau)\le e_1^TA_\tau e_1=-3<0.
$$
Therefore it is enough to find the parameters for which $b$ is orthogonal to the lowest eigenvector. At every other parameter, (1) gives uniqueness.

Step 2: Orthogonality forces one cubic parameter equation
Let $v=(v_1,v_2,v_3,v_4)^T$ be an eigenvector of $A_\tau$ with eigenvalue $\lambda$ and suppose
$$
b^Tv=v_2+v_3+v_4=0.
$$
Because $\lambda_1<-3$, the lowest eigenvalue is not $4$. From the fourth eigenvector equation,
$$
v_3+(4-\lambda)v_4=0,
$$
so $v_4\ne0$ and
$$
v_3=(\lambda-4)v_4,
\qquad
v_2=(3-\lambda)v_4.
$$
Substitute these into the third eigenvector equation:
$$
v_2+(\tau-\lambda)v_3+v_4=0.
$$
After factoring,
$$
(4-\lambda)(1-\tau+\lambda)=0.
$$
Hence
$$
\lambda=\tau-1. \tag{2}
$$
Now set $v_4=1$. Then
$$
v_3=\tau-5,\qquad v_2=4-\tau.
$$
The first equation gives
$$
v_1=\frac{4-\tau}{\tau+2},
$$
and the second equation becomes
$$
\frac{\tau^3-2\tau^2-10\tau+2}{\tau+2}=0.
$$
Thus any eigenvector orthogonal to $b$ in the stated interval forces
$$
P(\tau):=\tau^3-2\tau^2-10\tau+2=0. \tag{3}
$$
On $[-5/2,-17/7]$,
$$
P'(	au)=3\tau^2-4\tau-10>0,
$$
while
$$
P(-5/2)=-\frac98<0,
\qquad
P(-17/7)=\frac{57}{343}>0.
$$
Therefore there is exactly one root
$$
\tau_* = \operatorname{root}_{(-5/2,-17/7)}(P). \tag{4}
$$
For every $\tau\ne\tau_*$ in the interval, $b$ is not orthogonal to any eigenvector, hence in particular not to the lowest one; Step 1 proves that the trust-region minimizer is unique.

Step 3: At the cubic root the orthogonal eigenvector is the lowest one
Put $r=\tau_*$ and consider
$$
M=A_r-(r-1)I.
$$
Its leading principal determinants are
$$
D_1=-r-2,\qquad
D_2=r^2+r-3,\qquad
D_3=r^2+2r-1,\qquad
D_4=-P(r)=0.
$$
Throughout $[-5/2,-17/7]$, the first three displayed quantities are positive. Hence the $LDL^T$ pivots of $M$ are
$$
D_1,\qquad \frac{D_2}{D_1},\qquad \frac{D_3}{D_2},\qquad \frac{D_4}{D_3}=0,
$$
so
$$
M\succeq0,\qquad \operatorname{rank}M=3. \tag{5}
$$
Thus $r-1$ is the simple lowest eigenvalue of $A_r$. The eigenvector obtained in Step 2,
$$
v=\left(\frac{4-r}{r+2},\ 4-r,\ r-5,\ 1\right)^T, \tag{6}
$$
spans $\ker M$ and satisfies $b^Tv=0$.

Step 4: Construct all minimizers and the exact minimum value
Let
$$
x_0=(0,0,-1,0)^T,
\qquad
\mu=1-r>0.
$$
The third column of $M$ is exactly $b$, so
$$
Mx_0=-b,
\qquad \|x_0\|=1.
$$
Because $M=A_r+\mu I\succeq0$, identity (1) becomes
$$
q_r(y)-q_r(x_0)
=\frac12(y-x_0)^TM(y-x_0)
+\frac\mu2(1-\|y\|^2)\ge0
$$
for every feasible $y$. Hence $x_0$ is a global minimizer.

Equality holds exactly when $\|y\|=1$ and $y-x_0\in\ker M$. By (5), every minimizer therefore lies on the line
$$
x_0+s v.
$$
Since
$$
x_0^Tv=5-r\ne0,
$$
the equation $\|x_0+s v\|=1$ has exactly the two roots
$$
s=0,
\qquad
s=-\frac{2(5-r)}{\|v\|^2}.
$$
Thus $|\mathcal X_r|=2$ exactly. Finally,
$$
m(r)=q_r(x_0)=\frac r2-1=\frac{r-2}{2}. \tag{7}
$$
So the unique nonuniqueness parameter is the cubic root in (4), the minimizer set has exactly two points there, and the minimum value is $(\tau_*-2)/2$.

Final Answer: $\boxed{\operatorname{root}_{(-5/2,-17/7)}(x^3-2x^2-10x+2)}$

---

## Answer

$\operatorname{root}_{(-5/2,-17/7)}(x^3-2x^2-10x+2)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- trust-region hard case
- Jacobi eigenvector recurrence
- shifted positive-semidefinite certificate
- singular optimizer geometry

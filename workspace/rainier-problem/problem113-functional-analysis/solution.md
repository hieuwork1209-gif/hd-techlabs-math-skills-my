## Steps

Step 1: Reduce the sharp constant to a constrained Rayleigh quotient
For an odd function on $[-1,1]$, both the $L^2$ norm and the Dirichlet energy are twice their values on $[0,1]$. The moment conditions reduce to
$$
\int_0^1xu(x)\,dx=0,
\qquad
\int_0^1x^3u(x)\,dx=0.
$$
Let $H_0^1(0,1)$ denote the absolutely continuous functions that vanish at $0$ and $1$ and have square-integrable derivative, and set
$$
V=
\left\{
u\in H_0^1(0,1):
\int_0^1xu(x)\,dx=0,\
\int_0^1x^3u(x)\,dx=0
\right\}.
$$
The sharp constant is
$$
C=\frac{1}{\lambda_*},
$$
where
$$
\lambda_*
=
\inf_{u\in V\setminus\{0\}}
\frac{\int_0^1u'(x)^2\,dx}
{\int_0^1u(x)^2\,dx}.
$$

This infimum is positive because $u(0)=0$ gives
$$
|u(x)|
=
\left|
\int_0^xu'(t)\,dt
\right|
\leq
\sqrt{x}
\left(
\int_0^1u'(t)^2\,dt
\right)^{1/2},
$$
so
$$
\int_0^1u(x)^2\,dx
\leq
\frac{1}{2}
\int_0^1u'(x)^2\,dx.
$$

The infimum is attained. Take a minimizing sequence normalized by
$$
\int_0^1u_n(x)^2\,dx=1.
$$
Its derivative norms are bounded. The estimate
$$
|u_n(x)-u_n(y)|
\leq
\|u_n'\|_{L^2}|x-y|^{1/2}
$$
gives a uniformly bounded equicontinuous family, so a subsequence converges uniformly to a function $u$. The derivatives have a weakly convergent subsequence in $L^2$; write
$$
u_n'\rightharpoonup v.
$$
For every $x\in[0,1]$,
$$
u_n(x)
=
\int_0^xu_n'(t)\,dt
$$
passes to the weak limit because the indicator of $[0,x]$ belongs to $L^2$. Hence
$$
u(x)=\int_0^xv(t)\,dt,
$$
so $u\in H_0^1(0,1)$ and $u'=v$. Uniform convergence preserves both moment constraints and the $L^2$ normalization. Finally,
$$
\|u_n'\|_{L^2}^2
=
\|u'\|_{L^2}^2
+
\|u_n'-u'\|_{L^2}^2
+
2\langle u',u_n'-u'\rangle,
$$
and the last term tends to $0$ by weak convergence. Therefore
$$
\int_0^1u'(x)^2\,dx
\leq
\liminf_{n\to\infty}
\int_0^1u_n'(x)^2\,dx.
$$
A minimizer exists.

Step 2: Derive the Euler-Lagrange equation
Let $u$ be a normalized minimizer. On the tangent space
$$
W=
\left\{
v\in H_0^1(0,1):
\int_0^1xv(x)\,dx=0,\
\int_0^1x^3v(x)\,dx=0
\right\},
$$
the first variation of the Rayleigh quotient gives
$$
\int_0^1u'(x)v'(x)\,dx
=
\lambda_*
\int_0^1u(x)v(x)\,dx.
$$

The two moment functionals are linearly independent. If
$$
c_1\int_0^1xv(x)\,dx
+
c_3\int_0^1x^3v(x)\,dx
=
0
$$
for every $v\in H_0^1(0,1)$, choose
$$
v(x)=x(1-x)\left(c_1x+c_3x^3\right).
$$
Then
$$
\int_0^1x(1-x)\left(c_1x+c_3x^3\right)^2\,dx=0,
$$
which forces $c_1=c_3=0$. Thus the map
$$
v\mapsto
\left(
\int_0^1xv(x)\,dx,\
\int_0^1x^3v(x)\,dx
\right)
$$
has rank $2$, and $W$ is its kernel. Any linear functional that vanishes on $W$ therefore factors through this map. There are real constants $a,b$ such that
$$
\int_0^1u'v'\,dx
-
\lambda_*\int_0^1uv\,dx
=
a\int_0^1xv\,dx
+
b\int_0^1x^3v\,dx
$$
for every $v\in H_0^1(0,1)$.

In the weak sense,
$$
-u''=\lambda_*u+ax+bx^3.
$$
The right side is continuous, so integrating the equation twice shows that $u$ is twice continuously differentiable. Write
$$
\mu=\sqrt{\lambda_*}>0.
$$
For $\mu>0$, the map
$$
(B,D)
\mapsto
\left(
-\mu^2B-6D,\
-\mu^2D
\right)
$$
is invertible, so the polynomial forcing $ax+bx^3$ has a particular solution of the form $Bx+Dx^3$. The homogeneous solutions are $\sin(\mu x)$ and $\cos(\mu x)$, and $u(0)=0$ removes the cosine term. Hence
$$
u(x)=A\sin(\mu x)+Bx+Dx^3.
$$

Step 3: Convert the boundary and moment conditions into a determinant equation
The condition $u(1)=0$ gives
$$
A\sin\mu+B+D=0.
$$
Integration by parts gives
$$
\int_0^1x\sin(\mu x)\,dx
=
\frac{\sin\mu-\mu\cos\mu}{\mu^2},
$$
and a second integration-by-parts calculation gives
$$
\int_0^1x^3\sin(\mu x)\,dx
=
\frac{-\mu^3\cos\mu+3\mu^2\sin\mu+6\mu\cos\mu-6\sin\mu}{\mu^4}.
$$
The two moment constraints are therefore
$$
A\frac{\sin\mu-\mu\cos\mu}{\mu^2}
+\frac{B}{3}
+\frac{D}{5}
=0
$$
and
$$
A\frac{-\mu^3\cos\mu+3\mu^2\sin\mu+6\mu\cos\mu-6\sin\mu}{\mu^4}
+\frac{B}{5}
+\frac{D}{7}
=0.
$$

A nonzero triple $(A,B,D)$ exists exactly when
$$
\det
\begin{pmatrix}
\sin\mu & 1 & 1\\
\frac{\sin\mu-\mu\cos\mu}{\mu^2} & \frac{1}{3} & \frac{1}{5}\\
\frac{-\mu^3\cos\mu+3\mu^2\sin\mu+6\mu\cos\mu-6\sin\mu}{\mu^4}
& \frac{1}{5} & \frac{1}{7}
\end{pmatrix}
=
0.
$$
Expanding along the first column gives
$$
\frac{4}{525}\sin\mu
+
\frac{2}{35}
\frac{\sin\mu-\mu\cos\mu}{\mu^2}
-
\frac{2}{15}
\frac{-\mu^3\cos\mu+3\mu^2\sin\mu+6\mu\cos\mu-6\sin\mu}{\mu^4}.
$$
After multiplying by $525\mu^4/4$, the determinant equation is
$$
\mu^4\sin\mu
+10\mu^3\cos\mu
-45\mu^2\sin\mu
-105\mu\cos\mu
+105\sin\mu
=0.
$$

Step 4: Identify the smallest positive root with the sharp constant
Define
$$
g(x)
=
x^4\sin x
+10x^3\cos x
-45x^2\sin x
-105x\cos x
+105\sin x.
$$
The minimizer from Step 1 produces a number $\mu>0$ with
$$
g(\mu)=0
$$
and
$$
\lambda_*=\mu^2.
$$

Conversely, let $\mu>0$ satisfy $g(\mu)=0$. The determinant in Step 3 vanishes, so there is a nonzero triple $(A,B,D)$ for which
$$
u(x)=A\sin(\mu x)+Bx+Dx^3
$$
satisfies the boundary condition and both moment constraints. Also,
$$
-u''-\mu^2u
$$
is a linear combination of $x$ and $x^3$. Multiplying by $u$, integrating over $[0,1]$, and using the two moment constraints gives
$$
\int_0^1u'(x)^2\,dx
=
\mu^2
\int_0^1u(x)^2\,dx.
$$
Every positive root of $g$ therefore gives a feasible Rayleigh quotient equal to $\mu^2$.

If a positive root smaller than the minimizer's $\mu$ existed, it would produce a feasible quotient smaller than $\lambda_*$, which is impossible. Therefore
$$
\lambda_*
=
\left(
\min
\left\{
x>0:
x^4\sin x
+10x^3\cos x
-45x^2\sin x
-105x\cos x
+105\sin x
=0
\right\}
\right)^2.
$$
Taking the reciprocal gives the sharp constant.
Final Answer: $\boxed{\left(\min\{x>0:x^4\sin x+10x^3\cos x-45x^2\sin x-105x\cos x+105\sin x=0\}\right)^{-2}}$

---

## Answer

$\left(\min\{x>0:x^4\sin x+10x^3\cos x-45x^2\sin x-105x\cos x+105\sin x=0\}\right)^{-2}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- constrained Rayleigh quotients
- variational minimizers
- Euler-Lagrange equations
- moment constraints
- transcendental eigenvalue equations

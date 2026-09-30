## Steps

Step 1: Reduce the sharp constant to a constrained Rayleigh quotient
For an odd function on $[-1,1]$, both the $L^2$ norm and the Dirichlet energy are twice their values on $[0,1]$. The moment conditions also reduce to
$$
\int_0^1 xu(x)\,dx=0,
\qquad
\int_0^1 x^3u(x)\,dx=0.
$$
Let
$$
V=
\left\{
u\in H_0^1(0,1):
\int_0^1 xu(x)\,dx=0,\
\int_0^1 x^3u(x)\,dx=0
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
\frac{\int_0^1 u'(x)^2\,dx}
{\int_0^1 u(x)^2\,dx}.
$$

This infimum is positive because $u(0)=0$ gives
$$
|u(x)|
=
\left|
\int_0^x u'(t)\,dt
\right|
\leq
\sqrt{x}
\left(
\int_0^1 u'(t)^2\,dt
\right)^{1/2},
$$
so
$$
\int_0^1u(x)^2\,dx
\leq
\frac{1}{2}\int_0^1u'(x)^2\,dx.
$$

The infimum is attained. Indeed, take a minimizing sequence normalized by
$$
\int_0^1u_n(x)^2\,dx=1.
$$
Its derivative norms are bounded. The estimate
$$
|u_n(x)-u_n(y)|
\leq
\|u_n'\|_{L^2}|x-y|^{1/2}
$$
gives a uniformly bounded equicontinuous family. A uniformly convergent subsequence has limit $u$, while the derivatives have a weakly convergent subsequence in $L^2$. For every $x$,
$$
u_n(x)=\int_0^x u_n'(t)\,dt
$$
passes to the weak limit, so $u\in H_0^1(0,1)$. Uniform convergence preserves both moment constraints and the $L^2$ normalization. Weak lower semicontinuity of the $L^2$ norm of the derivative then gives
$$
\int_0^1u'(x)^2\,dx
\leq
\liminf_{n\to\infty}
\int_0^1u_n'(x)^2\,dx.
$$
Thus a minimizer exists.

Step 2: Derive the Euler-Lagrange equation
Let $u$ be a normalized minimizer. On the tangent space
$$
W=
\left\{
v\in H_0^1(0,1):
\int_0^1 xv(x)\,dx=0,\
\int_0^1 x^3v(x)\,dx=0
\right\},
$$
the first variation gives
$$
\int_0^1u'(x)v'(x)\,dx
=
\lambda_*
\int_0^1u(x)v(x)\,dx.
$$

The two moment functionals are linearly independent, so $W$ has codimension $2$. Therefore the linear functional
$$
v\mapsto
\int_0^1u'v'\,dx
-
\lambda_*\int_0^1uv\,dx
$$
is a linear combination of those two moment functionals. Hence there are real constants $a,b$ such that
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
The right side is continuous, so $u$ is twice continuously differentiable. Write
$$
\mu=\sqrt{\lambda_*}>0.
$$
The general solution satisfying $u(0)=0$ has the form
$$
u(x)=A\sin(\mu x)+Bx+Dx^3.
$$

Step 3: Convert the boundary and moment conditions into a determinant equation
The condition $u(1)=0$ gives
$$
A\sin\mu+B+D=0.
$$
Also,
$$
\int_0^1x\sin(\mu x)\,dx
=
\frac{\sin\mu-\mu\cos\mu}{\mu^2},
$$
and
$$
\int_0^1x^3\sin(\mu x)\,dx
=
\frac{-\mu^3\cos\mu+3\mu^2\sin\mu+6\mu\cos\mu-6\sin\mu}{\mu^4}.
$$
Thus the two moment constraints are
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

A nonzero triple $(A,B,D)$ exists exactly when the determinant of this homogeneous system vanishes. Multiplying that determinant by
$$
\frac{525\mu^4}{4}
$$
and collecting the sine and cosine terms gives
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

Conversely, let $\mu>0$ satisfy $g(\mu)=0$. The determinant in Step 3 then vanishes, so there is a nonzero triple $(A,B,D)$ for which
$$
u(x)=A\sin(\mu x)+Bx+Dx^3
$$
satisfies the boundary condition and both moment constraints. Moreover,
$$
-u''-\mu^2u
$$
is a linear combination of $x$ and $x^3$. Multiplying by $u$, integrating over $[0,1]$, and using the two moment constraints gives
$$
\int_0^1u'(x)^2\,dx
=
\mu^2\int_0^1u(x)^2\,dx.
$$
Hence every positive root of $g$ gives a feasible Rayleigh quotient equal to $\mu^2$.

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

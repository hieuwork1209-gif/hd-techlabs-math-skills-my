## Steps

Step 1: Parametrize every positive solution of the boundary-value problem.
Let $u$ be a positive solution of
$$
u''+\lambda e^u=0,\qquad u(0)=u(1)=0.
$$
Because $u''=-\lambda e^u<0$, the function is strictly concave, so it has a unique maximum $M$ at some $c\in(0,1)$, with $u'(c)=0$. Multiplying the differential equation by $u'$ and integrating gives the first integral
$$
\frac12u'(x)^2+\lambda e^{u(x)}=\lambda e^M.
$$
For any level $s\in[0,M)$, the distance from the maximum point to either point where $u=s$ is therefore
$$
\int_s^M\frac{dv}{\sqrt{2\lambda(e^M-e^v)}},
$$
which is independent of the side of the maximum. Since both endpoints have level $0$, their distances from $c$ are equal, so $c=\frac12$.

Set
$$
t=\sqrt{\frac{\lambda e^M}{2}}>0.
$$
Then the function
$$
U(x)=M-2\log\cosh\left(t\left(x-\frac12\right)\right)
$$
has $U(1/2)=M$, $U'(1/2)=0$, and
$$
U''=-2t^2\operatorname{sech}^2\left(t\left(x-\frac12\right)\right),
\qquad
\lambda e^U=2t^2\operatorname{sech}^2\left(t\left(x-\frac12\right)\right).
$$
Thus $U$ satisfies the same autonomous initial-value problem as $u$ at $x=1/2$, so uniqueness gives $u=U$. The boundary condition $u(0)=0$ yields
$$
M=2\log\cosh\left(\frac t2\right),
$$
and hence every positive solution is uniquely represented by
$$
u_t(x)=2\log\frac{\cosh(t/2)}{\cosh\left(t\left(x-\frac12\right)\right)},
\qquad
\lambda(t)=\frac{2t^2}{\cosh^2(t/2)},
\qquad t>0.
$$

Step 2: Determine when the linearized Dirichlet operator has a nontrivial kernel.
For the solution $u_t$, the linearized equation is
$$
v''+\lambda(t)e^{u_t}v=0,
\qquad v(0)=v(1)=0.
$$
Since
$$
\lambda(t)e^{u_t(x)}=2t^2\operatorname{sech}^2\left(t\left(x-\frac12\right)\right),
$$
putting $y=t(x-1/2)$ and $V(y)=v(x)$ reduces the equation to
$$
V''+2\operatorname{sech}^2(y)V=0
$$
on $[-t/2,t/2]$. Two solutions are
$$
V_1(y)=\tanh y,
\qquad
V_2(y)=y\tanh y-1.
$$
Indeed, direct differentiation gives $V_j''+2\operatorname{sech}^2(y)V_j=0$, and at $y=0$ their initial data are $(V_1,V_1')=(0,1)$ and $(V_2,V_2')=(-1,0)$, so they are linearly independent and span the solution space.

Write $a=t/2$ and $T=\tanh a>0$. A general solution is
$$
V=A\tanh y+B(y\tanh y-1).
$$
The two Dirichlet conditions become
$$
AT+B(aT-1)=0,
\qquad
-AT+B(aT-1)=0.
$$
Subtracting gives $A=0$. A nonzero solution therefore exists exactly when
$$
aT=1,
$$
that is,
$$
t\tanh\left(\frac t2\right)=2.
$$

Step 3: Prove uniqueness of the degeneracy parameter and state the exact set.
Define
$$
\phi(t)=t\tanh\left(\frac t2\right),\qquad t>0.
$$
Then
$$
\phi'(t)=\tanh\left(\frac t2\right)+\frac t2\operatorname{sech}^2\left(\frac t2\right)>0.
$$
Also $\phi(t)\to0$ as $t\downarrow0$ and $\phi(t)\to\infty$ as $t\to\infty$. Hence $\phi(t)=2$ has exactly one positive solution. Combining this with the parametrization of all positive solutions and the kernel criterion, the requested set of parameters is the singleton
$$
\left\{\frac{2t^2}{\cosh^2(t/2)}:t>0,\ t\tanh(t/2)=2\right\}.
$$
Final Answer: $\boxed{\left\{\frac{2t^2}{\cosh^2(t/2)}:t>0,\ t\tanh(t/2)=2\right\}}$

---

## Answer

$\left\{\frac{2t^2}{\cosh^2(t/2)}:t>0,\ t\tanh(t/2)=2\right\}$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Set or multiset of objects

---

## Solution Concepts

- autonomous first integral
- Bratu solution branch
- Sturm-Liouville linearization
- Pöschl-Teller equation
- bifurcation degeneracy

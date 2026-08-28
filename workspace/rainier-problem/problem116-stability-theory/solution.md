## Steps

Step 1: Expose the hidden triangular coordinate
Set
$$
u=x-y^2.
$$
Using the two differential equations,
$$
\dot u=\dot x-2y\dot y.
$$
Substituting and collecting terms gives
$$
\dot u=-u\left((u-1)^2+5-a-2b\right),
$$
while the second equation factors as
$$
\dot y=-y\left((y-2)^2+2a-b\right).
$$
The polynomial change of variables $(x,y)\mapsto(u,y)=(x-y^2,y)$ is a global bijection with inverse $x=u+y^2$, and in these coordinates the system is completely decoupled.

Step 2: Determine when the scalar y-equation converges globally to zero
Write
$$
c=2a-b.
$$
Then
$$
\dot y=-y\left((y-2)^2+c\right).
$$
If $c\leq0$, the factor in parentheses has a real zero: for $c=0$, $y=2$ is an additional equilibrium, while for $c<0$ its roots are $y=2\pm\sqrt{-c}$ and at least one of them is nonzero. So global convergence to zero is impossible.

If $c>0$, then $((y-2)^2+c)>0$ for every real $y$, so $y\dot y<0$ whenever $y\neq0$. Therefore $|y(t)|$ decreases, so every forward solution is bounded and exists for all $t\geq0$. Its limit exists. Any nonzero limit would keep $|\dot y|$ bounded away from zero, so the only possible limit is $0$. The origin is also Lyapunov stable for this scalar equation because $|y(t)|$ never increases. So the y-equation is globally asymptotically stable exactly when
$$
b<2a.
$$

Step 3: Determine when the scalar u-equation converges globally to zero
Write
$$
d=5-a-2b.
$$
Then
$$
\dot u=-u\left((u-1)^2+d\right).
$$
If $d\leq0$, the factor in parentheses has a real zero: for $d=0$, $u=1$ is an additional equilibrium, while for $d<0$ its roots are $u=1\pm\sqrt{-d}$ and at least one of them is nonzero. So global convergence to zero is impossible.

If $d>0$, then $((u-1)^2+d)>0$ for every real $u$, so $u\dot u<0$ whenever $u\neq0$. So $|u(t)|$ decreases, every forward solution is bounded and global, and the same limiting argument forces $u(t)\to0$. Lyapunov stability follows from monotonicity of $|u(t)|$. Therefore the u-equation is globally asymptotically stable exactly when
$$
a+2b<5.
$$

Step 4: Transfer the scalar criterion back to the original variables
The transformed system is globally asymptotically stable precisely when both scalar criteria hold:
$$
b<2a,
\qquad
a+2b<5.
$$
Under these inequalities, $u(t)\to0$ and $y(t)\to0$, so
$$
x(t)=u(t)+y(t)^2\to0.
$$
Because the change of variables and its inverse are polynomial and fix the origin, Lyapunov stability in $(u,y)$ coordinates is equivalent to Lyapunov stability in $(x,y)$ coordinates near the origin.

Conversely, if either inequality fails, the corresponding scalar equation has a nonzero equilibrium. If $b\geq2a$, choosing such a nonzero equilibrium for $y$ and $u=0$ gives a nonzero equilibrium of the original system. If $a+2b\geq5$, choosing such a nonzero equilibrium for $u$ and $y=0$ does the same. This proves the stated region is also necessary.
Final Answer: $\boxed{\{(a,b)\in\mathbb{R}^2:b<2a,\ a+2b<5\}}$

---

## Answer

$\{(a,b)\in\mathbb{R}^2:b<2a,\ a+2b<5\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- global asymptotic stability
- nonlinear change of variables
- scalar autonomous differential equations
- invariant equilibria
- Lyapunov stability

---

## Black-Box Audit — no issues found

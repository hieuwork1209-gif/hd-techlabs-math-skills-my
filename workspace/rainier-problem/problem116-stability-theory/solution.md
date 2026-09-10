## Steps

Step 1: Reduce global stability to positive definiteness of a homogeneous quartic
Define
$$
V(x,y)=x^4+a x^3y+b x^2y^2+a xy^3+y^4.
$$
The system is exactly the negative gradient flow
$$
(\dot x,\dot y)=-\nabla V(x,y),
$$
because
$$
V_x=4x^3+3a x^2y+2bxy^2+a y^3,
\qquad
V_y=a x^3+2b x^2y+3axy^2+4y^3.
$$
Hence
$$
\dot V=-V_x^2-V_y^2\leq0.
$$

If $V(x,y)>0$ for every $(x,y)\neq(0,0)$, then homogeneity and continuity imply $V(x,y)\geq c(x^2+y^2)^2$ for some $c>0$, so $V$ is proper and positive definite. Every forward trajectory therefore remains in a compact sublevel set and exists for all $t\geq0$. Moreover, Euler's identity for the homogeneous quartic gives
$$
xV_x+yV_y=4V.
$$
Thus $\nabla V=0$ at a nonzero point would force $V=0$, impossible. The origin is the unique equilibrium, and LaSalle's invariance principle yields convergence of every trajectory to the origin. Positive definiteness of $V$ gives Lyapunov stability.

Conversely, if $V$ is not positive definite, either $V(z)<0$ for some nonzero $z$, or $V\geq0$ everywhere and $V(z)=0$ for some nonzero $z$. In the first case, by homogeneity there are initial points arbitrarily close to the origin with negative $V$; since $V$ is nonincreasing along trajectories, such trajectories cannot converge to the origin where $V=0$. In the second case, $z$ is a global minimum of the differentiable function $V$, hence $\nabla V(z)=0$, giving a nonzero equilibrium. Therefore the origin is globally asymptotically stable exactly when $V$ is positive definite.

Step 2: Reduce the binary quartic to a quadratic on a disconnected domain
If $y=0$ and $x\neq0$, then $V=x^4>0$. For $y\neq0$, put
$$
t=\frac{x}{y}.
$$
Then
$$
\frac{V(x,y)}{y^4}=f(t):=t^4+a t^3+b t^2+a t+1.
$$
At $t=0$ this equals $1$. For $t\neq0$, divide by $t^2>0$ and set
$$
z=t+\frac1t.
$$
Using $t^2+t^{-2}=z^2-2$ gives
$$
\frac{f(t)}{t^2}=q(z):=z^2+a z+b-2.
$$
For real nonzero $t$, the possible values of $z$ are exactly
$$
(-\infty,-2]\cup[2,\infty).
$$
Hence $V$ is positive definite exactly when
$$
q(z)>0
\qquad\text{for every }|z|\geq2.
$$

Step 3: Minimize the quadratic on the two rays
The vertex of
$$
q(z)=z^2+a z+b-2
$$
is $z_0=-a/2$.

If $|a|\leq4$, then $z_0\in[-2,2]$. Therefore on the allowed set $|z|\geq2$, the minima occur at the endpoints $z=2$ and $z=-2$. We need
$$
q(2)=b+2a+2>0,
\qquad
q(-2)=b-2a+2>0,
$$
which is equivalent to
$$
b>2|a|-2.
$$

If $a\geq4$, then $z_0\leq-2$, so the minimum on the left ray is
$$
q(z_0)=b-2-\frac{a^2}{4}.
$$
The right-ray minimum is $q(2)$, which is automatically positive once $q(z_0)>0$. Thus the condition is
$$
b>2+\frac{a^2}{4}.
$$
For $a\leq-4$ the argument is symmetric, with the vertex on the right ray, and the same condition results. At $|a|=4$ the two formulas agree, both giving $b>6$.

Step 4: State the exact stability region
Combining the cases, the equilibrium is globally asymptotically stable exactly for
$$
\left\{
\begin{array}{ll}
|a|\leq4 &\text{and } b>2|a|-2,\\
\text{or}\\
|a|\geq4 &\text{and } b>2+\dfrac{a^2}{4}.
\end{array}
\right.
$$
The boundary is excluded because there $q$ vanishes at an allowed value of $z$, so $V$ has a nonzero zero and global asymptotic stability fails.
Final Answer: $\boxed{\{(a,b): |a|\leq4,\ b>2|a|-2\}\cup\{(a,b): |a|\geq4,\ b>2+a^2/4\}}$

---

## Answer

$\{(a,b): |a|\leq4,\ b>2|a|-2\}\cup\{(a,b): |a|\geq4,\ b>2+a^2/4\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- global asymptotic stability
- homogeneous gradient flows
- positive definite binary quartics
- reciprocal polynomial reduction
- Lyapunov functions

---

## Black-Box Audit — no issues found

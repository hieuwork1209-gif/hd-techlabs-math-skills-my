## Steps

Step 1: Expose the hidden polynomial coordinate
Set
$$
u=x-y^2.
$$
The second equation becomes
$$
\dot y=-y^3-by-u.
$$
Using $\dot u=\dot x-2y\dot y$ and substituting the given $\dot x$ gives
$$
\dot u=-u^3-au-y.
$$
Thus the polynomial change of variables $(x,y)\mapsto(u,y)=(x-y^2,y)$, with inverse $x=u+y^2$, transforms the system into
$$
\dot u=-u^3-au-y,
\qquad
\dot y=-y^3-by-u.
$$

Step 2: Identify the gradient structure
Define
$$
\Phi(u,y)=\frac14(u^4+y^4)+\frac12\left(au^2+2uy+by^2\right).
$$
Then
$$
\frac{\partial\Phi}{\partial u}=u^3+au+y,
\qquad
\frac{\partial\Phi}{\partial y}=y^3+u+by,
$$
so the transformed system is the gradient flow
$$
(\dot u,\dot y)=-\nabla\Phi(u,y).
$$
Let
$$
M=\begin{pmatrix}a&1\\1&b\end{pmatrix}.
$$
The quadratic part of $\Phi$ is $\frac12(u,y)M(u,y)^T$.

Step 3: Prove sufficiency when the quadratic form is positive semidefinite
Assume $M\succeq0$. Then
$$
\Phi(u,y)\geq \frac14(u^4+y^4),
$$
so $\Phi$ is positive definite and proper. Along every solution,
$$
\dot\Phi=-\left(u^3+au+y\right)^2-\left(y^3+u+by\right)^2\leq0.
$$
If $(u,y)$ is an equilibrium, multiplying the two equilibrium equations by $u$ and $y$ respectively and adding gives
$$
0=u^4+y^4+au^2+2uy+by^2
  =u^4+y^4+(u,y)M(u,y)^T.
$$
Every term on the right is nonnegative, hence $u=y=0$. Thus the origin is the unique equilibrium.

Because $\Phi$ is proper and nonincreasing, every forward trajectory stays in a compact sublevel set, so every solution exists for all $t\geq0$. Any omega-limit point must satisfy $\dot\Phi=0$, hence must be an equilibrium; since the origin is the unique equilibrium, every trajectory converges to $(0,0)$. Positive definiteness of $\Phi$ also gives Lyapunov stability. Therefore the origin is globally asymptotically stable whenever $M\succeq0$. Notice that singular positive-semidefinite matrices are allowed because the quartic terms remain strictly positive away from the origin.

Step 4: Prove necessity and translate the matrix condition
Suppose $M$ is not positive semidefinite. Then there is a nonzero vector $v=(v_1,v_2)$ with
$$
v^TMv<0.
$$
For sufficiently small $s>0$,
$$
\Phi(sv)=\frac{s^4}{4}(v_1^4+v_2^4)+\frac{s^2}{2}v^TMv<0.
$$
Such initial points can be chosen arbitrarily close to the origin. Since $\Phi$ is nonincreasing along trajectories, a solution starting from one of them can never converge to the origin, where $\Phi=0$. Hence global asymptotic stability is impossible when $M\not\succeq0$.

For a symmetric $2\times2$ matrix,
$$
M\succeq0
\quad\Longleftrightarrow\quad
a\geq0,\quad b\geq0,\quad ab-1\geq0.
$$
The inequality $ab\geq1$ then forces $a>0$ and $b>0$. Therefore the required parameter region is
$$
a>0,
\qquad
b>0,
\qquad
ab\geq1.
$$
Final Answer: $\boxed{\{(a,b)\in\mathbb{R}^2:a>0,\ b>0,\ ab\geq1\}}$

---

## Answer

$\{(a,b)\in\mathbb{R}^2:a>0,\ b>0,\ ab\geq1\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- global asymptotic stability
- polynomial change of variables
- gradient flows
- positive semidefinite quadratic forms
- Lyapunov functions

---

## Black-Box Audit — no issues found

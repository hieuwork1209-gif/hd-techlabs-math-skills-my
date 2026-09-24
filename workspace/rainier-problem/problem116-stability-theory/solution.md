## Steps

Step 1: Establish global existence and analyze the linear subfamily
Consider
$
x'=y,
\qquad
y'=-x-(a+bx^2)y,
$
with $a,b\geq0$. The energy
$
E(x,y)=\frac{x^2+y^2}{2}
$
satisfies
$
E'
=
xx'+yy'
=
-(a+bx^2)y^2
\leq0.
$
Thus every solution remains in its initial energy disk. Since the vector field is polynomial and the solution stays bounded, no finite-time blow-up is possible, so every solution exists for all $t\geq0$.

If $b=0$, the system is linear:
$$
\begin{pmatrix}x\\y\end{pmatrix}'
=
\begin{pmatrix}
0&1\\
-1&-a
\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}.
$$
Its characteristic polynomial is
$$
\lambda^2+a\lambda+1.
$$
If $a>0$, both roots have negative real part, so the origin is globally exponentially stable. If $a=0$, the system is the harmonic oscillator
$$
x''+x=0,
$$
and nonzero solutions are periodic, so the origin is not exponentially stable.

Step 2: Build a slow invariant region when the nonlinear damping is present
Assume $b>0$. Fix any constant
$$
K>\frac{1}{b},
$$
and choose initial data
$$
x(0)=R>0,
\qquad
y(0)=0.
$$
Set
$$
v=-y.
$$
As long as $x>0$, the equations become
$$
x'=-v,
\qquad
v'=x-(a+bx^2)v.
$$
Consider the region
$$
0\leq v\leq\frac{K}{x}.
$$
At the lower boundary $v=0$,
$$
v'=x>0,
$$
so the vector field points into the region. For the upper boundary define
$$
\phi(x,v)=v-\frac{K}{x}.
$$
Along a solution,
$$
\phi'
=
v'+\frac{Kx'}{x^2}.
$$
On $v=K/x$ this becomes
$$
\phi'
=
x-(a+bx^2)\frac{K}{x}
-\frac{K^2}{x^3}
=
(1-bK)x-\frac{aK}{x}-\frac{K^2}{x^3}<0,
$$
because $K>1/b$. Hence a solution that starts with $v=0$ cannot leave this region through either boundary while $x>0$.

Step 3: Derive the slow-decay lower bound
Inside the invariant region from Step 2,
$$
0\leq v\leq\frac{K}{x}.
$$
Therefore
$$
\frac{d}{dt}x^2
=
2xx'
=
-2xv
\geq
-2K.
$$
Thus, for every time before $x$ reaches zero,
$$
x(t)^2\geq R^2-2Kt.
$$
Set
$$
t_R=\frac{3R^2}{8K}.
$$
Then the right side is $R^2/4$, so in fact
$$
x(t)^2\geq\frac{R^2}{4}
$$
for $0\leq t\leq t_R$. In particular $x$ stays positive on this whole interval, so the argument is self-consistent, and
$$
\|(x(t_R),y(t_R))\|_2\geq x(t_R)\geq\frac{R}{2}.
$$

Step 4: Rule out global exponential stability for every $b>0$
Suppose that for some $a\geq0$ and $b>0$ the origin were globally exponentially stable. Then there would be constants $M,\gamma>0$ such that every solution satisfies
$$
\|(x(t),y(t))\|_2
\leq
M e^{-\gamma t}
\|(x(0),y(0))\|_2
$$
for all $t\geq0$.

Apply this estimate to the initial data used in Step 2. Since the initial norm is $R$, Step 3 gives
$$
\frac{R}{2}
\leq
M e^{-\gamma t_R}R.
$$
After cancelling $R>0$,
$$
\frac{1}{2}
\leq
M\exp\left(-\frac{3\gamma R^2}{8K}\right).
$$
The right side tends to $0$ as $R\to\infty$, a contradiction. Hence no pair with $b>0$ gives global exponential stability.

Step 5: State the complete parameter set
Step 1 shows that all pairs with $b=0$ and $a>0$ are globally exponentially stable, while $(a,b)=(0,0)$ is not. Step 4 excludes every pair with $b>0$. These cases exhaust $a,b\geq0$.
Final Answer: $\boxed{\{(a,b):a>0,\ b=0\}}$

---

## Answer

$\{(a,b):a>0,\ b=0\}$

---

## Classification

**Problem Type:** Exhaustive enumeration

**Answer Type:** Interval or region description

---

## Solution Concepts

- global exponential stability
- planar nonlinear systems
- invariant regions
- comparison inequalities
- Hurwitz stability

---

## Black-Box Audit — no issues found

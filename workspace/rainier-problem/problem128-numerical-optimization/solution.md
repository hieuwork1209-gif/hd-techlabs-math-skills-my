## Steps

Step 1: Derive the interpolation and orthogonality constraints
For a differentiable convex function with $1$-Lipschitz gradient, write $g(x)=\nabla f(x)$. For arbitrary $u,v$, the smooth convex interpolation inequality is
$$
f(u)\geq f(v)+g(v)^T(u-v)+\frac{1}{2}\|g(u)-g(v)\|^2.
$$
First derive the descent inequality. For $d=y-x$, the line-integral identity and the $1$-Lipschitz property give
$$
f(y)-f(x)-g(x)^Td
=
\int_0^1\bigl(g(x+td)-g(x)\bigr)^Td\,dt
\leq
\int_0^1 t\|d\|^2\,dt
=
\frac{1}{2}\|d\|^2.
$$
Now set $\psi(z)=f(z)-g(v)^Tz$. The function $\psi$ is convex and $1$-smooth and satisfies $\nabla\psi(v)=0$, so $v$ minimizes $\psi$. Apply the descent inequality to $\psi$ from $u$ to $u-\nabla\psi(u)$:
$$
\psi\bigl(u-\nabla\psi(u)\bigr)
\leq
\psi(u)-\frac{1}{2}\|\nabla\psi(u)\|^2.
$$
Since $\psi(v)$ is no larger than the left side, rearrangement gives the displayed interpolation inequality.

Let
$$
g_i=\nabla f(x_i),
\qquad
F_i=f(x_i)-f_*,
\qquad
d=x_0-x_*.
$$
Exact minimization on the first affine line gives
$$
g_1^Tg_0=0,
$$
and exact minimization on the second affine plane gives
$$
g_2^Tg_0=g_2^Tg_1=0.
$$
For $i=1,2$, the displacement $x_i-x_0$ lies in the span of the preceding gradients and is orthogonal to $g_i$. Together with the case $i=0$, this gives
$$
g_i^T(x_i-x_*)=g_i^Td
\qquad(i=0,1,2).
$$

Put $s_i=\|g_i\|$. Applying the interpolation inequality with $v=x_i$ and $u=x_*$ gives
$$
F_i\leq g_i^Td-\frac{1}{2}s_i^2.
$$
Applying it with $(u,v)=(x_i,x_{i+1})$ and using the orthogonality above gives
$$
F_i-F_{i+1}\geq\frac{1}{2}(s_i^2+s_{i+1}^2)
\qquad(i=0,1).
$$

Step 2: Convert the upper bound to a three-variable extremal problem
If $g_i\neq0$, define
$$
a_i=\frac{g_i^Td}{s_i}.
$$
The three gradients are mutually orthogonal, so Bessel's inequality gives
$$
a_0^2+a_1^2+a_2^2\leq\|d\|^2\leq1.
$$
If $g_0=0$, then $x_0$ is a global minimizer; if $g_1=0$, then $x_1$ is a global minimizer and belongs to the second search plane; if $g_2=0$, then $x_2$ is a global minimizer. In each case $F_2=0$. Assume $F_2>0$ and $s_0s_1s_2>0$.

Write $F=F_2$. The inequalities from Step 1 imply
$$
F\leq a_2s_2-\frac{1}{2}s_2^2,
$$
$$
F\leq a_1s_1-s_1^2-\frac{1}{2}s_2^2,
$$
and, after using both successive decreases,
$$
F\leq a_0s_0-s_0^2-s_1^2-\frac{1}{2}s_2^2.
$$
Scale
$$
u_i=\frac{s_i}{\sqrt{F}},
\qquad
A_i=\frac{a_i}{\sqrt{F}}.
$$
Then
$$
\frac{1}{F}\geq A_0^2+A_1^2+A_2^2,
$$
while the three preceding inequalities give
$$
A_0\geq
u_0+\frac{1+u_1^2+\frac{1}{2}u_2^2}{u_0},
$$
$$
A_1\geq
u_1+\frac{1+\frac{1}{2}u_2^2}{u_1},
\qquad
A_2\geq
\frac{1}{u_2}+\frac{u_2}{2}.
$$

Step 3: Solve the nested scalar minimization exactly
Set
$$
\phi=\frac{1+\sqrt{5}}{2},
\qquad
v=1+\frac{u_2^2}{2}.
$$
For fixed $u_1,u_2$, the arithmetic-geometric mean inequality gives
$$
A_0^2
\geq
4(v+u_1^2).
$$
Therefore
$$
A_0^2+A_1^2+A_2^2
\geq
6v+5u_1^2+\frac{v^2}{u_1^2}
+\left(\frac{1}{u_2}+\frac{u_2}{2}\right)^2.
$$
The inequality
$$
5u_1^2+\frac{v^2}{u_1^2}\geq2\sqrt{5}\,v
$$
turns the first three terms into
$$
(6+2\sqrt{5})v=4\phi^2v.
$$
Now put $y=u_2^2$. Then
$$
A_0^2+A_1^2+A_2^2
\geq
4\phi^2+1+\frac{1}{y}
+\frac{1+8\phi^2}{4}y.
$$
Let
$$
S=\sqrt{1+8\phi^2}=\sqrt{13+4\sqrt{5}}.
$$
Applying the arithmetic-geometric mean inequality to the last two terms gives a lower bound of $S$, so
$$
A_0^2+A_1^2+A_2^2
\geq
4\phi^2+1+S.
$$
With
$$
\theta=\frac{1+S}{2},
$$
the identity $S^2=1+8\phi^2$ gives
$$
4\phi^2+1+S=2\theta^2.
$$
Therefore
$$
F_2\leq\frac{1}{2\theta^2}
=
\frac{2}{(1+\sqrt{13+4\sqrt{5}})^2}.
$$

Step 4: Construct data attaining every inequality in the upper bound
Let
$
r=\frac{1}{2\theta^2}.
$
Equality in the final arithmetic-geometric mean inequality of Step 3 requires
$
u_2^2=\frac{2}{S}.
$
Then $v=1+u_2^2/2=1+1/S$. Equality in
$
5u_1^2+\frac{v^2}{u_1^2}\geq2\sqrt{5}\,v
$
requires $u_1^2=v/\sqrt{5}$, and equality in the first arithmetic-geometric mean bound requires $u_0^2=v+u_1^2$. Therefore set
$
u_2=\sqrt{\frac{2}{S}},
\qquad
v=1+\frac{1}{S},
\qquad
u_1=\sqrt{\frac{v}{\sqrt{5}}},
\qquad
u_0=\sqrt{v+u_1^2}.
$
Equality in the three original lower bounds for $A_i$ then forces
$
A_0=2u_0,
\qquad
A_1=u_1+\frac{v}{u_1},
\qquad
A_2=\frac{1}{u_2}+\frac{u_2}{2}.
$
The equalities in Step 3 give
$$
A_0^2+A_1^2+A_2^2=2\theta^2.
$$
Set
$$
a_i=\sqrt{r}\,A_i,
\qquad
s_i=\sqrt{r}\,u_i
\qquad(i=0,1,2).
$$
Then
$$
a_0^2+a_1^2+a_2^2=1.
$$

Let $e_0,e_1,e_2$ be the standard orthonormal basis of $\mathbb{R}^{3}$, and define
$$
x_*=0,
\qquad
x_0=a_0e_0+a_1e_1+a_2e_2,
\qquad
g_i=s_ie_i.
$$
Define the target function values by
$$
F_2=r,
$$
$$
F_1=r+\frac{1}{2}(s_1^2+s_2^2),
$$
$$
F_0=F_1+\frac{1}{2}(s_0^2+s_1^2).
$$
The equality conditions also give the normalized identities
$$
A_2u_2-\frac{1}{2}u_2^2=1,
$$
$$
A_1u_1-\frac{1}{2}u_1^2
=
1+\frac{1}{2}(u_1^2+u_2^2),
$$
and, because $u_0^2=v+u_1^2$,
$$
A_0u_0-\frac{1}{2}u_0^2
=
\frac{3}{2}u_0^2
=
1+\frac{1}{2}u_2^2+u_1^2+\frac{1}{2}u_0^2.
$$
Multiplying by $r$ and comparing with the definitions of $F_0,F_1,F_2$ proves
$$
F_i=a_is_i-\frac{1}{2}s_i^2
\qquad(i=0,1,2).
$$
To choose the locations, write
$
x_1=x_0-\alpha g_0,
\qquad
x_2=x_0-\beta g_0-\gamma g_1.
$
Making the reverse interpolation inequalities for the pairs $(0,1)$, $(0,2)$, and $(1,2)$ tight requires, respectively,
$
\alpha s_0^2=s_0^2+s_1^2,
\qquad
\beta s_0^2=s_0^2+s_1^2+s_2^2,
\qquad
\gamma s_1^2=s_1^2+s_2^2.
$
These conditions force
$
\alpha=1+\frac{s_1^2}{s_0^2},
\qquad
\beta=1+\frac{s_1^2+s_2^2}{s_0^2},
\qquad
\gamma=1+\frac{s_2^2}{s_1^2}.
$

Step 5: Build a smooth convex interpolant and close the lower bound
Include the minimizer data
$$
F_*=0,
\qquad
g_*=0,
\qquad
x_*=0.
$$
For all indices $i,j\in\{*,0,1,2\}$, the data from Step 4 satisfy
$$
F_i\geq
F_j+g_j^T(x_i-x_j)
+\frac{1}{2}\|g_i-g_j\|^2.
$$
For pairs involving $*$, the first required inequality follows from
$$
F_2-\frac{1}{2}s_2^2=r\left(1-\frac{1}{S}\right)>0,
$$
$$
F_1-\frac{1}{2}s_1^2
=
r\left(1+\frac{1}{2}u_2^2\right)>0,
$$
and
$$
F_0-\frac{1}{2}s_0^2=ru_0^2>0.
$$
The reverse inequalities are equalities because Step 4 gives
$$
F_i=a_is_i-\frac{1}{2}s_i^2
=
g_i^Tx_i-\frac{1}{2}s_i^2.
$$
For the adjacent pairs $(0,1)$ and $(1,2)$, the forward inequalities are equalities because the later gradient is orthogonal to the displacement, while the reverse inequalities are equalities because
$$
\alpha s_0^2=s_0^2+s_1^2,
\qquad
\gamma s_1^2=s_1^2+s_2^2.
$$
For the pair $(0,2)$, the forward inequality has slack $s_1^2$, and the reverse inequality is an equality because
$$
\beta s_0^2=s_0^2+s_1^2+s_2^2.
$$

To realize these finite data by an actual function, Put
$$
y_i=x_i-g_i,
\qquad
H_i=F_i-\frac{1}{2}\|g_i\|^2,
$$
including the index $*$. The preceding inequalities are equivalent to
$$
H_i\geq H_j+g_j^T(y_i-y_j).
$$
Define
$$
q(y)=
\max_j\left\{
H_j+g_j^T(y-y_j)
\right\},
$$
and its quadratic envelope
$$
f(x)=
\min_y\left\{
q(y)+\frac{1}{2}\|x-y\|^2
\right\}.
$$
Because $q$ is a finite maximum of affine functions, for every $x$ the envelope objective is continuous and coercive in $y$; its quadratic term makes it strongly convex. It therefore has a unique minimizer. At $y_i$, the $i$th affine term is active, so $g_i\in\partial q(y_i)$. Since $x_i=y_i+g_i$, the point $y_i$ satisfies the first-order condition for the envelope minimization at $x_i$, and
$$
f(x_i)=H_i+\frac{1}{2}\|g_i\|^2=F_i.
$$

For a general $x$, let $y(x)$ be the unique minimizer and put $G(x)=x-y(x)$. The first-order condition gives $G(x)\in\partial q(y(x))$. For $x,x'$ with corresponding $y,y'$ and $G,G'$, monotonicity of $\partial q$ gives
$$
(G-G')^T(y-y')\geq0.
$$
Since $x-x'=(y-y')+(G-G')$,
$$
\|G-G'\|^2
\leq
(G-G')^T(x-x')
\leq
\|G-G'\|\,\|x-x'\|,
$$
so
$$
\|G-G'\|\leq\|x-x'\|.
$$
Using $y(x)$ as a competitor in the definition of $f(x')$ gives
$$
f(x')
\leq
f(x)+G(x)^T(x'-x)+\frac{1}{2}\|x'-x\|^2.
$$
The same inequality with $x,x'$ interchanged and $x'=x+h$ gives
$$
(G(x+h)-G(x))^Th-\frac{1}{2}\|h\|^2
\leq
f(x+h)-f(x)-G(x)^Th
\leq
\frac{1}{2}\|h\|^2.
$$
Since $\|G(x+h)-G(x)\|\leq\|h\|$, the middle quantity is $O(\|h\|^2)$. Therefore $f$ is differentiable with $\nabla f=G$, and its gradient is $1$-Lipschitz. To see convexity directly, let $y,y'$ be the minimizers for $x,x'$ and let $t\in[0,1]$. The point $ty+(1-t)y'$ is an admissible competitor for $tx+(1-t)x'$, and convexity of $q$ together with convexity of the squared norm gives
$$
f\bigl(tx+(1-t)x'\bigr)
\leq
tf(x)+(1-t)f(x').
$$
In particular, $\nabla f(x_i)=g_i$. The affine term indexed by $*$ is zero, so $q\geq0$. The interpolation inequality with $i=*$ shows every other affine term is at most $0$ at $y_*=0$, so $q(0)=0$. Taking $y=0$ in the envelope gives $f(0)=0$, which is the minimum value.

The constructed $x_1$ lies in $x_0+\operatorname{span}\{g_0\}$ and has $g_1^Tg_0=0$, so convexity makes it an exact minimizer on that line. Likewise $x_2$ lies in $x_0+\operatorname{span}\{g_0,g_1\}$ and $g_2$ is orthogonal to both spanning gradients, so it is an exact minimizer on that plane. Also $\|x_0-x_*\|=1$ and
$$
f(x_2)-f_*=F_2=r.
$$
This matches the upper bound from Step 3.
Final Answer: $\boxed{\frac{2}{(1+\sqrt{13+4\sqrt{5}})^2}}$

---

## Answer

$\frac{2}{(1+\sqrt{13+4\sqrt{5}})^2}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- smooth convex interpolation
- exact span search
- orthogonal gradients
- nested extremal inequalities
- quadratic envelope interpolation

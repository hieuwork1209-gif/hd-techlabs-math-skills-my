## Steps

Step 1: Derive the smooth-convex interpolation inequality used in the upper bound
Let $f:\mathbb R^d\to\mathbb R$ be convex with $1$-Lipschitz gradient, and write $g(x)=\nabla f(x)$. The Lipschitz condition gives the descent inequality
$$
f(y)\leq f(x)+g(x)^T(y-x)+\frac{1}{2}\|y-x\|^2.
$$
Indeed, with $d=y-x$,
$$
f(y)-f(x)-g(x)^Td
=
\int_0^1\bigl(g(x+td)-g(x)\bigr)^Td\,dt
\leq
\int_0^1 t\|d\|^2\,dt.
$$

For arbitrary $u,v$, set
$$
\psi(z)=f(z)-g(v)^Tz.
$$
Then $\psi$ is convex and $1$-smooth, while $\nabla\psi(v)=0$, so $v$ minimizes $\psi$. Apply the descent inequality to $\psi$ at $u$ with the point
$$
u-\nabla\psi(u).
$$
This gives
$$
\psi\bigl(u-\nabla\psi(u)\bigr)
\leq
\psi(u)-\frac{1}{2}\|\nabla\psi(u)\|^2.
$$
Since $\psi(v)$ is no larger than the left side,
$$
f(u)\geq
f(v)+g(v)^T(u-v)
+\frac{1}{2}\|g(u)-g(v)\|^2.
$$
This is the interpolation inequality needed for the one-step analysis. It also shows that the worst-case quantity is finite: $\|g(x_0)\|\leq\|x_0-x_*\|\leq1$, so $\|x_1-x_*\|\leq1+h$, while the descent inequality applied from $x_*$ to $x_1$ gives
$
f(x_1)-f_*\leq\frac{1}{2}\|x_1-x_*\|^2.
$

Step 2: Construct two lower-bound instances valid for every step size
Let
$$
W(h)=
\sup\left\{
f(x_1)-f_*:
x_1=x_0-h\nabla f(x_0),\ 
f\in\mathcal F_d,\ 
\|x_0-x_*\|\leq1
\right\},
$$
where $\mathcal F$ is the class from the problem.

First take the one-dimensional quadratic
$$
f_Q(x)=\frac{1}{2}x^2,
\qquad
x_0=1.
$$
Then $x_*=0$ and
$$
x_1=1-h,
$$
so
$$
W(h)\geq\frac{1}{2}(1-h)^2.
$$

For the second instance, let $a\in(0,1]$ and define
$$
f_a(x)=
\begin{cases}
\frac{1}{2}x^2,& |x|\leq a,\\
a|x|-\frac{1}{2}a^2,& |x|\geq a.
\end{cases}
$$
Its derivative is the clipping map
$$
f_a'(x)=\max\{-a,\min\{x,a\}\},
$$
which is nondecreasing and $1$-Lipschitz. Therefore $f_a$ is convex and belongs to $\mathcal F_1$, with minimizer $0$.

Choose
$$
a=\frac{1}{1+2h},
\qquad
x_0=1.
$$
Then
$$
x_1=1-ha=\frac{1+h}{1+2h}>a,
$$
and therefore
$$
f_a(x_1)
=
ax_1-\frac{1}{2}a^2
=
\frac{1}{2(1+2h)}.
$$
Therefore
$
W(h)\geq
\frac{1}{2}
\max\left\{(1-h)^2,\frac{1}{1+2h}\right\}.
$$

Step 3: Locate the only possible minimizing step
The lower bound from Step 2 already forces a universal barrier. If
$$
0<h<\frac{3}{2},
$$
then
$$
\frac{1}{1+2h}>\frac{1}{4},
$$
so $W(h)>\frac{1}{8}$. If
$$
h>\frac{3}{2},
$$
then
$$
(1-h)^2>\frac{1}{4},
$$
so again $W(h)>\frac{1}{8}$.

At
$$
h=\frac{3}{2},
$$
the two lower-bound branches agree:
$$
(1-h)^2=\frac{1}{1+2h}=\frac{1}{4}.
$$
Therefore every step size satisfies
$$
W(h)\geq\frac{1}{8},
$$
and equality can occur only at $h=\frac{3}{2}$. The matching upper bound must hold for every function in the class.

Step 4: Prove the matching upper bound at the candidate step
Fix $h=\frac{3}{2}$ and an arbitrary admissible function and starting point. Write
$$
f_i=f(x_i),
\qquad
g_i=\nabla f(x_i),
\qquad
d=x_0-x_*.
$$
Since $x_*$ is a minimizer, $\nabla f(x_*)=0$, and
$$
x_1=x_0-\frac{3}{2}g_0.
$$

Apply the inequality from Step 1 to the pairs $(x_0,x_1)$, $(x_*,x_0)$, and $(x_*,x_1)$. The three quantities
$$
A=f_1-f_0+g_1^T(x_0-x_1)+\frac{1}{2}\|g_0-g_1\|^2,
$$
$$
B=f_0-f_*+g_0^T(x_*-x_0)+\frac{1}{2}\|g_0\|^2,
$$
and
$$
C=f_1-f_*+g_1^T(x_*-x_1)+\frac{1}{2}\|g_1\|^2
$$
are all nonpositive.

Now use $x_0-x_1=\frac{3}{2}g_0$ and
$$
x_1-x_*=d-\frac{3}{2}g_0.
$$
After the function values cancel,
$$
\frac{1}{2}(A+B+C)-(f_1-f_*)
=
\frac{1}{2}\|g_0+g_1\|^2
-\frac{1}{2}d^T(g_0+g_1).
$$
Completing the square gives the exact identity
$$
f_1-f_*
=
\frac{1}{2}(A+B+C)
+\frac{1}{8}\|d\|^2
-\frac{1}{2}
\left\|
\frac{1}{2}d-g_0-g_1
\right\|^2.
$$
Because $A,B,C\leq0$,
$$
f_1-f_*
\leq
\frac{1}{8}\|x_0-x_*\|^2
\leq
\frac{1}{8}.
$$
Therefore
$
W\left(\frac{3}{2}\right)\leq\frac{1}{8}.
$$

Step 5: Match the lower and upper bounds
The quadratic and clipped-quadratic instances in Step 2 both give value $\frac{1}{8}$ when $h=\frac{3}{2}$, while Step 4 proves that no admissible function can give a larger value. Therefore
$$
W\left(\frac{3}{2}\right)=\frac{1}{8}.
$$
Step 3 shows that every other positive step size has strictly larger worst-case value. The requested pair is
$$
\left(h_*,W_*\right)
=
\left(\frac{3}{2},\frac{1}{8}\right).
$$
Final Answer: $\boxed{\left(\frac{3}{2},\frac{1}{8}\right)}$

---

## Answer

$\left(\frac{3}{2},\frac{1}{8}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- smooth convex optimization
- gradient descent
- smooth convex interpolation
- worst-case lower bounds
- square completion certificate

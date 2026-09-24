## Steps

Step 1: Put every equilibrium into one common cubic
For $\kappa>0$, consider
$$
\dot x_i=x_i-x_i^3+\kappa(2x_i-x_j-x_k),
\qquad
\{i,j,k\}=\{1,2,3\}.
$$
Let
$$
S=x_1+x_2+x_3.
$$
Then
$$
\dot x_i=(1+3\kappa)x_i-x_i^3-\kappa S.
$$
At an equilibrium, every coordinate is therefore a real root of
$$
p_S(t)=t^3-(1+3\kappa)t+\kappa S.
$$
The Jacobian at an equilibrium is
$$
J=
\operatorname{diag}(d_1,d_2,d_3)
-\kappa
\begin{pmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{pmatrix},
\qquad
d_i=1+3\kappa-3x_i^2.
$$

The system is also a gradient flow,
$
\dot x=-\nabla V(x),
$
for
$
V(x)
=
\sum_{i=1}^3
\left(
\frac{x_i^4}{4}-\frac{x_i^2}{2}
\right)
-
\frac{\kappa}{2}
\sum_{1\leq i<j\leq3}(x_i-x_j)^2.
$
Along every trajectory,
$
\dot V
=
\nabla V\cdot\dot x
=
-\|\nabla V\|_2^2
\leq0.
$
This will be used only at the nonhyperbolic synchronized threshold.

Step 2: Classify the possible equilibrium shapes
If all coordinates are equal, say $x_1=x_2=x_3=s$, then the coupling vanishes and
$$
s-s^3=0.
$$
The synchronized equilibria are
$$
(0,0,0),
\qquad
(1,1,1),
\qquad
(-1,-1,-1).
$$

If the three coordinates are distinct, they are the three distinct roots of $p_S$. Since $p_S$ has no quadratic term, their sum is $0$. Therefore $S=0$, and
$$
p_0(t)=t\bigl(t^2-(1+3\kappa)\bigr).
$$
The all-distinct equilibria are the six permutations of
$$
\left(
-\sqrt{1+3\kappa},
0,
\sqrt{1+3\kappa}
\right).
$$
At the coordinate equal to $0$, the corresponding diagonal entry is $1+3\kappa$. Testing the Jacobian quadratic form on that coordinate vector gives
$$
e_i^{T}Je_i
=
1+3\kappa-\kappa
=
1+2\kappa>0.
$$
Since $J$ is symmetric, this positive Rayleigh quotient implies a positive Jacobian eigenvalue, so every all-distinct equilibrium is unstable.

The only remaining possibility is exactly two equal coordinates. By permutation symmetry write
$$
x_1=x_2=p,
\qquad
x_3=q,
\qquad
p\neq q.
$$

Step 3: Parametrize every two-equal branch
Subtracting the equilibrium equations for $p$ and $q$ gives
$$
(q-p)
\left(
1+3\kappa-p^2-pq-q^2
\right)
=0.
$$
Since $p\neq q$,
$$
p^2+pq+q^2=1+3\kappa.
$$
The equation for a coordinate equal to $p$ is
$$
(1+\kappa)p-p^3-\kappa q=0.
$$
If $p=0$, this forces $q=0$, contrary to $p\neq q$. Set
$
t=\frac{q}{p}.
$
The two displayed equations become
$$
p^2(1+t+t^2)=1+3\kappa,
$$
$$
p^2=1+\kappa-\kappa t.
$$
Eliminating $p^2$ yields
$$
\kappa(t^3+2)=t(t+1),
$$
so
$$
\kappa(t)=\frac{t(t+1)}{t^3+2},
\qquad
p^2=\frac{t+2}{t^3+2}.
$$

The simultaneous conditions $\kappa>0$ and $p^2>0$ give exactly
$$
t\in
\left(-\sqrt[3]{2},-1\right)
\cup
(0,\infty).
$$

Step 4: Determine which two-equal branches are stable
Let
$$
d_p=1+3\kappa-3p^2,
\qquad
d_q=1+3\kappa-3q^2.
$$
The antisymmetric perturbation $(1,-1,0)$ is an eigenvector of $J$ with eigenvalue $d_p$. Substituting the formulas from Step 3 gives
$$
d_p
=
\frac{(t-1)(t+2)^2}{t^3+2},
$$
$$
d_q
=
-\frac{(t-1)(t+2)(2t+1)}{t^3+2}.
$$

On the subspace of perturbations $(u,u,v)$, the Jacobian is represented by
$$
M=
\begin{pmatrix}
d_p-2\kappa&-\kappa\\
-2\kappa&d_q-\kappa
\end{pmatrix}.
$$
Set
$$
F(t)=t^4+2t^3-4t-2.
$$
The trace and determinant start as
$
\operatorname{tr}M
=
d_p+d_q-3\kappa,
$
$
\det M
=
(d_p-2\kappa)(d_q-\kappa)-2\kappa^2
=
d_pd_q-\kappa d_p-2\kappa d_q.
$
Substituting the displayed formulas for $d_p,d_q,\kappa$ and collecting the common denominator gives
$
\operatorname{tr}M
=
-\frac{t^3+3t^2+2}{t^3+2},
$
$
\det M
=
-\frac{2(t-1)(t+2)F(t)}{(t^3+2)^2}.
$

First take
$$
-\sqrt[3]{2}<t<-1.
$$
Then $t^3+2>0$, $t-1<0$, and $t+2>0$, so $d_p<0$. Also
$$
t^3+3t^2+2
>
-2+3+2
=
3,
$$
so $\operatorname{tr}M<0$.

To determine the determinant, put $s=-t\in(1,\sqrt[3]{2})$. Then
$$
F(-s)=s^4-2s^3+4s-2.
$$
Its derivative is
$$
4s^3-6s^2+4
=
2(2s^3-3s^2+2).
$$
The expression in parentheses has derivative $6s(s-1)>0$ and value $1$ at $s=1$. It follows that $F(-s)>F(-1)=1$. Therefore $\det M>0$, and all three Jacobian eigenvalues are negative.

Now take $t>0$. If $t>1$, then $d_p>0$, so the equilibrium is unstable. If $0<t<1$, then
$$
t^4+2t^3<3t,
$$
so
$$
F(t)<-t-2<0.
$$
The determinant formula then gives $\det M<0$, so this branch is also unstable.

A two-equal equilibrium is asymptotically stable exactly when
$$
-\sqrt[3]{2}<t<-1.
$$

Step 5: Count the stable equilibria for each coupling
Differentiate the branch parameter:
$$
\kappa'(t)
=
-\frac{F(t)}{(t^3+2)^2}.
$$
Step 4 gives $F(t)>0$ on
$$
\left(-\sqrt[3]{2},-1\right),
$$
so $\kappa(t)$ is strictly decreasing there. Also,
$$
\lim_{t\to-\sqrt[3]{2}^{+}}\kappa(t)=\infty,
\qquad
\lim_{t\to-1^{-}}\kappa(t)=0.
$$
Every $\kappa>0$ therefore has exactly one stable two-equal branch parameter $t$. There are three choices for the exceptional coordinate $q$ and two choices for the sign of $p$, giving exactly six stable nonsynchronized equilibria for every $\kappa>0$.

It remains to count the synchronized equilibria. At $(\pm1,\pm1,\pm1)$ the Jacobian has eigenvalue $-2$ in the synchronized direction and the double transverse eigenvalue
$$
-2+3\kappa.
$$
Therefore both synchronized equilibria are asymptotically stable for
$$
0<\kappa<\frac{2}{3},
$$
and unstable for $\kappa>2/3$.

At $\kappa=2/3$ the transverse linearization vanishes, so the nonlinear terms must be checked. For the potential in Step 1, write
$$
x_i=1+u_i,
\qquad
u_1+u_2+u_3=0.
$$
For
$
W(x)=\frac{x^4}{4}-\frac{x^2}{2},
$
one has
$
W(1+u)-W(1)
=
u^2+u^3+\frac{u^4}{4}.
$
Also, when $u_1+u_2+u_3=0$,
$
\sum_{1\leq i<j\leq3}(u_i-u_j)^2
=
3\sum_{i=1}^3u_i^2.
$
At $\kappa=2/3$, the quadratic terms therefore cancel and
$
V(1+u)-V(1,1,1)
=
\sum_{i=1}^3u_i^3
+
\frac14\sum_{i=1}^3u_i^4.
$
Taking
$$
(u_1,u_2,u_3)=(\varepsilon,\varepsilon,-2\varepsilon)
$$
gives
$$
V(1+u)-V(1,1,1)
=
-6\varepsilon^3+\frac{9}{2}\varepsilon^4<0
$$
for all sufficiently small $\varepsilon>0$. Since $V$ is nonincreasing along trajectories, $(1,1,1)$ cannot be asymptotically stable. By the symmetry $x\mapsto-x$, neither can $(-1,-1,-1)$.

There are eight asymptotically stable equilibria when $0<\kappa<2/3$ and six when $\kappa\geq2/3$.
Final Answer: $\boxed{N(\kappa)=6+2\mathbf{1}_{\{\kappa<2/3\}}}$

---

## Answer

$N(\kappa)=6+2\mathbf{1}_{\{\kappa<2/3\}}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Function or mapping

---

## Solution Concepts

- gradient dynamical systems
- symmetry-breaking equilibria
- rank-one Jacobian structure
- branch parametrization
- local bifurcation stability

---

## Black-Box Audit — no issues found

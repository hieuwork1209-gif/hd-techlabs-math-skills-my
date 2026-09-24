## Steps

Step 1: Reduce all equilibria to three coordinate patterns
Let
$$
S=x_1+x_2+x_3.
$$
The system can be written as
$$
\dot x_i
=
(1+3\kappa)x_i-x_i^3-\kappa S.
$$
Every coordinate of an equilibrium is therefore a real root of the same cubic
$$
p_S(z)
=
z^3-(1+3\kappa)z+\kappa S.
$$
A cubic has at most three distinct roots, so every equilibrium is of one of three types: all coordinates equal, all three coordinates distinct, or exactly two coordinates equal.

If all coordinates equal $s$, the coupling vanishes and
$$
s-s^3=0.
$$
This gives the three synchronized equilibria
$$
(0,0,0),
\qquad
(1,1,1),
\qquad
(-1,-1,-1).
$$

If all three coordinates are distinct, they are the three roots of $p_S$. Their sum is $0$ because $p_S$ has no quadratic term, but their sum is also $S$. Therefore $S=0$, and the roots are
$$
0,
\qquad
\sqrt{1+3\kappa},
\qquad
-\sqrt{1+3\kappa}.
$$
This gives six all-distinct equilibria for every $\kappa>0$.

It remains to classify equilibria with exactly two equal coordinates. By permutation symmetry write
$$
x_1=x_2=p,
\qquad
x_3=q,
\qquad
p\neq q.
$$

Step 2: Parametrize every two-equal equilibrium
Subtracting the equilibrium equations for $p$ and $q$ gives
$$
(q-p)
\left(
1+3\kappa-p^2-pq-q^2
\right)
=
0.
$$
Since $p\neq q$,
$$
p^2+pq+q^2
=
1+3\kappa.
$$
The equation for a coordinate equal to $p$ is
$$
(1+\kappa)p-p^3-\kappa q
=
0.
$$
If $p=0$, then $q=0$, contradicting $p\neq q$. Set
$$
t=\frac{q}{p}.
$$
The two relations become
$$
p^2(1+t+t^2)
=
1+3\kappa,
$$
$$
p^2
=
1+\kappa-\kappa t.
$$
Eliminating $p^2$ gives
$$
\kappa(t^3+2)
=
t(t+1),
$$
so
$$
\kappa(t)
=
\frac{t(t+1)}{t^3+2},
\qquad
p^2
=
\frac{t+2}{t^3+2}.
$$
The conditions $\kappa>0$ and $p^2>0$ are equivalent to
$$
t\in
\left(-\sqrt[3]{2},-1\right)
\cup
(0,\infty).
$$
For every admissible $t\neq1$, the sign of $p$ gives two equilibria and the exceptional position of $q$ gives three permutations, so each such $t$ contributes six distinct equilibria. The value $t=1$ instead gives the already-counted synchronized equilibria $(1,1,1)$ and $(-1,-1,-1)$.

Step 3: Count the negative and positive two-equal branches
Differentiate the branch parameter:
$$
\kappa'(t)
=
-\frac{F(t)}{(t^3+2)^2},
\qquad
F(t)
=
t^4+2t^3-4t-2.
$$

On
$$
-\sqrt[3]{2}<t<-1,
$$
write $s=-t\in(1,\sqrt[3]{2})$. Then
$$
F(-s)
=
s^4-2s^3+4s-2.
$$
Its derivative is
$$
4s^3-6s^2+4
=
2(2s^3-3s^2+2).
$$
The expression in parentheses has derivative $6s(s-1)>0$ and value $1$ at $s=1$. It follows that $F(-s)>F(-1)=1$. Therefore $\kappa'(t)<0$ on the whole negative interval. Also
$$
\lim_{t\to-\sqrt[3]{2}^{+}}\kappa(t)
=
\infty,
\qquad
\lim_{t\to-1^{-}}\kappa(t)
=
0.
$$
Every $\kappa>0$ has exactly one negative branch parameter, contributing six equilibria.

For $t>0$, one has
$$
F(0)=-2,
\qquad
\lim_{t\to\infty}F(t)=\infty.
$$
Also,
$$
F'(t)=4t^3+6t^2-4,
\qquad
F''(t)=12t(t+1)>0.
$$
The derivative $F'$ is strictly increasing on $(0,\infty)$, so $F$ decreases once and then increases. It follows that $F$ has exactly one positive zero, call it $t_*$. The branch function $\kappa(t)$ increases on $(0,t_*)$ and decreases on $(t_*,\infty)$. Therefore
$$
K
:=
\max_{t>0}
\frac{t(t+1)}{t^3+2}
=
\kappa(t_*)
$$
is attained uniquely.

Since
$$
F(1)=-3<0,
$$
we have $t_*>1$, and
$$
K>\kappa(1)=\frac{2}{3}.
$$
For $0<\kappa<K$, there are exactly two positive solutions of $\kappa(t)=\kappa$; for $\kappa=K$ there is exactly one; for $\kappa>K$ there are none. At $\kappa=2/3$, one of the two positive solutions is $t=1$, which produces only the synchronized equilibria already counted.

The total number of distinct equilibria is therefore
$$
27
$$
exactly when
$$
0<\kappa<K,
\qquad
\kappa\neq\frac{2}{3}.
$$

Step 4: Determine which equilibrium branches are stable
For this smooth system, the linearization criterion reduces asymptotic stability of a hyperbolic equilibrium to negativity of all Jacobian eigenvalues. At an equilibrium the Jacobian is
$$
J
=
\operatorname{diag}(d_1,d_2,d_3)
-
\kappa
\begin{pmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{pmatrix},
\qquad
d_i=1+3\kappa-3x_i^2.
$$
At $(0,0,0)$ the synchronized eigenvalue is $1>0$, so the origin is unstable. At $(\pm1,\pm1,\pm1)$ the synchronized eigenvalue is $-2$ and the two transverse eigenvalues are
$$
-2+3\kappa.
$$
Both nonzero synchronized equilibria are asymptotically stable for $0<\kappa<2/3$ and unstable for $\kappa>2/3$.

Every all-distinct equilibrium has one coordinate equal to $0$. For the corresponding coordinate vector $e_i$,
$$
e_i^{T}Je_i
=
1+2\kappa>0.
$$
Since $J$ is symmetric, it has a positive eigenvalue, so all all-distinct equilibria are unstable.

For a two-equal equilibrium $(p,p,q)$, set
$$
d_p=1+3\kappa-3p^2,
\qquad
d_q=1+3\kappa-3q^2.
$$
The vector $(1,-1,0)$ is an eigenvector with eigenvalue
$$
d_p
=
\frac{(t-1)(t+2)^2}{t^3+2}.
$$
On the complementary invariant subspace of vectors $(u,u,v)$, the Jacobian is represented by
$$
M
=
\begin{pmatrix}
d_p-2\kappa&-\kappa\\
-2\kappa&d_q-\kappa
\end{pmatrix},
$$
where
$$
d_q
=
-\frac{(t-1)(t+2)(2t+1)}{t^3+2}.
$$
Substitution gives
$$
\operatorname{tr}M
=
-\frac{t^3+3t^2+2}{t^3+2},
$$
$$
\det M
=
-\frac{2(t-1)(t+2)F(t)}{(t^3+2)^2}.
$$

On the negative branch $-\sqrt[3]{2}<t<-1$, Step 3 gives $F(t)>0$. There $d_p<0$, the trace is negative, and the determinant is positive. All three Jacobian eigenvalues are negative, so all six equilibria on this branch are asymptotically stable.

For $t>1$, one has $d_p>0$, so that branch is unstable. For $0<t<1$,
$$
t^4+2t^3<3t,
$$
and therefore
$$
F(t)<-t-2<0.
$$
The displayed determinant is then negative, so this branch is also unstable. The six negative-branch equilibria are the only nonsynchronized stable equilibria.

Step 5: Combine multiplicity and stability
For $0<\kappa<2/3$, the six stable negative-branch equilibria are joined by the two stable synchronized equilibria, so there are at least eight asymptotically stable equilibria. For $\kappa>2/3$, the synchronized equilibria and every positive branch are unstable, while the negative branch contributes exactly six stable equilibria.

Step 3 shows that the system has exactly $27$ distinct equilibria exactly when
$$
0<\kappa<K,
\qquad
\kappa\neq\frac{2}{3},
$$
where
$$
K
=
\max_{t>0}
\frac{t(t+1)}{t^3+2}.
$$
Combining this with the stability count gives
$$
\frac{2}{3}
<
\kappa
<
K.
$$
Final Answer: $\boxed{\{\kappa>0:\frac23<\kappa<\max_{t>0}\frac{t(t+1)}{t^3+2}\}}$

---

## Answer

$\{\kappa>0:\frac23<\kappa<\max_{t>0}\frac{t(t+1)}{t^3+2}\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- symmetry-breaking equilibria
- branch parametrization
- saddle-node bifurcation
- rank-one Jacobian structure
- stability by invariant subspaces

---

## Black-Box Audit — no issues found

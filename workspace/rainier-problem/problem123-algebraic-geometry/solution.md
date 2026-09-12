## Steps

Step 1: Compute the genus of the symmetric fiber product
Let
$$
h=\gcd(r,2),
\qquad
\epsilon=\begin{cases}1,&4\mid r,\\0,&4\nmid r.\end{cases}
$$
Set
$$
F=\mathbb C(x),
\qquad
K=F(y,z),
$$
with
$$
y^r=x(x-1),
\qquad
z^r=x(x+1).
$$
The first Kummer extension is totally ramified at $x=1$, whereas the second is unramified there. Hence the two degree-$r$ cyclic extensions have trivial intersection over $F$, so
$$
[K:F]=r^2.
$$
Thus $C\to\mathbb P^1_x$ is Galois with group $(\mathbb Z/r\mathbb Z)^2$.

The branch points are $0,1,-1,\infty$. Their valuation pairs for the two radicands are
$$
(1,1),\qquad (1,0),\qquad (0,1),\qquad (-2,-2),
$$
so the inertia orders are
$$
r,\qquad r,\qquad r,\qquad \frac r h.
$$
For a Galois cover of degree $D$, a branch point of inertia order $e$ contributes $D-D/e$ to the ramification term. Therefore Riemann-Hurwitz gives
$$
2g(C)-2
=-2r^2+3(r^2-r)+(r^2-rh)
=2r^2-3r-rh,
$$
and hence
$$
g(C)=1+r^2-\frac{r(3+h)}2.
$$

Step 2: Locate the fixed points of the involution above $x=0$
The map
$$
\tau(x,y,z)=(-x,z,y)
$$
is an involution of $C$. A fixed point of $\tau$ must lie over a fixed point of $x\mapsto -x$, hence only above $x=0$ or $x=\infty$.

Near $x=0$, use the regular quotient
$$
q=\frac yz,
\qquad
q^r=\frac{x-1}{x+1}.
$$
There are exactly $r$ points of $C$ above $0$, and they are distinguished by the values
$$
q(0)=\alpha,
\qquad
\alpha^r=-1.
$$
Since $\tau(q)=q^{-1}$, such a point is fixed exactly when
$$
\alpha=\alpha^{-1},
\qquad
\alpha^r=-1.
$$
Thus $\alpha^2=1$. If $r$ is odd, the unique solution is $\alpha=-1$; if $r$ is even, there is no solution. Therefore the number of fixed points above $0$ is
$$
N_0=\begin{cases}1,&r\text{ odd},\\0,&r\text{ even}.
\end{cases}
$$

Step 3: Count the fixed points above infinity
First suppose $r$ is odd. There are $r$ points above infinity. The same quotient $q=y/z$ satisfies
$$
q^r=\frac{x-1}{x+1}\longrightarrow 1
$$
as $x\to\infty$, so these points are distinguished by $r$-th roots of unity. Again $\tau(q)=q^{-1}$. For odd $r$, the only $r$-th root of unity equal to its inverse is $1$. Hence
$$
N_\infty=1
$$
when $r$ is odd.

Now suppose $r=2s$ is even and put $t=1/x$. Define
$$
A=t y^s,
\qquad
B=t z^s.
$$
Then
$$
A^2=1-t,
\qquad
B^2=1+t.
$$
At a point above infinity, $A$ and $B$ therefore take independent limiting values in $\{\pm1\}$. Together with
$$
q=\frac yz,
\qquad
q^s=\frac AB,
$$
these data distinguish all $4s=2r$ points above infinity.

Under $\tau$ one has
$$
t\mapsto -t,
\qquad
(A,B,q)\mapsto(-B,-A,q^{-1}).
$$
A fixed point must therefore satisfy
$$
A=-B,
\qquad
q=q^{-1}.
$$
Thus $q=\pm1$, while $A/B=-1$ forces
$$
q^s=-1.
$$
If $s$ is odd, equivalently $r\equiv2\pmod4$, only $q=-1$ works, and each of the two sign choices $(A,B)=(1,-1),(-1,1)$ gives one fixed point. Hence $N_\infty=2$. If $s$ is even, equivalently $4\mid r$, neither $q=1$ nor $q=-1$ satisfies $q^s=-1$, so $N_\infty=0$. Therefore
$$
N_\infty=
\begin{cases}
1,&r\text{ odd},\\
2,&r\equiv2\pmod4,\\
0,&4\mid r.
\end{cases}
$$
Combining with Step 2, the total number of fixed points of $\tau$ is
$$
R=N_0+N_\infty=2(1-\epsilon).
$$

Step 4: Apply Riemann-Hurwitz to the quotient map
Let
$$
Q=C/\langle\tau\rangle.
$$
The quotient map $C\to Q$ has degree $2$, and its ramification points are exactly the $R$ fixed points of $\tau$. Hence
$$
2g(C)-2=2\bigl(2g(Q)-2\bigr)+R.
$$
Substituting the genus from Step 1 and $R=2(1-\epsilon)$ gives
$$
4g(Q)
=2g(C)+2-R
=2r^2-r(3+h)+2+2\epsilon.
$$
Therefore
$$
g(Q)=\frac{2r^2-r(3+h)+2+2\epsilon}{4}.
$$

Final Answer: $\boxed{\frac{2r^2-r(3+h)+2+2\epsilon}{4}}$

---

## Answer

$\frac{2r^2-r(3+h)+2+2\epsilon}{4}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- Kummer covers and inertia groups
- normalization and local branches
- fixed points of an involution
- Riemann-Hurwitz for quotient curves

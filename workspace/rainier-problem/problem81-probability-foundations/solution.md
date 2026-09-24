## Steps

Step 1: Reduce the collision probabilities to two symmetric power sums
Let the random latent probability vector be $Q=(Q_1,Q_2,Q_3)$, and for one realization $q=(q_1,q_2,q_3)$ define
$$
s_k(q)=q_1^k+q_2^k+q_3^k.
$$
Conditional on $Q=q$, the probability that the first $k$ observations are all equal is $s_k(q)$. Hence, with
$$
x=s_2(Q),
\qquad
y=s_3(Q),
$$
the hypotheses are
$$
\mathbb E x=\frac{1}{2},
\qquad
\mathbb E y=\frac{11}{36}.
$$

For a deterministic probability vector $q$, put
$$
e_2=q_1q_2+q_2q_3+q_3q_1,
\qquad
e_3=q_1q_2q_3.
$$
Since $q_1+q_2+q_3=1$,
$$
x=1-2e_2,
\qquad
y=1-3e_2+3e_3.
$$
Newton's identities give
$$
s_4=s_3-e_2s_2+e_3
$$
and
$$
s_5=s_4-e_2s_3+e_3s_2.
$$
Substituting
$$
e_2=\frac{1-x}{2},
\qquad
e_3=\frac{1-3x+2y}{6}
$$
and simplifying yields
$$
s_5(q)=\frac{5xy-5x+5y+1}{6}.
$$
Therefore, if
$$
T=\mathbb E[xy],
$$
then the desired five-fold collision probability is
$$
\mathbb P(X_1=X_2=X_3=X_4=X_5)
=
\frac{5T}{6}+\frac{1}{216}.
$$
It remains to find the sharp range of $T$.

Step 2: Derive a sharp lower certificate from the deterministic contact point
A deterministic latent vector matching the two prescribed collision probabilities would have
$$
e_2=\frac{1-x}{2}=\frac{1}{4}
$$
and
$$
e_3=\frac{1-3x+2y}{6}=\frac{1}{54}.
$$
Its three coordinates must therefore be the roots of
$$
z^3-z^2+\frac{1}{4}z-\frac{1}{54}
=
\left(z-\frac{2}{3}\right)
\left(z-\frac{1}{6}\right)^2.
$$
Thus the natural deterministic contact point is
$$
q_0=\left(\frac{2}{3},\frac{1}{6},\frac{1}{6}\right),
$$
up to permutation, and it has
$$
xy=\frac{1}{2}\cdot\frac{11}{36}=\frac{11}{72}.
$$

To certify that no latent mixing can lower this value, seek an affine minorant whose expectation depends only on the known means:
$$
F=xy+Ax+By+C.
$$
Writing $u=e_2$ and $v=e_3$ gives
$$
F
=
6u^2-6uv+(-2A-3B-5)u+(3B+3)v+A+B+C+1.
$$
The coefficient of $v$ should have a definite sign when $u$ is fixed. Setting
$$
B=-1
$$
removes the standalone $v$ term, leaving dependence on $v$ only through $-6uv$. To make the certificate sharp at $q_0$, impose $F(q_0)=0$ and tangency along the two-equal boundary
$
q(t)=(1-2t,t,t)
$
at $t=\frac{1}{6}$. Since at that point
$
x=\frac{1}{2},
\qquad
y=\frac{11}{36},
\qquad
x'=-2,
\qquad
y'=-\frac{5}{2},
$
the two conditions are
$
\frac{A}{2}+C=\frac{11}{72}
$
and
$
\frac{23}{36}-2A=0.
$
Thus
$
A=\frac{23}{72},
\qquad
C=-\frac{1}{144}.
$
Hence it remains to prove
$$
M:=144F=144xy+46x-144y-1\geq0.
$$

Using $x=1-2u$ and $y=1-3u+3v$,
$$
M=864u^2-864uv-380u+45.
$$
For fixed $u$, this expression decreases as $v$ increases. When $u=0$, we have $M=45$. For $u>0$, it is enough to check $M$ when $v=q_1q_2q_3$ is maximal subject to
$$
q_1+q_2+q_3=1,
\qquad
q_1q_2+q_2q_3+q_3q_1=u.
$$
If a maximizer lies on the boundary, then $v=0$ and
$
M=864u^2-380u+45>0,
$
because its discriminant is
$
380^2-4\cdot864\cdot45=-11120<0.
$ At an interior maximizer, Lagrange multipliers applied to $\log(q_1q_2q_3)$ show that either all three coordinates are equal or two are equal: subtracting the stationarity equations for $q_i$ and $q_j$ gives
$$
(q_i-q_j)\left(\mu-\frac{1}{q_iq_j}\right)=0.
$$
Thus a maximizing vector may be written
$$
(q_1,q_2,q_3)=(1-2t,t,t),
\qquad
0\leq t\leq\frac{1}{2},
$$
up to permutation.

Substitution gives
$$
M
=
(6t-1)^2
\left(45-220t+336t^2-144t^3\right).
$$
Put $w=2t$. The remaining factor has the nonnegative decomposition
$$
45-110w+84w^2-18w^3
=
45(1-w)^4
+70w(1-w)^3
+24w^2(1-w)^2
+w^4.
$$
Therefore $M\geq0$ for every probability vector $q$, and
$$
xy
\geq
y-\frac{23}{72}x+\frac{1}{144}.
$$
Taking expectations yields
$$
T
\geq
\frac{11}{36}
-\frac{23}{72}\cdot\frac{1}{2}
+\frac{1}{144}
=
\frac{11}{72}.
$$
The deterministic vector $q_0$ attains equality.

Step 3: Derive a sharp upper certificate from the simplex support strata
For the upper side, consider the three canonical probability vectors that are uniform on supports of sizes one, two, and three. Their $(x,y,xy)$ values are
$$
(1,1,1),
\qquad
\left(\frac{1}{2},\frac{1}{4},\frac{1}{8}\right),
\qquad
\left(\frac{1}{3},\frac{1}{9},\frac{1}{27}\right).
$$
There is a unique affine plane
$
xy=A+Bx+Cy
$
through these three points. Its coefficients satisfy
$
A+B+C=1,
$
$
A+\frac{B}{2}+\frac{C}{4}=\frac{1}{8},
$
and
$
A+\frac{B}{3}+\frac{C}{9}=\frac{1}{27}.
$
Solving gives
$$
A=\frac{1}{6},
\qquad
B=-1,
\qquad
C=\frac{11}{6}.
$$
Thus define the candidate majorant gap
$$
N=\frac{1}{6}-x+\frac{11}{6}y-xy.
$$

Write again $u=e_2$ and $v=e_3$. Substitution gives
$$
2N=3u(1-4u)+(12u+5)v.
$$
If $0\leq u\leq\frac{1}{4}$, both terms on the right are nonnegative.

Now assume $\frac{1}{4}\leq u\leq\frac{1}{3}$. Schur's degree-three inequality in this setting is
$$
1+9v-4u\geq0.
$$
For completeness, after ordering $q_1\geq q_2\geq q_3$, its left side equals
$$
\sum_{\mathrm{cyc}}q_1(q_1-q_2)(q_1-q_3),
$$
and grouping the first two terms gives
$$
(q_1-q_2)^2(q_1+q_2-q_3)
+
q_3(q_1-q_3)(q_2-q_3)
\geq0.
$$
Thus
$$
v\geq\frac{4u-1}{9}.
$$
Since $12u+5>0$,
$$
2N
\geq
3u(1-4u)
+
\frac{(12u+5)(4u-1)}{9}
=
-\frac{5(3u-1)(4u-1)}{9}
\geq0,
$$
because $u\leq\frac{1}{3}$. Therefore
$$
xy
\leq
\frac{1}{6}-x+\frac{11}{6}y.
$$
Taking expectations yields
$$
T
\leq
\frac{1}{6}
-\frac{1}{2}
+\frac{11}{6}\cdot\frac{11}{36}
=
\frac{49}{216}.
$$

This bound is attained by the random latent vector
$$
Q=
\begin{cases}
(1,0,0),&\text{with probability }\frac{1}{6},\\
\left(\frac{1}{2},\frac{1}{2},0\right),&\text{with probability }\frac{1}{3},\\
\left(\frac{1}{3},\frac{1}{3},\frac{1}{3}\right),&\text{with probability }\frac{1}{2}.
\end{cases}
$$
Indeed, the corresponding $(s_2,s_3)$ values are
$$
(1,1),
\qquad
\left(\frac{1}{2},\frac{1}{4}\right),
\qquad
\left(\frac{1}{3},\frac{1}{9}\right),
$$
so their weighted means are exactly $\frac{1}{2}$ and $\frac{11}{36}$, while
$$
\mathbb E[s_2(Q)s_3(Q)]
=
\frac{1}{6}
+\frac{1}{24}
+\frac{1}{54}
=
\frac{49}{216}.
$$

Step 4: Classify the endpoint equality cases and the support-size law
For the lower endpoint, the nonnegative gap $M$ from Step 2 must have expectation zero, so $M=0$ almost surely. In the proof of Step 2, for fixed $u>0$ the gap decreases strictly as $v$ increases, so equality requires $v$ to be maximal at that $u$. The maximizing configuration has two equal coordinates and may be written
$$
q=(1-2t,t,t).
$$
On this curve,
$$
M
=
(6t-1)^2
\left(45-220t+336t^2-144t^3\right).
$$
After writing $w=2t$, the second factor becomes
$$
45(1-w)^4
+70w(1-w)^3
+24w^2(1-w)^2
+w^4,
$$
which is strictly positive for $0\leq w\leq1$. Thus equality forces
$$
t=\frac{1}{6},
$$
so every lower-endpoint latent vector is a coordinate permutation of
$$
\left(\frac{2}{3},\frac{1}{6},\frac{1}{6}\right).
$$
Hence
$$
K:=|\{i:Q_i>0\}|=3
$$
almost surely at the lower endpoint.

For the upper endpoint, the nonnegative gap $N$ from Step 3 must likewise vanish almost surely. If $0\leq u\leq\frac{1}{4}$, then
$$
2N=3u(1-4u)+(12u+5)v
$$
is a sum of two nonnegative terms. Equality therefore gives either
$$
(u,v)=(0,0)
$$
or
$$
(u,v)=\left(\frac{1}{4},0\right),
$$
corresponding respectively to coordinate permutations of
$$
(1,0,0)
$$
and
$$
\left(\frac{1}{2},\frac{1}{2},0\right).
$$
If $\frac{1}{4}\leq u\leq\frac{1}{3}$, Step 3 gives
$$
2N
\geq
-\frac{5(3u-1)(4u-1)}{9}.
$$
Equality can occur only at $u=\frac{1}{4}$ or $u=\frac{1}{3}$. The first case is the two-point uniform vector already listed, while $u=\frac{1}{3}$ forces
$$
q=\left(\frac{1}{3},\frac{1}{3},\frac{1}{3}\right).
$$
Therefore every upper-endpoint latent vector has support size $1$, $2$, or $3$ and is uniform on its support.

Let
$$
p_k=\mathbb P(K=k)
$$
under an upper-endpoint law. The prescribed two-fold and three-fold collision probabilities become
$$
p_1+p_2+p_3=1,
$$
$$
p_1+\frac{p_2}{2}+\frac{p_3}{3}=\frac{1}{2},
$$
and
$$
p_1+\frac{p_2}{4}+\frac{p_3}{9}=\frac{11}{36}.
$$
Solving this linear system gives
$$
(p_1,p_2,p_3)
=
\left(\frac{1}{6},\frac{1}{3},\frac{1}{2}\right).
$$

Step 5: Assemble the interval and endpoint support profiles
Using
$$
\mathbb P(X_1=\cdots=X_5)
=
\frac{5T}{6}+\frac{1}{216},
$$
the bounds from Steps 2 and 3 give
$$
\frac{5}{6}\cdot\frac{11}{72}+\frac{1}{216}
=
\frac{19}{144}
$$
and
$$
\frac{5}{6}\cdot\frac{49}{216}+\frac{1}{216}
=
\frac{251}{1296}.
$$
Mixing a lower-endpoint law with an upper-endpoint law preserves the two prescribed collision constraints, so every intermediate five-fold collision probability is attainable. Step 4 shows that $K=3$ almost surely at the lower endpoint and that the upper-endpoint support-size probabilities are $(\frac{1}{6},\frac{1}{3},\frac{1}{2})$.

Thus the requested tuple consisting of the feasible interval, the lower-endpoint value of $K$, and the upper-endpoint distribution $(p_1,p_2,p_3)$ is
$$
\left(
\left[\frac{19}{144},\frac{251}{1296}\right],
3,
\left(\frac{1}{6},\frac{1}{3},\frac{1}{2}\right)
\right).
$$
Final Answer: $\boxed{([\frac{19}{144},\frac{251}{1296}],3,(\frac{1}{6},\frac{1}{3},\frac{1}{2}))}$
---

## Answer

$([\frac{19}{144},\frac{251}{1296}],3,(\frac{1}{6},\frac{1}{3},\frac{1}{2}))$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- latent categorical mixtures
- symmetric power sums
- newton identities
- sharp polynomial certificates
- equality case analysis

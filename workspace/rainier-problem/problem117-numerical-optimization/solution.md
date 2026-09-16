## Steps

Step 1: Reduce the two uncertainties to an effective penalty parameter
Let
$$
U=\frac{1}{\sqrt{2}}\begin{bmatrix}1&-1\\1&1\end{bmatrix},
\qquad
Q_{\lambda,\mu}=\lambda\begin{bmatrix}\mu&0\\0&\frac{4}{\mu}\end{bmatrix},
\qquad
R_{\lambda,\mu}=UQ_{\lambda,\mu}U^T.
$$
For a quadratic with Hessian $H$, the reflected proximal map is
$$
2P_{h,\rho}-I=(\rho I-H)(\rho I+H)^{-1}.
$$
Set
$$
t=\frac{\rho}{\lambda},
\qquad
s=\frac{\theta}{2}\in(0,1],
$$
and
$$
a=\frac{t-\mu}{t+\mu},
\qquad
b=\frac{t-\frac{4}{\mu}}{t+\frac{4}{\mu}},
\qquad
D=\operatorname{diag}(a,b).
$$
The two reflected proximal maps are $D$ and $UDU^T$, so one relaxed Douglas-Rachford step has error operator
$$
T_{t,\mu,s}=(1-s)I+sUDU^TD.
$$
As $\lambda$ ranges over $[\frac{1}{2},2]$, the effective penalty parameter ranges over
$$
t\in\left[\frac{\rho}{2},2\rho\right].
$$
Thus the robust contraction is the supremum of $\|T_{t,\mu,s}\|_2$ over
$$
t\in\left[\frac{\rho}{2},2\rho\right],
\qquad
\mu\in[1,4].
$$

Step 2: Force the unique penalty parameter by testing scales outside the balanced interval
Write
$$
M=UDU^TD.
$$
If $0<t\leq1$, choose $\mu=1$. Then $a,b\leq0$. Put $x=-a$ and $y=-b$, so $0\leq x<1$, $0<y<1$, and
$$
y=\frac{4-t}{4+t}\geq\frac{3}{5}.
$$
For $e_2=(0,1)^T$,
$$
Me_2=\frac{b}{2}\begin{bmatrix}a-b\\a+b\end{bmatrix}=:m.
$$
Hence
$$
\|m\|_2^2=\frac{y^2(x^2+y^2)}{2},
\qquad
m_2=\frac{y(x+y)}{2}.
$$
Because $x^2+y^2\leq x+y\leq(x+y)/y$, we have $\|m\|_2^2\leq m_2$. Therefore the convex quadratic
$$
\|(1-s)e_2+sm\|_2^2
$$
has nonpositive derivative at $s=1$, so it decreases on $0<s\leq1$. Consequently
$$
\|T_{t,1,s}\|_2
\geq\|T_{t,1,s}e_2\|_2
\geq\|Me_2\|_2
=\frac{y\sqrt{x^2+y^2}}{\sqrt{2}}
\geq\frac{y^2}{\sqrt{2}}
\geq\frac{9\sqrt{2}}{50}.
$$
Equality in the last two inequalities forces $t=1$ and $x=0$.

If $t\geq4$, again choose $\mu=1$. Now $0\leq b\leq a<1$ and
$$
a=\frac{t-1}{t+1}\geq\frac{3}{5}.
$$
For $e_1=(1,0)^T$,
$$
Me_1=\frac{a}{2}\begin{bmatrix}a+b\\a-b\end{bmatrix}=:n,
$$
so
$$
\|n\|_2^2=\frac{a^2(a^2+b^2)}{2},
\qquad
n_1=\frac{a(a+b)}{2}.
$$
Since $a(a^2+b^2)\leq a^2+b^2\leq a+b$, we have $\|n\|_2^2\leq n_1$. Therefore
$$
\|(1-s)e_1+sn\|_2^2
$$
is a convex quadratic whose derivative at $s=1$ is nonpositive, so it also decreases on $0<s\leq1$. Hence
$$
\|T_{t,1,s}\|_2
\geq\|Me_1\|_2
=\frac{a\sqrt{a^2+b^2}}{\sqrt{2}}
\geq\frac{a^2}{\sqrt{2}}
\geq\frac{9\sqrt{2}}{50},
$$
with strict inequality when $t>4$.

Therefore a robust contraction no larger than $9\sqrt{2}/50$ requires
$$
\left[\frac{\rho}{2},2\rho\right]\subseteq[1,4].
$$
The two intervals have the same multiplicative width $4$, so this containment forces
$$
\rho=2.
$$

Step 3: Force full relaxation at the balanced penalty
Set $\rho=2$. Then $t\in[1,4]$. At the uncertainty point $t=1$, $\mu=1$,
$$
a=0,
\qquad
b=-\frac{3}{5},
$$
and
$$
Me_2=\begin{bmatrix}-\frac{9}{50}\\[1mm]\frac{9}{50}\end{bmatrix}.
$$
Thus
$$
\|T_{1,1,s}e_2\|_2^2
=\left(\frac{9s}{50}\right)^2
+\left(1-\frac{41s}{50}\right)^2
=1-\frac{41}{25}s+\frac{881}{1250}s^2.
$$
Its derivative is
$$
-\frac{41}{25}+\frac{881}{625}s<0
\qquad(0<s\leq1).
$$
Hence this lower bound is strictly decreasing in $s$, and
$$
\mathcal C(2,2s)>
\frac{9\sqrt{2}}{50}
$$
whenever $s<1$. Therefore any minimizer attaining the lower bound from Step 2 must satisfy
$$
s=1,
\qquad
\theta=2.
$$

Step 4: Bound every remaining uncertainty pair by a logarithmic diamond
It remains to evaluate the whole rectangle
$$
t\in[1,4],
\qquad
\mu\in[1,4]
$$
at $s=1$. Then $T_{t,\mu,1}=M$, and direct multiplication gives
$$
\|M\|_F^2=\frac{(a^2+b^2)^2}{2}.
$$
Therefore
$$
\|M\|_2\leq\frac{a^2+b^2}{\sqrt{2}}.
$$
The reflection coefficients depend on the two multiplicative coordinates $t/\mu$ and $t\mu/4$, so define their logarithms by
$$
x=\frac{1}{2}\log\frac{t}{\mu},
\qquad
y=\frac{1}{2}\log\frac{t\mu}{4}.
$$
Then
$$
a=\tanh x,
\qquad
b=\tanh y.
$$
If $X=\log t$, $Y=\log\mu$, and $L=\log 4$, then
$$
x=\frac{X-Y}{2},
\qquad
y=\frac{X+Y-L}{2},
$$
so inversely
$$
X=x+y+\frac{L}{2},
\qquad
Y=-x+y+\frac{L}{2}.
$$
Thus $0\leq X,Y\leq L$ is equivalent to
$$
|x+y|\leq\frac{L}{2},
\qquad
|y-x|\leq\frac{L}{2}.
$$
Since
$$
\max\{|x+y|,|y-x|\}=|x|+|y|,
$$
the square $0\leq X,Y\leq L$ is exactly the diamond
$$
|x|+|y|\leq\log 2.
$$
For $u,v\geq0$, write $p=\tanh u$ and $q=\tanh v$. The addition formula gives
$$
\tanh^2(u+v)-\tanh^2u-\tanh^2v
=\frac{pq\left(2-(2+pq)(p^2+q^2)\right)}{(1+pq)^2}.
$$
On $0\leq u,v\leq\log 2$ we have $0\leq p,q\leq3/5$, so
$$
(2+pq)(p^2+q^2)
\leq\left(2+\frac{9}{25}\right)\frac{18}{25}
=\frac{1062}{625}<2.
$$
Hence
$$
\tanh^2u+\tanh^2v\leq\tanh^2(u+v),
$$
with equality only when $uv=0$. Taking $u=|x|$ and $v=|y|$ yields
$$
a^2+b^2
\leq\tanh^2(|x|+|y|)
\leq\tanh^2(\log 2)
=\frac{9}{25}.
$$
Therefore every uncertainty pair satisfies
$$
\|T_{t,\mu,1}\|_2\leq\frac{9\sqrt{2}}{50}.
$$

Step 5: Determine the exact worst-case set and state the robust optimum
Equality in Step 4 requires both
$$
|x|+|y|=\log 2
$$
and equality in the hyperbolic-tangent inequality. Since its bracket is strictly positive on the stated range, equality there forces $xy=0$. Thus
$$
(x,y)\in\{(\log 2,0),(-\log 2,0),(0,\log 2),(0,-\log 2)\}.
$$
Using
$$
\log t=x+y+\log 2,
\qquad
\log\mu=-x+y+\log 2,
$$
these four points are exactly
$$
(t,\mu)\in\{1,4\}\times\{1,4\}.
$$
At each of them one of $a,b$ is $0$ and the other has magnitude $3/5$, so $M$ has rank one and its operator norm equals its Frobenius norm $9\sqrt{2}/50$. Hence the bound is attained exactly at those four points.

Since $\rho=2$ and $t=\rho/\lambda$, the values $t=1,4$ correspond to $\lambda=2,\frac{1}{2}$, respectively. Therefore
$$
\mathcal W_*=\left\{\frac{1}{2},2\right\}\times\{1,4\}.
$$
Steps 2 and 3 also show that no other $\rho$ or $\theta$ can attain the same robust contraction, so the minimizing pair is unique.

Final Answer: $\boxed{\left(2,2,\frac{9\sqrt{2}}{50},\left\{\frac{1}{2},2\right\}\times\{1,4\}\right)}$

---

## Answer

$\left(2,2,\frac{9\sqrt{2}}{50},\left\{\frac{1}{2},2\right\}\times\{1,4\}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- robust parameter tuning
- relaxed Douglas-Rachford splitting
- proximal reflections
- logarithmic coordinate transform
- operator norm bounds

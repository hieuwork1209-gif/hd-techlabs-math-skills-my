## Steps

Step 1: Characterize the convex hull as a truncated moment body
Let
$$
K=\operatorname{conv}\{(t,t^2,t^3,t^4):0\leq t\leq1\}\subset\mathbb R^4.
$$
Write a point as $(a,b,c,d)$ and set $m_0=1,m_1=a,m_2=b,m_3=c,m_4=d$. Equivalently, points of $K$ are the first four moments of probability measures on $[0,1]$.

We use the degree-$4$ Markov-Lukacs factorization in the following exact form: a real polynomial $P$ of degree at most $4$ is nonnegative on $[0,1]$ if and only if
$$
P(t)=\sum_j q_j(t)^2+t(1-t)\sum_k r_k(t)^2,
$$
where every $q_j$ has degree at most $2$ and every $r_k$ has degree at most $1$.

Define
$$
H=\begin{pmatrix}
1&a&b\\
a&b&c\\
b&c&d
\end{pmatrix},
\qquad
G=\begin{pmatrix}
a-b&b-c\\
b-c&c-d
\end{pmatrix}.
$$
For $q(t)=q_0+q_1t+q_2t^2$ and $r(t)=r_0+r_1t$,
$$
L(q^2)=\begin{pmatrix}q_0&q_1&q_2\end{pmatrix}H
\begin{pmatrix}q_0\\q_1\\q_2\end{pmatrix},
$$
and
$$
L\bigl(t(1-t)r^2\bigr)=\begin{pmatrix}r_0&r_1\end{pmatrix}G
\begin{pmatrix}r_0\\r_1\end{pmatrix},
$$
where $L(t^j)=m_j$. Hence every point of $K$ satisfies $H\succeq0$ and $G\succeq0$.

Conversely, suppose $H\succeq0$ and $G\succeq0$. If an affine functional
$$
\ell(x_1,x_2,x_3,x_4)=\alpha_0+\alpha_1x_1+\cdots+\alpha_4x_4
$$
is nonnegative on the moment curve, then $P(t)=\alpha_0+\alpha_1t+\cdots+\alpha_4t^4$ is nonnegative on $[0,1]$. The displayed factorization and the two positive-semidefinite matrices give $\ell(a,b,c,d)=L(P)\geq0$. If $(a,b,c,d)$ were outside the compact convex set $K$, a separating affine functional could be shifted so that it is nonnegative on $K$ but negative at $(a,b,c,d)$, a contradiction. Therefore
$$
K=\{(a,b,c,d):H\succeq0,\ G\succeq0\}.
$$

Step 2: Obtain sharp nested intervals for the moments
The boundary has $4$-dimensional measure zero, so the volume may be computed on the interior. There $H$ and $G$ are positive definite in the relevant leading blocks. From
$$
b-a^2>0,
\qquad
a-b>0,
$$
we get
$$
0<a<1,
\qquad
a^2<b<a.
$$

The principal minor
$$
\det\begin{pmatrix}a&b\\b&c\end{pmatrix}>0
$$
gives
$$
c>L_3:=\frac{b^2}{a}.
$$
For fixed $a,b,c$, the Schur complement of the upper-left $2\times2$ block of $H$ gives the sharp lower bound
$$
d>L_4:=\frac{b^3-2abc+c^2}{b-a^2}.
$$
The determinant condition for $G$ gives the sharp upper bound
$$
d<U_4:=c-\frac{(b-c)^2}{a-b}.
$$
A direct subtraction factors as
$$
U_4-L_4=
\frac{(ac-b^2)(a^2-ab-ac+b^2-b+c)}{(a-b)(a^2-b)}.
$$
Since $ac-b^2>0$, $a-b>0$, and $a^2-b<0$, the interval for $d$ is nonempty exactly when
$$
a^2-ab-ac+b^2-b+c<0.
$$
Because
$$
a^2-ab-ac+b^2-b+c=(1-a)(c-U_3),
$$
where
$$
U_3:=b-\frac{(a-b)^2}{1-a},
$$
we obtain the exact nested description
$$
0<a<1,
\qquad
a^2<b<a,
\qquad
L_3<c<U_3,
\qquad
L_4<d<U_4.
$$

Step 3: Introduce intrinsic interval coordinates and factor the Jacobian
Let
$$
\Delta_2=a-a^2=a(1-a),
\qquad
p=\frac{b-a^2}{\Delta_2}.
$$
Thus $0<p<1$ and
$$
b=a^2+p\Delta_2.
$$
Next define
$$
\Delta_3=U_3-L_3,
\qquad
q=\frac{c-L_3}{\Delta_3}.
$$
Using the formulas for $L_3$ and $U_3$,
$$
\Delta_3
=\frac{(b-a^2)(a-b)}{a(1-a)}
=a(1-a)p(1-p).
$$
Hence $0<q<1$ and $c=L_3+q\Delta_3$.

Finally put
$$
\Delta_4=U_4-L_4,
\qquad
r=\frac{d-L_4}{\Delta_4}.
$$
The factors in Step 2 simplify after $c=L_3+q\Delta_3$:
$$
ac-b^2=a\Delta_3q,
$$
$$
a^2-ab-ac+b^2-b+c=-(1-a)\Delta_3(1-q),
$$
and
$$
(a-b)(a^2-b)=-a(1-a)\Delta_3.
$$
Therefore
$$
\Delta_4=\Delta_3q(1-q)
=a(1-a)p(1-p)q(1-q).
$$
Thus $(a,p,q,r)\in(0,1)^4$ parametrizes the interior of $K$.

The map is triangular in the sense that $b$ depends only on $a,p$, $c$ only on $a,p,q$, and $d$ only on $a,p,q,r$. Consequently its Jacobian determinant is
$$
\left|\frac{\partial(a,b,c,d)}{\partial(a,p,q,r)}\right|
=\Delta_2\Delta_3\Delta_4
=[a(1-a)]^3[p(1-p)]^2q(1-q).
$$

Step 4: Integrate the factored Jacobian
Hence
$$
\operatorname{Vol}_4(K)
=\int_0^1\int_0^1\int_0^1\int_0^1
[a(1-a)]^3[p(1-p)]^2q(1-q)\,dr\,dq\,dp\,da.
$$
The four variables separate. Using
$$
\int_0^1x^m(1-x)^m\,dx=\frac{(m!)^2}{(2m+1)!},
$$
for $m=3,2,1$, we get
$$
\int_0^1[a(1-a)]^3\,da=\frac{1}{140},
$$
$$
\int_0^1[p(1-p)]^2\,dp=\frac{1}{30},
$$
and
$$
\int_0^1q(1-q)\,dq=\frac{1}{6}.
$$
The $r$-integral equals $1$, so
$$
\operatorname{Vol}_4(K)=\frac1{140}\cdot\frac1{30}\cdot\frac1{6}=\frac1{25200}.
$$

Final Answer: $\boxed{\frac{1}{25200}}$

---

## Answer

$\frac{1}{25200}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- convex hulls of moment curves
- truncated moment matrices
- positive polynomial certificates
- Schur complements
- Jacobian change of variables

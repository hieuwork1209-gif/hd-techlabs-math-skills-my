## Steps

Step 1: Represent point evaluation in the Dirichlet energy space
Let
$$
V=
\left\{
u\in H_0^1(0,1):
\int_0^1xu(x)\,dx=0,
\int_0^1x^3u(x)\,dx=0
\right\},
$$
with inner product
$$
\langle u,v\rangle
=
\int_0^1u'(x)v'(x)\,dx.
$$
The requested sharp constant is the squared norm of the evaluation functional
$$
L(u)=u\left(\frac{1}{2}\right)
$$
on $V$.

For $a\in(0,1)$ define
$$
G_a(x)
=
\begin{cases}
x(1-a),&0\leq x\leq a,\\
a(1-x),&a\leq x\leq1.
\end{cases}
$$
The function $G_a$ is continuous, vanishes at $0$ and $1$, and has derivative
$$
G_a'(x)
=
\begin{cases}
1-a,&0<x<a,\\
-a,&a<x<1.
\end{cases}
$$
For every $u\in H_0^1(0,1)$,
$$
\begin{aligned}
\langle u,G_a\rangle
&=
(1-a)\int_0^a u'(x)\,dx
-a\int_a^1u'(x)\,dx\\
&=
(1-a)u(a)+a u(a)\\
&=
u(a).
\end{aligned}
$$
Thus $G_a$ is the energy-space representer of evaluation at $a$. In particular,
$$
G_{1/2}\left(\frac{1}{2}\right)
=
\left\|G_{1/2}\right\|^2
=
\frac{1}{4}.
$$

Step 2: Represent the two moment constraints
Let $h_1,h_3\in H_0^1(0,1)$ solve
$$
-h_1''=x,
\qquad
-h_3''=x^3.
$$
Integrating twice and imposing zero boundary values gives
$$
h_1(x)=\frac{x(1-x^2)}{6},
\qquad
h_3(x)=\frac{x(1-x^4)}{20}.
$$
Integration by parts, with all boundary terms equal to zero, gives
$$
\langle u,h_1\rangle
=
\int_0^1xu(x)\,dx
$$
and
$$
\langle u,h_3\rangle
=
\int_0^1x^3u(x)\,dx.
$$
Therefore
$$
V=
\left(\operatorname{span}\{h_1,h_3\}\right)^\perp.
$$

The Gram matrix of $h_1,h_3$ is
$$
M=
\begin{pmatrix}
\langle h_1,h_1\rangle & \langle h_1,h_3\rangle\\
\langle h_3,h_1\rangle & \langle h_3,h_3\rangle
\end{pmatrix}.
$$
Using the moment identities just obtained,
$$
\langle h_1,h_1\rangle
=
\int_0^1x h_1(x)\,dx
=
\frac{1}{45},
$$
$$
\langle h_1,h_3\rangle
=
\int_0^1x h_3(x)\,dx
=
\frac{1}{105},
$$
and
$$
\langle h_3,h_3\rangle
=
\int_0^1x^3 h_3(x)\,dx
=
\frac{1}{225}.
$$
Hence
$$
M=
\begin{pmatrix}
\frac{1}{45} & \frac{1}{105}\\
\frac{1}{105} & \frac{1}{225}
\end{pmatrix}.
$$
Its determinant is
$$
\frac{1}{45\cdot225}-\frac{1}{105^2}
=
\frac{4}{496125}>0,
$$
so $M$ is invertible.

Step 3: Project the evaluation representer onto the constrained subspace
Set
$$
G=G_{1/2}.
$$
The vector of inner products of $G$ with the two constraint representers is
$$
b=
\begin{pmatrix}
\langle G,h_1\rangle\\
\langle G,h_3\rangle
\end{pmatrix}
=
\begin{pmatrix}
h_1(1/2)\\
h_3(1/2)
\end{pmatrix}
=
\begin{pmatrix}
\frac{1}{16}\\
\frac{3}{128}
\end{pmatrix}.
$$
Let
$$
c=M^{-1}b.
$$
Since
$$
M^{-1}
=
\begin{pmatrix}
\frac{2205}{4} & -\frac{4725}{4}\\
-\frac{4725}{4} & \frac{11025}{4}
\end{pmatrix},
$$
we get
$$
c=
\begin{pmatrix}
\frac{3465}{512}\\
-\frac{4725}{512}
\end{pmatrix}.
$$
Define
$$
g=G-c_1h_1-c_3h_3.
$$
For $j\in\{1,3\}$,
$$
\langle g,h_j\rangle
=
\langle G,h_j\rangle
-
\sum_{k\in\{1,3\}}c_k\langle h_k,h_j\rangle
=
0
$$
because $Mc=b$. Hence $g\in V$.

For every $u\in V$,
$$
u\left(\frac{1}{2}\right)
=
\langle u,G\rangle
=
\langle u,g\rangle,
$$
because $u$ is orthogonal to $h_1$ and $h_3$. Cauchy-Schwarz now gives
$$
\left|u\left(\frac{1}{2}\right)\right|^2
\leq
\|g\|^2
\int_0^1u'(x)^2\,dx.
$$
Equality holds for every nonzero scalar multiple of $g$, so the sharp constant is exactly
$$
C=\|g\|^2.
$$

Step 4: Compute the sharp constant
Because $G-g=c_1h_1+c_3h_3$ is orthogonal to $g$,
$$
\|G\|^2
=
\|g\|^2
+
\|G-g\|^2.
$$
Equivalently,
$$
C
=
\|G\|^2-b^TM^{-1}b.
$$
From Step 1,
$$
\|G\|^2=\frac{1}{4}.
$$
Also,
$$
b^TM^{-1}b
=
\begin{pmatrix}
\frac{1}{16} & \frac{3}{128}
\end{pmatrix}
\begin{pmatrix}
\frac{3465}{512}\\
-\frac{4725}{512}
\end{pmatrix}
=
\frac{13545}{65536}.
$$
Therefore
$$
C
=
\frac{1}{4}
-
\frac{13545}{65536}
=
\frac{2839}{65536}.
$$
The projected representer $g$ attains equality, so this constant is sharp.
Final Answer: $\boxed{\frac{2839}{65536}}$

---

## Answer

$\frac{2839}{65536}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- reproducing kernels
- riesz representers
- orthogonal projections
- moment constraints
- sharp inequalities

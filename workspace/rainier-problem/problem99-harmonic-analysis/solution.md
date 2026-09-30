## Steps

Step 1: Convert positivity into a coefficient-vector problem

Write
$$
p(\theta)=1+2\operatorname{Re}\sum_{k=1}^{4}c_ke^{ik\theta}\geq0.
$$
The degree-$4$ Fejer-Riesz factorization gives
$$
p(\theta)=\left|q(e^{i\theta})\right|^2,
\qquad
q(z)=\sum_{j=0}^{4}a_jz^j.
$$
For completeness, in this finite-degree case it follows by applying root pairing to the Laurent polynomial associated with $p$: nonreal off-circle zeros occur in reciprocal-conjugate pairs, while zeros on the unit circle have even multiplicity because $p$ is nonnegative there. Choosing one zero from each reciprocal-conjugate pair and half of each unit-circle multiplicity gives the polynomial factor $q$.

Comparing Fourier coefficients yields
$$
\sum_{j=0}^{4}|a_j|^2=1,
\qquad
c_1=\sum_{j=0}^{3}a_{j+1}\overline{a_j},
\qquad
c_2=\sum_{j=0}^{2}a_{j+2}\overline{a_j}.
$$
Replacing $p(\theta)$ by $p(\theta+\phi)$ multiplies $c_k$ by $e^{ik\phi}$. Since $c_2=0$, choose $\phi$ so that $c_1=|c_1|$ is real and nonnegative.

Let $A,B$ be the Hermitian $5\times5$ matrices whose only nonzero off-diagonal entries are
$$
A_{j,j+1}=A_{j+1,j}=\frac12,
\qquad
B_{j,j+2}=B_{j+2,j}=\frac12.
$$
For $a=(a_0,\ldots,a_4)^T$,
$$
a^*Aa=c_1,
\qquad
a^*Ba=\operatorname{Re}c_2=0,
\qquad
a^*a=1.
$$
Thus the problem is to maximize $a^*Aa$ on the unit sphere subject to the quadratic constraint $a^*Ba=0$.

Step 2: Derive the sharp multiplier candidate

For any real $\mu$,
$$
a^*Aa=a^*(A+\mu B)a
$$
on the constraint set. Hence a sharp bound can be obtained from the largest eigenvalue of $A+\mu B$.

The reversal map
$$
(a_0,a_1,a_2,a_3,a_4)\mapsto(a_4,a_3,a_2,a_1,a_0)
$$
commutes with both $A$ and $B$, so $A+\mu B$ splits into symmetric and antisymmetric sectors. In orthonormal parity bases the two blocks are
$$
H_+(\mu)=
\begin{pmatrix}
0&\frac12&\frac{\sqrt2\mu}{2}\\
\frac12&\frac\mu2&\frac{\sqrt2}{2}\\
\frac{\sqrt2\mu}{2}&\frac{\sqrt2}{2}&0
\end{pmatrix},
\qquad
H_-(\mu)=
\begin{pmatrix}
0&\frac12\\
\frac12&-\frac\mu2
\end{pmatrix}.
$$
To make the multiplier bound capable of being attained by a vector with $B$-quadratic form $0$, seek a common eigenvalue $\lambda$ of the two parity blocks. Their characteristic equations at $\lambda$ are
$$
4\lambda^2+2\lambda\mu-1=0
$$
and
$$
4\lambda^3-2\lambda^2\mu-2\lambda\mu^2-3\lambda+\mu^3-2\mu=0.
$$
The first gives
$$
\mu=\frac1{2\lambda}-2\lambda.
$$
Substituting this into the second gives
$$
\left(8\lambda^3-4\lambda^2-4\lambda+1\right)
\left(8\lambda^3+4\lambda^2-4\lambda-1\right)=0.
$$

Set
$$
\lambda=\cos\frac{2\pi}{7}.
$$
Since
$$
1+2\cos\frac{2\pi}{7}
+2\cos\frac{4\pi}{7}
+2\cos\frac{6\pi}{7}=0,
$$
and
$$
\cos\frac{4\pi}{7}=2\lambda^2-1,
\qquad
\cos\frac{6\pi}{7}=4\lambda^3-3\lambda,
$$
we obtain
$$
P(\lambda):=8\lambda^3+4\lambda^2-4\lambda-1=0.
$$
Take from now on
$$
\mu=\frac1{2\lambda}-2\lambda.
$$

Step 3: Prove the multiplier gives a global upper bound

Consider
$$
M=\lambda I-A-\mu B.
$$
Put
$$
d=\lambda-\frac1{4\lambda}.
$$
Then
$$
M=
\begin{pmatrix}
\lambda&-\frac12&d&0&0\\
-\frac12&\lambda&-\frac12&d&0\\
d&-\frac12&\lambda&-\frac12&d\\
0&d&-\frac12&\lambda&-\frac12\\
0&0&d&-\frac12&\lambda
\end{pmatrix}.
$$
Let $K$ be its leading $3\times3$ principal block. Its leading principal minors are
$$
\lambda,
\qquad
\frac{4\lambda^2-1}{4},
\qquad
\frac{8\lambda^2-3}{16\lambda}.
$$
The first two are positive because $2\pi/7<\pi/3$. For the third, $P'(x)=24x^2+8x-4>0$ for $x\geq1/2$, while
$$
P\left(\sqrt{\frac38}\right)
=\frac12-\frac{5\sqrt6}{8}<0=P(\lambda).
$$
Hence $\lambda>\sqrt{3/8}$, so $K$ is positive definite.

Write $M$ in block form with leading block $K$. Direct block elimination gives the $2\times2$ Schur complement
$$
M/K=
-\frac{P(\lambda)Q(\lambda)}
{16\lambda^3(8\lambda^2-3)}
\begin{pmatrix}
1&-2\lambda\\
-2\lambda&4\lambda^2
\end{pmatrix},
$$
where
$$
Q(x)=8x^3-4x^2-4x+1.
$$
Since $P(\lambda)=0$, this Schur complement is zero. Therefore $M$ is positive semidefinite.

For every feasible coefficient vector,
$$
c_1=a^*Aa
=a^*(A+\mu B)a
\leq\lambda a^*a
=\lambda.
$$
Thus $|c_1|\leq\cos(2\pi/7)$.

Step 4: Construct an extremizer

Define the real vectors
$$
u=
\begin{pmatrix}
1\\
2(1+\lambda)\\
2(1+2\lambda)\\
2(1+\lambda)\\
1
\end{pmatrix},
\qquad
v=
\begin{pmatrix}
1\\
2\lambda\\
0\\
-2\lambda\\
-1
\end{pmatrix}.
$$
Using $P(\lambda)=0$ in the displayed matrix for $M$ gives
$$
Mu=Mv=0.
$$
The vectors have opposite reversal parity, so $u^*Bv=0$. Their $B$-quadratic forms are
$$
u^*Bu=4(\lambda^2+4\lambda+2),
\qquad
v^*Bv=-4\lambda^2.
$$
Set
$$
\tau=\frac{\sqrt{\lambda^2+4\lambda+2}}{\lambda},
\qquad
w=u+\tau v,
\qquad
a=\frac{w}{\|w\|_2}.
$$
Then $a^*Ba=0$, $Ma=0$, and $a^*a=1$. Since $Ma=0$,
$$
a^*(A+\mu B)a=\lambda,
$$
and the constraint $a^*Ba=0$ gives $a^*Aa=\lambda$.

Finally let
$$
q(z)=\sum_{j=0}^{4}a_jz^j,
\qquad
p(\theta)=|q(e^{i\theta})|^2.
$$
This $p$ is nonnegative, has constant Fourier coefficient $1$, has $c_2=0$, and has $c_1=\lambda$. Hence the upper bound is attained.

Final Answer: $\boxed{\cos\frac{2\pi}{7}}$

---

## Answer

$\cos\frac{2\pi}{7}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- Fejer-Riesz factorization
- Fourier coefficients
- Hermitian quadratic forms
- Lagrange multiplier certificate
- Schur complement

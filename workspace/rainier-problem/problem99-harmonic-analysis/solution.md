## Steps

Step 1: Convert positivity into a coefficient-vector problem

Write
$$
p(\theta)=1+2\operatorname{Re}\sum_{k=1}^{4}c_ke^{ik\theta}\geq0.
$$
The degree-$4$ Fejer-Riesz factorization says that a nonnegative trigonometric polynomial of degree at most $4$ can be written as
$$
p(\theta)=\left|q(e^{i\theta})\right|^2,
\qquad
q(z)=\sum_{j=0}^{4}a_jz^j.
$$
In this finite-degree setting, the factorization follows by pairing the zeros of the associated Laurent polynomial: zeros off the unit circle occur in reciprocal-conjugate pairs, while unit-circle zeros have even multiplicity because the trigonometric polynomial is nonnegative.

Comparing Fourier coefficients gives
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
Thus the problem is to maximize $a^*Aa$ on the unit sphere subject to $a^*Ba=0$.

Step 2: Derive the sharp multiplier candidate

For any real $\mu$,
$$
a^*Aa=a^*(A+\mu B)a
$$
on the constraint set. Hence any upper bound for the largest eigenvalue of $A+\mu B$ is also an upper bound for $c_1$.

The reversal map
$$
(a_0,a_1,a_2,a_3,a_4)\mapsto(a_4,a_3,a_2,a_1,a_0)
$$
commutes with $A$ and $B$. Therefore $A+\mu B$ splits into symmetric and antisymmetric sectors. In orthonormal parity bases the blocks are
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
To make equality compatible with the indefinite constraint $a^*Ba=0$, seek a top eigenspace containing both parity sectors. Thus require a common eigenvalue $\lambda$ of the two blocks. Their characteristic equations are
$$
4\lambda^2+2\lambda\mu-1=0
$$
and
$$
4\lambda^3-2\lambda^2\mu-2\lambda\mu^2-3\lambda+\mu^3-2\mu=0.
$$
The first equation gives
$$
\mu=\frac1{2\lambda}-2\lambda.
$$
Substitution into the second gives
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
together with
$$
\cos\frac{4\pi}{7}=2\lambda^2-1,
\qquad
\cos\frac{6\pi}{7}=4\lambda^3-3\lambda,
$$
we obtain
$$
P(\lambda):=8\lambda^3+4\lambda^2-4\lambda-1=0.
$$
Take
$$
\mu=\frac1{2\lambda}-2\lambda.
$$

Step 3: Prove the multiplier gives a global upper bound

It is enough to prove
$$
\lambda I-(A+\mu B)\succeq0.
$$
On the antisymmetric sector,
$$
\lambda I-H_-(\mu)=
\begin{pmatrix}
\lambda&-\frac12\\
-\frac12&\frac1{4\lambda}
\end{pmatrix},
$$
which is positive semidefinite because $\lambda>0$ and its determinant is $0$.

On the symmetric sector, consider $M_+=\lambda I-H_+(\mu)$. Its diagonal entries are
$$
\lambda,\qquad \frac{8\lambda^2-1}{4\lambda},\qquad \lambda.
$$
Its three principal minors of order $2$ are
$$
\frac{4\lambda^2-1}{2},
\qquad
\frac{4\lambda^2+2\lambda-1}{16\lambda^2},
\qquad
\frac{8\lambda^2-3}{4},
$$
where the middle expression uses $P(\lambda)=0$. Also
$$
\det M_+
=
-\frac{
\left(8\lambda^3-4\lambda^2-4\lambda+1\right)P(\lambda)
}{32\lambda^3}
=0.
$$
Now $2\pi/7<\pi/3$, so $\lambda>1/2$. Moreover,
$$
P\left(\sqrt{\frac38}\right)=\frac12-\frac{\sqrt6}{4}<0,
$$
while $P'(x)=24x^2+8x-4>0$ for $x\geq1/2$ and $P(\lambda)=0$. Hence
$$
\lambda>\sqrt{\frac38}.
$$
All principal minors of $M_+$ are therefore nonnegative, so $M_+\succeq0$. Consequently
$$
\lambda I-(A+\mu B)\succeq0.
$$
For every feasible coefficient vector,
$$
c_1=a^*Aa
=a^*(A+\mu B)a
\leq\lambda a^*a
=\lambda.
$$
Thus
$$
|c_1|\leq\cos\frac{2\pi}{7}.
$$

Step 4: Construct an extremizer

Define
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
With $M=\lambda I-A-\mu B$, direct multiplication gives
$$
Mv=0,
\qquad
Mu=\frac{P(\lambda)}{2\lambda}
\begin{pmatrix}
1\\1\\1\\1\\1
\end{pmatrix}
=0.
$$
The vector $u$ is symmetric under reversal and $v$ is antisymmetric. Since $B$ preserves these parity sectors,
$$
u^*Bv=0.
$$
Also
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
Then $a^*Ba=0$, $Ma=0$, and $a^*a=1$. Therefore
$$
a^*Aa=a^*(A+\mu B)a=\lambda.
$$

Finally define
$$
q(z)=\sum_{j=0}^{4}a_jz^j,
\qquad
p(\theta)=|q(e^{i\theta})|^2.
$$
This $p$ is nonnegative, has constant Fourier coefficient $1$, satisfies $c_2=0$, and has $c_1=\lambda$. Hence the bound is attained.

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
- Spectral multiplier certificate
- Parity decomposition

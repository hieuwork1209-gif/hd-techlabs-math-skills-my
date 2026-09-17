## Steps

Step 1: Convert the extremal Fourier problem to a compressed Rayleigh quotient
Let
$$
P(\theta)=1+2\sum_{k=1}^n a_k\cos(k\theta)\geq0.
$$
By the Fejer-Riesz factorization theorem, there are complex numbers $c_0,\ldots,c_n$ such that
$$
P(\theta)=\left|\sum_{j=0}^n c_j e^{ij\theta}\right|^2.
$$
Comparing the constant Fourier coefficient gives
$$
\sum_{j=0}^n|c_j|^2=1.
$$
Since $P(\pi)=0$, the factor itself vanishes at $-1$, so
$$
\sum_{j=0}^n(-1)^jc_j=0.
$$
Also the coefficient of $e^{i\theta}$ is
$$
a_1=\sum_{j=0}^{n-1}c_{j+1}\overline{c_j},
$$
which is real because $P$ is even.

Let $B$ be the real symmetric $(n+1)\times(n+1)$ matrix with
$$
B_{j,j+1}=B_{j+1,j}=\frac12
$$
for $0\leq j<n$ and all other entries zero, and let
$$
v=(1,-1,1,-1,\ldots,(-1)^n)^T.
$$
Then
$$
a_1=c^*Bc,
\qquad
\|c\|_2=1,
\qquad
v^*c=0.
$$
Conversely, a real maximizing vector $c$ for this constrained Rayleigh quotient produces an even nonnegative trigonometric polynomial by the displayed Fejer-Riesz form. Therefore the required maximum is exactly the largest eigenvalue of the compression of $B$ to $v^\perp$.

Step 2: Solve the odd-degree case by parity
The eigenvalues and real eigenvectors of $B$ are
$$
\lambda_k=\cos\frac{k\pi}{n+2},
\qquad
u^{(k)}_j=\sin\frac{(j+1)k\pi}{n+2},
$$
for $1\leq k\leq n+1$ and $0\leq j\leq n$.

Suppose $n$ is odd. Then
$$
v_{n-j}=-v_j,
$$
whereas the Perron eigenvector $u^{(1)}$ is symmetric:
$$
u^{(1)}_{n-j}=u^{(1)}_j.
$$
Hence
$$
v^Tu^{(1)}=0.
$$
Thus the largest eigenvalue of $B$ is already feasible for the constrained problem, and no larger value is possible. Therefore
$$
\max a_1=\lambda_1=\cos\frac{\pi}{n+2}
$$
when $n$ is odd.

Step 3: Derive and solve the even-degree secular equation
Now let $n=2m$. The vector $v$ is symmetric under reversal. The eigenvector for
$$
\lambda_2=\cos\frac{2\pi}{n+2}
$$
is antisymmetric, so it lies in $v^\perp$. Hence the top compressed eigenvalue is at least $\lambda_2$ and, by Cauchy interlacing, at most
$$
\lambda_1=\cos\frac{\pi}{n+2}.
$$

Seek a compressed eigenvalue $\lambda$ strictly between $\lambda_2$ and $\lambda_1$. If $c\in v^\perp$ is a corresponding eigenvector, then
$$
Bc-\lambda c
$$
is a nonzero multiple of $v$. Put
$$
D=\operatorname{diag}(1,-1,\ldots,1),
\qquad
y=Dc.
$$
Since $DBD=-B$ and $Dv=\mathbf1$, rescaling $c$ reduces the eigenvalue condition to
$$
(B+\lambda I)y=\mathbf1,
\qquad
\mathbf1^Ty=0.
$$
Write
$$
\lambda=\cos\theta,
\qquad
\frac{\pi}{n+2}<\theta<\frac{2\pi}{n+2}.
$$
The coordinates of $y$ satisfy
$$
y_{j-1}+2\lambda y_j+y_{j+1}=2
$$
with ghost boundary values $y_{-1}=y_{n+1}=0$.

Set
$$
y_*=\frac{1}{1+\lambda},
\qquad
z_j=y_j-y_*,
\qquad
w_j=(-1)^jz_j.
$$
Then
$$
w_{j-1}-2\lambda w_j+w_{j+1}=0,
$$
and because $n=2m$,
$$
w_{-1}=w_{n+1}=y_*.
$$
Thus
$$
w_j
=y_*\frac{\cos((j-m)\theta)}{\cos((m+1)\theta)}.
$$
Using the finite geometric-series identity
$$
\sum_{j=0}^{2m}(-1)^j\cos((j-m)\theta)
=\frac{\cos((m+\frac12)\theta)}{\cos(\theta/2)},
$$
the constraint $\mathbf1^Ty=0$ becomes
$$
(2m+1)\cos((m+1)\theta)\cos\frac\theta2
+\cos((m+\tfrac12)\theta)=0.
$$
Equivalently,
$$
F_n(\theta):=(n+1)\cos\frac{(n+3)\theta}{2}
+(n+3)\cos\frac{(n+1)\theta}{2}=0.
$$
At the left endpoint,
$$
F_n\!\left(\frac{\pi}{n+2}\right)
=2\sin\frac{\pi}{2(n+2)}>0,
$$
while at the right endpoint,
$$
F_n\!\left(\frac{2\pi}{n+2}\right)
=-2(n+2)\cos\frac{\pi}{n+2}<0.
$$
Moreover,
$$
F_n'(\theta)
=-(n+1)(n+3)
\sin\frac{(n+2)\theta}{2}\cos\frac\theta2<0
$$
throughout this interval. Hence there is a unique root $\theta_n$ there.

The value $\cos\theta_n$ is therefore a compressed eigenvalue strictly larger than $\lambda_2$. Interlacing says there can be at most one compressed eigenvalue above $\lambda_2$, so it is the largest one.

Step 4: Translate the compressed eigenvalue back to the trigonometric polynomial
In the odd case, the real Perron eigenvector from Step 2 lies in $v^\perp$. In the even case, Step 3 constructs a real eigenvector in $v^\perp$ for the largest compressed eigenvalue. Normalize either vector to have Euclidean norm $1$ and use its entries as the coefficients of
$$
q(z)=\sum_{j=0}^n c_jz^j.
$$
Then
$$
P(\theta)=|q(e^{i\theta})|^2
$$
is an even nonnegative trigonometric polynomial with constant coefficient $1$ and $P(\pi)=0$, and its first cosine coefficient equals the corresponding Rayleigh quotient. Thus both bounds are attained.

Final Answer: $\boxed{\begin{cases}\cos\frac{\pi}{n+2},&n\text{ odd},\\\cos\theta_n,&n\text{ even}.\end{cases}}$

---

## Answer

$\begin{cases}\cos\frac{\pi}{n+2},&n\text{ odd},\\\cos\theta_n,&n\text{ even}.\end{cases}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- nonnegative trigonometric polynomials
- Fejer-Riesz factorization
- constrained Rayleigh quotients
- tridiagonal spectral theory
- secular equations

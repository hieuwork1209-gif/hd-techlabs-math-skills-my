## Steps

Step 1: Isolate the new Toeplitz lag by a two-endpoint Schur complement
Let
$$
T_k=(c_{|i-j|})_{i,j=0}^{k-1},
\qquad
D_k=\det T_k.
$$
Thus
$$
D_1=1,
\qquad
D_2=1-r^2.
$$
Fix $k\ge2$ and suppose $T_k$ is positive definite. In $T_{k+1}$, separate the first and last coordinates from the middle $k-1$ coordinates. Write
$$
M=T_{k-1},
$$
$$
a=(c_1,\dots,c_{k-1})^T,
\qquad
b=(c_{k-1},\dots,c_1)^T.
$$
Then
$$
T_{k+1}=
\begin{pmatrix}
1&a^T&c_k\\
a&M&b\\
c_k&b^T&1
\end{pmatrix}.
$$
Because $M$ is Toeplitz, reversing coordinates preserves it, so
$$
a^TM^{-1}a=b^TM^{-1}b.
$$
Set
$$
\delta_k=1-a^TM^{-1}a
$$
and
$$
h_k=c_k-a^TM^{-1}b.
$$
The Schur complement of $M$ in $T_{k+1}$ is
$$
\begin{pmatrix}
\delta_k&h_k\\
h_k&\delta_k
\end{pmatrix}.
$$
Also, the leading $k\times k$ block gives
$$
D_k=D_{k-1}\delta_k.
$$
Therefore
$$
D_{k+1}
=D_{k-1}(\delta_k^2-h_k^2)
=\frac{D_k^2}{D_{k-1}}\left(1-\kappa_k^2\right),
$$
where
$$
\kappa_k=\frac{h_k}{\delta_k}.
$$
Positive definiteness is equivalent at this extension step to
$$
|\kappa_k|<1.
$$
Since $c_k$ occurs in $h_k$ with coefficient $1$, once the earlier lags are fixed, every value of $\kappa_k$ in $(-1,1)$ is obtained by a unique choice of $c_k$.

Step 2: Identify the fixed second reflection parameter
For $k=2$, we have
$$
M=(1),
\qquad
a=b=(r).
$$
Hence
$$
\delta_2=1-r^2,
\qquad
h_2=s-r^2,
$$
so
$$
\kappa_2=\frac{s-r^2}{1-r^2}.
$$
The hypotheses
$$
|r|<1,
\qquad
|s-r^2|<1-r^2
$$
are exactly what is needed to give
$$
D_2>0,
\qquad
|\kappa_2|<1.
$$
Thus the prescribed $3\times3$ Toeplitz block is positive definite, and the recursive extension from Step 1 is available.

Step 3: Factor the determinant into independent extension losses
From
$$
D_{k+1}
=\frac{D_k^2}{D_{k-1}}(1-\kappa_k^2),
$$
a direct induction gives
$$
D_n
=(1-r^2)^{n-1}
\prod_{k=2}^{n-1}(1-\kappa_k^2)^{n-k}.
$$
Indeed, the formula is correct for $n=2$, and substituting the formulas for $D_k$ and $D_{k-1}$ into the recurrence produces the exponent $n-k$ for the new factor.

The data $r,s$ fix only $\kappa_2$. For every $k\ge3$, the new Toeplitz lag $c_k$ is free, and Step 1 shows that it is equivalent to choosing an arbitrary
$$
\kappa_k\in(-1,1).
$$
Hence every factor with $k\ge3$ is at most $1$, with equality exactly when
$$
\kappa_k=0.
$$
Therefore
$$
D_n
\le
(1-r^2)^{n-1}(1-\kappa_2^2)^{n-2}.
$$

This bound is attained. Starting from the prescribed positive definite $T_3$, choose each successive lag $c_k$ so that
$$
h_k=0
$$
for $k=3,\dots,n-1$. Then the $2\times2$ Schur complement in Step 1 is
$$
\delta_k I_2>0,
$$
so every extension remains positive definite and has $\kappa_k=0$.

Step 4: Simplify the sharp value
Using
$$
\kappa_2=\frac{s-r^2}{1-r^2},
$$
we get
$$
1-\kappa_2^2
=
\frac{(1-r^2)^2-(s-r^2)^2}{(1-r^2)^2}.
$$
The numerator factors as
$$
(1-r^2)^2-(s-r^2)^2
=(1-s)(1+s-2r^2).
$$
Consequently
$$
\max\det T
=(1-r^2)^{n-1}
\left(
\frac{(1-s)(1+s-2r^2)}{(1-r^2)^2}
\right)^{n-2},
$$
which simplifies to
$$
\max\det T
=
\frac{\bigl((1-s)(1+s-2r^2)\bigr)^{n-2}}
{(1-r^2)^{n-3}}.
$$

Final Answer: $\boxed{\frac{\bigl((1-s)(1+s-2r^2)\bigr)^{n-2}}{(1-r^2)^{n-3}}}$

---

## Answer

$\frac{\bigl((1-s)(1+s-2r^2)\bigr)^{n-2}}{(1-r^2)^{n-3}}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- positive definite Toeplitz matrices
- Schur complements
- determinant maximization
- reflection parameters
- recursive matrix completion

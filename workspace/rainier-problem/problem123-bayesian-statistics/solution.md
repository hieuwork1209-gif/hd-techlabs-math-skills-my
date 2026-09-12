## Steps

Step 1: Express the posterior predictive probability through the next unknown moment
Let
$$
m_k=\mathbb E_\mu[\Theta^k].
$$
The calibration assumptions give
$$
m_0=1,\qquad m_1=\frac{1}{2},\qquad m_2=\frac{1}{3},\qquad m_3=\frac{1}{4},\qquad m_4=r.
$$
After four observed successes, Bayes' rule weights the prior by $\theta^4$, so
$$
p_\mu=\frac{m_5}{m_4}=\frac{m_5}{r}.
$$
Because a feasible prior is assumed to exist and $m_2=1/3$, we have $r=m_4>0$. Thus the problem is to determine the exact feasible interval for $m_5$ once the first five moments through $m_4=r$ are fixed.

Step 2: Apply the degree-five Hausdorff moment criterion
Use the degree-five Hausdorff moment criterion in the following exact form. Real numbers $m_0,\ldots,m_5$ with $m_0=1$ are the moments of a Borel probability measure on $[0,1]$ if and only if both matrices
$$
H_x=(m_{i+j+1})_{i,j=0}^{2}
$$
and
$$
H_{1-x}=(m_{i+j}-m_{i+j+1})_{i,j=0}^{2}
$$
are positive semidefinite. These are the quadratic-form matrices of
$$
\mathbb E\!\left[\Theta q(\Theta)^2\right]\geq0
$$
and
$$
\mathbb E\!\left[(1-\Theta)q(\Theta)^2\right]\geq0
$$
for every quadratic polynomial $q$.

Write $s=m_5$. Substituting the fixed moments gives
$$
H_x=
\begin{pmatrix}
\frac{1}{2}&\frac{1}{3}&\frac{1}{4}\\
\frac{1}{3}&\frac{1}{4}&r\\
\frac{1}{4}&r&s
\end{pmatrix}
$$
and
$$
H_{1-x}=
\begin{pmatrix}
\frac{1}{2}&\frac{1}{6}&\frac{1}{12}\\
\frac{1}{6}&\frac{1}{12}&\frac{1}{4}-r\\
\frac{1}{12}&\frac{1}{4}-r&r-s
\end{pmatrix}.
$$
The leading $2\times 2$ block of each matrix is positive definite, with determinant $1/72$. Therefore each $3\times 3$ matrix is positive semidefinite exactly when its scalar Schur complement is nonnegative, equivalently exactly when its determinant is nonnegative.

Step 3: Derive the exact feasible interval for the fifth moment
Expanding the first determinant along its first row gives
$$
\begin{aligned}
\det H_x
&=\frac{1}{2}\left(\frac{s}{4}-r^2\right)
-\frac{1}{3}\left(\frac{s}{3}-\frac{r}{4}\right)
+\frac{1}{4}\left(\frac{r}{3}-\frac{1}{16}\right)\\
&=\frac{8s-288r^2+96r-9}{576}.
\end{aligned}
$$
Hence $H_x\succeq0$ is equivalent to
$$
s\geq36r^2-12r+\frac{9}{8}.
$$
For the second matrix, expansion along the first row gives
$$
\begin{aligned}
\det H_{1-x}
&=\frac{1}{2}\left[\frac{r-s}{12}-\left(\frac{1}{4}-r\right)^2\right]
-\frac{1}{6}\left[\frac{r-s}{6}-\frac{1}{12}\left(\frac{1}{4}-r\right)\right]\\
&\quad+\frac{1}{12}\left[\frac{1}{6}\left(\frac{1}{4}-r\right)-\frac{1}{144}\right]\\
&=\frac{-864r^2+408r-24s-43}{1728}.
\end{aligned}
$$
Therefore $H_{1-x}\succeq0$ is equivalent to
$$
s\leq-36r^2+17r-\frac{43}{24}.
$$
Thus the feasible fifth moments are exactly
$$
36r^2-12r+\frac{9}{8}
\leq s\leq
-36r^2+17r-\frac{43}{24}.
$$
The interval is nonempty exactly when
$$
-36r^2+17r-\frac{43}{24}
-\left(36r^2-12r+\frac{9}{8}\right)\geq0.
$$
The left side factors as
$$
-\frac{(24r-5)(36r-7)}{12},
$$
so feasibility is equivalent to
$$
\frac{7}{36}\leq r\leq\frac{5}{24}.
$$
This is automatically satisfied by the hypothesis that at least one calibrated prior exists.

Step 4: Identify the sharp boundary measures and show there are no missing values
At the lower endpoint for $s$, the matrix $H_x$ is singular. A kernel vector is
$$
\begin{pmatrix}
24r-\frac{9}{2}\\
6-36r\\
1
\end{pmatrix},
$$
corresponding to the quadratic
$$
q_-(x)=x^2+(6-36r)x+24r-\frac{9}{2}.
$$
Equality in the lower determinant bound gives
$$
\mathbb E\!\left[\Theta q_-(\Theta)^2\right]=0,
$$
so every lower-extremizing prior is supported on $\{0\}$ together with the roots of $q_-$. The Hausdorff criterion guarantees existence at the boundary, and the moment equations through degree $2$ determine the atomic weights uniquely once the support is fixed.

At the upper endpoint for $s$, the matrix $H_{1-x}$ is singular. A kernel vector is
$$
\begin{pmatrix}
\frac{5}{2}-12r\\
36r-8\\
1
\end{pmatrix},
$$
corresponding to
$$
q_+(x)=x^2+(36r-8)x+\frac{5}{2}-12r.
$$
Equality gives
$$
\mathbb E\!\left[(1-\Theta)q_+(\Theta)^2\right]=0,
$$
so every upper-extremizing prior is supported on the roots of $q_+$ together with $\{1\}$. Again the boundary moment sequence is representable by the Hausdorff criterion, and the atomic weights are uniquely fixed by the moment equations.

More generally, the same criterion is an if-and-only-if statement. Hence every $s$ between the two determinant bounds is realized by at least one Borel prior on $[0,1]$. Therefore there are no gaps in the feasible fifth-moment interval.

Step 5: Convert the fifth-moment interval to the posterior predictive interval
Since $p_\mu=s/r$ and $r>0$, divide the sharp bounds from Step 3 by $r$ to obtain
$$
36r-12+\frac{9}{8r}
\leq p_\mu\leq
17-36r-\frac{43}{24r}.
$$
Every value in this interval is attained by a calibrated prior.

Final Answer: $\boxed{\left[36r-12+\frac{9}{8r},17-36r-\frac{43}{24r}\right]}$

---

## Answer

$\left[36r-12+\frac{9}{8r},17-36r-\frac{43}{24r}\right]$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Interval or region description

---

## Solution Concepts

- posterior predictive distributions
- Hausdorff moment problem
- positive semidefinite moment matrices
- Schur complements
- extremal atomic priors

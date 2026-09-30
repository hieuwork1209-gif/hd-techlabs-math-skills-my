## Steps

Step 1: Reduce the two-periodic heavy-ball method to trace and determinant control
For an eigenmode with eigenvalue $\lambda$, one heavy-ball step with step size $\alpha$ has state matrix
$$
A_\alpha(\lambda)=
\begin{pmatrix}
1+\beta-\alpha\lambda & -\beta\\
1 & 0
\end{pmatrix}.
$$
With the two step sizes repeated periodically, the two-step monodromy is
$$
M(\lambda)=A_{\alpha_2}(\lambda)A_{\alpha_1}(\lambda).
$$
Its determinant is
$$
\det M(\lambda)=\beta^2,
$$
and direct multiplication gives
$$
\tau(\lambda):=\operatorname{tr}M(\lambda)
=1+\beta^2-(1+\beta)(\alpha_1+\alpha_2)\lambda
+\alpha_1\alpha_2\lambda^2.
$$
Thus the two eigenvalues of $M(\lambda)$ are the roots of
$$
z^2-\tau(\lambda)z+\beta^2=0.
$$
Consequently the spectral radius is at least $\beta$. If $|\tau(\lambda)|\leq2\beta$, both roots have modulus $\beta$. If $x:=|\tau(\lambda)|>2\beta$, the larger root modulus is
$$
g_\beta(x)=\frac{x+\sqrt{x^2-4\beta^2}}{2},
$$
which is increasing in $x$.

Step 2: Solve the unrestricted minimax problem
Fix $\beta\in[0,1)$. Every possible trace polynomial has degree at most $2$ and satisfies
$$
\tau(0)=1+\beta^2.
$$
The quadratic
$$
q(\lambda)=\lambda^2-7\lambda+8
$$
takes the values
$$
q(1)=2,\qquad q(2)=-2,\qquad q(5)=-2,\qquad q(6)=2,
$$
and $q(0)=8$. Hence
$$
\tau_\beta^*(\lambda)=\frac{1+\beta^2}{8}q(\lambda)
$$
has norm $(1+\beta^2)/4$ on $E=[1,2]\cup[5,6]$.

This norm is minimal among all degree-two polynomials with the same value at $0$. Indeed, if another polynomial $p$ had $p(0)=1+\beta^2$ and smaller norm, then $p-\tau_\beta^*$ would be negative at $1$, positive at $2$, negative at $6$, and zero at $0$. It would therefore have zeros in $(1,2)$, in $(2,6)$, and at $0$, impossible for a polynomial of degree at most $2$. Thus every trace polynomial satisfies
$$
\max_{\lambda\in E}|\tau(\lambda)|
\geq m(\beta):=\frac{1+\beta^2}{4}.
$$

Let
$$
\beta_* =4-\sqrt{15}.
$$
It is the smaller root of
$$
\beta^2-8\beta+1=0,
$$
so
$$
m(\beta_*)=2\beta_*.
$$
For $\beta\geq\beta_*$, the determinant bound gives
$$
\max_{\lambda\in E}r(M(\lambda))\geq\beta\geq\beta_*.
$$
For $0\leq\beta<\beta_*$, one has $m(\beta)>2\beta$. Also
$$
m(\beta)-\left(\beta_*+\frac{\beta^2}{\beta_*}\right)
=
\left(\frac14-\beta_*\right)
+\left(\frac14-\frac1{\beta_*}\right)\beta^2.
$$
The coefficient of $\beta^2$ is negative, and the right side is $0$ at $\beta=\beta_*$, so it is positive for $\beta<\beta_*$. Since $r+\beta^2/r$ is increasing for $r\geq\beta$, the relation
$$
m(\beta)=g_\beta(m(\beta))+\frac{\beta^2}{g_\beta(m(\beta))}
$$
implies
$$
g_\beta(m(\beta))\geq\beta_*.
$$
Therefore the unrestricted two-step factor is at least $\beta_*$.

At $\beta=\beta_*$, the extremal trace polynomial from this step is
$
\tau(\lambda)=\beta_*(\lambda^2-7\lambda+8),
$
because $1+\beta_*^2=8\beta_*$. Matching its coefficients with the trace formula from Step 1 forces
$
\alpha_1\alpha_2=\beta_*,
\qquad
(1+\beta_*)(\alpha_1+\alpha_2)=7\beta_*.
$
The relation $\beta_*^2-8\beta_*+1=0$ also gives
$
(1+\beta_*)^2=10\beta_*.
$
Therefore
$
\alpha_1+\alpha_2=\frac{7(1+\beta_*)}{10},
\qquad
\alpha_1\alpha_2=\frac{(1+\beta_*)^2}{10}.
$
The two positive roots of the resulting quadratic in the step size are
$
\alpha_1=\frac{1+\beta_*}{2},
\qquad
\alpha_2=\frac{1+\beta_*}{5},
$
up to order. These values realize the displayed trace, so
so $|\tau(\lambda)|\leq2\beta_*$ on $E$. Every two-step monodromy therefore has spectral radius exactly $\beta_*$, and
$$
\rho_2=4-\sqrt{15}.
$$

Step 3: Translate one-step stability into a bound on normalized step sizes
For one step, write
$$
t=1+\beta-\alpha\lambda.
$$
The characteristic polynomial is
$$
z^2-tz+\beta.
$$
For $0\leq\beta<1$, its two roots lie in the closed unit disk exactly when
$$
|t|\leq1+\beta.
$$
To see the nontrivial direction, suppose the roots are real. Their product is $\beta\geq0$, so they have the same sign. If one has modulus $s>1$, the other has modulus $\beta/s$, and
$
|t|=s+\frac{\beta}{s}>1+\beta,
$
because $s+\beta/s$ is increasing for $s\geq1$. This contradicts $|t|\leq1+\beta$. If the roots are nonreal, they are conjugates with modulus $\sqrt\beta<1$.

Since $\alpha>0$, the upper inequality $t\leq1+\beta$ is automatic. The lower inequality for every $\lambda\in E$ is equivalent to
$$
\alpha\lambda\leq2(1+\beta),
$$
and the largest spectral value is $6$. Thus one-step stability is exactly
$$
0<\alpha\leq\frac{1+\beta}{3}.
$$
For a stepwise-stable pair define
$$
x_i=\frac{\alpha_i}{1+\beta},
\qquad
0<x_i\leq\frac13.
$$
Then
$$
\tau(\lambda)=(1+\beta)^2q(\lambda)-2\beta,
$$
where
$$
q(\lambda)=(1-x_1\lambda)(1-x_2\lambda).
$$

Step 4: Obtain the sharp stable lower bound
Set
$$
u_i=|1-6x_i|\in[0,1],
\qquad
s=u_1u_2=|q(6)|.
$$
For fixed $u_i$, the two possibilities $x_i=(1\mp u_i)/6$ give
$$
1-x_i\geq\frac{5-u_i}{6}.
$$
Therefore
$$
q(1)\geq\frac{(5-u_1)(5-u_2)}{36}.
$$
For $u_1,u_2\in[0,1]$,
$$
(5-u_1)(5-u_2)-4(5-u_1u_2)
=5(1-u_1)(1-u_2)\geq0.
$$
Hence
$$
q(1)\geq\frac{5-s}{9}.
$$
Since $|q(6)|=s$,
$$
\max_{\lambda\in E}|q(\lambda)|
\geq
\max\left\{\frac{5-s}{9},s\right\}
\geq\frac12.
$$

It follows from
$$
\tau(\lambda)=(1+\beta)^2q(\lambda)-2\beta
$$
and the reverse triangle inequality that
$$
\max_{\lambda\in E}|\tau(\lambda)|
\geq
m_s(\beta):=
\frac{(1+\beta)^2}{2}-2\beta
=
\frac{(1-\beta)^2}{2}.
$$
Let
$$
\widehat\beta=3-2\sqrt2.
$$
It is the smaller root of
$$
\beta^2-6\beta+1=0,
$$
so
$$
m_s(\widehat\beta)=2\widehat\beta.
$$
If $\beta\geq\widehat\beta$, the determinant bound gives spectral radius at least $\widehat\beta$. If $0\leq\beta<\widehat\beta$, then $m_s(\beta)>2\beta$. The function
$$
D(\beta)=m_s(\beta)-\widehat\beta-\frac{\beta^2}{\widehat\beta}
$$
has
$$
D'(\beta)=-1+\beta-\frac{2\beta}{\widehat\beta}<0
$$
on $[0,\widehat\beta]$, and $D(\widehat\beta)=0$. Hence $D(\beta)>0$ for $\beta<\widehat\beta$. The same increasing relation $r+\beta^2/r$ used in Step 2 gives
$$
\max_{\lambda\in E}r(M(\lambda))\geq\widehat\beta.
$$

Step 5: Attain the stable lower bound
Equality in the last maximum of Step 4 requires $s=1/2$. Equality in
$
(5-u_1)(5-u_2)\geq4(5-u_1u_2)
$
requires one of $u_1,u_2$ to equal $1$. Up to order, take
$
u_1=1,\qquad u_2=\frac12.
$
Equality in $1-x_i\geq(5-u_i)/6$ then selects the larger admissible $x_i$, giving
$
x_1=\frac13,\qquad x_2=\frac14.
$
Therefore set
$
\beta=\widehat\beta,
\qquad
\alpha_1=\frac{1+\widehat\beta}{3},
\qquad
\alpha_2=\frac{1+\widehat\beta}{4}.
$
Both one-step matrices are stable by Step 3. The normalized residual polynomial is
$$
q(\lambda)=\left(1-\frac{\lambda}{3}\right)
\left(1-\frac{\lambda}{4}\right).
$$
It decreases from $1/2$ to $1/6$ on $[1,2]$ and increases from $1/6$ to $1/2$ on $[5,6]$, so
$$
\frac16\leq q(\lambda)\leq\frac12
\qquad(\lambda\in E).
$$
Because $(1+\widehat\beta)^2=8\widehat\beta$,
$$
\tau(\lambda)=8\widehat\beta\,q(\lambda)-2\widehat\beta.
$$
Thus
$$
-\frac{2\widehat\beta}{3}
\leq\tau(\lambda)\leq2\widehat\beta.
$$
Every two-step monodromy has spectral radius $\widehat\beta$, so
$$
\widehat\rho_2=3-2\sqrt2.
$$
Combining the unrestricted and stepwise-stable values gives the requested pair.
Final Answer: $\boxed{\left(4-\sqrt{15},3-2\sqrt2\right)}$

---

## Answer

$\left(4-\sqrt{15},3-2\sqrt2\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- heavy-ball method
- spectral radius
- periodic iteration matrices
- minimax quadratic polynomials
- stability of second-order recurrences

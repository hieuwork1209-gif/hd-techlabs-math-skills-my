## Steps

Step 1: Reduce the two-step iteration to a quadratic minimax problem
For real step sizes $\alpha,\beta$, define
$$
p(\lambda)
=
(1-\alpha\lambda)(1-\beta\lambda).
$$
Write
$$
s=\alpha+\beta,
\qquad
t=\alpha\beta.
$$
Then
$$
p(\lambda)=1-s\lambda+t\lambda^2.
$$
The worst-case two-step contraction factor on
$$
E=[1,2]\cup[4,8]
$$
is
$$
\rho(\alpha,\beta)
=
\max_{\lambda\in E}|p(\lambda)|.
$$
Thus every choice of real $\alpha,\beta$ produces a real quadratic with
$$
p(0)=1.
$$

Step 2: Build a sharp interpolation lower certificate
For every polynomial $p$ of degree at most $2$, Lagrange interpolation at the three points
$$
1,
\qquad
\frac{9}{2},
\qquad
8
$$
gives its value at $0$ as
$$
p(0)
=
\frac{72}{49}p(1)
-
\frac{32}{49}p\left(\frac{9}{2}\right)
+
\frac{9}{49}p(8).
$$
Indeed, the three Lagrange coefficients at $0$ are
$$
\frac{(0-\frac92)(0-8)}
{(1-\frac92)(1-8)}
=
\frac{72}{49},
$$
$$
\frac{(0-1)(0-8)}
{(\frac92-1)(\frac92-8)}
=
-\frac{32}{49},
$$
and
$$
\frac{(0-1)(0-\frac92)}
{(8-1)(8-\frac92)}
=
\frac{9}{49}.
$$

All three interpolation points lie in $E$. Since $p(0)=1$,
$$
1
\leq
\left(
\frac{72}{49}
+
\frac{32}{49}
+
\frac{9}{49}
\right)
\max_{\lambda\in E}|p(\lambda)|.
$$
Therefore
$$
\rho(\alpha,\beta)\geq\frac{49}{113}
$$
for every real pair $(\alpha,\beta)$.

Step 3: Construct a pair attaining the lower bound
Consider
$$
p_*(\lambda)
=
1-\frac{72}{113}\lambda+\frac{8}{113}\lambda^2.
$$
Its derivative is
$$
p_*'(\lambda)
=
\frac{16\lambda-72}{113},
$$
so its unique critical point is
$$
\lambda=\frac{9}{2}.
$$
At the relevant points,
$$
p_*(1)=\frac{49}{113},
\qquad
p_*(2)=\frac{1}{113},
$$
$$
p_*(4)=-\frac{47}{113},
\qquad
p_*\left(\frac{9}{2}\right)=-\frac{49}{113},
\qquad
p_*(8)=\frac{49}{113}.
$$

On $[1,2]$, the derivative is negative, so $p_*$ decreases from $49/113$ to $1/113$. Hence
$$
|p_*(\lambda)|\leq\frac{49}{113}
$$
there.

On $[4,\frac92]$, the polynomial decreases from $-47/113$ to $-49/113$. On $[\frac92,8]$, it increases from $-49/113$ to $49/113$. Hence the same bound holds throughout $[4,8]$.

Therefore
$$
\max_{\lambda\in E}|p_*(\lambda)|
=
\frac{49}{113}.
$$

It remains to verify that $p_*$ comes from real step sizes. We need
$$
\alpha+\beta=\frac{72}{113},
\qquad
\alpha\beta=\frac{8}{113}.
$$
Thus $\alpha,\beta$ are the roots of
$$
z^2-\frac{72}{113}z+\frac{8}{113}=0.
$$
The discriminant is
$$
\left(\frac{72}{113}\right)^2
-
\frac{32}{113}
=
\frac{1568}{12769}
=
\left(\frac{28\sqrt{2}}{113}\right)^2.
$$
Hence
$$
\{\alpha,\beta\}
=
\left\{
\frac{36-14\sqrt{2}}{113},
\frac{36+14\sqrt{2}}{113}
\right\}.
$$
These real step sizes attain the lower bound.

Step 4: Classify all optimal step sizes
Suppose
$$
\rho(\alpha,\beta)=\frac{49}{113}.
$$
Let $p(\lambda)=(1-\alpha\lambda)(1-\beta\lambda)$. The interpolation identity from Step 2 gives
$$
1
=
\frac{72}{49}p(1)
-
\frac{32}{49}p\left(\frac{9}{2}\right)
+
\frac{9}{49}p(8).
$$
Each of the three values has absolute value at most $49/113$. Equality in the triangle inequality is necessary, because the coefficient absolute values sum to $113/49$. Since the left side is positive, the signs must align with the interpolation coefficients:
$$
p(1)=\frac{49}{113},
\qquad
p\left(\frac{9}{2}\right)=-\frac{49}{113},
\qquad
p(8)=\frac{49}{113}.
$$
A polynomial of degree at most $2$ is uniquely determined by these three values, so
$$
p=p_*.
$$
Therefore every optimizer satisfies
$$
\alpha+\beta=\frac{72}{113},
\qquad
\alpha\beta=\frac{8}{113},
$$
and hence has the same unordered pair of step sizes found in Step 3.

Thus the minimum contraction factor and the complete optimizer set are
$$
\frac{49}{113}
\qquad\text{and}\qquad
\left\{
\frac{36-14\sqrt{2}}{113},
\frac{36+14\sqrt{2}}{113}
\right\}.
$$
Final Answer: $\boxed{\left(\frac{49}{113},\left\{\frac{36-14\sqrt{2}}{113},\frac{36+14\sqrt{2}}{113}\right\}\right)}$

---

## Answer

$\left(\frac{49}{113},\left\{\frac{36-14\sqrt{2}}{113},\frac{36+14\sqrt{2}}{113}\right\}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- minimax polynomials
- interpolation certificates
- richardson iteration
- equality in triangle inequality
- optimizer classification

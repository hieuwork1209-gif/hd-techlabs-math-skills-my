## Steps

Step 1: Reduce the problem to a quadratic minimax optimization
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
p(\lambda)=t\lambda^2-s\lambda+1.
$$
The objective is
$$
\rho(\alpha,\beta)
=
\max_{\lambda\in E}|p(\lambda)|,
\qquad
E=[1,2]\cup[4,8].
$$
The maximum exists because $E$ is compact and $p$ is continuous. Every real pair $(\alpha,\beta)$ therefore produces a real quadratic with
$$
p(0)=1.
$$

Step 2: Derive a balanced candidate and its interpolation certificate
To find a sharp candidate, balance the two outer spectral endpoints by requiring
$$
p(1)=p(8).
$$
For a nonconstant quadratic this forces its axis to be
$$
\lambda=\frac{1+8}{2}=\frac{9}{2}.
$$
A balanced minimax candidate should have the opposite value at this interior extremum, so write
$$
p(1)=p(8)=M,
\qquad
p\left(\frac{9}{2}\right)=-M.
$$
Because the axis is $9/2$, write
$$
p(\lambda)
=
a\left(\lambda-\frac{9}{2}\right)^2-M.
$$
The first equality gives
$$
a\left(\frac{7}{2}\right)^2=2M,
$$
so
$$
a=\frac{8M}{49}.
$$
Using $p(0)=1$ then gives
$$
1
=
\frac{8M}{49}\left(\frac{9}{2}\right)^2-M
=
\frac{113}{49}M.
$$
Hence
$$
M=\frac{49}{113},
$$
and the resulting candidate is
$$
p_*(\lambda)
=
\frac{8}{113}\lambda^2
-
\frac{72}{113}\lambda
+
1.
$$

The same three balancing points give a lower certificate for every quadratic. Lagrange interpolation at
$$
1,
\qquad
\frac{9}{2},
\qquad
8
$$
evaluated at $0$ gives
$$
p(0)
=
\frac{72}{49}p(1)
-
\frac{32}{49}p\left(\frac{9}{2}\right)
+
\frac{9}{49}p(8).
$$
The coefficients follow directly from
$$
\frac{(0-\frac{9}{2})(0-8)}
{(1-\frac{9}{2})(1-8)}
=
\frac{72}{49},
$$
$$
\frac{(0-1)(0-8)}
{(\frac{9}{2}-1)(\frac{9}{2}-8)}
=
-\frac{32}{49},
$$
and
$$
\frac{(0-1)(0-\frac{9}{2})}
{(8-1)(8-\frac{9}{2})}
=
\frac{9}{49}.
$$
All three nodes lie in $E$. Since $p(0)=1$,
$$
1
\leq
\frac{113}{49}
\max_{\lambda\in E}|p(\lambda)|.
$$
Therefore every real pair satisfies
$$
\rho(\alpha,\beta)\geq\frac{49}{113}.
$$

Step 3: Verify attainment and recover the real step sizes
The derivative of the candidate is
$$
p_*'(\lambda)
=
\frac{16\lambda-72}{113},
$$
so its unique critical point is $9/2$. Its relevant values are
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
On $[1,2]$, the polynomial decreases from $49/113$ to $1/113$. On $[4,\frac{9}{2}]$, it decreases from $-47/113$ to $-49/113$, and on $[\frac{9}{2},8]$ it increases from $-49/113$ to $49/113$. Therefore
$
\max_{\lambda\in E}|p_*(\lambda)|
=
\frac{49}{113}.
$$
The lower bound from Step 2 is attained.

To factor $p_*$ as
$$
(1-\alpha\lambda)(1-\beta\lambda),
$$
we need
$$
\alpha+\beta=\frac{72}{113},
\qquad
\alpha\beta=\frac{8}{113}.
$$
Therefore $\alpha,\beta$ are the roots of
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
Therefore
$$
\{\alpha,\beta\}
=
\left\{
\frac{36-14\sqrt{2}}{113},
\frac{36+14\sqrt{2}}{113}
\right\}.
$$

Step 4: Classify every optimizer
Suppose
$$
\rho(\alpha,\beta)=\frac{49}{113},
$$
and let
$$
p(\lambda)=(1-\alpha\lambda)(1-\beta\lambda).
$$
The interpolation certificate gives
$$
1
=
\frac{72}{49}p(1)
-
\frac{32}{49}p\left(\frac{9}{2}\right)
+
\frac{9}{49}p(8).
$$
Each sampled value has absolute value at most $49/113$, while the absolute values of the three coefficients sum to $113/49$. Equality in the triangle inequality is therefore necessary. Since the left side is positive, the three signed terms must all be nonnegative at full magnitude:
$$
p(1)=\frac{49}{113},
\qquad
p\left(\frac{9}{2}\right)=-\frac{49}{113},
\qquad
p(8)=\frac{49}{113}.
$$
A polynomial of degree at most $2$ is uniquely determined by its values at three distinct points, so
$$
p=p_*.
$$
Every optimizer therefore has
$$
\alpha+\beta=\frac{72}{113},
\qquad
\alpha\beta=\frac{8}{113},
$$
and therefore the same unordered pair from Step 3.

The minimum contraction factor and complete optimizer pair are
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

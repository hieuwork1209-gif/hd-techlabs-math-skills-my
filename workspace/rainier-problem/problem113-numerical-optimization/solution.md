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
The maximum exists because $E$ is compact and $p$ is continuous. Every real pair $(\alpha,\beta)$ produces a polynomial of degree at most $2$ with
$$
p(0)=1.
$$

Step 2: Optimize a family of interpolation lower certificates
Fix
$$
c\in[4,8).
$$
For every polynomial $p$ of degree at most $2$, Lagrange interpolation at $1,c,8$, evaluated at $0$, gives
$$
p(0)
=
\frac{8c}{7(c-1)}p(1)
+
\frac{8}{(c-1)(c-8)}p(c)
+
\frac{c}{7(8-c)}p(8).
$$
The middle coefficient is negative, while the other two are positive. Since all three nodes lie in $E$ and $p(0)=1$,
$$
1
\leq
D(c)\max_{\lambda\in E}|p(\lambda)|,
$$
where
$$
D(c)
=
\frac{8c}{7(c-1)}
+
\frac{8}{(c-1)(8-c)}
+
\frac{c}{7(8-c)}.
$$
Therefore
$$
\rho(\alpha,\beta)\geq\frac{1}{D(c)}
$$
for every $c\in[4,8)$.

To make this certificate as strong as possible, minimize $D(c)$. Combining the three fractions gives
$$
D(c)
=
\frac{c^2-9c-8}{(c-8)(c-1)}.
$$
Differentiation yields
$$
D'(c)
=
\frac{16(2c-9)}
{(c-8)^2(c-1)^2}.
$$
$D$ decreases on $[4,9/2]$ and increases on $[9/2,8)$. Its unique minimum occurs at
$$
c=\frac{9}{2},
$$
where
$$
D\left(\frac{9}{2}\right)
=
\frac{113}{49}.
$$
Therefore
$$
\rho(\alpha,\beta)\geq\frac{49}{113}
$$
for every real pair $(\alpha,\beta)$.

At the minimizing node, the interpolation identity is
$$
1
=
\frac{72}{49}p(1)
-
\frac{32}{49}p\left(\frac{9}{2}\right)
+
\frac{9}{49}p(8).
$$

Step 3: Construct a real pair attaining the certificate
To attain the lower bound from Step 2, equality in the triangle inequality there would require the alternating values
$$
p(1)=\frac{49}{113},
\qquad
p\left(\frac{9}{2}\right)=-\frac{49}{113},
\qquad
p(8)=\frac{49}{113}.
$$
The first and third values are equal, so the axis of the interpolating quadratic is $9/2$. Write
$$
p_*(\lambda)
=
a\left(\lambda-\frac{9}{2}\right)^2
-
\frac{49}{113}.
$$
Using $p_*(1)=49/113$ gives
$$
a\left(\frac{7}{2}\right)^2
=
\frac{98}{113},
$$
so
$$
a=\frac{8}{113}.
$$
Therefore
$$
p_*(\lambda)
=
\frac{8}{113}\lambda^2
-
\frac{72}{113}\lambda
+
1.
$$

Its derivative is
$$
p_*'(\lambda)
=
\frac{16\lambda-72}{113}.
$$
The relevant values are
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
$$
\max_{\lambda\in E}|p_*(\lambda)|
=
\frac{49}{113}.
$$

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
The discriminant of
$$
z^2-\frac{72}{113}z+\frac{8}{113}
$$
is
$$
\left(\frac{72}{113}\right)^2
-
\frac{32}{113}
=
\frac{1568}{12769}
=
\left(\frac{28\sqrt{2}}{113}\right)^2.
$$
Therefore the real step sizes
$$
\{\alpha,\beta\}
=
\left\{
\frac{36-14\sqrt{2}}{113},
\frac{36+14\sqrt{2}}{113}
\right\}
$$
attain the lower bound.

Step 4: Classify every optimizer
Suppose
$$
\rho(\alpha,\beta)=\frac{49}{113},
$$
and let
$$
p(\lambda)=(1-\alpha\lambda)(1-\beta\lambda).
$$
At $c=9/2$, the certificate from Step 2 is an equality:
$$
1
=
\frac{72}{49}p(1)
-
\frac{32}{49}p\left(\frac{9}{2}\right)
+
\frac{9}{49}p(8).
$$
Each sampled value has absolute value at most $49/113$, while the absolute values of the three coefficients sum to $113/49$. Equality in the triangle inequality is therefore necessary. Since the left side is positive,
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
Every optimizer therefore satisfies
$$
\alpha+\beta=\frac{72}{113},
\qquad
\alpha\beta=\frac{8}{113},
$$
and has the same unordered pair from Step 3.

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

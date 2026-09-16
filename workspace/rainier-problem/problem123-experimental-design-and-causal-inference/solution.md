## Steps

Step 1: Reduce the information determinant to a strictly concave Vandermonde problem
Let $V$ be the $5\times5$ matrix whose $i$th column is $v(x_i)$. Then
$$
M=\frac15VV^T,
$$
so the Vandermonde determinant gives
$$
\det M=5^{-5}\prod_{1\leq i<j\leq5}(x_j-x_i)^2.
$$
For distinct ordered points define
$$
\Phi(x_1,\ldots,x_5)=2\sum_{i<j}\log(x_j-x_i).
$$
For any direction $d=(d_1,\ldots,d_5)$,
$$
D^2\Phi[d,d]=-2\sum_{i<j}\frac{(d_j-d_i)^2}{(x_j-x_i)^2}.
$$
Hence $\Phi$ is strictly concave on the affine hyperplane $\sum_i x_i=5/3$, because equality in the displayed quadratic form forces all $d_i$ equal, and a tangent direction on that hyperplane then has $d=0$. Thus any feasible point satisfying the first-order concave optimality inequality is the unique global maximizer. Configurations with a collision have determinant $0$, so they cannot beat any distinct feasible configuration.

Step 2: Construct a centroid-constrained KKT candidate
Construct a candidate with $x_1=0$. Let its other four points be the roots of a monic quartic $q$, and set
$$
p(x)=xq(x).
$$
At an interior support point $r$, stationarity under the constraint $\sum_i x_i=5/3$ requires the common gradient value
$$
2\sum_{s\neq r}\frac1{r-s}=\lambda.
$$
For a simple root $r$ of $p$,
$$
\frac{p''(r)}{p'(r)}=2\sum_{s\neq r}\frac1{r-s},
$$
so $q$ divides $p''-\lambda p'$. Since $p$ is monic of degree $5$, comparison of leading coefficients gives
$$
p''-\lambda p'=-5\lambda q.
$$
Substituting $p=xq$ yields
$$
xq''+(2-\lambda x)q'+4\lambda q=0.
$$
Write
$$
q(x)=x^4+ax^3+bx^2+cx+d.
$$
Because its four roots must sum to $5/3$, $a=-5/3$. The $x^3$ coefficient in the differential equation is $\lambda a+20$, so $\lambda=12$. The remaining coefficient equations are
$$
24b+12a=0,\qquad 36c+6b=0,\qquad 48d+2c=0,
$$
which give
$$
q(x)=x^4-\frac53x^3+\frac56x^2-\frac5{36}x+\frac5{864}.
$$

Step 3: Verify feasibility and the global first-order certificate
Let
$$
Q(x)=864q(x)=864x^4-1440x^3+720x^2-120x+5.
$$
Its signs satisfy
$$
Q(0)=5,\quad Q\left(\frac1{10}\right)=-\frac{721}{625},\quad Q\left(\frac14\right)=\frac78,
$$
$$
Q\left(\frac12\right)=-1,\qquad Q(1)=29.
$$
Thus $q$ has exactly one root in each of $(0,1/10)$, $(1/10,1/4)$, $(1/4,1/2)$, and $(1/2,1)$. Denote them by $r_1<r_2<r_3<r_4$. By Vieta's formula their sum is $5/3$, so
$$
x^*=(0,r_1,r_2,r_3,r_4)
$$
is feasible. The differential equation gives $\partial\Phi/\partial x_i=12$ at the four interior coordinates. At $x_1=0$,
$$
\frac{\partial\Phi}{\partial x_1}=-2\sum_{j=1}^4\frac1{r_j}.
$$
For the monic quartic $q$, the reciprocal-root sum is
$$
\sum_{j=1}^4\frac1{r_j}=\frac{5/36}{5/864}=24,
$$
so this boundary gradient is $-48$. For any feasible ordered $y=(y_1,\ldots,y_5)$ with distinct coordinates, concavity gives
$$
\Phi(y)-\Phi(x^*)\leq\nabla\Phi(x^*)\cdot(y-x^*)
=-48y_1+12\sum_{i=2}^5(y_i-x_i^*)=-60y_1\leq0.
$$
The same determinant inequality is automatic for colliding $y$ because then $\det M(y)=0$. Therefore $x^*$ is the global maximizer.

Step 4: Evaluate the maximal determinant exactly
Differentiate $q$ and set
$$
R_2=-\frac5{576}(2x-1)(6x-1),\qquad R_1=-\frac1{18}(4x-1),\qquad c_0=\frac5{2304}.
$$
Direct polynomial division gives
$$
q=\frac{12x-5}{48}q'+R_2,
$$
$$
q'=-\frac{16(12x-7)}5R_2+R_1,
$$
$$
R_2=\frac{5(12x-5)}{128}R_1+c_0.
$$
If $A=BC+R$, then the resultant satisfies
$$
\operatorname{Res}(A,B)=(-1)^{(\deg A-\deg R)\deg B}\operatorname{lc}(B)^{\deg A-\deg R}\operatorname{Res}(R,B).
$$
Applying this identity successively to the three divisions, with no sign change when the two resultant arguments are swapped because the relevant degree products are even, and using
$$
\operatorname{lc}(q')=4,\qquad \operatorname{lc}(R_2)=-\frac5{48},\qquad \operatorname{lc}(R_1)=-\frac29,
$$
gives
$$
\operatorname{disc}(q)=\operatorname{Res}(q,q')
=4^2\left(-\frac5{48}\right)^2\left(-\frac29\right)^2\frac5{2304}
=\frac{5^3}{2^{10}3^8}.
$$
Since $p=xq$ is monic and $q(0)=5/864$, its discriminant is
$$
\operatorname{disc}(p)=q(0)^2\operatorname{disc}(q)
=\frac{5^5}{2^{20}3^{14}}.
$$
This discriminant is exactly the squared Vandermonde product of the five maximizing points. Therefore
$$
\max\det M=5^{-5}\operatorname{disc}(p)=\frac1{2^{20}3^{14}}.
$$

Final Answer: $\boxed{\frac1{2^{20}3^{14}}}$

---

## Answer

$\frac1{2^{20}3^{14}}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- D-optimal experimental design
- Vandermonde determinants
- strict concavity
- Karush-Kuhn-Tucker conditions
- polynomial resultants

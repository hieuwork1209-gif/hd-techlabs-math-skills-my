## Steps

Step 1: Reduce a maximizing simplex to five points on the moment curve
Let
$$
\gamma(t)=(t,t^2,t^3,t^4),\qquad 0\leq t\leq1,
$$
and let $K=\operatorname{conv}\gamma([0,1])$. Since $K$ is compact and the $4$-volume of a simplex is continuous in its five vertices, a maximum-volume simplex in $K$ exists.

Fix four vertices of a simplex and vary the fifth vertex $x\in K$. Its signed determinant is an affine function $L(x)$, so its volume is $|L(x)|/4!$. Because every point of $K$ is a convex combination of points $\gamma(t)$,
$$
\max_{x\in K}L(x)=\max_{0\leq t\leq1}L(\gamma(t)),
$$
and the same identity holds for $-L$. Therefore $\max_{x\in K}|L(x)|$ is attained on the generating curve. Starting from a maximizing simplex and replacing its vertices one at a time without decreasing volume shows that some maximizing simplex has all five vertices on the curve.

Thus write the parameters in increasing order as
$$
0\leq t_0<t_1<t_2<t_3<t_4\leq1.
$$
The affine determinant of the five curve points is the Vandermonde determinant, so
$$
\operatorname{Vol}_4
=\frac1{24}\prod_{0\leq i<j\leq4}(t_j-t_i).
$$
The maximum is positive, so all five parameters are distinct.

Step 2: Fix the endpoints and set up the logarithmic extremal problem
If $t_0>0$, replacing $t_0$ by $0$ strictly increases every factor $t_j-t_0$ with $j>0$. Hence a maximizer must have $t_0=0$. Similarly, a maximizer must have $t_4=1$.

For $0<t_1<t_2<t_3<1$, maximize
$$
\Phi(t_1,t_2,t_3)=\sum_{0\leq i<j\leq4}\log(t_j-t_i),
$$
with $t_0=0$ and $t_4=1$. The function tends to $-\infty$ when two parameters collide, so its maximum occurs in the interior.

For a variation $u=(u_1,u_2,u_3)$, put $u_0=u_4=0$. The second directional derivative is
$$
D^2\Phi[u,u]
=-\sum_{0\leq i<j\leq4}\frac{(u_j-u_i)^2}{(t_j-t_i)^2}.
$$
If this were $0$, then every $u_j-u_i$ would vanish; since $u_0=u_4=0$, all $u_i$ would be $0$. Hence $\Phi$ is strictly concave. Therefore any critical point is the unique global maximizer.

Step 3: Determine the unique critical configuration
The critical-point equations are
$$
\sum_{j\ne k}\frac1{t_k-t_j}=0,
\qquad k=1,2,3.
$$
Let
$$
p(x)=\prod_{j=0}^4(x-t_j)=x(x-1)q(x),
$$
where $q$ is the monic cubic with roots $t_1,t_2,t_3$. At a root $t_k$, write $p(x)=(x-t_k)g(x)$. Then
$$
p'(t_k)=g(t_k),
\qquad
p''(t_k)=2g'(t_k),
$$
and
$$
\frac{g'(t_k)}{g(t_k)}=\sum_{j\ne k}\frac1{t_k-t_j}.
$$
Thus the three critical-point equations are exactly $p''(t_k)=0$ for $k=1,2,3$. Since $p''$ is a cubic with leading coefficient $20$ and has the same three roots as the monic cubic $q$,
$$
p''(x)=20q(x).
$$
Using $p=x(x-1)q$ gives
$$
x(x-1)q''+(4x-2)q'-18q=0.
$$
Write
$$
q(x)=x^3+Ax^2+Bx+C.
$$
Substitution gives, from the coefficients of $x^2,x,1$ respectively,
$$
-8A-12=0,
\qquad
-6A-14B=0,
\qquad
-2B-18C=0.
$$
Hence
$$
A=-\frac32,
\qquad
B=\frac9{14},
\qquad
C=-\frac1{14},
$$
so
$$
q(x)=\left(x-\frac12\right)
\left(\left(x-\frac12\right)^2-\frac3{28}\right).
$$
Therefore the unique maximizing parameters are
$$
0,
\quad \frac{1-\sqrt{3/7}}2,
\quad \frac12,
\quad \frac{1+\sqrt{3/7}}2,
\quad1.
$$

Step 4: Evaluate the Vandermonde product
Set $a=\sqrt{3/7}$ and change variables by $x=2t-1$. The five maximizing nodes become
$$
-1,-a,0,a,1.
$$
Their Vandermonde product is
$$
\prod_{i<j}(x_j-x_i)
=4a^3(1-a^2)^2
=\frac{192\sqrt{21}}{2401}.
$$
There are $\binom52=10$ pairwise differences, and each $t$-difference is half the corresponding $x$-difference. Hence
$$
\prod_{i<j}(t_j-t_i)
=2^{-10}\frac{192\sqrt{21}}{2401}
=\frac{3\sqrt{21}}{38416}.
$$
Dividing by $4!=24$ gives the maximum simplex volume
$$
\frac1{24}\cdot\frac{3\sqrt{21}}{38416}
=\frac{\sqrt{21}}{307328}.
$$

Final Answer: $\boxed{\frac{\sqrt{21}}{307328}}$

---

## Answer

$\frac{\sqrt{21}}{307328}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- convex hulls of moment curves
- maximum-volume simplices
- Vandermonde determinants
- strict concavity
- Fekete point optimization

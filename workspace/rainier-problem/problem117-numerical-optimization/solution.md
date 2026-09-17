## Steps

Step 1: Isolate the genuine trust-region hard case
For a fixed symmetric matrix $A$ with simple eigenvalues
$$
\lambda_1<\cdots<\lambda_n
$$
and orthonormal eigenvectors $u_i$, write $c_i=u_i^Tb$ and put
$$
r=-\lambda_1>0.
$$
For every $\mu>r$,
$$
x(\mu)=-(A+\mu I)^{-1}b,
\qquad
\|x(\mu)\|^2=\sum_{i=1}^n\frac{c_i^2}{(\lambda_i+\mu)^2}. \tag{1}
$$
The right side is strictly decreasing in $\mu$. If $c_1\ne0$, it tends to $+\infty$ as $\mu\downarrow r$ and to $0$ as $\mu\to\infty$, so there is a unique $\mu>r$ with $\|x(\mu)\|=1$.

If $c_1=0$, the limit of $x(\mu)$ as $\mu\downarrow r$ is the minimum-norm solution $x_p$ of
$$
(A+rI)x=-b,
\qquad x_p\perp\ker(A+rI). \tag{2}
$$
If $\|x_p\|>1$, (1) again gives a unique multiplier $\mu>r$ with norm $1$. If $\|x_p\|=1$, only $x_p$ is feasible at the singular multiplier. If $\|x_p\|<1$, then the affine line
$$
x_p+\ker(A+rI)
$$
meets the unit sphere in exactly two points.

In all cases, if $x$ has norm $1$, $(A+\mu I)x=-b$, and $A+\mu I\succeq0$, then for every $\|y\|\le1$,
$$
q(y)-q(x)
=\frac12(y-x)^T(A+\mu I)(y-x)
+\frac\mu2(1-\|y\|^2)\ge0. \tag{3}
$$
Thus the two sphere intersections in the last case are exactly the two global minimizers. Consequently, nonuniqueness requires both lowest-eigenspace orthogonality and radius feasibility.

For our tridiagonal $A_\tau$, every eigenspace is one-dimensional: an eigenvector is determined recursively by its first component, and first component $0$ forces the zero vector. Also
$$
\lambda_1(A_\tau)\le e_1^TA_\tau e_1=-3<0.
$$

Step 2: Find every singular positive-semidefinite candidate
Write the singular multiplier as $r>0$ and set
$$
M=A_\tau+rI.
$$
Let $v\in\ker M$ and normalize $v_1=1$. The first, second, and fourth rows give
$$
v_2=3-r,
\qquad
v_3=d:=r^2-3r-1,
\qquad
v_4=-\frac{d}{r+4}. \tag{4}
$$
For
$$
b=(1,3,1,3)^T,
$$
the necessary orthogonality condition $b^Tv=0$ becomes
$$
1+3(3-r)+d-\frac{3d}{r+4}=0.
$$
Since $10-3r+d=(r-3)^2$, this is
$$
q(r):=r^3-5r^2-6r+39=0. \tag{5}
$$
A positive-semidefinite singular shift must have $r>3$. On $(3,\infty)$, $q'$ has only one zero, so $q$ has at most two roots there. The sign checks
$$
q\!\left(\frac{17}{5}\right)=\frac{13}{125}>0,
\quad
q\!\left(\frac{24}{7}\right)=-\frac{15}{343}<0,
$$
$$
q\!\left(\frac{17}{4}\right)=-\frac{3}{64}<0,
\quad
q\!\left(\frac{30}{7}\right)=\frac{57}{343}>0
$$
therefore give exactly two candidates
$$
\rho_1\in\left(\frac{17}{5},\frac{24}{7}\right),
\qquad
\rho_2\in\left(\frac{17}{4},\frac{30}{7}\right). \tag{6}
$$

The third row of $Mv=0$, together with $b^Tv=0$, gives
$$
v_2+v_4=-\frac{1+d}{3}=-\frac{r(r-3)}3,
$$
so
$$
\tau=T(r):=-r+\frac{r(r-3)}{3(r^2-3r-1)}. \tag{7}
$$
For either root in (6), the leading principal determinants of $M$ are
$$
D_1=r-3>0,
\qquad
D_2=d>0,
$$
$$
D_3=(\tau+r)d-(r-3)=\frac{(r-3)^2}{3}>0,
$$
and
$$
D_4=(r+4)D_3-D_2=\frac{q(r)}3=0. \tag{8}
$$
Hence the $LDL^T$ pivots are positive, positive, positive, zero. Therefore
$$
M\succeq0,
\qquad
\operatorname{rank}M=3, \tag{9}
$$
so both $\rho_1$ and $\rho_2$ really are lowest-eigenvalue singular candidates.

Moreover
$$
T'(r)=-\frac{r(3r^3-18r^2+21r+20)}{3(r^2-3r-1)^2}<0
$$
on the two brackets in (6). Thus both $T(\rho_1)$ and $T(\rho_2)$ lie in $[-4,-2]$; in particular
$$
T(\rho_2)\in
\left(-\frac{6000}{1547},-\frac{3179}{828}\right)
\subset\left(-4,-\frac{15}{4}\right). \tag{10}
$$

Step 3: The unit radius rejects one singular candidate
For any root $r$ of $q$ with $r>3$, a convenient particular solution of
$$
Mx=-b
$$
is
$$
x_0=
\left(-\frac r d,\frac1d,-3,0\right)^T. \tag{11}
$$
Indeed, the only nonzero residual is the third component, equal to
$$
\frac{q(r)}{(r+4)d}=0.
$$
Hence every singular stationary point is
$$
x_0+s v.
$$
The equation $\|x_0+sv\|^2=1$ is quadratic in $s$. One quarter of its discriminant is
$$
\mathcal D(r)
=(x_0^Tv)^2-\|v\|^2(\|x_0\|^2-1).
$$
Expanding gives
$$
\mathcal D(r)=\frac{N(r)}{(r+4)^2},
$$
where
$$
N(r)=r^6+2r^5-42r^4+2r^3+340r^2+216r-1593.
$$
The identity
$$
N(r)=61r^2+255r-1593+r(r^2+7r-1)q(r) \tag{12}
$$
shows that at either candidate,
$$
\operatorname{sgn}\mathcal D(r)
=\operatorname{sgn}h(r),
\qquad
h(r)=61r^2+255r-1593. \tag{13}
$$
Since $h'(r)>0$ for $r>0$,
$$
h\!\left(\frac{24}{7}\right)=-\frac{81}{49}<0
$$
implies $\mathcal D(\rho_1)<0$. Thus the affine singular stationary line for $\rho_1$ misses the unit sphere, so the unit trust-region minimizer there is still unique, with a multiplier strictly larger than $\rho_1$ by Step 1.

On the other hand,
$$
h\!\left(\frac{17}{4}\right)=\frac{9481}{16}>0
$$
implies $\mathcal D(\rho_2)>0$. Hence the singular affine line for $\rho_2$ meets the unit sphere in exactly two points. By (3) and (9), those two points are exactly the global minimizers. Therefore
$$
|\mathcal X_{T(\rho_2)}|=2, \tag{14}
$$
while $T(\rho_1)$ still has a singleton minimizer set. Every other $\tau\in[-4,-2]$ has no lowest-eigenspace orthogonality and is unique by Step 1.

Step 4: Eliminate the hidden multiplier and state the exact parameter
Let $t=T(r)$ with $q(r)=0$. Equation (7) is
$$
3(r^2-3r-1)(t+r)-r(r-3)=0.
$$
Using $q(r)=0$ to replace $r^3$ reduces this to
$$
(3t+5)r^2+(18-9t)r-3t-117=0. \tag{15}
$$
The Sylvester resultant of the cubic (5) and the quadratic (15) is
$$
\det\begin{pmatrix}
1&-5&-6&39&0\\
0&1&-5&-6&39\\
3t+5&18-9t&-3t-117&0&0\\
0&3t+5&18-9t&-3t-117&0\\
0&0&3t+5&18-9t&-3t-117
\end{pmatrix}
$$
$$
=9\bigl(81t^3+254t^2-793t-2197\bigr). \tag{16}
$$
Thus the nonuniqueness parameter is a root of
$$
P(t)=81t^3+254t^2-793t-2197.
$$
By (10) it is the root in $(-4,-15/4)$. Finally,
$$
P(-4)=-145<0,
\qquad
P\!\left(-\frac{15}{4}\right)=\frac{4937}{64}>0,
$$
and
$$
P'(t)=243t^2+508t-793>0
$$
throughout $[-4,-15/4]$. Therefore that root is unique. Numerically it is approximately $-3.8483195359$.

Final Answer: $\boxed{\operatorname{root}_{(-4,-15/4)}(81x^3+254x^2-793x-2197)}$

---

## Answer

$\operatorname{root}_{(-4,-15/4)}(81x^3+254x^2-793x-2197)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- trust-region hard case
- Jacobi eigenvector recurrence
- singular stationary geometry
- radius feasibility discriminant
- shifted positive-semidefinite certificate

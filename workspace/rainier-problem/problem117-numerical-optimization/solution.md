## Steps

Step 1: Convert the robust three-stage contraction to a symmetric rational minimax problem
Put
$$
x=\frac{\lambda}{3},
\qquad
c_j=3\alpha_j,
\qquad j=1,2,3.
$$
Then $x\in[1/3,3]$ and
$$
\frac{1-\alpha_j\lambda}{1+\alpha_j\lambda}
=\frac{1-c_jx}{1+c_jx}.
$$
Now use the fractional-linear coordinate
$$
z=\frac{x-1}{x+1}.
$$
It maps $[1/3,3]$ bijectively onto $[-1/2,1/2]$. For
$$
a_j=\frac{1-c_j}{1+c_j}\in(-1,1),
$$
direct substitution of $x=(1+z)/(1-z)$ gives
$$
\frac{1-c_jx}{1+c_jx}=\frac{a_j-z}{1-a_jz}.
$$
Conversely every $a_j\in(-1,1)$ comes from the positive parameter
$$
\alpha_j=\frac{1-a_j}{3(1+a_j)}.
$$
Thus the required infimum equals
$$
\inf_{a_1,a_2,a_3\in(-1,1)}
\max_{|z|\leq1/2}
\left|B(z)\right|,
\qquad
B(z)=\prod_{j=1}^3\frac{a_j-z}{1-a_jz}.
$$

Step 2: Establish an alternation certificate for degree-three products
Suppose a feasible product $B_*(z)$ has four points
$$
z_0<z_1<z_2<z_3
$$
in $(-1,1)$ at which its values are consecutively
$$
\rho,-\rho,\rho,-\rho.
$$
Then no other feasible degree-three product can have uniform norm strictly smaller than $\rho$ on an interval containing these four points.

To prove this, write
$$
P(z)=\prod_{j=1}^3(z-a_j),
\qquad
P^{\#}(z)=z^3P(1/z)=\prod_{j=1}^3(1-a_jz),
$$
so $B(z)=-P(z)/P^{\#}(z)$. For a competitor $C(z)=-Q(z)/Q^{\#}(z)$, the denominator of $C-B_*$ is positive on $(-1,1)$ and its numerator is
$$
H(z)=P(z)Q^{\#}(z)-Q(z)P^{\#}(z).
$$
This polynomial has degree at most $6$ and satisfies
$$
z^6H(1/z)=-H(z).
$$
If $\|C\|_{\infty}<\rho$, then $C-B_*$ has alternating signs at $z_0,z_1,z_2,z_3$, so $H$ has one zero in each of the three intervening open intervals. The first and third of these zeros are nonzero and lie in $(-1,1)$, hence their reciprocals are two further zeros outside $[-1,1]$. Also every feasible degree-three product equals $1$ at $z=-1$ and $-1$ at $z=1$, so $H(-1)=H(1)=0$. This gives at least seven distinct zeros of a polynomial of degree at most $6$, a contradiction. Therefore any feasible product with four alternating extrema is globally optimal.

Step 3: Construct a four-point equioscillating candidate
The transformed interval is symmetric under $z\mapsto-z$, and the degree is odd. The canonical product respecting that symmetry has zeros $-a,0,a$. Since Step 2 turns four-point equioscillation into a global optimality certificate, it is enough to tune this symmetric family until its two positive peak heights agree.

Choose $0<a<1/2$ and set $y=a^2$. The corresponding product is
$$
B_y(z)=\frac{z(y-z^2)}{1-yz^2}.
$$
For $z>0$,
$$
B_y'(z)=\frac{y+(y^2-3)z^2+yz^4}{(1-yz^2)^2}.
$$
Writing $u=z^2$, the critical-point equation is
$$
yu^2+(y^2-3)u+y=0.
$$
Its two positive roots have product $1$. Moreover the left side is positive at $u=0$ and equals $2y(y^2-1)<0$ at $u=y$, so the smaller root $u_*$ lies in $(0,y)$. Hence $r=\sqrt{u_*}$ is the unique critical point in $(0,a)$, where $B_y$ attains its positive inner maximum. The other critical value has $u>1$, so there is no further critical point before $z=1/2$; therefore on $(a,1/2]$ the magnitude increases to the endpoint.

The endpoint magnitude is
$$
-B_y\left(\frac12\right)=\frac{1-4y}{2(4-y)}.
$$
Equating this with $B_y(r)$ and squaring gives
$$
4(4-y)^2u_*(y-u_*)^2-(1-4y)^2(1-yu_*)^2=0.
$$
The critical equation gives
$$
u_*^2=\frac{(3-y^2)u_*-y}{y}.
$$
Using this repeatedly to reduce the equal-height equation to first degree in $u_*$ gives
$$
\begin{aligned}
0={}&\left(16y^5+8y^4-127y^3+220y^2+288y-576\right)u_*\\
&+y\left(16y^3+4y^2-95y+192\right).
\end{aligned}
$$
Solving this linear equation for $u_*$ and substituting into the critical equation produces the factorization
$$
4y^2(4y^2+17y-12)^2(y^4-6y^2+17y-3)=0.
$$
On $0<y<1/4$, the quadratic factor has no zero, while
$$
h(y)=y^4-6y^2+17y-3
$$
satisfies $h(0)<0<h(1/4)$ and
$$
h'(y)=4y^3-12y+17>0.
$$
Therefore there is a unique $y_0\in(0,1/4)$ with
$$
y_0^4-6y_0^2+17y_0-3=0.
$$
For this $y_0$, the values at $-1/2,-r,r,1/2$ alternate between $\rho$ and $-\rho$, where
$$
\rho=\frac{1-4y_0}{2(4-y_0)}.
$$
Step 2 now shows that this $\rho$ is exactly $\rho_*$. The chosen zeros correspond to positive original parameters by the inverse formula in Step 1, so the bound is attained by an admissible three-stage cycle.

Step 4: Eliminate the auxiliary zero parameter and obtain the exact algebraic value
Solving the displayed relation for $y_0$ in terms of $\rho$ gives
$$
y_0=\frac{1-8\rho}{4-2\rho}.
$$
Substituting this into
$$
y_0^4-6y_0^2+17y_0-3=0
$$
and clearing denominators yields
$$
16\rho^4-8\rho^3+24\rho^2-32\rho+1=0.
$$
Also $h(2/13)<0$ and $h$ is increasing on $(0,1/4)$, so $y_0>2/13$. Therefore
$$
0<\rho=\frac{1-4y_0}{2(4-y_0)}<\frac{1}{20}.
$$
The polynomial
$$
p(t)=16t^4-8t^3+24t^2-32t+1
$$
has exactly one zero in $(0,1/20)$: indeed $p(0)=1$, $p(1/20)=-5409/10000$, and
$$
p'(t)=64t^3-24t^2+48t-32<0
$$
throughout that interval.

Step 5: Express the optimum in the notation requested by the problem
The global alternation certificate identifies the robust optimum, and Step 4 identifies it as the unique root of $p(t)$ in $(0,1/20)$. Numerically this root is approximately $0.0320108453$, consistent with the isolating interval but not needed for the exact answer.

Final Answer: $\boxed{\operatorname{Root}(16t^4-8t^3+24t^2-32t+1;(0,1/20))}$

---

## Answer

$\operatorname{Root}(16t^4-8t^3+24t^2-32t+1;(0,1/20))$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- reflected proximal iteration
- rational minimax approximation
- fractional linear transformation
- alternation certificate
- algebraic elimination

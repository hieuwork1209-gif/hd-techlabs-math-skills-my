## Steps

Step 1: Shift the spectral set and reduce the unrestricted problem to a polynomial extremal problem
Put $y=\lambda-3$. Then
$$
E=[1,2]\cup[4,5]
$$
becomes
$$
K=[-2,-1]\cup[1,2],
$$
and $\lambda=0$ corresponds to $y=-3$. For any five positive step sizes,
$$
P(\lambda)=\prod_{j=1}^{5}(1-\eta_j\lambda)
$$
has degree $5$ and satisfies $P(0)=1$. So $Q(y)=P(y+3)$ has degree at most $5$ and $Q(-3)=1$.

To obtain the extremal polynomial on the symmetric set $K$, it is enough to consider odd monic quintics. Indeed, if $S$ is any monic quintic, then its odd part
$$
S_{\mathrm{o}}(y)=\frac{S(y)-S(-y)}{2}
$$
is also monic, and symmetry of $K$ gives
$$
|S_{\mathrm{o}}(y)|\leq\frac{|S(y)|+|S(-y)|}{2}\leq\|S\|_K.
$$
Therefore minimizing over all monic quintics reduces to minimizing over odd monic quintics, which have the form
$$
T(y)=y^5+ay^3+by.
$$

Step 2: Determine the odd monic minimax polynomial by equioscillation
Seek $1<t<2$ and $L>0$ so that the odd quintic alternates with a positive interior critical point. Impose
$$
T(1)=L,\qquad T(t)=-L,\qquad T(2)=L,\qquad T'(t)=0.
$$
From $T(1)=T(2)$,
$$
1+a+b=32+8a+2b,
$$
so
$$
b=-31-7a.
$$
The derivative condition gives
$$
5t^4+3at^2+b=0.
$$
After inserting $b=-31-7a$,
$$
a(3t^2-7)=31-5t^4.
$$
The factor $3t^2-7$ cannot vanish, because $t^2=7/3$ would make the right side equal to $34/9$. Solving for $a$ and then $b$ gives
$$
a=-\frac{5t^4-31}{3t^2-7},\qquad
b=\frac{t^2(35t^2-93)}{3t^2-7}.
$$
Substituting these expressions into $T(t)+T(1)=0$ gives the explicit numerator identity
$$
(3t^2-7)(T(t)+T(1))
=-2(t+1)^2(t+2)^2(t^3-6t^2+9t-3).
$$
Since $1<t<2$, the first three factors on the right are nonzero, so
$$
t^3-6t^2+9t-3=0.
$$
Therefore $t$ is the unique root in $(1,2)$ of
$$
t^3-6t^2+9t-3=0.
$$
Indeed the cubic is strictly decreasing on $(1,2)$ because its derivative is $3(t-1)(t-3)$, and its values at $1$ and $2$ are $1$ and $-1$.

Since $L=T(1)=1+a+b=-30-6a$, substitution gives
$$
L=\frac{6(5t^4-15t^2+4)}{3t^2-7}.
$$
Also $t\in(\frac85,\frac53)$, because the cubic equals $17/125$ at $8/5$ and $-1/27$ at $5/3$. Using $T'(t)=0$, the derivative factors as
$$
T'(y)=5(y^2-t^2)(y^2-u_0),
\qquad
u_0=\frac{35t^2-93}{5(3t^2-7)}.
$$
Here $3t^2-7>0$, and $u_0<1$ is equivalent to $20t^2<58$, which follows from $t^2<\frac{25}{9}<\frac{29}{10}$. Therefore $t$ is the only critical point of $T$ in $(1,2)$. The endpoint and critical values are $L,-L,L$, so monotonicity on the two subintervals gives $|T(y)|\leq L$ on $[1,2]$. Oddness gives the same bound on $K$. The six ordered points
$$
-2,-t,-1,1,t,2
$$
carry the alternating values
$$
-L,L,-L,L,-L,L.
$$

Step 3: Normalize at the starting point, certify extremality, and evaluate $\rho_5$
The six alternating values certify that $T$ is the monic minimax polynomial: if another monic quintic $S$ had norm smaller than $L$, then $T-S$ would have alternating signs at those six points and so at least five distinct zeros, impossible for a polynomial of degree at most $4$.

Now set
$$
Q_*(y)=\frac{T(y)}{T(-3)}.
$$
Then $Q_*(-3)=1$ and $\|Q_*\|_K=L/|T(-3)|$. If another polynomial $Q$ of degree at most $5$ satisfied $Q(-3)=1$ and had smaller norm, then
$$
R(y)=T(y)-T(-3)Q(y)
$$
would satisfy $|T(-3)Q(y_i)|<L=|T(y_i)|$ at each of the six alternating points $y_i$. Therefore $R$ has the same alternating signs as $T$ there, so it has five zeros between them. It also has $R(-3)=0$. This gives six distinct zeros for a polynomial of degree at most $5$, a contradiction. Therefore $Q_*$ is the unrestricted residual minimizer.

The sign changes of $T$ give two roots in $(-2,-1)$, the root $0$, and two roots in $(1,2)$. After translating back by $\lambda=y+3$, all five roots lie in $(1,2)\cup\{3\}\cup(4,5)$, so they are positive and $Q_*$ is realizable by five positive gradient steps.

Using the formulas from Step 2,
$$
T(-3)=-243-27a-3b
=\frac{6(5t^4-75t^2+144)}{3t^2-7}.
$$
The bracket $t\in(\frac85,\frac53)$ from Step 2 makes the denominator positive. Writing $z=t^2$, the numerator factor $5z^2-75z+144$ is decreasing for $z<15/2$ and at $z=64/25$ it equals $-1904/125<0$, so $T(-3)<0$. Therefore
$$
\rho_5=\frac{L}{|T(-3)|}
=-\frac{5t^4-15t^2+4}{5t^4-75t^2+144}.
$$
Let
$$
c=\frac{2-t}{2}.
$$
Then $0<c<\frac12$, and the cubic for $t$ becomes
$$
8c^3-6c+1=0.
$$
Since $4c^3-3c=\cos(3\theta)$ when $c=\cos\theta$, the root in $(0,\frac12)$ is
$$
c=\cos\left(\frac{4\pi}{9}\right).
$$
Substituting $t=2-2c$ and using $c^3=(6c-1)/8$ and $c^4=(6c^2-c)/8$ reduces the numerator and denominator to
$$
-480c^2+450c-64
\quad\text{and}\quad
240c^2+30c-36.
$$
The identity
$$
(240c^2+30c-36)(-560c^2+520c-71)-171(-480c^2+450c-64)
=-300(56c-45)(8c^3-6c+1)
$$
then gives
$$
\rho_5=\frac{-560c^2+520c-71}{171}.
$$

Step 4: Derive a sharp lower bound for the stepwise-stable problem
For one step, the condition
$$
\max_{\lambda\in E}|1-\eta\lambda|\leq1
$$
is equivalent to
$$
0<\eta\leq\frac25.
$$
For a stable five-step schedule define
$$
u_j=|1-5\eta_j|\in[0,1],\qquad s=\prod_{j=1}^{5}u_j.
$$
For fixed $u_j$, the two possibilities $\eta_j=(1\mp u_j)/5$ show that
$$
1-\eta_j\geq\frac{4-u_j}{5}.
$$
For $P(\lambda)=\prod_{j=1}^{5}(1-\eta_j\lambda)$,
$$
P(1)\geq\frac{1}{5^5}\prod_{j=1}^{5}(4-u_j),
\qquad
|P(5)|=s.
$$
For $x,y\in[0,1]$,
$$
(4-x)(4-y)-3(4-xy)=4(1-x)(1-y)\geq0.
$$
Apply this inequality first to $u_1,u_2$, then to $u_1u_2,u_3$, and continue. Every intermediate product remains in $[0,1]$, so after four applications,
$$
\prod_{j=1}^{5}(4-u_j)\geq3^4(4-s).
$$
Therefore every stepwise-stable schedule satisfies
$$
\max_{\lambda\in E}|P(\lambda)|
\geq
\max\left\{\frac{81}{3125}(4-s),s\right\}.
$$
The first term decreases and the second increases with $s\in[0,1]$, so the minimum of this lower bound occurs when they are equal:
$$
s=\frac{81}{3125}(4-s).
$$
Therefore
$$
s=\frac{162}{1603},
$$
and therefore
$$
\widehat\rho_5\geq\frac{162}{1603}.
$$

Step 5: Attain the stable lower bound and assemble the ordered pair
Choose four steps equal to $\frac25$ and the fifth equal to
$$
\eta_* = \frac{353}{1603}.
$$
Then
$$
P_s(\lambda)=\left(1-\frac{2\lambda}{5}\right)^4
\left(1-\frac{353\lambda}{1603}\right).
$$
On $[1,2]$ all factors are positive with decreasing magnitudes, so
$$
\max_{\lambda\in[1,2]}|P_s(\lambda)|
=P_s(1)
=\left(\frac35\right)^4\frac{1250}{1603}
=\frac{162}{1603}.
$$

Let $r=1603/353$, the zero of the last factor. On $[r,5]$, both absolute factors increase with $\lambda$, so the maximum there is
$$
|P_s(5)|=\frac{162}{1603}.
$$
On $[4,r]$, one has $r<55/12$, so
$$
0\leq\frac{2\lambda}{5}-1<\frac56,
$$
while
$$
0\leq1-\frac{353\lambda}{1603}\leq\frac{191}{1603}<\frac{324}{1603}.
$$
Since $(5/6)^4<1/2$, these two bounds give
$$
|P_s(\lambda)|<\frac12\cdot\frac{324}{1603}=\frac{162}{1603}
$$
throughout $[4,r]$. Therefore the lower bound is attained and
$$
\widehat\rho_5=\frac{162}{1603}.
$$
With $c=\cos(4\pi/9)$ in the unrestricted value from Step 3, the required pair is obtained.
Final Answer: $\boxed{\left(\frac{-560\cos^2(4\pi/9)+520\cos(4\pi/9)-71}{171},\frac{162}{1603}\right)}$

---

## Answer

$\left(\frac{-560\cos^2(4\pi/9)+520\cos(4\pi/9)-71}{171},\frac{162}{1603}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- minimax residual polynomials
- equioscillation
- odd polynomial symmetrization
- nonstationary gradient descent
- extremal product inequalities

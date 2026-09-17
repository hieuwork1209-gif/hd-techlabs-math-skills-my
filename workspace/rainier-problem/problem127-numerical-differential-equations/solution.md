## Steps

Step 1: Impose the Runge-Kutta order conditions
Write
$$
A=\begin{pmatrix}
\gamma&0&0\\
a&\gamma&0\\
u&v&\gamma
\end{pmatrix},
\qquad
b^T=(u,v,\gamma),
\qquad
c=A\mathbf 1.
$$
Stiff accuracy means that the weight vector is the last row of $A$. The classical order-three conditions are
$$
b^T\mathbf 1=1,
\qquad
b^Tc=\frac12,
\qquad
b^T(c\circ c)=\frac13,
\qquad
b^TAc=\frac16.
$$
The first condition gives
$$
u+v+\gamma=1,
$$
so the last component of $c$ is $1$. Put
$$
s=a+\gamma.
$$
Then
$$
c=(\gamma,s,1)^T.
$$
The order-two condition becomes
$$
2\gamma-\gamma^2+v(s-\gamma)=\frac12.
$$
Hence
$$
v(s-\gamma)=\gamma^2-2\gamma+\frac12.
$$
For the fourth order condition above, the last component of $Ac$ is exactly $b^Tc=1/2$, while the first two components are $\gamma^2$ and $\gamma(2s-\gamma)$. Therefore
$$
b^TAc
=\gamma^2(1-\gamma)+2\gamma v(s-\gamma)+\frac{\gamma}{2}.
$$
Substituting the preceding expression for $v(s-\gamma)$ and setting $b^TAc=1/6$ gives
$$
6\gamma^3-18\gamma^2+9\gamma-1=0.
$$
Conversely, for any root of this cubic, the remaining order conditions give
$$
a=\frac{1-\gamma}{2},
$$
$$
u=\frac{-6\gamma^2+16\gamma-1}{4},
\qquad
v=\frac{6\gamma^2-20\gamma+5}{4}.
$$
Substitution into the four displayed order conditions verifies order three. Thus the cubic is exactly the algebraic condition for existence of a stiffly accurate three-stage SDIRK method of order three.

Step 2: Reduce A-stability to an exact inequality on the imaginary axis
For the test equation $y'=zy$, the stability function of a Runge-Kutta method is
$$
R(z)=1+z\,b^T(I-zA)^{-1}\mathbf1.
$$
Because the method is stiffly accurate,
$$
b^T=e_3^TA,
$$
and therefore
$$
R(z)=e_3^T(I-zA)^{-1}\mathbf1.
$$
Since every diagonal entry of $A$ equals $\gamma$,
$$
\det(I-zA)=(1-\gamma z)^3.
$$
The numerator has degree at most two. Order three requires
$$
R(z)=e^z+O(z^4)
$$
near $z=0$, so the numerator is forced to be
$$
N(z)=1+(1-3\gamma)z+\left(\frac12-3\gamma+3\gamma^2\right)z^2.
$$
Thus
$$
R(z)=\frac{N(z)}{(1-\gamma z)^3}.
$$
For $\gamma>0$, all poles lie at the positive real point $1/\gamma$. Hence $R$ is analytic on the closed left half-plane and tends to $0$ at infinity there. By the maximum-modulus principle, A-stability is equivalent to
$$
|R(iy)|\leq1
$$
for every real $y$.

Using the cubic relation from Step 1, direct expansion gives
$$
|(1-i\gamma y)^3|^2-|N(iy)|^2
$$
$$
=\frac{y^4}{36}
\left[
(1575\gamma^2-936\gamma+109)y^2
-108\gamma^2+72\gamma-9
\right].
$$
Therefore A-stability requires
$$
-108\gamma^2+72\gamma-9\geq0,
$$
which is equivalent to
$$
\frac16\leq\gamma\leq\frac12.
$$

Step 3: Show that exactly one cubic root passes the stability inequality
Let
$$
p(x)=6x^3-18x^2+9x-1.
$$
Then
$$
p'(x)=9(2x^2-4x+1).
$$
On $[1/6,1/2]$, $p$ first increases and then decreases, with its only critical point there at
$$
1-\frac1{\sqrt2}.
$$
Moreover,
$$
p\left(\frac16\right)=\frac1{36}>0,
\qquad
p\left(\frac12\right)=-\frac14<0.
$$
Hence $p$ has exactly one root $\gamma_*$ in $[1/6,1/2]$.

It remains to check that the coefficient of $y^2$ in the bracket from Step 2 is positive at this root. Since $p$ is decreasing near $\gamma_*$ and
$$
p\left(\frac{61}{140}\right)=\frac{683}{1372000}>0,
$$
$$
p\left(\frac{109}{250}\right)=-\frac{3413}{7812500}<0,
$$
we have
$$
\frac{61}{140}<\gamma_*<\frac{109}{250}.
$$
The quadratic
$$
A(x)=1575x^2-936x+109
$$
is increasing for $x>52/175$, and
$$
A\left(\frac{61}{140}\right)=\frac{101}{560}>0.
$$
Thus
$$
A(\gamma_*)>0.
$$
Consequently the expression in Step 2 is nonnegative for every real $y$, so $\gamma_*$ is A-stable.

Every other root of $p$ lies outside $[1/6,1/2]$, so for those roots the constant term
$$
-108\gamma^2+72\gamma-9
$$
is negative; then $|R(iy)|>1$ for all sufficiently small nonzero $y$. Hence no other cubic root is A-stable.

Step 4: State the complete parameter set
There is therefore exactly one admissible diagonal parameter: the unique root of the order-three cubic lying between $1/6$ and $1/2$.

Final Answer: $\boxed{\{\gamma\in(1/6,1/2):6\gamma^3-18\gamma^2+9\gamma-1=0\}}$

---

## Answer

$\{\gamma\in(1/6,1/2):6\gamma^3-18\gamma^2+9\gamma-1=0\}$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Set or multiset of objects

---

## Solution Concepts

- Runge-Kutta order conditions
- stiffly accurate SDIRK methods
- rational stability functions
- A-stability
- maximum-modulus principle

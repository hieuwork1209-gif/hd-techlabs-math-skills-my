## Steps

Step 1: Build a global certificate from three alternating rational contacts
For $A,B>0$, write
$$
R_{A,B}(x)=\frac{Ax^2}{x^2+B},\qquad e_{A,B}(x)=x-R_{A,B}(x).
$$
Suppose a candidate $R_*$ has points $0<u<v<1$ such that
$$
e_*(u)=E,\qquad e_*(v)=-E,\qquad e_*(1)=E,
$$
and $\|e_*\|_{\infty,[0,1]}=E>0$. If another $R_{A,B}$ had smaller uniform error, then
$$
D(x)=R_{A,B}(x)-R_*(x)=e_*(x)-e_{A,B}(x)
$$
would have signs $+,-,+$ at $u,v,1$. Hence $D$ would have one zero in $(u,v)$ and another in $(v,1)$. But for $R_*=R_{A_*,B_*}$,
$$
D(x)=\frac{x^2\left((A-A_*)x^2+AB_*-A_*B\right)}{(x^2+B)(x^2+B_*)}.
$$
For $x>0$ its numerator is affine in $x^2$, so a nonzero $D$ has at most one positive zero. Thus any candidate with the displayed alternating contacts and full error bound is globally optimal.

Step 2: Derive the scale-free equations for the two interior extrema
Set
$$
y=\sqrt B,
$$
and write the two interior stationary points as
$$
u=yr,\qquad v=ys,
$$
with $0<r<s$. Since
$$
e_{A,B}'(x)=1-\frac{2ABx}{(x^2+B)^2},
$$
a stationary point $x=yt$ satisfies
$$
A=y\frac{(1+t^2)^2}{2t}.
$$
Therefore stationarity at both $r$ and $s$ gives
$$
\frac{(1+r^2)^2}{r}=\frac{(1+s^2)^2}{s}.
$$
At a stationary point,
$$
e_{A,B}(yt)=\frac{yt(1-t^2)}2.
$$
Equal magnitudes with opposite signs at the two interior extrema therefore give
$$
r(1-r^2)=s(s^2-1).
$$
The second equation is equivalent to
$$
r^2-rs+s^2=1.
$$
The first equation factors, since $r\ne s$, to
$$
rs\left(r^2+rs+s^2+2\right)=1.
$$
Let $q=rs$. Using $r^2+s^2=1+q$, this becomes
$$
q(3+2q)=1.
$$
Hence
$$
q=\frac{\sqrt{17}-3}{4}.
$$
Let $S=\sqrt{1+3q}$ and let $r<s$ be the two roots of
$$
t^2-St+q=0.
$$
Then $r^2-rs+s^2=1$ and the stationarity equation above both hold. Also $S>1+q$, so $1-S+q<0$ and the two positive roots straddle $1$; thus
$$
0<r<1<s.
$$
Since $q<2/7$ and $s>1$, one also has $r=q/s<2/7<1/\sqrt3$.

Step 3: Fix the denominator scale and verify the full alternating error pattern
Define
$$
K=\frac{(1+r^2)^2}{2r},\qquad L=\frac{r(1-r^2)}2.
$$
Choose
$$
y=\frac{2r}{1-r^2},\qquad B=y^2,\qquad A=yK.
$$
The two stationary points are $u=yr$ and $v=ys$. Since
$$
v=\frac{2rs}{1-r^2}=\frac{2q}{1-r^2}
$$
and $q<2/7$, $r<2/7$, one gets
$$
v<\frac{4/7}{1-4/49}=\frac{28}{45}<1.
$$
Thus $0<u<v<1$.

At the two stationary points the errors are $yL$ and $-yL$. It remains to match the endpoint. The condition $e_{A,B}(1)=yL$ is
$$
1-\frac{yK}{1+y^2}=yL.
$$
After clearing $1+y^2$, this is equivalent to
$$
Ly^3-y^2+(K+L)y-1=0.
$$
Direct factorization gives
$$
Ly^3-y^2+(K+L)y-1
=-\frac{(ry-1)^2(r^2y+2r-y)}{2r}.
$$
Our choice $y=2r/(1-r^2)$ makes the last factor zero, so indeed
$$
e_{A,B}(u)=yL,\qquad e_{A,B}(v)=-yL,\qquad e_{A,B}(1)=yL.
$$

To prove there are no larger errors, define
$$
H(t)=\frac{(1+t^2)^2}{2t}.
$$
Then
$$
e_{A,B}'(yt)=1-\frac{H(r)}{H(t)}.
$$
Moreover,
$$
H'(t)=\frac{3t^4+2t^2-1}{2t^2},
$$
so $H$ decreases on $(0,1/\sqrt3)$ and increases on $(1/\sqrt3,\infty)$. Because $r<1/\sqrt3<s$ and $H(r)=H(s)$, the derivative of the error has signs $+,-,+$ across $u,v$. Since $v<1$, the error rises from $e(0)=0$ to $yL$, falls to $-yL$, and rises to $e(1)=yL$. Hence
$$
\|e_{A,B}\|_{\infty,[0,1]}=yL.
$$
Step 1 now proves global optimality.

Step 4: Express the optimal error algebraically
For the constructed minimizer,
$$
E=yL=\frac{2r}{1-r^2}\cdot\frac{r(1-r^2)}2=r^2.
$$
Since $q=rs$ and $r^2-rs+s^2=1$, substituting $s=q/r$ gives
$$
E^2-(1+q)E+q^2=0.
$$
Together with
$$
2q^2+3q-1=0,
$$
this yields
$$
q=\frac{2E^2-2E+1}{2E+3}.
$$
Substitution back into $2q^2+3q-1=0$ gives
$$
4E^4-2E^3+9E^2-16E+1=0.
$$
Thus the optimal error is annihilated by
$$
P(T)=4T^4-2T^3+9T^2-16T+1.
$$

Step 5: Prove that the polynomial is primitive and irreducible
The coefficients of $P$ have gcd $1$, so $P$ is primitive. Modulo $3$,
$$
P(T)\equiv T^4+T^3-T+1.
$$
Its values at $T=0,1,2$ are $1,2,2$, so it has no linear factor over $\mathbb F_3$. The three monic irreducible quadratics over $\mathbb F_3$ are
$$
T^2+1,\qquad T^2+T+2,\qquad T^2-T+2.
$$
Dividing $T^4+T^3-T+1$ by these gives respective remainders
$$
T-1,\qquad T-1,\qquad T+1,
$$
so no quadratic factor exists. Hence the reduction is irreducible over $\mathbb F_3$, and Gauss's lemma implies that $P$ is irreducible over $\mathbb Q$.

Therefore $P$ is the primitive irreducible polynomial with positive leading coefficient satisfied by the minimum error.

Final Answer: $\boxed{4T^4-2T^3+9T^2-16T+1}$

---

## Answer

$4T^4-2T^3+9T^2-16T+1$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Polynomial or rational function

---

## Solution Concepts

- rational minimax approximation
- alternation sign-change certificate
- scale-free stationary equations
- algebraic elimination
- finite-field irreducibility

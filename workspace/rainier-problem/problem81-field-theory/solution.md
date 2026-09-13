## Steps

Step 1: Recover the unique function for a fixed phase vector and flag.
For a nonzero projective character direction, set $\alpha=\widehat f(y)$ and let $m=m_y\in\{q,q+2Q,q+4Q\}$. The Galois conjugates of $\alpha$ have common absolute value $m$. Since each such prime is congruent to $q\equiv2^{-1}\pmod\ell$ and $2$ generates $\mathbb F_\ell^\times$, each is inert in $\mathbb Q(\zeta)$. In particular,
$$
\alpha\overline\alpha=m^2.
$$
Because $m$ is inert, $(m)$ is a conjugation-invariant prime ideal. Taking ideal valuations in
$$
(\alpha)(\overline\alpha)=(m)^2
$$
shows that no prime other than $(m)$ occurs, while conjugation fixes $(m)$ and gives equal valuations to $(\alpha)$ and $(\overline\alpha)$. Their sum is $2$, so each valuation is $1$ and therefore $(\alpha)=(m)$. Hence $\alpha/m$ is an algebraic-integer unit, and all of its conjugates have modulus $1$. By Kronecker's theorem, $\alpha/m$ is a root of unity in $\mathbb Q(\zeta)$, so
$$
\frac{\alpha}{m}=\pm\zeta^{a_y}
$$
for some $a_y\in\mathbb F_\ell$.

Put $\lambda=1-\zeta$. Modulo $\lambda$, one has $\alpha\equiv\sum_xf(x)=2q^2$ and $m\equiv q$, so
$$
\frac{\alpha}{m}\equiv\frac{2q^2}{q}=2q\equiv1\pmod\lambda.
$$
Since $\pm\zeta^{a_y}\equiv\pm1\pmod\lambda$ and $\ell$ is odd, the negative sign is impossible. Thus $\alpha=m\zeta^{a_y}$.

Modulo $\lambda^2$,
$$
\widehat f(y)\equiv2q^2-\lambda\Bigl(\sum_xf(x)x\Bigr)\cdot y
=2q^2-\lambda(Ps\cdot y),
$$
while
$$
m_y\zeta^{a_y}\equiv m_y-\lambda m_ya_y.
$$
Because $2q^2-m_y$ is divisible by $Q=\ell^r$, the constant terms agree modulo $\lambda^2$. Thus
$$
Ps\cdot y=q\,a_y,
$$
and $q^{-1}\equiv2\pmod\ell$ gives
$$
a_y=2Ps\cdot y.
$$
Therefore $f$ is forced by Fourier inversion. Writing $a=2Ps-x$ and using
$$
\sum_{0\ne y\in V^\perp}\zeta^{a\cdot y}=|V^\perp|1_V(a)-1,
$$
we obtain
$$
f(x)=d-4+q\,1_{\{2Ps\}}(x)+2\ell^2 1_{2Ps+W}(x)+2\ell 1_{2Ps+U}(x),
\qquad d=\frac{q(2q-1)}Q.
$$
This is nonnegative and has the required Fourier magnitudes. It also satisfies the original mass and moment conditions. Since $|G|=Q$, $|W|=Q/\ell^2$, and $|U|=Q/\ell$,
$$
\sum_x f(x)=Q(d-4)+q+2Q+2Q=2q^2.
$$
For the first moment, the constant term contributes zero in $G$. The two affine-coset terms also contribute zero: for either relevant subspace $V$, one has $\sum_{v\in V}v=0$ and $|V|=0$ as a scalar in $\mathbb F_\ell$, so the sum of the points of any coset of $V$ is zero. The singleton contributes
$$
q(2Ps)=Ps,
$$
because $2q=1$ in $\mathbb F_\ell$. Thus $\sum_xf(x)x=Ps$. The four values of $f$ are distinct, so for fixed $s$ it recovers $W$ and $U$. Hence counting pairs $(s,f)$ is exactly counting admissible triples $(s,U,W)$.

Step 2: Couple the reciprocal frequency to the product constraint.
The span condition implies
$$
Ps+P^{-1}s=a\mathbf{1}+bs.
$$
The constant case is excluded by the product conditions. With $y=s-\mathbf{1}$ and $\sum_jy_j=0$, diagonalizing the cyclic shift gives
$$
s_j=1+u\omega^{j-1}+v\omega^{-(j-1)},
$$
where $\omega$ is a nontrivial $r$th root of unity. Reciprocal frequencies give the same eigenspace.

Since $r$ is odd,
$$
\prod_{j=0}^{r-1}(u\omega^j+v\omega^{-j})=u^r+v^r.
$$
The condition $\prod_j(s_j-1)=2$ therefore gives $u^r+v^r=2$. Since $r=(\ell-1)/2$, Euler's criterion gives
$$
z^r\in\{0,1,-1\}
$$
for every $z\in\mathbb F_\ell$. Because $\ell\ge11$, the residues represented by $-2,-1,0,1,2$ are distinct, so two values from $\{0,1,-1\}$ can sum to $2$ only when both are $1$. Hence $u^r=v^r=1$. Thus $u,v$ lie in the subgroup $H\subset\mathbb F_\ell^\times$ of order $r$. Put $c=uv$ and $t=\omega+\omega^{-1}$.

Now
$$
y_j+y_{j+1}=u(1+\omega)\omega^{j-1}+v(1+\omega^{-1})\omega^{-(j-1)}.
$$
The pure Fourier modes sum to zero, so
$$
\sum_j(y_j+y_{j+1})^2
=2rc(1+\omega)(1+\omega^{-1})
=-c(t+2),
$$
because $2r=-1$ in $\mathbb F_\ell$. The cyclic energy condition therefore gives
$$
c=\frac1{t+2}=\frac{\omega}{(1+\omega)^2}.
$$
Here $1+\omega\ne0$ because $H$ has odd order.

Let $A,B$ be the roots of $T^2+T+c$. Then
$$
\prod_js_j=2-(A^r+B^r).
$$
For $c=\omega/(1+\omega)^2$, the roots are explicitly
$$
A=-\frac1{1+\omega},\qquad B=-\frac{\omega}{1+\omega}.
$$
Since $\omega\in H$, both roots have quadratic character
$$
\chi(A)=\chi(B)=-\chi(1+\omega),
$$
using $\chi(-1)=-1$. Therefore $\prod_js_j=4$ exactly when both roots are nonresidues, which is equivalent to
$$
\chi(1+\omega)=1.
$$

The number of $\omega\in H$ satisfying this condition is
$$
\frac14\sum_{x\ne0,-1}(1+\chi(x))(1+\chi(1+x))
=\frac{\ell-3}{4}=\frac{r-1}{2}.
$$
Indeed the three nonconstant character sums are $1,-1,-1$. The value $\omega=1$ is not counted because $\chi(2)=-1$, and the condition is invariant under $\omega\mapsto\omega^{-1}$. Thus there are $(r-1)/4$ admissible reciprocal frequency pairs. For each pair, the displayed formula for $c$ fixes $c\in H$, and there are exactly $r$ factorizations $c=uv$ in $H^2$. Therefore
$$
N_s=\frac{r(r-1)}4.
$$

Step 3: Count flags from the full affine conic and its secant directions.
For a phase vector from Step 2, put
$$
e_0=\mathbf{1},\qquad e_+=(\omega^{j-1})_j,\qquad e_-=(\omega^{-(j-1)})_j,
$$
and let
$$
H_s=\operatorname{span}\{e_0,e_+,e_-\}.
$$
The three eigenvalues $1,\omega,\omega^{-1}$ of $P$ are distinct, so $\dim H_s=3$. Also $Pe_0=e_0$, $Pe_+=\omega e_+$, $Pe_-=\omega^{-1}e_-$, and the phase-vector formula gives
$$
s=e_0+ue_++ve_-,
$$
with $u,v\ne0$. We now verify that the required orbit vectors actually span $H_s$. If
$$
\alpha_0s+\alpha_1Ps+\alpha_2P^2s=0,
$$
set $p(z)=\alpha_0+\alpha_1z+\alpha_2z^2$. Comparing the $e_0,e_+,e_-$ coefficients yields
$$
p(1)=p(\omega)=p(\omega^{-1})=0.
$$
These are three distinct field elements, while $\deg p\le2$, so $p=0$. Hence $s,Ps,P^2s$ are linearly independent and therefore span $H_s$. Since they are among the required vectors $P^ts$, every admissible $U$ contains $H_s$. Conversely, $H_s$ is $P$-invariant and contains $s$, $2\mathbf{1}-s$, and $Ps-s$, so all three required cyclic orbits lie in $H_s$. Thus the condition on $U$ is exactly $H_s\subset U$, giving
$$
\frac{\ell^{r-3}-1}{\ell-1}
$$
choices.

After scaling the last two projective coordinates, set
$$
A_t=[1:\omega^t:\omega^{-t}],\qquad
B_t=[1:-\omega^t:-\omega^{-t}],
$$
$$
D_t=[0:\omega^t(\omega-1):\omega^{-t}(\omega^{-1}-1)].
$$
The $A_t$ are the points coming from $P^ts$, the $B_t$ from $P^t(2\mathbf{1}-s)$, and the $D_t$ from $P^t(Ps-s)$. Since $H$ is the subgroup of squares and $-1$ is a nonsquare, the sets $\{A_t\}$ and $\{B_t\}$ together are exactly
$$
\{[1:a:a^{-1}]:a\in\mathbb F_\ell^\times\},
$$
the full affine part of the conic $YZ=X^2$.

Moreover
$$
\{D_t\}=\{[0:1:-1/c]:c\in H\}.
$$
For two affine conic points with parameters $a,b$, their secant meets the line at infinity at
$$
[0:1:-1/(ab)].
$$
Thus the forbidden $D_t$ are exactly the secant directions for which $ab$ is a square.

Fix $U$. The projective line $\mathbb P(W\cap H_s)$ must avoid all affine conic points and forbidden directions described above. A permitted direction at infinity is either one of the $r$ complementary nonzero directions or one of the two conic points at infinity. For a complementary nonzero direction, the secant formula pairs the $\ell-1$ affine conic points into exactly $r$ secants, with no tangent of that direction. Hence among the $\ell$ affine lines of that direction exactly
$$
\ell-r=r+1
$$
avoid the affine conic. For either conic direction at infinity, exactly one affine line avoids it. Therefore the number of allowable projective kernel lines is
$$
r(r+1)+2=r^2+r+2.
$$
Each extends to a hyperplane $W\subset U$ in exactly $\ell^{r-4}$ ways. Thus the number of admissible flags for one $s$ is
$$
F=\ell^{r-4}(r^2+r+2)\frac{\ell^{r-3}-1}{\ell-1}.
$$

Step 4: Multiply the coupled phase count by the flag count.
By Step 1, every admissible phase vector and admissible flag produces exactly one pair $(s,f)$, and $f$ recovers the flag. Multiplying
$$
N_s=\frac{r(r-1)}4
$$
by
$$
F=\ell^{r-4}(r^2+r+2)\frac{\ell^{r-3}-1}{\ell-1}
$$
gives the required count.
Final Answer: $\boxed{\frac{r(r-1)(r^2+r+2)}4\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}}$

---

## Answer

$\frac{r(r-1)(r^2+r+2)}4\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- cyclotomic phase rigidity from inert primes
- reciprocal cyclic modes over a finite field
- cyclic quadratic-energy coupling
- quadratic-character counting
- affine conic secants and projective directions

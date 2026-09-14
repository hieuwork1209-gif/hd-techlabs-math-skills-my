## Steps

Step 1: Recover the unique function for a fixed phase vector and flag.
For a nonzero projective character direction, set $\alpha=\widehat f(y)$ and let $m=m_y\in\{q,q+2Q,q+4Q\}$. The Galois conjugates of $\alpha$ have common absolute value $m$. We justify the inertness used below. For a prime $p\ne\ell$, the residue degree of any prime of $\mathbb Q(\zeta)$ above $p$ equals $\operatorname{ord}_\ell(p)$; hence $p$ is inert exactly when this order is $[\mathbb Q(\zeta):\mathbb Q]=\ell-1$. Here every possible $m$ satisfies
$$
m\equiv q\equiv2^{-1}\pmod\ell,
$$
because $\ell\mid Q$ and $2q\equiv1\pmod Q$. Since $2$ generates $\mathbb F_\ell^\times$, $\operatorname{ord}_\ell(2)=\ell-1$, and inversion preserves multiplicative order, so $\operatorname{ord}_\ell(2^{-1})=\ell-1$. Thus every possible $m$ is inert in $\mathbb Q(\zeta)$. In particular,
$$
\alpha\overline\alpha=m^2.
$$
Because $(m)$ is then a conjugation-invariant prime ideal, taking valuations in
$$
(\alpha)(\overline\alpha)=(m)^2
$$
shows that no other prime ideal occurs, while conjugation gives equal valuations to $(\alpha)$ and $(\overline\alpha)$. Their sum is $2$, so each is $1$, hence $(\alpha)=(m)$. Therefore $\alpha/m$ is an algebraic-integer unit all of whose conjugates have modulus $1$. By Kronecker's theorem,
$$
\frac{\alpha}{m}=\pm\zeta^{a_y}
$$
for some $a_y\in\mathbb F_\ell$.

Put $\lambda=1-\zeta$. Modulo $\lambda$,
$$
\frac{\alpha}{m}\equiv\frac{2q^2}{q}=2q\equiv1,
$$
while $\pm\zeta^{a_y}\equiv\pm1$, so the negative sign is impossible. Thus $\alpha=m\zeta^{a_y}$. Modulo $\lambda^2$,
$$
\widehat f(y)\equiv2q^2-\lambda(Ps\cdot y),
\qquad
m_y\zeta^{a_y}\equiv m_y-\lambda m_ya_y.
$$
Since $2q^2-m_y$ is divisible by $Q=\ell^r$, the constant terms agree modulo $\lambda^2$. Hence
$$
Ps\cdot y=q\,a_y,
$$
and $q^{-1}\equiv2\pmod\ell$ gives $a_y=2Ps\cdot y$.

Fourier inversion is now forced. Writing $a=2Ps-x$ and using
$$
\sum_{0\ne y\in V^\perp}\zeta^{a\cdot y}=|V^\perp|1_V(a)-1,
$$
we obtain
$$
f(x)=d-4+q\,1_{\{2Ps\}}(x)+2\ell^2 1_{2Ps+W}(x)+2\ell 1_{2Ps+U}(x),
\qquad d=\frac{q(2q-1)}Q.
$$
This is nonnegative and has the required Fourier magnitudes. Also
$$
\sum_x f(x)=Q(d-4)+q+2Q+2Q=2q^2.
$$
The constant term has zero first moment in $G$. For either relevant subspace $V$, $\sum_{v\in V}v=0$ and $|V|=0$ in $\mathbb F_\ell$, so every affine coset of $V$ also has vector sum $0$. The singleton contributes $q(2Ps)=Ps$ because $2q=1$ in $\mathbb F_\ell$. Thus $\sum_xf(x)x=Ps$. The four values of $f$ are distinct, so for fixed $s$ the function recovers $W$ and $U$. Hence counting pairs $(s,f)$ is exactly counting admissible triples $(s,U,W)$.

Step 2: Couple the reciprocal frequency to the product constraint.
The span condition implies
$$
Ps+P^{-1}s=a\mathbf{1}+bs.
$$
The constant case is excluded by the product conditions. With $y=s-\mathbf{1}$ and $\sum_jy_j=0$, diagonalizing the cyclic shift gives
$$
s_j=1+u\omega^{j-1}+v\omega^{-(j-1)},
$$
where $\omega$ is a nontrivial $r$th root of unity; reciprocal frequencies give the same eigenspace.

Since $r$ is odd,
$$
\prod_{j=0}^{r-1}(u\omega^j+v\omega^{-j})=u^r+v^r.
$$
Thus $\prod_j(s_j-1)=2$ gives $u^r+v^r=2$. Since $r=(\ell-1)/2$, Euler's criterion gives $z^r\in\{0,1,-1\}$ for every $z\in\mathbb F_\ell$. As $\ell\ge11$, only $1+1$ can equal $2$, so $u^r=v^r=1$. Hence $u,v$ lie in the subgroup $H\subset\mathbb F_\ell^\times$ of order $r$. Put $c=uv$ and $t=\omega+\omega^{-1}$.

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
because $2r=-1$ in $\mathbb F_\ell$. The cyclic energy condition gives
$$
c=\frac1{t+2}=\frac{\omega}{(1+\omega)^2}.
$$
Here $1+\omega\ne0$ because $H$ has odd order.

Let $A,B$ be the roots of $T^2+T+c$. For $z_j=u\omega^j$ we have $v\omega^{-j}=c/z_j$, hence
$$
s_{j+1}=1+z_j+\frac c{z_j}=\frac{(z_j-A)(z_j-B)}{z_j}.
$$
Since $u^r=1$ and $\{u\omega^j:0\le j<r\}$ is the full set of roots of $Z^r-1$, while $r$ is odd so their product is $1$,
$$
\prod_j(z_j-A)=1-A^r,
\qquad
\prod_j(z_j-B)=1-B^r.
$$
Also $AB=c$ and $c^r=1$. Therefore
$$
\prod_js_j=(1-A^r)(1-B^r)
=1-(A^r+B^r)+(AB)^r
=2-(A^r+B^r).
$$
For $c=\omega/(1+\omega)^2$ the roots are
$$
A=-\frac1{1+\omega},\qquad B=-\frac{\omega}{1+\omega}.
$$
Since $\omega\in H$ and $\chi(-1)=-1$,
$$
\chi(A)=\chi(B)=-\chi(1+\omega).
$$
Thus $\prod_js_j=4$ exactly when both roots are nonresidues, equivalently $\chi(1+\omega)=1$.

We now evaluate the character count explicitly:
$$
N=\frac14\sum_{x\ne0,-1}(1+\chi(x))(1+\chi(1+x)).
$$
The three nonconstant sums are
$$
\sum_{x\ne0,-1}\chi(x)=-\chi(-1)=1,
$$
$$
\sum_{x\ne0,-1}\chi(1+x)=\sum_{y\ne0,1}\chi(y)=-1,
$$
and
$$
\sum_{x\ne0,-1}\chi(x(1+x))=-1.
$$
For the last identity, completing the square and changing variables reduces it to $\sum_t\chi(t^2-1)$. If
$$
M=\#\{(t,z):z^2=t^2-1\},
$$
then $M=\ell+\sum_t\chi(t^2-1)$. On the other hand $(t-z)(t+z)=1$, and each $a\in\mathbb F_\ell^\times$ gives uniquely
$$
t=\frac{a+a^{-1}}2,\qquad z=\frac{a^{-1}-a}2,
$$
so $M=\ell-1$. Hence the sum is $-1$. Therefore
$$
N=\frac14\bigl((\ell-2)+1-1-1\bigr)=\frac{\ell-3}{4}=\frac{r-1}{2}.
$$
The value $\omega=1$ is not counted because $\chi(2)=-1$, and the condition is invariant under $\omega\mapsto\omega^{-1}$. Hence there are $(r-1)/4$ admissible reciprocal frequency pairs. For each pair, $c$ is fixed and there are exactly $r$ factorizations $c=uv$ in $H^2$. Thus
$$
N_s=\frac{r(r-1)}4.
$$

Step 3: Count flags from the full affine conic and its secant directions.
For a phase vector from Step 2, put
$$
e_0=\mathbf{1},\qquad e_+=(\omega^{j-1})_j,\qquad e_-=(\omega^{-(j-1)})_j,
$$
and let $H_s=\operatorname{span}\{e_0,e_+,e_-\}$. The eigenvalues $1,\omega,\omega^{-1}$ are distinct, so $\dim H_s=3$. Since
$$
s=e_0+ue_++ve_-,
$$
if $\alpha_0s+\alpha_1Ps+\alpha_2P^2s=0$ and $p(z)=\alpha_0+\alpha_1z+\alpha_2z^2$, comparison of the three eigencoordinates gives $p(1)=p(\omega)=p(\omega^{-1})=0$. Thus $p=0$, so $s,Ps,P^2s$ span $H_s$. Consequently every admissible $U$ contains $H_s$. Conversely, $H_s$ is $P$-invariant and contains $s$, $2\mathbf{1}-s$, and $Ps-s$, so it contains all required cyclic orbits. Hence the condition on $U$ is exactly $H_s\subset U$.

Now $U$ is a hyperplane of the $r$-dimensional space $G$. Hyperplanes of $G$ containing $H_s$ correspond bijectively to hyperplanes of the quotient $G/H_s$, which has dimension $r-3$. The number of hyperplanes in an $n$-dimensional $\mathbb F_\ell$-space equals the number of one-dimensional subspaces of its dual,
$$
\frac{\ell^n-1}{\ell-1}.
$$
Therefore the number of possible $U$ is
$$
\frac{\ell^{r-3}-1}{\ell-1}.
$$

After scaling the last two projective coordinates, set
$$
A_t=[1:\omega^t:\omega^{-t}],\qquad
B_t=[1:-\omega^t:-\omega^{-t}],
$$
$$
D_t=[0:\omega^t(\omega-1):\omega^{-t}(\omega^{-1}-1)].
$$
The $A_t$ come from $P^ts$, the $B_t$ from $P^t(2\mathbf{1}-s)$, and the $D_t$ from $P^t(Ps-s)$. Since $H$ is the subgroup of squares and $-1$ is a nonsquare, $\{A_t\}\cup\{B_t\}$ is exactly
$$
\{[1:a:a^{-1}]:a\in\mathbb F_\ell^\times\},
$$
the full affine part of the conic $YZ=X^2$. Moreover
$$
\{D_t\}=\{[0:1:-1/c]:c\in H\}.
$$
For affine conic points with parameters $a,b$, their secant meets the line at infinity at $[0:1:-1/(ab)]$. Thus the forbidden $D_t$ are exactly the secant directions for which $ab$ is a square.

Fix $U$. The projective line $\mathbb P(W\cap H_s)$ must avoid all affine conic points and forbidden directions. A permitted direction at infinity is either one of the $r$ complementary nonzero directions or one of the two conic points at infinity. For a complementary nonzero direction, the secant formula pairs the $\ell-1$ affine conic points into exactly $r$ secants and there is no tangent of that direction. Thus among the $\ell$ affine lines of that direction exactly $\ell-r=r+1$ avoid the affine conic. For either conic direction at infinity, exactly one affine line avoids it. Hence the number of allowable projective kernel lines is
$$
r(r+1)+2=r^2+r+2.
$$

Let $K=W\cap H_s$ be one fixed allowable $2$-dimensional subspace. Choose a nonzero linear functional $\lambda$ on $H_s$ with kernel $K$. A hyperplane $W\subset U$ with $W\cap H_s=K$ is the kernel of a linear functional $\varphi$ on $U$ whose restriction to $H_s$ is $\lambda$. Since $\dim U=r-1$ and $\dim H_s=3$, the extensions of $\lambda$ from $H_s$ to $U$ form an affine space of dimension $r-4$, hence there are $\ell^{r-4}$ of them. Distinct such extensions have distinct kernels because they agree nontrivially on $H_s$. Therefore each allowable projective line extends to exactly $\ell^{r-4}$ hyperplanes $W$. The number of admissible flags for one $s$ is
$$
F=\ell^{r-4}(r^2+r+2)\frac{\ell^{r-3}-1}{\ell-1}.
$$

Step 4: Multiply the coupled phase count by the flag count.
By Step 1, every admissible phase vector and admissible flag produces exactly one pair $(s,f)$, and $f$ recovers the flag. Therefore
$$
N_sF=\frac{r(r-1)}4\ell^{r-4}(r^2+r+2)\frac{\ell^{r-3}-1}{\ell-1}.
$$
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

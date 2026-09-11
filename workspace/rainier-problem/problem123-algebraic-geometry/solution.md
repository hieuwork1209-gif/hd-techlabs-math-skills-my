## Steps

Step 1: Compute the genus of the generic fiber

Put
$$
d=\gcd(m,n),
\qquad
\ell=\operatorname{lcm}(m,n)=\frac{mn}{d},
\qquad
h=\gcd(\ell,2).
$$
Fix $\lambda\in\mathbb C^\times\setminus\{1\}$ and let
$$
F=\mathbb C(x),
\qquad
K_\lambda=F(y,z),
$$
with
$$
y^m=x(x-1),
\qquad
z^n=x(x-\lambda).
$$
At the valuation $v_0$ of $F$ corresponding to $x=0$,
$$
v_0(x(x-1))=1.
$$
If $P$ is a place of $F(y)$ above $v_0$, then
$$
m\,v_P(y)=v_P(x(x-1))=e(P/v_0).
$$
Hence $m\mid e(P/v_0)$, while
$$
e(P/v_0)\le [F(y):F]\le m.
$$
Therefore
$$
[F(y):F]=m.
\tag{1}
$$

At $x=\lambda$, the element $x(x-1)$ is a nonzero unit. Over the completed local field, whose residue field is $\mathbb C$, that unit has an $m$-th root, so the $y$-cover is unramified there. Thus for every place $Q$ of $F(y)$ above $x=\lambda$,
$$
v_Q(x(x-\lambda))=1.
$$
If $R$ is a place of $K_\lambda$ above $Q$, then
$$
n\,v_R(z)=v_R(x(x-\lambda))=e(R/Q).
$$
Hence $n\mid e(R/Q)$, whereas
$$
e(R/Q)\le[K_\lambda:F(y)]\le n.
$$
Thus
$$
[K_\lambda:F(y)]=n,
\qquad
[K_\lambda:F]=mn.
\tag{2}
$$
The independent root-of-unity actions on $y$ and $z$ give $mn$ distinct $F$-automorphisms, so
$$
\operatorname{Gal}(K_\lambda/F)
\cong \mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z.
\tag{3}
$$

For a Kummer equation $u^r=g(x)$ in characteristic $0$, a local parameter loop at a point where $g$ has valuation $s$ acts on the chosen radical by multiplication by $\zeta_r^s$. Hence in the simultaneous cover, the inertia order is the order of the pair of valuation classes in
$$
\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z.
$$
The branch points are $0,1,\lambda,\infty$. At $0$ the valuation pair is $(1,1)$, so
$$
e_0=\ell.
\tag{4}
$$
At $1$ and $\lambda$ only one cover ramifies, giving
$$
e_1=m,
\qquad
e_\lambda=n.
\tag{5}
$$
At infinity both radicands have valuation $-2$, so
$$
e_\infty
=\operatorname{lcm}\left(\frac{m}{\gcd(m,2)},\frac{n}{\gcd(n,2)}\right).
\tag{6}
$$
The odd prime powers in this least common multiple are the same as those of $\ell$, while its $2$-adic exponent is lower by one exactly when $\ell$ is even. Thus
$$
e_\infty=\frac{\ell}{h}.
\tag{7}
$$

For a Galois cover of degree $D$, a branch point of inertia order $e$ has $D/e$ points above it, each contributing $e-1$, so its total ramification contribution is
$$
\frac De(e-1)=D-\frac De.
$$
With $D=mn$, equations (4)-(7) give
$$
\frac D{e_0}=d,
\qquad
\frac D{e_1}=n,
\qquad
\frac D{e_\lambda}=m,
\qquad
\frac D{e_\infty}=dh.
$$
Riemann-Hurwitz therefore yields
$$
2g(C_\lambda)-2
=-2mn+4mn-(d+n+m+dh),
$$
so
$$
g(C_\lambda)
=1+mn-\frac{m+n+d(1+h)}2.
\tag{8}
$$

Step 2: Normalize the collision fiber at $\lambda=1$

Now let $\lambda=1$. Then both equations have the same radicand
$$
f=x(x-1):
\qquad
y^m=f,
\qquad
z^n=f.
$$
The generic degree argument no longer applies because the two cyclic extensions intersect.

Set
$$
a=\frac{\ell}{m}=\frac nd,
\qquad
b=\frac{\ell}{n}=\frac md.
$$
Since $\gcd(a,b)=1$, choose integers $r,s$ with
$$
ar+bs=1.
\tag{9}
$$
Define in $K_1=F(y,z)$
$$
u=y^r z^s.
$$
Then
$$
u^\ell
=(y^m)^{r\ell/m}(z^n)^{s\ell/n}
=f^{ar+bs}=f.
\tag{10}
$$
Conversely,
$$
\left(\frac{y}{u^a}\right)^m=1,
\qquad
\left(\frac{z}{u^b}\right)^n=1.
$$
Any element of this function field whose positive power is $1$ is algebraic over the constant field, and the constant field is $\mathbb C$. Hence both ratios are constant roots of unity. Therefore
$$
K_1=F(u),
\qquad
u^\ell=x(x-1).
\tag{11}
$$
Since the radicand in (11) has valuation $1$ at $x=0$, the same valuation argument as in (1) shows
$$
[K_1:F]=\ell.
\tag{12}
$$
Thus the collision fiber is not a degree-$mn$ fiber product after normalization: it is a single degree-$\ell$ Kummer cover.

Step 3: Compute the genus of the collision fiber

For the Kummer cover (11), the radicand has valuations
$$
1,\quad 1,\quad -2
$$
at $0,1,\infty$. Therefore the inertia orders are
$$
\ell,\qquad \ell,\qquad \frac{\ell}{h}.
\tag{13}
$$
Applying Riemann-Hurwitz to the degree-$\ell$ map $C_1\to\mathbb P^1$ gives
$$
2g(C_1)-2
=-2\ell+(\ell-1)+(\ell-1)+(\ell-h)
=\ell-2-h.
$$
Hence
$$
g(C_1)=\frac{\ell-h}{2}.
\tag{14}
$$

Step 4: Compute the genus drop

For $\lambda\ne1$ define
$$
\Delta_{m,n}=g(C_\lambda)-g(C_1).
$$
Subtracting (14) from (8) gives
$$
\Delta_{m,n}
=1+mn-
\frac{m+n+d(1+h)+\ell-h}{2}.
$$
This is independent of the chosen generic parameter $\lambda\in\mathbb C^\times\setminus\{1\}$, because all such fibers have the same branch and inertia pattern.

## Solution Concepts

- Kummer composita and simultaneous inertia in the generic fiber.
- Degree collapse under collision of branch data via a Bezout reconstruction of the common radical.
- Riemann-Hurwitz comparison of generic and normalized collision fibers.

Final Answer: $\displaystyle 1+mn-\frac{m+n+d(1+h)+\ell-h}{2}$.

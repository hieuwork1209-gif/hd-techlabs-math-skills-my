## Steps

Step 1: Compute the genus of the generic fiber
Let
$$
d=\gcd(m,n),
\qquad
\ell=\operatorname{lcm}(m,n)=\frac{mn}{d},
\qquad
h=\gcd(\ell,2).
$$
Fix $\lambda\in\mathbb C^\times\setminus\{1\}$ and set
$$
F=\mathbb C(x),
\qquad
K_\lambda=F(y,z),
$$
where
$$
y^m=x(x-1),
\qquad
z^n=x(x-\lambda).
$$
At $x=0$, the first radicand has valuation $1$. If $P$ is a place of $F(y)$ above this valuation, then
$$
m\,v_P(y)=e(P/v_0),
$$
so $m\mid e(P/v_0)$. Since $e(P/v_0)\leq [F(y):F]\leq m$, one gets $[F(y):F]=m$.

At $x=\lambda$, the element $x(x-1)$ is a nonzero unit. Over the completed local field, whose residue field is $\mathbb C$, this unit has an $m$-th root, so the $y$-cover is unramified there. Thus for every place $Q$ of $F(y)$ above $x=\lambda$,
$$
v_Q(x(x-\lambda))=1.
$$
If $R$ lies above $Q$ in $K_\lambda$, then
$$
n\,v_R(z)=e(R/Q).
$$
Hence $n\mid e(R/Q)$, while $e(R/Q)\leq[K_\lambda:F(y)]\leq n$. Therefore
$$
[K_\lambda:F(y)]=n,
\qquad
[K_\lambda:F]=mn.
$$
The independent root-of-unity actions on $y$ and $z$ give $mn$ distinct $F$-automorphisms, so the cover $C_\lambda\to\mathbb P^1_x$ is Galois with group
$$
\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z.
$$

For a Kummer equation $u^r=g(x)$ in characteristic $0$, a local loop at a point where $g$ has valuation $s$ acts on the radical by multiplication by $\zeta_r^s$. Hence the inertia order in the simultaneous cover is the order of the corresponding valuation pair. The branch points are $0,1,\lambda,\infty$, with inertia orders
$$
e_0=\ell,
\qquad
e_1=m,
\qquad
e_\lambda=n.
$$
At infinity both radicands have valuation $-2$, so
$$
e_\infty
=\operatorname{lcm}\left(\frac{m}{\gcd(m,2)},\frac{n}{\gcd(n,2)}\right)
=\frac{\ell}{h}.
$$
Indeed, dividing each modulus by its factor $\gcd(\cdot,2)$ lowers the maximum $2$-adic exponent in the least common multiple by one exactly when $\ell$ is even and leaves all odd prime exponents unchanged.

For a Galois cover of degree $D$, a branch point of inertia order $e$ has $D/e$ points above it, so its total ramification contribution is
$$
\frac{D}{e}(e-1)=D-\frac{D}{e}.
$$
With $D=mn$,
$$
\frac{D}{e_0}=d,
\qquad
\frac{D}{e_1}=n,
\qquad
\frac{D}{e_\lambda}=m,
\qquad
\frac{D}{e_\infty}=dh.
$$
Riemann-Hurwitz gives
$$
2g(C_\lambda)-2
=-2mn+4mn-(d+n+m+dh),
$$
so
$$
g(C_\lambda)=1+mn-\frac{m+n+d(1+h)}{2}.
$$

Step 2: Normalize the collision fiber at $\lambda=1$
When $\lambda=1$, both equations have the same radicand
$$
f=x(x-1),
\qquad
y^m=f,
\qquad
z^n=f.
$$
Set
$$
a=\frac{\ell}{m}=\frac{n}{d},
\qquad
b=\frac{\ell}{n}=\frac{m}{d}.
$$
Since $\gcd(a,b)=1$, choose integers $r,s$ with $ar+bs=1$ and define
$$
u=y^r z^s.
$$
Then
$$
u^\ell
=(y^m)^{r\ell/m}(z^n)^{s\ell/n}
=f^{ar+bs}=f.
$$
Conversely,
$$
\left(\frac{y}{u^a}\right)^m=1,
\qquad
\left(\frac{z}{u^b}\right)^n=1.
$$
Any element of this function field whose positive power is $1$ is algebraic over the constant field, which is $\mathbb C$. Thus both ratios are constant roots of unity, and therefore
$$
K_1=\mathbb C(x)(u),
\qquad
u^\ell=x(x-1).
$$
The radicand has valuation $1$ at $x=0$. The same valuation argument gives $[K_1:\mathbb C(x)]=\ell$. Hence after normalization the collision fiber is a single degree-$\ell$ Kummer cover rather than a degree-$mn$ fiber product.

Step 3: Compute the genus of the collision fiber
For the degree-$\ell$ Kummer cover from Step 2, the radicand has valuations $1,1,-2$ at $0,1,\infty$. Thus the inertia orders are
$$
\ell,
\qquad
\ell,
\qquad
\frac{\ell}{h}.
$$
Riemann-Hurwitz gives
$$
2g(C_1)-2
=-2\ell+(\ell-1)+(\ell-1)+(\ell-h)
=\ell-2-h,
$$
and hence
$$
g(C_1)=\frac{\ell-h}{2}.
$$

Step 4: Compute the genus drop
From Step 1 and Step 3,
$$
\Delta_{m,n}=g(C_\lambda)-g(C_1)
=1+mn-\frac{m+n+d(1+h)+\ell-h}{2}.
$$
The result is independent of the chosen $\lambda\in\mathbb C^\times\setminus\{1\}$ because all such generic fibers have the same branch and inertia pattern.

Final Answer: $\boxed{1+mn-\frac{m+n+d(1+h)+\ell-h}{2}}$

---

## Answer

$1+mn-\frac{m+n+d(1+h)+\ell-h}{2}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- Kummer extensions and local valuations
- ramification inertia in fiber products
- normalization under branch point collision
- Riemann-Hurwitz genus formula

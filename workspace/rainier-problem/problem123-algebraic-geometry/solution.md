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
At $x=0$, the first radicand has valuation $1$, so $[F(y):F]=m$. At $x=\lambda$, the $y$-cover is unramified because $x(x-1)$ is a nonzero unit there, whereas $x(x-\lambda)$ has valuation $1$. Hence adjoining $z$ over $F(y)$ has degree $n$. Therefore
$$
[K_\lambda:F]=mn.
\tag{1}
$$
The independent root-of-unity actions on $y$ and $z$ give a Galois group
$$
G\cong \mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z.
\tag{2}
$$

The branch points are $0,1,\lambda,\infty$. At $0$ the simultaneous valuation vector is $(1,1)$, so
$$
e_0=\ell.
\tag{3}
$$
At $1$ and $\lambda$ only one cover ramifies, giving
$$
e_1=m,
\qquad
e_\lambda=n.
\tag{4}
$$
At infinity both radicands have valuation $-2$, so
$$
e_\infty
=\operatorname{lcm}\left(\frac{m}{\gcd(m,2)},\frac{n}{\gcd(n,2)}\right).
\tag{5}
$$
The odd prime powers in this least common multiple are the same as those of $\ell$, while its $2$-adic exponent is lower by one exactly when $\ell$ is even. Thus
$$
e_\infty=\frac{\ell}{h}.
\tag{6}
$$

For a Galois cover of degree $D$, a branch point of inertia order $e$ contributes
$$
D-\frac De
$$
to the ramification sum. With $D=mn$, equations (3)-(6) give
$$
\frac D{e_0}=d,
\qquad
\frac D{e_1}=n,
\qquad
\frac D{e_\lambda}=m,
\qquad
\frac D{e_\infty}=dh.
$$
Riemann-Hurwitz yields
$$
2g(C_\lambda)-2
=-2mn+4mn-(d+n+m+dh),
$$
so
$$
g(C_\lambda)
=1+mn-\frac{m+n+d(1+h)}2.
\tag{7}
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
\tag{8}
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
\tag{9}
$$
Conversely,
$$
\left(\frac{y}{u^a}\right)^m=1,
\qquad
\left(\frac{z}{u^b}\right)^n=1.
$$
Because the constant field is $\mathbb C$, both ratios are constants that are roots of unity. Hence
$$
K_1=F(u),
\qquad
u^\ell=x(x-1).
\tag{10}
$$
Thus the collision fiber is not a degree-$mn$ fiber product after normalization: it is the single Kummer cover of degree $\ell$.

Step 3: Compute the genus of the collision fiber

For the Kummer cover (10), the radicand has valuations
$$
1,\quad 1,\quad -2
$$
at $0,1,\infty$. Therefore the inertia orders are
$$
\ell,\qquad \ell,\qquad \frac{\ell}{h}.
\tag{11}
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
\tag{12}
$$

Step 4: Compute the genus drop

Define
$$
\Delta_{m,n}=g(C_\lambda)-g(C_1)
\qquad(\lambda\ne1).
$$
Subtracting (12) from (7) gives
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

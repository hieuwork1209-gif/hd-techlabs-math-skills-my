## Steps

Step 1: Lift both the forward target and the backward iterate to the multiplicative coordinate

Let
$$
f(x)=x^2-2,
$$
and put
$$
\pi(z)=z+z^{-1}\qquad(z\ne0).
$$
Then
$$
f(\pi(z))=(z+z^{-1})^2-2=z^2+z^{-2}=\pi(z^2),
$$
so by induction
$$
f^{\circ m}(\pi(z))=\pi(z^{2^m})
\tag{1}
$$
for every $m\ge0$.

Fix an odd prime $\ell$, integers $n\ge1$ and $q\ge0$, and write
$$
M=2^n,
\qquad
\zeta=e^{2\pi i/M},
\qquad
\beta=\ell^{\,2^{q-n}}>1,
$$
where the positive real value is taken. Thus
$$
\beta^M=\ell^{2^q}.
\tag{2}
$$
Since $\ell+\ell^{-1}=\pi(\ell)$, equation (1) gives
$$
f^{\circ q}(\ell+\ell^{-1})
=\ell^{2^q}+\ell^{-2^q}.
\tag{3}
$$

Now solve
$$
f^{\circ n}(x)=f^{\circ q}(\ell+\ell^{-1}).
$$
Writing $x=\pi(z)$ and using (1)--(3), this is equivalent to
$$
z^M+z^{-M}=\ell^{2^q}+\ell^{-2^q}.
$$
With $y=z^M$, multiplication by $y$ gives
$$
(y-\ell^{2^q})(y-\ell^{-2^q})=0.
$$
Hence the roots are
$$
x_k=\beta\zeta^k+\beta^{-1}\zeta^{-k},
\qquad k\in\mathbb Z/M\mathbb Z.
\tag{4}
$$
The $M$ values in (4) are distinct. Indeed, if $x_j=x_k$ with $j\ne k$, then
$$
\beta(\zeta^j-\zeta^k)
=-\beta^{-1}(\zeta^{-j}-\zeta^{-k})
=\beta^{-1}\frac{\zeta^j-\zeta^k}{\zeta^{j+k}},
$$
so $\beta^2=\zeta^{-(j+k)}$, impossible because $\beta^2>1$ while the right side has absolute value $1$.

Step 2: Identify the effective radical depth

Set
$$
d=\max(n-q,0),
\qquad
E=2^d.
\tag{5}
$$
If $q<n$, then
$$
\beta=\ell^{1/E}.
$$
If $q\ge n$, then $d=0$, $E=1$, and
$$
\beta=\ell^{2^{q-n}}\in\mathbb Q.
$$
Thus the forward depth $q$ cancels exactly $\min(n,q)$ layers of the $2$-power radical tower, while the roots in (4) still involve the full $M$th roots of unity.

Let
$$
L=\mathbb Q(\beta,\zeta).
$$
Equation (4) shows that the splitting field $K_{n,q}$ is contained in $L$.

When $d=0$, $L=\mathbb Q(\zeta)$ is already Galois over $\mathbb Q$. When $d>0$, $L$ contains all roots of $X^E-\ell$, because
$$
\eta=\zeta^{2^q}
$$
is a primitive $E$th root of unity and the roots are $\beta\eta^b$, $b\in\mathbb Z/E\mathbb Z$. Hence in all cases $L/\mathbb Q$ is Galois.

Step 3: Prove that the visible roots generate the full field $L$

Take $\sigma\in\operatorname{Gal}(L/\mathbb Q)$. Since $\zeta$ is primitive of order $M$,
$$
\sigma(\zeta)=\zeta^a
$$
for some
$$
a\in(\mathbb Z/M\mathbb Z)^\times.
$$
If $d>0$, $\beta$ is a root of $X^E-\ell$, so
$$
\sigma(\beta)=\beta\eta^b
=\beta\zeta^{2^q b}
$$
for some $b\in\mathbb Z/E\mathbb Z$. If $d=0$, take $b=0$. Therefore (4) gives
$$
\sigma(x_k)=x_{ak+2^q b}
\tag{6}
$$
when $q<n$, while for $q\ge n$ the translation term is absent and $\sigma(x_k)=x_{ak}$.

Suppose $\sigma$ fixes $K_{n,q}$ pointwise. Then it fixes every root $x_k$. By distinctness, (6) forces
$$
ak+2^q b\equiv k\pmod M
$$
for every $k$ when $q<n$. Taking $k=0$ gives
$$
2^q b\equiv0\pmod{2^n},
$$
so $b\equiv0\pmod E$; then $k=1$ gives $a\equiv1\pmod M$. If $q\ge n$, the same conclusion $a=1$ follows directly from $x_{ak}=x_k$ for all $k$.

Thus
$$
\operatorname{Gal}(L/K_{n,q})=1,
$$
and therefore
$$
K_{n,q}=L.
\tag{7}
$$

Step 4: Separate the radical and cyclotomic parts when a radical layer remains

Assume $d>0$. Put
$$
R=\mathbb Q(\beta),
\qquad
C=\mathbb Q(\zeta).
$$
The polynomial $X^E-\ell$ is Eisenstein at $\ell$, so
$$
[R:\mathbb Q]=E.
\tag{8}
$$
Also $\beta$ is an algebraic integer with
$$
|N_{R/\mathbb Q}(\beta)|=\ell.
$$
Hence the principal ideal $\mathfrak p=(\beta)$ has norm $\ell$ and is prime. Since $\ell=\beta^E$,
$$
(\ell)=\mathfrak p^E,
$$
so $\ell$ is totally ramified in $R/\mathbb Q$.

We next show explicitly that $\ell$ is unramified in $C$. For $n=1$, $C=\mathbb Q$. For $n\ge2$, put $s=2^{n-1}$. Then
$$
\Phi_{2^n}(X)=X^s+1.
$$
For a monic polynomial $g$ of degree $s$,
$$
\operatorname{disc}(g)=(-1)^{s(s-1)/2}\operatorname{Res}(g,g').
$$
Applying this to $g(X)=X^s+1$ and $g'(X)=sX^{s-1}$ gives
$$
\operatorname{disc}(X^s+1)=\pm s^s,
$$
which is a power of $2$. Since $\zeta$ is an algebraic integer and
$$
\operatorname{disc}(\mathbb Z[\zeta])
=[\mathcal O_C:\mathbb Z[\zeta]]^2\operatorname{disc}(C),
$$
the field discriminant $\operatorname{disc}(C)$ also has no odd prime divisor. Therefore the odd prime $\ell$ is unramified in $C$.

Let
$$
F=R\cap C.
$$
If $F\ne\mathbb Q$, then $\ell$ ramifies in $F$. Indeed, $R$ has a unique prime $\mathfrak p$ above $\ell$. Every prime of $F$ above $\ell$ extends to a prime of $R$ above $\ell$, so $F$ also has a unique prime $\mathfrak q=\mathfrak p\cap\mathcal O_F$ above $\ell$. The residue field $\mathcal O_F/\mathfrak q$ embeds into $\mathcal O_R/\mathfrak p\cong\mathbb F_\ell$, hence its residue degree is $1$. The fundamental identity therefore gives
$$
e(\mathfrak q/\ell)=[F:\mathbb Q]>1,
$$
so $\ell$ ramifies in $F$.

But $F\subseteq C$, and ramification indices in a tower multiply. Since the ramification index of every prime above $\ell$ in $C/\mathbb Q$ is $1$, every intermediate field of $C/\mathbb Q$ is also unramified at $\ell$. This contradiction proves
$$
R\cap C=\mathbb Q.
\tag{9}
$$

It follows from (8)--(9) that
$$
[L:C]=E,
$$
so $X^E-\ell$ remains irreducible over $C$. Consequently the subgroup fixing $C$ is
$$
\langle\tau\rangle\cong C_E,
\qquad
\tau(\beta)=\beta\eta,
\quad
\tau(\zeta)=\zeta.
\tag{10}
$$

Step 5: Determine the semidirect-product action

Let
$$
U_n=(\mathbb Z/2^n\mathbb Z)^\times.
$$
Equation (9) implies that $R$ and $C$ are linearly disjoint over $\mathbb Q$. Hence for each
$$
a\in U_n,
$$
the cyclotomic automorphism $\zeta\mapsto\zeta^a$ extends uniquely to the compositum $L=RC$ while fixing $R$ pointwise; explicitly, on products it is the well-defined map
$$
r c\longmapsto r\,\sigma_a(c)
\qquad(r\in R,\ c\in C).
$$
Denote this extension by $\sigma_a$. Since
$$
\eta=\zeta^{2^q}
$$
when $d>0$, we have
$$
\sigma_a(\eta)=\eta^a.
$$
Therefore
$$
\sigma_a\tau^b\sigma_a^{-1}=\tau^{ab},
\tag{11}
$$
where $a$ is reduced modulo $E=2^d$ on the cyclic factor.

Thus for $d>0$,
$$
\operatorname{Gal}(K_{n,q}/\mathbb Q)
\cong
C_{2^d}\rtimes_\rho U_n,
$$
where
$$
\rho(a)(b)=ab\pmod{2^d}.
$$

If $d=0$, equation (7) gives
$$
K_{n,q}=\mathbb Q(\zeta_{2^n}),
$$
so the same formula remains valid after interpreting $C_{2^0}=C_1$ as the trivial group. Since $d=\max(n-q,0)$, the uniform answer is
$$
\operatorname{Gal}(K_{n,q}/\mathbb Q)
\cong
C_{2^d}\rtimes_\rho(\mathbb Z/2^n\mathbb Z)^\times,
\qquad
d=\max(n-q,0),
$$
with $\rho(a)(b)=ab$ on $\mathbb Z/2^d\mathbb Z$.

## Solution Concepts

- Semiconjugacy of $x^2-2$ to squaring via $z+z^{-1}$, with overlap between forward and backward orbit depths.
- Ramification separation of the surviving pure radical layer from the full power-of-two cyclotomic layer.
- Faithful affine root action and the induced reduction action on the surviving translation subgroup.

Final Answer: $\displaystyle C_{2^d}\rtimes_\rho(\mathbb Z/2^n\mathbb Z)^\times,\ d=\max(n-q,0),\ \rho(a)b=ab$.

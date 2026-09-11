## Steps

Step 1: Pass to logarithmic coordinates and expose the differential hierarchy

Let
$$
g(s)=f(e^s),\qquad a(s)=A(e^s),\qquad b(s)=B(e^s),\qquad c(s)=C(e^s).
$$
Then
$$
a(s)=\frac1s\int_0^s g(u)\,du,
$$
$$
b(s)=\frac2{s^2}\int_0^s(s-u)g(u)\,du,
$$
and
$$
c(s)=\frac3{s^3}\int_0^s(s-u)^2g(u)\,du.
$$
Since $g$ is concave, it is continuous on $(0,\infty)$, and direct differentiation gives
$$
g=a+sa',\qquad sb'=2(a-b),\qquad sc'=3(b-c).
$$
Define
$$
X=2-c,
$$
$$
Y=2-3b+2c,
$$
and
$$
Z=2-3a+3b-c.
$$
The differential identities become
$$
sX'=Y-X,
$$
$$
sY'=2(Z-Y).
$$
The rank-one condition in the problem is exactly
$$
Y^2=XZ.
$$
The two normalizations become
$$
X(1)^2=\frac14,
$$
and
$$
\lim_{s\to\infty}s^2X(s)^2=1.
$$

Step 2: Use the rank-one relation to derive the hidden ratio equation

Let $I$ be the connected component of $\{s>0:X(s)\ne0\}$ containing $s=1$. On $I$, put
$$
p=\frac{Y}{X}.
$$
Then $Y^2=XZ$ gives
$$
Z=p^2X.
$$
Using $Y=pX$ together with the differential hierarchy,
$$
sY'=sp'X+p\,sX'=sp'X+p(p-1)X,
$$
while
$$
sY'=2(Z-Y)=2p(p-1)X.
$$
Hence
$$
sp'=p(p-1).
$$
If $p$ vanishes at one point of $I$, uniqueness for this scalar ODE gives $p\equiv0$ on $I$. Then $sX'=-X$, so $X=\kappa/s$. The explicit formula has no finite zero or pole, so the same continuation argument used below extends it to all $s>0$. But then
$$
X(1)^2=\kappa^2=\frac14,
$$
whereas
$$
\lim_{s\to\infty}s^2X(s)^2=\kappa^2=1,
$$
a contradiction. Thus $p$ never vanishes on $I$.

Set $q=1/p$. Then
$$
sq'=q-1,
$$
so
$$
q=1+\lambda s,
\qquad
p=\frac1{1+\lambda s}
$$
for some constant $\lambda$. Moreover,
$$
\frac{sX'}{X}=p-1=\frac{sp'}p,
$$
so $X/p$ is constant. Therefore
$$
X(s)=\frac{\kappa}{1+\lambda s}
$$
for some nonzero constant $\kappa$.

We now justify that this formula is global. If a finite endpoint of $I$ occurs while $1+\lambda s\ne0$, then $X$ has a finite nonzero limit there, and continuity of $X=2-c$ extends the nonvanishing interval, contradicting maximality. If $1+\lambda s$ vanishes at a positive point, then $X$ blows up there, impossible because $c(s)=C(e^s)$ is finite for every $s>0$. Hence $\lambda\ge0$ and $I=(0,\infty)$.

Step 3: Couple the local and asymptotic normalizations

If $\lambda=0$, then $X\equiv\kappa\ne0$, so $s^2X(s)^2\to\infty$, contradicting the asymptotic condition. Thus $\lambda>0$. From
$$
\lim_{s\to\infty}s^2X(s)^2
=
\frac{\kappa^2}{\lambda^2}
=1,
$$
we get
$$
\kappa^2=\lambda^2.
$$
On the other hand,
$$
\frac14=X(1)^2=\frac{\kappa^2}{(1+\lambda)^2}
=\frac{\lambda^2}{(1+\lambda)^2}.
$$
Since $\lambda>0$,
$$
\frac{\lambda}{1+\lambda}=\frac12,
$$
so
$$
\lambda=1,
\qquad
\kappa=\pm1.
$$
Therefore
$$
c(s)=2-\frac{\kappa}{1+s}.
$$

Step 4: Recover the source function and use concavity to select the sign

From the definition of $c$,
$$
\frac{s^3c(s)}3=\int_0^s(s-u)^2g(u)\,du.
$$
Differentiating three times gives
$$
g(s)=\frac16\frac{d^3}{ds^3}\bigl(s^3c(s)\bigr).
$$
Since
$$
\frac{d^3}{ds^3}\left(\frac{s^3}{1+s}\right)=\frac6{(1+s)^4},
$$
we obtain
$$
g(s)=2-\frac{\kappa}{(1+s)^4}.
$$
Hence
$$
g''(s)=-\frac{20\kappa}{(1+s)^6}.
$$
The hypothesis that $g$ is concave forces $\kappa=1$. Thus
$$
g(s)=2-\frac1{(1+s)^4}.
$$

Step 5: Verify the candidate and return to $x$

Let $r=(1+s)^{-1}$. For
$$
g(s)=2-r^4,
$$
direct integration gives
$$
a(s)=2-\frac{r+r^2+r^3}{3},
$$
$$
b(s)=2-\frac{2r+r^2}{3},
$$
and
$$
c(s)=2-r.
$$
Consequently
$$
X=r,\qquad Y=r^2,\qquad Z=r^3,
$$
so indeed $Y^2=XZ$. Also $X(1)^2=1/4$ and
$$
\lim_{s\to\infty}s^2X(s)^2
=
\lim_{s\to\infty}\frac{s^2}{(1+s)^2}=1.
$$
Finally $g(s)\to1$ as $s\to0^+$, so the improper integrals converge at the lower endpoint. Since $s=\log x$,
$$
f(x)=2-\frac1{(1+\log x)^4}.
$$

Final Answer: $\boxed{f(x)=2-\frac1{(1+\log x)^4}}$

---

## Answer

$f(x)=2-\frac1{(1+\log x)^4}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Function or mapping

---

## Solution Concepts

- logarithmic weighted integral means
- rank-one invariant of transformed means
- nonlinear ratio differential equation
- local and asymptotic normalization
- concavity branch selection

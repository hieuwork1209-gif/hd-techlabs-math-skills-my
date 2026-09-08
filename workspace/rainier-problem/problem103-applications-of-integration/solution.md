## Steps

Step 1: Reduce the matrix-invariant phase

Write
$$
M=\begin{pmatrix}x&z\\ z&y\end{pmatrix}.
$$
Then
$$
\det M=xy-z^2,
\qquad
\|M\|_F^2=x^2+y^2+2z^2.
$$
Put
$$
m=\frac{x+y}{2},\qquad
u=\frac{x-y}{2},
$$
and use polar coordinates
$$
\nu=d\cos\theta,\qquad z=d\sin\theta,\qquad d\ge0.
$$
Since $dx\,dy\,dz=2d\,dm\,dd\,d\theta$, integration in $\theta$ gives
$$
I_n=4\pi\int_{-\infty}^{\infty}\int_0^\infty
 d\,e^{-n\left((m^2-d^2)^2+8(m^2+d^2)^3\right)}\,dd\,dm.
$$

Step 2: Obtain an exact two-variable boundary representation

Set
$$
a=m^2,\qquad b=d^2.
$$
Using both signs of $m$ and $d\,dd=db/2$,
$$
I_n=2\pi\int_0^\infty\int_0^\infty
a^{-1/2}e^{-n\left((a-b)^2+8(a+b)^3\right)}\,da\,db.
$$
Now let
$$
s=a+b,\qquad q=a-b.
$$
Then $s\ge0$, $|q|\le s$, $da\,db=\frac12ds\,dq$, and
$$
a^{-1/2}=\sqrt2\,(s+q)^{-1/2}.
$$
Therefore the exact formula is
$$
I_n=\pi\sqrt2\int_0^\infty e^{-8ns^3}
\int_{-s}^{s}(s+q)^{-1/2}e^{-nq^2}\,dq\,ds.
$$
The determinant-zero cone is $q=0$; its apex is $s=0$.

Step 3: Compute the leading contribution along the cone

Away from the apex, the $q$-Gaussian has scale $n^{-1/2}$ while the radial variable has scale $s\asymp n^{-1/3}$. Thus the interval $[-s,s]$ may first be replaced by the whole line and $(s+q)^{-1/2}$ by $s^{-1/2}$. This gives
$$
I_n\sim\pi\sqrt2\,\sqrt{\frac\pi n}
\int_0^\infty s^{-1/2}e^{-8ns^3}\,ds.
$$
With $u=8ns^3$,
$$
\int_0^\infty s^{-1/2}e^{-8ns^3}\,ds
=\frac{\Gamma(1/6)}{3\sqrt2\,n^{1/6}}.
$$
Hence
$$
I_n\sim\frac{\pi^{3/2}\Gamma(1/6)}{3n^{2/3}}.
$$

Step 4: Resolve the nonuniform apex correction

Subtract the leading cone model before taking the next limit:
$$
\begin{aligned}
R_n={}&I_n-rac{\pi^{3/2}\Gamma(1/6)}{3n^{2/3}}\\
=\pi\sqrt2\int_0^\infty e^{-8ns^3}\Bigg[
&\int_{-s}^{s}(s+q)^{-1/2}e^{-nq^2}\,dq
-\int_{-\infty}^{\infty}s^{-1/2}e^{-nq^2}\,dq\Bigg]ds.
\end{aligned}
$$
The difference is concentrated at the apex scale
$$
s=n^{-1/2}S,\qquad q=n^{-1/2}Q.
$$
At this scale $e^{-8ns^3}\to1$, and dominated splitting between bounded $S$ and the integrable large-$S$ tail gives
$$
n^{3/4}R_n\to\pi\sqrt2\,K,
$$
where
$$
K=\int_0^\infty\left[
\int_{-S}^{S}(S+Q)^{-1/2}e^{-Q^2}\,dQ
-\sqrt\pi\,S^{-1/2}
\right]dS.
$$
To evaluate $K$, write $\sqrt\pi=\int_{-\infty}^{\infty}e^{-Q^2}\,dQ$ and integrate first in $S$. For fixed $Q$,
$$
\begin{aligned}
&\int_{|Q|}^{\infty}(S+Q)^{-1/2}\,dS
-\int_0^\infty S^{-1/2}\,dS\\
&\qquad=-2\sqrt{|Q|+Q}.
\end{aligned}
$$
Thus only $Q>0$ contributes, and
$$
K=-2\sqrt2\int_0^\infty Q^{1/2}e^{-Q^2}\,dQ
=-\sqrt2\,\Gamma\left(\frac34\right).
$$
Consequently
$$
n^{3/4}R_n\to-2\pi\Gamma\left(\frac34\right).
$$

Step 5: Recover the requested limit

We have proved
$$
I_n=rac{\pi^{3/2}\Gamma(1/6)}{3n^{2/3}}
-\frac{2\pi\Gamma(3/4)}{n^{3/4}}
+o(n^{-3/4}).
$$
Therefore
$$
\lim_{n\to\infty}n^{3/4}
\left(I_n-\frac{\pi^{3/2}\Gamma(1/6)}{3n^{2/3}}\right)
=-2\pi\Gamma\left(\frac34\right).
$$
Final Answer: $\boxed{-2\pi\Gamma\left(\frac34\right)}$

---

## Answer

$-2\pi\Gamma\left(\frac34\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- symmetric-matrix invariants
- determinant-zero cone
- degenerate Laplace asymptotics
- apex matching correction
- Gamma-function moments

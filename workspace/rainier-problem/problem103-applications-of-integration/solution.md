## Steps

Step 1: Set up the Mellin representation

Let
$$
T=\{(x,y):x\geq0,\ y\geq0,\ x+y\leq1\},
\qquad z=1-x-y,
$$
and write
$$
P=xyz,
\qquad
\Delta=(x-y)(y-z)(z-x),
$$
$$
W(x,y)=\frac{\Delta^2}{\sqrt{xyz}(x+y)(y+z)(z+x)}.
$$
For $0<c<\frac{1}{2}$, Mellin inversion gives
$$
e^{-nP}=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}
\Gamma(s)n^{-s}P^{-s}\,ds.
$$
Hence
$$
I_n=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}
\Gamma(s)n^{-s}M(s)\,ds,
$$
where
$$
M(s)=\iint_T
\frac{\Delta^2(xyz)^{-s-1/2}}{(x+y)(y+z)(z+x)}\,dx\,dy.
$$
The condition $\Re s<\frac{1}{2}$ is forced by a generic boundary edge, where one coordinate tends to $0$ and the Bures weight has an inverse-square-root singularity.

Step 2: Evaluate the Bures Mellin transform

For $a>0$, define the fixed-trace moment
$$
K(a)=\iint_T
\frac{\Delta^2(xyz)^{a-1}}{(x+y)(y+z)(z+x)}\,dx\,dy.
$$
Also define the trace-unfixed integral
$$
J(a)=\iiint_{(0,\infty)^3}
\frac{\Delta^2(xyz)^{a-1}e^{-(x+y+z)}}{(x+y)(y+z)(z+x)}\,dx\,dy\,dz.
$$
Writing $(x,y,z)=r(\lambda_1,\lambda_2,\lambda_3)$ with $\lambda_1+\lambda_2+\lambda_3=1$ gives
$$
J(a)=\Gamma(3a+3)K(a).
$$

Now use
$$
\Delta=\det
\begin{pmatrix}
1&x&x^2\\
1&y&y^2\\
1&z&z^2
\end{pmatrix}
$$
and the three-variable Schur identity
$$
\frac{\Delta}{(x+y)(y+z)(z+x)}
=\frac{y-x}{x+y}-\frac{z-x}{x+z}+\frac{z-y}{y+z}.
$$
For $1\leq i,j\leq3$, put
$$
\nu_i=\int_0^\infty x^{a+i-2}e^{-x}\,dx
=\Gamma(a+i-1),
$$
and
$$
\mu_{ij}=\int_0^\infty\int_0^\infty
x^{a+i-2}y^{a+j-2}e^{-x-y}\frac{y-x}{x+y}\,dx\,dy.
$$
With $r=x+y$ and $t=x/r$, the last integral becomes a beta integral, giving
$$
\mu_{ij}
=\frac{j-i}{2a+i+j-2}
\Gamma(a+i-1)\Gamma(a+j-1).
$$
In particular, $\mu_{ji}=-\mu_{ij}$.

To make the determinant reduction explicit, set
$$
q_{12}=\frac{y-x}{x+y},\qquad
q_{13}=\frac{z-x}{x+z},\qquad
q_{23}=\frac{z-y}{y+z},
$$
and
$$
d\omega_a=(xyz)^{a-1}e^{-(x+y+z)}\,dx\,dy\,dz.
$$
Then
$$
J(a)=\iiint \Delta\,(q_{12}-q_{13}+q_{23})\,d\omega_a.
$$
Expanding
$$
\Delta=yz^2-y^2z-xz^2+xy^2+x^2z-x^2y
$$
against the first Schur term gives
$$
\begin{aligned}
\iiint \Delta q_{12}\,d\omega_a
&=\mu_{12}\nu_3-\mu_{13}\nu_2-\mu_{21}\nu_3
+\mu_{23}\nu_1+\mu_{31}\nu_2-\mu_{32}\nu_1\\
&=2\left(\mu_{12}\nu_3-\mu_{13}\nu_2+\mu_{23}\nu_1\right).
\end{aligned}
$$
Likewise, expanding against $q_{13}$ gives
$$
\begin{aligned}
\iiint \Delta q_{13}\,d\omega_a
&=\mu_{13}\nu_2-\mu_{12}\nu_3-\mu_{23}\nu_1
+\mu_{21}\nu_3+\mu_{32}\nu_1-\mu_{31}\nu_2\\
&=-2\left(\mu_{12}\nu_3-\mu_{13}\nu_2+\mu_{23}\nu_1\right),
\end{aligned}
$$
and expanding against $q_{23}$ gives
$$
\begin{aligned}
\iiint \Delta q_{23}\,d\omega_a
&=\mu_{23}\nu_1-\mu_{32}\nu_1-\mu_{13}\nu_2
+\mu_{31}\nu_2+\mu_{12}\nu_3-\mu_{21}\nu_3\\
&=2\left(\mu_{12}\nu_3-\mu_{13}\nu_2+\mu_{23}\nu_1\right).
\end{aligned}
$$
These signs also follow directly from symmetry: interchanging $y$ and $z$ changes $\Delta$ to $-\Delta$ and $q_{12}$ to $q_{13}$, while the cyclic permutation $(x,y,z)\mapsto(y,z,x)$ preserves $\Delta$ and sends $q_{12}$ to $q_{23}$. Therefore the three terms in $q_{12}-q_{13}+q_{23}$ contribute the same amount, and
$$
J(a)=6\left(\mu_{12}\nu_3-\mu_{13}\nu_2+\mu_{23}\nu_1\right).
$$
For these three terms, the formulas above give
$$
\mu_{12}\nu_3
=\frac{\Gamma(a)\Gamma(a+1)\Gamma(a+2)}{2a+1},
$$
$$
\mu_{13}\nu_2
=\frac{2\Gamma(a)\Gamma(a+2)\Gamma(a+1)}{2a+2}
=\frac{\Gamma(a)\Gamma(a+1)\Gamma(a+2)}{a+1},
$$
and
$$
\mu_{23}\nu_1
=\frac{\Gamma(a+1)\Gamma(a+2)\Gamma(a)}{2a+3}.
$$
Thus
$$
\begin{aligned}
\mu_{12}\nu_3-\mu_{13}\nu_2+\mu_{23}\nu_1
&=\Gamma(a)\Gamma(a+1)\Gamma(a+2)
\left(\frac{1}{2a+1}-\frac{1}{a+1}+\frac{1}{2a+3}\right)\\
&=\Gamma(a)\Gamma(a+1)\Gamma(a+2)
\frac{4(a+1)^2-(2a+1)(2a+3)}{(a+1)(2a+1)(2a+3)}\\
&=\frac{\Gamma(a)\Gamma(a+1)\Gamma(a+2)}{(a+1)(2a+1)(2a+3)}\\
&=\frac{\Gamma(a)\Gamma(a+1)^2}{(2a+1)(2a+3)},
\end{aligned}
$$
where the last line uses $\Gamma(a+2)=(a+1)\Gamma(a+1)$. Hence
$$
J(a)=
\frac{6\Gamma(a)\Gamma(a+1)^2}{(2a+1)(2a+3)}.
$$
Therefore
$$
K(a)=
\frac{6\Gamma(a)\Gamma(a+1)^2}
{(2a+1)(2a+3)\Gamma(3a+3)}.
$$
Taking $a=\frac{1}{2}-s$ yields
$$
M(s)=
\frac{3\Gamma\left(\frac{1}{2}-s\right)
\Gamma\left(\frac{3}{2}-s\right)^2}
{2(1-s)(2-s)\Gamma\left(\frac{9}{2}-3s\right)}.
$$

Step 3: Extract the first two boundary terms

Put
$$
F(s)=\Gamma(s)M(s)
=\frac{3\Gamma(s)\Gamma\left(\frac{1}{2}-s\right)
\Gamma\left(\frac{3}{2}-s\right)^2}
{2(1-s)(2-s)\Gamma\left(\frac{9}{2}-3s\right)}.
$$
We first fix the contour-shift sign convention. Consider a positively oriented rectangle with left side $\Re s=c$ and right side $\Re s=R>c$. When both vertical-line integrals are written upward, the right side contributes the integral on $\Re s=R$, while the left side is traversed downward and therefore contributes minus the integral on $\Re s=c$. After the horizontal sides vanish, the residue theorem gives
$$
\int_{R-i\infty}^{R+i\infty}F(s)n^{-s}\,ds
-
\int_{c-i\infty}^{c+i\infty}F(s)n^{-s}\,ds
=2\pi i S,
$$
where $S$ is the sum of the residues at the poles crossed between the two lines. Thus
$$
\int_{c-i\infty}^{c+i\infty}F(s)n^{-s}\,ds
=
\int_{R-i\infty}^{R+i\infty}F(s)n^{-s}\,ds
-2\pi i S.
$$
Hence every crossed pole enters the original Mellin integral with minus its residue.

At $s=\frac{1}{2}$ the only singular factor is $\Gamma\left(\frac{1}{2}-s\right)$, and
$$
\lim_{s\to1/2}\left(s-\frac12\right)
\Gamma\left(\frac12-s\right)=-1.
$$
The remaining factors satisfy
$$
\Gamma\left(\frac12\right)=\sqrt\pi,
\qquad
\Gamma(1)=1,
\qquad
\Gamma(3)=2,
$$
so
$$
\begin{aligned}
\operatorname*{Res}_{s=1/2}F(s)
&=\frac{3\Gamma\left(\frac12\right)\Gamma(1)^2}
{2\left(1-\frac12\right)\left(2-\frac12\right)\Gamma(3)}(-1)\\
&=-\sqrt\pi.
\end{aligned}
$$
Therefore this pole contributes
$$
\frac{\sqrt{\pi}}{n^{1/2}}.
$$

At $s=1$ the singular factor is $(1-s)^{-1}$, with
$$
\lim_{s\to1}\frac{s-1}{1-s}=-1.
$$
Using
$$
\Gamma(1)=1,
\qquad
\Gamma\left(-\frac12\right)=-2\sqrt\pi,
\qquad
\Gamma\left(\frac12\right)=\sqrt\pi,
\qquad
\Gamma\left(\frac32\right)=\frac{\sqrt\pi}{2},
$$
we get
$$
\begin{aligned}
\operatorname*{Res}_{s=1}F(s)
&=\frac{3\Gamma(1)\Gamma\left(-\frac12\right)
\Gamma\left(\frac12\right)^2}
{2(2-1)\Gamma\left(\frac32\right)}(-1)\\
&=6\pi.
\end{aligned}
$$
Hence this pole contributes
$$
-\frac{6\pi}{n}.
$$
Thus the two simple poles contribute
$$
\frac{\sqrt{\pi}}{n^{1/2}}-\frac{6\pi}{n},
$$
and the next singularity to be crossed is at $s=\frac{3}{2}$.

Step 4: Resolve the double pole at $s=\frac{3}{2}$

Write
$$
s=\frac{3}{2}+\varepsilon.
$$
Substitution into the formula for $F$ gives
$$
F\left(\frac32+\varepsilon\right)
=\frac{3\Gamma\left(\frac32+\varepsilon\right)
\Gamma(-1-\varepsilon)\Gamma(-\varepsilon)^2}
{2\left(-\frac12-\varepsilon\right)
\left(\frac12-\varepsilon\right)\Gamma(-3\varepsilon)}.
$$
Applying $\Gamma(z+1)=z\Gamma(z)$ successively,
$$
\Gamma(-\varepsilon)
=-\frac{\Gamma(1-\varepsilon)}{\varepsilon},
$$
$$
\Gamma(-1-\varepsilon)
=\frac{\Gamma(-\varepsilon)}{-1-\varepsilon}
=\frac{\Gamma(1-\varepsilon)}{\varepsilon(1+\varepsilon)},
$$
and
$$
\Gamma(-3\varepsilon)
=-\frac{\Gamma(1-3\varepsilon)}{3\varepsilon}.
$$
Consequently
$$
\Gamma(-1-\varepsilon)\Gamma(-\varepsilon)^2
=\frac{\Gamma(1-\varepsilon)^3}
{\varepsilon^3(1+\varepsilon)},
$$
while
$$
\begin{aligned}
2\left(-\frac12-\varepsilon\right)
\left(\frac12-\varepsilon\right)\Gamma(-3\varepsilon)
&=-\frac{1-4\varepsilon^2}{2}
\left(-\frac{\Gamma(1-3\varepsilon)}{3\varepsilon}\right)\\
&=\frac{(1-4\varepsilon^2)\Gamma(1-3\varepsilon)}{6\varepsilon}.
\end{aligned}
$$
Therefore the exact singular factor is
$$
F\left(\frac{3}{2}+\varepsilon\right)
=
\frac{18\Gamma\left(\frac{3}{2}+\varepsilon\right)
\Gamma(1-\varepsilon)^3}
{\varepsilon^2(1+\varepsilon)(1-4\varepsilon^2)
\Gamma(1-3\varepsilon)}.
$$
We use
$$
\Gamma(1-\varepsilon)=1+\gamma\varepsilon+O(\varepsilon^2),
$$
$$
\Gamma(1-3\varepsilon)=1+3\gamma\varepsilon+O(\varepsilon^2).
$$
The duplication formula together with
$\Gamma(1+\varepsilon)=1-\gamma\varepsilon+O(\varepsilon^2)$ gives
$$
\Gamma\left(\frac{3}{2}+\varepsilon\right)
=\frac{\sqrt{\pi}}{2}
\left(1+(2-\gamma-2\log2)\varepsilon+O(\varepsilon^2)\right).
$$
Hence
$$
F\left(\frac{3}{2}+\varepsilon\right)
=
\frac{9\sqrt{\pi}}{\varepsilon^2}
+
\frac{9\sqrt{\pi}(1-\gamma-2\log2)}{\varepsilon}
+O(1).
$$
Also
$$
n^{-3/2-\varepsilon}
=n^{-3/2}
\left(1-\varepsilon\log n+O(\varepsilon^2)\right).
$$
Therefore the residue of $F(s)n^{-s}$ at $s=\frac{3}{2}$ is
$$
\frac{9\sqrt{\pi}(1-\gamma-2\log2)-9\sqrt{\pi}\log n}{n^{3/2}}.
$$
After the contour-shift sign is included, the double pole contributes
$$
\frac{9\sqrt{\pi}(\log n+\gamma+2\log2-1)}{n^{3/2}}.
$$

Step 5: Justify the contour shift and recover the requested limit

Choose
$$
\sigma=\frac{3}{2}+\delta,
\qquad 0<\delta<\frac{1}{2}.
$$
There are no poles of $F$ in $\frac{3}{2}<\Re s\leq\sigma$. For fixed $u$ in the compact strip $c\leq u\leq\sigma$, Stirling's formula on vertical strips gives, uniformly as $|t|\to\infty$,
$$
|\Gamma(\alpha+i\beta t)|
\leq C(1+|t|)^{\alpha-1/2}e^{-\pi|\beta t|/2}
$$
when $\alpha$ ranges over a fixed compact interval and $\beta\neq0$ is fixed. Applying this to
$$
F(s)=
\frac{3\Gamma(s)\Gamma\left(\frac{1}{2}-s\right)
\Gamma\left(\frac{3}{2}-s\right)^2}
{2(1-s)(2-s)\Gamma\left(\frac{9}{2}-3s\right)}
$$
shows that on the new vertical line $s=\sigma+it$,
$$
|F(\sigma+it)|
\leq C_\sigma(1+|t|)^{\sigma-9/2}e^{-\pi|t|/2}.
$$
Indeed, the Gamma factors in the numerator contribute the polynomial power
$$
\left(\sigma-\frac12\right)-\sigma+2(1-\sigma)
=\frac32-2\sigma,
$$
the reciprocal Gamma factor contributes $-(4-3\sigma)$, and the two linear factors contribute $-2$, for the total power $\sigma-\frac92$; the net exponential factor is $e^{-\pi|t|/2}$. Hence the shifted vertical integral converges absolutely and
$$
R_n:=\frac{1}{2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}
F(s)n^{-s}\,ds
=O(n^{-\sigma})
=O(n^{-3/2-\delta})
=o(n^{-3/2}).
$$

It remains to justify that the horizontal sides disappear. Shift first on the positively oriented rectangle with vertical sides $\Re s=c$ and $\Re s=\sigma$ and horizontal sides at $\Im s=\pm T$. Uniform Stirling bounds on the whole compact strip give, for some constants $C,B$ independent of $u\in[c,\sigma]$,
$$
|F(u\pm iT)|\leq C(1+T)^B e^{-\pi T/2}.
$$
Since $n^{-u}\leq n^{-c}\leq1$ for $n\geq1$ and each horizontal side has bounded length $\sigma-c$, both horizontal integrals are
$$
O\left((1+T)^B e^{-\pi T/2}\right)\to0
\qquad(T\to\infty).
$$
Let $S_n$ denote the sum of the residues of $F(s)n^{-s}$ at the crossed poles $s=\frac12,1,\frac32$. On a positively oriented rectangle the right vertical side is traversed upward and the left vertical side downward. Therefore, after letting $T\to\infty$,
$$
\int_{\sigma-i\infty}^{\sigma+i\infty}F(s)n^{-s}\,ds
-
\int_{c-i\infty}^{c+i\infty}F(s)n^{-s}\,ds
=2\pi i S_n,
$$
or equivalently
$$
\int_{c-i\infty}^{c+i\infty}F(s)n^{-s}\,ds
=
\int_{\sigma-i\infty}^{\sigma+i\infty}F(s)n^{-s}\,ds
-2\pi i S_n.
$$
This confirms the sign used in Steps 3 and 4 and proves the claimed remainder estimate.

Combining Steps 3 and 4 with $R_n=o(n^{-3/2})$,
$$
I_n=
\frac{\sqrt{\pi}}{n^{1/2}}
-\frac{6\pi}{n}
+\frac{9\sqrt{\pi}(\log n+\gamma+2\log2-1)}{n^{3/2}}
+o(n^{-3/2}).
$$
Hence
$$
\lim_{n\to\infty}
\left(
n^{3/2}I_n-\sqrt{\pi}\,n+6\pi\sqrt{n}-9\sqrt{\pi}\log n
\right)
=
9\sqrt{\pi}(\gamma+2\log2-1).
$$
Final Answer: $\boxed{9\sqrt{\pi}(\gamma+2\log2-1)}$

---

## Answer

$9\sqrt{\pi}(\gamma+2\log2-1)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Mellin inversion
- Bures eigenvalue weight
- Schur-Pfaffian reduction
- fixed-trace scaling
- double-pole asymptotics

## Steps

Step 1: Set up Mellin inversion with absolute convergence

Put
$$
P=xyz,\qquad
W(x,y)=\frac{\Delta^2}{\sqrt{xyz}(x+y)(y+z)(z+x)}.
$$
For $0<c<\frac{1}{2}$, Mellin inversion gives
$$
e^{-nP}=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\Gamma(s)n^{-s}P^{-s}\,ds.
$$
To justify Fubini, set
$$
M(c)=\iint_T W(x,y)P^{-c}\,dx\,dy.
$$
Near a generic edge, say $x\to0$ with $y,z$ bounded away from $0$, the integrand is $O(x^{-c-\frac{1}{2}})$. Near the vertex $x,y\to0$, write $r=x+y$ and $t=x/r$; since $dx\,dy=r\,dr\,dt$, $\Delta^2=O(r^2)$ and $(x+y)(y+z)(z+x)\asymp r$, the integrand times $dx\,dy$ is
$$
O\left(r^{1-2c}[t(1-t)]^{-c-\frac{1}{2}}\,dr\,dt\right).
$$
By symmetry these estimates cover the whole boundary, so $M(c)<\infty$ for $0<c<\frac{1}{2}$. Also Stirling's formula gives
$$
|\Gamma(c+it)|=O\left((1+|t|)^{c-\frac{1}{2}}e^{-\pi|t|/2}\right),
\qquad
\int_{\mathbb R}|\Gamma(c+it)|\,dt<\infty.
$$
The absolute integral is therefore
$$
\frac{n^{-c}}{2\pi}M(c)\int_{\mathbb R}|\Gamma(c+it)|\,dt<\infty,
$$
so Fubini applies and
$$
I_n=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\Gamma(s)n^{-s}M(s)\,ds,
$$
where
$$
M(s)=\iint_T\frac{\Delta^2(xyz)^{-s-\frac{1}{2}}}{(x+y)(y+z)(z+x)}\,dx\,dy.
$$

Step 2: Evaluate the Mellin transform

For $a>0$, let
$$
K(a)=\iint_T\frac{\Delta^2(xyz)^{a-1}}{(x+y)(y+z)(z+x)}\,dx\,dy
$$
and
$$
J(a)=\iiint_{(0,\infty)^3}\frac{\Delta^2(xyz)^{a-1}e^{-(x+y+z)}}{(x+y)(y+z)(z+x)}\,dx\,dy\,dz.
$$
With $(x,y,z)=r(\lambda_1,\lambda_2,\lambda_3)$, $\lambda_1+\lambda_2+\lambda_3=1$, the radial power is $r^{3a+2}$, hence
$$
J(a)=\left(\int_0^\infty e^{-r}r^{3a+2}\,dr\right)K(a)=\Gamma(3a+3)K(a).
$$
Use the exact identity
$$
\frac{\Delta}{(x+y)(y+z)(z+x)}
=\frac{y-x}{x+y}-\frac{z-x}{x+z}+\frac{z-y}{y+z}.
$$
Define
$$
\nu_i=\Gamma(a+i-1),
$$
$$
\mu_{ij}=\int_0^\infty\!\int_0^\infty x^{a+i-2}y^{a+j-2}e^{-x-y}\frac{y-x}{x+y}\,dx\,dy.
$$
With $r=x+y$, $t=x/r$,
$$
\mu_{ij}=\Gamma(2a+i+j-2)\int_0^1 t^{a+i-2}(1-t)^{a+j-2}(1-2t)\,dt
=\frac{j-i}{2a+i+j-2}\Gamma(a+i-1)\Gamma(a+j-1),
$$
so $\mu_{ji}=-\mu_{ij}$. Put
$$
q_{12}=\frac{y-x}{x+y},\qquad q_{13}=\frac{z-x}{x+z},\qquad q_{23}=\frac{z-y}{y+z}.
$$
Expanding
$$
\Delta=yz^2-y^2z-xz^2+xy^2+x^2z-x^2y
$$
gives
$$
\iiint \Delta q_{12}(xyz)^{a-1}e^{-(x+y+z)}\,dx\,dy\,dz
=2(\mu_{12}\nu_3-\mu_{13}\nu_2+\mu_{23}\nu_1).
$$
Interchanging $y,z$ changes $\Delta$ to $-\Delta$ and $q_{12}$ to $q_{13}$, while the cyclic permutation sends $q_{12}$ to $q_{23}$ and preserves $\Delta$. Therefore the three terms in the displayed identity contribute with signs $+,-,+$, and
$$
J(a)=6(\mu_{12}\nu_3-\mu_{13}\nu_2+\mu_{23}\nu_1).
$$
Substitution gives
$$
\begin{aligned}
\mu_{12}\nu_3-\mu_{13}\nu_2+\mu_{23}\nu_1
&=\Gamma(a)\Gamma(a+1)\Gamma(a+2)
\left(\frac{1}{2a+1}-\frac{1}{a+1}+\frac{1}{2a+3}\right)\\
&=\frac{\Gamma(a)\Gamma(a+1)^2}{(2a+1)(2a+3)}.
\end{aligned}
$$
Hence
$$
K(a)=\frac{6\Gamma(a)\Gamma(a+1)^2}{(2a+1)(2a+3)\Gamma(3a+3)}.
$$
Taking $a=\frac{1}{2}-s$ yields
$$
M(s)=\frac{3\Gamma\left(\frac{1}{2}-s\right)\Gamma\left(\frac{3}{2}-s\right)^2}
{2(1-s)(2-s)\Gamma\left(\frac{9}{2}-3s\right)}.
$$

Step 3: Extract the simple poles

Set
$$
F(s)=\Gamma(s)M(s).
$$
On a positively oriented rectangle, the right vertical side is traversed upward and the left vertical side downward. Thus a valid rightward contour shift has the form "original line = shifted line minus $2\pi i$ times the crossed residues," so each crossed pole contributes minus its residue. At $s=\frac{1}{2}$,
$$
\operatorname{Res}_{s=\frac{1}{2}}F(s)
=-\frac{3\Gamma(\frac{1}{2})\Gamma(1)^2}{2(\frac{1}{2})(\frac{3}{2})\Gamma(3)}
=-\sqrt{\pi},
$$
while at $s=1$,
$$
\operatorname{Res}_{s=1}F(s)
=-\frac{3\Gamma(1)\Gamma(-\frac{1}{2})\Gamma(\frac{1}{2})^2}{2\Gamma(\frac{3}{2})}
=6\pi.
$$
Therefore these poles contribute
$$
\frac{\sqrt{\pi}}{n^{\frac{1}{2}}}-\frac{6\pi}{n}.
$$

Step 4: Resolve the double pole at $s=\frac{3}{2}$

Write $s=\frac{3}{2}+\varepsilon$. Then
$$
F\left(\frac{3}{2}+\varepsilon\right)
=\frac{3\Gamma\left(\frac{3}{2}+\varepsilon\right)\Gamma(-1-\varepsilon)\Gamma(-\varepsilon)^2}
{2\left(-\frac{1}{2}-\varepsilon\right)\left(\frac{1}{2}-\varepsilon\right)\Gamma(-3\varepsilon)}.
$$
Using $\Gamma(z+1)=z\Gamma(z)$,
$$
\Gamma(-\varepsilon)=-\frac{\Gamma(1-\varepsilon)}{\varepsilon},\quad
\Gamma(-1-\varepsilon)=\frac{\Gamma(1-\varepsilon)}{\varepsilon(1+\varepsilon)},\quad
\Gamma(-3\varepsilon)=-\frac{\Gamma(1-3\varepsilon)}{3\varepsilon},
$$
so
$$
F\left(\frac{3}{2}+\varepsilon\right)
=\frac{18\Gamma\left(\frac{3}{2}+\varepsilon\right)\Gamma(1-\varepsilon)^3}
{\varepsilon^2(1+\varepsilon)(1-4\varepsilon^2)\Gamma(1-3\varepsilon)}.
$$
Now $\Gamma(1+u)=1-\gamma u+O(u^2)$. For $\Gamma(\frac{3}{2}+\varepsilon)$ use the duplication formula in the exact form
$$
\Gamma(z)\Gamma\left(z+\frac{1}{2}\right)=2^{1-2z}\sqrt{\pi}\,\Gamma(2z).
$$
With $z=1+\varepsilon$,
$$
\Gamma\left(\frac{3}{2}+\varepsilon\right)
=\frac{2^{-1-2\varepsilon}\sqrt{\pi}\,\Gamma(2+2\varepsilon)}{\Gamma(1+\varepsilon)}.
$$
Since
$$
2^{-1-2\varepsilon}=\frac{1}{2}(1-2\log 2\,\varepsilon+O(\varepsilon^2)),
$$
$$
\Gamma(2+2\varepsilon)=1+2(1-\gamma)\varepsilon+O(\varepsilon^2),
\qquad
\Gamma(1+\varepsilon)^{-1}=1+\gamma\varepsilon+O(\varepsilon^2),
$$
we obtain
$$
\Gamma\left(\frac{3}{2}+\varepsilon\right)
=\frac{\sqrt{\pi}}{2}\left(1+(2-\gamma-2\log 2)\varepsilon+O(\varepsilon^2)\right).
$$
Also
$$
\frac{\Gamma(1-\varepsilon)^3}{\Gamma(1-3\varepsilon)}=1+O(\varepsilon^2),\quad
\frac{1}{1+\varepsilon}=1-\varepsilon+O(\varepsilon^2),\quad
\frac{1}{1-4\varepsilon^2}=1+O(\varepsilon^2).
$$
Therefore
$$
F\left(\frac{3}{2}+\varepsilon\right)
=\frac{9\sqrt{\pi}}{\varepsilon^2}
+\frac{9\sqrt{\pi}(1-\gamma-2\log 2)}{\varepsilon}+O(1).
$$
Since
$$
n^{-\frac{3}{2}-\varepsilon}=n^{-\frac{3}{2}}(1-\varepsilon\log n+O(\varepsilon^2)),
$$
the residue of $F(s)n^{-s}$ at $s=\frac{3}{2}$ is
$$
n^{-\frac{3}{2}}\left(9\sqrt{\pi}(1-\gamma-2\log 2)-9\sqrt{\pi}\log n\right).
$$
By the contour sign in Step 3, this contributes
$$
\frac{9\sqrt{\pi}(\log n+\gamma+2\log 2-1)}{n^{\frac{3}{2}}}.
$$

Step 5: Bound the shifted contour and take the limit

Choose $\sigma=\frac{3}{2}+\delta$ with $0<\delta<\frac{1}{2}$; no further pole lies in $\frac{3}{2}<\Re s\leq\sigma$. Stirling's formula on vertical strips gives
$$
|F(\sigma+it)|\leq C_\sigma(1+|t|)^{\sigma-\frac{9}{2}}e^{-\pi|t|/2};
$$
the polynomial exponent is
$$
\left(\sigma-\frac{1}{2}\right)-\sigma+2(1-\sigma)-(4-3\sigma)-2
=\sigma-\frac{9}{2}.
$$
Thus the shifted vertical integral is $O(n^{-\sigma})=o(n^{-\frac{3}{2}})$. The same uniform Stirling bound on the compact strip $c\leq\Re s\leq\sigma$ makes each horizontal side $O((1+T)^B e^{-\pi T/2})$, so the contour shift is valid.

Combining Steps 3 and 4,
$$
I_n=\frac{\sqrt{\pi}}{n^{\frac{1}{2}}}-\frac{6\pi}{n}
+\frac{9\sqrt{\pi}(\log n+\gamma+2\log 2-1)}{n^{\frac{3}{2}}}
+o(n^{-\frac{3}{2}}).
$$
Therefore
$$
\lim_{n\to\infty}\left(n^{\frac{3}{2}}I_n-\sqrt{\pi}\,n+6\pi\sqrt{n}-9\sqrt{\pi}\log n\right)
=9\sqrt{\pi}(\gamma+2\log 2-1).
$$
Final Answer: $\boxed{9\sqrt{\pi}(\gamma+2\log 2-1)}$

---

## Answer

$9\sqrt{\pi}(\gamma+2\log 2-1)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- Mellin inversion
- beta integrals
- symmetry reduction
- gamma duplication formula
- residue asymptotics

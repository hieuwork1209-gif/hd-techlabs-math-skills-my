## Steps

Step 1: Record the one-variable quadratic sums

Write
$$
e_j(u)=\exp(2\pi i u/2^j),\qquad
G_j(b)=\sum_{x\bmod2^j}e_j(x^2+bx),
$$
and put $g_j=G_j(0)$. Pairing $x$ with $x+2^{j-1}$ shows that $G_j(b)=0$ when $b$ is odd. If $b=2c$, completing the square gives
$$
G_j(2c)=e_j(-c^2)g_j.
$$
For $j\ge2$, splitting the ordinary Gauss sum into even and odd residues gives $g_{j+2}=2g_j$, with
$$
g_2=2(1+i),\qquad g_3=4e^{\pi i/4}.
$$
Hence
$$
g_j=
\begin{cases}
2^{j/2}(1+i),&j\text{ even},\\[1mm]
2^{(j+1)/2}e^{\pi i/4},&j\text{ odd}.
\end{cases}
$$
In particular, for every $m\ge4$,
$$
g_m^2g_{m-1}=C_m e^{3\pi i/4}
$$
with $C_m>0$.

Step 2: Collapse the $A_3$ Fourier coefficient

Let
$$
Q(x,y,z)=x^2+y^2+z^2-xy-yz.
$$
For fixed $y$, the sums over $x$ and $z$ are
$$
G_m(-(y+r)),\qquad G_m(-(y+t)).
$$
Thus a nonzero coefficient requires $r\equiv t\pmod2$, and then only the $y$ having this common parity contribute. Write
$$
r=p+2a,\qquad t=p+2b,\qquad y=p+2u,
$$
where $p\in\{0,1\}$ and $a,b,u$ are taken modulo $2^{m-1}$. Step 1 gives
$$
A_m(r,s,t)=g_m^2\sum_{u\bmod2^{m-1}}
 e_m\!\left(2u^2-2(s+a+b)u+C\right),
$$
where
$$
C=-p-sp-2p(a+b)-a^2-b^2.
$$
The remaining sum is zero unless $s+a+b$ is even. Put
$$
s+a+b=2d.
$$
Then
$$
A_m(r,s,t)=g_m^2g_{m-1}e_m(\Phi),
$$
with
$$
\Phi=-a^2-b^2-2d^2-p(1+a+b+2d).
$$
If
$$
w=p+2d,
$$
then the identity
$$
4\Phi=-(r^2+t^2+2w^2)
$$
will control the phase.

Step 3: Reduce positive and negative values to a ternary congruence

By Step 1, every nonzero coefficient has global Gauss phase $3\pi/4$. Therefore
$$
A_m(r,s,t)>0\iff \Phi\equiv5\cdot2^{m-3}\pmod{2^m},
$$
and
$$
A_m(r,s,t)<0\iff \Phi\equiv2^{m-3}\pmod{2^m}.
$$
If $p=1$, then $r,t,w$ are odd, so
$$
\frac{r^2+t^2+2w^2}{4}\equiv1\pmod2.
$$
Hence $\Phi$ is odd. Since $m\ge4$, neither real-sign target above is odd, so no real nonzero coefficient comes from $p=1$.

For $p=0$, write
$$
r=2R,\qquad t=2T,\qquad w=2W.
$$
Then
$$
\Phi=-(R^2+T^2+2W^2),
$$
and the support with $p=0$ is parametrized by $R,T,W\bmod2^{m-1}$. Thus positive values correspond to
$$
R^2+T^2+2W^2\equiv3\cdot2^{m-3}\pmod{2^m},
$$
and negative values to
$$
R^2+T^2+2W^2\equiv7\cdot2^{m-3}\pmod{2^m}.
$$
For $c\in\{3,7\}$, let $C_m(c)$ be the number of triples $(X,Y,Z)\bmod2^m$ satisfying
$$
X^2+Y^2+2Z^2\equiv c2^{m-3}\pmod{2^m}.
$$
Lifting each of $R,T,W$ from modulus $2^{m-1}$ to $2^m$ does not change the quadratic form modulo $2^m$, and gives $2^3$ lifts. Hence
$$
P_m=\frac{C_m(3)}8,\qquad N_m=\frac{C_m(7)}8.
$$

Step 4: Count the ternary representations

For $m\ge6$, the right-hand side is divisible by $8$. If
$$
X^2+Y^2+2Z^2\equiv0\pmod8,
$$
then $X,Y,Z$ must all be even. Indeed, if $X,Y$ are odd then $X^2+Y^2\equiv2\pmod8$, and adding $2Z^2$ gives $2$ or $4$ modulo $8$; if $X,Y$ are even and $Z$ is odd, the value is $2$ or $6$ modulo $8$. Thus write $X=2X_1$, $Y=2Y_1$, $Z=2Z_1$. Dividing by $4$ lowers the modulus by two powers, and each reduced variable has one unused high bit. Therefore
$$
C_m(c)=8C_{m-2}(c)\qquad(m\ge6).
$$

It remains to compute two small bases. Modulo $16$, the square residues $0,1,4,9$ each occur four times, while $2Z^2$ has multiplicities
$$
0:4,\qquad 2:8,\qquad 8:4.
$$
The resulting convolution gives
$$
C_4(3)=256,\qquad C_4(7)=0.
$$
Modulo $32$, the square-residue multiplicities are
$$
0:4,\ 1:4,\ 4:8,\ 9:4,\ 16:4,\ 17:4,\ 25:4,
$$
and $2Z^2$ takes each of $0,2,8,18$ eight times. The same convolution gives
$$
C_5(3)=C_5(7)=1536.
$$
Iterating the recurrence therefore yields
$$
C_m(3)=
\begin{cases}
2^{3m/2+2},&m\text{ even},\\
3\cdot2^{3(m-1)/2+3},&m\text{ odd},
\end{cases}
$$
and
$$
C_m(7)=
\begin{cases}
0,&m\text{ even},\\
3\cdot2^{3(m-1)/2+3},&m\text{ odd}.
\end{cases}
$$
Dividing by $8$ gives the required sign counts.

Final Answer: $\boxed{2^{3\lfloor m/2\rfloor-1}\left(1+\frac52(1-(-1)^m),\,3(1-(-1)^m)\right)}$

---

## Answer

$2^{3\lfloor m/2\rfloor-1}\left(1+\frac52(1-(-1)^m),\,3(1-(-1)^m)\right)$

---

## Classification

Problem Type: Exact computation

Answer Type: Tuple or ordered list

---

## Solution Concepts

- root lattice $A_3$
- quadratic Gauss sum
- degenerate two-adic Fourier transform
- ternary quadratic congruence
- valuation recurrence

---

## Black-Box Audit

No issues found.

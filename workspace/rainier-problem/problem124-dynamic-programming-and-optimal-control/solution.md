## Steps

Step 1: Reduce the terminal conditions and record three excursion bounds
Write $x=x_u$. Then $x(0)=x(1)=0$, $|x'|\leq1$ almost everywhere, and
$$
\int_0^1x(t)\,dt=0,\qquad \int_0^1t x(t)\,dt=0.
$$
Indeed the first identity is $y_u(1)=0$, while $z_u(1)=0$ gives $\int_0^1(1-t)x(t)\,dt=0$. Conversely these two moments give the required terminal values after taking $u=x'$ almost everywhere.

Let $v\geq0$ be $1$-Lipschitz on an interval of length $L$, with $v=0$ at both endpoints. Put
$$
B=\int v,\qquad Q=\int v^3,\qquad H=\max v.
$$
For $0\leq a<H$, let $m(a)=|\{v>a\}|$. If $a<b$, the $(b-a)$-neighborhood of $\{v>b\}$ lies in $\{v>a\}$, so
$$
m(a)\geq m(b)+2(b-a).
$$
Hence $e(a)=m(a)-2(H-a)$ is nonnegative and nonincreasing. Layer cake gives
$$
B=H^2+E,\qquad
Q=\frac{H^4}{2}+\int_0^H3a^2e(a)\,da,
\qquad
E=\int_0^He(a)\,da.
$$
For increasing $f$ and decreasing $g$ on $[0,H]$, reversed Chebyshev gives
$$
\frac{1}{H}\int_0^Hfg
\leq
\left(\frac{1}{H}\int_0^Hf\right)
\left(\frac{1}{H}\int_0^Hg\right).
$$
With $f(a)=a^2$,
$$
Q\leq H^2B-\frac{H^4}{2}\leq\frac{B^2}{2}.
$$
Also $v(t)\leq\min\{t,L-t\}$, so $B\leq L^2/4$ and therefore $L\geq2\sqrt B$.

For the reverse cubic bound at fixed $B,L$, let $b$ be the smaller root of $B=b(L-b)$ and let $v_b(t)=\min\{t,L-t,b\}$. With $\phi(s)=s^3-3b^2s$, one has $\phi(v)\geq\phi(v_b)$ pointwise: where $v_b<b$, the endpoint Lipschitz bounds give $v\leq v_b\leq b$ and $\phi$ is decreasing; where $v_b=b$,
$$
\phi(v)-\phi(b)=(v-b)^2(v+2b)\geq0.
$$
Since $\int v=\int v_b=B$,
$$
Q\geq\Phi(B,L):=Bb^2-\frac{b^4}{2}.
$$
At fixed $B$,
$$
b_L=-\frac{b}{L-2b}<0,\qquad
\Phi_L=-2b^3,
$$
so $\Phi$ decreases and is strictly convex in $L$.

Finally, if $\beta=B^{-1}\int_0^Lt,v(t)\,dt$ is the barycenter, then
$$
\sqrt B\leq\beta\leq L-\sqrt B.
$$
For the left inequality, $v(t)\leq t$ implies that the first moment of $\{v>a\}$ is at least $a,m(a)+m(a)^2/2$. Using reversed Chebyshev for $a$ and $e(a)$ and Cauchy-Schwarz for $e$,
$$
\int_0^Lt,v(t)\,dt
\geq
H^3+\frac{3H}{2}E+\frac{E^2}{2H}
\geq
(H^2+E)^{3/2}=B^{3/2},
$$
because
$$
\left(1+\frac{3}{2}r+\frac{1}{2}r^2\right)^2-(1+r)^3
=\frac{1}{4}r^2(1+r)^2\geq0.
$$
Reflection gives the right inequality.

Step 2: Use the largest positive excursion and handle the easy area-ratio range
Let the positive excursions have areas $A_i$ and total area
$$
A=\int_0^1x_+\,dt=\int_0^1x_-\,dt=a^2.
$$
If $A=0$, then $x=0$. Assume $A>0$, choose a positive excursion of largest area $h^2$, and put
$$
s=\frac{h}{a},\qquad 0<s\leq1.
$$
A largest excursion exists because the positive numbers $A_i$ are summable. Step 1 gives
$$
\int_0^1x_+^3\,dt
\leq\frac{1}{2}\sum_iA_i^2
\leq\frac{h^2A}{2}
=\frac{s^2a^4}{2}.
$$
Every positive excursion of area $A_i$ has length at least
$$
2\sqrt{A_i}\geq\frac{2A_i}{h},
$$
so their total occupied length is at least $2a/s$. Hence the negative excursions occupy total length at most
$$
S=1-\frac{2a}{s}.
$$
Let $B_N,L_N,Q_N$ be the area, length, and cubic-integral partial sums of the first $N$ negative excursions. Concatenating those excursions at zero endpoints preserves the $1$-Lipschitz bound, so Step 1 gives
$$
Q_N\geq\Phi(B_N,L_N).
$$
As $N\to\infty$, monotone convergence gives
$$
B_N\to a^2,\qquad L_N\to L_-,\qquad
Q_N\to\int_0^1x_-^3\,dt.
$$
By continuity of $\Phi$ and $L_-\leq S$,
$$
\int_0^1x_-^3\,dt
\geq\Phi(a^2,L_-)
\geq\Phi(a^2,S).
$$
This also handles countably many excursions.

Write the corresponding cap depth as $az$. Then
$$
S=a\left(z+\frac{1}{z}\right),
\qquad
a=\frac{z}{1+2z/s+z^2},
\qquad 0<z\leq1.
$$
Therefore
$$
\int_0^1x^3\,dt
\leq
a^4\left(\frac{s^2}{2}-z^2+\frac{z^4}{2}\right)
=:F_s(z).
$$
Differentiation gives
$$
F_s'(z)=
\frac{2s^4z^3(2z-s)(s+z)^2(z^2-1)}
{(sz^2+s+2z)^5}.
$$
Thus $F_s$ is maximized at $z=s/2$, with
$$
F_s(z)\leq\frac{s^6}{2(s^2+8)^3}.
$$
If $s^2\leq8/9$, then $10s^2\leq8+s^2$, so the right side is at most $1/2000$.

Step 3: Use the first moment when the largest positive excursion carries more than eight ninths of the area
Assume $s^2>8/9$. Let $c$ be the barycenter of the largest positive excursion. The barycenter margin from Step 1 puts $[c-h,c+h]$ inside that excursion, so all negative mass lies outside this interval. Reflecting $t\mapsto1-t$ preserves the moments and the objective, so write the smaller negative area on the left:
$$
B_L=a^2r^2,\qquad B_R=a^2w^2,
\qquad r^2+w^2=1,\qquad 0\leq r\leq w.
$$
Let
$$
E=A-h^2=a^2(1-s^2).
$$
If one side has zero area, its moment term is $0$. For nonzero sides with barycenters $c_L,c_R$, Step 1 gives
$$
ar\leq c_L\leq c-h-ar,
\qquad
c+h+aw\leq c_R\leq1-aw,
$$
and therefore
$$
c\geq h+2ar,\qquad 1-c\geq h+2aw.
$$

Set
$$
M_\pm=\int_0^1(t-c)x_\pm(t)\,dt.
$$
The chosen positive excursion has zero first moment about $c$, while the remaining positive area gives $M_+\leq E(1-c)$. The two moment constraints give $M_+=M_-$. The negative barycenter bounds give
$$
M_-
\geq
a^2w^2(h+aw)-a^2r^2(c-ar).
$$
Hence
$$
E(1-c)
\geq
a^2w^2(h+aw)-a^2r^2(c-ar).
$$

If $w\geq s$, the right side minus $E(1-c)$ has derivative $a^2(w^2-s^2)\geq0$ with respect to $c$, so the weakest necessary condition occurs at $c=h+2ar$. This gives
$$
aK_1\leq1-s^2,
$$
where
$$
K_1=w^3+w^2s-r^3-r^2s-2rs^2+2r-s^3+s.
$$
Since $w\geq s$ implies $r^2\leq1-s^2<1/9$,
$$
K_1
=(w^3-s^3)+s(w^2-r^2)+r\bigl(2(1-s^2)-r^2\bigr)
\geq\frac{7s}{9}.
$$
Thus
$$
a\leq\frac{3}{14\sqrt{2}},
$$
and already
$$
\int_0^1x^3\,dt\leq\frac{a^4}{2}<\frac{1}{2000}.
$$

We may therefore assume $w<s$. Now the same derivative is negative, so use the largest allowed value $c=1-h-2aw$. After simplification,
$$
aK(s,r)\leq r^2,
$$
where
$$
K(s,r)=2ws^2+s^3+r-w^3-w^2r.
$$
Put $s_0=2\sqrt{2}/3$. Since
$$
\frac{\partial K}{\partial s}=s(4w+3s)>0,
$$
we have
$$
K(s,r)\geq K(s_0,r)
=w\left(\frac{7}{9}+r^2\right)+\frac{16\sqrt{2}}{27}+r^3.
$$

Let $\ell_L,\ell_R$ be the total occupied lengths of the left and right negative excursions. Using the same finite-partial-sum concatenation argument as in Step 2,
$$
\int_0^1x_-^3\,dt
\geq
\Phi(a^2r^2,\ell_L)+\Phi(a^2w^2,\ell_R),
$$
while
$$
\ell_L+\ell_R\leq1-\frac{2a}{s}.
$$
Since $\Phi$ decreases and is strictly convex, the minimum uses all available length. At an interior minimum its derivatives $-2b^3$ agree, so the two cap depths are equal. Writing the common depth as $az$,
$$
1=\frac{2a}{s}+a\left(2z+\frac{1}{z}\right),
\qquad
\int_0^1x_-^3\,dt\geq a^4(z^2-z^4).
$$
Hence
$$
\int_0^1x^3\,dt
\leq
\frac{s^4z^4(s^2/2-z^2+z^4)}
{(2sz^2+s+2z)^4}
=:G_s(z).
$$
For $0<z\leq1/\sqrt{2}$,
$$
G_s'(z)=
\frac{2s^4z^3(2z-s)(s+z)^2(2z^2-1)}
{(2sz^2+s+2z)^5},
$$
so $G_s$ is maximized at $z=s/2$. Therefore
$$
G_s(z)
\leq
\frac{s^6}{16(s^2+4)^3}
\leq
\frac{1}{2000}.
$$

At a boundary minimizer, the boundary where the larger packet is triangular cannot minimize: its cap depth is $aw\geq ar$, while the other cap depth is at most $ar$, so transferring length toward the larger packet decreases the convex objective. Hence the smaller packet is triangular. If the larger packet has cap depth $av$, the one-sided derivative condition is
$$
-2r^3+2v^3\geq0,
$$
so $v\geq r$. Since $w^2v^2-v^4/2$ increases on $0\leq v\leq w$,
$$
\int_0^1x_-^3\,dt\geq a^4r^2w^2,
$$
and therefore
$$
\int_0^1x^3\,dt
\leq
a^4\left(\frac{s^2}{2}-r^2w^2\right).
$$

For $r\leq1/2$, $w\geq\sqrt{3}/2$ and the lower bound for $K$ gives
$$
K
>
\frac{7\sqrt{3}}{18}+\frac{16\sqrt{2}}{27}
>
\frac{3}{2},
$$
where the last inequality follows from $\sqrt{3}>19/11$ and $\sqrt{2}>7/5$. Thus $a\leq1/6$, so the objective is at most $1/2592<1/2000$.

For $1/2\leq r\leq5/8$, set
$$
D(r)=K(s_0,r)-5r^2.
$$
Then
$$
D'(r)=
\frac{r\left(11-27r^2-(90-27r)w\right)}{9w}<0,
$$
because $90-27r\geq585/8$ and $w\geq\sqrt{39}/8>3/4$. Also
$$
D\left(\frac{5}{8}\right)
=
-\frac{875}{512}
+\frac{16\sqrt{2}}{27}
+\frac{673\sqrt{39}}{4608}
>
\frac{113}{4320}>0,
$$
using $\sqrt{2}>7/5$ and $\sqrt{39}>31/5$. Thus $K\geq5r^2$, so $a\leq1/5$. Since $r^2w^2=r^2(1-r^2)$ is increasing on $r\leq1/\sqrt2$,
$$
r^2w^2\geq\frac{3}{16},
$$
and the same upper bound is at most $1/2000$.

Finally, if $r\geq5/8$, the occupied-length bounds give
$$
1\geq\frac{2a}{s}+2a(r+w).
$$
Using $s\leq1$ and $w\geq\sqrt{39}/8$,
$$
a\leq\frac{4}{13+\sqrt{39}}.
$$
Also
$$
r^2w^2\geq\frac{975}{4096},
$$
so
$$
\int_0^1x^3\,dt
\leq
\frac{1073}{16(13+\sqrt{39})^4}
<
\frac{1}{2000}.
$$
Indeed
$$
(13+\sqrt{39})^4
=69628+10816\sqrt{39}
>134125
=125\cdot1073.
$$
Every admissible control has value at most $1/2000$.

Step 4: Exhibit an admissible control attaining the bound
Define
$$
x(t)=
\begin{cases}
-t,&0\leq t\leq\frac{1}{10},\\
-\frac{1}{10},&\frac{1}{10}\leq t\leq\frac{1}{5},\\
t-\frac{3}{10},&\frac{1}{5}\leq t\leq\frac{1}{2},\\
\frac{7}{10}-t,&\frac{1}{2}\leq t\leq\frac{4}{5},\\
-\frac{1}{10},&\frac{4}{5}\leq t\leq\frac{9}{10},\\
t-1,&\frac{9}{10}\leq t\leq1.
\end{cases}
$$
Then $u=x'$ belongs to $[-1,1]$ almost everywhere. The positive area is $1/25$ and the two negative areas are $1/50$ each, so $\int_0^1x=0$. Since $x(t)=x(1-t)$,
$$
\int_0^1t x(t)\,dt
=
\frac{1}{2}\int_0^1x(t)\,dt
=0.
$$
Thus all terminal constraints hold. The positive triangle contributes $1/1250$, while the two negative capped tents contribute $3/10000$, so
$$
\int_0^1x(t)^3\,dt
=
\frac{1}{1250}-\frac{3}{10000}
=
\frac{1}{2000}.
$$

Final Answer: $\boxed{\frac{1}{2000}}$

---

## Answer

$\frac{1}{2000}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- layer-cake representation
- lipschitz excursion bounds
- barycenter margin
- convex length allocation
- moment-constrained extremal packing
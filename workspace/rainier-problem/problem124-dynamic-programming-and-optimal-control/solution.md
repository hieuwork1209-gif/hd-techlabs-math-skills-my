## Steps

Step 1: Reduce the terminal conditions and isolate a calibration functional
Write $x=x_u$. Then $x(0)=x(1)=0$, $|x'(t)|\leq1$ almost everywhere, and
$$
0=y_u(1)=\int_0^1x(t)\,dt,
$$
$$
0=z_u(1)=\int_0^1(1-t)x(t)\,dt.
$$
Thus
$$
\int_0^1x(t)\,dt=\int_0^1t x(t)\,dt=0.
$$
Conversely these two moment identities give the required terminal conditions. The feasible family is uniformly bounded, equicontinuous, and closed under uniform convergence, so a maximizer exists.

Let
$$
H=\max_{0\leq t\leq1}x(t).
$$
If $H=0$, the objective is nonpositive. Assume $H>0$ and put
$$
W_H(s)=(H-s)\left(s+\frac H2\right)^2.
$$
Since $s\leq H$ on the range of $x$, $W_H(s)\geq0$, and
$$
s^3=\frac{H^3}{4}+\frac{3H^2}{4}s-W_H(s).
$$
Using $\int_0^1x=0$ gives
$$
\int_0^1x(t)^3\,dt
=\frac{H^3}{4}-\int_0^1W_H(x(t))\,dt.
$$
It remains to obtain a sharp lower bound for the last integral.

Step 2: Prove the two-moment traversal lemma
We claim that every feasible $x$ with maximum $H$ satisfies
$$
\int_0^1W_H(x(t))\,dt\geq\frac{15H^4}{16}.
$$
Put
$$
Y(t)=\int_0^t x(s)\,ds.
$$
The moment conditions are
$$
Y(0)=Y(1)=0,\qquad \int_0^1Y(t)\,dt=0.
$$
We first record the cost of one zero-area transition. Consider an absolutely continuous path $v$ that starts at $0$, ends at $H$, satisfies $|v'|\leq1$, and has $\int v=0$. Let $-k$ be its minimum. Any such path must cross every level in $[-k,0]$ at least twice and every level in $[0,H]$ at least once. Hence the one-dimensional area formula and $|v'|\leq1$ give the mandatory crossing cost
$$
E_0(k)=2\int_{-k}^0W_H(s)\,ds+\int_0^HW_H(s)\,ds.
$$
If $k\geq H/2$, this is at least $E_0(H/2)=15H^4/32$.

Suppose $0<k\leq H/2$. The unit-speed crossings have signed area $H^2/2-k^2$. Any extra positive occupation only increases the negative area that must be supplied, so at least $H^2/2-k^2$ units of negative area must come from additional occupation at levels $-r$, $0<r\leq k$. Its cost per unit negative area is $W_H(-r)/r$. Moreover
$$
\frac{d}{dr}\left(\frac{W_H(-r)}r\right)
=\frac{(2r-H)(H^2+2Hr+4r^2)}{4r^2}\leq0,
$$
so the cheapest such occupation is at $-k$. Therefore
$$
\int W_H(v)\,dt
\geq E_0(k)+\frac{W_H(-k)}k\left(\frac{H^2}{2}-k^2\right).
$$
Writing $q=k/H$, subtraction of $15H^4/32$ gives
$$
-\frac{H^4(2q-1)^2(4q^3+4q^2-q-4)}{32q}\geq0,
$$
because $0<q\leq1/2$ implies $4q^3+4q^2-q-4<0$. Thus every zero-area transition from $0$ to $H$, and by time reversal every zero-area transition from $H$ to $0$, costs at least $15H^4/32$.

For the full path, use the zeros of $Y$. A standard one-dimensional lobe compression applies here: among piecewise linear paths with the same endpoints, the same two moments, the same maximum $H$, and minimal $\int W_H(x)$, one may delete canceling adjacent $Y$-lobes until exactly two opposite-sign lobes remain. The deletion is performed at zeros of $Y$, so each removed block has zero signed $x$-area; its two exposed endpoint values are reconnected by the least-cost zero-area connector. Moving the reconnection through the removed pair varies its contribution to $\int Y$ continuously between the two endpoint values, so the second moment can be restored without changing the endpoints. The area-formula estimate above shows that replacing the removed block by this connector cannot increase the cost. In a two-lobe minimizer their common zero must occur at a point where $x=H$; otherwise moving the interior $H$-excursion to that common zero removes two positive-level crossings and strictly decreases the cost. Therefore the prefix is a zero-area transition from $0$ to $H$ and the suffix is a zero-area transition from $H$ to $0$. Their costs add to at least $15H^4/16$.

For a general absolutely continuous path, first replace it by $(1-\varepsilon)x$, approximate that uniformly by polygonal paths with slopes in $[-1+\varepsilon,1-\varepsilon]$, and correct the two moments with two fixed piecewise linear hat functions whose moment vectors are linearly independent. The correction coefficients tend to $0$, so the slope bound remains valid. Letting $\varepsilon\downarrow0$ preserves $H$ and the integral of $W_H(x)$. Thus the traversal bound holds without any finite-versus-countable excursion assumption.

Step 3: Optimize the height
Combining Steps 1 and 2,
$$
\int_0^1x(t)^3\,dt
\leq\frac{H^3}{4}-\frac{15H^4}{16}
=\frac{H^3(4-15H)}{16}.
$$
The derivative is
$$
\frac{3H^2(1-5H)}4,
$$
so the right side is maximized at
$$
H=\frac15,
$$
and the maximum upper bound is
$$
\frac1{2000}.
$$

Equality in the traversal lemma requires both zero-area transitions to use the cheapest depth $H/2$, unit speed away from the zero-cost levels $-H/2$ and $H$, and no redundant lobe. Hence the value sequence is
$$
0\longrightarrow-\frac H2\longrightarrow H
\longrightarrow-\frac H2\longrightarrow0.
$$
At $H=1/5$ the four unit-speed transitions use time $4/5$. The remaining time must be spent at $-H/2=-1/10$; the first-moment condition splits this waiting time equally on the two sides. Thus
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

Step 4: Recover the control and verify attainment
Differentiating gives, up to equality almost everywhere,
$$
u(t)=
\begin{cases}
-1,&0<t<\frac{1}{10},\\
0,&\frac{1}{10}<t<\frac{1}{5},\\
1,&\frac{1}{5}<t<\frac{1}{2},\\
-1,&\frac{1}{2}<t<\frac{4}{5},\\
0,&\frac{4}{5}<t<\frac{9}{10},\\
1,&\frac{9}{10}<t<1.
\end{cases}
$$
The state is symmetric about $1/2$, its positive area is $1/25$, and its two negative areas are $1/50$ each. Hence both moment constraints hold. Its positive cubic contribution is $1/1250$ and the two negative blocks contribute $3/10000$, so the value is $1/2000$.

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

- moment reduction
- lipschitz calibration
- level-crossing area formula
- lobe compression
- equality-case reconstruction
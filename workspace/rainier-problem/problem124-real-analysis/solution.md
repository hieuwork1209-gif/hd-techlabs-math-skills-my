## Steps

Step 1: Establish the sharp cap estimates with a prescribed endpoint value

Let $h\geq0$ be $1$-Lipschitz on $[0,1]$, with $h(0)=0$ and $h(1)=r\geq0$. Put
$$
a=\int_0^1h(x)\,dx,\qquad q=\int_0^1h(x)^2\,dx,\qquad S=|\{h>0\}|.
$$
We first prove
$$
S\geq\sqrt{4a+2r^2}-r
$$
and
$$
q\leq\frac23\left(a+\frac{r^2}{2}\right)^{3/2}-\frac{r^3}{3}.
$$
For the support bound, let the positivity component ending at $1$ have length $\ell_0$; when $r=0$ it may be absent. Every other component of length $\ell$ has both endpoint values $0$, so the Lipschitz condition gives the tent bound $h(x)\leq\min(x-u,v-x)$ and hence area at most $\ell^2/4$. On the terminal component, after translating its left endpoint to $0$, the pointwise envelope is
$$
h(t)\leq\min(t,r+\ell_0-t),
$$
whose integral is $(\ell_0^2+2r\ell_0-r^2)/4$. Therefore, if the other component lengths are $\ell_i$,
$$
4a\leq \ell_0^2+2r\ell_0-r^2+\sum_i\ell_i^2
\leq S^2+2rS-r^2,
$$
which gives the stated lower bound for $S$.

For the quadratic bound, let $M=\max h$ and $m(t)=|\{h>t\}|$ for $0\leq t<M$. Set $p=\lim_{t\uparrow M}m(t)$. If $0\leq s<t<r$, the terminal superlevel component loses at least $t-s$ of length when the level rises from $s$ to $t$, so $m(s)\geq m(t)+(t-s)$. If $r\leq s<t<M$, every nonempty superlevel component has two finite boundary points, so $m(s)\geq m(t)+2(t-s)$. Thus
$$
m_0(t)=
\begin{cases}
p+2M-r-t,&0\leq t<r,\\
p+2(M-t),&r\leq t<M
\end{cases}
$$
has the property that $e(t):=m(t)-m_0(t)$ is nonincreasing on each side of $r$; splitting an interval at $r$ gives the same conclusion across $r$. Since $e(t)\to0$ as $t\uparrow M$, we have $e(t)\geq0$ for all $t<M$. Layer cake gives
$$
a=pM+M^2-\frac{r^2}{2}+\int_0^M e(t)\,dt
$$
and
$$
q=pM^2+\frac{2M^3-r^3}{3}+2\int_0^M t e(t)\,dt.
$$
Since $e$ is nonincreasing,
$$
\int_0^M\int_0^M(t-s)(e(t)-e(s))\,ds\,dt\leq0,
$$
so $2\int_0^Mte(t)\,dt\leq M\int_0^Me(t)\,dt$. Hence
$$
q\leq M\left(a+\frac{r^2}{2}\right)-\frac{M^3}{3}-\frac{r^3}{3}.
$$
The area identity also gives $M^2\leq a+r^2/2$. The right-hand side is increasing for $0\leq M\leq\sqrt{a+r^2/2}$, which proves
$$
q\leq\frac23\left(a+\frac{r^2}{2}\right)^{3/2}-\frac{r^3}{3}.
$$
For $r=0$ these become the familiar two-sided estimates $S\geq2\sqrt a$ and $q\leq\frac23a^{3/2}$.

Step 2: Solve the normalized one-sided zero-mean problem

Let $g$ be $1$-Lipschitz on $[0,1]$, with
$$
g(0)=0,\qquad g(1)=r\geq0,\qquad \int_0^1g(x)\,dx=0.
$$
Write the common positive and negative area as
$$
A=\int_0^1g_+(x)\,dx=\int_0^1g_-(x)\,dx=s^2.
$$
Because $g_+(1)=r$ and $g_-(0)=g_-(1)=0$, Step 1 gives
$$
|\{g_+>0\}|\geq\sqrt{4s^2+2r^2}-r,
\qquad |\{g_->0\}|\geq2s.
$$
The supports are disjoint, so
$$
2s+\sqrt{4s^2+2r^2}-r\leq1.
$$
Squaring after moving $2s$ to the right gives
$$
s\leq s_r:=\frac{1+2r-r^2}{4(1+r)}.
$$
Also, $g_+(x)\geq\max(0,r+x-1)$ by the endpoint Lipschitz bound, so $A\geq r^2/2$, or $s\geq r/\sqrt2$. Thus feasibility requires
$$
\frac{r}{\sqrt2}\leq\frac{1+2r-r^2}{4(1+r)},
$$
which is equivalent to
$$
(4+\sqrt2)r^2+(4-2\sqrt2)r-\sqrt2\leq0.
$$
Its roots are $\sqrt2-1$ and $-(3+\sqrt2)/7$. Since $r\geq0$, the inequality holds exactly for
$$
0\leq r\leq r_0:=\sqrt2-1.
$$
Thus $r_0$ is the largest possible endpoint magnitude for a one-sided zero-mean function.

Applying the quadratic estimate from Step 1 to $g_+$ with endpoint $r$, and to $g_-$ with endpoint $0$, yields
$$
\int_0^1g(x)^2\,dx
\leq \frac23s^3+\frac23\left(s^2+\frac{r^2}{2}\right)^{3/2}-\frac{r^3}{3}.
$$
This expression is strictly increasing in $s>0$, so $s=s_r$ gives the sharp bound. The defining equality for $s_r$ gives
$$
\sqrt{s_r^2+\frac{r^2}{2}}=\frac{1+r-2s_r}{2}=\frac{1+2r+3r^2}{4(1+r)}.
$$
If
$$
A_r=1+2r-r^2,\qquad B_r=1+2r+3r^2,
$$
then substitution into the preceding energy bound gives
$$
E(r):=\max\int_0^1g(x)^2\,dx
=\frac{A_r^3+B_r^3}{96(1+r)^3}-\frac{r^3}{3}
=\frac{1+4r+6r^2-12r^3-3r^4}{48(1+r)}.
$$
Differentiating this rational expression and factoring gives
$$
E'(r)=\frac{(1-2r-r^2)(3r^2+6r+1)}{16(1+r)^2}\geq0
$$
for $0\leq r\leq r_0$.

For $0<r\leq r_0$, equality in the energy bound forces $s=s_r$, hence equality in both support estimates from Step 1. In the support proof, equality in the sum-of-squares bound forces a single component, and equality in the pointwise envelope forces that component to fill its tent or terminal-cap envelope. Thus the negative set is one full tent of length $2s_r$, the positive set is one terminal cap filling the remaining interval, and there is no zero gap. With
$$
b_r=s_r+\frac{1+r}{2},
$$
the resulting function is
$$
g_r(x)=
\begin{cases}
-x,&0\leq x\leq s_r,\\
x-2s_r,&s_r\leq x\leq b_r,\\
1+r-x,&b_r\leq x\leq1.
\end{cases}
$$
The equality
$$
2s_r+\sqrt{4s_r^2+2r^2}-r=1
$$
shows that the terminal cap has area $s_r^2$, while the negative tent has area $s_r^2$. Hence $g_r$ has mean zero and attains equality in the two cap estimates, so it attains $E(r)$. The equality conditions above show that it is the unique maximizer with endpoint $r>0$. For endpoint $-r<0$, the unique maximizer is $-g_r$. At $r=0$ there are exactly two maximizers, $g_0$ and $-g_0$.

Step 3: Couple the two unequal cancellation intervals

For an admissible $f$, put $m=f(1/3)$ and define
$$
g_1(t)=3f\left(\frac{t}{3}\right),
\qquad
g_2(t)=\frac32 f\left(1-\frac{2t}{3}\right),
\qquad 0\leq t\leq1.
$$
Both functions are $1$-Lipschitz, start at $0$, and have integral $0$. Their endpoint magnitudes are
$$
|g_1(1)|=3|m|=:r,
\qquad |g_2(1)|=\frac32|m|=\frac r2.
$$
Step 2 gives $0\leq r\leq r_0$ and, after the two changes of variables,
$$
\int_0^1 f(x)^2\,dx
\leq \frac1{27}E(r)+\frac8{27}E\left(\frac r2\right).
$$
Because $E$ is nondecreasing on $[0,r_0]$ and $E(r/2)$ is strictly increasing there, the right-hand side is strictly increasing in $r$ and is maximized at $r=r_0$.

Write $\rho=r_0=\sqrt2-1$, so $\rho^2+2\rho-1=0$. In the numerator of $E(\rho)$ this relation gives
$$
1+4\rho+6\rho^2-12\rho^3-3\rho^4=16-32\rho,
$$
so
$$
E(\rho)=\frac{1-2\rho}{3(1+\rho)}=\frac{\sqrt2}{2}-\frac23.
$$
Likewise,
$$
E\left(\frac\rho2\right)
=\frac{16+32\rho+24\rho^2-24\rho^3-3\rho^4}{384(\rho+2)}
=\frac{73-100\rho}{384(\rho+2)}
=\frac{273\sqrt2-373}{384}.
$$
Therefore
$$
\begin{aligned}
\int_0^1 f(x)^2\,dx
&\leq \frac1{27}\left(\frac{\sqrt2}{2}-\frac23\right)
+\frac8{27}\left(\frac{273\sqrt2-373}{384}\right)\\
&=\frac{11\sqrt2-15}{48}.
\end{aligned}
$$

Step 4: Verify attainment and classify every equality case

Let $r_0=\sqrt2-1$, $r_1=r_0/2$, and let $g_r$ be the explicit one-sided extremizer from Step 2. Define
$$
f_*(x)=
\begin{cases}
\frac13 g_{r_0}(3x),&0\leq x\leq\frac13,\\
\frac23 g_{r_1}\left(\frac32(1-x)\right),&\frac13\leq x\leq1.
\end{cases}
$$
The two formulas agree at $x=1/3$ because
$$
\frac13r_0=\frac23r_1.
$$
Thus $f_*$ is absolutely continuous, has endpoint values $0$, and satisfies $|f_*'|=1$ almost everywhere. Scaling the zero-mean identities for $g_{r_0}$ and $g_{r_1}$ gives
$$
\int_0^{1/3}f_*(x)\,dx=0,
\qquad
\int_{1/3}^1f_*(x)\,dx=0.
$$
The calculation in Step 3 is therefore attained by $f_*$, and also by $-f_*$. Conversely, equality in the global bound forces $r=r_0$ by the strict increase established in Step 3, and then equality must hold in both applications of the one-sided lemma. Their endpoint signs must agree at $x=1/3$, so the only possibilities are exactly $f_*$ and $-f_*$. Hence all equality cases are classified.

Final Answer: $\boxed{\frac{11\sqrt{2}-15}{48}}$

---

## Answer

$\frac{11\sqrt{2}-15}{48}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- Lipschitz extremal inequalities
- layer-cake representation
- positive and negative parts
- scaling arguments
- equality classification

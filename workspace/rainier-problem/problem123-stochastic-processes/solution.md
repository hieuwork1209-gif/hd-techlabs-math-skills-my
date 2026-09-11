## Steps

Step 1: Reduce the urn to the red-count chain

Let $R_n$ and $B_n$ be the red and blue counts after $n$ draws, with
$$
R_0=B_0=1.
$$
Every draw adds exactly two balls, so
$$
R_n+B_n=2n+2.
\tag{1}
$$
Conditional on the history $\mathcal F_n$, the red count increases by one exactly when a red ball is drawn. Hence
$$
P(R_{n+1}=R_n+1\mid\mathcal F_n)=\frac{R_n}{2n+2},
$$
$$
P(R_{n+1}=R_n\mid\mathcal F_n)=1-\frac{R_n}{2n+2},
\tag{2}
$$
and therefore
$$
E(R_{n+1}\mid\mathcal F_n)
=R_n\left(1+\frac1{2n+2}\right).
\tag{3}
$$

Step 2: Obtain an almost-sure $\sqrt n$ scaling limit

Define
$$
a_0=1,
\qquad
a_n=\prod_{j=0}^{n-1}\left(1+\frac1{2j+2}\right).
$$
By (3),
$$
M_n:=\frac{R_n}{a_n}
$$
is a nonnegative martingale, so $M_n$ converges almost surely to a finite random variable $M_\infty$.

The product is
$$
a_n
=\prod_{j=0}^{n-1}\frac{j+3/2}{j+1}
=\frac{\Gamma(n+3/2)}{\Gamma(3/2)\Gamma(n+1)}.
$$
For fixed $c,d$, Stirling's formula gives
$$
\frac{\Gamma(n+c)}{\Gamma(n+d)}
=n^{c-d}(1+O(n^{-1})).
\tag{4}
$$
Using $\Gamma(3/2)=\sqrt\pi/2$,
$$
\frac{a_n}{\sqrt n}\longrightarrow\frac2{\sqrt\pi}.
$$
Thus
$$
\frac{R_n}{\sqrt n}\longrightarrow
W:=\frac2{\sqrt\pi}M_\infty
\qquad\text{almost surely.}
\tag{5}
$$

Step 3: Identify the law of the limit

For an integer $k\ge1$, write
$$
x^{\overline{k}}=x(x+1)\cdots(x+k-1).
$$
For $r\ge1$,
$$
(r+1)^{\overline{k}}
=r^{\overline{k}}\frac{r+k}{r}.
$$
Using (2), conditional on $R_n=r$,
$$
\begin{aligned}
E(R_{n+1}^{\overline{k}}\mid R_n=r)
&=r^{\overline{k}}
\left(1-\frac r{2n+2}\right)
+r^{\overline{k}}\frac{r+k}{r}\frac r{2n+2}\\
&=r^{\overline{k}}
\left(1+\frac{k}{2n+2}\right).
\end{aligned}
$$
Since $R_0=1$ and $1^{\overline{k}}=k!$, iteration yields
$$
E R_n^{\overline{k}}
=k!\prod_{j=0}^{n-1}\left(1+\frac{k}{2j+2}\right)
=k!\frac{\Gamma(n+1+k/2)}{\Gamma(1+k/2)\Gamma(n+1)}.
\tag{6}
$$
By (4),
$$
\frac{E R_n^{\overline{k}}}{n^{k/2}}
\longrightarrow
\frac{k!}{\Gamma(1+k/2)}.
\tag{7}
$$
Because
$$
x^{\overline{k}}=x^k+O_k(x^{k-1}+1)
$$
and (6) with $k-1$ gives $E R_n^{k-1}=O(n^{(k-1)/2})$, replacing the rising factorial by $R_n^k$ does not change the limit. Also (6) with $k+1$ gives a uniform bound on the $(k+1)$st moments of $R_n/\sqrt n$, so the $k$th powers are uniformly integrable. Combining this with (5),
$$
E W^k=\frac{k!}{\Gamma(1+k/2)}.
\tag{8}
$$

Let $Z\sim N(0,2)$. The density of $|Z|$ on $(0,\infty)$ is
$$
\frac1{\sqrt\pi}e^{-x^2/4},
$$
so
$$
E|Z|^k
=\frac{2^k\Gamma((k+1)/2)}{\sqrt\pi}.
$$
The duplication identity
$$
\Gamma\!\left(\frac{k+1}{2}\right)
\Gamma\!\left(1+\frac k2\right)
=2^{-k}\sqrt\pi\,\Gamma(k+1)
$$
shows that these moments equal (8).

For uniqueness, Carleman's criterion says that a law with moments $m_j$ is moment-determinate if
$$
\sum_{j=1}^\infty m_{2j}^{-1/(2j)}=\infty.
$$
Here
$$
m_{2j}=\frac{(2j)!}{j!},
$$
and Stirling's formula gives
$$
m_{2j}^{-1/(2j)}\sim\frac{\sqrt e}{2\sqrt j},
$$
so the series diverges. Therefore
$$
W\overset d=|N(0,2)|,
\qquad
P(W>0)=1.
\tag{9}
$$

Step 4: Invert the global scaling at the hitting times

For $m\ge2$, let
$$
\tau_m=\inf\{n\ge0:R_n=m\}.
$$
By (5) and (9), $R_n\to\infty$ almost surely. Since every increment of $R_n$ is either $0$ or $1$, every positive integer level is hit almost surely, and $R_{\tau_m}=m$.

Also $\tau_m\to\infty$ almost surely. Evaluating (5) along the random subsequence $n=\tau_m$ gives
$$
\frac{m}{\sqrt{\tau_m}}
=\frac{R_{\tau_m}}{\sqrt{\tau_m}}
\longrightarrow W
\qquad\text{almost surely.}
$$
Hence, with
$$
X_m:=\frac{m^2}{\tau_m},
$$
we have
$$
X_m\longrightarrow W^2
\qquad\text{almost surely.}
\tag{10}
$$

Step 5: Analyze the next-level spacing conditionally on the random clock

Set
$$
G_m:=\tau_{m+1}-\tau_m,
\qquad
V_m:=\frac{mG_m}{\tau_m}
=m\left(\frac{\tau_{m+1}}{\tau_m}-1\right).
\tag{11}
$$
Fix $m$ and condition on $\tau_m=n$. Until the next red draw occurs, the red count stays equal to $m$. Therefore, for every integer $\ell\ge0$,
$$
P(G_m>\ell\mid\tau_m=n)
=\prod_{j=0}^{\ell-1}
\left(1-\frac{m}{2(n+j)+2}\right).
\tag{12}
$$

We now show that, on the natural scale determined by $n$, this waiting time has an asymptotically universal law. Fix constants $0<a<b<\infty$ and $C>0$, assume
$$
a m^2\le n\le b m^2,
$$
and for $0\le x\le C$ put
$$
\ell=\left\lfloor\frac{xn}{m}\right\rfloor.
$$
Write
$$
p_j=\frac{m}{2(n+j)+2}.
$$
Since $j\le\ell=O(n/m)$, uniformly over the stated ranges,
$$
p_j=O(m^{-1}),
\qquad
\sum_{j=0}^{\ell-1}p_j^2=O(m^{-1}).
\tag{13}
$$
Also
$$
\begin{aligned}
\sum_{j=0}^{\ell-1}p_j
&=\frac m2\sum_{j=0}^{\ell-1}\frac1{n+j+1}\\
&=\frac m2\left(\frac{\ell}{n}+O\left(\frac{\ell^2}{n^2}+\frac{\ell}{n^2}\right)\right)\\
&=\frac x2+O(m^{-1}),
\end{aligned}
\tag{14}
$$
again uniformly. Because $\log(1-y)=-y+O(y^2)$ uniformly for $0\le y\le1/2$, equations (12)-(14) imply
$$
P(V_m>x\mid\tau_m=n)
=e^{-x/2+O(m^{-1})}
\tag{15}
$$
uniformly for $n/m^2\in[a,b]$ and $x\in[0,C]$.

Thus the conditional law of $V_m$ converges uniformly on such clock windows to an exponential law of rate $1/2$. Equivalently, for every $u\ge0$,
$$
\phi_{m,u}(n)
:=E(e^{-uV_m}\mid\tau_m=n)
\longrightarrow\frac1{1+2u}
\tag{16}
$$
uniformly for $n/m^2\in[a,b]$. For $u>0$, this follows directly from
$$
E(e^{-uV})
=1-u\int_0^\infty e^{-ux}P(V>x)\,dx,
$$
using (15) on $[0,C]$ and then letting $C\to\infty$; for $u=0$, (16) is immediate.

Step 6: Couple the local spacing with the global limit and evaluate the transform

By (10), $X_m=m^2/\tau_m\to W^2$ almost surely, where $0<W<\infty$ almost surely. Hence for every $\varepsilon>0$ there exist $0<a<b<\infty$ such that
$$
P\left(a\le\frac{\tau_m}{m^2}\le b\right)\ge1-\varepsilon
$$
for all sufficiently large $m$.
Together with the uniform convergence (16), this gives
$$
\phi_{m,u}(\tau_m)
\longrightarrow\frac1{1+2u}
$$
in probability. Since $0\le\phi_{m,u}\le1$, the convergence also holds in $L^1$.

Using conditional expectation and (11),
$$
\begin{aligned}
&E\exp\!\left[-t\frac{m^2}{\tau_m}
-u m\left(\frac{\tau_{m+1}}{\tau_m}-1\right)\right]\\
&\qquad=E\left[e^{-tX_m}\phi_{m,u}(\tau_m)\right]\\
&\qquad=\frac1{1+2u}E(e^{-tX_m})+o(1).
\end{aligned}
$$
By (10) and bounded convergence,
$$
E(e^{-tX_m})\longrightarrow E(e^{-tW^2}).
$$
Using (9), $W^2\overset d=Z^2$ with $Z\sim N(0,2)$, and therefore
$$
E(e^{-tW^2})
=\frac1{\sqrt{1+4t}}.
$$
Consequently
$$
\lim_{m\to\infty}
E\exp\!\left[-t\frac{m^2}{\tau_m}
-u m\left(\frac{\tau_{m+1}}{\tau_m}-1\right)\right]
=\frac1{(1+2u)\sqrt{1+4t}}.
$$

## Solution Concepts

- Martingale normalization and rising-factorial moments for a triangular balanced urn.
- Inversion of the global red-count scaling at first hitting times.
- Conditional local-hazard asymptotics yielding an exponential successive-level spacing independent of the global limit.

Final Answer: $\displaystyle \frac1{(1+2u)\sqrt{1+4t}}$.

## Steps

Step 1: Reduce the urn to a one-dimensional Markov update

Let $R_n$ and $B_n$ be the red and blue counts after $n$ draws, starting from
$$
R_0=B_0=1.
$$
Every draw adds exactly two balls, so the total count is deterministic:
$$
T_n=R_n+B_n=2n+2.
\tag{1}
$$
Conditional on the history $\mathcal F_n$, the red count changes only when a red ball is drawn. Hence
$$
P(R_{n+1}=R_n+1\mid\mathcal F_n)=\frac{R_n}{2n+2},
$$
$$
P(R_{n+1}=R_n\mid\mathcal F_n)=1-\frac{R_n}{2n+2}.
\tag{2}
$$
In particular,
$$
E(R_{n+1}\mid\mathcal F_n)
=R_n\left(1+\frac1{2n+2}\right).
\tag{3}
$$

Step 2: Construct the normalization that gives almost-sure convergence

Define
$$
a_0=1,
\qquad
a_n=\prod_{j=0}^{n-1}\left(1+\frac1{2j+2}\right).
$$
Equation (3) shows that
$$
M_n=\frac{R_n}{a_n}
$$
is a nonnegative martingale. Therefore $M_n$ converges almost surely to a finite random variable $M_\infty$.

The product can be written exactly as
$$
a_n
=\prod_{j=0}^{n-1}\frac{j+3/2}{j+1}
=\frac{\Gamma(n+3/2)}{\Gamma(3/2)\Gamma(n+1)}.
$$
Dividing the usual Stirling expansions gives, for fixed $c,d$,
$$
\frac{\Gamma(n+c)}{\Gamma(n+d)}
=n^{c-d}(1+O(n^{-1})).
\tag{4}
$$
Applying (4) with $(c,d)=(3/2,1)$ and using $\Gamma(3/2)=\sqrt\pi/2$ yields
$$
\frac{a_n}{\sqrt n}\longrightarrow\frac2{\sqrt\pi}.
$$
Consequently
$$
\frac{R_n}{\sqrt n}\longrightarrow
W:=\frac2{\sqrt\pi}M_\infty
\qquad\text{almost surely.}
\tag{5}
$$

Step 3: Compute every moment of the limit from a rising-factorial identity

For an integer $k\ge1$, write
$$
x^{\overline{k}}=x(x+1)\cdots(x+k-1).
$$
For $r\ge1$,
$$
(r+1)^{\overline{k}}
=r^{\overline{k}}\frac{r+k}{r}.
$$
Using (2), conditional on $R_n=r$ we obtain
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
Iterating from $R_0=1$, for which $1^{\overline{k}}=k!$, gives
$$
E R_n^{\overline{k}}
=k!\prod_{j=0}^{n-1}\left(1+\frac{k}{2j+2}\right)
=k!\frac{\Gamma(n+1+k/2)}{\Gamma(1+k/2)\Gamma(n+1)}.
\tag{6}
$$
Using (4),
$$
\frac{E R_n^{\overline{k}}}{n^{k/2}}
\longrightarrow
\frac{k!}{\Gamma(1+k/2)}.
\tag{7}
$$
For $k=1$, $x^{\overline1}=x$. For $k\ge2$,
$$
x^{\overline{k}}=x^k+O_k(x^{k-1}+1),
$$
and (6) with $k-1$ gives $E R_n^{k-1}=O(n^{(k-1)/2})$. Therefore replacing the rising factorial by $R_n^k$ does not change the limit in (7), and
$$
E\left(\frac{R_n}{\sqrt n}\right)^k
\longrightarrow
\frac{k!}{\Gamma(1+k/2)}.
\tag{8}
$$
Moreover (6) with $k+1$ gives a uniform bound on the $(k+1)$st moments of $R_n/\sqrt n$. Hence the $k$th powers are uniformly integrable. Combining this with the almost-sure convergence (5) yields
$$
E W^k=\frac{k!}{\Gamma(1+k/2)}
\qquad(k\ge1).
\tag{9}
$$

Step 4: Identify the limiting law and prove it is nonzero

Let $Z\sim N(0,2)$. The density of $|Z|$ on $(0,\infty)$ is
$$
\frac1{\sqrt\pi}e^{-x^2/4}.
$$
Therefore
$$
E|Z|^k
=\frac1{\sqrt\pi}\int_0^\infty x^k e^{-x^2/4}\,dx
=\frac{2^k\Gamma((k+1)/2)}{\sqrt\pi}.
$$
The gamma duplication identity
$$
\Gamma\!\left(\frac{k+1}{2}\right)
\Gamma\!\left(1+\frac k2\right)
=2^{-k}\sqrt\pi\,\Gamma(k+1)
$$
shows that this equals the right-hand side of (9).

To justify uniqueness from the moments, use the precise Carleman criterion: a probability law with moments $m_j$ is moment-determinate if
$$
\sum_{j=1}^\infty m_{2j}^{-1/(2j)}=\infty.
$$
Here
$$
m_{2j}=E W^{2j}=\frac{(2j)!}{j!}.
$$
Stirling's formula gives
$$
m_{2j}^{-1/(2j)}\sim\frac{\sqrt e}{2\sqrt j},
$$
so the displayed series diverges. Hence (9) determines the law, and
$$
W\overset d=|N(0,2)|.
\tag{10}
$$
In particular,
$$
P(W>0)=1.
\tag{11}
$$

Step 5: Invert the deterministic-time asymptotic at the hitting times

For $m\ge2$, let
$$
\tau_m=\inf\{n\ge0:R_n=m\}.
$$
By (5) and (11), $R_n\to\infty$ almost surely. Since $R_n$ increases only by $0$ or $1$, every level is reached, so
$$
P(\tau_m<\infty)=1.
$$
Also $\tau_m\ge m-1$, hence $\tau_m\to\infty$ almost surely as $m\to\infty$.

On the almost-sure event where (5) holds, evaluate it along the random subsequence $n=\tau_m$. Since $R_{\tau_m}=m$,
$$
\frac{m}{\sqrt{\tau_m}}
=\frac{R_{\tau_m}}{\sqrt{\tau_m}}
\longrightarrow W.
$$
Therefore
$$
\frac{m^2}{\tau_m}\longrightarrow W^2
\qquad\text{almost surely.}
\tag{12}
$$

Step 6: Evaluate the requested Laplace transform

Fix $t\ge0$. Because $0\le e^{-t m^2/\tau_m}\le1$, bounded convergence and (12) give
$$
\lim_{m\to\infty}E\exp\!\left(-t\frac{m^2}{\tau_m}\right)
=E e^{-tW^2}.
$$
Using (10),
$$
\begin{aligned}
E e^{-tW^2}
&=\frac1{\sqrt\pi}\int_0^\infty
\exp\!\left[-\left(t+\frac14\right)x^2\right]dx\\
&=\frac1{\sqrt{1+4t}}.
\end{aligned}
$$
Thus the limit exists for every $t\ge0$ and has the claimed exact form.

## Solution Concepts

- Martingale normalization for a triangular balanced urn.
- Exact rising-factorial moments and moment-determinate identification of the scaling limit.
- Inversion of an almost-sure scaling law through first hitting times.

Final Answer: $\displaystyle \frac1{\sqrt{1+4t}}$.

## Steps

Step 1: Solve the regime before the box constraint becomes active
Fix $0\le m\le 1/2$, and let $f\in L^2([-1,1])$ satisfy
$$
0\le f\le1\quad\text{a.e.},\qquad
\int_{-1}^1 f(x)\,dx=1,
\qquad
\int_{-1}^1 x f(x)\,dx=m.
$$
First consider the affine function
$$
g_0(x)=\frac{1+3mx}{2}.
$$
It has the prescribed mass and first moment, because
$$
\int_{-1}^1 g_0(x)\,dx=1,
\qquad
\int_{-1}^1 xg_0(x)\,dx=m.
$$
Moreover,
$$
0\le g_0(x)\le1\quad(-1\le x\le1)
$$
holds exactly when $m\le1/3$.

For $0\le m\le1/3$, every admissible $f$ satisfies
$$
\int_{-1}^1 f(x)g_0(x)\,dx
=\frac12\int f+\frac{3m}{2}\int xf
=\frac{1+3m^2}{2}.
$$
The same value is
$$
\int_{-1}^1 g_0(x)^2\,dx.
$$
Hence
$$
\int f^2-\int g_0^2
=\int(f-g_0)^2\ge0.
$$
Thus in this regime the unique minimizer is $g_0$, and
$$
\min\int_{-1}^1 f(x)^2\,dx
=\frac{1+3m^2}{2}.
$$

Step 2: Reconstruct the two-sided active candidate for $m>1/3$
Assume now
$$
\frac13<m<\frac12.
$$
Set
$$
t=\sqrt{3(1-2m)},
$$
so $0<t<1$, and define
$$
g(x)=
\begin{cases}
0,&-1\le x\le -t,\\[2pt]
\dfrac{x+t}{2t},&-t\le x\le t,\\[6pt]
1,&t\le x\le1.
\end{cases}
$$
Then $g(-x)=1-g(x)$, so
$$
\int_{-1}^1 g(x)\,dx=1.
$$
Also
$$
\begin{aligned}
\int_{-1}^1 xg(x)\,dx
&=\int_{-t}^t x\frac{x+t}{2t}\,dx+\int_t^1x\,dx\\
&=\frac{t^2}{3}+\frac{1-t^2}{2}\\
&=\frac12-\frac{t^2}{6}=m.
\end{aligned}
$$
Thus $g$ is admissible.

Its energy is
$$
\begin{aligned}
\int_{-1}^1g(x)^2\,dx
&=\int_{-t}^t\left(\frac{x+t}{2t}\right)^2dx+\int_t^1 1\,dx\\
&=\frac{2t}{3}+1-t\\
&=1-\frac t3\\
&=1-\sqrt{\frac{1-2m}{3}}.
\end{aligned}
$$

Step 3: Prove optimality with a two-sided affine certificate
Let
$$
\ell(x)=\frac{x+t}{2t}.
$$
Then $g=\ell$ on $[-t,t]$, while
$$
g=0,\ \ell\le0\quad\text{on }[-1,-t],
$$
and
$$
g=1,\ \ell\ge1\quad\text{on }[t,1].
$$
Since $\ell$ is affine and $f,g$ have the same mass and first moment,
$$
\int_{-1}^1\ell(x)(f(x)-g(x))\,dx=0.
$$
Therefore
$$
\int g(f-g)
=\int (g-\ell)(f-g).
$$
On $[-1,-t]$ both factors on the right are nonnegative, on $[-t,t]$ the first factor is zero, and on $[t,1]$ both factors are nonpositive because $0\le f\le1$. Hence
$$
\int g(f-g)\ge0.
$$
Consequently
$$
\int f^2-\int g^2
=\int(f-g)^2+2\int g(f-g)\ge0.
$$
Equality forces $f=g$ almost everywhere, so the minimizer is unique.

Step 4: Include the endpoint and combine the regimes
If $m=1/2$, then for every admissible $f$,
$$
\frac12-\int_{-1}^1xf(x)\,dx
=\int_0^1x(1-f(x))\,dx+\int_{-1}^0(-x)f(x)\,dx\ge0.
$$
Equality forces
$$
f=0\ \text{a.e. on }[-1,0),
\qquad
f=1\ \text{a.e. on }(0,1],
$$
so the minimum energy is $1$. This agrees with
$$
1-\sqrt{\frac{1-2m}{3}}
$$
at $m=1/2$.

Thus
$$
\min\int_{-1}^1f(x)^2\,dx
=
\begin{cases}
\dfrac{1+3m^2}{2},&0\le m\le\dfrac13,\\[6pt]
1-\sqrt{\dfrac{1-2m}{3}},&\dfrac13\le m\le\dfrac12.
\end{cases}
$$
To write this compactly, put $t=\sqrt{3(1-2m)}$. The difference of the second branch and the first is
$$
\left(1-\frac t3\right)-\frac{1+3m^2}{2}
=\frac{(1-t)^3(t+3)}{24}.
$$
Hence the first branch is larger for $m<1/3$, the second is larger for $m>1/3$, and they agree at $m=1/3$.

Final Answer: $\boxed{\max\left\{\frac{1+3m^2}{2},1-\sqrt{\frac{1-2m}{3}}\right\}}$

---

## Answer

$\max\left\{\frac{1+3m^2}{2},1-\sqrt{\frac{1-2m}{3}}\right\}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- convex optimization in $L^2$
- affine moment constraints
- box constraints and active sets
- affine dual certificate
- uniqueness by strict convexity

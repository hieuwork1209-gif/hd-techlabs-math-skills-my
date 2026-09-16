## Steps

Step 1: Solve the unconstrained moment projection
Fix $0\le m<1$, and let $f\in L^2([-1,1])$ satisfy
$$
f\ge0\quad\text{a.e.},\qquad \int_{-1}^1 f(x)\,dx=1,\qquad \int_{-1}^1 x f(x)\,dx=m.
$$
Consider first an affine function
$$
g(x)=\alpha+\beta x.
$$
Imposing the same two moment conditions gives
$$
2\alpha=1,
\qquad
\frac{2}{3}\beta=m,
$$
so
$$
g(x)=\frac{1+3mx}{2}.
$$
This function is nonnegative on $[-1,1]$ exactly when
$$
m\le\frac13.
$$
For such $m$, every admissible $f$ satisfies
$$
\int_{-1}^1 f(x)g(x)\,dx
=\frac12\int f+\frac{3m}{2}\int xf
=\frac{1+3m^2}{2}.
$$
Since $g$ itself has the prescribed moments,
$$
\int_{-1}^1 g(x)^2\,dx=\frac{1+3m^2}{2}.
$$
Therefore
$$
\begin{aligned}
\int f^2-\int g^2
&=\int (f-g)^2+2\int fg-2\int g^2\\
&=\int (f-g)^2\ge0.
\end{aligned}
$$
Thus for $0\le m\le1/3$ the unique minimizer is $g$, and
$$
\min\int_{-1}^1 f(x)^2\,dx=\frac{1+3m^2}{2}.
$$

Step 2: Construct the active-support candidate when $m>1/3$
Now suppose
$$
\frac13<m<1.
$$
Set
$$
a=3m-2,
\qquad
A=\frac{2}{9(1-m)^2},
$$
and define
$$
g(x)=A(x-a)_+,
\qquad
(t)_+=\max\{t,0\}.
$$
Because $a\in(-1,1)$, the support of $g$ is $[a,1]$. Put
$$
L=1-a=3(1-m).
$$
Then
$$
\int_{-1}^1 g(x)\,dx
=A\int_a^1(x-a)\,dx
=A\frac{L^2}{2}=1.
$$
Also
$$
\begin{aligned}
\int_{-1}^1 xg(x)\,dx
&=A\int_a^1 x(x-a)\,dx\\
&=A\left(\frac{aL^2}{2}+\frac{L^3}{3}\right)\\
&=a+\frac{2L}{3}=m.
\end{aligned}
$$
Hence $g$ is admissible.

Step 3: Prove optimality by an affine certificate
Let
$$
\ell(x)=A(x-a).
$$
Then $g=\ell$ on $[a,1]$, while $g=0$ and $\ell\le0$ on $[-1,a]$. For any admissible $f$,
$$
\begin{aligned}
\int fg
&=\int_a^1 f\ell\\
&=\int_{-1}^1 f\ell-\int_{-1}^a f\ell\\
&\ge \int_{-1}^1 f\ell\\
&=A\left(\int xf-a\int f\right)\\
&=A(m-a).
\end{aligned}
$$
For the candidate $g$,
$$
\int g^2=\int g\ell=A(m-a).
$$
Therefore
$$
\begin{aligned}
\int f^2-\int g^2
&=\int(f-g)^2+2\left(\int fg-\int g^2\right)\\
&\ge0.
\end{aligned}
$$
Equality forces $\int(f-g)^2=0$, so the minimizer is unique and equals $g$ almost everywhere.

Step 4: Evaluate and combine the two regimes
Since
$$
m-a=m-(3m-2)=2(1-m),
$$
we obtain in the active regime
$$
\int_{-1}^1 g(x)^2\,dx
=A(m-a)
=\frac{4}{9(1-m)}.
$$
Thus
$$
\min\int_{-1}^1 f(x)^2\,dx
=
\begin{cases}
\dfrac{1+3m^2}{2},&0\le m\le\dfrac13,\\[4pt]
\dfrac{4}{9(1-m)},&\dfrac13\le m<1.
\end{cases}
$$
The difference of the two displayed branches is
$$
\frac{1+3m^2}{2}-\frac4{9(1-m)}
=-\frac{(3m-1)^3}{18(1-m)}.
$$
Hence the first branch is larger for $m<1/3$, the second is larger for $m>1/3$, and they agree at $m=1/3$. Therefore the piecewise expression is exactly their maximum.

Final Answer: $\boxed{\max\left\{\frac{1+3m^2}{2},\frac4{9(1-m)}\right\}}$

---

## Answer

$\max\left\{\frac{1+3m^2}{2},\frac4{9(1-m)}\right\}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- convex optimization in $L^2$
- affine moment constraints
- nonnegativity active set
- dual affine certificate
- uniqueness by strict convexity

## Steps

Step 1: Pass to logarithmic coordinates and derive the weighted-mean hierarchy

Let
$$
g(s)=f(e^s),\qquad a(s)=A(e^s),\qquad b(s)=B(e^s),\qquad c(s)=C(e^s).
$$
Then
$$
a(s)=\frac1s\int_0^s g(u)\,du,
$$
$$
b(s)=\frac2{s^2}\int_0^s(s-u)g(u)\,du,
$$
and
$$
c(s)=\frac3{s^3}\int_0^s(s-u)^2g(u)\,du.
$$
Concavity makes $g$ continuous on $(0,\infty)$, so these functions are differentiable there. Direct differentiation gives
$$
g=a+sa',
$$
$$
sb'=2(a-b),
$$
and
$$
sc'=3(b-c).
$$
Now define
$$
X=2-c,
$$
$$
Y=2-3b+2c,
$$
and
$$
Z=2-3a+3b-c.
$$
The differential identities above become
$$
sX'=Y-X,
$$
$$
sY'=2(Z-Y).
$$
The hypotheses become
$$
Y^2=X^4,
\qquad
Z^2=X^6,
$$
and the normalization gives
$$
X(1)^2=\frac14.
$$

Step 2: Resolve the algebraic signs and use the differential hierarchy

On any interval on which $X\ne0$, continuity gives fixed signs $\varepsilon,\delta\in\{-1,1\}$ such that
$$
Y=\varepsilon X^2,
\qquad
Z=\delta X^3.
$$
From the first differential identity,
$$
sX'=\varepsilon X^2-X=X(\varepsilon X-1).
$$
Differentiating $Y=\varepsilon X^2$ and using this equation gives
$$
sY'=2X^2(X-\varepsilon).
$$
But the second differential identity also gives
$$
sY'=2(\delta X^3-\varepsilon X^2)=2X^2(\delta X-\varepsilon).
$$
Hence $\delta=1$ wherever $X\ne0$.

There are now four local possibilities, according to $X(1)=\pm\frac12$ and $\varepsilon=\pm1$.

If $\varepsilon=1$, then
$$
sX'=X(X-1),
$$
so
$$
\frac{X-1}{X}=Ks.
$$
Thus
$$
X(1)=\frac12\Longrightarrow X(s)=\frac1{1+s},
$$
whereas
$$
X(1)=-\frac12\Longrightarrow X(s)=\frac1{1-3s}.
$$
The latter has a pole at $s=\frac13$, impossible because $C(e^s)$ is finite for every $s>0$.

If $\varepsilon=-1$, then
$$
sX'=-X(X+1),
$$
so
$$
\frac{X}{X+1}=\frac Ks.
$$
Hence
$$
X(1)=\frac12\Longrightarrow X(s)=\frac1{3s-1},
$$
which again has a pole at $s=\frac13$, while
$$
X(1)=-\frac12\Longrightarrow X(s)=-\frac1{1+s}.
$$
Therefore only two global branches remain:
$$
(X,Y,Z)=\left(\frac1{1+s},\frac1{(1+s)^2},\frac1{(1+s)^3}\right),
$$
or
$$
(X,Y,Z)=\left(-\frac1{1+s},-\frac1{(1+s)^2},-\frac1{(1+s)^3}\right).
$$

Step 3: Recover the two candidate functions and use concavity

Put
$$
\alpha=2-a.
$$
From the definitions of $X,Y,Z$,
$$
\alpha=\frac{X+Y+Z}{3}.
$$
Also, since $g=a+sa'$, we have
$$
2-g=\alpha+s\alpha'.
$$

For the first global branch,
$$
Y=X^2,
\qquad
Z=X^3,
\qquad
sX'=X^2-X.
$$
Thus
$$
\alpha=\frac{X+X^2+X^3}{3},
$$
and a direct differentiation gives
$$
\alpha+s\alpha'=X^4.
$$
Hence
$$
g(s)=2-\frac1{(1+s)^4}.
$$
Its second derivative is
$$
g''(s)=-\frac{20}{(1+s)^6}<0.
$$

For the second global branch,
$$
Y=-X^2,
\qquad
Z=X^3,
\qquad
sX'=-X^2-X.
$$
Then
$$
\alpha=\frac{X-X^2+X^3}{3},
$$
and
$$
\alpha+s\alpha'=-X^4.
$$
Therefore
$$
g(s)=2+\frac1{(1+s)^4},
$$
whose second derivative is
$$
g''(s)=\frac{20}{(1+s)^6}>0.
$$
This branch is convex and contradicts the hypothesis. Hence only the first branch is admissible.

Step 4: Return to $x$ and verify the solution

Since $g(s)=f(e^s)$,
$$
f(x)=2-\frac1{(1+\log x)^4}.
$$
For $r=(1+s)^{-1}$, direct integration gives
$$
a(s)=2-\frac{r+r^2+r^3}{3},
$$
$$
b(s)=2-\frac{2r+r^2}{3},
$$
and
$$
c(s)=2-r.
$$
Hence
$$
2-3b+2c=r^2,
$$
$$
2-3a+3b-c=r^3,
$$
and
$$
2-c=r.
$$
Thus both algebraic identities hold. Also $c(1)=\frac32$, so $(C(e)-2)^2=\frac14$. The integrands are bounded near the lower endpoint because $g(s)\to1$ as $s\to0^+$, so all three improper integrals converge.

Final Answer: $\boxed{f(x)=2-\frac1{(1+\log x)^4}}$

---

## Answer

$f(x)=2-\frac1{(1+\log x)^4}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Function or mapping

---

## Solution Concepts

- logarithmic weighted integral means
- differential hierarchy of means
- algebraic sign branches
- global ODE continuation
- concavity branch selection

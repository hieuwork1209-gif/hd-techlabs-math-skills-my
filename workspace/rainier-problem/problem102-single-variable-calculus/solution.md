## Steps

Step 1: Pass to logarithmic time and determine the wave speed

Let
$$
u(t)=g(e^t),\qquad t\in\mathbb R.
$$
Then
$$
u_{tt}+c u_t+u(1-u)=0,
$$
with
$$
u(-\infty)=1,\qquad u(+\infty)=0,\qquad u_t<0,
$$
and
$$
u(0)=\frac14.
$$
The endpoint rates become
$$
\alpha=-\lim_{t\to-\infty}\frac{u_t}{1-u},
\qquad
\beta=-\lim_{t\to+\infty}\frac{u_t}{u},
$$
where $\alpha,\beta>0$ and $\beta=2\alpha$.

Set $v=1-u$ near $-\infty$. Then
$$
v_{tt}+cv_t-v+v^2=0.
$$
Since $v_t/v\to\alpha$,
$$
\frac{v_{tt}}v\to1-c\alpha.
$$
Also
$$
\left(\frac{v_t}{v}\right)'
=\frac{v_{tt}}v-\left(\frac{v_t}{v}\right)^2.
$$
The left-hand ratio converges, so the right-hand side cannot tend to a nonzero constant. Hence
$$
\alpha^2+c\alpha-1=0.
$$
Similarly, from the equation for $u$ at $+\infty$,
$$
\beta^2-c\beta+1=0.
$$
Using $\beta=2\alpha$ gives
$$
\frac1\alpha-\alpha=2\alpha+\frac1{2\alpha},
$$
so
$$
\alpha=\frac1{\sqrt6},
\qquad
\beta=\frac2{\sqrt6},
\qquad
c=\frac5{\sqrt6}.
$$

Step 2: Expose the first-order factorization

Put
$$
a=\frac1{\sqrt6},
\qquad
z(t)=\sqrt{u(t)}.
$$
Then $0<z<1$, $z_t<0$, and the wave equation becomes
$$
2z_t^2+2zz_{tt}+10azz_t+z^2(1-z^2)=0.
$$
Define
$$
r(t)=\frac{z_t}{z}+a(1-z).
$$
Using $a^2=1/6$, direct substitution simplifies the second-order equation to
$$
r_t=-r\bigl(2r+a(1+5z)\bigr).
$$

The rate $\alpha=a$ at $-\infty$ gives
$$
-\frac{z_t}{1-z}\to a,
$$
so $r(t)\to0$ as $t\to-\infty$. The rate $\beta=2a$ likewise gives $r(t)\to0$ as $t\to+\infty$.

We claim that $r\equiv0$. If not, uniqueness for the scalar equation prevents $r$ from crossing zero. For all sufficiently negative $t$, we have $|r|<a/2$ and $a(1+5z)>5a$, hence
$$
\frac{d}{dt}\log|r|
=-\bigl(2r+a(1+5z)\bigr)
<-4a.
$$
Integrating backward would force $|r(t)|$ to grow exponentially as $t\to-\infty$, contradicting $r(t)\to0$. Therefore
$$
r\equiv0.
$$
Thus
$$
z_t=-az(1-z).
$$
Separation gives
$$
z(t)=\frac1{1+Ke^{at}}
$$
for some $K>0$.

Step 3: Fix the translation and return to $x$

Since $u(0)=1/4$, we have $z(0)=1/2$, so $K=1$. Hence
$$
u(t)=\frac1{(1+e^{t/\sqrt6})^2}.
$$
Because $s=e^t$,
$$
g(s)=\frac1{\left(1+s^{1/\sqrt6}\right)^2}.
$$
This profile is strictly decreasing from $1$ to $0$, satisfies $g(1)=1/4$, and its endpoint logarithmic rates are $1/\sqrt6$ and $2/\sqrt6$. Direct differentiation verifies the differential equation with $c=5/\sqrt6$.

Finally $s=\log x$, so
$$
f(x)=\frac1{\left(1+(\log x)^{1/\sqrt6}\right)^2}.
$$

Final Answer: $\boxed{f(x)=\frac1{\left(1+(\log x)^{1/\sqrt6}\right)^2}}$

---

## Answer

$f(x)=\frac1{\left(1+(\log x)^{1/\sqrt6}\right)^2}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Function or mapping

---

## Solution Concepts

- scale-invariant Fisher-KPP wave
- logarithmic traveling-wave coordinate
- endpoint characteristic rates
- nonlinear first-order factorization
- translation normalization

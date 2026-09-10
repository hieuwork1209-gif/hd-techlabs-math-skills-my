## Steps

Step 1: Reduce global stability to positivity of the restoring polynomial
Write
$$
p(x)=x^4+a x^2+b x+1
$$
and
$$
U(x)=\int_0^x s p(s)\,ds
=\frac{x^6}{6}+\frac{a x^4}{4}+\frac{b x^3}{3}+\frac{x^2}{2}.
$$
For the system
$$
\dot x=y,
\qquad
\dot y=-(1+x^2)y-xp(x),
$$
define the mechanical energy
$$
E(x,y)=\frac{y^2}{2}+U(x).
$$
Along every solution,
$$
\dot E
=y\dot y+U'(x)\dot x
=-(1+x^2)y^2\leq0.
$$

Assume first that $p(x)>0$ for every real $x$. Then $xp(x)$ has the sign of $x$, so $U(x)>0$ for $x\neq0$, and $U(x)\to+\infty$ as $|x|\to\infty$. Hence $E$ is positive definite and proper. Every trajectory remains in a compact sublevel set of $E$, so every forward solution is global and bounded. The set where $\dot E=0$ is $y=0$. A trajectory can remain in that set only if also
$$
\dot y=-xp(x)=0,
$$
which, because $p>0$, forces $x=0$. Thus the only invariant subset of $\{\dot E=0\}$ is the origin, and the energy decay implies every trajectory converges to $(0,0)$. Positive definiteness of $E$ gives Lyapunov stability.

Conversely, if $p$ is not strictly positive on $\mathbb R$, then since $p(0)=1$ there is a nonzero real $r$ with $p(r)=0$: this is immediate if $p$ vanishes, while if $p$ is negative somewhere continuity gives a zero between that point and $0$. Then $(r,0)$ is a nonzero equilibrium. Therefore global asymptotic stability is equivalent to
$$
p(x)>0\qquad\text{for all }x\in\mathbb R.
$$

Step 2: Convert quartic positivity into a one-variable minimum
For $t>0$, define
$$
h_a(t)=t^3+a t+\frac1t.
$$
For $x=t>0$,
$$
\frac{p(t)}{t}=h_a(t)+b,
$$
whereas for $x=-t<0$,
$$
\frac{p(-t)}{t}=h_a(t)-b.
$$
Thus $p(x)>0$ for every nonzero real $x$ exactly when
$$
-h_a(t)<b<h_a(t)\qquad\text{for every }t>0.
$$
Equivalently,
$$
|b|<m(a),
\qquad
m(a):=\inf_{t>0}h_a(t),
$$
provided $m(a)>0$.

Step 3: Compute the minimum explicitly
The derivative is
$$
h_a'(t)=3t^2+a-\frac1{t^2}.
$$
Setting $s=t^2>0$, the critical-point equation becomes
$$
3s^2+a s-1=0.
$$
It has exactly one positive root,
$$
s=\frac{\sqrt{a^2+12}-a}{6}.
$$
Since $h_a(t)\to+\infty$ as $t\to0^+$ and as $t\to\infty$, this critical point gives the global minimum. From
$$
a=\frac1s-3s
$$
we obtain
$$
m(a)=h_a(\sqrt s)
=\frac{2(1-s^2)}{\sqrt s}.
$$
The function $a(s)=s^{-1}-3s$ is strictly decreasing for $s>0$, and $a(1)=-2$. Hence
$$
m(a)>0
\quad\Longleftrightarrow\quad
s<1
\quad\Longleftrightarrow\quad
a>-2.
$$
At $a=-2$ the minimum is $0$, while for $a<-2$ it is negative, so no value of $b$ can make $p$ strictly positive.

Step 4: State the exact parameter region
Combining the previous steps, put
$$
s=\frac{\sqrt{a^2+12}-a}{6}.
$$
Then the origin is globally asymptotically stable exactly when
$$
a>-2,
\qquad
|b|<\frac{2(1-s^2)}{\sqrt s}.
$$
Equality is excluded: when $|b|=m(a)$, the quartic $p$ has a nonzero double real root, which produces a nonzero equilibrium $(r,0)$.
Final Answer: $\boxed{\{(a,b):a>-2,\ |b|<2(1-s^2)/\sqrt{s},\ s=(\sqrt{a^2+12}-a)/6\}}$

---

## Answer

$\{(a,b):a>-2,\ |b|<2(1-s^2)/\sqrt{s},\ s=(\sqrt{a^2+12}-a)/6\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- global asymptotic stability
- energy Lyapunov functions
- nonlinear damped oscillators
- positivity of quartic polynomials
- parameter-dependent minimization

---

## Black-Box Audit — no issues found

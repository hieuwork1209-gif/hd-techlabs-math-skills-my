## Steps

Step 1: Control the singular endpoint

Set
$$
g(s)=f(e^s),\qquad s>0.
$$
The differential equation is
$$
g''(s)+\frac5s g'(s)+g(s)^2=0,
$$
or equivalently
$$
\bigl(s^5g'(s)\bigr)'=-s^5g(s)^2.
$$
Since $g(s)\to1$ as $s\to0^+$, the right-hand side is integrable near $0$, so $s^5g'(s)$ has a finite limit there. If that limit were nonzero, then $g'(s)$ would have size comparable to $s^{-5}$ near $0$, contradicting the finite limit of $g$. Hence
$$
\lim_{s\to0^+}s^5g'(s)=0.
$$
Integrating from $0$ to $s$ gives
$$
s^5g'(s)=-\int_0^s t^5g(t)^2\,dt.
$$
Because $g(t)^2\to1$,
$$
g'(s)=-\frac{s}{6}+o(s).
$$

Step 2: Apply the Emden-Fowler transform

Let
$$
t=\log s,
\qquad
u(t)=s^2g(s).
$$
Since $g=u/s^2$, direct differentiation gives
$$
g'(s)=\frac{u_t-2u}{s^3},
$$
and
$$
g''(s)=\frac{u_{tt}-5u_t+6u}{s^4}.
$$
Substitution into the differential equation yields the autonomous equation
$$
u_{tt}-4u+u^2=0.
$$
As $t\to-\infty$, we have $s=e^t\to0^+$, and Step 1 gives
$$
u(t)=e^{2t}g(e^t)\to0,
$$
$$
u_t(t)=2s^2g(s)+s^3g'(s)\to0.
$$

Step 3: Use the conserved energy and linearize it

Multiplying
$$
u_{tt}-4u+u^2=0
$$
by $u_t$ shows that
$$
E=\frac12u_t^2-2u^2+\frac13u^3
$$
is constant. The limits from Step 2 give $E=0$, so
$$
u_t^2=4u^2-\frac23u^3.
$$
Because $f$ is positive, $u$ is positive. Define
$$
v=u^{-1/2}.
$$
Using $u_{tt}=4u-u^2$ together with the energy identity,
$$
v_{tt}
=\frac34u^{-5/2}u_t^2-\frac12u^{-3/2}u_{tt}
=v.
$$
Also,
$$
v_t^2
=\frac14u^{-3}u_t^2
=v^2-\frac16.
$$
Thus
$$
v(t)=Ae^t+Be^{-t}.
$$
Since
$$
e^t v(t)=\frac1{\sqrt{g(e^t)}}\to1
$$
as $t\to-\infty$, we get $B=1$. Moreover,
$$
v^2-v_t^2=\frac16.
$$
For $v=Ae^t+e^{-t}$, the left-hand side equals $4A$, hence
$$
A=\frac1{24}.
$$
Therefore
$$
v(t)=e^{-t}+\frac1{24}e^t.
$$
Since $s=e^t$,
$$
u(t)=\frac1{v(t)^2}
=\frac{s^2}{\left(1+\frac{s^2}{24}\right)^2}.
$$
Recalling that $u=s^2g(s)$,
$$
g(s)=\frac1{\left(1+\frac{s^2}{24}\right)^2}.
$$

Step 4: Return to $x$ and verify

Since $s=\log x$,
$$
f(x)=\frac1{\left(1+\frac{(\log x)^2}{24}\right)^2}.
$$
This function is positive, its logarithmic profile tends to $1$ as $s\to0^+$, and direct differentiation gives
$$
g''(s)+\frac5s g'(s)+g(s)^2=0.
$$
Hence it satisfies all the hypotheses.

Final Answer: $\boxed{f(x)=\frac1{\left(1+\frac{(\log x)^2}{24}\right)^2}}$

---

## Answer

$f(x)=\frac1{\left(1+\frac{(\log x)^2}{24}\right)^2}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Function or mapping

---

## Solution Concepts

- singular Lane-Emden equation
- Emden-Fowler logarithmic transform
- conserved energy
- reciprocal-square-root linearization
- endpoint asymptotics

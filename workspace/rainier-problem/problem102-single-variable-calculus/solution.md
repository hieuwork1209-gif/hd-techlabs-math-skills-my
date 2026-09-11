## Steps

Step 1: Pass to the angular coordinate

Let
$$
g(s)=f(e^s),\qquad s>0,
$$
and set
$$
u=\arctan s,\qquad F(u)=g(\tan u),\qquad 0<u<\frac\pi2.
$$
For a $C^3$ function $H$ with $H'\ne0$, write
$$
\mathcal S(H)=\frac{H'''}{H'}-\frac32\left(\frac{H''}{H'}\right)^2.
$$
A direct differentiation gives the chain rule
$$
\mathcal S(F\circ u)=\bigl(\mathcal S(F)\circ u\bigr)(u')^2+\mathcal S(u).
$$
For $u(s)=\arctan s$,
$$
u'(s)=\frac1{1+s^2}
$$
and
$$
\mathcal S(u)=-\frac2{(1+s^2)^2}.
$$
The differential equation in the problem therefore implies
$$
\mathcal S(F)=0
$$
on $(0,\pi/2)$.

Step 2: Solve the zero-Schwarzian equation

Put
$$
p=\frac{F''}{F'}.
$$
Since $F'>0$, this is well defined, and
$$
\mathcal S(F)=p'-\frac12p^2=0.
$$
If $p\equiv0$, then $F$ is affine. Otherwise, separation gives
$$
p(u)=-\frac2{u+c}
$$
for a constant $c$, and integration gives
$$
F(u)=\frac{Au+B}{Cu+D}
$$
with $AD-BC\ne0$. Thus in every case $F$ is fractional linear.

The endpoint conditions become
$$
F(0)=0,
\qquad
F\!\left(\frac\pi2\right)=1.
$$
Let
$$
a=\frac\pi2,
\qquad
t=\frac ua.
$$
After using the two endpoint conditions, every such fractional-linear map can be written as
$$
F(u)=\frac{(1+k)t}{1+kt}
$$
for some real constant $k$ for which the denominator does not vanish on $[0,1]$.

Step 3: Use the inversion symmetry to eliminate the Möbius freedom

For $s>0$,
$$
\arctan\frac1s=\frac\pi2-\arctan s.
$$
Hence the condition
$$
g(s)+g(1/s)=1
$$
becomes
$$
F(u)+F(a-u)=1.
$$
In terms of $t=u/a$,
$$
\frac{(1+k)t}{1+kt}
+
\frac{(1+k)(1-t)}{1+k(1-t)}
-1
=
\frac{k(k+2)t(t-1)}{(1+kt)(1+k(1-t))}.
$$
This vanishes for every $0<t<1$, so
$$
k=0
\quad\text{or}\quad
k=-2.
$$
The value $k=-2$ is impossible because $1+kt$ vanishes at $t=1/2$, whereas $F$ is finite and $C^3$ throughout the interval. Therefore
$$
k=0,
$$
and hence
$$
F(u)=\frac{u}{a}=\frac2\pi u.
$$
Thus
$$
g(s)=\frac2\pi\arctan s.
$$

Step 4: Return to $x$ and verify

Since $s=\log x$,
$$
f(x)=\frac2\pi\arctan(\log x).
$$
The function $g(s)=\frac2\pi\arctan s$ is strictly increasing, tends to $0$ at $0^+$ and to $1$ at infinity, and satisfies
$$
g(s)+g(1/s)=1
$$
for $s>0$. Multiplication by the nonzero constant $2/\pi$ does not change the Schwarzian derivative, so
$$
\frac{g'''}{g'}-\frac32\left(\frac{g''}{g'}\right)^2
=-\frac2{(1+s^2)^2}.
$$
Hence all hypotheses hold.

Final Answer: $\boxed{f(x)=\frac2\pi\arctan(\log x)}$

---

## Answer

$f(x)=\frac2\pi\arctan(\log x)$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Function or mapping

---

## Solution Concepts

- Schwarzian differential invariant
- angular change of variables
- fractional-linear solution family
- inversion symmetry
- global branch elimination

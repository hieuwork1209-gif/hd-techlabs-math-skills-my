## Steps

Step 1: Encode the two turning points

Let
$$
g(s)=f(e^s),\qquad s>0.
$$
For each $E>0$, let $a(E)\in(0,1)$ and $b(E)>1$ be the unique points such that
$$
g(a(E))=g(b(E))=E.
$$
Because $g'<0$ on $(0,1)$ and $g'>0$ on $(1,\infty)$, the inverse branches $a,b$ are $C^1$ for $E>0$. Split the period integral at $s=1$ and use $u=g(s)$ on each branch. This gives
$$
\pi
=
\int_0^E\frac{b'(u)-a'(u)}{\sqrt{E-u}}\,du.
$$
Define the turning-point width
$$
W(E)=b(E)-a(E).
$$
Then
$$
\pi=\int_0^E\frac{W'(u)}{\sqrt{E-u}}\,du.
$$
Also $W(E)\to0$ as $E\to0^+$ because both turning points tend to the unique minimum point $s=1$.

Step 2: Invert the Abel relation without using an external theorem

Fix $R>0$. Multiply the last identity by $(R-E)^{-1/2}$ and integrate from $E=0$ to $E=R$. Since the integrands are nonnegative after splitting into the two monotone branches, the order of integration may be reversed. We obtain
$$
\int_0^R\frac{\pi}{\sqrt{R-E}}\,dE
=
\int_0^R W'(u)
\left(
\int_u^R\frac{dE}{\sqrt{E-u}\sqrt{R-E}}
\right)du.
$$
The inner integral equals $\pi$ by the substitution
$$
E=u+(R-u)t.
$$
Hence
$$
2\pi\sqrt R
=
\pi\int_0^R W'(u)\,du
=
\pi W(R),
$$
so
$$
W(E)=2\sqrt E.
$$
Thus the isochronous condition determines the separation of the two turning points.

Step 3: Use inversion symmetry to determine the well

The symmetry
$$
g(s)=g(1/s)
$$
forces the two points on the same positive level to satisfy
$$
a(E)b(E)=1.
$$
Together with
$$
b(E)-a(E)=2\sqrt E,
$$
this gives
$$
b(E)-\frac1{b(E)}=2\sqrt E.
$$
Since $b(E)>1$,
$$
b(E)=\sqrt{1+E}+\sqrt E,
$$
and consequently
$$
a(E)=\sqrt{1+E}-\sqrt E.
$$
Now let $s>1$ and put $E=g(s)$. Since $s=b(E)$,
$$
s-\frac1s=2\sqrt{g(s)},
$$
so
$$
g(s)=\frac14\left(s-\frac1s\right)^2.
$$
For $0<s<1$, the same formula follows from $g(s)=g(1/s)$, and it also gives $g(1)=0$.

Step 4: Verify the period and return to $x$

For
$$
g(s)=\frac14\left(s-\frac1s\right)^2,
$$
set
$$
y=\frac12\left(s-\frac1s\right).
$$
This is strictly increasing on $(0,\infty)$ and satisfies $g(s)=y^2$. Solving for $s$ gives
$$
s=y+\sqrt{1+y^2},
$$
so
$$
\frac{ds}{dy}=1+\frac{y}{\sqrt{1+y^2}}.
$$
At energy $E$, the turning points correspond to $y=\pm\sqrt E$. Therefore
$$
\int_{a(E)}^{b(E)}\frac{ds}{\sqrt{E-g(s)}}
=
\int_{-\sqrt E}^{\sqrt E}
\frac{1+\frac{y}{\sqrt{1+y^2}}}{\sqrt{E-y^2}}\,dy.
$$
The second term is odd, while the first integrates to $\pi$. Hence the required period condition holds.

Since $s=\log x$,
$$
f(x)=\frac14\left(\log x-\frac1{\log x}\right)^2.
$$

Final Answer: $\boxed{f(x)=\frac14\left(\log x-\frac1{\log x}\right)^2}$

---

## Answer

$f(x)=\frac14\left(\log x-\frac1{\log x}\right)^2$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Function or mapping

---

## Solution Concepts

- isochronous turning-point integral
- Abel inversion by double integration
- inversion symmetry of the potential well
- recovery from level-set width
- logarithmic change of variables

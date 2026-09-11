## Steps

Step 1: Compactify the half-line

Let
$$
g(s)=f(e^s),\qquad s>0.
$$
The differential equation is
$$
\bigl(sg'(s)\bigr)'+\frac{\lambda}{(1+s)^2}g(s)=0.
$$
Set
$$
z=\frac{s-1}{s+1},\qquad y(z)=g\!\left(\frac{1+z}{1-z}\right).
$$
Then $s\in(0,\infty)$ corresponds monotonically to $z\in(-1,1)$. A direct differentiation gives
$$
(1-z^2)y''(z)-2zy'(z)+\lambda y(z)=0,
$$
or
$$
\bigl((1-z^2)y'(z)\bigr)'+\lambda y(z)=0.
$$
The endpoint assumptions say that $y$ extends continuously to $[-1,1]$, with
$$
y(-1)=1.
$$

Step 2: Quantize the parameter by endpoint regularity

Put
$$
F(z)=(1-z^2)y'(z).
$$
Since $F'=-\lambda y$ and $y$ is bounded, $F$ has finite limits at both endpoints. If $F(-1)\ne0$, then $y'(z)$ has a nonzero multiple of $(z+1)^{-1}$ as its leading behavior, forcing a logarithmic divergence of $y$. Thus $F(-1)=0$. The same argument at $z=1$ gives
$$
\lim_{z\to\pm1}(1-z^2)y'(z)=0.
$$

For each integer $n\ge0$, let $P_n$ be the Legendre polynomial
$$
P_n(z)=\frac1{2^n n!}\frac{d^n}{dz^n}(z^2-1)^n.
$$
It satisfies
$$
\bigl((1-z^2)P_n'(z)\bigr)'+n(n+1)P_n(z)=0.
$$
Multiply the equation for $y$ by $P_n$, the equation for $P_n$ by $y$, subtract, and integrate over $(-1,1)$. The boundary term vanishes because $y$ is bounded, $(1-z^2)y'\to0$, and $P_n,P_n'$ are finite. Therefore
$$
\bigl(\lambda-n(n+1)\bigr)
\int_{-1}^1 y(z)P_n(z)\,dz=0.
$$

Suppose that $\lambda\ne n(n+1)$ for every $n\ge0$. Then $y$ is orthogonal to every $P_n$, hence to every polynomial because $P_0,\ldots,P_m$ span the polynomials of degree at most $m$. By the Weierstrass approximation theorem, there are polynomials $q_m$ converging uniformly to the continuous function $y$ on $[-1,1]$. Thus
$$
0=\lim_{m\to\infty}\int_{-1}^1 y(z)q_m(z)\,dz
=\int_{-1}^1 y(z)^2\,dz,
$$
which would give $y\equiv0$, contradicting $y(-1)=1$. Hence
$$
\lambda=n(n+1)
$$
for some integer $n\ge0$.

For this $n$, the same Lagrange identity applied to $y$ and $P_n$ shows that
$$
(1-z^2)\bigl(y'P_n-yP_n'\bigr)
$$
is constant. Its limit at $z=-1$ is zero, so the constant is zero. Therefore $y$ is a constant multiple of $P_n$ on $(-1,1)$.

Step 3: Use the zero count to determine the degree

The Rodrigues formula gives, by $n$ integrations by parts,
$$
\int_{-1}^1 P_n(z)q(z)\,dz=0
$$
for every polynomial $q$ of degree less than $n$. Every interior zero of $P_n$ is simple, because a solution of a second-order linear ODE whose value and derivative vanish at one interior point is identically zero.

If $P_n$ had fewer than $n$ zeros in $(-1,1)$, let $q$ be the product of its distinct zero factors. Then $\deg q<n$ and $P_nq$ has one fixed sign and is not identically zero, contradicting the orthogonality above. Hence $P_n$ has exactly $n$ zeros in $(-1,1)$.

The map $s\mapsto z=(s-1)/(s+1)$ preserves the number of zeros. Since $g$ has exactly two zeros on $(0,\infty)$,
$$
n=2,
\qquad
\lambda=6.
$$

Step 4: Normalize and return to $x$

Now
$$
P_2(z)=\frac12(3z^2-1),
$$
and $P_2(-1)=1$. Since $y(-1)=1$,
$$
y(z)=P_2(z).
$$
Therefore
$$
g(s)
=P_2\!\left(\frac{s-1}{s+1}\right)
=\frac{s^2-4s+1}{(1+s)^2}.
$$
Its two positive zeros are $2-\sqrt3$ and $2+\sqrt3$, and $g(s)\to1$ as $s\to\infty$, so the endpoint and zero-count conditions hold.

Since $s=\log x$,
$$
f(x)=\frac{(\log x)^2-4\log x+1}{(1+\log x)^2}.
$$

Final Answer: $\boxed{f(x)=\frac{(\log x)^2-4\log x+1}{(1+\log x)^2}}$

---

## Answer

$f(x)=\frac{(\log x)^2-4\log x+1}{(1+\log x)^2}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Function or mapping

---

## Solution Concepts

- compactification of the half-line
- singular Sturm-Liouville equation
- Legendre spectral quantization
- polynomial density and orthogonality
- zero count of orthogonal polynomials

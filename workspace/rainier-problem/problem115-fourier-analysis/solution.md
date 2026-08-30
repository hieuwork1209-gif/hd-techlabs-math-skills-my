## Steps

Step 1: Reduce the nonlinear identity to modulus data for the positive-frequency part

Set
$$
F(x)=\sum_{k=1}^4\widehat f(k)e^{ikx}.
$$
Because $f$ is real and $\widehat f(0)=0$,
$$
f=F+\overline F,
\qquad
Hf=-iF+i\overline F.
$$
Hence
$$
f^2=F^2+2|F|^2+\overline F^{\,2},
$$
and, since $F^2$ and $\overline F^{\,2}$ contain only positive and negative frequencies respectively,
$$
H(f^2)=-iF^2+i\overline F^{\,2}+2H(|F|^2).
$$
Also
$$
fHf=(F+\overline F)(-iF+i\overline F)
=-iF^2+i\overline F^{\,2}.
$$
Therefore
$$
H(f^2)-fHf=2H(|F|^2).
$$
The hypothesis becomes
$$
2H(|F|^2)
=\frac{-1250\sin x+331\sin(2x)-30\sin(3x)}{981}.
$$

Step 2: Recover $|F|^2$ completely

With the stated convention, $H(\cos kx)=\sin kx$ for $k>0$. Thus the preceding identity determines every nonzero Fourier mode of $|F|^2$:
$$
|F(x)|^2=C+\frac{-2500\cos x+662\cos(2x)-60\cos(3x)}{3924}
$$
for some constant $C$.

Averaging
$$
f^2=F^2+2|F|^2+\overline F^{\,2}
$$
over one period kills $F^2$ and $\overline F^{\,2}$. Since the mean of $f^2$ is $1$,
$$
2C=1,
\qquad C=\frac12.
$$
Hence
$$
|F(x)|^2
=\frac{1962-2500\cos x+662\cos(2x)-60\cos(3x)}{3924}.
$$

Step 3: Convert the recovered modulus into a finite spectral-factor problem

Put $z=e^{ix}$ and define
$$
A(z)=2\sqrt{981}\,F(x).
$$
Then $A$ is a polynomial involving only $z,z^2,z^3,z^4$, and
$$
|A(z)|^2
=1962-2500\cos x+662\cos(2x)-60\cos(3x)
\qquad(|z|=1).
$$
A direct expansion gives the factorization
$$
1962-2500\cos x+662\cos(2x)-60\cos(3x)
=|(z-2)(z-3)(z-5)|^2.
$$
The nonzero frequency-$3$ term shows that the smallest and largest exponents occurring in $A$ differ by $3$. Because $A$ has no constant term and degree at most $4$, those exponents must be $1$ and $4$. Thus
$$
A(z)=zB(z)
$$
with $B$ a cubic having nonzero constant and leading coefficients, and
$$
|B(z)|=|(z-2)(z-3)(z-5)|
\qquad(|z|=1).
$$

Let
$$
B^*(z)=z^3\overline{B(1/\overline z)}.
$$
Equality of the boundary moduli implies the polynomial identity
$$
B(z)B^*(z)=Q(z)Q^*(z),
\qquad
Q(z)=(z-2)(z-3)(z-5).
$$
The six zeros on the right are
$$
2,\ 3,\ 5,\ \frac12,\ \frac13,\ \frac15,
$$
all simple. Since zeros of $B^*$ are reciprocal conjugates of zeros of $B$, a cubic spectral factor $B$ must choose exactly one zero from each reciprocal pair
$$
\left\{2,\frac12\right\},
\quad
\left\{3,\frac13\right\},
\quad
\left\{5,\frac15\right\}.
$$
Thus there are $2^3$ root-choice patterns before fixing the unimodular phase.

Step 4: Use $f(0)$ to fix the phase of every spectral factor

From $A=2\sqrt{981}F$ and $f=F+\overline F$,
$$
f(x)=\frac{\operatorname{Re}A(e^{ix})}{\sqrt{981}}.
$$
At $x=0$, the recovered modulus gives $|A(1)|=8$, while the condition $f(0)=8/\sqrt{981}$ gives $\operatorname{Re}A(1)=8$. Hence
$$
A(1)=B(1)=8.
$$
This fixes the unimodular phase uniquely for each root-choice pattern.

A convenient normalized list is
$$
B_S(z)=\prod_{r\in S}(r-z)\prod_{r\in\{2,3,5\}\setminus S}(rz-1),
\qquad S\subseteq\{2,3,5\},
$$
because each factor has the required boundary modulus and every $B_S(1)=8$.

Step 5: Use the second point value to select the unique spectral factor

At $x=\pi/2$ we have $z=i$ and $A(i)=iB(i)$. Therefore
$$
f\!\left(\frac\pi2\right)=-\frac{36}{\sqrt{981}}
$$
is equivalent to
$$
\operatorname{Re}(iB(i))=-36,
\qquad\text{or equivalently}\qquad
\operatorname{Im}B(i)=36.
$$
For the eight normalized factors $B_S$, the values of $\operatorname{Im}B_S(i)$ are
$$
-20,-20,-12,36,-2,34,30,-30,
$$
corresponding respectively to
$$
S=\varnothing,\{5\},\{3\},\{3,5\},\{2\},\{2,5\},\{2,3\},\{2,3,5\}.
$$
Thus the unique choice is
$$
S=\{3,5\}.
$$
Hence
$$
B(z)=(2z-1)(3-z)(5-z)=2z^3-17z^2+38z-15,
$$
so
$$
A(z)=2z^4-17z^3+38z^2-15z.
$$
Consequently
$$
f(x)=\frac{-15\cos x+38\cos(2x)-17\cos(3x)+2\cos(4x)}{\sqrt{981}}.
$$
The squared coefficient sum is
$$
15^2+38^2+17^2+2^2=1962,
$$
so the mean of $f^2$ is $1962/(2\cdot981)=1$. The factorization above gives exactly the recovered $|F|^2$, so Step 1 verifies the nonlinear Hilbert-transform identity, and the two point values are immediate from the displayed formula.

Final Answer: $\boxed{f(x)=\frac{-15\cos x+38\cos(2x)-17\cos(3x)+2\cos(4x)}{\sqrt{981}}}$

---

## Answer

$f(x)=\frac{-15\cos x+38\cos(2x)-17\cos(3x)+2\cos(4x)}{\sqrt{981}}$

---

## Classification

**Problem Type:** Construction under constraints

**Answer Type:** Function or mapping

---

## Solution Concepts

- periodic Hilbert transform as a Fourier multiplier
- positive-frequency analytic signal
- finite spectral factorization
- reciprocal-polynomial root pairing
- phase selection from point constraints

---

## Black-Box Audit — no issues found

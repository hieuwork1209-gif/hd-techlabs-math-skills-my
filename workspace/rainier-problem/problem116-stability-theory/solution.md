## Steps

Step 1: Bound possible unstable characteristic roots
Consider
$$
\ddot x(t)+x(t)+\frac12\dot x(t-\tau)=0,
\qquad \tau>0,
$$
with characteristic equation
$$
F(\lambda,\tau):=\lambda^2+1+\frac\lambda2e^{-\lambda\tau}=0.
$$
If $\operatorname{Re}\lambda\ge0$ and $F(\lambda,\tau)=0$, then
$$
|\lambda^2+1|=\frac{|\lambda|}{2}e^{-\tau\operatorname{Re}\lambda}\le\frac{|\lambda|}{2}.
$$
Hence
$$
|\lambda|^2-1\le\frac{|\lambda|}{2},
$$
so every root in the closed right half-plane satisfies
$$
|\lambda|\le\frac{1+\sqrt{17}}4.
$$
Thus the right-half-plane root count can change only through imaginary-axis crossings. At $\tau=0$,
$$
F(\lambda,0)=\lambda^2+\frac12\lambda+1,
$$
whose roots have negative real part. Since the above bound is uniform and $F(\cdot,\tau)\to F(\cdot,0)$ uniformly on the bounded right-half-plane region, there are no unstable roots for all sufficiently small positive $\tau$.

Step 2: Find the two crossing families
Let $\lambda=i\omega$ with $\omega>0$ and put $\theta=\omega\tau$. Then
$$
1-\omega^2+\frac{i\omega}{2}e^{-i\theta}=0.
$$
Separating real and imaginary parts gives
$$
1-\omega^2+\frac\omega2\sin\theta=0,
\qquad
\cos\theta=0.
$$
If $\sin\theta=1$, then
$$
\omega_+=\frac{1+\sqrt{17}}4,
\qquad
\theta=\frac\pi2+2\pi k,
$$
so the crossing delays are
$$
D_k=\frac{(4k+1)\pi(\sqrt{17}-1)}8,
\qquad k=0,1,2,\dots.
$$
If $\sin\theta=-1$, then
$$
\omega_- =\frac{\sqrt{17}-1}4,
\qquad
\theta=\frac{3\pi}{2}+2\pi k,
$$
so
$$
S_k=\frac{(4k+3)\pi(\sqrt{17}+1)}8,
\qquad k=0,1,2,\dots.
$$
These are all imaginary-axis crossings; $F(0,\tau)=1$, so zero is never a characteristic root.

Step 3: Determine crossing directions and count roots
Implicit differentiation gives
$$
\frac{d\lambda}{d\tau}=-\frac{F_\tau}{F_\lambda}.
$$
At an imaginary crossing,
$$
\operatorname{Re}\left(\frac{d\lambda}{d\tau}\right)^{-1}
=\frac{4\omega\sin\theta-1}{\omega^2}.
$$
The real part of a nonzero complex number and that of its reciprocal have the same sign. Therefore each $D_k$ crossing has positive direction because
$$
4\omega_+-1=\sqrt{17}>0,
$$
while each $S_k$ crossing has negative direction because
$$
-4\omega_- -1=-\sqrt{17}<0.
$$
Thus every $D_k$ sends one conjugate pair from left to right, and every $S_k$ sends one pair from right to left.

Now
$$
D_0<S_0<D_1
$$
because $\sqrt{17}>4$. Hence the root count is $0$ on $(0,D_0)$, then $2$ on $(D_0,S_0)$, then returns to $0$ on $(S_0,D_1)$.

For every $k\ge1$,
$$
D_{k+1}<S_k,
$$
because this inequality is equivalent to $\sqrt{17}<4k+4$. Hence after $D_1$ each later stabilizing crossing is preceded by at least one additional destabilizing crossing, so the right-half-plane root count never returns to zero.

Step 4: State the exact stability set
Exponential stability also fails at every crossing delay itself because a conjugate pair lies on the imaginary axis. Therefore the characteristic roots all have negative real part exactly for
$$
0<\tau<\frac{\pi(\sqrt{17}-1)}8
$$
or
$$
\frac{3\pi(\sqrt{17}+1)}8<\tau<\frac{5\pi(\sqrt{17}-1)}8.
$$
Final Answer: $\boxed{(0,\frac{\pi(\sqrt{17}-1)}8)\cup(\frac{3\pi(\sqrt{17}+1)}8,\frac{5\pi(\sqrt{17}-1)}8)}$

---

## Answer

$(0,\frac{\pi(\sqrt{17}-1)}8)\cup(\frac{3\pi(\sqrt{17}+1)}8,\frac{5\pi(\sqrt{17}-1)}8)$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- delayed damping oscillators
- characteristic root counting
- multiple Hopf crossing frequencies
- crossing direction
- delay-induced stability switches

---

## Black-Box Audit — no issues found

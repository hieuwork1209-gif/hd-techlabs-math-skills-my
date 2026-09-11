## Steps

Step 1: Write the characteristic equation and localize possible unstable roots
Consider
$$
\dot x(t)+\frac12\dot x(t-\tau)+\frac32x(t-\tau)=0,
\qquad \tau>0.
$$
Its characteristic equation is
$$
F(\lambda,\tau)
:=\lambda+\left(\frac\lambda2+\frac32\right)e^{-\lambda\tau}=0.
$$
At $\tau=0$ this reduces to
$$
\frac32\lambda+\frac32=0,
$$
so the only finite characteristic root is $\lambda=-1$.

If $\operatorname{Re}\lambda\ge0$ and $F(\lambda,\tau)=0$, then
$$
\lambda\left(1+\frac12e^{-\lambda\tau}\right)
=-\frac32e^{-\lambda\tau}.
$$
Because $|e^{-\lambda\tau}|\le1$,
$$
\left|1+\frac12e^{-\lambda\tau}\right|\ge\frac12,
$$
and hence $|\lambda|\le3$. Thus all roots in the closed right half-plane remain in a fixed compact disk. Consequently their number can change as $\tau$ varies only when a characteristic root crosses the imaginary axis.

Step 2: Find every imaginary-axis crossing
Let $\lambda=i\omega$ with $\omega\in\mathbb R$. Since $F(0,\tau)=3/2$, we have $\omega\ne0$. Taking absolute values in
$$
i\omega=-\left(\frac{i\omega}{2}+\frac32\right)e^{-i\omega\tau}
$$
gives
$$
\omega^2=\frac{\omega^2+9}{4},
$$
so
$$
\omega^2=3.
$$
For the positive frequency $\omega=\sqrt3$,
$$
e^{-i\sqrt3\tau}
=-\frac{i\sqrt3}{\frac32+\frac{i\sqrt3}{2}}
=e^{-2\pi i/3}.
$$
Therefore all positive crossing delays are
$$
\tau_k
=\frac{\frac{2\pi}{3}+2\pi k}{\sqrt3}
=\frac{2\pi(3k+1)}{3\sqrt3},
\qquad k=0,1,2,\dots.
$$
The conjugate root $-i\sqrt3$ crosses at the same delays.

Step 3: Determine the crossing direction
Implicit differentiation of $F(\lambda,\tau)=0$ gives
$$
\frac{d\lambda}{d\tau}=-\frac{F_\tau}{F_\lambda}.
$$
At a crossing point $\lambda=i\sqrt3$, using the characteristic equation to simplify the exponential factor yields
$$
\operatorname{Re}\frac{d\lambda}{d\tau}
=\frac{3}{3\tau_k^2+(\tau_k-1)^2}>0.
$$
Thus at every $\tau_k$ one simple conjugate pair crosses from the left half-plane into the right half-plane as $\tau$ increases.

Since there are no right-half-plane roots at $\tau=0$, and Step 1 prevents roots from appearing from infinity, the open right-half-plane root count is constant between successive $\tau_k$ and increases by $2$ after each crossing.

Step 4: Count exactly four unstable characteristic roots
The first three crossing delays are
$$
\tau_0=\frac{2\pi}{3\sqrt3},
\qquad
\tau_1=\frac{8\pi}{3\sqrt3},
\qquad
\tau_2=\frac{14\pi}{3\sqrt3}.
$$
For $\tau_1<\tau<\tau_2$, exactly the pairs born at $\tau_0$ and $\tau_1$ lie in the open right half-plane, so there are exactly four roots there. At $\tau=\tau_2$, the third pair is still on the imaginary axis and is not counted, so the number of roots with positive real part is still four. At $\tau=\tau_1$, only the first pair has positive real part, so the lower endpoint is excluded.

Hence the required delay interval is
$$
\frac{8\pi}{3\sqrt3}<\tau\le\frac{14\pi}{3\sqrt3}.
$$
Final Answer: $\boxed{\left(\frac{8\pi}{3\sqrt3},\frac{14\pi}{3\sqrt3}\right]}$

---

## Answer

$\left(\frac{8\pi}{3\sqrt3},\frac{14\pi}{3\sqrt3}\right]$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- neutral delay differential equations
- characteristic root counting
- imaginary-axis crossings
- implicit root differentiation
- spectral stability

---

## Black-Box Audit — no issues found

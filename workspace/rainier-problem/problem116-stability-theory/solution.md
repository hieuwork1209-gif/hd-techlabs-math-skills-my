## Steps

Step 1: Localize the unstable characteristic roots
Consider
$$
\dot x(t)+x(t)+2x(t-\tau)+2x(t-2\tau)=0,
\qquad \tau>0.
$$
Its characteristic equation is
$$
F(\lambda,\tau)=\lambda+1+2e^{-\lambda\tau}+2e^{-2\lambda\tau}=0.
$$
If $\operatorname{Re}\lambda\ge0$, then at a root
$$
|\lambda+1|\le2|e^{-\lambda\tau}|+2|e^{-2\lambda\tau}|\le4,
$$
so all closed-right-half-plane roots lie in a fixed compact disk. At $\tau=0$,
$$
F(\lambda,0)=\lambda+5,
$$
which has no root with nonnegative real part. Hence for small positive $\tau$ the open right-half-plane root count is zero, and that count can change only at imaginary-axis crossings.

Step 2: Find all imaginary-axis crossings
Let $\lambda=i\omega$ with $\omega>0$, and put $\theta=\omega\tau$. Separating real and imaginary parts gives
$$
1+2\cos\theta+2\cos2\theta=0,
$$
$$
\omega=2\sin\theta+2\sin2\theta.
$$
Writing $c=\cos\theta$, the first equation becomes
$$
4c^2+2c-1=0,
$$
so
$$
c_+=\frac{\sqrt5-1}{4}=\cos\frac{2\pi}{5},
\qquad
c_-=-\frac{\sqrt5+1}{4}=\cos\frac{4\pi}{5}.
$$
For $c_+$, positivity of $\omega$ selects
$$
\theta=\frac{2\pi}{5}+2\pi k,
\qquad
\omega_+=\sqrt{5+2\sqrt5}.
$$
For $c_-$, positivity of $\omega$ selects the lower-half-circle branch
$$
\theta=\frac{6\pi}{5}+2\pi k,
\qquad
\omega_- =\sqrt{5-2\sqrt5}.
$$
Thus the two crossing families are
$$
A_k=\frac{2\pi(5k+1)}{5\omega_+},
\qquad
B_k=\frac{2\pi(5k+3)}{5\omega_-},
\qquad k=0,1,2,\dots.
$$
Also
$$
\frac{\omega_+}{\omega_-}=2+\sqrt5,
$$
so the two crossing families never coincide.

Step 3: Determine every crossing direction
Write $z=e^{-i\theta}$. At a crossing,
$$
F_\tau=-2\lambda z(1+2z),
\qquad
F_\lambda=1-2\tau z-4\tau z^2.
$$
Since $F_\lambda=1+(\tau/\lambda)F_\tau$,
$$
\left(\frac{d\lambda}{d\tau}\right)^{-1}
=-\frac{F_\lambda}{F_\tau}
=-\frac1{F_\tau}-\frac\tau\lambda.
$$
For $\lambda=i\omega$, the second term is purely imaginary. If $c=\cos\theta$ and $s=\sin\theta$, direct rationalization gives
$$
\operatorname{Re}\left(-\frac1{F_\tau}\right)
=\frac{s(4c+1)}{2\omega(5+4c)}.
$$
On the $A_k$ family, $s>0$ and $4c_++1=\sqrt5>0$. On the $B_k$ family, $s<0$ and $4c_-+1=-\sqrt5<0$. Therefore every crossing has positive direction: at each $A_k$ or $B_k$, one simple conjugate pair moves from the left half-plane into the right half-plane as $\tau$ increases.

Step 4: Order the first crossings and count eight roots
The relevant first crossings are
$$
A_0=\frac{2\pi}{5\omega_+},\quad
A_1=\frac{12\pi}{5\omega_+},\quad
A_2=\frac{22\pi}{5\omega_+},\quad
B_0=\frac{6\pi}{5\omega_-},\quad
A_3=\frac{32\pi}{5\omega_+}.
$$
Using $\omega_+/\omega_-=2+\sqrt5$,
$$
A_2<B_0<A_3
$$
because
$$
11<3(2+\sqrt5)<16.
$$
Hence the first five crossing events are
$$
A_0<A_1<A_2<B_0<A_3.
$$
Starting from zero unstable roots, each event adds two. Thus immediately after $B_0$ there are exactly eight roots in the open right half-plane. At $A_3$ the fifth conjugate pair is still on the imaginary axis, so it is not counted and the open right-half-plane count is still eight there. Therefore
$$
B_0<\tau\le A_3.
$$
Substituting the exact frequencies gives the required interval.
Final Answer: $\boxed{\left(\frac{6\pi}{5\sqrt{5-2\sqrt5}},\frac{32\pi}{5\sqrt{5+2\sqrt5}}\right]}$

---

## Answer

$\left(\frac{6\pi}{5\sqrt{5-2\sqrt5}},\frac{32\pi}{5\sqrt{5+2\sqrt5}}\right]$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- retarded delay differential equations
- characteristic root counting
- commensurate delays
- imaginary-axis crossings
- crossing direction

---

## Black-Box Audit — no issues found

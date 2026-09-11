## Steps

Step 1: Reduce stability to the characteristic roots
Consider
$$
\dot x(t)=-x(t)-a\,x(t-b),
\qquad a>0,\ b>0,
$$
with a continuous initial history on $[-b,0]$. An exponential mode $x(t)=e^{\lambda t}$ gives the characteristic equation
$$
\Delta(\lambda;b):=\lambda+1+a e^{-b\lambda}=0.
$$
For this scalar retarded linear equation, the zero solution is exponentially asymptotically stable exactly when every zero of $\Delta$ has negative real part. Indeed, a characteristic root with nonnegative real part produces a nondecaying real solution from the real or imaginary part of $e^{\lambda t}$. Conversely, if all characteristic roots lie in a half-plane $\operatorname{Re}\lambda\le-\eta<0$, the Laplace transform of the fundamental solution has denominator $\Delta$ and shifting the inversion contour to $\operatorname{Re}\lambda=-\eta/2$ gives exponential decay for every continuous history. Because the equation is linear, exponential stability is global and implies Lyapunov stability in the history sup norm.

For later continuation in $b$, note that every characteristic root with $\operatorname{Re}\lambda\ge0$ satisfies
$$
|\lambda+1|=a e^{-b\operatorname{Re}\lambda}\le a.
$$
Thus all roots in the closed right half-plane lie in the fixed compact disk $|\lambda+1|\le a$; they cannot enter from infinity as $b$ varies.

Step 2: Find every imaginary-axis crossing
A zero root is impossible because
$$
\Delta(0;b)=1+a>0.
$$
Let $\lambda=i\omega$ with $\omega>0$. Separating real and imaginary parts gives
$$
1+a\cos(b\omega)=0,
\qquad
\omega-a\sin(b\omega)=0.
$$
If $0<a\le1$, the first equation would require $\cos(b\omega)=-1/a\le-1$. For $a<1$ this is impossible; for $a=1$ it forces $\cos(b\omega)=-1$ and hence $\sin(b\omega)=0$, contradicting $\omega>0$. Therefore there are no imaginary-axis roots for any $b>0$ when $0<a\le1$.

Now assume $a>1$. Put
$$
\theta=\arccos\left(-\frac1a\right)\in\left(\frac\pi2,\pi\right),
\qquad
\omega_0=\sqrt{a^2-1}.
$$
The two equations above imply
$$
\sin(b\omega)>0,
\qquad
\omega^2=a^2-1=\omega_0^2.
$$
Hence all positive-frequency crossings are
$$
\omega=\omega_0,
\qquad
b=b_k:=\frac{\theta+2\pi k}{\omega_0},
\qquad k=0,1,2,\ldots
$$
The first possible crossing therefore occurs at
$$
b_0=\frac{\arccos(-1/a)}{\sqrt{a^2-1}}.
$$

Step 3: Determine the crossing direction and the stable side
At $b=0$ the delay equation reduces to
$$
\dot x=-(1+a)x,
$$
so the zero solution is exponentially stable. Since right-half-plane roots stay in a fixed compact set, the argument principle shows that their number can change with $b$ only when a root crosses the imaginary axis.

Differentiate $\Delta(\lambda(b);b)=0$ with respect to $b$:
$$
\frac{d\lambda}{db}
=\frac{a\lambda e^{-b\lambda}}{1-ab e^{-b\lambda}}.
$$
At an imaginary crossing $\lambda=i\omega_0$, the characteristic equation gives
$$
a e^{-ib\omega_0}=-(1+i\omega_0).
$$
Therefore
$$
\frac{d\lambda}{db}
=\frac{\omega_0^2-i\omega_0}{1+b+i b\omega_0},
$$
and hence
$$
\operatorname{Re}\frac{d\lambda}{db}
=\frac{\omega_0^2}{(1+b)^2+b^2\omega_0^2}>0.
$$
Every conjugate pair therefore crosses from the left half-plane to the right half-plane as $b$ increases.

Consequently, if $0<a\le1$, no crossing ever occurs and the equation is stable for every $b>0$. If $a>1$, it is stable precisely before the first crossing, namely for $0<b<b_0$. At $b=b_0$ there is a purely imaginary conjugate pair, and for $b>b_0$ at least one conjugate pair lies in the open right half-plane, so asymptotic stability fails.

Step 4: State the exact parameter region
Combining the two cases, the zero solution is globally asymptotically stable exactly for
$$
\{(a,b):0<a\le1,\ b>0\}
\cup
\left\{(a,b):a>1,\ 0<b<\frac{\arccos(-1/a)}{\sqrt{a^2-1}}\right\}.
$$
Final Answer: $\boxed{\{(a,b):0<a\le1,b>0\}\cup\{(a,b):a>1,0<b<\arccos(-1/a)/\sqrt{a^2-1}\}}$

---

## Answer

$\{(a,b):0<a\le1,b>0\}\cup\{(a,b):a>1,0<b<\arccos(-1/a)/\sqrt{a^2-1}\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- delay differential equations
- characteristic roots
- spectral stability
- imaginary-axis crossings
- transversality

---

## Black-Box Audit — no issues found

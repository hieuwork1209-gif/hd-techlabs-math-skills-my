## Steps

Step 1: Identify when the deterministic system is unstable
Let
$$
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
A=-I+aS+J.
$$
Then
$$
A=\begin{pmatrix}-1&a-1\\a+1&-1\end{pmatrix}.
$$
Its characteristic equation is
$$
(\lambda+1)^2=a^2-1.
$$
If $0<a\le1$, both eigenvalues have real part $-1$. If $a>1$, the larger eigenvalue is
$$
-1+\sqrt{a^2-1}.
$$
Hence the deterministic system $\dot z=Az$ is exponentially stable exactly when $a<\sqrt2$. Therefore it is not exponentially stable exactly when
$$
a\ge\sqrt2.
$$

Step 2: Reduce the stochastic growth rate to an angular diffusion
Consider
$$
dZ_t=AZ_t\,dt+bJZ_t\circ dW_t,
\qquad b>0.
$$
For a nonzero solution write
$$
Z_t=r_t(\cos\theta_t,\sin\theta_t)^T.
$$
Because Stratonovich calculus obeys the ordinary chain rule, $J$ is purely rotational, and $S$ is symmetric,
$$
d\log r_t=(-1+a\sin2\theta_t)\,dt,
$$
$$
d\theta_t=(1+a\cos2\theta_t)\,dt+b\,dW_t.
$$
Set
$$
X_t=2\theta_t\pmod{2\pi}.
$$
Then
$$
dX_t=2(1+a\cos X_t)\,dt+2b\,dW_t.
$$
This is a nondegenerate diffusion on the circle, so it has a unique invariant probability law and is ergodic from every initial angle.

Step 3: Compute the stationary first Fourier moment
Let
$$
m_n=\mathbb E_{\rm stat}(e^{inX}),\qquad n\ge0,
$$
so $m_0=1$. The generator is
$$
\mathcal L f=2(1+a\cos x)f'(x)+2b^2f''(x).
$$
Applying stationarity to $e^{inx}$ gives, for $n\ge1$,
$$
a(m_{n+1}+m_{n-1})+2(1+ib^2n)m_n=0.
$$
Put
$$
\kappa=\frac{a}{b^2},\qquad \delta=\frac1{b^2}.
$$
Using the modified-Bessel recurrence
$$
I_{\nu-1}(\kappa)-I_{\nu+1}(\kappa)
=\frac{2\nu}{\kappa}I_\nu(\kappa),
$$
one checks that the bounded solution of the moment recurrence with $m_0=1$ is
$$
m_n=i^n\frac{I_{n-i\delta}(\kappa)}{I_{-i\delta}(\kappa)}.
$$
Indeed this sequence satisfies the recurrence, and the second independent recurrence solution grows with $n$, whereas stationary Fourier moments satisfy $|m_n|\le1$.

Thus
$$
m_1=i\frac{I_{1-i/b^2}(a/b^2)}{I_{-i/b^2}(a/b^2)},
$$
and hence
$$
\mathbb E_{\rm stat}(\sin X)
=\operatorname{Im}m_1
=\operatorname{Re}\frac{I_{1-i/b^2}(a/b^2)}{I_{-i/b^2}(a/b^2)}.
$$

Step 4: Compute the top Lyapunov exponent and combine the conditions
By the ergodic theorem applied to the angular diffusion,
$$
\lim_{t\to\infty}\frac1t\log\frac{\|Z_t\|}{\|Z_0\|}
=-1+a\operatorname{Re}\frac{I_{1-i/b^2}(a/b^2)}{I_{-i/b^2}(a/b^2)}
$$
almost surely for every deterministic $Z_0\ne0$. Therefore the stochastic origin is almost surely exponentially stable exactly when
$$
a\operatorname{Re}\frac{I_{1-i/b^2}(a/b^2)}{I_{-i/b^2}(a/b^2)}<1.
$$
Combining this with the deterministic instability condition $a\ge\sqrt2$ gives the required region.
Final Answer: $\boxed{\{(a,b):a\ge\sqrt2,b>0,a\Re[I_{1-i/b^2}(a/b^2)/I_{-i/b^2}(a/b^2)]<1\}}$

---

## Answer

$\{(a,b):a\ge\sqrt2,b>0,a\Re[I_{1-i/b^2}(a/b^2)/I_{-i/b^2}(a/b^2)]<1\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- Stratonovich linear stochastic systems
- noise-induced stabilization
- angular diffusions
- Fourier moment recurrences
- modified Bessel functions of complex order

---

## Black-Box Audit — no issues found

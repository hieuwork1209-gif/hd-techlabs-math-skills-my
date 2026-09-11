## Steps

Step 1: Reduce the almost-sure exponent to an angular diffusion
Let
$$
A=\begin{pmatrix}-1&a\\a&-1\end{pmatrix},
\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad a,b>0,
$$
and consider the Stratonovich equation
$$
dZ_t=A Z_t\,dt+bJZ_t\circ dW_t.
$$
For a nonzero solution write
$$
Z_t=r_t(\cos\theta_t,\sin\theta_t)^T.
$$
Because Stratonovich calculus obeys the ordinary chain rule and $J$ is the infinitesimal rotation matrix,
$$
d\log r_t=(-1+a\sin2\theta_t)\,dt,
$$
while
$$
d\theta_t=a\cos2\theta_t\,dt+b\,dW_t.
$$
Thus the top almost-sure Lyapunov exponent is obtained by averaging $-1+a\sin2\theta$ against the stationary law of the angular diffusion.

Step 2: Find the stationary angular law and the almost-sure exponent
The angular diffusion on the circle has generator
$$
\mathcal L f=a\cos2\theta\,f'(\theta)+\frac{b^2}{2}f''(\theta).
$$
Since $b>0$, it is elliptic and has a unique invariant probability density. The stationary Fokker-Planck equation has zero periodic probability flux, and therefore
$$
\rho(\theta)=\frac1{Z_q}e^{q\sin2\theta},
\qquad
q=\frac{a}{b^2}.
$$
Indeed,
$$
\frac{\rho'}{\rho}=2q\cos2\theta=\frac{2a}{b^2}\cos2\theta,
$$
so
$$
a\cos2\theta\,\rho-\frac{b^2}{2}\rho'=0.
$$

Using the modified Bessel functions of the first kind,
$$
\int_0^{2\pi}e^{q\sin2\theta}\,d\theta=2\pi I_0(q),
$$
and differentiation with respect to $q$ gives
$$
\int_0^{2\pi}\sin2\theta\,e^{q\sin2\theta}\,d\theta=2\pi I_1(q).
$$
Hence
$$
\int_0^{2\pi}\sin2\theta\,\rho(\theta)\,d\theta
=\frac{I_1(q)}{I_0(q)}.
$$
Ergodicity of the angular diffusion now yields the almost-sure top exponent
$$
\Lambda_{\rm as}(a,b)
=-1+a\frac{I_1(a/b^2)}{I_0(a/b^2)}.
$$
Therefore the origin is almost surely exponentially stable exactly when
$$
aI_1(a/b^2)<I_0(a/b^2).
$$
Because the angular diffusion is nondegenerate, the same top exponent applies to every deterministic nonzero initial direction.

Step 3: Convert the Stratonovich equation to Itô form
Since $J^2=-I$, the Itô form is
$$
dZ_t=\left(A-\frac{b^2}{2}I\right)Z_t\,dt+bJZ_t\,dW_t.
$$
Let
$$
M(t)=\mathbb E[Z_tZ_t^T].
$$
Then
$$
\dot M=\widetilde A M+M\widetilde A^T+b^2J M J^T,
\qquad
\widetilde A=A-\frac{b^2}{2}I.
$$
An orthogonal change of coordinates diagonalizes $A$ to
$$
\operatorname{diag}(-1+a,-1-a).
$$
Under the same orthogonal change, $J$ is replaced by $\pm J$, which leaves $J M J^T$ unchanged.

Step 4: Determine the exact mean-square stability threshold
In the diagonal coordinates write
$$
x=\mathbb E[Y_1^2],
\qquad
y=\mathbb E[Y_1Y_2],
\qquad z=\mathbb E[Y_2^2].
$$
The second moments satisfy
$$
\frac d{dt}\begin{pmatrix}x\\z\end{pmatrix}
=
\begin{pmatrix}
-2+2a-b^2&b^2\\
b^2&-2-2a-b^2
\end{pmatrix}
\begin{pmatrix}x\\z\end{pmatrix},
$$
and
$$
\dot y=(-2-2b^2)y.
$$
The larger eigenvalue of the $2\times2$ block is
$$
\lambda_{\rm ms}
=-2-b^2+\sqrt{4a^2+b^4}.
$$
Thus mean-square exponential stability holds exactly when
$$
\sqrt{4a^2+b^4}<2+b^2.
$$
Both sides are positive, so squaring gives
$$
4a^2+b^4<4+4b^2+b^4,
$$
i.e.
$$
a^2<1+b^2.
$$
At $a^2=1+b^2$ the second-moment system has a zero eigenvalue, so exponential decay already fails. Hence the system is not mean-square exponentially stable exactly when
$$
a^2\ge1+b^2.
$$

Step 5: Combine the two stability notions
We need almost-sure exponential stability but failure of mean-square exponential stability. Combining Steps 2 and 4 gives
$$
a,b>0,
\qquad
a^2\ge1+b^2,
\qquad
aI_1(a/b^2)<I_0(a/b^2).
$$
Final Answer: $\boxed{\{(a,b):a,b>0,a^2\ge1+b^2,\ aI_1(a/b^2)<I_0(a/b^2)\}}$

---

## Answer

$\{(a,b):a,b>0,a^2\ge1+b^2,\ aI_1(a/b^2)<I_0(a/b^2)\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- Stratonovich linear stochastic systems
- almost-sure Lyapunov exponents
- invariant angular diffusions
- mean-square stability
- modified Bessel functions

---

## Black-Box Audit — no issues found

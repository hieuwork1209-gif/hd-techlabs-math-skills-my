## Steps

Step 1: Reduce the cyclic sweep to a one-parameter matrix norm
Let
$$
D(\alpha)=\operatorname{diag}(1-\alpha,1-4\alpha),
\qquad
U=R(-\pi/3)=
\begin{bmatrix}
1/2&\sqrt3/2\\
-\sqrt3/2&1/2
\end{bmatrix}.
$$
Since $\nabla f(x)=x$ and
$$
I-\alpha P_k=R_kD(\alpha)R_k^T,
$$
one cycle is
$$
x_3=M(\alpha)x_0,
\qquad
M(\alpha)=R_2DUDUD.
$$
Thus
$$
R(\alpha)=\|M(\alpha)\|_2=\|N(\alpha)\|_2,
\qquad
N(\alpha)=DUDUD.
$$
Writing $a=\alpha$, direct multiplication gives
$$
N(a)=\frac14
\begin{bmatrix}
(a-1)^2(11a-2)&-\sqrt3(a-1)(4a-1)(5a-2)\\
\sqrt3(a-1)(4a-1)(5a-2)&-(a+2)(4a-1)^2
\end{bmatrix}.
$$

Step 2: Express the larger squared singular value explicitly
Let $\lambda_+(a)=R(a)^2$, the larger eigenvalue of $N(a)^TN(a)$. Its trace and determinant are
$$
T(a)=\operatorname{tr}(N^TN)
=\frac{2777a^6-7680a^5+11136a^4-7840a^3+2784a^2-480a+32}{16},
$$
$$
\Delta(a)=\det N=(a-1)^3(4a-1)^3.
$$
Therefore
$$
\lambda_+(a)=\frac{T(a)+\sqrt{T(a)^2-4\Delta(a)^2}}2.
$$
The discriminant factors as
$$
T(a)^2-4\Delta(a)^2
=\frac{729}{256}a^6(5a-2)^2Q(a),
$$
where
$$
Q(a)=193a^4-460a^3+492a^2-160a+16.
$$
On $0<a\le1/2$, $Q(a)>0$, so the formula is smooth except for the harmless absolute-value switch at $a=2/5$.

Step 3: Locate the global minimizer
Differentiate $\lambda_+(a)$ separately on $(0,2/5)$ and $(2/5,1/2)$. Clearing the positive square-root denominator and then squaring the remaining radical equation yields the stationary polynomial
$$
q(a)=772a^4-1840a^3+2031a^2-820a+100.
$$
The squaring step can introduce extraneous roots, so the candidates must be checked in the unsquared derivative equation. The quartic has two real roots in $(0,1/2)$:
$$
0.220728857620266\ldots,
\qquad
0.408367343518342\ldots.
$$
Only the first satisfies the original stationary equation for the larger singular-value branch. Moreover, direct sign evaluation of $\lambda_+'$ gives
$$
\lambda_+'(a)<0\quad(0<a<a_*),
\qquad
\lambda_+'(a)>0\quad(a_*<a\le1/2),
$$
with the one-sided derivatives at $2/5$ also positive. Hence the unique global minimizer is
$$
a_*=0.2207288576202662980\ldots.
$$
Equivalently, $a_*$ is the unique root of $q(a)$ in $(0.2207,0.2208)$ that satisfies the unsquared stationary equation.

Step 4: Evaluate the optimal contraction
Substituting $a_*$ into the larger singular-value formula gives
$$
R_*=\sqrt{\lambda_+(a_*)}
=0.0818685765867553545\ldots.
$$
Thus, to ten decimal places,
$$
R_*=0.0818685766,
\qquad
\alpha_*=0.2207288576.
$$

Final Answer: $\boxed{\left(0.0818685766,0.2207288576\right)}$

---

## Answer

$\left(0.0818685766,0.2207288576\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- cyclic preconditioned gradient descent
- singular values of a matrix product
- one-parameter spectral-norm optimization
- algebraic stationary-point isolation

## Steps

Step 1: Prove that the implicit root is unique

Put
$$
\sigma(x)=2x-1,\qquad y=x(1-x),\qquad h(x)=\exp\!\left(-\frac1{x(1-x)}\right).
$$
Since $0<y\leq1/4$ on $(0,1)$,
$$
0<h(x)\leq e^{-4},
$$
so
$$
1+\sigma(x)h(x)>0.
$$
Define the positive weight
$$
W_n(x)=e^{-ny^2}\bigl(1+\sigma(x)h(x)\bigr)
$$
and
$$
Z_n(\lambda)=\int_0^1 W_n(x)e^{\lambda\sigma(x)}\,dx.
$$
Then
$$
I_n(\lambda)=Z_n'(\lambda),
$$
and
$$
I_n'(\lambda)=Z_n''(\lambda)
=\int_0^1\sigma(x)^2W_n(x)e^{\lambda\sigma(x)}\,dx>0.
$$
Thus $I_n$ is strictly increasing. As $\lambda\to+\infty$, any fixed interval near $x=1$ gives a positive exponentially growing contribution while the part with $\sigma\leq0$ stays bounded; hence $I_n(\lambda)\to+\infty$. Similarly $I_n(\lambda)\to-\infty$ as $\lambda\to-\infty$. Therefore the root $\lambda_n$ exists and is unique.

Step 2: Isolate the beyond-all-orders asymmetry

The functions $y=x(1-x)$ and $h(x)$ are invariant under $x\mapsto1-x$, while
$$
\sigma(1-x)=-\sigma(x).
$$
At $\lambda=0$ the symmetric part cancels exactly:
$$
\int_0^1\sigma(x)e^{-ny^2}\,dx=0.
$$
Therefore
$$
I_n(0)=J_n,
$$
where
$$
J_n=\int_0^1\sigma(x)^2\exp\!\left(-ny^2-\frac1y\right)\,dx>0. \tag{1}
$$
The derivative has another exact symmetry cancellation:
$$
I_n'(0)
=\int_0^1\sigma(x)^2e^{-ny^2}\,dx
+\int_0^1\sigma(x)^3e^{-ny^2-1/y}\,dx
=K_n, \tag{2}
$$
where
$$
K_n=\int_0^1\sigma(x)^2e^{-ny^2}\,dx.
$$
The second integral in (2) vanishes because its integrand is antisymmetric.

Step 3: Evaluate the ordinary endpoint scale $K_n$

On $0\leq x\leq1/2$, the change of variable
$$
y=x(1-x)
$$
gives
$$
\sigma(x)^2=1-4y,
\qquad
 dx=\frac{dy}{\sqrt{1-4y}}.
$$
Using symmetry about $x=1/2$,
$$
K_n=2\int_0^{1/4}\sqrt{1-4y}\,e^{-ny^2}\,dy.
$$
Set $y=t/\sqrt n$. Then
$$
\sqrt n\,K_n
=2\int_0^{\sqrt n/4}\sqrt{1-\frac{4t}{\sqrt n}}\,e^{-t^2}\,dt.
$$
For every fixed $t$ the square-root factor tends to $1$, and the Gaussian tail gives domination. Hence
$$
\sqrt n\,K_n\longrightarrow2\int_0^\infty e^{-t^2}\,dt=\sqrt\pi,
$$
so
$$
K_n\sim\sqrt\pi\,n^{-1/2}. \tag{3}
$$

Step 4: Find the moving saddle created by the flat perturbation

Applying the same change of variable to (1),
$$
J_n=2\int_0^{1/4}\sqrt{1-4y}\,
\exp\!\left(-ny^2-\frac1y\right)\,dy.
$$
Let
$$
N=n^{1/3},\qquad y=\frac zN.
$$
Then
$$
J_n=\frac2N\int_0^{N/4}\sqrt{1-\frac{4z}{N}}\,e^{-N\Phi(z)}\,dz,
\qquad
\Phi(z)=z^2+\frac1z. \tag{4}
$$
The function $\Phi$ has a unique critical point on $(0,\infty)$ because
$$
\Phi'(z)=2z-\frac1{z^2}=0
\iff z=z_0:=2^{-1/3}.
$$
It is the unique minimum, and
$$
\Phi(z_0)=\frac{3}{2^{2/3}}=:c,
\qquad
\Phi''(z_0)=6. \tag{5}
$$
To extract the constant in (4), write
$$
z=z_0+\frac u{\sqrt N}.
$$
Taylor's formula at $z_0$ gives, for bounded $u$,
$$
N\bigl(\Phi(z)-c\bigr)=3u^2+O\!\left(\frac{|u|^3}{\sqrt N}\right),
$$
and the square-root amplitude in (4) tends to $1$. On the complement of any fixed neighborhood of $z_0$, continuity and the uniqueness of the minimum give $\Phi\geq c+\eta$ for some $\eta>0$; inside that neighborhood the positive second derivative gives a Gaussian majorant after shrinking it if necessary. Thus the rescaled integral converges to the Gaussian integral, and
$$
\int_0^{N/4}\sqrt{1-\frac{4z}{N}}\,e^{-N\Phi(z)}\,dz
\sim e^{-cN}\frac1{\sqrt N}\int_{-\infty}^{\infty}e^{-3u^2}\,du
=e^{-cN}\sqrt{\frac{\pi}{3N}}.
$$
Substituting into (4),
$$
J_n\sim2\sqrt{\frac\pi3}\,n^{-1/2}
\exp\!\left(-\frac{3}{2^{2/3}}n^{1/3}\right). \tag{6}
$$
In particular, (3) and (6) imply $J_n/K_n\to0$.

Step 5: Convert the asymmetry into the root displacement

For $-1\leq\lambda\leq0$,
$$
I_n'(\lambda)
=\int_0^1\sigma^2 e^{-ny^2+\lambda\sigma}(1+\sigma h)\,dx
\geq e^{-1}(1-e^{-4})K_n.
$$
Since $I_n(0)=J_n$ and $J_n/K_n\to0$, we have $I_n(-1)<0$ for all sufficiently large $n$. Hence
$$
-1<\lambda_n<0.
$$
By the mean value theorem, for some $\xi_n\in(\lambda_n,0)$,
$$
0=I_n(\lambda_n)=J_n+\lambda_n I_n'(\xi_n),
$$
so
$$
-\lambda_n=\frac{J_n}{I_n'(\xi_n)}. \tag{7}
$$
The lower bound above and $J_n/K_n\to0$ first give $\lambda_n\to0$, hence $\xi_n\to0$. Moreover,
$$
\int_0^1\sigma^2e^{-ny^2}\bigl(e^{\xi_n\sigma}-1\bigr)\,dx=O(|\xi_n|K_n),
$$
and
$$
\left|\int_0^1\sigma^3h\,e^{-ny^2+\xi_n\sigma}\,dx\right|
\leq e^{|\xi_n|}J_n=o(K_n).
$$
Therefore
$$
I_n'(\xi_n)\sim K_n.
$$
Using (3), (6), and (7),
$$
\lambda_n
\sim-\frac{J_n}{K_n}
\sim-\frac2{\sqrt3}
\exp\!\left(-\frac{3}{2^{2/3}}n^{1/3}\right).
$$
Consequently the requested constants are
$$
c=\frac{3}{2^{2/3}},
\qquad
L=-\frac2{\sqrt3}.
$$
Final Answer: $\boxed{\left(\frac{3}{2^{2/3}},-\frac2{\sqrt3}\right)}$

---

## Answer

$\left(\frac{3}{2^{2/3}},-\frac2{\sqrt3}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- implicit integral roots
- exact symmetry cancellation
- flat endpoint perturbation
- moving-saddle Laplace scaling
- beyond-all-orders asymptotics

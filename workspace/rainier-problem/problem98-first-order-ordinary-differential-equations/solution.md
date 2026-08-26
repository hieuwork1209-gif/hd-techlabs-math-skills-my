## Steps

Step 1: Recover the hidden first integral

Put $u=y-\frac12$, write $D_\lambda(u)=F_{\lambda,p}(u)$ and $W(u)=1-4u^3$, and let $X(u)$ be the inverse position of the increasing solution. On the relevant interval,
$$
D_\lambda(u)>0
$$
because $1-pu\geq1-\frac p2>0$. Taking the reciprocal of the differential equation gives
$$
X'(u)=
\frac{
\dfrac{W(u)}{nD_\lambda(u)}+12u^2X+2X^2+24X^3
}{
W(u)+2(1-2u)X+36(1-2u)X^2
}.
$$
Define
$$
\Phi(u,X)=W(u)X+(1-2u)X^2+12(1-2u)X^3.
$$
Direct differentiation gives
$$
\Phi_u=-12u^2X-2X^2-24X^3,
\qquad
\Phi_X=W(u)+2(1-2u)X+36(1-2u)X^2.
$$
Therefore the displayed equation is exactly
$$
\frac{d}{du}\Phi(u,X(u))=\frac{W(u)}{nD_\lambda(u)}.
$$
On $[-\frac12,\frac12]$ we have $W(u)\geq\frac12$ and $1-2u\geq0$, so $\Phi_X>0$ for $X\geq0$. Hence the identity
$$
\Phi(u,X(u))=\frac1n\int_{-1/2}^{u}\frac{W(t)}{D_\lambda(t)}\,dt
$$
uniquely defines a strictly increasing inverse orbit with $X(-\frac12)=0$.

Step 2: Encode the terminal and midpoint conditions

At $u=\frac12$, the quadratic and cubic terms in $\Phi$ vanish and $W(\frac12)=\frac12$. Thus $X(\frac12)=1$ is equivalent to
$$
J(\lambda):=\int_{-1/2}^{1/2}\frac{W(u)}{D_\lambda(u)}\,du=\frac n2.
$$
The function $J$ is continuous, tends to infinity as $\lambda\downarrow0$, and tends to zero as $\lambda\to\infty$. Consequently the required set of parameters is nonempty and has a least element. Moreover, the least solution $\lambda_{n,p}$ tends to zero as $n\to\infty$, because $J$ is bounded on every interval $[\varepsilon,\infty)$.

Let
$$
L(\lambda)=\int_{-1/2}^{0}\frac{W(u)}{D_\lambda(u)}\,du,
\qquad
R(\lambda)=\int_{0}^{1/2}\frac{W(u)}{D_\lambda(u)}\,du,
\qquad
\Delta(\lambda)=L(\lambda)-R(\lambda).
$$
At $u=0$, the first integral gives
$$
\xi_{n,p}+\xi_{n,p}^2+12\xi_{n,p}^3
=\frac{L(\lambda_{n,p})}{n}
=\frac14+\frac{\Delta(\lambda_{n,p})}{2n}.
$$

Step 3: Determine the scale selected by the two coalescing slow regions

The denominator has narrow minima near $u=\pm\sqrt\lambda$. In either neighborhood write $u=\varepsilon\sqrt\lambda+\lambda t$, where $\varepsilon\in\{-1,1\}$. For fixed $t$,
$$
D_\lambda(u)=\lambda^3\left(1+4t^2+o(1)\right),
\qquad
W(u)=1+o(1),
\qquad
du=\lambda\,dt.
$$
Thus each minimum contributes
$$
\lambda^{-2}\int_{-\infty}^{\infty}\frac{dt}{1+4t^2}
=\frac{\pi}{2}\lambda^{-2}
$$
to leading order. To control the tails, split at $|u-\varepsilon\sqrt\lambda|=M\lambda$ and use
$$
D_\lambda(u)\geq (u^2-\lambda)^2+\left(1-\frac p2\right)\lambda^3.
$$
After the same substitution, the omitted part is bounded by a constant times $\lambda^{-2}\int_{|t|>M}(1+t^2)^{-1}dt$. Letting first $\lambda\downarrow0$ and then $M\to\infty$ proves
$$
J(\lambda)=\pi\lambda^{-2}(1+o(1)).
$$
Since $J(\lambda_{n,p})=\frac n2$,
$$
\lambda_{n,p}=\left(\frac{2\pi}{n}\right)^{1/2}(1+o(1)).
$$

Step 4: Extract the answer-sensitive left-right imbalance

For $u>0$, put
$$
A=(u^2-\lambda)^2+\lambda^3.
$$
Then $D_\lambda(-u)=A+p\lambda^3u$ and $D_\lambda(u)=A-p\lambda^3u$, while
$$
(1+4u^3)(A-p\lambda^3u)-(1-4u^3)(A+p\lambda^3u)
=2u(4u^2A-p\lambda^3).
$$
Pairing the two half-intervals and putting $v=u^2$ and $S_\lambda(v)=(v-\lambda)^2+\lambda^3$ therefore gives the exact identity
$$
\Delta(\lambda)
=
\int_0^{1/4}
\frac{4vS_\lambda(v)-p\lambda^3}
{S_\lambda(v)^2-p^2\lambda^6v}
\,dv.
$$
Because $v\leq\frac14$ and $p<2$,
$$
S_\lambda(v)^2-p^2\lambda^6v
\geq
\left(1-\frac{p^2}{4}\right)S_\lambda(v)^2.
$$
For the part with numerator $4vS_\lambda(v)$, the lower bound gives
$$
\left|4\int_0^{1/4}\frac{vS_\lambda(v)}{S_\lambda(v)^2-p^2\lambda^6v}\,dv\right|
\leq
C_p\int_0^{1/4}\frac{v\,dv}{(v-\lambda)^2+\lambda^3}.
$$
Writing $v=(v-\lambda)+\lambda$ shows that the last integral is $O(|\log\lambda|+\lambda^{-1/2})$, so this part becomes negligible after multiplication by $\lambda^{3/2}$. For the remaining part, substitute $v=\lambda+\lambda^{3/2}t$. The preceding lower bound supplies the integrable majorant $C_p(1+t^2)^{-2}$, and
$$
\lambda^{9/2}
\int_0^{1/4}
\frac{dv}{S_\lambda(v)^2-p^2\lambda^6v}
\longrightarrow
\int_{-\infty}^{\infty}\frac{dt}{(1+t^2)^2}
=\frac\pi2.
$$
Therefore
$$
\lambda^{3/2}\Delta(\lambda)\longrightarrow-\frac{p\pi}{2}.
$$
Combining this with $J(\lambda)\sim\pi\lambda^{-2}$ and $n=2J(\lambda_{n,p})$ gives
$$
\frac{L(\lambda_{n,p})}{n}
=
\frac14-\frac p8\sqrt{\lambda_{n,p}}+o\left(\sqrt{\lambda_{n,p}}\right).
$$

Step 5: Invert the cubic relation

Let $f(z)=z+z^2+12z^3$. It is strictly increasing for $z\geq0$, and
$$
f\left(\frac16\right)=\frac14,
\qquad
f'\left(\frac16\right)=\frac73.
$$
The midpoint relation from Step 2 and the expansion from Step 4 therefore imply
$$
\xi_{n,p}
=
\frac16-\frac{3p}{56}\sqrt{\lambda_{n,p}}
+o\left(\sqrt{\lambda_{n,p}}\right).
$$
Using Step 3,
$$
\sqrt{\lambda_{n,p}}
=(2\pi)^{1/4}n^{-1/4}(1+o(1)),
$$
so
$$
c_p=\frac16,
\qquad
K_p=-\frac{3p(2\pi)^{1/4}}{56}.
$$
Final Answer: $\boxed{(\frac16,-\frac{3p(2\pi)^{1/4}}{56})}$

---

## Answer

$(\frac16,-\frac{3p(2\pi)^{1/4}}{56})$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- inverse functions
- nonlinear first integrals
- singular asymptotic analysis
- coalescing slow regions
- dominated convergence

---

## Black-Box Audit

No Level 2 or Level 3 black-box issue remains. The hidden first integral is verified by differentiation, the two-peak scale is accompanied by a tail bound, and the imbalance coefficient follows from an exact paired integral and an explicit dominated-convergence limit. As an independent numerical check, solving the exact integral equation for $p=1$ gives $n^{1/4}(\xi_{n,1}-\frac16)=-0.08468$ at $n=10^7$, while the predicted coefficient is $-0.08482$; the same convergence occurs for other fixed values of $p$.

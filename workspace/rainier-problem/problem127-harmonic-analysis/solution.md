## Steps

Step 1: Normalize the phase and obtain the sharp upper bound
Let
$$
P_{\alpha,\beta}(\theta)=1+2\operatorname{Re}\!\left(\alpha e^{i\theta}+\beta e^{in\theta}\right)\ge0
$$
for every real $\theta$. Write
$$
\alpha=a e^{i\gamma},\qquad a=|\alpha|\ge0,
$$
and put
$$
B=\beta e^{-in\gamma}.
$$
After the change of variable $x=\theta+\gamma$,
$$
Q(x):=P_{\alpha,\beta}(x-\gamma)
=1+2a\cos x+2\operatorname{Re}(Be^{inx})\ge0.
$$
Set
$$
\phi=\frac{\pi}{2n},\qquad c=\cos\phi,
\qquad s=\sin\phi.
$$
If $B=0$, then $Q(\pi)=1-2a\ge0$, so $a\le1/2<1/(2c)$.

Now assume $B\ne0$ and write $B=\rho e^{i\delta}$ with $\rho>0$. The zeros of
$$
q(x)=\operatorname{Re}(Be^{inx})=\rho\cos(nx+\delta)
$$
are spaced by $\pi/n=2\phi$. Hence one zero $x_0$ has circular distance
$$
d=|x_0-\pi|\le\phi
$$
from $\pi$. At that point,
$$
0\le Q(x_0)=1+2a\cos x_0=1-2a\cos d.
$$
Therefore
$$
a\le\frac1{2\cos d}\le\frac1{2\cos\phi}.
$$
Thus
$$
|\alpha|\le\frac1{2\cos(\pi/(2n))}.
$$

Step 2: Equality forces the phase and the high-frequency coefficient
Assume equality holds:
$$
a=\frac1{2c}.
$$
Then $B\ne0$, and equality must hold in the distance bound from Step 1. Thus the closest zeros of $q$ to $\pi$ are exactly
$$
\pi-\phi,\qquad \pi+\phi.
$$
In particular,
$$
0=q(\pi-\phi)
=\rho\cos\left(n\pi-\frac\pi2+\delta\right)
=(-1)^n\rho\sin\delta.
$$
Hence $\sin\delta=0$, so $B$ is real. Write $B=b$.

At
$$
x_*=\pi-\phi
$$
we have $q(x_*)=0$ and
$$
1+2a\cos x_*=1-2ac=0,
$$
so $Q(x_*)=0$. Since $Q\ge0$ and is differentiable, $x_*$ is a local minimum and therefore
$$
Q'(x_*)=0.
$$
Now
$$
Q'(x)=-2a\sin x-2bn\sin(nx).
$$
Using
$$
\sin x_*=s,
\qquad
\sin(nx_*)=(-1)^{n+1},
$$
we obtain
$$
0=-2as-2bn(-1)^{n+1},
$$
so
$$
b=\frac{(-1)^n}{2n}\tan\phi.
$$
Since $B=\beta e^{-in\gamma}$,
$$
\beta
=\frac{(-1)^n}{2n}\tan\phi\,e^{in\gamma}
=\frac{(-1)^n}{2n}\tan\phi\,e^{in\arg\alpha}.
$$
Thus equality, if attainable, already forces the unique relative phase and magnitude of $\beta$.

Step 3: Prove the forced normalized pair is globally nonnegative
It remains to prove attainability. Take
$$
a=\frac1{2c},
\qquad
b=\frac{(-1)^n}{2n}\tan\phi.
$$
For the normalized polynomial
$$
Q(x)=1+2a\cos x+2b\cos(nx),
$$
it is enough by evenness and periodicity to consider $0\le x\le\pi$. Put
$$
t=\pi-x.
$$
Then
$$
cQ(x)=h(t):=c-\cos t+\frac{s}{n}\cos(nt).
$$
We show $h(t)\ge0$ on $[0,\pi]$.

For $0<u\le\pi/2$, define
$$
r(u)=\frac{\sin(u/n)}{\sin u}.
$$
Because $x\cot x$ is strictly decreasing on $(0,\pi/2]$,
$$
\frac{r'(u)}{r(u)}
=\frac1n\cot\frac un-\cot u>0.
$$
Hence $r$ is increasing. For $0\le t\le\phi$, taking $u=nt$ gives
$$
\frac{\sin t}{\sin(nt)}\le r\left(\frac\pi2\right)=s,
$$
so
$$
h'(t)=\sin t-s\sin(nt)\le0.
$$
Since $h(\phi)=0$, we get $h(t)\ge0$ on $[0,\phi]$.

For $\phi\le t\le\pi-\phi$,
$$
\sin t\ge s,
\qquad
\sin(nt)\le1,
$$
so $h'(t)\ge0$. Hence again $h(t)\ge h(\phi)=0$.

Finally, for $\pi-\phi\le t\le\pi$ we have $\cos t\le-c$, and therefore
$$
h(t)
\ge 2c-\frac{s}{n}>0.
$$
Thus $Q(x)\ge0$ for every real $x$.

Step 4: Restore the original phase and conclude uniqueness
For any phase $\gamma$, shifting the normalized extremizer back gives
$$
\alpha=\frac{e^{i\gamma}}{2\cos\phi},
\qquad
\beta=\frac{(-1)^n}{2n}\tan\phi\,e^{in\gamma},
$$
and preserves nonnegativity. Hence the upper bound is attained for every phase of $\alpha$.

Conversely, Step 2 shows that every extremizer must have exactly this relative phase and high-frequency coefficient. Therefore the maximum and the corresponding $\beta$ are uniquely determined once $\alpha$ is given.

Final Answer: $\boxed{\left(\frac1{2\cos(\pi/(2n))},\frac{(-1)^n}{2n}\tan\frac\pi{2n}e^{in\arg\alpha}\right)}$

---

## Answer

$\left(\frac1{2\cos(\pi/(2n))},\frac{(-1)^n}{2n}\tan\frac\pi{2n}e^{in\arg\alpha}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- nonnegative trigonometric polynomials
- Fourier phase normalization
- zero-lattice spacing
- tangency at an extremal zero
- global trigonometric positivity

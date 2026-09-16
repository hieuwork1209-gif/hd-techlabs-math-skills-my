## Steps

Step 1: Get a sharp upper bound from a zero of the high-frequency mode
Fix an integer $n\ge2$. Suppose
$$
P(\theta)=1+2a\cos\theta+2b\cos(n\theta)\ge0
$$
for every real $\theta$.

Set
$$
\phi=\frac{\pi}{2n},
\qquad
\theta_0=\pi-\phi.
$$
Then
$$
\cos(n\theta_0)=\cos\left(n\pi-\frac\pi2\right)=0,
$$
so nonnegativity at $\theta_0$ gives
$$
0\le P(\theta_0)=1-2a\cos\phi.
$$
Hence
$$
a\le\frac1{2\cos\phi}.
$$
Thus no admissible pair can have a larger first Fourier coefficient.

Step 2: Determine the only possible $b$ at equality
Assume now that
$$
a=\frac1{2\cos\phi}.
$$
Then $P(\theta_0)=0$. Since $P$ is differentiable and nonnegative everywhere, every zero is a local minimum, so
$$
P'(\theta_0)=0.
$$
Now
$$
P'(\theta)=-2a\sin\theta-2bn\sin(n\theta).
$$
Using
$$
\sin\theta_0=\sin\phi,
\qquad
\sin(n\theta_0)=\sin\left(n\pi-\frac\pi2\right)=(-1)^{n+1},
$$
we obtain
$$
0=-2a\sin\phi-2bn(-1)^{n+1}.
$$
Therefore the only possible coefficient at the optimum is
$$
b=\frac{(-1)^n}{2n}\tan\phi.
$$
It remains to prove that this forced pair is actually admissible.

Step 3: Prove global nonnegativity of the extremal polynomial
Take
$$
a=\frac1{2\cos\phi},
\qquad
b=\frac{(-1)^n}{2n}\tan\phi.
$$
Because $P$ is even and $2\pi$-periodic, it is enough to consider $0\le\theta\le\pi$. Put
$$
t=\pi-\theta,
\qquad
c=\cos\phi,
\qquad
s=\sin\phi.
$$
Then
$$
\cos\theta=-\cos t,
\qquad
(-1)^n\cos(n\theta)=\cos(nt),
$$
so
$$
P(\theta)=\frac{F(t)}{nc},
$$
where
$$
F(t)=n(c-\cos t)+s\cos(nt).
$$
We prove $F(t)\ge0$ on $[0,\pi]$.

First, for $0<u\le\pi/2$, define
$$
h(u)=\frac{\sin(u/n)}{\sin u}.
$$
The function $x\cot x$ is strictly decreasing on $(0,\pi/2]$, because
$$
\frac{d}{dx}(x\cot x)
=\frac{\sin x\cos x-x}{\sin^2x}<0.
$$
Hence
$$
\frac{h'(u)}{h(u)}
=\frac1n\cot\frac un-\cot u
>0.
$$
Thus $h$ is increasing, and therefore
$$
\frac{\sin(u/n)}{\sin u}
\le h\left(\frac\pi2\right)
=\sin\phi=s.
$$
Taking $u=nt$ shows that for $0\le t\le\phi$,
$$
\sin t\le s\sin(nt).
$$
Since
$$
F'(t)=n\bigl(\sin t-s\sin(nt)\bigr),
$$
we have $F'(t)\le0$ on $[0,\phi]$. Also
$$
F(\phi)=n(c-c)+s\cos\frac\pi2=0,
$$
so $F\ge0$ on $[0,\phi]$.

For $\phi\le t\le\pi-\phi$, we have $\sin t\ge s$ and $\sin(nt)\le1$, hence
$$
F'(t)=n\bigl(\sin t-s\sin(nt)\bigr)\ge0.
$$
Thus $F\ge F(\phi)=0$ throughout this interval.

Finally let $\pi-\phi\le t\le\pi$ and put $u=\pi-t\in[0,\phi]$. If $n$ is even, then
$$
\sin(nt)=-\sin(nu),
$$
so $F'(t)\ge0$. If $n$ is odd, then
$$
\sin(nt)=\sin(nu),
$$
and the inequality already proved gives $F'(t)\le0$. In that odd case the minimum on the final interval is at $t=\pi$, where
$$
F(\pi)=n(c+1)-s>0.
$$
Hence $F(t)\ge0$ for all $t\in[0,\pi]$, so $P(\theta)\ge0$ for every real $\theta$.

Step 4: Conclude sharpness and uniqueness of the extremal pair
Step 1 proves
$$
a\le\frac1{2\cos(\pi/(2n))}.
$$
Step 3 shows this value is attained. Step 2 shows that once equality holds, nonnegativity forces the unique corresponding coefficient
$$
b=\frac{(-1)^n}{2n}\tan\frac\pi{2n}.
$$
Therefore the requested extremal pair is unique.

Final Answer: $\boxed{\left(\frac1{2\cos(\pi/(2n))},\frac{(-1)^n}{2n}\tan\frac\pi{2n}\right)}$

---

## Answer

$\left(\frac1{2\cos(\pi/(2n))},\frac{(-1)^n}{2n}\tan\frac\pi{2n}\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- nonnegative trigonometric polynomials
- Fourier coefficient extremization
- tangency at a forced zero
- trigonometric monotonicity
- equality and uniqueness

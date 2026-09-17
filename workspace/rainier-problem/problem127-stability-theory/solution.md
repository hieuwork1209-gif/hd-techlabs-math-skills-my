## Steps

Step 1: Show stability holds for all sufficiently small delays and can be lost only on the imaginary axis
The characteristic equation is
$$
\Delta_\tau(\lambda)
=\lambda+a+(c\lambda+b)e^{-\lambda\tau}=0.
$$
Suppose $\lambda=u+iv$ is a characteristic root with $u\geq0$. Then
$$
|\lambda+a|
=|c\lambda+b|e^{-u\tau}
\leq |c\lambda+b|.
$$
After squaring,
$$
(1-c^2)(u^2+v^2)+2(a-bc)u+a^2-b^2\leq0.
$$
Writing $r=|\lambda|$ and using $0\leq u\leq r$ gives
$$
(1-c^2)r^2-2|a-bc|r-(b^2-a^2)\leq0.
$$
Hence every characteristic root in the closed right half-plane is bounded by a constant depending only on $a,b,c$, uniformly in $\tau$.

Now suppose there were delays $\tau_j\to0^+$ with roots $\lambda_j$ satisfying $\operatorname{Re}\lambda_j\geq0$. By the uniform bound, a subsequence converges to some $\lambda_*$. Passing to the limit in the characteristic equation gives
$$
(1+c)\lambda_*+a+b=0,
$$
so
$$
\lambda_*=-\frac{a+b}{1+c}<0,
$$
contradicting $\operatorname{Re}\lambda_*\geq0$. Thus all characteristic roots lie in the open left half-plane for all sufficiently small positive delays.

Because right-half-plane roots are uniformly bounded, a first loss of stability cannot occur through roots escaping from infinity. By continuity of zeros of analytic functions under parameter variation, any first loss must therefore occur when a characteristic root lies on the imaginary axis.

Step 2: Determine every imaginary-axis crossing
Let $\lambda=i\omega$ with $\omega\ne0$. The characteristic equation gives
$$
e^{-i\omega\tau}
=-\frac{a+i\omega}{b+ic\omega}.
$$
Taking absolute values yields
$$
a^2+\omega^2=b^2+c^2\omega^2,
$$
so every imaginary root has the same frequency magnitude
$$
\omega_0
=\sqrt{\frac{b^2-a^2}{1-c^2}}.
$$
Since $0<a<b$ and $0<c<1$, this is positive.

At $\omega=\omega_0$, write
$$
e^{-i\omega_0\tau}=\cos\theta-i\sin\theta.
$$
Expanding the quotient gives
$$
\cos\theta
=-\frac{ab+c\omega_0^2}{b^2+c^2\omega_0^2},
\qquad
\sin\theta
=\frac{\omega_0(b-ac)}{b^2+c^2\omega_0^2}>0.
$$
Using
$$
\omega_0^2=\frac{b^2-a^2}{1-c^2}
$$
and factoring the numerator and denominator gives the simpler identity
$$
\cos\theta=-\frac{a+bc}{b+ac}.
$$
Moreover,
$$
0<\frac{a+bc}{b+ac}<1,
$$
so the relevant phase is uniquely
$$
\theta_0
=\arccos\left(-\frac{a+bc}{b+ac}\right)
\in\left(\frac\pi2,\pi\right).
$$
Thus the complete sequence of imaginary-axis crossings is
$$
\tau_k
=\frac{\theta_0+2\pi k}{\omega_0},
\qquad k=0,1,2,\ldots.
$$
In particular, the first possible crossing delay is
$$
\tau_0
=\sqrt{\frac{1-c^2}{b^2-a^2}}
\arccos\left(-\frac{a+bc}{b+ac}\right).
$$

Step 3: Prove that every crossing is from left to right
Near an imaginary root, use a local logarithm of
$$
e^{-\lambda\tau}
=-\frac{\lambda+a}{c\lambda+b}.
$$
Along a root branch this gives
$$
-\lambda\tau
=\log\left(-\frac{\lambda+a}{c\lambda+b}\right)+2\pi i k.
$$
Differentiating with respect to $\lambda$ gives
$$
-\tau-\lambda\frac{d\tau}{d\lambda}
=\frac{1}{\lambda+a}-\frac{c}{c\lambda+b},
$$
so
$$
\frac{d\tau}{d\lambda}
=-\frac{\tau}{\lambda}
-\frac{1}{\lambda}
\left(
\frac{1}{\lambda+a}-\frac{c}{c\lambda+b}
\right).
$$
At $\lambda=i\omega_0$, the first term is purely imaginary. Also the modulus identity from Step 2 gives
$$
a^2+\omega_0^2=b^2+c^2\omega_0^2.
$$
Therefore
$$
\operatorname{Im}
\left(
\frac{1}{a+i\omega_0}
-\frac{c}{b+ic\omega_0}
\right)
=-\frac{(1-c^2)\omega_0}{a^2+\omega_0^2}.
$$
Hence
$$
\operatorname{Re}\frac{d\tau}{d\lambda}
=\frac{1-c^2}{a^2+\omega_0^2}>0.
$$
Since
$$
\frac{d\lambda}{d\tau}
=\left(\frac{d\tau}{d\lambda}\right)^{-1},
$$
its real part has the same sign. Thus at every $\tau_k$ the conjugate pair of roots crosses the imaginary axis from left to right as $\tau$ increases.

Step 4: Complete the global stability classification
Step 1 shows that all roots are initially in the open left half-plane. Step 2 shows that the first possible boundary crossing occurs at $\tau_0$, and Step 3 shows that the crossing there is into the right half-plane. Hence every
$$
0<\tau<\tau_0
$$
is stable, while $\tau=\tau_0$ is not because it has purely imaginary roots.

The only later imaginary-axis crossings are the delays $\tau_k$ from Step 2, and Step 3 shows that every one of them is again left-to-right. Consequently the number of right-half-plane roots can never decrease as $\tau$ grows, so stability can never be recovered after $\tau_0$.

Therefore the desired set of delays is exactly the open interval below.

Final Answer: $\boxed{\left(0,\sqrt{\frac{1-c^2}{b^2-a^2}}\arccos\left(-\frac{a+bc}{b+ac}\right)\right)}$

---

## Answer

$\left(0,\sqrt{\frac{1-c^2}{b^2-a^2}}\arccos\left(-\frac{a+bc}{b+ac}\right)\right)$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Set or multiset of objects

---

## Solution Concepts

- neutral delay differential equations
- characteristic roots
- imaginary-axis crossings
- transversality of characteristic roots
- delay-dependent stability

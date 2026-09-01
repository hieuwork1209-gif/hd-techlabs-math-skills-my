## Steps

Step 1: Separate the implicit root from the asymptotic integral

Define
$$
A_n=\int_0^1\!\int_0^1 e^{-n(xy)^2}\,dx\,dy
$$
and
$$
J_n=\int_0^1\!\int_0^1
\left(1-\sqrt[3]{2n}\,xy\right)^5
\exp\!\left(-n(xy)^2-\frac1{xy}\right)dx\,dy.
$$
Then
$$
I_n(\lambda)=2A_n\sinh\lambda+2J_n.
$$
Since $A_n>0$, the function $I_n$ is strictly increasing in $\lambda$ and tends to $\pm\infty$ as $\lambda\to\pm\infty$. Hence the root is unique and satisfies
$$
\sinh\lambda_n=-\frac{J_n}{A_n}. \tag{1}
$$
Thus the problem reduces to finding the first nonzero asymptotic term of $J_n/A_n$.

Step 2: Reduce the product integrals to one variable and evaluate $A_n$

For every integrable function $F$ on $(0,1)$,
$$
\int_0^1\!\int_0^1 F(xy)\,dx\,dy
=\int_0^1(-\log t)F(t)\,dt. \tag{2}
$$
Indeed, for fixed $x$, put $t=xy$ and then reverse the order of integration:
$$
\int_0^1\frac1x\int_0^xF(t)\,dt\,dx
=\int_0^1F(t)\int_t^1\frac{dx}{x}\,dt.
$$
Applying (2),
$$
A_n=\int_0^1(-\log t)e^{-nt^2}\,dt.
$$
With $s=\sqrt n\,t$,
$$
A_n=\frac1{\sqrt n}\left[
\frac12\log n\int_0^{\sqrt n}e^{-s^2}\,ds
-\int_0^{\sqrt n}(\log s)e^{-s^2}\,ds
\right].
$$
The second integral converges to a finite constant, while the first tends to
$$
\frac12\log n\cdot\frac{\sqrt\pi}{2}.
$$
Therefore
$$
A_n\sim\frac{\sqrt\pi}{4}\,n^{-1/2}\log n. \tag{3}
$$
It will be convenient to write
$$
N=n^{1/3}.
$$
Then (3) becomes
$$
A_n\sim\frac{3\sqrt\pi}{4}(\log N)N^{-3/2}. \tag{4}
$$

Step 3: Locate the moving saddle in $J_n$

Using (2) again and then $t=z/N$,
$$
J_n
=\frac1N\int_0^N(\log N-\log z)
\left(1-2^{1/3}z\right)^5e^{-N\Phi(z)}\,dz, \tag{5}
$$
where
$$
\Phi(z)=z^2+\frac1z.
$$
Now
$$
\Phi'(z)=2z-\frac1{z^2},
$$
so the unique critical point on $(0,\infty)$ is
$$
r=2^{-1/3}.
$$
It is the unique minimum, with
$$
c:=\Phi(r)=\frac{3}{2^{2/3}},
\qquad
\Phi''(r)=6,
\qquad
\Phi'''(r)=-6\,2^{4/3}. \tag{6}
$$
The amplitude in (5) has a fifth-order zero at the same point:
$$
\left(1-2^{1/3}z\right)^5
=-2^{5/3}(z-r)^5. \tag{7}
$$
This is the decisive cancellation.

Set
$$
z=r+\frac{u}{\sqrt N}.
$$
Taylor expansion of the phase gives
$$
N\bigl(\Phi(z)-c\bigr)
=3u^2+\frac{\Phi'''(r)}{6\sqrt N}u^3
+O\!\left(\frac{u^4}{N}\right).
$$
Hence, uniformly for $|u|\leq N^{1/10}$,
$$
e^{-N(\Phi(z)-c)}
=e^{-3u^2}\left[
1-\frac{\Phi'''(r)}{6\sqrt N}u^3
+O\!\left(\frac{u^4+u^6}{N}\right)
\right]. \tag{8}
$$
Also, by (7),
$$
\left(1-2^{1/3}z\right)^5
=-\frac{2^{5/3}u^5}{N^{5/2}}. \tag{9}
$$
The product of the leading terms in (8) and (9) is odd in $u$, so its integral over the asymptotically symmetric saddle neighborhood vanishes. The first nonzero term is obtained by multiplying (9) by the cubic correction in (8). Its coefficient is
$$
(-2^{5/3})\left(-\frac{\Phi'''(r)}6\right)=-8. \tag{10}
$$
Moreover
$$
\log N-\log z=\log N+O(1)+O\!\left(\frac{|u|}{\sqrt N}\right)
$$
near the saddle. Thus only the $\log N$ part contributes to the leading coefficient.

The contribution outside a fixed neighborhood of $r$ is exponentially smaller because $r$ is the unique minimum of $\Phi$. Inside that neighborhood, (8) gives a Gaussian majorant, so the expansion may be integrated term by term. Using
$$
\int_{-\infty}^{\infty}u^8e^{-3u^2}\,du
=\frac{35\sqrt\pi}{432\sqrt3},
$$
we obtain from (5), (8), (9), and (10)
$$
J_n
\sim
-8(\log N)e^{-cN}N^{-9/2}
\int_{-\infty}^{\infty}u^8e^{-3u^2}\,du.
$$
Therefore
$$
J_n
\sim
-\frac{35\sqrt\pi}{54\sqrt3}
(\log N)N^{-9/2}
\exp\!\left(-\frac{3}{2^{2/3}}N\right). \tag{11}
$$

Step 4: Recover the root and identify all three constants

Combining (4) and (11),
$$
\frac{J_n}{A_n}
\sim
-\frac{70}{81\sqrt3}
N^{-3}
\exp\!\left(-\frac{3}{2^{2/3}}N\right).
$$
Since $N^3=n$,
$$
-\frac{J_n}{A_n}
\sim
\frac{70}{81\sqrt3}\,
\frac1n
\exp\!\left(-\frac{3}{2^{2/3}}n^{1/3}\right). \tag{12}
$$
The right side tends to $0$, so from (1) and $\operatorname{arsinh}u\sim u$,
$$
\lambda_n
\sim
\frac{70}{81\sqrt3}\,
\frac1n
\exp\!\left(-\frac{3}{2^{2/3}}n^{1/3}\right).
$$
Hence the unique constants are
$$
\alpha=1,
\qquad
c=\frac{3}{2^{2/3}},
\qquad
L=\frac{70}{81\sqrt3}.
$$
Final Answer: $\boxed{\left(1,\frac{3}{2^{2/3}},\frac{70}{81\sqrt3}\right)}$

---

## Answer

$\left(1,\frac{3}{2^{2/3}},\frac{70}{81\sqrt3}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- product-integral reduction
- logarithmic density
- moving-saddle asymptotics
- high-order saddle cancellation
- implicit root asymptotics

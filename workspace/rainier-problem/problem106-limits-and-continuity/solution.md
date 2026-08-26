## Steps

Step 1: Replace the one-parameter limits by a compact torus fiber.

The numbers $1,\sqrt{2},\sqrt{3}$ are linearly independent over $\mathbb{Q}$. To see this, suppose $p+q\sqrt{2}+r\sqrt{3}=0$ for integers $p,q,r$. If $r\ne 0$, squaring $r\sqrt{3}=-(p+q\sqrt{2})$ gives
$$
3r^2=p^2+2q^2+2pq\sqrt{2},
$$
so $pq=0$. The cases $p=0$ and $q=0$ would respectively give $3r^2=2q^2$ and $3r^2=p^2$, both impossible by comparing prime valuations; if $r=0$, irrationality of $\sqrt{2}$ gives $p=q=0$. This leaves, for every nonzero $k\in\mathbb{Z}^{3}$,
$$
k_1+k_2\sqrt{2}+k_3\sqrt{3}\ne 0.
$$
For $\omega=k_1+k_2\sqrt{2}+k_3\sqrt{3}\ne 0$, the relevant character average is
$$
\frac{1}{T}\int_0^T e^{i\omega t}\,dt
=\frac{e^{i\omega T}-1}{i\omega T}\longrightarrow 0.
$$
The same calculation works on every interval beginning at a fixed positive time. The trigonometric-polynomial form of the Weyl criterion then shows that
$$
t\longmapsto(e^{it},e^{i\sqrt{2}t},e^{i\sqrt{3}t})
$$
is dense in the three-dimensional unit torus. Every tail of this orbit is also dense.

Put
$$
\lambda_1=e^{it},\quad \lambda_2=e^{i\sqrt{2}t},\quad \lambda_3=e^{i\sqrt{3}t},\quad
\lambda_4=e^{-i(1+\sqrt{2}+\sqrt{3})t}.
$$
Then $|\lambda_j|=1$ and $\lambda_1\lambda_2\lambda_3\lambda_4=1$. Density and compactness show that the possible joint cluster points of $(A(t),B(t))$ are exactly
$$
\left(\sum_{j=1}^{4}\lambda_j,\sum_{j=1}^{4}\lambda_j^2\right)
$$
over all unit complex numbers $\lambda_j$ with product $1$. The assertion includes the converse: after choosing any three of the $\lambda_j$, density supplies arbitrarily large $t$ approaching them, and the fourth coordinate follows from the product condition.

Step 2: Express the conditional fiber by one real coefficient.

Set $z=a(1+i)$ and suppose that the first sum is $z$. Let
$$
s=\sum_{1\leq j<k\leq 4}\lambda_j\lambda_k.
$$
Since the product of the four roots is $1$,
$$
\overline{s}
=\sum_{j<k}\frac{1}{\lambda_j\lambda_k}
=\sum_{j<k}\lambda_j\lambda_k=s,
$$
where complementation permutes the six pairs. So $s$ is real. Newton's identity gives
$$
\sum_{j=1}^{4}\lambda_j^2=z^2-2s=2ia^2-2s.
$$

Conversely, a real number $s$ occurs precisely when all four roots of
$$
q_s(w)=w^4-zw^3+sw^2-\overline{z}w+1
$$
lie on the unit circle. In that case its coefficients give product $1$, first sum $z$, and second power sum $z^2-2s$; Step 1 realizes the resulting ordered roots by a sequence tending to infinity. The remaining task is to find the exact interval of such $s$.

Step 3: Count the unit-circle roots without solving the quartic.

For $w=e^{i\theta}$, division by $e^{2i\theta}$ gives
$$
e^{-2i\theta}q_s(e^{i\theta})
=s-h(\theta),
$$
where
$$
h(\theta)=2a(\cos\theta-\sin\theta)-2\cos 2\theta.
$$
Therefore all four roots of $q_s$ lie on the unit circle exactly when the level equation $h(\theta)=s$ has four solutions on one period, counted with multiplicity.

Write
$$
u=\cos\theta+\sin\theta,
\qquad v=\cos\theta-\sin\theta.
$$
Then $u^2+v^2=2$, $h=2v(a-u)$, and differentiation gives
$$
h'(\theta)=2(2u^2-au-2).
$$
Let
$$
D=\sqrt{a^2+16},
\qquad u_+=\frac{a+D}{4},
\qquad u_-=\frac{a-D}{4}.
$$
For $0<a<\sqrt{2}$, both $u_\pm$ lie strictly between $-\sqrt{2}$ and $\sqrt{2}$. Also, $D^2-9a^2=16-8a^2>0$, so $a<u_+$. Each value of $u$ occurs at two critical points, with opposite values of $v$. The corresponding critical levels are $\pm c_+$ and $\pm c_-$, where
$$
c_+=2(u_+-a)\sqrt{2-u_+^2},
\qquad
c_-=2(a-u_-)\sqrt{2-u_-^2}.
$$
Substitution of $u_\pm$ gives
$$
c_-^2-c_+^2
=4\left[\left(\frac{3a+D}{4}\right)^2\left(2-\frac{(a-D)^2}{16}\right)
-\left(\frac{D-3a}{4}\right)^2\left(2-\frac{(a+D)^2}{16}\right)\right]
=\frac{aD^3}{4}>0.
$$
The parametrization
$$
(u,v)=\left(\sqrt{2}\cos\left(\theta-\frac{\pi}{4}\right),-\sqrt{2}\sin\left(\theta-\frac{\pi}{4}\right)\right)
$$
shows that the critical pairs occur in cyclic order
$$
(u_+,v>0),\ (u_+,v<0),\ (u_-,v<0),\ (u_-,v>0).
$$
Their corresponding values of $h$ are $-c_+,c_+,-c_-,c_-$. Between consecutive critical points the function is strictly monotone. A horizontal level meets the graph four times, with tangencies counted twice, exactly for
$$
|s|\leq c_+.
$$
For $c_+<|s|\leq c_-$ it meets the graph only twice when multiplicity is counted, and beyond $c_-$ it does not meet it. This proves both necessity and sufficiency for all four roots of $q_s$ to lie on the unit circle.

Step 4: Simplify the endpoint and state the cluster set.

The identities
$$
u_+-a=\frac{D-3a}{4},
\qquad
2-u_+^2=\frac{8-a^2-aD}{8}
$$
give
$$
2c_+=(D-3a)\sqrt{\frac{8-a^2-aD}{8}}.
$$
Since every possible limit has the form $L=2ia^2-2s$, the condition $|s|\leq c_+$ gives the claimed horizontal segment.

Final Answer: $\boxed{\{2ia^2+r:r\in\mathbb{R},|r|\leq(\sqrt{a^2+16}-3a)\sqrt{\frac{8-a^2-a\sqrt{a^2+16}}{8}}\}}$

---

## Answer

$\{2ia^2+r:r\in\mathbb{R},|r|\leq(\sqrt{a^2+16}-3a)\sqrt{\frac{8-a^2-a\sqrt{a^2+16}}{8}}\}$

---

## Classification

Problem Type: Exhaustive enumeration

Answer Type: Interval or region description

---

## Solution Concepts

- dense torus orbits
- elementary symmetric polynomials
- self-inversive quartics
- critical-level analysis

---

## Black-Box Audit

No issues found.

## Steps

Step 1: Replace the one-parameter limits by a compact torus fiber.

The numbers $1,\sqrt{2},\sqrt{3}$ are linearly independent over $\mathbb{Q}$. To see this, suppose $p+q\sqrt{2}+r\sqrt{3}=0$ for integers $p,q,r$. If $r\ne 0$, squaring $r\sqrt{3}=-(p+q\sqrt{2})$ gives
$$
3r^2=p^2+2q^2+2pq\sqrt{2},
$$
so $pq=0$. The cases $p=0$ and $q=0$ would respectively give $3r^2=2q^2$ and $3r^2=p^2$, both impossible by comparing prime valuations; if $r=0$, irrationality of $\sqrt{2}$ gives $p=q=0$. Thus, for every nonzero $k=(k_1,k_2,k_3)\in\mathbb{Z}^3$,
$$
\omega_k=k_1+k_2\sqrt{2}+k_3\sqrt{3}\ne 0.
$$
For every fixed $S\ge 0$,
$$
\frac1T\int_S^{S+T}e^{i\omega_k t}\,dt
=e^{i\omega_k S}\frac{e^{i\omega_k T}-1}{i\omega_k T}\longrightarrow 0.
$$
Hence, if
$$
P(\theta_1,\theta_2,\theta_3)=\sum_{k\in F}c_ke^{i(k_1\theta_1+k_2\theta_2+k_3\theta_3)}
$$
is any trigonometric polynomial, termwise integration gives
$$
\frac1T\int_S^{S+T}P(t,\sqrt2t,\sqrt3t)\,dt\longrightarrow c_0,
$$
and $c_0$ is exactly the normalized average of $P$ over the three-dimensional unit torus.

We now prove directly that every tail of
$$
t\longmapsto(e^{it},e^{i\sqrt2t},e^{i\sqrt3t})
$$
is dense. Fix a target $(e^{i\alpha_1},e^{i\alpha_2},e^{i\alpha_3})$ and a neighborhood of it. Choose $0<\delta<\pi$ so that the angular box
$$
d(\theta_j,\alpha_j)<\delta\qquad(j=1,2,3),
$$
where $d$ is circular distance modulo $2\pi$, lies inside that neighborhood. Put
$$
\rho=\frac{1+\cos\delta}{2}<1
$$
and, for a positive integer $N$, define the nonnegative trigonometric polynomial
$$
P_N(\theta_1,\theta_2,\theta_3)
=\prod_{j=1}^3\left(\frac{1+\cos(\theta_j-\alpha_j)}2\right)^N.
$$
The normalized one-dimensional average of each factor is
$$
\frac1{2\pi}\int_0^{2\pi}\left(\frac{1+\cos x}{2}\right)^Ndx
=\frac{\binom{2N}{N}}{4^N},
$$
so the torus average of $P_N$ is
$$
M_N=\left(\frac{\binom{2N}{N}}{4^N}\right)^3.
$$
Since $\binom{2N}{N}$ is the largest of the $2N+1$ coefficients in $(1+x)^{2N}$,
$$
\binom{2N}{N}\ge\frac{4^N}{2N+1},
$$
and therefore
$$
M_N\ge\frac1{(2N+1)^3}.
$$
Choose $N$ so large that $M_N>\rho^N$, which is possible because $0<\rho<1$. If some tail $t\ge S$ never entered the chosen angular box, then at each such $t$ at least one circular distance would be at least $\delta$, so $P_N(t,\sqrt2t,\sqrt3t)\le\rho^N$. Consequently
$$
\frac1T\int_S^{S+T}P_N(t,\sqrt2t,\sqrt3t)\,dt\le\rho^N
$$
for every $T>0$, whereas the trigonometric-polynomial average computed above says that the left side tends to $M_N>\rho^N$, a contradiction. Thus every tail is dense.

Put
$$
\lambda_1=e^{it},\quad \lambda_2=e^{i\sqrt{2}t},\quad \lambda_3=e^{i\sqrt{3}t},\quad
\lambda_4=e^{-i(1+\sqrt{2}+\sqrt{3})t}.
$$
Then $|\lambda_j|=1$ and $\lambda_1\lambda_2\lambda_3\lambda_4=1$. If $(A(t_n),B(t_n))$ converges along $t_n\to\infty$, compactness of the three-torus gives a subsequence on which $(\lambda_1,\lambda_2,\lambda_3)$ converges; the fourth coordinate then converges to the inverse of their product. Hence every joint cluster point has the form
$$
\left(\sum_{j=1}^{4}\lambda_j,\sum_{j=1}^{4}\lambda_j^2\right)
$$
for unit complex numbers $\lambda_j$ with product $1$. Conversely, given any such quadruple, density of every tail lets us choose $t_n\ge n$ with
$$
(e^{it_n},e^{i\sqrt2t_n},e^{i\sqrt3t_n})\longrightarrow(\lambda_1,\lambda_2,\lambda_3).
$$
Then
$$
e^{-i(1+\sqrt2+\sqrt3)t_n}
=\left(e^{it_n}e^{i\sqrt2t_n}e^{i\sqrt3t_n}\right)^{-1}
\longrightarrow(\lambda_1\lambda_2\lambda_3)^{-1}=\lambda_4,
$$
so the displayed pair is indeed realized as a joint cluster point.

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
Call these successive critical points $C_1,C_2,C_3,C_4$. Their corresponding values are
$$
h(C_1)=-c_+,\qquad h(C_2)=c_+,\qquad h(C_3)=-c_-,\qquad h(C_4)=c_-.
$$
Because there are no other critical points, $h$ is strictly monotone on the four open arcs between successive $C_j$. Thus the four successive arc ranges are
$$
[-c_+,c_+],\qquad [-c_-,c_+],\qquad [-c_-,c_-],\qquad [-c_+,c_-],
$$
with the directions respectively increasing, decreasing, increasing, decreasing.

The endpoint tangencies are genuinely quadratic. Since $u'=v$,
$$
h''(\theta)=2(4u-a)v.
$$
At $u=u_+$ we have $4u_+-a=D$, while at $u=u_-$ we have $4u_--a=-D$. Also $v\ne0$ at every critical point because $|u_\pm|<\sqrt2$. Hence $h''(C_j)\ne0$ for all four $j$. In particular, at the levels $s=\pm c_+$ the zero of $h(\theta)-s$ at the tangency has multiplicity exactly two.

Now count intersections arc by arc. If $|s|<c_+$, then $s$ lies in the interior of all four arc ranges, giving four distinct simple solutions. If $s=c_+$, the point $C_2$ is a double solution and there is one additional simple solution on each of the third and fourth arcs, for total multiplicity $2+1+1=4$. Similarly, if $s=-c_+$, the point $C_1$ is double and there is one simple solution on each of the second and third arcs, again giving total multiplicity four. For $c_+<|s|<c_-$ there are only two simple intersections. At $s=\pm c_-$ there is only the corresponding nondegenerate tangency, counted twice, and for $|s|>c_-$ there are no intersections. Therefore the level equation has four solutions on one period, counted with multiplicity, exactly when
$$
|s|\leq c_+.
$$
This proves both necessity and sufficiency for all four roots of $q_s$ to lie on the unit circle.

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

No issues found. Step 1 now contains a self-contained trigonometric-polynomial certificate for density of every tail of the torus orbit.

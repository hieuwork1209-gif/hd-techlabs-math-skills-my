## Steps

Step 1: Encode the centroid constraint by the cubic with the three vertices as roots
Let the unit circle be centered at the origin. Since only the distance of the centroid from the origin is prescribed, rotate the configuration so that the centroid is the real number $r$. Identify the plane with the complex plane and write the three vertices as $z_1,z_2,z_3$, where
$$
|z_1|=|z_2|=|z_3|=1,
\qquad
z_1+z_2+z_3=3r.
$$
Set
$$
s=3r,
\qquad
q=z_1z_2+z_2z_3+z_3z_1,
\qquad
p=z_1z_2z_3.
$$
Here $0<s<3$ and $|p|=1$. The unit-circle condition gives $\overline{z_i}=1/z_i$, so
$$
\overline{s}
=\frac1{z_1}+\frac1{z_2}+\frac1{z_3}
=\frac{q}{p}.
$$
Because $s$ is real, $q=sp$. Thus the three vertices are precisely the roots of
$$
f(z)=z^3-sz^2+spz-p.
$$
These coefficients are forced: the centroid gives the first elementary symmetric function, the unit-circle condition determines the second from the first and the product, and $p$ is the remaining unimodular parameter.

Step 2: Convert the area into the cubic discriminant and obtain the sharp bound
Let
$$
\Delta=(z_1-z_2)^2(z_2-z_3)^2(z_3-z_1)^2.
$$
For a monic cubic $z^3-sz^2+qz-p$, expanding this product gives
$$
\Delta=s^2q^2-4q^3-4s^3p-27p^2+18sqp.
$$
Substituting $q=sp$ yields
$$
\frac{\Delta}{p^2}
=s^4+18s^2-27-4s^3\left(p+p^{-1}\right).
$$
Write $p=e^{i\phi}$. Then
$$
\frac{\Delta}{p^2}
=s^4+18s^2-27-8s^3\cos\phi.
$$

We now relate this quantity to the Euclidean area $K$ of the triangle. If $z_j=e^{i\theta_j}$, then for each pair
$$
\frac{(z_i-z_j)^2}{z_iz_j}
=2\cos(\theta_i-\theta_j)-2
=-4\sin^2\left(\frac{\theta_i-\theta_j}{2}\right).
$$
For a nondegenerate triangle all three factors are negative, hence $\Delta/p^2<0$. Also the product of the three side lengths is
$$
|(z_1-z_2)(z_2-z_3)(z_3-z_1)|=\sqrt{|\Delta|}.
$$
For any triangle with side lengths $a,b,c$, area $K$, and circumradius $R$, the identity $K=abc/(4R)$ holds. Here $R=1$, so
$$
16K^2=|\Delta|=-\frac{\Delta}{p^2}.
$$
Therefore
$$
16K^2
=8s^3\cos\phi-s^4-18s^2+27
\leq 8s^3-s^4-18s^2+27.
$$
The right-hand side factors as
$$
8s^3-s^4-18s^2+27=(3-s)^3(s+1).
$$
Since $s=3r$,
$$
K\leq \frac14\sqrt{(3-3r)^3(1+3r)}
=\frac{3\sqrt3}{4}\sqrt{(1-r)^3(1+3r)}.
$$

Step 3: Construct a triangle attaining the bound
Equality in Step 2 is possible when $\cos\phi=1$, so take $p=1$. The cubic then factors as
$$
f(z)=z^3-sz^2+sz-1
=(z-1)\left(z^2+(1-s)z+1\right).
$$
Because $0<s<3$, we have $|1-s|<2$. Hence the two quadratic roots are distinct points on the unit circle:
$$
z_{\pm}=\frac{s-1}{2}\pm\frac{i}{2}\sqrt{4-(s-1)^2}.
$$
Together with $z_0=1$, their sum is $s=3r$, so their centroid is exactly $r$ after the normalization in Step 1.

The segment joining $z_+$ and $z_-$ has length $\sqrt{4-(s-1)^2}$, while its supporting vertical line has real coordinate $(s-1)/2$. Thus the altitude from $1$ is $(3-s)/2$, and the area is
$$
\frac12\cdot\sqrt{4-(s-1)^2}\cdot\frac{3-s}{2}
=\frac14\sqrt{(3-s)^3(s+1)}.
$$
This is exactly the upper bound from Step 2, so the maximum is attained.

Step 4: Classify all maximizing triangles
If a triangle attains the upper bound, equality must hold in the only inequality used in Step 2, namely $\cos\phi\leq1$. Hence $\cos\phi=1$. Since $|p|=1$, this forces $p=1$.

With $s=3r$ and $p=1$, the cubic having the three vertices as roots is forced uniquely:
$$
(z-1)\left(z^2+(1-3r)z+1\right).
$$
Thus, after rotating so that the centroid lies at $r>0$ on the real axis, the unordered vertex set is exactly
$$
\left\{
1,
\frac{3r-1}{2}+\frac{i}{2}\sqrt{4-(3r-1)^2},
\frac{3r-1}{2}-\frac{i}{2}\sqrt{4-(3r-1)^2}
\right\}.
$$
Equivalently, if $u$ is the unit vector from the circle center toward the centroid and $v$ is either unit vector perpendicular to $u$, every maximizing triangle has vertices
$$
u,
\qquad
\frac{3r-1}{2}u\pm\frac12\sqrt{4-(3r-1)^2}\,v.
$$
Changing the sign of $v$ only swaps the last two vertices. Hence these, up to rotation and permutation of the vertices, are all maximizers.

Final Answer: $\boxed{\frac{3\sqrt3}{4}\sqrt{(1-r)^3(1+3r)}}$

---

## Answer

$\frac{3\sqrt3}{4}\sqrt{(1-r)^3(1+3r)}$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- complex coordinates on the unit circle
- elementary symmetric polynomials
- cubic discriminant
- circumradius area formula
- equality-case reconstruction

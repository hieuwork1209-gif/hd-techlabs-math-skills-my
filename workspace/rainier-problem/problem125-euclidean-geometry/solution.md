## Steps

Step 1: Encode the triangle by a self-inversive cubic and express the area through its discriminant
Let the unit circle be centered at the origin. Write
$$
r=OG,
\qquad
K=\operatorname{Area}(ABC).
$$
For $r>0$, rotate the configuration so that the centroid is the positive real number $r$. If the vertices are $z_1,z_2,z_3$, then
$$
|z_1|=|z_2|=|z_3|=1,
\qquad
z_1+z_2+z_3=s,
\qquad
s=3r.
$$
Set
$$
q=z_1z_2+z_2z_3+z_3z_1,
\qquad
p=z_1z_2z_3.
$$
Since $\overline{z_j}=1/z_j$ and $s$ is real,
$$
s=\overline{s}
=\frac1{z_1}+\frac1{z_2}+\frac1{z_3}
=\frac{q}{p},
$$
so $q=sp$, while $|p|=1$. Hence the vertices are the roots of
$$
f(z)=z^3-sz^2+spz-p.
$$
The coefficients are forced by the centroid and unit-circle conditions; $p$ is the only remaining parameter.

For a monic cubic $z^3+az^2+bz+c$, the discriminant is
$$
a^2b^2-4b^3-4a^3c-27c^2+18abc.
$$
Applying this with $a=-s$, $b=sp$, $c=-p$ gives
$$
\Delta=(z_1-z_2)^2(z_2-z_3)^2(z_3-z_1)^2
$$
and
$$
D:=\frac{\Delta}{p^2}
=s^4-4s^3\left(p+p^{-1}\right)+18s^2-27.
$$
Write $p=e^{i\phi}$. Then
$$
D=s^4-8s^3\cos\phi+18s^2-27.
$$
For unit-circle points,
$$
\frac{(z_i-z_j)^2}{z_iz_j}
=-4\sin^2\left(\frac{\theta_i-\theta_j}{2}\right)
$$
when $z_j=e^{i\theta_j}$. Thus $D<0$ for a nondegenerate triangle. Moreover, if $a,b,c$ are its side lengths, then
$$
abc=|(z_1-z_2)(z_2-z_3)(z_3-z_1)|=\sqrt{|\Delta|}.
$$
For a triangle of circumradius $R$, $K=abc/(4R)$. Here $R=1$, so
$$
16K^2=|\Delta|=-D
=8s^3\cos\phi-s^4-18s^2+27.
$$

Step 2: Derive the two sharp inequalities that every attainable pair must satisfy
Because $-1\leq\cos\phi\leq1$, the identity from Step 1 gives
$$
-s^4-8s^3-18s^2+27
\leq16K^2\leq
-s^4+8s^3-18s^2+27.
$$
The endpoint polynomials factor as
$$
-s^4-8s^3-18s^2+27=(3+s)^3(1-s),
$$
$$
-s^4+8s^3-18s^2+27=(3-s)^3(1+s).
$$
Substituting $s=3r$ yields
$$
27(1+r)^3(1-3r)
\leq16K^2\leq
27(1-r)^3(1+3r).
$$
Also $K>0$ because the triangle is nondegenerate. Since the centroid is an average of three points of the closed unit disk, $r\leq1$; equality in the triangle inequality would force all three vertices to coincide, so in fact $r<1$. Thus every attainable pair satisfies
$$
0\leq r<1,
\qquad
K>0,
\qquad
27(1+r)^3(1-3r)\leq16K^2\leq27(1-r)^3(1+3r).
$$

Step 3: Prove that every pair satisfying the inequalities is actually attainable
First suppose $r=0$. The two inequalities coincide and force
$$
16K^2=27.
$$
An equilateral triangle on the unit circle has centroid at the origin and area $3\sqrt{3}/4$, so this unique admissible value is attained.

Now let $0<r<1$, set $s=3r$, and suppose $K>0$ satisfies the two inequalities. Define
$$
c=\frac{s^4+18s^2+16K^2-27}{8s^3}.
$$
The lower and upper inequalities are exactly $c\geq-1$ and $c\leq1$. Choose $\phi\in[0,\pi]$ with $\cos\phi=c$ and put $p=e^{i\phi}$. Then
$$
D=s^4-8s^3\cos\phi+18s^2-27=-16K^2<0.
$$
We must show that
$$
f(z)=z^3-sz^2+spz-p
$$
has three distinct roots on the unit circle.

If $\phi=0$, then $p=1$ and
$$
f(z)=(z-1)\left(z^2+(1-s)z+1\right).
$$
Since $0<s<3$, $|1-s|<2$. Hence the quadratic has two distinct conjugate roots of modulus $1$, and all three roots lie on the unit circle.

Assume now $0<\phi\leq\pi$ and set $\alpha=\phi/3$. Write $z=e^{i\alpha}w$. After division by $e^{3i\alpha}$, $f(z)=0$ becomes
$$
g(w)=w^3-se^{-i\alpha}w^2+se^{i\alpha}w-1=0.
$$
Use the Cayley parametrization
$$
w=\frac{x+i}{x-i}.
$$
For real $x$, this has modulus $1$. The identities
$$
(x+i)^3-(x-i)^3=2i(3x^2-1),
$$
$$
(x+i)^2(x-i)=x^3+x+i(x^2+1)
$$
with the conjugate identity for $(x+i)(x-i)^2$ give
$$
(x-i)^3g\left(\frac{x+i}{x-i}\right)=2iH(x),
$$
where
$$
H(x)=s\sin\alpha\,x^3+(3-s\cos\alpha)x^2+s\sin\alpha\,x-(1+s\cos\alpha).
$$
For a real cubic $Ax^3+Bx^2+Cx+D_0$, the discriminant is
$$
B^2C^2-4AC^3-4B^3D_0-27A^2D_0^2+18ABCD_0.
$$
Here
$$
A=C=s\sin\alpha,
\qquad
B=3-s\cos\alpha,
\qquad
D_0=-(1+s\cos\alpha).
$$
Writing $u=\sin\alpha$ and $v=\cos\alpha$, substitution gives
$$
\operatorname{disc}(H)
=s^2u^2(3-sv)^2-4s^4u^4
+4(3-sv)^3(1+sv)
-27s^2u^2(1+sv)^2
-18s^2u^2(3-sv)(1+sv).
$$
Expanding the five displayed terms and collecting powers of $s$ gives
$
\operatorname{disc}(H)
=108-72s^2(u^2+v^2)
+32s^3\left(v^3-3vu^2\right)
-4s^4(u^2+v^2)^2.
$
Using $u^2+v^2=1$, this becomes
$
\operatorname{disc}(H)
=108-72s^2+32s^3\left(v^3-3vu^2\right)-4s^4
=-4\left[s^4-8s^3\left(v^3-3vu^2\right)+18s^2-27\right].
$
Since $v^3-3vu^2=\cos(3\alpha)=\cos\phi$,
$$
\operatorname{disc}(H)=-4D=64K^2>0.
$$
If the three roots of a real cubic are $x_1,x_2,x_3$, its discriminant is
$$
A^4(x_1-x_2)^2(x_1-x_3)^2(x_2-x_3)^2.
$$
A real cubic has either three real roots or one real root and a nonreal conjugate pair; in the latter case the factor $(x_2-x_3)^2$ is a negative real number while the other two squared factors have positive product, so the discriminant is negative. Thus positive discriminant is equivalent to three distinct real roots. Hence $H$ has three distinct real roots $x_1,x_2,x_3$, producing three distinct unit-modulus roots
$$
z_j=e^{i\alpha}\frac{x_j+i}{x_j-i}
$$
of $f$. Their sum is $s$, so their centroid has distance $r=s/3$ from the origin. Finally $D=-16K^2$ and the area-discriminant identity from Step 1 show that the resulting triangle has area exactly $K$. Therefore every pair satisfying the inequalities is attainable.

Step 4: Classify all triangles attaining the upper sharp boundary
Equality in the upper inequality is equivalent to $\cos\phi=1$. After the rotation used in Step 1 this forces $p=1$, so
$$
f(z)=(z-1)\left(z^2+(1-3r)z+1\right).
$$
Thus for $0<r<1$ every upper-boundary triangle has, after rotation, the unordered vertex set
$$
\left\{
1,
\frac{3r-1}{2}+\frac{i}{2}\sqrt{4-(3r-1)^2},
\frac{3r-1}{2}-\frac{i}{2}\sqrt{4-(3r-1)^2}
\right\}.
$$
Conversely these three points lie on the unit circle, have centroid distance $r$, and attain
$$
16K^2=27(1-r)^3(1+3r).
$$
For $r=0$, the upper and lower bounds coincide and the boundary configuration is an equilateral triangle. Hence the upper-boundary triangles are unique up to rotation, reflection, and permutation of the vertices.

Step 5: Classify the lower sharp boundary and state the full feasible region
Equality in the lower inequality is equivalent to $\cos\phi=-1$. Since $K>0$, the lower right-hand side must be positive, so necessarily $0\leq r<1/3$. For $0<r<1/3$, after rotating as in Step 1 we have $p=-1$ and
$$
f(z)=z^3-3rz^2-3rz+1
=(z+1)\left(z^2-(1+3r)z+1\right).
$$
Because $1+3r<2$, the quadratic has two distinct unit-circle roots. Hence every lower-boundary triangle has, after rotation, the unordered vertex set
$$
\left\{
-1,
\frac{1+3r}{2}+\frac{i}{2}\sqrt{4-(1+3r)^2},
\frac{1+3r}{2}-\frac{i}{2}\sqrt{4-(1+3r)^2}
\right\}.
$$
Conversely this configuration attains
$$
16K^2=27(1+r)^3(1-3r).
$$
At $r=0$ it is again equilateral, up to rotation. At $r\geq1/3$, the algebraic lower bound is nonpositive and cannot be attained by a nondegenerate triangle; the condition $K>0$ is the true lower edge there, but it is not attained.

Combining necessity, sufficiency, and the equality classifications gives the exact set of possible pairs $(r,K)$.

Final Answer: $\boxed{\{(r,K):0\leq r<1,\ K>0,\ 27(1+r)^3(1-3r)\leq16K^2\leq27(1-r)^3(1+3r)\}}$

---

## Answer

$\{(r,K):0\leq r<1,\ K>0,\ 27(1+r)^3(1-3r)\leq16K^2\leq27(1-r)^3(1+3r)\}$

---

## Classification

**Problem Type:** Exhaustive enumeration

**Answer Type:** Interval or region description

---

## Solution Concepts

- complex coordinates on the unit circle
- self-inversive cubic
- cubic discriminant
- Cayley transform
- equality-case reconstruction

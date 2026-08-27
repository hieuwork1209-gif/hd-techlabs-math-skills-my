## Steps

Step 1: Reduce the alternating recurrence to two scalar inequalities

Fix $s\geq0$ and abbreviate $R=R_{a,b}(s)$ and $c=3/25$. Then
$$
v_{2k}=C_s^k v_0,\qquad v_{2k+1}=A_sC_s^k v_0,
$$
where
$$
C_s=B_sA_s
=
\begin{pmatrix}
R&cRs\\
-cs&R-c^2s^2
\end{pmatrix}.
$$
Thus the alternating recurrence is bounded for every $v_0$ exactly when $C_s$ is power bounded.

The characteristic polynomial of $C_s$ is
$$
p_s(\lambda)
=
\lambda^2-(2R-c^2s^2)\lambda+R^2.
$$
For a real monic quadratic with product of roots $D\in[0,1]$, its roots lie in the closed unit disk exactly when its values at $1$ and $-1$ are nonnegative. Indeed, nonreal roots are conjugate and have modulus $\sqrt D\leq1$; for real roots, a root outside $[-1,1]$ makes one of the endpoint values negative unless both roots lie beyond the same endpoint, which would force $D>1$.

Here
$$
p_s(1)=(1-R)^2+c^2s^2,
\qquad
p_s(-1)=(1+R)^2-c^2s^2.
$$
Hence, for $0<s<50/3$, all roots lie in the closed unit disk exactly when
$$
cs-1\leq R\leq1. \tag{1}
$$
There is no defective unit-root case under (1): if $p_s(-1)=0$, then $-1$ is simple unless $R=1$ and $cs=2$, excluded by $s<50/3$; if $R=1$, the two unit roots are distinct for $0<cs<2$. At $s=0$, $C_0=I$.

Therefore, on every interval contained in $[0,50/3)$, boundedness is equivalent to (1). Put
$$
P(s):=1-R_{a,b}(s)=s-as^2-bs^3.
$$
Then (1) becomes the pair of inequalities
$$
0\leq P(s)\leq 2-\frac{3s}{25}. \tag{2}
$$

Step 2: Prove the sharp upper bound by a hidden interpolation identity

For every cubic of the form
$$
P(s)=s+\alpha s^2+\beta s^3,
$$
the following identity holds:
$$
3P\left(\frac{25}{6}\right)
-\frac{48}{25}P\left(\frac{125}{12}\right)
+P\left(\frac{25}{2}\right)
=5. \tag{3}
$$
This follows by substituting $P$: the displayed weights annihilate both the $s^2$ and $s^3$ terms, while their weighted sum on the linear term is $5$.

Suppose $\rho(a,b)>25/2$. Since admissible lengths are downward closed, there is an admissible interval longer than $25/2$ but still shorter than $50/3$. Applying (2) at
$$
x_1=\frac{25}{6},\qquad
x_2=\frac{125}{12},\qquad
x_3=\frac{25}{2},
$$
gives
$$
P(x_1)\leq\frac32,\qquad
P(x_2)\geq0,\qquad
P(x_3)\leq\frac12.
$$
Using these in (3),
$$
5
=
3P(x_1)-\frac{48}{25}P(x_2)+P(x_3)
\leq
3\cdot\frac32+\frac12
=5.
$$
Thus equality must hold in all three inequalities:
$$
P(x_1)=\frac32,\qquad P(x_2)=0,\qquad P(x_3)=\frac12. \tag{4}
$$
The unique cubic with fixed linear coefficient $1$ satisfying (4) is
$$
P_*(s)
=
s\left(1-\frac{12s}{125}\right)^2
=
s-\frac{24}{125}s^2+\frac{144}{15625}s^3. \tag{5}
$$
For this polynomial,
$$
2-\frac{3s}{25}-P_*(s)
=
\frac{2(25-2s)(6s-25)^2}{15625}. \tag{6}
$$
The right side is negative for every $s>25/2$ sufficiently close to $25/2$, contradicting (2). Therefore
$$
\rho(a,b)\leq\frac{25}{2}
$$
for every pair $(a,b)$.

Step 3: Construct and verify the extremizer

Take
$$
a_*=\frac{24}{125},
\qquad
b_*=-\frac{144}{15625}.
$$
Then (5) gives
$$
1-R_{a_*,b_*}(s)
=
\frac{s(12s-125)^2}{15625}\geq0.
$$
Also, by (6),
$$
R_{a_*,b_*}(s)-\frac{3s}{25}+1
=
\frac{2(25-2s)(6s-25)^2}{15625}\geq0
\qquad
\left(0\leq s\leq\frac{25}{2}\right).
$$
Hence
$$
\frac{3s}{25}-1
\leq
R_{a_*,b_*}(s)
\leq1
\qquad
\left(0\leq s\leq\frac{25}{2}\right).
$$
Since $25/2<50/3$, Step 1 shows that the alternating recurrence is bounded for every initial vector throughout this interval. Thus
$$
\rho(a_*,b_*)\geq\frac{25}{2}.
$$
Together with Step 2,
$$
\rho_*=\frac{25}{2}.
$$

Step 4: Prove uniqueness

Suppose $\rho(a,b)=25/2$. Every interval $[0,L]$ with $L<25/2$ is admissible. Hence (2) holds at $x_1$ and $x_2$, and by continuity it also holds at $x_3=25/2$. Applying the identity (3) again forces equality in all three bounds, so (4) holds.

As in Step 2, these values uniquely determine
$$
P(s)=P_*(s)
=
s-\frac{24}{125}s^2+\frac{144}{15625}s^3.
$$
Since $P(s)=s-as^2-bs^3$, this forces
$$
a=\frac{24}{125},
\qquad
b=-\frac{144}{15625}.
$$
Therefore the maximizing pair is unique.

Final Answer: $\boxed{(\frac{25}{2},\frac{24}{125},-\frac{144}{15625})}$

## Answer

$(\frac{25}{2},\frac{24}{125},-\frac{144}{15625})$

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

## Solution Concepts

- two-step monodromy matrix
- direct unit-disk root criterion
- sharp interpolation certificate
- equality-case rigidity

## Black-Box Audit

The matrix power-boundedness criterion is derived directly from the characteristic quadratic, including the unit-root cases. The sharp upper bound comes from the explicit interpolation identity (3), and the extremizer is verified by the factorizations (5) and (6). No optimization theorem, root-location black box, or numerical search is used.

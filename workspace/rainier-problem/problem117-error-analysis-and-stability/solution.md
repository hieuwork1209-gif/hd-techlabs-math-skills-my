## Steps

Step 1: Reduce the alternating BDF5 recurrence to a two-phase Floquet determinant

For one phase, scale the current step to length (1) and write the other step ratio as (ho>0). The five backward distances are
$$
H(ho)=(1,1+ho,2+ho,2+2ho,3+2ho).
$$
After translating the current time to (0), the derivative weights are
$$
w_0(ho)=sum_{m=1}^{5}rac{1}{H_m},
$$
and, for (1leq jleq5),
$$
w_j(ho)=
-rac{prod_{substack{1leq mleq5\m
e j}}H_m}
{H_jprod_{substack{1leq mleq5\m
e j}}(H_m-H_j)}.
$$
For (y'=0),
$$
sum_{j=0}^{5}w_j(ho)y_{n-j}=0.
$$
Since the weights annihilate constants, (sum_{j=0}^{5}w_j(ho)=0). Thus for (d_n=y_n-y_{n-1}),
$$
d_n=sum_{k=1}^{4}eta_k(ho)d_{n-k},
qquad
eta_k(ho)=rac{sum_{j=k+1}^{5}w_j(ho)}{w_0(ho)}.
$$

The two alternating phases are (ho=r) and (ho=1/r). For a two-step Floquet multiplier (z), write
$$
d_{2m}=a z^m,qquad d_{2m+1}=b z^m.
$$
Substitution into the two phase recurrences gives the homogeneous system
$$
egin{pmatrix}
z^2-eta_2(r)z-eta_4(r) & -eta_1(r)z-eta_3(r)\
-eta_1(1/r)z^2-eta_3(1/r)z &
z^2-eta_2(1/r)z-eta_4(1/r)
end{pmatrix}
inom{a}{b}=0.
$$
Hence the parasitic period multipliers are exactly the zeros of this (2	imes2) determinant.

Step 2: Convert the Floquet determinant to a compact Hurwitz polynomial

Put
$$
u=r+rac1r,qquad s=u+2.
$$
Interchanging (r) and (1/r) only swaps the two phases, so the determinant from Step 1 is reciprocal-symmetric in (r). Substitute the product formula for the weights into that single determinant, clear the nonzero common denominator, and use
$$
r^2+r^{-2}=u^2-2,qquad
r^3+r^{-3}=u^3-3u.
$$
With the Cayley variable
$$
z=rac{1+x}{1-x},
$$
the resulting polynomial, up to a nonzero scalar factor, is
$$
q_s(x)=4D(s)x^4+2C(s)x^3+B(s)x^2+A(s)x+60s^3,
$$
where
$$
D(s)=-4s^3+32s^2+15s+1,
$$
$$
C(s)=2s^3+176s^2+63s+4,
$$
$$
B(s)=116s^3+372s^2+106s+5,
$$
$$
A(s)=156s^3+132s^2+32s+1.
$$
This reduction is a direct polynomial identity from the (2	imes2) determinant; the reciprocal pairing above is the only simplification used.

Since (s=u+2),
$$
D(s)=-(4u^3-8u^2-95u-127).
$$
Let
$$
F(u)=4u^3-8u^2-95u-127.
$$
Now
$$
F(6)=-121,qquad Fleft(rac{13}{2}ight)=16.
$$
Also
$$
F'(u)=12u^2-16u-95
$$
has exactly one positive zero, smaller than (6). Therefore (F) decreases and then increases on (ugeq2), so it has a unique zero (u_*) in ((6,13/2)), and (D(s)>0) exactly for (2leq u<u_*).

Step 3: Prove Hurwitz stability without any high-degree expansion

Assume (2leq u<u_*). Then
$$
4leq s<rac{17}{2},
$$
and (A,B,C,D) are positive. Four short inequalities control the two quartic Hurwitz determinants.

First,
$$
C-10D=42s^3-144s^2-87s-6.
$$
Its value at (s=4) is (30), and its derivative is positive for (sgeq4), so (C>10D).

Second,
$$
10B-9A=s^2(2532-244s)+772s+41>0
$$
because (s<17/2). Hence (B>rac9{10}A). Therefore
$$
CB>9DA>8DA.
$$

Third,
$$
A-3C=150s^3-396s^2-157s-11.
$$
Its value at (s=4) is (2625), and its derivative is positive for (sgeq4), so (A>3C).

Finally,
$$
B-160s^3=s^2(372-44s)+106s+5.
$$
Since (s<17/2), the right-hand side is larger than
$$
-2s^2+106s+5>0.
$$
Thus
$$
AB>480Cs^3.
$$

For
$$
q_s(x)=a_4x^4+a_3x^3+a_2x^2+a_1x+a_0,
$$
the coefficients are
$$
(a_4,a_3,a_2,a_1,a_0)=(4D,2C,B,A,60s^3).
$$
The quartic Routh-Hurwitz conditions reduce to
$$
a_3a_2-a_4a_1=2CB-4DA>0
$$
and
$$
a_3a_2a_1-a_4a_1^2-a_3^2a_0
=
2left(CBA-2DA^2-120C^2s^3ight).
$$
From (CB>8DA),
$$
2DA^2<rac14 CBA,
$$
and from (AB>480Cs^3),
$$
120C^2s^3<rac14 CBA.
$$
Hence the second Hurwitz determinant is positive as well. All roots of (q_s) therefore satisfy (operatorname{Re}x<0). The Cayley map then gives (|z|<1), so every parasitic period multiplier is strictly inside the unit disk for (2leq u<u_*).

Step 4: Include the boundary and exclude all larger step ratios

At (u=u_*), (D=0), so (q_s) drops from degree (4) to degree (3) and its cubic leading coefficient is (2C>0). Because
$$
z+1=rac{2}{1-x},
$$
a loss of exactly one degree in ((1-x)^4) times the period characteristic polynomial means that (z=-1) is a simple period multiplier.

The remaining three roots are still strictly stable. Indeed the cubic Hurwitz condition is
$$
BA>(2C)(60s^3)=120Cs^3,
$$
which follows from the stronger inequality (AB>480Cs^3) established in Step 3. Thus the endpoint is zero-stable and its only parasitic unit-circle multiplier is (-1).

For (u>u_*), (D<0). Since
$$
q_s(0)=60s^3>0
$$
while the leading coefficient (4D) is negative, (q_s(x)	o-infty) as (x	o+infty). Therefore (q_s) has a positive real zero. Under
$$
z=rac{1+x}{1-x},
$$
every positive real (x) gives (|z|>1), so zero-stability fails.

Finally, the full two-step state can be written as one base value together with four consecutive first differences. Its period matrix is block upper triangular with diagonal blocks ([1]) and the first-difference monodromy. Since (q_s(0)>0), (z=1) is not a parasitic multiplier; at the boundary (z=-1) is simple. Hence every unit-modulus multiplier is semisimple.

Step 5: Recover the stable interval and the requested scalar

For (r>0),
$$
u=r+rac1rgeq2.
$$
The result of Step 4 gives zero-stability exactly when
$$
2leq uleq u_*.
$$
Equivalently,
$$
r_-leq rleq r_+,
qquad
r_pm=rac{u_*pmsqrt{u_*^2-4}}{2},
qquad
r_-r_+=1.
$$
At (r=r_-), the parasitic period multiplier on the unit circle is (-1). Since (u_*) is the unique zero of (F) in ((6,7)),
$$
u_*=operatorname{root}_{(6,7)}(4x^3-8x^2-95x-127).
$$

Final Answer: $\boxed{\operatorname{root}_{(6,7)}(4x^3-8x^2-95x-127)}$

---

## Answer

$\operatorname{root}_{(6,7)}(4x^3-8x^2-95x-127)$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Exact scalar

---

## Solution Concepts

- variable-step backward differentiation formulas
- floquet multipliers
- cayley transform
- routh-hurwitz stability criterion
- reciprocal step-ratio symmetry

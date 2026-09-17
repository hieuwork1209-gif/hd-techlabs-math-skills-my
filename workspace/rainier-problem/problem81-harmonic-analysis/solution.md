## Steps

Step 1: Convert the sixth moment to a finite convolution energy

Write
\[
f(\theta)=a(1+e^{6i\theta})+b(e^{i\theta}+e^{5i\theta})+c(e^{2i\theta}+e^{4i\theta}),
\]
so its coefficient vector is
\[
(d_0,\ldots,d_6)=(a,b,c,0,c,b,a).
\]
The normalization is
\[
2(a^2+b^2+c^2)=1.
\tag{1}
\]
Since \(|f|^6=|f^3|^2\), Parseval gives
\[
\frac1{2\pi}\int_0^{2\pi}|f(\theta)|^6\,d\theta
=\sum_{k=0}^{18}\left(\sum_{i+j+\ell=k}d_i d_j d_\ell\right)^2.
\tag{2}
\]
Expanding (2) and collecting terms gives
\[
\begin{aligned}
E_6(a,b,c):={}&\frac1{2\pi}\int|f|^6\\
={}&20a^6+180a^4b^2+180a^4c^2+360a^3b^2c+120a^3c^3\\
&+180a^2b^4+900a^2b^2c^2+180a^2c^4\\
&+240ab^4c+600ab^2c^3+60ac^5\\
&+20b^6+180b^4c^2+210b^2c^4+20c^6.
\end{aligned}
\tag{3}
\]

Step 2: Reduce the signs and isolate the boundary

Every sign-sensitive term in (3) is a positive coefficient times an odd power of both \(a\) and \(c\). Hence replacing \((a,c)\) by \((|a|,|c|)\) cannot decrease the objective, while the sign of \(b\) is irrelevant. Thus at an interior maximizer we may assume
\[
a\ge0,\qquad c>0.
\]

The boundary \(c=0\) is far from optimal. Indeed, with \(a^2+b^2=1/2\), (3) becomes
\[
E_6=20(a^2+b^2)(a^4+8a^2b^2+b^4)
\le \frac{25}{4}.
\tag{4}
\]
On the other hand the admissible choice \(p=7/8,\ v=1\) introduced below gives
\[
E_6=\frac{59501255}{3696822}>16,
\]
so every global maximizer has \(c\ne0\).

Step 3: Reduce to two nonnegative ratios

Put
\[
p=\frac ac\ge0,
\qquad
v=\frac{b^2}{c^2}\ge0.
\]
From (1),
\[
c^2=\frac1{2(p^2+v+1)}.
\tag{5}
\]
Substitution into (3) gives
\[
E_6=\frac54\,\frac{N(p,v)}{(p^2+v+1)^3},
\tag{6}
\]
where
\[
\begin{aligned}
N(p,v)={}&2p^6+18p^4v+18p^4+36p^3v+12p^3\\
&+18p^2v^2+90p^2v+18p^2+24pv^2+60pv+6p\\
&+2v^3+18v^2+21v+2.
\end{aligned}
\tag{7}
\]
Let
\[
F(p,v)=\frac{N(p,v)}{(p^2+v+1)^3}.
\]

Step 4: For each fixed \(p\), optimize uniquely in \(v\)

A calculation gives
\[
\partial_v F=\frac{3H(p,v)}{(p^2+v+1)^4},
\tag{8}
\]
with
\[
H(p,v)=C(p)-B(p)v-4(p+1)^2v^2,
\tag{9}
\]
where
\[
C(p)=4p^6+12p^5+18p^4+20p^3+19p^2+14p+5,
\]
\[
B(p)=8p^3+36p^2+24p+2.
\]
For every \(p\ge0\), both \(B(p)\) and \(C(p)\) are positive. Hence \(H(p,v)\) is strictly decreasing for \(v\ge0\), starts positive at \(v=0\), and tends to \(-\infty\). Thus there is a unique positive root \(v=v_p\), and it is the unique global maximizer of \(F(p,\cdot)\) on \([0,\infty)\).

Step 5: Locate the unique admissible stationary point in \(p\)

Also
\[
\partial_pF=-\frac{6J(p,v)}{(p^2+v+1)^4},
\tag{10}
\]
where
\[
\begin{aligned}
J(p,v)={}&4p^5v+4p^5+18p^4v+6p^4+36p^3v\\
&+2p^2v^2+26p^2v-p^2-4pv^3-18pv^2-15pv-4p\\
&-4v^3-14v^2-11v-1.
\end{aligned}
\tag{11}
\]
Thus an interior stationary point must satisfy
\[
H(p,v)=J(p,v)=0.
\tag{12}
\]
Eliminating \(v\) gives
\[
\operatorname{Res}_v(H,J)
=-48(p+1)P_5(p)K(p),
\tag{13}
\]
where
\[
P_5(p)=4p^5+14p^4+12p^3+15p^2+10p+1>0
\qquad(p\ge0),
\]
and
\[
\begin{aligned}
K(p)={}&20p^{11}+200p^{10}+786p^9+1690p^8+2013p^7+517p^6\\
&-1924p^5-2236p^4-522p^3+504p^2+352p+68.
\end{aligned}
\tag{14}
\]
A Sturm sequence for \(K\) gives the following exact variation counts:
\[
\begin{array}{c|cccccc}
x&0&0.6189&0.6190&0.8725&0.8726&+\infty\\ \hline
V(x)&5&5&4&4&3&3.
\end{array}
\tag{15}
\]
Hence \(K\) has exactly two positive roots, one in \((0.6189,0.6190)\) and one in \((0.8725,0.8726)\).

The degree-one subresultant of \(H,J\) is
\[
\begin{aligned}
S(p,v)={}&(p+1)^2(20p^7+68p^6+74p^5+52p^4+15p^3-12p^2-54p-32)\\
&+2(10p^7+36p^6-6p^5-112p^4-43p^3+42p^2+4p-10)v.
\end{aligned}
\tag{16}
\]
Exact interval arithmetic in the first root interval of (15) gives \(v<0\), so that root cannot correspond to an admissible stationary point. In the second root interval, (12) has a unique solution with
\[
0.8725<p_*<0.8726,
\qquad
0.921<v_*<0.923.
\tag{17}
\]
Numerically,
\[
p_*\approx0.8725362666668867,
\qquad
v_*\approx0.9218658788134108.
\]

There are no other stationary points on the positive maximizing branch \(v=v_p\). At \(p=0\), the positive root of \(H(0,v)=0\) gives \(\partial_pF>0\). At \(p=1\), the positive root of \(H(1,v)=0\) gives \(\partial_pF<0\). By continuity and the uniqueness just proved, the reduced one-variable function \(p\mapsto F(p,v_p)\) increases up to \(p_*\) and decreases after \(p_*\). Therefore \((p_*,v_*)\) is the unique global maximizer in the nonnegative quadrant.

Step 6: Evaluate the maximum and recover all signs

Define \((p_*,v_*)\) equivalently as the unique real solution of
\[
H(p,v)=J(p,v)=0
\]
in the isolating box (17). Then
\[
\boxed{
M_*=\frac54\,\frac{N(p_*,v_*)}{(p_*^2+v_*+1)^3}
}.
\tag{18}
\]
Numerically,
\[
M_*\approx16.11107890701402.
\]

By (5),
\[
c^2=\frac1{2(p_*^2+v_*+1)}.
\]
The sign reduction shows that equality requires \(a\) and \(c\) to have the same sign, while the sign of \(b\) is free. Hence the complete extremizer set is
\[
\boxed{
\mathcal E_*
=
\left\{
\frac{(\varepsilon p_*,\delta\sqrt{v_*},\varepsilon)}
{\sqrt{2(p_*^2+v_*+1)}}:
\varepsilon,\delta\in\{\pm1\}
\right\}.
}
\tag{19}
\]
There are exactly four maximizing triples.

Final Answer:
\[
\boxed{
\left(
\frac54\frac{N(p_*,v_*)}{(p_*^2+v_*+1)^3},
\left\{
\frac{(\varepsilon p_*,\delta\sqrt{v_*},\varepsilon)}
{\sqrt{2(p_*^2+v_*+1)}}:
\varepsilon,\delta\in\{\pm1\}
\right\}
\right)
}
\]
where \((p_*,v_*)\) is the unique solution of (12) in (17).

---

## Answer

$\left(\dfrac54\dfrac{N(p_*,v_*)}{(p_*^2+v_*+1)^3},\left\{\dfrac{(\varepsilon p_*,\delta\sqrt{v_*},\varepsilon)}{\sqrt{2(p_*^2+v_*+1)}}:\varepsilon,\delta\in\{\pm1\}\right\}\right)$, where $(p_*,v_*)$ is the unique solution with $0.8725<p_*<0.8726$ and $0.921<v_*<0.923$ of $H(p,v)=J(p,v)=0$, with $H,J,N$ defined above.

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- sixth Fourier moment as triple-convolution energy
- sign reduction for symmetric Fourier coefficients
- exact rational optimization in two variables
- resultant and Sturm isolation of the unique admissible stationary point
- complete classification of extremizers

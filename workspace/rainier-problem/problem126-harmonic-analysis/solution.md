## Steps

Step 1: Build a positive quadrature certificate for the first Fourier coefficient
Write
$$
T(\theta)=1+2a\cos\theta+2a_4\cos(4\theta)+2a_5\cos(5\theta)+2a_6\cos(6\theta).
$$
Set
$$
r=\sqrt5,\qquad m=\frac{\sqrt{10-2r}}4,\qquad c=\frac{\sqrt{10+2r}}4.
$$
The free frequencies are $4,5,6$, so it is natural to look at zeros of $\cos(5\theta)$. For every odd multiple of $\pi/10$, one also has $\cos(6\theta)=-\cos(4\theta)$. Choose
$$
\theta_1=\frac{7\pi}{10},\qquad \theta_2=\frac{9\pi}{10},
$$
for which $\cos\theta_1,\cos\theta_2<0$ and the fourth-frequency values have opposite signs. Explicitly,
$$
\cos\theta_1=-m,\qquad \cos\theta_2=-c,
$$
$$
\cos(4\theta_1)=-\frac{1+r}{4},\qquad
\cos(4\theta_2)=\frac{r-1}{4},
$$
and $\cos(5\theta_i)=0$, $\cos(6\theta_i)=-\cos(4\theta_i)$.

The positive weights that cancel the fourth frequency are forced to be
$$
w_1=\frac{5-r}{10},\qquad w_2=\frac{5+r}{10}.
$$
Indeed $w_1+w_2=1$ and
$$
w_1\cos(4\theta_1)+w_2\cos(4\theta_2)=0,
$$
so the same cancellation holds for the sixth frequency. Also
$$
m^2=\frac{5-r}{8},\qquad mc=\frac r4,
$$
and therefore
$$
2m(w_1m+w_2c)
=\frac{(5-r)^2}{40}+\frac{(5+r)r}{20}
=\frac{3-r}{4}+\frac{r+1}{4}=1.
$$
Thus
$$
w_1\cos\theta_1+w_2\cos\theta_2=-\frac1{2m}.
$$
Taking the same weighted average of the two nonnegative values of $T$ gives
$$
0\leq w_1T(\theta_1)+w_2T(\theta_2)=1-\frac{a}{m}.
$$
Hence every admissible polynomial satisfies
$$
a\leq m=\frac{\sqrt{10-2\sqrt5}}4.
$$

Step 2: Use the equality contacts to reconstruct an extremal polynomial
To attain the bound, equality in the positive weighted average from Step 1 requires
$$
T(\theta_1)=T(\theta_2)=0.
$$
Let $x=\cos\theta$ and let $F(x)=T(\arccos x)$. Since $F\geq0$ on $[-1,1]$ and the two contact points $-m,-c$ are interior, each contact is a double zero. Thus a degree-six extremizer should have the form
$$
F_*(x)=K(x+m)^2(x+c)^2(x^2+px+q).
$$
Put
$$
s=m+c=\frac{\sqrt{5+2r}}2,\qquad t=mc=\frac r4.
$$
Then
$$
(x+m)^2(x+c)^2=(x^2+sx+t)^2.
$$

For an allowed polynomial
$$
1+2aT_1(x)+2a_4T_4(x)+2a_5T_5(x)+2a_6T_6(x),
$$
where $T_k$ is the Chebyshev polynomial, the monomial expansion is
$$
\begin{aligned}
&64a_6x^6+32a_5x^5+(16a_4-96a_6)x^4-40a_5x^3\\
&\quad+(-16a_4+36a_6)x^2+(2a+10a_5)x+(1+2a_4-2a_6).
\end{aligned}
$$
If $d_j$ denotes the coefficient of $x^j$, every polynomial in the allowed class therefore satisfies
$$
d_3=-\frac54d_5,
$$
$$
d_2+d_4+\frac{15}{16}d_6=0,
$$
$$
d_0=1+\frac18d_4+\frac5{32}d_6.
$$

Let
$$
H(x)=(x^2+sx+t)^2(x^2+px+q)=\sum_{j=0}^6h_jx^j.
$$
The coefficients needed for the first two relations are
$$
h_5=p+2s,
$$
$$
h_4=q+2sp+s^2+2t,
$$
$$
h_3=2sq+(s^2+2t)p+2st,
$$
$$
h_2=(s^2+2t)q+2stp+t^2.
$$
Using $s^2=(5+2r)/4$ and $t=r/4$, the two missing-frequency relations become the linear system
$$
\left(r+\frac52\right)p+2sq+\frac{s(r+5)}2=0,
$$
$$
s\left(\frac r2+2\right)p+\left(r+\frac94\right)q+r+\frac52=0.
$$
Solving gives
$$
p=\frac{(5r-31)s}{19},\qquad q=\frac{5+9r}{38}.
$$
For these values,
$$
h_4=-\frac{105}{76}+\frac{5r}{19},\qquad h_0=\frac{25+45r}{608}.
$$
The normalization relation for $F_*=KH$ is therefore
$$
Kh_0=1+\frac{Kh_4}{8}+\frac{5K}{32},
$$
which forces
$$
K=\frac{8(5r-7)}5>0.
$$

Step 3: Verify positivity and attainment
The remaining quadratic factor has discriminant
$$
p^2-4q=\frac{785-373r}{722}<0,
$$
because $373^2\cdot5>785^2$. Since its leading coefficient is positive, $x^2+px+q>0$ for every real $x$. Together with $K>0$, this proves
$$
F_*(x)\geq0
$$
for every real $x$.

Substituting the derived values of $p,q,K$ and expanding in the Chebyshev basis gives
$$
F_*(x)=1+2mT_1(x)+\frac{23-5r}{20}T_4(x)+\frac{2s}{5}T_5(x)+\frac{5r-7}{20}T_6(x).
$$
Thus $T_*(\theta)=F_*(\cos\theta)$ is an admissible nonnegative trigonometric polynomial: its second and third Fourier coefficients vanish, its constant coefficient is $1$, and its first coefficient is $m$. Hence the upper bound from Step 1 is attained.

Final Answer: $\boxed{\frac{\sqrt{10-2\sqrt5}}4}$

---

## Answer

$\frac{\sqrt{10-2\sqrt5}}4$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact scalar

---

## Solution Concepts

- nonnegative trigonometric polynomials
- positive quadrature certificates
- Fourier coefficient annihilation
- Chebyshev polynomials
- equality case reconstruction

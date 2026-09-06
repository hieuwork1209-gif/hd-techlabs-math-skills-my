## Steps

Step 1: Recover the unique multiplicity function for a fixed flag.
For a projective character direction $L=\langle y\rangle$, the numbers $\widehat f(ay)$, $a\in\mathbb F_\ell^\times$, are Galois conjugate in $\mathbb Q(\zeta)$ and have a common absolute value $p_L\in\{q,q+2Q,q+4Q\}$. Each $p_L$ is inert because $p_L\equiv q\equiv2^{-1}\pmod\ell$ and $2$ is primitive modulo $\ell$. Hence $(\widehat f(y))=(p_L)$, so $\widehat f(y)/p_L$ is an algebraic integer all of whose conjugates have modulus $1$; therefore it is a root of unity. With $\lambda=1-\zeta$,
$$
\widehat f(y)\equiv2q^2\pmod\lambda,
$$
while $p_L\equiv q\pmod\ell$, so $\widehat f(y)/p_L\equiv2q\equiv1\pmod\lambda$. The roots of unity in $\mathbb Q(\zeta)$ are $\pm\zeta^c$, and the congruence selects $\zeta^c$. Thus every projective direction determines one affine hyperplane carrying its Fourier phase.

Let
$$
D=\frac{Q-1}{\ell-1},\qquad h=\ell^{r-1},\qquad d_0=\frac{h-1}{\ell-1}.
$$
For $x\in G$, let $e(x)$ count all $D$ phase hyperplanes through $x$, let $e_W(x)$ count those from the $\ell+1$ directions in $W^\perp$, and let $i_U(x)$ indicate the one from $U^\perp$. Fourier inversion gives
$$
Qf(x)=2q^2-qD-2Q(\ell+2)+\ell q\,e(x)+2\ell Q\,e_W(x)+2\ell Q\,i_U(x).
$$
Reducing modulo $Q$ gives $1-D+\ell e(x)\equiv0\pmod Q$. Since $D=d_0+h$ and $D-1=\ell d_0$, one has $e(x)\equiv d_0\pmod h$; as $0\le e(x)\le D$, each $e(x)$ is $d_0$ or $D$. Counting incidences, $\sum_xe(x)=Dh$, so exactly one point, say $z_0$, has value $D$. Hence all phase hyperplanes pass through $z_0$, and
$$
e_W(x)=1+\ell 1_{z_0+W}(x),\qquad i_U(x)=1_{z_0+U}(x).
$$
Writing $d=q(2q-1)/Q$ and substituting gives
$$
f(x)=d-4+2\ell^2 1_{z_0+W}(x)+2\ell 1_{z_0+U}(x)+q\,1_{\{z_0\}}(x). \tag{1}
$$
The first moment of the three coset terms is $0$ in $G$, so $\sum_xf(x)x=Ps$ gives $qz_0=Ps$. Thus for fixed $(s,U,W)$ there is exactly one $f$. Conversely, the Fourier transform of (1) has the stated magnitudes. Its four values are distinct, so $f$ recovers $z_0,W,U$; distinct admissible flags give distinct pairs $(s,f)$.

Step 2: Classify the phase vectors using the second product constraint.
Write $\mathbf1=\alpha s+\beta(Ps+P^{-1}s)$. Here $\beta\ne0$, for otherwise $s$ is constant, and $\sum_js_j=r$ gives $s=\mathbf1$, contradicting $\prod_j(s_j-1)=2$. Hence
$$
Ps+P^{-1}s=a\mathbf1+bs.
$$
Summing coordinates gives $a+b=2$. Put $y=s-\mathbf1$. Since $r\mid\ell-1$, the cyclic shift diagonalizes over $\mathbb F_\ell$, and $\sum_jy_j=0$ removes the eigenvalue $1$. Therefore
$$
s_j=1+u\omega^{j-1}+v\omega^{-(j-1)}, \tag{2}
$$
where $\omega$ is a nontrivial $r$th root. Reciprocal frequencies give the same eigenspace, so there are $(r-1)/2$ frequency pairs.

Because $r$ is odd,
$$
\prod_{j=0}^{r-1}(u\omega^j+v\omega^{-j})=u^r+v^r.
$$
As $\ell=2r+1$, every nonzero element has $r$th power $\pm1$, so $\prod_j(s_j-1)=2$ forces $u^r=v^r=1$. Let $H\subset\mathbb F_\ell^\times$ be the subgroup of order $r$ and put $c=uv\in H$.

Let $A,B$ be the roots of
$$
T^2+T+c=0. \tag{3}
$$
Multiplying $1+u x+v x^{-1}$ over the $r$ roots $x^r=1$ gives
$$
\prod_js_j=2-(A^r+B^r). \tag{4}
$$
Indeed, after multiplying by $x$, the two roots are $A/u,B/u$, and $u^r=v^r=c^r=1$.

If (3) splits over $\mathbb F_\ell$, then $A^r=\chi(A)$ and $B^r=\chi(B)$, where $\chi$ is the quadratic character. Since $AB=c\in H$, the two characters are equal. Thus (4) equals $4$ exactly when both roots are nonresidues; it equals $0$ when both are residues. If (3) is nonsplit and $t=A^r$, then $B^r=t^{-1}$; equality in (4) with $4$ would force $t=-1$, hence $A^{\ell-1}=A^{2r}=1$, contradicting $A\notin\mathbb F_\ell$. Therefore the new condition $\prod_js_j=4$ is equivalent to (3) having two distinct nonresidue roots.

It remains to count such $c$. Since $4H=H$, the number of $c\in H$ for which $1-4c$ is a nonzero square is
$$
\#\{d\in H:1-d\in H\}=\frac{\ell-3}{4}=\frac{r-1}{2}. \tag{5}
$$
This follows by expanding
$$
\frac14\sum_{d\ne0,1}(1+\chi(d))(1+\chi(1-d));
$$
the three character sums are $-1,-1,1$ because $\chi(-1)=-1$. Among these split values, those with residue roots are obtained from $A\in H$ with $-1-A\in H$. The corresponding ordered-root count is $(r+1)/2$; removing the double root $A=-1/2$ and dividing by $2$ leaves $(r-1)/4$ distinct nonzero-discriminant values of $c$. Hence the number with two nonresidue roots is also
$$
\frac{r-1}{4}. \tag{6}
$$
For each such $c$, there are $r$ factorizations $c=uv$ in $H^2$. Therefore
$$
N_s=\frac{r-1}{2}\,r\,\frac{r-1}{4}=\frac{r(r-1)^2}{8}. \tag{7}
$$

Step 3: Count the admissible flags for one phase vector.
For (2), set
$$
H_s=\operatorname{span}\{\mathbf1,(\omega^{j-1})_j,(\omega^{-(j-1)})_j\}.
$$
It has dimension $3$, and the $r$ projective points $[P^ts]$ have coordinates
$$
[1:u\omega^t:v\omega^{-t}],
$$
so they lie on the nonsingular conic $YZ=uvX^2$. They are distinct and no three are collinear.

A hyperplane $U$ containing $H_s$ can be chosen in
$$
\frac{\ell^{r-3}-1}{\ell-1}
$$
ways. Fix such a $U$. A hyperplane $W\subset U$ avoids every $P^ts$ exactly when the projective kernel line of its restriction to $H_s$ avoids the $r$ conic points. Among the $\ell^2+\ell+1$ lines of $\mathbb P(H_s)$, the number meeting at least one selected point is
$$
r(\ell+1)-\binom r2,
$$
because no line contains three selected points. Hence the number of allowable kernel lines is
$$
L_0=\ell^2+\ell+1-r(\ell+1)+\binom r2=\frac{5r^2+7r+6}{2}.
$$
Each kernel line has $\ell^{r-4}$ extensions to a hyperplane of $U$, so
$$
F=\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}\frac{5r^2+7r+6}{2}. \tag{8}
$$

Step 4: Multiply the independent choices.
By Step 1, every admissible phase vector and admissible flag produces exactly one pair $(s,f)$, and $f$ recovers the flag. Combining (7) and (8) gives
$$
\frac{r(r-1)^2(5r^2+7r+6)}{16}\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}.
$$
Final Answer: $\boxed{\frac{r(r-1)^2(5r^2+7r+6)}{16}\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}}$

---

## Answer

$\frac{r(r-1)^2(5r^2+7r+6)}{16}\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- cyclotomic phase rigidity from inert primes
- reciprocal cyclic modes over a finite field
- resultant split-versus-nonsplit classification
- quadratic-character counting
- projective conic incidence
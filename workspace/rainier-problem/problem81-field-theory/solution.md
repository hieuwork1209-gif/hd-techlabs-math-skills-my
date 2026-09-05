## Steps

Step 1: Recover the unique multiplicity function for a fixed flag.
For a projective character direction $L=\langle y\rangle$, the numbers $\widehat f(ay)$, $a\in\mathbb F_\ell^\times$, are Galois conjugate in $\mathbb Q(\zeta)$ and have a common absolute value $p_L\in\{q,q+2Q,q+4Q\}$. Each $p_L$ is inert because $p_L\equiv q\equiv2^{-1}\pmod\ell$ and $2$ is primitive modulo $\ell$. Hence $(\widehat f(y))=(p_L)$, so $\widehat f(y)/p_L$ is an algebraic integer all of whose conjugates have modulus $1$; therefore it is a root of unity. With $\lambda=1-\zeta$,
$$
\widehat f(y)\equiv2q^2\pmod\lambda,
$$
while $p_L\equiv q\pmod\ell$, so $\widehat f(y)/p_L\equiv2q\equiv1\pmod\lambda$. The roots of unity in $\mathbb Q(\zeta)$ are $\pm\zeta^c$, and the congruence selects $\zeta^c$. Galois conjugacy along $L$ therefore makes every projective direction determine one affine hyperplane carrying its Fourier phase.

Let
$$
D=\frac{Q-1}{\ell-1},\qquad h=\ell^{r-1},\qquad d_0=\frac{h-1}{\ell-1}.
$$
For $x\in G$, let $e(x)$ count all $D$ phase hyperplanes through $x$, let $e_W(x)$ count those from the $\ell+1$ directions in $W^\perp$, and let $i_U(x)$ indicate the one from $U^\perp$. Fourier inversion is
$$
Qf(x)=2q^2-qD-2Q(\ell+2)+\ell q\,e(x)+2\ell Q\,e_W(x)+2\ell Q\,i_U(x).
$$
Reducing modulo $Q$ gives
$$
1-D+\ell e(x)\equiv0\pmod Q.
$$
Since $D=d_0+h$ and $D-1=\ell d_0$, one has $e(x)\equiv d_0\pmod h$; as $0\le e(x)\le D$, each $e(x)$ is $d_0$ or $D$. Counting incidences gives
$$
\sum_xe(x)=Dh,
$$
so exactly one point, say $z_0$, has value $D$. Hence all phase hyperplanes pass through $z_0$. Consequently
$$
e_W(x)=1+\ell 1_{z_0+W}(x),\qquad i_U(x)=1_{z_0+U}(x).
$$
Writing $d=q(2q-1)/Q$ (an integer, and $d\ge4$) and substituting in the inversion formula gives
$$
f(x)=d-4+2\ell^2 1_{z_0+W}(x)+2\ell 1_{z_0+U}(x)+q\,1_{\{z_0\}}(x). \tag{1}
$$
The first moment of the three coset terms is $0$ in $G$, so the condition $\sum_xf(x)x=Ps$ gives
$$
qz_0=Ps. \tag{2}
$$
Thus for fixed $(s,U,W)$ there is exactly one $f$. Conversely, $\widehat{1_{z_0+V}}(y)=|V|\zeta^{z_0\cdot y}1_{V^\perp}(y)$ shows directly that (1) has the stated Fourier magnitudes. Its four values are distinct, so $f$ recovers $z_0$, $W$, and $U$; therefore different admissible flags give different pairs $(s,f)$.

Step 2: Count the admissible phase vectors.
Write the span relation as $\mathbf1=\alpha s+\beta(Ps+P^{-1}s)$. Here $\beta\ne0$: otherwise $s$ is constant, and $\sum_js_j=r$ forces $s=\mathbf1$, contradicting $\prod_j(s_j-1)=2$. Hence
$$
Ps+P^{-1}s=a\mathbf1+bs.
$$
Summing coordinates gives $a+b=2$. Put $y=s-\mathbf1$; then
$$
Py+P^{-1}y=by.
$$
Because $r\mid\ell-1$, the cyclic shift $P$ diagonalizes over $\mathbb F_\ell$ with the $r$th roots of unity as eigenvalues. Since $\sum_jy_j=0$, the eigenvalue $1$ is absent, so a nonconstant solution is
$$
s_j=1+u\omega^{j-1}+v\omega^{-(j-1)}, \tag{3}
$$
where $\omega$ is a nontrivial $r$th root of unity. Reciprocal frequencies give the same eigenspace, so there are $(r-1)/2$ choices for $\{\omega,\omega^{-1}\}$.

Because $r$ is odd,
$$
\prod_{j=0}^{r-1}(u\omega^j+v\omega^{-j})=u^r+v^r.
$$
As $\ell=2r+1$, every nonzero element has $r$th power $\pm1$; the product condition therefore forces $u^r=v^r=1$. Let $H\subset\mathbb F_\ell^\times$ be the subgroup of order $r$. For $u,v\in H$, put $c=uv$. As $j$ varies, $a=u\omega^j$ runs through $H$, and $s_j=0$ exactly when
$$
a^2+a+c=0.
$$
For $a\in H$, the value $c=-a(a+1)$ lies in $H$ exactly when $\chi(a+1)=-1$, where $\chi$ is the quadratic character. Since $2$ is primitive, $\chi(2)=-1$, and since $\ell\equiv3\pmod4$, $\chi(-1)=-1$. Expanding the indicator gives
$$
\frac14\sum_{a\ne0,-1}(1+\chi(a))(1-\chi(a+1)).
$$
The three nonconstant sums are $1,-1,-1$: the last follows from $4a(a+1)=(2a+1)^2-1$ and the fact that $x^2-z^2=1$ has exactly $\ell-1$ solutions. Hence the display equals $(\ell+1)/4=(r+1)/2$, the number of bad $a$. The involution $a\mapsto-1-a$ has the single fixed point $-1/2$, and $\chi(-1/2)=\chi(-1)\chi(2)=1$, so that point lies in $H$. Hence the number of bad products $c$ is $(r+3)/4$. Hence there are $3(r-1)/4$ good products. Each has $r$ factorizations $c=uv$ in $H^2$, and therefore
$$
N_s=\frac{r-1}{2}\,r\,\frac{3(r-1)}4=\frac{3r(r-1)^2}{8}. \tag{4}
$$

Step 3: Count the admissible flags for one phase vector.
For (3), set
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
because no line contains three selected points. Thus the number of allowable kernel lines is
$$
L_0=\ell^2+\ell+1-r(\ell+1)+\binom r2=\frac{5r^2+7r+6}{2}.
$$
Each kernel line has $\ell^{r-4}$ extensions to a hyperplane of $U$, so the number of admissible flags is
$$
F=\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}\frac{5r^2+7r+6}{2}. \tag{5}
$$

Step 4: Multiply the independent choices.
By Step 1, every admissible phase vector and admissible flag produces exactly one pair $(s,f)$, and $f$ recovers the flag, so there is no overcount. Combining (4) and (5) gives
$$
\frac{3r(r-1)^2(5r^2+7r+6)}{16}\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}.
$$
Final Answer: $\boxed{\frac{3r(r-1)^2(5r^2+7r+6)}{16}\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}}$

---

## Answer

$\frac{3r(r-1)^2(5r^2+7r+6)}{16}\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- cyclotomic phase rigidity from inert primes
- affine-hyperplane recovery by Fourier inversion
- reciprocal cyclic modes over a finite field
- quadratic-character exclusion of zero coordinates
- projective conic incidence

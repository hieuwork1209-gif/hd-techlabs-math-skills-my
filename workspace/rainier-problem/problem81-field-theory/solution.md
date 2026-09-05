## Steps

Step 1: Parameterize the lifts and the cyclic first moment.
Put
$$
Q=\ell^r,\qquad h=\ell^{r-1},\qquad m=2q^2,\qquad d=\frac{q(2q-1)}Q.
$$
Also set
$$
A=d+q+2\ell+2\ell^2-4,\quad B=d+2\ell+2\ell^2-4,
$$
$$
C=d+2\ell-4,\qquad E=d-4.
$$
The primes $q,q+2Q,q+4Q$ are congruent to $2^{-1}$ modulo $\ell$, hence are inert in $\mathbb Q(\zeta)$ because $2$ generates $\mathbb F_\ell^\times$.

Write indices cyclically and let $P(s_1,\ldots,s_r)=(s_2,\ldots,s_r,s_1)$. A lift of $\pi$ has the form
$$
\sigma(\alpha_i^{(j)})=\zeta^{a_i^{(j)}}\alpha_{\pi(i)}^{(j)},\qquad
\sigma(\rho_j)=\zeta^{s_j}\rho_j,
$$
with every $s_j\ne0$. Applying $\sigma$ to $\prod_i\alpha_i^{(j)}=\rho_{j+1}$ gives
$$
\sum_i a_i^{(j)}=s_{j+1}. \tag{1}
$$
For each transposition block $T$ of $\pi$, define
$$
Z_T=\left(\sum_{i\in T}a_i^{(1)},\ldots,\sum_{i\in T}a_i^{(r)}\right)\in G:=\mathbb F_\ell^r,
$$
and let $m_z$ count the blocks with label $z$. Then
$$
\sum_zm_z=m,\qquad \sum_zm_zz=Ps. \tag{2}
$$

Step 2: Convert the cycle data into a Fourier-magnitude flag.
Let $D_s=\operatorname{diag}(s_1,\ldots,s_r)$. Two applications of $\sigma$ on $\Omega_k$, with indices in blocks $T,R$, translate the fiber by
$$
w+Z_T-Z_R,\qquad w=2D_sk.
$$
Put $\overline W=2D_sW$ and $\overline U=2D_sU$. If
$$
N_w=\sum_zm_zm_{z+w},
$$
then the number of base orbits with zero two-step translation is
$$
R_w=2N_w-m\delta_{w,0}. \tag{3}
$$
Each such base orbit yields $Q$ cycles of length $2$, while every nonzero translation has order $\ell$. Thus the prescribed gaps are equivalent to
$$
R_w=R_0+8\ell(q+3Q)1_{\overline U}(w)+8\ell^2(q+Q)1_{\overline W}(w). \tag{4}
$$
For $M(\chi)=\sum_zm_z\chi(z)$, Fourier transforming gives
$$
|M(\chi)|=
\begin{cases}
q+4Q,&\chi\in\overline U^\perp\setminus\{1\},\\
q+2Q,&\chi\in\overline W^\perp\setminus\overline U^\perp,\\
q,&\chi\notin\overline W^\perp.
\end{cases} \tag{5}
$$
For $c_s^{(t)}=(s_{1+t}/s_1,\ldots,s_{r+t}/s_r)$, one has $D_sc_s^{(t)}=P^ts$. Hence the incidence condition is
$$
P^ts\in\overline U\setminus\overline W\qquad(0\le t<r). \tag{6}
$$

Step 3: Recover the affine flag and its phase center.
Fix a nontrivial projective character direction $L$. By (5), its nontrivial Fourier coefficients have one absolute value $p_L\in\{q,q+2Q,q+4Q\}$. Since $p_L$ is inert, $(M(\chi))=(p_L)$, so $M(\chi)/p_L$ is an algebraic integer all of whose conjugates have absolute value $1$, hence a root of unity.

Let $\lambda=1-\zeta$. Every character value is $1$ modulo $\lambda$, so
$$
M(\chi)\equiv2q^2\pmod\lambda,
$$
and $p_L\equiv q\pmod\ell$ gives $M(\chi)/p_L\equiv1\pmod\lambda$. Therefore each projective direction determines a distinguished affine hyperplane carrying the Fourier phase.

Put
$$
D=\frac{Q-1}{\ell-1},\qquad d_0=\frac{h-1}{\ell-1}.
$$
Let $e(z)$ count all distinguished hyperplanes through $z$, let $f(z)$ count those with normals in $\mathbb P(\overline W^\perp)$, and let $I(z)$ indicate the distinguished hyperplane for $\overline U^\perp$. Fourier inversion gives
$$
Qm_z=m-qD-2Q(\ell+2)+\ell q\,e(z)+2\ell Q\,f(z)+2\ell Q\,I(z). \tag{7}
$$
Reducing modulo $Q$ gives $e(z)\equiv d_0\pmod h$. Since $0\le e(z)\le D=d_0+h$, every $e(z)$ is either $d_0$ or $D$. Counting incidences shows exactly one point has value $D$; call it $z_0$. Hence
$$
m_z=d-4+2\ell^2 1_{z_0+\overline W}(z)+2\ell 1_{z_0+\overline U}(z)+q\delta_{z_0}(z). \tag{8}
$$
Taking the first moment and using (2) gives
$$
qz_0=Ps. \tag{9}
$$
The four multiplicity levels $A,B,C,E$ are distinct, so the profile recovers $z_0$ and the transformed flag. Conversely, every admissible $s$ and transformed flag satisfying (6) gives exactly one such profile.

Step 4: Classify the reciprocal-mode phase vectors.
The statement imposes
$$
\mathbf1\in\operatorname{span}\{s,Ps+P^{-1}s\},\qquad \sum_js_j=r,\qquad \prod_j(s_j-1)=2. \tag{10}
$$
If the coefficient of $Ps+P^{-1}s$ vanished, $s$ would be constant; the sum condition would give $s=\mathbf1$, contradicting the product condition. Thus
$$
Ps+P^{-1}s=a\mathbf1+bs.
$$
Summing coordinates gives $a+b=2$. After putting $y=s-\mathbf1$, we obtain
$$
Py+P^{-1}y=by. \tag{11}
$$
A nonconstant $r$-periodic solution therefore has
$$
s_j=1+u\omega^{j-1}+v\omega^{-(j-1)}, \tag{12}
$$
where $\omega$ is a nontrivial $r$th root of unity. Since $r$ is prime, $\omega$ has order $r$. Replacing $\omega$ by $\omega^{-1}$ swaps $u,v$, so there are $(r-1)/2$ choices of reciprocal frequency pair.

Because $r$ is odd,
$$
\prod_{j=0}^{r-1}(u\omega^j+v\omega^{-j})=u^r+v^r.
$$
Now $\ell=2r+1$, so every nonzero $x\in\mathbb F_\ell$ has $x^r=\pm1$. The product condition in (10) forces
$$
u^r=v^r=1. \tag{13}
$$
Let $H\subset\mathbb F_\ell^\times$ be the subgroup of order $r$. For fixed reciprocal frequencies, $u,v\in H$. Put $c=uv\in H$. As $j$ varies, $a=u\omega^j$ runs through $H$, and $s_j=0$ exactly when
$$
a^2+a+c=0. \tag{14}
$$
Let $\chi$ be the quadratic character. Since $2$ is primitive, $\chi(2)=-1$; also $\ell\equiv3\pmod4$, so $\chi(-1)=-1$. For $a\in H$, the value $c=-a(a+1)$ lies in $H$ exactly when $\chi(a+1)=-1$. The number of such $a$ is
$$
\frac14\sum_{a\ne0,-1}(1+\chi(a))(1-\chi(a+1))=\frac{\ell+1}{4}=\frac{r+1}{2}. \tag{15}
$$
The map $a\mapsto-a(a+1)$ pairs $a$ with $-1-a$, with the single fixed point $a=-1/2\in H$. Hence the number of bad products $c\in H$ is $(r+3)/4$, and the number of good products is $3(r-1)/4$. For each good $c$ there are $r$ pairs $(u,v)\in H^2$ with $uv=c$. Thus the number of admissible phase vectors is
$$
N_s=\frac{r-1}{2}\cdot r\cdot\frac{3(r-1)}4=\frac{3r(r-1)^2}{8}. \tag{16}
$$

Step 5: Count hyperplanes avoiding the conic orbit and prove the orbit classification.
For a phase vector (12), let
$$
H_s=\operatorname{span}\{\mathbf1,(\omega^{j-1})_j,(\omega^{-(j-1)})_j\}.
$$
It has dimension $3$, and in projective coordinates on $\mathbb P(H_s)$ the $r$ points $[P^ts]$ are
$$
[1:u\omega^t:v\omega^{-t}],
$$
so they lie on the nonsingular conic $YZ=uvX^2$. In particular, they are distinct and no three are collinear.

The number of hyperplanes $\overline U\subset G$ containing $H_s$ is
$$
\frac{\ell^{r-3}-1}{\ell-1}. \tag{17}
$$
Fix one. A hyperplane $\overline W\subset\overline U$ avoids all $r$ orbit vectors precisely when the projective kernel line of its restriction to $H_s$ avoids all $r$ conic points. There are $\ell^2+\ell+1$ projective lines in $\mathbb P(H_s)$. The union of the lines through at least one selected conic point has size
$$
r(\ell+1)-\binom r2,
$$
because no line contains three selected points. Hence the number of allowable kernel lines is
$$
L_0=\ell^2+\ell+1-r(\ell+1)+\binom r2=\frac{5r^2+7r+6}{2}. \tag{18}
$$
For each kernel line there are $\ell^{r-4}$ extensions to a hyperplane of $\overline U$. Therefore the number of flags for each admissible $s$ is
$$
F=\ell^{r-4}\frac{\ell^{r-3}-1}{\ell-1}\frac{5r^2+7r+6}{2}. \tag{19}
$$

It remains to justify that multiplying $N_s$ by $F$ counts conjugacy orbits rather than merely parameter pairs. Let $\tau\in\widetilde C_\pi$ have base permutation $c=\pi_\tau\in C_{S_n}(\pi)$, and write
$$
\tau(\alpha_i^{(j)})=\zeta^{b_i^{(j)}}\alpha_{c(i)}^{(j)},\qquad
\tau(\rho_j)=\zeta^{u_j}\rho_j.
$$
The relation $\prod_i\alpha_i^{(j)}=\rho_{j+1}$ forces
$$
u_{j+1}=\sum_i b_i^{(j)}. \tag{20}
$$
Conversely, because the displayed product relations are the only Kummer relations, any choice of $c$ and the $b_i^{(j)}$ satisfying (20) defines such a lift after setting the $u_j$ accordingly.

For $\sigma'=\tau\sigma\tau^{-1}$, direct substitution gives
$$
s_j'=s_j,
$$
$$
a_i'^{(j)}=a_{c^{-1}(i)}^{(j)}+b_{\pi c^{-1}(i)}^{(j)}-b_{c^{-1}(i)}^{(j)}. \tag{21}
$$
Since $c$ commutes with $\pi$, summing (21) over the two endpoints of a transposition block $T$ cancels the two $b$-terms and yields
$$
Z_T'=Z_{c^{-1}T}. \tag{22}
$$
Thus $s$ and the multiplicity profile $z\mapsto m_z$ are invariants of a $\widetilde C_\pi$-conjugacy orbit.

Conversely, let $\sigma$ and $\sigma'$ have the same $s$ and the same multiplicity profile. Since
$$
C_{S_n}(\pi)\cong C_2\wr S_m
$$
permutes the $m$ transposition blocks arbitrarily, choose $c\in C_{S_n}(\pi)$ so that $Z_T'=Z_{c^{-1}T}$ for every block $T$. Conjugate $\sigma$ by any lift of this $c$; by (22) we may now assume the two lifts have exactly the same label on every block. Write the remaining endpoint differences as
$$
\Delta_i^{(j)}=a_i'^{(j)}-a_i^{(j)}.
$$
Equality of the block labels gives
$$
\Delta_{\pi(i)}^{(j)}=-\Delta_i^{(j)}. \tag{23}
$$
For one endpoint $i$ of each transposition block choose $b_i^{(j)}=0$ and
$$
b_{\pi(i)}^{(j)}=\Delta_i^{(j)}.
$$
Set $u_{j+1}=\sum_i b_i^{(j)}$ as in (20). The resulting element $\kappa\in\Gamma$ has base permutation equal to the identity, hence lies in $\widetilde C_\pi$, and (21) with $c=1$ changes $a_i^{(j)}$ by exactly $\Delta_i^{(j)}$ on both endpoints because of (23). It leaves every $s_j$ unchanged. Therefore $\kappa$ conjugates the first lift to the second. Hence two qualifying lifts are conjugate if and only if they have the same $s$ and the same multiplicity profile.

Finally, the four distinct levels in (8) recover $z_0,\overline W,\overline U$, so distinct admissible flags give distinct profiles. Thus there is exactly one conjugacy orbit for each admissible pair consisting of a phase vector and a flag, and multiplying (16) and (19) gives the required count.
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

- cyclic Kummer coupling of total phases
- three-level autocorrelation on a finite vector space
- reciprocal-mode cyclic recurrences
- quadratic-character exclusion of zero phases
- conic incidence in a projective plane

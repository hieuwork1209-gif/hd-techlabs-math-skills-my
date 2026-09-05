## Steps

Step 1: Identify the relevant cluster allocations

Put
$$
q=\sqrt{t},\qquad \phi(x)=x(1-x)(3x-1)^2.
$$
Andréief's identity gives
$$
D_m(t)=\frac{1}{(4m+2)!}\int_{[0,1]^{4m+2}}\prod_{i<j}(x_i-x_j)^2
\prod_i(1+q(3x_i-1))e^{-\frac{\phi(x_i)}{t}}\,dx_i.
$$
Away from fixed disjoint neighborhoods of $0,\frac13,1$, the phase has a positive minimum, so the contribution is exponentially small. In the three wells use
$$
x=q^2u,\qquad x=\frac13+\frac{q}{\sqrt2}z,\qquad x=1-\frac{q^2}{4}v.
$$
For an allocation $(k,l,r)$ the Jacobians and internal squared Vandermondes contribute
$$
t^{E(k,l,r)},\qquad E(k,l,r)=k^2+\frac{l^2}{2}+r^2,\qquad k+l+r=4m+2.
$$
Writing $k=m+a$, $r=m+c$, $l=2m+2-a-c$, then $u=2a-1$, $v=2c-1$, gives
$$
E-\left(4m^2+4m+\frac32\right)=\frac{3u^2+2uv+3v^2-4}{8}.
$$
For a gap at most $\frac32$, $2u^2+2v^2+(u+v)^2\leq16$; if $|u|\geq3$ or $|v|\geq3$ the left side is at least $20$. Since $u,v$ are odd, $u,v\in\{-1,1\}$. Thus the dominant allocations are
$$
(m,2m+1,m+1),\qquad(m+1,2m+1,m),
$$
and the only neighbors needed through relative order $q^3$ are
$$
(m,2m+2,m),\qquad(m+1,2m,m+1).
$$

Step 2: Derive the local Vandermonde integrals and cluster constants

For a weight $w$, let $p_j$ be its monic orthogonal polynomials and $h_j=\int p_j(x)^2w(x)\,dx$. Since $\Delta(x)=\det(p_{j-1}(x_i))$, Andréief gives
$$
\int\Delta(x)^2\prod_iw(x_i)\,dx_i=n!\prod_{j=0}^{n-1}h_j.
$$
For $w(u)=e^{-u}$ on $[0,\infty)$, Rodrigues gives the monic Laguerre polynomial
$$
p_j(u)=(-1)^je^u\frac{d^j}{du^j}(e^{-u}u^j).
$$
The same Rodrigues formula, integrated against any polynomial of degree below $j$, gives orthogonality. Integrating by parts $j$ times, with vanishing boundary terms,
$$
h_j=(-1)^j\int_0^\infty p_j\frac{d^j}{du^j}(e^{-u}u^j)\,du
=\int_0^\infty e^{-u}u^jp_j^{(j)}\,du=(j!)^2.
$$
For $w(z)=e^{-z^2}$, $H_j=(-1)^je^{z^2}\frac{d^j}{dz^j}e^{-z^2}$ has leading coefficient $2^j$, so $p_j=2^{-j}H_j$; the same integration-by-parts argument gives orthogonality. Moreover,
$$
\int_{\mathbb R}e^{-z^2}H_j^2\,dz
=\int_{\mathbb R}H_j^{(j)}e^{-z^2}\,dz
=2^jj!\sqrt\pi,
$$
hence $h_j=\sqrt\pi\,2^{-j}j!$. Therefore
$$
L_n=\prod_{j=0}^{n-1}(j!)^2,\qquad
G_n=\pi^{n/2}2^{-n(n-1)/2}\prod_{j=0}^{n-1}j!,
$$
and the labeled Laguerre and Gaussian Vandermonde integrals are $n!L_n$ and $n!G_n$.

For $(k,l,r)$, the left scaling gives $q^{2k^2}$: $q^{2k}$ from Jacobians and $q^{2k(k-1)}$ from the squared Vandermonde. The center gives
$$
q^{l}2^{-l/2}\,q^{l(l-1)}2^{-l(l-1)/2}
=q^{l^2}2^{-l^2/2},
$$
and the right gives
$$
(q^2/4)^r(q^4/16)^{r(r-1)/2}=q^{2r^2}4^{-r^2}.
$$
There are $kl,lr,kr$ cross pairs; their limiting squared distances are respectively $\frac19,\frac49,1$. Also
$$
\frac1{(4m+2)!}\frac{(4m+2)!}{k!l!r!}(k!L_k)(l!G_l)(r!L_r)=L_kG_lL_r.
$$
Thus
$$
K_{k,l,r}=4^{-r^2}2^{-l^2/2}3^{-2kl}\left(\frac49\right)^{rl}L_kL_rG_l.
$$
Substituting $G_l$,
$$
K_{k,l,r}=2^{-2r^2+2rl-l^2+l/2}3^{-2l(k+r)}
\pi^{l/2}L_kL_r\prod_{j=0}^{l-1}j!.
$$
For $(m,2m+1,m+1)$ the powers are $-2m^2-m-\frac12$ and $-8m^2-8m-2$, so
$$
K_{m,2m+1,m+1}=\frac{C_m}{2}.
$$
The other dominant allocation has the same powers and $L_mL_{m+1}$, hence also $C_m/2$. Using $L_{n+1}/L_n=(n!)^2$,
$$
\frac{K_{m,2m+2,m}}{C_m/2}
=9\,2^{-2m-5/2}\sqrt\pi\,\frac{(2m+1)!}{(m!)^2}
=\frac{9(2m+1)\sqrt\pi}{2^{2m+5/2}}\binom{2m}{m}=r_m,
$$
and
$$
\frac{K_{m+1,2m,m+1}}{C_m/2}
=9\,2^{2m-3/2}\pi^{-1/2}\frac{(m!)^2}{(2m)!}
=\frac{9\,2^{2m-3/2}}{\sqrt\pi\binom{2m}{m}}=s_m.
$$

Step 3: Derive the local logarithmic coefficients and control the expansion

Write $U_j=\sum_{i=1}^ku_i^j$, $V_j=\sum_{i=1}^rv_i^j$, $Z_j=\sum_{i=1}^lz_i^j$. The phase corrections are
$$
-\frac{3}{2\sqrt2}qZ_3+q^2\left(7U_2+V_2+\frac94Z_4\right)+O(q^4).
$$
For one left-middle, middle-right, and left-right pair, respectively,
$$
3\sqrt2\,qz+q^2\left(-6u-\frac92z^2\right)
+9\sqrt2\,q^3\left(uz+\frac12z^3\right),
$$
$$
-\frac{3\sqrt2}{2}qz+q^2\left(-\frac34v-\frac98z^2\right)
-\frac{9\sqrt2}{16}q^3(vz+z^3),
$$
$$
q^2\left(-2u-\frac12v\right),
$$
up to $O(q^4)$. Summing over the $kl,lr,kr$ pairs gives
$$
\begin{aligned}
LM&:3\sqrt2\,kqZ_1+q^2\left(-6lU_1-\frac92kZ_2\right)
+9\sqrt2\,q^3\left(U_1Z_1+\frac{k}{2}Z_3\right),\\
MR&:-\frac{3\sqrt2}{2}rqZ_1+q^2\left(-\frac34lV_1-\frac98rZ_2\right)
-\frac{9\sqrt2}{16}q^3(V_1Z_1+rZ_3),\\
LR&:q^2\left(-2rU_1-\frac{k}{2}V_1\right).
\end{aligned}
$$
Adding the phase terms yields $qA+q^2B+q^3C+O(q^4)$ with
$$
A=\frac{3}{2\sqrt2}\left((4k-2r)Z_1-Z_3\right),
$$
$$
B=7U_2+V_2-(6l+2r)U_1-\left(\frac{3l}{4}+\frac{k}{2}\right)V_1
+\frac94Z_4-\left(\frac{9k}{2}+\frac{9r}{8}\right)Z_2,
$$
$$
C=9\sqrt2\left(U_1-\frac{V_1}{16}\right)Z_1+\frac{9\sqrt2}{16}(8k-r)Z_3.
$$

For rigor on the expanding domains, take $R_q=q^{-1/16}$. The endpoint phases are exactly
$$
\frac{\phi(q^2u)}{q^2}=u-7q^2u^2+15q^4u^3-9q^6u^4,
$$
$$
\frac{\phi(1-\frac{q^2v}{4})}{q^2}=v-q^2v^2+\frac{21}{64}q^4v^3-\frac9{256}q^6v^4.
$$
On $u_i,v_i,|z_i|\leq R_q$, the omitted phase terms are $O(q^4R_q^3)$, the logarithmic fourth-order remainders are $O((qR_q)^4)$, and $A=O(R_q^3)$, $B=O(R_q^4)$, $C=O(R_q^3)$. The perturbing factor $\prod_i(1+q(3x_i-1))$ contributes $O(q(1+R_q))$ to its logarithm on the core, so the full logarithmic correction still satisfies $S_q=O(qR_q^3)$ and
$$
\left|e^{S_q}-1-S_q-\frac{S_q^2}{2}-\frac{S_q^3}{6}\right|
\leq C|S_q|^4=O(q^4R_q^{12})=O(q^{13/4})=o(q^3).
$$
Outside the core the phase is bounded below by $c\sum u_i+c\sum v_i+c\sum z_i^2$, while all other factors have polynomial growth, so the tails are $O(P(R_q)e^{-cR_q})+O(P(R_q)e^{-cR_q^2})=o(q^3)$. Hence exponentiation and termwise integration through $q^3$ are valid.

Step 4: Compute the local moments and coefficients

Laguerre integration by parts gives
$$
\mathbb E[p_jF]=\mathbb E\left[\sum_{a=0}^{j-1}p_ap_{j-1-a}F+
\sum_i u_i^j\frac{\partial F}{\partial u_i}\right],
$$
hence
$$
\mathbb E[U_1]=k^2,\quad\mathbb E[U_2]=2k^3,\quad
\mathbb E[V_1]=r^2,\quad\mathbb E[V_2]=2r^3.
$$
For the Gaussian ensemble,
$$
2\mathbb E[Z_{j+1}F]=\mathbb E\left[\sum_{a=0}^{j-1}Z_aZ_{j-1-a}F+
\sum_i z_i^j\frac{\partial F}{\partial z_i}\right],
$$
which gives
$$
\mathbb E[Z_1^2]=\frac l2,\quad \mathbb E[Z_2]=\frac{l^2}{2},\quad
\mathbb E[Z_4]=\frac{l(2l^2+1)}4,\quad
\mathbb E[Z_1Z_3]=\frac{3l^2}{4},\quad
\mathbb E[Z_3^2]=\frac{3l(4l^2+1)}8.
$$
Therefore
$$
\mathbb E[B]=14k^3-6k^2l-2k^2r-\frac94kl^2-\frac12kr^2
+\frac98l^3-\frac9{16}l^2r-\frac34lr^2+\frac9{16}l+2r^3,
$$
and
$$
\frac12\mathbb E[A^2]
=\frac92k^2l-\frac{27}{8}kl^2-\frac92klr
+\frac{27}{32}l^3+\frac{27}{16}l^2r+\frac98lr^2+\frac{27}{128}l.
$$
Thus
$$
\mathcal Q=14k^3+2r^3-\frac32k^2l-2k^2r-\frac{45}{8}kl^2-\frac92klr-\frac12kr^2
+\frac{63}{32}l^3+\frac98l^2r+\frac38lr^2+\frac{99}{128}l.
$$
The perturbing factor gives
$$
h=-k+2r,\quad d=-\frac{k}{2}-2r,\quad
\mathbb E[T]=3k^2-\frac{k}{3}+\frac{8r}{3}-\frac{3r^2}{4},
$$
and
$$
J:=\frac3{\sqrt2}\mathbb E[AZ_1]=\frac{9l}{4}\left(2k-r-\frac{3l}{4}\right).
$$
Hence
$$
\alpha=\mathcal Q+d+\frac{h^2}{2},\qquad
\beta=\mathbb E[T]+h\mathcal Q+hd+\frac{h^3}{6}+J.
$$
For $(k,l,r)=(m,2m+1,m+1)$,
$$
(\mathcal Q,h,d,\mathbb E[T],J)=\left(\frac{2030m+799}{128},m+2,-\frac{5m+4}{2},
\frac{27m^2+10m+23}{12},-\frac9{16}(2m+1)(2m+7)\right).
$$
Thus
$$
\alpha=\frac{2030m+799}{128}-\frac{5m+4}{2}+\frac{(m+2)^2}{2}
=\frac{64m^2+1966m+799}{128},
$$
$$
\beta=\frac{27m^2+10m+23}{12}+\frac{(m+2)(2030m+799)}{128}
-\frac{(m+2)(5m+4)}{2}+\frac{(m+2)^3}{6}
-\frac9{16}(2m+1)(2m+7)
=\frac{64m^3+5514m^2+9521m+2994}{384}.
$$
For $(m+1,2m+1,m)$,
$$
(\mathcal Q,h,d,\mathbb E[T],J)=\left(\frac{2030m+1231}{128},m-1,-\frac{5m+1}{2},
\frac{27m^2+100m+32}{12},-\frac9{16}(2m-5)(2m+1)\right),
$$
so
$$
\alpha=\frac{2030m+1231}{128}-\frac{5m+1}{2}+\frac{(m-1)^2}{2}
=\frac{64m^2+1582m+1231}{128},
$$
$$
\beta=\frac{27m^2+100m+32}{12}+\frac{(m-1)(2030m+1231)}{128}
-\frac{(m-1)(5m+1)}{2}+\frac{(m-1)^3}{6}
-\frac9{16}(2m-5)(2m+1)
=\frac{64m^3+4938m^2+3491m-1461}{384}.
$$
For $(m,2m+2,m)$,
$$
\alpha=\frac{27(73m+41)}{64}-\frac{5m}{2}+\frac{m^2}{2}
=\frac{32m^2+1811m+1107}{64},
$$
and for $(m+1,2m,m+1)$,
$$
\alpha=\frac{27(73m+32)}{64}-\frac{5m+5}{2}+\frac{(m+1)^2}{2}
=\frac{32m^2+1875m+736}{64}.
$$

Step 5: Combine the four cluster expansions

After division by $C_mt^{4m^2+4m+3/2}$, the dominant leading weights are $\frac12,\frac12$ and the neighboring weights are $\frac{r_m}{2},\frac{s_m}{2}$. Thus
$$
\frac{D_m(t)}{C_mt^{4m^2+4m+3/2}}=1+c_1q+c_2q^2+c_3q^3+o(q^3),
$$
where
$$
c_1=m+\frac12+\frac{r_m+s_m}{2},
$$
$$
c_2=\frac{64m^2+1774m+1015}{128}+\frac{mr_m+(m+1)s_m}{2},
$$
and
$$
c_3=\frac{128m^3+10452m^2+13012m+1533}{768}
+\frac{r_m(32m^2+1811m+1107)+s_m(32m^2+1875m+736)}{128}.
$$
Since $q^3=t^{3/2}$, the prescribed subtraction removes the $q$ and $q^2$ terms.

Final Answer: $\boxed{\frac{128m^3+10452m^2+13012m+1533}{768}+\frac{r_m(32m^2+1811m+1107)+s_m(32m^2+1875m+736)}{128}}$

---

## Answer

$\frac{128m^3+10452m^2+13012m+1533}{768}+\frac{r_m(32m^2+1811m+1107)+s_m(32m^2+1875m+736)}{128}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- competing Laplace clusters
- Hankel determinant integrals
- Gaussian and Laguerre moment recurrences
- perturbative asymptotic expansion

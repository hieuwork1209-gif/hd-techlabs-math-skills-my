## Steps

Step 1: Isolate the four relevant cluster allocations

Put
$$
q=\sqrt t,\qquad \phi(x)=x(1-x)(3x-1)^2.
$$
By Andreief,
$$
D_m(t)=\frac1{(4m+2)!}\int_{[0,1]^{4m+2}}\Delta(x)^2
\prod_i(1+q(3x_i-1))e^{-\phi(x_i)/t}\,dx_i.
$$
The phase vanishes only at $0,\frac13,1$, so all other regions are exponentially small. Use
$$
x=q^2u,\qquad x=\frac13+\frac q{\sqrt2}z,\qquad x=1-\frac{q^2}{4}v.
$$
If $(k,l,r)$ variables occupy these three wells, the Jacobians and internal Vandermondes contribute
$$
t^{E(k,l,r)},\qquad E(k,l,r)=k^2+\frac{l^2}{2}+r^2.
$$
Write $k=m+a$, $r=m+c$, $l=2m+2-a-c$, and set $u=2a-1$, $v=2c-1$. Then
$$
E-\left(4m^2+4m+\frac32\right)
=\frac{3u^2+2uv+3v^2-4}{8}.
$$
To affect the expansion through $t^{3/2}$, the gap is at most $3/2$, which forces $u,v\in\{-1,1\}$. Hence only
$$
A_1=(m,2m+1,m+1),\quad A_2=(m+1,2m+1,m)
$$
have gap $0$, while
$$
A_3=(m,2m+2,m),\quad A_4=(m+1,2m,m+1)
$$
have gap $1/2$, i.e. one extra factor $q$.

Step 2: Compute the leading cluster constants

For the Laguerre and Gaussian Vandermonde integrals,
$$
L_n=\prod_{j=0}^{n-1}(j!)^2,
\qquad
G_n=\pi^{n/2}2^{-n(n-1)/2}\prod_{j=0}^{n-1}j!.
$$
Indeed these follow from the monic Laguerre and Hermite squared norms
$$
h_j^{(L)}=(j!)^2,\qquad h_j^{(G)}=\sqrt\pi\,2^{-j}j!,
$$
via $\int\Delta^2\prod w=n!\prod h_j$.

Under the three scalings, the left, middle, and right internal factors are respectively
$$
q^{2k^2},\qquad q^{l^2}2^{-l^2/2},\qquad q^{2r^2}4^{-r^2},
$$
and the limiting cross distances contribute $3^{-2kl}(4/9)^{rl}$. Thus
$$
K_{k,l,r}
=2^{-2r^2+2rl-l^2+l/2}3^{-2l(k+r)}
\pi^{l/2}L_kL_r\prod_{j=0}^{l-1}j!.
$$
Directly comparing with $C_m$ gives
$$
K_{A_1}=K_{A_2}=\frac{C_m}{2},\qquad
K_{A_3}=\frac{C_mr_m}{2},\qquad
K_{A_4}=\frac{C_ms_m}{2}.
$$
For example, using $L_{n+1}/L_n=(n!)^2$,
$$
\frac{K_{A_3}}{C_m/2}
=9\,2^{-2m-5/2}\sqrt\pi\frac{(2m+1)!}{(m!)^2}=r_m,
$$
and the $A_4$ ratio similarly equals $s_m$.

Step 3: Expand one local cluster through order $q^3$

Write
$$
U_j=\sum_{i=1}^ku_i^j,\qquad V_j=\sum_{i=1}^rv_i^j,\qquad Z_j=\sum_{i=1}^lz_i^j.
$$
The phase contributes
$$
-\frac{3}{2\sqrt2}qZ_3
+q^2\left(7U_2+V_2+\frac94Z_4\right)+O(q^4).
$$
For every cross pair we use the single Taylor formula
$$
2\log(1+aq+bq^2)
=2aq+(2b-a^2)q^2+\left(-2ab+\frac{2a^3}{3}\right)q^3+O(q^4).
$$
The three normalized cross distances give
$$
\begin{array}{c|c|c|l}
 & a & b & \text{logarithm through }q^3\\ \hline
LM&3z/\sqrt2&-3u&
3\sqrt2zq+(-6u-\frac92z^2)q^2+9\sqrt2(uz+\frac12z^3)q^3\\[2mm]
MR&-3z/(2\sqrt2)&-3v/8&
-\frac{3\sqrt2}{2}zq+(-\frac34v-\frac98z^2)q^2-\frac{9\sqrt2}{16}(vz+z^3)q^3\\[2mm]
LR&0&-(u+v/4)&(-2u-\frac12v)q^2
\end{array}
$$
(the last line is $2\log(1-q^2(u+v/4))$). Summing these pairwise coefficients and adding the phase gives
$$
qA+q^2B+q^3C+O(q^4),
$$
where
$$
A=\frac{3}{2\sqrt2}\bigl((4k-2r)Z_1-Z_3\bigr),
$$
$$
B=7U_2+V_2-(6l+2r)U_1
-\left(\frac{3l}{4}+\frac{k}{2}\right)V_1
+\frac94Z_4-\left(\frac{9k}{2}+\frac{9r}{8}\right)Z_2,
$$
$$
C=9\sqrt2\left(U_1-\frac{V_1}{16}\right)Z_1
+\frac{9\sqrt2}{16}(8k-r)Z_3.
$$
This summation uses only
$\sum_{i,j}z_j=kZ_1$, $\sum_{i,j}u_i=lU_1$, and
$\sum_{i,j}u_iz_j=U_1Z_1$ (and the analogous right-hand identities).

For the remainder, restrict first to $|u_i|,|v_i|,|z_i|\le R_q$ with $R_q=q^{-1/16}$. The omitted Taylor terms give a logarithmic correction $S_q=O(qR_q^3)$, hence
$$
e^{S_q}-1-S_q-\frac{S_q^2}{2}-\frac{S_q^3}{6}
=O(q^4R_q^{12})=O(q^{13/4})=o(q^3).
$$
Outside this core, the Laguerre/Gaussian weights give exponentially small tails. Thus termwise integration through $q^3$ is justified.

Step 4: Evaluate the required moments without repeated bookkeeping

For the Laguerre ensemble, with $U_0=k$, integration by parts gives
$$
\mathbb E[U_jF]
=\mathbb E\left[\sum_{a=0}^{j-1}U_aU_{j-1-a}F
+\sum_i u_i^j\partial_iF\right].
$$
Taking $F=1$, $j=1,2$ yields
$$
\mathbb E[U_1]=k^2,\qquad \mathbb E[U_2]=2k^3,
$$
and similarly
$$
\mathbb E[V_1]=r^2,\qquad \mathbb E[V_2]=2r^3.
$$

For the Gaussian ensemble, with $Z_0=l$,
$$
2\mathbb E[Z_{j+1}F]
=\mathbb E\left[\sum_{a=0}^{j-1}Z_aZ_{j-1-a}F
+\sum_i z_i^j\partial_iF\right].
$$
The moments needed in $B$ and $A^2$ follow in five short applications:
$$
2\mathbb E[Z_1^2]=l,\qquad 2\mathbb E[Z_2]=l^2,
$$
$$
2\mathbb E[Z_4]
=2l\mathbb E[Z_2]+\mathbb E[Z_1^2]
=l^3+\frac l2,
$$
$$
2\mathbb E[Z_1Z_3]
=2l\mathbb E[Z_1^2]+\mathbb E[Z_2]
=\frac{3l^2}{2},
$$
$$
2\mathbb E[Z_3^2]
=2l\mathbb E[Z_1Z_3]+3\mathbb E[Z_4]
=\frac{3l(4l^2+1)}4.
$$
Hence
$$
\mathbb E[Z_4]=\frac{l(2l^2+1)}4,\quad
\mathbb E[Z_1Z_3]=\frac{3l^2}{4},\quad
\mathbb E[Z_3^2]=\frac{3l(4l^2+1)}8.
$$
Substitution into $\mathbb E[B+A^2/2]$ gives
$$
\mathcal Q=
14k^3+2r^3-\frac32k^2l-2k^2r-\frac{45}{8}kl^2
-\frac92klr-\frac12kr^2
+\frac{63}{32}l^3+\frac98l^2r+\frac38lr^2+\frac{99}{128}l.
$$

The remaining factor $\prod_i(1+q(3x_i-1))$ has one-variable logarithms
$$
-q-\frac{q^2}{2}+q^3\left(3u-\frac13\right),\qquad
\frac{3}{\sqrt2}q^2z,\qquad
2q-2q^2+q^3\left(\frac83-\frac34v\right),
$$
for the left, middle, and right wells. Therefore its total logarithm is
$$
qh+q^2\left(d+\frac3{\sqrt2}Z_1\right)+q^3T+O(q^4),
$$
with
$$
h=-k+2r,\qquad d=-\frac k2-2r,
$$
$$
\mathbb E[T]=3k^2-\frac k3+\frac{8r}{3}-\frac{3r^2}{4}.
$$
By $z\mapsto-z$ symmetry the odd Gaussian terms vanish except
$$
J:=\frac3{\sqrt2}\mathbb E[AZ_1]
=\frac{9l}{4}\left(2k-r-\frac{3l}{4}\right).
$$
Thus a cluster with exponent gap $0$ has local expansion
$$
1+hq+\alpha q^2+\beta q^3+o(q^3),
$$
where
$$
\alpha=\mathcal Q+d+\frac{h^2}{2},\qquad
\beta=\mathbb E[T]+h\mathcal Q+hd+\frac{h^3}{6}+J.
$$

Now use the common parametrization
$$
k=m+a,\qquad r=m+c,\qquad l=2m+2-a-c,\qquad a,c\in\{0,1\}.
$$
Instead of four separate polynomial expansions, substituting this once into $\mathcal Q$ and using $a^2=a$, $c^2=c$ gives
$$
128\mathcal Q
=3942m+2214-(1912m+983)a-(1912m+1415)c
+(3824m+1912)ac.
$$
Therefore, in the order $A_1,A_2,A_3,A_4$,
$$
128(\mathcal Q_1,\mathcal Q_2,\mathcal Q_3,\mathcal Q_4)
=(2030m+799,\ 2030m+1231,\ 3942m+2214,\ 3942m+1728),
$$
while
$$
(h_1,h_2,h_3,h_4)=(m+2,m-1,m,m+1),
$$
$$
2(d_1,d_2,d_3,d_4)=(-(5m+4),-(5m+1),-5m,-5m-5).
$$
For the two dominant clusters,
$$
(\mathbb E[T]_1,J_1)
=\left(\frac{27m^2+10m+23}{12},-\frac9{16}(2m+1)(2m+7)\right),
$$
$$
(\mathbb E[T]_2,J_2)
=\left(\frac{27m^2+100m+32}{12},-\frac9{16}(2m-5)(2m+1)\right).
$$
Hence
$$
\alpha_1=\frac{64m^2+1966m+799}{128},\qquad
\alpha_2=\frac{64m^2+1582m+1231}{128},
$$
$$
\alpha_3=\frac{32m^2+1811m+1107}{64},\qquad
\alpha_4=\frac{32m^2+1875m+736}{64},
$$
and
$$
\beta_1=\frac{64m^3+5514m^2+9521m+2994}{384},
$$
$$
\beta_2=\frac{64m^3+4938m^2+3491m-1461}{384}.
$$
The neighbor clusters already carry an extra factor $q$, so their $\beta$ terms would be global order $q^4$ and are not needed.

Step 5: Combine the four clusters

After dividing by $C_mt^{4m^2+4m+3/2}$,
$$
\frac{D_m(t)}{C_mt^{4m^2+4m+3/2}}
=1+c_1q+c_2q^2+c_3q^3+o(q^3).
$$
Using the weights $\frac12,\frac12,\frac{r_m}{2},\frac{s_m}{2}$,
$$
c_1=\frac{h_1+h_2}{2}+\frac{r_m+s_m}{2}
=m+\frac12+\frac{r_m+s_m}{2},
$$
$$
c_2=\frac{\alpha_1+\alpha_2}{2}
+\frac{r_mh_3+s_mh_4}{2}
=\frac{64m^2+1774m+1015}{128}
+\frac{mr_m+(m+1)s_m}{2},
$$
and
$$
\begin{aligned}
c_3
&=\frac{\beta_1+\beta_2}{2}
+\frac{r_m\alpha_3+s_m\alpha_4}{2}\\
&=\frac{128m^3+10452m^2+13012m+1533}{768}\\
&\quad+\frac{r_m(32m^2+1811m+1107)+s_m(32m^2+1875m+736)}{128}.
\end{aligned}
$$
Since $q^3=t^{3/2}$ and the prescribed subtraction removes $c_1q+c_2q^2$, the requested limit is
$$
\boxed{
\frac{128m^3+10452m^2+13012m+1533}{768}
+\frac{r_m(32m^2+1811m+1107)+s_m(32m^2+1875m+736)}{128}
}.
$$

---

## Answer

$\displaystyle \frac{128m^3+10452m^2+13012m+1533}{768}
+\frac{r_m(32m^2+1811m+1107)+s_m(32m^2+1875m+736)}{128}$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- competing Laplace clusters
- Hankel determinant / Vandermonde integrals
- Gaussian and Laguerre moment recurrences
- perturbative asymptotic expansion
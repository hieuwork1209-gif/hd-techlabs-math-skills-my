## Steps

Step 1: Identify the dominant and neighboring cluster allocations

Put
$$
q=\sqrt{t},\qquad \phi(x)=x(1-x)(3x-1)^2.
$$
Andréief's identity gives
$$
D_m(t)=\frac{1}{(4m+2)!}\int_{[0,1]^{4m+2}}
\prod_{i<j}(x_i-x_j)^2
\prod_i\left(1+q(3x_i-1)\right)e^{-\frac{\phi(x_i)}{t}}\,dx_i.
$$
Outside disjoint fixed neighborhoods of $0,\frac{1}{3},1$, the phase has a positive minimum, so those contributions are exponentially small. In the three wells use
$$
x=q^2u,\qquad x=\frac{1}{3}+\frac{q}{\sqrt{2}}z,\qquad x=1-\frac{q^2}{4}v.
$$
For an allocation $(k,l,r)$, the Jacobians and internal squared Vandermonde factors give
$$
t^{E(k,l,r)},\qquad E(k,l,r)=k^2+\frac{l^2}{2}+r^2,\qquad k+l+r=4m+2.
$$
Writing $k=m+a$, $r=m+c$, $l=2m+2-a-c$, and then $u=2a-1$, $v=2c-1$, gives
$$
E(k,l,r)-\left(4m^2+4m+\frac{3}{2}\right)
=\frac{3u^2+2uv+3v^2-4}{8}.
$$
If this gap is at most $\frac{3}{2}$, then
$$
3u^2+2uv+3v^2=2u^2+2v^2+(u+v)^2\leq16.
$$
Since $u,v$ are odd, this forces $u,v\in\{-1,1\}$. Hence the dominant allocations are
$$
(m,2m+1,m+1),\qquad (m+1,2m+1,m),
$$
and the only neighboring allocations contributing through relative order $q^3$ are
$$
(m,2m+2,m),\qquad (m+1,2m,m+1).
$$

Step 2: Evaluate the four leading local constants

Define
$$
L_n=\prod_{j=0}^{n-1}(j!)^2,\qquad
G_n=\pi^{\frac{n}{2}}2^{-\frac{n(n-1)}{2}}\prod_{j=0}^{n-1}j!.
$$
For labeled variables,
$$
\int_{[0,\infty)^n}\Delta(u)^2e^{-\sum_i u_i}\,du_1\cdots du_n=n!L_n,\qquad
\int_{\mathbb{R}^{n}}\Delta(z)^2e^{-\sum_i z_i^2}\,dz_1\cdots dz_n=n!G_n.
$$
The allocation $(k,l,r)$ occurs $\frac{(4m+2)!}{k!l!r!}$ times, so the Andréief prefactor cancels this multinomial factor and then the local factors $k!l!r!$. Thus
$$
K_{k,l,r}=4^{-r^2}2^{-\frac{l^2}{2}}3^{-2kl}\left(\frac{4}{9}\right)^{rl}L_kL_rG_l.
$$
Substituting $G_l$ gives the useful form
$$
K_{k,l,r}
=2^{-2r^2+2rl-l^2+\frac{l}{2}}3^{-2l(k+r)}
\pi^{\frac{l}{2}}L_kL_r\prod_{j=0}^{l-1}j!.
$$
For $(m,2m+1,m+1)$,
$$
-2r^2+2rl-l^2+\frac{l}{2}=-2m^2-m-\frac{1}{2},\qquad
-2l(k+r)=-8m^2-8m-2,
$$
so
$$
K_{m,2m+1,m+1}
=2^{-2m^2-m-\frac{1}{2}}3^{-8m^2-8m-2}\pi^{m+\frac{1}{2}}
L_mL_{m+1}\prod_{j=0}^{2m}j!=\frac{C_m}{2}.
$$
The allocation $(m+1,2m+1,m)$ has the same two powers and the same product $L_mL_{m+1}$, hence also equals $\frac{C_m}{2}$.

Using
$$
\frac{L_{n+1}}{L_n}=(n!)^2,\qquad
\frac{G_{n+1}}{G_n}=\sqrt{\pi}\,2^{-n}n!,
$$
the first neighboring ratio is
$$
\frac{K_{m,2m+2,m}}{K_{m,2m+1,m+1}}
=2^{-2m-\frac{5}{2}}3^2\pi^{\frac{1}{2}}
\frac{L_m}{L_{m+1}}
\frac{\prod_{j=0}^{2m+1}j!}{\prod_{j=0}^{2m}j!}
$$
$$
=9\,2^{-2m-\frac{5}{2}}\sqrt{\pi}\,\frac{(2m+1)!}{(m!)^2}
=\frac{9(2m+1)\sqrt{\pi}}{2^{2m+\frac{5}{2}}}\binom{2m}{m}=r_m,
$$
because $\frac{(2m+1)!}{(m!)^2}=(2m+1)\binom{2m}{m}$. Similarly,
$$
\frac{K_{m+1,2m,m+1}}{K_{m,2m+1,m+1}}
=2^{2m-\frac{3}{2}}3^2\pi^{-\frac{1}{2}}
\frac{L_{m+1}}{L_m}
\frac{\prod_{j=0}^{2m-1}j!}{\prod_{j=0}^{2m}j!}
$$
$$
=9\,2^{2m-\frac{3}{2}}\pi^{-\frac{1}{2}}\frac{(m!)^2}{(2m)!}
=\frac{9\,2^{2m-\frac{3}{2}}}{\sqrt{\pi}\binom{2m}{m}}=s_m.
$$

Step 3: Derive the local logarithmic expansion and control its remainder

For a cluster $(k,l,r)$ set
$$
U_j=\sum_{i=1}^k u_i^j,\qquad V_j=\sum_{i=1}^r v_i^j,\qquad Z_j=\sum_{i=1}^l z_i^j.
$$
The phase expansions are
$$
\frac{\phi(q^2u)}{q^2}=u-7q^2u^2+O(q^4),\quad
\frac{\phi(\frac{1}{3}+\frac{qz}{\sqrt{2}})}{q^2}
=z^2+\frac{3}{2\sqrt{2}}qz^3-\frac{9}{4}q^2z^4,\quad
\frac{\phi(1-\frac{q^2v}{4})}{q^2}=v-q^2v^2+O(q^4).
$$
The three cross-cluster logarithms are
$$
2\log\left(1+\frac{3}{\sqrt{2}}qz-3q^2u\right)
=3\sqrt{2}\,qz+q^2\left(-6u-\frac{9}{2}z^2\right)
+9\sqrt{2}\,q^3\left(uz+\frac{1}{2}z^3\right)+O(q^4),
$$
$$
2\log\left(1-\frac{3}{2\sqrt{2}}qz-\frac{3}{8}q^2v\right)
=-\frac{3\sqrt{2}}{2}qz+q^2\left(-\frac{3}{4}v-\frac{9}{8}z^2\right)
-\frac{9\sqrt{2}}{16}q^3(vz+z^3)+O(q^4),
$$
$$
2\log\left(1-q^2u-\frac{1}{4}q^2v\right)
=q^2\left(-2u-\frac{1}{2}v\right)+O(q^4).
$$
After summation the logarithmic correction is $qA+q^2B+q^3C+O(q^4)$, where
$$
A=\frac{3}{2\sqrt{2}}\left((4k-2r)Z_1-Z_3\right),
$$
$$
B=7U_2+V_2-(6l+2r)U_1-\left(\frac{3l}{4}+\frac{k}{2}\right)V_1
+\frac{9}{4}Z_4-\left(\frac{9k}{2}+\frac{9r}{8}\right)Z_2,
$$
$$
C=9\sqrt{2}\left(U_1-\frac{V_1}{16}\right)Z_1
+\frac{9\sqrt{2}}{16}(8k-r)Z_3.
$$

Take $R_q=q^{-\frac{1}{16}}$ and restrict first to
$$
0\leq u_i,v_i\leq R_q,\qquad |z_i|\leq R_q.
$$
The endpoint phases are exactly
$$
\frac{\phi(q^2u)}{q^2}=u-7q^2u^2+15q^4u^3-9q^6u^4,
$$
$$
\frac{\phi(1-\frac{q^2v}{4})}{q^2}
=v-q^2v^2+\frac{21}{64}q^4v^3-\frac{9}{256}q^6v^4.
$$
Hence their omitted terms are $O(q^4R_q^3)=o(q^3)$ on the core, while the logarithmic fourth-order remainders are $O((qR_q)^4)=o(q^3)$. Also
$$
A=O(R_q^3),\qquad B=O(R_q^4),\qquad C=O(R_q^3),
$$
so the full logarithmic correction $S_q$ satisfies $S_q=O(qR_q^3)=O(q^{\frac{13}{16}})$. The perturbing factor contributes only $O(q(1+R_q))$ to its logarithm, so this bound is unchanged. Therefore, uniformly on the core,
$$
\left|e^{S_q}-\left(1+S_q+\frac{S_q^2}{2}+\frac{S_q^3}{6}\right)\right|
\leq C|S_q|^4
=O(q^4R_q^{12})=O(q^{\frac{13}{4}})=o(q^3).
$$
When the cubic Taylor polynomial is collected by powers of $q$, every discarded monomial has $q$-degree at least $4$ and polynomial degree at most $12$, so it is also $O(q^4R_q^{12})=o(q^3)$.
Inside the fixed wells there is $c>0$ with
$$
\frac{\phi(q^2u)}{q^2}\geq cu,\qquad
\frac{\phi(\frac{1}{3}+\frac{qz}{\sqrt{2}})}{q^2}\geq cz^2,\qquad
\frac{\phi(1-\frac{q^2v}{4})}{q^2}\geq cv.
$$
The remaining factors grow at most polynomially, so the complement of the core is bounded by polynomial factors times $e^{-cR_q}$ or $e^{-cR_q^2}$, hence is $o(q^3)$. Thus exponentiation and termwise integration through order $q^3$ are justified.

Step 4: Evaluate the moments and the local coefficients

For a size-$n$ Laguerre ensemble, integration by parts gives
$$
\mathbb E[p_jF]=\mathbb E\left[
\sum_{a=0}^{j-1}p_ap_{j-1-a}F+\sum_i u_i^j\frac{\partial F}{\partial u_i}
\right],
$$
hence
$$
\mathbb E[U_1]=k^2,\qquad \mathbb E[U_2]=2k^3,
$$
and likewise $\mathbb E[V_1]=r^2$, $\mathbb E[V_2]=2r^3$. For the size-$l$ Gaussian ensemble,
$$
2\mathbb E[Z_{j+1}F]=\mathbb E\left[
\sum_{a=0}^{j-1}Z_aZ_{j-1-a}F+\sum_i z_i^j\frac{\partial F}{\partial z_i}
\right],
$$
which yields
$$
\mathbb E[Z_1^2]=\frac{l}{2},\quad
\mathbb E[Z_2]=\frac{l^2}{2},\quad
\mathbb E[Z_4]=\frac{l(2l^2+1)}{4},\quad
\mathbb E[Z_1Z_3]=\frac{3l^2}{4},\quad
\mathbb E[Z_3^2]=\frac{3l(4l^2+1)}{8}.
$$
Substitution into $B$ gives
$$
\mathbb E[B]
=14k^3-6k^2l-2k^2r-\frac{9}{4}kl^2-\frac{1}{2}kr^2
+\frac{9}{8}l^3-\frac{9}{16}l^2r-\frac{3}{4}lr^2+\frac{9}{16}l+2r^3.
$$
Since
$$
A=\frac{3}{2\sqrt{2}}\left((4k-2r)Z_1-Z_3\right),
$$
the three Gaussian moments above give
$$
\frac{1}{2}\mathbb E[A^2]
=\frac{9}{16}\left((4k-2r)^2\frac{l}{2}
-2(4k-2r)\frac{3l^2}{4}+\frac{3l(4l^2+1)}{8}\right)
$$
$$
=\frac{9}{2}k^2l-\frac{27}{8}kl^2-\frac{9}{2}klr
+\frac{27}{32}l^3+\frac{27}{16}l^2r+\frac{9}{8}lr^2+\frac{27}{128}l.
$$
Therefore
$$
\mathcal Q(k,l,r)=\mathbb E[B]+\frac{1}{2}\mathbb E[A^2]
$$
$$
=14k^3+2r^3-\frac{3}{2}k^2l-2k^2r-\frac{45}{8}kl^2-\frac{9}{2}klr-\frac{1}{2}kr^2
+\frac{63}{32}l^3+\frac{9}{8}l^2r+\frac{3}{8}lr^2+\frac{99}{128}l.
$$

The perturbing factor has logarithm
$$
qh+q^2\left(d+\frac{3}{\sqrt{2}}Z_1\right)+q^3T+O(q^4),
$$
where
$$
h=-k+2r,\qquad d=-\frac{k}{2}-2r,\qquad
T=3U_1-\frac{k}{3}+\frac{8r}{3}-\frac{3}{4}V_1.
$$
By Step 3, expansion of the full exponential is valid through $q^3$. Parity gives
$$
\mathbb E[C]=\mathbb E[AB]=\mathbb E[A^3]=0.
$$
Hence
$$
\alpha(k,l,r)=\mathcal Q(k,l,r)+d+\frac{h^2}{2},
$$
and
$$
\beta(k,l,r)=\mathbb E[T]+h\mathcal Q(k,l,r)+hd+\frac{h^3}{6}
+\frac{3}{\sqrt{2}}\mathbb E[AZ_1],
$$
with
$$
\mathbb E[T]=3k^2-\frac{k}{3}+\frac{8r}{3}-\frac{3r^2}{4},\qquad
\frac{3}{\sqrt{2}}\mathbb E[AZ_1]
=\frac{9l}{4}\left(2k-r-\frac{3l}{4}\right).
$$
Substitution gives
$$
\begin{array}{c|c|c}
(k,l,r)&\alpha&\beta\\ \hline
(m,2m+1,m+1)&\frac{64m^2+1966m+799}{128}&\frac{64m^3+5514m^2+9521m+2994}{384}\\
(m+1,2m+1,m)&\frac{64m^2+1582m+1231}{128}&\frac{64m^3+4938m^2+3491m-1461}{384}
\end{array}
$$
and for the two neighboring allocations,
$$
\alpha(m,2m+2,m)=\frac{32m^2+1811m+1107}{64},\qquad
\alpha(m+1,2m,m+1)=\frac{32m^2+1875m+736}{64}.
$$

Step 5: Combine the four cluster expansions and evaluate the limit

After division by $C_mt^{4m^2+4m+\frac{3}{2}}$, the two dominant clusters have leading weights $\frac{1}{2}$, while the neighboring clusters have leading weights $\frac{r_m}{2}$ and $\frac{s_m}{2}$. Thus
$$
\frac{D_m(t)}{C_mt^{4m^2+4m+\frac{3}{2}}}
=1+c_1q+c_2q^2+c_3q^3+o(q^3),
$$
where the coefficients from Step 4 are
$$
c_1=m+\frac{1}{2}+\frac{r_m+s_m}{2},
$$
$$
c_2=\frac{64m^2+1774m+1015}{128}
+\frac{mr_m+(m+1)s_m}{2},
$$
and
$$
c_3=\frac{128m^3+10452m^2+13012m+1533}{768}
+\frac{r_m(32m^2+1811m+1107)+s_m(32m^2+1875m+736)}{128}.
$$
Since $q^3=t^{\frac{3}{2}}$, the prescribed subtraction removes the $q$ and $q^2$ terms.

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

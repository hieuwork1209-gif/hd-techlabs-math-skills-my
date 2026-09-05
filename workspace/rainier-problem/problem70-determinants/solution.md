## Steps

Step 1: Convert the determinant to a stationary product
For
$$
A_N(a)=S_1(N,a)=B(a,N+1),
$$
we have $S_2(N,a)=-A_N'(a)$. Put $L=\log n$, $N=n^3$,
$$
m_1=\left\lfloor\frac{n^2}{3}\right\rfloor,\qquad m_2=n^2,
$$
and write
$$
F(a)=T_1(n,a),\qquad G(a)=U_1(n,a).
$$
Then $T_2=-F'$ and $U_2=-G'$, so the determinant condition is $(G/F)'=0$. Define
$$
p_n(a)=\frac{e^2A_N(a)}{F(a)},\qquad
r_i(a)=\frac{A_{N+m_i}(a)}{A_N(a)}\quad(i=1,2),
$$
$$
h_n(a)=1-\frac34r_1(a)-\frac14r_2(a).
$$
Since $G/F=1-p_nh_n$, the root equation is exactly
$$
\frac{d}{da}\log p_n(a)+\frac{d}{da}\log h_n(a)=0.
$$

Step 2: Identify the unchanged limiting equation
Put $c=aL$. With
$$
R_q(a)=\frac{\Gamma(n^q+1)}{\Gamma(n^q+a+1)},\qquad
\rho_q(a)=\frac{e^{q-1}R_q(a)}{\sum_{j=1}^3e^{j-1}R_j(a)},
$$
we have
$$
\frac1L\frac{d}{da}\log p_n
=\frac1L\left(\sum_{q=1}^3\rho_q\psi(n^q+a+1)-\psi(n^3+a+1)\right).
$$
For
$$
s_i=\sum_{j=1}^{m_i}\frac1{N+j},
$$
one has $r_i=1-a s_i+o(a/n)$ uniformly for fixed $c$ near $1$, hence $h_n=a(\frac34s_1+\frac14s_2)(1+o(1))$. Therefore the normalized root equation tends to
$$
H_0(c)=\frac1c+\sum_{q=1}^3q\pi_q(c)-3,
\qquad
\pi_q(c)=\frac{e^{q-1-qc}}{\sum_{j=1}^3e^{j-1-jc}}.
$$
At $c=1$ the weights are uniform, so $H_0(1)=0$ and
$$
H_0'(1)=-1-\operatorname{Var}_{\{1,2,3\}}(q)=-\frac53.
$$
Thus the nearby limiting root is simple and unique.

Step 3: Expand the base-column bias
At $c=1$, so $a=1/L$,
$$
R_q(a)=n^{-qa}\left(1-\frac{a(a+1)}{2n^q}+O\!\left(\frac{a}{n^{2q}}\right)\right),
$$
and
$$
\psi(n^q+a+1)=qL+\frac{a+1/2}{n^q}+O(n^{-2q}).
$$
Only $q=1$ contributes at the required finite-size scale. Expanding the normalized weighted average gives
$$
\frac1L\frac{d}{da}\log p_n
=-1+\frac{a(a+1)}{6n}+\frac{a+1/2}{3nL}+o((nL^2)^{-1}).
$$
Substituting $a=1/L$,
$$
\frac1L\frac{d}{da}\log p_n
=-1+\frac{1}{3nL}+\frac{1}{2nL^2}+o((nL^2)^{-1}).
$$

Step 4: Use the hidden shift-moment ratio
Set
$$
\mu_k=\frac34s_1^k+\frac14s_2^k.
$$
The product formula for $r_i$ gives
$$
\log r_i=-a s_i+O(a^2n^{-4}),
$$
so
$$
h_n=a\mu_1-\frac{a^2}{2}\mu_2+O(a^2n^{-4}+a^3n^{-3}).
$$
Consequently
$$
\frac{d}{da}\log h_n
=\frac1a-\frac{\mu_2}{2\mu_1}+O(an^{-2}).
$$
Now
$$
s_1=\frac{1}{3n}+O(n^{-2}),\qquad s_2=\frac1n+O(n^{-2}),
$$
whence
$$
\mu_1=\frac{1}{2n}+O(n^{-2}),\qquad
\mu_2=\frac{1}{3n^2}+O(n^{-3}),
$$
and therefore
$$
\frac{\mu_2}{\mu_1}=\frac{2}{3n}+O(n^{-2}).
$$
Thus at $a=1/L$,
$$
\frac1L\frac{d}{da}\log h_n
=1-\frac{1}{3nL}+o((nL^2)^{-1}).
$$
The load-bearing correction depends on $\mu_2/\mu_1$, not on the average shift $\mu_1$. Combining with Step 3 gives
$$
H_n(1)=\frac{1}{2nL^2}+o((nL^2)^{-1}).
$$

Step 5: Extract the root displacement
Since the normalized equations converge in $C^1$ near $1$ and $H_0'(1)=-5/3$, the unique nearby zero $c_n=a_nL$ satisfies
$$
c_n-1=-\frac{H_n(1)}{H_0'(1)}+o((nL^2)^{-1})
=\frac{3}{10nL^2}+o((nL^2)^{-1}).
$$
Hence
$$
n(\log n)^2(a_n\log n-1)\longrightarrow\frac3{10}.
$$

Final Answer: $\boxed{\frac3{10}}$

---

## Answer

$\frac3{10}$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Exact scalar

---

## Solution Concepts

- determinant stationary condition
- mixed mesoscopic cutoffs
- shift-moment cancellation
- Beta and digamma asymptotics
- competing asymptotic scales

---

## Black-Box Audit — no issues found

The hardening is structural: replacing one shifted cutoff by a two-cutoff mixture destroys the single-product recurrence shortcut. The first correction is controlled by the second-to-first moment ratio of the two shifts, which is tuned to preserve the previous cancellation while forcing the solver to identify the hidden mixture invariant.

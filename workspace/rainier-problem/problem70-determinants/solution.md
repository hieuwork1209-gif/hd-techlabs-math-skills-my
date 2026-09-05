## Steps

Step 1: Convert the determinant to a stationary product
For
$$
A_N(a)=S_1(N,a)=B(a,N+1),
$$
we have $S_2(N,a)=-A_N'(a)$. Put $L=\log n$, $N=n^3$, $t=n^{-1/2}$,
$$
m_j=\lfloor jn^{5/2}\rfloor\qquad(j=1,2,3),
$$
and
$$
b_1=\frac{27-5t}{19},\qquad b_2=\frac{-9+10t}{19},\qquad b_3=\frac{1-5t}{19}.
$$
Write
$$
F(a)=T_1(n,a),\qquad G(a)=U_1(n,a).
$$
Then $T_2=-F'$ and $U_2=-G'$, so the determinant condition is $(G/F)'=0$. Define
$$
\rho_n(a)=\frac{e^2A_N(a)}{F(a)},\qquad
r_j(a)=\frac{A_{N+m_j}(a)}{A_N(a)},
$$
$$
h_n(a)=1-\sum_{j=1}^3b_jr_j(a).
$$
Since $b_1+b_2+b_3=1$ and $G/F=1-\rho_nh_n$, the root equation is exactly
$$
\frac{d}{da}\log\rho_n(a)+\frac{d}{da}\log h_n(a)=0.
$$

Step 2: Identify the unchanged limiting equation
Put $c=aL$. With
$$
R_q(a)=\frac{\Gamma(n^q+1)}{\Gamma(n^q+a+1)},\qquad
w_q(a)=\frac{e^{q-1}R_q(a)}{\sum_{j=1}^3e^{j-1}R_j(a)},
$$
we have
$$
\frac1L\frac{d}{da}\log\rho_n
=\frac1L\left(\sum_{q=1}^3w_q\psi(n^q+a+1)-\psi(n^3+a+1)\right).
$$
For
$$
s_j=\sum_{k=1}^{m_j}\frac1{N+k},
$$
one has $r_j=e^{-as_j}(1+o(n^{-2}))$. Also
$$
\sum_{j=1}^3b_js_j=\frac{12}{19}t+O(t^3)>0,
$$
so $h_n=a\Theta(t)(1+o(1))$. Hence the normalized root equation tends to
$$
H_0(c)=\frac1c+\sum_{q=1}^3q\pi_q(c)-3,
\qquad
\pi_q(c)=\frac{e^{q-1-qc}}{\sum_{j=1}^3e^{j-1-jc}}.
$$
At $c=1$ the weights are uniform, so
$$
H_0(1)=0,\qquad H_0'(1)=-1-\operatorname{Var}_{\{1,2,3\}}(q)=-\frac53.
$$
Thus the nearby limiting root is simple and unique.

Step 3: Record the base-column finite-size bias
At $c=1$, so $a=1/L$,
$$
R_q(a)=n^{-qa}\left(1-\frac{a(a+1)}{2n^q}+O\!\left(\frac{a}{n^{2q}}\right)\right),
$$
and
$$
\psi(n^q+a+1)=qL+\frac{a+1/2}{n^q}+O(n^{-2q}).
$$
Only $q=1$ contributes before order $n^{-3/2}$. Therefore
$$
\frac1L\frac{d}{da}\log\rho_n
=-1+\frac{1}{3nL}+\frac{1}{2nL^2}
+o\!\left(\frac1{n^{3/2}L}\right).
$$

Step 4: Expose the signed-stencil moment cancellation
Set
$$
\mu_k=\sum_{j=1}^3b_js_j^k.
$$
Since
$$
s_j=\log(1+jt)+O(t^6),
$$
direct expansion gives
$$
\mu_1=\frac{12}{19}t-\frac1{19}t^3-\frac{11}{19}t^4+O(t^5),
$$
$$
\mu_2=\frac8{19}t^3+\frac{27}{19}t^4+O(t^5),
$$
$$
\mu_3=-\frac{18}{19}t^3-\frac6{19}t^4+O(t^5),
\qquad
\mu_4=-\frac{36}{19}t^4+O(t^5).
$$
Hence
$$
\frac{\mu_2}{\mu_1}=\frac23t^2+\frac94t^3+O(t^4),
$$
$$
\frac{\mu_3}{\mu_1}=-\frac32t^2-\frac12t^3+O(t^4),
\qquad
\frac{\mu_4}{\mu_1}=-3t^3+O(t^4).
$$
The key point is that the $t^2$ term of $\mu_2$ vanishes: the signed coefficients force the second shift moment to start one order later.

From
$$
h_n=a\mu_1-\frac{a^2}{2}\mu_2+\frac{a^3}{6}\mu_3-\frac{a^4}{24}\mu_4+\cdots,
$$
we obtain
$$
\frac{d}{da}\log h_n
=\frac1a-\frac{\mu_2}{2\mu_1}
+a\left(\frac{\mu_3}{3\mu_1}-\frac{\mu_2^2}{4\mu_1^2}\right)
-a^2\frac{\mu_4}{8\mu_1}+O(t^4).
$$
Substituting $a=L^{-1}$ and the ratios above,
$$
\frac1L\frac{d}{da}\log h_n
=1-\frac{1}{3nL}-\frac{1}{2nL^2}
+\frac1{n^{3/2}}\left(-\frac{9}{8L}-\frac{1}{6L^2}+\frac{3}{8L^3}\right)
+O(n^{-2}).
$$
The two order-$1/n$ terms cancel Step 3, while the new surviving term comes from the coupled second/third/fourth stencil moments. Thus
$$
H_n(1)=-\frac{9}{8n^{3/2}L}+o\!\left(\frac1{n^{3/2}L}\right).
$$

Step 5: Extract the new mesoscopic root displacement
Since $H_n\to H_0$ in $C^1$ near $1$ and $H_0'(1)=-5/3$, the unique nearby zero $c_n=a_nL$ satisfies
$$
c_n-1=-\frac{H_n(1)}{H_0'(1)}+o\!\left(\frac1{n^{3/2}L}\right)
=-\frac{27}{40n^{3/2}L}+o\!\left(\frac1{n^{3/2}L}\right).
$$
Therefore
$$
n^{3/2}(\log n)(a_n\log n-1)\longrightarrow-\frac{27}{40}.
$$

Final Answer: $\boxed{-\frac{27}{40}}$

---

## Answer

$-\frac{27}{40}$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Exact scalar

---

## Solution Concepts

- determinant stationary condition
- signed mesoscopic stencil
- shift-moment cancellation
- Beta and digamma asymptotics
- mesoscopic root displacement

---

## Black-Box Audit — no issues found

The hardening changes the asymptotic mechanism rather than merely adding another logarithmic Taylor term. A signed three-cutoff stencil cancels the leading second shift moment, so the first uncanceled perturbation occurs at the $n^{-3/2}$ scale and requires tracking the interaction of several shift moments.

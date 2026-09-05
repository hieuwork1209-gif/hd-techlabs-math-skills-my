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
and
$$
p_n=\frac34-\frac{9}{8L}.
$$
Write
$$
F(a)=T_1(n,a),\qquad G(a)=U_1(n,a).
$$
Then $T_2=-F'$ and $U_2=-G'$, so the determinant condition is $(G/F)'=0$. Define
$$
\rho_n(a)=\frac{e^2A_N(a)}{F(a)},\qquad
r_i(a)=\frac{A_{N+m_i}(a)}{A_N(a)}\quad(i=1,2),
$$
$$
h_n(a)=1-p_nr_1(a)-(1-p_n)r_2(a).
$$
Since $G/F=1-\rho_nh_n$, the root equation is exactly
$$
\frac{d}{da}\log \rho_n(a)+\frac{d}{da}\log h_n(a)=0.
$$

Step 2: Identify the limiting equation and its simple root
Put $c=aL$. With
$$
R_q(a)=\frac{\Gamma(n^q+1)}{\Gamma(n^q+a+1)},\qquad
w_q(a)=\frac{e^{q-1}R_q(a)}{\sum_{j=1}^3e^{j-1}R_j(a)},
$$
we have
$$
\frac1L\frac{d}{da}\log \rho_n
=\frac1L\left(\sum_{q=1}^3w_q\psi(n^q+a+1)-\psi(n^3+a+1)\right).
$$
Because both shifts are $O(n^2)$, $h_n(a)=a\Theta(n^{-1})(1+o(1))$. Hence for fixed $c$ near $1$ the normalized root equation tends to
$$
H_0(c)=\frac1c+\sum_{q=1}^3q\pi_q(c)-3,
$$
where
$$
\pi_q(c)=\frac{e^{q-1-qc}}{\sum_{j=1}^3e^{j-1-jc}}.
$$
At $c=1$ the weights are uniform, so $H_0(1)=0$ and
$$
H_0'(1)=-1-\operatorname{Var}_{\{1,2,3\}}(q)=-\frac53.
$$
Thus the nearby limiting root is simple and unique.

Step 3: Keep the base-column expansion through the second canceled scale
At $c=1$, so $a=1/L$,
$$
R_q(a)=n^{-qa}\left(1-\frac{a(a+1)}{2n^q}+O\!\left(\frac{a}{n^{2q}}\right)\right),
$$
and
$$
\psi(n^q+a+1)=qL+\frac{a+1/2}{n^q}+O(n^{-2q}).
$$
Only $q=1$ contributes at order $n^{-1}$. Expanding the normalized weighted average gives
$$
\frac1L\frac{d}{da}\log \rho_n
=-1+\frac{a(a+1)}{6n}+\frac{a+1/2}{3nL}
+o((nL^3)^{-1}).
$$
Substituting $a=1/L$,
$$
\frac1L\frac{d}{da}\log \rho_n
=-1+\frac{1}{3nL}+\frac{1}{2nL^2}
+o((nL^3)^{-1}).
$$
There is no $1/(nL^3)$ term from the base column.

Step 4: Track the varying hidden shift-moment ratio
Let
$$
s_i=\sum_{j=1}^{m_i}\frac1{N+j},\qquad
\mu_k=p_ns_1^k+(1-p_n)s_2^k.
$$
The product formula for $r_i$ gives
$$
h_n=a\mu_1-\frac{a^2}{2}\mu_2+O(a^2n^{-4}+a^3n^{-3}),
$$
so
$$
\frac{d}{da}\log h_n
=\frac1a-\frac{\mu_2}{2\mu_1}+O(an^{-2}).
$$
Now
$$
s_1=\frac{1}{3n}+O(n^{-2}),\qquad s_2=\frac1n+O(n^{-2}).
$$
Therefore
$$
\frac{\mu_2}{\mu_1}
=\frac1n\,
\frac{p_n/9+(1-p_n)}{p_n/3+(1-p_n)}+O(n^{-2}).
$$
Writing $z=L^{-1}$ and using $p_n=3/4-9z/8$, the rational factor is
$$
\frac{4(1+3z)}{3(2+3z)}
=\frac23+z-\frac32z^2+O(z^3).
$$
Hence
$$
\frac{\mu_2}{\mu_1}
=\frac1n\left(\frac23+\frac1L-\frac{3}{2L^2}+O(L^{-3})\right)+O(n^{-2}).
$$
At $a=1/L$ this yields
$$
\frac1L\frac{d}{da}\log h_n
=1-\frac{1}{3nL}-\frac{1}{2nL^2}
+\frac{3}{4nL^3}+o((nL^3)^{-1}).
$$
Thus the first two finite-size scales cancel against Step 3, and
$$
H_n(1)=\frac{3}{4nL^3}+o((nL^3)^{-1}).
$$

Step 5: Extract the third-scale root displacement
Since $H_n\to H_0$ in $C^1$ near $1$ and $H_0'(1)=-5/3$, the unique nearby zero $c_n=a_nL$ satisfies
$$
c_n-1=-\frac{H_n(1)}{H_0'(1)}+o((nL^3)^{-1})
=\frac{9}{20nL^3}+o((nL^3)^{-1}).
$$
Therefore
$$
n(\log n)^3(a_n\log n-1)\longrightarrow\frac9{20}.
$$

Final Answer: $\boxed{\frac9{20}}$

---

## Answer

$\frac9{20}$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Exact scalar

---

## Solution Concepts

- determinant stationary condition
- adaptive cutoff mixture
- shift-moment ratio
- nested asymptotic cancellation
- finite-size root displacement

---

## Black-Box Audit — no issues found

The hardening remains structural and local. The mixture weights now drift on the logarithmic scale, so the second-to-first shift-moment ratio must itself be expanded. This cancels both earlier finite-size terms and exposes a third asymptotic scale without enlarging the determinant or adding bookkeeping-heavy invariants.

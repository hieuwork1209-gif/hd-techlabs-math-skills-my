## Steps

Step 1: Rewrite the two normalized quantities as determinant-ratio derivatives
Put $c=aL$ and $P_n(a)=W_1/T_1=1-U_1/T_1$. Since
$$
T_1'=-T_2,\qquad T_1''=2T_3,
$$
and the same identities hold for $W_r$, direct differentiation gives
$$
H_n(a)=\frac{d}{dc}\log P_n(a),\qquad
K_n(a)=\frac{d^2}{dc^2}\log P_n(a)=\frac{dH_n}{dc}.
$$
Moreover
$$
H_n(a)=\frac{T_1U_2-U_1T_2}{L\,T_1W_1},
$$
so $H_n$ is precisely the normalized $2\times2$ determinant invariant from the previous stationary-ratio formulation. Define
$$
F_n(c)=K_n(c/L)+\frac{66}{125}H_n(c/L)^2+\frac65H_n(c/L)+\frac53.
$$
The defining equation is $F_n(c_n)=0$, where $c_n=a_nL$.

Step 2: Identify the limiting determinant invariant
Let $A_N(a)=S_1(N,a)=B(a,N+1)$ with $N=n^3$, and put
$$
r_j(a)=\frac{A_{N+m_j}(a)}{A_N(a)},\qquad
h_n(a)=1-\sum_{j=1}^3b_jr_j(a),
$$
$$
\rho_n(a)=\frac{e^2A_N(a)}{T_1(n,a)}.
$$
Then $P_n=\rho_nh_n$. For $c$ in a fixed neighborhood of $1$, beta-function asymptotics give, uniformly with the needed $c$-derivatives,
$$
H_n(c/L)\longrightarrow H_0(c)
=\frac1c+\sum_{q=1}^3q\pi_q(c)-3,
$$
where
$$
\pi_q(c)=\frac{e^{q-1-qc}}{\sum_{j=1}^3e^{j-1-jc}}.
$$
At $c=1$ the three weights are equal. Writing $d=c-1$ and expanding the elementary three-point log-sum gives
$$
H_0(1+d)=-\frac53d+d^2-\frac89d^3+d^4+O(d^5).
$$
Hence
$$
H_0(1)=0,\quad H_0'(1)=-\frac53,\quad H_0''(1)=2,
$$
$$
H_0'''(1)=-\frac{16}{3},\qquad H_0''''(1)=24.
$$

Step 3: Verify the designed cubic degeneracy
Set
$$
F_0(c)=H_0'(c)+\frac{66}{125}H_0(c)^2+\frac65H_0(c)+\frac53.
$$
The constants were chosen so that
$$
F_0(1)=0,
$$
$$
F_0'(1)=H_0''(1)+\frac65H_0'(1)=2-2=0,
$$
and
$$
F_0''(1)=H_0'''(1)
+2\frac{66}{125}H_0'(1)^2+\frac65H_0''(1)=0.
$$
The next derivative does not vanish:
$$
F_0'''(1)=H_0''''(1)
+6\frac{66}{125}H_0'(1)H_0''(1)
+\frac65H_0'''(1)=\frac{176}{25}.
$$
Therefore
$$
F_0(1+d)=\frac{88}{75}d^3+O(d^4).
$$
Thus both ordinary linearization and a quadratic branch-splitting shortcut are structurally unavailable.

Step 4: Compute the finite-size forcing at the cusp
Let
$$
Z(c)=\sum_{q=1}^3e^{q-1-qc},\qquad
\pi_1(c)=\frac{e^{-c}}{Z(c)}.
$$
The $q=1$ beta correction is the only base-column correction of order $1/n$:
$$
\log\rho_n(c/L)
=\text{const}-3c-\log Z(c)
+\frac{\pi_1(c)}{2n}\left(\frac cL+\frac{c^2}{L^2}\right)
+o\!\left(\frac1{nL}\right),
$$
uniformly after two $c$-derivatives. At $c=1$,
$$
\pi_1=\frac13,\qquad \pi_1'=\frac13,\qquad \pi_1''=\frac19.
$$
Hence its contributions to the first two log derivatives are
$$
\delta H_\rho(1)=\frac1{3nL}+\frac1{2nL^2}+o\!\left(\frac1{nL^2}\right),
$$
$$
\delta K_\rho(1)=\frac7{18nL}+\frac{19}{18nL^2}
+o\!\left(\frac1{nL^2}\right).
$$

For the signed stencil, with $\mu_k=\sum_jb_js_j^k$ and
$s_j=\sum_{k=1}^{m_j}(N+k)^{-1}$, the coefficient choice gives
$$
\frac{\mu_2}{\mu_1}=\frac{2}{3n}+O(n^{-3/2}),\qquad
\frac{\mu_3}{\mu_1}=-\frac{3}{2n}+O(n^{-3/2}).
$$
Therefore
$$
\log h_n(c/L)=\text{const}+\log c
-\frac{c}{3nL}-\frac{c^2}{4nL^2}
+O\!\left(\frac1{n^{3/2}L}\right),
$$
so
$$
\delta H_h(1)=-\frac1{3nL}-\frac1{2nL^2}
+O\!\left(\frac1{n^{3/2}L}\right),
$$
$$
\delta K_h(1)=-\frac1{2nL^2}
+O\!\left(\frac1{n^{3/2}L}\right).
$$
The order-$1/n$ terms in $H_n(1)$ cancel, but they do not cancel after one more scale derivative. Consequently
$$
H_n(1/L)=O\!\left(\frac1{n^{3/2}L}\right),
$$
$$
K_n(1/L)=-\frac53+\frac7{18nL}
+O\!\left(\frac1{nL^2}+\frac1{n^{3/2}L}\right),
$$
and hence
$$
F_n(1)=\frac7{18nL}+o\!\left(\frac1{nL}\right).
$$

Step 5: Extract the cubic cusp displacement
The same uniform beta and shift expansions give $F_n\to F_0$ with the required derivatives near $1$. Since the limiting zero is cubic and
$F_n(1)=O((nL)^{-1})$, the selected nearby root satisfies
$$
d_n:=c_n-1=O((nL)^{-1/3}).
$$
Expanding at $c=1$ on this scale,
$$
0=F_n(1+d_n)
=\frac{88}{75}d_n^3+\frac7{18nL}
+o\!\left(\frac1{nL}\right).
$$
Thus
$$
(nL)d_n^3\longrightarrow
-\frac7{18}\frac{75}{88}=-\frac{175}{528}.
$$
The real cubic branch is unique near $1$, so
$$
(nL)^{1/3}(a_nL-1)
\longrightarrow-\sqrt[3]{\frac{175}{528}}.
$$

Final Answer: $\boxed{-\sqrt[3]{\frac{175}{528}}}$

---

## Answer

$-\sqrt[3]{\frac{175}{528}}$

---

## Classification

**Problem Type:** Parameter identification

**Answer Type:** Exact scalar

---

## Solution Concepts

- determinant-ratio log derivatives
- signed mesoscopic stencil
- cubic limiting degeneracy
- beta-function finite-size bias
- cusp root scaling

---

## Black-Box Audit — no issues found

The hardening retains the same signed-stencil construction and attacks the previous stationary-ratio shortcut directly. The tuned invariant has a cubic limiting zero, while the surviving $1/(n\log n)$ forcing is derived from the mismatch between the first and second scale derivatives of the two previously cancelling finite-size corrections.

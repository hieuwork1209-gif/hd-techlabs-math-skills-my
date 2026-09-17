## Steps

Step 1: Character decomposition modulo $8$

Let
$$
\mathcal X=\{1,\chi_{-4},\chi_8,\chi_{-8}\},
$$
where the three nontrivial real primitive characters are taken modulo $8$ and
$$
\chi_{-8}=\chi_{-4}\chi_8.
$$
For the odd residue classes $r\in\{1,3,5,7\}$ their values are
$$
\begin{array}{c|rrrr}
r&1&3&5&7\\ \hline
1&1&1&1&1\\
\chi_{-4}&1&-1&1&-1\\
\chi_8&1&-1&-1&1\\
\chi_{-8}&1&1&-1&-1
\end{array}
\tag{1}
$$

Define
$$
m(1)=1,\qquad m(3)=3,\qquad m(5)=5,\qquad m(7)=7.
\tag{2}
$$
Let $a(n)$ be the indicator of the odd integers satisfying
$$
v_p(n)\equiv0\pmod3\quad(p\equiv3\!\!\pmod8),
$$
$$
v_p(n)\equiv0\pmod5\quad(p\equiv5\!\!\pmod8),
$$
$$
v_p(n)\equiv0\pmod7\quad(p\equiv7\!\!\pmod8).
$$
For each $\psi\in\mathcal X$, put
$$
F_\psi(s)=\sum_{n\ge1}\frac{a(n)\psi(n)}{n^s}.
$$
Since all $m(r)$ are odd,
$$
F_\psi(s)
=
\prod_{p\equiv1(8)}(1-p^{-s})^{-1}
\prod_{r\in\{3,5,7\}}
\prod_{p\equiv r(8)}
\bigl(1-\psi(r)p^{-m(r)s}\bigr)^{-1}.
\tag{3}
$$

If
$$
N_r(x)=\#\{n\le x:a(n)=1,\ n\equiv r\pmod8\},
$$
then character orthogonality gives
$$
N_r(x)=\frac14\sum_{\psi\in\mathcal X}\psi(r)
\sum_{n\le x}a(n)\psi(n).
\tag{4}
$$

Step 2: Extract the common $\zeta(s)^{1/4}$ singularity

For every odd prime $p$,
$$
\frac14\sum_{\xi\in\mathcal X}\xi(p)
=
\begin{cases}
1,&p\equiv1\pmod8,\\
0,&p\equiv3,5,7\pmod8.
\end{cases}
\tag{5}
$$
Hence
$$
B(s):=
\bigl(\zeta(s)L(s,\chi_{-4})L(s,\chi_8)L(s,\chi_{-8})\bigr)^{1/4}
\tag{6}
$$
has exactly the same first-order prime contribution as $F_\psi(s)$.

Define
$$
E_\psi(s)
=(1-2^{-s})^{1/4}
\prod_{p\ {m odd}}
\left[
\frac{
\prod_{\xi\in\mathcal X}(1-\xi(p)p^{-s})^{1/4}
}
{1-\psi(p)p^{-m(p)s}}
\right],
\tag{7}
$$
where $m(p)=m(r)$ for $p\equiv r\pmod8$. Then
$$
F_\psi(s)=B(s)E_\psi(s)
=\zeta(s)^{1/4}K_\psi(s),
\tag{8}
$$
with
$$
K_\psi(s)
=
\bigl(L(s,\chi_{-4})L(s,\chi_8)L(s,\chi_{-8})\bigr)^{1/4}
E_\psi(s).
\tag{9}
$$

The logarithm of the Euler product in (7) starts at $O(p^{-2\Re s})$, so $E_\psi$ converges absolutely and locally uniformly for $\Re s>1/2$. Since the three Dirichlet $L$-functions in (9) are nonzero at $s=1$, every $K_\psi$ is holomorphic and nonzero near $1$.

Step 3: Exact leading factors and logarithmic derivatives

Put
$$
Q_\psi:=E_\psi(1)
=2^{-1/4}
\prod_{p\ {m odd}}
\left[
\frac{
\prod_{\xi\in\mathcal X}(1-\xi(p)/p)^{1/4}
}
{1-\psi(p)/p^{m(p)}}
\right].
\tag{10}
$$
Also define the common positive factor
$$
\mathcal A
=
\frac{
\bigl(
L(1,\chi_{-4})L(1,\chi_8)L(1,\chi_{-8})
\bigr)^{1/4}
}{\Gamma(1/4)}.
\tag{11}
$$
Then
$$
\frac{K_\psi(1)}{\Gamma(1/4)}=\mathcal A Q_\psi.
\tag{12}
$$

For the derivative, write
$$
e_\psi:=\frac{E_\psi'(1)}{E_\psi(1)}.
$$
Differentiating (7),
$$
\boxed{
\begin{aligned}
e_\psi={}&\frac{\log2}{4}
+\sum_{p\ {m odd}}
\Biggl[
-\frac{m(p)\psi(p)\log p}{p^{m(p)}-\psi(p)}\\
&\hspace{24mm}
+\frac14\sum_{\xi\in\mathcal X}
\frac{\xi(p)\log p}{p-\xi(p)}
\Biggr].
\end{aligned}
}
\tag{13}
$$
The $p\equiv1\pmod8$ summands vanish identically, and the remaining prime sum converges absolutely.

Thus
$$
\boxed{
\kappa_\psi
:=\frac{K_\psi'(1)}{K_\psi(1)}
=
\frac14\sum_{\xi\in\{\chi_{-4},\chi_8,\chi_{-8}\}}
\frac{L'}{L}(1,\xi)
+e_\psi.
}
\tag{14}
$$

Step 4: Two-term Selberg-Delange for exponent $1/4$

We use the following special case. If
$$
F(s)=\zeta(s)^\alpha K(s),
\qquad \alpha=\frac14,
$$
with $K$ holomorphic near $1$, then
$$
\sum_{n\le x}f(n)
=
\frac{K(1)}{\Gamma(1/4)}
\frac{x}{(\log x)^{3/4}}
\left(
1+\frac{d(K)}{\log x}
+O((\log x)^{-2})
\right),
\tag{15}
$$
where
$$
\boxed{
d(K)=\frac34\left(1-\frac\gamma4-\frac{K'(1)}{K(1)}\right).
}
\tag{16}
$$

Indeed, with $s=1+w$,
$$
\zeta(1+w)^{1/4}
=w^{-1/4}\left(1+\frac\gamma4w+O(w^2)\right),
$$
and the Perron factor contributes $(1-w+O(w^2))$. Hence the coefficient multiplying $w$ before the Hankel integral is
$$
\frac\gamma4+\frac{K'(1)}{K(1)}-1.
$$
The next Hankel term is multiplied by
$$
\frac{\Gamma(1/4)}{\Gamma(-3/4)}=-\frac34,
$$
which gives (16).

Define
$$
\boxed{
d_\psi
=\frac34\left(1-\frac\gamma4-\kappa_\psi\right).
}
\tag{17}
$$
Then (8), (12), and (15) give
$$
\sum_{n\le x}a(n)\psi(n)
=
\mathcal A Q_\psi
\frac{x}{(\log x)^{3/4}}
\left(
1+\frac{d_\psi}{\log x}
+O((\log x)^{-2})
\right).
\tag{18}
$$

Step 5: Recover the four residue classes

Insert (18) into (4). For each $r\in\{1,3,5,7\}$ define
$$
S_r:=\sum_{\psi\in\mathcal X}\psi(r)Q_\psi,
\qquad
T_r:=\sum_{\psi\in\mathcal X}\psi(r)Q_\psi d_\psi.
\tag{19}
$$
Then
$$
\boxed{
C_r=\frac{\mathcal A}{4}S_r,
\qquad
D_r=\frac{T_r}{S_r}.
}
\tag{20}
$$
Therefore
$$
\boxed{
N_r(x)
=C_r\frac{x}{(\log x)^{3/4}}
\left(
1+\frac{D_r}{\log x}
+O((\log x)^{-2})
\right).
}
\tag{21}
$$

The constants $C_r$ are positive. For example, for each $r$ one may fix one admissible integer $u_r\equiv r\pmod8$ (take $u_1=1$, $u_3=3^3$, $u_5=5^5$, $u_7=7^7$) and multiply it by arbitrary integers composed only of primes $\equiv1\pmod8$; this already produces a positive-order subfamily of size $\asymp x/(\log x)^{3/4}$.

Using the character table (1), the leading constants can be written explicitly as
$$
C_1=\frac{\mathcal A}{4}
(Q_1+Q_{-4}+Q_8+Q_{-8}),
$$
$$
C_3=\frac{\mathcal A}{4}
(Q_1-Q_{-4}-Q_8+Q_{-8}),
$$
$$
C_5=\frac{\mathcal A}{4}
(Q_1+Q_{-4}-Q_8-Q_{-8}),
$$
$$
C_7=\frac{\mathcal A}{4}
(Q_1-Q_{-4}+Q_8-Q_{-8}),
\tag{22}
$$
with the same Hadamard sign patterns for the numerators defining $D_r$ after replacing $Q_\psi$ by $Q_\psi d_\psi$.

Finally, every pairwise limiting bias is exact:
$$
\boxed{
\lim_{x\to\infty}\frac{N_r(x)}{N_t(x)}
=\frac{C_r}{C_t}
=\frac{S_r}{S_t}
\qquad(r,t\in\{1,3,5,7\}).
}
\tag{23}
$$

---

## Answer

$\left(C_1,C_3,C_5,C_7,D_1,D_3,D_5,D_7\right)$, where for $r\in\{1,3,5,7\}$
$$
C_r=\frac{\mathcal A}{4}\sum_{\psi\in\mathcal X}\psi(r)Q_\psi,
\qquad
D_r=\frac{\sum_{\psi\in\mathcal X}\psi(r)Q_\psi d_\psi}{\sum_{\psi\in\mathcal X}\psi(r)Q_\psi},
$$
$$
\mathcal A=
\frac{\bigl(L(1,\chi_{-4})L(1,\chi_8)L(1,\chi_{-8})\bigr)^{1/4}}{\Gamma(1/4)},
$$
$$
Q_\psi=2^{-1/4}\prod_{p\ {m odd}}
\frac{\prod_{\xi\in\mathcal X}(1-\xi(p)/p)^{1/4}}
{1-\psi(p)/p^{m(p)}},
$$
and
$$
d_\psi=\frac34\left(1-\frac\gamma4-\frac14\sum_{\xi\in\{\chi_{-4},\chi_8,\chi_{-8}\}}\frac{L'}L(1,\xi)-e_\psi\right),
$$
with $e_\psi$ given in (13). Moreover $\lim N_r(x)/N_t(x)=C_r/C_t$ for every pair $r,t$.

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- four-character Fourier decomposition modulo $8$
- Euler products with residue-dependent exponent constraints
- common quarter-power zeta singularity
- two-term Selberg-Delange expansion
- arithmetic bias across four residue classes

## Steps

Step 1: Parametrize the triples and isolate the scale variable

Let
$$
g=\gcd(a,c),\qquad a=gA,\qquad c=gC,
$$
with $\gcd(A,C)=1$. Since $ac=g^2AC$ is a perfect square and $A,C$ are coprime, both $A$ and $C$ are squares. Hence there are coprime positive integers $r<s$ such that
$$
a=gr^2,\qquad c=gs^2,
$$
and the arithmetic-progression condition gives
$$
b=\frac{g(r^2+s^2)}2.
$$

Because $\gcd(r,s)=1$, either $r,s$ are both odd or they have opposite parity. If they are both odd, then $r^2+s^2$ is even and every positive $g$ makes $b$ integral. If they have opposite parity, then $r^2+s^2$ is odd, so $g$ must be even.

Since $p$ is odd,
$$
p\nmid abc
\iff
p\nmid g,\quad p\nmid r,\quad p\nmid s,\quad p\nmid r^2+s^2.
$$
Define
$$
\eta(r,s)=
\begin{cases}
1,&r,s\text{ both odd},\\[2mm]
\dfrac12,&r,s\text{ of opposite parity}.
\end{cases}
$$
For fixed admissible $(r,s)$, the condition $c=gs^2\le X$ gives $g\le X/s^2$. Therefore
$$
\#\{g:\text{all conditions hold}\}
=
\left(1-\frac1p\right)\eta(r,s)\frac{X}{s^2}+O(1).
$$
Summing over $1\le r<s\le\sqrt X$ gives
$$
T_p(X)=\left(1-\frac1p\right)X\,S_p(\sqrt X)+O(X),
$$
where
$$
S_p(R)=
\sum_{\substack{1\le r<s\le R\\(r,s)=1\\p\nmid rs(r^2+s^2)}}
\frac{\eta(r,s)}{s^2}.
$$

Step 2: Compute the weighted density of admissible primitive pairs

Let $D_p$ be the density, among ordered integer pairs $(r,s)$, obtained from the local restrictions appearing in $S_p(R)$.

At the prime $2$, the primitive residue classes are $(1,1),(1,0),(0,1)$. Their weights are respectively $1,\frac12,\frac12$, so the weighted local factor is
$$
\frac14\cdot1+\frac14\cdot\frac12+\frac14\cdot\frac12=\frac12.
$$

For every prime $q\ne2,p$, the only restriction is that $q$ cannot divide both $r$ and $s$, giving the factor
$$
1-\frac1{q^2}.
$$

At $p$, we require $r,s\not\equiv0\pmod p$ and
$$
r^2+s^2\not\equiv0\pmod p.
$$
There are $(p-1)^2$ ordered pairs with $r,s\ne0$. For each nonzero $s$, the forbidden pairs correspond to solutions of
$$
(r/s)^2\equiv-1\pmod p.
$$
Thus the number $N_p$ of allowed ordered residue pairs is
$$
N_p=
\begin{cases}
(p-1)(p-3),&p\equiv1\pmod4,\\[2mm]
(p-1)^2,&p\equiv3\pmod4.
\end{cases}
$$
Indeed, when $p\equiv1\pmod4$, the congruence $x^2\equiv-1\pmod p$ has two roots, giving $2(p-1)$ forbidden pairs; when $p\equiv3\pmod4$, it has no roots.

Hence
$$
D_p=
\frac12\frac{N_p}{p^2}
\prod_{\substack{q\text{ prime}\\q\ne2,p}}
\left(1-\frac1{q^2}\right).
$$
Using the Euler product identity
$$
\prod_{q\text{ prime}}\left(1-\frac1{q^2}\right)=\frac6{\pi^2},
$$
we obtain
$$
\prod_{q\ne2,p}\left(1-\frac1{q^2}\right)
=
\frac{6/\pi^2}{(1-1/4)(1-1/p^2)}
=
\frac8{\pi^2(1-1/p^2)}.
$$
Therefore
$$
D_p=\frac{4N_p}{\pi^2(p^2-1)}
=
\begin{cases}
\dfrac{4(p-3)}{\pi^2(p+1)},&p\equiv1\pmod4,\\[3mm]
\dfrac{4(p-1)}{\pi^2(p+1)},&p\equiv3\pmod4.
\end{cases}
$$

Step 3: Derive the lattice density and convert it into the logarithmic asymptotic

Set
$$
A_p(R)=
\sum_{\substack{1\le r<s\le R\\(r,s)=1\\p\nmid rs(r^2+s^2)}}
\eta(r,s).
$$
We now derive its asymptotic rather than invoking a lattice-density theorem.

First ignore coprimality at odd primes. For $Y\ge1$, let
$$
B_p(Y)=
\sum_{\substack{1\le u,v\le Y\\
(u,v)\not\equiv(0,0)\pmod2\\
p\nmid uv(u^2+v^2)}}
\eta(u,v),
$$
where the three allowed parity classes $(1,1),(1,0),(0,1)$ have weights $1,\frac12,\frac12$. Their total weight modulo $2$ is therefore $2$, while modulo $p$ there are exactly $N_p$ admissible ordered classes. By the Chinese remainder theorem, modulo $2p$ the weighted total of admissible residue-pair classes is $2N_p$.

For each fixed residue pair modulo $2p$, the number of representatives in $[1,Y]^2$ is
$$
\left(\frac{Y}{2p}+O(1)\right)^2
=\frac{Y^2}{4p^2}+O_p(Y+1).
$$
Since $p$ is fixed, summing over the admissible classes gives
$$
B_p(Y)=\frac{N_p}{2p^2}Y^2+O_p(Y+1).
$$

Now impose $\gcd(r,s)=1$ by Möbius inversion. Every pair counted here is not both even and is prime to $p$ in each coordinate, so any common divisor $d$ that occurs is automatically coprime to $2p$. Conversely, for $(d,2p)=1$, writing $r=du$, $s=dv$ preserves both the parity class and the condition $p\nmid uv(u^2+v^2)$. Thus the weighted count in the full square is
$$
\begin{aligned}
C_p(R)
&:=\sum_{\substack{1\le r,s\le R\\(r,s)=1\\p\nmid rs(r^2+s^2)}}\eta(r,s)\\
&=\sum_{\substack{d\le R\\(d,2p)=1}}\mu(d)
B_p\!\left(\frac{R}{d}\right).
\end{aligned}
$$
Substituting the estimate for $B_p$ yields
$$
C_p(R)
=\frac{N_p}{2p^2}R^2
\sum_{\substack{d\le R\\(d,2p)=1}}\frac{\mu(d)}{d^2}
+O_p\!\left(
R\sum_{d\le R}\frac1d+\sum_{d\le R}1
\right).
$$
The error is $O_p(R\log R)$. Also, absolute convergence gives
$$
\sum_{\substack{(d,2p)=1}}\frac{\mu(d)}{d^2}
=\prod_{q\ne2,p}\left(1-\frac1{q^2}\right),
$$
and the omitted tail is
$$
\sum_{d>R}\frac1{d^2}=O\!\left(\frac1R\right),
$$
which contributes only $O_p(R)$ after multiplication by $R^2$. Therefore
$$
C_p(R)
=\frac{N_p}{2p^2}
\prod_{q\ne2,p}\left(1-\frac1{q^2}\right)R^2
+O_p(R\log R)
=D_pR^2+O_p(R\log R).
$$

The summand and all local conditions are symmetric in $r,s$. In the full square, the only primitive diagonal pair is $(1,1)$, so its total contribution is $1$. Hence
$$
A_p(R)=\frac{C_p(R)-1}{2}
=\frac{D_p}{2}R^2+O_p(R\log R).
$$
Since $p$ is fixed, we may write the error simply as $O(R\log R)$.

Because $r<s$, the upper variable in $S_p(R)$ is exactly $s$, so partial summation gives
$$
S_p(R)
=
\frac{A_p(R)}{R^2}
+2\int_1^R\frac{A_p(t)}{t^3}\,dt.
$$
Substituting the estimate for $A_p(t)$ gives
$$
S_p(R)=D_p\log R+O(1).
$$
Therefore
$$
S_p(\sqrt X)=\frac{D_p}{2}\log X+O(1),
$$
and Step 1 becomes
$$
T_p(X)
=
\left(1-\frac1p\right)\frac{D_p}{2}X\log X+O(X).
$$
Hence
$$
C_p=\left(1-\frac1p\right)\frac{D_p}{2}.
$$

Step 4: Simplify the constant and give a compact self-contained answer

If $p\equiv1\pmod4$, then
$$
C_p=\frac{2(p-1)(p-3)}{\pi^2p(p+1)}.
$$
If $p\equiv3\pmod4$, then
$$
C_p=\frac{2(p-1)^2}{\pi^2p(p+1)}.
$$
Because $(-1)^{(p-1)/2}=1$ in the first case and $-1$ in the second, these combine into
$$
C_p=\frac{2(p-1)(p-2-(-1)^{(p-1)/2})}{\pi^2p(p+1)}.
$$
Final Answer: $\boxed{\frac{2(p-1)(p-2-(-1)^{(p-1)/2})}{\pi^2p(p+1)}}$

---

## Answer

$\frac{2(p-1)(p-2-(-1)^{(p-1)/2})}{\pi^2p(p+1)}$

---

## Classification

Problem Type: Symbolic derivation

Answer Type: Exact symbolic expression

---

## Solution Concepts

- square-product parametrization
- parity restrictions in arithmetic progressions
- local congruence densities
- Euler products and Mobius inversion
- partial summation

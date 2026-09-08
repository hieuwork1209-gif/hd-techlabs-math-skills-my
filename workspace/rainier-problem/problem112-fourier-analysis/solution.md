## Steps

Step 1: Establish the cubic scaling recurrence

For an auxiliary exponent $m\ge3$, write
$$
e_m(u)=\exp(2\pi i u/2^m),\qquad
S_m(r)=\sum_{x\bmod2^m}e_m(x^3-rx).
$$
The sum is real, because complex conjugation followed by $x\mapsto-x$ leaves it unchanged.

Pair $x$ with $x+2^{m-1}$. Since
$$
(x+2^{m-1})^3-r(x+2^{m-1})-(x^3-rx)
\equiv2^{m-1}(3x^2-r)\pmod{2^m},
$$
the paired summands differ by $(-1)^{x-r}$. Thus only $x$ having the same parity as $r$ survive.

If $r=4s$, only even $x=2y$ contribute, and
$$
S_m(4s)=2\sum_{y\bmod2^{m-2}}e_m\!\left(8(y^3-sy)\right).
$$
The summand now has period $2^{m-3}$ in $y$, so
$$
S_m(4s)=4S_{m-3}(s).
$$
If $r=2s$ with $s$ odd, the same reduction gives
$$
S_m(2s)=2\sum_{y\bmod2^{m-2}}e_{m-2}(2y^3-sy).
$$
Pairing $y$ with $y+2^{m-3}$ changes the phase by $(-1)^s=-1$, hence
$$
S_m(r)=0\qquad(r\equiv2\pmod4).
$$

Step 2: Count and sign the odd nonzero frequencies

Assume $m\ge6$ and $r$ is odd. Step 1 shows that only odd $x$ contribute. Translating those $x$ by $2^{m-3}$ multiplies every surviving summand by
$$
\exp\left(\frac{2\pi i}{8}(3x^2-r)\right)
=\exp\left(\frac{2\pi i}{8}(3-r)\right),
$$
because $x^2\equiv1\pmod8$. Therefore
$$
S_m(r)\ne0\Longrightarrow r\equiv3\pmod8.
$$

Conversely, let $r\equiv3\pmod8$. Then $3^{-1}r\equiv1\pmod8$, so it has an odd square root modulo $2^m$. Indeed, an odd root modulo $2^n$ lifts from $n$ to $n+1$ by replacing $u$ with $u+\varepsilon2^{n-1}$; exactly one choice of $\varepsilon\in\{0,1\}$ fixes the next binary digit. Choose odd $u$ with
$$
3u^2\equiv r\pmod{2^m}.
$$
The odd residues split into the two classes $x\equiv u$ and $x\equiv-u\pmod4$. For $x=u+4y$,
$$
x^3-3u^2x=-2u^3+16y^2(3u+4y),
$$
so this class contributes
$$
4e_m(-2u^3)J_{m-4}(3u),
$$
where
$$
J_n(a)=\sum_{y\bmod2^n}e_n(ay^2+4y^3).
$$
For odd $a$, put more generally
$$
J_n^{(c)}(a)=\sum_{y\bmod2^n}e_n(ay^2+2^cy^3),\qquad c\ge2.
$$
When $n\ge4$, the odd $y$ terms cancel under $y\mapsto y+2^{n-2}$, while the even terms give
$$
J_n^{(c)}(a)=2J_{n-2}^{(c+1)}(a).
$$
Iterating until the cubic coefficient is divisible by the remaining modulus gives
$$
J_n(a)=g_n(a),\qquad
g_n(a)=\sum_{y\bmod2^n}e_n(ay^2),
$$
for every $n\ge4$; for $n=2$ the equality is immediate. These are exactly the cases $n=m-4$ when $m$ is a multiple of $3$ and $m\ge6$.

Splitting the quadratic sum into even and odd residues gives $g_{n+2}(a)=2g_n(a)$, with
$$
g_2(a)=2(1+i^a),\qquad g_3(a)=4e^{2\pi ia/8}.
$$
Hence $g_n(a)$ is nonzero and its argument is always an odd multiple of $\pi/4$. The class $x\equiv-u\pmod4$ is the complex conjugate contribution, so
$$
S_m(r)=8\operatorname{Re}\!\left(e_m(-2u^3)g_{m-4}(3u)\right).
$$
This cannot vanish: if the displayed factor were purely imaginary, writing the Gauss-sum phase as $\ell\pi/4$ with $\ell$ odd would force
$$
-u^3+\ell2^{m-4}\equiv2^{m-3}\pmod{2^{m-2}},
$$
whose left side is odd and right side even. Therefore
$$
S_m(r)\ne0\iff r\equiv3\pmod8
$$
for odd $r$.

There are $2^{m-3}$ such odd residues. Replacing $r$ by $r+2^{m-1}$ multiplies every surviving odd-$x$ term by $-1$, so
$$
S_m(r+2^{m-1})=-S_m(r).
$$
Thus among odd $r$ there are exactly
$$
2^{m-4}
$$
positive values and the same number of negative values.

Step 3: Derive the recurrence for the sign counts

Now put $m=3q$. Let $P_q$ and $N_q$ denote the positive and negative counts for $S_{3q}(r)$.

For the base exponent $m=3$, even $x$ satisfy $x^3\equiv0\pmod8$ and odd $x$ satisfy $x^3\equiv x\pmod8$. Hence
$$
S_3(r)=
\sum_{y\bmod4}e_4(-ry)
+e_8(1-r)\sum_{y\bmod4}e_4((1-r)y).
$$
The first term is $4$ exactly when $r\equiv0\pmod4$, and the second is $4e_8(1-r)$ exactly when $r\equiv1\pmod4$. Therefore $S_3(r)$ is positive for $r=0,1,4$, negative for $r=5$, and zero otherwise. Thus
$$
P_1=3,\qquad N_1=1.
$$

For $q\ge2$, Step 2 contributes $2^{3q-4}$ positive and $2^{3q-4}$ negative odd frequencies. The class $r\equiv2\pmod4$ contributes only zeros. Finally, if $r=4s$, Step 1 gives $S_{3q}(4s)=4S_{3q-3}(s)$; as $r$ runs through multiples of $4$, each residue $s\bmod2^{3q-3}$ occurs twice. Consequently
$$
P_q=2^{3q-4}+2P_{q-1},\qquad
N_q=2^{3q-4}+2N_{q-1}.
$$

Step 4: Solve the recurrence

We prove by induction on $q$ that
$$
P_q=\frac{2^q}{6}\left(2^{2q-1}+7\right),\qquad
N_q=\frac{2^q}{6}\left(2^{2q-1}+1\right).
$$
For $q=1$ these give $(3,1)$, as established in Step 3. If the formulas hold for $q-1$, then
$$
2^{3q-4}+2P_{q-1}
=\frac{2^q}{6}\left(3\cdot2^{2q-3}+2^{2q-3}+7\right)
=\frac{2^q}{6}\left(2^{2q-1}+7\right),
$$
and the same calculation with $7$ replaced by $1$ gives the formula for $N_q$.

Final Answer: $\boxed{\frac{2^q}{6}\left(2^{2q-1}+7,\,2^{2q-1}+1\right)}$

---

## Answer

$\frac{2^q}{6}\left(2^{2q-1}+7,\,2^{2q-1}+1\right)$

---

## Classification

Problem Type: Exact computation

Answer Type: Tuple or ordered list

---

## Solution Concepts

- cubic exponential sum
- two-adic stationary phase
- quadratic Gauss sum
- cubic scaling recurrence

---

## Black-Box Audit

No issues found.

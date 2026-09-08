## Steps

Step 1: Evaluate the Eisenstein binary Gauss transform

Put
$$
m=2M+1,\qquad k=2K,\qquad n=m-k=2(M-K)+1,
$$
and write $e_j(u)=\exp(2\pi i u/2^j)$. For odd $a$ define
$$
g_j(a)=\sum_{x\bmod 2^j}e_j(ax^2).
$$
Splitting into even and odd residues gives $g_{j+2}(a)=2g_j(a)$, while
$$
g_2(a)=2(1+i^a),\qquad g_3(a)=4e^{2\pi ia/8}.
$$
Hence
$$
g_j(a)=
\begin{cases}
2^{j/2}(1+i^a),&j\text{ even},\\[1mm]
2^{(j+1)/2}e^{2\pi ia/8},&j\text{ odd}.
\end{cases}
$$
The same pairing shows that an odd linear coefficient makes the shifted sum vanish, while for even coefficient
$$
\sum_{x\bmod2^j}e_j(ax^2-2bx)=e_j(-a^{-1}b^2)g_j(a).
$$

Let
$$
E(x,y)=x^2-xy+y^2,\qquad B(r,s)=r^2+rs+s^2.
$$
The gradient matrix of $E$ is
$$
\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
$$
whose determinant is $3$. Thus for every $(r,s)$ there is a unique stationary point
$$
x_0=3^{-1}(2r+s),\qquad y_0=3^{-1}(r+2s)\pmod{2^m}.
$$
Shifting to this point gives
$$
\sum_{x,y\bmod2^m}e_m(E(x,y)-rx-sy)
=S_m\,e_m(-3^{-1}B(r,s)),
$$
where $S_m=\sum e_m(E(x,y))$. To evaluate $S_m$, sum first over $x$. Only even $y=2u$ contribute, and then
$$
S_m=g_m(1)\sum_{u\bmod2^{m-1}}e_m(3u^2)
=\frac12g_m(1)g_m(3).
$$
Since $m$ is odd, the formulas above give
$$
S_m=-2^m.
$$

Step 2: Determine the support and phase of the $z$-sum

For a frequency $t$, put
$$
Z(t)=\sum_{z\bmod2^m}e_m(3\cdot2^kz^2-tz).
$$
Translation by $2^{m-k}$ first forces $2^k\mid t$. After writing $t=2^ku$, the reduced odd-coefficient Gauss sum modulo $2^n$ vanishes unless $u$ is even. Hence
$$
Z(t)\ne0\iff t=2^{k+1}q,
$$
where $q$ runs modulo $2^{n-1}$. For such $t$,
$$
Z(t)=2^k g_n(3)e_n(-3^{-1}q^2).
$$
Because $n$ is odd,
$$
g_n(3)=2^{(n+1)/2}e^{3\pi i/4}.
$$
Combining with Step 1, every nonzero Fourier coefficient has the form
$$
A_{M,K}(r,s,t)=C\,e^{-\pi i/4}
 e_m\!\left(-3^{-1}\bigl(B(r,s)+2^kq^2\bigr)\right),
$$
with $C>0$. Therefore
$$
A_{M,K}(r,s,t)>0
\iff B(r,s)+2^kq^2\equiv5\cdot2^{m-3}\pmod{2^m},
$$
and
$$
A_{M,K}(r,s,t)<0
\iff B(r,s)+2^kq^2\equiv2^{m-3}\pmod{2^m}.
$$

Step 3: Remove the common $2^{2K}$ scale

For $c\in\{1,5\}$, let $R_c$ count the support triples satisfying
$$
B(r,s)+2^{2K}q^2\equiv c2^{m-3}\pmod{2^m}.
$$
The form $B$ is anisotropic modulo $2$: if $(u,v)$ is not $(0,0)$ modulo $2$, then $B(u,v)$ is odd. Consequently, for a nonzero pair,
$$
v_2(B(r,s))=2\min(v_2(r),v_2(s)).
$$
Since the other two terms in the congruence are divisible by $2^{2K}$, every solution has $2^K\mid r,s$. Write
$$
r=2^KR,\qquad s=2^KS.
$$
After division by $2^{2K}$ the modulus becomes $2^n$. The reduced congruence only depends on $R,S$ modulo $2^n$, while each reduced pair has $2^K$ lifts in each of $R,S$. Thus
$$
R_c=2^{2K}T_c(n),
$$
where $T_c(n)$ counts
$$
R,S\bmod2^n,\qquad q\bmod2^{n-1},
$$
satisfying
$$
B(R,S)+q^2\equiv c2^{n-3}\pmod{2^n}.
$$

Step 4: Count odd values of the Eisenstein norm

For every odd residue $u\bmod2^j$, let $F_j(u)$ be the number of pairs $(R,S)\bmod2^j$ with
$$
B(R,S)\equiv u\pmod{2^j}.
$$
Modulo $2$ there are exactly three solutions to $B(R,S)=1$, namely the three nonzero pairs. Suppose a primitive solution is fixed modulo $2^j$. Its four lifts have the form
$$
(R+\varepsilon2^j,S+\delta2^j),\qquad \varepsilon,\delta\in\{0,1\}.
$$
The next binary digit of $B$ changes by the nonzero linear form
$$
\varepsilon S+\delta R\pmod2,
$$
so exactly two of the four lifts hit any prescribed lift of the odd target. Therefore
$$
F_j(u)=3\cdot2^{j-1}
$$
for every odd $u$.

Step 5: Evaluate $T_1(n)$ and $T_5(n)$

Write
$$
L=\frac{n-3}{2}.
$$
First suppose $n\ge5$. If a solution has valuation below $2L$, then the valuations of $B(R,S)$ and $q^2$ must agree. Hence for some $0\le t<L$,
$$
\min(v_2(R),v_2(S))=v_2(q)=t.
$$
There are $2^{n-t-2}$ choices of $q$ with exact valuation $t$. After dividing by $2^{2t}$, the required value of the primitive norm is odd modulo $2^{n-2t}$. By Step 4 there are $3\cdot2^{n-2t-1}$ reduced norm pairs, and each has $2^{2t}$ lifts to $(R,S)\bmod2^n$. Thus each fixed $q$ contributes $3\cdot2^{n-1}$ pairs. The total contribution from all $t<L$, common to $c=1$ and $c=5$, is
$$
C_0=\sum_{t=0}^{L-1}3\cdot2^{n-1}2^{n-t-2}
=3\cdot2^{2n-2}-3\cdot2^{(3n-1)/2}.
$$

It remains to count the solutions with $R,S,q$ all divisible by $2^L$. After dividing by $2^{2L}$, only the residues modulo $8$ matter:
$$
B(a,b)+d^2\equiv c\pmod8.
$$
For $(a,b)\bmod8$, the residue counts of $B(a,b)$ are
$$
0:4,\qquad 1,3,4,5,7:12,
$$
and for $d\bmod8$ the square counts are
$$
0:2,\qquad1:4,\qquad4:2.
$$
Their convolution gives $64$ triples for $c=1$ and $96$ triples for $c=5$. Restoring the unused high bits contributes respectively
$$
2^{(3n+1)/2},\qquad 3\cdot2^{(3n-1)/2}.
$$
Therefore
$$
T_1(n)=3\cdot2^{2n-2}-2^{(3n-1)/2},
$$
$$
T_5(n)=3\cdot2^{2n-2}.
$$
For the remaining base case $n=3$, direct reduction modulo $8$ with $q\bmod4$ gives $T_1(3)=32$ and $T_5(3)=48$, which are the same formulas.

Step 6: Recover the positive and negative counts

By Step 2, positive coefficients correspond to $c=5$ and negative coefficients to $c=1$. Since $n=2(M-K)+1$,
$$
P_{M,K}=2^{2K}T_5(n)=3\cdot2^{4M-2K},
$$
while
$$
N_{M,K}=2^{2K}T_1(n)
=3\cdot2^{4M-2K}-2^{3M-K+1}.
$$

Final Answer: $\boxed{\left(3\cdot2^{4M-2K},\,3\cdot2^{4M-2K}-2^{3M-K+1}\right)}$

---

## Answer

$\left(3\cdot2^{4M-2K},\,3\cdot2^{4M-2K}-2^{3M-K+1}\right)$

---

## Classification

Problem Type: Exact computation

Answer Type: Tuple or ordered list

---

## Solution Concepts

- Eisenstein norm
- quadratic Gauss sum
- two-adic lifting
- valuation stratification
- local representation count

---

## Black-Box Audit

No issues found.

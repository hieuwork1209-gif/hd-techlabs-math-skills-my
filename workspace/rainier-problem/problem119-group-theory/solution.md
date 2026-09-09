## Steps

Step 1: Normalize the quartic Jacobi sum

Let
$$
p\equiv1\pmod4,
$$
let $g$ be a primitive root modulo $p$, and put
$$
r=g^{(p-1)/4}.
$$
Choose the quartic character
$$
\chi:\mathbb F_p^\times\to\{1,i,-1,-i\}
$$
by $\chi(g)=i$, and set
$$
\eta=\chi^2,\qquad s=\chi(-1)=(-1)^{(p-1)/4}.
$$
Write
$$
J=J(\chi,\chi)=\sum_{x\in\mathbb F_p}\chi(x)\chi(1-x)=A+iB.
$$
For a nontrivial character $\theta$, let
$$
G(\theta)=\sum_{x\in\mathbb F_p}\theta(x)e^{2\pi ix/p}.
$$
The identities
$$
G(\alpha)G(\beta)=J(\alpha,\beta)G(\alpha\beta),
\qquad |G(\theta)|^2=p
$$
for nontrivial $\alpha,\beta,\alpha\beta$ give
$$
J\overline J=p.
$$
Hence
$$
A^2+B^2=p.
$$

Put $\lambda=1+i$. Pair $x$ with $1-x$ in the sum defining $J$. The unique fixed point is $x=1/2$, and for every fourth root of unity $\zeta$,
$$
2\zeta\equiv2\pmod{\lambda^3}.
$$
Therefore
$$
J\equiv\chi(1/4)+(p-3)\pmod{\lambda^3}.
$$
Now
$$
\chi(1/4)=\chi(4)=\eta(2)=s,
$$
so
$$
J\equiv-s\pmod{\lambda^3}.
$$
Since $A^2+B^2=p$, $A$ is odd and $B$ is even; the congruence above gives
$$
A\equiv-1\pmod4.
$$
Thus, with
$$
p=a^2+b^2,\qquad a\equiv1\pmod4,
$$
we have
$$
A=-a.
$$

To determine the sign of $B$, reduce $\mathbb Z[i]$ modulo $p$ through the embedding
$$
i\longmapsto r.
$$
Because $\chi(g)=i$, the value $\chi(x)$ maps to $x^{(p-1)/4}$. With $m=(p-1)/4$,
$$
J\longmapsto\sum_{x\in\mathbb F_p}x^m(1-x)^m.
$$
After expanding $(1-x)^m$, every exponent lies strictly between $0$ and $p-1$, so every power sum vanishes. Hence the image of $J$ is $0$, and
$$
-a+Br\equiv0\pmod p.
$$
The normalization $br\equiv a\pmod p$ therefore forces
$$
B=b.
$$
Consequently
$$
J=-a+ib.
$$
Also the change of variables $x=t/(t-1)$ in Jacobi sums gives
$$
J(\chi,\eta)=sJ,
$$
and by conjugation
$$
J(\eta,\overline\chi)=s\overline J.
$$

Step 2: Obtain the six Frobenius factors by lifting Jacobi sums

For a diagonal Fermat curve
$$
X^4+Y^4=cZ^4
$$
over $\mathbb F_p$, character expansion over $\mathbb F_{p^k}$ uses the norm-lifted quartic character
$$
\chi_k=\chi\circ N_{\mathbb F_{p^k}/\mathbb F_p}.
$$
For $m+n\not\equiv0\pmod4$, the Davenport--Hasse lifting identity is
$$
J_{p^k}(\chi_k^m,\chi_k^n)
=(-1)^{k-1}J(\chi^m,\chi^n)^k.
$$
Moreover, for $c\in\mathbb F_p$,
$$
\chi_k(c)=\chi(c)^k.
$$
Thus the character expansion of the point count becomes
$$
\#C_c(\mathbb F_{p^k})
=p^k+1+(-1)^{k-1}
\sum_{\substack{1\le m,n\le3\\m+n\not\equiv0\ (4)}}
\left(\chi^{m+n}(c)J(\chi^m,\chi^n)\right)^k.
$$
Hence the six reciprocal Frobenius roots are
$$
\alpha_{m,n}=-\chi^{m+n}(c)J(\chi^m,\chi^n),
$$
and therefore
$$
L_c(T)=
\prod_{\substack{1\le m,n\le3\\m+n\not\equiv0\ (4)}}
\left(1+\chi^{m+n}(c)J(\chi^m,\chi^n)T\right).
$$

Step 3: Specialize the six factors to $c=g$

Because $\chi(g)=i$, the six admissible ordered pairs
$$
(1,1),(1,2),(2,1),(2,3),(3,2),(3,3)
$$
give
$$
-J,\quad -isJ,\quad -isJ,\quad is\overline J,\quad is\overline J,\quad -\overline J.
$$
Therefore
$$
L_{C_g}(T)
=(1-JT)(1-\overline JT)
(1-isJT)^2(1+is\overline JT)^2.
$$

Step 4: Pair conjugate factors

Since
$$
J=-a+ib,\qquad J\overline J=p,
$$
the first pair is
$$
(1-JT)(1-\overline JT)
=1-(J+\overline J)T+pT^2
=1+2aT+pT^2.
$$
For the second pair,
$$
(1-isJT)(1+is\overline JT)
=1+is(\overline J-J)T+pT^2.
$$
But
$$
\overline J-J=-2ib,
$$
so
$$
is(\overline J-J)=2sb.
$$
Hence
$$
L_{C_g}(T)
=(1+2aT+pT^2)(1+2sbT+pT^2)^2,
$$
where
$$
s=(-1)^{(p-1)/4}.
$$

Final Answer: $\boxed{(1+2aT+pT^2)(1+2(-1)^{(p-1)/4}bT+pT^2)^2}$

---

## Answer

$(1+2aT+pT^2)(1+2(-1)^{(p-1)/4}bT+pT^2)^2$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- zeta function of a Fermat curve
- quartic Jacobi sums
- Davenport--Hasse lifting
- Frobenius eigenvalues
- Gaussian prime normalization

---

## Black-Box Audit - no issues found
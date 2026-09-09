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
J=J(\chi,\chi)=\sum_{x\in\mathbb F_p}\chi(x)\chi(1-x).
$$
As in the quartic Jacobi-sum evaluation, Gauss sums give
$$
J\overline J=p.
$$
Writing $J=A+iB$, the primary congruence modulo $(1+i)^3$ gives
$$
A\equiv-1\pmod4.
$$
Under the reduction $i\mapsto r$, one has
$$
J\mapsto\sum_x x^{(p-1)/4}(1-x)^{(p-1)/4}=0,
$$
so
$$
A+Br\equiv0\pmod p.
$$
With the normalization
$$
p=a^2+b^2,\qquad a\equiv1\pmod4,\qquad br\equiv a\pmod p,
$$
we therefore get
$$
J=-a+ib.
$$
Also the Jacobi-sum change of variables gives
$$
J(\chi,\eta)=sJ,
$$
and by conjugation
$$
J(\eta,\overline\chi)=s\overline J.
$$

Step 2: State the Fermat-curve zeta factorization in the needed form

For a diagonal Fermat curve
$$
X^4+Y^4=cZ^4
$$
over $\mathbb F_p$, character expansion over every extension field together with the Davenport--Hasse lifting identity gives
$$
L_c(T)=
\prod_{\substack{1\le m,n\le3\\m+n\not\equiv0\ (4)}}
\left(1+\chi^{m+n}(c)J(\chi^m,\chi^n)T\right).
$$
Indeed, if the characters are lifted to $\mathbb F_{p^k}$ by the norm map, then for $m+n\not\equiv0\pmod4$,
$$
J_{p^k}(\chi^m\circ N,\chi^n\circ N)
=(-1)^{k-1}J(\chi^m,\chi^n)^k.
$$
Since $c\in\mathbb F_p$, the twist factor also lifts to its $k$th power. Hence
$$
\#C_c(\mathbb F_{p^k})
=p^k+1-\sum\alpha_{m,n}^k,
$$
with
$$
\alpha_{m,n}=-\chi^{m+n}(c)J(\chi^m,\chi^n),
$$
which is exactly the displayed product for the zeta numerator.

Step 3: Specialize the six Frobenius factors to $c=g$

Because $\chi(g)=i$, the six admissible ordered pairs
$$
(1,1),(1,2),(2,1),(2,3),(3,2),(3,3)
$$
give the six quantities
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
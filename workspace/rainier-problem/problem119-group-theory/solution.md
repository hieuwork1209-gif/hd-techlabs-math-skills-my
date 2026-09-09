## Steps

Step 1: Normalize the quartic Jacobi sum

Let
$$
p\equiv1\pmod4,
$$
let $g$ be a primitive root modulo $p$, and put
$$
r=g^{(p-1)/4},\qquad s=(-1)^{(p-1)/4}.
$$
Choose the quartic character
$$
\chi:\mathbb F_p^\times\to\{1,i,-1,-i\}
$$
by $\chi(g)=i$, and put $\eta=\chi^2$. Write
$$
J=J(\chi,\chi)=A+iB.
$$
For a nontrivial character $\theta$, let $G(\theta)$ be its Gauss sum. The identities
$$
G(\alpha)G(\beta)=J(\alpha,\beta)G(\alpha\beta),
\qquad |G(\theta)|^2=p
$$
show that
$$
J\overline J=p,
$$
so $A^2+B^2=p$.

Put $\lambda=1+i$. Pairing $x$ with $1-x$ in the Jacobi sum gives
$$
J\equiv\chi(1/4)+(p-3)\pmod{\lambda^3}.
$$
Since
$$
\chi(1/4)=\chi(4)=\eta(2)=s,
$$
we get
$$
J\equiv-s\pmod{\lambda^3}.
$$
Hence $A\equiv-1\pmod4$. With the normalization
$$
p=a^2+b^2,\qquad a\equiv1\pmod4,
$$
this forces $A=-a$.

To fix the sign of $B$, reduce $\mathbb Z[i]$ modulo $p$ through $i\mapsto r$. Since $\chi(g)=i$, the value $\chi(x)$ maps to $x^{(p-1)/4}$. Thus $J$ maps to
$$
\sum_{x\in\mathbb F_p}x^m(1-x)^m,
\qquad m=\frac{p-1}{4}.
$$
After expanding $(1-x)^m$, every occurring exponent is strictly between $0$ and $p-1$, so all power sums vanish. Therefore
$$
-a+Br\equiv0\pmod p.
$$
The condition $br\equiv a\pmod p$ gives $B=b$. Hence
$$
J=-a+ib.
$$

We shall also use the pairwise Jacobi sums
$$
J(\chi,\eta)=J(\eta,\chi)=sJ,
$$
$$
J(\eta,\overline\chi)=J(\overline\chi,\eta)=s\overline J,
$$
$$
J(\chi,\overline\chi)=J(\overline\chi,\chi)=-s,
\qquad J(\eta,\eta)=-1.
$$

Step 2: Describe the primitive Frobenius roots of the quartic surface

Let
$$
S_c:\ X_0^4+X_1^4+X_2^4=cX_3^4.
$$
For $k\ge1$, extend $\chi$ to $\mathbb F_{p^k}$ by the norm. Character expansion of the point count, together with Davenport--Hasse lifting, shows that the primitive middle-cohomology Frobenius roots are indexed by
$$
\mathcal A=\{(u_0,u_1,u_2,u_3)\in\{1,2,3\}^4:
 u_0+u_1+u_2+u_3\equiv0\pmod4\}
$$
and are
$$
\alpha_{\mathbf u}
=\chi^{-u_3}(c)J(\chi^{u_0},\chi^{u_1},\chi^{u_2}),
$$
where
$$
J(A,B,C)=\sum_{x+y+z=1}A(x)B(y)C(z).
$$
The hyperplane class contributes one additional Frobenius root $p$. Therefore
$$
P_{2,S_c}(T)
=(1-pT)\prod_{\mathbf u\in\mathcal A}(1-\alpha_{\mathbf u}T).
$$

For three characters whose product is nontrivial,
$$
J(A,B,C)=J(A,B)J(AB,C)
$$
whenever $AB$ is nontrivial. The only exceptional triple needed below is
$$
J(\eta,\eta,\eta)=p,
$$
because Gauss sums give
$$
J(\eta,\eta,\eta)=\frac{G(\eta)^3}{G(\eta)}=G(\eta)^2=p
$$
for $p\equiv1\pmod4$.

Step 3: Classify the twenty-one primitive roots for $c=g$

The set $\mathcal A$ has $21$ elements, belonging to exactly five pattern types:
$$
(1,1,1,1),\quad(3,3,3,3),\quad(2,2,2,2),
$$
plus the permutations of
$$
(1,1,3,3),\qquad(1,2,2,3).
$$
Using $\chi(g)=i$ and the Jacobi sums from Step 1 gives the following multiset of primitive Frobenius roots:
$$
-isJ^2\quad(1\text{ time}),
$$
$$
is\overline J^{\,2}\quad(1\text{ time}),
$$
$$
-p\quad(1\text{ time}),
$$
$$
-isp\quad(3\text{ times}),\qquad isp\quad(3\text{ times}),
$$
$$
-ip\quad(3\text{ times}),\qquad ip\quad(3\text{ times}),
$$
$$
-sp\quad(6\text{ times}).
$$
Indeed, the two constant patterns $(1,1,1,1)$ and $(3,3,3,3)$ give the two $J^2$-terms; $(2,2,2,2)$ gives $-p$; the six permutations of $(1,1,3,3)$ split according to whether the distinguished fourth coordinate is $1$ or $3$; and the twelve permutations of $(1,2,2,3)$ split according to whether that coordinate is $1$, $3$, or $2$.

Step 4: Multiply the factors

The twelve roots $\pm ip$ and $\pm isp$ contribute
$$
(1+p^2T^2)^6.
$$
The six roots $-sp$ contribute
$$
(1+spT)^6,
$$
and the root $-p$ contributes $1+pT$.

For the two exceptional roots, since
$$
J=-a+ib,
$$
we have
$$
is(\overline J^{\,2}-J^2)=-4sab,
\qquad J^2\overline J^{\,2}=p^2.
$$
Hence their quadratic factor is
$$
1+4sabT+p^2T^2.
$$
Including the hyperplane factor $1-pT$ gives
$$
P_{2,S_g}(T)
=(1-pT)(1+pT)(1+spT)^6(1+p^2T^2)^6(1+4sabT+p^2T^2).
$$
Thus
$$
P_{2,S_g}(T)
=(1-p^2T^2)(1+spT)^6(1+p^2T^2)^6(1+4sabT+p^2T^2).
$$
The degree is
$$
2+6+12+2=22,
$$
as required for a smooth quartic K3 surface.

Final Answer: $\boxed{(1-p^2T^2)(1+spT)^6(1+p^2T^2)^6(1+4sabT+p^2T^2)}$

---

## Answer

$(1-p^2T^2)(1+spT)^6(1+p^2T^2)^6(1+4sabT+p^2T^2)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- quartic K3 surface
- quartic Jacobi sums
- Davenport--Hasse lifting
- Frobenius eigenvalues
- Gaussian prime normalization

---

## Black-Box Audit - no issues found
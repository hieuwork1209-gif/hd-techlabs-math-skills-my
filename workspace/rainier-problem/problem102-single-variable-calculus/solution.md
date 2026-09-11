## Steps

Step 1: Convert the sum into a genus-three point count

For every integer $n\ge1$, put
$$
K_n=\sum_{x\in\mathbb F_{2^n}}(-1)^{\operatorname{Tr}_{\mathbb F_{2^n}/\mathbb F_2}(x^7+x^3)}.
$$
Consider the Artin-Schreier curve over $\mathbb F_2$
$$
C:\quad y^2+y=x^7+x^3.
$$
The right side has odd degree $7$. Hence the smooth projective model has one point at infinity and genus
$$
g=\frac{7-1}{2}=3.
$$
Indeed, the degree-two Artin-Schreier map $C\to\mathbb P^1$ is ramified only at infinity, where the pole order is $7$ and the different exponent is $8$; Riemann-Hurwitz gives
$$
2g-2=2(-2)+8=4.
$$

For $a\in\mathbb F_{2^n}$, the equation
$$
y^2+y=a
$$
has two solutions when $\operatorname{Tr}(a)=0$ and no solutions when $\operatorname{Tr}(a)=1$. Therefore each $x$ contributes
$$
1+(-1)^{\operatorname{Tr}(x^7+x^3)}
$$
affine points. Including the unique point at infinity,
$$
\#C(\mathbb F_{2^n})=2^n+1+K_n.
$$

Step 2: Determine the first three Frobenius power sums

For $n=1$, both elements of $\mathbb F_2$ satisfy $x^7+x^3=0$, so
$$
K_1=2.
$$

For $n=2$, let $\mathbb F_4=\{0,1,\omega,\omega^2\}$ with $\omega^2+\omega+1=0$. On $\mathbb F_4^\times$, $x^3=1$ and $x^7=x$. Thus $x=0,1$ contribute $+1$, while for $x=\omega,\omega^2$ the value $x+1$ has absolute trace $1$. Hence
$$
K_2=0.
$$

For $n=3$, every nonzero $x\in\mathbb F_8$ satisfies $x^7=1$, and $x\mapsto x^3$ permutes $\mathbb F_8^\times$. Since $\operatorname{Tr}_{\mathbb F_8/\mathbb F_2}(1)=1$ and the nontrivial additive character has total sum $0$,
$$
\sum_{x\ne0}(-1)^{\operatorname{Tr}(1+x^3)}
=-\sum_{u\ne0}(-1)^{\operatorname{Tr}(u)}=1.
$$
The term $x=0$ contributes $1$, so
$$
K_3=2.
$$

Let $\alpha_1,\ldots,\alpha_6$ be the Frobenius eigenvalues of $C$. The genus-three point-count formula is
$$
\#C(\mathbb F_{2^n})=2^n+1-p_n,
\qquad
p_n=\sum_{j=1}^6\alpha_j^n.
$$
Thus
$$
p_1=-2,\qquad p_2=0,\qquad p_3=-2.
$$

Step 3: Recover the Weil polynomial

For a genus-three curve over $\mathbb F_2$, Frobenius duality gives a characteristic polynomial of the form
$$
P(T)=T^6+c_1T^5+c_2T^4+c_3T^3+2c_2T^2+4c_1T+8.
$$
Newton's identities give
$$
p_1+c_1=0,
$$
$$
p_2+c_1p_1+2c_2=0,
$$
and
$$
p_3+c_1p_2+c_2p_1+3c_3=0.
$$
Substituting $p_1=-2$, $p_2=0$, $p_3=-2$ yields
$$
c_1=c_2=c_3=2.
$$
Therefore
$$
P(T)=T^6+2T^5+2T^4+2T^3+4T^2+8T+8.
$$

Step 4: Iterate the Frobenius recurrence to $n=17$

For $n\ge7$, the roots of $P$ give
$$
p_n+2p_{n-1}+2p_{n-2}+2p_{n-3}+4p_{n-4}+8p_{n-5}+8p_{n-6}=0.
$$
Newton's identities first give
$$
p_4=-8,\qquad p_5=-12,\qquad p_6=12.
$$
Iterating the recurrence gives
$$
\begin{aligned}
p_7&=40,&p_8&=-32,&p_9&=88,&p_{10}&=-80,\\
p_{11}&=-112,&p_{12}&=-80,&p_{13}&=128,&p_{14}&=0,\\
p_{15}&=288,&p_{16}&=1024,&p_{17}&=-1600.
\end{aligned}
$$
Since $K_n=-p_n$ by Step 1,
$$
K_{17}=1600.
$$

Final Answer: $\boxed{K=1600}$

---

## Answer

$K=1600$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- Artin-Schreier character sums
- genus-three point counting
- Frobenius Weil polynomial
- Newton identities and recurrence

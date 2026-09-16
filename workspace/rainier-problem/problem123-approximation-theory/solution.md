## Steps

Step 1: Turn four alternating contacts into a global minimax certificate
Let
$$
\mathcal P=\{x^4+x^3+ax^2+bx+c:a,b,c\in\mathbb R\}.
$$
If two polynomials belong to $\mathcal P$, their difference has degree at most $2$. Therefore, suppose one candidate $p_*$ has four ordered points
$$
-1<u<v<1
$$
with
$$
p_*(-1)=-E,\qquad p_*(u)=E,\qquad p_*(v)=-E,\qquad p_*(1)=E,
$$
and $\|p_*\|_{\infty}=E>0$. If some $q\in\mathcal P$ had $\|q\|_{\infty}<E$, then $h=q-p_*$ would have signs $+,-,+,-$ at $-1,u,v,1$. The intermediate value theorem would force at least three distinct zeros of $h$, impossible for a nonzero polynomial of degree at most $2$. Thus constructing such a candidate proves global optimality.

Step 2: Derive the two interior contacts from the critical-point equations
For a candidate with the alternating pattern from Step 1, the two interior contacts are critical points. Write the third root of the derivative as $w$. Since
$$
p'(x)=4x^3+3x^2+2ax+b=4(x-u)(x-v)(x-w),
$$
comparison of the $x^2$ coefficient gives
$$
u+v+w=-\frac34.
$$
The equalities $p(u)=p(1)$ and $p(v)=p(-1)$ are equivalent to
$$
\int_u^1p'(x)\,dx=0,\qquad \int_{-1}^vp'(x)\,dx=0.
$$
Substituting $w=-3/4-u-v$ and expanding reduces these two equations to
$$
2u^2-4uv+5u-4v^2-3v+4=0,
$$
$$
4u^2+4uv+3u-2v^2+3v=0.
$$
Subtracting twice the second equation from the first gives
$$
v=-\frac{6u^2+u-4}{3(4u+3)}.
$$
Substitution back into the second equation gives
$$
\frac{4F(u)}{9(4u+3)^2}=0,
$$
where
$$
F(u)=54u^4+198u^3+256u^2+130u+19.
$$

Step 3: Select the feasible branch and build the extremal polynomial
The endpoint values
$$
F\left(-\frac6{25}\right)=-\frac{4841}{390625}<0,
$$
$$
F\left(-\frac{119}{500}\right)=\frac{2026045367}{31250000000}>0
$$
show that $F$ has a root in $(-6/25,-119/500)$. On this interval, $F''(u)=4(162u^2+297u+128)>0$ and
$$
F'\left(-\frac6{25}\right)=\frac{599194}{15625}>0,
$$
so this root is unique; call it $u$. For
$$
v=-\frac{6u^2+u-4}{3(4u+3)},
$$
one has $3/5<v<2/3$, while
$$
w=-\frac34-u-v<-\frac{111}{100}<-1.
$$
Define
$$
a=2(uv+uw+vw),\qquad b=-4uvw,\qquad c=-1-a,
$$
and
$$
p_*(x)=x^4+x^3+ax^2+bx+c,\qquad E=1+b.
$$
Then $p_*'(x)=4(x-u)(x-v)(x-w)$ and
$$
p_*(-1)=-E,\qquad p_*(1)=E.
$$
The two integral equations from Step 2 give $p_*(u)=E$ and $p_*(v)=-E$. Since $w<-1$, the derivative is positive on $(-1,u)$, negative on $(u,v)$, and positive on $(v,1)$, hence $\|p_*\|_{\infty}=E$. Moreover,
$$
E-(u+1)^2(2u+1)=-\frac{8uF(u)}{9(4u+3)^2}=0,
$$
so
$$
E=(u+1)^2(2u+1)
$$
and in particular $3/10<E<31/100$. Step 1 now proves that this $E$ is the required minimum.

Step 4: Eliminate the critical point and obtain a polynomial for the minimum
Set
$$
G(u,T)=2u^3+5u^2+4u+1-T.
$$
The equations $F(u)=0$ and $G(u,E)=0$ hold simultaneously. A subresultant Euclidean elimination in $u$ gives the successive nonconstant remainders
$$
2\left(54Tu+63T-19u^2-46u-25\right),
$$
$$
2\left(2916T^2u+3402T^2-1206Tu-1436T+178u+143\right),
$$
and the final constant remainder
$$
2\left(78732T^4-32076T^3+7724T^2-1476T-27\right).
$$
Therefore
$$
P(E)=0,
$$
where
$$
P(T)=78732T^4-32076T^3+7724T^2-1476T-27.
$$
The coefficients have gcd $1$, so $P$ is primitive.

Step 5: Prove that the quartic is irreducible
Modulo $5$, multiplication by the inverse of the leading coefficient reduces $P$ to
$$
g(T)=T^4+2T^3+2T^2+2T+4.
$$
Its values at $T=0,1,2,3,4$ are respectively $4,1,3,3,3$, so it has no linear factor over $\mathbb F_5$. If it factored into monic quadratics,
$$
g=(T^2+aT+b)(T^2+cT+d),
$$
then $bd=4$. Up to interchanging the factors, the possibilities are $(b,d)=(1,4),(2,2),(3,3)$. In the first case, $a+c=2$, $ac=2$, and $4a+c=2$, forcing $a=0$ and contradicting $ac=2$. In the second case, $a+c=2$ and $ac=3$, whose discriminant is $2$, a nonsquare in $\mathbb F_5$. In the third case, $a+c=2$ and $ac=1$, but then $ad+bc=3(a+c)=1\neq2$. Hence $g$, and therefore $P$, is irreducible over $\mathbb Q$.

Thus $P$ is the primitive irreducible polynomial with positive leading coefficient annihilating the minimum.

Final Answer: $\boxed{78732T^4-32076T^3+7724T^2-1476T-27}$

---

## Answer

$78732T^4-32076T^3+7724T^2-1476T-27$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Polynomial or rational function

---

## Solution Concepts

- minimax polynomial approximation
- equioscillation certificate
- critical-point factorization
- polynomial elimination
- finite-field irreducibility

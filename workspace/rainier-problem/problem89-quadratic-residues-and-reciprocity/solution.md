## Steps

Step 1: Pass to the order of discriminant $-80$
Let
$$
\mathcal O=\mathbb Z[2\sqrt{-5}]\subset\mathbb Q(\sqrt{-5}).
$$
Then
$$
N(x+2y\sqrt{-5})=x^2+20y^2,
$$
and the only units of $\mathcal O$ are $\pm1$. The primitive reduced positive definite binary quadratic forms of discriminant $-80$ are
$$
Q_0=[1,0,20],\qquad Q_1=[3,2,7],\qquad Q_2=[4,0,5],\qquad Q_3=[3,-2,7].
$$
Thus the proper ideal class group of $\mathcal O$ has four elements. The forms $Q_1$ and $Q_3$ are inverses, while Gauss composition gives
$$
Q_1^2\sim Q_2.
$$
Since $Q_2$ is nonprincipal and ambiguous, it has order $2$. Hence
$$
\operatorname{Pic}(\mathcal O)\cong C_4,
$$
with class orders
$$
\operatorname{ord}(Q_0)=1,\qquad
\operatorname{ord}(Q_2)=2,\qquad
\operatorname{ord}(Q_1)=\operatorname{ord}(Q_3)=4.
$$

Step 2: Identify the prime-ideal class in cases (A), (B), and (C)
Because $p\nmid10$ and $\left(\frac{-5}{p}\right)=1$, the prime $p$ splits in $\mathbb Q(\sqrt{-5})$, hence also into two invertible prime ideals of norm $p$ in the order $\mathcal O$.

In case (A), write $b=2c$. Then
$$
p=a^2+5b^2=a^2+20c^2,
$$
so $p$ is represented by the principal form $Q_0$. Therefore the prime-ideal class has order
$$
d=1.
$$

In case (B), $b$ is odd. Since $p\equiv1,9\pmod{20}$, in particular $p\equiv1\pmod4$. From
$$
p=a^2+5b^2
$$
and $b$ odd, it follows that $a$ is even; write $a=2c$. Then
$$
p=4c^2+5b^2,
$$
so $p$ is represented by $Q_2$, whose class has order
$$
d=2.
$$

In case (C), $p\equiv3,7\pmod{20}$. Primitive odd prime values represented by $Q_0=x^2+20y^2$ or $Q_2=4x^2+5y^2$ are congruent to $1$ or $9$ modulo $20$. Therefore a split prime in classes $3,7\pmod{20}$ must be represented by $Q_1$ or $Q_3$. Hence its prime-ideal class has order
$$
d=4.
$$

Step 3: Convert representations into a class-group congruence
Write
$$
p\mathcal O=\mathfrak p\overline{\mathfrak p},
$$
where both prime ideals have norm $p$, and let
$$
c=[\mathfrak p]\in\operatorname{Pic}(\mathcal O),
\qquad \operatorname{ord}(c)=d.
$$
Every invertible ideal of norm $p^m$ is uniquely
$$
\mathfrak p^j\overline{\mathfrak p}^{\,m-j},
\qquad 0\le j\le m.
$$
Since
$$
[\overline{\mathfrak p}]=c^{-1},
$$
its class is
$$
c^j(c^{-1})^{m-j}=c^{2j-m}.
$$
Thus it is principal exactly when
$$
d\mid(2j-m).
$$
Because $p$ is coprime to the conductor $2$, these ideals are invertible, and every principal ideal of norm $p^m$ has exactly two generators differing by the units $\pm1$. Therefore
$$
r_m(p)=2\#\{0\le j\le m:d\mid(2j-m)\}.
$$

Step 4: Sum the class condition by a roots-of-unity filter
Put $k=m-j$. Then the condition is
$$
j-k\equiv0\pmod d.
$$
Hence
$$
R_p(T)=2\sum_{\substack{j,k\ge0\\j\equiv k\ (\mathrm{mod}\ d)}}T^{j+k}.
$$
For a primitive $d$-th root filter,
$$
\mathbf 1_{j\equiv k\ (\mathrm{mod}\ d)}
=\frac1d\sum_{\zeta^d=1}\zeta^{j-k}.
$$
Therefore
$$
R_p(T)
=\frac2d\sum_{\zeta^d=1}
\left(\sum_{j\ge0}(\zeta T)^j\right)
\left(\sum_{k\ge0}(\zeta^{-1}T)^k\right)
=\frac2d\sum_{\zeta^d=1}
\frac1{(1-\zeta T)(1-\zeta^{-1}T)}.
$$

Step 5: Evaluate the three possible class orders
For case (A), $d=1$, so
$$
R_p(T)=\frac{2}{(1-T)^2}.
$$

For case (B), $d=2$, so
$$
R_p(T)
=\frac1{(1-T)^2}+\frac1{(1+T)^2}
=\frac{2(1+T^2)}{(1-T^2)^2}.
$$

For case (C), $d=4$. Using the fourth roots $1,-1,i,-i$,
$$
R_p(T)
=\frac12\left(
\frac1{(1-T)^2}+\frac1{(1+T)^2}+\frac{2}{1+T^2}
\right)
=\frac{2(1+T^2)(1+T^4)}{(1-T^4)^2}.
$$

Step 6: State the result in the requested cases
The three class orders are $1,2,4$ in cases (A), (B), and (C), respectively, so the three rational functions above give the required ordinary generating functions.

Final Answer: $\boxed{R_p(T)=\frac2{(1-T)^2}(A),\frac{2(1+T^2)}{(1-T^2)^2}(B),\frac{2(1+T^2)(1+T^4)}{(1-T^4)^2}(C)}$

---

## Answer

$R_p(T)=\frac2{(1-T)^2}(A),\frac{2(1+T^2)}{(1-T^2)^2}(B),\frac{2(1+T^2)(1+T^4)}{(1-T^4)^2}(C)$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Polynomial or rational function

---

## Solution Concepts

- quadratic reciprocity and split primes
- binary quadratic forms of discriminant $-80$
- cyclic ideal class group of order $4$
- Gauss composition
- roots-of-unity filters

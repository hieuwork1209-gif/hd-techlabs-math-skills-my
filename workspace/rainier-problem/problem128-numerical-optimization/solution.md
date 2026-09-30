## Steps

Step 1: Express the two-step expected energy as a generalized eigenvalue problem
Set
$$
G=rac{H}{2}=
egin{pmatrix}
1&rac{1}{2}&0\
rac{1}{2}&1&rac{1}{2}\
0&rac{1}{2}&1
end{pmatrix}.
$$
Since $H_{ii}=2$, an exact update in coordinate $i$ is
$$
T_i=I-e_i e_i^TG,
$$
and $f(x)=x^TGx$. The three update matrices are
$$
T_1=
egin{pmatrix}
0&-rac{1}{2}&0\
0&1&0\
0&0&1
end{pmatrix},
quad
T_2=
egin{pmatrix}
1&0&0\
-rac{1}{2}&0&-rac{1}{2}\
0&0&1
end{pmatrix},
quad
T_3=
egin{pmatrix}
1&0&0\
0&1&0\
0&-rac{1}{2}&0
end{pmatrix}.
$$
They satisfy
$$
T_i^2=T_i,
qquad
T_i^TG=GT_i.
$$
With
$$
p_1=p_3=a,
qquad
p_2=1-2a,
$$
two independent draws give
$$
mathbb E[f(x_2)]
=
x_0^TN(a)x_0,
$$
where
$$
N(a)=
sum_{i,j=1}^{3}p_ip_j(T_jT_i)^TG(T_jT_i).
$$
Substituting the displayed $T_i$ gives
$$
8N(a)=
egin{pmatrix}
6a^2-11a+6&a(2a+1)&(2-3a)(2a-1)\
a(2a+1)&a(14a+3)&a(2a+1)\
(2-3a)(2a-1)&a(2a+1)&6a^2-11a+6
end{pmatrix}.
$$
Therefore
$$
R_2(a)
=
max_{x
eq0}rac{x^TN(a)x}{x^TGx},
$$
the largest generalized eigenvalue of the symmetric pencil $(N(a),G)$.

Step 2: Use reflection symmetry to reduce the generalized spectrum
Both $G$ and $N(a)$ are invariant under exchanging coordinates $1$ and $3$. The antisymmetric line spanned by
$$
u=(1,0,-1)^T
$$
and the symmetric plane spanned by
$$
v=(1,0,1)^T,
qquad
w=(0,1,0)^T
$$
are therefore invariant for the generalized eigenproblem.

On the antisymmetric line,
$$
lambda_0(a)=rac{6a^2-9a+4}{4}.
$$
On the symmetric plane, the matrices in the basis $(v,w)$ are
$$
G_s=
egin{pmatrix}
2&1\
1&1
end{pmatrix},
qquad
N_s=
egin{pmatrix}
1-a&rac{a(2a+1)}{4}\
rac{a(2a+1)}{4}&rac{a(14a+3)}{8}
end{pmatrix}.
$$
Thus the two symmetric generalized eigenvalues are the roots of
$$
16lambda^2-(40a^2-12a+16)lambda
-4a^4-32a^3+21a^2+6a=0.
$$
Writing
$$
D(a)=116a^4+68a^3+5a^2-48a+16,
$$
the larger root is
$$
lambda_+(a)
=
rac{10a^2-3a+4+sqrt{D(a)}}{8}.
$$

Let $Q_a(lambda)$ denote the quadratic on the left side of the generalized characteristic equation. Direct substitution gives
$$
Q_a(lambda_0)
=
-a(2a-1)(14a^2+23a-18).
$$
For $0<a<rac{1}{2}$, the factor $14a^2+23a-18$ is negative because it is increasing and equals $-3$ at $a=rac{1}{2}$. Therefore $Q_a(lambda_0)<0$. Since $Q_a$ opens upward, $lambda_0$ lies between the two symmetric roots. It follows that
$$
R_2(a)=lambda_+(a).
$$

Step 3: Derive the polynomial condition for a stationary point
Differentiate the explicit expression for $lambda_+$. If
$$
C(a)=232a^3+102a^2+5a-24,
$$
then
$$
lambda_+'(a)
=
rac{C(a)+(20a-3)sqrt{D(a)}}{8sqrt{D(a)}}.
$$
A stationary point with $a>rac{3}{20}$ and $C(a)<0$ must satisfy
$$
(20a-3)^2D(a)=C(a)^2.
$$
Expanding the difference gives
$$
(20a-3)^2D(a)-C(a)^2=-4F(a),
$$
where
$$
F(a)=
1856a^6+8512a^5+4460a^4+2268a^3-4269a^2+528a+108.
$$
This polynomial is not introduced as a guess: it is the elimination condition obtained directly from the derivative equation.

Step 4: Isolate the unique minimizing root
The derivative
$$
C'(a)=696a^2+204a+5
$$
is positive for $a>0$. Since $C(0)<0$ and $C(rac{2}{5})>0$, there is a unique $gammain(0,rac{2}{5})$ with $C(gamma)=0$.

For $0<aleqrac{3}{20}$, both $C(a)$ and $20a-3$ are nonpositive, so $lambda_+'(a)<0$. For $ageqgamma$, both terms in the numerator of $lambda_+'(a)$ are nonnegative, with at least one positive, so $lambda_+'(a)>0$.

It remains to inspect $rac{3}{20}<a<gamma$. There
$$
20a-3>0,
qquad
-C(a)>0.
$$
Hence the sign of the numerator of $lambda_+'(a)$ is the sign of
$$
(20a-3)sqrt{D(a)}-(-C(a)),
$$
which is the sign of
$$
(20a-3)^2D(a)-C(a)^2=-4F(a).
$$

The coefficient signs of $F$ have exactly two changes, so Descartes' rule of signs gives at most two positive roots. Also,
$$
Fleft(rac{3}{10}ight)=rac{24831}{15625}>0,
qquad
Fleft(rac{1}{3}ight)=-rac{9985}{729}<0,
$$
and
$$
Fleft(rac{2}{5}ight)=-rac{152296}{15625}<0,
qquad
Fleft(rac{1}{2}ight)=162>0.
$$
Therefore $F$ has exactly two positive roots: one in
$$
left(rac{3}{10},rac{1}{3}ight)
$$
and one in
$$
left(rac{2}{5},rac{1}{2}ight).
$$
Because $gamma<rac{2}{5}$, only the first root can occur before $gamma$. Call it $a_*$. The sign relation above gives
$$
lambda_+'(a)<0quad(0<a<a_*),
qquad
lambda_+'(a)>0quad(a_*<a<	frac12).
$$
Thus $a_*$ is the unique global minimizer of $R_2$.

Step 5: State the minimizing sampling parameter in the requested exact form
By the definition of the root notation in the problem statement, the unique minimizer found in Step 4 is
$$
a_*=
operatorname{root}left(
1856x^6+8512x^5+4460x^4+2268x^3-4269x^2+528x+108;
rac{3}{10},rac{1}{3}
ight).
$$
This value determines the minimizing symmetric sampling law
$$
(p_1,p_2,p_3)=(a_*,1-2a_*,a_*).
$$
Final Answer: $oxed{operatorname{root}(1856x^6+8512x^5+4460x^4+2268x^3-4269x^2+528x+108;rac{3}{10},rac{1}{3})}$

---

## Answer

$operatorname{root}(1856x^6+8512x^5+4460x^4+2268x^3-4269x^2+528x+108;rac{3}{10},rac{1}{3})$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- randomized coordinate descent
- exact coordinate minimization
- generalized eigenvalues
- reflection symmetry
- algebraic root isolation

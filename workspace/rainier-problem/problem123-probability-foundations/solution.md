## Steps

Step 1: Reduce the conditional probability to a linear-fractional moment problem
By the Bernoulli de Finetti theorem, there is a random variable $\Theta\in[0,1]$ such that, conditional on $\Theta$, the variables $X_i$ are independent Bernoulli$(\Theta)$. The hypotheses become
$$
\mathbb E\Theta=\frac12,\qquad \mathbb E\Theta^2=\frac13,\qquad \mathbb E\Theta^3=\frac14.
$$
If
$$
w(x)=x^2(1-x)^4,
$$
then conditional independence gives
$$
\mathbb P(X_1+\cdots+X_6=2)=15\mathbb E w(\Theta),
$$
$$
\mathbb P(X_7=1,\ X_1+\cdots+X_6=2)=15\mathbb E[\Theta w(\Theta)].
$$
Hence the quantity to maximize is
$$
\frac{\mathbb E[\Theta w(\Theta)]}{\mathbb E w(\Theta)}.
$$
The denominator is positive for every admissible law: if it were zero, then $\Theta\in\{0,1\}$ almost surely, which would force $\mathbb E\Theta^2=\mathbb E\Theta$, contradicting $1/3\ne1/2$.

Step 2: Construct a feasible three-atom family from the moment constraints
Let $y\in(1/10,2/19)$ and set
$$
S=\frac{1+y}{2},\qquad P=\frac y6.
$$
Let $a<b$ be the roots of
$$
x^2-Sx+P=0.
$$
Its discriminant is
$$
S^2-4P=\frac{3y^2-2y+3}{12}>0.
$$
Moreover,
$$
P>0,\qquad \left(\frac13\right)^2-S\left(\frac13\right)+P=-\frac1{18},
$$
$$
\left(\frac12\right)^2-S\left(\frac12\right)+P=-\frac y{12},\qquad S<1,
$$
so
$$
0<a<\frac13<\frac12<b<1.
$$
Let $L$ be the moment functional on quadratic polynomials defined by
$$
L(1)=1,\qquad L(x)=\frac12,\qquad L(x^2)=\frac13.
$$
Applying $L$ to the Lagrange cardinal polynomials for the nodes $a,b,1$ gives the weights
$$
\omega_a=\frac{3b-1}{6(a-b)(a-1)},
$$
$$
\omega_b=\frac{3a-1}{6(b-a)(b-1)},
$$
$$
\omega_1=\frac{1-S}{5-4S}.
$$
The displayed location of $a,b$ shows that all three weights are positive; they sum to $1$ and match the first two moments by construction. On the support $\{a,b,1\}$,
$$
x^3=(S+1)x^2-(P+S)x+P.
$$
Taking expectations gives
$$
\mathbb E\Theta^3=\frac{S+1}{3}-\frac{P+S}{2}+P=\frac14.
$$
Thus these weights define an admissible mixing law $\mu_y$.

The same support relation gives a recurrence for its moments. Reducing $w(x)$ and $xw(x)$ by that recurrence yields
$$
D(y):=\mathbb E_{\mu_y}w(\Theta)=\frac{(3-y)(3y^2-2y+3)}{864},
$$
$$
N(y):=\mathbb E_{\mu_y}[\Theta w(\Theta)]
=-\frac{3y^4-10y^3+6y^2+6y-9}{1728}.
$$
Therefore the conditional probability for $\mu_y$ is
$$
R(y)=\frac{3y^4-10y^3+6y^2+6y-9}{2(y-3)(3y^2-2y+3)}.
$$

Step 3: Build the dual certificate and force the parameter equation
For a real number $T$, define
$$
h_T(x)=x^2(1-x)^4(x-T).
$$
If every admissible mixing law satisfies $\mathbb E h_T(\Theta)\leq0$, then every admissible conditional probability is at most $T$.

Seek a cubic majorant $q_T$ with slack
$$
d_T(x)=q_T(x)-h_T(x)
=(1-x)(x^2-Sx+P)^2(x^2+Ux+V).
$$
The $x^7$ terms cancel automatically. Requiring the coefficients of $x^6,x^5,x^4$ in $q_T=h_T+d_T$ to vanish gives
$$
-T-U+y-2=0,
$$
$$
48T+12Uy+24U-12V-3y^2-22y+57=0,
$$
$$
72T+3Uy^2+22Uy+15U-12Vy-24V-5y^2-12y+45=0.
$$
Solving this linear system gives, with
$$
\Delta_0=9y^2-22y+9,
$$
$$
T(y)=\frac{3(y-1)(2y^2-3y-1)}{\Delta_0},
$$
$$
U(y)=\frac{3y^3-25y^2+47y-21}{\Delta_0},
$$
$$
V(y)=\frac{(y-3)(9y^3-45y^2+79y-51)}{12\Delta_0}.
$$
A direct subtraction of the primal value from the dual contact value gives
$$
T(y)-R(y)=
\frac{F(y)}{2(y-3)(3y^2-2y+3)(9y^2-22y+9)},
$$
where
$$
F(y)=9y^6-66y^5+173y^4-324y^3+471y^2-306y+27.
$$
Now
$$
10^6F\left(\frac1{10}\right)=802649>0,
$$
$$
19^6F\left(\frac2{19}\right)=-16427869<0.
$$
Also, throughout this interval,
$$
F'(y)\leq54\left(\frac2{19}\right)^5+692\left(\frac2{19}\right)^3+942\left(\frac2{19}\right)-306<-200.
$$
Hence $F$ has a unique root $y_0$ in $(1/10,2/19)$. Set
$$
T_0=T(y_0).
$$
Then $T_0=R(y_0)$.

Step 4: Prove that the candidate is the global maximum
For $y=y_0$, the denominator $\Delta_0$ is positive. The discriminant of the last quadratic factor in the slack is
$$
U^2-4V=-\frac{2K(y)}{3(9y^2-22y+9)^2},
$$
where
$$
K(y)=27y^6-198y^5+435y^4-260y^3-69y^2-18y+27.
$$
For $0<y<2/19$,
$$
K(y)>27-198\left(\frac2{19}\right)^5-260\left(\frac2{19}\right)^3-69\left(\frac2{19}\right)^2-18\left(\frac2{19}\right)>24.
$$
Thus $x^2+Ux+V$ is positive for every real $x$, and therefore
$$
d_{T_0}(x)\geq0\qquad(0\leq x\leq1).
$$
Since $q_{T_0}$ has degree at most $3$, its expectation is the same for every admissible mixing law. Under $\mu_{y_0}$ the slack vanishes at the support points $a,b,1$, so
$$
\mathbb E_{\mu_{y_0}}q_{T_0}(\Theta)
=\mathbb E_{\mu_{y_0}}h_{T_0}(\Theta)
=N(y_0)-T_0D(y_0)=0.
$$
Hence every admissible law satisfies
$$
\mathbb E h_{T_0}(\Theta)\leq\mathbb E q_{T_0}(\Theta)=0.
$$
Because the denominator in Step 1 is always positive, every admissible conditional probability is at most $T_0$, while $\mu_{y_0}$ attains $T_0$. Thus $T_0$ is the required maximum.

Step 5: Eliminate the support parameter
The two equations satisfied by $y_0,T_0$ are
$$
F(y_0)=0
$$
and
$$
G(y_0,T_0)=0,
$$
where
$$
G(y,T)=(9y^2-22y+9)T-3(y-1)(2y^2-3y-1).
$$
Apply the Euclidean subresultant algorithm to $F$ and $G$ as polynomials in $y$. After removing nonzero scalar factors, the last degree-two remainder is
$$
\begin{aligned}
&y^2(2187T^4-6804T^3+5718T^2-10924T+3375)\\
&+y(-5346T^4+16830T^3-14818T^2+27482T-8964)\\
&+(2187T^4-7614T^3+8136T^2-12522T+4821),
\end{aligned}
$$
the next remainder is
$$
\begin{aligned}
&y(5472T^5-25371T^4+38060T^3-48096T^2+73296T-7533)\\
&-298080T^5+1030941T^4-1101996T^3+1791672T^2-1037160T+147987,
\end{aligned}
$$
and the final constant remainder is a nonzero scalar multiple of
$$
Q(T)=4608T^6-17280T^5+21755T^4-33196T^3+24320T^2-6960T+669.
$$
Therefore
$$
Q(T_0)=0.
$$

Step 6: Prove irreducibility and identify the requested polynomial
The coefficients of $Q$ have gcd $1$, so $Q$ is primitive. Modulo $5$, multiplication by the unit $2$ reduces $Q$ to
$$
g(T)=T^6+3T^3+3.
$$
Let $z$ be a root of
$$
z^2+3z+3=0
$$
over $\mathbb F_5$. Its discriminant is $2$, a nonsquare, so $z\in\mathbb F_{25}\setminus\mathbb F_5$. From $z^2=2z+2$,
$$
z^4=z+2,
$$
$$
z^8=z+1\ne1.
$$
Since $\mathbb F_{25}^{\times}$ has order $24$, an element is a cube exactly when its eighth power is $1$. Thus $z$ is not a cube in $\mathbb F_{25}$, so $X^3-z$ has no root there and is irreducible. If $\alpha$ is any root of $g$, then $z=\alpha^3$ has degree $2$ over $\mathbb F_5$ and $\alpha$ has degree $3$ over $\mathbb F_{25}$, hence degree $6$ over $\mathbb F_5$. Therefore $g$, and hence $Q$, is irreducible. Gauss's lemma now gives irreducibility over $\mathbb Q$.

Final Answer: $\boxed{4608T^6-17280T^5+21755T^4-33196T^3+24320T^2-6960T+669}$

---

## Answer

$4608T^6-17280T^5+21755T^4-33196T^3+24320T^2-6960T+669$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Polynomial or rational function

---

## Solution Concepts

- de Finetti theorem
- linear-fractional moment problems
- polynomial dual certificates
- subresultant elimination
- finite-field irreducibility

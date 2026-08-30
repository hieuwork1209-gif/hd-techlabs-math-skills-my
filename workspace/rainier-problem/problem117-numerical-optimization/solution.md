## Steps

Step 1: Reduce the transient objective to scalar prefix products
The Hessian is
$$
A=\operatorname{diag}(1,3,5,7),
$$
so every eigencoordinate with eigenvalue $\lambda\in\{1,3,5,7\}$ is multiplied successively by
$$
1-\alpha_0\lambda,\qquad
(1-\alpha_0\lambda)(1-\alpha_1\lambda),\qquad
\prod_{j=0}^2(1-\alpha_j\lambda).
$$
Consequently, if $R\le r$, then at the endpoint modes $\lambda=1,7$ we have
$$
\max\{|1-\alpha_0|,|1-7\alpha_0|\}\le \frac{14}{5}r,
$$
$$
\max\{|(1-\alpha_0)(1-\alpha_1)|,
|(1-7\alpha_0)(1-7\alpha_1)|\}\le \frac75r,
$$
and
$$
\max\left\{\prod_{j=0}^2|1-\alpha_j|,
\prod_{j=0}^2|1-7\alpha_j|\right\}\le r.
$$
We will prove that these endpoint conditions alone force $r\ge3/10$.

Step 2: Analyze the first two prefixes at the putative level $3/10$
Suppose $R\le3/10$ and put
$$
a=\alpha_0,\qquad b=\alpha_1,\qquad
A=(1-a)(1-b),\qquad B=|1-7a|\,|1-7b|.
$$
The one-step endpoint bound gives
$$
1-a\le\frac{21}{25},\qquad |1-7a|\le\frac{21}{25},
$$
so
$$
\frac4{25}\le a\le\frac{46}{175}.
$$
The two-step endpoint bound gives
$$
A\le\frac{21}{50},\qquad B\le\frac{21}{50}. \tag{1}
$$
From $A\le21/50$ and the displayed range of $a$ we get $b>1/7$. Also $a>1/7$, so in fact
$$
B=(7a-1)(7b-1).
$$
The first inequality in (1) is equivalent to
$$
b\ge b_A(a):=1-\frac{21}{50(1-a)},
$$
while the second is equivalent to
$$
b\le b_B(a):=\frac17\left(1+\frac{21}{50(7a-1)}\right).
$$
Feasibility therefore requires $b_A(a)\le b_B(a)$, which on the present interval yields
$$
\frac4{25}\le a\le a_*:=\frac{58}{175}-\frac{\sqrt{3306}}{350}<\frac{17}{100}. \tag{2}
$$
In particular $b$ lies between $b_A(a)$ and $\min\{1/2,b_B(a)\}$.

Step 3: Prove the endpoint certificate for the third step
Define
$$
F(a,b)=20AB-A-7B.
$$
We claim that every pair allowed by Step 2 satisfies
$$
F(a,b)\ge0, \tag{3}
$$
with equality only at
$$
(a,b)=\left(\frac4{25},\frac12\right).
$$
On the feasible strip from (2), direct differentiation gives
$$
\frac{\partial F}{\partial b}
=2\left(980a^2b-560a^2-1120ab+468a+140b-55\right)<0.
$$
Indeed this derivative decreases with $b$, and at $b=b_A(a)$ it equals
$$
\frac25(2100a^2-1202a+131)<0
$$
throughout $4/25\le a\le a_*$. Hence, for fixed $a$, $F$ is smallest at the largest admissible $b$.

If $4/25\le a\le146/875$, that largest value is $b=1/2$, and
$$
F\left(a,\frac12\right)=-(7a-2)(25a-4)\ge0,
$$
with equality only at $a=4/25$. If $146/875\le a\le a_*$, the largest admissible value is $b=b_B(a)$, so $B=21/50$ and
$$
F=\frac{37}{5}A-\frac{147}{50}.
$$
Substitution of $b=b_B(a)$ gives
$$
A-\frac{147}{370}
=-\frac{3(12950a^2-8927a+1122)}{6475(7a-1)}>0
$$
on this interval. This proves (3) and its equality statement.

We also need the location of the one-variable balance in the third step. Since $b\ge b_A(a)$,
$$
B\ge (7a-1)(7b_A(a)-1),
$$
and a simplification gives
$$
(7a-1)(7b_A(a)-1)-\frac3{10}
=\frac{21(2a-1)(25a-4)}{25(a-1)}\ge0.
$$
Thus $B\ge3/10$, while $A\le21/50$, so $A\le5B$.

Now fix any admissible third step $c=\alpha_2$. The minimum over $0<c\le1/2$ of
$$
\max\{A(1-c),B|1-7c|\}
$$
is therefore attained with $1/7\le c\le1/2$ when the two terms are equal. Solving
$$
A(1-c)=B(7c-1)
$$
gives
$$
c=\frac{A+B}{A+7B},\qquad
\min_c\max\{A(1-c),B|1-7c|\}
=\frac{6AB}{A+7B}.
$$
By (3),
$$
\frac{6AB}{A+7B}\ge\frac3{10}.
$$
Thus every schedule has $R\ge3/10$. Equality forces
$$
a=\frac4{25},\qquad b=\frac12,\qquad
A=\frac{21}{50},\qquad B=\frac3{10},
$$
and then the balancing formula forces
$$
c=\frac27.
$$

Step 4: Verify all four modes and attain the lower bound
Take
$$
\alpha_*=\left(\frac4{25},\frac12,\frac27\right).
$$
After one step the multipliers at $\lambda=1,3,5,7$ are
$$
\frac{21}{25},\quad\frac{13}{25},\quad\frac15,\quad-\frac3{25},
$$
so the weighted one-step contribution is
$$
\frac5{14}\cdot\frac{21}{25}=\frac3{10}.
$$
After two steps the multipliers are
$$
\frac{21}{50},\quad-\frac{13}{50},\quad-\frac3{10},\quad\frac3{10},
$$
so the weighted two-step contribution is
$$
\frac57\cdot\frac{21}{50}=\frac3{10}.
$$
After three steps they are
$$
\frac3{10},\quad-\frac{13}{350},\quad\frac9{70},\quad-\frac3{10},
$$
whose largest absolute value is $3/10$. Hence $R(\alpha_*)=3/10$. Together with Step 3, this proves both optimality and uniqueness of the ordered triple.
Final Answer: $\boxed{\left(\frac3{10},\left(\frac4{25},\frac12,\frac27\right)\right)}$

---

## Answer

$\left(\frac3{10},\left(\frac4{25},\frac12,\frac27\right)\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- periodic gradient descent
- transient growth control
- prefix convergence products
- endpoint minimax certificate
- constrained step-size optimization

---

## Black-Box Audit — no issues found

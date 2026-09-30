# Normalized Math Problem

## LaTeX (Normalized)

Let
$$
H=
egin{pmatrix}
2&1&0\
1&2&1\
0&1&2
end{pmatrix},
qquad
f(x)=rac{1}{2}x^THx.
$$
At each iteration, exact randomized coordinate descent independently selects $iin{1,2,3}$ with
$$
p_1=p_3=a,
qquad
p_2=1-2a,
qquad
0<a<rac{1}{2},
$$
and performs
$$
x^+=x-rac{e_i^THx}{H_{ii}}e_i,
$$
where $e_i$ is the $i$th standard basis vector.

After two independent coordinate draws, define the worst-case expected energy ratio
$$
R_2(a)=
sup_{x_0
eq0}
rac{mathbb E[f(x_2)]}{f(x_0)}.
$$
For a real polynomial $F$ having exactly one zero in $(u,v)$, write
$$
operatorname{root}(F;u,v)
$$
for that zero.

Determine the minimizing value of $a$ exactly.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Numerical optimization |
| **Problem Type** | Optimization |
| **Answer Type** | Exact symbolic expression |

---

## Domain Explanation

The problem asks for the sampling probability that minimizes a worst-case two-step convergence factor of exact randomized coordinate descent on a quadratic objective. The difficulty comes from the interaction of two independently sampled coordinate projections in the expected energy operator, so the primary sub-domain is Numerical optimization.

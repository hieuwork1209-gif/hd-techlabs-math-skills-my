# Normalized Math Problem

## LaTeX (Normalized)

Fix $r>0$ and $h>0$. Let the time-step lengths alternate periodically as
$$
h,\quad rh,\quad h,\quad rh,\ldots
$$
For each $n\geq5$, let $p_n$ be the polynomial of degree at most $5$ interpolating
$$
(t_{n-j},y_{n-j}),\qquad j=0,1,\ldots,5,
$$
and define the variable-step BDF5 method by
$$
p_n'(t_n)=f(t_n,y_n).
$$

Apply the method to the test equation $y'=0$. Call $r$ zero-stable if every solution of the resulting homogeneous recurrence is bounded for all $n\geq0$.

For a polynomial $g(x)$ having a unique zero in $(a,b)$, write $\operatorname{root}_{(a,b)}g$ for that zero.

Let $r_-<1$ be the lower endpoint of the set of zero-stable values of $r$. Find
$
u_*=r_-+\frac1{r_-}.
$

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Optimization and Numerical Mathematics |
| **Sub-domain** | Error analysis and stability |
| **Problem Type** | Parameter identification |
| **Answer Type** | Exact scalar |

---

## Domain Explanation

This problem asks for the exact lower zero-stability threshold of a periodically varying BDF5 recurrence. The central task is the stability analysis of a variable-step numerical time integrator through its period multipliers, so the primary classification is error analysis and stability.

# Normalized Math Problem

## LaTeX (Normalized)

Fix \(0<r\leq1\). Let the time-step lengths repeat periodically as
$$
h,\quad rh,\quad r^2h,\quad h,\quad rh,\quad r^2h,\ldots
$$
For each \(n\geq4\), let \(p_n\) be the polynomial of degree at most \(4\) interpolating
$$
(t_{n-j},y_{n-j}),\qquad j=0,1,2,3,4,
$$
and define the variable-step BDF4 method by
$$
p_n'(t_n)=f(t_n,y_n).
$$

Apply the method to the test equation \(y'=0\). Call \(r\) zero-stable if every solution of the resulting homogeneous recurrence is bounded for all \(n\geq0\).

Define
$$
\begin{aligned}
Q(t)={}&4t^{14}+18t^{13}+63t^{12}+172t^{11}+371t^{10}
+656t^9+926t^8\\
&+1074t^7+986t^6+728t^5+399t^4+164t^3+37t^2+4t-2,
\end{aligned}
$$
and write \(\operatorname{root}_{(u,v)}Q\) for the unique zero of \(Q\) in \((u,v)\), whenever it exists.

Determine exactly the critical value \(r_*\) such that the method is zero-stable precisely for
$$
r_*\leq r\leq1.
$$
Also determine which parasitic period multiplier lies on the unit circle when \(r=r_*\).

Give the final answer as \(r_*\).

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

This problem asks for the exact step-ratio threshold at which a periodic variable-step BDF4 recurrence loses zero-stability. The main task is the stability analysis of a numerical time-stepping method through its periodic parasitic modes, so the primary classification is error analysis and stability.

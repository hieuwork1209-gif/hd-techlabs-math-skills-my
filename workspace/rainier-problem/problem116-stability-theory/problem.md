# Normalized Math Problem

## LaTeX (Normalized)

Let $a,b>0$. On the interval $0<x<b$, consider the reaction-diffusion system
$$
\begin{aligned}
u_t&=u_{xx}+a u+v,\\
v_t&=10v_{xx}-3u-2v,
\end{aligned}
$$
with homogeneous Neumann boundary conditions
$$
u_x(t,0)=u_x(t,b)=v_x(t,0)=v_x(t,b)=0.
$$
Determine all pairs $(a,b)$ for which the spatially homogeneous ODE obtained by dropping the diffusion terms is exponentially stable, while the PDE has exactly three unstable nonconstant Neumann spatial frequencies. A frequency $n\ge1$ is called unstable if the corresponding two-dimensional Fourier-mode system has an eigenvalue with positive real part; each integer frequency $n$ is counted once.

---

## Domain Classification

| Field | Value |
|---|---|
| **Domain** | Differential Equations and Dynamical Systems |
| **Sub-domain** | Stability theory |
| **Problem Type** | Solve for unknowns |
| **Answer Type** | Interval or region description |

---

## Domain Explanation

This is a linear stability and pattern-selection problem for a two-species reaction-diffusion system on a bounded interval. The parameters control the local reaction dynamics and the spatial domain size, and the question asks for the exact region where diffusion creates a prescribed number of unstable spatial modes.

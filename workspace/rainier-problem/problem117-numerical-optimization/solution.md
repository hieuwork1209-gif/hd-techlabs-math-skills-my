## Steps

Step 1: Reduce the two heavy-ball steps to a residual polynomial
For a scalar eigendirection with curvature $\lambda$, put $t=\alpha\lambda$. Since $x_{-1}=x_0$,
$$
x_1=(1-t)x_0.
$$
The second step gives
$$
x_2=(1+\beta-t)x_1-\beta x_0,
$$
so
$$
\frac{x_2}{x_0}=q_{\alpha,\beta}(\lambda)
=1-\alpha(2+\beta)\lambda+\alpha^2\lambda^2.
$$
Therefore
$$
R(\alpha,\beta)=
\max_{\lambda\in[1,4]\cup[6,9]}|q_{\alpha,\beta}(\lambda)|.
$$

Step 2: Prove a sharp minimax lower bound from three spectral points
Let $p$ be any polynomial of degree at most $2$ with $p(0)=1$, and set
$$
M=\max_{\lambda\in[1,4]\cup[6,9]}|p(\lambda)|.
$$
The points $1,6,9$ belong to the spectral set. Lagrange interpolation at these three points, evaluated at $0$, gives
$$
p(0)=\frac{27}{20}p(1)-\frac35p(6)+\frac14p(9).
$$
Hence
$$
1\le
\left(\frac{27}{20}+\frac35+\frac14\right)M
=\frac{11}{5}M,
$$
so every such quadratic satisfies
$$
M\ge\frac5{11}.
$$
Since every two-step heavy-ball residual from Step 1 has degree at most $2$ and value $1$ at $\lambda=0$, this proves
$$
R(\alpha,\beta)\ge\frac5{11}.
$$

Step 3: Construct the extremal residual and recover the parameters
Consider
$$
p_*(\lambda)
=\frac{2(\lambda-5)^2-17}{33}
=1-\frac{20}{33}\lambda+\frac{2}{33}\lambda^2.
$$
At the four endpoints of the two spectral bands,
$$
p_*(1)=p_*(9)=\frac5{11},
\qquad
p_*(4)=p_*(6)=-\frac5{11}.
$$
Moreover,
$$
p_*'(\lambda)=\frac{4(\lambda-5)}{33}.
$$
Thus $p_*$ decreases on $[1,4]$ and increases on $[6,9]$. Its deeper minimum occurs at $\lambda=5$, which lies in the spectral gap and is not part of the maximization set. Consequently
$$
\max_{\lambda\in[1,4]\cup[6,9]}|p_*(\lambda)|=\frac5{11}.
$$
Matching $p_*$ with the heavy-ball residual from Step 1 gives
$$
\alpha^2=\frac2{33},
\qquad
\alpha(2+\beta)=\frac{20}{33}.
$$
Because $\alpha>0$,
$$
\alpha_*=\frac{\sqrt{66}}{33},
\qquad
\beta_*=\frac{10\sqrt{66}}{33}-2.
$$
The momentum is feasible since $10\sqrt{66}>66$. Equality in the interpolation bound from Step 2 forces the signs
$$
p(1)=\frac5{11},\qquad p(6)=-\frac5{11},\qquad p(9)=\frac5{11},
$$
so the extremal quadratic is unique; hence the heavy-ball parameters above are unique as well.

Final Answer: $\boxed{\left(\frac5{11},\left(\frac{\sqrt{66}}{33},\frac{10\sqrt{66}}{33}-2\right)\right)}$

---

## Answer

$\left(\frac5{11},\left(\frac{\sqrt{66}}{33},\frac{10\sqrt{66}}{33}-2\right)\right)$

---

## Classification

**Problem Type:** Optimization

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- heavy-ball residual polynomial
- minimax interpolation certificate
- clustered spectrum with a spectral gap

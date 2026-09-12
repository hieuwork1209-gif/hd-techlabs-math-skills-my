## Steps

Step 1: Identify the non-univalence locus
For $c>1$ and $F_{\lambda}(z)=z+\lambda/(z-c)$, put $U_c=\{u:|u+c|<1\}$. If $u=z-c$ and $v=w-c$, then
$$
F_{\lambda}(z)-F_{\lambda}(w)=(z-w)\left(1-\frac{\lambda}{uv}\right).
$$
Hence distinct points collide exactly when $\lambda=uv$ with $u,v\in U_c$. If $u=v$ and $\lambda=u^2$, then $F_{\lambda}'(u+c)=0$, so $F_{\lambda}$ is not injective. Therefore
$$
S_c=U_cU_c.
$$

Step 2: Convert the product set into a square image
Let $V_c=-U_c=\{w:|w-c|<1\}$. Then $S_c=V_cV_c$. Since $c>1$, $V_c$ lies in the right half-plane and the principal logarithm is defined there.

For $w=\rho e^{i\theta}\in V_c$, necessarily $|\theta|<\alpha:=\arcsin(1/c)$ and
$$
r_-(\theta)<\rho<r_+(\theta),\qquad
r_{\pm}=c\cos\theta\pm\sqrt{1-c^2\sin^2\theta}.
$$
Also $r_-r_+=c^2-1$. If $s(\theta)=\log r_+(\theta)$, then
$$
s''(\theta)=-\frac{c\cos\theta}{(1-c^2\sin^2\theta)^{3/2}}<0.
$$
Thus the upper boundary of $\log V_c$ is concave, while
$$
\log r_-(\theta)=\log(c^2-1)-s(\theta)
$$
is convex. Hence $\log V_c$ is convex. For $u,v\in V_c$,
$$
\frac{\log u+\log v}{2}\in\log V_c,
$$
so $w=\exp((\log u+\log v)/2)\in V_c$ and $w^2=uv$. Therefore
$$
V_cV_c=V_c^2,
$$
and hence $S_c=V_c^2$.

Step 3: Use the area formula
The squaring map $q(w)=w^2$ is injective on $V_c$, because $V_c$ lies in the right half-plane and cannot contain both $w$ and $-w$. The change-of-variables formula for an injective holomorphic map gives
$$
\operatorname{Area}(S_c)=\int_{V_c}|q'(w)|^2\,dA(w)=4\int_{V_c}|w|^2\,dA(w).
$$

Step 4: Evaluate the disk moment
Write $w=c+\zeta$, $|\zeta|<1$. Symmetry gives $\int\operatorname{Re}\zeta\,dA=0$, and
$$
\int_{|\zeta|<1}|\zeta|^2\,dA=2\pi\int_0^1r^3\,dr=\frac{\pi}{2}.
$$
Therefore
$$
\int_{V_c}|w|^2\,dA=\pi c^2+\frac{\pi}{2},
$$
so
$$
\operatorname{Area}(S_c)=4\pi c^2+2\pi=2\pi(2c^2+1).
$$

Final Answer: $\boxed{2\pi(2c^2+1)}$

---

## Answer

$2\pi(2c^2+1)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact symbolic expression

---

## Solution Concepts

- univalent holomorphic functions
- principal logarithm
- logarithmic convexity
- holomorphic area formula
- disk moment integrals

## Steps

Step 1: Prove uniform exponential stability when $ab<4$
Let
$$
A_1=\begin{pmatrix}-1&a\\0&-1\end{pmatrix},
\qquad
A_2=\begin{pmatrix}-1&0\\b&-1\end{pmatrix},
$$
and suppose $ab<4$. We seek a common quadratic Lyapunov function
$$
V(z)=z^TPz,
\qquad
P=\operatorname{diag}(1,r),
\qquad r>0.
$$
For mode $1$,
$$
A_1^TP+PA_1
=\begin{pmatrix}-2&a\\a&-2r\end{pmatrix},
$$
which is negative definite exactly when
$$
4r-a^2>0.
$$
For mode $2$,
$$
A_2^TP+PA_2
=\begin{pmatrix}-2&br\\br&-2r\end{pmatrix},
$$
which is negative definite exactly when
$$
4r-b^2r^2>0.
$$
Thus it is enough to choose
$$
\frac{a^2}{4}<r<\frac{4}{b^2}.
$$
Such an $r$ exists exactly when $ab<4$.

For this choice there is $\eta>0$ such that
$$
z^T(A_i^TP+PA_i)z\le-\eta\|z\|^2
\qquad(i=1,2).
$$
Therefore along every switching signal,
$$
\dot V\le-\eta\|z\|^2\le-\frac{\eta}{\lambda_{\max}(P)}V.
$$
Hence there are constants $C,\gamma>0$, depending only on $(a,b)$, for which
$$
\|z(t)\|\le Ce^{-\gamma t}\|z(0)\|
$$
for every admissible switching signal. Thus $ab<4$ is sufficient.

Step 2: Exclude $ab>4$ by a periodic switching signal
Let the system use mode $1$ for time $h>0$ and then mode $2$ for time $h$, repeated periodically. Since
$$
e^{A_1h}=e^{-h}\begin{pmatrix}1&ah\\0&1\end{pmatrix},
\qquad
e^{A_2h}=e^{-h}\begin{pmatrix}1&0\\bh&1\end{pmatrix},
$$
the one-cycle matrix is
$$
\Phi_h=e^{-2h}
\begin{pmatrix}
1&ah\\
bh&1+ab h^2
\end{pmatrix}.
$$
The matrix inside has determinant $1$ and trace $2+ab h^2$. Writing $c=\sqrt{ab}$, its larger eigenvalue is
$$
\mu_+(h)
=\exp\left(2\operatorname{arsinh}\frac{ch}{2}\right).
$$
Therefore
$$
\rho(\Phi_h)
=\exp\left(-2h+2\operatorname{arsinh}\frac{ch}{2}\right).
$$
If $ab>4$, then $c>2$, and the exponent has derivative $-2+c>0$ at $h=0$. Hence for all sufficiently small $h>0$,
$$
\rho(\Phi_h)>1.
$$
The corresponding periodic switching signal has an exponentially growing solution, so arbitrary-switching stability is impossible.

Step 3: Exclude the boundary $ab=4$
Now let $ab=4$, so $c=2$. For the same equal-dwell periodic switching,
$$
\rho(\Phi_h)
=\exp\bigl(-2h+2\operatorname{arsinh}h\bigr)<1
$$
for every fixed $h>0$. Thus each such periodic signal is individually exponentially stable. However its decay rate per unit time is
$$
\gamma_h
:= -\frac{1}{2h}\log\rho(\Phi_h)
=1-\frac{\operatorname{arsinh}h}{h}.
$$
Since
$$
\operatorname{arsinh}h=h-\frac{h^3}{6}+O(h^5),
$$
we have
$$
\gamma_h\to0
\qquad(h\to0^+).
$$

Suppose, contrary to uniform exponential stability under arbitrary switching, that there were constants $C,\gamma>0$ valid for every switching signal. Choose $h$ so small that $\gamma_h<\gamma/2$, and start on an eigenvector of $\Phi_h$ corresponding to its larger eigenvalue. At the cycle times $t=2nh$,
$$
\|z(t)\|=e^{-\gamma_h t}\|z(0)\|
$$
up to the fixed normalization of that eigenvector, whereas the assumed uniform estimate would give
$$
\|z(t)\|\le Ce^{-\gamma t}\|z(0)\|.
$$
Thus
$$
e^{(\gamma-\gamma_h)t}\le C
$$
for all $n$, which is impossible as $n\to\infty$. Hence the boundary $ab=4$ is not uniformly exponentially stable under arbitrary switching.

Step 4: State the exact parameter region
The common quadratic Lyapunov construction proves sufficiency for $ab<4$. The periodic-switching argument excludes $ab>4$, and the vanishing uniform decay rate excludes $ab=4$. Therefore the exact region is
$$
a>0,\qquad b>0,\qquad ab<4.
$$
Final Answer: $\boxed{\{(a,b):a>0,\ b>0,\ ab<4\}}$

---

## Answer

$\{(a,b):a>0,\ b>0,\ ab<4\}$

---

## Classification

**Problem Type:** Solve for unknowns

**Answer Type:** Interval or region description

---

## Solution Concepts

- switched linear systems
- common quadratic Lyapunov functions
- uniform exponential stability
- periodic switching
- matrix spectral radius

---

## Black-Box Audit — no issues found

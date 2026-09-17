## Steps

Step 1: Identify the critical eigenspace

Let
\[
F(u,\lambda)=-\Delta u-\lambda u-\eta u^2+u^3
\]
on \(\Omega=(0,\pi)^2\) with Neumann boundary conditions, and put
\[
\delta=\lambda-1,
\qquad
L=-\Delta-1.
\]
The Neumann eigenfunctions are \(\cos(mx)\cos(ny)\), with eigenvalues \(m^2+n^2\) for \(-\Delta\). Thus
\[
\ker L=\operatorname{span}\{\phi,\psi\},
\qquad
\phi(x,y)=\cos x,
\quad
\psi(x,y)=\cos y.
\]
Write
\[
u=A\phi+B\psi+w,
\qquad w\perp\ker L.
\]
Let \(v=A\phi+B\psi\).

Step 2: Solve the range equation to quadratic order

Since the reduced equation has no quadratic kernel term, it is enough for the cubic reduction to determine the quadratic range correction \(w_2\). The range equation gives
\[
Lw_2=\eta v^2.
\]
Using
\[
\cos^2x=\frac{1+\cos2x}{2},
\qquad
\cos^2y=\frac{1+\cos2y}{2},
\]
one gets
\[
v^2
=\frac{A^2+B^2}{2}
+\frac{A^2}{2}\cos2x
+\frac{B^2}{2}\cos2y
+2AB\cos x\cos y.
\]
On these four modes, \(L\) has eigenvalues
\[
-1,\quad 3,\quad 3,\quad 1,
\]
respectively. Therefore
\[
w_2
=\eta\left(
-\frac{A^2+B^2}{2}
+\frac{A^2}{6}\cos2x
+\frac{B^2}{6}\cos2y
+2AB\cos x\cos y
\right).
\tag{1}
\]

Step 3: Project the cubic terms onto the kernel

The kernel projection of \(v^3\) is
\[
\Pi(v^3)
=
\left(\frac34A^3+\frac32AB^2\right)\phi
+
\left(\frac34B^3+\frac32A^2B\right)\psi.
\tag{2}
\]
Indeed, \(\cos^3x\) projects onto \(\cos x\) with coefficient \(3/4\), while averaging \(\cos^2y\) gives \(1/2\).

Using (1), a direct projection gives
\[
\Pi(vw_2)
=\eta\left[
\left(-\frac5{12}A^3+\frac12AB^2\right)\phi
+
\left(-\frac5{12}B^3+\frac12A^2B\right)\psi
\right].
\tag{3}
\]

Now
\[
F(v+w_2,1+\delta)
=Lw_2-\delta v-\eta v^2-2\eta vw_2+v^3+\text{higher-order terms}.
\]
The quadratic range equation cancels \(Lw_2-\eta v^2\). Projecting the remaining cubic terms with (2) and (3) gives
\[
0
=A\left[-\delta+\alpha(\eta)A^2+\beta(\eta)B^2\right]+\text{higher-order terms},
\]
\[
0
=B\left[-\delta+\beta(\eta)A^2+\alpha(\eta)B^2\right]+\text{higher-order terms},
\tag{4}
\]
where
\[
\boxed{
\alpha(\eta)=\frac34+\frac56\eta^2,
\qquad
\beta(\eta)=\frac32-\eta^2.
}
\tag{5}
\]
The square symmetries \(x\mapsto\pi-x\), \(y\mapsto\pi-y\), and \(x\leftrightarrow y\) force the reduced equations to have exactly this \(D_4\)-equivariant cubic form.

Step 4: Determine the axial and diagonal branches

At cubic order, axial branches have \((A,B)=(r,0)\) or \((0,r)\), and satisfy
\[
\delta=\alpha r^2.
\tag{6}
\]
Since \(\alpha(\eta)>0\) for all \(\eta\), the axial branch is always on the \(\lambda>1\) side.

Diagonal branches have \(A=\pm B=r\), and satisfy
\[
\delta=(\alpha+\beta)r^2.
\tag{7}
\]
Now
\[
\alpha+\beta
=\frac94-\frac16\eta^2.
\]
Hence the diagonal cubic coefficient changes sign when
\[
\eta^2=\frac{27}{2},
\]
so
\[
\boxed{
\eta_{\mathrm{flip}}=\sqrt{\frac{27}{2}}=\frac{3\sqrt6}{2}.
}
\tag{8}
\]
For \(0\le\eta<\eta_{\mathrm{flip}}\), the diagonal branch lies on the \(\lambda>1\) side; for \(\eta>\eta_{\mathrm{flip}}\), it lies on the \(\lambda<1\) side. At \(\eta=\eta_{\mathrm{flip}}\), the diagonal cubic term is degenerate.

Step 5: Find the axial/diagonal exchange threshold

The quartic reduced potential corresponding to (4) is, up to an irrelevant positive overall factor,
\[
V_4(A,B)
=-\frac\delta2(A^2+B^2)
+\frac\alpha4(A^4+B^4)
+\frac\beta2A^2B^2.
\tag{9}
\]
At an axial critical point \((r,0)\) with \(r^2=\delta/\alpha\), the transverse Hessian eigenvalue is proportional to
\[
\beta-\alpha.
\]
Thus the axial branch is a strict local minimum of the quartic reduced energy when \(\beta>\alpha\).

At a diagonal critical point \((r,r)\) with \(r^2=\delta/(\alpha+\beta)\), the angular Hessian eigenvalue is proportional to
\[
\alpha-\beta.
\]
Thus, when \(\alpha+\beta>0\), the diagonal branch is a strict local minimum when \(\alpha>\beta\).

The exchange occurs at
\[
\alpha=\beta.
\]
Using (5),
\[
\frac34+\frac56\eta^2
=\frac32-\eta^2,
\]
so
\[
\eta^2=\frac9{22}.
\]
Therefore
\[
\boxed{
\eta_{\mathrm{ex}}=\frac3{\sqrt{22}}.
}
\tag{10}
\]
At this value
\[
\alpha=\beta=\frac{12}{11},
\]
and the cubic system becomes radially symmetric:
\[
0=A\left[-\delta+\frac{12}{11}(A^2+B^2)\right],
\qquad
0=B\left[-\delta+\frac{12}{11}(A^2+B^2)\right].
\]
Thus the cubic truncation has a whole circle of mixed directions, and higher-order terms are needed to resolve the branch selection.

For \(0\le\eta<\eta_{\mathrm{ex}}\), one has \(\beta>\alpha\), so the axial branches are the strict quartic-energy minima and the diagonal branches are saddles. For
\[
\eta_{\mathrm{ex}}<\eta<\eta_{\mathrm{flip}},
\]
one has \(\alpha>\beta\) and \(\alpha+\beta>0\), so the diagonal branches are the strict quartic-energy minima and the axial branches are saddles.

Final Answer:
\[
\boxed{
\left(
\alpha(\eta),\beta(\eta),\eta_{\mathrm{ex}},\eta_{\mathrm{flip}}
\right)
=
\left(
\frac34+\frac56\eta^2,
\frac32-\eta^2,
\frac3{\sqrt{22}},
\frac{3\sqrt6}{2}
\right)
}.
\]

---

## Answer

$\left(\frac34+\frac56\eta^2,\frac32-\eta^2,\frac3{\sqrt{22}},\frac{3\sqrt6}{2}\right)$

---

## Classification

**Problem Type:** Symbolic derivation

**Answer Type:** Tuple or ordered list

---

## Solution Concepts

- Lyapunov-Schmidt reduction at a multiple eigenvalue
- Neumann Laplacian mode decomposition
- quadratic slaving onto noncritical modes
- $D_4$-equivariant cubic normal form
- reduced-energy branch selection

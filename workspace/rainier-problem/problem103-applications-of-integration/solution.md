## Steps

Step 1: Set up a Mellin transform for the squared discriminant

Put
$$
F(x,y)=x^2-y^3,
$$
so
$$
I_n=\iint_{\mathbb R^2}e^{-y^2}e^{-nF(x,y)^2}\,dx\,dy.
$$
For $1/4<c<5/12$, Mellin inversion gives
$$
e^{-nF^2}=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
\Gamma(s)n^{-s}|F|^{-2s}\,ds.
$$
Hence
$$
I_n=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
\Gamma(s)n^{-s}M(s)\,ds,
$$
where
$$
M(s)=\iint_{\mathbb R^2}e^{-y^2}|x^2-y^3|^{-2s}\,dx\,dy.
$$
The strip $1/4<\Re s<5/12$ is exactly where the $x$-integral converges at infinity and the cusp at $(0,0)$ is still locally integrable.

Step 2: Evaluate the Mellin transform exactly

For $y>0$, set $x=y^{3/2}u$. Then
$$
\int_{\mathbb R}|x^2-y^3|^{-2s}\,dx
=y^{3/2-6s}A_+(s),
$$
where
$$
A_+(s)=\int_{\mathbb R}|u^2-1|^{-2s}\,du.
$$
Splitting at $|u|=1$ gives
$$
A_+(s)=
\sqrt\pi\,\frac{\Gamma(1-2s)}{\Gamma(3/2-2s)}
+\frac{\Gamma(2s-1/2)\Gamma(1-2s)}{\sqrt\pi}.
$$
For $y<0$, writing $y=-v$ and $x=v^{3/2}u$ gives
$$
\int_{\mathbb R}|x^2-y^3|^{-2s}\,dx
=v^{3/2-6s}A_-(s),
$$
with
$$
A_-(s)=\int_{\mathbb R}(1+u^2)^{-2s}\,du
=\sqrt\pi\,\frac{\Gamma(2s-1/2)}{\Gamma(2s)}.
$$
Since
$$
\int_0^\infty e^{-y^2}y^{3/2-6s}\,dy
=\frac12\Gamma\left(\frac54-3s\right),
$$
we obtain
$$
M(s)=\frac12\Gamma\left(\frac54-3s\right)
\left(A_+(s)+A_-(s)\right).
$$

Step 3: Extract the cusp contribution

The first pole to the right of the initial contour is at
$$
s=\frac5{12},
$$
coming from $\Gamma(5/4-3s)$. Since
$$
\Gamma\left(\frac54-3s\right)
\sim-\frac1{3(s-5/12)},
$$
the contribution of this pole is
$$
\frac{\Gamma(5/12)}6
\left(A_+\left(\frac5{12}\right)+A_-\left(\frac5{12}\right)\right)n^{-5/12}.
$$
At $s=5/12$,
$$
A_-\left(\frac5{12}\right)
=\sqrt\pi\frac{\Gamma(1/3)}{\Gamma(5/6)},
$$
$$
A_+\left(\frac5{12}\right)
=\sqrt\pi\frac{\Gamma(1/6)}{\Gamma(2/3)}
+\frac{\Gamma(1/3)\Gamma(1/6)}{\sqrt\pi}.
$$
Using
$$
\Gamma(1/6)\Gamma(5/6)=2\pi,
\qquad
\Gamma(1/3)\Gamma(2/3)=\frac{2\pi}{\sqrt3},
$$
we get
$$
A_+\left(\frac5{12}\right)+A_-\left(\frac5{12}\right)
=\frac{3+\sqrt3}{2\sqrt\pi}\Gamma(1/6)\Gamma(1/3).
$$
Thus the leading term is
$$
C_0n^{-5/12},
\qquad
C_0=
\frac{(3+\sqrt3)\Gamma(5/12)\Gamma(1/6)\Gamma(1/3)}{12\sqrt\pi}.
$$
This is the contribution of the singular cusp where the two real branches meet.

Step 4: Extract the regular-branch correction

The next pole is at $s=1/2$. It comes only from $A_+(s)$, because $u^2-1=0$ corresponds to the two regular branches $x=\pm y^{3/2}$ for $y>0$.

Write
$$
A_+(s)=\Gamma(1-2s)
\left(
\frac{\sqrt\pi}{\Gamma(3/2-2s)}
+\frac{\Gamma(2s-1/2)}{\sqrt\pi}
\right).
$$
The bracket tends to $2$ at $s=1/2$, while
$$
\Gamma(1-2s)\sim-\frac1{2(s-1/2)}.
$$
Hence
$$
\operatorname*{Res}_{s=1/2}A_+(s)=-1.
$$
Therefore
$$
\operatorname*{Res}_{s=1/2}M(s)
=-\frac12\Gamma\left(-\frac14\right)
=2\Gamma\left(\frac34\right).
$$
Multiplying by $\Gamma(1/2)=\sqrt\pi$, the residue of the full Mellin integrand is
$$
2\sqrt\pi\,\Gamma\left(\frac34\right)n^{-1/2}.
$$
Shifting the contour to the right contributes minus the crossed residues, so the regular-branch term is
$$
-2\sqrt\pi\,\Gamma\left(\frac34\right)n^{-1/2}.
$$
The next pole is at $s=3/4$, so the remaining contour is $o(n^{-1/2})$.

Step 5: Recover the requested limit

Combining Steps 3 and 4,
$$
I_n=
C_0n^{-5/12}
-2\sqrt\pi\,\Gamma\left(\frac34\right)n^{-1/2}
+o(n^{-1/2}),
$$
where
$$
C_0=
\frac{(3+\sqrt3)\Gamma(5/12)\Gamma(1/6)\Gamma(1/3)}{12\sqrt\pi}.
$$
Hence
$$
\lim_{n\to\infty}n^{1/2}
\left(I_n-\frac{C_0}{n^{5/12}}\right)
=-2\sqrt\pi\,\Gamma\left(\frac34\right).
$$
Final Answer: $\boxed{-2\sqrt\pi\,\Gamma\left(\frac34\right)}$

---

## Answer

$-2\sqrt\pi\,\Gamma(3/4)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Real number

---

## Solution Concepts

- discriminant cusp geometry
- Mellin inversion
- weighted cusp scaling
- regular-branch correction
- Gamma-function residues

## Steps

Step 1: Set up a Mellin transform for the squared discriminant

Put
$$
F(x,y)=x^2-y^3,
$$
so
$$
I_n=\iint_{\mathbb{R}^2}e^{-y^2}e^{-nF(x,y)^2}\,dx\,dy.
$$
For $\frac{1}{4}<c<\frac{5}{12}$, Mellin inversion gives
$$
e^{-nF^2}=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}
\Gamma(s)n^{-s}|F|^{-2s}\,ds.
$$
So
$$
I_n=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}
\Gamma(s)n^{-s}M(s)\,ds,
$$
where
$$
M(s)=\iint_{\mathbb{R}^2}e^{-y^2}|x^2-y^3|^{-2s}\,dx\,dy.
$$
The strip $\frac{1}{4}<\Re s<\frac{5}{12}$ is exactly where the $x$-integral converges at infinity and the cusp at $(0,0)$ remains locally integrable.

Step 2: Evaluate the Mellin transform exactly

For $y>0$, set $x=y^{\frac{3}{2}}u$. Then
$$
\int_{\mathbb{R}}|x^2-y^3|^{-2s}\,dx
=y^{\frac{3}{2}-6s}A_+(s),
$$
where
$$
A_+(s)=\int_{\mathbb{R}}|u^2-1|^{-2s}\,du.
$$
Splitting at $|u|=1$ gives
$$
A_+(s)=
\sqrt{\pi}\,\frac{\Gamma(1-2s)}{\Gamma\left(\frac{3}{2}-2s\right)}
+\frac{\Gamma\left(2s-\frac{1}{2}\right)\Gamma(1-2s)}{\sqrt{\pi}}.
$$
For $y<0$, write $y=-v$ and set $x=v^{\frac{3}{2}}u$. This gives
$$
\int_{\mathbb{R}}|x^2-y^3|^{-2s}\,dx
=v^{\frac{3}{2}-6s}A_-(s),
$$
with
$$
A_-(s)=\int_{\mathbb{R}}(1+u^2)^{-2s}\,du
=\sqrt{\pi}\,\frac{\Gamma\left(2s-\frac{1}{2}\right)}{\Gamma(2s)}.
$$
Since
$$
\int_0^\infty e^{-y^2}y^{\frac{3}{2}-6s}\,dy
=\frac{1}{2}\Gamma\left(\frac{5}{4}-3s\right),
$$
we get
$$
M(s)=\frac{1}{2}\Gamma\left(\frac{5}{4}-3s\right)
\left(A_+(s)+A_-(s)\right).
$$

Step 3: Extract the cusp contribution

The first pole to the right of the initial contour is at
$$
s=\frac{5}{12},
$$
coming from $\Gamma\left(\frac{5}{4}-3s\right)$. Since
$$
\Gamma\left(\frac{5}{4}-3s\right)
\sim-\frac{1}{3\left(s-\frac{5}{12}\right)},
$$
the contribution of this pole is
$$
\frac{\Gamma\left(\frac{5}{12}\right)}{6}
\left(A_+\left(\frac{5}{12}\right)+A_-\left(\frac{5}{12}\right)\right)n^{-\frac{5}{12}}.
$$
At $s=\frac{5}{12}$,
$$
A_-\left(\frac{5}{12}\right)
=\sqrt{\pi}\frac{\Gamma\left(\frac{1}{3}\right)}{\Gamma\left(\frac{5}{6}\right)},
$$
$$
A_+\left(\frac{5}{12}\right)
=\sqrt{\pi}\frac{\Gamma\left(\frac{1}{6}\right)}{\Gamma\left(\frac{2}{3}\right)}
+\frac{\Gamma\left(\frac{1}{3}\right)\Gamma\left(\frac{1}{6}\right)}{\sqrt{\pi}}.
$$
Using
$$
\Gamma\left(\frac{1}{6}\right)\Gamma\left(\frac{5}{6}\right)=2\pi,
\qquad
\Gamma\left(\frac{1}{3}\right)\Gamma\left(\frac{2}{3}\right)=\frac{2\pi}{\sqrt{3}},
$$
we get
$$
A_+\left(\frac{5}{12}\right)+A_-\left(\frac{5}{12}\right)
=\frac{3+\sqrt{3}}{2\sqrt{\pi}}\Gamma\left(\frac{1}{6}\right)\Gamma\left(\frac{1}{3}\right).
$$
So the leading term is
$$
C_0n^{-\frac{5}{12}},
\qquad
C_0=
\frac{(3+\sqrt{3})\Gamma\left(\frac{5}{12}\right)\Gamma\left(\frac{1}{6}\right)\Gamma\left(\frac{1}{3}\right)}{12\sqrt{\pi}}.
$$
This term comes from the singular cusp where the two real branches meet.

Step 4: Extract the regular-branch correction

The next pole is at $s=\frac{1}{2}$. It comes only from $A_+(s)$, because $u^2-1=0$ corresponds to the two regular branches $x=\pm y^{\frac{3}{2}}$ for $y>0$.

Write
$$
A_+(s)=\Gamma(1-2s)
\left(
\frac{\sqrt{\pi}}{\Gamma\left(\frac{3}{2}-2s\right)}
+\frac{\Gamma\left(2s-\frac{1}{2}\right)}{\sqrt{\pi}}
\right).
$$
The bracket tends to $2$ at $s=\frac{1}{2}$, while
$$
\Gamma(1-2s)\sim-\frac{1}{2\left(s-\frac{1}{2}\right)}.
$$
This gives
$$
\operatorname*{Res}_{s=\frac{1}{2}}A_+(s)=-1.
$$
Then
$$
\operatorname*{Res}_{s=\frac{1}{2}}M(s)
=-\frac{1}{2}\Gamma\left(-\frac{1}{4}\right)
=2\Gamma\left(\frac{3}{4}\right).
$$
Multiplying by $\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}$, the residue of the full Mellin integrand is
$$
2\sqrt{\pi}\,\Gamma\left(\frac{3}{4}\right)n^{-\frac{1}{2}}.
$$
Shifting the contour to the right contributes minus the crossed residues, so the regular-branch term is
$$
-2\sqrt{\pi}\,\Gamma\left(\frac{3}{4}\right)n^{-\frac{1}{2}}.
$$
The next pole is at $s=\frac{3}{4}$, so the remaining contour is $o\left(n^{-\frac{1}{2}}\right)$.

Step 5: Recover the requested limit

Combining Steps 3 and 4,
$$
I_n=
C_0n^{-\frac{5}{12}}
-2\sqrt{\pi}\,\Gamma\left(\frac{3}{4}\right)n^{-\frac{1}{2}}
+o\left(n^{-\frac{1}{2}}\right),
$$
where
$$
C_0=
\frac{(3+\sqrt{3})\Gamma\left(\frac{5}{12}\right)\Gamma\left(\frac{1}{6}\right)\Gamma\left(\frac{1}{3}\right)}{12\sqrt{\pi}}.
$$
It follows that
$$
\lim_{n\to\infty}n^{\frac{1}{2}}
\left(I_n-\frac{C_0}{n^{\frac{5}{12}}}\right)
=-2\sqrt{\pi}\,\Gamma\left(\frac{3}{4}\right).
$$
Final Answer: $\boxed{-2\sqrt{\pi}\,\Gamma\left(\frac{3}{4}\right)}$

---

## Answer

$-2\sqrt{\pi}\,\Gamma\left(\frac{3}{4}\right)$

---

## Classification

**Problem Type:** Exact computation

**Answer Type:** Exact scalar

---

## Solution Concepts

- discriminant cusp geometry
- Mellin inversion
- weighted cusp scaling
- regular-branch correction
- Gamma-function residues

# Lattice Arithmetic Calculations

## Scope

This module records explicit arithmetic calculations used in the research framework. It is intentionally limited to inspectable algebraic and computational statements.

It distinguishes:

- Gram-matrix invariants;
- discriminant groups and quadratic forms;
- lattice inclusions and saturation indices;
- inclusion/transition matrices;
- gluing and isotropy tests;
- primitivity calculations;
- rational comparison maps;
- Navier–Stokes identities.

An arithmetic calculation is not, by itself, a proof of geometric cycle realization. Any identification of an arithmetic lattice with a geometrically defined lattice requires additional geometric input and is marked **OPEN** where that input has not been established.

---

## 1. Saturated Gram Matrix

The principal Gram matrix is

\[
G_{\mathrm{sat}}=
\begin{pmatrix}
36&12\\
12&0
\end{pmatrix}.
\]

Its determinant is

\[
\det(G_{\mathrm{sat}})=-144.
\]

The gcd of the entries is 12.

The Smith normal form is

\[
\operatorname{SNF}(G_{\mathrm{sat}})
=\operatorname{diag}(12,12).
\]

Therefore the discriminant group of the corresponding nondegenerate rank-two lattice is

\[
A_{\mathrm{sat}}
\cong (\mathbb Z/12\mathbb Z)^2.
\]

**Status:** COMPUTATIONALLY VERIFIED.

---

## 2. Discriminant Form

For an integral nondegenerate lattice \(L\) with dual lattice \(L^\vee\),

\[
A_L=L^\vee/L.
\]

When the lattice is even, the discriminant quadratic form is

\[
q_L(x+L)=\langle x,x\rangle\pmod{2\mathbb Z}.
\]

The discriminant group and its quadratic form must be treated as separate data: the group alone does not determine the full discriminant form.

**Status:** DERIVED.

---

## 3. Primary Decomposition

Since

\[
12=2^2\cdot3,
\]

the group decomposes into its primary components:

\[
(\mathbb Z/12\mathbb Z)^2
\cong
(\mathbb Z/4\mathbb Z)^2
\oplus
(\mathbb Z/3\mathbb Z)^2.
\]

This decomposition is useful when testing local obstructions and possible isotropic subgroups.

**Status:** DERIVED.

---

## 4. Saturation and Index Formula

Let

\[
\Lambda\subseteq\Lambda'\subseteq\Lambda_{\mathrm{sat}}
\]

be full-rank lattices in the same rational vector space.

The determinant relation for a finite-index inclusion

\[
L\subseteq L'
\]

is

\[
|\det G_L|
=
[L':L]^2|\det G_{L'}|.
\]

Thus an index cannot be inferred from a Gram determinant alone unless the reference lattice and its Gram determinant are specified.

In particular, the expression

\[
[\Lambda_{\mathrm{sat}}:\Lambda]=\sqrt{|\det G|}
\]

is **not** used as a universal formula.

**Status:** PROVED.

---

## 5. Index-2 Extension

The index-2 extension considered in the research is

\[
R=\frac{P+Q}{2}.
\]

The inclusion presentation has Smith normal form

\[
\operatorname{SNF}(M_{\mathrm{inc}})
=\operatorname{diag}(1,2),
\]

so the inclusion has index 2.

This is an inclusion-matrix statement. It is not the Smith normal form of the Gram matrix.

The saturated Gram matrix remains

\[
G_{\mathrm{sat}}=
\begin{pmatrix}
36&12\\
12&0
\end{pmatrix},
\]

with determinant \(-144\).

**Status:** COMPUTATIONALLY VERIFIED.

---

## 6. Gram SNF vs. Inclusion SNF

These are distinct invariants.

### Gram matrix

For a basis matrix with Gram matrix \(G\),

\[
\operatorname{SNF}(G)
\]

describes the integral structure encoded by the bilinear form and determines the discriminant group in the nondegenerate case.

### Inclusion matrix

For an inclusion

\[
L\subseteq L',
\]

a presentation/transition matrix \(M_{\mathrm{inc}}\) describes the module quotient

\[
L'/L.
\]

Its Smith normal form gives the elementary divisors of that quotient.

Therefore

\[
\operatorname{SNF}(G)
\neq
\operatorname{SNF}(M_{\mathrm{inc}})
\]

in general, and neither should be substituted for the other.

**Status:** PROVED.

---

## 7. Ambient Identification Boundary

The arithmetic data above determine explicit lattice invariants.

They do not automatically establish that the computed lattice is the intended geometrically defined cohomological or cycle lattice.

The remaining identification question is therefore kept separate:

\[
\text{arithmetic lattice}
\quad\longrightarrow\quad
\text{geometric lattice}.
\]

This boundary is explicitly marked **OPEN** wherever the required ambient-module or cohomological identification has not been established.

**Status:** OPEN.

---

## 8. Weil Lattice

The Weil calculation gives

\[
G_W=M_W=8I_2.
\]

Hence

\[
A_W\cong(\mathbb Z/8\mathbb Z)^2.
\]

For the standard even-lattice convention, the associated discriminant quadratic form is represented by

\[
q_W(a,b)=\frac{a^2+b^2}{8}
\pmod{2\mathbb Z}.
\]

**Status:** COMPUTATIONALLY VERIFIED.

---

## 9. Comparison Lattice \(L_1\)

The comparison matrix is

\[
L_1=
\begin{pmatrix}
144&24\\
24&0
\end{pmatrix}.
\]

Its determinant is

\[
\det(L_1)=-576.
\]

Its discriminant group is

\[
A_{L_1}\cong(\mathbb Z/24\mathbb Z)^2.
\]

The corresponding quadratic expression used in the comparison is

\[
q_{L_1}(a,b)
=
\frac{ab}{12}-\frac{b^2}{4}
\pmod{2\mathbb Z}.
\]

**Status:** COMPUTATIONALLY VERIFIED.

---

## 10. Gluing and Isotropy Tests

A candidate gluing subgroup must be tested inside the appropriate discriminant form, not merely by matching group orders.

For a subgroup \(H\subseteq A_L\), isotropy requires

\[
q_L(h)=0
\pmod{2\mathbb Z}
\]

for every \(h\in H\), together with the appropriate bilinear compatibility.

The tested order-8 candidate

\[
H=\langle(8,0)\rangle
\]

does not provide the required isotropic gluing.

A simple index-3 gluing likewise does not supply the required identification.

The four-dimensional candidate \(8I_4\) is rejected by the relevant signature constraint.

**Status:** COMPUTATIONALLY VERIFIED.

---

## 11. Tensor-Product Primitivity

For the tensor-product matrix \(M_{PR}\), the Smith normal form is

\[
\operatorname{SNF}(M_{PR})
=
\operatorname{diag}(1,1,0,\ldots,0).
\]

Thus the image is primitive in the module in which this matrix is being considered.

This establishes an intra-lattice primitivity statement.

It does **not** by itself establish the identification of that module with the intended ambient cohomology.

**Status:** COMPUTATIONALLY VERIFIED.

---

## 12. Rational Comparison Matrix

The rational comparison matrix is

\[
B=
\begin{pmatrix}
11/4&3/4\\
7/4&3/4
\end{pmatrix}.
\]

Its determinant is

\[
\det B=-3/4,
\]

and therefore

\[
|\det B|^2=9/16.
\]

This is recorded as a rational comparison invariant; it is not interpreted as a geometric realization statement.

**Status:** COMPUTATIONALLY VERIFIED.

---

## 13. Cup-Product Weil Matrix

The standard symplectic calculation gives

\[
M_W^{\cup}
=
\operatorname{diag}(32,-32).
\]

This value is retained as the explicit result of the normalization/calibration calculation.

**Status:** DERIVED / COMPUTATIONALLY VERIFIED.

---

## 14. Calculation vs. Realization

The logical hierarchy used throughout this repository is:

1. exact matrix construction;
2. exact determinant and Smith normal form;
3. discriminant-group computation;
4. discriminant-form and gluing tests;
5. module inclusion and primitivity analysis;
6. comparison of candidate lattices;
7. geometric identification;
8. geometric realization.

Steps 1–6 can be established by explicit arithmetic and computation.

Steps involving geometric identification or realization require additional mathematical input and are not promoted to **PROVED** merely because the preceding arithmetic is consistent.

---

# Navier–Stokes Arithmetic and Identities

## 15. Navier–Stokes System

For incompressible flow,

\[
\partial_tu+(u\cdot\nabla)u
=
-\nabla p+\nu\Delta u+f,
\qquad
\nabla\cdot u=0.
\]

The vorticity is

\[
\omega=\nabla\times u.
\]

The strain tensor is

\[
S=\frac{\nabla u+(\nabla u)^T}{2}.
\]

**Status:** PROVED.

---

## 16. Global Enstrophy Identity

Under the appropriate smoothness and boundary/decay assumptions, the unforced identity is

\[
\frac12\frac{d}{dt}\|\omega\|_2^2
+
\nu\|\nabla\omega\|_2^2
=
\int \omega^TS\omega\,dx.
\]

With forcing, the corresponding forcing contribution must also be retained.

This is an equality, not a one-sided lower bound on vortex stretching.

**Status:** PROVED.

---

## 17. Magnitude-Direction Factorization

On the set where \(\omega\neq0\), write

\[
\omega=\rho\xi,
\qquad
\rho=|\omega|,
\qquad
|\xi|=1.
\]

Then the local magnitude balance is

\[
D_t\rho
=
\rho\,\xi^TS\xi
+
\nu\Delta\rho
-
\nu\rho|\nabla\xi|^2.
\]

Equivalently, defining

\[
M=D_t\rho,
\qquad
P=\rho\xi^TS\xi,
\qquad
N=\nu\rho|\nabla\xi|^2,
\]

gives

\[
M=P+\nu\Delta\rho-N.
\]

**Status:** DERIVED.

---

## 18. Nonlinear Regularity Boundary

The vortex-stretching term

\[
\int \omega^TS\omega\,dx
\]

does not have a universal positive lower bound of the form

\[
C\|\omega\|_3^3
\]

with \(C>0\). Its sign can vary.

Likewise, a Beale–Kato–Majda-type divergence condition is a conditional obstruction criterion for continuation: under its hypotheses, loss of regularity implies divergence of the relevant vorticity integral. It is not, by itself, a construction or proof of finite-time blow-up.

Therefore the global nonlinear regularity closure remains:

**Status: OPEN.**

---

## 19. Reproducibility Checklist

For every numerical or symbolic claim in this module, the intended verification order is:

1. state the exact matrix or equation;
2. compute determinant/rank where relevant;
3. compute Smith normal form;
4. identify the resulting quotient or discriminant group;
5. record the discriminant form when applicable;
6. distinguish Gram data from inclusion data;
7. test gluing/isotropy explicitly;
8. test primitivity in the stated module;
9. identify the exact ambient module before making a geometric identification;
10. assign one of the statuses:
   - **PROVED**
   - **DERIVED**
   - **COMPUTATIONALLY VERIFIED**
   - **OPEN**

No geometric conclusion is promoted solely from arithmetic compatibility.

---

## Status Summary

| Item | Status |
|---|---|
| \(G_{\mathrm{sat}}\), determinant, SNF | COMPUTATIONALLY VERIFIED |
| \(A_{\mathrm{sat}}\cong(\mathbb Z/12)^2\) | COMPUTATIONALLY VERIFIED |
| Discriminant-form definition | DERIVED |
| Index-2 extension / inclusion SNF | COMPUTATIONALLY VERIFIED |
| Gram SNF vs. inclusion SNF distinction | PROVED |
| Ambient geometric identification | OPEN |
| \(M_W=8I_2\) | COMPUTATIONALLY VERIFIED |
| \(A_W\cong(\mathbb Z/8)^2\) | COMPUTATIONALLY VERIFIED |
| \(L_1\) and its discriminant data | COMPUTATIONALLY VERIFIED |
| Tested gluing obstructions | COMPUTATIONALLY VERIFIED |
| \(M_{PR}\) primitivity | COMPUTATIONALLY VERIFIED |
| Rational matrix \(B\) | COMPUTATIONALLY VERIFIED |
| \(M_W^{\cup}=\operatorname{diag}(32,-32)\) | DERIVED / COMPUTATIONALLY VERIFIED |
| Navier–Stokes identities | PROVED / DERIVED as marked |
| Global nonlinear regularity closure | OPEN |

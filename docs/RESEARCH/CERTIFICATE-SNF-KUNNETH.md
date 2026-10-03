# Certificate: Künneth-Graded Lattice and Smith Normal Form Calculation

**Repository:** `jackophil-dev/public-math-research`  
**Author / Researcher:** Philippe Beauchamp  
**ORCID:** [0009-0003-7407-394X](https://orcid.org/0009-0003-7407-394X)

> **Status:** Public mathematical certificate / reproducible arithmetic record.  
> This document records an explicit lattice calculation. It does **not** claim a proof of the Hodge Conjecture or of a general geometric realization theorem.

## 1. Purpose

This certificate isolates one part of the research program that can be stated and checked independently of the unresolved geometric realization questions:

1. identify a specified integral lattice coming from a chosen middle-dimensional/Künneth component;
2. record its integral Gram matrix;
3. compute its determinant and Smith normal form (SNF);
4. identify the resulting discriminant group;
5. keep the arithmetic lattice calculation separate from any claim that the lattice is the full lattice of algebraic cycles.

The distinction is important: an SNF computation is an arithmetic invariant of a specified integral lattice. By itself it does not prove that a rational Hodge class is or is not represented by an algebraic cycle.

## 2. Künneth grading and the lattice under study

For an abelian fourfold (A), the middle cohomology is

$$
H^4(A,\mathbf Z),
$$

with its usual Künneth decomposition into tensor-degree components. In a concrete Weil-type/CM model, one may select a specified rational subspace and then specify the integral lattice obtained from the chosen integral cohomology basis.

For this certificate, denote the resulting rank-two integral lattice by

$$
L = \mathbf Z e_1 \oplus \mathbf Z e_2,
$$

and suppose its intersection pairing in the ordered basis ((e_1,e_2)) is represented by

$$
G =
\begin{pmatrix}
36 & 12 \\
12 & 0
\end{pmatrix}.
$$

The matrix is integral and symmetric, so it defines an integral bilinear pairing on (L).

## 3. Arithmetic theorem

### Proposition (SNF and discriminant group of the explicit rank-two lattice)

For

$$
G =
\begin{pmatrix}
36 & 12 \\
12 & 0
\end{pmatrix},
$$

the following statements hold:

1. (det(G)=-144);
2. the gcd of all entries is (12);
3. the Smith normal form is

$$
\operatorname{SNF}(G)
=
\operatorname{diag}(12,12);
$$

4. consequently, for the nondegenerate lattice (L),

$$
L^*/L \cong
\mathbf Z/12\mathbf Z \oplus \mathbf Z/12\mathbf Z.
$$

### Verification

The determinant is

$$
\det(G)=36\cdot 0-12\cdot12=-144.
$$

For a (2\times2) integer matrix, the first Smith invariant is the gcd of all entries. Hence

$$
d_1=\gcd(36,12,12,0)=12.
$$

Since the product of the Smith invariants equals the absolute determinant,

$$
d_1d_2=|\det(G)|=144,
$$

so

$$
d_2=144/12=12.
$$

Therefore

$$
\operatorname{SNF}(G)=\operatorname{diag}(12,12).
$$

Because the determinant is nonzero, the lattice is nondegenerate and its discriminant group has order (144). The SNF gives the decomposition

$$
A_L:=L^*/L
\cong
\mathbf Z/12\mathbf Z\oplus\mathbf Z/12\mathbf Z.
$$

This completes the arithmetic verification.

## 4. What the calculation does and does not establish

### Established by this certificate

- the determinant of the displayed Gram matrix;
- the Smith invariant factors;
- the abstract discriminant-group decomposition of the displayed lattice;
- a reproducible arithmetic checkpoint for any larger construction that contains this lattice.

### Not established by this certificate

The calculation does **not** by itself establish:

- that this rank-two lattice is the complete lattice of algebraic codimension-two cycles;
- that every rational Hodge class in the ambient cohomology is algebraic;
- that the discriminant group constitutes an obstruction to algebraicity in a particular geometric model;
- that a proposed Künneth component is saturated in the full ambient integral lattice;
- a general theorem about Weil-type abelian fourfolds.

Any of those stronger conclusions require additional geometric input and, where relevant, an explicit saturation or realization argument.

## 5. Saturation checkpoint

If

$$
L \subseteq L' \subseteq L_{\mathrm{amb}}
$$

are integral lattice inclusions, then the index

$$
[L':L]
$$

must be determined before identifying (L) with a saturated geometric lattice.

In particular, a finite-index enlargement can change the discriminant group. Thus the SNF calculation above should be regarded as a certificate for the **specified lattice (L)**, not automatically for every larger lattice containing it.

A complete realization claim would therefore require, at minimum:

1. an explicit embedding into the ambient integral cohomology lattice;
2. the index of the embedding or an independent proof of saturation;
3. compatibility of the intersection pairing;
4. the relevant geometric identification of the lattice with the intended cycle/Hodge subspace.

## 6. Reproducibility protocol

A computational implementation should verify the following identities from integer arithmetic:

$$
\det(G)=-144,
$$

$$
\gcd(G_{ij})=12,
$$

and

$$
\operatorname{SNF}(G)=\operatorname{diag}(12,12).
$$

A direct implementation should preferably produce the unimodular matrices (U,V\in GL_2(\mathbf Z)) satisfying

$$
UGV=\operatorname{diag}(12,12).
$$

Recording (U) and (V), when available, provides a stronger audit trail than recording the diagonal result alone.

## 7. Relation to the broader research program

This certificate is one arithmetic component of the broader Q(i)/Weil research notes. The public research record intentionally separates:

- explicit calculations;
- normalization and scaling questions;
- lattice identification and saturation;
- conjectural CM/Weil-to-geometric realization steps.

The existing public Q(i) calibration explicitly records that the full realization lattice/SNF problem remains open. This certificate should therefore be read as a **local, explicit SNF calculation**, not as a resolution of that open problem.

## 8. Research status

**Arithmetic calculation:** explicit and checkable.  
**Discriminant-group identification:** explicit for the displayed lattice.  
**Saturation in an ambient geometric lattice:** open unless separately proved.  
**General geometric realization:** not established.

---

**Researcher:** Philippe Beauchamp  
**ORCID:** [0009-0003-7407-394X](https://orcid.org/0009-0003-7407-394X)  
**Public repository:** [public-math-research](https://github.com/jackophil-dev/public-math-research)

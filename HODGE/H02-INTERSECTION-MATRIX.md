# H02 — Intersection Matrix Realization

**Researcher:** Philippe Beauchamp  
**ORCID:** 0009-0003-7407-394X  
**Track:** Hodge / Weil-type abelian fourfolds

## 1. Certificate ID

**CERT-H02 — Intersection Matrix Realization**

## 2. Theorem Statement

For a specified integral middle-dimensional cohomology lattice equipped with its cup-product pairing, an ordered integral basis determines an integral Gram matrix. The matrix records the pairing of the chosen basis vectors and can be used to compute determinant and discriminant invariants.

## 3. Definitions / Hypotheses

Let (L) be the explicitly specified integral lattice and (G=(langle e_i,e_jangle)) its Gram matrix in an ordered integral basis.

The concrete rank-two checkpoint used in this research is

[
G=
egin{pmatrix}
36&12\
12&0
end{pmatrix}.
]

## 4. Calculation / Proof

The matrix is integral and symmetric. Its determinant is

[
det(G)=36cdot0-12cdot12=-144.
]

Hence the displayed pairing is non-degenerate.

This calculation is the arithmetic intersection-matrix checkpoint used by the subsequent SNF and discriminant analysis.

## 5. Reproducibility Checkpoint

Directly verify:

[
G_{12}=G_{21}=12,
qquad
det(G)=-144.
]

Any geometric interpretation must use the explicitly stated lattice and basis.

## 6. Status

**COMPUTATIONALLY VERIFIED — explicit integral Gram-matrix calculation.**

## 7. Explicit Scope Limitation

The calculation proves properties of the **specified matrix/lattice**. It does not by itself identify that lattice with the complete algebraic-cycle lattice of a general abelian fourfold.

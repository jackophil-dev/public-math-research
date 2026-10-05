# H06 — Smith Normal Form and Discriminant Group

**Researcher:** Philippe Beauchamp  
**ORCID:** 0009-0003-7407-394X  
**Track:** Hodge / Weil-type abelian fourfolds

## 1. Certificate ID

**CERT-H06 — Smith Normal Form Torsion Bounds**

## 2. Theorem Statement

For the explicitly specified rank-two integral lattice with Gram matrix

[
G=
egin{pmatrix}
36&12\
12&0
end{pmatrix},
]

the Smith normal form is

[
operatorname{SNF}(G)=operatorname{diag}(12,12),
]

and the associated discriminant group is

[
L^*/Lcong
mathbf Z/12mathbf Zoplusmathbf Z/12mathbf Z.
]

## 3. Definitions / Hypotheses

Let (L=mathbf Ze_1oplusmathbf Ze_2), with pairing represented by the displayed integral Gram matrix (G).

The lattice is non-degenerate because (det(G)
e0).

## 4. Calculation / Proof

First,

[
det(G)=36cdot0-12cdot12=-144.
]

For a (2	imes2) integer matrix, the first Smith invariant is the gcd of its entries:

[
d_1=gcd(36,12,12,0)=12.
]

Since the product of the Smith invariants equals the absolute determinant,

[
d_1d_2=144,
]

so

[
d_2=12.
]

Therefore

[
oxed{operatorname{SNF}(G)=operatorname{diag}(12,12)}.
]

Consequently,

[
oxed{L^*/Lcong(mathbf Z/12mathbf Z)^2}.
]

The discriminant group has order (144).

## 5. Reproducibility Checkpoint

An independent arithmetic implementation should return exactly:

[
det(G)=-144,
]

[
gcd(G_{ij})=12,
]

[
operatorname{SNF}(G)=operatorname{diag}(12,12).
]

Where available, recording unimodular (U,Vin GL_2(mathbf Z)) with

[
UGV=operatorname{diag}(12,12)
]

provides an additional audit trail.

## 6. Status

**COMPUTATIONALLY VERIFIED — explicit arithmetic calculation for the specified lattice.**

## 7. Explicit Scope Limitation

The SNF and discriminant group belong to the specified lattice. They do not, by themselves, prove that the lattice is the complete algebraic-cycle lattice, establish a universal torsion obstruction, or prove the Hodge Conjecture.

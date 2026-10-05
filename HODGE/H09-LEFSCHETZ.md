# H09 — Lefschetz Operators

**Status:** STANDARD THEOREM + OPEN MODEL-SPECIFIC COMPATIBILITY

## 1. Objective

H09 records the Lefschetz operator attached to a polarization and identifies the exact point where the standard Hard Lefschetz theorem ends and the present Q(i)/Weil-lattice investigation begins.

The goal is to connect the polarization class, cup-product action, primitive decomposition, and the explicit Weil/CM structures used in H03–H08 without asserting an unverified global compatibility theorem.

## 2. Standard Lefschetz operator

Let (X) be a smooth projective complex variety of dimension (d), and let (	hetain H^2(X,mathbf{Q})) be the first Chern class of an ample line bundle.

Define
[
L_	heta(alpha)=	hetacupalpha,
qquad
L_	heta:H^k(X,mathbf{Q})	o H^{k+2}(X,mathbf{Q}).
]

The Hard Lefschetz theorem states that, for (0le kle d),
[
L_	heta^{,d-k}:H^k(X,mathbf{Q})
overset{sim}{longrightarrow}
H^{2d-k}(X,mathbf{Q}).
]

This is a standard theorem of projective Hodge theory, not a new claim of this certificate.

## 3. Primitive decomposition

For (kle d), define the primitive subspace
[
P^k(X,mathbf{Q})
=
ker!left(
L_	heta^{,d-k+1}:
H^k(X,mathbf{Q})
	o
H^{2d-k+2}(X,mathbf{Q})
ight).
]

The Lefschetz decomposition is
[
H^k(X,mathbf{Q})
=
igoplus_{jge0}
L_	heta^j P^{k-2j}(X,mathbf{Q}).
]

Thus H09 supplies the formal operator/decomposition framework needed to study how the selected Hodge/Weil classes sit inside the full cohomology.

## 4. Interaction with the explicit Weil/CM model

For the decomposable model (A=J	imes J) used in H03–H05, the public record contains explicit Q(i)-Weil classes and explicit endomorphism actions.

The required model-specific calculation is to choose and document the actual polarization class (	heta), then compute its cup-product action on the relevant Künneth components and on the selected Weil subspace.

In particular, the following compatibility questions remain open in the present public record:

- the exact coordinate expression of (	heta) in the chosen (omega_1,omega_2,omega_sigma) basis;
- the explicit matrix of (L_	heta) on the selected integral/rational bases;
- preservation or transformation of the (W_K) subspace under the Lefschetz operator;
- commutation/intertwining relations between (L_	heta) and the explicit Q(i) endomorphism action;
- compatibility of these maps with the integral lattice and its saturation.

No such matrix or commutation relation is asserted here without an explicit basis-level calculation.

## 5. Relation to H06–H08

H06 fixes the arithmetic checkpoint
[
G=
egin{pmatrix}
36&12\
12&0
end{pmatrix},
qquad
det G=-144,
qquad
operatorname{SNF}(G)=operatorname{diag}(12,12),
]
with discriminant group
[
L^*/Lcong(mathbf Z/12mathbf Z)^2.
]

H07 records the index-2 extension and separates that calculation from the still-open ambient saturation problem.

H08 records the standard Künneth decomposition together with the selected arithmetic component, while explicitly leaving its complete integral/CM embedding and projector compatibility open.

H09 does not modify those arithmetic invariants. It asks whether the Lefschetz operator associated with the actual polarization can be represented compatibly on those same components.

## 6. What is established vs. open

### Established

- The Lefschetz operator is cup-product with an ample class.
- Hard Lefschetz and the primitive/Lefschetz decomposition are standard theorems for smooth projective varieties.
- The selected H06 lattice invariants remain unchanged.
- The H08 Künneth structure provides the relevant cohomological framework.

### Open in this research record

- explicit polarization coordinates for the present Q(i) model;
- explicit Lefschetz matrices on the selected bases;
- basis-level commutation/intertwining with the Q(i) Weil endomorphism action;
- integral-lattice compatibility;
- ambient saturation compatibility;
- any deduction from these ingredients to a general Hodge/Weil realization theorem.

Therefore H09 is **not** a proof of a new Lefschetz theorem and does **not** establish the Hodge Conjecture.

## 7. Next verification target

A reproducible H09 completion should provide:

1. an explicit polarization class (	heta);
2. an ordered cohomology basis;
3. the cup-product table needed to compute (L_	heta);
4. the resulting rational and integral matrices;
5. the primitive kernels and Lefschetz decomposition;
6. the explicit Q(i) endomorphism matrices in the same basis;
7. a direct matrix test for the claimed commutation/intertwining relation.

Until those data are supplied, the correct status is:

**H09 — STANDARD LEFSCHETZ THEORY ESTABLISHED; MODEL-SPECIFIC CM/LATTICE COMPATIBILITY OPEN.**

### Source note

The standard Hard Lefschetz formulation used here is the classical statement that cup-product with the first Chern class of an ample line bundle gives the Lefschetz isomorphisms and primitive decomposition. The present certificate deliberately separates that theorem from the unresolved basis-level compatibility questions of this research program.

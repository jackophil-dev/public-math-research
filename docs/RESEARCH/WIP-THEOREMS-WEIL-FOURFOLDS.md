# Working Document: Potential Theorems & Conjectures in Progress

**Repository:** `public-math-research`  
**Author / Researcher:** Philippe Beauchamp (ORCID: `0009-0003-7407-394X`)  
**Status:** In Progress / Experimental Verification  
**Scope:** Weil-Type Abelian Fourfolds, Smith Normal Form Torsion, and Künneth Block Structures

---

## 1. Purpose of this Document

This document collects formal mathematical statements, potential theorems, and working hypotheses derived from computational experiments and structural analysis of middle-dimensional integral lattices on abelian fourfolds.

Unlike finalized certificates, these entries represent ongoing research targets subject to algorithmic validation and peer/community scrutiny. They are **not established theorems unless explicitly marked as such elsewhere**.

The document intentionally separates general algebraic facts from conjectural or incomplete geometric claims.

---

## 2. Working Theorem 1: Smith Normal Form and Discriminant Data

### Statement

Let (Lambda) be a rank-(k) integral lattice with Gram matrix (G) in an integral basis. If the Smith normal form is

$$
operatorname{SNF}(G)=operatorname{diag}(d_1,ldots,d_k),
qquad d_imid d_{i+1},
$$

then the cokernel is

$$
operatorname{coker}(G)cong
igoplus_{i=1}^{k}mathbf Z/d_imathbf Z.
$$

When (G) is non-singular, this cokernel is canonically identified, after choosing the Gram realization, with the discriminant group

$$
Lambda^*/Lambda.
$$

Hence

$$
|Lambda^*/Lambda|=|det G|
=prod_i d_i.
$$

### Important qualification

The existence of non-trivial invariant factors (d_i>1) records non-unimodularity of the **specified lattice**. It does **not by itself** prove that rational Hodge classes fail to be algebraic, nor does it establish a geometric obstruction to primitive embedding in every ambient lattice.

Any claimed obstruction must additionally specify the ambient lattice, the embedding, the pairing, and the relevant saturation/denominator conditions.

### Status

- [x] Explicit SNF computation for the recorded rank-two examples.
- [x] Discriminant-group interpretation for the specified non-singular Gram matrices.
- [ ] General geometric obstruction theorem for arbitrary Weil-type fourfolds.

---

## 3. Working Lemma 2: Künneth / CM Block Couplings

### Status: Working Hypothesis — Not Established

Let (A) be an abelian fourfold of Weil type with complex multiplication by an imaginary quadratic field (K).

The Künneth decomposition provides a grading of cohomological tensor factors, while the CM action supplies additional structure. In a chosen integral basis, these structures can produce block matrices whose off-diagonal terms encode pairings between the selected subspaces.

The working question is whether the relevant spectral or CM-adapted projectors are orthogonal for the **specific intersection pairing and basis under consideration**.

A potential mixed term has the form

$$
leftlangle pi_i(x),pi_j(y)ightangle
eq 0,
qquad i
eq j.
$$

If such terms occur, the resulting Gram matrix need not be block diagonal in that chosen decomposition.

### Critical distinction

Non-orthogonality of a chosen decomposition is **not automatic** merely because CM acts on the cohomology. Likewise, the Hodge decomposition and the integral Künneth decomposition should not be conflated.

The claim therefore remains a computational/structural hypothesis until an explicit pairing calculation establishes the relevant off-diagonal terms.

### Verification target

For a concrete Weil-type fourfold:

1. specify the integral basis;
2. specify the Künneth decomposition;
3. write the CM action;
4. define the projectors being used;
5. compute the intersection matrix;
6. isolate the off-diagonal blocks;
7. determine whether they vanish identically or only after a basis change.

---

## 4. Saturation and SNF Checkpoint

For a sublattice (Lsubseteq L_{mathrm{amb}}), define

$$
operatorname{Sat}_{L_{mathrm{amb}}}(L)
=
(Lotimesmathbf Q)cap L_{mathrm{amb}}.
$$

The inclusion is saturated precisely when

$$
operatorname{Sat}_{L_{mathrm{amb}}}(L)=L.
$$

An index-two extension such as

$$
R=rac{P+Q}{2}
$$

is a concrete arithmetic operation that may enlarge a generated lattice, but it is not by itself a proof of full ambient saturation.

The previously recorded candidate checkpoint

$$
det(G_{mathrm{sat}})=-144,
qquad
A_{mathrm{sat}}cong(mathbf Z/12mathbf Z)^2
$$

should therefore be treated as data attached to the specified candidate lattice until the ambient embedding is fully documented.

---

## 5. Computational Targets

1. Cross-reference the discriminant groups with the relevant lattice-theoretic literature.
2. Automate saturation checks for explicitly specified ambient lattices.
3. Compute the Künneth/CM block intersection matrices for concrete examples.
4. Test whether apparent mixed blocks disappear under an explicitly recorded integral basis change.
5. Separate invariant statements from coordinate-dependent matrix phenomena.
6. Record every computational certificate independently from any geometric conjecture.

---

## 6. Research Status

This file is a **WIP research document**.

The calculations and certificates elsewhere in the repository should be read according to their individual status. Nothing in this document is intended to constitute a proof of the Hodge conjecture, a general theorem about algebraicity of Hodge classes, or a complete classification of Weil-type abelian fourfolds.

---

**Researcher:** Philippe Beauchamp  
**ORCID:** `0009-0003-7407-394X`

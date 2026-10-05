# H07 — Saturation and Index-2 Extension

**Author / Researcher:** Philippe Beauchamp  
**ORCID:** [0009-0003-7407-394X](https://orcid.org/0009-0003-7407-394X)

> **Status:** VERIFIED CHECKPOINT + OPEN AMBIENT SATURATION
>
> This record isolates the explicit index-2 lattice extension and the associated discriminant checkpoint. It does **not** claim that the resulting candidate lattice is the full geometric lattice of algebraic cycles.

## 1. Objective

The purpose of H07 is to place the saturation calculation into the Hodge research ledger as a precisely scoped arithmetic step.

The relevant chain is

$$
L_0
\longrightarrow
L_1
\longrightarrow
\operatorname{Sat}_{L_{\mathrm{amb}}}(L_1)
\longrightarrow
\text{geometric realization}.
$$

The first arrow is explicit. The later identification with an ambient geometric cycle lattice remains open.

## 2. Explicit index-2 extension

Start with

$$
L_0=\mathbf ZP\oplus\mathbf ZQ.
$$

Adjoin

$$
R=\frac{P+Q}{2}.
$$

Then

$$
2R=P+Q\in L_0,
$$

while, when $P+Q$ is not divisible by $2$ in $L_0$,

$$
R\notin L_0.
$$

Therefore

$$
L_1=L_0+\mathbf ZR,
$$

satisfies

$$
L_1/L_0\cong\mathbf Z/2\mathbf Z,
\qquad
[L_1:L_0]=2.
$$

This is the concrete arithmetic extension recorded in the underlying saturation certificate.

## 3. Smith-normal-form checkpoint

Relative to the original ordered generators $(P,Q)$,

$$
R=\frac12P+\frac12Q.
$$

After choosing an integral basis adapted to the finite-index extension, the corresponding elementary-divisor checkpoint is

$$
\operatorname{SNF}=\operatorname{diag}(1,2).
$$

This records one nontrivial elementary divisor of order $2$.

It is important to distinguish this from the SNF of a Gram matrix. The former records the finite-index extension; the latter records arithmetic information about a bilinear form.

## 4. Candidate saturated discriminant data

The recorded candidate saturated rank-two lattice has Gram determinant

$$
\det(G_{\mathrm{sat}})=-144.
$$

Hence

$$
|\det(G_{\mathrm{sat}})|=144.
$$

For the specified rank-two model, the associated abstract discriminant group is

$$
A_{\mathrm{sat}}
\cong
\mathbf Z/12\mathbf Z\oplus\mathbf Z/12\mathbf Z.
$$

These are arithmetic properties of the specified candidate lattice.

They do **not** by themselves establish that this candidate equals the complete lattice of algebraic Hodge cycles.

## 5. Precise meaning of saturation

For an explicitly specified ambient integral lattice $L_{\mathrm{amb}}$ containing a rational subspace,

$$
\operatorname{Sat}_{L_{\mathrm{amb}}}(L)
=
(L\otimes\mathbf Q)\cap L_{\mathrm{amb}}.
$$

The inclusion is saturated precisely when

$$
\operatorname{Sat}_{L_{\mathrm{amb}}}(L)=L.
$$

Consequently, the index-2 extension is a concrete saturation **step**, not automatically a proof of full saturation.

A complete proof requires:

1. an explicit ambient integral lattice;
2. the embedding of the generated lattice into that ambient lattice;
3. determination of the saturation quotient;
4. verification that no further finite-index enlargement exists.

## 6. What H07 establishes

### Established / recorded

- Explicit extension:
  $$
  R=\frac{P+Q}{2}.
  $$
- Extension index:
  $$
  [L_1:L_0]=2.
  $$
- Extension SNF checkpoint:
  $$
  \operatorname{diag}(1,2).
  $$
- Candidate saturated determinant:
  $$
  -144.
  $$
- Candidate discriminant group:
  $$
  (\mathbf Z/12\mathbf Z)^2.
  $$

### Still open

- Full saturation inside the intended ambient cohomology lattice.
- Identification of the candidate lattice with the complete geometric algebraic-cycle lattice.
- Any general Hodge/Weil realization theorem.

## 7. Relation to H06

H06 records the Gram-matrix arithmetic

$$
\operatorname{SNF}(G)=\operatorname{diag}(12,12),
$$

with discriminant group

$$
L^*/L\cong(\mathbf Z/12\mathbf Z)^2.
$$

H07 records a different layer:

$$
\text{generated lattice}
\rightarrow
\text{index-2 extension}
\rightarrow
\text{saturation checkpoint}
\rightarrow
\text{candidate discriminant}.
$$

Thus H06 and H07 are complementary rather than redundant.

## 8. Research status

**Index-2 extension:** explicit arithmetic construction.  
**Extension SNF:** recorded checkpoint.  
**Candidate determinant:** $-144$.  
**Candidate discriminant:** $(\mathbf Z/12\mathbf Z)^2$.  
**Full ambient saturation:** OPEN.  
**Geometric cycle-lattice identification:** OPEN.  
**General Hodge realization:** NOT ESTABLISHED.

---

**Source record:** [CERTIFICATE-SATURATION-INDEX-2.md](../docs/RESEARCH/CERTIFICATE-SATURATION-INDEX-2.md)  
**Researcher:** Philippe Beauchamp  
**ORCID:** [0009-0003-7407-394X](https://orcid.org/0009-0003-7407-394X)

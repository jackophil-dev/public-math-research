# FOUNDATIONAL THEOREMS 01–04: CORE ARCHITECTURAL PRINCIPLES

**Track:** HODGE  
**Status:** ESTABLISHED FRAMEWORK & CONDITIONAL PROPOSITIONS  
**Scope:** Defines the four primary theoretical pillars governing the Weil-type abelian fourfold lattice and cycle architecture, complete with explicit proof basis and boundary limitations.

---

## Theorem 1: Base Cycle Class Mapping and Primitive Decomposition

* **Statement:** Let $X$ be a Weil-type abelian fourfold over an imaginary quadratic CM-field $K = \mathbb{Q}(i)$. The algebraic cycle class map induces a well-defined, functorial homomorphism from algebraic cycles to middle-dimensional Betti and Deligne-Beilinson cohomology spaces, admitting an orthogonal primitive decomposition under the algebraic Lefschetz action.
* **Status:** PROVED FOR EXPLICIT SUB-MODULES / STANDARD THEORY
* **Scope Definition:** Establishes the structural domain for Certificates H01 through H03.

### Explanation & Proof Basis

1. **Mathematical Meaning:** Establishes the baseline map from algebraic cycles into cohomology, ensuring that cycle classes respect Hodge weight filtrations and split under the Hard Lefschetz primitive decomposition.
2. **Establishing Basis:** Grounded in standard algebraic cycle theory and the Hodge decomposition for smooth projective complex varieties and abelian varieties.
3. **Link to H-Certificates:** Directly implemented in **H01** (Base Cohomology), **H02** (Intersection Matrix), and **H03** (Q(i) CM Calibration).
4. **Remaining Open Limitations:** This standard structural input does not establish surjectivity onto all Hodge classes and does not itself resolve the Hodge Conjecture.

---

## Theorem 2: CM-Calibration and Rosati Polarization Invariance

* **Statement:** The complex multiplication structure induced by $K = \mathbb{Q}(i)$ provides explicit eigenspace structure on the relevant cohomology, while the associated polarization is required to satisfy the corresponding Rosati involution invariants.
* **Status:** DERIVED FOR THE EXPLICIT TARGET MODEL / ROSATI VERIFICATION OPEN
* **Scope Definition:** Governs the calibration parameters utilized in Certificates H03, H04, and H11.

### Explanation & Proof Basis

1. **Mathematical Meaning:** The $K = \mathbb{Q}(i)$ action supplies explicit rational/eigen-component structure, giving the Weil-type subspace its CM symmetry. The Rosati involution supplies the compatibility condition between the polarization and the CM action.
2. **Establishing Basis:** The explicit CM representation and Weil-space calculations are recorded in **H03** and **H11**. The polarization/Rosati component is a structural target rather than a completed global verification.
3. **Link to H-Certificates:** Addressed in **H03** (CM Calibration), **H04** (Weil Polarization), and **H11** (Invariant Subspace).
4. **Remaining Open Limitations:** **The complete model-specific Rosati/polarization verification remains OPEN**, as recorded in H04. No universal Rosati positivity theorem is claimed here.

---

## Theorem 3: Intersection Matrix Realization and SNF Torsion Bounds

* **Statement:** The cup product pairing on the specified rank-two lattice $L$ yields an explicit Gram matrix $G$ with determinant $\det G = -144$. The inclusion of $L$ into its dual $L^*$ is governed by the Smith normal form $\operatorname{SNF}(G) = \operatorname{diag}(12, 12)$, producing the exact discriminant group structure $L^*/L \cong (\mathbb{Z}/12)^2$ for this specified lattice.

* **Status:** COMPUTATIONALLY VERIFIED & PROVED FOR EXPLICIT LATTICE
* **Scope Definition:** Serves as the immutable arithmetic anchor for Certificates H05, H06, and H10.

### Explanation & Proof Basis

1. **Mathematical Meaning:** For the explicit Gram matrix
   $$G = \begin{pmatrix} 36 & 12 \\ 12 & 0 \end{pmatrix},$$
   direct calculation gives $\det G = -144$. Its Smith normal form is $\operatorname{diag}(12,12)$, hence
   $$L^*/L \simeq (\mathbb{Z}/12\mathbb{Z})^2.$$
2. **Establishing Basis:** This follows from exact integer matrix arithmetic and elementary divisor theory for the specified non-degenerate lattice.
3. **Link to H-Certificates:** Explicitly detailed in **H05** (Hodge Cycle Lattices), **H06** (SNF Torsion), and **H10** (Discriminant Obstruction).
4. **Remaining Open Limitations:** **This proves the arithmetic statement for the specified lattice model; it does not prove that this lattice is the complete or exhaustive geometric algebraic-cycle lattice of the ambient variety.**

---

## Theorem 4: Discriminant Obstruction and Candidate Saturation Bound

* **Statement:** The selected lattice admits a calculated index-2 extension $R = (P+Q)/2$, with candidate determinant $-144$ and candidate discriminant group $A_{\mathrm{sat}} \cong (\mathbb{Z}/12)^2$. These data define a rigorous realization test, while a geometric obstruction still requires comparison with the explicitly identified ambient integral lattice, its saturation, and the relevant discriminant form.
* **Status:** VERIFIED CHECKPOINT / CONDITIONAL OBSTRUCTION TARGET
* **Scope Definition:** Governs the arithmetic-to-geometry transition across Certificates H07, H10, and H12.

### Explanation & Proof Basis

1. **Mathematical Meaning:** The extension $R=(P+Q)/2$ gives an explicit index-2 enlargement of the selected lattice. The associated discriminant data provide arithmetic diagnostics for testing a later geometric realization.
2. **Establishing Basis:** Direct lattice-extension arithmetic, index computation, and discriminant/SNF analysis.
3. **Link to H-Certificates:** Implemented in **H07** (Saturation), **H10** (Discriminant Obstruction), and synthesized in **H12** (Realization Synthesis).
4. **Remaining Open Limitations:** The calculated index-2 extension is **not by itself a proof of full geometric saturation**, and the discriminant data are **not by themselves a universal obstruction theorem**. Full ambient-lattice identification, saturation, and discriminant-form comparison remain open.

---

**Architectural Note:** These four theorems govern the formal boundaries of the explicit model. They provide the logical foundation for Certificates H01–H12 without asserting a universal resolution of the general Hodge Conjecture.

**Scientific boundary:** The statuses above apply to the explicitly specified model and/or standard structural theory. They do not establish a universal theorem for all Weil-type abelian fourfolds or all rational Hodge classes.

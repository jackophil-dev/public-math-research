# Start Here — Recruiters and Mathematical Researchers

**Author:** Philippe Beauchamp  
**ORCID:** [0009-0003-7407-394X](https://orcid.org/0009-0003-7407-394X)  
**Repository:** [jackophil-dev/public-math-research](https://github.com/jackophil-dev/public-math-research)

This guide is an additional navigation and reproducibility entry point. It supplements the existing README and research documents; it does not replace them. Existing files and research tracks are retained.

## What this repository contains

The repository brings together mathematical research notes, exact arithmetic calculations, computational checks, certificate registers, theorem statements, and explicitly identified open research questions. It is not a claim that every research program is complete or that an open Millennium Prize problem has been solved.

## Browse the research tracks

- [HODGE — Weil-type abelian fourfolds and lattice invariants](https://github.com/jackophil-dev/public-math-research/tree/main/HODGE)  
  Research record and certificates; the open geometric-realization boundary remains explicit. [Zenodo record](https://doi.org/10.5281/zenodo.23117845)

- [P/PN — exterior arithmetic and geometric identification gate](https://github.com/jackophil-dev/public-math-research/tree/main/P-PN)  
  The arithmetic block is distinguished from the open geometric identification. [Zenodo record](https://doi.org/10.5281/zenodo.23196136)

- [Navier–Stokes](https://github.com/jackophil-dev/public-math-research/tree/main/NAVIER-STOKES)  
  Structural identities and certificates; no completed proof of global regularity or finite-time singularity construction is claimed. [Zenodo record](https://doi.org/10.5281/zenodo.23248842)

- [BSD — Birch and Swinnerton-Dyer, Part I](https://github.com/jackophil-dev/public-math-research/tree/main/Birch%20and%20Swinnerton)  
  Research-in-progress framework, certificate and theorem registers, and open obligations. The general BSD conjecture is not claimed as proved. [Zenodo record](https://doi.org/10.5281/zenodo.23304606)

- [Replicator Engine & System Control Architecture](https://github.com/jackophil-dev/public-math-research/tree/main/REPLICATOR)  
  A formal control and verification architecture with conditional statements and specifications; physical implementation is not established by the documents. [Selected Zenodo record](https://doi.org/10.5281/zenodo.23204583)

- [Fabricator / Duplicator Technologies](https://github.com/jackophil-dev/public-math-research/tree/main/Fabricator/duplicator-technologies)  
  A separate exploratory material-reconstruction framework. It is not the same project as Replicator, and it is not presented as a demonstrated machine.

- [Measurements of Paradoxes](https://github.com/jackophil-dev/public-math-research/tree/main/Measurements%20of%20Paradoxes)  
  A separate research track with its own certificate and theorem folders.

- [SINGULARITY-POWER-CORE](https://github.com/jackophil-dev/public-math-research/tree/main/SINGULARITY-POWER-CORE)  
  Existing repository material retained as its own directory.

- [CERTIFICATES](https://github.com/jackophil-dev/public-math-research/tree/main/CERTIFICATES) · [docs](https://github.com/jackophil-dev/public-math-research/tree/main/docs) · [lattice arithmetic calculations](https://github.com/jackophil-dev/public-math-research/blob/main/lattice_arithmetic_calculations.md)

## Reproduce the existing lattice-check example

The repository already contains [scripts/validate_lattice.py](https://github.com/jackophil-dev/public-math-research/blob/main/scripts/validate_lattice.py). Its sample checks the Smith normal form of the matrix
\[
\begin{pmatrix}12&0\\0&12\end{pmatrix}
\]
and a finite-index calculation.

### Tested environment

The script was run successfully in a separate environment using **Python 3.13.5** and **SymPy 1.14.0**. The run printed the invariant factors `[12, 12]`, determinant `144`, and `All checks passed.` This is a runtime check of the script's sample assertions, not an independent proof of the broader research claims.

For a compatible modern Python installation, install the tested SymPy version and run the script from the repository root:

```bash
python -m pip install sympy==1.14.0
python scripts/validate_lattice.py
```

The tested configuration is not a claim of compatibility with every Python version or operating system. In particular, compatibility with legacy systems such as Windows 7 has not been tested. This guide does not ask the user to upgrade or change their existing machine.

### What the script does — and does not — verify

- It computes Smith normal form invariant factors and the determinant for its supplied integer matrix.
- It checks a sample determinant-ratio index calculation.
- It does **not** establish geometric saturation without a specified ambient lattice and embedding.
- The sample matrix is a regression example, not a substitute for independently checking every research certificate.

## Research integrity and citation

The repository distinguishes **PROVED**, **DERIVED**, **COMPUTATIONALLY VERIFIED**, **OPEN**, and conditional/specification-level claims where appropriate. A successful script run supports only the assertions actually tested by that script.

- [Repository README](https://github.com/jackophil-dev/public-math-research/blob/main/README.md)
- [Public research status](https://github.com/jackophil-dev/public-math-research/blob/main/PUBLIC-RESEARCH-STATUS.md)
- [Citation metadata](https://github.com/jackophil-dev/public-math-research/blob/main/CITATION.cff)
- [License](https://github.com/jackophil-dev/public-math-research/blob/main/LICENSE)
- [Contact and collaboration information](https://github.com/jackophil-dev/public-math-research/blob/main/CONTACT.md)

Use the versioned Zenodo records and their file manifests for canonical publication versions. GitHub folders are browsable research companions and should not automatically be assumed to be byte-for-byte mirrors of every deposit.

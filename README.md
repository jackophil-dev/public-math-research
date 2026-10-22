# Public Math Research & Verification Framework

**Researcher:** Philippe Beauchamp ([ORCID: 0009-0003-7407-394X](https://orcid.org/0009-0003-7407-394X))  
**Repository:** [jackophil-dev/public-math-research](https://github.com/jackophil-dev/public-math-research)  
**Status:** Active Independent Research  
**License:** CC BY 4.0

---

## Overview

This repository contains public mathematical research notes, explicit calculations, computational certificates, theorem targets, and verification frameworks developed by Philippe Beauchamp as an independent researcher.

The public record is organized around several distinct research tracks:

1. **Hodge / Weil-Type Abelian Fourfolds & Lattices** — cohomological structures, intersection forms, discriminant groups, Smith Normal Form (SNF), saturation, K = Q(i) calibration, and related realization questions.
2. **P / PN Research** — public verification targets and theorem/certificate structure, with unresolved geometric links explicitly marked rather than reconstructed.
3. **Navier–Stokes** — exact vorticity and enstrophy identities, local balance laws, computational certificates, and the boundary between established identities and the open global regularity problem.
4. **Fabricator / Duplicator Technologies** — formal state-space, resource-bounding, feedback, invariant-preservation, and safety-gated verification architecture.

The repository is intentionally public and inspectable. Private supporting calculations and unresolved connecting steps are not reproduced here unless explicitly designated as public.

---

## Repository Structure

- [HODGE/](HODGE/) — Hodge / Weil fourfold research sequence and core theorem targets.
- [P-PN/](P-PN/) — P / PN public certificates and theorem structure.
- [NAVIER-STOKES/](NAVIER-STOKES/) — Navier–Stokes identities, certificates, and regularity boundary.
- [Fabricator/](Fabricator/) — formal Fabricator / duplicator-system architecture, theorems, certificates, and status.
- [CERTIFICATES/](CERTIFICATES/) — existing public certificate material retained for reference.
- [docs/](docs/) — research navigation and supporting public documentation.
- [PUBLIC-RESEARCH-STATUS.md](PUBLIC-RESEARCH-STATUS.md) — current public research status.
- [scripts/](scripts/) — public computational/support scripts where applicable.

---

## Calculation vs. Geometric Realization

A central methodological distinction in this repository is the difference between **exact arithmetic calculation** and **geometric realization**.

Smith Normal Form computations, determinants, Gram matrices, discriminant groups, and related lattice invariants are exact consequences of the stated integer or rational matrices. For example, a computation yielding a group such as Z/12Z is an arithmetic statement about the presented lattice/module data.

That calculation does **not**, by itself, prove that the computed arithmetic lattice is the geometric lattice of algebraic cycles, nor does it prove a geometric realization or identification with an ambient cohomological module.

Where an identification, saturation boundary, inclusion map, or geometric realization remains unresolved, the repository marks it explicitly rather than inferring it from matching numerical invariants.

In particular:

- **Gram-matrix invariants** and their SNF control arithmetic lattice/discriminant information.
- **Inclusion or transition matrices** describe actual module inclusions and their cokernels.
- These are distinct objects and must not be conflated.
- A numerical discriminant match is not, by itself, a proof of geometric realization.

---

## Epistemic Status

Public results use explicit status language where appropriate:

- **PROVED** — established from the stated hypotheses.
- **DERIVED** — obtained by a documented mathematical derivation, with its hypotheses stated.
- **COMPUTATIONALLY VERIFIED** — checked by explicit computation from the stated data.
- **OPEN** — an unresolved mathematical question or boundary.

The repository does not present an open geometric identification or an unresolved global regularity problem as solved.

---

## Published Research Tracks

- [HODGE/](HODGE/) — Weil-type abelian fourfolds and H01–H12 certificates. [Zenodo DOI](https://doi.org/10.5281/zenodo.23117845)
- [P-PN/](P-PN/) — exterior arithmetic, primitive bivectors, lattice invariants, and open geometric-identification gate. [Zenodo DOI](https://doi.org/10.5281/zenodo.23196136)
- [REPLICATOR/](REPLICATOR/) — Replicator Engine & System Control Architecture, v0.50-RC1 milestone, certificates and conditional theorem statements. [Zenodo DOI](https://doi.org/10.5281/zenodo.23204583)
- [NAVIER-STOKES/](NAVIER-STOKES/) — Part I structural identities and open global-regularity boundary. [DOI listed in ORCID](https://doi.org/10.5281/zenodo.23248842)
- [Birch and Swinnerton/](Birch%20and%20Swinnerton/) — BSD Part I framework, certificate/theorem registers, and open problems. [Zenodo DOI](https://doi.org/10.5281/zenodo.23304606)

The GitHub research files are intended to be browsable companions. A GitHub folder is not automatically a byte-for-byte mirror of a Zenodo deposit; use each publication record and the Zenodo file manifest to determine which versioned files are canonical. The Replicator DOI above is the selected citation target for one milestone; the author reports additional same-license records were accidentally created for the same work and should not be treated as separate research outputs.

## Citation

For citation metadata, see [CITATION.cff](CITATION.cff).

The research is also archived through Zenodo where indicated in the research materials.

---

## Independent Research and Verification Approach

This is an independent research program spanning several distinct areas of mathematics and system architecture. Each track retains its own scope, assumptions, evidence, and unresolved questions.

The work combines mathematical derivations, exact arithmetic, computational checks, structured research records, and explicit verification boundaries. Public claims are classified according to what the available evidence supports:

- **PROVED** — established from stated hypotheses by a mathematical argument.
- **DERIVED** — obtained through a documented derivation, with its assumptions made explicit.
- **COMPUTATIONALLY VERIFIED** — checked by computation from the stated inputs; this status alone does not imply a general mathematical proof.
- **OPEN** — an unresolved question, missing implication, or boundary that has not been established.

A numerical match or successful computation is not, by itself, proof of geometric realization, a general theorem, or resolution of an open problem. Where a required step remains unresolved, the public record should say so rather than infer a conclusion.

AI tools may assist with exploration, organization, symbolic computation, checking, and technical writing. Their outputs are not automatically verified results. Mathematical claims are intended to remain independently inspectable against the stated assumptions, calculations, and public evidence. Responsibility for the research record and the interpretation of its claims remains with the independent researcher, Philippe Beauchamp.

Only material intended for public inspection is included here. Private implementation details and unresolved supporting material are not included merely to make a public presentation appear more complete.

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

## Citation

For citation metadata, see [CITATION.cff](CITATION.cff).

The research is also archived through Zenodo where indicated in the research materials.

---

## Independent Research

This is independent mathematical research. AI tools may assist with organization, symbolic computation, checking, or research workflow, but mathematical claims are intended to remain independently inspectable and verifiable from the public record.

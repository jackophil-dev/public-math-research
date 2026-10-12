# Navier–Stokes — Computational Verification

A reproducible numerical record should state the domain, boundary conditions, viscosity, initial data, discretization, time integrator, resolution, stability/CFL limits, solver tolerances, and convergence checks.

For sampled fields, check discrete divergence, energy/enstrophy balances, vorticity definition, and sensitivity to mesh/time-step refinement. Report discretization residuals and numerical uncertainty; finite-resolution simulation is not proof of a continuum theorem.

The enstrophy identity in this folder is derived analytically under smoothness and boundary assumptions. This file does not claim a new numerical run or validate a project-specific SPN identity. Link existing certificate outputs and source fields/matrices for each computational claim.
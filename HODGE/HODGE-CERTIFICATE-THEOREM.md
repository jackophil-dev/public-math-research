# HODGE — Certificate + Governing Theorem

**Research-ID:** HODGE  
**Author:** Philippe Beauchamp  
**AI assistance:** ChatGPT  
**Status:** Public research track; explicit/model-specific results only. This document does not claim a general proof of the Hodge Conjecture.

## Governing research framework

The current program uses:

geometry → measurement/signature → invariant → reconstruction

with the extended signature chain:

S–N–P–I–T.

The explicit Q(i) / J×J calculations below are model-specific. The general Hodge Conjecture remains unproved by this research package.

---

## Certificate 05 — Normalisation locale et séparation du point double

### Governing statement

For the Bernoulli lemniscate
\[
F(x,y)=(x^2+y^2)^2-c^2(x^2-y^2)=0,
\]
the quadratic part at the double point determines the tangent directions
\[
y=x,\qquad y=-x.
\]

### Verification

A local normalization separates the two local branch directions/preimages at the level of tangent directions.

### Result

\[
\boxed{y=x,\quad y=-x}.
\]

### Limitation

This certificate does not by itself establish a global resolution of a general algebraic-geometric problem.

---

## Certificate 06 — Intégrale de la 1-forme sur le lobe orienté

### Governing statement

For
\[
F=(x^2+y^2)^2-c^2(x^2-y^2)=0
\]
and
\[
\omega=y\,dx-x\,dy,
\]
the normalized integral on the positively oriented normalized lobe is
\[
\widehat I=-1.
\]

### Result

\[
\boxed{\widehat I=-1}.
\]

The sign depends on orientation.

### Limitation

This is an exact calculation in the stated normalized model; it is not by itself a general theorem.

---

## Certificate 07 — Calibration Q(i) dans le modèle décomposable J×J

### Governing theorem statement

For the explicit decomposable model
\[
A=J\times J,\qquad K=\mathbb Q(i),
\]
the calculated Weil sector is the two-dimensional rational space
\[
\boxed{W_K=\mathbb Q\alpha_1\oplus\mathbb Q\alpha_2}.
\]

### Explicit calibration

With the corrected van Geemen mixed form,
\[
\omega_\sigma
=dx_1\wedge dy_2-dx_2\wedge dy_1
+dx_3\wedge dy_4-dx_4\wedge dy_3,
\]
and
\[
\omega_1=dx_1\wedge dx_2+dx_3\wedge dx_4,
\qquad
\omega_2=dy_1\wedge dy_2+dy_3\wedge dy_4,
\]
the working Weil generators are
\[
\alpha_1
=\omega_1^2-2\omega_1\omega_2+\omega_2^2-\omega_\sigma^2,
\]
\[
\alpha_2
=\omega_1\omega_\sigma-\omega_2\omega_\sigma.
\]

For the exceptional algebraic cycle calculation,
\[
c=\omega_1^2+6\omega_1\omega_2+\omega_2^2+\omega_\sigma^2,
\]
and with
\[
P=(\omega_1+\omega_2)^2,
\]
one obtains
\[
\boxed{\alpha_1=2P-c}.
\]

Thus \(\alpha_1\) is algebraic in this explicit decomposable model.

### Remaining calculation

For the algebraic endomorphism corresponding to \(2+i\), the working action is
\[
(2+i)^*\alpha_1=-7\alpha_1-48\alpha_2,
\]
up to the sign convention for \(\omega_+\) versus \(\omega_-\). The magnitude 48 is invariant under that convention change.

The explicit exterior-power calculation remains the required verification before treating the induced \(\alpha_2\) conclusion as final.

### Important boundary

The separate E^4 lattice calculation
\[
M_W=8I_2
\]
must not be silently identified with the J×J coordinates without an explicit coordinate transformation.

### Status

- Q(i) calibration: verified in explicit model.
- \(\alpha_1\) algebraicity: verified in explicit model.
- \(\alpha_2\) via \(2+i\): pending explicit exterior-power verification.
- Full realization lattice / SNF: open.
- General Hodge Conjecture: not established.

## Research boundary

This track records explicit calculations and model-specific consequences. It does not claim a universal Hodge resolution.

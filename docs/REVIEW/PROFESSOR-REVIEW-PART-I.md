# Professor Review — Part I

**Author:** Philippe Beauchamp  
**Research area:** Hodge theory / algebraic geometry / CM-Weil structures  
**Purpose:** concise, independently checkable review packet for an academic reader

> **PUBLIC RESEARCH — INTENTIONALLY INCOMPLETE**
>
> This packet is intentionally limited to the public mathematical record. Private certificates, private connecting constructions, and unpublished research material are not included.

## 1. Scope

Part I concerns explicit calculations in a decomposable Q(i) model and related lattice calculations. The goal of this packet is not to ask a reviewer to accept a broad conjectural claim, but to identify concrete statements that can be checked line by line.

The research is authored by Philippe Beauchamp with AI research assistance. AI assistance does not constitute independent mathematical verification.

## 2. Explicit Q(i) model

Take:

- CM field K = Q(i)
- Abelian fourfold A = J × J
- Integral H^1 lattice Lambda = H^1(A,Z) ~= Z^8
- rational Weil space W_K of dimension 2

The mixed invariant form uses the corrected van Geemen convention:

omega_sigma =
dx1∧dy2 - dx2∧dy1
+ dx3∧dy4 - dx4∧dy3.

This correction is important: earlier same-index coordinates must not be silently reused.

## 3. Weil-plane calculation

For the embedding i -> [[0,-1],[1,0]], define

omega_+ = omega_1 + i omega_sigma - omega_2.

Then

omega_+^2 = alpha_1 + 2 i alpha_2,

with

alpha_1 =
omega_1^2 - 2 omega_1 omega_2 + omega_2^2 - omega_sigma^2,

alpha_2 =
omega_1 omega_sigma - omega_2 omega_sigma.

Therefore the candidate Weil plane is

W_K = Q alpha_1 + Q alpha_2.

## 4. CM action checkpoint

For k = 2+i,

k^4 = -7 + 24i.

The derived action is recorded as

(2+i)^* alpha_1 = -7 alpha_1 - 48 alpha_2,

(2+i)^* alpha_2 = 12 alpha_1 - 7 alpha_2,

subject to the sign convention for omega_+ versus omega_-.

The magnitude 48 is invariant under that convention change.

**Review request:** independently reproduce the exterior-algebra matrix calculation and confirm the action.

## 5. Explicit algebraic cycle

Define

S_1 = 1/2(omega_1 + omega_2 - omega_sigma)^2,

S_2 = omega_1 omega_2,

S_-1 = 1/2(omega_1 + omega_2 + omega_sigma)^2,

T = 4 S_2.

The recorded exceptional algebraic cycle is

c = [T] + [S_1] + [S_-1]

and expands to

c = omega_1^2 + 6 omega_1 omega_2
    + omega_2^2 + omega_sigma^2.

With P = (omega_1 + omega_2)^2,

c = 2P - alpha_1,

hence

alpha_1 = 2(omega_1 + omega_2)^2 - c.

Within this explicit decomposable Q(i) model, this gives the recorded algebraicity of alpha_1.

## 6. Route toward alpha_2

The CM element 2+i corresponds to the integral matrix

[[2,-1],[1,2]]

and therefore to an algebraic endomorphism/isogeny in the model.

If the exterior-power calculation confirms

(2+i)^* alpha_1 = -7 alpha_1 - 48 alpha_2,

then algebraicity of alpha_1 implies algebraicity of 48 alpha_2, and therefore alpha_2 over Q.

This implication depends on independently confirming the displayed pullback calculation.

## 7. Independent lattice checkpoint

A separate explicit E^4 Q(i) lattice model gives

W_{K,Z} = Z alpha_0 ⊕ Z beta_0

with Gram matrix

M_W = 8 I_2.

This separate calibration must not be silently identified with the J × J alpha_1, alpha_2 coordinates without an explicit coordinate transformation.

## 8. What is established vs open

### Concrete checks recorded in the public file

- corrected van Geemen coordinate convention;
- dim_Q W_K = 2;
- Q(i) eigenform description;
- k^4 normalization;
- explicit exceptional algebraic-cycle expansion;
- alpha_1 algebraicity in the explicit model;
- separate E^4 lattice calibration M_W = 8 I_2.

### Still requiring independent checking

- explicit exterior-power confirmation of the 2+i action;
- reconciliation of the earlier T_1,T_2 identity with the corrected coordinate convention;
- full realization lattice and its Smith-normal-form calculation;
- any extension from this explicit decomposable model to a general Hodge-Conjecture statement.

## 9. Questions for a professor/reviewer

1. Is the corrected van Geemen coordinate convention used consistently?
2. Does the exterior-power computation give the stated 2+i pullback matrix?
3. Is the algebraic-cycle expansion correct?
4. Does the displayed implication from alpha_1 to alpha_2 follow once the pullback matrix is confirmed?
5. Are the separate J × J and E^4 lattice models being kept correctly distinct?
6. Which statement, if any, is strong enough to formulate as a standalone theorem?
7. What additional proof is required before submitting a formal paper?

## 10. Status statement

This packet is a request for independent mathematical examination of explicit calculations and their logical consequences. It does **not** claim a proof of the general Hodge Conjecture.

The public research record is intentionally incomplete; private research material is excluded.

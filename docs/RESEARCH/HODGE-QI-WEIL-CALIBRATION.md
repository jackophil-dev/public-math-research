# Hodge Research — Q(i) Weil Calibration Checkpoint

> Research note: this is a working mathematical investigation by the user, developed with AI research assistance. It is not a claimed proof of the Hodge Conjecture.

## Verified Q(i) calibration

Explicit model:
- CM field: K = Q(i)
- Abelian fourfold: decomposable J x J
- Integral H^1 lattice: Lambda = H^1(A,Z) ~= Z^8
- Hodge/CM construction gives a 2-dimensional rational Weil space W_K.

## IMPORTANT coordinate correction — van Geemen convention

The current bottom-up calculation must use van Geemen's actual convention for the mixed invariant 2-form:

omega_1 = dx1^dx2 + dx3^dx4
omega_2 = dy1^dy2 + dy3^dy4

omega_sigma = dx1^dy2 - dx2^dy1 + dx3^dy4 - dx4^dy3.

This is NOT the previously used same-index expression dx1^dy1 + dx2^dy2 + dx3^dy3 + dx4^dy4.

Therefore all coordinate calculations involving omega_sigma must be rechecked in the van Geemen basis before being declared final.

## Q(i) Weil plane

For the embedding i -> [[0,-1],[1,0]], take omega_+ = omega_1 + i omega_sigma - omega_2.

Then omega_+^2 = alpha_1 + 2 i alpha_2, where

alpha_1 = omega_1^2 - 2 omega_1 omega_2 + omega_2^2 - omega_sigma^2,

alpha_2 = omega_1 omega_sigma - omega_2 omega_sigma.

Thus W_K = Q alpha_1 + Q alpha_2.

For k=2+i, k^4=-7+24i, giving the derived action

(2+i)^* alpha_1 = -7 alpha_1 - 48 alpha_2,

(2+i)^* alpha_2 = 12 alpha_1 - 7 alpha_2,

up to the sign convention for omega_+ versus omega_-.

The magnitude 48 is invariant under that convention change. The exterior-algebra matrix computation should be used to independently confirm this action.

## Algebraic exceptional cycle

Let

S_1 = (1/2)(omega_1 + omega_2 - omega_sigma)^2,
S_2 = omega_1 omega_2,
S_{-1} = (1/2)(omega_1 + omega_2 + omega_sigma)^2,
T = 4 S_2.

The exceptional algebraic cycle c = [T] + [S_1] + [S_{-1}] expands to

c = omega_1^2 + 6 omega_1 omega_2 + omega_2^2 + omega_sigma^2.

With P=(omega_1+omega_2)^2,

c = 2P - alpha_1,

so alpha_1 = 2(omega_1+omega_2)^2 - c.

Hence alpha_1 is algebraic in this explicit decomposable Q(i) model.

## Route for alpha_2

The embedded CM element 2+i corresponds to the integral matrix [[2,-1],[1,2]], hence an algebraic endomorphism/isogeny.

If the explicit exterior-power calculation confirms

(2+i)^* alpha_1 = -7 alpha_1 - 48 alpha_2,

then algebraicity of alpha_1 implies algebraicity of 48 alpha_2, hence alpha_2 is algebraic over Q.

This is a result for the explicit decomposable Q(i) calibration, not a proof of the general Hodge Conjecture.

## Earlier mixed-correspondence identity

Previously computed matrices T_1=[[1,i],[0,1]] and T_2=[[1,0],[i,1]] gave

T_2^* alpha_1 - T_1^* alpha_1
= 5(omega_1^2 - omega_2^2) + 6 alpha_2.

This remains a consistency check, but the coordinate convention for omega_sigma must be reconciled before treating it as final.

## Integral Weil lattice

For a separate explicit E^4 Q(i) lattice model, the checked exterior-product construction gave

W_{K,Z} = Z alpha_0 direct-sum Z beta_0,

with M_W = 8 I_2.

This separate calibration model should not be silently identified with the J x J alpha_1, alpha_2 coordinates without an explicit coordinate transformation.

## Five-path framework

The user-designated signature (S,N,P,I,T) and related framework

geometry -> operator data -> invariant/signature -> reconstruction/identification -> algebraic realization/test

remain research frameworks/hypotheses, not established theorems.

## Current status

- Van Geemen coordinate convention: GREEN / source verified
- dim_Q W_K = 2: GREEN / source verified
- Q(i) eigenform description: GREEN / source verified
- k^4 normalization: GREEN / algebraically derived; explicit matrix test pending
- Exceptional algebraic cycle: GREEN / source verified
- alpha_1 algebraic: GREEN / direct algebraic consequence
- alpha_2 via k=2+i: YELLOW / explicit exterior-power calculation remains
- Earlier T_1,T_2 identity: YELLOW / coordinate reconciliation required
- Integral lattice M_W=8I_2 in separate E^4 model: GREEN / checked
- Full realization lattice / SNF: OPEN
- General Hodge-Conjecture proof: NOT established

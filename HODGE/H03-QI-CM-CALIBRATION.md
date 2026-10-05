# H03 — Q(i) CM-Field Calibration

**Researcher:** Philippe Beauchamp  
**ORCID:** 0009-0003-7407-394X  
**Track:** Hodge / Weil-type abelian fourfolds

## 1. Certificate ID

**CERT-H03 — Q(i) CM-Field Calibration**

## 2. Theorem Statement

In the explicit decomposable calibration model (A=J	imes J) with (K=mathbf Q(i)), the rational Weil sector used in the calculation is two-dimensional and is represented by

[
W_K=mathbf Qalpha_1oplusmathbf Qalpha_2.
]

## 3. Definitions / Hypotheses

The working model uses:

- (K=mathbf Q(i));
- (A=J	imes J);
- (Lambda=H^1(A,mathbf Z)simeqmathbf Z^8);
- the corrected van Geemen mixed form
[
omega_sigma=
dx_1wedge dy_2-dx_2wedge dy_1+
dx_3wedge dy_4-dx_4wedge dy_3.
]

With
[
omega_+=omega_1+iomega_sigma-omega_2,
]
the calculation gives
[
omega_+^2=alpha_1+2ialpha_2,
]
where
[
alpha_1=omega_1^2-2omega_1omega_2+omega_2^2-omega_sigma^2,
]
[
alpha_2=omega_1omega_sigma-omega_2omega_sigma.
]

## 4. Calculation / Proof

The displayed expansion places the Weil sector in the rational span of (alpha_1,alpha_2). Thus the recorded calibration is

[
W_K=mathbf Qalpha_1oplusmathbf Qalpha_2.
]

For (k=2+i),
[
k^4=-7+24i,
]
and the derived action is

[
(2+i)^*alpha_1=-7alpha_1-48alpha_2,
]
[
(2+i)^*alpha_2=12alpha_1-7alpha_2,
]

subject to the stated sign convention for (omega_+) versus (omega_-). The explicit exterior-power matrix calculation remains the independent confirmation target.

## 5. Reproducibility Checkpoint

Reproduce:

1. the corrected (omega_sigma);
2. the expansion of (omega_+^2);
3. (k^4=-7+24i);
4. the induced (2	imes2) action matrix.

## 6. Status

**DERIVED / COMPUTATIONALLY CHECKABLE — valid for the explicit decomposable Q(i) calibration.**

## 7. Explicit Scope Limitation

This establishes the stated calibration in the explicit model. It does not establish a general CM realization theorem or a proof of the Hodge Conjecture.

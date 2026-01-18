## Open Interest as a Signal

Open Interest reflects outstanding positions.

Rapid expansion in OI often indicates:

* Institutional entry
* Aggressive writing
* Position rollover
* Structural market interest

However, OI alone is not directional.

---

## OI Change Detection

The scanner computes percentage change between successive observations.

This relative approach normalizes across:

* Different instruments
* Different lot sizes
* Different liquidity regimes

---

## Expiry Classification

Expiry behavior differs significantly:

* Weekly options react violently
* Monthly options accumulate gradually
* Stock options require higher thresholds

Automatic expiry classification ensures correct interpretation.

---

## Directional Bias Logic

* Large PUT OI increase often implies support
* Large CALL OI increase often implies resistance

Bias is inferred contextually, not assumed as price prediction.

---

## Confidence Score

Confidence reflects signal quality, not expected profit.

Factors include:

* Magnitude of OI change
* Relative volume
* Stability across intervals

High confidence does not imply certainty.

---

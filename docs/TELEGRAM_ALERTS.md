## Purpose of Alerts

Alerts exist to notify humans.

They are not trade instructions.

---

## Alert Structure

Each alert contains:

* Instrument name
* Strike price
* Option type
* OI change percentage
* Directional bias
* Confidence score

This ensures clarity and auditability.

---

## Delivery Behavior

Alerts are sent via Telegram Bot API.

Failures do not crash the system but are logged.

---

## Alert Frequency

Alerts are triggered only when thresholds are crossed.

Repeated alerts for the same instrument are naturally limited by OI stabilization.

---

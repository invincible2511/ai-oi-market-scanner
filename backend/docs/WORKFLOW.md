## Runtime Flow

1. Application starts
2. Configuration validation occurs
3. Market-hour check is enforced
4. Instrument list is loaded
5. Scanner loop begins
6. OI deltas are calculated
7. Threshold rules are evaluated
8. Bias is inferred
9. Confidence is calculated
10. Telegram alert is sent if criteria match

---

## Loop Timing

The scanner runs at fixed intervals to:

* Reduce API load
* Avoid noise amplification
* Maintain consistent sampling

Intervals can be adjusted without modifying scanner logic.

---

## Shutdown Behavior

The system can be stopped safely using standard process termination.

No state persistence is required between runs.

---

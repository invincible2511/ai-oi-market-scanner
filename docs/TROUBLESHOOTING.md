## Common Issues

### Missing Environment Variables

The system will refuse to start.

This is intentional to prevent undefined behavior.

---

### Invalid Access Token

Zerodha access tokens expire daily.

A new token must be generated each trading day.

---

### No Alerts Appearing

Possible causes:

* Market conditions are stable
* Thresholds not met
* Low liquidity
* Outside market hours

This is expected behavior.

---

### API Rate Limits

Excessive polling may result in temporary blocking.

Adjust scan frequency if needed.

---

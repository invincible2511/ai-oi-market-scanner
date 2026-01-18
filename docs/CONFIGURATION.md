## Environment Variables

All sensitive information is externalized.

### Required Variables

* KITE_API_KEY
* KITE_ACCESS_TOKEN
* TELEGRAM_BOT_TOKEN
* TELEGRAM_CHAT_ID

These are loaded using python-dotenv.

---

## Why Environment-Based Configuration

Using `.env` provides:

* Credential isolation
* Safe version control
* Easy environment switching
* Compliance with security best practices

Secrets must never be committed to source control.

---

## Rule Configuration

OI thresholds are defined centrally.

Examples:

* NIFTY weekly expiry requires larger OI changes
* Monthly expiries require lower thresholds
* Stock options use higher thresholds due to lower liquidity

This reflects real market microstructure differences.

---

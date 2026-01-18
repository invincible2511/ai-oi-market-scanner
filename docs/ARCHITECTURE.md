## Architectural Philosophy

The architecture follows principles used in professional quantitative research systems:

* Separation of concerns
* Explicit data flow
* Clear ownership of responsibilities
* No hidden side effects
* Replaceable components

Each module performs exactly one role.

---

## High-Level Architecture

```
Market Data (Zerodha)
        |
        v
Broker Abstraction Layer
        |
        v
Scanner Engine
        |
        v
Inference Engine
        |
        v
Alert Delivery
```

Execution logic is intentionally excluded.

---

## Module Responsibilities

### Core

Contains configuration, constants, and logging.

* Loads environment variables
* Validates required runtime configuration
* Defines global scanner rules
* Initializes logging infrastructure

This layer has no market logic.

---

### Broker Layer

Abstracts Zerodha KiteConnect.

Responsibilities:

* API authentication
* Instrument fetching
* Quote retrieval
* LTP access

The rest of the system never directly calls KiteConnect.

This allows broker replacement in the future.

---

### Scanner Layer

Responsible for:

* Expiry classification
* Strike filtering
* OI delta computation
* Noise reduction

This layer transforms raw market data into structured observations.

---

### AI Engine Layer

Despite the name, this is not machine learning.

It performs:

* Pattern-based inference
* Weighted scoring
* Confidence estimation
* Directional interpretation

All logic is deterministic and auditable.

---

### Scheduler Layer

Controls when the system is allowed to run.

* Enforces market hours
* Prevents off-market scanning
* Reduces unnecessary API usage

---

### Alerts Layer

Responsible only for:

* Formatting messages
* Sending alerts
* Handling delivery errors

No business logic exists here.

---
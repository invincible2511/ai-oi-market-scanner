## Purpose of This Document

This document explains how to prepare the local environment required to run the AI Open Interest (OI) Scanner.
It focuses on reproducible setup steps and avoids assumptions about the developer’s machine state.

---

## System Requirements

Before proceeding, ensure the following are available:

* Operating System: Windows, Linux, or macOS
* Python version: **3.10 or higher**
* Internet connectivity during market hours
* Zerodha trading account with Kite Connect API access
* Telegram account for alert delivery

The application is designed as a backend CLI service and does not require a graphical interface.

---

## Python Environment Setup

Using an isolated Python environment is strongly recommended to avoid dependency conflicts.

### Create Virtual Environment

From the project root directory:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

## Dependency Installation

All required third-party libraries are defined in `backend/requirements.txt`.

Dependencies must be installed from inside the backend directory so that relative paths and runtime assumptions remain consistent.

Install dependencies using:

```bash
cd backend
pip install -r requirements.txt
```

This installs:

* Zerodha KiteConnect SDK
* Telegram Bot client
* Environment variable loader
* Scheduler utilities
* Logging dependencies

No additional packages should be installed manually unless extending the system.

---

## Environment Variable Configuration

All credentials and runtime parameters are externalized.

### Create Environment File

Copy the example configuration:

```bash
cp .env.example .env
```

(On Windows, create manually if required.)

### Configure Required Variables

Update `.env` with:

* Zerodha API key
* Zerodha access token (generated daily)
* Telegram bot token
* Telegram chat ID

The application will not start if any required variable is missing.

---

## Zerodha Access Token Note

Zerodha access tokens expire every trading day.

This means:

* A new token must be generated daily
* The token must be updated in `.env` before market hours
* Failure to refresh will result in authentication errors

This behavior is enforced by Zerodha and cannot be bypassed.

---

## Running the Application

From the project root:

**Windows**

```bash
run.bat
```

**Linux / macOS**

```bash
./run.sh
```

The application will:

1. Validate environment variables
2. Initialize logging
3. Connect to Zerodha APIs
4. Load instruments
5. Start scanning during market hours only

---

## Verifying Successful Startup

A successful startup will show:

* Logger initialization messages
* Broker connection confirmation
* Scheduler activation
* Scanner loop entry during market hours

If startup fails, consult the log files before modifying code.

---

## Setup Scope

This setup process prepares the system for:

* Real-time market observation
* OI anomaly detection
* Telegram alert delivery

It does **not** enable:

* Trade execution
* Strategy backtesting
* Historical data analysis

Those capabilities require separate systems.

---
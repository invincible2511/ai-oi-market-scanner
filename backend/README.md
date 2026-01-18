## Overview

This project is a command-line–based Open Interest (OI) market scanner designed for Indian derivatives markets.
It integrates with the Zerodha Kite Connect API to observe option chain behavior and identify abnormal shifts in Open Interest that may indicate institutional positioning.

The system is intentionally designed as a **scanner and alerting framework**, not a trading system.
It does not place orders, manage positions, or provide trade recommendations.

Its role is to assist in **market observation**, not execution.

---

## Purpose

The scanner exists to solve one core problem:

> Manual monitoring of option chain OI behavior is slow, inconsistent, and error-prone.

This system automates:

* Continuous option chain observation
* Detection of abnormal OI expansion
* Context-aware classification of expiry types
* Rule-based inference of directional bias
* Delivery of structured alerts for human decision-making

---

## Key Characteristics

* CLI-based backend system
* Modular and extensible architecture
* Configuration-driven behavior
* No hardcoded credentials
* No auto trading
* Market-hour–restricted execution
* Designed for research and monitoring use

---

## Intended Audience

This project is suitable for:

* Developers building market analytics systems
* Traders with basic technical literacy
* Quantitative researchers exploring derivatives data
* Future maintainers extending scanner logic

It is not designed for non-technical users.

---

## What This System Is Not

* Not a strategy engine
* Not a signal generator promising profitability
* Not an execution bot
* Not a replacement for risk management
* Not a predictive model

It is an **observational inference tool**.

---
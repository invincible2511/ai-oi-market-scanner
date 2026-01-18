
import time
from datetime import date
from app.core.config import Config
from app.core.logger import setup_logger
from app.core.constants import OI_RULES
from app.broker.zerodha_client import ZerodhaClient
from app.scanner.expiry_detector import detect_expiry_type
from app.scanner.oi_anomaly import oi_change_percent
from app.scanner.ai_engine import confidence_score
from app.alerts.telegram import TelegramAlert
from app.scheduler.market_runner import market_open

Config.validate()
logger = setup_logger()
broker = ZerodhaClient()
alert = TelegramAlert()

previous_oi = {}

def run():
    instruments = broker.instruments()
    while True:
        if not market_open():
            time.sleep(60)
            continue

        for ins in instruments:
            symbol = ins["name"]
            expiry = ins["expiry"]
            strike = ins["strike"]
            opt_type = ins["instrument_type"]

            expiry_type = detect_expiry_type(symbol, expiry)
            rule_key = f"{symbol}_{expiry_type}"
            threshold = OI_RULES.get(rule_key, OI_RULES["STOCK_MONTHLY"])

            ts = f"NFO:{ins['tradingsymbol']}"
            q = broker.quote(ts)[ts]

            oi = q.get("oi", 0)
            volume = q.get("volume", 0)

            prev = previous_oi.get(ts, oi)
            change = oi_change_percent(oi, prev)
            previous_oi[ts] = oi

            if abs(change) >= threshold:
                direction = "BULLISH" if opt_type == "PE" else "BEARISH"
                conf = confidence_score(change, volume)

                msg = f"""AI OI ALERT
Symbol: {symbol}
Strike: {strike}
Type: {opt_type}
OI Change: {round(change,2)}%
Bias: {direction}
Confidence: {conf}
"""
                alert.send(msg)
                logger.info(msg)

        time.sleep(300)

if __name__ == "__main__":
    run()

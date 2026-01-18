
from datetime import date

def detect_expiry_type(symbol, expiry):
    days = (expiry - date.today()).days
    if symbol in ["NIFTY", "BANKNIFTY"]:
        return "WEEKLY" if days <= 7 else "MONTHLY"
    return "MONTHLY"

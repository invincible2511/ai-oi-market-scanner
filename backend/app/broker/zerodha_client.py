
from kiteconnect import KiteConnect
from app.core.config import Config

class ZerodhaClient:
    def __init__(self):
        self.kite = KiteConnect(api_key=Config.KITE_API_KEY)
        self.kite.set_access_token(Config.KITE_ACCESS_TOKEN)

    def get_ltp(self, symbol):
        return self.kite.ltp(symbol)

    def instruments(self):
        return self.kite.instruments("NFO")

    def quote(self, symbol):
        return self.kite.quote(symbol)

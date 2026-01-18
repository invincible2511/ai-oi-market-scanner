
import datetime
from app.core.constants import MARKET_START, MARKET_END

def market_open():
    now = datetime.datetime.now().time()
    start = datetime.time(*MARKET_START)
    end = datetime.time(*MARKET_END)
    return start <= now <= end

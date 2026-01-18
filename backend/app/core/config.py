
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    KITE_API_KEY = os.getenv("KITE_API_KEY")
    KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    @staticmethod
    def validate():
        missing = []
        for k, v in vars(Config).items():
            if k.isupper() and not v:
                missing.append(k)
        if missing:
            raise RuntimeError(f"Missing environment variables: {missing}")

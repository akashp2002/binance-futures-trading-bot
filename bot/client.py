from binance.client import Client
from dotenv import load_dotenv
from binance.exceptions import BinanceAPIException
import os
import time


class BinanceClient:
    def __init__(self):
        load_dotenv()

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )

        # Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Synchronize timestamp with Binance server
        server_time = self.client.get_server_time()
        self.client.timestamp_offset = (
            server_time["serverTime"] - int(time.time() * 1000)
        )

    def get_client(self):
        return self.client

    def test_connection(self):
        try:
            account = self.client.futures_account()

            print("✅ Successfully connected to Binance Futures Testnet!")
            print(f"Assets: {len(account['assets'])}")

        except BinanceAPIException as e:
            print(f"❌ Binance API Error: {e}")

        except Exception as e:
            print(f"❌ Connection Error: {e}")
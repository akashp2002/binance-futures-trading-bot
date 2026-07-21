from binance.exceptions import BinanceAPIException
from bot.client import BinanceClient
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import logger


class OrderManager:

    def __init__(self):
        self.client = BinanceClient().get_client()

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):
        """
        Places a MARKET or LIMIT order on Binance Futures.
        """

        try:
            # -----------------------------
            # Validate Inputs
            # -----------------------------
            validate_symbol(symbol)
            validate_side(side)
            validate_order_type(order_type)
            validate_quantity(quantity)

            if order_type == "LIMIT":
                validate_price(price)

            # Build Request Parameters
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            # Place Order
       
            order = self.client.futures_create_order(**params)

            logger.info(
            f"{order_type} order placed successfully. "
            f"Order ID: {order['orderId']}"
            )

            return order

        except ValueError as e:
            logger.error(f"Validation Error: {e}")
            print(f"Validation Error: {e}")
            return None

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            print(f"Binance API Error: {e}")
            return None

        except Exception as e:
            logger.exception(f"Unexpected Error: {e}")
            print(f"Unexpected Error: {e}")
            return None
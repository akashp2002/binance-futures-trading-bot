VALID_SYMBOLS = ["BTCUSDT", "ETHUSDT"]

VALID_SIDES = ["BUY", "SELL"]

VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):
    if symbol not in VALID_SYMBOLS:
        raise ValueError(f"Invalid symbol: {symbol}")


def validate_side(side):
    if side not in VALID_SIDES:
        raise ValueError(f"Invalid side: {side}")


def validate_order_type(order_type):
    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(f"Invalid order type: {order_type}")


def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price):
    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0")
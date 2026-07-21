import argparse
from pprint import pprint

from bot.orders import OrderManager


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Symbol (Example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order Side"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order Type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order Quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Required for LIMIT orders"
    )

    args = parser.parse_args()

    if args.type == "LIMIT" and args.price is None:
        parser.error("--price is required for LIMIT orders")

    manager = OrderManager()

    response = manager.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    if response:
        print("\n========== ORDER DETAILS ==========\n")

        print(f"Order ID      : {response.get('orderId')}")
        print(f"Symbol        : {response.get('symbol')}")
        print(f"Side          : {response.get('side')}")
        print(f"Order Type    : {response.get('type')}")
        print(f"Status        : {response.get('status')}")
        print(f"Quantity      : {response.get('origQty')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Price         : {response.get('price')}")
        print(f"Average Price : {response.get('avgPrice')}")

if __name__ == "__main__":
    main()
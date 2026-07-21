# Binance Futures Testnet Trading Bot

A Python-based command-line trading bot that interacts with the Binance Futures Testnet. The application supports placing MARKET and LIMIT orders, validates user input, logs trading activity, and uses environment variables to securely manage API credentials.

---

## Features

- Connects to Binance Futures Testnet
- Place MARKET orders
- Place LIMIT orders
- Input validation for:
  - Trading symbol
  - Order side
  - Order type
  - Quantity
  - Price (for LIMIT orders)
- Logging of successful orders and errors
- Command-line interface using `argparse`
- Secure API key management using `.env`

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── .gitignore
├── cli.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python 3.x
- python-binance
- python-dotenv
- argparse
- logging

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/akashp2002/binance-futures-trading-bot 
cd trading_bot
```

### 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=YOUR_BINANCE_API_KEY
API_SECRET=YOUR_BINANCE_API_SECRET
```

Generate your API keys from the **Binance Futures Demo/Testnet**.

---

## Running the Application

### Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.005 --price 10000
```

---

## Logging

Application logs are automatically stored in

```
logs/trading_bot.log
```

Example:

```
2026-07-21 15:45:10 - INFO - MARKET order placed successfully. Order ID: 23122385304

2026-07-21 15:48:30 - ERROR - Validation Error: Quantity must be greater than 0
```

---

## Input Validation

The application validates:

- Valid trading symbol
- Valid order side (BUY / SELL)
- Valid order type (MARKET / LIMIT)
- Positive quantity
- Positive price for LIMIT orders

Invalid requests are rejected before reaching the Binance API.

---

## Example Output

```
========== ORDER DETAILS ==========

Order ID      : 23122385304
Symbol        : BTCUSDT
Side          : BUY
Order Type    : MARKET
Status        : NEW
Quantity      : 0.001
Executed Qty  : 0.000
Price         : 0
Average Price : 0
```

---

## Future Improvements

- Support additional order types (STOP, STOP_MARKET, TAKE_PROFIT)
- Dynamic symbol validation using Binance Exchange Info API
- Unit testing with pytest
- Docker support
- Order history
- Cancel open orders
- Account balance display

---

## Author

**Akash P**

MCA Student | Python Developer | AI & Full-Stack Enthusiast
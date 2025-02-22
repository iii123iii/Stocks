# Stock Portfolio Tracker 📈

A simple Python application to track your stock portfolio performance using real-time data from Yahoo Finance.

## Features 🌟

- Real-time stock price tracking
- Multiple purchase tracking for the same stock
- Profit/Loss calculation
- Percentage gain/loss
- Visual emoji indicators
- Clean, formatted output

## Requirements 📋

- Python 3.x
- yfinance package

## Installation 🔧

```bash
pip install -r requirements.txt
```

## Usage 💡

1. Create a `config.py` file

2. Add your stocks to the `config.py` file in the format:

```python
stocks = [
    ["STOCK_SYMBOL", QUANTITY, PURCHASE_PRICE],
    # Example:
    ["AAPL", 2, 124.56],
]
```

3. Run the application:

```bash
python main.py
```

## Output Example 🖥️

```
••••••••••••••••••••••••••••••••••••••••
📈 Stock name:             AAPL
🔢 Quantity:               2
💵 Purchase price:         $124.56
💰 Current price:          $245.55
💎 Holdings:               $491.10
📈 Profit:                 $241.98
📈 Profit %:               97.13%
••••••••••••••••••••••••••••••••••••••••
```

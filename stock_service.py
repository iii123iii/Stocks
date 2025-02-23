import logging
from yfinance import Tickers
from models import Stock
from typing import Dict

class StockService:

    def __init__(self, stocks: list[Stock]):
        self.stocks = stocks
        self.symbols = list(set(stock.symbol for stock in stocks))

    def get_current_prices(self) -> Dict[str, float]:
        try:
            tickers = Tickers(" ".join(self.symbols)).tickers
            prices = {}
            for name, data in tickers.items():
                try:
                    prices[name] = data.info['currentPrice']
                except KeyError:
                    logging.error(f"Could not fetch price for {name}")
                    prices[name] = 0.0
            return prices
        except Exception as e:
            logging.error(f"Failed to fetch stock data: {str(e)}")
            raise ConnectionError("Failed to connect to the Yahoo Finance API") from e
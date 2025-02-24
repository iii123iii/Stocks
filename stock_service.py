import logging
from yfinance import Tickers
from models import Stock
from typing import Dict

class StockService:

    def __init__(self, stocks: list[Stock]):
        self.stocks = stocks
        self.symbols = list(set(stock.symbol for stock in stocks))

    def get_stock_ticker_data(self) -> Dict[str, list[float, str, str]]:
        try:
            tickers = Tickers(" ".join(self.symbols)).tickers
            prices = {}
            for name, data in tickers.items():
                try:
                    ticker_list = []
                    ticker_list.append(data.info['currentPrice'])
                    ticker_list.append(data.info['financialCurrency'])
                    ticker_list.append(data.info['language'])
                    prices[name] = ticker_list

                except KeyError:
                    logging.error(f"Could not fetch price for {name}")
                    prices[name] = 0.0
            return prices
        except Exception as e:
            logging.error(f"Failed to fetch stock data: {str(e)}")
            raise ConnectionError("Failed to connect to the Yahoo Finance API") from e
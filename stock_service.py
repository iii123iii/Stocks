from yfinance import Tickers
from models import Stock

class StockService:
    def __init__(self, stocks: list[Stock]):
        self.stocks = stocks
        self.symbols = list(set(stock.symbol for stock in stocks))

    def get_current_prices(self):
        tickers = Tickers(" ".join(self.symbols)).tickers
        return {name: data.info['currentPrice'] for name, data in tickers.items()}
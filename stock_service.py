from yfinance import Tickers

class StockService:
    def __init__(self, stocks):
        self.stocks = stocks
        self.symbols = list(set(stock[0] for stock in stocks))

    def get_current_prices(self):
        tickers = Tickers(" ".join(self.symbols)).tickers
        return {name: data.info['currentPrice'] for name, data in tickers.items()}

    def calculate_metrics(self, stock, current_price):
        quantity = stock[1]
        purchase_price = stock[2]
        
        holdings = current_price * quantity
        profit = holdings - (purchase_price * quantity)
        profit_percentage = ((current_price - purchase_price) / purchase_price) * 100
        
        return holdings, profit, profit_percentage

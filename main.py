from yfinance import Tickers

stocks = [["AAPL", 2, 84.26], ["AAPL", 3, 245.55], ["GOOGL", 4, 45]]
owned_stocks = []


owned_stocks = list(set(stock[0] for stock in stocks))


stocks_string = " ".join(owned_stocks)

stocks_data = Tickers(stocks_string).tickers
stocks_data_map = {}

for name, value in stocks_data.items():
    stocks_data_map[name] = value.info['currentPrice']

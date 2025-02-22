from yfinance import Tickers

stocks = [["AAPL", 2, 84.26], ["AAPL", 3, 245.55], ["GOOGL", 4, 45]]
owned_stocks = []

owned_stocks = list(set(stock[0] for stock in stocks))


stocks_string = " ".join(owned_stocks)

stocks_data = Tickers(stocks_string).tickers
stocks_data_map = {}

for name, value in stocks_data.items():
    stocks_data_map[name] = value.info['currentPrice']

grouped_stocks = {}

for value in stocks:
    if value[0] not in grouped_stocks:
        grouped_stocks[value[0]] = [value]
    else:
        grouped_stocks[value[0]].append(value)

for key, value in grouped_stocks.items():
    for stock in value:
        border = "•" * 40
        print("\n" + border)
        print(f"{'📈 Stock name:':<25} {stock[0]}")
        print(f"{'🔢 Quantity:':<25} {stock[1]}")
        print(f"{'💵 Purchase price:':<25} ${stock[2]:.2f}")
        print(f"{'💰 Current price:':<25} ${stocks_data_map[stock[0]]:.2f}")
        print(f"{'💎 Holdings:':<25} ${stocks_data_map[stock[0]] * stock[1]:.2f}")
        
        profit = stocks_data_map[stock[0]] * stock[1] - stock[2] * stock[1]
        profit_percentage = ((stocks_data_map[stock[0]] - stock[2]) / stock[2]) * 100
        
        profit_emoji = "📈" if profit > 0 else "📉"
        print(f"{profit_emoji + ' Profit:':<25} ${profit:.2f}")
        print(f"{profit_emoji + ' Profit %:':<25} {profit_percentage:.2f}%")
        print(border + "\n")
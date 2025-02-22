from yfinance import Tickers
from config import stocks

def get_current_prices(symbols):
    tickers = Tickers(" ".join(symbols)).tickers
    return {name: data.info['currentPrice'] for name, data in tickers.items()}

def calculate_metrics(stock, current_price):
    quantity = stock[1]
    purchase_price = stock[2]
    
    holdings = current_price * quantity
    profit = holdings - (purchase_price * quantity)
    profit_percentage = ((current_price - purchase_price) / purchase_price) * 100
    
    return holdings, profit, profit_percentage

def display_stock(stock, current_price):
    holdings, profit, profit_percentage = calculate_metrics(stock, current_price)
    profit_emoji = "📈" if profit > 0 else "📉"
    border = "•" * 40
    
    print(f"\n{border}")
    print(f"{'📈 Stock name:':<25} {stock[0]}")
    print(f"{'🔢 Quantity:':<25} {stock[1]}")
    print(f"{'💵 Purchase price:':<25} ${stock[2]:.2f}")
    print(f"{'💰 Current price:':<25} ${current_price:.2f}")
    print(f"{'💎 Holdings:':<25} ${holdings:.2f}")
    print(f"{profit_emoji + ' Profit:':<25} ${profit:.2f}")
    print(f"{profit_emoji + ' Profit %:':<25} {profit_percentage:.2f}%")
    print(f"{border}\n")

def main():
    try:
        symbols = list(set(stock[0] for stock in stocks))
        current_prices = get_current_prices(symbols)
        
        for stock in stocks:
            display_stock(stock, current_prices[stock[0]])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
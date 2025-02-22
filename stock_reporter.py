class StockReporter:
    def __init__(self, service):
        self.service = service
        
    def display_stock(self, stock, current_price):
        holdings, profit, profit_percentage = self.service.calculate_metrics(stock, current_price)
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
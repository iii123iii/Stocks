from models import StockData
from typing import NoReturn

class StockReporter:
    def __init__(self, borderChar:str = "•", borderLen:int = 40):
        borderChar = borderChar
        borderLen = borderLen
        self.border = borderChar * borderLen

    def display_stock(self, stock: StockData) -> NoReturn:
        profit_emoji = "📈" if stock.profit > 0 else "📉"
        
        print(f"\n{self.border}")
        print(f"{'📈 Stock symbol:':<25} {stock.symbol}")
        print(f"{'🔢 Shares:':<25} {stock.shares}")
        print(f"{'💵 Purchase price:':<25} ${stock.purchase_price:.2f}")
        print(f"{'💰 Current price:':<25} ${stock.current_price:.2f}")
        print(f"{'💎 Holdings:':<25} ${stock.holdings:.2f}")
        print(f"{profit_emoji + ' Profit:':<25} ${stock.profit:.2f}")
        print(f"{profit_emoji + ' Profit %:':<25} {stock.profit_percentage:.2f}%")
        print(f"{self.border}\n")
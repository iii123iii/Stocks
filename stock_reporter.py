from rich import print as printColor
from typing import NoReturn
from models import StockData

class StockReporter:
    def __init__(self, borderChar:str = "•", borderLen:int = 40):
        borderChar = borderChar
        borderLen = borderLen
        self.border = borderChar * borderLen

    def display_stock(self, stock: StockData) -> NoReturn:
        isProfit = stock.profit > 0
        profit_emoji = "📈" if isProfit else "📉"
        
        print(f"\n{self.border}")
        print(f"{'📈 Stock symbol:':<25} {stock.symbol}")
        print(f"{'🔢 Shares:':<25} {stock.shares}")
        print(f"{'💵 Purchase price:':<25} ${stock.purchase_price:.2f}")
        printColor(f"{'💰 Current price:':<25} [{"green" if isProfit else "red"}]${stock.current_price:.2f}[/]")
        printColor(f"{'💎 Holdings:':<25} [{"green" if isProfit else "red"}]${stock.holdings:.2f}[/]")
        printColor(f"{profit_emoji + ' Profit:':<25} [{"green" if isProfit else "red"}]${stock.profit:.2f}[/]")
        printColor(f"{profit_emoji + ' Profit %:':<25} [{"green" if isProfit else "red"}]{stock.profit_percentage:.2f}%[/]")
        print(f"{self.border}\n")
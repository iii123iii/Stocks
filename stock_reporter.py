from rich import print as printColor
from typing import NoReturn
from models import StockData

class StockReporter:
    def __init__(self, borderChar:str = "•", borderLen:int = 40, stockStaticColor: str = "yellow"):
        borderChar = borderChar
        borderLen = borderLen
        self.border = borderChar * borderLen
        self.stockStaticColor = stockStaticColor

    def display_stock(self, stock: StockData) -> NoReturn:
        profit_emoji = "📈" if stock.isProfit else "📉"
        stockDynamicColor = "green" if stock.isProfit else "red"
        
        print(f"\n{self.border}")
        printColor(f"{'📈 Stock symbol:':<25} [{self.stockStaticColor}]{stock.symbol}[/]")
        printColor(f"{'🔢 Shares:':<25} [{self.stockStaticColor}]{stock.shares}[/]")
        printColor(f"{'💵 Purchase price:':<25} [{self.stockStaticColor}]${stock.purchase_price:.2f}[/]")
        printColor(f"{'💰 Current price:':<25} [{stockDynamicColor}]${stock.current_price:.2f}[/]")
        printColor(f"{'💎 Holdings:':<25} [{stockDynamicColor}]${stock.holdings:.2f}[/]")
        printColor(f"{profit_emoji + ' Profit:':<25} [{stockDynamicColor}]${stock.profit:.2f}[/]")
        printColor(f"{profit_emoji + ' Profit/Stock:':<25} [{stockDynamicColor}]${stock.profitPerStock:.2f}[/]")
        printColor(f"{profit_emoji + ' Profit %:':<25} [{stockDynamicColor}]{stock.profit_percentage:.2f}%[/]")
        print(f"{self.border}\n")
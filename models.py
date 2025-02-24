from dataclasses import dataclass

@dataclass
class Stock:
    symbol: str
    shares: int
    purchase_price: float

    def __post_init__(self):
        if not self.symbol or not isinstance(self.symbol, str):
            raise ValueError("Symbol must be a non-empty string")
        if self.shares <= 0:
            raise ValueError("Shares must be positive")
        if self.purchase_price <= 0:
            raise ValueError("Purchase price must be positive")

@dataclass
class StockData:
    symbol: str
    shares: int
    purchase_price: float
    current_price: float

    @property
    def holdings(self) -> float:
        return self.current_price * self.shares
    
    @property
    def profit(self) -> float:
        return self.holdings - (self.purchase_price * self.shares)
    
    @property
    def profitPerStock(self) -> float:
        return self.profit / self.shares

    
    @property
    def profit_percentage(self) -> float:
        return ((self.current_price - self.purchase_price) / self.purchase_price) * 100
    
    @property
    def isProfit(self) -> bool:
        return self.profit > 0
from dataclasses import dataclass

@dataclass
class Stock:
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
    def profit_percentage(self) -> float:
        return ((self.current_price - self.purchase_price) / self.purchase_price) * 100
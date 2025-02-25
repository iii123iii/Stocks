from babel.numbers import format_currency
from dataclasses import dataclass

@dataclass(frozen=True)
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

@dataclass(frozen=True)
class StockData:
    symbol: str
    shares: int
    purchase_price: float
    current_price: float
    currency: str
    language: str

    @property
    def __holdings(self) -> float:
        return self.current_price * self.shares

    @property
    def holdings(self) -> str:
        return self.__formatNumber(self.__holdings)
    
    @property
    def __profit(self) -> float:
        return self.__holdings - (self.purchase_price * self.shares)
    
    @property
    def profit(self) -> str:
        return self.__formatNumber(self.__profit)

    @property
    def profit_per_stock(self) -> str:
        return self.__formatNumber(self.__profit / self.shares)

    
    @property
    def profit_percentage(self) -> float:
        return ((self.current_price - self.purchase_price) / self.purchase_price) * 100
    
    @property
    def is_profit(self) -> bool:
        return self.__profit > 0
    
    def __formatNumber(self, number: float) -> str:
        return format_currency(round(number, 2), self.currency, locale=self.language.replace('-', '_'))
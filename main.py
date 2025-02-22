from config import stocks
from stock_service import StockService
from stock_reporter import StockReporter
from models import StockData
from typing import NoReturn

def main() -> NoReturn:
    try:
        service = StockService(stocks)
        reporter = StockReporter()
        
        print("Fetching current stock prices...")
        current_prices = service.get_current_prices()
        
        print("\nStock Portfolio Report:")
        print("-" * 50)
        for value in stocks:
            if current_prices[value.symbol] > 0:
                stock = StockData(value.symbol, value.shares, value.purchase_price, current_prices[value.symbol])

                reporter.display_stock(stock)
            
    except Exception as e:
        print(f"Fatal error in main program: {str(e)}")
        raise

if __name__ == "__main__":
    main()
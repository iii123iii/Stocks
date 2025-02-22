from config import stocks
from stock_service import StockService
from stock_reporter import StockReporter
from stock import Stock
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
            if current_prices[value[0]] > 0:
                stock = Stock(value[0], value[1], value[2], current_prices[value[0]])

                reporter.display_stock(stock)
            
    except Exception as e:
        print(f"Fatal error in main program: {str(e)}")
        raise

if __name__ == "__main__":
    main()
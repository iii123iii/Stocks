from config import stocks
from stock_service import StockService
from stock_reporter import StockReporter
from typing import NoReturn

def main() -> NoReturn:
    try:
        service = StockService(stocks)
        reporter = StockReporter(service)
        
        print("Fetching current stock prices...")
        current_prices = service.get_current_prices()
        
        print("\nStock Portfolio Report:")
        print("-" * 50)
        for stock in stocks:
            if current_prices[stock[0]] > 0:
                reporter.display_stock(stock, current_prices[stock[0]])
            
    except Exception as e:
        print(f"Fatal error in main program: {str(e)}")
        raise

if __name__ == "__main__":
    main()
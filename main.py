import logging
from os import system, name
from config import stocks
from stock_service import StockService
from stock_reporter import StockReporter
from models import StockData, Stock
from typing import NoReturn

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def validate_config(stocks: list[Stock]) -> None:
    if not stocks:
        raise ValueError("No stocks configured in config.py")

def main() -> NoReturn:
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    setup_logging()
    
    try:
        validate_config(stocks)
        service = StockService(stocks)
        reporter = StockReporter()
        
        logging.info("Fetching current stock prices...")
        current_data = service.get_stock_ticker_data()
        
        logging.info("Generating stock portfolio report...")
        for stock in stocks:
            stock_ticker = current_data[stock.symbol]
            current_price = stock_ticker[0]
            currency = stock_ticker[1]
            language = stock_ticker[2]

            if current_price > 0:
                stock_data = StockData(
                    stock.symbol, 
                    stock.shares, 
                    stock.purchase_price, 
                    current_price,
                    currency,
                    language,
                )
                reporter.display_stock(stock_data)
            else:
                logging.warning(f"Skipping {stock.symbol} due to invalid price data")
            
    except ConnectionError as e:
        logging.error(f"Failed to connect to stock service: {e}")
        raise
    except Exception as e:
        logging.error(f"Fatal error in main program: {e}")
        raise

if __name__ == "__main__":
    main()
import yfinance as yf

class Stock:

    # Constructor
    def __init__(self, ticker):
        self.ticker = ticker
        print(self.ticker, "object created")

    # Method to download data
    def get_data(self):
        stock = yf.Ticker(self.ticker)
        data = stock.history(period="5d")
        print(data)


# Create objects
apple = Stock("AAPL")
tesla = Stock("TSLA")

# Call methods
apple.get_data()
tesla.get_data()
import yfinance as yf
# yfinance library is used to download stock market data
# from Yahoo Finance

import matplotlib.pyplot as plt
# matplotlib is used to create charts/graphs

import pandas as pd
# pandas is used for working with DataFrames (tables)


# ==========================================================
# 🧱 Parent Class: Stock
# ==========================================================
# This class contains the CORE functionality:
# - storing ticker symbol
# - downloading stock data
#
# Child classes can REUSE these methods using inheritance
# ==========================================================
class Stock:

    # ------------------------------------------------------
    # Constructor
    # ------------------------------------------------------
    # Parameter:
    # ticker → stock symbol entered by user
    #
    # Example:
    # ticker = "aapl"
    #
    # Python internally does:
    # self.ticker = "AAPL"
    # ------------------------------------------------------
    def __init__(self, ticker):

        self.ticker = ticker.upper()
        # converts lowercase to uppercase

        print(f"{self.ticker} object created")

        # Empty placeholders for storing downloaded data
        self.data_7d = None
        self.data_1mo = None
        self.data_1y = None


    # ------------------------------------------------------
    # Method to download stock data
    # ------------------------------------------------------
    # Parameter:
    # period → tells Yahoo Finance how much data to fetch
    #
    # Example calls:
    # self.get_data("7d")
    # self.get_data("1mo")
    # self.get_data("1y")
    #
    # Python internally does:
    # period = "7d"
    # ------------------------------------------------------
    def get_data(self, period):

        stock = yf.Ticker(self.ticker)
        # connects to Yahoo Finance

        data = stock.history(period=period)
        # downloads historical stock data

        return data
        # sends dataframe back to caller


# ==========================================================
# 👶 Child Class: StockAnalysis
# ==========================================================
# Inheritance:
# StockAnalysis inherits from Stock
#
# Meaning:
# This class automatically gets:
# - __init__()
# - get_data()
#
# So we DO NOT rewrite them again
# ==========================================================
class StockAnalysis(Stock):


    # ------------------------------------------------------
    # Load all stock datasets
    # ------------------------------------------------------
    # This method calls inherited method:
    # get_data()
    #
    # Flow:
    #
    # self.get_data("7d")
    #         ↓
    # period = "7d"
    #         ↓
    # returns dataframe
    #         ↓
    # stored in self.data_7d
    # ------------------------------------------------------
    def load_data(self):

        self.data_7d = self.get_data("7d")
        # stores 7-day stock dataframe

        self.data_1mo = self.get_data("1mo")
        # stores 1-month dataframe

        self.data_1y = self.get_data("1y")
        # stores 1-year dataframe


    # ------------------------------------------------------
    # Calculate stock performance
    # ------------------------------------------------------
    # Parameter:
    # data → dataframe passed into method
    #
    # Example call:
    # self.calculate_performance(self.data_7d)
    #
    # Python internally does:
    # data = self.data_7d
    #
    # Formula:
    #
    # (last close - first close)
    # -------------------------- × 100
    # first close
    # ------------------------------------------------------
    def calculate_performance(self, data):

        return round(
            (data["Close"].iloc[-1] - data["Close"].iloc[0])
            / data["Close"].iloc[0] * 100,
            2
        )

        # round(..., 2)
        # rounds answer to 2 decimal places


    # ------------------------------------------------------
    # Plot stock chart
    # ------------------------------------------------------
    # Parameters:
    # data  → dataframe
    # title → chart title
    #
    # Example call:
    #
    # self.plot(
    #     self.data_7d,
    #     "AAPL - 7 Day Performance"
    # )
    #
    # Python internally does:
    #
    # data = self.data_7d
    # title = "AAPL - 7 Day Performance"
    # ------------------------------------------------------
    def plot(self, data, title):

        plt.figure(figsize=(8,5))
        # creates graph area

        plt.plot(data.index, data["Close"])
        # X-axis → dates
        # Y-axis → closing prices

        plt.title(title)

        plt.xlabel("Date")
        plt.ylabel("Closing Price")

        plt.grid(True)
        # adds grid lines

        plt.show()
        # displays chart


    # ------------------------------------------------------
    # Display dataframe
    # ------------------------------------------------------
    # Parameters:
    # data → dataframe to display
    # name → label for dataset
    #
    # Example call:
    #
    # self.show_dataframe(self.data_7d, "7-DAY")
    #
    # Python internally does:
    #
    # data = self.data_7d
    # name = "7-DAY"
    # ------------------------------------------------------
    def show_dataframe(self, data, name):

        print("\n" + "="*50)

        print(f"{name} DATA ({self.ticker})")

        print("="*50)

        print(data.head())
        # displays first 5 rows

        print("\nLast 5 rows:")

        print(data.tail())
        # displays last 5 rows

        print("\nShape:", data.shape)
        # displays:
        # (rows, columns)


    # ------------------------------------------------------
    # Main Analysis Method
    # ------------------------------------------------------
    # This method controls the FULL program flow
    #
    # Flow:
    #
    # show_analysis()
    #         ↓
    # load_data()
    #         ↓
    # calculate_performance()
    #         ↓
    # show_dataframe()
    #         ↓
    # plot()
    # ------------------------------------------------------
    def show_analysis(self):

        self.load_data()
        # downloads all datasets


        # ==================================================
        # 📊 7-DAY ANALYSIS
        # ==================================================
        perf_7d = self.calculate_performance(self.data_7d)

        print(f"\n7-Day Performance: {perf_7d}%")

        self.show_dataframe(self.data_7d, "7-DAY")

        self.plot(
            self.data_7d,
            f"{self.ticker} - 7 Day Performance"
        )


        # ==================================================
        # 📊 1-MONTH ANALYSIS
        # ==================================================
        perf_1mo = self.calculate_performance(self.data_1mo)

        print(f"\n1-Month Performance: {perf_1mo}%")

        self.show_dataframe(self.data_1mo, "1-MONTH")

        self.plot(
            self.data_1mo,
            f"{self.ticker} - 1 Month Performance"
        )


        # ==================================================
        # 📊 1-YEAR ANALYSIS
        # ==================================================
        perf_1y = self.calculate_performance(self.data_1y)

        print(f"\n1-Year Performance: {perf_1y}%")

        self.show_dataframe(self.data_1y, "1-YEAR")

        self.plot(
            self.data_1y,
            f"{self.ticker} - 1 Year Performance"
        )

# ==========================================================
# 🚀 OBJECT CREATION
# ==========================================================
# Inheritance happening here:
#
# StockAnalysis does NOT have __init__()
#
# So Python automatically uses:
#
# Stock.__init__()

if __name__ == "__main__":

    ticker = input("Enter Stock Ticker: ")

    stock = StockAnalysis(ticker)

    stock.show_analysis()
# ==========================================================
# 🚀 RUN PROGRAM
# ==========================================================

# Flow:
#
# show_analysis()
#         ↓
# load_data()
#         ↓
# inherited get_data()
#         ↓
# calculate_performance()
#         ↓
# show_dataframe()
#         ↓
# plot()
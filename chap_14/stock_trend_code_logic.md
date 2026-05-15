# 🧠 Visual Flow of the Stock Analysis Project

```text
USER enters ticker
        ↓
ticker = input("Enter Stock Ticker: ")

        ↓

stock = StockAnalysis(ticker)

        ↓

__init__(ticker)
(Constructor runs automatically)

        ↓

self.ticker = ticker.upper()

Example:
ticker = "aapl"
self.ticker = "AAPL"

        ↓

show_analysis()
(Main method starts execution)

        ↓

self.load_data()

        ↓

load_data() calls:

    self.get_data("7d")
            ↓
        period = "7d"
            ↓
        Yahoo Finance API
            ↓
        returns 7-day DataFrame
            ↓
        stored in:
        self.data_7d


    self.get_data("1mo")
            ↓
        period = "1mo"
            ↓
        returns 1-month DataFrame
            ↓
        stored in:
        self.data_1mo


    self.get_data("1y")
            ↓
        period = "1y"
            ↓
        returns 1-year DataFrame
            ↓
        stored in:
        self.data_1y

        ↓

calculate_performance(data)

Example call:
self.calculate_performance(self.data_7d)

        ↓

Python internally does:

data = self.data_7d

        ↓

Uses formula:

(last close - first close)
-------------------------------- × 100
first close

        ↓

Returns percentage performance

Example:
7-Day Performance: 4.25%

        ↓

show_dataframe(data, name)

Example call:
self.show_dataframe(self.data_7d, "7-DAY")

        ↓

Python internally does:

data = self.data_7d
name = "7-DAY"

        ↓

Displays:
- first 5 rows
- last 5 rows
- dataframe shape

        ↓

plot(data, title)

Example call:

self.plot(
    self.data_7d,
    "AAPL - 7 Day Performance"
)

        ↓

Python internally does:

data = self.data_7d

title = "AAPL - 7 Day Performance"

        ↓

matplotlib creates chart

        ↓

Chart displayed to user




| Method                              | Parameters      | Arguments Passed                             |
| ----------------------------------- | --------------- | -------------------------------------------- |
| `__init__(self, ticker)`            | `ticker`        | `"AAPL"`                                     |
| `get_data(self, period)`            | `period`        | `"7d"`                                       |
| `calculate_performance(self, data)` | `data`          | `self.data_7d`                               |
| `show_dataframe(self, data, name)`  | `data`, `name`  | `self.data_7d`, `"7-DAY"`                    |
| `plot(self, data, title)`           | `data`, `title` | `self.data_7d`, `"AAPL - 7 Day Performance"` |

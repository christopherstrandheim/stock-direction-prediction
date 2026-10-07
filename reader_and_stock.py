from pathlib import Path
import pandas as pd

data_file = Path(__file__).parent / "data"/ "World-Stock-Prices-Dataset.csv"

stocks = pd.read_csv(data_file)

stocks["Date"] = pd.to_datetime(stocks["Date"], utc=True)

apple = stocks[stocks["Ticker"] == "AAPL"].copy()

apple = apple.sort_values("Date").reset_index(drop=True)

print(stocks.columns)
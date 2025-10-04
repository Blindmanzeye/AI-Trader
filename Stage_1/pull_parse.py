import yfinance as yf
import pandas as pd
import numpy as np


def pullStockData(tickers: list[str], period: str, interval: str) -> pd.DataFrame:
    return yf.download(tickers=tickers, period=period, interval=interval).tail(5)


if __name__ == "__main__":
    tickers = ["NVDA"]
    print(pullStockData(tickers, '1d', '1m'))
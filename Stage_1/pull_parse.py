import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp


def pullStockData(tickers: list[str], period: str, interval: str) -> pd.DataFrame:
    return yf.download(tickers=tickers, period=period, interval=interval)


if __name__ == "__main__":
    # Sentiments as of 05/10/2025 @ 8:30 AM DD/MM/YYYY
    # APPL liquidation Risk due to current liabilities > Current Assets, But financials and total asset/liabilities good. Appl long term
    # Meta Huge current asset/liability ratio with big platform but not too good long term due to low stock price, great time to buy
    # AMD sleeper, great current asset/liability ratio, undervalued stock price, great profit over last 4 years and quarters, also dominating cpu scene rn
    # NVDIA good current asset/liability, great profit over last 4 years and quarters, dominating gpu scene for gaming and AI dev, Risk of a great sell due to extensive
    # Stock options given to previous nvidia employees
    # GOOG good current asset/liability ratio, market dominator, decent profit increases over the last 4 years and quarters, correct value stock price
    tickers = ["NVDA", "AAPL", "AMD", "META", "GOOG"]
    stock_data = pullStockData(tickers, '1d', '1m')
    # stock_data.to_csv("stock_prices.csv")
    aaplCloseData = stock_data.tail(20)[("Close", "AAPL")]
    dateTime = stock_data.index.to_series().rename("dates")

    plotData = pd.DataFrame({"date": dateTime, "price": aaplCloseData})
    print(plotData)
    # Deal with ts later
    plotData.plot(x=plotData["date"], y=plotData["price"], kind="line")
    


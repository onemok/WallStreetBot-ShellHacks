#packages we need
import pandas as pd
import matplotlib as ml
import sklearn as sk
import yfinance as yf

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

def alltimegraph(stockdf, name):
    stockdf.plot.line(y = "Close", use_index = True, title = f"Historical Price of {name}")

def rolldates(stockdf):
    data = stockdf[["Close"]]
    data = data.rename(columns = {'Close': 'Actual Close'})
    data["Target"] = stockdf.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0], raw = False)["Close"]
    return data

def shiftrows(stockdf):
    stock_copy = stockdf.copy()
    stock_copy = stock_copy.shift(1)
    return stock_copy()








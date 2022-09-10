#packages we need
import pandas as pd
import matplotlib as ml
import sklearn as sk
import yfinance as yf

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

#print stock chart
def alltimegraph(stockdf, name):
    stockdf.plot.line(y = "Close", use_index = True, title = f"Historical Price of {name}")

#create our target to predict with our model. Target is a higher/lower close
def rolldates(stockdf):
    data = stockdf[["Close"]]
    data = data.rename(columns = {'Close': 'Actual Close'})
    data["Target"] = stockdf.rolling(2).apply(lambda x: x.iloc[1] > x.iloc[0], raw = False)["Close"]
    return data

#shift all rows forward by one
def shiftrows(stockdf):
    stock_copy = stockdf.copy()
    stock_copy = stock_copy.shift(1)
    return stock_copy()

#basic predictors the model will use
predictors = ["Open", "High", "Low", "Close", "Volume"]

def joinpreds(stockdf, data):
    data = data.join(stockdf[predictors]).iloc[1:]
    return data

#create more columns. more possible predictors
def catcols(data):
    data["dayofweek"] = data.index.day
    data["month"] = data.index.month
    data["year"] = data.index.year
    return data

#initialize Random Forest
def makemodel():
    model = RandomForestClassifier(n_estimators = 100, criterion = "log_loss")
    return model










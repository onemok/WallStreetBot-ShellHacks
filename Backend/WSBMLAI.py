#packages we need
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
import yfinance as yf
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

#print stock chart
def alltimegraph(stockdf, name):
    plt.plot(stockdf.index, stockdf["Close"])
    plt.title(label = f"Last 5 year price history of {name}")
    plt.xlabel("Date")
    plt.ylabel("Price($)")
    filename = f"5y{name}.png"
    plt.savefig("../Frontend/images/"+filename)


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
    return stock_copy

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
    model = RandomForestClassifier(n_estimators = 100)
    return model

def backtest(data, model, predictors, start = 100, step = 10):
    predictions = []
    for i in range(start, data.shape[0], step):

        train = data.iloc[0:i].copy()
        test = data.iloc[i: (i + step)].copy()

        model.fit(train[predictors], train["Target"])

        #preds = model.predict_proba(test[predictors])[:,1]
        preds = model.predict(test[predictors])
        preds = pd.Series(preds, index = test.index)

        #preds[preds > .6] = 1
        #preds[preds <= .6] = 0

        combined = pd.concat({"Target":test["Target"], "Predictions" : preds}, axis = 1)
        predictions.append(combined)
    
    predictions = pd.concat(predictions)
    return predictions

def trends(data):
    sma20 = data.rolling(20).mean()
    sma50 = data.rolling(50).mean()
    sma200 = data.rolling(200).mean()

    weekly_trend = data.shift(1).rolling(7).mean()["Target"]

    #rolling mean ratios and breakouts to find trends to better predict next day
    data["sma20"] = sma20["Close"]
    data["sma50"] = sma50["Close"]
    data["sma200"] = sma200["Close"]
    data["sma20/close"] = sma20["Close"]/data["Close"]
    data["sma50/close"] = sma50["Close"]/data["Close"]
    data["sma200/close"] = sma200["Close"]/data["Close"]
    #data["breakoutclose20"] = ((data["Close"] > sma20["Close"]) and (data["Open"] < sma20["Close"]))
    #data["breakoutclose50"] = ((data["Close"] > sma50["Close"]) and (data["Open"] < sma50["Close"]))
    #data["breakoutclose200"] = ((data["Close"] > sma200["Close"]) and (data["Open"] < sma200["Close"]))

    data["200/50"] = data["sma200"]/data["sma50"]
    data["200/20"] = data["sma200"]/data["sma20"]
    data["50/20"] = data["sma50"]/data["sma20"]
    data["weekly_trend"] = weekly_trend

    data["open_close_ratio"] = data["Open"]/data["Close"]
    data["high_close_ratio"] = data["High"]/data["Close"]
    data["low_close_ratio"] = data["Low"]/data["Close"]

    data["dayrange/volume"] = (data["Open"] - data["Close"]) / data["Volume"]


    #data["direction"] = data["Open"] > data["Close"]
    #data["day_range"] = abs(data["Open"] - data["Close"])
    #data["intraday_range"] = abs(data["High"] - data["Low"])
    
    return data

full_predictors = predictors + ["sma20/close","sma50/close","sma200/close","200/20","200/50","50/20","weekly_trend", "month", "open_close_ratio", "high_close_ratio", "low_close_ratio", "dayrange/volume"]

def call_stock(stock_name):
  aapl = yf.Ticker(stock_name)
  aapl = aapl.history(period = "5y")
  alltimegraph(aapl, stock_name)
  aapldata = rolldates(aapl)
  aaplcopy = shiftrows(aapl)
  aapldata = joinpreds(aaplcopy, aapldata)
  model = makemodel()
  aapldata = trends(aapldata)
  aapldata = catcols(aapldata)
  aaplpredictions = backtest(aapldata.iloc[365:], model, full_predictors)

  print(aaplpredictions['Predictions'][-1], round(precision_score(aaplpredictions["Target"], aaplpredictions["Predictions"]),4))

call_stock("AMZN")
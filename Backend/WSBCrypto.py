import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import sklearn as sk

from sklearn.ensemble import RandomForestRegressor

import statsmodels

def read_chart(name):
    crypto = yf.Ticker("")
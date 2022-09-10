#packages we need
import pandas as pd
import matplotlib.pylab as plt
import matplotlib
matplotlib.style.use('seaborn')
from matplotlib.pylab import rcParams
import sklearn as sk
import yfinance as yf
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

import statsmodels


from plotly.graph_objs import *
from plotly.offline import init_notebook_mode, iplot, iplot_mpl
init_notebook_mode()


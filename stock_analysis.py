from typing import Type
from pandas_datareader import data as pd
import pandas
import datetime 
import sys
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as pl
import plotly.graph_objects as go


# start date, ticker 
# taking start date from today to how many years ago

# reading the data from two years ago to today for a particular stock

# pickling the data frame so do not have reload every time
def get_mid(df):
    high = df['HighPrice']
    low = df['LowPrice']
    # if the bid or ask doesn't exist, return 0.0
    if np.isnan(high) or np.isnan(low):
        return 0.0
    else:
        return (high + low) / 2.0
    
def stock_plot(df, select=None):
    if select is not None:
        # shows the data of interest selected
        df[select].plot()
        pl.show()
    else:
        # graphs the candle stick
        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['OpenPrice'],
                high=df['HighPrice'],
                low=df['LowPrice'],
                close=df['ClosePrice'])])
        fig.show()
    
        
def main(ticker: str, start: datetime, end=datetime.datetime.now()):
    # reading data
    raw_data = pd.DataReader(ticker, 'yahoo', start, end)
    raw_data.to_pickle('stock_frame.pickle')
    stock_frame = pandas.read_pickle('stock_frame.pickle')
    
    # deleting unnecessary data
    del stock_frame['Volume']
    del stock_frame['Adj Close']
    
    
    # resetting the index to be able to access date
    stock_frame = stock_frame.reset_index()
    
    # renaming the data
    columns = {'High': 'HighPrice',
               'Low': 'LowPrice',
               'Open': 'OpenPrice',
               'Close': 'ClosePrice',}
    stock_frame.rename(columns=columns, inplace=True)
    stock_frame['MidPrice'] = stock_frame.apply(get_mid, axis=1)
    print(stock_frame)
    
    # selection of a particular interest of data, or graphing all in a candle stick
    selection = input("Select your column of interest or press enter if there is none: ")
    if selection == "":
        stock_plot(stock_frame)
    else:
        stock_plot(stock_frame, selection)
    
    
    
    
    


if __name__ == "__main__":
    try:
        startDate = input("Please enter a starting date: ")
        startDateArray = startDate.split("/")
        startDate = datetime.datetime(int(startDateArray[2]),int(startDateArray[1]),int(startDateArray[0]))
        
        ticker = input("Please enter a ticker: ")
        stockTicker = ticker.upper()
    except Exception:
        print("Please enter a valid start date and ticker")
    else:
        result = main(stockTicker, startDate)

        
        





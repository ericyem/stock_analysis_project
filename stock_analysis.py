from typing import Type
from pandas_datareader import data as pd
import pandas
import datetime 
import sys
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as pl

# start date, ticker 
# taking start date from today to how many years ago

# reading the data from two years ago to today for a particular stock


# pickling the data frame so do not have reload every time

def stock_plot(df, select=None):
    if select is not None:
        df[select].plot()
        pl.show()
    else:
        df.plot()
        pl.show()
    
        
def main(ticker: str, start: datetime, end=datetime.datetime.now()):
    # reading data
    raw_data = pd.DataReader(ticker, 'yahoo', start, end)
    raw_data.to_pickle('stock_frame.pickle')
    stock_frame = pandas.read_pickle('stock_frame.pickle')
    
    # deleting unnecessary data
    del stock_frame['Volume']
    del stock_frame['Adj Close']
    
    
    # renaming the columns
    columns = {'High': 'High Price',
           'Low': 'Low Price',
           'Open': 'Open Price',
           'Close': 'Close Price',}
    stock_frame.rename(columns=columns, inplace=True)
    
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

        
        




